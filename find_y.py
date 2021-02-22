def interface():
    print("Welcome! This program can be used to calculate the y value of a point on a line.")
    print("In order to do so, the x value of that point, and the x and y values of two others, must be entered.")
    
def get_input():
    x1 = input("Please enter the x value of the first point on the line: ")
    y1 = input("Please enter the y value of the first point on the line: ")
    x2 = input("Please enter the x value of the second point on the line: ")
    y2 = input("Please enter the y value of the second point on the line: ")
    return x1, y1, x2, y2

def driver():
    interface()
    (x1, y1, x2, y2) = get_input()