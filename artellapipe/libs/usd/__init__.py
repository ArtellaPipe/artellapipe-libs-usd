#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialization module for artellapipe-libs-usd
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import os
import sys
import logging

import tpDcc as tp

import artellapipe.register
from artellapipe.libs.usd.core import usdpaths

LOGGER = logging.getLogger('artellapipe-libs-usd')


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

    usd_dcc_root_path = usdpaths.get_usd_dcc_path()
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


def update_al_usd_environment():
    """
    Updates current Python environment to setup Animal Logic (AL) USD plugin
    """

    from tpDcc.libs.python import path

    usd_dcc_root_path = usdpaths.get_usd_dcc_path()
    if not usd_dcc_root_path or not os.path.isdir(usd_dcc_root_path):
        LOGGER.warning('Impossible to setup AL USD environment. Maya USD is not available!')
        return

    maya_usd_plugins = path.clean_path(os.path.join(usd_dcc_root_path, 'plugin'))
    maya_al_plugin_path = path.clean_path(os.path.join(maya_usd_plugins, 'al'))
    maya_al_lib_path = path.clean_path(os.path.join(maya_al_plugin_path, 'lib'))
    maya_al_lib_python_path = path.clean_path(os.path.join(maya_al_lib_path, 'python'))
    maya_al_plugin_name = path.clean_path(os.path.join(maya_al_plugin_path, 'plugin'))
    maya_al_usd_lib_path = path.clean_path(os.path.join(maya_al_lib_path, 'usd'))

    add_to_env('PATH', maya_al_lib_path)
    add_to_env('PYTHONPATH', maya_al_lib_python_path)
    add_to_env('MAYA_PLUG_IN_PATH', maya_al_plugin_name)
    add_to_env('PXR_PLUGINPATH_NAME', maya_al_plugin_name)
    add_to_env('PXR_PLUGINPATH_NAME', maya_al_usd_lib_path)
    set_env('MAYA_WANT_UFE_SELECTION', '1')

    return True


def update_pixar_maya_usd_environment():
    """
    Updates current Python environment to setup Pixar Maya USD plugin
    """

    import tpDcc as tp
    from tpDcc.libs.python import path

    if not tp.is_maya():
        return False

    usd_dcc_root_path = usdpaths.get_usd_dcc_path()
    if not usd_dcc_root_path or not os.path.isdir(usd_dcc_root_path):
        LOGGER.warning('Impossible to setup Pixar USD environment. Maya USD is not available!')
        return

    maya_usd_plugins = path.clean_path(os.path.join(usd_dcc_root_path, 'plugin'))
    pixar_plugin_path = path.clean_path(os.path.join(maya_usd_plugins, 'pxr'))
    maya_pixar_lib_path = path.clean_path(os.path.join(pixar_plugin_path, 'lib'))
    maya_pixar_lib_python_path = path.clean_path(os.path.join(maya_pixar_lib_path, 'python'))
    maya_pixar_plugin_path = path.clean_path(os.path.join(pixar_plugin_path, 'maya'))
    maya_pixar_plugin_lib_path = path.clean_path(os.path.join(maya_pixar_plugin_path, 'lib'))
    maya_pixar_plugin_plugin_path = path.clean_path(os.path.join(maya_pixar_plugin_path, 'plugin'))
    maya_pixar_plugin_lib_usd_path = path.clean_path(os.path.join(maya_pixar_plugin_lib_path, 'usd'))
    maya_pixar_plugin_resources = path.clean_path(os.path.join(maya_pixar_plugin_lib_usd_path, 'usdMaya', 'resources'))
    maya_pixar_surface_resources = path.clean_path(
        os.path.join(maya_pixar_plugin_plugin_path, 'pxrUsdPreviewSurface', 'resources'))

    add_to_env('PYTHONPATH', maya_pixar_lib_python_path)
    add_to_env('PATH', maya_pixar_plugin_lib_path)
    add_to_env('XBMLANGPATH', maya_pixar_plugin_resources)
    add_to_env('XBMLANGPATH', maya_pixar_surface_resources)
    add_to_env('MAYA_SCRIPT_PATH', maya_pixar_plugin_resources)
    add_to_env('MAYA_SCRIPT_PATH', maya_pixar_surface_resources)
    add_to_env('MAYA_PLUG_IN_PATH', maya_pixar_plugin_plugin_path)
    add_to_env('PXR_PLUGINPATH_NAME', maya_pixar_plugin_lib_usd_path)

    return True


def update_qt_usd_environment():
    """
    Updates current Python environment to setup Qt USD
    """

    from tpDcc.libs.python import path

    usd_qt_path = usdpaths.get_usd_qt_path()
    if not usd_qt_path or not os.path.isdir(usd_qt_path):
        LOGGER.warning('Impossible to setup Qt USD environment. Qt USD is not available!')
        return False

    qt_lib_python = path.clean_path(os.path.join(usd_qt_path, 'lib', 'python'))
    add_to_env('PYTHONPATH', qt_lib_python)

    return True


def update_pixar_usd_environment():
    """
    Updates current Python Maya environment to setup Pixar USD plugin
    """

    from tpDcc.libs.python import path

    usd_pixar_path = usdpaths.get_usd_path()
    if not usd_pixar_path or not os.path.isdir(usd_pixar_path):
        LOGGER.warning('Impossible to setup Pixar USD environment. USD is not available!')
        return False

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

    arnold_usd_path = usdpaths.get_arnold_path()
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

    return True


def update_hydra_usd_environment():
    """
    Updates current Python Maya environment to setup Animal Logic USD plugin
    """

    usd_dcc_root_path = usdpaths.get_usd_dcc_path()
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

    usd_root_path = usdpaths.get_usd_path()
    if not usd_root_path or not os.path.isdir(usd_root_path):
        LOGGER.warning('Impossible to setup USD Maya environment. USD is not available!')
        return

    valid_maya_pixar = update_pixar_maya_usd_environment()
    valid_usd_maya = update_maya_usd_environment()
    valid_usd_al = update_al_usd_environment()
    valid_qt = update_qt_usd_environment()
    valid_hydra = update_hydra_usd_environment()
    valid_arnold = update_arnold_usd_environment()

    # We must import pixar usd the last, otherwise we will have problems due to Python import orders
    valid_pixar_usd = update_pixar_usd_environment()

    if load_plugins:
        if valid_maya_pixar:
            tp.Dcc.load_plugin('pxrUsd.mll')
        if valid_usd_maya and valid_pixar_usd:
            tp.Dcc.load_plugin('mayaUsdPlugin.mll')
        if valid_usd_al:
            tp.Dcc.load_plugin('AL_USDMayaPlugin.mll')
        if valid_hydra:
            tp.Dcc.load_plugin('mtoh.mll')


def init(*args, **kwargs):
    LOGGER.info('Initializing USD libraries ...')
    try:
        update_usd_environments(load_plugins=True)

        from artellapipe.libs.usd.core import usdpxr
        artellapipe.register.register_class('UsdPixar', usdpxr.AbstractUsdPixar)

        if tp.is_maya():
            from artellapipe.libs.usd.maya import usdpxr as maya_usdpxr
            artellapipe.register.register_class('UsdPixar', maya_usdpxr.MayaUsdPixar)

    except Exception as exc:
        LOGGER.warning('Error while initializing USD libraries: {}!'.format(exc))
        return

    LOGGER.info('USD libraries initialized successfully!')
