my_tuple = (0, 1, 2, "hi", 4, 5)
my_list = list(my_tuple)
my_list[3] = 3
my_tuple = tuple(my_list)
print(my_tuple)