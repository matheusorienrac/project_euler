# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import time
def is_prime(number, primes_list):
    """
    Checks if a certain number is a prime number using a list of prime numbers
    as auxiliary so that less calculation is required
    :param number: number that will be checked
    :param primes_list: list with all prime numbers smaller than number
    :return: true if prime, false if not
    """
    if (number % 10 == 5):
        return False

    if primes_list[round(primes_list * 9 / 16 - 1)] > number // 2:
        primes_list = primes_list[0:round(primes_list * 9 / 16 - 1)]
    elif primes_list[round(primes_list * 5 / 8 - 1)] > number // 2:
        primes_list = primes_list[0:round(primes_list * 5 / 8 - 1)]
    elif primes_list[round(primes_list * 3 / 4 - 1)] > number // 2:
        primes_list = primes_list[0:round(primes_list * 3 / 4 - 1)]
    for prime in primes_list:
            if number % prime == 0:
                return False
    return True

start = time.time()
primes_list = [2, 3, 5] # will use this to reduce amount of numbers to test in the
Sum = 10  # starting with number 10 so the 'for' below can skip 2,3,5
for i in range(7, 2000000, 2):
    if is_prime(i, primes_list):
        Sum += i
        primes_list.append(i)

end = time.time()
print(Sum, end - start)