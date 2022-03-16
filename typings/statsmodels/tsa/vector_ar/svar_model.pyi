"""
This type stub file was generated by pyright.
"""

import statsmodels.tsa.base.tsa_model as tsbase
from statsmodels.tsa.vector_ar.var_model import VARProcess, VARResults

"""
Vector Autoregression (VAR) processes

References
----------
Lütkepohl (2005) New Introduction to Multiple Time Series Analysis
"""
def svar_ckerr(svar_type, A, B): # -> None:
    ...

class SVAR(tsbase.TimeSeriesModel):
    r"""
    Fit VAR and then estimate structural components of A and B, defined:

    .. math:: Ay_t = A_1 y_{t-1} + \ldots + A_p y_{t-p} + B\var(\epsilon_t)

    Parameters
    ----------
    endog : array_like
        1-d endogenous response variable. The independent variable.
    dates : array_like
        must match number of rows of endog
    svar_type : str
        "A" - estimate structural parameters of A matrix, B assumed = I
        "B" - estimate structural parameters of B matrix, A assumed = I
        "AB" - estimate structural parameters indicated in both A and B matrix
    A : array_like
        neqs x neqs with unknown parameters marked with 'E' for estimate
    B : array_like
        neqs x neqs with unknown parameters marked with 'E' for estimate

    References
    ----------
    Hamilton (1994) Time Series Analysis
    """
    y = ...
    def __init__(self, endog, svar_type, dates=..., freq=..., A=..., B=..., missing=...) -> None:
        ...
    
    def fit(self, A_guess=..., B_guess=..., maxlags=..., method=..., ic=..., trend=..., verbose=..., s_method=..., solver=..., override=..., maxiter=..., maxfun=...): # -> SVARResults:
        """
        Fit the SVAR model and solve for structural parameters

        Parameters
        ----------
        A_guess : array_like, optional
            A vector of starting values for all parameters to be estimated
            in A.
        B_guess : array_like, optional
            A vector of starting values for all parameters to be estimated
            in B.
        maxlags : int
            Maximum number of lags to check for order selection, defaults to
            12 * (nobs/100.)**(1./4), see select_order function
        method : {'ols'}
            Estimation method to use
        ic : {'aic', 'fpe', 'hqic', 'bic', None}
            Information criterion to use for VAR order selection.
            aic : Akaike
            fpe : Final prediction error
            hqic : Hannan-Quinn
            bic : Bayesian a.k.a. Schwarz
        verbose : bool, default False
            Print order selection output to the screen
        trend, str {"c", "ct", "ctt", "n"}
            "c" - add constant
            "ct" - constant and trend
            "ctt" - constant, linear and quadratic trend
            "n" - co constant, no trend
            Note that these are prepended to the columns of the dataset.
        s_method : {'mle'}
            Estimation method for structural parameters
        solver : {'nm', 'newton', 'bfgs', 'cg', 'ncg', 'powell'}
            Solution method
            See statsmodels.base for details
        override : bool, default False
            If True, returns estimates of A and B without checking
            order or rank condition
        maxiter : int, default 500
            Number of iterations to perform in solution method
        maxfun : int
            Number of function evaluations to perform

        Notes
        -----
        Lütkepohl pp. 146-153
        Hamilton pp. 324-336

        Returns
        -------
        est : SVARResults
        """
        ...
    
    def loglike(self, params): # -> Any:
        """
        Loglikelihood for SVAR model

        Notes
        -----
        This method assumes that the autoregressive parameters are
        first estimated, then likelihood with structural parameters
        is estimated
        """
        ...
    
    def score(self, AB_mask): # -> ndarray[Any, dtype[Any]]:
        """
        Return the gradient of the loglike at AB_mask.

        Parameters
        ----------
        AB_mask : unknown values of A and B matrix concatenated

        Notes
        -----
        Return numerical gradient
        """
        ...
    
    def hessian(self, AB_mask): # -> NDArray[floating[Any]]:
        """
        Returns numerical hessian.
        """
        ...
    
    def check_order(self, J): # -> None:
        ...
    
    def check_rank(self, J): # -> None:
        ...
    


class SVARProcess(VARProcess):
    """
    Class represents a known SVAR(p) process

    Parameters
    ----------
    coefs : ndarray (p x k x k)
    intercept : ndarray (length k)
    sigma_u : ndarray (k x k)
    names : sequence (length k)
    A : neqs x neqs np.ndarray with unknown parameters marked with 'E'
    A_mask : neqs x neqs mask array with known parameters masked
    B : neqs x neqs np.ndarry with unknown parameters marked with 'E'
    B_mask : neqs x neqs mask array with known parameters masked
    """
    def __init__(self, coefs, intercept, sigma_u, A_solve, B_solve, names=...) -> None:
        ...
    
    def orth_ma_rep(self, maxn=..., P=...):
        """

        Unavailable for SVAR
        """
        ...
    
    def svar_ma_rep(self, maxn=..., P=...): # -> NDArray[_SCT@array]:
        """

        Compute Structural MA coefficient matrices using MLE
        of A, B
        """
        ...
    


class SVARResults(SVARProcess, VARResults):
    """
    Estimate VAR(p) process with fixed number of lags

    Parameters
    ----------
    endog : ndarray
    endog_lagged : ndarray
    params : ndarray
    sigma_u : ndarray
    lag_order : int
    model : VAR model instance
    trend : str {'n', 'c', 'ct'}
    names : array_like
        List of names of the endogenous variables in order of appearance in `endog`.
    dates

    Attributes
    ----------
    aic
    bic
    bse
    coefs : ndarray (p x K x K)
        Estimated A_i matrices, A_i = coefs[i-1]
    cov_params
    dates
    detomega
    df_model : int
    df_resid : int
    endog
    endog_lagged
    fittedvalues
    fpe
    intercept
    info_criteria
    k_ar : int
    k_trend : int
    llf
    model
    names
    neqs : int
        Number of variables (equations)
    nobs : int
    n_totobs : int
    params
    k_ar : int
        Order of VAR process
    params : ndarray (Kp + 1) x K
        A_i matrices and intercept in stacked form [int A_1 ... A_p]
    pvalue
    names : list
        variables names
    resid
    sigma_u : ndarray (K x K)
        Estimate of white noise process variance Var[u_t]
    sigma_u_mle
    stderr
    trenorder
    tvalues
    """
    _model_type = ...
    def __init__(self, endog, endog_lagged, params, sigma_u, lag_order, A=..., B=..., A_mask=..., B_mask=..., model=..., trend=..., names=..., dates=...) -> None:
        ...
    
    def irf(self, periods=..., var_order=...): # -> IRAnalysis:
        """
        Analyze structural impulse responses to shocks in system

        Parameters
        ----------
        periods : int

        Returns
        -------
        irf : IRAnalysis
        """
        ...
    
    def sirf_errband_mc(self, orth=..., repl=..., steps=..., signif=..., seed=..., burn=..., cum=...): # -> tuple[ndarray[Any, Unknown], ndarray[Any, Unknown]]:
        """
        Compute Monte Carlo integrated error bands assuming normally
        distributed for impulse response functions

        Parameters
        ----------
        orth : bool, default False
            Compute orthogonalized impulse response error bands
        repl : int
            number of Monte Carlo replications to perform
        steps : int, default 10
            number of impulse response periods
        signif : float (0 < signif <1)
            Significance level for error bars, defaults to 95% CI
        seed : int
            np.random.seed for replications
        burn : int
            number of initial observations to discard for simulation
        cum : bool, default False
            produce cumulative irf error bands

        Notes
        -----
        Lütkepohl (2005) Appendix D

        Returns
        -------
        Tuple of lower and upper arrays of ma_rep monte carlo standard errors
        """
        ...
    


