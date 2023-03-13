# In this project, I will be creating a python calculator as my first project

# Welcome message
def welcome():
    print('''Welcome to the Calculator program. Have fun!''')


# Define the calculator function
def Calculator():
    # Adding conditions
    operation = input('''Enter the operation your want to use
    + for addition
    - for subtraction
    * for multiplication
    / for division''')
    
    # Prompt user to enter numbers
    num_1 = int(input('Enter the first Number: '))
    num_2 = int(input('Enter the second number: '))
    # Adding operations
    if operation == '+':
        print('{} + {} = '.format(num_1, num_2))
        print(num_1 + num_2)
    # Subtraction operations
    elif operation == '-':
        print('{} - {} = '.format(num_1, num_2))
        print(num_1  - num_2)
    # multiplication operations
    elif operation == '*':
        print('{} * {} = '.format(num_1, num_2))
        print(num_1 * num_2)
    
    # division operations
    elif operation == '/':
        print('{} / {} = '.format(num_1, num_2))
        print(num_1 / num_2)

    else:
        print('You have not entered any operator!') 

# Define another function for the user to perform a calculation again
def calc_again():

    calc_again = input('''If you want to calculate again type Y for Yes
    and N for No''')

    # check for the validity
    if calc_again.upper() == 'Y':
        Calculator()
    elif calc_again.Upper() == 'N':
        print('Thanks for using the calculator')
    else:
        calc_again()

#Calling the Function
welcome()
Calculator()