"""
This type stub file was generated by pyright.
"""

from . import DefaultTable

META_HEADER_FORMAT = ...
DATA_MAP_FORMAT = ...
class table__m_e_t_a(DefaultTable.DefaultTable):
    def __init__(self, tag=...) -> None:
        ...
    
    def decompile(self, data, ttFont): # -> None:
        ...
    
    def compile(self, ttFont): # -> bytes:
        ...
    
    def toXML(self, writer, ttFont): # -> None:
        ...
    
    def fromXML(self, name, attrs, content, ttFont): # -> None:
        ...
    


