# övning 4 Figurer med loopar
# Skriv in följande kod och modifiera den, så att den skriver ut figurerna a-j en i taget.

# Figur a

print("Figur A ")
# Skriv ut 6 rader
for y in range(1, 7):
    s = ""
    # skriv ut 9 positioner med tecken
    for x in range(1, 9):
        if x == 1:
            s += "#"
        else:
            s += "."
    print(s)

# Figur b
print("\nFigur B ")
# Skriv ut 6 rader
for y in range(1, 7):
    s = ""
    # skriv ut 9 positioner med tecken
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)

# Figur c
print("\nFigur C ")
# Skriv ut 6 rader
for y in range(1, 7):
    s = ""
    # skriv ut 9 positioner med tecken
    for x in range(1, 9):
        if x == 3 or x == 4 or x == 5:
            s += "#"
        else:
            s += "."
    print(s)

# Figur D
print("\nFigur D ")
# Skriv ut 6 rader
for y in range(1, 7):
    s = ""
    if y <=2 or y>=4:
        for x in range(1, 9):
            if x == 3:
                s += "#"
            else:
                s += "."
        print(s)
    # rad 3 är bara #
    elif y == 3:
        for x in range(1, 9):
            s += "#"
        print(s)

# Figur E
print("\nFigur E ")
# Skriv ut 6 rader
new = 6
for y in range(1, 7):
    s = ""
    # skriv ut 9 positioner med tecken
    for x in range(1, 9):
        if x == 5 or x == new:
            s += "#"
        else:
            s += "."
    new += -1
    print(s)

# Figur F
print("\nFigur F ")
# Skriv ut 6 rader
new = 6
for y in range(1, 7):
    s = ""
    # skriv ut 9 positioner med tecken
    for x in range(1, 9):
        if x == y or x == new:
            s += "#"
        else:
            s += "."
    new += -1
    print(s)

# Figur G
print("\nFigur G ")
# Skriv ut 6 rader
for y in range(1, 7):
    s = ""
    # skriv ut 9 positioner med tecken
    for x in range(1, 9):
        if x%2 != 0:
            s += "#"
        else:
            s += "."
    print(s)