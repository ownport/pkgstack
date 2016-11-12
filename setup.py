from setuptools import setup

from pkgstack import __title__
from pkgstack import __version__

setup(
    name=__title__,
    version=__version__,
    description='Simple python package management tool based on pip',
    url='https://github.com/ownport/pkgstack',
    author='ownport',
    author_email='ownport@gmail.com',
    py_modules=['pkgstack'],
    packages=[
        'pkgstack',
        'pkgstack.vendor',
        'pkgstack.vendor.lib2x',
        'pkgstack.vendor.lib2x.yaml',
        'pkgstack.vendor.lib3x',
        'pkgstack.vendor.lib3x.yaml',
    ],
    entry_points={
        'console_scripts': [
            'pkgstack = pkgstack.main:run',
        ]
    },
    keywords=['pip', 'install', 'wrapper', 'yaml', 'package', 'pypi'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python',
    ],
)
