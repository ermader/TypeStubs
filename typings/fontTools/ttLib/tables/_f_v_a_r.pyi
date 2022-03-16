"""
This type stub file was generated by pyright.
"""

from . import DefaultTable

FVAR_HEADER_FORMAT = ...
FVAR_AXIS_FORMAT = ...
FVAR_INSTANCE_FORMAT = ...
class table__f_v_a_r(DefaultTable.DefaultTable):
    dependencies = ...
    def __init__(self, tag=...) -> None:
        ...
    
    def compile(self, ttFont): # -> bytes:
        ...
    
    def decompile(self, data, ttFont): # -> None:
        ...
    
    def toXML(self, writer, ttFont): # -> None:
        ...
    
    def fromXML(self, name, attrs, content, ttFont): # -> None:
        ...
    


class Axis:
    def __init__(self) -> None:
        ...
    
    def compile(self): # -> bytes:
        ...
    
    def decompile(self, data): # -> None:
        ...
    
    def toXML(self, writer, ttFont): # -> None:
        ...
    
    def fromXML(self, name, _attrs, content, ttFont): # -> None:
        ...
    


class NamedInstance:
    def __init__(self) -> None:
        ...
    
    def compile(self, axisTags, includePostScriptName): # -> bytes:
        ...
    
    def decompile(self, data, axisTags): # -> None:
        ...
    
    def toXML(self, writer, ttFont): # -> None:
        ...
    
    def fromXML(self, name, attrs, content, ttFont): # -> None:
        ...
    

