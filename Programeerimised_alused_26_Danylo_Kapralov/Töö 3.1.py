# 1
# Sisestatakse 15 arvu. Määrata, mitu neist on täisarvud.

# Variant 1: for-tsükkel
taisarvude_arv = 0
for i in range(15):
    try:
        arv = float(input(f"{i+1}. arv: "))
        if arv.is_integer():
            taisarvude_arv += 1
    except ValueError:
        print("Palun sisestage arv.")
print(f"Täisarve oli kokku: {taisarvude_arv}")

# Variant 2: while-tsükkel
taisarvude_arv = 0
i = 0
while i < 15:
    try:
        arv = float(input(f"{i+1}. arv: "))
        if arv.is_integer():
            taisarvude_arv += 1
        i += 1  # Suurendame loendurit ainult korrektse sisestuse korral
    except ValueError:
        print("Palun sisestage arv.")
print(f"Täisarve oli kokku: {taisarvude_arv}")

# Variant 3: while True ja break
taisarvude_arv = 0
i = 0
while True:
    try:
        arv = float(input(f"{i+1}. arv: "))
        if arv.is_integer():
            taisarvude_arv += 1
        i += 1
        if i == 15:
            break
    except ValueError:
        print("Palun sisestage arv.")
print(f"Täisarve oli kokku: {taisarvude_arv}")


# 2
# Küsi kasutajalt arv A ja leia kõigi naturaalarvude summa vahemikus 1 kuni A.
try:
    A = int(input("Sisesta arv A: "))
    summa = 0
    for i in range(1, A + 1):
        summa += i
    print(f"Summa vahemikus 1 kuni {A} on {summa}")
except ValueError:
    print("Palun sisestage täisarv.")


# 3
# Sisestatakse 8 arvu. Leida nende korrutis (ainult positiivsete arvude puhul).
korrutis = 1
on_positiivseid = False
for i in range(8):
    try:
        arv = float(input(f"{i + 1}. arv: "))
        if arv > 0:
            korrutis *= arv
            on_positiivseid = True
    except ValueError:
        print("Palun sisestage arv.")  # Parandatud kirjaviga 'priint'

if on_positiivseid:
    print(f"Positiivsete arvude korrutis on {korrutis}.")
else:
    print("Positiivseid arve ei sisestatud.")


# 4
# Koosta programm, mis väljastab ekraanile arvude ruudud vahemikus 10 kuni 20.
for i in range(10, 21):
    print(f"{i}^2 = {i**2}")

# while-tsükliga (oli valesti for-tsükli sees)
i = 10
while i <= 20:
    print(f"{i}^2 = {i**2}")  # Eemaldatud üleliigne koma rea lõpust
    i += 1


# 5
# Koosta programm, mis arvutab ainult negatiivsete arvude summa N sisestatud arvu seast.
try:
    N = int(input("Sisesta arvude kogus N: "))
    negatiivsete_summa = 0  # Parandatud: vaja oli summat, mitte kogust
    for i in range(N):
        try:
            arv = float(input(f"{i + 1}. arv: "))
            if arv < 0:
                negatiivsete_summa += arv
        except ValueError:
            print("Palun sisestage arv.")
    print(f"Negatiivsete arvude summa on: {negatiivsete_summa}")
except ValueError:
    print("Palun sisestage täisarv.")


# 6
# Klaviatuurilt sisestatakse N arvu. Määra positiivsete, negatiivsete ja nullide arv.
try:
    n = int(input("Mitu arvu soovid sisestada (N)? "))
    negatiivsed = 0
    positiivsed = 0
    nullid = 0

    for i in range(n):
        arv = float(input(f"Sisesta {i + 1}. arv: "))
        if arv < 0:
            negatiivsed += 1
        elif arv > 0:
            positiivsed += 1
        else:
            nullid += 1

    print(f"Negatiivseid arve: {negatiivsed}")
    print(f"Positiivseid arve: {positiivsed}")
    print(f"Nulle: {nullid}")
except ValueError:
    print("Palun sisestage korrektne arv.")


# 7
# Väljastada ekraanile arvud, mis on K-ga jaguvad vahemikust [A, B].
# (See ülesanne oli sul juba õigesti tehtud!)
a = int(input("Sisesta vahemiku algus (A): "))
b = int(input("Sisesta vahemiku lõpp (B): "))
k = int(input("Sisesta jagaja (K): "))
,
print(f"Arvud vahemikus [{a}, {b}], mis jaguvad arvuga {k}:")
for arv in range(a, b + 1):
    if arv % k == 0:
        print(arv)


# 8
# Tollide ja sentimeetrite teisendustabel (1 toll = 2,5 cm) väärtuste jaoks 1 kuni 20.
# (Samuti töökorras, kohendasin vaid eraldusjoont ilusamaks)
print("Tollid | Sentimeetrid")
print("+")
for toll in range(1, 21):
    cm = toll * 2.5
    print(f"{toll:<6} | {cm}")


# 9
# Panka pandi S eurot 3% intressiga. Määrata, kui suureks summa muutub N aasta järel.
# (Täiesti õige!)
s = float(input("Sisesta algne summa (S) eurodes: "))
n = int(input("Sisesta aastate arv (N): "))

for aasta in range(n):
    s = s * 1.03

print(f"Summa {n} aasta pärast on {s:.2f} eurot.")
# 10
# Klaviatuurilt sisestatakse 10 arvu paari. Väljasta neist suurem arv.
# (Täiesti õige!)
for i in range(1, 11):
    print(f"--- {i}. arvupaar ---")
    arv1 = float(input("Sisesta esimene arv: "))
    arv2 = float(input("Sisesta teine arv: "))

    if arv1 > arv2:
        print(f"Suurem arv on: {arv1}")
    elif arv2 > arv1:
        print(f"Suurem arv on: {arv2}")
    else:
        


# 11
# Leia kahekohaliste paaritute arvude korrutis, mis jaguvad juhusliku arvuga.
# (Täiesti õige!)
import random

juhuslik_arv = random.randint(1, 10)
print(f"Juhuslikult genereeritud arv on: {juhuslik_arv}")

korrutis = 1
leiti_arv = False

for arv in range(11, 100, 2):
    if arv % juhuslik_arv == 0:
        korrutis *= arv
        leiti_arv = True



