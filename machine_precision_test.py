from decimal import *
from fractions import *


def correctness(x):
    return x if (abs(x) + 2 ** -52) % 1 != 0 else x + 2 ** -52


print(3.0 * (4 / 3 - 1) - 1)  # Wrong answer


print(3.0 * (4.0 - 3.0) - 3)  # Right answer after multiplying by common divisor. First method
precision = 2 ** -52
print(3.0 * (4.0 / 3.0 - 1) - 1 + precision)  # Second method.
