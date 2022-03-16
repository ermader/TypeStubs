"""
This type stub file was generated by pyright.
"""

"""Helper files for pickling"""
def save_pickle(obj, fname): # -> None:
    """
    Save the object to file via pickling.

    Parameters
    ----------
    fname : {str, pathlib.Path}
        Filename to pickle to
    """
    ...

def load_pickle(fname): # -> Any:
    """
    Load a previously saved object

    .. warning::

       Loading pickled models is not secure against erroneous or maliciously
       constructed data. Never unpickle data received from an untrusted or
       unauthenticated source.

    Parameters
    ----------
    fname : {str, pathlib.Path}
        Filename to unpickle

    Notes
    -----
    This method can be used to load *both* models and results.
    """
    ...

