"""
This type stub file was generated by pyright.
"""

"""
"Cholesky Factor Algorithm" (CFA) simulation smoothing for state space models

Author: Chad Fulton
License: BSD-3
"""
class CFASimulationSmoother:
    r"""
    "Cholesky Factor Algorithm" (CFA) simulation smoother

    Parameters
    ----------
    model : Representation
        The state space model.

    Notes
    -----
    This class allows simulation smoothing by the "Cholesky Factor Algorithm"
    (CFA) described in [1]_ and [2]_, which essentially takes advantage of the
    existence of an efficient sparse Cholesky factor algorithm for banded
    matrices that are held in a sparse matrix format.

    In particular, this simulation smoother computes the joint posterior mean
    and covariance matrix for the unobserved state vector all at once, rather
    than using the recursive computations of the Kalman filter and smoother. It
    then uses these posterior moments to sample directly from this joint
    posterior. For some models, it can be more computationally efficient than
    the simulation smoother based on the Kalman filter and smoother.

    **Important caveat**:

    However, this simulation smoother cannot be used with all state space
    models, including several of the most popular. In particular, the CFA
    algorithm cannot support degenerate distributions (i.e. positive
    semi-definite covariance matrices) for the initial state (which is the
    prior for the first state) or the observation or state innovations.

    One practical problem with this algorithm is that an autoregressive term
    with order higher than one is typically put into state space form by
    augmenting the states using identities. As identities, these augmenting
    terms will not be subject to random innovations, and so the state
    innovation will be degenerate. It is possible to take these higher order
    terms directly into account when constructing the posterior covariance
    matrix, but this has not yet been implemented.

    Similarly, some state space forms of SARIMA and VARMA models make
    the observation equation an identity, which is not compatible with the CFA
    simulation smoothing approach.

    This simulation smoother has so-far found most of its use with dynamic
    factor and stochastic volatility models, which satisfy the restrictions
    described above.

    **Not-yet-implemented**:

    There are several features that are not yet available with this simulation
    smoother:

    - It does not yet allow diffuse initialization of the state vector.
    - It produces simulated states only for exactly the observations in the
      model (i.e. it cannot produce simulations for a subset of the model
      observations or for observations outside the model).


    References
    ----------
    .. [1] McCausland, William J., Shirley Miller, and Denis Pelletier.
           "Simulation smoothing for state-space models: A computational
           efficiency analysis."
           Computational Statistics & Data Analysis 55, no. 1 (2011): 199-212.
    .. [2] Chan, Joshua CC, and Ivan Jeliazkov.
           "Efficient simulation and integrated likelihood estimation in
           state space models."
           International Journal of Mathematical Modelling and Numerical
           Optimisation 1, no. 1-2 (2009): 101-120.
    """
    def __init__(self, model, cfa_simulation_smoother_classes=...) -> None:
        ...
    
    @property
    def posterior_mean(self): # -> NDArray[_SCT@array]:
        r"""
        Posterior mean of the states conditional on the data

        Notes
        -----

        .. math::

            \hat \alpha_t = E[\alpha_t \mid Y^n ]

        This posterior mean is identical to the `smoothed_state` computed by
        the Kalman smoother.
        """
        ...
    
    @property
    def posterior_cov_inv_chol_sparse(self): # -> NDArray[_SCT@array]:
        r"""
        Sparse Cholesky factor of inverse posterior covariance matrix

        Notes
        -----
        This attribute holds in sparse diagonal banded storage the Cholesky
        factor of the inverse of the posterior covariance matrix. If we denote
        :math:`P = Var[\alpha \mid Y^n ]`, then the this attribute holds the
        lower Cholesky factor :math:`L`, defined from :math:`L L' = P^{-1}`.
        This attribute uses the sparse diagonal banded storage described in the
        documentation of, for example, the SciPy function
        `scipy.linalg.solveh_banded`.
        """
        ...
    
    @property
    def posterior_cov(self):
        r"""
        Posterior covariance of the states conditional on the data

        Notes
        -----
        **Warning**: the matrix computed when accessing this property can be
        extremely large: it is shaped `(nobs * k_states, nobs * k_states)`. In
        most cases, it is better to use the `posterior_cov_inv_chol_sparse`
        property if possible, which holds in sparse diagonal banded storage
        the Cholesky factor of the inverse of the posterior covariance matrix.

        .. math::

            Var[\alpha \mid Y^n ]

        This posterior covariance matrix is *not* identical to the
        `smoothed_state_cov` attribute produced by the Kalman smoother, because
        it additionally contains all cross-covariance terms. Instead,
        `smoothed_state_cov` contains the `(k_states, k_states)` block
        diagonal entries of this posterior covariance matrix.
        """
        ...
    
    def simulate(self, variates=..., update_posterior=...): # -> None:
        r"""
        Perform simulation smoothing (via Cholesky factor algorithm)

        Does not return anything, but populates the object's `simulated_state`
        attribute, and also makes available the attributes `posterior_mean`,
        `posterior_cov`, and `posterior_cov_inv_chol_sparse`.

        Parameters
        ----------
        variates : array_like, optional
            Random variates, distributed standard Normal. Usually only
            specified if results are to be replicated (e.g. to enforce a seed)
            or for testing. If not specified, random variates are drawn. Must
            be shaped (nobs, k_states).

        Notes
        -----
        The first step in simulating from the joint posterior of the state
        vector conditional on the data is to compute the two relevant moments
        of the joint posterior distribution:

        .. math::

            \alpha \mid Y_n \sim N(\hat \alpha, Var(\alpha \mid Y_n))

        Let :math:`L L' = Var(\alpha \mid Y_n)^{-1}`. Then simulation proceeds
        according to the following steps:

        1. Draw :math:`u \sim N(0, I)`
        2. Compute :math:`x = \hat \alpha + (L')^{-1} u`

        And then :math:`x` is a draw from the joint posterior of the states.
        The output of the function is as follows:

        - The simulated draw :math:`x` is held in the `simulated_state`
          attribute.
        - The posterior mean :math:`\hat \alpha` is held in the
          `posterior_mean` attribute.
        - The (lower triangular) Cholesky factor of the inverse posterior
          covariance matrix, :math:`L`, is held in sparse diagonal banded
          storage in the `posterior_cov_inv_chol` attribute.
        - The posterior covariance matrix :math:`Var(\alpha \mid Y_n)` can be
          computed on demand by accessing the `posterior_cov` property. Note
          that this matrix can be extremely large, so care must be taken when
          accessing this property. In most cases, it will be preferred to make
          use of the `posterior_cov_inv_chol` attribute rather than the
          `posterior_cov` attribute.

        """
        ...
    

