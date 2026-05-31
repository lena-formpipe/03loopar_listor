# Övning 1 diskutera i grupp

# 1
# så länge som index är mindre eller lika med 15 så ska värdet skrivas ut och sedan ökas med 2
# SVar: 5, 7, 9, 11, 13, 15 RÄTT
print("Övning 1")
limit = 15
index = 5
while index <= limit:
    print(index)
    index += 2

# 2
# Range betyder upp till men inte inkluderat, utan värde startar från 0
# svar: 0, 1, 2, 3, 4, "", 6, 7, 8, 9 FEL
# rätt svar är givetvis att det skrivs ut en TOM rad, tänkte lite galet där :-)
print("Övning 2")
for i in range(10):
    if i ==5:
        print("")
    else:
        print(i)
    i = i + 1

# 3 vad blir summan?
# 0+1+2+3+4+5 = 15 RÄTT
print("Övning 3")
counter = 0
for i in range (6):
    counter += i
print(counter)

# 4
# inget skriv ut för det finns ingen print!!
# -1, 9, 5, 25, 19, 49, 41, 81
print("Övning 4")
x = 0
y = 1
while y < 10:           # så länge som y är mindre än 10
    if y % 2 == 0:      # om y är ett jämnt tal ska du dra bort y från x
        x -= y
    else:
        x = y * y       # om y är ett udda tal blir x = y * y
    y += 1
    print(x)

# övning 5. Kan du göra om koden så att den skriver ut "time" istället
print("Övning 5")
message = "its_time_to_get_coding"
print(message[3:7])
# edit flytta slicingen ett steg åt höger, räknat från index 4
print(message[4:8])

# 6 kan du flytta linjen ett steg åt höger?
# om x är lika med y så ska # skrivas ut, ger en diagonal linje från position 0 till 6
print("Övning 6")
for y in range(1, 7):        # rader = höjd 6 positioner
    s = ""
    for x in range(1, 9):   # bredd 8 positioner
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)


print("Övning 6 ett steg åt höger")
for y in range(1, 7):        # rader = höjd 6 positioner
    s = ""

    for x in range(1, 9):   # bredd 8 positioner
        # flytta ett steg åt höger genom att ange position y+1
        if x == (y+1):
            s += "#"
        else:
            s += "."
    print(s)