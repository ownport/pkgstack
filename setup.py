from setuptools import setup

from pkgstack import __title__
from pkgstack import __version__

setup(
    name=__title__,
    version=__version__,
    packages=[__title__,],
    url='https://github.com/ownport/pkgstack',
    author='Andrey Usov',
    author_email='ownport@gmail.com',
    py_modules=['pkgstack'],
    entry_points='''
        [console_scripts]
        pkgstack=pkgstack.main:run
    ''',
    keywords=['pip', 'install', 'wrapper', 'yaml', 'package', 'pypi']
)
