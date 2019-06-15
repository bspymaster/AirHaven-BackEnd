# from flask import jsonify, abort, make_response, request
import os
from base.config import (
    connexion_app,
    app_host,
    app_port,
    base_dir,
    database_folder,
    database_file_name
)
# datamodel needs to be run before we can create_all on the database, so it knows what to pull
from base.datamodel import database

# build database if it doesn't exist
if not os.path.exists(os.path.join(base_dir, database_folder, database_file_name)):
    database.create_all()


@connexion_app.route('/')
def hello_world():
    return f'Please see the Swagger UI for API documentation, located at:<br>{app_host}/&lt;your_api_server_url&gt;/ui.'


if __name__ == '__main__':
    connexion_app.run(debug=True, host=app_host, port=app_port)
