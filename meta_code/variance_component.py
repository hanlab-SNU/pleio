## Dependancies : 
import numpy as np
from scipy.stats import multivariate_normal 
from scipy.optimize import fminbound

## T is the number of traits
## Sg is the Genetic covariance matrix with the size of [T x T];
## Se is the covariance matrix of error with the size of [T x T];

def is_pos_def( x ):

    '''
    In optimization process, python uses the scipy package to inverse the covariance matrix
    The inverse of a matrix requires the state of positive semi-definite
    In DELPY, covaiance matrix can be Se or tau^2 * Sg + Se
    Thus, We check the state of positive definite for both Sg and Se 
    '''
    
    eigs = np.linalg.eigvals( x )
    return np.all( eigs > 0 )

def likelihood_function ( pars, x, Sg, Se, n ):
    tau = pars;
    genetic_vc = tau * Sg;
    vc = genetic_vc + Se;
    k = multivariate_normal.logpdf( x = x, mean = [0] * n, cov = vc );

    return( -1 * k );

def vcm_optimization ( beta, stders, Sg, Re, n, bnds = [(0,3000)] ):

    '''
    - Variance Component Model Optimization - 
    The function estimates the log-likelihood ratio test statistic
    The convergence of optimizing tau-squared statistics may fail if the number of studies increases
    In that case, we can change the value of 'eps' and 'ftol' 
    llrs: log-likelihood ratio statistic;    ll: log-likelihood;    b: beta;    s: standard errors
    '''

    b = beta; s = stders;
    Se = np.diag( s ).dot( Re ).dot( np.diag( s ) );
    tau, alt_n, ierr,_ = fminbound( func = likelihood_function, x1 = 0 , x2 = 199, args=( b, Sg, Se, n ), xtol = 1e-12, maxfun = 1000, full_output = True, disp = True );
    alt_ll = - 1 * alt_n
    nul_ll = multivariate_normal.logpdf( x = b, mean = [0] * n, cov = Se );
    llrs = max( 2 * ( alt_ll - nul_ll ), 0.0 )

    return( llrs ) 
    #return(nul_ll, alt_ll, llrs, tau);
