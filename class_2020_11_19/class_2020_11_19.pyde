width = 600
height = 600
size_circle = 60
y = height
x = width/2 - 100
speed_x = 20
speed_y = -16
g = 10
napr = True

def setup():
    size(width, height)
    frameRate(30)
    fill(255)
    
def draw():
    background(155)
    global x, y, napr, speed_x, speed_y
    speed_y = speed_y + (g/frameRate)
    y += speed_y
    if y > height: speed_y = -speed_y
    if x > width or x < 0: napr = not(napr)
    if napr == True: 
        x = x + speed_x
    else: x = x - speed_x
    circle(x, y, size_circle)
