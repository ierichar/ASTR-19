import numpy as np

x = 1.0
y = 2.0

print(f"np.sin{x} = {np.sin(x)}")
# sin, cos tan
# arcsin, arccos, arctan
# arctan2, rad2deg

# sinh, cosh, tanh
# arcsinh, arccosh, arctanh

# exponents and logarithms
# np.exp, log, log10, log2

# min/max/misc functions
# np.fabs - absolute value as float
# np.min(x,y) - min of x and y
# np.max(x,y) - max of x and y

# populate arrays
n = 100
z = np.arrange(n,dtype=float)
z *= 2.0*np.pi / float(n=1)
sin_z = np.sin(z)
