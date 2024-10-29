import pgzrun
WIDTH=800
HEIGHT=600
TITLE="gallaga game"
jet=Actor("jet")
jet.pos=(400,550)
bug=Actor("bug")
bug.pos=(400,200)
def draw():
    screen.fill("red")
    jet.draw()
    bug.draw()
    

pgzrun.go()

