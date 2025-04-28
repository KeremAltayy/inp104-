
my_list = input("Lütfen sayılardan oluşan bir liste girin (virgül kullan): ").split(',')
my_list = [int(i) for i in my_list]
biggest_int = my_list[0]
for num in my_list:
    if num > biggest_int:
        biggest_int = num2
print("En büyük sayı: {biggest_int}")