# Variant 6 - Suurim arv, valuuta ja jõusaal (tsükliga)

# Lõpmatu tsükkel: programm töötab seni, kuni kasutaja valib väljumise (4)
while True:
    print("\nVali programm:")
    print("1 - Suurim arv")
    print("2 - Valuutavahetus")
    print("3 - Jõusaali kuutasu")
    print("4 - Välju")

    # .strip() eemaldab algusest ja lõpust juhuslikud tühikud
    valik = input("Sisesta valik (1-4) => ").strip()

    # 1. OSA: Suurima ja vähima arvu leidmine 
    if valik == "1":
        print("Suurim arv")
        try:
            # Teisendame kõik sisendid ujukomaarvudeks (float)
            a = float(input("Sisesta 1. arv => "))
            b = float(input("Sisesta 2. arv => "))
            c = float(input("Sisesta 3. arv => "))

            # Leiame suurima ja vähima arvu sisseehitatud funktsioonidega
            suurim = max(a, b, c)
            vaikim = min(a, b, c)

            print("Suurim on", suurim)
            print("Vähim on", vaikim)

        # Veatöötlus juhuks, kui arvu asemel sisestatakse tekst
        except ValueError:
            print("Vigane sisend! Sisesta arv.")

    # 2. OSA: Valuutavahetus
    elif valik == "2":
        print("Valuutavahetus")
        try:
            summa = float(input("Sisesta summa eurodes => "))

            # Kontrollime, et summa oleks positiivne
            if summa <= 0:
                print("Summa peab olema suurem kui 0.")
            else:
                # .strip() eemaldab tühikud ja .upper() muudab teksti suurtähtedeks
                valuuta = input("Sisesta valuuta (USD/GBP) => ").strip().upper()

                # Arvutame summa ja ümardame kahe komakohani
                if valuuta == "USD":
                    print("Saad", round(summa * 1.08, 2), "USD")
                elif valuuta == "GBP":
                    print("Saad", round(summa * 0.85, 2), "GBP")
                else:
                    print("Tundmatu valuuta")

        except ValueError:
            print("Vigane sisend! Sisesta arv.")

    #  3. OSA: Jõusaali kuutasu arvutamine 
    elif valik == "3":
        print("Jõusaali kuutasu")
        try:
            # Vanus peab olema täisarv (int)
            vanus = int(input("Sisesta vanus => "))

            # Kontrollime vanuse sobivust ja vanusepiirangut
            if vanus < 0:
                print("Vigane vanus")
            elif vanus < 16:
                print("Alla 16-aastased jõusaali ei pääse")
            else:
                # .lower() muudab vastuse väiketähtedeks
                tudeng = input("Kas oled tudeng (jah/ei)? => ").strip().lower()

                # Tingimuste õige järjekord: esmalt soodsam pensionäri hind,
                # seejärel tudengi soodustus ja lõpuks tavahind
                if vanus >= 65:
                    print("Kuutasu: 20 €")
                elif tudeng == "jah":
                    print("Kuutasu: 25 €")
                elif tudeng == "ei":
                    print("Kuutasu: 40 €")
                else:
                    print("Vigane vastus! Sisesta 'jah' või 'ei'.")

        except ValueError:
            print("Vigane sisend! Sisesta täisarv.")

    #  4. OSA: Programmist väljumine 
    elif valik == "4":
        print("Programm lõpetatud. Head aega!")
        break  # Katkestab tsükli ja lõpetab programmi töö

    # Kui menüüst valiti midagi muud kui 1–4
    else:
        print("Vigane valik! Vali number 1 kuni 4.")

