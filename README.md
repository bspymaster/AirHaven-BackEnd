# AirHaven #

**Author**: Ben Schwabe

**Webpage**: https://github.com/scytail/AirHaven-BackEnd

## Summary ##
Keep your files secure in your own flying fortress in the clouds.

This application is designed to be a back end file server "haven" to which a all sorts of applications can "dock" to trade and interact with the files stored.

## Requirements ##
- Python 3.3+
- Virtualenv

## Installation ##
1. Set up a python virtual environment by executing `virtualenv flaskenv` from inside the directory that the webapp will reside.
2. Activate the virtual environment. Documentation on how to do so can be found [here](https://virtualenv.pypa.io/en/stable/userguide/#activate-script).
3. Install the dependencies by executing `pip install -r requirements.txt` from the same subfolder that the `requirements.txt` file is located.

## Usage ##
1. Confirm that the software has been set up and that the configuration settings are correct.
2. Execute `Dock.py` and confirm that the ip and port were properly bound and that the web server is running.
3. Make API calls as needed, or view the UI by taking your API server's URL and appending `/ui` to it.

## Configuration Details ##
The configuration data for the application is located in `config/app-config.yaml`, and is a standard YAML script file. The details for the specific configuration settings are found below.

- `app/host`: The IP address on which the server will run.
- `app/port`: The port on which the server will listen.
- `files/root_folder`: The root directory in which all user root folders will be saved. To use an absolute path, start the path with a forward slash (`/`), followed by the path. To use a relative path, omit the leading forward slash. **Never** end the path with a forward slash.
