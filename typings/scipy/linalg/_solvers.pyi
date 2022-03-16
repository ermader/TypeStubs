"""
This type stub file was generated by pyright.
"""

"""Matrix equation solver routines"""
__all__ = ['solve_sylvester', 'solve_continuous_lyapunov', 'solve_discrete_lyapunov', 'solve_lyapunov', 'solve_continuous_are', 'solve_discrete_are']
def solve_sylvester(a, b, q): # -> Any:
    """
    Computes a solution (X) to the Sylvester equation :math:`AX + XB = Q`.

    Parameters
    ----------
    a : (M, M) array_like
        Leading matrix of the Sylvester equation
    b : (N, N) array_like
        Trailing matrix of the Sylvester equation
    q : (M, N) array_like
        Right-hand side

    Returns
    -------
    x : (M, N) ndarray
        The solution to the Sylvester equation.

    Raises
    ------
    LinAlgError
        If solution was not found

    Notes
    -----
    Computes a solution to the Sylvester matrix equation via the Bartels-
    Stewart algorithm. The A and B matrices first undergo Schur
    decompositions. The resulting matrices are used to construct an
    alternative Sylvester equation (``RY + YS^T = F``) where the R and S
    matrices are in quasi-triangular form (or, when R, S or F are complex,
    triangular form). The simplified equation is then solved using
    ``*TRSYL`` from LAPACK directly.

    .. versionadded:: 0.11.0

    Examples
    --------
    Given `a`, `b`, and `q` solve for `x`:

    >>> from scipy import linalg
    >>> a = np.array([[-3, -2, 0], [-1, -1, 3], [3, -5, -1]])
    >>> b = np.array([[1]])
    >>> q = np.array([[1],[2],[3]])
    >>> x = linalg.solve_sylvester(a, b, q)
    >>> x
    array([[ 0.0625],
           [-0.5625],
           [ 0.6875]])
    >>> np.allclose(a.dot(x) + x.dot(b), q)
    True

    """
    ...

def solve_continuous_lyapunov(a, q):
    """
    Solves the continuous Lyapunov equation :math:`AX + XA^H = Q`.

    Uses the Bartels-Stewart algorithm to find :math:`X`.

    Parameters
    ----------
    a : array_like
        A square matrix

    q : array_like
        Right-hand side square matrix

    Returns
    -------
    x : ndarray
        Solution to the continuous Lyapunov equation

    See Also
    --------
    solve_discrete_lyapunov : computes the solution to the discrete-time
        Lyapunov equation
    solve_sylvester : computes the solution to the Sylvester equation

    Notes
    -----
    The continuous Lyapunov equation is a special form of the Sylvester
    equation, hence this solver relies on LAPACK routine ?TRSYL.

    .. versionadded:: 0.11.0

    Examples
    --------
    Given `a` and `q` solve for `x`:

    >>> from scipy import linalg
    >>> a = np.array([[-3, -2, 0], [-1, -1, 0], [0, -5, -1]])
    >>> b = np.array([2, 4, -1])
    >>> q = np.eye(3)
    >>> x = linalg.solve_continuous_lyapunov(a, q)
    >>> x
    array([[ -0.75  ,   0.875 ,  -3.75  ],
           [  0.875 ,  -1.375 ,   5.3125],
           [ -3.75  ,   5.3125, -27.0625]])
    >>> np.allclose(a.dot(x) + x.dot(a.T), q)
    True
    """
    ...

solve_lyapunov = ...
def solve_discrete_lyapunov(a, q, method=...): # -> ndarray[Unknown, Unknown]:
    """
    Solves the discrete Lyapunov equation :math:`AXA^H - X + Q = 0`.

    Parameters
    ----------
    a, q : (M, M) array_like
        Square matrices corresponding to A and Q in the equation
        above respectively. Must have the same shape.

    method : {'direct', 'bilinear'}, optional
        Type of solver.

        If not given, chosen to be ``direct`` if ``M`` is less than 10 and
        ``bilinear`` otherwise.

    Returns
    -------
    x : ndarray
        Solution to the discrete Lyapunov equation

    See Also
    --------
    solve_continuous_lyapunov : computes the solution to the continuous-time
        Lyapunov equation

    Notes
    -----
    This section describes the available solvers that can be selected by the
    'method' parameter. The default method is *direct* if ``M`` is less than 10
    and ``bilinear`` otherwise.

    Method *direct* uses a direct analytical solution to the discrete Lyapunov
    equation. The algorithm is given in, for example, [1]_. However, it requires
    the linear solution of a system with dimension :math:`M^2` so that
    performance degrades rapidly for even moderately sized matrices.

    Method *bilinear* uses a bilinear transformation to convert the discrete
    Lyapunov equation to a continuous Lyapunov equation :math:`(BX+XB'=-C)`
    where :math:`B=(A-I)(A+I)^{-1}` and
    :math:`C=2(A' + I)^{-1} Q (A + I)^{-1}`. The continuous equation can be
    efficiently solved since it is a special case of a Sylvester equation.
    The transformation algorithm is from Popov (1964) as described in [2]_.

    .. versionadded:: 0.11.0

    References
    ----------
    .. [1] Hamilton, James D. Time Series Analysis, Princeton: Princeton
       University Press, 1994.  265.  Print.
       http://doc1.lbfl.li/aca/FLMF037168.pdf
    .. [2] Gajic, Z., and M.T.J. Qureshi. 2008.
       Lyapunov Matrix Equation in System Stability and Control.
       Dover Books on Engineering Series. Dover Publications.

    Examples
    --------
    Given `a` and `q` solve for `x`:

    >>> from scipy import linalg
    >>> a = np.array([[0.2, 0.5],[0.7, -0.9]])
    >>> q = np.eye(2)
    >>> x = linalg.solve_discrete_lyapunov(a, q)
    >>> x
    array([[ 0.70872893,  1.43518822],
           [ 1.43518822, -2.4266315 ]])
    >>> np.allclose(a.dot(x).dot(a.T)-x, -q)
    True

    """
    ...

def solve_continuous_are(a, b, q, r, e=..., s=..., balanced=...):
    r"""
    Solves the continuous-time algebraic Riccati equation (CARE).

    The CARE is defined as

    .. math::

          X A + A^H X - X B R^{-1} B^H X + Q = 0

    The limitations for a solution to exist are :

        * All eigenvalues of :math:`A` on the right half plane, should be
          controllable.

        * The associated hamiltonian pencil (See Notes), should have
          eigenvalues sufficiently away from the imaginary axis.

    Moreover, if ``e`` or ``s`` is not precisely ``None``, then the
    generalized version of CARE

    .. math::

          E^HXA + A^HXE - (E^HXB + S) R^{-1} (B^HXE + S^H) + Q = 0

    is solved. When omitted, ``e`` is assumed to be the identity and ``s``
    is assumed to be the zero matrix with sizes compatible with ``a`` and
    ``b``, respectively.

    Parameters
    ----------
    a : (M, M) array_like
        Square matrix
    b : (M, N) array_like
        Input
    q : (M, M) array_like
        Input
    r : (N, N) array_like
        Nonsingular square matrix
    e : (M, M) array_like, optional
        Nonsingular square matrix
    s : (M, N) array_like, optional
        Input
    balanced : bool, optional
        The boolean that indicates whether a balancing step is performed
        on the data. The default is set to True.

    Returns
    -------
    x : (M, M) ndarray
        Solution to the continuous-time algebraic Riccati equation.

    Raises
    ------
    LinAlgError
        For cases where the stable subspace of the pencil could not be
        isolated. See Notes section and the references for details.

    See Also
    --------
    solve_discrete_are : Solves the discrete-time algebraic Riccati equation

    Notes
    -----
    The equation is solved by forming the extended hamiltonian matrix pencil,
    as described in [1]_, :math:`H - \lambda J` given by the block matrices ::

        [ A    0    B ]             [ E   0    0 ]
        [-Q  -A^H  -S ] - \lambda * [ 0  E^H   0 ]
        [ S^H B^H   R ]             [ 0   0    0 ]

    and using a QZ decomposition method.

    In this algorithm, the fail conditions are linked to the symmetry
    of the product :math:`U_2 U_1^{-1}` and condition number of
    :math:`U_1`. Here, :math:`U` is the 2m-by-m matrix that holds the
    eigenvectors spanning the stable subspace with 2-m rows and partitioned
    into two m-row matrices. See [1]_ and [2]_ for more details.

    In order to improve the QZ decomposition accuracy, the pencil goes
    through a balancing step where the sum of absolute values of
    :math:`H` and :math:`J` entries (after removing the diagonal entries of
    the sum) is balanced following the recipe given in [3]_.

    .. versionadded:: 0.11.0

    References
    ----------
    .. [1]  P. van Dooren , "A Generalized Eigenvalue Approach For Solving
       Riccati Equations.", SIAM Journal on Scientific and Statistical
       Computing, Vol.2(2), :doi:`10.1137/0902010`

    .. [2] A.J. Laub, "A Schur Method for Solving Algebraic Riccati
       Equations.", Massachusetts Institute of Technology. Laboratory for
       Information and Decision Systems. LIDS-R ; 859. Available online :
       http://hdl.handle.net/1721.1/1301

    .. [3] P. Benner, "Symplectic Balancing of Hamiltonian Matrices", 2001,
       SIAM J. Sci. Comput., 2001, Vol.22(5), :doi:`10.1137/S1064827500367993`

    Examples
    --------
    Given `a`, `b`, `q`, and `r` solve for `x`:

    >>> from scipy import linalg
    >>> a = np.array([[4, 3], [-4.5, -3.5]])
    >>> b = np.array([[1], [-1]])
    >>> q = np.array([[9, 6], [6, 4.]])
    >>> r = 1
    >>> x = linalg.solve_continuous_are(a, b, q, r)
    >>> x
    array([[ 21.72792206,  14.48528137],
           [ 14.48528137,   9.65685425]])
    >>> np.allclose(a.T.dot(x) + x.dot(a)-x.dot(b).dot(b.T).dot(x), -q)
    True

    """
    ...

def solve_discrete_are(a, b, q, r, e=..., s=..., balanced=...):
    r"""
    Solves the discrete-time algebraic Riccati equation (DARE).

    The DARE is defined as

    .. math::

          A^HXA - X - (A^HXB) (R + B^HXB)^{-1} (B^HXA) + Q = 0

    The limitations for a solution to exist are :

        * All eigenvalues of :math:`A` outside the unit disc, should be
          controllable.

        * The associated symplectic pencil (See Notes), should have
          eigenvalues sufficiently away from the unit circle.

    Moreover, if ``e`` and ``s`` are not both precisely ``None``, then the
    generalized version of DARE

    .. math::

          A^HXA - E^HXE - (A^HXB+S) (R+B^HXB)^{-1} (B^HXA+S^H) + Q = 0

    is solved. When omitted, ``e`` is assumed to be the identity and ``s``
    is assumed to be the zero matrix.

    Parameters
    ----------
    a : (M, M) array_like
        Square matrix
    b : (M, N) array_like
        Input
    q : (M, M) array_like
        Input
    r : (N, N) array_like
        Square matrix
    e : (M, M) array_like, optional
        Nonsingular square matrix
    s : (M, N) array_like, optional
        Input
    balanced : bool
        The boolean that indicates whether a balancing step is performed
        on the data. The default is set to True.

    Returns
    -------
    x : (M, M) ndarray
        Solution to the discrete algebraic Riccati equation.

    Raises
    ------
    LinAlgError
        For cases where the stable subspace of the pencil could not be
        isolated. See Notes section and the references for details.

    See Also
    --------
    solve_continuous_are : Solves the continuous algebraic Riccati equation

    Notes
    -----
    The equation is solved by forming the extended symplectic matrix pencil,
    as described in [1]_, :math:`H - \lambda J` given by the block matrices ::

           [  A   0   B ]             [ E   0   B ]
           [ -Q  E^H -S ] - \lambda * [ 0  A^H  0 ]
           [ S^H  0   R ]             [ 0 -B^H  0 ]

    and using a QZ decomposition method.

    In this algorithm, the fail conditions are linked to the symmetry
    of the product :math:`U_2 U_1^{-1}` and condition number of
    :math:`U_1`. Here, :math:`U` is the 2m-by-m matrix that holds the
    eigenvectors spanning the stable subspace with 2-m rows and partitioned
    into two m-row matrices. See [1]_ and [2]_ for more details.

    In order to improve the QZ decomposition accuracy, the pencil goes
    through a balancing step where the sum of absolute values of
    :math:`H` and :math:`J` rows/cols (after removing the diagonal entries)
    is balanced following the recipe given in [3]_. If the data has small
    numerical noise, balancing may amplify their effects and some clean up
    is required.

    .. versionadded:: 0.11.0

    References
    ----------
    .. [1]  P. van Dooren , "A Generalized Eigenvalue Approach For Solving
       Riccati Equations.", SIAM Journal on Scientific and Statistical
       Computing, Vol.2(2), :doi:`10.1137/0902010`

    .. [2] A.J. Laub, "A Schur Method for Solving Algebraic Riccati
       Equations.", Massachusetts Institute of Technology. Laboratory for
       Information and Decision Systems. LIDS-R ; 859. Available online :
       http://hdl.handle.net/1721.1/1301

    .. [3] P. Benner, "Symplectic Balancing of Hamiltonian Matrices", 2001,
       SIAM J. Sci. Comput., 2001, Vol.22(5), :doi:`10.1137/S1064827500367993`

    Examples
    --------
    Given `a`, `b`, `q`, and `r` solve for `x`:

    >>> from scipy import linalg as la
    >>> a = np.array([[0, 1], [0, -1]])
    >>> b = np.array([[1, 0], [2, 1]])
    >>> q = np.array([[-4, -4], [-4, 7]])
    >>> r = np.array([[9, 3], [3, 1]])
    >>> x = la.solve_discrete_are(a, b, q, r)
    >>> x
    array([[-4., -4.],
           [-4.,  7.]])
    >>> R = la.solve(r + b.T.dot(x).dot(b), b.T.dot(x).dot(a))
    >>> np.allclose(a.T.dot(x).dot(a) - x - a.T.dot(x).dot(b).dot(R), -q)
    True

    """
    ...

