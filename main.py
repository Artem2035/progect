import pygame
from dino import Dino
from terrain import Terrain

player = Dino()
terrain = Terrain()

back_color = (255, 255, 255)
size = (600, 400)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("DinoRex")

FPS = 30
clock = pygame.time.Clock()

font = pygame.font.SysFont('candara', 32)
color1 = (100, 0, 0)
color2 = (0, 0, 50)
text1 = font.render("tst", 1, color1, color2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change_speed(-3)
            elif event.key == pygame.K_RIGHT:
                player.change_speed(3)
            elif event.key == pygame.K_SPACE:
                if player.state != "jump" and player.state != "tilt":
                    player.set_start_anim_time()
                    player.change_state("jump")
            elif event.key == pygame.K_DOWN:
                player.state = "tilt"
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.change_speed(3)
            elif event.key == pygame.K_RIGHT:
                player.change_speed(-3)
            elif event.key == pygame.K_DOWN:
                player.state = "run"

    player.move()

    screen.fill(back_color)
    screen.blit(text1, (0, 0))
    for block in terrain.terrain:
        screen.blit(block.surf, block.get_coordinates(), block.rect)
        block.move()

    terrain.ckeck_ground()

    screen.blit(player.dino_surf, player.coordinates(), player.dino_rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
