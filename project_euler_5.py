# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

answer = 0
number = 20
while not answer:
    for i in range(1, 21):
        if number % i != 0:  # if not divisible by one of the 20 numbers, break the for loop to gain processing time
            break
    if i == 20:
        answer = number
    number = number + 20  # if the number we are looking for is divisible by 20,we can test multiples of 20 to save time

print(answer)
