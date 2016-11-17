
#
#   Package details
#
#
import pip

class Package(object):

    def __init__(self, details):

        self._details = details


    def _install(self, pkg):
        ''' pip install <package>
        '''
        return pip.main(['install', pkg])


    def install(self):
        ''' install package

        returns
            primary = True if primary installation rule was used
            alternative = True if one of the alternative rule was used
        '''
        print self._details
        if 'name' in self._details:
            print('[INFO] %s, %s' % (self._details['name'], self._details))
        else:
            print('[INFO] Package: %s' % self._details)

        if 'install' in self._details:
            if self._install(self._details['install']) == 0:
                return {'primary': True, "alternative": False}

        if 'alternatives' in self._details:
            for alt in self._details['alternatives']:
                if self._install(alt) == 0:
                    return {'primary': False, "alternative": True}

        print('[ERROR] Cannot install the package: %s' % self._details['name'])
        return {'primary': False, "alternative": False}
