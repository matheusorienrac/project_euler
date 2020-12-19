# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def is_prime(number):
    divisors = 0
    for i in range(1,number+1):
        if(number % i == 0):
            divisors = divisors + 1
    if divisors == 2:
        return True
    return False

primes_list = [2]   # ill start the list with the number 2 so that i can start iterating from number 3 and skip all even
# numbers
iterator = 3
while(len(primes_list) != 10001):
    if is_prime(iterator):
        primes_list.append(iterator)
    iterator = iterator + 2  # This will skip even numbers so that we arrive at the answer a little bit faster

print(primes_list[10000])
