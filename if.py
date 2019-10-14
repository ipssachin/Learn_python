# x = int(input("Please enter an integer: "))
# # z = int(x)
# # print(z)
# # print(type(z))
# #
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print("more")


#for loop
# Measure some strings:
# words = ['cat', 'window', 'defenestrate']
# print(len(words))
# print(words[0],len(words[0]))
# print(words[1],len(words[1]))
# print(words[2],len(words[2]))
#
# for w in words:
#     print(w, len(w))
# #
# d = [1,5,4,3,7,6,9]
#
# for i in d:
#     print(i,type(i))

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


# #continue statement
# for num in range(2, 21):
#     if num % 2==0:
#         print("Found an even number", num)
#         continue
#         print("Found a number", num)


#While loop

i = 0



while True:
    print(i)
    i+=1
