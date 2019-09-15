# from flask import jsonify, abort, make_response, request
import os
from base.config import (
    connexion_app,
    database,
    base_dir,
    database_folder,
    database_file_name,
    config_folder,
    api_config_file_name,
    app_host,
    app_port
)


# build database if it doesn't exist
if not os.path.exists(os.path.join(base_dir, database_folder, database_file_name)):
    database.create_all()


@connexion_app.route('/')
def hello_world():
    return f'Please see the Swagger UI for API documentation, located at:<br>{app_host}/&lt;your_api_server_url&gt;/ui.'


if __name__ == '__main__':
    # Add the API and start the application
    connexion_app.add_api(os.path.join(base_dir, config_folder, api_config_file_name))
    connexion_app.run(debug=True, host=app_host, port=app_port)
