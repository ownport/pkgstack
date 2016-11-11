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

The sample of configuration file:

.. code-block:: yaml

    - install: pytest

    - name: Install pytest-cov
      install: pytest-cov

    - name: Install codecov
      install: codecov
      alternatives:
      - test1
      - test2

    - name: Install dtguess
      install: dtguess==0.1.3

    - install: dtguess==0.1.3
      alternatives:
      - https://github.com/ownport/dtguess/releases/download/v0.1.3/dtguess-0.1.3.tar.gz


For developers
--------------

All the tests are performed in Docker containers. Use the command:

    $ make run-local-ci

to start docker containers vi local-ci tool

.. _Packaging and Distributing Projects: https://packaging.python.org/distributing/
