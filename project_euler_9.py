# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math
# Brute forcing the solution:

a, b, c = (1, 2, 3)
answer = False
while not answer:
    while a + b + c < 1000:
        while a + b + c < 1000:
            c += 1
            if a + b + c == 1000:
                if pow(a, 2) + pow(b, 2) == pow(c, 2):  # means we've found the solution
                    answer = (a, b, c)
        b += 1
        c = b + 1
    a += 1
    b = a + 1
    c = b + 1

print(math.prod(answer))