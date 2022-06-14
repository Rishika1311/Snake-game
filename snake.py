import turtle as t
x_pos = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()

    def create_snake(self):
        for i in x_pos:
            self.add_segment(i)

    def add_segment(self, pos):
        tim = t.Turtle()
        tim.color("white")
        tim.shape("square")
        tim.penup()
        tim.goto(pos)
        self.squares.append(tim)

    def extend(self):
        self.add_segment(self.squares[-1].position())

    def move(self):
        for seg in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[seg - 1].xcor()
            new_y = self.squares[seg - 1].ycor()
            self.squares[seg].goto(new_x, new_y)
        self.squares[0].forward(20)

    def up(self):
        if self.squares[0].heading() != 270:
            self.squares[0].setheading(90)

    def down(self):
        if self.squares[0].heading() != 90:
            self.squares[0].setheading(270)

    def right(self):
        if self.squares[0].heading() != 180:
            self.squares[0].setheading(0)

    def left(self):
        if self.squares[0].heading() != 0:
            self.squares[0].setheading(180)
