# In this calculator app, I'm building a calculator app using Class concepts instead of functions

# Welcome Message
class Welcome:

    def welcome():
        print('''Welcome to this calculator app. Have Fun performing your Calculations''')


# Define the Calculator class
class Calculator:

    # User information
    operator = input('''Enter the operator as
        + for Addition
        - for subtraction
        * for multiplication
        / for division''')

    #Request for user input
    num_1 = int(input('Enter the first Number: '))
    num_1 = int(input('Enter the first Number: '))

    # Assign the data locations
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2


    # Create the calculations
    def operations(self):
         
        if operator == '+':
            print('{} + {} = '.format(self.num_1, self.num_2 ))
            print(self.num_1 + self.num_2)
        elif operator == '-':
            print('{} - {} = '.format(self.num_1, self.num_2))
            print(self.num_1 - self.num_2)
        elif operator == '*':
            print('{} * {} = '.format(self.num_1, self.num_2))
            print(self.num_1 * self.num_2)
        elif operator == '/':
            print('{} / {} = '.format(self.num_1, self.num_2))
            print(self.num_1 / self.num_2)
        else:
            print('Your Operator is not Defined!')

class calc_again:
    def calc_again():
        calc_again = input('''Type Y for Yes
        or N for No''')

        # to check for the user input
        if calc_again. Upper() == 'Y':
            Calculator()
        elif calc_again.Upper() == 'N':
            print('Thanks for using the Calculator')
        else:
            calc_again()


# Drivers code
calc = Calculator()

