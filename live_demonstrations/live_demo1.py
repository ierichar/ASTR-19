'''
    Live Demo 1

    Import the sys and numpy modules.
    Defines a main() function.
    In the main() function:
    - Define variable x and initializes its value to 0.0. 
    - Use a for loop to iterate a variable i from 0 to 19 inclusive.
    - For each value of i, set the value of x to be twice i plus 19 as a float.
    - Use an f-string to print() out the value of x, including the text string βThe value of x is = β.
    Use the if __name__==β__main__β: conditional to call main().
'''
import sys
import numpy as np

def main():
    x = 0.0
    for i in range(0, 20):
        x = 2 * i + float(19)
        print(f"The value of x is = {x}")
    return

if __name__=="__main__":
    main()