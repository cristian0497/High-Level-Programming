#!/usr/bin/python3
def fizzbuzz():
    cont = 1
    while (cont <= 100):
        if cont % 15 == 0:
            print("FizzBuzz", end=" ")
        elif cont % 3 == 0:
            print("Fizz", end=" ")
        elif cont % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(cont, end=" ")
        cont += 1
