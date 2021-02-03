H = 512
V = 512
Width = 200
Height = 200

def setup():
    size(H, V)
    noLoop()
    background(0, 0, 0)
    fill(255, 0, 0)
    rect(H/2-Width/2, (V/2)-Height/2, Width, Height)
