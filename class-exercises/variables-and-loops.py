'''
    Class Notes
    04/07/2022
    flow control
    04/05/2022
    numpy, variables, loops, and data types
'''
import numpy as np

def flow_control(k):
    if(k==0):
        s = "Variable k = %d equals 0. " % k
    elif(k==1):
        s = "Variable k = %d equals 1. " % k
    else:
        s = "Variable k = %d does not equal 0 or 1" % k
    print(s)

def main():
    i = 0
    n = 10
    x = 19.0

    y = np.zeros(n, dtype=float) # declares 10 0.0's

    for i in range(n):
        y[i] = 2.0 * float(i) + 1

    for y_element in y:
        print(y_element)

    # y = 1.9e2 == 190 in scientific notation

    i = 0
    flow_control(i)
    i = 1
    flow_control(i)
    i = 2
    flow_control(i)

if __name__=="__main__":
    main()