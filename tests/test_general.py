#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains general tests for artellapipe-libs-usd
"""

import pytest

from artellapipe.libs.usd import __version__


def test_version():
    assert __version__.get_version()
