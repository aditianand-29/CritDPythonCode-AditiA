# -------------------------------------------------------------------------------------------
#         Python code that checks if three numbers can be sides of a triangle or not
# -------------------------------------------------------------------------------------------

print ('This program aims to determine if any three numbers can be sides of a triangle or not')

print ('Input any 3 Positive real numbers greater than 0 to check if they can be sides of a triangle')

# input three integers: a, b & c
# input validation checks : [1] Check if string or number [2] Check if number is > 0

a = input('Enter positive value for a = ')

while not a.isdigit() or int(a) <= 0:      #this is a while loop that tells the computer what to do if the input is a string or number is < 0.
    
    if not a.isdigit():   #isdigit is a function that checks if the number is a digit or not
       a = input('No strings allowed. Re-enter positive value for a = ')   #if it is not a number, it will output an error message, and ask for the input again
       
    elif int(a) <= 0:
       a = input('Number must be greater than 0. Re-enter positive value for a = ') # output error message when the number is less than zero

b = input('Enter positive value for b = ')

while not b.isdigit() or int(b) <= 0:
    
    if not b.isdigit():
       b = input('No strings allowed. Re-enter positive value for b = ')
       
    elif int(b) <= 0:
       b = input('Number must be greater than 0. Re-enter positive value for b = ')
       
c = input('Enter positive value for c = ')

while not c.isdigit() or int(c) <= 0:
    
    if not c.isdigit():
       c = input('No strings allowed. Re-enter positive value for c = ')
       
    elif int(a) <= 0:
       c = input('Number must be greater than 0. Re-enter positive value for c = ')

# print with format; {variable} outputs the value/content of the variable to the screen
print(f'You entered a = {a} , b = {b} and c = {c}')

if a+b>c and b+c>a and a+c>b:
    print ('These numbers CAN be sides of a triangle') 

else:print ('These numbers CANNOT be sides of a triangle')
print ('end')