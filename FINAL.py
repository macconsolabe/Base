
  # Write a simple program to average three exam scores.- 
  #Get user inputs for three scores- 
  #Write a function to calculate the average- 
  #Print the average value
def average():
	
	print("Welcome to our average program")
	first_number = int(input("Please Enter your first number here : "))
	second_number = int(input("Please Enter Your second number here :"))
	third_number = int(input("Please Enter Your second number here :"))
	average = (first_number + second_number+third_number)/3
	print (average)

average()


#Write a program to calculate area for the circles.  
#-Get user input for the starting radius
#-Calculate the area for the next 5 numbers including user entered radius value.
#-write a function to calculate the area.        
#- Print the areas horizontally         
#-Use python library to get the pi - value.

def circle_area():
	print("Welcome to our area calculator")
	input1= int(input("Please enter the radius you would like to calculate the area of here :"))
	import math
	results = math.pi* (input1*input1)
	i = 0
	while i < 5:
		print(math.pi* (input1*input1))
		input1 = input1 + 1
		if (i == 5):
			break
		i = i + 1
	
circle_area()

# Write a program to list the square root, starting from 2 to user entered number
#- get the user input
#- Calculate the square root for each number
#- round to the 2 decimal position.        
#   NO              Square root
#----------     ------------------   
#2                    1.4    
#3                    1.73   
#4                    2   
#5                    2.2

numbers = int(input("Please Enter your number here : ")) 
print("No", "Square root") 
print("--", "-------") 
for x in range(numbers): 
	print (x, math.sqrt(x))


#  Simple string processing program to generate usernames.
#- get user input (first name and last name)
#- Take first character from the first name and the last character from the last name       
#- add number 042019 and print the user nameif users enters "John" and "Smith" as first and last name respectively, your programshould print the user name as "js042019
input4 = input("Please Enter Your First name :")
input5 = input("Please enter your last name : ")

list(input4)
list(input5)


print(input4[0]+input5[0]+"042019")

# Draw a circle in a rectangle using python turtle graphics library.   
# - use a function to draw rectangle    
#- use a function to draw circle
import turtle as t
def circle():
	t.begin_fill()
	t.color("red")
	t.circle(50)
	t.end_fill()

def line():
	t.forward(100)

def square():
	t.begin_fill()
	t.forward(100)
	t.left(90)
	t.forward(100)
	t.left(90)
	t.forward(100)
	t.left(90)
	t.forward(100)
	t.end_fill
line()
circle()
square()