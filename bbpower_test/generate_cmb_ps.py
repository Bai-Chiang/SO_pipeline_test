#import numpy as np
import camb

#exec(open('envs.py').read())

camb_params_lensed_r0 = camb.set_params(
    cosmomc_theta=0.0104085,
    As=2.1e-9,
    ombh2=0.02237,
    omch2=0.1200,
    ns=0.9649,
    Alens=1.0,
    tau=0.0544,
    r=0.0,
    lmax=l_max,
)
camb_results_lensed_r0 = camb.get_results(camb_params_lensed_r0)
camb_powers_lensed_r0 = camb_results_lensed_r0.get_cmb_power_spectra(camb_params_lensed_r0, CMB_unit='muK', raw_cl=True)

Cl_TT_lensed_r0 = camb_powers_lensed_r0["total"][:, 0][:l_max+1]
Dl_TT_lensed_r0 = cl2dl * Cl_TT_lensed_r0
Cl_EE_lensed_r0 = camb_powers_lensed_r0["total"][:, 1][:l_max+1]
Dl_EE_lensed_r0 = cl2dl * Cl_EE_lensed_r0
Cl_BB_lensed_r0 = camb_powers_lensed_r0["total"][:, 2][:l_max+1]
Dl_BB_lensed_r0 = cl2dl * Cl_BB_lensed_r0
Cl_TE_lensed_r0 = camb_powers_lensed_r0["total"][:, 3][:l_max+1]
Dl_TE_lensed_r0 = cl2dl * Cl_TE_lensed_r0

Cl_TT_lensed_r0_binned = np.sum(Cl_TT_lensed_r0 * bpw, axis=-1)
Cl_EE_lensed_r0_binned = np.sum(Cl_EE_lensed_r0 * bpw, axis=-1)
Cl_BB_lensed_r0_binned = np.sum(Cl_BB_lensed_r0 * bpw, axis=-1)
Cl_TE_lensed_r0_binned = np.sum(Cl_TE_lensed_r0 * bpw, axis=-1)

camb_params_lensed_r1 = camb.set_params(
    cosmomc_theta=0.0104085,
    As=2.1e-9,
    ombh2=0.02237,
    omch2=0.1200,
    ns=0.9649,
    Alens=1.0,
    tau=0.0544,
    r=1.0,
    lmax=l_max,
)
camb_results_lensed_r1 = camb.get_results(camb_params_lensed_r1)
camb_powers_lensed_r1 = camb_results_lensed_r1.get_cmb_power_spectra(camb_params_lensed_r1, CMB_unit='muK', raw_cl=True)

Cl_TT_lensed_r1 = camb_powers_lensed_r1["total"][:, 0][:l_max+1]
Dl_TT_lensed_r1 = cl2dl * Cl_TT_lensed_r1
Cl_EE_lensed_r1 = camb_powers_lensed_r1["total"][:, 1][:l_max+1]
Dl_EE_lensed_r1 = cl2dl * Cl_EE_lensed_r1
Cl_BB_lensed_r1 = camb_powers_lensed_r1["total"][:, 2][:l_max+1]
Dl_BB_lensed_r1 = cl2dl * Cl_BB_lensed_r1
Cl_TE_lensed_r1 = camb_powers_lensed_r1["total"][:, 3][:l_max+1]
Dl_TE_lensed_r1 = cl2dl * Cl_TE_lensed_r1

Cl_TT_lensed_r1_binned = np.sum(Cl_TT_lensed_r1 * bpw, axis=-1)
Cl_EE_lensed_r1_binned = np.sum(Cl_EE_lensed_r1 * bpw, axis=-1)
Cl_BB_lensed_r1_binned = np.sum(Cl_BB_lensed_r1 * bpw, axis=-1)
Cl_TE_lensed_r1_binned = np.sum(Cl_TE_lensed_r1 * bpw, axis=-1)

np.savetxt('inputs/dl_camb_lensed_r0.txt', np.array([ells,Dl_TT_lensed_r0, Dl_EE_lensed_r0, Dl_BB_lensed_r0, Dl_TE_lensed_r0]).T)
np.savetxt('inputs/dl_camb_lensed_r1.txt', np.array([ells,Dl_TT_lensed_r1, Dl_EE_lensed_r1, Dl_BB_lensed_r1, Dl_TE_lensed_r1]).T)
