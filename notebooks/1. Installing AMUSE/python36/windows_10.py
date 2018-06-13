def prerequisites(MPI):
    text = """Installing AMUSE directly on Windows is not possible at this point. However, using the Windows subsystem for Linux present in Windows 10, we can install a Linux environment on Windows and use that instead.
On earlier versions of Windows, this subsystem is not available. We recommend using Virtualbox (LINK) with a Linux image on these systems, although it may be possible to run AMUSE under Cygwin.

When you have enabled the Windows subsystem for Linux, please install a suitable Linux distribution from the Windows store. We recommend using the Ubuntu (18.04) image for this. 
Then, please follow the appropriate instructions for that Linux distribution.
"""
    return text
