import math 

def calculate_distance(x1, y1, x2, y2): 
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
print("Calculate the Distance between two points")
print("Enter the coordinates for the first point:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
print("\nEnter the coordinates for the second point:")
x2 = float(input("x2: "))
y2 = float(input("y2: ")) 

# Calculate and display the result
result = calculate_distance(x1, y1, x2, y2)
print("The distance between the points is:", result)