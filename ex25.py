people = 50
cars = 10
trucks = 55

if cars > people:
    print("We should take the cars.")
elif cars<people:
    print("We should not take the cars.")
else:
    print("We cant decide.")

if trucks>cars:
    print("That's too many trucks.")
elif trucks<cars:
    print("Maybe we could take trucks.")
else:
    print("We still cant decide.")
if people>trucks:
    print("Alright lets just take the trucks.")
else:
    print("Fine, let's stay home then.")
