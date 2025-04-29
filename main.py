# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
	pygame.init()
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	### 
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0.0
	
	# all the objects that can be updated
	updatable = pygame.sprite.Group()
	# all the objects that can be drawn
	drawable = pygame.sprite.Group()
	# all the asteroids
	asteroids = pygame.sprite.Group()
	# all the shots
	shots = pygame.sprite.Group()


	Player.containers = (updatable, drawable)
	Asteroid.containers = (updatable, drawable, asteroids)
	AsteroidField.containers = (updatable,)
	Shot.containers = (updatable, drawable, shots)

	player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
	asteroidfield = AsteroidField()

	while True:
		clock.tick(60)
		dt = clock.get_time() / 1000.0
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))
		updatable.update(dt)
		# check for collisions
		for asteroid in asteroids:
			if player.collides_with(asteroid):
				print("Game Over!")
				pygame.quit()
				return
		for drawable_object in drawable:
			drawable_object.draw(screen)

		pygame.display.flip()







if __name__ == "__main__":
    main()
