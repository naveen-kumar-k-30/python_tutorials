import turtle
import winsound
score_a = 0
score_b = 0
# Create a Screen object
win = turtle.Screen()

# Set the size and background color of the window
win.setup(width=800, height=600)
win.bgcolor("blue")

# Set the title of the window
win.title("Pong Game")
win.tracer(0)  # to neglect the trase
# left paddle
left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()  # neglect marking line
left_paddle.speed(0)  # neglect animation
left_paddle.goto(-380, 0)

# right paddle
right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()  # neglect marking line
right_paddle.speed(0)  # neglect animation
right_paddle.goto(380, 0)

# ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.speed(0)
ball.penup()
ball.dx = .125
ball.dy = .125

#score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.write("Player A: 0 Player B: 0",align="center",font=("Ariel",24,"normal"))

# moving paddles:
def left_paddle_up():
    left_paddle.sety(left_paddle.ycor() + 20)


def left_paddle_down():
    left_paddle.sety(left_paddle.ycor() - 20)


def right_paddle_up():
    right_paddle.sety(right_paddle.ycor() + 20)


def right_paddle_down():
    right_paddle.sety(right_paddle.ycor() - 20)


win.listen()
win.onkeypress(left_paddle_up, 'w')
win.onkeypress(left_paddle_down, 'z')

win.onkeypress(right_paddle_up, 'Up')
win.onkeypress(right_paddle_down, 'Down')

# Main game loop
while True:
    win.update()
    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # ball collision
    # top wall
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    # bottom Wall
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    # right wall
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Ariel", 24, "normal"))

    # left wall
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Ariel", 24, "normal"))

    # collision with paddle
    if ball.xcor() > 370 and right_paddle.ycor()-50 < ball.ycor() < right_paddle.ycor() + 50:
        ball.setx(360)
        ball.dx *= -1
    if ball.xcor() < -370 and left_paddle.ycor()-50< ball.ycor() < left_paddle.ycor() + 50:
        ball.setx(-360)
        ball.dx *= -1
