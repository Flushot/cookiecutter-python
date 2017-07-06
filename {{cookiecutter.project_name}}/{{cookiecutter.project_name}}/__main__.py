#!/usr/bin/env python
from __future__ import absolute_import, print_function, unicode_literals, division

import locale
import logging
import logging.config

import argparse

from . import utils, __version__


def main():
    # Parse arguments
    argp = argparse.ArgumentParser(description='{{cookiecutter.project_name}}')
    args = argp.parse_args()

    locale.setlocale(locale.LC_ALL, '')  # Use system locale

    # Init logging
    logging.config.fileConfig(utils.get_config_path('logging.ini'))
    log = logging.getLogger(__name__)

    log.info('Starting {{cookiecutter.project_name}} v{}'.format(__version__))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
