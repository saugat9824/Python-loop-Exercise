#Sum of even number
# Calculate the sum of even numbers up to a given number n.

n = 9 # user input
sum_even = 0 # starting for 0 

for i in range(1, n+1): # for nth  number loop. Starting from 1 and reach to n = 10th
    if i % 2 == 0:
        sum_even += 1

print("Sum of even number is : ", sum_even)