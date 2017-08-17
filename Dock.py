from flask import Flask, jsonify, abort, make_response, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from passlib.hash import pbkdf2_sha256
import filetable_def
import usertable_def
import yaml
import base64


# Load the configuration
with open("config/app-config.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

    if cfg['app']['host'] == 'localhost':
        APP_HOST = '127.0.0.1'
    else:
        APP_HOST = cfg['app']['host']

    APP_PORT = cfg['app']['port']

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
    query = file_table.query(filetable_def.FileSystemObject).filter(filetable_def.FileSystemObject.id == file_id).\
                                               filter(filetable_def.FileSystemObject.type == "file")
    if query.count() < 1:
        abort(404)

    file_obj = query.first()
    # TODO: replace path with file data itself for /download
    data = {file_obj.type: {'id': file_obj.id, 'name': file_obj.name, 'path': file_obj.path}}

    return jsonify(data)


@app.route('/AirHaven/api/1.0/files/<int:folder_id>/children', methods=['POST'])
def get_children(folder_id):
    # gets a query of all the rows were the specified folder ID is in the
    query = file_table.query(filetable_def.Child).filter(filetable_def.Child.folder_id == folder_id)

    if query.count() < 1:
        abort(404)

    data = []
    for row in query:
        subquery = file_table.query(filetable_def.FileSystemObject).filter(filetable_def.FileSystemObject.id == row.child_id)

        # TODO: special handling with empty folders? (subquery.count() == 0)
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
    if result:
        user_validated = pbkdf2_sha256.verify(credentials.password, result.password_hash)
    else:
        user_validated = False

    return jsonify({'token': user_validated})


if __name__ == '__main__':
    app.run(debug=True, host=APP_HOST, port=APP_PORT)
