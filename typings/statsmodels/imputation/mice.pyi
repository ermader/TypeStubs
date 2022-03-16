"""
This type stub file was generated by pyright.
"""

from statsmodels.base.model import LikelihoodModelResults

"""
Overview
--------

This module implements the Multiple Imputation through Chained
Equations (MICE) approach to handling missing data in statistical data
analyses. The approach has the following steps:

0. Impute each missing value with the mean of the observed values of
the same variable.

1. For each variable in the data set with missing values (termed the
'focus variable'), do the following:

1a. Fit an 'imputation model', which is a regression model for the
focus variable, regressed on the observed and (current) imputed values
of some or all of the other variables.

1b. Impute the missing values for the focus variable.  Currently this
imputation must use the 'predictive mean matching' (pmm) procedure.

2. Once all variables have been imputed, fit the 'analysis model' to
the data set.

3. Repeat steps 1-2 multiple times and combine the results using a
'combining rule' to produce point estimates of all parameters in the
analysis model and standard errors for them.

The imputations for each variable are based on an imputation model
that is specified via a model class and a formula for the regression
relationship.  The default model is OLS, with a formula specifying
main effects for all other variables.

The MICE procedure can be used in one of two ways:

* If the goal is only to produce imputed data sets, the MICEData class
can be used to wrap a data frame, providing facilities for doing the
imputation.  Summary plots are available for assessing the performance
of the imputation.

* If the imputed data sets are to be used to fit an additional
'analysis model', a MICE instance can be used.  After specifying the
MICE instance and running it, the results are combined using the
`combine` method.  Results and various summary plots are then
available.

Terminology
-----------

The primary goal of the analysis is usually to fit and perform
inference using an 'analysis model'. If an analysis model is not
specified, then imputed datasets are produced for later use.

The MICE procedure involves a family of imputation models.  There is
one imputation model for each variable with missing values.  An
imputation model may be conditioned on all or a subset of the
remaining variables, using main effects, transformations,
interactions, etc. as desired.

A 'perturbation method' is a method for setting the parameter estimate
in an imputation model.  The 'gaussian' perturbation method first fits
the model (usually using maximum likelihood, but it could use any
statsmodels fit procedure), then sets the parameter vector equal to a
draw from the Gaussian approximation to the sampling distribution for
the fit.  The 'bootstrap' perturbation method sets the parameter
vector equal to a fitted parameter vector obtained when fitting the
conditional model to a bootstrapped version of the data set.

Class structure
---------------

There are two main classes in the module:

* 'MICEData' wraps a Pandas dataframe, incorporating information about
  the imputation model for each variable with missing values. It can
  be used to produce multiply imputed data sets that are to be further
  processed or distributed to other researchers.  A number of plotting
  procedures are provided to visualize the imputation results and
  missing data patterns.  The `history_func` hook allows any features
  of interest of the imputed data sets to be saved for further
  analysis.

* 'MICE' takes both a 'MICEData' object and an analysis model
  specification.  It runs the multiple imputation, fits the analysis
  models, and combines the results to produce a `MICEResults` object.
  The summary method of this results object can be used to see the key
  estimands and inferential quantities.

Notes
-----

By default, to conserve memory 'MICEData' saves very little
information from one iteration to the next.  The data set passed by
the user is copied on entry, but then is over-written each time new
imputations are produced.  If using 'MICE', the fitted
analysis models and results are saved.  MICEData includes a
`history_callback` hook that allows arbitrary information from the
intermediate datasets to be saved for future use.

References
----------

JL Schafer: 'Multiple Imputation: A Primer', Stat Methods Med Res,
1999.

TE Raghunathan et al.: 'A Multivariate Technique for Multiply
Imputing Missing Values Using a Sequence of Regression Models', Survey
Methodology, 2001.

SAS Institute: 'Predictive Mean Matching Method for Monotone Missing
Data', SAS 9.2 User's Guide, 2014.

A Gelman et al.: 'Multiple Imputation with Diagnostics (mi) in R:
Opening Windows into the Black Box', Journal of Statistical Software,
2009.
"""
_mice_data_example_1 = ...
class PatsyFormula:
    """
    A simple wrapper for a string to be interpreted as a Patsy formula.
    """
    def __init__(self, formula) -> None:
        ...
    


class MICEData:
    __doc__ = ...
    def __init__(self, data, perturbation_method=..., k_pmm=..., history_callback=...) -> None:
        ...
    
    def next_sample(self):
        """
        Returns the next imputed dataset in the imputation process.

        Returns
        -------
        data : array_like
            An imputed dataset from the MICE chain.

        Notes
        -----
        `MICEData` does not have a `skip` parameter.  Consecutive
        values returned by `next_sample` are immediately consecutive
        in the imputation chain.

        The returned value is a reference to the data attribute of
        the class and should be copied before making any changes.
        """
        ...
    
    def set_imputer(self, endog_name, formula=..., model_class=..., init_kwds=..., fit_kwds=..., predict_kwds=..., k_pmm=..., perturbation_method=..., regularized=...): # -> None:
        """
        Specify the imputation process for a single variable.

        Parameters
        ----------
        endog_name : str
            Name of the variable to be imputed.
        formula : str
            Conditional formula for imputation. Defaults to a formula
            with main effects for all other variables in dataset.  The
            formula should only include an expression for the mean
            structure, e.g. use 'x1 + x2' not 'x4 ~ x1 + x2'.
        model_class : statsmodels model
            Conditional model for imputation. Defaults to OLS.  See below
            for more information.
        init_kwds : dit-like
            Keyword arguments passed to the model init method.
        fit_kwds : dict-like
            Keyword arguments passed to the model fit method.
        predict_kwds : dict-like
            Keyword arguments passed to the model predict method.
        k_pmm : int
            Determines number of neighboring observations from which
            to randomly sample when using predictive mean matching.
        perturbation_method : str
            Either 'gaussian' or 'bootstrap'. Determines the method
            for perturbing parameters in the imputation model.  If
            None, uses the default specified at class initialization.
        regularized : dict
            If regularized[name]=True, `fit_regularized` rather than
            `fit` is called when fitting imputation models for this
            variable.  When regularized[name]=True for any variable,
            perturbation_method must be set to boot.

        Notes
        -----
        The model class must meet the following conditions:
            * A model must have a 'fit' method that returns an object.
            * The object returned from `fit` must have a `params` attribute
              that is an array-like object.
            * The object returned from `fit` must have a cov_params method
              that returns a square array-like object.
            * The model must have a `predict` method.
        """
        ...
    
    def update_all(self, n_iter=...): # -> None:
        """
        Perform a specified number of MICE iterations.

        Parameters
        ----------
        n_iter : int
            The number of updates to perform.  Only the result of the
            final update will be available.

        Notes
        -----
        The imputed values are stored in the class attribute `self.data`.
        """
        ...
    
    def get_split_data(self, vname): # -> tuple[NDArray[_SCT@asarray], NDArray[_SCT@asarray], NDArray[_SCT@asarray], Unknown | dict[Unknown, Unknown], Unknown | dict[Unknown, Unknown]]:
        """
        Return endog and exog for imputation of a given variable.

        Parameters
        ----------
        vname : str
           The variable for which the split data is returned.

        Returns
        -------
        endog_obs : DataFrame
            Observed values of the variable to be imputed.
        exog_obs : DataFrame
            Current values of the predictors where the variable to be
            imputed is observed.
        exog_miss : DataFrame
            Current values of the predictors where the variable to be
            Imputed is missing.
        init_kwds : dict-like
            The init keyword arguments for `vname`, processed through Patsy
            as required.
        fit_kwds : dict-like
            The fit keyword arguments for `vname`, processed through Patsy
            as required.
        """
        ...
    
    def get_fitting_data(self, vname): # -> tuple[NDArray[_SCT@asarray], NDArray[_SCT@asarray], dict[Unknown, Unknown], dict[Unknown, Unknown]]:
        """
        Return the data needed to fit a model for imputation.

        The data is used to impute variable `vname`, and therefore
        only includes cases for which `vname` is observed.

        Values of type `PatsyFormula` in `init_kwds` or `fit_kwds` are
        processed through Patsy and subset to align with the model's
        endog and exog.

        Parameters
        ----------
        vname : str
           The variable for which the fitting data is returned.

        Returns
        -------
        endog : DataFrame
            Observed values of `vname`.
        exog : DataFrame
            Regression design matrix for imputing `vname`.
        init_kwds : dict-like
            The init keyword arguments for `vname`, processed through Patsy
            as required.
        fit_kwds : dict-like
            The fit keyword arguments for `vname`, processed through Patsy
            as required.
        """
        ...
    
    def plot_missing_pattern(self, ax=..., row_order=..., column_order=..., hide_complete_rows=..., hide_complete_columns=..., color_row_patterns=...):
        """
        Generate an image showing the missing data pattern.

        Parameters
        ----------
        ax : AxesSubplot
            Axes on which to draw the plot.
        row_order : str
            The method for ordering the rows.  Must be one of 'pattern',
            'proportion', or 'raw'.
        column_order : str
            The method for ordering the columns.  Must be one of 'pattern',
            'proportion', or 'raw'.
        hide_complete_rows : bool
            If True, rows with no missing values are not drawn.
        hide_complete_columns : bool
            If True, columns with no missing values are not drawn.
        color_row_patterns : bool
            If True, color the unique row patterns, otherwise use grey
            and white as colors.

        Returns
        -------
        A figure containing a plot of the missing data pattern.
        """
        ...
    
    def plot_bivariate(self, col1_name, col2_name, lowess_args=..., lowess_min_n=..., jitter=..., plot_points=..., ax=...):
        """
        Plot observed and imputed values for two variables.

        Displays a scatterplot of one variable against another.  The
        points are colored according to whether the values are
        observed or imputed.

        Parameters
        ----------
        col1_name : str
            The variable to be plotted on the horizontal axis.
        col2_name : str
            The variable to be plotted on the vertical axis.
        lowess_args : dictionary
            A dictionary of dictionaries, keys are 'ii', 'io', 'oi'
            and 'oo', where 'o' denotes 'observed' and 'i' denotes
            imputed.  See Notes for details.
        lowess_min_n : int
            Minimum sample size to plot a lowess fit
        jitter : float or tuple
            Standard deviation for jittering points in the plot.
            Either a single scalar applied to both axes, or a tuple
            containing x-axis jitter and y-axis jitter, respectively.
        plot_points : bool
            If True, the data points are plotted.
        ax : AxesSubplot
            Axes on which to plot, created if not provided.

        Returns
        -------
        The matplotlib figure on which the plot id drawn.
        """
        ...
    
    def plot_fit_obs(self, col_name, lowess_args=..., lowess_min_n=..., jitter=..., plot_points=..., ax=...):
        """
        Plot fitted versus imputed or observed values as a scatterplot.

        Parameters
        ----------
        col_name : str
            The variable to be plotted on the horizontal axis.
        lowess_args : dict-like
            Keyword arguments passed to lowess fit.  A dictionary of
            dictionaries, keys are 'o' and 'i' denoting 'observed' and
            'imputed', respectively.
        lowess_min_n : int
            Minimum sample size to plot a lowess fit
        jitter : float or tuple
            Standard deviation for jittering points in the plot.
            Either a single scalar applied to both axes, or a tuple
            containing x-axis jitter and y-axis jitter, respectively.
        plot_points : bool
            If True, the data points are plotted.
        ax : AxesSubplot
            Axes on which to plot, created if not provided.

        Returns
        -------
        The matplotlib figure on which the plot is drawn.
        """
        ...
    
    def plot_imputed_hist(self, col_name, ax=..., imp_hist_args=..., obs_hist_args=..., all_hist_args=...):
        """
        Display imputed values for one variable as a histogram.

        Parameters
        ----------
        col_name : str
            The name of the variable to be plotted.
        ax : AxesSubplot
            An axes on which to draw the histograms.  If not provided,
            one is created.
        imp_hist_args : dict
            Keyword arguments to be passed to pyplot.hist when
            creating the histogram for imputed values.
        obs_hist_args : dict
            Keyword arguments to be passed to pyplot.hist when
            creating the histogram for observed values.
        all_hist_args : dict
            Keyword arguments to be passed to pyplot.hist when
            creating the histogram for all values.

        Returns
        -------
        The matplotlib figure on which the histograms were drawn
        """
        ...
    
    def perturb_params(self, vname): # -> None:
        ...
    
    def impute(self, vname): # -> None:
        ...
    
    def update(self, vname): # -> None:
        """
        Impute missing values for a single variable.

        This is a two-step process in which first the parameters are
        perturbed, then the missing values are re-imputed.

        Parameters
        ----------
        vname : str
            The name of the variable to be updated.
        """
        ...
    
    def impute_pmm(self, vname): # -> None:
        """
        Use predictive mean matching to impute missing values.

        Notes
        -----
        The `perturb_params` method must be called first to define the
        model.
        """
        ...
    


_mice_example_1 = ...
_mice_example_2 = ...
class MICE:
    __doc__ = ...
    def __init__(self, model_formula, model_class, data, n_skip=..., init_kwds=..., fit_kwds=...) -> None:
        ...
    
    def next_sample(self):
        """
        Perform one complete MICE iteration.

        A single MICE iteration updates all missing values using their
        respective imputation models, then fits the analysis model to
        the imputed data.

        Returns
        -------
        params : array_like
            The model parameters for the analysis model.

        Notes
        -----
        This function fits the analysis model and returns its
        parameter estimate.  The parameter vector is not stored by the
        class and is not used in any subsequent calls to `combine`.
        Use `fit` to run all MICE steps together and obtain summary
        results.

        The complete cycle of missing value imputation followed by
        fitting the analysis model is repeated `n_skip + 1` times and
        the analysis model parameters from the final fit are returned.
        """
        ...
    
    def fit(self, n_burnin=..., n_imputations=...): # -> MICEResults:
        """
        Fit a model using MICE.

        Parameters
        ----------
        n_burnin : int
            The number of burn-in cycles to skip.
        n_imputations : int
            The number of data sets to impute
        """
        ...
    
    def combine(self): # -> MICEResults:
        """
        Pools MICE imputation results.

        This method can only be used after the `run` method has been
        called.  Returns estimates and standard errors of the analysis
        model parameters.

        Returns a MICEResults instance.
        """
        ...
    


class MICEResults(LikelihoodModelResults):
    def __init__(self, model, params, normalized_cov_params) -> None:
        ...
    
    def summary(self, title=..., alpha=...): # -> Summary:
        """
        Summarize the results of running MICE.

        Parameters
        ----------
        title : str, optional
            Title for the top table. If not None, then this replaces
            the default title
        alpha : float
            Significance level for the confidence intervals

        Returns
        -------
        smry : Summary instance
            This holds the summary tables and text, which can be
            printed or converted to various output formats.
        """
        ...
    


