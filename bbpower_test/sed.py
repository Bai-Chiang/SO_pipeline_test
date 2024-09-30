#import numpy as np

def sed_cmb(nu):
    # CMB
    # x = h * nv / (kB * Theta_CMB )
    x = 0.017608676067552197*nu
    ex = np.exp(x)
    return ex * (x/(np.expm1(x)))**2

def sed_sync(nu, nu0, beta):
    return (nu/nu0)**beta * sed_cmb(nu0)

def sed_dust(nu, nu0, beta, temp):
    x0 = 0.04799244662211351*nu0/temp
    ex0 = np.exp(x0)
    x = 0.04799244662211351*nu/temp
    ex = np.exp(x)
    return (nu/nu0)**(beta+1) * (ex0-1)/(ex-1) * sed_cmb(nu0)
