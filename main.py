import pygame, time, sys, _thread, math
from PIL import Image
from random import randint
from libs import mapGenerator

def updateMyScreen(threadName, delay):

	#get area to draw
	surfaceRect = mainSurface.get_rect()

	while True:
		screen.blit(mainSurface, surfaceRect)
		pygame.display.flip()
		pygame.time.wait(delay)

#some Colours
black = 0,0,0,255
white = 255, 255, 255
gold = 255, 255, 0
trees = 10, 100, 10

#starts pygame ingine
pygame.init()

#setting windows size
size = width, height = 800, 800
screen = pygame.display.set_mode(size)

#setting a surface to draw into 
mainSurface = pygame.Surface(size)

_thread.start_new_thread(mapGenerator.generateMap, (mainSurface, [width, height] , [1,1,0.3], 200000, 120, 0.0, 5, 20))
_thread.start_new_thread(updateMyScreen, ("Updater", 40))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()