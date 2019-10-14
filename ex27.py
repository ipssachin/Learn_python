#Loops and Lists

the_count=[1,2,3,4,5,8]
fruits = ['apples', 'oranges', 'pears', 'appricots','banana']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
#this first kind of for-loop goes throught Lists

# for number in the_count:
#     print(f"This is count {number}")
#
# #same as above
# for fruit in fruits:
#     print(f"A fruit of type: {fruit}")
#
# #also we can go through mixed list too
# #Notice we have to use {} since we dont know whats in it
#
# for i in change:
#     print(f"I got {i}")
# #we can also build lists, first start with an empty one
#
elements=[]
#
# #then use the range functin to do 0 to 5 counts
#
for i in range(0,6):
    # print(f"Adding {i} to the list.")
    #append is a function that lists understand
    elements.append(i)
print(elements)
# #now we can print them out too
for i in elements:
    print(f"Element was: {i}")
#
