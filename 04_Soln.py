# Reverse a String
# Reverse a string using a loop.

input_str = 'Python'
reversed_str = ""

for char in input_str:
    # reversed_str = reversed_str + char # print same Python
# for reversed
    reversed_str =  char + reversed_str 

print(reversed_str)