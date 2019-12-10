#!/usr/bin/python3
cont1 = 0
cont2 = 1
y = cont2
while (cont1 < 8):
    while (y < 10):
        print("{}{}".format(cont1, y), end=", ")
        y += 1
    y = cont2 + 1
    cont2 += 1
    cont1 += 1
print("{}{}".format(cont1, cont2))
