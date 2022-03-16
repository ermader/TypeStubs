"""
This type stub file was generated by pyright.
"""

from statsmodels.compat.pandas import Appender
from .mlemodel import MLEModel, MLEResults, MLEResultsWrapper

"""
Linear exponential smoothing models

Author: Chad Fulton
License: BSD-3
"""
class ExponentialSmoothing(MLEModel):
    """
    Linear exponential smoothing models

    Parameters
    ----------
    endog : array_like
        The observed time-series process :math:`y`
    trend : bool, optional
        Whether or not to include a trend component. Default is False.
    damped_trend : bool, optional
        Whether or not an included trend component is damped. Default is False.
    seasonal : int, optional
        The number of periods in a complete seasonal cycle for seasonal
        (Holt-Winters) models. For example, 4 for quarterly data with an
        annual cycle or 7 for daily data with a weekly cycle. Default is
        no seasonal effects.
    initialization_method : str, optional
        Method for initialize the recursions. One of:

        * 'estimated'
        * 'concentrated'
        * 'heuristic'
        * 'known'

        If 'known' initialization is used, then `initial_level` must be
        passed, as well as `initial_slope` and `initial_seasonal` if
        applicable. Default is 'estimated'.
    initial_level : float, optional
        The initial level component. Only used if initialization is 'known'.
    initial_trend : float, optional
        The initial trend component. Only used if initialization is 'known'.
    initial_seasonal : array_like, optional
        The initial seasonal component. An array of length `seasonal`
        or length `seasonal - 1` (in which case the last initial value
        is computed to make the average effect zero). Only used if
        initialization is 'known'.
    bounds : iterable[tuple], optional
        An iterable containing bounds for the parameters. Must contain four
        elements, where each element is a tuple of the form (lower, upper).
        Default is (0.0001, 0.9999) for the level, trend, and seasonal
        smoothing parameters and (0.8, 0.98) for the trend damping parameter.
    concentrate_scale : bool, optional
        Whether or not to concentrate the scale (variance of the error term)
        out of the likelihood.

    Notes
    -----

    **Overview**

    The parameters and states of this model are estimated by setting up the
    exponential smoothing equations as a special case of a linear Gaussian
    state space model and applying the Kalman filter. As such, it has slightly
    worse performance than the dedicated exponential smoothing model,
    :class:`statsmodels.tsa.holtwinters.ExponentialSmoothing`, and it does not
    support multiplicative (nonlinear) exponential smoothing models.

    However, as a subclass of the state space models, this model class shares
    a consistent set of functionality with those models, which can make it
    easier to work with. In addition, it supports computing confidence
    intervals for forecasts and it supports concentrating the initial
    state out of the likelihood function.

    **Model timing**

    Typical exponential smoothing results correspond to the "filtered" output
    from state space models, because they incorporate both the transition to
    the new time point (adding the trend to the level and advancing the season)
    and updating to incorporate information from the observed datapoint. By
    contrast, the "predicted" output from state space models only incorporates
    the transition.

    One consequence is that the "initial state" corresponds to the "filtered"
    state at time t=0, but this is different from the usual state space
    initialization used in Statsmodels, which initializes the model with the
    "predicted" state at time t=1. This is important to keep in mind if
    setting the initial state directly (via `initialization_method='known'`).

    **Seasonality**

    In seasonal models, it is important to note that seasonals are included in
    the state vector of this model in the order:
    `[seasonal, seasonal.L1, seasonal.L2, seasonal.L3, ...]`. At time t, the
    `'seasonal'` state holds the seasonal factor operative at time t, while
    the `'seasonal.L'` state holds the seasonal factor that would have been
    operative at time t-1.

    Suppose that the seasonal order is `n_seasons = 4`. Then, because the
    initial state corresponds to time t=0 and the time t=1 is in the same
    season as time t=-3, the initial seasonal factor for time t=1 comes from
    the lag "L3" initial seasonal factor (i.e. at time t=1 this will be both
    the "L4" seasonal factor as well as the "L0", or current, seasonal factor).

    When the initial state is estimated (`initialization_method='estimated'`),
    there are only `n_seasons - 1` parameters, because the seasonal factors are
    normalized to sum to one. The three parameters that are estimated
    correspond to the lags "L0", "L1", and "L2" seasonal factors as of time
    t=0 (alternatively, the lags "L1", "L2", and "L3" as of time t=1).

    When the initial state is given (`initialization_method='known'`), the
    initial seasonal factors for time t=0 must be given by the argument
    `initial_seasonal`. This can either be a length `n_seasons - 1` array --
    in which case it should contain the lags "L0" - "L2" (in that order)
    seasonal factors as of time t=0 -- or a length `n_seasons` array, in which
    case it should contain the "L0" - "L3" (in that order) seasonal factors
    as of time t=0.

    Note that in the state vector and parameters, the "L0" seasonal is
    called "seasonal" or "initial_seasonal", while the i>0 lag is
    called "seasonal.L{i}".

    References
    ----------
    [1] Hyndman, Rob, Anne B. Koehler, J. Keith Ord, and Ralph D. Snyder.
        Forecasting with exponential smoothing: the state space approach.
        Springer Science & Business Media, 2008.
    """
    def __init__(self, endog, trend=..., damped_trend=..., seasonal=..., initialization_method=..., initial_level=..., initial_trend=..., initial_seasonal=..., bounds=..., concentrate_scale=..., dates=..., freq=..., missing=...) -> None:
        ...
    
    def clone(self, endog, exog=..., **kwargs): # -> Self@ExponentialSmoothing:
        ...
    
    @property
    def state_names(self): # -> list[str]:
        ...
    
    @property
    def param_names(self): # -> list[str]:
        ...
    
    @property
    def start_params(self): # -> NDArray[_SCT@array]:
        ...
    
    @property
    def k_params(self): # -> int:
        ...
    
    def transform_params(self, unconstrained): # -> NDArray[_SCT@array]:
        ...
    
    def untransform_params(self, constrained): # -> NDArray[_SCT@array]:
        ...
    
    def update(self, params, transformed=..., includes_fixed=..., complex_step=...):
        ...
    
    @Appender(MLEModel.loglike.__doc__)
    def loglike(self, params, *args, **kwargs): # -> Any:
        ...
    
    @Appender(MLEModel.filter.__doc__)
    def filter(self, params, cov_type=..., cov_kwds=..., return_ssm=..., results_class=..., results_wrapper_class=..., *args, **kwargs): # -> MLEResultsWrapper:
        ...
    
    @Appender(MLEModel.smooth.__doc__)
    def smooth(self, params, cov_type=..., cov_kwds=..., return_ssm=..., results_class=..., results_wrapper_class=..., *args, **kwargs): # -> MLEResultsWrapper:
        ...
    


class ExponentialSmoothingResults(MLEResults):
    """
    Results from fitting a linear exponential smoothing model
    """
    def __init__(self, model, params, filter_results, cov_type=..., **kwargs) -> None:
        ...
    
    @Appender(MLEResults.summary.__doc__)
    def summary(self, alpha=..., start=...):
        ...
    


class ExponentialSmoothingResultsWrapper(MLEResultsWrapper):
    _attrs = ...
    _wrap_attrs = ...
    _methods = ...
    _wrap_methods = ...

