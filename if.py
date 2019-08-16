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
#     print("more")


# #for loop
# # Measure some strings:
# words = ['cat', 'window', 'defenestrate']
# # for w in words:
# #     print(w, len(w))
#
# for w in words[:]:          # Loop over a slice copy of the entire list.
#     if len(w) > 6:
#         words.insert(0, w)
#         print(words)
#
# #range() Function
# for i in range(5):
#     print(i)

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# print(a)
# for i in range(len(a)):
#     print(i,a[i])

# #print(range()) what went wrong
# print(range(10))
# #instead we can use list(range())
# print(list(range(10)))

# #break and continue Statements, and else Clauses on Loops
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')


#continue statement
for num in range(2, 21):
    if num % 2==0:
        print("Found an even number", num)
        continue
        print("Found a number", num)
