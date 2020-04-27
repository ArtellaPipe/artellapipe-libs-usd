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


def update_arnold_usd_environment():
    """
    Updates current Python Maya environmetn to setup Arnold USD
    """

    import tpDcc as tp
    from tpDcc.libs.python import path, osplatform

    if not tp.is_maya():
        return False

    arnold_usd_path = get_arnold_path()
    if not arnold_usd_path or not os.path.isdir(arnold_usd_path):
        LOGGER.warning('Impossible to setup Arnold USD environment. Arnold USD is not available!')
        return

    arnold_procedural_plugin = path.clean_path(os.path.join(arnold_usd_path, 'procedural'))
    arnold_libs_path = path.clean_path(os.path.join(arnold_usd_path, 'lib'))
    arnold_usd_bin = path.clean_path(os.path.join(arnold_usd_path, 'bin'))
    arnold_python_lib = path.clean_path(os.path.join(arnold_libs_path, 'python'))
    arnold_plugin_path = path.clean_path(os.path.join(arnold_usd_path, 'plugin'))
    arnold_usd_lib = path.clean_path(os.path.join(arnold_libs_path, 'usd'))

    add_to_env('ARNOLD_PLUGIN_PATH', arnold_procedural_plugin)
    add_to_env('PYTHONPATH', arnold_python_lib)
    add_to_env('PXR_PLUGINPATH_NAME', arnold_plugin_path)
    add_to_env('PXR_PLUGINPATH_NAME', arnold_usd_lib)

    platform_name = osplatform.get_platform().lower()
    if platform_name == 'windows':
        add_to_env('PATH', arnold_usd_bin)
        add_to_env('PATH', arnold_libs_path)
    elif platform_name == 'linux':
        add_to_env('LD_LIBRARY_PATH', arnold_usd_bin)
        add_to_env('LD_LIBRARY_PATH', arnold_libs_path)
    elif platform_name == 'macos':
        add_to_env('DYLD_LIBRARY_PATH', arnold_usd_bin)
        add_to_env('DYLD_LIBRARY_PATH', arnold_libs_path)


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

    if tp.is_maya():
        update_arnold_usd_environment()

    if load_plugins:
        if valid_usd_maya and valid_pixar_usd:
            tp.Dcc.load_plugin('mayaUsdPlugin.mll')
        if valid_hydra:
            tp.Dcc.load_plugin('mtoh.mll')
