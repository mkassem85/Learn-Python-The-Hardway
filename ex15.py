#This ex to use the latest argv to open a file and read then print its content
from sys import argv
ex_name, file_name = argv
#open the file
txt = open(file_name)

#print the content of the file_name
print(f"Here's your file {file_name}:")
print(txt.read())
txt.close()

#Take the file name from the user
prompt = '> '
print("="*50,"\nType the file name again:")
file_again = input(prompt)
txt_user = open(file_again)

print(txt_user.read())
txt_user.close()
