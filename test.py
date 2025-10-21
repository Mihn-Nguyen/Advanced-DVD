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
# pygame.mouse.set_visible(False)

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