width = 800
height = 800
nx = 6
ny = 6
len = 60
type_forms = 0 #0 - линия, 1 - квадрат, 2 - круг

def setup():
    size(width, height)
    stroke(255)
    noFill()
    frameRate(1)
    
def draw():
    global type_forms
    background(0)
    for i in range(ny):
        for k in range(nx):
            x = ((k+1)*width/nx)-((width/nx)/2)
            y = ((i+1)*height/ny)-((height/ny)/2)
            if type_forms == 0:
                line(x, y-(len/2), x, y+(len/2)) 
            if type_forms == 1:
                rect(x-len/2, y-len/2, len, len)
            if type_forms == 2:
                ellipse(x, y, len, len)
    type_forms = (type_forms + 1) % 3
