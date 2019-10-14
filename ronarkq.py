fruits = ['Apple','Tomato','Cake','Chockolate']
print(range(len(fruits)))
for s in range(len(fruits)):
    f= input("Enter a fruits name: ")
    for x in fruits:
        if f == x:
            print("We found this in Fruits list.")
            break
    else:
        print("Try again.")
        continue
