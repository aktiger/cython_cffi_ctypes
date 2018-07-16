import ctypes
from ctypes import *
from ctypes.util import find_library

# Ctypes structures

class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double), ('y', ctypes.c_double)]

class Test(ctypes.Structure):
    _fields_ = [
        ('sentence', ctypes.c_char_p),
        ('nb_points', ctypes.c_int),
        ('points', ctypes.POINTER(Point)),
        ('distances', ctypes.POINTER(c_double)),
    ]
    
# Lib C functiions
_libc = ctypes.CDLL(find_library('c'))
_libc.free.argtypes =[ctypes.c_void_p]
_libc.free.restype = ctypes.c_void_p

# Lib shared functions
_libblog = ctypes.CDLL("./libblog.so")
_libblog.increment_string.argtypes = [ctypes.c_char_p, ctypes.c_int]
_libblog.increment_string.restype = ctypes.c_char_p
_libblog.generate_points.argtypes = [ctypes.POINTER(Test), ctypes.c_int]
_libblog.distance_between_points.argtypes = [ctypes.POINTER(Test)]


if __name__ == '__main__':
    #create the dict for generate the ctypes structure
    test = {}
    test['sentence'] = "A nice sentence to test.".encode('utf-8')
    test['nb_points'] = 0
    test['points'] = None
    test['distances'] = None
    c_test = Test(**test)
    ptr_test = ctypes.pointer(c_test)

    #Call C function
    _libblog.generate_points(ptr_test, 10000)
    ptr_test.contents.sentence = _libblog.increment_string(ptr_test.contents.sentence, -5)
    _libblog.distance_between_points(ptr_test)
    _libc.free(ptr_test.contents.points)
    _libc.free(ptr_test.contents.distances)
    







