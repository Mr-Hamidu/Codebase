from sys import argv
monitor,myname= argv

print(f"We are going to earse {myname}.")
print("If you don't want that , hit CTRL-C (^C).")
print("If you want that hit RETURN.")

input("")

print("Opening the file.....")
target = open(myname, "w+")

print("Truncating the file. Goodbye!")
#target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)#,"\n" line2, "\n", line3,"\n")
#target.write("\n")
target.write(line2)
#target.write("\n")
target.write(line3)
#target.write("\n")

print("And finally, we close it.")
target.close( )
