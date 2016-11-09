pkgstack
===========

.. image:: https://travis-ci.org/ownport/pkgstack.svg?branch=master
    :target: https://travis-ci.org/ownport/pkgstack
.. image:: https://codecov.io/gh/ownport/pkgstack/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/ownport/pkgstack

Simple python package management tool based on pip

How to install
--------------

to install `pkgstack` use the Releases page ..image:: https://github.com/ownport/pkgstack/releases
to download `pkgstack` and run it from command line as:

    $ ./pkgstack


How to use
----------

To get a help about how to use `pkgstack` please use option `--help`:

    $ ./pkgstack --help


For developers
--------------

All the tests are performed in Docker containers. Use the command:

    $ make run-local-ci

to start docker containers vi local-ci tool
