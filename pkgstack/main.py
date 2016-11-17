# -*- coding: utf-8 -*-

import os
import sys
import pip
import argparse

import utils

from __init__ import __version__
from profile import Profile

# path = utils.realpath(__file__)
# utils.vendor_add(os.path.dirname(os.path.dirname(path)))
# utils.vendor_add(os.path.join(os.path.dirname(path), 'vendor/'))
# # PY2/PY3 support for YAML lib
# if sys.version_info.major == 3:
#     from vendor.lib3x import yaml
# else:
#     from vendor.lib2x import yaml


def run():

    parser = argparse.ArgumentParser(prog='pkgstack')
    parser.add_argument('-v', '--version', action='version', version='v%s' % __version__)
    parser.add_argument('-p', '--profile', required=True,
            action='append', help='the path to the package profile, yaml file')
    args = parser.parse_args()

    if args.profile:
        for profile_path in args.profile:
            if not os.path.exists(profile_path):
                raise IOError('The path to profile does not exist, %s' % profile_path)
            Profile(profile_path).process()
    else:
        parser.print_help()
