#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains utilities functions to work with USD variants
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from pxr import Sdf


def get_variant_set(prim, variant_set_name):
    """
    Returns variant from given variant set of the given prim
    :param prim: Usd.Prim
    :param variant_set_name: str
    :return: Usd.Variant
    """

    variant_sets = prim.GetVariantSets()
    variant_set_names = variant_sets.GetNames()
    if variant_set_name in variant_set_names:
        return variant_sets.GetVariantSet(variant_set_name)

    return None


def add_variant_set(prim, variant_set_name):
    """
    Addas a new USD variant set into the given USD prim
    :param prim: Usd.Prim
    :param variant_set_name: str
    :return: Usd.VariantSet
    """

    variant_set = get_variant_set(prim, variant_set_name)
    if not variant_set:
        variant_sets = prim.GetVariantSets()
        variant_set = variant_sets.AddVariantSet(variant_set_name)

    return variant_set


def add_variant_to_variant_set(prim, variant_set_name, variant_name):
    """
    Adds a new variant to given variant set in prim
    :param prim: Usd.Prim
    :param variant_set_name: str
    :param variant_name: str
    :return: Usd.Variant
    """

    variant_set = get_variant_set(prim, variant_set_name)
    if not variant_set:
        return None

    variant = variant_set.AddVariant(variant_name)

    return variant


def add_payload_to_variant(prim, variant_set_name, variant_name, payload_file):
    """
    Adds a new payload variant to given variant set in prim
    :param prim: Usd.Prim
    :param variant_set_name: str
    :param variant_name: str
    :param payload_file: str
    :return: bool
    """

    variant_set = get_variant_set(prim, variant_set_name)
    if not variant_set:
        return False

    variant_set.SetVariantSelection(variant_name)
    with variant_set.GetVariantEditContext():
        prim.GetPayloads().AddPayload(Sdf.Payload(payload_file))

    return True


def set_variant(prim, variant_set_name, variant_name):
    variant_set = get_variant_set(prim, variant_set_name)
    if not variant_set:
        return False

    variant_set.SetVariantSelection(variant_name)


# def set_variant_value(prim, variant_set_name, variant_name, value):
#     variant_set = get_variant_set(prim, variant_set_name)
#     if not variant_set:
#         return None
#
#     variant_set.SetVariantSelection(variant_name)
#     with variant_set.GetVariantEditContext():
#         pass
