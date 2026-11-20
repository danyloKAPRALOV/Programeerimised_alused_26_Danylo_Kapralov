 1 Juku kinno
 eesnimi=input("Sisesta eesnimi: ")
 if eesnimi.lower() == "juku" :
     print("Lähme Jukuga kinno!")
     if eesnimi.isupper():
         print("Ära karju, Juku!")
     elif eesnimi.islower():
        print("Ära soosista, Juku!")
     vanus=int(input(f"Kui vana on {eesnimi}?"))
     if vanus<6:
         pilet="tasuta pilet"
     elif 6<=vanus<14:
         pilet="lapsepilet"
         elif 14<=vanus<65:
         pilet="täispilet"
     elif 65<=vanus<=100:
         pilet="sooduspilet"
 else:
     pilet="tundmatu pilet"
 print(f"{eesnimi}vajab {pilet}.")
 else:
     print("Täna kinno ei minda")
Kontrolli enne, kas sisestatud vanus on täisarv.
 Kui ei ole, kuva veateade.
     vanus=input(f"Kui vana on {eesnimi}?")
     if vanus.isdigit():
         vanus=int(vanus)
     if 0<vanus<6:
         pilet="tasuta pilet"
     elif 6<=vanus<14:
         pilet="lapsepilet"
     elif 14<=vanus<65:
         pilet="täispilet"
     elif

# #Küsi kahe inimese nimed. Kontrolli, kas mõlemad nimed koosnevad ainult tähtedest. Kui jah, teata kasutajale, kas nad on täna pinginaabrid või mitte. Kui mõnes nimes on numbreid või muid märke, kuva veateade.

# #Otsusta ise, kuidas „pinginaabrid“ määratakse, näiteks juhuslikult või nimede algustähtede järgi.

# #Kasuta: isalpha(), capitalize()
# # pinginaabrid=("Mati", "Kati")
# # nimi1=input("Sisesta nimi: ")
# # nimi2=input("Sisesta nimi: ")
# # if nimi1.isalpha() and nimi2.isalpha():
# #     print(f"Tere {nimi1.capitalize()} ja {nimi2.capitalize()}")
# #     if nimi1.capitalize() in pinginaabrid and nimi2.capitalize() in pinginaabrid:
# #         print(f"{nimi1} ja {nimi2} on pinginaabrid")
# #     else:
# #         print("Nad ei ole pinginaabrid")

# # else:
# #     print("Viga: nimed on valesti sisestud! Kasuta ainult tähed")
# # 3. Remont
# # Küsi ristkülikukujulise toa pikkus ja laius ning arvuta põranda pindala.
# # Seejärel küsi, kas kasutaja soovib remonti teha. Kui vastus on jaatav,
# #  küsi ruutmeetri hind ja arvuta põranda vahetamise hind.
# # Lisaküsimus: kas kasutaja teeb remondi ise või kasutab professionaali abi? Professionaali
# # puhul küsi ka töö hind ruutmeetri kohta ja arvuta remondi koguhind koos tööga.
# # # Kasuta: float(), lower() (vastuse „Jah“, „JAH“, „jah“ äratundmiseks), round()
# # try:
# #     pikkus=float(input("Sisesta pikkus: "))
# #     laius=float(input("Sisesta laius "))
# #     pindala=round(pikkus*laius,2) #ümardamine
# #     print(f"Pindala on {pindala}")
# #     remont=input("Kas soovid remonti teha? (jah/ei)").lower() #tähed on väikesed
# #     if remont=="jah":
# #         print("Teeme remonti!")
# #         try:
# #             rm_hind=float(input("Sisesta ruutmeetri hind: "))
# #             hind=round(pindala*rm_hind,2)
# #             print(f"Põranda vahetamise hind on {hind}€")
# #             ise=input("Kas teeb remondi ise?(jah/ei)").lower()
# #             if ise=="jah":
# #                 print(f"Põranda vahetamise hind on sama {hind}€")
# #             else:
# #                     try:
# #                         töö_hind=float(input("Töö hind: "))
# #                         koguhind=(hind+pindala*töö_hind,2)
# #                         print(f"Remondi koguhind koos tööga on {koguhind}")
# #                     except ValueError:
# #                         print("tööhind on ujukomarv")

# #         except ValueError:
# #             print("Viga: ruutmeetri hind on arv")

# #     else:
# #         print("Remonti ei tehta")

# # except ValueError:
# #     print("Viga: kasuta numbreid pikkuse ja laiuse sisestamiseks")
    


# # 4. Allahindlus
# # Küsi toote alghind. Kui alghind on üle 700 euro, arvuta hind 30% soodustusega. Muul juhul jääb hind samaks. Kuva lõplik hind kahe komakohaga.
# from multiprocessing import Value


# try:  
#     hind=float(input("Sisesta kauba hind: "))
#     if hind>700:  
#         lõp_hind = hind * 0.7
#     else:
#         lõp_hind=hind

#     print(f"lõpu hind: {lõp_hind:.2f} €") 
# except ValueError:
#     print("Viga! Palun sisesta korektnee hind")
# # 5. Temperatuur
# # Küsi toatemperatuur ja teata, kas see on üle 18 kraadi (soovitatav toasoojus talvel). 
# # Temperatuur võib olla ka negatiivne või kümnendarv, seega kontrolli sisendit try/except abil.
# try:
#     temperatuur = float(input("Sisesta täpselt temperatuur: "))
#     if temperatuur > 18:
#         print("Temperatuur on üle 18 kraadi. Toas on piisavalt soe.")
#     elif temperatuur == 18:
#         print("Temperatuur on täpselt 18 kraadi.")
#     else:
#         print("Temperatuur on alla 18 kraadi. Toas on jahe.")
# except ValueError:
#     print("Viga! Palun sisesta kehtiv number (kasuta kümnendkoha eraldajana punkti).")
# # 6. Pikkus
# # Küsi inimese pikkus sentimeetrites ja teata, kas ta on lühike, keskmise pikkusega või pikk. Piirid pane ise paika ja kirjuta need programmi alguses kommentaarina.
# try:
#     pikkus = float(input("Sisesta oma pikkus sentimeetrites: "))
    
#     if pikkus <= 0:
#         print("Viga: Pikkus peab olema positiivne arv!")
#     elif pikkus < 160:
#         print("Sa oled lühike.")
#     elif pikkus <= 180:
#         print("Sa oled keskmise pikkusega.")
#     else:
#         print("Sa oled pikk.")
# except ValueError:
#     print("Viga: Palun sisesta pikkus numbrina!")
# # 7. Pikkus ja sugu
# # Täienda ülesannet 6: küsi lisaks sugu. Meestele ja naistele kehtivad erinevad piirid. Tingimusplokid võivad olla üksteise sees.

# # Sugu võib sisestada mis tahes kujul (M, m, mees, MEES). Programm peab selle ära tundma.
# # Kui sugu on sisestatud valesti, kuva veateade.
# # Kasuta: pesastatud if-laused, lower()
# # Piirid meestele: lühike < 170, keskmine 170-185, pikk > 185
# # Piirid naistele: lühike < 160, keskmine 160-175, pikk > 175


# try:
#     if sugu in ["m", "mees"]:
#         pikkus = float(input("Sisesta oma pikkus sentimeetrites: "))
#         if pikkus <= 0:
#             print("Viga: Pikkus peab olema positiivne!")
#         elif pikkus < 170:
#             print("Sa oled lühike mees.")
#         elif pikkus <= 185:
#             print("Sa oled keskmise pikkusega mees.")
#         else:
#             print("Sa oled pikk mees.")
            
  