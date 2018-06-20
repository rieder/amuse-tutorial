def prerequisites(MPI):
    text = """In Ubuntu, use apt-get to install dependencies:  

```bash

sudo apt-get install build-essential gfortran python-dev \\
     libgsl0-dev cmake libfftw3-3 libfftw3-dev \\
     libgmp3-dev libmpfr4 libmpfr-dev \\
     libhdf5-serial-dev hdf5-tools \\
     python-nose python-numpy python-setuptools python-docutils \\
     python-h5py python-setuptools git \\"""
    if MPI=="openmpi":
        text += """
     libopenmpi-dev openmpi-bin"""
    elif MPI=="mpich":
        text += """
     mpich libmpich-dev"""
    
    text += """
sudo easy_install mpi4py 
```"""
    return text