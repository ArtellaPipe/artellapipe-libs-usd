#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains utilities functions to work with USD layers
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from pxr import Sdf


def create_new_layer(file_path, args_dict=None):
    """
    Creates a new Usd Layer
    :param file_path: str, layer file path to open
    :param args_dict: dict with custom attributes for the layer
    :return:
    """

    args_dict = args_dict or dict()
    new_layer = Sdf.Layer.CreateNew(file_path, args=args_dict)

    return new_layer
