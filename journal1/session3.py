'''
    Session 3
    ASTR-19-01 Spring 2022
    March 31st, 2022
    Ian Richardson
    
    This program that defines a function f(x) that returns x**3 + 8. 
    In the main function of the program, f(x) is called with x = 9 and 
    prints the result. This program uses an if statement that executes
    if the result is larger than 27 and prints “YAY!”.
'''
import math

def f(x):
    # f(x) = x**3 + 8
    return (math.pow(x, 3) + 8)

def main():
    if (f(9) > 27):
        print("YAY!")

if __name__=="__main__":
    main()