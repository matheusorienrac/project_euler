# largest prime factor that divides 600851475143?

number = 600851475143
largest_prime_factor = 1

while number != 1:  # method to reduce a number to its prime factors

    for j in range(2, number + 1):
        if number % j == 0:
            number = number // j
            largest_prime_factor = j
            break
print(largest_prime_factor)
