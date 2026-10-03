from turtle import *
screen = getscreen()
def create_ball(x, y,h, cl):
    ball = Turtle()
    ball.x = x
    ball.y = y
    ball.count = 0
    ball.shape("circle")
    ball.speed(0)
    ball.color(cl)
    ball.penup()
    ball.goto(x, y)
    ball.pendown()
    ball.setheading(h)
    return ball
b1 = create_ball(-120,-120,0,"red")
b2 = create_ball(120,-140,90,"yellow")
b3 = create_ball(140,120,180,"blue")
b4 = create_ball(-100,140,270,"green")
balls = [b1, b2, b3, b4]
def move_balls():
    for b in balls:
        b.fd(10)
        if b.count >26:
            b.goto(b.x,b.y)
            b.count = 0
        b.count += 1
    screen.ontimer(move_balls, 100)
move_balls()
done()