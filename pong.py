#PONG game
#Author == Brendan Li
#Date == November 1st, 2021
#Easy program; no OOP


import turtle #good package for getting started with games
import random

#create a window for our game
win = turtle.Screen()
win.title("Pong by B-Li")
win.bgcolor("black")
win.setup(width=800, height=600) #numbers are in pixels
win.tracer(0) #stops window from updating; manually update window, which speeds our game up

#PADDLE ONE
paddle1 = turtle.Turtle()
paddle1.speed(0) #this is speed of animation; max speed set
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup() #doesn't draw line when in motion
paddle1.goto(-350, 0) #location of ball on screen


#PADDLE TWO
paddle2 = turtle.Turtle()
paddle2.speed(0) #this is speed of animation; max speed set
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup() #doesn't draw line when in motion
paddle2.goto(350, 0) #location of ball on screen


#pong ball
ball = turtle.Turtle()
ball.speed(0) #this is speed of animation; max speed set
ball.shape("square")
ball.color("white")
ball.penup() #doesn't draw line when in motion
ball.goto(0, 0) #location of ball on screen
#y and x movement of ball
ball.dx = 0.3 #speed kinda depends on hardware
ball.dy = 0.25



#SCORE BOARDDDDDD
score1 = 0
score2 = 0
#pen, from turtle package
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 265)
pen.write("Left Player: {}   Right Player: {}".format(score1, score2), align = "center", font=("Courier", 24, "normal"))



#FUNCTIONS FOR PADDLE 1 MOVEMENT
#function to move paddle up
def paddle1_up():
    y = paddle1.ycor() #returns y cordinate
    y += 20
    paddle1.sety(y)
#function to move paddle down
def paddle1_down():
    y = paddle1.ycor() #returns y cordinate
    y -= 20
    paddle1.sety(y)
#KEYBOARD BINDING
win.listen()
win.onkeypress(paddle1_down, "s")
win.listen()
win.onkeypress(paddle1_up, "w")
#FUNCTIONS FOR PADDLE 2 MOVEMENT
#function to move paddle up
def paddle2_up():
    y = paddle2.ycor() #returns y cordinate
    y += 20
    paddle2.sety(y)
#function to move paddle down
def paddle2_down():
    y = paddle2.ycor() #returns y cordinate
    y -= 20
    paddle2.sety(y)
#KEYBOARD BINDING
win.listen()
win.onkeypress(paddle2_down, "Down")
win.listen()
win.onkeypress(paddle2_up, "Up")




#MAIN GAME LOOP; IMPORTANT WHEN MAKING GAMES
while True:
    win.update() #evertime loop runs, update window

    #Let's move dis ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #BORDER CHECKING
    #paddle 1 check
    if paddle1.ycor()>290:
        paddle1.goto(-350, 290)
    if paddle1.ycor()<-290:
        paddle1.goto(-350, -290)
    #paddle 2 check
    if paddle2.ycor()>290:
        paddle2.goto(350, 290)
    if paddle2.ycor()<-290:
        paddle2.goto(350, -290)
    
    #BORDER CHECK FOR BALLLLLL
    #top and bottom check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    #left and right borders
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy = random.uniform(-0.2, 0.2)
        score1+=1
        pen.clear()
        pen.write("Left Player: {}   Right Player: {}".format(score1, score2), align = "center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy = random.uniform(-0.2, 0.2)
        score2+=1
        pen.clear()
        pen.write("Left Player: {}   Right Player: {}".format(score1, score2), align = "center", font=("Courier", 24, "normal"))


    #PADDLE BOUNCES
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < (paddle2.ycor() + 40) and ball.ycor() > (paddle2.ycor() - 40)):
        ball.dy = random.uniform(-0.2, 0.2)
        ball.dx *= -1
        ball.setx(340)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < (paddle1.ycor() + 40) and ball.ycor() > (paddle1.ycor() - 40)):
        ball.dy = random.uniform(-0.2, 0.2)
        ball.dx *= -1
        ball.setx(-340)