import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Buttons in pygame')
clock = pygame.time.Clock()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Button:
	def __init__(self, width, height, x, y, color, hover_color):
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		self.color = color
		self.hover_color = hover_color

		pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

	def action(self, action = None):
		# Check if the mouse is inside the button
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
			pygame.draw.rect(screen, self.hover_color, (self.x, self.y, self.width, self.height))
		
			if click[0] == 1 and action != None:
				action()


def game_quit():
	pygame.quit()
	sys.exit()


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_quit()

	screen.fill((0, 0, 0))

	b1 = Button(100, 60, 250, 350, GREEN, BLUE)
	b1.action(game_quit)


	pygame.display.update()
	clock.tick(60)