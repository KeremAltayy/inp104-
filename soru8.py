my_list = input("Bir liste girin (virgülle ayırarak): ").split(',')
even_numbers = [int(i.strip()) for i in my_list if int(i.strip()) % 2 == 0]
print("Çift sayılar:", even_numbers)