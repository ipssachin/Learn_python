def test():
    print("this is test")


def test1():
    print("this is test1.")

if __name__ == "__main__":
    test()
    test1()
    print("Executed when called from same file.")
else:

    print("Executed when used as imported")
