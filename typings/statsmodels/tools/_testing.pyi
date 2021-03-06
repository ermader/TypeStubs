"""
This type stub file was generated by pyright.
"""

"""Testing helper functions

Warning: current status experimental, mostly copy paste

Warning: these functions will be changed without warning as the need
during refactoring arises.

The first group of functions provide consistency checks

"""
class PytestTester:
    def __init__(self, package_path=...) -> None:
        ...
    
    def __call__(self, extra_args=..., exit=...):
        ...
    


def check_ttest_tvalues(results): # -> None:
    ...

def check_ftest_pvalues(results): # -> None:
    """
    Check that the outputs of `res.wald_test` produces pvalues that
    match res.pvalues.

    Check that the string representations of `res.summary()` and (possibly)
    `res.summary2()` correctly label either the t or z-statistic.

    Parameters
    ----------
    results : Results

    Raises
    ------
    AssertionError
    """
    ...

def check_fitted(results): # -> None:
    ...

def check_predict_types(results): # -> None:
    """
    Check that the `predict` method of the given results object produces the
    correct output type.

    Parameters
    ----------
    results : Results

    Raises
    ------
    AssertionError
    """
    ...

