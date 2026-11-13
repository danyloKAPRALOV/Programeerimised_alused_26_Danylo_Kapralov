#1 Juku kinno
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
#Kontrolli enne, kas sisestatud vanus on täisarv.
#Kui ei ole, kuva veateade.
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

#Küsi kahe inimese nimed. Kontrolli, kas mõlemad nimed koosnevad ainult tähtedest. Kui jah, teata kasutajale, kas nad on täna pinginaabrid või mitte. Kui mõnes nimes on numbreid või muid märke, kuva veateade.

#Otsusta ise, kuidas „pinginaabrid“ määratakse, näiteks juhuslikult või nimede algustähtede järgi.

#Kasuta: isalpha(), capitalize()
pingi



f