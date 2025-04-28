my_list = input("Bir liste girin (virgülle ayırarak): ").split(',')
my_list = [int(i.strip()) for i in my_list]
negative_numbers = [i for i in my_list if i < 0]
print("Negatif sayılar:", negative_numbers)