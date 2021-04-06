#here we declare our variable formatting
formatting = "5,{},{},{},{},"
a=1,2,3,4
#display we have value asigned to famatting
print(f"we have {formatting.format(1,2,3,4)}")
print("I like ",formatting.format("one","two",'three',"four"))
print(formatting.format('False' ,"False","True","True"))
print(formatting.format("I'm the boss",
"better than those",
 "higher than most",
 'I fear no man'))
print("The key word here",formatting)
