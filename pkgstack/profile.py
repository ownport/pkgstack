
import sys

# PY2/PY3 support for YAML lib
if sys.version_info.major == 3:
    from pkgstack.vendor.lib3x import yaml
else:
    from pkgstack.vendor.lib2x import yaml

from pkgstack.package import Package


class Profile(object):

    def __init__(self, path):

        self._profile = None
        with open(path, 'r') as profile:
            _config = yaml.load(profile)
            self._profile = _config


    @property
    def config(self):
        ''' returns profile details
        '''
        return self._profile


    def process(self):
        ''' process packages in the profile
        '''
        result = dict()
        result['packages.successed'] = 0
        result['packages.failed'] = 0
        result['packages.total'] = len(self._profile)

        for pkg_info in self._profile:

            install_result = Package(pkg_info).install()
            if not install_result['primary'] and not install_result['alternative']:
                result['packages.failed'] += 1
            else:
                result['packages.successed'] += 1
        return result
