'''
    Session 5
    ASTR-19-01 Spring 2022
    March 31st, 2022
    Ian Richardson

    This program writes out a table of the function
    sin(x) vs x and is tabulated between 0 and 2PI
    with a thousand entries.
'''
import numpy as np

NUM_OF_ENTRIES = 1000

def main():
    x_values = np.arange(0, 2*np.pi, (1/NUM_OF_ENTRIES))
    y_values = np.sin(x_values, dtype=float)

    print("sin(x)" + " "*9 + "x")
    for i in range(NUM_OF_ENTRIES):
        print(f"{y_values[i]:1.8e} {x_values[i]:1.8e}")

if __name__=="__main__":
    main()