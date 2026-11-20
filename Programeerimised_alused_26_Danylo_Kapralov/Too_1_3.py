# # import calendar
# # from datetime import *
# # from calendar import * #monthrange
# # #Ülesanne1
# # tana=date.today()
# # print(f"Täna on {tana}")

# # # 27/12/2022
# # tana1 = tana.strftime("%d/%m/%Y")
# # print(f"Täna on {tana1}")

# # # December 27, 2022
# # tana2 = tana.strftime("%B %d, %Y")
# # print(f"Täna on {tana2}")

# # # 12/27/22
# # tana3 = tana.strftime("%m/%d/%y")
# # print(f"Täna on {tana3}")

# # # Dec-27-2022
# # tana4 = tana.strftime("%b-%d-%Y")
# # print(f"Täna on {tana4}")

# # # Omadused day, month, year kasutatakse päeva,
# # # kuu ja aasta parameetri leidmiseks date klassist.
# # # Arvuta mitu päeva on jäänud kuu lõpuni,
# # # aasta lõpuni.
# # # Arvuta oma vanus aastates, kuudes ja päevades.
# # print("Täna on", tana.day)
# # print("Päev, kuu number on", tana.month)
# # print("ja aasta on", tana.year)

# # kuulõpuni=monthrange(tana.year, tana.month)[1]- tana.day
# # #oktoobris on 31 päeva, 31-24=4 päeva jäänud
# # print("Kuu lõpuni on jäänud", kuulõpuni, "päeva.")
# # aastalõpuni=(date(tana.year, 12, 31)) - tana) - tana).days
# # #date()-> 31.12.2026
# # #tana ->27.10.2026
# # #days -> 65 päeva jäänud
# # print("Aasta lõpuni on jäänud", aastalõpuni, "päeva.")
# # sünnipäev=date(2010, 05, 20)
# # vanus=aastalõpuni//365
# # print("Oled", vanus, "aastat,")
# # print((aastalõpuni%365)//30, "kuud ja")
# # print((aastalõpuni%365)%30, "päeva vana.")

# # #Ülesanne2
# # # Koosta programm on öeldud tehte 3 + 8 / (4 - 2) * 4 vastuse?
# # # +Kuidas mõjutab sulgude kasutamine/kasutamata jätmine tööd?
# # # +Katseta erinevaid kombinatsioone paralleelselt ning lisa ka selgitavad tekstid, et väljund oleks arusaadav.
# # print("3 + 8 / (4 - 2) * 4=", 3+8 / (4 - 2) * 4)
# # print("3 + 8 / 4 - 2 * 4=", 3+8 / 4 - 2 * 4)
# # print("3 + 8 / 4 - 2 * 4=", (3+8) / 4 - 2 * 4)

# # #Ülesanne3
# # # Ruudu sees asub ring. Ringi raadius on R.
# # # Leia ja väljasta ekraanile ruudu pindala, ruudu ümbermõõt, ringi pindala, ringi ümbermõõt.

# # try:
# #     R=float(input("Sisesta ringi raadius:"))
# #     print("Ruudu pindala:", R**2)
# #     print("Ruudu ümbermõõt:", 4*R)
# #     print("Ruudu pindala:", round(3.14*R**2, 2))
# #     print("Ruudu ümbermõõt:", round(2*3.14*R, 2))
# # except :
# #     print("Valed andmed")
# #     .
# # #Ülesanne4
# # # Koosta programm, mis arvutab välja Maa ümbermõõdu ekvaatori kohal 2-eurostes müntides ehk teisisõnu: kui palju 2-euroseid münte tuleb panna üksteise kõrvale, et rida ulatuks ümber Maa. Kasuta teadmist, et Maa raadius ekvaatori kohal on 6378 km.
# # import math

# # maa_raadius_km = 6378
# # mundi_labimoot_mm = 25.75
# # pi = 3.14159
# # maa_raadius_mm = maa_raadius_km * 1000000
# # maa_umbermoot_mm = 2 * pi * maa_raadius_mm
# # print("Maa ümbermõõt:", maa_umbermoot_mm / 1000000, "km")
# # print("Vajalike 2-euroste müntide arv:", muntide_arv)

# # #Ülesanne5
# # # Eelnevaid teadmisi kasutades kirjuta programm, mis väljastaks:
# # a="Kill-koll"
# # b="Kadi-koll
# # print(a.upper() * 3 + b.upper() + a.upper() * 3 + b.upper() + a.upper() * 3)"

# # #Ülesanne6
# # # Koosta programm, mis väljastaks järgmised laulusõnad suurte tähtedega:
# # print("Rong see sõitis tsuhh tsuhh tsuhh,".upper())
# # print("piilupart oli rongijuht.".upper())
# # print("Rattad tegid rat tat taa,".upper())
# # print("rat tat taa ja tat tat taa.".upper())
# # print("Aga seal rongi peal,".upper())
# # print("kas sa tead, kes olid seal?".upper())
# # print("Rong see sõitis tuut tuut tuut,".upper())
# # print("piilupart oli rongijuht.".upper())
# # print("Rattad tegid kill koll koll,".upper())
# # print("kill koll koll ja kill koll kill..".upper())

# # #Ülesanne7
# # # Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning
# # #  väljastab ekraanile ristküliku ümbermõõdu ja pindala.
# print("2026", "10", "02", sep="-")
