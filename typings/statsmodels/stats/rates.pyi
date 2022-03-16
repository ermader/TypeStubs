"""
This type stub file was generated by pyright.
"""

'''Test for ratio of Poisson intensities in two independent samples

Author: Josef Perktold
License: BSD-3

'''
def test_poisson_2indep(count1, exposure1, count2, exposure2, ratio_null=..., method=..., alternative=..., etest_kwds=...):
    '''test for ratio of two sample Poisson intensities

    If the two Poisson rates are g1 and g2, then the Null hypothesis is

    - H0: g1 / g2 = ratio_null

    against one of the following alternatives

    - H1_2-sided: g1 / g2 != ratio_null
    - H1_larger: g1 / g2 > ratio_null
    - H1_smaller: g1 / g2 < ratio_null

    Parameters
    ----------
    count1 : int
        Number of events in first sample.
    exposure1 : float
        Total exposure (time * subjects) in first sample.
    count2 : int
        Number of events in second sample.
    exposure2 : float
        Total exposure (time * subjects) in second sample.
    ratio: float
        ratio of the two Poisson rates under the Null hypothesis. Default is 1.
    method : string
        Method for the test statistic and the p-value. Defaults to `'score'`.
        Current Methods are based on Gu et. al 2008.
        Implemented are 'wald', 'score' and 'sqrt' based asymptotic normal
        distribution, and the exact conditional test 'exact-cond', and its
        mid-point version 'cond-midp'. method='etest' and method='etest-wald'
        provide pvalues from `etest_poisson_2indep` using score or wald
        statistic respectively.
        see Notes.
    alternative : string
        The alternative hypothesis, H1, has to be one of the following

        - 'two-sided': H1: ratio of rates is not equal to ratio_null (default)
        - 'larger' :   H1: ratio of rates is larger than ratio_null
        - 'smaller' :  H1: ratio of rates is smaller than ratio_null
    etest_kwds: dictionary
        Additional parameters to be passed to the etest_poisson_2indep
        function, namely ygrid.

    Returns
    -------
    results : instance of HolderTuple class
        The two main attributes are test statistic `statistic` and p-value
        `pvalue`.

    Notes
    -----
    - 'wald': method W1A, wald test, variance based on separate estimates
    - 'score': method W2A, score test, variance based on estimate under Null
    - 'wald-log': W3A
    - 'score-log' W4A
    - 'sqrt': W5A, based on variance stabilizing square root transformation
    - 'exact-cond': exact conditional test based on binomial distribution
    - 'cond-midp': midpoint-pvalue of exact conditional test
    - 'etest': etest with score test statistic
    - 'etest-wald': etest with wald test statistic

    References
    ----------
    Gu, Ng, Tang, Schucany 2008: Testing the Ratio of Two Poisson Rates,
    Biometrical Journal 50 (2008) 2, 2008

    See Also
    --------
    tost_poisson_2indep
    etest_poisson_2indep
    '''
    ...

def etest_poisson_2indep(count1, exposure1, count2, exposure2, ratio_null=..., method=..., alternative=..., ygrid=...): # -> tuple[Unknown, Unknown]:
    """E-test for ratio of two sample Poisson rates

    If the two Poisson rates are g1 and g2, then the Null hypothesis is

    - H0: g1 / g2 = ratio_null

    against one of the following alternatives

    - H1_2-sided: g1 / g2 != ratio_null
    - H1_larger: g1 / g2 > ratio_null
    - H1_smaller: g1 / g2 < ratio_null

    Parameters
    ----------
    count1 : int
        Number of events in first sample
    exposure1 : float
        Total exposure (time * subjects) in first sample
    count2 : int
        Number of events in first sample
    exposure2 : float
        Total exposure (time * subjects) in first sample
    ratio : float
        ratio of the two Poisson rates under the Null hypothesis. Default is 1.
    method : {"score", "wald"}
        Method for the test statistic that defines the rejection region.
    alternative : string
        The alternative hypothesis, H1, has to be one of the following

           'two-sided': H1: ratio of rates is not equal to ratio_null (default)
           'larger' :   H1: ratio of rates is larger than ratio_null
           'smaller' :  H1: ratio of rates is smaller than ratio_null

    ygrid : None or 1-D ndarray
        Grid values for counts of the Poisson distribution used for computing
        the pvalue. By default truncation is based on an upper tail Poisson
        quantiles.

    Returns
    -------
    stat_sample : float
        test statistic for the sample
    pvalue : float

    References
    ----------
    Gu, Ng, Tang, Schucany 2008: Testing the Ratio of Two Poisson Rates,
    Biometrical Journal 50 (2008) 2, 2008

    """
    ...

def tost_poisson_2indep(count1, exposure1, count2, exposure2, low, upp, method=...): # -> HolderTuple:
    '''Equivalence test based on two one-sided `test_proportions_2indep`

    This assumes that we have two independent binomial samples.

    The Null and alternative hypothesis for equivalence testing are

    - H0: g1 / g2 <= low or upp <= g1 / g2
    - H1: low < g1 / g2 < upp

    where g1 and g2 are the Poisson rates.

    Parameters
    ----------
    count1 : int
        Number of events in first sample
    exposure1 : float
        Total exposure (time * subjects) in first sample
    count2 : int
        Number of events in second sample
    exposure2 : float
        Total exposure (time * subjects) in second sample
    low, upp :
        equivalence margin for the ratio of Poisson rates
    method: string
        Method for the test statistic and the p-value. Defaults to `'score'`.
        Current Methods are based on Gu et. al 2008
        Implemented are 'wald', 'score' and 'sqrt' based asymptotic normal
        distribution, and the exact conditional test 'exact-cond', and its
        mid-point version 'cond-midp', see Notes

    Returns
    -------
    results : instance of HolderTuple class
        The two main attributes are test statistic `statistic` and p-value
        `pvalue`.

    Notes
    -----
    - 'wald': method W1A, wald test, variance based on separate estimates
    - 'score': method W2A, score test, variance based on estimate under Null
    - 'wald-log': W3A  not implemented
    - 'score-log' W4A  not implemented
    - 'sqrt': W5A, based on variance stabilizing square root transformation
    - 'exact-cond': exact conditional test based on binomial distribution
    - 'cond-midp': midpoint-pvalue of exact conditional test

    The latter two are only verified for one-sided example.

    References
    ----------
    Gu, Ng, Tang, Schucany 2008: Testing the Ratio of Two Poisson Rates,
    Biometrical Journal 50 (2008) 2, 2008

    See Also
    --------
    test_poisson_2indep
    '''
    ...

