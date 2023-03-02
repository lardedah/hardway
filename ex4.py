#assigns 100 to 'cars', shows available cars 
cars = 100

#assigns 4.0 to space in each 'car'
space_in_a_car = 4.0

#assigns 30 drivers to the 100 cars, capping maximum useable cars to 30.
drivers = 30

#assigns 90 passengers to the task for transport
passengers = 90

#clarifies cars not driven, subtracts 30 (drivers) from 100 (cars), thus variable is given 70
cars_not_driven = cars - drivers

#clarifies total cars to be driven as being the amount of drivers available. now linked one-way (changing drivers after this point would change cars_driven)
cars_driven = drivers

#creates variable to represent the amount of passengers that that can be carried by pulling cars_driven (drivers) and simply multiplying that by the seats per vehicle.
carpool_capacity = cars_driven * space_in_a_car

#defines how many people will be in each car, as we know the total passengers and the number of cars (drivers) available.
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
        "in each car.")