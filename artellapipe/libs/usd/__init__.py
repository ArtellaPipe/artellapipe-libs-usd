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


def get_usd_path():
    """
    Returns path where USD plugin is located for current DCC version
    :return: str
    """

    import tpDcc as tp
    from tpDcc.libs.python import path, osplatform

    externals_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'externals')
    if not externals_dir or not os.path.isdir(externals_dir):
        LOGGER.warning('No externals directory found: "{}"'.format(externals_dir))
        return

    platform_name = osplatform.get_platform().lower()
    os_architecture = osplatform.get_architecture()
    dcc_name = tp.Dcc.get_name()
    dcc_version = tp.Dcc.get_version_name()

    usd_path = path.clean_path(
        os.path.join(externals_dir, platform_name, os_architecture, 'usd', dcc_name, dcc_version))
    if not os.path.isdir(usd_path):
        LOGGER.warning('No USD executable folder found: "{}"'.format(usd_path))
        return None

    return usd_path


def add_to_env(env_name, env_value):
    """
    Adds given value to the given environment variable
    :param env_name: str
    :param env_value: str
    """

    if env_name == 'PYTHONPATH':
        if env_value not in sys.path:
            sys.path.append(env_value)
    else:
        if not os.environ.get(env_name):
            os.environ[env_name] = env_value
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


def update_pixar_usd_maya_environment():
    """
    Updates current Python Maya environment to setup Pixar USD plugin
    :param load_plugin: bool
    """

    usd_root_path = get_usd_path()
    if not usd_root_path or not os.path.isdir(usd_root_path):
        LOGGER.warning('Impossible to setup Pixar USD Maya environment. Pixar USD Maya is not available!')
        return

    pxr_root_path = os.path.join(usd_root_path, 'plugin', 'pxr')
    pxr_python_path = os.path.join(pxr_root_path, 'lib', 'python')
    pxr_maya_path = os.path.join(pxr_root_path, 'maya', 'lib')
    pxr_maya_resources = os.path.join(pxr_maya_path, 'usd', 'usdMaya', 'resources')
    pxr_plugin_path = os.path.join(pxr_root_path, 'maya', 'plugin')
    pxr_usd_lib = os.path.join(pxr_root_path, 'lib', 'usd')
    add_to_env('PYTHONPATH', pxr_python_path)
    add_to_env('PATH', pxr_maya_path)
    add_to_env('XBMLANGPATH', pxr_maya_resources)
    add_to_env('MAYA_SCRIPT_PATH', pxr_maya_resources)
    add_to_env('MAYA_PLUG_IN_PATH', pxr_plugin_path)
    add_to_env('PXR_PLUGINPATH_NAME', pxr_usd_lib)

    return True


def update_usd_maya_environment():
    """
    Updates current Python Maya environment to setup Maya USD plugin
    :param load_plugin: bool
    """

    usd_root_path = get_usd_path()
    if not usd_root_path or not os.path.isdir(usd_root_path):
        LOGGER.warning('Impossible to setup USD Maya environment. USD Maya is not available!')
        return

    maya_usd_lib = os.path.join(usd_root_path, 'lib')
    maya_usd_python = os.path.join(maya_usd_lib, 'python')
    maya_usd_plugin_name = os.path.join(maya_usd_lib, 'usd')
    add_to_env('PATH', maya_usd_lib)
    add_to_env('PYTHONPATH', maya_usd_python)
    add_to_env('PXR_PLUGINPATH_NAME', maya_usd_plugin_name)
    set_env('VP2_RENDER_DELEGATE_PROXY', '1')

    return True


def update_usd_autodesk_maya_environment():
    """
    Updates current Python Maya environment to setup Maya USD plugin
    :param load_plugin: bool
    """

    usd_root_path = get_usd_path()
    if not usd_root_path or not os.path.isdir(usd_root_path):
        LOGGER.warning('Impossible to setup Autodesk USD Maya environment. Autodesk USD is not available!')
        return

    adsk_usd_plugin_root = os.path.join(usd_root_path, 'plugin', 'adsk')
    adsk_usd_plugin_path = os.path.join(adsk_usd_plugin_root, 'plugin')
    add_to_env('MAYA_PLUG_IN_PATH', adsk_usd_plugin_path)

    return True


def update_pixar_usd_environment():
    """
    Updates current Python Maya environment to setup Pixar USD plugin
    :param load_plugin: bool
    """

    usd_root_path = get_usd_path()
    if not usd_root_path or not os.path.isdir(usd_root_path):
        LOGGER.warning('Impossible to setup Pixar USD environment. USD is not available!')
        return

    usd_bin = os.path.join(usd_root_path, 'pixar', 'bin')
    usd_lib = os.path.join(usd_root_path, 'pixar', 'lib')
    usd_lib_python = os.path.join(usd_lib, 'python')
    add_to_env('PYTHONPATH', usd_lib_python)
    add_to_env('PATH', usd_bin)
    add_to_env('PATH', usd_lib)

    return True


def update_animal_logic_usd_environment():
    """
    Updates current Python Maya environment to setup Animal Logic USD plugin
    :param load_plugin: bool
    """

    usd_root_path = get_usd_path()
    if not usd_root_path or not os.path.isdir(usd_root_path):
        LOGGER.warning('Impossible to setup Animal Logic USD environment. Animal Logic USD is not available!')
        return

    al_usd_plugin_root = os.path.join(usd_root_path, 'plugin', 'al')
    al_usd_plugin_lib = os.path.join(al_usd_plugin_root, 'lib')
    al_usd_plugin_python = os.path.join(al_usd_plugin_lib, 'python')
    al_usd_plugin_usd = os.path.join(al_usd_plugin_lib, 'usd')
    al_usd_plugin_name = os.path.join(al_usd_plugin_root, 'plugin')
    add_to_env('PYTHONPATH', al_usd_plugin_python)
    add_to_env('PATH', al_usd_plugin_lib)
    add_to_env('MAYA_PLUG_IN_PATH', al_usd_plugin_name)
    add_to_env('PXR_PLUGINPATH_NAME', al_usd_plugin_usd)
    add_to_env('PXR_PLUGINPATH_NAME', al_usd_plugin_name)
    set_env('MAYA_WANT_UFE_SELECTION', '1')

    return True


def update_hydra_usd_environment():
    """
    Updates current Python Maya environment to setup Animal Logic USD plugin
    :param load_plugin: bool
    """

    usd_root_path = get_usd_path()
    if not usd_root_path or not os.path.isdir(usd_root_path):
        LOGGER.warning('Impossible to setup Hydra USD environment. Hydra USD is not available!')
        return

    mtoah_root_path = os.path.join(usd_root_path, 'lib')
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

    valid_pixar_usd_maya = update_pixar_usd_maya_environment()
    valid_usd_maya = update_usd_maya_environment()
    valid_usd_autodesk_maya = update_usd_autodesk_maya_environment()
    # We must import pixar usd the last, otherwise we will have problems due to Python import orders
    valid_pixar_usd = update_pixar_usd_environment()
    valid_animal_logic_usd = update_animal_logic_usd_environment()
    valid_hydra = update_hydra_usd_environment()

    if load_plugins:
        if valid_pixar_usd and valid_usd_maya:
            tp.Dcc.load_plugin('pxrUsd.mll')
            tp.Dcc.load_plugin('pxrUsdPreviewSurface.mll')
            # tp.Dcc.load_plugin('mayaUsdPlugin.mll')
        if valid_usd_autodesk_maya:
            tp.Dcc.load_plugin('mayaUsdPlugin.mll')
        if valid_animal_logic_usd:
            tp.Dcc.load_plugin('AL_USDMayaPlugin.mll')
            tp.Dcc.load_plugin('AL_USDMayaPxrTranslators.mll')
        if valid_hydra:
            tp.Dcc.load_plugin('mtoh.mll')
