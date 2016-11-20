
import os
import sys
import logging
import importlib


def current_py_version():
    ''' return current python version
    '''
    return sys.version_info[0], sys.version_info[1]

#
#   Vendoring of python packages as example:
#   https://cloud.google.com/appengine/docs/python/refdocs/modules/google/appengine/ext/vendor
#   https://cloud.google.com/appengine/docs/python/tools/using-libraries-python-27#installing_a_third-party_library
#
def vendor_add(path):
    ''' add vendor path to sys.path
    '''
    if os.path.exists(path) and os.path.isdir(path):
        sys.path.insert(0, path)
    else:
        raise IOError('The vendor path does not exist, %s' % path)


def realpath(path):
    ''' return absolute real path
    '''
    return os.path.realpath(os.path.abspath(path))


def import_module(name, package=None):
    ''' returns imported module (vendored)
    '''
    package_prefix = ''
    if package and package_exists(package):
        package_prefix = '%s.' % package

    params = (package_prefix, name)
    if sys.version_info.major == 3:
        return importlib.import_module('%svendor.lib3x.%s' % params)
    else:
        return importlib.import_module('%svendor.lib2x.%s' % params)


def package_exists(name):
    ''' check if package exists and can be imported
    '''
    try:
        __import__(name)
    except ImportError:
        return False
    else:
        return True
