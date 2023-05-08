import pygame
from game import Game

game = Game()

pygame.init()
screen = pygame.display.set_mode(game.size)
pygame.display.set_caption("DinoRex")

clock = pygame.time.Clock()

font = pygame.font.SysFont('candara', 32)

score_text = font.render("000", True, game.score_color, game.back_color)

while game.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.player.change_speed(-3)
            elif event.key == pygame.K_RIGHT:
                game.player.change_speed(3)
            elif event.key == pygame.K_SPACE:
                if game.player.state != "jump" and game.player.state != "tilt":
                    game.player.set_start_anim_time()
                    game.player.change_state("jump")
            elif event.key == pygame.K_DOWN:
                game.player.state = "tilt"
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                game.player.change_speed(3)
            elif event.key == pygame.K_RIGHT:
                game.player.change_speed(-3)
            elif event.key == pygame.K_DOWN:
                game.player.state = "run"

    game.player.move()

    screen.fill(game.back_color)
    screen.blit(score_text, (0, 0))
    for block in game.game_terrain.terrain:
        screen.blit(block.surf, block.get_coordinates(), block.rect)
        block.move()

    game.game_terrain.ckeck_ground()

    for cloud in game.sky:
        cloud.check()
        cloud.move()
        screen.blit(cloud.surf, cloud.get_coordinates(), cloud.rect)

    screen.blit(game.player.dino_surf, game.player.coordinates(), game.player.dino_rect)
    pygame.display.update()
    clock.tick(game.FPS)
    score_text = font.render(f"{game.score // 10}", True, game.score_color, game.back_color)
    game.score += 1
pygame.quit()
