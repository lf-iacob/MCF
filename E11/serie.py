import numpy as np
import ctypes

#carico la libreria nella cartella
_libserie=np.ctypeslib.load_library('libserie','/home/li030002/MCF/E11')
_libserie.fibonacci_argtypes=[ctypes.c_int]
_libserie.fibonacci_restype=ctypes.c_double

def fibonacci(n):
    return _libserie.fibonacci(int(n))
