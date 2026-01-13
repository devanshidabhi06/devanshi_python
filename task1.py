#simple intrest
p = float(input("Enter principal: "))
t = float(input("Enter time (years): "))
r = float(input("Enter rate (%): "))
si = (p * t * r) / 100
print("Simple Interest:", si)

#Maximum of Two Numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
max_num = max(a, b)
print("Maximum:", max_num)

#Print 1 to 5
for i in range(1, 6):
    print(i)

#String Length
s = input("Enter a string: ")
length = len(s)
print("Length:", length)

#Welcome Message
print("Welcome to Python Programming!")

#First Character
s = input("Enter a string: ")
first = s[0]
print("First character:", first)

#Last Character
s = input("Enter a string: ")
last = s[-1]
print("Last character:", last)

# Positive/Negative
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#Add Three Numbers
a = float(input("Enter first: "))
b = float(input("Enter second: "))
c = float(input("Enter third: "))
sum_num = a + b + c
print("Sum:", sum_num)

# User Input
user_input = input("Enter anything: ")
print("You entered:", user_input)
