from sys import argv
script, user_name,local = argv
#prompt=''

print(f" Hi {user_name}, I'm the {script} script.")
print(" I'd like to ask you a few questions.",local)
print("Do you like me", user_name,end='')
likes = input()

print(f"Where do ou live {user_name}?",end='')
lives = input()
print("What kind of computer do you have?",end="")
computer = input()
print(f"Alright so you said {likes} about me \n You live in {lives} . Not sure Where that should be, \n and you have a {computer} computer that's nice ")
