from tokenize import Name
import sys
import os

import numpy as np
import matplotlib.pyplot as plt

print(sys.argv)
print(os.getcwd())

try:
    print(a)
except:
    print("as is not defined!")

try:
    print(a)
except NameError:
    print("a is still not defined!")
except:
    print("Something else went wrong.")

print(a)