# Write a function that takes length and width as parameters and returns the area of a rectangle.

def rectangle_area(length, width):
    area = length * width
    return area

# Example usage:
length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = rectangle_area(length, width)
print(f"The area of the rectangle is: {area}")