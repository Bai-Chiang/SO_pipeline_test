#import numpy as np

#exec(open('envs.py').read())

l0_sync = 80.0
alpha_sync_EE = -0.6
alpha_sync_BB = -0.4
A_sync_BB = 2.0
EB_sync = 2.0
A_sync_EE = A_sync_BB*EB_sync

Dl_EE_sync = np.zeros(l_max + 1)
Dl_EE_sync[1:] = A_sync_EE * (ells[1:]/l0_sync)**alpha_sync_EE
Dl_EE_sync[0] = Dl_EE_sync[1]
Cl_EE_sync = dl2cl * Dl_EE_sync

Dl_BB_sync = np.zeros(l_max + 1)
Dl_BB_sync[1:] = A_sync_BB * (ells[1:]/l0_sync)**alpha_sync_BB
Dl_BB_sync[0] = Dl_BB_sync[1]
Cl_BB_sync = dl2cl * Dl_BB_sync


Cl_EE_sync_binned = np.sum(Cl_EE_sync * bpw, axis=-1)
Cl_BB_sync_binned = np.sum(Cl_BB_sync * bpw, axis=-1)
