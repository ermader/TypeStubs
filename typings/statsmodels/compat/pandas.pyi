"""
This type stub file was generated by pyright.
"""

import numpy as np
import pandas as pd
from typing import Optional

__all__ = ["assert_frame_equal", "assert_index_equal", "assert_series_equal", "data_klasses", "frequencies", "is_numeric_dtype", "testing", "cache_readonly", "deprecate_kwarg", "Appender", "Substitution", "is_int_index", "is_float_index", "make_dataframe", "to_numpy", "PD_LT_1_0_0", "get_cached_func", "get_cached_doc", "call_cached_func", "PD_LT_1_4"]
version = ...
PD_LT_1_0_0 = ...
PD_LT_1_4 = ...
data_klasses = ...
assert_frame_equal = ...
assert_index_equal = ...
assert_series_equal = ...
def is_int_index(index: pd.Index) -> bool:
    """
    Check if an index is integral

    Parameters
    ----------
    index : pd.Index
        Any numeric index

    Returns
    -------
    bool
        True if is an index with a standard integral type
    """
    ...

def is_float_index(index: pd.Index) -> bool:
    """
    Check if an index is floating

    Parameters
    ----------
    index : pd.Index
        Any numeric index

    Returns
    -------
    bool
        True if an index with a standard numpy floating dtype
    """
    ...

def to_numpy(po: pd.DataFrame) -> np.ndarray:
    """
    Workaround legacy pandas lacking to_numpy

    Parameters
    ----------
    po : Pandas obkect

    Returns
    -------
    ndarray
        A numpy array
    """
    ...

def get_cached_func(cached_prop):
    ...

def call_cached_func(cached_prop, *args, **kwargs):
    ...

def get_cached_doc(cached_prop) -> Optional[str]:
    ...
