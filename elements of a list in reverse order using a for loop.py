#elements of a list in reverse order using a "for" loop
list = [1, 2, 3, 4, 5]
for i in range(len(list) - 1, -1, -1):
    print(list[i])