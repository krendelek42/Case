# Case-study #1
# Developers:   Dokukina K. (%),
#               Nazirova E. (%),
#               Shevchenko V. (%)
import turtle


def square(x, y, a):
    '''
    Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a square
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.pensize(2)
    turtle.pencolor('white')
    turtle.fillcolor('#ff7c00')
    turtle.speed(100)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()


def parallelogram(x, y, a, c):
    '''
    Function, drawing parallelogram.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: long side of a parallelogram
    :param c: short side of a parallelogram
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.pensize(2)
    turtle.pencolor('white')
    turtle.fillcolor('#8ecc23')
    turtle.speed(100)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(c)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(c)
    turtle.end_fill()


def triangle(x, y, a, b, c):
    '''
    Function, drawing triangle.
    :param x: right angle coordinate x
    :param y: right angle coordinate y
    :param a: leg of a triangle
    :param b: hypotenuse of triangle
    :param c: color of triangle
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.pensize(2)
    turtle.pencolor('white')
    turtle.fillcolor(c)
    turtle.speed(100)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(135)
    turtle.end_fill()
    turtle.forward(a)


def main():
    '''
    Main function.
    :return: None
    '''
    square(-300, 300, 35)
    turtle.right(45)
    square(0, 270, 35)
    turtle.right(45)
    square(300, 300, 35)
    turtle.right(45)
    square(-270, 40, 35)
    square(100, 0, 85)
    square(300, 40, 35)
    square(-180, -240, 35)
    square(-50, -240, 35)
    square(250, -290, 35)
    turtle.right(45)
    triangle(-300, 210, 70, 9800**0.5, '#f72a49')
    triangle(25, 315, 70, 9800**0.5, '#f72a49')
    turtle.right(90)
    triangle(230, 300, 70, 9800**0.5, '#f72a49')
    triangle(-310, 15, 70, 9800**0.5, '#f72a49')
    turtle.left(45)
    triangle(-20, 0, 175, 61250**0.5, '#f72a49')
    turtle.left(45)
    triangle(275, 15, 70, 9800**0.5, '#f72a49')
    turtle.right(135)
    triangle(-205, -215, 70, 9800**0.5, '#f72a49')
    turtle.right(90)
    triangle(100, -240, 70, 9800**0.5, '#f72a49')
    turtle.left(90)
    triangle(225, -265, 70, 9800**0.5, '#f72a49')
    parallelogram(-320, 300, 50, 35)
    turtle.right(45)
    parallelogram(-60, 245, 50, 35)
    turtle.right(90)
    parallelogram(160, 250, 50, 35)
    turtle.right(90)
    parallelogram(-345, -20, 50, 35)
    turtle.left(90)
    parallelogram(-20, -120, 125, 85)
    parallelogram(275, -85, 50, 35)
    turtle.left(45)
    parallelogram(-280, -265, 50, 35)
    parallelogram(75, -169, 50, 35)
    turtle.left(45)
    parallelogram(274, -310, 50, 35)

#Vera Shevchenko
    turtle.left(-135)
    triangle(-370, 210, 70, 9800 ** 0.5, '#fcde15')
    turtle.left(-225)
    triangle(-20, 0, 175, 61250 ** 0.5, '#fcde15')
    turtle.left(225)
    triangle(25, 180, 70, 9800 ** 0.5, '#fcde15')
    turtle.left(90)
    triangle(230, 265, 70, 9800 ** 0.5, '#fcde15')
    turtle.left(-270)
    triangle(-280, -95, 70, 9800 ** 0.5, '#fcde15')
    turtle.left(-270)
    triangle(275, 15, 70, 9800 ** 0.5, '#fcde15')
    turtle.left(-270)
    triangle(-255, -255, 70, 9800 ** 0.5, '#fcde15')
    turtle.left(135)
    triangle(1, -240, 70, 9800 ** 0.5, '#fcde15')
    turtle.left(90)
    triangle(272, -218, 70, 9800 ** 0.5, '#fcde15')
    turtle.done()


if __name__ == '__main__':
    main()

