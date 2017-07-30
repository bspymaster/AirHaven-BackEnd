# AirHaven #

**Author**: Ben Schwabe

**Webpage**: https://github.com/bspymaster/AirHaven-BackEnd    

## Summary ##
Keep your files secure in your own flying fortress in the clouds.

This application is designed to be a back end file server "haven" to which the web app can "dock", found [here](https://github.com/bspymaster/AirHaven-FrontEnd).

## Requirements ##
- Python 3.3+
- Virtualenv

## Installation ##
1. Set up a python virtual environment by executing `virtualenv flaskenv` from inside the directory that the webapp will reside.
2. Activate the virtual environment. Documentation on how to do so can be found [here](https://virtualenv.pypa.io/en/stable/userguide/#activate-script).
3. Install the dependencies by executing `pip install -r requirements.txt` from the same subfolder that the `requirements.txt` file is located.

## Usage ##
1. Confirm that the software has been set up and that the configuration settings are correct.
2. Execute `tabledef.py` (usually by running the command `python tabledef.py`).
    1. After executing, there should be an SQLite file in the same directory as `tabledef.py` called `filetable.db`.
3. Execute `Dock.py` and confirm that the ip and port were properly bound and that the web server is running.
4. Make API calls as needed, or run the web app front end located [here](https://github.com/bspymaster/AirHaven-FrontEnd).
