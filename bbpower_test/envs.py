import numpy as np

num_split = 4
nbins = 100
bin_size = 10
l_max = 2 + bin_size*nbins
ells = np.arange(l_max+1)
ell_eff = np.array([ 2.0 + bin_size * 0.5 * (2*i+1) for i in range(nbins)])
cl2dl = ells*(ells+1)/(2*np.pi)
dl2cl = np.zeros(l_max+1)
dl2cl[1:] = 1/cl2dl[1:]
dl2cl[0] = dl2cl[1]

freq_channels = [27, 39, 90, 150, 220, 280]
n_freq = len(freq_channels)

# window function for Dl
bpw = np.zeros((nbins,l_max+1))
for b in range(nbins):
    l0 = 2 + b*bin_size
    l1 = 2 + (b+1)*bin_size
    #bpw[b,l0:l1] = 1
    bpw[b,l0:l1] = (ells[l0:l1] * (ells[l0:l1] + 1.0))/(2*np.pi*bin_size)

