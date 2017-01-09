pkgstack
===========

.. image:: https://travis-ci.org/ownport/pkgstack.svg?branch=master
   :target: https://travis-ci.org/ownport/pkgstack
.. image:: https://codecov.io/gh/ownport/pkgstack/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/ownport/pkgstack

Simple python package management tool based on pip

How to install
--------------

to install `pkgstack` use the `Release page <https://github.com/ownport/pkgstack/releases>`_
to download `pkgstack` and run it from command line as:

    $ ./pkgstack


How to use
----------

To get a help about how to use `pkgstack` please use option `--help`:

    $ ./pkgstack --help

    usage: pkgstack [-h] [-v] -p PROFILE [-s STAGE] [-l LOGGING]

    optional arguments:
    -h, --help            show this help message and exit
    -v, --version         show program's version number and exit
    -p PROFILE, --profile PROFILE
                          the path to the package profile, yaml file
    -s STAGE, --stage STAGE
                          the stage name
    -l LOGGING, --logging LOGGING
                          logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL


The profile sample:

.. code-block:: yaml

    - install: pytest
      stage: test

    - name: pytest-cov, pytest plugin for measuring coverage.
      install: pytest-cov
      stage: test

    - name: codecov, report uploader for Codecov https://codecov.io
      install: codecov
      stage: test
      alternatives:
      - test1
      - test2

    - name: dtguess, library for data type guessing
      install: dtguess==0.1.3

    - install: dtguess==0.1.3
      alternatives:
      - https://github.com/ownport/dtguess/releases/download/v0.1.3/dtguess-0.1.3.tar.gz
      target: pkgstack/vendor/


The profile contains the list of packages which shall be installed. Each package section consists from:

- name: optional parameter is used to define short description of the package
- install: mandatory word is used to define the primary installation step
- alternatives: optional parameter is used to define the alternatives for installation, if primary is not successful
- target: optional parameter is used to define the target directory for package installation
- stage: optional parameter is used to define the stage where the package is needed to be installed. The package will be installed only if the stage specified obviously in command line via --stage parameter. The packages without stage parameter will be installed automatically.
- no-deps: optional parameters, if true, don't install package dependencies.

Samples
---------

To install python packages from profile:

    $ ./pkgstack --profile packages.yml

If there is needed to install packages from several profiles:

    $ ./pkgstack --profile primary.yml --profile secondary.yml

The profile can contains packages which are required in different stages. For example: if you need to install only required packages without development packages, you need to tun

    $ ./pkgstack --profile packages.yml

this command will install only packages without "stage" parameter. If you define stage parameter in the command line with indication a stage or stages, pkgstack will install all packages without stage parameter + packages with specified stage

    $ ./pkgstack --profile packages.yml --stage test

Also you can specify several stages:

    $ ./pkgstack --profile packages.yml --stage test --stage docker


For developers
--------------

All the tests are performed in Docker containers. Use the command:

    $ make run-local-ci

to start docker containers vi local-ci tool

.. _Packaging and Distributing Projects: https://packaging.python.org/distributing/
