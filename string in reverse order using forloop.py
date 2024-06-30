def print_reverse(string):
    for i in range(len(string) - 1, -1, -1):
        print(string[i])

input_string = "sushma"
print("Characters of the string in reverse order:")
print_reverse(input_string)
