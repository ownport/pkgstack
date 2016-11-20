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


For developers
--------------

All the tests are performed in Docker containers. Use the command:

    $ make run-local-ci

to start docker containers vi local-ci tool

.. _Packaging and Distributing Projects: https://packaging.python.org/distributing/
