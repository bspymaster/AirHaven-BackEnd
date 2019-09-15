import os
import sys
import connexion
import yaml
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Get the base directory
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# Folder names
config_folder = 'config'
database_folder = 'base'

# File names
database_file_name = 'data.db'
api_config_file_name = 'api-config.yaml'
app_config_file_name = 'app-config.yaml'

# Create the Connexion application instance
connexion_app = connexion.App(__name__, specification_dir=base_dir)

# Get the underlying Flask app instance
flask_app = connexion_app.app

# SqlLite needs a different URI prefix on Windows than other OSes
if sys.platform.startswith('win32'):
    _sqllite_prefix = 'sqlite:///'
else:
    _sqllite_prefix = 'sqlite:////'

# Configure the SQLAlchemy part of the app instance
flask_app.config['SQLALCHEMY_ECHO'] = True  # turn off for production
flask_app.config['SQLALCHEMY_DATABASE_URI'] = _sqllite_prefix + database_file_name
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # turn off event system

# Create the SQLAlchemy db instance
database = SQLAlchemy(flask_app)

# Initialize Marshmallow
marshmallow = Marshmallow(flask_app)


# Load the configuration
with open(os.path.join(base_dir, config_folder, app_config_file_name), 'r') as _yml_file:
    _cfg = yaml.load(_yml_file, Loader=yaml.FullLoader)

    # Load connection details
    if _cfg['app']['host'] == 'localhost':
        app_host = '127.0.0.1'
    else:
        app_host = _cfg['app']['host']
    app_port = _cfg['app']['port']

    # Load file system details
    user_root_dir = _cfg['files']['root_folder']
    # Create the user root directory if it does not exist
    if not os.path.exists(user_root_dir):
        os.makedirs(user_root_dir)
