import numpy as np
import healpy as hp

exec(open('envs.py').read())

# full-width half-max in arcmin
# LF1   f027   7.4
# LF1   f039   5.1
# MF1   f093   2.2
# MF2   f145   1.4
# UHF1  f225   1.0
# UHF2  f280   0.9
beams = {
        27: hp.sphtfunc.gauss_beam(fwhm=np.deg2rad(7.4/60), lmax=l_max, pol=False),
        39: hp.sphtfunc.gauss_beam(fwhm=np.deg2rad(5.1/60), lmax=l_max, pol=False),
        90: hp.sphtfunc.gauss_beam(fwhm=np.deg2rad(2.2/60), lmax=l_max, pol=False),
        150: hp.sphtfunc.gauss_beam(fwhm=np.deg2rad(1.4/60), lmax=l_max, pol=False),
        220: hp.sphtfunc.gauss_beam(fwhm=np.deg2rad(1.0/60), lmax=l_max, pol=False),
        280: hp.sphtfunc.gauss_beam(fwhm=np.deg2rad(0.9/60), lmax=l_max, pol=False),
        }

