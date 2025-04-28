my_list = input("Bir liste girin (virgülle ayırarak): ").split(',')
for i in range(len(my_list)):
    print(f"my_list[{i}] = {my_list[i].strip()}")