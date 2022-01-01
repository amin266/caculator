# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 12:44:15 2022

@author: kyubi
"""

 
def add(self, other):
    return self + other

    
def subtract(self, other):
    return self - other


def multiply(self, other):
    return self * other

    
def divide(self, other):
    return self / other

    
def Exponentiation(self, other):
    return self ** other

 
print('>>>HELLO<<<')
print('Welcome, read the documentation string below:')
print('(Type add to add two numbers)')
print('(Type subtract to subtract two numbers)')
print('(Type multiply to mupltiply two numbers)')
print('(Type divide to divide two numbers)')
print('(Type Exponentiation or power to Exponentiation two numbers)')


while True:
    choose = input('How can i help you? ')
    first_number = float(input('First number: '))
    second_number = float(input('second number: '))

    if choose == 'add': 
        print(first_number, '+', second_number, '=', add(first_number, second_number))

        
    elif choose == 'subtract': 
        print(first_number, '-', second_number, '=', subtract(first_number, second_number))

        
    elif choose == 'multiply': 
        print(first_number, '*', second_number, '=', multiply(first_number, second_number))

        
    elif choose == 'divide': 
        print(first_number, '/', second_number, '=', divide(first_number, second_number))


    elif choose == 'Exponentiation': 
        print(first_number, '**', second_number, '=', Exponentiation(first_number, second_number))

    
    repetition = input('Do you another calculation? (yes/no): ')

    
    if repetition == 'no': 
        print('Thanks')
        break


else:
    print('Try again')