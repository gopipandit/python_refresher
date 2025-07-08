class BasicMath:

    def __init__(self):
        pass

    def add(self, a,b):
        return a+b

    def subtract(self, a,b):
        return a-b

    def multiply(self,a,b):
        return a*b

    def divide(self,a,b):
        if b == 0:
            raise ZeroDivisionError("Denominator is zero")
        else:
            return a/b


if __name__ == "__main__":
    a = 35
    b = 7
    m = BasicMath()
    print("This is my Internal file")
    print("Add::\n",m.add(a,b))
    print("subtract::\n",m.subtract(a,b))
    print("multiply::\n",m.multiply(a,b))
    print("multiply::\n",m.multiply(a,b))