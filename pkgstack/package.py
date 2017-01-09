
#
#   Package details
#
#
import os
import pip
import shutil
import logging

logger = logging.getLogger(__name__)


class Package(object):

    def __init__(self, details):

        self._details = details

    def _install(self, pkg, **args):
        ''' pip install <package>
        '''
        params = ['install', ]
        if 'target' in args:
            if not os.path.exists(args['target']):
                os.makedirs(args['target'])
            params.extend(['--target', args['target']])
        if 'no-deps' in args and args['no-deps'] is True:
            params.extend(['--no-deps'])

        params.append(pkg)
        logger.debug('Package: {}, params: {}'.format(pkg, params))
        return pip.main(params)

    def _clear_vendor_dir(self, path):
        ''' clean vendor dir
        '''
        if not path or not os.path.exists(path):
            return

        for root, dirs, files in os.walk(path):
            # remove directories ended with .egg-info
            if root.endswith('.dist-info') and os.path.isdir(root):
                shutil.rmtree(root)
                continue
            # remove directories ended with .egg-info
            if root.endswith('.egg-info') and os.path.isdir(root):
                shutil.rmtree(root)
                continue
            # remove *.pyc
            map(lambda x: os.remove(os.path.join(root,x)) if x.endswith('.pyc') else x, files)

    def install(self):
        ''' install package

        returns
            primary = True if primary installation rule was used
            alternative = True if one of the alternative rule was used
        '''
        if 'name' in self._details:
            logger.info('%s, %s' % (self._details['name'], self._details))
        else:
            logger.info('Package: %s' % self._details)

        if 'install' in self._details:
            if self._install(self._details['install'], **self._details) == 0:
                self._clear_vendor_dir(self._details.get('target', None))
                return {'primary': True, "alternative": False}

        if 'alternatives' in self._details:
            for alt in self._details['alternatives']:
                if self._install(alt, **self._details) == 0:
                    self._clear_vendor_dir(self._details.get('target', None))
                    return {'primary': False, "alternative": True}

        logger.error('Cannot install the package: %s' % self._details['name'])
        return {'primary': False, "alternative": False}
