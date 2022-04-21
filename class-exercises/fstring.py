import sys

class Shape:
    def print(self):
        print("Here is our shape!")
        print(f"Number of sides = {self.num_sides}")
        print(f"Length of sides = {self.side_length}")
    
    def __init__(self, nsides=3, length=1.):
        self.num_sides = nsides
        self.side_length = length


def main():
    s = 'hi'
    t = 'more'
    u = 'let'
    v = 'creed'

    print(f"{s} {t} {u} {v}")

    i = 10230493
    print(f"{i}")
    print(f"{i:12d}")
    print(f"{i:012d}")

    x = 1031029233.4
    print(f"{x}")
    print(f"x with 9 digits and 8 after decimal =  {x:9.8e}")
    print(f"x with 11 digits and 10 after decimal = {x:11.10e}")

    nsides = 3
    length = 10
    if(len(sys.argv)>=2):
        nsides = int(sys.argv[1])
    if(len(sys.argv)>=3):
        length = float(sys.argv[2])
    our_shape = Shape(nsides=nsides, length=length)
    our_shape.print()

if __name__=="__main__":
    main()