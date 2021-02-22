def interface():
    print("Welcome! This program can be used to calculate the y value of a point on a line.")
    print("In order to do so, the x value of that point, and the x and y values of two others, must be entered.")
    
def get_input():
    x1 = input("Please enter the x value of the first point on the line: ")
    y1 = input("Please enter the y value of the first point on the line: ")
    x2 = input("Please enter the x value of the second point on the line: ")
    y2 = input("Please enter the y value of the second point on the line: ")
    return x1, y1, x2, y2


def convert_input(x1, y1, x2, y2):
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    point_1 = (x1, y1)
    point_2 = (x2, y2)


def calc_m(x1, y1, x2, y2):
    m = (y2 - y1)/(x2 - x1)
    return m


def calc_y_int(x1,y1,m):
    b = y1 - (m*x1)
    return b


def calc_y(point_1,point_2,x):
    m = calc_m(point_1[0], point_1[1], point_2[0], point_2[1])
    b = calc_y_int(point_1[0], point_1[1],m)
    y = (m*x_of_point_3) + b
    return y


def driver():
    interface()
    (x1, y1, x2, y2) = get_input()

if __name__ == "__main__":
    driver()
