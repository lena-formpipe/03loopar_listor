# 5 Gissa talet:
# Gör ett spel som slumpar ett hemligt tal mellan 1 och 100.
# Sedan ska man försöka gissa det. Om man gissar för lågt eller för högt ska spelet tala om det.
# Efter att man har gissat rätt ska spelet skriva ut antalet gissningar.
#
# # Slumpa ett hemligt tal
import random
min_number = 1
max_number = 100
secret_number = random.randint(min_number, max_number)
print(secret_number)

print(f"Välkommen till gissa talet! \nJag tänker på ett tal mellan {min_number} och {max_number}. \nKan du gissa vilket det är?")
number_of_guesses = 0
while True:
    guess_number = input("Gissa (eller skriv q för att avsluta): ")

    if guess_number == "q" or guess_number == "Q":
        print("\nProgrammet avslutas på din begäran.")
        print(f"Det slumpade talet var {secret_number}.")
        break
    number_of_guesses += 1
    # kontroll och felhantering ifall inmatat_belopp inte är integer
    try:
        guess_number = int(guess_number)
        if guess_number == secret_number:
            print(f"\nRÄTT!! Du gjorde det på {number_of_guesses} gissningar.")
            break
        elif guess_number > secret_number:
            print("Nej, det är för högt!.")
            if guess_number <= (secret_number + 5):
                print("Nu börjar det brännas!")
            if guess_number > max_number:
                print(f"OBS! Din gissning var högre än {max_number}. ")
        elif guess_number < secret_number:
            print("Nej, det är för lågt!")
            if guess_number >= (secret_number - 5):
                print("Nu börjar det brännas!")
            if guess_number < min_number:
                print(f"OBS! Din gissning var lägre än {min_number}. ")

    except:
        print("Du får bara skriva heltal eller q")






