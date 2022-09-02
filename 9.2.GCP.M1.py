# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 13:06:13 2022

@author: jingy
"""
# convert money amount to change
money = float(input('Please enter a money amount: '))
quarters = int(money//0.25)
dimes = int((money%0.25)//0.1)
nickels = int(((money%0.25)%0.1)//0.05)
pennies = int((((money%0.25)%0.1)%0.05)//0.01)
print(f'{quarters} quarter(s),')
print(f'{dimes} dime(s),')
print(f'{nickels} nickel(s),')
print(f'{pennies} penny(s).')

# calculate perimeter and area of triangle in 2D
import math
vert1 = input('Enter first coordinate: ')
vert1 = vert1.split(',')
vert2 = input('Enter second coordinate: ')
vert2 = vert2.split(',')
vert3 = input('Enter third coordinate: ')
vert3 = vert3.split(',')
x1 = float(vert1[0])
y1 = float(vert1[1])
x2 = float(vert2[0])
y2 = float(vert2[1])
x3 = float(vert3[0])
y3 = float(vert3[1])
a = math.sqrt((x2-x1)**2 + (y2-y1)**2)
b = math.sqrt((x3-x1)**2 + (y3-y1)**2)
c = math.sqrt((x3-x2)**2 + (y3-y2)**2)
perimeter = a+b+c
d = (a+b+c)/2
area = math.sqrt(d*(d-a)*(d-b)*(d-c))
print(f'Perimeter: {perimeter:.2f}')
print(f'Area: {area:.2f}')
      
