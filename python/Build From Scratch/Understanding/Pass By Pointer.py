

print("Scalar Test")
print("===============")
a = 1
print("Value before change:\t", a)

def change(x):
    x = 3

change(a)
print("Value after change:\t", a)



print("\n\n#Immutable Object")
print("===============")
print("\nString Test #1")
"""
Replace the string
"""
a = "123456"
print("Value before change:\t", a)

def change(x):
    x = "333"

change(a)
print("Value after change:\t", a)



print("\nString Test #2")
"""
Replace the string
"""
a = "123456"
print("Value before change:\t", a)

def change(x):
    x = x.replace("3","9")

change(a)
print("Value after change:\t", a)



print("\n\nMutable Object")
print("===============")
print("\nList Test #1")
"""
Replace the list
"""
a = [1,2,3,4]
print("Value before change:\t", a)

def change(x):
    x = [3]

change(a)
print("Value after change:\t", a)



print("\nList Test #2")
"""
Update one of the variable in list
"""
a = [1,2,3,4]
print("Value before change:\t", a)

def change_a4(x):
    x[0] = 9

change_a4(a)
print("Value after change:\t", a)



print("\nList Test #3")
"""
Replace the list
"""
a = [1,2,3,4]
print("Value before change:\t", a)

def change_a4(x):
    x = x[:] * 2

change_a4(a)
print("Value after change:\t", a)


print("\nList Test #4")
"""
Append to current list
"""
a = [1,2,3,4]
print("Value before change:\t", a)

def change_a4(x):
    x.append("5")

change_a4(a)
print("Value after change:\t", a)



print("\nDict Test #1")
"""
Add new key/value to current dict
"""
a = {"A": 1}
print("Value before change:\t", a)

def change(x):
    x["B"] = 3

change(a)
print("Value after change:\t", a)


print("\nDict Test #2")
"""
Replace the dict
"""
a = {"A": 1}
print("Value before change:\t", a)

def change(x):
    x = {"C": 3}

change(a)
print("Value after change:\t", a)





print("\n\nObject Oriented")
print("===============")
print("\nOO Test #1")
"""
Replace the OO scalar value
"""
class Dummy:
    def __init__(self, x):
        self.x = x



a = Dummy(1)
print("Value before change:\t", a.x)

def change(x):
    x.x = 3

change(a)
print("Value after change:\t", a.x)



print("\nOO Test #2")
"""
Replace the OO list value
"""
a = Dummy([1,2,3])
print("Value before change:\t", a.x)

def change(x):
    x.x = [5,6,7]

change(a)
print("Value after change:\t", a.x)