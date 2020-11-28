from ball import Ball

width = 600
height = 600
RADIUS_ = 10
STEP = 10

def setup():
    size(width, height)
    global balls
    balls = [Ball(300, 300, RADIUS_)]
    
    
def draw():
    background(155)
    for i in range(len(balls)):
        balls[i].display()
    
    
def mousePressed():
    if mouseButton == LEFT: balls[(len(balls) - 1)].changeColor()
    
def keyPressed():
    if keyCode == UP: balls[(len(balls) - 1)].MoveUp(STEP)
    if keyCode == DOWN: balls[(len(balls) - 1)].MoveDown(STEP)
    if keyCode == LEFT: balls[(len(balls) - 1)].MoveLeft(STEP)
    if keyCode == RIGHT: balls[(len(balls) - 1)].MoveRight(STEP)
    if keyCode == 32: balls.append(Ball(random(width), random(height), RADIUS_))
