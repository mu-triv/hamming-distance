import numpy as np
import struct


def to_uint32(x):
    if type(x) in [np.float32, float]:
        val = struct.unpack('@I', struct.pack('@f', x))[0]
    elif type(x) in [np.int8]:
        val = np.uint8(x)
    elif type(x) in [np.int16]:
        val = np.uint16(x)
    elif type(x) in [np.uint8, np.uint16, np.int32, np.uint32, int]:
        val = x
    else:
        raise TypeError('unsupported type %s' % type(x))
    return np.uint32(val)


def hamming_weight(x):
    return bin(to_uint32(x)).count('1')


def hamming_distance(a, b):
    return bin(to_uint32(a) ^ to_uint32(b)).count('1')
