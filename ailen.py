import pgzrun 
import random

TITLE = 'Good shot'

WIDTH = 500
HEIGHT = 500

message = ''

alien = Actor('alien.png')
alien.pos = 50,50

def draw():
    screen.clear()
    screen.fill(color = (128,100,30))
    alien.draw()
    screen.draw.text(message,center=(400,10),fontsize=30)

def place_alien():
    alien.x = random.randint(50,WIDTH-50)
    alien.y = random.randint(50,HEIGHT-50)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "yipee"
        place_alien()
    else:
        message = "no yipee"

pgzrun.go() 