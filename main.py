


import logging
from unittest import result
logging.basicConfig(level=logging.DEBUG)



#Funkcja mnożąca
def multiply(*args):
    result = 1     
    for x in args:
        result *= x
    return result

#Funkcja dodająca
def add(*args):
    logging.info("Ok czyli dodajemy")
    n=int(input("Ile liczb bedziesz dodawał: "))
    list1 =[]
    for i in range(n):
        numbers= int(input(f"Liczba {i+1}:"))
        list1.append(numbers)
    return print(f"Wynik to {sum(list1)}")

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

      
                

logging.info("Witaj, ten program pomoże Tobie wykonać obliczenia. Wybierz rodzaj:)")
choice=input("(1)Dodawanie,(2)Odejmowanie,(3)Mnożenie,(4)Dzielenie :")
if choice == '1':
    result=add()
    
    
if choice == '2':
    logging.info("Ok a wiec odejmujmy")
    x=int(input("Podaj pierwsza liczbę:"))
    y=int(input("Podaj druga liczbe:"))
    
    check(x,y) 
    logging.info(f"Odejmuje:{x} i {y}" )
 
    logging.debug("Wynik to: %d" % subtract(x,y))


