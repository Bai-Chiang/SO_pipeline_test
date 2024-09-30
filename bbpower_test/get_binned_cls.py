import numpy as np
import sacc

exec(open('envs.py').read())

exec(open('generate_cmb_ps.py').read())
exec(open('generate_dust_ps.py').read())
exec(open('generate_sync_ps.py').read())

exec(open('sed.py').read())
exec(open('cl_bands.py').read())

sacc_coadded = sacc.Sacc()
sacc_fiducial = sacc.Sacc()
sacc_noise = sacc.Sacc()

# Add tracers
exec(open('beams.py').read())
for i in freq_channels:
    bp = bandpass[i]
    bm = beams[i]

    for s in [sacc_coadded, sacc_fiducial, sacc_noise]:
        s.add_tracer(
                tracer_type='NuMap',
                name='band{:03d}'.format(i),
                quantity='cmb_polarization',
                spin=2,
                nu=bp[0],
                bandpass=bp[1],
                ell=ells,
                beam=bm,
                nu_unit='GHz',
                map_unit='uK_CMB',
                )

# Add power spectra
# Get unique map pairs (2 polarizations for each freq channel)
exec(open('noise.py').read())
i_pairs = np.triu_indices(n_freq*2)
for i,j in zip(i_pairs[0], i_pairs[1]):
    f1 = i//2
    f2 = j//2
    p1 = i%2
    p2 = j%2
    cl_type = 'cl_'
    cl_type += 'e' if p1 == 0 else 'b'
    cl_type += 'e' if p2 == 0 else 'b'

    sacc_coadded.add_ell_cl(
            data_type=cl_type,
            tracer1='band{:03d}'.format(freq_channels[f1]),
            tracer2='band{:03d}'.format(freq_channels[f2]),
            ell=ell_eff,
            x=cl_bands[f1,p1,f2,p2,:],
            window=sacc.BandpowerWindow(ells, bpw.T)
            )
    sacc_fiducial.add_ell_cl(
            data_type=cl_type,
            tracer1='band{:03d}'.format(freq_channels[f1]),
            tracer2='band{:03d}'.format(freq_channels[f2]),
            ell=ell_eff,
            x=cl_bands[f1,p1,f2,p2,:],
            window=sacc.BandpowerWindow(ells, bpw.T)
            )
    sacc_noise.add_ell_cl(
            data_type=cl_type,
            tracer1='band{:03d}'.format(freq_channels[f1]),
            tracer2='band{:03d}'.format(freq_channels[f2]),
            ell=ell_eff,
            x=Nell_bands[f1,p1,f2,p2,:],
            window=sacc.BandpowerWindow(ells, bpw.T)
            )

# Add covariance
sacc_coadded.add_covariance(covariance=cov.reshape(n_pairs*nbins, n_pairs*nbins))

sacc_coadded.save_fits('inputs/cls_coadd.fits', overwrite=True)
sacc_fiducial.save_fits('inputs/cls_fiducial.fits', overwrite=True)
sacc_noise.save_fits('inputs/cls_noise.fits', overwrite=True)

