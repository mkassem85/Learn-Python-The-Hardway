from sys import argv

script,filename = argv

#Just printing the file name
print(f"We're going to raise {filename}.")
#Instructions for the user
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename,'w')
#Empty the file
print("Truncating the file. Goodbye!")
target.truncate()

#Get the text from the user to write in the file
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

#Writing to the file

print("I'm going to write this to the file")

#Use the write function
target.write(line1+"\n"+line2+"\n"+line3)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finallly, we close it.")
target.close()

read_target = open(filename)
print(read_target.read())