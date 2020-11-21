width = 800
height = 600
size_circle = 60
y = height-size_circle/2
x = width/2 - 100
speed_x = 20
speed_y = -16
accel_g = 10
napr = True #True - враво False - влево

def setup():
    size(width, height)
    frameRate(30)
    fill(255)
    
def draw():
    background(155)
    global x, y, napr, speed_x, speed_y
    speed_y = speed_y + (accel_g/frameRate)
    
    
    if y + speed_y <= height-size_circle/2: y += speed_y
    else: 
        y = height-size_circle/2
        accel_x = random(2)
        if speed_x > 0 and speed_x - accel_x > 0: speed_x -= accel_x
        elif speed_x < 0 and speed_x + accel_x < 0: speed_x += accel_x
        else: speed_x = 0
    
    if y == height-size_circle/2 and speed_y > 0: 
        speed_y = -speed_y
        accel_y = random(2)
        if -speed_y > accel_y: speed_y += accel_y
        else: speed_y = 0
    if x >= width-size_circle/2 or x <= size_circle/2: 
        napr = not(napr)
        accel_x = random(2)
        if speed_x > 0: speed_x -= accel_x
        else: speed_x += accel_x
    
    if napr == True: 
        if x + speed_x < width-size_circle/2: x += speed_x 
        else: x = width-size_circle/2
    else: 
        if x - speed_x > size_circle/2: x -= speed_x 
        else: x = size_circle/2
    
    circle(x, y, size_circle)
