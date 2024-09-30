#import numpy as np

#exec(open('envs.py').read())

l0_dust = 80.0
alpha_dust_EE = -0.42
alpha_dust_BB = -0.2
A_dust_BB = 5.0
EB_dust = 2.0
A_dust_EE = A_dust_BB*EB_dust

Dl_EE_dust = np.zeros(l_max + 1)
Dl_EE_dust[1:] = A_dust_EE * (ells[1:]/l0_dust)**alpha_dust_EE
Dl_EE_dust[0] = Dl_EE_dust[1]
Cl_EE_dust = dl2cl * Dl_EE_dust

Dl_BB_dust = np.zeros(l_max + 1)
Dl_BB_dust[1:] = A_dust_BB * (ells[1:]/l0_dust)**alpha_dust_BB
Dl_BB_dust[0] = Dl_BB_dust[1]
Cl_BB_dust = dl2cl * Dl_BB_dust


Cl_EE_dust_binned = np.sum(Cl_EE_dust * bpw, axis=-1)
Cl_BB_dust_binned = np.sum(Cl_BB_dust * bpw, axis=-1)
