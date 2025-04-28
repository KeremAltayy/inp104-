my_list = input("Bir liste girin (virgülle ayırarak): ").split(',')
my_list = [int(i.strip()) for i in my_list]
my_list2 = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print("Büyük olan sayılar:", my_list24)