import random

class Ball(object):
    
    def __init__(self):
        self.radius = 20
        self.position = self.StartPosition()
        self.velocity = self.StartVelocity()
        self.bcolor = color(33, 53, 237, 50)
        self.number = random.randrange(0, 21)
        self.dead = False
        self.start = True
        self.img_deadball = loadImage("deadball.png")    

    def StartVelocity(self):
        return PVector(random.uniform(width/2 - width/4, width/2 + width/4) - self.position.x, 
                   random.uniform(height/2 - height/4, height/2 + height/4) - self.position.y).div(1000)

    def StartPosition(self):
        if random.randrange(0, 2) == 0:
            return PVector(random.randrange(-self.radius, width + 1 + self.radius, width + 2 * self.radius), 
                        random.randrange(-self.radius, height + 1 + self.radius))
        else:
            return PVector(random.randrange(-self.radius, width + 1 + self.radius), 
                        random.randrange(-self.radius, height + 1 + self.radius, height + 2 * self.radius))

    def Display(self):
        if self.dead == False:
            if self.start == False: stroke(255, 255, 255)
            else: stroke(255, 255, 255, 50)
            strokeWeight(2)
            fill(self.bcolor)
            circle(self.position.x, self.position.y, self.radius * 2 - 2)
            fill(255)
            textSize(20)
            textAlign(CENTER, CENTER)
            text(self.number, self.position.x, self.position.y - 3)
        else:
            imageMode(CENTER)
            image(self.img_deadball, self.position.x, self.position.y, self.radius * 2, self.radius * 2)
    
    def Move(self):
        if self.start == True and frameCount % 30 == 0:
            self.velocity.add(self.StartVelocity())
        self.position.add(self.velocity)
        
    def Position(self, x, y):
        self.position = PVector(x, y)
    
    def CheckWall(self):
        if self.start == False:
            if self.position.x > width - self.radius:
                self.position.x = width - self.radius
                self.velocity.x *= -1
            
            elif self.position.x < self.radius:
                self.position.x = self.radius
                self.velocity.x *= -1
            
            if self.position.y > height - self.radius:
                self.position.y = height - self.radius
                self.velocity.y *= -1
            
            elif self.position.y < self.radius:
                self.position.y = self.radius
                self.velocity.y *= -1
        elif self.position.x - self.radius > 0 and self.position.x + self.radius < width and self.position.y - self.radius > 0 and self.position.y + self.radius < height:
                self.start = False
        
            
class Player_Ball(Ball):
    Damping = 0.995
    
    def __init__(self, x, y, radius):
        self.position = PVector(x, y)
        self.velocity = PVector(0, 0)
        self.radius = radius
        self.bcolor = color(237, 33, 35)
        self.start = False
        self.img_playerball = loadImage("playerball.png")
        
    def Display(self):
        imageMode(CENTER)
        image(self.img_playerball, self.position.x, self.position.y, self.radius * 2, self.radius * 2)
        
    def Move(self):
        self.velocity.mult(Player_Ball.Damping)
        self.position.add(self.velocity)
