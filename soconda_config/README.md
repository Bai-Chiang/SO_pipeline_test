[soconda](git@github.com:simonsobs/soconda.git) config

Usage:
- clone soconda
```
git clone --depth 1 git@github.com:simonsobs/soconda.git
```

- create a symlink of `soopercool` config to soconda directory
```
ln -sr soopercool /path/to/soconda/config/
```

- Run soconda and create a conda env called `soopercool` with config `soopercool`
```
./soconda.sh -e soopercool -c soopercool
```
