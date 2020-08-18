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
import logging

import mayaUsd.lib as mayaUsdLib

import tpDcc as tp
import tpDcc.dccs.maya as maya

from artellapipe.libs.usd.core import usdutils

LOGGER = logging.getLogger('artellapipe-libs-usd')


class UsdReferenceAssemblyRepresentations(object):
    CARDS = 'Cards'
    COLLAPSED = 'Collapsed'
    EXPANDED = 'Expanded'
    FULL = 'Full'
    PLAYBACK = 'Playback'


class MayaUsdPixar(object):

    @staticmethod
    def load_usd_pixar_plugin():
        """
        Forces the loading of the Pixar Plugin if it is not already loaded
        """

        if not tp.Dcc.is_plugin_loaded('mayaUsdPlugin.mll'):
            tp.Dcc.load_plugin('mayaUsdPlugin.mll')

    @classmethod
    def is_usd_pixar_available(cls):
        """
        Returns whether or not Pixar Plugin functionality is available or not
        :return: bool
        """

        return tp.Dcc.is_plugin_loaded('mayaUsdPlugin.mll')

    @classmethod
    def import_usd_file(cls, file_path):
        """
        Imports a new USD file using Pixar USD Maya Importer (pxrUsdImport)
        :param file_path: str, file path of the USD to import
        :return:
        """

        if not file_path or not os.path.isfile(file_path):
            LOGGER.warning('Given USD file path to import is not valid: "{}"!'.format(file_path))
            return False

        file_path_name = os.path.splitext(os.path.basename(file_path))[0]

        if not MayaUsdPixar.is_usd_pixar_available():
            LOGGER.warning('Pixar Plugin is not available. Impossible to import USD file using Pixar USD importer.')
            return False

        return maya.cmds.file(
            file_path, i=True, type='pxrUsdImport', ignoreVersion=True, ra=True, mergeNamespacesOnClash=False,
            namespace=file_path_name, options=';shadingMode=displayColor;readAnimData=0;useAsAnimationCache=0;'
                                              'assemblyRep=Collapsed;startTime=0;endTime=0;useCustomFrameRange=0',
            pr=True, importFrameRate=True, importTimeRange='override')

    @classmethod
    def export_usd_file(cls, file_directory, file_name, extension=usdutils.UsdFormats.Text, export_selection=False):
        """
        Exports a USD file using Pixar USD Maya Importer (pxrUsdExport)
        :param file_directory:
        :param file_name:
        :param extension:
        :param export_selection:
        :return:
        """

        if not file_directory or not os.path.isdir(file_directory):
            LOGGER.warning(
                'Impossible to export USD file. Export directory is not valid or does not exists: "{}"'.format(
                    file_directory))
            return False

        if not extension.startswith('.'):
            extension = '.{}'.format(extension)

        file_path_name = '{}{}'.format(file_name, extension)
        file_path = os.path.join(file_directory, file_path_name)

        if not MayaUsdPixar.is_usd_pixar_available():
            LOGGER.warning('Pixar Plugin is not available. Impossible to export USD file using Pixar USD exporter.')
            return False

        return maya.cmds.file(
            file_path, typ='pxrUsdExport', pr=True, es=export_selection, ea=not export_selection, force=True,
            options=';shadingMode=none;materialsScopeName=Looks;exportDisplayColor=0;exportRefsAsInstanceable=0;'
                    'exportUVs=1;exportMaterialCollections=0;materialCollectionsPath=;exportCollectionBasedBindings=0;'
                    'exportColorSets=1;exportReferenceObjects=0;renderableOnly=1;filterTypes=;defaultCameras=0;'
                    'renderLayerMode=defaultLayer;mergeTransformAndShape=1;exportInstances=1;'
                    'defaultMeshScheme=catmullClark;exportSkels=none;exportSkin=none;exportVisibility=1;'
                    'stripNamespaces=0;animation=0;eulerFilter=0;startTime=1;endTime=1;frameStride=1;'
                    'parentScope=;compatibility=none', de=False
        )

    @staticmethod
    def create_usd_reference_assembly(file_path, active_representation=UsdReferenceAssemblyRepresentations.COLLAPSED):
        """
        Creates a new Pixar USD Maya Reference Assembly node (pxrUsdReferenceAssembly)
        pointing to the given USD file path
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

        usd_prim = mayaUsdLib.GetPrim(assembly_node)
        variant_sets = usd_prim.GetVariantSets()
        variant_set_names = variant_sets.GetNames()

        for variant_set_name in variant_set_names:
            usd_variant = usd_prim.GetVariantSet(variant_set_name)
            if not usd_variant:
                continue
            usd_variant_choices = usd_variant.GetVariantNames()
            variant_attr = 'usdVariantSet_%s' % variant_set_name
            if not tp.Dcc.attribute_exists(assembly_node, variant_attr):
                maya.cmds.addAttr(assembly_node, ln=variant_attr, dt='string', internalSet=True)
            if not usd_variant_choices:
                continue
            usd_variant_value = usd_variant_choices[-1]
            maya.cmds.setAttr('{}.{}'.format(assembly_node, variant_attr), usd_variant_value, type='string')

        return assembly_node

    @staticmethod
    def set_usd_reference_assembly_representation(usd_reference_assembly_node, representation):
        """
        Sets the representation type used by given Pixar USD Maya Reference Assembly node (pxrUsdReferenceAssembly)
        :param usd_reference_assembly_node: str, UsdReferenceAssemblyRepresentations
        :param representation:
        :return:
        """

        return maya.cmds.assembly(usd_reference_assembly_node, active=representation, edit=True)

    @staticmethod
    def set_usd_reference_assembly_variant(usd_reference_assmebly_node, variant_name, variant_value):
        """
        Sets the value of the given variant for the given Pixar USD Maya
        Reference Assembly Node (pxrUsdReferenceAssembly)
        :param usd_reference_assmebly_node: str
        :param variant_name: str
        :param variant_value: str
        :return:
        """

        usd_prim = mayaUsdLib.GetPrim(usd_reference_assmebly_node)
        variant_sets = usd_prim.GetVariantSets()
        variant_set_names = variant_sets.GetNames()
        if variant_name not in variant_set_names:
            LOGGER.warning(
                'Variant with name "{}" not found in Usd Prim "{}" ({})'.format(
                    variant_name, usd_prim, variant_set_names))
            return

        usd_variant = usd_prim.GetVariantSet(variant_name)
        usd_variant_choices = usd_variant.GetVariantNames()
        if variant_value not in usd_variant_choices:
            LOGGER.warning(
                'Variant Value "{}" not found in Variant Set Name "{}" for Usd Prim "{}" ({})'.format(
                    variant_value, variant_name, usd_prim, usd_variant_choices))
            return

        variant_attr_name = 'usdVariantSet_{}'.format(variant_name)
        return tp.Dcc.set_string_attribute_value(usd_reference_assmebly_node, variant_attr_name, str(variant_value))
