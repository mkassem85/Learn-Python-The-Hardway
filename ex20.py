from sys import argv
script, input_file = argv

#Function to read all the file contents
def print_all(file):
    print(file.read())

#function to reset the cursor of reading the file to the start point
def rewind(file):
    file.seek(0)

#function to read the file line by line
def print_a_line(line_count,file):
    print(line_count, file.readline(),  end="")

current_file = open(input_file)
#reading the whole file
print("First let's print the whole file:\n")
print_all(current_file)

#rewind the file
rewind(current_file)

#reading the file line by line
print("Now let's print three lines:")

current_line = 1

print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

#Test readline function
print(current_file.readline())
print(current_file.readline())
print(current_file.readline())
