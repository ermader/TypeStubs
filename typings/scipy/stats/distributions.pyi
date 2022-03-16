"""
This type stub file was generated by pyright.
"""

from . import _continuous_distns, _discrete_distns
from ._continuous_distns import *
from ._discrete_distns import *

__all__ = ['rv_discrete', 'rv_continuous', 'rv_histogram', 'entropy']
__all__ += _continuous_distns._distn_names
__all__ += _discrete_distns._distn_names