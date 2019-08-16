# Fibonacci series:
# the sum of two elements defines the next

# a, b = 0, 1
# while a < 1000:
#     print(a)
#     a, b = b, a+b   #demonstrating that the expressions on the right-hand side
#                     #are all evaluated first before any of the assignments take place.
#                     #The right-hand side expressions are evaluated from the left to the right.

#defining function

def fib(n):        # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(n=int(input("Enter the value of n: ")))



def fib2(n):  # return Fibonacci series up to n
     """Return a list containing the Fibonacci series up to n."""
     result = []
     a, b = 0, 1
     while a < n:
         result.append(a)    # see below
         a, b = b, a+b
     return result
f100 = fib2(100)

print(f100)
