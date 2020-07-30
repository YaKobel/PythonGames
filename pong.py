import turtle

win = turtle.Screen()
win.title("My paint")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# racket
racket_a = turtle.Turtle()
racket_a.speed(0)
racket_a.shape("square")
racket_a.color("blue")
racket_a.shapesize(stretch_len=1, stretch_wid=5)
racket_a.penup()
racket_a.goto(-350,0)


while True:
    win.update()