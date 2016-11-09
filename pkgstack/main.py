# -*- coding: utf-8 -*-

import os
import sys
import pip
import argparse


# PY2/PY3 support for YAML lib
if sys.version_info.major == 3:
    from vendor.lib3x import yaml
else:
    from vendor.lib2x import yaml


def read_config(configfile):

    config = None
    with open(configfile, 'r') as config:
        config = yaml.load(config)
    return config


def install_package(pkg_info):

    if 'name' in pkg_info:
        print('[INFO] %s, %s' % (pkg_info['name'], pkg_info))
    else:
        print('[INFO] Package: %s' % pkg_info)

    return pip.main(['install', pkg_info['install']])



def process(config):

    result = dict()
    result['packages.successed'] = 0
    result['packages.failed'] = 0
    result['packages.total'] = len(config)

    for pkg_info in config:

        if 'install' in pkg_info:
            if install_package(pkg_info) == 0:
                result['packages.successed'] += 1
                continue
            elif 'alternatives' in pkg_info:
                for alt in pkg_info['alternatives']:
                    if pip.main(['install', alt]) == 0:
                        result['packages.successed'] += 1
                        break
                result['packages.failed'] += 1

            else:
                print('[ERROR] Cannot install the package: %s' % pkg_info['name'])
    return result


def run():

    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    print(args)


    # if len(sys.argv) == 1:
    #     usage()
    #
    # for profile in sys.argv[1:]:
    #     if profile in ('deps', 'dev-deps'):
    #         install(profile)
    #     else:
    #         print '[ERROR] Only "deps" or/and "dev-deps" profiles are supported'
    #         usage()
