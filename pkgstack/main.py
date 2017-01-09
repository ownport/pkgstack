# -*- coding: utf-8 -*-

import os
import argparse

import logging
# Set default logging handler to avoid "No handler found" warnings.
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logger = logging.getLogger(__name__)

from __init__ import __version__
from profile import Profile


def run():

    parser = argparse.ArgumentParser(prog='pkgstack')
    parser.add_argument('-v', '--version', action='version', version='v%s' % __version__)
    parser.add_argument('-p', '--profile', required=True,
            action='append', help='the path to the package profile, yaml file')
    parser.add_argument('-s', '--stage', action='append', help='the stage name')
    parser.add_argument('-l', '--logging', type=str,
            help='logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL')
    process(parser, parser.parse_args())


def process(parser, args):

    result = list()
    log_level = logging.ERROR
    if args.logging:
        log_level = getattr(logging, args.logging.upper(), None)
        if not isinstance(log_level, int):
            logger.warning('Invalid log level: %s' % log_level)
            logger.info('Default log level: ERROR')

    logging.basicConfig(level=log_level,
                        handler=NullHandler(),
                        format="%(asctime)s (%(name)s) [%(levelname)s] %(message)s"
    )

    if args.profile:
        for profile_path in args.profile:
            if not os.path.exists(profile_path):
                logger.error('The path to profile does not exist, %s' % profile_path)
                continue
            stages = args.stage if isinstance(args.stage, list) else []
            try:
                result.append(Profile(profile_path, stages=stages).process())
            except Exception, err:
                logger.error(err)
                continue
    else:
        parser.print_help()

    return result
