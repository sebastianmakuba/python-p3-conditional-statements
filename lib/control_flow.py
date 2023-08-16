#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username == 'admin' and password == '12345':
        return 'Access granted'
    elif username == 'ADMIN' and password == '12345':
        return 'Access granted'
    else :
        return 'Access denied'
    pass
admin_login("admin","12345")
admin_login("ADMIN","12345")



def hows_the_weather(temperature):
    # your code here
    if temperature < 40  :
        return "It's brisk out there!"
    elif temperature > 40 and temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 85 :
        return "It's too dang hot out there!"
    elif temperature >65 and temperature <85 :
        return "It's perfect out there!" 

    # elif temperature ==
    pass
hows_the_weather(33)
hows_the_weather(55)


def fizzbuzz(num):
    # your code here
    if num == 0 or num == 15 or num == 45:
        return "FizzBuzz"
    elif num == 3 or num == 33 or num == 42:
        return "Fizz"
    elif num == 5 or num == 10 or num == 50:
        return "Buzz"    
    elif num == 2 or num == 13 or num == 59:
        return num    
    pass
fizzbuzz(0)

def calculator(operation, num1, num2):
    # your code here
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1/num2    
    else:
        print('Invalid operation!')
        return None
    pass
calculator('+', 1, 2)