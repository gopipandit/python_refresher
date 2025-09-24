from setuptools import *
from functools import *



def get_reduced(*args):
    return reduce(lambda x,y: x+y, args)


if __name__ == '__main__':
    print(get_reduced(12,3,4,5,6,7,4,6,90))