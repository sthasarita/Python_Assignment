import calculator
import geometry

while True:
    print("1.Calculator")
    print("2.Geometry")
    print("3.Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        a = int(input("Enter first number:"))
        b = int(input("Enter second number:"))
        print(f"Addition = {calculator.add(a,b)} \n Subtraction = {calculator.subtract(a,b)} \n Multiplication = {calculator.multiply(a,b)} \n Division = {calculator.divide(a,b)}")
    elif choice == 2:
        length = int(input("Enter the length of the rectangle:"))
        breadth = int(input("Enter the breadth of the rectangle:"))
        print("The area of the rectangle = ", geometry.area_rectangle(length, breadth))
        r = int(input("Enter the radius of the circle:"))
        print("The area of circle = ", geometry.area_circle(r))
    else:
        print("Exiting...")
        break
    
