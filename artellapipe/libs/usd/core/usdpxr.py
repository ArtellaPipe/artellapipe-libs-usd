#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains utilities functions to work with Pixar USD
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from tpDcc.libs.python import decorators
from artellapipe.libs.usd.core import usdutils


class AbstractUsdPixar(object):

    @classmethod
    @decorators.abstractmethod
    def is_usd_pixar_available(cls):
        """
        Returns whether or not Pixar Plugin functionality is available or not
        :return: bool
        """

        raise NotImplementedError('load_arnold_plugin function for "{}" is not implemented!'.format(cls.__name__))

    @classmethod
    @decorators.abstractmethod
    def import_usd_file(cls, file_path):
        """
        Imports a new USD file using Pixar USD Maya Importer (pxrUsdImport)
        :param file_path: str, file path of the USD to import
        :return:
        """

        raise NotImplementedError('import_usd_file function for "{}" is not implemented!'.format(cls.__name__))

    @classmethod
    @decorators.abstractmethod
    def export_usd_file(cls, file_directory, file_name, extension=usdutils.UsdFormats.Text, export_selection=False):
        """
        Exports a USD file using Pixar USD Maya Importer (pxrUsdExport)
        :param file_directory:
        :param file_name:
        :param extension:
        :param export_selection:
        :return:
        """

        raise NotImplementedError('export_usd_file function for "{}" is not implemented!'.format(cls.__name__))
