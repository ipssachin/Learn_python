#names Variables, Code, Functions
def print_two(*argv):
    arg1,arg2=argv
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1,arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothing'.")

print_two("Sachin", "Jadhav")
print_two_again("Sachin", "Jadhav")
print_one("First")
print_none()
