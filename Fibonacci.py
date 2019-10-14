# Fibonacci series:
# the sum of two elements defines the next

a, b = 0, 1
while a < 1000:
    print(a)
    a, b = b, a+b   #demonstrating that the expressions on the right-hand side
                    #are all evaluated first before any of the assignments take place.
                    #The right-hand side expressions are evaluated from the left to the right.
