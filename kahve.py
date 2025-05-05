kahve = {
    "Espresso": 2.5,
    "Americano": 3.0,
    "Latte": 2.5,
    "Cappuccino": 3.0,
    "Macchiato": 2.5,
    "Mocha": 3.5,
    "Flat White": 2.5
}

sizeprice = {
    "Medium": 0.0,
    "Large": 1.0,
    "XL": 1.5
}

takeawayprice = {
    "Eat-In": 0.0,
    "Take away": 1.0
}

coffee = input("Kahve türünü gir (örn: Latte): ")
size = input("Boyut gir (Medium, Large, XL): ")
place = input("Eat-In mi Take away mi?: ")

total = kahve[coffee] + sizeprice[size] + takeawayprice[place]

print("Toplam fiyat: £", total)