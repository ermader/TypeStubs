"""
This type stub file was generated by pyright.
"""

import statsmodels.regression.linear_model as lm
from statsmodels.discrete.discrete_model import CountModel, CountResults, DiscreteModel, L1CountResults
from statsmodels.compat.pandas import Appender

__all__ = ["ZeroInflatedPoisson", "ZeroInflatedGeneralizedPoisson", "ZeroInflatedNegativeBinomialP"]
_doc_zi_params = ...
class GenericZeroInflated(CountModel):
    __doc__ = ...
    def __init__(self, endog, exog, exog_infl=..., offset=..., inflation=..., exposure=..., missing=..., **kwargs) -> None:
        ...
    
    def loglike(self, params): # -> Any:
        """
        Loglikelihood of Generic Zero Inflated model.

        Parameters
        ----------
        params : array_like
            The parameters of the model.

        Returns
        -------
        loglike : float
            The log-likelihood function of the model evaluated at `params`.
            See notes.

        Notes
        -----
        .. math:: \\ln L=\\sum_{y_{i}=0}\\ln(w_{i}+(1-w_{i})*P_{main\\_model})+
            \\sum_{y_{i}>0}(\\ln(1-w_{i})+L_{main\\_model})
            where P - pdf of main model, L - loglike function of main model.
        """
        ...
    
    def loglikeobs(self, params): # -> NDArray[_SCT@zeros_like]:
        """
        Loglikelihood for observations of Generic Zero Inflated model.

        Parameters
        ----------
        params : array_like
            The parameters of the model.

        Returns
        -------
        loglike : ndarray
            The log likelihood for each observation of the model evaluated
            at `params`. See Notes for definition.

        Notes
        -----
        .. math:: \\ln L=\\ln(w_{i}+(1-w_{i})*P_{main\\_model})+
            \\ln(1-w_{i})+L_{main\\_model}
            where P - pdf of main model, L - loglike function of main model.

        for observations :math:`i=1,...,n`
        """
        ...
    
    @Appender(DiscreteModel.fit.__doc__)
    def fit(self, start_params=..., method=..., maxiter=..., full_output=..., disp=..., callback=..., cov_type=..., cov_kwds=..., use_t=..., **kwargs):
        ...
    
    @Appender(DiscreteModel.fit_regularized.__doc__)
    def fit_regularized(self, start_params=..., method=..., maxiter=..., full_output=..., disp=..., callback=..., alpha=..., trim_mode=..., auto_trim_tol=..., size_trim_tol=..., qc_tol=..., **kwargs):
        ...
    
    def score_obs(self, params): # -> ndarray[Any, dtype[Any]] | NDArray[_SCT@hstack]:
        """
        Generic Zero Inflated model score (gradient) vector of the log-likelihood

        Parameters
        ----------
        params : array_like
            The parameters of the model

        Returns
        -------
        score : ndarray, 1-D
            The score vector of the model, i.e. the first derivative of the
            loglikelihood function, evaluated at `params`
        """
        ...
    
    def score(self, params): # -> Any:
        ...
    
    def hessian(self, params): # -> NDArray[floating[Any]] | NDArray[float64]:
        """
        Generic Zero Inflated model Hessian matrix of the loglikelihood

        Parameters
        ----------
        params : array_like
            The parameters of the model

        Returns
        -------
        hess : ndarray, (k_vars, k_vars)
            The Hessian, second derivative of loglikelihood function,
            evaluated at `params`

        Notes
        -----
        """
        ...
    
    def predict(self, params, exog=..., exog_infl=..., exposure=..., offset=..., which=...):
        """
        Predict response variable of a count model given exogenous variables.

        Parameters
        ----------
        params : array_like
            The parameters of the model
        exog : ndarray, optional
            A reference to the exogenous design.
            If not assigned, will be used exog from fitting.
        exog_infl : ndarray, optional
            A reference to the zero-inflated exogenous design.
            If not assigned, will be used exog from fitting.
        offset : ndarray, optional
            Offset is added to the linear prediction with coefficient equal to 1.
        exposure : ndarray, optional
            Log(exposure) is added to the linear prediction with coefficient
            equal to 1. If exposure is specified, then it will be logged by the method.
            The user does not need to log it first.
        which : str, optional
            Define values that will be predicted.
            'mean', 'mean-main', 'linear', 'mean-nonzero', 'prob-zero, 'prob', 'prob-main'
            Default is 'mean'.

        Notes
        -----
        """
        ...
    


class ZeroInflatedPoisson(GenericZeroInflated):
    __doc__ = ...
    def __init__(self, endog, exog, exog_infl=..., offset=..., exposure=..., inflation=..., missing=..., **kwargs) -> None:
        ...
    


class ZeroInflatedGeneralizedPoisson(GenericZeroInflated):
    __doc__ = ...
    def __init__(self, endog, exog, exog_infl=..., offset=..., exposure=..., inflation=..., p=..., missing=..., **kwargs) -> None:
        ...
    


class ZeroInflatedNegativeBinomialP(GenericZeroInflated):
    __doc__ = ...
    def __init__(self, endog, exog, exog_infl=..., offset=..., exposure=..., inflation=..., p=..., missing=..., **kwargs) -> None:
        ...
    


class ZeroInflatedPoissonResults(CountResults):
    __doc__ = ...
    def get_margeff(self, at=..., method=..., atexog=..., dummy=..., count=...):
        """Get marginal effects of the fitted model.

        Not yet implemented for Zero Inflated Models
        """
        ...
    


class L1ZeroInflatedPoissonResults(L1CountResults, ZeroInflatedPoissonResults):
    ...


class ZeroInflatedPoissonResultsWrapper(lm.RegressionResultsWrapper):
    ...


class L1ZeroInflatedPoissonResultsWrapper(lm.RegressionResultsWrapper):
    ...


class ZeroInflatedGeneralizedPoissonResults(CountResults):
    __doc__ = ...
    def get_margeff(self, at=..., method=..., atexog=..., dummy=..., count=...):
        """Get marginal effects of the fitted model.

        Not yet implemented for Zero Inflated Models
        """
        ...
    


class L1ZeroInflatedGeneralizedPoissonResults(L1CountResults, ZeroInflatedGeneralizedPoissonResults):
    ...


class ZeroInflatedGeneralizedPoissonResultsWrapper(lm.RegressionResultsWrapper):
    ...


class L1ZeroInflatedGeneralizedPoissonResultsWrapper(lm.RegressionResultsWrapper):
    ...


class ZeroInflatedNegativeBinomialResults(CountResults):
    __doc__ = ...
    def get_margeff(self, at=..., method=..., atexog=..., dummy=..., count=...):
        """Get marginal effects of the fitted model.

        Not yet implemented for Zero Inflated Models
        """
        ...
    


class L1ZeroInflatedNegativeBinomialResults(L1CountResults, ZeroInflatedNegativeBinomialResults):
    ...


class ZeroInflatedNegativeBinomialResultsWrapper(lm.RegressionResultsWrapper):
    ...


class L1ZeroInflatedNegativeBinomialResultsWrapper(lm.RegressionResultsWrapper):
    ...


