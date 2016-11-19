
import sys
import pytest

from pkgstack import utils

def test_current_python_version():

    major_version, minor_version  = utils.current_py_version()
    assert major_version in (2,3)
    assert minor_version >= 0


def test_vendor_add(tmpdir):

    path = str(tmpdir.mkdir('add_libpath'))
    utils.vendor_add(path)
    assert path in sys.path

    with pytest.raises(IOError):
        utils.vendor_add('/example')


def test_realpath():

    assert utils.realpath('tests/test_utils.py') == __file__


def test_package_ckeck():

    assert utils.package_exists('sys') == True
    assert utils.package_exists('-sys-') == False
