width = 800
height = 600
size_circle = 60
y = height-size_circle/2
x = width/2 - 100
speed_x = 20
accel_x = -1
speed_y = -16
accel_y = -1
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
    if y + speed_y <= height-size_circle/2: y += speed_y
    else: 
        y = height-size_circle/2
        if speed_x > 0: speed_x += accel_x
    
    if y == height-size_circle/2: 
        speed_y = -speed_y
        if speed_y < 0: speed_y -= accel_y
    if x >= width-size_circle/2 or x <= size_circle/2: 
        napr = not(napr)
        if speed_x > 0: speed_x += accel_x
    
    if napr == True: 
        if x + speed_x < width: x += speed_x 
        else: x = width-size_circle/2
    else: 
        if x - speed_x > size_circle/2: x -= speed_x 
        else: x = size_circle/2
    
    circle(x, y, size_circle)
