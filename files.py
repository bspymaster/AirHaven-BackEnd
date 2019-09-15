from flask import abort
# from base.datamodel import *

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

    # if not isinstance(file_id, int):
    #     abort(400, f'{file_id} is not a valid integer.')
    #
    # query = FileSystem.query.filter(FileSystem.filesystem_id == file_id).one_or_none()
    #
    # if query is not None:
    #     query_schema = FileSystemSchema()
    #     return query_schema.dump(query).data
    # else:
    #     abort(404, f'File not found for ID {file_id}')

    abort(500, 'This feature has not been implemented yet (file={0})'.format(file_id))


def update_file_by_id(file_id):
    abort(500, 'This feature has not been implemented yet (fileID={0})'.format(file_id))


def delete_file_by_id(file_id):
    abort(500, 'This feature has not been implemented yet (fileID={0})'.format(file_id))
