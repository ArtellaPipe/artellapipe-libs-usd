#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains functions to retrieve USD related paths
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import os
import logging

LOGGER = logging.getLogger('artellapipe-libs-usd')


def get_usd_externals_path():
    """
    Returns artellapipe-libs-usd USD externals directory
    :return: str
    """

    externals_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'externals')

    return externals_dir


def get_usd_plugins_path():
    """
    Returns artellapipe-libs-usd USD plugins directory
    :return: str
    """

    plugins_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'plugins')

    return plugins_dir


def get_platform_path():
    """
    Returns externals path based on current platform
    :return: str
    """

    from tpDcc.libs.python import path, osplatform

    externals_dir = get_usd_externals_path()
    if not externals_dir or not os.path.isdir(externals_dir):
        LOGGER.warning('No externals directory found: "{}"'.format(externals_dir))
        return

    platform_name = osplatform.get_platform().lower()
    os_architecture = osplatform.get_architecture()

    platform_path = path.clean_path(
        os.path.join(externals_dir, platform_name, os_architecture, 'usd'))
    if not os.path.isdir(platform_path):
        LOGGER.warning('No USD externals platform folder found: "{}"'.format(platform_path))
        return None

    return platform_path


def get_usd_path():
    """
    Returns path where USD plugin is located
    :return: str
    """

    from tpDcc.libs.python import path

    platform_dir = get_platform_path()
    if not platform_dir or not os.path.isdir(platform_dir):
        LOGGER.warning('No USD platform directory found: "{}"'.format(platform_dir))
        return

    pixar_usd_path = path.clean_path(
        os.path.join(platform_dir, 'pixar')
    )
    if not os.path.isdir(pixar_usd_path):
        LOGGER.warning('No Pixar USD folder found: "{}"'.format(pixar_usd_path))
        return None

    return pixar_usd_path


def get_pixar_usd_python_libs_path():
    """
    Returns Python libraries directory of Pixar USD library
    :return: str
    """

    pixar_usd_path = get_usd_path()
    if not pixar_usd_path:
        return

    pixar_usd_python_libs = os.path.join(pixar_usd_path, 'lib', 'python')
    if not os.path.isdir(pixar_usd_python_libs):
        LOGGER.warning('No Pixar USD Python libraries directory found: "{}"'.format(pixar_usd_python_libs))
        return

    return pixar_usd_python_libs


def get_pixar_usd_binaries_path():
    """
    Returns binaries directory of Pixar USD library
    :return: str
    """

    pixar_usd_path = get_usd_path()
    if not pixar_usd_path:
        return

    pixar_usd_bin_path = os.path.join(pixar_usd_path, 'bin')
    if not os.path.isdir(pixar_usd_bin_path):
        LOGGER.warning('No Pixar USD binaries directory found: "{}"'.format(pixar_usd_bin_path))
        return

    return pixar_usd_bin_path


def get_pixar_usd_libraries_path():
    """
    Returns libraries directory of Pixar USD library
    :return: str
    """

    pixar_usd_path = get_usd_path()
    if not pixar_usd_path:
        return

    pixar_usd_libs_path = os.path.join(pixar_usd_path, 'lib')
    if not os.path.isdir(pixar_usd_libs_path):
        LOGGER.warning('No Pixar USD libraries directory found: "{}"'.format(pixar_usd_libs_path))
        return

    return pixar_usd_libs_path


def get_usd_dcc_path():
    """
    Returns path where USD plugin is located for current DCC version
    :return: str
    """

    import tpDcc as tp
    from tpDcc.libs.python import path

    platform_dir = get_platform_path()
    if not platform_dir or not os.path.isdir(platform_dir):
        LOGGER.warning('No USD platform directory found: "{}"'.format(platform_dir))
        return

    dcc_name = tp.Dcc.get_name()
    dcc_version = tp.Dcc.get_version_name()

    usd_dcc_path = path.clean_path(os.path.join(platform_dir, dcc_name, dcc_version))
    if not os.path.isdir(platform_dir):
        LOGGER.warning('No USD executable folder found: "{}"'.format(usd_dcc_path))
        return None

    return usd_dcc_path


def get_usd_qt_path():
    """
    Returns path where USD Qt files are located
    :return: str
    """

    from tpDcc.libs.python import path

    platform_dir = get_platform_path()
    if not platform_dir or not os.path.isdir(platform_dir):
        LOGGER.warning('No USD platform directory found: "{}"'.format(platform_dir))
        return

    usd_qt_path = path.clean_path(os.path.join(platform_dir, 'qt'))
    if not os.path.isdir(platform_dir):
        LOGGER.warning('No USD Qt folder found: "{}"'.format(usd_qt_path))
        return None

    return usd_qt_path


def get_arnold_path():
    """
    Returns path where Arnold USD is located
    :return:str
    """

    import tpDcc as tp
    from tpDcc.libs.python import path

    if not tp.is_maya():
        return

    MTOA_ARNOLD_MAPPING = {
        '0.16': '4.0.4.0',
        '0.17': '4.0.6.0',
        '0.18': '4.0.6.0',
        '0.19': '4.0.9.1',
        '0.20': '4.0.10.0',
        '0.21': '4.0.11.0',
        '0.22': '4.0.12.1',
        '0.22.1': {'win': '4.0.12.1', 'linux': '4.0.12.0'},
        '0.23': '4.0.14.0',
        '0.23.1': '4.0.14.0',
        '0.24': '4.0.15.1',
        '0.25': '4.0.16.0',
        '0.25.1': '4.0.16.0',
        '0.25.2': '4.0.16.0',
        '0.25.3': '4.0.16.2',
        '1.0': '4.1.3.2',
        '1.0.0.1': '4.1.3.3',
        '1.0.0.2': '4.1.3.5',
        '1.1': '4.2.0.5',
        '1.1.0.4': '4.2.0.6',
        '1.1.1.0': '4.2.1.2',
        '1.1.1.1': '4.2.1.2',
        '1.1.2.0': '4.2.2.0',
        '1.1.2.1': '4.2.2.0',
        '1.1.2.2': '4.2.2.0',
        '1.2': '4.2.3.0',
        '1.2.0.2': '4.2.3.1',
        '1.2.0.3': '4.2.3.1',
        '1.2.0.4': '4.2.3.1',
        '1.2.1.0': '4.2.4.1',
        '1.2.2.0': '4.2.6.1',
        '1.2.3.0': '4.2.7.3',
        '1.2.3.1': '4.2.7.4',
        '1.2.4.0': '4.2.9.0',
        '1.2.4.1': '4.2.9.0',
        '1.2.4.2': '4.2.10.0',
        '1.2.4.3': '4.2.11.0',
        '1.2.5.0': '4.2.11.3',
        '1.2.6.0': '4.2.12.2',
        '1.2.6.1': '4.2.12.2',
        '1.2.7.0': '4.2.13.0',
        '1.2.7.1': '4.2.13.1',
        '1.2.7.2': '4.2.13.3',
        '1.2.7.3': '4.2.13.4',
        '1.3.0.1': '4.2.14.2',
        '1.3.1': '4.2.14.2',
        '1.3.1.1': '4.2.14.3',
        '1.3.1.2': '4.2.14.4',
        '1.4.0': '4.2.15.1',
        '1.4.1': '4.2.16.0',
        '1.4.1.1': '4.2.16.0',
        '1.4.1.2': '4.2.16.1',
        '1.4.2': '4.2.16.2',
        '2.0.0': '5.0.0.0',
        '2.0.0.1': '5.0.0.2',
        '2.0.1': '5.0.1.0',
        '2.0.1.1': '5.0.1.1',
        '2.0.2': '5.0.1.2',
        '2.0.2.1': '5.0.1.3',
        '2.0.2.2': '5.0.1.4',
        '2.0.2.3': '5.0.1.4',
        '2.0.2.4': '5.0.1.5',
        '2.1.0': '5.0.2.0',
        '2.1.0.1': '5.0.2.1',
        '2.1.0.2': '5.0.2.3',
        '2.1.0.3': '5.0.2.4',
        '3.0.0': '5.1.0.0',
        '3.0.0.1': '5.1.0.0',
        '3.0.0.2': '5.1.0.1',
        '3.0.1': '5.1.1.0',
        '3.0.1.1': '5.1.1.1',
        '3.1.0': '5.2.0.0',
        '3.1.0.1': '5.2.0.1',
        '3.1.1': '5.2.1.0',
        '3.1.2': '5.2.2.0',
        '3.1.2.1': '5.2.2.1',
        '3.2.0': '5.3.0.0',
        '3.2.0.1': '5.3.0.1',
        '3.2.0.2': '5.3.0.2',
        '3.2.1': '5.3.1.0',
        '3.2.1.1': '5.3.1.1',
        '3.2.2': '5.3.1.1',
        '3.3.0': '5.4.0.0',
        '3.3.0.1': '5.4.0.1',
        '3.3.0.2': '5.4.0.2',
        '4.0.0': '6.0.0.0',
        '4.0.1': '6.0.1.0',
        '4.0.1.1': '6.0.1.1',
        '4.0.2': '6.0.2.0',
        '4.0.2.1': '6.0.2.1',
        '4.0.3': '6.0.3.0'
    }

    import tpDcc.dccs.maya as maya

    mtoa_version = maya.cmds.pluginInfo('mtoa', query=True, version=True)
    if mtoa_version not in MTOA_ARNOLD_MAPPING:
        LOGGER.warning('MtoA plugin version: {} is not supported!'.format(mtoa_version))
        return

    arnold_core_version = MTOA_ARNOLD_MAPPING[mtoa_version]

    platform_dir = get_platform_path()
    if not platform_dir or not os.path.isdir(platform_dir):
        LOGGER.warning('No USD platform directory found: "{}"'.format(platform_dir))
        return

    arnold_usd_path = path.clean_path(os.path.join(platform_dir, 'arnold'))
    if not os.path.isdir(arnold_usd_path):
        LOGGER.warning('No Arnold USD folder found: "{}"'.format(arnold_usd_path))
        return None

    arnold_version_path = path.clean_path(os.path.join(arnold_usd_path, arnold_core_version))
    if not os.path.isdir(arnold_version_path):
        LOGGER.warning(
            'Arnold USD for Mtoa: {} | Arnold Core: {} is not being deployed!'.format(
                mtoa_version, arnold_core_version))
        return

    return arnold_version_path
