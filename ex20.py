#Functions can return someting
def add (a,b):
    print(f"ADDING {a} + {b}")
    return a + b
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b
def multiply(a, b):
    print(f"MULTIPLY {a} * {b}")
    return a * b
def divide(a,b):
    print(f"DIVIDE {a}/{b}")
    return (a / b)
print("Let's do some Math with just functions.")

age = add(30 , 5)
height = subtract(78 , 4)
weight = multiply(90 , 2)
iq = divide(100 , 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

#little extra
# 
# print("Here is a puzzle.")
#
# What = add(age,subtract(height,multiply(weight,divide(iq,2))))
#
# print("That becomes: ", What, "Can you do it by hands?")
