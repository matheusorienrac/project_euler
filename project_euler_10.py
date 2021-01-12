# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def is_prime(number, primes_list):
    """
    Checks if a certain number is a prime number using a list of prime numbers
    as auxiliary so that less calculation is required
    :param number: number that will be checked
    :param primes_list: list with all prime numbers smaller than number
    :return: true if prime, false if not
    """
    for prime in primes_list:
        if number % prime == 0:
            return False
    return True


primes_list = [2]  # will use this to reduce amount of numbers to test in the
# is_prime function
Sum = 2  # starting with number 2 so the 'for' below can skip even numbers
for i in range(3, 2000000, 2):
    if is_prime(i, primes_list):
        Sum += i
        primes_list.append(i)
print(Sum)
