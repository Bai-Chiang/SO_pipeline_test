#!/usr/bin/env bash

#rm -rf inputs &> /dev/null
#rm -rf outputs &> /dev/null
#
#mkdir -p inputs
#mkdir -p outputs
#
#python get_binned_cls.py

python -m bbpower BBCompSep \
    --cells_coadded=inputs/cls_coadd.fits \
    --cells_noise=inputs/cls_noise.fits \
    --cells_fiducial=inputs/cls_fiducial.fits \
    --cells_coadded_cov=inputs/cls_coadd.fits \
    --output_dir=outputs \
    --config_copy=outputs/config_copy.yml \
    --config=config_emcee.yml

