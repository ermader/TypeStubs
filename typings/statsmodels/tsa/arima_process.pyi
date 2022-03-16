"""
This type stub file was generated by pyright.
"""

from statsmodels.compat.pandas import Appender
from statsmodels.tools.docstring import remove_parameters

"""ARMA process and estimation with scipy.signal.lfilter

Notes
-----
* written without textbook, works but not sure about everything
  briefly checked and it looks to be standard least squares, see below

* theoretical autocorrelation function of general ARMA
  Done, relatively easy to guess solution, time consuming to get
  theoretical test cases, example file contains explicit formulas for
  acovf of MA(1), MA(2) and ARMA(1,1)

Properties:
Judge, ... (1985): The Theory and Practise of Econometrics

Author: josefpktd
License: BSD
"""
__all__ = ["arma_acf", "arma_acovf", "arma_generate_sample", "arma_impulse_response", "arma2ar", "arma2ma", "deconvolve", "lpol2index", "index2lpol"]
NONSTATIONARY_ERROR = ...
def arma_generate_sample(ar, ma, nsample, scale=..., distrvs=..., axis=..., burnin=...):
    """
    Simulate data from an ARMA.

    Parameters
    ----------
    ar : array_like
        The coefficient for autoregressive lag polynomial, including zero lag.
    ma : array_like
        The coefficient for moving-average lag polynomial, including zero lag.
    nsample : int or tuple of ints
        If nsample is an integer, then this creates a 1d timeseries of
        length size. If nsample is a tuple, creates a len(nsample)
        dimensional time series where time is indexed along the input
        variable ``axis``. All series are unless ``distrvs`` generates
        dependent data.
    scale : float
        The standard deviation of noise.
    distrvs : function, random number generator
        A function that generates the random numbers, and takes ``size``
        as argument. The default is np.random.standard_normal.
    axis : int
        See nsample for details.
    burnin : int
        Number of observation at the beginning of the sample to drop.
        Used to reduce dependence on initial values.

    Returns
    -------
    ndarray
        Random sample(s) from an ARMA process.

    Notes
    -----
    As mentioned above, both the AR and MA components should include the
    coefficient on the zero-lag. This is typically 1. Further, due to the
    conventions used in signal processing used in signal.lfilter vs.
    conventions in statistics for ARMA processes, the AR parameters should
    have the opposite sign of what you might expect. See the examples below.

    Examples
    --------
    >>> import numpy as np
    >>> np.random.seed(12345)
    >>> arparams = np.array([.75, -.25])
    >>> maparams = np.array([.65, .35])
    >>> ar = np.r_[1, -arparams] # add zero-lag and negate
    >>> ma = np.r_[1, maparams] # add zero-lag
    >>> y = sm.tsa.arma_generate_sample(ar, ma, 250)
    >>> model = sm.tsa.ARIMA(y, (2, 0, 2), trend='n').fit(disp=0)
    >>> model.params
    array([ 0.79044189, -0.23140636,  0.70072904,  0.40608028])
    """
    ...

def arma_acovf(ar, ma, nobs=..., sigma2=..., dtype=...):
    """
    Theoretical autocovariances of stationary ARMA processes

    Parameters
    ----------
    ar : array_like, 1d
        The coefficients for autoregressive lag polynomial, including zero lag.
    ma : array_like, 1d
        The coefficients for moving-average lag polynomial, including zero lag.
    nobs : int
        The number of terms (lags plus zero lag) to include in returned acovf.
    sigma2 : float
        Variance of the innovation term.

    Returns
    -------
    ndarray
        The autocovariance of ARMA process given by ar, ma.

    See Also
    --------
    arma_acf : Autocorrelation function for ARMA processes.
    acovf : Sample autocovariance estimation.

    References
    ----------
    .. [*] Brockwell, Peter J., and Richard A. Davis. 2009. Time Series:
        Theory and Methods. 2nd ed. 1991. New York, NY: Springer.
    """
    ...

def arma_acf(ar, ma, lags=...): # -> Any:
    """
    Theoretical autocorrelation function of an ARMA process.

    Parameters
    ----------
    ar : array_like
        Coefficients for autoregressive lag polynomial, including zero lag.
    ma : array_like
        Coefficients for moving-average lag polynomial, including zero lag.
    lags : int
        The number of terms (lags plus zero lag) to include in returned acf.

    Returns
    -------
    ndarray
        The autocorrelations of ARMA process given by ar and ma.

    See Also
    --------
    arma_acovf : Autocovariances from ARMA processes.
    acf : Sample autocorrelation function estimation.
    acovf : Sample autocovariance function estimation.
    """
    ...

def arma_pacf(ar, ma, lags=...): # -> NDArray[float64]:
    """
    Theoretical partial autocorrelation function of an ARMA process.

    Parameters
    ----------
    ar : array_like, 1d
        The coefficients for autoregressive lag polynomial, including zero lag.
    ma : array_like, 1d
        The coefficients for moving-average lag polynomial, including zero lag.
    lags : int
        The number of terms (lags plus zero lag) to include in returned pacf.

    Returns
    -------
    ndarrray
        The partial autocorrelation of ARMA process given by ar and ma.

    Notes
    -----
    Solves yule-walker equation for each lag order up to nobs lags.

    not tested/checked yet
    """
    ...

def arma_periodogram(ar, ma, worN=..., whole=...): # -> tuple[Unknown, Any]:
    """
    Periodogram for ARMA process given by lag-polynomials ar and ma.

    Parameters
    ----------
    ar : array_like
        The autoregressive lag-polynomial with leading 1 and lhs sign.
    ma : array_like
        The moving average lag-polynomial with leading 1.
    worN : {None, int}, optional
        An option for scipy.signal.freqz (read "w or N").
        If None, then compute at 512 frequencies around the unit circle.
        If a single integer, the compute at that many frequencies.
        Otherwise, compute the response at frequencies given in worN.
    whole : {0,1}, optional
        An options for scipy.signal.freqz/
        Normally, frequencies are computed from 0 to pi (upper-half of
        unit-circle.  If whole is non-zero compute frequencies from 0 to 2*pi.

    Returns
    -------
    w : ndarray
        The frequencies.
    sd : ndarray
        The periodogram, also known as the spectral density.

    Notes
    -----
    Normalization ?

    This uses signal.freqz, which does not use fft. There is a fft version
    somewhere.
    """
    ...

def arma_impulse_response(ar, ma, leads=...):
    """
    Compute the impulse response function (MA representation) for ARMA process.

    Parameters
    ----------
    ar : array_like, 1d
        The auto regressive lag polynomial.
    ma : array_like, 1d
        The moving average lag polynomial.
    leads : int
        The number of observations to calculate.

    Returns
    -------
    ndarray
        The impulse response function with nobs elements.

    Notes
    -----
    This is the same as finding the MA representation of an ARMA(p,q).
    By reversing the role of ar and ma in the function arguments, the
    returned result is the AR representation of an ARMA(p,q), i.e

    ma_representation = arma_impulse_response(ar, ma, leads=100)
    ar_representation = arma_impulse_response(ma, ar, leads=100)

    Fully tested against matlab

    Examples
    --------
    AR(1)

    >>> arma_impulse_response([1.0, -0.8], [1.], leads=10)
    array([ 1.        ,  0.8       ,  0.64      ,  0.512     ,  0.4096    ,
            0.32768   ,  0.262144  ,  0.2097152 ,  0.16777216,  0.13421773])

    this is the same as

    >>> 0.8**np.arange(10)
    array([ 1.        ,  0.8       ,  0.64      ,  0.512     ,  0.4096    ,
            0.32768   ,  0.262144  ,  0.2097152 ,  0.16777216,  0.13421773])

    MA(2)

    >>> arma_impulse_response([1.0], [1., 0.5, 0.2], leads=10)
    array([ 1. ,  0.5,  0.2,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ])

    ARMA(1,2)

    >>> arma_impulse_response([1.0, -0.8], [1., 0.5, 0.2], leads=10)
    array([ 1.        ,  1.3       ,  1.24      ,  0.992     ,  0.7936    ,
            0.63488   ,  0.507904  ,  0.4063232 ,  0.32505856,  0.26004685])
    """
    ...

def arma2ma(ar, ma, lags=...):
    """
    A finite-lag approximate MA representation of an ARMA process.

    Parameters
    ----------
    ar : ndarray
        The auto regressive lag polynomial.
    ma : ndarray
        The moving average lag polynomial.
    lags : int
        The number of coefficients to calculate.

    Returns
    -------
    ndarray
        The coefficients of AR lag polynomial with nobs elements.

    Notes
    -----
    Equivalent to ``arma_impulse_response(ma, ar, leads=100)``
    """
    ...

def arma2ar(ar, ma, lags=...):
    """
    A finite-lag AR approximation of an ARMA process.

    Parameters
    ----------
    ar : array_like
        The auto regressive lag polynomial.
    ma : array_like
        The moving average lag polynomial.
    lags : int
        The number of coefficients to calculate.

    Returns
    -------
    ndarray
        The coefficients of AR lag polynomial with nobs elements.

    Notes
    -----
    Equivalent to ``arma_impulse_response(ma, ar, leads=100)``
    """
    ...

def ar2arma(ar_des, p, q, n=..., mse=..., start=...): # -> tuple[tuple[Any], Any, Unknown]:
    """
    Find arma approximation to ar process.

    This finds the ARMA(p,q) coefficients that minimize the integrated
    squared difference between the impulse_response functions (MA
    representation) of the AR and the ARMA process. This does not  check
    whether the MA lag polynomial of the ARMA process is invertible, neither
    does it check the roots of the AR lag polynomial.

    Parameters
    ----------
    ar_des : array_like
        The coefficients of original AR lag polynomial, including lag zero.
    p : int
        The length of desired AR lag polynomials.
    q : int
        The length of desired MA lag polynomials.
    n : int
        The number of terms of the impulse_response function to include in the
        objective function for the approximation.
    mse : str, 'ar'
        Not used.
    start : ndarray
        Initial values to use when finding the approximation.

    Returns
    -------
    ar_app : ndarray
        The coefficients of the AR lag polynomials of the approximation.
    ma_app : ndarray
        The coefficients of the MA lag polynomials of the approximation.
    res : tuple
        The result of optimize.leastsq.

    Notes
    -----
    Extension is possible if we want to match autocovariance instead
    of impulse response function.
    """
    ...

_arma_docs = ...
def lpol2index(ar): # -> tuple[Unknown | Any, ndarray[Unknown, Unknown]]:
    """
    Remove zeros from lag polynomial

    Parameters
    ----------
    ar : array_like
        coefficients of lag polynomial

    Returns
    -------
    coeffs : ndarray
        non-zero coefficients of lag polynomial
    index : ndarray
        index (lags) of lag polynomial with non-zero elements
    """
    ...

def index2lpol(coeffs, index): # -> NDArray[float64]:
    """
    Expand coefficients to lag poly

    Parameters
    ----------
    coeffs : ndarray
        non-zero coefficients of lag polynomial
    index : ndarray
        index (lags) of lag polynomial with non-zero elements

    Returns
    -------
    ar : array_like
        coefficients of lag polynomial
    """
    ...

def lpol_fima(d, n=...): # -> Any:
    """MA representation of fractional integration

    .. math:: (1-L)^{-d} for |d|<0.5  or |d|<1 (?)

    Parameters
    ----------
    d : float
        fractional power
    n : int
        number of terms to calculate, including lag zero

    Returns
    -------
    ma : ndarray
        coefficients of lag polynomial
    """
    ...

def lpol_fiar(d, n=...): # -> Any:
    """AR representation of fractional integration

    .. math:: (1-L)^{d} for |d|<0.5  or |d|<1 (?)

    Parameters
    ----------
    d : float
        fractional power
    n : int
        number of terms to calculate, including lag zero

    Returns
    -------
    ar : ndarray
        coefficients of lag polynomial

    Notes:
    first coefficient is 1, negative signs except for first term,
    ar(L)*x_t
    """
    ...

def lpol_sdiff(s):
    """return coefficients for seasonal difference (1-L^s)

    just a trivial convenience function

    Parameters
    ----------
    s : int
        number of periods in season

    Returns
    -------
    sdiff : list, length s+1
    """
    ...

def deconvolve(num, den, n=...): # -> tuple[Unknown | list[Unknown], NDArray[_SCT@atleast_1d] | Unknown]:
    """Deconvolves divisor out of signal, division of polynomials for n terms

    calculates den^{-1} * num

    Parameters
    ----------
    num : array_like
        signal or lag polynomial
    denom : array_like
        coefficients of lag polynomial (linear filter)
    n : None or int
        number of terms of quotient

    Returns
    -------
    quot : ndarray
        quotient or filtered series
    rem : ndarray
        remainder

    Notes
    -----
    If num is a time series, then this applies the linear filter den^{-1}.
    If both num and den are both lag polynomials, then this calculates the
    quotient polynomial for n terms and also returns the remainder.

    This is copied from scipy.signal.signaltools and added n as optional
    parameter.
    """
    ...

_generate_sample_doc = ...
class ArmaProcess:
    r"""
    Theoretical properties of an ARMA process for specified lag-polynomials.

    Parameters
    ----------
    ar : array_like
        Coefficient for autoregressive lag polynomial, including zero lag.
        Must be entered using the signs from the lag polynomial representation.
        See the notes for more information about the sign.
    ma : array_like
        Coefficient for moving-average lag polynomial, including zero lag.
    nobs : int, optional
        Length of simulated time series. Used, for example, if a sample is
        generated. See example.

    Notes
    -----
    Both the AR and MA components must include the coefficient on the
    zero-lag. In almost all cases these values should be 1. Further, due to
    using the lag-polynomial representation, the AR parameters should
    have the opposite sign of what one would write in the ARMA representation.
    See the examples below.

    The ARMA(p,q) process is described by

    .. math::

        y_{t}=\phi_{1}y_{t-1}+\ldots+\phi_{p}y_{t-p}+\theta_{1}\epsilon_{t-1}
               +\ldots+\theta_{q}\epsilon_{t-q}+\epsilon_{t}

    and the parameterization used in this function uses the lag-polynomial
    representation,

    .. math::

        \left(1-\phi_{1}L-\ldots-\phi_{p}L^{p}\right)y_{t} =
            \left(1+\theta_{1}L+\ldots+\theta_{q}L^{q}\right)\epsilon_{t}

    Examples
    --------
    ARMA(2,2) with AR coefficients 0.75 and -0.25, and MA coefficients 0.65 and 0.35

    >>> import statsmodels.api as sm
    >>> import numpy as np
    >>> np.random.seed(12345)
    >>> arparams = np.array([.75, -.25])
    >>> maparams = np.array([.65, .35])
    >>> ar = np.r_[1, -arparams] # add zero-lag and negate
    >>> ma = np.r_[1, maparams] # add zero-lag
    >>> arma_process = sm.tsa.ArmaProcess(ar, ma)
    >>> arma_process.isstationary
    True
    >>> arma_process.isinvertible
    True
    >>> arma_process.arroots
    array([1.5-1.32287566j, 1.5+1.32287566j])
    >>> y = arma_process.generate_sample(250)
    >>> model = sm.tsa.ARIMA(y, (2, 0, 2), trend='n').fit(disp=0)
    >>> model.params
    array([ 0.79044189, -0.23140636,  0.70072904,  0.40608028])

    The same ARMA(2,2) Using the from_coeffs class method

    >>> arma_process = sm.tsa.ArmaProcess.from_coeffs(arparams, maparams)
    >>> arma_process.arroots
    array([1.5-1.32287566j, 1.5+1.32287566j])
    """
    def __init__(self, ar=..., ma=..., nobs=...) -> None:
        ...
    
    @classmethod
    def from_roots(cls, maroots=..., arroots=..., nobs=...): # -> Self@ArmaProcess:
        """
        Create ArmaProcess from AR and MA polynomial roots.

        Parameters
        ----------
        maroots : array_like
            Roots for the MA polynomial
            1 + theta_1*z + theta_2*z^2 + ..... + theta_n*z^n
        arroots : array_like
            Roots for the AR polynomial
            1 - phi_1*z - phi_2*z^2 - ..... - phi_n*z^n
        nobs : int, optional
            Length of simulated time series. Used, for example, if a sample
            is generated.

        Returns
        -------
        ArmaProcess
            Class instance initialized with arcoefs and macoefs.

        Examples
        --------
        >>> arroots = [.75, -.25]
        >>> maroots = [.65, .35]
        >>> arma_process = sm.tsa.ArmaProcess.from_roots(arroots, maroots)
        >>> arma_process.isstationary
        True
        >>> arma_process.isinvertible
        True
        """
        ...
    
    @classmethod
    def from_coeffs(cls, arcoefs=..., macoefs=..., nobs=...): # -> Self@ArmaProcess:
        """
        Create ArmaProcess from an ARMA representation.

        Parameters
        ----------
        arcoefs : array_like
            Coefficient for autoregressive lag polynomial, not including zero
            lag. The sign is inverted to conform to the usual time series
            representation of an ARMA process in statistics. See the class
            docstring for more information.
        macoefs : array_like
            Coefficient for moving-average lag polynomial, excluding zero lag.
        nobs : int, optional
            Length of simulated time series. Used, for example, if a sample
            is generated.

        Returns
        -------
        ArmaProcess
            Class instance initialized with arcoefs and macoefs.

        Examples
        --------
        >>> arparams = [.75, -.25]
        >>> maparams = [.65, .35]
        >>> arma_process = sm.tsa.ArmaProcess.from_coeffs(ar, ma)
        >>> arma_process.isstationary
        True
        >>> arma_process.isinvertible
        True
        """
        ...
    
    @classmethod
    def from_estimation(cls, model_results, nobs=...): # -> Self@ArmaProcess:
        """
        Create an ArmaProcess from the results of an ARIMA estimation.

        Parameters
        ----------
        model_results : ARIMAResults instance
            A fitted model.
        nobs : int, optional
            If None, nobs is taken from the results.

        Returns
        -------
        ArmaProcess
            Class instance initialized from model_results.

        See Also
        --------
        statsmodels.tsa.arima.model.ARIMA
            The models class used to create the ArmaProcess
        """
        ...
    
    def __mul__(self, oth): # -> Self@ArmaProcess:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __str__(self) -> str:
        ...
    
    @Appender(remove_parameters(arma_acovf.__doc__, ["ar", "ma", "sigma2"]))
    def acovf(self, nobs=...): # -> NDArray[_SCT@zeros]:
        ...
    
    @Appender(remove_parameters(arma_acf.__doc__, ["ar", "ma"]))
    def acf(self, lags=...): # -> Any:
        ...
    
    @Appender(remove_parameters(arma_pacf.__doc__, ["ar", "ma"]))
    def pacf(self, lags=...): # -> NDArray[float64]:
        ...
    
    @Appender(remove_parameters(arma_periodogram.__doc__, ["ar", "ma", "worN", "whole"]))
    def periodogram(self, nobs=...): # -> tuple[Unknown, Any]:
        ...
    
    @Appender(remove_parameters(arma_impulse_response.__doc__, ["ar", "ma"]))
    def impulse_response(self, leads=...):
        ...
    
    @Appender(remove_parameters(arma2ma.__doc__, ["ar", "ma"]))
    def arma2ma(self, lags=...):
        ...
    
    @Appender(remove_parameters(arma2ar.__doc__, ["ar", "ma"]))
    def arma2ar(self, lags=...):
        ...
    
    @property
    def arroots(self):
        """Roots of autoregressive lag-polynomial"""
        ...
    
    @property
    def maroots(self):
        """Roots of moving average lag-polynomial"""
        ...
    
    @property
    def isstationary(self): # -> bool:
        """
        Arma process is stationary if AR roots are outside unit circle.

        Returns
        -------
        bool
             True if autoregressive roots are outside unit circle.
        """
        ...
    
    @property
    def isinvertible(self): # -> bool:
        """
        Arma process is invertible if MA roots are outside unit circle.

        Returns
        -------
        bool
             True if moving average roots are outside unit circle.
        """
        ...
    
    def invertroots(self, retnew=...): # -> Self@ArmaProcess | tuple[Unknown | NDArray[_SCT@ascontiguousarray] | ndarray[Unknown, Unknown] | None, bool]:
        """
        Make MA polynomial invertible by inverting roots inside unit circle.

        Parameters
        ----------
        retnew : bool
            If False (default), then return the lag-polynomial as array.
            If True, then return a new instance with invertible MA-polynomial.

        Returns
        -------
        manew : ndarray
           A new invertible MA lag-polynomial, returned if retnew is false.
        wasinvertible : bool
           True if the MA lag-polynomial was already invertible, returned if
           retnew is false.
        armaprocess : new instance of class
           If retnew is true, then return a new instance with invertible
           MA-polynomial.
        """
        ...
    
    @Appender(str(_generate_sample_doc))
    def generate_sample(self, nsample=..., scale=..., distrvs=..., axis=..., burnin=...):
        ...
    

