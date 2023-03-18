# In this code, I will be using the class function to create a circular arithimetic calculator

class Circle:

    # Define the inputs
    def __init__(self):
        self.radius = float(input('Enter the radius: '))
        self.pi = float(input('Enter the PI parameter: '))

    # Calculate circumference
    def get_perimeter(self):
        perimeter = self.pi * (self.radius * 2)
        print('The perimeter is ', perimeter)

    # calculate the area
    def get_area(self):
        area = self.pi * self.radius * self.radius
        print('The area is ', area)

# Call the calculator
circle = Circle()
