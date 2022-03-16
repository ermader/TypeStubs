"""
This type stub file was generated by pyright.
"""

"""
Provides a function to open the system browser to either search or go directly
to a function's reference
"""
BASE_URL = ...
def webdoc(func=..., stable=...): # -> None:
    """
    Opens a browser and displays online documentation

    Parameters
    ----------
    func : {str, callable}
        Either a string to search the documentation or a function
    stable : bool
        Flag indicating whether to use the stable documentation (True) or
        the development documentation (False).  If not provided, opens
        the stable documentation if the current version of statsmodels is a
        release

    Examples
    --------
    >>> import statsmodels.api as sm

    Documentation site

    >>> sm.webdoc()

    Search for glm in docs

    >>> sm.webdoc('glm')

    Go to current generated help for OLS

    >>> sm.webdoc(sm.OLS, stable=False)

    Notes
    -----
    By default, open stable documentation if the current version of
    statsmodels is a release.  Otherwise opens the development documentation.

    Uses the default system browser.
    """
    ...
