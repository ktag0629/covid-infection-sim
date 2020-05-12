import sys, random, pygame
from pygame.locals import *

pygame.init()

dirs = {"N":(0,1),
        "S":(0,-1),
        "W":(-1,0),
        "E":(1,0)
        }

WIDTH = 1040
HEIGHT = 840
FPS = 60
px  = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Person:
    def __init__(self):
        self.x = random.randrange(10, WIDTH-10)
        self.y = random.randrange(10, HEIGHT-10)

    def draw(self):
        pygame.draw.rect(screen, (255,255,255),
                         (self.x, self.y, px, px), 0)

    def move(self):
        # change direction of person

        # if going south subtract the current y coord by 1
        # if going north add the current y coord by 1
        # if going east add the current x coord by 1
        # if going west subtract the current x coord by 1
        # if NW, -1, 1
        # if NE, 1, 1
        # if SW, -1, -1
        # if SE, 1, -1


def main():
    people = []
    for i in range (100):
        node = Person()
        people.append(node)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0,0,0))
        for person in people:
            person.draw()
        pygame.display.update()
        pygame.time.Clock().tick(FPS)

main()
