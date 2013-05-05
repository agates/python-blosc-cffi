########################################################################
#
#       License: MIT
#       Created: September 22, 2010
#       Author:  Francesc Alted - faltet@blosc.org
#
########################################################################

"""
blosc: a Python package that wraps the Blosc compressor
=======================================================

The functions in this package allow compression and decompression
using the Blosc library (http://blosc.org).

Public variables
----------------

* __version__ : the version of blosc package
* blosclib_version : the version of the Blosc C library
* ncores : the number of detected cores

Public functions
----------------

compress(bytesobj, typesize[, clevel=5, shuffle=True])::
    Compress bytesobj, with a given type size.

compress_ptr(address, items, typesize[, clevel=9, shuffle=True]])::
    Compress the data at address with given items and typesize.

decompress(bytesobj)::
    Decompresses a bytesobj compressed object.

decompress_ptr(bytesobj, address)::
    Decompresses a bytesobj compressed object into the memory at address.

pack_array(array[, clevel=9, shuffle=True])::
    Pack (compress) a NumPy array.

unpack_array(packed_array)::
    Unpack (decompress) a packed NumPy array.

Utilities
---------

detect_number_of_cores()::
    Returns the number of cores in the system.

free_resources()::
    Free possible memory temporaries and thread resources.

set_nthreads(nthreads)::
    Set the number of threads to be used during Blosc operation.

print_versions()::
    Print most relevant versions useful for reporting problems.

test()::
    Run the test suite.

"""

from blosc.version import __version__

from blosc.toplevel import (
    compress,
    compress_ptr,
    decompress,
    decompress_ptr,
    pack_array,
    unpack_array,
    detect_number_of_cores,
    free_resources,
    set_nthreads,
    print_versions,
    )

# Blosc symbols that we want to export
from blosc.blosc_extension import (
    BLOSC_VERSION_STRING,
    BLOSC_VERSION_DATE,
    BLOSC_MAX_BUFFERSIZE,
    BLOSC_MAX_THREADS,
    BLOSC_MAX_TYPESIZE,
    )


# Initialize Blosc
ncores = detect_number_of_cores()
set_nthreads(ncores)
blosclib_version = "%s (%s)" % (BLOSC_VERSION_STRING, BLOSC_VERSION_DATE)

# Tests
from blosc.test import run as test


