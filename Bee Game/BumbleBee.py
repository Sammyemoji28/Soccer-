
import pgzrun
import random

HEIGHT = 500
WIDTH = 600

bee = Actor("bee")
bee.pos = (293,208)

flower = Actor("flower")
flower.pos = (192,420)

score = 0
gameover = False

def draw():
    screen.blit("grass",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score: {}".format(score),fontsize = 45, topleft = (30,30))
    if gameover:
        screen.fill("light blue")
        screen.draw.text("Times Up! Your final score it {}!".format(score),fontsize = 45, color = "red", center = (300,250))

def flowerPos():
    flower.x = random.randint(50,550)
    flower.y = random.randint(50,450)

def update():
    global score
    if keyboard.left:
        bee.x = bee.x - 5
    if keyboard.right:
        bee.x = bee.x + 5
    if keyboard.up:
        bee.y = bee.y - 5
    if keyboard.down:
        bee.y = bee.y + 5
    
    if bee.colliderect(flower):
        score += 1
        flowerPos()

def timeup():
    global gameover
    gameover = True

clock.schedule(timeup,60.0)

pgzrun.go()