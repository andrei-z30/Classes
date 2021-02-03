class Ball(object):
    Gravity = PVector(0, 0.3)
    Damping = 0.8
    
    def __init__(self, x, y, radius):
        self.position = PVector(x, y)
        self.velocity = PVector(0, 0)
        self.radius = radius
        self.bcolor = color(random(255), random(255), random(255))

    def display(self):
        noStroke()
        fill(self.bcolor)
        circle(self.position.x, self.position.y, self.radius * 2)
    
    def changeColor(self):
        self.bcolor = color(random(255), random(255), random(255))
    
    def move(self):
        self.velocity.add(Ball.Gravity)
        self.position.add(self.velocity)
        
    def MoveUp(self, step):
        self.position.y -= step
        
    def MoveDown(self, step):
        self.position.y += step
        
    def MoveLeft(self, step):
        self.position.x -= step
        
    def MoveRight(self, step):
        self.position.x += step
        
    def position(self, x, y):
        self.position = PVector(x, y)
    
    def checkWall(self):
        if self.position.x > width - self.radius:
            self.position.x = width - self.radius
            self.velocity.x *= -Ball.Damping
        
        elif self.position.x < self.radius:
             self.position.x = self.radius
             self.velocity.x *= -Ball.Damping
        
    def checkGround(self):
        if self.position.y > height - self.radius:
            self.position.y = height - self.radius
            self.velocity.y *= -Ball.Damping
