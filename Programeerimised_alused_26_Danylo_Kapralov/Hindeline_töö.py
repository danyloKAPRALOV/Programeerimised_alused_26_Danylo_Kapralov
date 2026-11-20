menüü=input("Sisestega menüü (Arvu kontroll / Ostu allahindlus / Kehamassiindeks )")
if menüü in ("a", "arv")
print("Arvu kontroll")
try:
 arv=float(input("Sisesta täisarv =>"))
 if arv>0:
    print("Arvu ")
     print("Ostu allahindlus")
print("Arvu kontroll") # jutumärkides oli viga
arv=float(input("Sisesta täisarv => ")) # siin peab olema float
if arv>0: #peab olema ":"
    print("Arv on positiivne")
    if arv==0: #"if" oli vagades ridas ja peab olema ":"
        print("Arv on null") #"print" oli vigades kohta
    else: #"else" oli vigades kohta
        print("Arv on negatiivne")#"print" oli vigades kohta
    if arv%2==0: #"if" oli on vigades kohta
        print("Arv on paarisarv")#"print" oli vigades kohta
    else:#"else" oli vigades kohta
        print("Arv on paaritu")
    print() # "print" oli vigades kohta
    print("Kehamassiindeks")# "print" oli vigades kohta
    mass=float(input("Sisesta kaal (kg) => "))# "mass" oli vigades kohta
    pikkus=float(input("Sisesta pikkus (m) => ")) # sulgud ei ole kinni ja pikkus oli vigades kohta
    kmi=mass/pikkus**2 #"kmi" oli vigades kohta
    print("KMI:", round(kmi,1))# "print" oli vigades kohta
    if kmi<18.5:
        print("Alakaal")# "print" oli vigades kohta
    elif kmi>=18.5: # "elif" oli vigades kohta
        print("Normaalkaal")# "print" oli vigades kohta
    elif kmi>=25:# "elif" oli vigades kohta
        print("Ülekaal")# "print" oli vigades kohta
    elif kmi>=30:# "elif" oli vigades kohta ja peab olema ":"
        print("Rasvumine")#"print" oli vigades kohta
    print()# "print" oli vigades kohta
    print("Ostu allahindlus")# "print" oli vigades kohta
    summa=float(input("Sisesta ostusumma => "))# "summa" oli vigades kohta
    if summa<0:# "if" oli vigades kohta ja "=" see on viga
        print("Vigane summa")# "print" oli vigades kohta
    elif summa>100 or summa<=500:# "elif" oli vigades kohta
        print("Allahindlus 5%, maksta:", round(summa*0.95,2))# "print" oli vigades kohta
    elif summa>500:# "elif" oli vigades kohta
        print("Allahindlus 10%, maksta:", round(summa*0.9,2))# "print" oli vigades kohta
    else: #peab olema ":" ja  "else" oli vigades kohta
        print("Allahindlust pole, maksta:", summa)# "print" oli vigades kohta
        
# Lisaülesanne:
#Muuda programmi nii, et alguses kuvatakse menüü ja kasutaja valib, millist osa käivitada:
 
# Vali programm:
# 1 - Arvu kontroll
# 2 - Kehamassiindeks
# 3 - Ostu allahindlus
# Sisesta valik (1-3) =>


