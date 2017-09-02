import time, math, pygame, time
from random import randint
from opensimplex import OpenSimplex

def generateMap(surfaceToDraw, sizeOfMap, listOfOctaves, waveL, waterLevel, a, b, c):

	#generating seeds for the map and biomes
	currentNumber = ""
	currentNumber2 = ""

	while len(currentNumber) < 31:
		currentNumber += str(randint(0, 9))

	while len(currentNumber2) < 31:
		currentNumber2 += str(randint(0, 9))

	seed = int(currentNumber)
	seed2 = int(currentNumber2)
	mapNoiseGen = OpenSimplex(seed=seed)
	biomeNoiseGen = OpenSimplex(seed=seed2)

	noiseGen(surfaceToDraw, sizeOfMap, listOfOctaves, waveL, waterLevel, a, b, c, mapNoiseGen, biomeNoiseGen)
	
#using openSimplex to generate noise
def noise(mapNoiseGen, nx, ny):
	return mapNoiseGen.noise2d(nx, ny) / 2.0 + 0.5

def noiseGen(surfaceToDraw, sizeOfMap, listOfOctaves, waveL, waterLevel, a, b, c, mapNoiseGen, biomeNoiseGen):

	width = sizeOfMap[0]
	height = sizeOfMap[1]

	freq = (width * height) / waveL

	for y in range(height):
		for x in range(width):

			nx, ny = x/width - 0.5, y/height - 0.5
			d = 2 * max(abs(nx), abs(ny))

			valueOfNoise = 0
			valueOfNoise2 = 0
			i = 0
			valueOfDiv = 0

			for octave in listOfOctaves:

				currentPower = math.pow(2, i)
				valueOfNoise += octave * noise(mapNoiseGen, freq * currentPower * nx, freq * currentPower * ny)
				valueOfNoise2 += octave * noise(biomeNoiseGen, freq/4 * currentPower * nx, freq/4 * currentPower * ny)
				valueOfDiv += octave
				i+=1

			valueOfNoise /= valueOfDiv
			valueOfNoise2 /= valueOfDiv

			valueOfNoise = (valueOfNoise + a) * (1 - b*math.pow(d, c))

			if valueOfNoise > 1:
				valueOfNoise = 1
			elif valueOfNoise < 0:
				valueOfNoise = 0

			if valueOfNoise2 > 1:
				valueOfNoise2 = 1
			elif valueOfNoise2 < 0:
				valueOfNoise2 = 0

			value = int(valueOfNoise * 255)
			value2 = int(valueOfNoise2 * 255)

			#setting water
			if value <= waterLevel:
				color = pygame.Color(20, 10, 90, 255)
			
			#setting Biomes
			elif value2 >= 200:
				color = pygame.Color(200, 200, 10, 255)
			elif value2 < 180 and value2 >= 130:
				color = pygame.Color(100, 200, 10, 255)
			elif value2 < 130 and value2 >= 80:
				color = pygame.Color(50, 160, 10, 255)
			elif value2 < 80 and value2 >= 20:
				color = pygame.Color(60, 100, 10, 255)
			
			#setting each pixle an color
			surfaceToDraw.set_at((x,y), color)