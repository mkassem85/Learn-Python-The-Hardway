#assign the number to type of people
types_of_people = 10
#string x to print types of people
x = f"There are {types_of_people} types of people."

#assign new variable
binary = "binary"
do_not = "don't"

#assign new string
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny! {}"

#use another format function
print(joke_evaluation.format(hilarious))

#Try adding two strings
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
