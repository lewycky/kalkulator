
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

      
                
            

                      


example=check(30,20,10)

#print(example)
