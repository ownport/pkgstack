
import os
import pytest

from pkgstack.package import Package


def test_target_dir(tmpdir):

    vendor_path = os.path.join(str(tmpdir), 'vendor/')
    pkg = Package({
        'install': 'pkgstack', 'target': vendor_path
    })
    pkg.install()
    for f in os.listdir(os.path.join(vendor_path, 'pkgstack/')):
        if f.endswith('.egg-info'):
            assert False, 'Error! Founded path with ended .egg-info'

    pkg = Package({
        'install': 'six', 'target': vendor_path
    })
    pkg.install()
    for f in os.listdir(os.path.join(vendor_path, 'pkgstack/')):
        if f.endswith('.dist-info'):
            assert False, 'Error! Founded path with ended .dist-info'
