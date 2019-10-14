#4.1. if Statements
# x = int(input("Please enter an integer: "))
#
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')


#4.2. for Statements

# # Measure some strings:
# words = ['cat', 'window', 'defenestrate']
# # for w in words:
# #     print(w, len(w))
#
# for w in words[:]:  # Loop over a slice copy of the entire list.
#     if len(w) > 6:
#         words.insert(1, w)
# #
# print(words)
#
# a =[]
#
# for i in range(0,100):
#     if i < 10:
#         # a.append(i)
#         print('-\t' * i)
#     elif i > 30 and i <60:
#         print('*'*i)
#     else:
#         print("\t\/\/"*i)

#4.3. The range() Function
# It generates arithmetic progressions
#
# for i in range(2,3):
#     print(i)


# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])


# print(range(10))

# print(list(range(20)))



#4.4. break and continue Statements, and else Clauses on Loops

#check on pythontutor

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')


# for n in range(2, 5):
#     print("n: ", n)
#     for x in range(2, n):
#         print("x: ",x)
#         print("n: ",n)
#         print("mod: ", n%x)
#
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')

#continue statement

# for num in range(2, 10):
#     if num % 2 == 0:
#         print("Found an even number", num)
#         continue
#     print("Found an odd number", num)





#4.5. pass Statements
#The pass statement does nothing. It can be used when a statement is
#required syntactically but the program requires no action.


# while True:
#     pass  # Busy-wait for keyboard interrupt (Ctrl+C)

# def initlog(*args):
#     pass   # Remember to implement this!
#
# initlog()

#pass will be just ignored







#4.6. Defining Functions
#
# def fib(n):        # write Fibonacci series up to n
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()
#
# fib(n=int(input("Enter the value of n: ")))
# #
#
#read and ask tommorow if you don t understand This
# def fib2(n):  # return Fibonacci series up to n
#      """Return a list containing the Fibonacci series up to n."""
#      result = []
#      a, b = 0, 1
#      while a < n:
#          result.append(a)    # see below
#          a, b = b, a+b
#      return result
# f100 = fib2(100)
#
# print(f100)


# #4.7. More on Defining Functions
#4.7.1. Default Argument Values¶
# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         #below line of code introduces 'in' key word which compares our resoponse in the predefined set of responses
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)

# #function can be called in servarl ways:
# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 2)
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

# #The default values are evaluated at the point of
 # function definition in the defining scope
# i = 5
#
# def f(arg=i):
#     print(arg)
#
# i = 6
# f()

"""Important warning:
The default value is evaluated only once. This makes a difference
when the default is a mutable object such as a list, dictionary,
or instances of most classes.
For example, the following function accumulates the arguments passed
to it on subsequent calls:"""

# def f(a, L=[]):
#     L.append(a)
#     #return functon will return value to the function
#     return L
#
# print(f(1))
# print(f(2))
# print(f(3))

#If you don’t want the default to be shared between subsequent calls,
#you can write the function like this instead:

# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L
#
# print(f(1))
# print(f(2))
# print(f(3))

#4.7.2. Keyword Arguments

#Functions can also be called using keyword arguments of the form
#kwarg=value. For instance, the following function:

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
# parrot()                                              # required argument missing
# parrot(voltage=5.0, 'dead')                           # non-keyword argument after a keyword argument
# parrot(110, voltage=220)                              # duplicate value for the same argument
# parrot(actor='John Cleese')                           # unknown keyword argument


"""
 dict constructor:
 Return a new dictionary initialized from an optional
 positional argument and a possibly empty set of keyword arguments.
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
"""
#
# #
# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])
#
# # cheeseshop('Limburger')
#
# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.","anything else sir!",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")
# # Note that the order in which the keyword arguments are printed
# # is guaranteed to match the order in which they were provided in the function call.

# #4.7.3. Arbitrary Argument Lists create custom Functions
#
# def concat(*args, sep="/"):
#     return sep.join(args)
# print("earth", "mars", "venus")
# print(concat("earth", "mars", "venus"))
# print("earth", "mars", "venus", sep="*")

#4.7.4. Unpacking Argument Lists

# print(list(range(3, 6)))            # normal call with separate arguments
#
# args = [0,6]
# print(list(range(*args)))           # call with arguments unpacked from a list

# #same way we can pass dictionary values using **
# #
# def parrot(voltage, state='a stiff', action='voom'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.", end=' ')
#     print("E's", state, "!")
#
# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# parrot(**d)

#4.7.5. Lambda Expressions
#Small anonymous functions can be created with the lambda keyword.
#This function returns the sum of its two arguments: lambda a, b: a+b.
#λ(x)

# def make_incrementor(n):
#     return lambda x: x + n
#
# f = make_incrementor(42)
# print(f(0))
# print(f(1))

#another example of incrementing position:
# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'), (6, 'six')]
# pairs.sort(key=lambda pair: pair[1])
# print(pairs)

# #4.7.6. Documentation Strings (print document string __doc__)
# #
# def my_function():
#     """Do nothing, but document it.
#
#     No, really, it doesn't do anything.
#     """
#     pass
# #
# # print(my_function)
# print(my_function.__doc__)


#4.7.7. Function Annotations
#Return annotations are defined by a literal ->

# def f(ham: str, eggs: str = 'eggs') -> int:
#     print("Annotations:", f.__annotations__)
#     print("Arguments:", ham, eggs)
#     return ham + ' and ' + eggs
#
# f('1','milk')

"""
4.8. Intermezzo: Coding Style
google Intermezzo: Coding Style or PEP 8 coding style.
"""
