#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains functions related Pixar USD (pxr)
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import os

import tpDcc as tp
import tpDcc.dccs.maya as maya


class UsdReferenceAssemblyRepresentations(object):
    CARDS = 'Cards'
    COLLAPSED = 'Collapsed'
    EXPANDED = 'Expanded'
    FULL = 'Full'
    PLAYBACK = 'Playback'


def import_usd_file(file_path):
    """
    Imports a new USD file using Pixar USD Maya Importer (pxrUsdImport)
    :param file_path: str, file path of the USD to import
    :return:
    """

    if not file_path or not os.path.isfile(file_path):
        return False

    file_path_name = os.path.splitext(os.path.basename(file_path))[0]

    return maya.cmds.file(
        file_path, i=True, type='pxrUsdImport', ignoreVersion=True, ra=True, mergeNamespacesOnClash=False,
        namespace=file_path_name, options=';shadingMode=displayColor;readAnimData=0;useAsAnimationCache=0;'
                                          'assemblyRep=Collapsed;startTime=0;endTime=0;useCustomFrameRange=0',
        pr=True, importFrameRate=True, importTimeRange='override')


def create_usd_reference_assembly(file_path, active_representation=UsdReferenceAssemblyRepresentations.FULL):
    """
    Creates a new Pixar USD Maya Reference Assembly node (pxrUsdReferenceAssembly) pointing to the given USD file path
    :param file_path: str
    :param active_representation: str, UsdReferenceAssemblyRepresentations
    :return:
    """

    if not file_path or not os.path.isfile(file_path):
        return False

    file_path_name = os.path.splitext(os.path.basename(file_path))[0]

    assembly_node = maya.cmds.assembly(name=file_path_name, type='pxrUsdReferenceAssembly')
    tp.Dcc.set_attribute_value(assembly_node, 'filePath', file_path)
    maya.cmds.assembly(assembly_node, active=active_representation, edit=True)

    return assembly_node


def set_usd_reference_assembly_representation(usd_reference_assembly_node, representation):
    """
    Sets the representation type used by given Pixar USD Maya Reference Assembly node (pxrUsdReferenceAssembly)
    :param usd_reference_assembly_node: str, UsdReferenceAssemblyRepresentations
    :param representation:
    :return:
    """

    return maya.cmds.assembly(usd_reference_assembly_node, active=representation, edit=True)
