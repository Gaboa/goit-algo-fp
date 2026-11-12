import sys
import turtle


def draw_pythagoras_tree(pen, size, rec_level, branch_angle=45, shrink_factor=0.75):
    if rec_level < 0:
        raise ValueError("The recursion level must be zero or greater.")

    start = pen.position()
    heading = pen.heading()
    pen.forward(size)

    if rec_level > 0:
        pen.left(branch_angle)
        draw_pythagoras_tree(
            pen,
            size * shrink_factor,
            rec_level - 1,
            branch_angle,
            shrink_factor,
        )
        pen.setheading(heading - branch_angle)
        draw_pythagoras_tree(
            pen,
            size * shrink_factor,
            rec_level - 1,
            branch_angle,
            shrink_factor,
        )

    pen.penup()
    pen.goto(start)
    pen.setheading(heading)
    pen.pendown()


def draw_pythagoras_tree_window(rec_level, size=200):
    if rec_level < 0:
        raise ValueError("The recursion level must be zero or greater.")

    window = turtle.Screen()
    window.setup(width=1000, height=800)
    window.title(f"Pythagoras tree, recursion level {rec_level}")

    pen = turtle.Turtle()
    pen.speed(0)
    pen.pensize(2)
    pen.color("#b22121")
    pen.penup()
    pen.goto(0, -350)
    pen.setheading(90)
    pen.pendown()

    draw_pythagoras_tree(pen, size, rec_level)

    pen.hideturtle()
    window.update()
    window.mainloop()


def main():
    args = sys.argv[1:]
    if not args:
        rec_level = 7
    else:
        rec_level = int(args[0])

    draw_pythagoras_tree_window(rec_level)


if __name__ == "__main__":
    main()