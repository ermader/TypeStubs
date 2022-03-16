"""
This type stub file was generated by pyright.
"""

"""
Handle file opening for read/write
"""
class EmptyContextManager:
    """
    This class is needed to allow file-like object to be used as
    context manager, but without getting closed.
    """
    def __init__(self, obj) -> None:
        ...
    
    def __enter__(self): # -> Unknown:
        """When entering, return the embedded object"""
        ...
    
    def __exit__(self, *args): # -> Literal[False]:
        """Do not hide anything"""
        ...
    
    def __getattr__(self, name): # -> Any:
        ...
    


def get_file_obj(fname, mode=..., encoding=...):
    """
    Light wrapper to handle strings, path objects and let files (anything else)
    pass through.

    It also handle '.gz' files.

    Parameters
    ----------
    fname : str, path object or file-like object
        File to open / forward
    mode : str
        Argument passed to the 'open' or 'gzip.open' function
    encoding : str
        For Python 3 only, specify the encoding of the file

    Returns
    -------
    A file-like object that is always a context-manager. If the `fname` was
    already a file-like object, the returned context manager *will not
    close the file*.
    """
    ...

