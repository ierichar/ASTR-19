# Session 2
# ASTR-19-01 Spring 2022
# March 29th, 2022
# Ian Richardson
# This program prints the sum of two floating point numbers, the
# difference between two integers, and the product of a floating 
# point number and an integer. In each case, the program prints out
# the data type of the resulting answer.

def sum(a, b):
    return a + b

def diff(a, b):
    return a - b

def prod(a, b):
    return a * b

def main():
    try:
        a = float(input('float 1: '))
        b = float(input('float 2: '))
        c = int(input('integer 1: '))
        d = int(input('integer 2: '))

        print('Sum of Floats: ', sum(a, b), 
        'Type:', type(sum(a, b))) 
        print('Difference of Integers: ', diff(c, d),
        'Type:', type(diff(c, d)))
        print('Product of Float and Integer: ', prod(a, b),
        'Type:', type(prod(a, b)))
        
    except ValueError:
        print('Enter appropriate values!')

if __name__=="__main__":
    main()