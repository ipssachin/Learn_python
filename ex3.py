#Will learn to use Variable and Names
print('='*100)
print("\t\t\t              Welcome to UDMS")
print('='*100)
cars = 90
space_in_a_car = 3.0
drives = int(input("Number of drivers can drive today: "))
passengers = int(input("Number of passangers availing uber today: "))
print('='*100)
print("System can be utilized for:")
print('='*100)
cars_not_driven = cars - drives
cars_driven= drives
carpool_capacity = cars_driven* space_in_a_car




print('There are ',cars,' cars available.')
print('There are only ',drives,' drivers available')
print('There will be ',cars_not_driven,' empty cars today')
print('We can transport ',carpool_capacity,' people Today')
print('We have ', passengers,' to carpool today')
average_passengers_per_car = passengers / cars_driven

if average_passengers_per_car > 4:
    #Homework find number of trips
    print("we need to do more trips to accomodate the number of passangers")
else:
    print("passangers has to wait")
# print('We need to put about ',average_passengers_per_car,' in each car')
print('='*100)
print('='*100)
