from flask import abort, jsonify
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# from base.datamodel import FileSystem

# # Load the file table
# filetable_engine = create_engine('sqlite:///filetable.db', echo=True)
# filetable_session = sessionmaker(bind=filetable_engine)
# file_table = filetable_session()
#
# # Load the user table
# usertable_engine = create_engine('sqlite:///usertable.db', echo=True)
# usertable_session = sessionmaker(bind=usertable_engine)
# user_table = usertable_session()


def retrieve_all(length=-1):
    """

    :param length:  the number of objects to get
    :return:        json string of list of files, limited to the length provided, if any
    """

    abort(500, 'This feature has not been implemented yet (file={0})'.format(length))


def create_new_file(file_data):
    """

    :param file_data:   A formatted JSON object containing all the information needed to add a file to the system
    :return:            A success or error code
    """
    abort(500, 'This feature has not been implemented yet (file={0})'.format(file_data))


def retrieve_file_by_id(file_id):
    """

    :param file_id: The ID of the file to retrieve
    :return:        A JSON object of all the file data
    """
    # query = FileSystem.query.filter(FileSystem.id == file_id).filter(FileSystem.type == "file")
    # if query.count() < 1:
    #     abort(404)
    #
    # file_obj = query.first()
    # # TODO: replace path with file data itself for download
    # data = {file_obj.type: {'id': file_obj.id, 'name': file_obj.name, 'path': file_obj.path}}
    #
    # return jsonify(data)

    abort(500, 'This feature has not been implemented yet (file={0})'.format(file_id))


def update_file_by_id(file_id):
    abort(500, 'This feature has not been implemented yet (fileID={0})'.format(file_id))


def delete_file_by_id(file_id):
    abort(500, 'This feature has not been implemented yet (fileID={0})'.format(file_id))
