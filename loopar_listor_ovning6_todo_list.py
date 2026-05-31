# övning 6 Todo list (att göra-lista)
# Bygg ett program där användaren kan lägga till saker till en todo-lista.

# meny att välja mellan
option_1 = 1
option_1_text = "Se innehållet i din lista"
option_2 = 2
option_2_text = "Lägga till nya punkter i din lista"
option_3 = 3
option_3_text = "Markera en uppgift som klar"
option_4 = 4
option_4_text = "Visa listan över klarmarkerade saker "
option_5 = 5
option_5_text = "Avsluta"
todo_list = []
done_list = []
choise = 0

print("** Todo list extravaganza **")
print(str(option_1), option_1_text)
print(str(option_2), option_2_text)
print(str(option_3), option_3_text)
print(str(option_4), option_4_text)
print(str(option_5), option_5_text)

while choise !=5:
    choise = input("\nVälj ett alternativ: ")

    # kontroll och felhantering ifall inmatat_belopp inte är mellan 1 och 3
    try:
        choise = int(choise)
        if not ( option_1 <= choise <= option_5):
            print("Siffran finns ej i menyn")
    except:
        print(f"Du får bara välja 1, 2, 3, 4, 5.")

    if choise == 5:
        print("\nProgrammet avslutas på din begäran.")

    # Skriv ut todo-listan
    elif choise == 1:
        if len(todo_list) < 1:
            print("Din todo-lista är tom")
        else:
            for y in range(0, len(todo_list)):
                print("Så här ser din todo-lista ut:")
                print(f"+ {todo_list[y]}")
                y += 1
    # Skriv in en ny sak på todo-listan
    elif choise == 2:
        add_item = input("Skriv in en ny sak du måste komma ihåg att göra: ")
        add_item = add_item.strip()
        todo_list.append(add_item)
        print(f"Ok, lade till '{add_item}' i listan.")

    # version 2: lägg till ett menyalternativ, "Markera som klar".
    # När användaren väljer det, ska programmet fråga efter vilken grej man är färdig med.
    # Den färdiga grejen ska tas bort från listan.
    # Version 3: lägg över färdiga grejer i en ny lista.
    # Användaren ska kunna välja vad man har bockat av tidigare,
    # eller välja att lägga tillbaka grejen i todo-listan.

    elif choise == 3:
        remove_item = input("Vilken uppgift ska markeras som klar?: ")
        remove_item = remove_item.strip()
        if remove_item in todo_list:
            index = todo_list.index(remove_item)
            done_list.append(todo_list[index])
            todo_list.remove(remove_item)
            print(f"Ok, '{remove_item}' är klarmarkerad borttagen från todo-listan.")
        else:
            print(f"Hittade inte '{remove_item}' i listan.")

    # Skriv ut done-listan
    elif choise == 4:
        if len(done_list) < 1:
            print("Din done-lista är tom")
        else:
            print("Så här ser din done-lista ut:")
            for y in range(0, len(done_list)):
                print(f"klarmarkerad - {done_list[y]}")
                y += 1



