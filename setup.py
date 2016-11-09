from setuptools import setup

from pkgstack import __title__
from pkgstack import __version__

setup(
    name=__title__,
    version=__version__,
    url='https://github.com/ownport/pkgstack',
    py_modules=['pkgstack'],
    entry_points='''
        [console_scripts]
        pkgstack=pkgstack.main:cli
    ''',
)
