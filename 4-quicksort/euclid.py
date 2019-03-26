#!/usr/bin/python3

class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def GCD(self):
        x = self.x
        y = self.y
        if x == y:
            # perfect square already
            return x
        elif x > y:
            if x % y == 0:
                # y is the GCD
                return y
            else:
                # recurse
                new_box = Box(x%y, y)
                return new_box.GCD()
        elif y > x:
            if y % x == 0:
                # x is the GCD
                return x
            else:
                # recurse
                new_box = Box(y%x, x)
                return new_box.GCD()


def main():
    print("Welcome to the Euclid's algorithm demonstrator.\nThis will show you the greatest common denominator between two numbers.")
    x = float(input("First number: "))
    y = float(input("Second number: "))
    box = Box(x,y)
    print(box.GCD())

if __name__ == "__main__":
    main()