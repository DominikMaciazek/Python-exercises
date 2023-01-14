import pygame
import random


pygame.init()
clock = pygame.time.Clock()
FPS = 60  # Frames per second.

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

window = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(window)
background = pygame.Surface(window)

COLORS_OF_BALLS = [(0, 0, 0),(41, 41, 41),(161, 31, 41),(153, 0, 0),(240, 248, 255),(250, 235, 215),(255, 0, 0)]


class MovingSquare:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.krok_x = random.randint(0,10)
        self.krok_y = random.randint(0,10)
        self.color = random.choice(COLORS_OF_BALLS)

    def paint(self):
        pygame.draw.rect(background, self.color, (self.x, self.y, 50, 50), border_radius=50)
        


    def update_position(self):
        self.x += self.krok_x
        if self.x < 0:
            self.krok_x = -self.krok_x
            self.x = 0
        elif self.x + 50 > WINDOW_WIDTH:
            self.krok_x = -self.krok_x
            self.x = WINDOW_WIDTH - 50
        self.y += self.krok_y
        if self.y < 0:
            self.krok_y = -self.krok_y
            self.y = 0
        elif self.y + 50 > WINDOW_HEIGHT:
            self.krok_y = -self.krok_y
            self.y = WINDOW_HEIGHT - 50

square_1 = MovingSquare(120, 220)
square_2 = MovingSquare(190, 20)
square_3 = MovingSquare(19, 200)




def paint():
    #background-color
    pygame.draw.rect(background, (255, 255, 255), (0, 0, *window))
    #moving squares
    square_1.paint()
    square_2.paint()
    square_3.paint()
    screen.blit(background, (0, 0))
    pygame.display.flip()



done = False
while not done:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    paint()
    square_1.update_position()
    square_2.update_position()
    square_3.update_position()
    
pygame.quit()