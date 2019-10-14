i= True
def number():
    global i
    if i== True:
        try:
            num  = int(input("Enter any number: "))
            return num
            i= False
        except:
            print("You must learn how to enter a number")
            i = True
        # return number()


print("Wellcome to the wordtionary game.")
objective = input("Give me an objective: ")
funny_name = input("Give me a funny name: ")
place = input("name of a place: ")
number()

print("""I thought to have {}
                but {}
                    is {} not my cup of team.
                        I might take {} balls and keep busting them.""".format(funny_name,place,objective,number()))
