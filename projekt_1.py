"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Josef Kauc
email: kauc@email.cz
discord: joska_82262
"""


TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


# Program bude obsahovat následující:
# 1. Vyžádá si od uživatele přihlašovací jméno a heslo,
# 2. zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů, 
# 3. pokud je registrovaný, pozdraví jej a umožni mu analyzovat texty,
# 4. pokud není registrovaný, upozorni jej a ukonči program.

reg_uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

username  = input("username:")
password = input("password:")

while True:   # nekonečná smyčka kvůli možnosti ukončit program v případě nesouhlasu uživatele, hesla nebo volby příkazem exit
    
    if username not in reg_uzivatele.keys():
        print("Neregistrovaný uživatel. Ukončuji program.")
        exit()

    # kontrola hesla sice nebyla v zadání, ale asi je to přirozená záležitost (pokud nemá být, lze zakomentovat příslušný elif)
    elif username in reg_uzivatele.keys() and password != reg_uzivatele[username]:
        print("Nesouhlasí heslo. Ukončuji program.")
        exit()
    
    else:
        print("Vítejte v aplikaci pro analýzu textu,", username)
        print("Jsou zde 3 texty k analýze")

        # Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS:
        # Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí,
        # pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.

        volba_textu = input("Zadejte číslo od 1 - 3: ")

        if volba_textu.isdigit() and (volba_textu not in ["1","2","3"]):
            print("Vybrali jste jiné číslo než z rozmezí 1-3. Ukončuji program.")
            exit()
        elif volba_textu.isdigit() and volba_textu in ["1","2","3"]:
            volba_textu = int(volba_textu)
            slova = list(TEXTS[volba_textu-1].replace(".","").split())
            break
        else: 
            print("Nezadali jste číslo. Ukončuji program.")
            exit()
        
        # Pokud nebudeme chtít, aby program skončil, ale kontroloval volbu textu a nutit uživatele zadat číslici 1-3:
        # while volba_textu not in ["1","2","3"]:
        # volba_textu = input("Zadejte prosím číslici od 1 do 3: ")

# Pro vybraný text spočítá následující statistiky:
                    
# počet slov,
# počet slov začínajících velkým písmenem,
# počet slov psaných velkými písmeny,
# počet slov psaných malými písmeny,
# počet čísel (ne cifer)
# sumu všech čísel (ne cifer) v textu.


slova_s_velkym_pismenem = 0
slovo_all_big_pismena = 0
slovo_lower_pismena = 0
pocet_cisel = 0
soucet_cisel = 0

delky_slov_slovnik = {}

# Pro každé slovo v seznamu proveď :
for slovo in slova:
    index = slova.index(slovo)  # zjisti pozici slova v seznamu

    # každý speciální znak z množiny vymaž
    for spec_znak in ("\n","\r","\t","\b","\f",","):
        slovo = slovo.replace(spec_znak,"")

    # zařaď upravené slovo zpět na příslušnou pozici ve slovníku "slova"
    slova[index] = slovo
    
    # zjisti délku slova a přidej do slovníku 
    # nebo připočti k již zadané hodnotě další slovo s danou délkou (delka slova je klíčem)
    delka_slova = len(slovo)

    # zjištění hodnoty ke klíči (délka slova), tj. zda je již ve slovnku (jinak vrací none)
    delka_slova_ve_slovniku = delky_slov_slovnik.get(delka_slova) 

    if delka_slova_ve_slovniku is None:
        delky_slov_slovnik[delka_slova] = [1]
    else:
        delka_slova_ve_slovniku = int(delka_slova_ve_slovniku[0])
        delka_slova_ve_slovniku += 1
        delky_slov_slovnik[delka_slova] = [delka_slova_ve_slovniku]


    # ověř podmínky a spočítej příslušnou statistiku
    # vzhledem k předchozímu nahrazení čárek a teček nebude fungovat na desetinná čísla

    if slovo.istitle():   # slovo s velkým písmenem na začátku a pak již jen malá písmena
        slova_s_velkym_pismenem += 1 
    if slovo.isupper(): # slovo jen čistě s velkými písmeny (pozor, mohou být i číslice, ty totiž metoda ignoruje...)
        znak_je_cislice = 0
        # cyklus pro zjištění situace, kdy se ve slově s velkým písmenem vyskytují zároveň i číslice (pak nepočítat do statistiky)
        for znak in slovo:
            if znak.isdigit():
                znak_je_cislice += 1
        if znak_je_cislice == 0:
            slovo_all_big_pismena += 1
    if slovo.islower(): # slovo jen čistě s malými písmeny (pozor, mohou být i číslice, ty totiž metoda ignoruje...)
        # cyklus pro zjištění situace, kdy se ve slově s malým písmenem vyskytují zároveň i číslice (nepočítat do statistiky)
        znak_je_cislice = 0
        for znak in slovo:
            if znak.isdigit():
                znak_je_cislice += 1
        if znak_je_cislice == 0:
            slovo_lower_pismena += 1
    if slovo.isdigit(): # slovo pouze z číslic, tj. CELÉ číslo
        pocet_cisel += 1
        soucet_cisel += int(slovo)


pocet_slov = len(slova)
# print(slova)
print("Počet slov: ", pocet_slov)
print("Slova s velkým písmenem na začátku: ", slova_s_velkym_pismenem)
print("Slova s velkými pismeny: ", slovo_all_big_pismena)
print("Slova s malými pismeny: ", slovo_lower_pismena)
print("Počet číslic: ", pocet_cisel)
print("Součet všech číslic: ", soucet_cisel)

# Setřídění list délky slov
list_delka_slov = sorted(list(delky_slov_slovnik.keys()))

# Setřídění list hodnot délky slov
list_cetnost_delky_slov = (sorted(list(delky_slov_slovnik.values())))

# GRAFICKÝ VÝSTUP:

max_hodnota_cetnosti = list_cetnost_delky_slov[-1]

# print("-"*50)
# # snaha o zarovnani slova OCCURENCES vlevo a doplnění mezer tak, aby lícoval "graf"
# if int(max_hodnota_cetnosti[0] <=12):
#     print("LEN|","OCCURENCES   ","|NR.")
# else:
#     pocet_mezer = int(max_hodnota_cetnosti[0]) - 12
#     print("LEN|","OCCURENCES  "," "*pocet_mezer,"|NR.")
# print("-"*50)


# ZOBRAZENÍ HLAVIČKY STATISTIKY 

print("-"*40)
 # snaha o zarovnani slova OCCURENCES na střed a doplnění mezer zleva i zprava tak, aby lícoval "graf"
if int(max_hodnota_cetnosti[0] <=10): # slovo OCCURENCES má 10 znaků, nepřidávat mezery ani zleva, ani zprava
    print("LEN|" + "OCCURENCES" + "|NR.")    
else:
    pocet_mezer = int(max_hodnota_cetnosti[0])
    # pocet_mezer_zbytek = pocet_mezer % 2
    if pocet_mezer % 2 == 0 and pocet_mezer >= 12:
        mezery_zleva = int((pocet_mezer - 10) / 2)
        mezery_zprava = mezery_zleva # + pocet_mezer_zbytek
        print("LEN|" + " "*mezery_zleva + "OCCURENCES" + " "*mezery_zprava,"|NR.")
    elif pocet_mezer % 2 > 0 and pocet_mezer >= 12:
        pocet_mezer += 1  # protože liché číslo, tak změn na sudé, aby se mohlo delit dvěma a dát stejný počet mezer zleva i zprava
        mezery_zleva = int((pocet_mezer - 10) / 2)  # odečítám 10, protože slovo OCCURENCES má 10 znaků a chci jen kolem doplnit mezery
        mezery_zprava = mezery_zleva 
        print("LEN|" + " "*mezery_zleva + "OCCURENCES" + " "*mezery_zprava,"|NR.")
    
print("-"*40)
 

# ZOBRAZENÍ PŘEHLEDU VLASTNÍCH STATISTIK

hodnota_ze_slovniku = list()

nejvyssi_cetnost = int(max_hodnota_cetnosti[0])

if nejvyssi_cetnost % 2 > 0: # jestliže není sudé
    nejvyssi_cetnost += 1    # změň na sudé, aby se mohlo dále doplnit stejný počet mezer zleva i zprava


for i in list_delka_slov:  # pro každou délku slova z (setříděného) listu delky slov
    hodnota_ze_slovniku = delky_slov_slovnik[i]   # najdi její hodnotu ze slovníku (což je četnost výskytu slova dané délky)

    mezery = nejvyssi_cetnost - int(hodnota_ze_slovniku[0])   # výpočet, kolik celkem doplnit mezer k *

    # jestliže nejvyšší četnost je menší 12, nastaví mezery větší, aby lícovalo s OCCURENCES
    if int(max_hodnota_cetnosti[0]) < 12:           
        mezery = 9 - int(hodnota_ze_slovniku[0])

    if i in range(1,10): # pro slova délky od 1-9 doplníme mezeru před číslo kvůli zarovnání grafu (sloupec LEN)
        print("",i,"|" + "*"*int(hodnota_ze_slovniku[0]), # tisk délky slova a četnosti výskytu ve formě hvězdiček (graf)
            " "*mezery + # doplnění o mezery kvůli zarovnání
            "|" + str(hodnota_ze_slovniku[0]))  # tisk čísla četnosti
    else: # tady už bude dvojciferná délka slova, zarovnání mezerou již není třeba
        print(i,"|" + "*"*int(hodnota_ze_slovniku[0]), # tisk délky slova a četnosti výskytu ve formě hvězdiček (graf)
            " "*mezery +  # doplnění o mezery kvůli zarovnání
            "|" +  str(hodnota_ze_slovniku[0]))  # tisk čísla četnosti