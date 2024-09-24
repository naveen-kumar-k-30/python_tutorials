import turtle
import winsound
s = 0
win = turtle.Screen()
win.setup(width=500, height=500)
win.title("Up and Down")
win.bgcolor("red")
win.tracer(0)

# bottom_paddle
bottom_bar = turtle.Turtle()
bottom_bar.shape("square")
bottom_bar.shapesize(stretch_wid=1, stretch_len=5)
bottom_bar.penup()
bottom_bar.speed(0)
bottom_bar.goto(0, -230)

# ball
ball = turtle.Turtle()
ball.shape("circle")
ball.penup()
ball.speed(0)
ball.goto(0, 230)
ball.bx = .05
ball.by = .05

# Score display background
bg_pen = turtle.Turtle()
bg_pen.hideturtle()
bg_pen.speed(0)
bg_pen.penup()
bg_pen.goto(-60, 225)  # Adjust starting position for the background
bg_pen.color("black")  # Set the background color (e.g., black)
bg_pen.begin_fill()
for _ in range(2):
    bg_pen.forward(120)  # Width of the rectangle
    bg_pen.right(90)
    bg_pen.forward(30)  # Height of the rectangle
    bg_pen.right(90)
bg_pen.end_fill()

# written
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.goto(0, 194)
pen.write(f"score {s}", align="center", font=("Ariel", 24, "normal"))


def bar_l():
    bottom_bar.setx(bottom_bar.xcor() - 20)


def bar_r():
    bottom_bar.setx(bottom_bar.xcor() + 20)


win.listen()
win.onkeypress(bar_l, 'Left')
win.onkeypress(bar_r, 'Right')
while True:
    win.update()
    ball.sety(ball.ycor() - ball.by)
    ball.setx(ball.xcor() + ball.bx)
    if ball.xcor() > 240:
        ball.setx(240)
        ball.bx *= -1
    if ball.xcor() < -240:
        ball.setx(-240)
        ball.bx *= -1
    if ball.ycor() > 230:
        ball.sety(230)
        ball.by *= -1
    if ball.ycor() < -240:
        ball.sety(230)
        s = 0
        pen.clear()
        pen.write(f"score {s}", align="center", font=("Ariel", 24, "normal"))

    if ball.ycor() < -220 and bottom_bar.xcor() - 50 < ball.xcor() < bottom_bar.xcor() + 50:
        ball.sety(-220)
        ball.by *= -1
        s += 1
        pen.clear()
        winsound.PlaySound("Pong_bounce.wav", winsound.SND_ASYNC)
        pen.write(f"score {s}", align="center", font=("Ariel", 24, "normal"))
    if s == 3:
        pen.clear()
        pen.write("you won", align="center", font=("Ariel", 24, "normal"))
