#print message
print('hello world')

#add two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
sum = int(num1) + int(num2)
print("print the sum is:",sum)

#leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

    #PI value
    import math
print(math.pi)

#square
num = float(input("Enter a number: "))  
square = num ** 2                       
print(f"Square: {square}")    

#area of circle
import math
radius = float(input("Enter the radius: "))
area = math.pi * radius ** 2  
print(f"Area of the circle: {area:.2f}")

#check data type
num = 42
text = "hello"
print(type(num)) 
print(type(text)) 

#math function
import math
print(math.pi)       
print(math.sqrt(16))  
print(math.sin(math.pi / 2))  

#power
base = float(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print(base ** exponent) 

#positive or negative
num = float(input("Enter a number: "))

if num > 0:
    print("Positive")  
elif num < 0:
    print("Negative") 
else:
    print("Zero")

#odd or even 
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")

    #constant value
    SPEED_OF_LIGHT = 299792458
PI = 3.14159
MAX_VALUE = 100
print(SPEED_OF_LIGHT)
print(PI)
print(MAX_VALUE)






