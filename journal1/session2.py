'''
    Session 2
    ASTR-19-01 Spring 2022
    March 29th, 2022
    Ian Richardson
    
    This program prints the sum of two floating point numbers, the
    difference between two integers, and the product of a floating 
    point number and an integer. In each case, the program prints out
    the data type of the resulting answer.
'''

def sum(a, b):
    # Sum of two floating point numbers
    return a + b

def diff(a, b):
    # Difference between two integers
    return a - b

def prod(a, b):
    # Product of a floating point number and integer
    return a * b

def main():
    print('Sum of Floats: ', sum(float(8.125), float(8.125)), 
    'Type:', type(sum(float(8.125), float(8.125)))) 
    print('Difference of Integers: ', diff(int(1002), int(924)),
    'Type:', type(diff(int(1002), int(924))))
    print('Product of Float and Integer: ', prod(float(8.125), int(1002)),
    'Type:', type(prod(float(8.125), int(1002))))

if __name__=="__main__":
    main()