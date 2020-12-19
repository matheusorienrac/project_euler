# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit number
largest_palindrome = 0
for i in range(999,100,-1): ##tries all the possible combinations starting from the largest numbers.
    for j in range(i,100,-1):
        product = i * j
        if str(product) == str(product)[::-1]:
            if product > largest_palindrome:
                largest_palindrome = product
print(largest_palindrome)
