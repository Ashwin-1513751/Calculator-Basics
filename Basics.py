import math
import pip
import numpy

operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
1 for binomaial expansion
2 for integration
3 for differentioation
4 for suvat
5 for circuits
6 for straight lines
7 for eponentials
8 for logarithms
9 for linear interpolation
10 for cosine rule
''')

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)    

else:
    print('You have not typed a valid operator, please run the program again.')
