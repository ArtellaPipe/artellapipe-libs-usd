'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_framebuffer_multisample_blit_scaled'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_EXT_framebuffer_multisample_blit_scaled',error_checker=_errors._error_checker)
GL_SCALED_RESOLVE_FASTEST_EXT=_C('GL_SCALED_RESOLVE_FASTEST_EXT',0x90BA)
GL_SCALED_RESOLVE_NICEST_EXT=_C('GL_SCALED_RESOLVE_NICEST_EXT',0x90BB)
