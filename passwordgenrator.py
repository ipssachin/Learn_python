# import random
#
# chl = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*_?"
#
# choice = int(input("Kindly enter password length: "))
#
# password = "".join(random.sample(chl,choice))
#
# print(password)




# import random
# import string
#
# chs = string.ascii_uppercase+string.ascii_lowercase+string.punctuation+str(list(range(0,10)))
#
# choice = int(input("Kindly enter password length: "))
#
# password = "".join(random.sample(chs,choice))
#
# print(password)


from collections import Counter


def find_duplicate_char(inputw):
    WC = Counter(inputw.lower())
    print(WC)
    j = -1

    for i in WC.values():
        j = j + 1
        if (i > 1):

            print(list(WC.keys())[j], end="")


if __name__ == "__main__":
    inputw = input("Enter word: ")
    find_duplicate_char(inputw)
