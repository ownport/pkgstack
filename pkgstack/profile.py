
import sys
import utils
import logging

from package import Package

yaml = utils.import_module('yaml', package='pkgstack')


class Profile(object):

    def __init__(self, path, stages=[]):

        if not isinstance(stages, list):
            raise RuntimeError('Stages shall be defined as list')
        self._stages = stages

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

            pkg_stage = pkg_info.get('stage', None)
            if pkg_stage and pkg_info not in self._stages:
                continue

            install_result = Package(pkg_info).install()
            if not install_result['primary'] and not install_result['alternative']:
                result['packages.failed'] += 1
            else:
                result['packages.successed'] += 1
        return result
