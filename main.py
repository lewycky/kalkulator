
import sys
import logging
import operator
import math

#Funkcja mnożąca
def multiply(*args):
    result = 1     
    for x in args:
        result *= x
    return result

#Funkcja dodająca
def add(*args):
    return sum(args)

#Funkcja odejmująca
def subtract(x, y):
    return x-y

#Funkcja dzieląca:
def divide(x, y):
    return x/y

#Funkcja sprawdzająca argumenty    
def check(*args):
        
    for i in args:
        if type(i) == str:
            print(f"Argument {i} jest stringiem")
            print("Obliczenie nie jest możliwe")
            break
        else:
            print(f"Argument {i} jest liczbą")

      
                
            




print("Witaj, ten program pomoże Tobie wykonać obliczenia. Wybierz rodzaj:)")
choice=input("(1)Dodawanie,(2)Odejmowanie,(3)Mnożenie,(4)Dzielenie :")
if choice == '1':
    print("Ok czyli dodajemy")
    numbers=input("Podaj liczby które chcesz do siebie dodać")
if choice == '2':
    print("Ok a wiec odejmujmy")
    x=int(input("Podaj pierwsza liczbę:"))
    y=int(input("Podaj druga liczbe:"))
    
    check(x,y) 
    print("Wynik to", subtract(x,y))


#print(example)
