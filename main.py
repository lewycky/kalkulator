
import sys
import logging
import operator
import math



def add(*args):

    return sum(args)

def subtract(x, y):
    
    if type(x) == int and type(y) == int:
         print("Podane wartości są liczbami!")
             
    score=x-y
    return print('Wynik odejmowania to: %s' % score)
     
def multiply(*args):
    
    for i in args:
        if type(i) == str:
            print(f"Argument {i} nie jest liczbą")
            print("Obliczenie nie jest możliwe")
            break
        else:
            print(f"Argument {i} jest liczbą")
                 ### po przerwie zajac sie szukaniem tutaj 
            
              
 
        
           

multiply(12,"321")

