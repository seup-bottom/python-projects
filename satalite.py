import pgzrun
import random

WIDTH = 800
HEIGHT = 600

satellites = []
lines = []
next_satellite = 0
number_of_satellite = 15

def create_satellite():
    for count in range(0,number_of_satellite):
        satellite = Actor("satellite.png")
        satellite.pos= random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
        satellites.append(satellite)


def draw():
    screen.blit("satellite_background.png",(0,0))
    number = 1
    for satellite in satellites:
        screen.draw.text(str(number),(satellite.pos[0],satellite.pos[1]+20))
        satellite.draw()
        number = number + 1 
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))

def update():
    pass

def on_mouse_down(pos):
    global next_satellite,lines
    if next_satellite < number_of_satellite:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite-1].pos,satellites[next_satellite].pos))
            next_satellite = next_satellite + 1
        else:
            line = []
            next_satellite = 0
  
create_satellite()
pgzrun.go()
