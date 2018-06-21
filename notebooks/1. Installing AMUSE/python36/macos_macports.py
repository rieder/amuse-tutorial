def prerequisites(MPI):
    text = """In macOS, we use macports to install dependencies. 
Other methods (e.g. Homebrew) will probably work just as well, but we have not tested these.
    
In the example below, we use GCC version 7, but other versions will also work.

```bash

sudo port install python36
sudo port install gcc7 hdf5 gsl cmake gmp mpfr fftw-3 +gcc7
"""
    if MPI=="openmpi":
        text += """
sudo port install openmpi-gcc7"""
    elif MPI=="mpich":
        text += """
sudo port install mpich-gcc7"""
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
sudo port select --set python3 python36

```
"""
    return text
