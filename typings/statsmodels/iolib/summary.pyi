"""
This type stub file was generated by pyright.
"""

def forg(x, prec=...):
    ...

def d_or_f(x, width=...): # -> str:
    """convert number to string with either integer of float formatting

    This is used internally for nobs and degrees of freedom which are usually
    integers but can be float in some cases.

    Parameters
    ----------
    x : int or float
    width : int
        only used if x is nan

    Returns
    -------
    str : str
        number as formatted string
    """
    ...

def summary(self, yname=..., xname=..., title=..., alpha=..., returns=..., model_info=...):
    """
    Parameters
    ----------
    yname : str
            optional, Default is `Y`
    xname : list[str]
            optional, Default is `X.#` for # in p the number of regressors
    Confidance interval : (0,1) not implimented
    title : str
            optional, Defualt is 'Generalized linear model'
    returns : str
              'text', 'table', 'csv', 'latex', 'html'

    Returns
    -------
    Default :
    returns='print'
            Prints the summarirized results

    Option :
    returns='text'
            Prints the summarirized results

    Option :
    returns='table'
             SimpleTable instance : summarizing the fit of a linear model.

    Option :
    returns='csv'
            returns a string of csv of the results, to import into a spreadsheet

    Option :
    returns='latex'
    Not implimented yet

    Option :
    returns='HTML'
    Not implimented yet


    Examples (needs updating)
    --------
    >>> import statsmodels as sm
    >>> data = sm.datasets.longley.load()
    >>> data.exog = sm.add_constant(data.exog)
    >>> ols_results = sm.OLS(data.endog, data.exog).results
    >>> print ols_results.summary()
    ...

    Notes
    -----
    conf_int calculated from normal dist.
    """
    ...

def summary_top(results, title=..., gleft=..., gright=..., yname=..., xname=...):
    '''generate top table(s)


    TODO: this still uses predefined model_methods
    ? allow gleft, gright to be 1 element tuples instead of filling with None?

    '''
    ...

def summary_params(results, yname=..., xname=..., alpha=..., use_t=..., skip_header=..., title=...): # -> SimpleTable:
    '''create a summary table for the parameters

    Parameters
    ----------
    res : results instance
        some required information is directly taken from the result
        instance
    yname : {str, None}
        optional name for the endogenous variable, default is "y"
    xname : {list[str], None}
        optional names for the exogenous variables, default is "var_xx"
    alpha : float
        significance level for the confidence intervals
    use_t : bool
        indicator whether the p-values are based on the Student-t
        distribution (if True) or on the normal distribution (if False)
    skip_headers : bool
        If false (default), then the header row is added. If true, then no
        header row is added.

    Returns
    -------
    params_table : SimpleTable instance
    '''
    ...

def summary_params_frame(results, yname=..., xname=..., alpha=..., use_t=...): # -> DataFrame:
    '''create a summary table for the parameters

    Parameters
    ----------
    res : results instance
        some required information is directly taken from the result
        instance
    yname : {str, None}
        optional name for the endogenous variable, default is "y"
    xname : {list[str], None}
        optional names for the exogenous variables, default is "var_xx"
    alpha : float
        significance level for the confidence intervals
    use_t : bool
        indicator whether the p-values are based on the Student-t
        distribution (if True) or on the normal distribution (if False)
    skip_headers : bool
        If false (default), then the header row is added. If true, then no
        header row is added.

    Returns
    -------
    params_table : SimpleTable instance
    '''
    ...

def summary_params_2d(result, extras=..., endog_names=..., exog_names=..., title=...): # -> SimpleTable:
    '''create summary table of regression parameters with several equations

    This allows interleaving of parameters with bse and/or tvalues

    Parameters
    ----------
    result : result instance
        the result instance with params and attributes in extras
    extras : list[str]
        additional attributes to add below a parameter row, e.g. bse or tvalues
    endog_names : {list[str], None}
        names for rows of the parameter array (multivariate endog)
    exog_names : {list[str], None}
        names for columns of the parameter array (exog)
    alpha : float
        level for confidence intervals, default 0.95
    title : None or string

    Returns
    -------
    tables : list of SimpleTable
        this contains a list of all seperate Subtables
    table_all : SimpleTable
        the merged table with results concatenated for each row of the parameter
        array

    '''
    ...

def summary_params_2dflat(result, endog_names=..., exog_names=..., alpha=..., use_t=..., keep_headers=..., endog_cols=...): # -> tuple[list[Unknown], Unknown]:
    '''summary table for parameters that are 2d, e.g. multi-equation models

    Parameters
    ----------
    result : result instance
        the result instance with params, bse, tvalues and conf_int
    endog_names : {list[str], None}
        names for rows of the parameter array (multivariate endog)
    exog_names : {list[str], None}
        names for columns of the parameter array (exog)
    alpha : float
        level for confidence intervals, default 0.95
    use_t : bool
        indicator whether the p-values are based on the Student-t
        distribution (if True) or on the normal distribution (if False)
    keep_headers : bool
        If true (default), then sub-tables keep their headers. If false, then
        only the first headers are kept, the other headerse are blanked out
    endog_cols : bool
        If false (default) then params and other result statistics have
        equations by rows. If true, then equations are assumed to be in columns.
        Not implemented yet.

    Returns
    -------
    tables : list of SimpleTable
        this contains a list of all seperate Subtables
    table_all : SimpleTable
        the merged table with results concatenated for each row of the parameter
        array

    '''
    ...

def table_extend(tables, keep_headers=...):
    '''extend a list of SimpleTables, adding titles to header of subtables

    This function returns the merged table as a deepcopy, in contrast to the
    SimpleTable extend method.

    Parameters
    ----------
    tables : list of SimpleTable instances
    keep_headers : bool
        If true, then all headers are kept. If falls, then the headers of
        subtables are blanked out.

    Returns
    -------
    table_all : SimpleTable
        merged tables as a single SimpleTable instance

    '''
    ...

def summary_return(tables, return_fmt=...): # -> str:
    ...

class Summary:
    """
    Result summary

    Construction does not take any parameters. Tables and text can be added
    with the `add_` methods.

    Attributes
    ----------
    tables : list of tables
        Contains the list of SimpleTable instances, horizontally concatenated
        tables are not saved separately.
    extra_txt : str
        extra lines that are added to the text output, used for warnings
        and explanations.
    """
    def __init__(self) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self):
        ...
    
    def add_table_2cols(self, res, title=..., gleft=..., gright=..., yname=..., xname=...): # -> None:
        """
        Add a double table, 2 tables with one column merged horizontally

        Parameters
        ----------
        res : results instance
            some required information is directly taken from the result
            instance
        title : str, optional
            if None, then a default title is used.
        gleft : list[tuple], optional
            elements for the left table, tuples are (name, value) pairs
            If gleft is None, then a default table is created
        gright : list[tuple], optional
            elements for the right table, tuples are (name, value) pairs
        yname : str, optional
            optional name for the endogenous variable, default is "y"
        xname : list[str], optional
            optional names for the exogenous variables, default is "var_xx".
            Must match the number of parameters in the model.
        """
        ...
    
    def add_table_params(self, res, yname=..., xname=..., alpha=..., use_t=...): # -> None:
        '''create and add a table for the parameter estimates

        Parameters
        ----------
        res : results instance
            some required information is directly taken from the result
            instance
        yname : {str, None}
            optional name for the endogenous variable, default is "y"
        xname : {list[str], None}
            optional names for the exogenous variables, default is "var_xx"
        alpha : float
            significance level for the confidence intervals
        use_t : bool
            indicator whether the p-values are based on the Student-t
            distribution (if True) or on the normal distribution (if False)

        Returns
        -------
        None : table is attached

        '''
        ...
    
    def add_extra_txt(self, etext): # -> None:
        '''add additional text that will be added at the end in text format

        Parameters
        ----------
        etext : list[str]
            string with lines that are added to the text output.

        '''
        ...
    
    def as_text(self): # -> str | list[Unknown]:
        '''return tables as string

        Returns
        -------
        txt : str
            summary tables and extra text as one string

        '''
        ...
    
    def as_latex(self): # -> str | list[Unknown]:
        '''return tables as string

        Returns
        -------
        latex : str
            summary tables and extra text as string of Latex

        Notes
        -----
        This currently merges tables with different number of columns.
        It is recommended to use `as_latex_tabular` directly on the individual
        tables.

        '''
        ...
    
    def as_csv(self): # -> str | list[Unknown]:
        '''return tables as string

        Returns
        -------
        csv : str
            concatenated summary tables in comma delimited format

        '''
        ...
    
    def as_html(self): # -> str | list[Unknown]:
        '''return tables as string

        Returns
        -------
        html : str
            concatenated summary tables in HTML format

        '''
        ...
    


