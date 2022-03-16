"""
This type stub file was generated by pyright.
"""

import sys
import numpy as np
import numpy.typing as npt
from typing import Any, Dict, Generic, List, Literal, Optional, Set, Tuple, TypeVar, Union, overload
from scipy.sparse import coo_matrix, dok_matrix

if sys.version_info >= (3, 8):
    ...
else:
    ...
_BoxType = TypeVar("_BoxType", None, npt.NDArray[np.float64])
_ArrayLike0D = Union[bool, int, float, complex, str, bytes, np.generic],
_WeightType = Union[npt.ArrayLike, Tuple[Optional[npt.ArrayLike], Optional[npt.ArrayLike]]],
class cKDTreeNode:
    @property
    def data_points(self) -> npt.NDArray[np.float64]:
        ...
    
    @property
    def indices(self) -> npt.NDArray[np.intp]:
        ...
    
    @property
    def level(self) -> int:
        ...
    
    @property
    def split_dim(self) -> int:
        ...
    
    @property
    def children(self) -> int:
        ...
    
    @property
    def start_idx(self) -> int:
        ...
    
    @property
    def end_idx(self) -> int:
        ...
    
    @property
    def split(self) -> float:
        ...
    
    @property
    def lesser(self) -> Optional[cKDTreeNode]:
        ...
    
    @property
    def greater(self) -> Optional[cKDTreeNode]:
        ...
    


class cKDTree(Generic[_BoxType]):
    @property
    def n(self) -> int:
        ...
    
    @property
    def m(self) -> int:
        ...
    
    @property
    def leafsize(self) -> int:
        ...
    
    @property
    def size(self) -> int:
        ...
    
    @property
    def tree(self) -> cKDTreeNode:
        ...
    
    @property
    def data(self) -> npt.NDArray[np.float64]:
        ...
    
    @property
    def maxes(self) -> npt.NDArray[np.float64]:
        ...
    
    @property
    def mins(self) -> npt.NDArray[np.float64]:
        ...
    
    @property
    def indices(self) -> npt.NDArray[np.float64]:
        ...
    
    @property
    def boxsize(self) -> _BoxType:
        ...
    
    @overload
    def __new__(cls, data: npt.ArrayLike, leafsize: int = ..., compact_nodes: bool = ..., copy_data: bool = ..., balanced_tree: bool = ..., boxsize: None = ...) -> cKDTree[None]:
        ...
    
    @overload
    def __new__(cls, data: npt.ArrayLike, leafsize: int = ..., compact_nodes: bool = ..., copy_data: bool = ..., balanced_tree: bool = ..., boxsize: npt.ArrayLike = ...) -> cKDTree[npt.NDArray[np.float64]]:
        ...
    
    def query(self, x: npt.ArrayLike, k: npt.ArrayLike = ..., eps: float = ..., p: float = ..., distance_upper_bound: float = ..., workers: Optional[int] = ...) -> Tuple[Any, Any]:
        ...
    
    def query_ball_point(self, x: npt.ArrayLike, r: npt.ArrayLike, p: float, eps: float = ..., workers: Optional[int] = ..., return_sorted: Optional[bool] = ..., return_length: bool = ...) -> Any:
        ...
    
    def query_ball_tree(self, other: cKDTree, r: float, p: float, eps: float = ...) -> List[List[int]]:
        ...
    
    @overload
    def query_pairs(self, r: float, p: float = ..., eps: float = ..., output_type: Literal["set"] = ...) -> Set[Tuple[int, int]]:
        ...
    
    @overload
    def query_pairs(self, r: float, p: float = ..., eps: float = ..., output_type: Literal["ndarray"] = ...) -> npt.NDArray[np.intp]:
        ...
    
    @overload
    def count_neighbors(self, other: cKDTree, r: _ArrayLike0D, p: float = ..., weights: None | Tuple[None, None] = ..., cumulative: bool = ...) -> int:
        ...
    
    @overload
    def count_neighbors(self, other: cKDTree, r: _ArrayLike0D, p: float = ..., weights: _WeightType = ..., cumulative: bool = ...) -> np.float64:
        ...
    
    @overload
    def count_neighbors(self, other: cKDTree, r: npt.ArrayLike, p: float = ..., weights: None | Tuple[None, None] = ..., cumulative: bool = ...) -> npt.NDArray[np.intp]:
        ...
    
    @overload
    def count_neighbors(self, other: cKDTree, r: npt.ArrayLike, p: float = ..., weights: _WeightType = ..., cumulative: bool = ...) -> npt.NDArray[np.float64]:
        ...
    
    @overload
    def sparse_distance_matrix(self, other: cKDTree, max_distance: float, p: float = ..., output_type: Literal["dok_matrix"] = ...) -> dok_matrix:
        ...
    
    @overload
    def sparse_distance_matrix(self, other: cKDTree, max_distance: float, p: float = ..., output_type: Literal["coo_matrix"] = ...) -> coo_matrix:
        ...
    
    @overload
    def sparse_distance_matrix(self, other: cKDTree, max_distance: float, p: float = ..., output_type: Literal["dict"] = ...) -> Dict[Tuple[int, int], float]:
        ...
    
    @overload
    def sparse_distance_matrix(self, other: cKDTree, max_distance: float, p: float = ..., output_type: Literal["ndarray"] = ...) -> npt.NDArray[np.void]:
        ...
    


