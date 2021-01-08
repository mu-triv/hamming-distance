# hamming-distance

Hamming weight and Hamming distance are widely used in Side-Channel Attacks. We can easily find an implementation of Hamming weight and Hamming distance on the Internet:
- https://www.geeksforgeeks.org/hamming-distance-between-two-integers/
- https://www.tutorialspoint.com/hamming-distance-in-python

I just wonder if I can improve their implementation to make the computation faster, simpler and working for different types???

This demonstrates a simple way to compute the hamming distance of two integer numbers.


## Bit-wise XOR
This implemtation is clearly simpler than the implementations in the two above articles since it does not use any explicite **for loop**.

**pseudo-code**
```C code
#
# a and b are the uint32 numbers

hamming_distance = count_bits_set(a ^ b)
```

## Usage

```python
from hamming_distance import hamming_distance

hamming_distance(1, 10)
# a: 00000000000000000000000000000001
# b: 00000000000000000000000000001010
# hamming_distance: 3

hamming_distance(np.int32(124), np.int32(-1))
# a: 00000000000000000000000001111100
# b: 11111111111111111111111111111111
# hamming_distance: 27

hamming_distance(np.int32(15), np.int32(35487))
# a: 00000000000000000000000000001111
# b: 00000000000000001000101010011111
# hamming_distance: 5

hamming_distance(np.uint32(151123), np.uint32(35487))
# a: 00000000000000100100111001010011
# b: 00000000000000001000101010011111
# hamming_distance: 8

hamming_distance(np.int16(124), np.int16(-1))
# a: 00000000000000000000000001111100
# b: 00000000000000001111111111111111
# hamming_distance: 11

hamming_distance(1.1234, 23.21312344452)

# a: 00111111100011111100101110010010
# b: 01000001101110011011010001111010
# hamming_distance: 21
```

## Credit
You just need to put my name in your paper works or your code, if you find my implementation useful for your work.


## Support
If you need any support, please feel free to contact me at tvk6843@gmail.com.

If you report a bug, please use github issues (https://github.com/mu-triv/hamming-distance/issues)

