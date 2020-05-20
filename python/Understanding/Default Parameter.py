"""
Python evaluate the default values for parameteres upon defined, 
not upon called
Modification on mutable objects will be persistent across invocation
"""
from random import random

def dummy(x = []):
    x.append(random())
    return x


print(dummy())
print(dummy())