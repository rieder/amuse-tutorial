def prerequisites(MPI):
    text = """In macOS, we use macports to install dependencies. 
Other methods (e.g. Homebrew) will probably work just as well, but we have not tested these.
    
In the example below, we use GCC version 7, but other versions will also work.

```bash

sudo port install gcc7
    
sudo port install python27
sudo port install fftw-3 +gcc7
sudo port install hdf5 gsl cmake gmp mpfr
sudo port install py27-numpy py27-h5py py27-nose py27-docutils
sudo port install py27-matplotlib
sudo port install py27-pandas py27-seaborn
"""
    if MPI=="openmpi":
        text += """
sudo port install openmpi-gcc7
sudo port install py27-mpi4py +gcc7 +openmpi"""
    elif MPI=="mpich":
        text += """
sudo port install mpich-gcc7
sudo port install py27-mpi4py +gcc7 +mpich"""
    text +="""
```

To make sure the right MacPorts compilers and python are set as default, do the following:

```bash"""
    if MPI=="openmpi":
        text += """
sudo port select --set mpi openmpi-gcc7-fortran"""
    elif MPI=="mpich":
        text += """
sudo port select --set mpi mpich-gcc7"""
    text += """
sudo port select --set gcc mp-gcc7
sudo port select --set python python27
sudo port select --set nosetests nosetests27

```

After installing you will need to configure the code with the following line:

```bash

./configure --with-fftw=/opt/local
```"""
    return text
