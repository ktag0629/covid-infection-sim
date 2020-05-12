import sys, random, pygame
from pygame.locals import *

pygame.init()
random.seed()

directions = {"N":(0,1),
        "S":(0,-1),
        "W":(-1,0),
        "E":(1,0),
        "NW":(-1,1),
        "NE":(1,1),
        "SW":(-1,-1),
        "SE":(1,-1),
        }
speeds = list(range(1,5))

WIDTH = 1040
HEIGHT = 840
FPS = 60
px  = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Person:

    def __init__(self):
        self.x = random.randrange(10, WIDTH-10)
        self.y = random.randrange(10, HEIGHT-10)
        self.direction = None
        self.speed = None
        self.rect = pygame.Rect((self.x, self.y, px, px))
        self.infected = 0

    def draw(self):
        if (self.infected):
            color = (255,0,0)
        else:
            color = (255,255,255)

        pygame.draw.rect(screen, color, self.rect, 0)

    def move(self):
        # pick a random direction that person could take 
        if (self.direction == None):
            d = random.choice(list(directions.keys()))
            self.direction = d
        if (self.speed == None):
            self.speed = random.choice(speeds)

        # see if the current direction will cause the person to move off of the map
        if (self.rect.x + (directions[self.direction][0] * self.speed) >= WIDTH or
                self.rect.x + (directions[self.direction][0] * self.speed) <= 0 or
                self.rect.y + (directions[self.direction][1] * self.speed) >= HEIGHT or
                self.rect.y + (directions[self.direction][1] * self.speed) <= 0):

            # choose a different direction
            tmp = self.direction
            while (self.direction == tmp):
                self.direction = random.choice(list(directions.keys()))

            # apply change
            self.rect.x += directions[self.direction][0] * self.speed
            self.rect.y += directions[self.direction][1] * self.speed

        else:
            # include randomness in the changing of direction
            if (random.randrange(1,100) > 98): # 2%
                tmp = self.direction
                while (self.direction == tmp):
                    self.direction = random.choice(list(directions.keys()))
                if (random.randrange(1, 100) > 95):
                    tmp = self.speed
                    while (self.speed == tmp):
                        self.speed = random.choice(speeds)
            self.rect.x += directions[self.direction][0] * self.speed
            self.rect.y += directions[self.direction][1] * self.speed

def main():
    people = []
    infectedPeople = []
    nInitInfected = 10
    for i in range (200):
        node = Person()
        if(bool(random.getrandbits(1)) and nInitInfected > 0):
            node.infected = 1
            nInitInfected -= 1
            infectedPeople.append(node)
        people.append(node)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0,0,0))
        for person in people:
            for x in infectedPeople:
                if (person in infectedPeople):
                    break
                if (person.rect.colliderect(x.rect) and x.infected == True):
                    person.infected = True
                    infectedPeople.append(person)
            person.draw()
            person.move()
        pygame.display.update()
        pygame.time.Clock().tick(FPS)

main()
