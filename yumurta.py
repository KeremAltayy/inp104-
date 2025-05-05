
while True:
    eier = int(input("Wieviele Eier:"))
    if eier < 6:
        print("ungultiger Wert")
        continue
    else:
        toplamyumurtasayisi = eier
        buyukkutusayisi = toplamyumurtasayisi // 12
        print("Ihtiyaciniz olan 12li yumurta kutusu sayisi: %s" % buyukkutusayisi)
        kalanyumurta = toplamyumurtasayisi % 12
        if kalanyumurta > 0:
            kucukkutugerekli = kalanyumurta // 6
            kalantekyumurta = kalanyumurta % 6
            if kucukkutugerekli > 0:
                print("Ayrıca %s adet 6li yumurta kutusuna ihtiyaciniz var." % kucukkutugerekli)
                kahvaltilikyumurta = kalantekyumurta
            else:
                kahvaltilikyumurta = kalanyumurta
        else:
            kahvaltilikyumurta = 0
        print("Kahvaltida pisirmek icin size kalan yumurta sayisi: %s" % kahvaltilikyumurta)
        break