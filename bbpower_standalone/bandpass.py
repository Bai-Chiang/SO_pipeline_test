import numpy as np

exec(open('envs.py').read())
exec(open('sed.py').read())

# LF1   f027
# LF2   f039
# MF1   f090
# MF2   f150
# UHF1  f220
# UHF2  f280
bandpass = {
        27: np.array([
            np.linspace(20.25, 60, 160, endpoint=True),
            (np.linspace(20.25, 60, 160, endpoint=True) == 27).astype(float)
            ]),
        39: np.array([
            np.linspace(20.25, 60, 160, endpoint=True),
            (np.linspace(20.25, 60, 160, endpoint=True) == 39).astype(float)
            ]),
        90: np.array([
            np.linspace(60, 220, 81, endpoint=True),
            (np.linspace(60, 220, 81, endpoint=True) == 90).astype(float)
            ]),
        150: np.array([
            np.linspace(60, 220, 81, endpoint=True),
            (np.linspace(60, 220, 81, endpoint=True) == 150).astype(float)
            ]),
        220: np.array([
            np.linspace(150, 350, 401, endpoint=True),
            (np.linspace(150, 350, 401, endpoint=True) == 220).astype(float)
            ]),
        280: np.array([
            np.linspace(150, 350, 401, endpoint=True),
            (np.linspace(150, 350, 401, endpoint=True) == 280).astype(float)
            ]),
        }

# normalize bandpass
for i in bandpass:
    nu = bandpass[i][0]
    dnu = nu[1] - nu[0]
    bp = bandpass[i][1]
    norm = np.sum( dnu * bp * nu**2 * sed_cmb(nu))
    bandpass[i][1] /= norm


# Beams
exec(open('sed.py').read())

nu0_sync = 23.0
beta_sync = -3.0
nu0_dust = 353.0
beta_dust = 1.59
temp_dust = 19.6

# 3 components for each freq channel
sed_bands = np.zeros((n_freq,3))
for i,n in enumerate(bandpass):
    nu = bandpass[n][0]
    dnu = nu[1] - nu[0]
    bp = bandpass[n][1]
    sed_bands[i,:] = np.array([
        np.sum( dnu * bp * nu**2 * sed_cmb(nu)),
        np.sum( dnu * bp * nu**2 * sed_sync(nu, nu0=nu0_sync, beta=beta_sync)),
        np.sum( dnu * bp * nu**2 * sed_dust(nu, nu0=nu0_dust, beta=beta_dust, temp=temp_dust))
        ])

exec(open('generate_cmb_ps.py').read())
exec(open('generate_sync_ps.py').read())
exec(open('generate_dust_ps.py').read())
# 3 components 2 polarization (EE,BB)
cl_binned = np.zeros((3,2,3,2,nbins))
# CMB
cl_binned[0,0,0,0,:] = Cl_EE_lensed_r0_binned
cl_binned[0,1,0,1,:] = Cl_BB_lensed_r0_binned
# Sync
cl_binned[1,0,1,0,:] = Cl_EE_sync_binned
cl_binned[1,1,1,1,:] = Cl_BB_sync_binned
# Dust
cl_binned[2,0,2,0,:] = Cl_EE_dust_binned
cl_binned[2,1,2,1,:] = Cl_BB_dust_binned

# dl_bands.shape = ( #freq #pol #freq #pol #bin )
cl_bands = np.einsum('fc,nk,cpkql->fpnql',
        sed_bands,
        sed_bands,
        cl_binned,
        )


