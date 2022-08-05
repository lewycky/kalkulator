
import logging

logging.basicConfig(level=logging.DEBUG)

#Funkcja mnożąca
def multiply(args):
    result = 1     
    for x in args:
        result *= x
    return result

#Funkcja dodająca
def add(args):
    return sum(args)

#Funkcja odejmująca
def subtract(x,y):
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


if __name__== "__main__":
    logging.info("Witaj, ten program pomoże Tobie wykonać obliczenia. Wybierz rodzaj:)")
    choice=input("(1)Dodawanie,(2)Odejmowanie,(3)Mnożenie,(4)Dzielenie :")
if choice == '1':

    logging.info("Ok czyli dodajemy")
    n=int(input("Ile liczb bedziesz dodawał: "))
    list1 =[]

    for i in range(n):
        numbers= float(input(f"Liczba {i+1}:"))
        list1.append(numbers) 

    logging.debug(f"Wynik to {add(list1)}")   
        
  
if choice == '2':
    logging.info("Ok a wiec odejmujmy")
    x=float(input("Podaj pierwsza liczbę:"))
    y=float(input("Podaj druga liczbe:"))
    check(x,y) 
    logging.info(f"Odejmuje:{x} i {y}" )
    logging.debug("Wynik to: %d" % subtract(x,y))

if choice == '3': 
    logging.info("Ok bierzemy sie za mnożenie")
    n=int(input("Ile liczb bedziesz mnożył: "))
    list2 =[]

    for i in range(n):
        numbers= float(input(f"Liczba {i+1}:"))
        list2.append(numbers) 

    logging.debug("Wynik to: %d" % multiply(list2))
  
if choice == '4':
    logging.info("Ok dzielimy")
    x=float(input("Podaj pierwsza liczbę:"))
    y=float(input("Podaj druga liczbe:"))
    check(x,y) 
    logging.info(f"Dzielę: {x} i {y}" )
    logging.debug("Wynik to: %d" % divide(x,y))
       
    
    
    
    
 
    


