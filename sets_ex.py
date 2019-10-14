people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun","Jay"}


#Unique values from both sets

population = people.union(vampires)

print(population)

#Common values from both sets

victims = people.intersection(vampires)

print(victims)

#clears the set
victims.clear()
print(victims)

#new set = set1 - set2

safe = people.difference(vampires)

print(safe)