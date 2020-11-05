width = 800
height = 800
nx = 6
ny = 6
l = 60
var = 1 #0 - линия, 1 - квадрат, 2 - круг

def setup():
    size(width, height)
    stroke(255)
    noFill()
    frameRate(30)
    
def draw():
    background(0)
    for i in range(ny):
        for k in range(nx):
            x = ((k+1)*width/nx)-((width/nx)/2)
            y = ((i+1)*height/ny)-((height/ny)/2)
            if var == 0:
                line(x, y-(l/2), x, y+(l/2)) 
            if var == 1:
                rect(x-l/2, y-l/2, l, l)
            if var == 2:
                ellipse(x, y, l, l)
