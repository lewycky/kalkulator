
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
    result = 1
    
    for x in args:
        result *= x
    return result   


print(multiply(13,12))

    