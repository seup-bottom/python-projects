import pgzrun 
import random

WIDTH = 600
HEIGHT = 500

score = 0 
game_over = False

bee = Actor('bee.png')
bee.pos = 100,100

flower = Actor("flower.png")
flower.pos = 200,200

def draw():
    screen.blit("background.png",(0,0))
    flower.draw()
    bee.draw()
    screen.draw.text("Score: "+str(score),color='black',topleft=(10,10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("time's up! your final score is: "+str(score),color="red",midtop=(300,10),fontsize=40)

def place_flower():
    flower.x = random.randint(70,WIDTH-70)
    flower.Y = random.randint(70,HEIGHT-70)

def time_up():
        global game_over
        game_over = True

def update():
        global score
        if keyboard.left:
            bee.x = bee.x - 2
        if keyboard.right:
            bee.x = bee.x + 2
        if keyboard.up:
            bee.y = bee.y - 2
        if keyboard.down:
            bee.y = bee.y + 2
        flower_collected = bee.colliderect(flower)
        if flower_collected:
            score=score + 10
            place_flower()


clock.schedule(time_up,60.0)
pgzrun.go()