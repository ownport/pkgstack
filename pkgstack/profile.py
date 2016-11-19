
import sys
import utils

from package import Package

yaml = utils.import_module('yaml', package='pkgstack')

class Profile(object):

    def __init__(self, path):

        print yaml

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
