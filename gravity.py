from random import randint
import pygame

SIZE = width, height = 1500, 800  # Can resize window
BG_COLOR = (0, 0, 0)  # Background color in RGB

logo = pygame.image.load('logo.png')
logo = pygame.transform.scale(logo, (100, 50))
img_size = logo.get_rect().size
clock = pygame.time.Clock()
screen = pygame.display
screen.set_caption("DVD Logo")
screen.set_icon(logo)
screen = screen.set_mode(SIZE, pygame.RESIZABLE)

x = 0#Starting Pos. (0, 0) very satisfying(fast corner bounce)
y = 0
x_speed = 2.5#Speed
y_speed = 2.5

def changeColor(newColor):
    pixels = pygame.PixelArray(logo) 
    pixels.replace(color, newColor)

color = pygame.Color(0, 0, 0)
newColor = pygame.Color(randint(50, 255), randint(50, 255), randint(50, 255))
changeColor(newColor)
color = newColor
while True:
    screen.fill(BG_COLOR)
    SIZE = width, height = pygame.display.get_surface().get_size()
    if (x + img_size[0] >= width) or (x <= 0):
        if abs(x_speed) <= 1:
            x_speed = -x_speed*(randint(100, 300)/100)
        elif abs(x_speed) >= 10:
            x_speed = -x_speed*(randint(30, 100)/100)
        else:
            x_speed = -x_speed*(randint(30, 300)/100)
        newColor = pygame.Color(randint(50, 255), randint(50, 255), randint(50, 255))
        changeColor(newColor)
        color = newColor
    if (y + img_size[1] >= height):
        if y_speed < 2:
            y_speed = -height/randint(25, 30)
        else:
            y_speed = -0.9*y_speed
        
    y_speed += 1
    y += y_speed
    x += x_speed
    screen.blit(logo, (x, y))
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
