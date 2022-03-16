"""
This type stub file was generated by pyright.
"""

import numpy as np
from ._trustregion import BaseQuadraticSubproblem

"""Nearly exact trust-region optimization subproblem."""
__all__ = ['_minimize_trustregion_exact', 'estimate_smallest_singular_value', 'singular_leading_submatrix', 'IterativeSubproblem']
def estimate_smallest_singular_value(U): # -> tuple[Unknown | floating[Any], Unknown]:
    """Given upper triangular matrix ``U`` estimate the smallest singular
    value and the correspondent right singular vector in O(n**2) operations.

    Parameters
    ----------
    U : ndarray
        Square upper triangular matrix.

    Returns
    -------
    s_min : float
        Estimated smallest singular value of the provided matrix.
    z_min : ndarray
        Estimatied right singular vector.

    Notes
    -----
    The procedure is based on [1]_ and is done in two steps. First, it finds
    a vector ``e`` with components selected from {+1, -1} such that the
    solution ``w`` from the system ``U.T w = e`` is as large as possible.
    Next it estimate ``U v = w``. The smallest singular value is close
    to ``norm(w)/norm(v)`` and the right singular vector is close
    to ``v/norm(v)``.

    The estimation will be better more ill-conditioned is the matrix.

    References
    ----------
    .. [1] Cline, A. K., Moler, C. B., Stewart, G. W., Wilkinson, J. H.
           An estimate for the condition number of a matrix.  1979.
           SIAM Journal on Numerical Analysis, 16(2), 368-375.
    """
    ...

def gershgorin_bounds(H): # -> tuple[Any, Any]:
    """
    Given a square matrix ``H`` compute upper
    and lower bounds for its eigenvalues (Gregoshgorin Bounds).
    Defined ref. [1].

    References
    ----------
    .. [1] Conn, A. R., Gould, N. I., & Toint, P. L.
           Trust region methods. 2000. Siam. pp. 19.
    """
    ...

def singular_leading_submatrix(A, U, k): # -> tuple[Unknown, NDArray[float64]]:
    """
    Compute term that makes the leading ``k`` by ``k``
    submatrix from ``A`` singular.

    Parameters
    ----------
    A : ndarray
        Symmetric matrix that is not positive definite.
    U : ndarray
        Upper triangular matrix resulting of an incomplete
        Cholesky decomposition of matrix ``A``.
    k : int
        Positive integer such that the leading k by k submatrix from
        `A` is the first non-positive definite leading submatrix.

    Returns
    -------
    delta : float
        Amount that should be added to the element (k, k) of the
        leading k by k submatrix of ``A`` to make it singular.
    v : ndarray
        A vector such that ``v.T B v = 0``. Where B is the matrix A after
        ``delta`` is added to its element (k, k).
    """
    ...

class IterativeSubproblem(BaseQuadraticSubproblem):
    """Quadratic subproblem solved by nearly exact iterative method.

    Notes
    -----
    This subproblem solver was based on [1]_, [2]_ and [3]_,
    which implement similar algorithms. The algorithm is basically
    that of [1]_ but ideas from [2]_ and [3]_ were also used.

    References
    ----------
    .. [1] A.R. Conn, N.I. Gould, and P.L. Toint, "Trust region methods",
           Siam, pp. 169-200, 2000.
    .. [2] J. Nocedal and  S. Wright, "Numerical optimization",
           Springer Science & Business Media. pp. 83-91, 2006.
    .. [3] J.J. More and D.C. Sorensen, "Computing a trust region step",
           SIAM Journal on Scientific and Statistical Computing, vol. 4(3),
           pp. 553-572, 1983.
    """
    UPDATE_COEFF = ...
    EPS = np.finfo(float).eps
    def __init__(self, x, fun, jac, hess, hessp=..., k_easy=..., k_hard=...) -> None:
        ...
    
    def solve(self, tr_radius):
        """Solve quadratic subproblem"""
        ...
    

