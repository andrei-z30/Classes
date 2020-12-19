import random
from ball import Ball
from ball import Player_Ball

width = 1200
height = 700
PLAYER_RADIUS = 20
STEP = 10
score = 0
game_over = False

def setup():
    size(width, height)
    frameRate(30)
    LoadImage()
    NewGame()
    
def draw():
    imageMode(CORNER)
    image(img_background, 0, 0, width, height)
    DrawText()
    if mousePressed: Player_Pull()
    GoBalls()
    
def LoadImage():
    global img_krest
    img_krest = loadImage("krest.png")
    global img_background
    img_background = loadImage("Background.jpg")
    global img_pointer
    img_pointer = loadImage("pointer.png")
     
def GoBalls():
    for i in range(len(balls)):
        balls[i].Move()
        balls[i].CheckWall()
        CheckCollision(i)
        if game_over == False: balls[i].Display()
    
def DrawText():
    textSize(32)
    textAlign(LEFT, CENTER)
    fill(255)
    text("Score: " + str(score), 20, 20)
    if game_over == False:
        textAlign(CENTER, CENTER)
        text(str(num_A) + str(znak) + str(num_B), width/2, 20)
    
def CheckCollision(k):
    for i in range(len(balls)):
        if i != k:
            min_dist = balls[k].radius + balls[i].radius
            bVect = PVector.sub(balls[i].position, balls[k].position)
            if  bVect.mag() < min_dist:
                angleA = PVector.angleBetween(balls[k].velocity, bVect)
                angleB = PVector.angleBetween(balls[i].velocity, PVector.mult(bVect, -1))
                bVect.setMag(min_dist)
                balls[k].position = PVector.sub(balls[i].position, bVect)
                
                vectA = bVect
                vectA.setMag(balls[k].velocity.mag() * cos(angleA))
                vectB = PVector.mult(bVect, -1)
                vectB.setMag(balls[i].velocity.mag() * cos(angleB))
                
                balls[k].velocity.add(vectB)
                balls[k].velocity.sub(vectA)
                
                balls[i].velocity.add(vectA)
                balls[i].velocity.sub(vectB)
                
                if k == 0: PlayerCollision(i) 
                elif i == 0: PlayerCollision(k)
                if game_over == True: break
                
def PlayerCollision(i):
    if balls[i].number == num_result:
        global score
        score += 1
        DestroyBalls()
        UpdateNumber()
        GenerateNewBalls(10)
    else:
        balls[0].radius += 10
        balls[i].position.add(PVector.sub(balls[i].position, balls[0].position).setMag(10))
        balls[i].dead = True
        if balls[0].radius > 200: GameOver()
    balls[0].velocity.div(10)
                               
def Player_Pull():
    imageMode(CENTER)
    image(img_krest, mouseX, mouseY, 20, 20)
    stroke(255)
    strokeWeight(1)
    global pointer
    pointer = PVector(balls[0].position.x - mouseX, balls[0].position.y - mouseY)
    if pointer.mag() > 200: pointer.setMag(200)
    
    translate(balls[0].position.x + pointer.x, balls[0].position.y + pointer.y)
    rotate(pointer.heading())
    image(img_pointer, 0, 0, 30, 30)
    rotate(-pointer.heading())
    translate(-(balls[0].position.x + pointer.x), -(balls[0].position.y + pointer.y))
    
def mousePressed():
    for i in range(len(balls)):
        balls[i].velocity.div(10)

def mouseReleased():
    for i in range(len(balls)):
        balls[i].velocity.mult(10)
    balls[0].velocity.add(pointer.div(10))
    
def UpdateNumber():
    global num_result, num_A, num_B, znak
    num_result = random.randrange(1, 21)
    num_A = random.randrange(1, 21)
    znak = random.randrange(4)
    if znak == 0:
        znak = " + "
        num_A = random.randrange(1, num_result + 1)
        num_B = num_result - num_A
    elif znak == 1:
        znak = " - "
        num_A = random.randrange(num_result, 21)
        num_B = num_A - num_result
    elif znak == 2:
        znak = " * "
        while num_result % num_A != 0: num_A = random.randrange(1, num_result + 1)
        num_B = num_result / num_A
    elif znak == 3:
        znak = " / "
        while num_A % num_result: num_A = random.randrange(num_result, 21)
        num_B = num_A / num_result
        
def GameOver():
    global game_over
    game_over = True
    noLoop()
    imageMode(CORNER)
    image(img_background, 0, 0, width, height)
    balls[0].position = PVector(width/2, height/2)
    balls[0].radius = height/2
    balls[0].Display()
    textSize(64)
    textAlign(CENTER, CENTER)
    fill(0, 0 , 255)
    text("GAME OVER", width/2, height/2)
    text("ENTER", width/2, height - 64)
    DrawText()
    
def keyPressed():
    if game_over == True and key == ENTER:
        NewGame()
        
def NewGame():
    global game_over, balls, score
    game_over = False
    score = 0
    balls = [Player_Ball(width/2, height/2, PLAYER_RADIUS)]
    UpdateNumber()
    GenerateNewBalls(10)
    loop()
        
def DestroyBalls():
    del balls[1:]
        
def GenerateNewBalls(count):
    check_result = False
    for i in range(1, count + 1):
        balls.append(Ball())
        balls[i].velocity.setMag(balls[i].velocity.mag() + score)
        if balls[i].number == num_result: check_result = True
    if check_result == False: balls[1].number = num_result
    print(num_result)
    
