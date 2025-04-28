
my_list = input("Sayılardan oluşan bir liste girin: ").split(',')
toplam = 0
for sayi in my_list:
    toplam += int(sayi.strip())
print("Toplam:", toplam)