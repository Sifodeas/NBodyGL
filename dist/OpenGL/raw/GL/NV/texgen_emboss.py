'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_NV_texgen_emboss'
_p.unpack_constants( """GL_EMBOSS_LIGHT_NV 0x855D
GL_EMBOSS_CONSTANT_NV 0x855E
GL_EMBOSS_MAP_NV 0x855F""", globals())


def glInitTexgenEmbossNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )