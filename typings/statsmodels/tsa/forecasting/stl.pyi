"""
This type stub file was generated by pyright.
"""

import datetime as dt
import numpy as np
import pandas as pd
from statsmodels.compat.pandas import Substitution
from typing import Any, Dict, Optional, Union
from statsmodels.iolib.summary import Summary
from statsmodels.tools.docstring import indent
from statsmodels.tsa.seasonal import DecomposeResult, STL

DateLike = Union[int, str, dt.datetime, pd.Timestamp, np.datetime64]
ds = ...
_stl_forecast_params = ...
ds = ...
_fit_params = ...
@Substitution(stl_forecast_params=indent(_stl_forecast_params, "    "))
class STLForecast:
    r"""
    Model-based forecasting using STL to remove seasonality

    Forecasts are produced by first subtracting the seasonality
    estimated using STL, then forecasting the deseasonalized
    data using a time-series model, for example, ARIMA.

    Parameters
    ----------
%(stl_forecast_params)s

    See Also
    --------
    statsmodels.tsa.arima.model.ARIMA
        ARIMA modeling.
    statsmodels.tsa.ar_model.AutoReg
        Autoregressive modeling supporting complex deterministics.
    statsmodels.tsa.exponential_smoothing.ets.ETSModel
        Additive and multiplicative exponential smoothing with trend.
    statsmodels.tsa.statespace.exponential_smoothing.ExponentialSmoothing
        Additive exponential smoothing with trend.

    Notes
    -----
    If :math:`\hat{S}_t` is the seasonal component, then the deseasonalize
    series is constructed as

    .. math::

        Y_t - \hat{S}_t

    The trend component is not removed, and so the time series model should
    be capable of adequately fitting and forecasting the trend if present. The
    out-of-sample forecasts of the seasonal component are produced as

    .. math::

        \hat{S}_{T + h} = \hat{S}_{T - k}

    where :math:`k = m - h + m \lfloor (h-1)/m \rfloor` tracks the period
    offset in the full cycle of 1, 2, ..., m where m is the period length.

    This class is mostly a convenience wrapper around ``STL`` and a
    user-specified model. The model is assumed to follow the standard
    statsmodels pattern:

    * ``fit`` is used to estimate parameters and returns a results instance,
      ``results``.
    * ``results`` must exposes a method ``forecast(steps, **kwargs)`` that
      produces out-of-sample forecasts.
    * ``results`` may also exposes a method ``get_prediction`` that produces
      both in- and out-of-sample predictions.

    Examples
    --------
    >>> import numpy as np
    >>> import pandas as pd
    >>> from statsmodels.tsa.api import STLForecast
    >>> from statsmodels.tsa.arima.model import ARIMA
    >>> from statsmodels.datasets import macrodata
    >>> ds = macrodata.load_pandas()
    >>> data = np.log(ds.data.m1)
    >>> base_date = f"{int(ds.data.year[0])}-{3*int(ds.data.quarter[0])+1}-1"
    >>> data.index = pd.date_range(base_date, periods=data.shape[0], freq="QS")

    Generate forecasts from an ARIMA

    >>> stlf = STLForecast(data, ARIMA, model_kwargs={"order": (2, 1, 0)})
    >>> res = stlf.fit()
    >>> forecasts = res.forecast(12)

    Generate forecasts from an Exponential Smoothing model with trend
    >>> from statsmodels.tsa.statespace import exponential_smoothing
    >>> ES = exponential_smoothing.ExponentialSmoothing
    >>> config = {"trend": True}
    >>> stlf = STLForecast(data, ES, model_kwargs=config)
    >>> res = stlf.fit()
    >>> forecasts = res.forecast(12)
    """
    def __init__(self, endog, model, *, model_kwargs=..., period=..., seasonal=..., trend=..., low_pass=..., seasonal_deg=..., trend_deg=..., low_pass_deg=..., robust=..., seasonal_jump=..., trend_jump=..., low_pass_jump=...) -> None:
        ...
    
    @Substitution(fit_params=indent(_fit_params, " " * 8))
    def fit(self, *, inner_iter=..., outer_iter=..., fit_kwargs=...): # -> STLForecastResults:
        """
        Estimate STL and forecasting model parameters.

        Parameters
        ----------\n%(fit_params)s
        fit_kwargs : Dict[str, Any]
            Any additional keyword arguments to pass to ``model``'s ``fit``
            method when estimating the model on the decomposed residuals.

        Returns
        -------
        STLForecastResults
            Results with forecasting methods.
        """
        ...
    


class STLForecastResults:
    """
    Results for forecasting using STL to remove seasonality

    Parameters
    ----------
    stl : STL
        The STL instance used to decompose the data.
    result : DecomposeResult
        The result of applying STL to the data.
    model : Model
        The time series model used to model the non-seasonal dynamics.
    model_result : Results
        Model results instance supporting, at a minimum, ``forecast``.
    """
    def __init__(self, stl: STL, result: DecomposeResult, model, model_result, endog) -> None:
        ...
    
    @property
    def period(self) -> int:
        """The period of the seasonal component"""
        ...
    
    @property
    def stl(self) -> STL:
        """The STL instance used to decompose the time series"""
        ...
    
    @property
    def result(self) -> DecomposeResult:
        """The result of applying STL to the data"""
        ...
    
    @property
    def model(self) -> Any:
        """The model fit to the additively deseasonalized data"""
        ...
    
    @property
    def model_result(self) -> Any:
        """The result class from the estimated model"""
        ...
    
    def summary(self) -> Summary:
        """
        Summary of both the STL decomposition and the model fit.

        Returns
        -------
        Summary
            The summary of the model fit and the STL decomposition.

        Notes
        -----
        Requires that the model's result class supports ``summary`` and
        returns a ``Summary`` object.
        """
        ...
    
    def forecast(self, steps: int = ..., **kwargs: Dict[str, Any]) -> Union[np.ndarray, pd.Series]:
        """
        Out-of-sample forecasts

        Parameters
        ----------
        steps : int, str, or datetime, optional
            If an integer, the number of steps to forecast from the end of the
            sample. Can also be a date string to parse or a datetime type.
            However, if the dates index does not have a fixed frequency, steps
            must be an integer. Default
        **kwargs
            Additional arguments may required for forecasting beyond the end
            of the sample. These arguments are passed into the time series
            model results' ``forecast`` method.

        Returns
        -------
        forecast : {ndarray, Series}
            Out of sample forecasts
        """
        ...
    
    def get_prediction(self, start: Optional[DateLike] = ..., end: Optional[DateLike] = ..., dynamic: Union[bool, DateLike] = ..., **kwargs: Dict[str, Any]): # -> PredictionResults:
        """
        In-sample prediction and out-of-sample forecasting

        Parameters
        ----------
        start : int, str, or datetime, optional
            Zero-indexed observation number at which to start forecasting,
            i.e., the first forecast is start. Can also be a date string to
            parse or a datetime type. Default is the the zeroth observation.
        end : int, str, or datetime, optional
            Zero-indexed observation number at which to end forecasting, i.e.,
            the last forecast is end. Can also be a date string to
            parse or a datetime type. However, if the dates index does not
            have a fixed frequency, end must be an integer index if you
            want out of sample prediction. Default is the last observation in
            the sample.
        dynamic : bool, int, str, or datetime, optional
            Integer offset relative to `start` at which to begin dynamic
            prediction. Can also be an absolute date string to parse or a
            datetime type (these are not interpreted as offsets).
            Prior to this observation, true endogenous values will be used for
            prediction; starting with this observation and continuing through
            the end of prediction, forecasted endogenous values will be used
            instead.
        **kwargs
            Additional arguments may required for forecasting beyond the end
            of the sample. These arguments are passed into the time series
            model results' ``get_prediction`` method.

        Returns
        -------
        PredictionResults
            PredictionResults instance containing in-sample predictions,
            out-of-sample forecasts, and prediction intervals.
        """
        ...
    


