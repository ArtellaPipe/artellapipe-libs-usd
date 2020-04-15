#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialization module for artellapipe-libs-usd
"""

from __future__ import print_function, division, absolute_import

import os
import sys

import logging

LOGGER = logging.getLogger()


def get_platform_path():
    """
    Returns externals path based on current platform
    :return: str
    """

    from tpDcc.libs.python import path, osplatform

    externals_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'externals')
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

    usd_dcc_path = path.clean_path(
        os.path.join(platform_dir, dcc_name, dcc_version))
    if not os.path.isdir(platform_dir):
        LOGGER.warning('No USD executable folder found: "{}"'.format(usd_dcc_path))
        return None

    return usd_dcc_path


def add_to_env(env_name, env_value):
    """
    Adds given value to the given environment variable
    :param env_name: str
    :param env_value: str
    """

    if env_name == 'PYTHONPATH':
        if env_value not in sys.path:
            sys.path.append(env_value)

    if not os.environ.get(env_name):
        os.environ[env_name] = str(env_value)
    else:
        if env_value not in os.environ[env_name]:
            os.environ[env_name] = '{};{}'.format(os.environ[env_name], env_value)


def set_env(env_name, env_value):
    """
    Sets given environment variable with the given value
    :param env_name: str
    :param env_value: str
    """

    os.environ[env_name] = env_value


def update_maya_usd_environment():
    """
    Updates current Python Maya environment to setup Maya USD plugin
    """

    from tpDcc.libs.python import path

    usd_dcc_root_path = get_usd_dcc_path()
    if not usd_dcc_root_path or not os.path.isdir(usd_dcc_root_path):
        LOGGER.warning('Impossible to setup Maya USD environment. Maya USD is not available!')
        return

    maya_usd_lib = path.clean_path(os.path.join(usd_dcc_root_path, 'lib'))
    maya_usd_python = path.clean_path(os.path.join(maya_usd_lib, 'python'))
    maya_usd_plugins = path.clean_path(os.path.join(usd_dcc_root_path, 'plugin'))

    maya_usd_plugin_name = path.clean_path(os.path.join(maya_usd_lib, 'usd'))
    maya_adsk_plugin_path = path.clean_path(os.path.join(maya_usd_plugins, 'adsk'))
    maya_adsk_scripts_path = path.clean_path(os.path.join(maya_adsk_plugin_path, 'scripts'))
    maya_adsk_usd_plugin_name = path.clean_path(os.path.join(maya_adsk_plugin_path, 'plugin'))

    add_to_env('PATH', maya_usd_lib)
    add_to_env('PYTHONPATH', maya_usd_python)
    add_to_env('PXR_PLUGINPATH_NAME', maya_usd_plugin_name)
    add_to_env('MAYA_SCRIPT_PATH', maya_adsk_scripts_path)
    add_to_env('MAYA_PLUG_IN_PATH', maya_adsk_usd_plugin_name)
    set_env('VP2_RENDER_DELEGATE_PROXY', '1')

    return True


def update_pixar_usd_environment():
    """
    Updates current Python Maya environment to setup Pixar USD plugin
    """

    from tpDcc.libs.python import path

    usd_pixar_path = get_usd_path()
    if not usd_pixar_path or not os.path.isdir(usd_pixar_path):
        LOGGER.warning('Impossible to setup Pixar USD environment. USD is not available!')
        return

    usd_bin = path.clean_path(os.path.join(usd_pixar_path, 'bin'))
    usd_lib = path.clean_path(os.path.join(usd_pixar_path, 'lib'))
    usd_lib_python = path.clean_path(os.path.join(usd_lib, 'python'))
    add_to_env('PYTHONPATH', usd_lib_python)
    add_to_env('PATH', usd_bin)
    add_to_env('PATH', usd_lib)

    return True


def update_hydra_usd_environment():
    """
    Updates current Python Maya environment to setup Animal Logic USD plugin
    """

    usd_dcc_root_path = get_usd_dcc_path()
    if not usd_dcc_root_path or not os.path.isdir(usd_dcc_root_path):
        LOGGER.warning('Impossible to setup Hydra USD environment. Hydra USD is not available!')
        return

    mtoah_root_path = os.path.join(usd_dcc_root_path, 'lib')
    mtoah_maya_plugin = os.path.join(mtoah_root_path, 'maya')
    add_to_env('MAYA_PLUG_IN_PATH', mtoah_maya_plugin)

    return True


def update_usd_environments(load_plugins=True):
    """
    Updates current Python Maya environment to setup Maya USD
    :param load_plugins: bool
    """

    import tpDcc as tp

    usd_root_path = get_usd_path()
    if not usd_root_path or not os.path.isdir(usd_root_path):
        LOGGER.warning('Impossible to setup USD Maya environment. USD is not available!')
        return

    usd_bin_path = os.path.join(usd_root_path, 'bin')
    usd_lib_path = os.path.join(usd_root_path, 'lib')
    usd_python_lib_path = os.path.join(usd_lib_path, 'python')
    add_to_env('PYTHONPATH', usd_python_lib_path)
    add_to_env('PATH', usd_bin_path)
    add_to_env('PATH', usd_lib_path)

    valid_usd_maya = update_maya_usd_environment()
    # We must import pixar usd the last, otherwise we will have problems due to Python import orders
    valid_pixar_usd = update_pixar_usd_environment()
    valid_hydra = update_hydra_usd_environment()

    if load_plugins:
        if valid_usd_maya and valid_pixar_usd:
            tp.Dcc.load_plugin('mayaUsdPlugin.mll')
        if valid_hydra:
            tp.Dcc.load_plugin('mtoh.mll')
