from flask import Flask, jsonify, abort, make_response, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import tabledef

engine = create_engine('sqlite:///filetable.db', echo=True)

user_session = sessionmaker(bind=engine)
s = user_session()

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
    query = s.query(tabledef.FileSystemObject).filter(tabledef.FileSystemObject.id == file_id).\
                                               filter(tabledef.FileSystemObject.type == "file")
    if query.count() < 1:
        abort(404)

    file_obj = query.first()
    # TODO: replace path with file data itself for /download
    data = {file_obj.type: {'id': file_obj.id, 'name': file_obj.name, 'path': file_obj.path}}

    return jsonify(data)


@app.route('/AirHaven/api/1.0/files/<int:folder_id>/children', methods=['POST'])
def get_children(folder_id):
    # gets a query of all the rows were the specified folder ID is in the
    query = s.query(tabledef.Child).filter(tabledef.Child.folder_id == folder_id)

    if query.count() < 1:
        abort(404)

    data = []
    for row in query:
        subquery = s.query(tabledef.FileSystemObject).filter(tabledef.FileSystemObject.id == row.child_id)

        # TODO: special handling with empty folders? (subquery.count() == 0)
        if subquery.count() > 0:
            file_row = subquery.first()
            file_data = {'id': file_row.id, 'type': file_row.type, 'name': file_row.name}

            data.append(file_data)

    return jsonify({'children': data})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=4000)
