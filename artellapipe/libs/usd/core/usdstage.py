#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains utilities functions to work with USD stages
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import os

from pxr import Usd, UsdGeom, Sdf

from artellapipe.libs.usd.core import usdutils


def create_new_stage(stage_name, stage_extension=usdutils.UsdFormats.Text):
    """
    Creates a new USD stage with the given name and extension
    :param stage_name: str
    :param stage_extension: str
    :return: Usd.Stage
    """

    if not stage_extension.startswith('.'):
        stage_extension = '.{}'.format(stage_extension)

    stage_name = '{}{}'.format(stage_name, stage_extension)
    new_stage = Usd.Stage.CreateNew(stage_name)

    return new_stage


def print_stage(stage):
    """
    Prints stage root contents into output
    :param stage: str
    """

    print(stage.GetRootLayer().ExportToString())


def get_root_layer(stage):
    """
    Returns given stage root layer
    :param stage: Usd.Stage
    :return: Usd.Layer
    """

    return stage.GetRootLayer()


def save_stage(stage, file_path=None):
    """
    Saves given stage data into file path
    :param stage: Usd.Stage
    :param file_path: str
    """

    return stage.Save(file_path) if file_path else stage.Save()


def export_stage(stage, file_path):
    """
    Exports given stage into file path
    You can pass a different extension to transition between different serialization formats
    :param stage: Usd.Stage
    :param file_path: str
    :return:
    """

    return stage.Export(file_path)


def define_transform_prim(stage, prim_path, get_as_prim=False):
    """
    Defines a new USD transforms prim in the given path
    :param stage: Usd.Stage
    :param prim_path: str
    :param get_as_prim: bool
    :return: Usd.XForm or Usd.Prim
    """

    if not prim_path.startswith('/'):
        prim_path = '/{}'.format(prim_path)

    xform = UsdGeom.Xform.Define(stage, prim_path)

    if get_as_prim:
        xform_prim = stage.GetPrimAtPath(prim_path)
        return xform_prim

    return xform


def set_default_prim(stage, prim):
    """
    Sets given prim as the default prim in the given stage
    :param stage: Usd.Stage
    :param prim: Usd.Prim
    """

    return stage.SetDefaultPrim(prim)


def add_layer(stage, layer_file=None):
    """
    Adds a new composition layer into given stage
    :param stage: Usd.Stage
    :param layer_file: str
    :return: Usd.Layer
    """

    root_layer = stage.GetRootLayer()

    if not layer_file or not os.path.isfile(layer_file):
        Sdf.Layer.CreateNew(layer_file)

    root_layer.subLayerPaths.append(layer_file)

