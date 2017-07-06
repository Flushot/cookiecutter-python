from __future__ import absolute_import, print_function, unicode_literals, division

import locale
import logging
import os

log = logging.getLogger(__name__)


def get_package_root_path():
    """
    Get the absolute path to the installed Python package.

    :return: path.
    """
    return os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))


def get_config_path(config_file=None):
    """
    Get the absolute path to the config directory.

    :param config_file: (optional) name of config file to include in path.
    :return: path.
    """
    config_path = os.path.join(get_package_root_path(), 'config')
    if config_file is None:
        return config_path
    else:
        return os.path.join(config_path, config_file)
