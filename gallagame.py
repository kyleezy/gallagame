import pgzrun
import random
WIDTH=800
HEIGHT=600
TITLE="gallaga game"
bullets=[]
jet=Actor("jet")
jet.pos=(400,550)
bug=Actor("bug")
bug.pos=(random.randint(0,800),0)
score=0
def draw():
    screen.fill("red")
    jet.draw()
    bug.draw()
    screen.draw.text(str(score),(50,50))
    for bullet in bullets:
        bullet.draw()
def update():
    global score
    global bullets
    bug.y=bug.y+5
    if bug.y>600:
        bug.pos=(random.randint(0,800),0)
    if keyboard.left:
        jet.x=jet.x-5
    if keyboard.right:
        jet.x=jet.x+5
    if keyboard.space and len(bullets)<5:
        bullet=Actor("bullet")
        bullet.pos=jet.pos
        bullets.append(bullet)
    for bullet in bullets:
        bullet.y=bullet.y-5
        if bullet.colliderect(bug):
            bullets.remove(bullet)
            bug.pos=(random.randint(0,800),0)
            score=score+5
        if bullet.y<0:
            bullets.remove(bullet)





     

    

   


pgzrun.go()

