#Person name
my_name = 'Zed A. Shaw'
#Person age
my_age = 35
#Height in inches
my_height = 74
#height in cm
my_height_cm = my_height * 2.54
#Weight in lbs
my_weight = 180
#weight in kg
my_weight_kgs = my_weight / 2.205
#eyes color
my_eyes = 'Blue'
#Teeth color
my_teeth = 'White'
#Hair color
my_hair = 'Brown'

#Printing the name using the (f) format
print(f"Let's talk about {my_name}")
#Printing tall in inches and converting it to cm
print(f"He's {my_height} inches tall which is {my_height_cm} in cm")
#Printing weight in lbs and converitng it to kg
print(f"He's {my_weight} pounds heavy which is {round(my_weight_kgs)} in kgs")
print("Actually that's not too heavy.")
#Printing his eyes and hair colors
print(f"He's got {my_eyes} eyes and {my_hair} hair")
#Printing his teeth color
print(f"His teeth are usually {my_teeth} depending on the coffe.")
#Printing adding together his age, height and Weight
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}")
