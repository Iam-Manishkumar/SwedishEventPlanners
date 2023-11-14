

from setuptools import setup

APP = ['SwedishEventPlanner.py']
DATA_FILES = ['tasklist.json', 'eventRequest.json', 'none.json', 'none.json']
OPTIONS = {
    'argv_emulation': True,
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

from setuptools import setup

APP = ['SwedishEventPlanner.py']
DATA_FILES = ['tasklist.json', 'eventRequest.json', 'none.json', 'none.json']
OPTIONS = {
    'argv_emulation': True,
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)