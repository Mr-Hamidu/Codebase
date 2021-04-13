def add(a,b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a,d):
    print(f"Subtrasctng {a} - {d}")
    return a - d

def multiply(a,b):
    print(f"Multiplying {a} * {b}")
    return a* b

def divide(a,b):
    print(f"Dividing {a} / {b}")
    return a /b
print("Let's d some math with just functions")
age = add(float(input()),float(input()))
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)
print(f"Age: {age},\n Height:{height},\n Weight:{weight},\n IQ:{iq}\n")

print("Here is a puzzle.")
meat = multiply(age, divide(height,add(weight,subtract(iq,2))))
print("That becomes:", meat,"Can you do it by hand?")
