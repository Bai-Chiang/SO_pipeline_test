import noise_calc

exec(open('envs.py').read())

Nell = np.zeros((n_freq,l_max+1))

# sensitivity_mode
#     1: baseline,
#     2: goal
# one_over_f_mode
#     0: pessimistic
#     1: optimistic
# SAT_yrs_LF: 0,1,2,3,4,5:  number of years where an LF is deployed on SAT
# f_sky:  number from 0-1
# ell_max: the maximum value of ell used in the computation of N(ell)
# delta_ell: the step size for computing N_ell
_, Nell[:,2:], _ = noise_calc.Simons_Observatory_V3_SA_noise(
        sensitivity_mode=2,
        one_over_f_mode=1,
        SAT_yrs_LF=1,
        f_sky=0.1,
        ell_max=l_max+1,
        delta_ell=1
        )

# Nell.shape = (#freq channel, #ell)
# bpw.shape = (#bins, #ell)
Nell_binned = np.sum(Nell[:,None,:] * bpw, axis=-1)

# n_freq channel 2 polarization (EE,BB) n_freq 2 pol bins
Nell_bands = np.zeros((n_freq,2,n_freq,2,nbins))
for i in range(n_freq):
    Nell_bands[i,0,i,0,:] = Nell_binned[i,:]
    Nell_bands[i,1,i,1,:] = Nell_binned[i,:]

exec(open('bandpass.py').read())
CNell_bands = cl_bands + Nell_bands

# covariance matrix
def is_cross(s1,f1,s2,f2):
    if s1 != s2:
        return True
    else:
        if f1 != f2:
            return True
        else:
            return False

def get_cross_splits(f1,f2):
    if f1 == f2:
        # If freq are the same, then all cross pairs would have different
        # split, so the number of total cross pairs is:
        num_cross = num_split*(num_split-1)/2
        split_pairs = np.triu_indices(num_split,1)
        assert num_cross == split_pairs[0].size
        return split_pairs, num_cross
    else:
        # If freq are different, then any split combination will be cross pair,
        # so the number of total cross pairs is:
        num_cross = num_split**2
        split_pairs = np.triu_indices(num_split,-num_split)
        assert num_cross == split_pairs[0].size
        return split_pairs, num_cross

i_pairs = np.triu_indices(n_freq*2)
n_pairs = len(i_pairs[0])
cov = np.zeros((n_pairs,nbins,n_pairs,nbins))
for i,(m1,m2) in enumerate(zip(i_pairs[0], i_pairs[1])):
    for j,(m3,m4) in enumerate(zip(i_pairs[0], i_pairs[1])):
        f1 = m1//2
        p1 = m1%2
        f2 = m2//2
        p2 = m2%2
        f3 = m3//2
        p3 = m3%2
        f4 = m4//2
        p4 = m4%2
        split_pairs_12, num_cross_12 = get_cross_splits(f1,f2)
        split_pairs_34, num_cross_34 = get_cross_splits(f3,f4)
        for s_alpha, s_beta in zip(*split_pairs_12):
            for s_mu, s_nu in zip(*split_pairs_34):
                if is_cross(s_alpha, f1, s_mu, f3):
                    Cell_13 = cl_bands[f1,p1,f3,p3,:]
                else:
                    Cell_13 = CNell_bands[f1,p1,f3,p3,:]

                if is_cross(s_beta, f2, s_nu, f4):
                    Cell_24 = cl_bands[f2,p2,f4,p4,:]
                else:
                    Cell_24 = CNell_bands[f2,p2,f4,p4,:]

                if is_cross(s_alpha, f1, s_nu, f4):
                    Cell_14 = cl_bands[f1,p1,f4,p4,:]
                else:
                    Cell_14 = CNell_bands[f1,p1,f4,p4,:]

                if is_cross(s_beta, f2, s_mu, f3):
                    Cell_23 = cl_bands[f2,p2,f3,p3,:]
                else:
                    Cell_23 = CNell_bands[f2,p2,f3,p3,:]

                cov[i,:,j,:] += np.diag(
                        1/(2*ell_eff+1) * (1/num_cross_12) * (1/num_cross_34)
                        * ( Cell_13 * Cell_24 + Cell_14 * Cell_23)
                        )
