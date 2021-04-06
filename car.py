cars=200
space_in_a_car=4
drivers= 30.0
passengers=155

cars_not_driven =cars-drivers
cars_driven= drivers
car_pull_capacity=drivers * space_in_a_car
average_passengers_per_car=passengers/cars_driven
print("There are",cars,"cars available.")
print("We have only",drivers,"drivers available now.")
print("There will be",cars_not_driven,"not available.")
print("We can transport only",car_pull_capacity,"people today sorry with the inconvinces we might have cost")
print("We have",passengers,'number of people to carry')
print("We can cater for",average_passengers_per_car,'per car for each car')
