# Find the First Non-Repeated Character
# Given a string, find the first non-repeated character.

input_str = "teeteracdacd" # add acd acd


for char in input_str:
    print(char)

    if input_str.count(char) == 1: # count is a methode to see a string how many times it come
        print("Char is: ", char)
        break
        