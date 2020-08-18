#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains utilities functions related with USD
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from pxr import Pcp, Sdf


class UsdFormats(object):
    Generic = '.usd'
    Binary = '.usdc'
    Text = '.usda'


def get_prim_variants(prim):
    """
    Returns a list of tuples representing a prim's variant set names and active values
    Results are ordered "depth-first" by variant opinion strength in the prim's index
    :param prim: Usd.Prim
    :return: list(tuple(str, str))
    """

    def _walk_variant_nodes(node):
        if node.arcType == Pcp.ArcTypeVariant and not node.IsDueToAncestor():
            yield node.path.GetVariantSelection()
        for child_node in node.children:
            for child_selection in _walk_variant_nodes(child_node):
                yield child_selection

    results = list()
    prim_index = prim.GetPrimIndex()
    set_names = set(prim.GetVariantSets().GetNames())
    for variant_set_name, variant_set_value, in _walk_variant_nodes(prim_index.rootNode):
        try:
            set_names.remove(variant_set_name)
        except KeyError:
            pass
        else:
            results.append((variant_set_name, variant_set_value))

    # If a variant is not selected, it will not be included in the prim index, so we need a way to get those variants.
    # Prim.ComputeExpandedPrimIndex() seems unstable and slow so far. We can easily get variant names using the main
    # API functions. The problem is they are not ordered hierarchically ... Variants with no selection hide subsequent
    # variants so missing ones are usually top level variants.

    for set_name in set_names:
        set_value = prim.GetVariantSet(set_name).GetVariantSelection()
        results.append((set_name, set_value))

    return results
