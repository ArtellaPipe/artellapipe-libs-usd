#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains functions related with Pixar USD usdview application
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import os
import sys
import logging
import subprocess

from artellapipe.libs.usd.core import usdpaths

LOGGER = logging.getLogger('artellapipe-libs-usd')


def get_usd_view_path():
    """
    Returns path to USD view executable
    :return: str
    """

    platform_path = usdpaths.get_platform_path()

    usd_view_path = os.path.join(platform_path, 'pixar', 'bin', 'usdview')

    return usd_view_path


def get_usd_view_python_libs_path():

    externals_path = usdpaths.get_usd_externals()

    if sys.version[0] == '2':
        usd_view_py_libs_path = os.path.join(externals_path, 'python', '2')
    else:
        usd_view_py_libs_path = os.path.join(externals_path, 'python', '3')

    return usd_view_py_libs_path


def open_usd_file(usd_file_path):
    """
    Opens given USD file in USD viewer (usdview)
    :param usd_file_path: str
    :return: bool
    """

    if not usd_file_path or not os.path.isfile(usd_file_path):
        LOGGER.warning('Given USD file path does not exists: {}!'.format(usd_file_path))
        return False

    usd_view_path = get_usd_view_path()
    if not os.path.exists(usd_view_path):
        LOGGER.warning(
            'usdview path does not exists: {}. Impossible to open USD file!'.format(usd_view_path))
        return False

    usd_view_python_libs_path = get_usd_view_python_libs_path()
    if not os.path.isdir(usd_view_python_libs_path):
        LOGGER.warning(
            'No usdview Pythyon libs directory found. usdview cannot be opened or usdview OpenGL can be disabled')
        usd_view_python_libs_path = None

    pixar_usd_binaries_path = usdpaths.get_pixar_usd_binaries_path()
    if not pixar_usd_binaries_path:
        LOGGER.warning(
            'No Pixar USD binaries path found: "{}". Impossible to launch usdview'.format(pixar_usd_binaries_path))
        return False

    pixar_usd_libraries_path = usdpaths.get_pixar_usd_libraries_path()
    if not pixar_usd_libraries_path:
        LOGGER.warning(
            'No Pixar USD libraries path found: "{}". Impossible to launch usdview'.format(pixar_usd_libraries_path))
        return False

    # Dictionary that contains the environment configuration that will be used by usdview instance
    usd_view_env = dict()

    usd_view_env['PATH'] = r'{};{}'.format(pixar_usd_binaries_path, pixar_usd_libraries_path)

    pixar_usd_python_libs_path = usdpaths.get_pixar_usd_python_libs_path()
    if pixar_usd_python_libs_path and os.path.isdir(pixar_usd_python_libs_path):
        if usd_view_python_libs_path and os.path.isdir(usd_view_python_libs_path):
            usd_view_env['PYTHONPATH'] = r'{};{}'.format(pixar_usd_python_libs_path, usd_view_python_libs_path)
        else:
            usd_view_env['PYTHONPATH'] = r'{}'.format(pixar_usd_python_libs_path)
    else:
        if usd_view_python_libs_path and os.path.isdir(usd_view_python_libs_path):
            usd_view_env['PYTHONPATH'] = r'{}'.format(usd_view_python_libs_path)

    p = subprocess.Popen(
        ['python.exe', usd_view_path, usd_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=usd_view_env)
    output, error = p.communicate()
    if error:
        LOGGER.error('>>> usdview: {}'.format(error))

    return True
