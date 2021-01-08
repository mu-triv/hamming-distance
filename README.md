# hamming-distance

Hamming weight and Hamming distance are widely used in Side-Channel Attacks. We can easily find an implementation of Hamming weight and Hamming distance on the Internet:
- https://www.geeksforgeeks.org/hamming-distance-between-two-integers/
- https://www.tutorialspoint.com/hamming-distance-in-python

I just wonder if I can improve their implementation to make the computation faster, simpler???

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
# 3

hamming_distance(np.int16(124), np.int16(-1))
# 14

hamming_distance(1.1234, 23.21312344452)
# 21
```

## Credit
You just need to put my name in your paper works or your code, if you find my implementation useful for your work.


## Support
If you need any support, please feel free to contact me at tvk6843@gmail.com.

If you report a bug, please use github issues (https://github.com/mu-triv/hamming-distance/issues)

