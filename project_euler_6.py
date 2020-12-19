import numpy as np
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
one_hundred_nat_numbers = np.array(range(1,101))
diff = sum(one_hundred_nat_numbers**2) - sum(one_hundred_nat_numbers)**2
print(diff)