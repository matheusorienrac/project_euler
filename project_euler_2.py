term_1 = 1
term_2 = 2
sum = 0
while(term_2 < 4000000):
    if (term_2 % 2 == 0):##if new term is even, add it to total sum
        sum = sum + term_2
    aux = term_2
    term_2 = term_1 + term_2
    term_1 = aux
print(sum)

