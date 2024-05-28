# Multiplication Table Printer
# Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = 3                 # 3 x 1 = 3
                           # 3 x 2 = 6

# for i in range(1, 11):
#     print(number, 'x', i, '=', number * i)

#now for skeep 5 iteration
for i in range(1, 11):
    if i ==5:
        continue # detect value skip, used to skip the remaining code inside a loop for the current iteration only.
    print(number, 'x', i, '=', number * i)
