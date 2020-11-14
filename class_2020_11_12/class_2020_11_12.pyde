width = 600
height = 600
nx = 6
ny = 6
len = 60
type_forms = 0 #0 - линия, 1 - квадрат, 2 - круг

fill_R_start, fill_G_start, fill_B_start = 108, 255, 50 #Начальный цвет заливки в RGB
fill_R_end, fill_G_end, fill_B_end = 209, 31, 192 #Конечный цвет заливки в RGB

stroke_R_start, stroke_G_start, stroke_B_start = 209, 31, 192 #Начальный цвет контура в RGB
stroke_R_end, stroke_G_end, stroke_B_end = 108, 255, 50 #Конечный цвет контура в RGB

def setup():
    size(width, height)
    frameRate(1)
    
def draw():
    background(155)
    for i in range(1, ny + 1):
        for k in range(1, nx + 1):
            x = (k*width/nx)-((width/nx)/2)
            y = (i*height/ny)-((height/ny)/2)
            draw_form(x, y, i, k)
    global type_forms
    type_forms = (type_forms + 1) % 3 
                    
def draw_form(x, y, i, k):
    fill(calc_color(i, k, fill_R_start, fill_R_end), 
         calc_color(i, k, fill_G_start, fill_G_end), 
         calc_color(i, k, fill_B_start, fill_B_end))
    stroke(calc_color(i, k, stroke_R_start, stroke_R_end),
           calc_color(i, k, stroke_G_start, stroke_G_end),
           calc_color(i, k, stroke_B_start, stroke_B_end))
    if type_forms == 0:
        line(x, y-(len/2), x, y+(len/2)) 
    if type_forms == 1:
        rect(x-len/2, y-len/2, len, len)
    if type_forms == 2:
        ellipse(x, y, len, len)

def calc_color(i, k, start_color, end_color):
    return start_color+((end_color-start_color)/(nx*ny))*(((i-1)*6)+k)
