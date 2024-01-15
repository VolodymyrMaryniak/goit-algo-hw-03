import turtle
import argparse

def parse_argv() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Draw Koch snowflake')
    parser.add_argument('-l', '--level', type=int, required=False, default=3, help='Recursion level')
    args = parser.parse_args()
    return args

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    koch_curve(t, order, size)

    window.mainloop()

def draw_koch_figure(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

def main():
    args = parse_argv()
    draw_koch_figure(args.level)

if __name__ == '__main__':
    main()