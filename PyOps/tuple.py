my_tuple = (1, 22, 3, 2, 4)
print(my_tuple.count(1)) # Output: 1
print(my_tuple.index(3)) # Output: 4
sorted_tuple = tuple(sorted(my_tuple))
print(sorted_tuple) # Output: (1, 1, 2, 3,4, 22)
reversed_tuple = tuple(reversed(my_tuple))
print(reversed_tuple) # Output: (4, 2, 3, 22, 1)
sliced_tuple = my_tuple[1:4]
print(sliced_tuple) # Output: (22, 3, 2)
len_tuple = len(my_tuple)
print(len_tuple) # Output: 5
for item in my_tuple:
    print(item)
# Output:
# 1
# 22
# 3