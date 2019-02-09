#!/usr/bin/python

# Introduction Learn Python:SYNTAX
#Python is a programming language. Like other languages, it gives us a way to communicate ideas. In the case of a programming language, these ideas are "commands" that people use to communicate with a computer!

#We convey our commands to the computer by writing them in a text file using a programming language. These files are called programs. Running a program means telling a computer to read the text file, translate it to the set of operations that it understands, and perform those actions.

my_name = "David Klaymi"
print("Hello and welcome " + my_name + "!")

#Comments

#Ironically, the first thing we're going to do is show how to tell a computer to ignore a part of a program. Text written in a program but not run by the computer is called a comment. Python interprets anything after a # as a comment.

#Variables
#Programming languages offer a method of storing data for reuse. If there is a greeting we want to present, a date we need to reuse, or a user ID we need to remember we can create a variable which can store a value. In Python, we assign variables by using the equals sign (=).

message_string = "Hello there"
# Prints "Hello there"
print(message_string)

#In the above example, we store the message "Hello there" in a variable called message_string. Variables can't have spaces or symbols in their names other than an underscore (_). They can't begin with numbers but they can have numbers after the first letter (e.g., cool_variable_5 is OK).

#It's no coincidence we call these creatures "variables". If the context of a program changes, we can update a variable but perform the same logical process on it.

# Greeting
message_string = "Hello there"
print(message_string)

# Farewell
message_string = "Hasta la vista"
print(message_string)

#Above, we create the variable message_string, assign a welcome message, and print the greeting. After we greet the user, we want to wish them goodbye. We then update message_string to a departure message and print that out.

lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""

lovely_loveseat_price = 254.00

stylish_settee_description ="""Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""

stylish_settee_price = 180.50

luxurious_lamp_description ="""Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""

luxurious_lamp_price = 52.15

sales_tax = 0.088


customer_one_total = 0

customer_one_itemization =""


customer_one_total += lovely_loveseat_price

customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price


customer_one_itemization += luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax

print("Customer One Items:")
print(customer_one_itemization)

print("Customer One Total:")
print(customer_one_total)

customer_two_total = 0

customer_two_itemization =""

customer_two_total += stylish_settee_price

customer_two_itemization += stylish_settee_description


customer_two_total +=luxurious_lamp_price

customer_two_itemization +=luxurious_lamp_description


customer_two_tax = customer_two_total * sales_tax

customer_two_total += customer_two_tax


print("Customer Two Items:")
print(customer_two_itemization)

print("Customer Two Total:")
print(customer_two_total)

def loading_screen():
	print("This page is loading...")
  
loading_screen()

def mult_two_add_three(number):
	#number = 5
	print(number*2 + 3)
  
# Call mult_two_add_three() here:

mult_two_add_three(0)

def mult_x_add_y(number, x, y):
	print(number*x + y)
  
mult_x_add_y(1, 3, 1)  
