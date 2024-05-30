# Factorial Calculator
# Compute the factorial of a number using a while loop.

number = 5
factorial = 1 # to stope the factorial

while number > 0:
    #factorial = factorial * number # 5 * 1
    factorial *= number
    #number = number - 1
    number -= 1

print("Factorial: ",factorial)