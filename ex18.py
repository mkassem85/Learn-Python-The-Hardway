#New things to learn, including function arguments
#using something like argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#Define simpme function with two arguments
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#function with only 1 argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#function with no arguments
def print_none():
    print("I got nothin'.")

#Calling the functions
print_two("Muhammad","Kassem")
print_two_again("Muhammad","Kassem")
print_one("First!")
print_none()
