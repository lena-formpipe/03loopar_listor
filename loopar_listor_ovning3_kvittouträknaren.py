# 3 Kvittouträknaren
# Gör ett program som upprepade gånger ber användaren skriva in ett tal.
# När man skriver in strängen "quit" eller "avsluta" ska programmet ska det räkna ut summan av talen.
from loopar_listor_ovning2 import length_lista_filmer

print("Välkommen till Kvittokompis! \nProgrammet summerar dina kvitton.\nAvsluta genom att skriva quit eller avsluta. ")
summa = 0
lista_inmatade_belopp =[]

# Man kan använda while True om man inte vet i förväg hur många gånger loopen ska köras.
# Då är det viktigt att se till att det finns ett sätt att bryta loopen!
while True:
    inmatat_belopp = input(f"Skriv in ett belopp: ")

    if inmatat_belopp == "quit" or inmatat_belopp =="avsluta":
        print("Programmet avslutas och summerar inmatade belopp.")
        break

    try:
        inmatat_belopp = float(inmatat_belopp)
        lista_inmatade_belopp.append(inmatat_belopp)
    except:
        print("Du får bara skriva heltal eller quit eller avsluta")

# Summera inmatade belopp från listan
print(lista_inmatade_belopp)

# range med endast ett värde räknar från 0 till (värde-1)
# for-loopen fortsätter så lång som listan är
for i in range(len(lista_inmatade_belopp)):
    summa += lista_inmatade_belopp[i]
    i += 1
print(f"Det blir {summa} kr totalt.")

# Version 2: programmet ska fråga hur många man är, och tala om hur mycket varje person i sällskapet ska betala.
antal_personer = input("\nHur många personer är ni i sällskapet? ")
antal_personer = int(antal_personer)
summa_per_person = summa/antal_personer
print(f"Det blir {summa} kr totalt, alltså {round(summa_per_person,2)} kr per person.\nVälkommen åter!")

# Version 3: programmet ska fråga hur många procent dricks man vill lägga på.
# Om användaren inte skriver något (tom sträng) ska programmet använda 10% som standardinställning.



