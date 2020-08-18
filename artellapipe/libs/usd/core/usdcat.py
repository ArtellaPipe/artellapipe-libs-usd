# ! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains functions related with Pixar USD usdcat application
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import os
import logging
import subprocess

from tpDcc.libs.python import fileio

from artellapipe.libs.usd.core import usdpaths

LOGGER = logging.getLogger('artellapipe-libs-usd')


def get_usd_cat_path():
    """
    Returns path to USD cat executable
    :return: str
    """

    platform_path = usdpaths.get_platform_path()

    usd_view_path = os.path.join(platform_path, 'pixar', 'bin', 'usdcat')

    return usd_view_path


def convert_usd_file(in_file_path, new_format, clean_original=False):

    if not new_format.startswith('.'):
        new_format = '.{}'.format(new_format)
    simple_format = new_format[1:]

    usdcat_app = get_usd_cat_path()

    in_file_name = os.path.splitext(os.path.basename(in_file_path))[0]
    out_file_name = '{}{}'.format(in_file_name, new_format)
    out_file_path = os.path.join(os.path.dirname(in_file_path), out_file_name)

    # p = subprocess.Popen(
    #     '"{}" -o "{}" --usdFormat {} "{}"'.format(usdcat_app, out_file_path, simple_format, in_file_path))

    # p = subprocess.Popen(
    #     ['python.exe', usdcat_app, '-o', out_file_path, '--usdFormat', simple_format, in_file_path],
    #     stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    p = subprocess.Popen(
        ['python.exe', usdcat_app, '-o', out_file_path, in_file_path],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    output, error = p.communicate()
    if error:
        LOGGER.error('>>> usdcat: {}'.format(error))
        return False

    if clean_original:
        fileio.delete_file(in_file_path)

    return True
