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
def draw():
    screen.fill("red")
    jet.draw()
    bug.draw()
    for bullet in bullets:
        bullet.draw()
def update():
    global bullets
    bug.y=bug.y+5
    if bug.y>600:
        bug.pos=(random.randint(0,800),0)
    if keyboard.left:
        jet.x=jet.x-5
    if keyboard.right:
        jet.x=jet.x+5
    if keyboard.space:
        bullet=Actor("bullet")
        bullet.pos=jet.pos
        bullets.append(bullet)




     

    

   


pgzrun.go()

