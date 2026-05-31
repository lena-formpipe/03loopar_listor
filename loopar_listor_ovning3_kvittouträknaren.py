# 3 Kvittouträknaren
# Gör ett program som upprepade gånger ber användaren skriva in ett tal.
# När man skriver in strängen "quit" eller "avsluta" ska programmet ska det räkna ut summan av talen.

print("Välkommen till Kvittokompis! \nProgrammet summerar dina kvitton.\nSkriv quit eller avsluta när du inte vill lägga till fler kvitton. ")
summa = 0
lista_inmatade_belopp =[]

# Man kan använda while True om man inte vet i förväg hur många gånger loopen ska köras.
# Då är det viktigt att se till att det finns ett sätt att bryta loopen!
while True:
    inmatat_belopp = input(f"Skriv in ett belopp: ")

    if inmatat_belopp == "quit" or inmatat_belopp =="avsluta":
        print("\nProgrammet summerar inmatade belopp.")
        break

    # kontroll och felhantering ifall inmatat_belopp inte är float
    try:
        inmatat_belopp = float(inmatat_belopp)
        lista_inmatade_belopp.append(inmatat_belopp)
    except:
        print("Du får bara skriva tal eller quit eller avsluta")

# Summera inmatade belopp från listan
# range med endast ett värde räknar från index 0 till index (värde-1)
# for-loopen fortsätter så lång som listan är
for i in range(len(lista_inmatade_belopp)):
    summa += lista_inmatade_belopp[i]
    i += 1
print(f"Det blir {summa} kr totalt.")

# Version 2: programmet ska fråga hur många man är, och tala om hur mycket varje person i sällskapet ska betala.
# måste vara ett positivt heltal
antal_personer = 0
# while kör så länge som antal personer är lika med eller mindre än noll
while antal_personer <=0:
    try:
        antal_personer = input("\nHur många personer är ni i sällskapet? ")
        antal_personer = int(antal_personer)
        if antal_personer <= 0:
            print("Antal personer måste var större än 0.")
        else:
            summa_per_person = summa / antal_personer
    except:
        print("Du får bara skriva positiva heltal.")
        # kom ihåg att sätta antal_personer = 0 så att while körs igen
        antal_personer = 0

# beräkning och utskrift
summa_per_person = summa/antal_personer
print(f"Det blir {round(summa,2)} kr totalt utan dricks, alltså {round(summa_per_person,2)} kr per person.")

# Version 3: programmet ska fråga hur många procent dricks man vill lägga på.
# Om användaren inte skriver något (tom sträng) ska programmet använda 10% som standardinställning.
# det är inte logiskt att ange en bokastav eller negativt belopp
dricks_procent = -1
# while kör så länge som dricks_procent är negativ eller bokstav
while dricks_procent <0:
    try:
        dricks_procent = input("\nAnge hur många procents dricks ni vill ge (tom inmatning = 10%): ")

        if dricks_procent == "":
            dricks_procent = 10
        else:
            dricks_procent = int(dricks_procent)
            if dricks_procent < 0:
                print("Du kan inte ge negativ procent i dricks, försök igen.")
    except:
        print("Du får bara skriva positiva heltal.")
        # kom ihåg att sätta dricks_procent = -1 så att while körs igen
        dricks_procent = -1

dricks_per_person = summa_per_person * dricks_procent/100
total_summa_inkl_dricks_per_person = dricks_per_person + summa_per_person
print(f"Med {dricks_procent} % i dricks blir det {round(dricks_per_person, 2)} kr i dricks per person.")
print(f"Varje person ska betala {round(total_summa_inkl_dricks_per_person, 2)} när dricksen är inkluderad.")

