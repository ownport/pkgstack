
#
#   Package details
#
#
import os
import pip
import shutil
import logging

class Package(object):

    def __init__(self, details):

        self._details = details
        self._logger = logging.getLogger(__name__)


    def _install(self, pkg, target_dir=None):
        ''' pip install <package>
        '''
        params = ['install',]
        if target_dir:
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            params.extend(['--target', target_dir])
        params.append(pkg)
        return pip.main(params)


    def _clear_vendor_dir(self, path):
        ''' clean vendor dir
        '''
        if not path or not os.path.exists(path):
            return

        for root, dirs, files in os.walk(path):
            # remove directories ended with .egg-info
            if root.endswith('.egg-info') and os.path.isdir(root):
                shutil.rmtree(root)
            # remove *.pyc
            map(lambda x: os.remove(x) if x.endswith('.pyc') else x, files)


    def install(self):
        ''' install package

        returns
            primary = True if primary installation rule was used
            alternative = True if one of the alternative rule was used
        '''
        if 'name' in self._details:
            self._logger.info('%s, %s' % (self._details['name'], self._details))
        else:
            self._logger.info('Package: %s' % self._details)

        target_dir = self._details.get('target', None)
        if 'install' in self._details:
            if self._install(self._details['install'], target_dir=target_dir) == 0:
                self._clear_vendor_dir(target_dir)
                return {'primary': True, "alternative": False}

        if 'alternatives' in self._details:
            for alt in self._details['alternatives']:
                if self._install(alt, target_dir=target_dir) == 0:
                    self._clear_vendor_dir(target_dir)
                    return {'primary': False, "alternative": True}

        self._logger.error('Cannot install the package: %s' % self._details['name'])
        return {'primary': False, "alternative": False}
