#Total number of cars
cars= 100
#Car capacity
space_in_a_car = 4.0
#Total number of drivers
drivers = 30
#Total number of passengers
passengers = 90
#Cars without drivers
cars_not_driven = cars - drivers
#Actula cars driven
cars_driven = drivers
#Total number of carpool capacity (number of cars_driven * car capcity)
carpool_capacity = cars_driven * space_in_a_car
#Average passengers per cars driven (number of passengers / cars_driven)
average_passengers_per_car = passengers/cars_driven

#Print Total number of cars
print("There are", cars,"cars available.")
#Print total number of drivers
print("There are only", drivers,"drivers available.")
#Print totla number of cars not cars not driven
print("There will be", cars_not_driven,"empty cars today.")
#Print car pool capcity
print("We can transport", carpool_capacity,"people today.")
#Print total number of passengers
print("we have", passengers,"to carpool today.")
#Print passengers per cars
print("We need to put about",average_passengers_per_car,"in each car")
