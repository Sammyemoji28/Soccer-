
import pgzrun
import random

HEIGHT = 500
WIDTH = 600

ball = Actor("soccerball2")
ball.pos = (293,208)

goal = Actor("soccergoal")
goal.pos = (192,420)

score = 0
gameover = False

def draw():
    screen.blit("grass",(0,0))
    ball.draw()
    goal.draw()
    screen.draw.text("Score: {}".format(score),fontsize = 45, topleft = (30,30))
    if gameover:
        screen.fill("light blue")
        screen.draw.text("Times Up! Your final score is {}!".format(score),fontsize = 35, color = "blue", center = (300,250))

def goalPos():
    goal.x = random.randint(50,550)
    goal.y = random.randint(50,450)

def update():
    global score
    if keyboard.left:
        ball.x = ball.x - 5
    if keyboard.right:
        ball.x = ball.x + 5
    if keyboard.up:
        ball.y = ball.y - 5
    if keyboard.down:
        ball.y = ball.y + 5
    
    if ball.colliderect(goal):
        score += 1
        goalPos()

def timeup():
    global gameover
    gameover = True

clock.schedule(timeup,60.0)

pgzrun.go()