#Function and Methonds

import time
import threading
import pandas as pd
import random

def cr_lst():
    """This function will create a list from user input"""
    lst =[]
    idx =[]
    print(""" Select 1 for manual list creation and 2 for automated list creation""")

    # s = int(input("Provide a number to create a list >> "))
    try:
        choice = int(input(">> "))
        if choice == 1:
            s = int(input("Provide a number to create a list >> "))
            for i in range(s):
                time.sleep(1)
                lst.append(i)
                print(lst,end="\r")
                idx.append(id(i))

            return lst, idx
        elif choice == 2:
            for i in range(random.randint(0,20)):
                time.sleep(1)
                lst.append(i)
                print(lst,end="\r")
                idx.append(id(i))

            return lst, idx
        else:
            print("Kindly Enter 1 or 2")

    except TypeError as e:
        print("Error: {}\n".format(e))
        return




# result =cr_lst(int(input(">> ")))

# print(len(result))
# print(result[0])
# def s_b_s():
#
#     f1= cr_lst()
#     j =[]
#     b=[]
#     for i in range(len(f1[0])):
#         j.append(f1[0][i])
#         b.append(f1[1][i])
#     print(pd.DataFrame({'number':j,'memory_location':b}))
#
#     # rem=[(i,j) for i in result[0] for j in result[1]]
#     # print (rem)
# s_b_s()


def cr_sort_tuple():
    t = []
    while True:
        a = input(">> ")
        if a == 'brk':
            break
        else:
            for i in a:
                t.append(i)
    print(type(t))
    print("t =",t)

    t = sorted(t)
    t= tuple(t)
    print(t)
    print(type(t))
    return t

# print(cr_sort_tuple())


def sr_str(s):
    str = """
                The Zen of Python

        Beautiful is better than ugly.
        Explicit is better than implicit.
        Simple is better than complex.
        Complex is better than complicated.
        Flat is better than nested.
        Sparse is better than dense.
        Readability counts.
        Special cases aren't special enough to break the rules.
        Although practicality beats purity.
        Errors should never pass silently.
        Unless explicitly silenced.
        In the face of ambiguity, refuse the temptation to guess.
        There should be one–and preferably only one–obvious way to do it.
        Now is better than never.
        Although never is often better than *right* now.
        If the implementation is hard to explain, it's a bad idea.
        If the implementation is easy to explain, it may be a good idea.
        """
    # str = tuple(str)
    if s != "":
        if s in str:
            print("we found '{}' in the string".format(s))
            j = str.find(s)
            for i in range(j):
                print(str[i], end="")
            print(s)
        else:
            print("Sorry requested word '{}' not available in the string.".format(s))
            print(str)
# sr_str(input(">>"))


def pd_lst():
    cr1 = cr_lst()
    num = pd.Series(cr1[0])
    ids = pd.Series(cr1[1])
    print(pd.DataFrame({'Number': num,'Id': ids}))


if __name__ == '__main__':

    print("""
                        Welcome to PyLearn
            We have created a module to understand basic python concepts in 
            a better way. Below are the few examples which you should try.
            select the option to understand more about these functions
                 1) List Creation using loop
                 2) return list elements and there identity
                 3) Turn list into DataFrame for Pandas
                 4) Create and sort Tuple
                 5) Search and return string
                         """)
    choice = int(input(">> "))

    if choice == 1:
        print(cr_lst())
    elif choice == 3:
        pd_lst()
    elif choice ==5:
        sr_str(input("Entere search string>>"))
    elif choice == 4:
        cr_sort_tuple()
