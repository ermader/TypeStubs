"""
This type stub file was generated by pyright.
"""

import enum

"""
colorLib.table_builder: Generic helper for filling in BaseTable derivatives from tuples and maps and such.

"""
class BuildCallback(enum.Enum):
    """Keyed on (BEFORE_BUILD, class[, Format if available]).
    Receives (dest, source).
    Should return (dest, source), which can be new objects.
    """
    BEFORE_BUILD = ...
    AFTER_BUILD = ...
    CREATE_DEFAULT = ...


class TableBuilder:
    """
    Helps to populate things derived from BaseTable from maps, tuples, etc.

    A table of lifecycle callbacks may be provided to add logic beyond what is possible
    based on otData info for the target class. See BuildCallbacks.
    """
    def __init__(self, callbackTable=...) -> None:
        ...
    
    def build(self, cls, source):
        ...
    


class TableUnbuilder:
    def __init__(self, callbackTable=...) -> None:
        ...
    
    def unbuild(self, table):
        ...
    


