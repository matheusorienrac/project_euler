# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
answer = 0
number = 1  # smallest positive number
while not answer:
    for i in range(1, 21):
        if number % i != 0:
            break
    if i == 20:
        answer = number
    number = number + 1
print(answer)
