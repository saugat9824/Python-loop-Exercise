#Prime Number Checker
# Check if a number is prime.

#prime ==> A whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1.(2, 3, 5, 7, 11 )

number = 29

is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break
print(is_prime)
