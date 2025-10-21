from random import randint
import pygame

SIZE = width, height = 1500, 800  # Can resize window
BG_COLOR = (0, 0, 0)  # Background color in RGB

logo = pygame.image.load('/Users/aaditya/Desktop/Coding/python/Projects/DVD/logo.png')
logo = pygame.transform.scale(logo, (100, 50))
img_size = logo.get_rect().size
clock = pygame.time.Clock()
screen = pygame.display
screen.set_caption("DVD Logo")
screen.set_icon(logo)
screen = screen.set_mode(SIZE, pygame.RESIZABLE)
pygame.mouse.set_visible(False)

x = randint(50, width-60)#Starting Pos. (0, 0) very satisfying(fast corner bounce)
y = randint(50, height-60)
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
        x_speed = -x_speed
        newColor = pygame.Color(randint(50, 255), randint(50, 255), randint(50, 255))
        changeColor(newColor)
        color = newColor
    if (y + img_size[1] >= height) or (y <= 0):
        y_speed = -y_speed
        newColor = pygame.Color(randint(50, 255), randint(50, 255), randint(50, 255))
        changeColor(newColor)
        color = newColor
        
    x += x_speed
    y += y_speed
    screen.blit(logo, (x, y))
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get(): 
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]: 
            y_speed -= 1
        if pressed[pygame.K_s]: 
            y_speed += 1
        if pressed[pygame.K_a]: 
            x_speed -= 1
        if pressed[pygame.K_d]: 
            x_speed += 1
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)