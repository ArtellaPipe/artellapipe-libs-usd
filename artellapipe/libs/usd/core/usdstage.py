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

from tpDcc.libs.python import python

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


def open_stage(file_path):
    """
    Opens given USD files as an USD stage
    :param file_path: str
    :return: Usd.Stage
    """

    return Usd.Stage.Open(file_path)


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
        return xform.GetPrim()

    return xform


def get_prim_at_path(stage, prim_path):
    """
    Returns Usd Prim at given path
    :param stage: Usd.Stage
    :param prim_path: str
    :return: Usd.Prim or None
    """

    if not prim_path.startswith('/'):
        prim_path = '/{}'.format(prim_path)

    return stage.GetPrimAtPath(Sdf.Path(prim_path))


def set_default_prim(stage, prim):
    """
    Sets given prim as the default prim in the given stage
    :param stage: Usd.Stage
    :param prim: Usd.Prim
    """

    if python.is_string(prim):
        prim = get_prim_at_path(stage, prim)

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


def add_reference(prim, file_path, update_default_prim=True):
    """
    Adds a new reference to the given prim
    :param prim: Usd.Prim
    :param file_path: str
    :param update_default_prim: bool or None or str
    :return:
    """

    if os.path.isfile(file_path):
        referenced_stage = Usd.Stage.Open(file_path)
    else:
        referenced_stage = Usd.Stage.CreateNew(file_path)
    reference_stage_prim = referenced_stage.DefinePrim(prim.GetPath())
    if update_default_prim:
        if isinstance(update_default_prim, Usd.Prim):
            referenced_stage.SetDefaultPrim(update_default_prim)
        else:
            referenced_stage.SetDefaultPrim(reference_stage_prim)

    referenced_stage.GetRootLayer().Save()
    prim.GetReferences().AddReference(file_path)
