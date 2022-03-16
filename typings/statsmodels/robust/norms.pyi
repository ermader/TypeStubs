"""
This type stub file was generated by pyright.
"""

class RobustNorm:
    """
    The parent class for the norms used for robust regression.

    Lays out the methods expected of the robust norms to be used
    by statsmodels.RLM.

    See Also
    --------
    statsmodels.rlm

    Notes
    -----
    Currently only M-estimators are available.

    References
    ----------
    PJ Huber.  'Robust Statistics' John Wiley and Sons, Inc., New York, 1981.

    DC Montgomery, EA Peck. 'Introduction to Linear Regression Analysis',
        John Wiley and Sons, Inc., New York, 2001.

    R Venables, B Ripley. 'Modern Applied Statistics in S'
        Springer, New York, 2002.
    """
    def rho(self, z):
        """
        The robust criterion estimator function.

        Abstract method:

        -2 loglike used in M-estimator
        """
        ...
    
    def psi(self, z):
        """
        Derivative of rho.  Sometimes referred to as the influence function.

        Abstract method:

        psi = rho'
        """
        ...
    
    def weights(self, z):
        """
        Returns the value of psi(z) / z

        Abstract method:

        psi(z) / z
        """
        ...
    
    def psi_deriv(self, z):
        """
        Derivative of psi.  Used to obtain robust covariance matrix.

        See statsmodels.rlm for more information.

        Abstract method:

        psi_derive = psi'
        """
        ...
    
    def __call__(self, z):
        """
        Returns the value of estimator rho applied to an input
        """
        ...
    


class LeastSquares(RobustNorm):
    """
    Least squares rho for M-estimation and its derived functions.

    See Also
    --------
    statsmodels.robust.norms.RobustNorm
    """
    def rho(self, z):
        """
        The least squares estimator rho function

        Parameters
        ----------
        z : ndarray
            1d array

        Returns
        -------
        rho : ndarray
            rho(z) = (1/2.)*z**2
        """
        ...
    
    def psi(self, z): # -> NDArray[_SCT@asarray]:
        """
        The psi function for the least squares estimator

        The analytic derivative of rho

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        psi : ndarray
            psi(z) = z
        """
        ...
    
    def weights(self, z): # -> NDArray[_SCT@ones]:
        """
        The least squares estimator weighting function for the IRLS algorithm.

        The psi function scaled by the input z

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        weights : ndarray
            weights(z) = np.ones(z.shape)
        """
        ...
    
    def psi_deriv(self, z): # -> NDArray[_SCT@ones]:
        """
        The derivative of the least squares psi function.

        Returns
        -------
        psi_deriv : ndarray
            ones(z.shape)

        Notes
        -----
        Used to estimate the robust covariance matrix.
        """
        ...
    


class HuberT(RobustNorm):
    """
    Huber's T for M estimation.

    Parameters
    ----------
    t : float, optional
        The tuning constant for Huber's t function. The default value is
        1.345.

    See Also
    --------
    statsmodels.robust.norms.RobustNorm
    """
    def __init__(self, t=...) -> None:
        ...
    
    def rho(self, z):
        r"""
        The robust criterion function for Huber's t.

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        rho : ndarray
            rho(z) = .5*z**2            for \|z\| <= t

            rho(z) = \|z\|*t - .5*t**2    for \|z\| > t
        """
        ...
    
    def psi(self, z): # -> NDArray[signedinteger[Any]]:
        r"""
        The psi function for Huber's t estimator

        The analytic derivative of rho

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        psi : ndarray
            psi(z) = z      for \|z\| <= t

            psi(z) = sign(z)*t for \|z\| > t
        """
        ...
    
    def weights(self, z): # -> NDArray[floating[Any]]:
        r"""
        Huber's t weighting function for the IRLS algorithm

        The psi function scaled by z

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        weights : ndarray
            weights(z) = 1          for \|z\| <= t

            weights(z) = t/\|z\|      for \|z\| > t
        """
        ...
    
    def psi_deriv(self, z): # -> Any:
        """
        The derivative of Huber's t psi function

        Notes
        -----
        Used to estimate the robust covariance matrix.
        """
        ...
    


class RamsayE(RobustNorm):
    """
    Ramsay's Ea for M estimation.

    Parameters
    ----------
    a : float, optional
        The tuning constant for Ramsay's Ea function.  The default value is
        0.3.

    See Also
    --------
    statsmodels.robust.norms.RobustNorm
    """
    def __init__(self, a=...) -> None:
        ...
    
    def rho(self, z): # -> NDArray[floating[Any]]:
        r"""
        The robust criterion function for Ramsay's Ea.

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        rho : ndarray
            rho(z) = a**-2 * (1 - exp(-a*\|z\|)*(1 + a*\|z\|))
        """
        ...
    
    def psi(self, z): # -> NDArray[bool_]:
        r"""
        The psi function for Ramsay's Ea estimator

        The analytic derivative of rho

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        psi : ndarray
            psi(z) = z*exp(-a*\|z\|)
        """
        ...
    
    def weights(self, z): # -> NDArray[Any]:
        r"""
        Ramsay's Ea weighting function for the IRLS algorithm

        The psi function scaled by z

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        weights : ndarray
            weights(z) = exp(-a*\|z\|)
        """
        ...
    
    def psi_deriv(self, z):
        """
        The derivative of Ramsay's Ea psi function.

        Notes
        -----
        Used to estimate the robust covariance matrix.
        """
        ...
    


class AndrewWave(RobustNorm):
    """
    Andrew's wave for M estimation.

    Parameters
    ----------
    a : float, optional
        The tuning constant for Andrew's Wave function.  The default value is
        1.339.

    See Also
    --------
    statsmodels.robust.norms.RobustNorm
    """
    def __init__(self, a=...) -> None:
        ...
    
    def rho(self, z): # -> NDArray[floating[Any]]:
        r"""
        The robust criterion function for Andrew's wave.

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        rho : ndarray
            rho(z) = a*(1-cos(z/a))     for \|z\| <= a*pi

            rho(z) = 2*a                for \|z\| > a*pi
        """
        ...
    
    def psi(self, z): # -> NDArray[bool_]:
        r"""
        The psi function for Andrew's wave

        The analytic derivative of rho

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        psi : ndarray
            psi(z) = sin(z/a)       for \|z\| <= a*pi

            psi(z) = 0              for \|z\| > a*pi
        """
        ...
    
    def weights(self, z): # -> NDArray[floating[Any]]:
        r"""
        Andrew's wave weighting function for the IRLS algorithm

        The psi function scaled by z

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        weights : ndarray
            weights(z) = sin(z/a)/(z/a)     for \|z\| <= a*pi

            weights(z) = 0                  for \|z\| > a*pi
        """
        ...
    
    def psi_deriv(self, z): # -> Any:
        """
        The derivative of Andrew's wave psi function

        Notes
        -----
        Used to estimate the robust covariance matrix.
        """
        ...
    


class TrimmedMean(RobustNorm):
    """
    Trimmed mean function for M-estimation.

    Parameters
    ----------
    c : float, optional
        The tuning constant for Ramsay's Ea function.  The default value is
        2.0.

    See Also
    --------
    statsmodels.robust.norms.RobustNorm
    """
    def __init__(self, c=...) -> None:
        ...
    
    def rho(self, z): # -> NDArray[floating[Any]]:
        r"""
        The robust criterion function for least trimmed mean.

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        rho : ndarray
            rho(z) = (1/2.)*z**2    for \|z\| <= c

            rho(z) = 0              for \|z\| > c
        """
        ...
    
    def psi(self, z): # -> NDArray[bool_]:
        r"""
        The psi function for least trimmed mean

        The analytic derivative of rho

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        psi : ndarray
            psi(z) = z              for \|z\| <= c

            psi(z) = 0              for \|z\| > c
        """
        ...
    
    def weights(self, z): # -> NDArray[Any]:
        r"""
        Least trimmed mean weighting function for the IRLS algorithm

        The psi function scaled by z

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        weights : ndarray
            weights(z) = 1             for \|z\| <= c

            weights(z) = 0             for \|z\| > c
        """
        ...
    
    def psi_deriv(self, z): # -> NDArray[Any]:
        """
        The derivative of least trimmed mean psi function

        Notes
        -----
        Used to estimate the robust covariance matrix.
        """
        ...
    


class Hampel(RobustNorm):
    """

    Hampel function for M-estimation.

    Parameters
    ----------
    a : float, optional
    b : float, optional
    c : float, optional
        The tuning constants for Hampel's function.  The default values are
        a,b,c = 2, 4, 8.

    See Also
    --------
    statsmodels.robust.norms.RobustNorm
    """
    def __init__(self, a=..., b=..., c=...) -> None:
        ...
    
    def rho(self, z): # -> Any:
        r"""
        The robust criterion function for Hampel's estimator

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        rho : ndarray
            rho(z) = (1/2.)*z**2                    for \|z\| <= a

            rho(z) = a*\|z\| - 1/2.*a**2              for a < \|z\| <= b

            rho(z) = a*(c*\|z\|-(1/2.)*z**2)/(c-b)    for b < \|z\| <= c

            rho(z) = a*(b + c - a)                  for \|z\| > c
        """
        ...
    
    def psi(self, z): # -> NDArray[floating[Any]]:
        r"""
        The psi function for Hampel's estimator

        The analytic derivative of rho

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        psi : ndarray
            psi(z) = z                            for \|z\| <= a

            psi(z) = a*sign(z)                    for a < \|z\| <= b

            psi(z) = a*sign(z)*(c - \|z\|)/(c-b)    for b < \|z\| <= c

            psi(z) = 0                            for \|z\| > c
        """
        ...
    
    def weights(self, z): # -> NDArray[_SCT@asarray]:
        r"""
        Hampel weighting function for the IRLS algorithm

        The psi function scaled by z

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        weights : ndarray
            weights(z) = 1                            for \|z\| <= a

            weights(z) = a/\|z\|                        for a < \|z\| <= b

            weights(z) = a*(c - \|z\|)/(\|z\|*(c-b))      for b < \|z\| <= c

            weights(z) = 0                            for \|z\| > c
        """
        ...
    
    def psi_deriv(self, z):
        ...
    


class TukeyBiweight(RobustNorm):
    """

    Tukey's biweight function for M-estimation.

    Parameters
    ----------
    c : float, optional
        The tuning constant for Tukey's Biweight.  The default value is
        c = 4.685.

    Notes
    -----
    Tukey's biweight is sometime's called bisquare.
    """
    def __init__(self, c=...) -> None:
        ...
    
    def rho(self, z):
        r"""
        The robust criterion function for Tukey's biweight estimator

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        rho : ndarray
            rho(z) = -(1 - (z/c)**2)**3 * c**2/6.   for \|z\| <= R

            rho(z) = 0                              for \|z\| > R
        """
        ...
    
    def psi(self, z): # -> NDArray[floating[Any]]:
        r"""
        The psi function for Tukey's biweight estimator

        The analytic derivative of rho

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        psi : ndarray
            psi(z) = z*(1 - (z/c)**2)**2        for \|z\| <= R

            psi(z) = 0                           for \|z\| > R
        """
        ...
    
    def weights(self, z):
        r"""
        Tukey's biweight weighting function for the IRLS algorithm

        The psi function scaled by z

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        weights : ndarray
            psi(z) = (1 - (z/c)**2)**2          for \|z\| <= R

            psi(z) = 0                          for \|z\| > R
        """
        ...
    
    def psi_deriv(self, z):
        """
        The derivative of Tukey's biweight psi function

        Notes
        -----
        Used to estimate the robust covariance matrix.
        """
        ...
    


def estimate_location(a, scale, norm=..., axis=..., initial=..., maxiter=..., tol=...): # -> Any:
    """
    M-estimator of location using self.norm and a current
    estimator of scale.

    This iteratively finds a solution to

    norm.psi((a-mu)/scale).sum() == 0

    Parameters
    ----------
    a : ndarray
        Array over which the location parameter is to be estimated
    scale : ndarray
        Scale parameter to be used in M-estimator
    norm : RobustNorm, optional
        Robust norm used in the M-estimator.  The default is HuberT().
    axis : int, optional
        Axis along which to estimate the location parameter.  The default is 0.
    initial : ndarray, optional
        Initial condition for the location parameter.  Default is None, which
        uses the median of a.
    niter : int, optional
        Maximum number of iterations.  The default is 30.
    tol : float, optional
        Toleration for convergence.  The default is 1e-06.

    Returns
    -------
    mu : ndarray
        Estimate of location
    """
    ...
