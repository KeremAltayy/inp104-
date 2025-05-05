kap_fiyat = {"Kap": 0.5, "Külah": 0.8}
ekstra = {"Flake": 0.4, "Serpme": 0.3, "Çilek Sosu": 0.6}
top_fiyati = 1.0
print("Dondurmanı Oluştur")
kap = input("Kap mı Külah mı? (Kap/Külah): ")
top = int(input("Kaç top istersin? (1-4): "))
flake = input("Flake ekle? (e/h): ") == "e"
serpme = input("Çikolata serpme? (e/h): ") == "e"
sos = input("Çilek sosu? (e/h): ") == "e"
toplam = kap_fiyat[kap] + top * top_fiyati
if flake: toplam += ekstra["Flake"]
if serpme: toplam += ekstra["Serpme"]
if sos: toplam += ekstra["Çilek Sosu"]
print("Toplam Fiyat: £", round(toplam, 2))