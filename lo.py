from sys import argv
#seperate the argument module into two variables
script, filename = argv
# the value given to file name is opened
text = open(filename)
#string shows user the name of file
print(f"Here's your file {filename:}")
#displays the content of text
print(text.read())
#Displays string to the user
print("Type the filename again:")
#user inputs the value of file_again
file_again = input("")
#give value t varialble text_again which is to open file_again
text_again = open(file_again)
#displays value of text_again
print (text_again.read())
