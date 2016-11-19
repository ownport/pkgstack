# -*- coding: utf-8 -*-

import os
import argparse

from __init__ import __version__
from profile import Profile

def run():

    parser = argparse.ArgumentParser(prog='pkgstack')
    parser.add_argument('-v', '--version', action='version', version='v%s' % __version__)
    parser.add_argument('-p', '--profile', required=True,
            action='append', help='the path to the package profile, yaml file')
    parser.add_argument('-s', '--stage', action='append', help='the stage name')
    args = parser.parse_args()

    if args.profile:
        for profile_path in args.profile:
            if not os.path.exists(profile_path):
                raise IOError('The path to profile does not exist, %s' % profile_path)
            Profile(profile_path).process()
    else:
        parser.print_help()
