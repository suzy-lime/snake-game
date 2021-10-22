from turtle import Turtle, Screen

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# CREATE SNAKE SEGMENTS
class Snake:
    def __init__(self):
        self.segments = []
        self.screen = Screen()
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[len(self.segments)-1]

    def create_snake(self):
        for x in range(0, 3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(x=int((0 + -(20 * x))), y=0)
            self.segments.append(segment)
        self.screen.update()

    def add_segment(self):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(self.tail.position())
        self.segments.append(segment)

    def restart(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[len(self.segments) - 1]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            this_segment = self.segments[seg_num - 1]
            x = this_segment.xcor()
            y = this_segment.ycor()
            self.segments[seg_num].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
