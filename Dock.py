from flask import Flask, jsonify, abort, make_response, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from passlib.hash import pbkdf2_sha256
import filetable_def
import usertable_def
import yaml
import os

# Load the configuration
with open("config/app-config.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

    # Load connection details
    if cfg['app']['host'] == 'localhost':
        APP_HOST = '127.0.0.1'
    else:
        APP_HOST = cfg['app']['host']
    APP_PORT = cfg['app']['port']

    # Load file system details
    USER_ROOT_DIR = cfg['files']['root_folder']
    # Create the user root directory if it does not exist
    if not os.path.exists(USER_ROOT_DIR):
        os.makedirs(USER_ROOT_DIR)

# Create the application

# Load the file table
filetable_engine = create_engine('sqlite:///filetable.db', echo=True)
filetable_session = sessionmaker(bind=filetable_engine)
file_table = filetable_session()

# Load the user table
usertable_engine = create_engine('sqlite:///usertable.db', echo=True)
usertable_session = sessionmaker(bind=usertable_engine)
user_table = usertable_session()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Dock here!'


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


# DOWNLOAD A FILE
@app.route('/AirHaven/api/1.0/files/<int:file_id>/download', methods=['POST'])
@app.route('/AirHaven/api/1.0/files/<int:file_id>', methods=['POST'])
def get_file(file_id):
    query = file_table.query(filetable_def.FileSystemObject).filter(filetable_def.FileSystemObject.id == file_id). \
        filter(filetable_def.FileSystemObject.type == "file")
    if query.count() < 1:
        abort(404)

    file_obj = query.first()
    # TODO: replace path with file data itself for /download
    data = {file_obj.type: {'id': file_obj.id, 'name': file_obj.name, 'path': file_obj.path}}

    return jsonify(data)


@app.route('/AirHaven/api/1.0/files/<int:folder_id>/children', methods=['POST'])
def get_children(folder_id):
    # gets a query of all the rows where the specified folder ID is the parent
    query = file_table.query(filetable_def.Child).filter(filetable_def.Child.folder_id == folder_id)

    data = []
    for row in query:
        subquery = file_table.query(filetable_def.FileSystemObject).filter(
            filetable_def.FileSystemObject.id == row.child_id)

        if subquery.count() > 0:
            file_row = subquery.first()
            file_data = {'id': file_row.id, 'type': file_row.type, 'name': file_row.name}

            data.append(file_data)

    return jsonify({'children': data})


@app.route('/AirHaven/api/1.0/users/authenticate-user')
def auth_user():
    # Process the standard authentication header
    credentials = request.authorization

    # Find a matching username in the table
    query = user_table.query(usertable_def.User).filter(usertable_def.User.username.in_([credentials.username]))
    result = query.first()

    # Check the password hashes if a username was found in the database
    user_root_folder_id = -1
    if result:
        user_validated = pbkdf2_sha256.verify(credentials.password, result.password_hash)
        # If a valid token is given, update the root folder.
        if user_validated:
            user_root_folder_id = result.root_folder_id
    else:
        user_validated = False

    return jsonify({'token': user_validated, 'root_directory': user_root_folder_id})


@app.route('/AirHaven/api/1.0/users/register-user')
def register_user():
    success = True
    return_json = []
    user_data = request.json

    username = user_data['username']
    email = user_data['email']
    password = user_data['password']

    query = user_table.query(usertable_def.User).filter(usertable_def.User.username.in_([username]))
    result = query.first()

    if result:
        success = False
        return_json.append('That username is already in use.')

    if success:
        # Add a file path root for the user if it doesn't exist already
        user_local_root_dir = '/'.join([USER_ROOT_DIR, username])
        if not os.path.exists(user_local_root_dir):
            os.makedirs(user_local_root_dir)
        # Add the new local root to the database
        user_root_obj = filetable_def.FileSystemObject('username', 'folder', user_local_root_dir)
        file_table.add(user_root_obj)

        # Get the ID of the path just created, by looking for the path
        query = file_table.query(filetable_def.FileSystemObject). \
            filter(filetable_def.FileSystemObject.path.in_([user_local_root_dir]))
        result = query.first()
        user_root_id = result.id

        # Assign the root ID to the new user
        new_user = usertable_def.User(username, email, pbkdf2_sha256.hash(password), user_root_id)
        user_table.add(new_user)

    return jsonify({'errors': return_json})


if __name__ == '__main__':
    app.run(debug=True, host=APP_HOST, port=APP_PORT)
