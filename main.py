# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')


import math
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y



def multiply(x, y):
    return x * y



def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed"
    return x /y
def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)


def calculate_rectangle_area(length, width):
    return length * width



def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Sum")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Division")
        print("5. Calculate Triangle Area")
        print("6. Calculate Circle Area")
        print("7. Calculate Rectangle Area")
        print("8. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

        if choice == '8':
            print("Exiting the program. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result: ", add(num1, num2))
            elif choice == '2':
                print("Result: ", subtract(num1, num2))
            elif choice == '3':
                print("Result: ", multiply(num1, num2))
            elif choice == '4':
                print("Result: ", divide(num1, num2))
        elif choice == '5':
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            print("Triangle Area: ", calculate_triangle_area(base, height))
        elif choice == '6':
            radius = float(input("Enter the radius of the circle: "))
            print("Circle Area: ", calculate_circle_area(radius))
        elif choice == '7':
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            print("Rectangle Area: ", calculate_rectangle_area(length, width))
        else:
            print("Invalid input. Please choose a valid option (1/2/3/4/5/6/7/8).")


if __name__ == "__main__":
    main_menu()