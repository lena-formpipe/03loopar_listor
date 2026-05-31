# 03 loopar och listor, Lena Sandberg

# Ovning 2 - Öva på loopar och listor

# 1a skriv färdigt kodexemplet
answer_1a = 0
for i in range(1,11):
    answer_1a += i
print(f"1a: Summan av talen 1 till 10 är: {answer_1a}")

# ----------------------------------------------------------------------------
# 1b Räkna ut summan av alla tal mellan 1 och 100 (inklusive 1 och 100, rätt svar är 5050)
answer_1b = 0
for i in range(1,101):
    answer_1b += i
print(f"1b: Summan av talen 1 till 100 är: {answer_1b}")

# -----------------------------------------------
# 1c Skriv om 1b så att den använder en while-loop.
sum_1c = 0
i = 1
while i <= 100:
    sum_1c += i
    i += +1
print(f"1c: Summan av talen 1 till 100 är: {sum_1c}")

# ----------------------------------------------------
# 2 Räkna ut summan av alla elementen i listan: [1, -2, 3, -2, 4, -3]
list = [1, -2, 3, -2, 4, -3]
sum_2 = 0
print("\n2: Räkna ut summan av alla element i listan:")
print(list)
# for loop av samma längd som listans längd gör att alla element summeras
for i in range(len(list)):
    sum_2 += list[i]
    i += 1
print(f"Summan av talen i listan är: {sum_2}")

# -------------------------------------------------
# 3 Träna på att skapa och manipulera listor.
# Alla uppgifter ska lösas med funktionerna som står i presentationen.

# 3a Skapa en lista med namnen på fyra filmer. Namnen ska vara strängar.
# Skriv ut hela listan med funktionen print.
lista_filmer =[ "Fåglarna", "Hajen", "Shrek", "Bolt"]
print(f"\nUppgift 3a: Skriv ut listan med filmer: {lista_filmer}")

# 3b Lägg till "Fellowship of the ring" sist i listan.
lista_filmer.append("Fellowship of the ring")
print(f"\nUppgift 3b: Skriv ut listan med filmer  efter tillägg på slutet:\n{lista_filmer}")

# 3c Lägg till "The two towers" på första platsen i listan. (index noll)
lista_filmer.insert(0, "The two towers")
print(f"\nUppgift 3c: Skriv ut listan med filmer efter tillägg av film på index 0:\n{lista_filmer}")

# 3d Ta reda på vilken position (index) "Fellowship of the ring" har nu.
index_fellowship = lista_filmer.index("Fellowship of the ring")
print(f"\nUppgift 3d: Fellowship of the ring har nu bytt till index: {index_fellowship}")

# 3e Ta bort en annan av filmerna. Har Fellowship-filmen ändrat index?
lista_filmer.pop(0)
print(f"\nUppgift 3e: Skriver ut listan efter borttag av film med index 0:\n{lista_filmer}")
index_fellowship = lista_filmer.index("Fellowship of the ring")
print(f"Uppgift 3e: Fellowship of the ring har nu bytt till index: {index_fellowship}")

# Ta reda på hur lång listan är. (len)
length_lista_filmer = len(lista_filmer)
print(f"\n3f: Längden på listan med filmer är {length_lista_filmer}")
print(lista_filmer)

# 3g Vänd listan baklänges.
lista_filmer.reverse()
print(f"\nUppgift 3g: Skriver ut listan efter att den vänts baklänges:\n{lista_filmer}")

# 3h Sortera listan stigande i bokstavsordning.
lista_filmer.sort()
print(f"\nUppgift 3h: Skriver ut listan efter att den sorterats i bokstavsordning:\n{lista_filmer}")