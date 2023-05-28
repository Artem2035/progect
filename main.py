import pygame
from game import Game
from bird import Bird



pygame.init()
screen = pygame.display.set_mode((600,300))
pygame.display.set_caption("DinoRex")
font = pygame.font.SysFont('candara', 32)
best_score = 0
def init_game():
    game = Game()
    clock = pygame.time.Clock()
    score_text = font.render("000", True, game.score_color, game.back_color)
    best_score_text = font.render("000", True, game.best_score_color, game.back_color)

    game_retry = False
    game_stop = False
    while not(game_stop):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game_stop = True
            elif event.type == pygame.KEYDOWN and game.running:
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
            elif event.type == pygame.KEYUP and game.running:
                if event.key == pygame.K_LEFT:
                    game.player.change_speed(3)
                elif event.key == pygame.K_RIGHT:
                    game.player.change_speed(-3)
                elif event.key == pygame.K_DOWN:
                    game.player.state = "run"
            elif event.type == pygame.MOUSEBUTTONDOWN and not(game.running):
                if game.button_rect.collidepoint(event.pos):
                    game_stop = True
                    game_retry =True

        if game.running:
            screen.fill(game.back_color)
            for block in game.game_terrain.terrain:
                block.move()
                screen.blit(block.surf, block.rect)
                screen.blit(block.surf, block.rect)
                if isinstance(block, Bird):
                    screen.blit(block.bird_surf, block.bird_rect)

            game.game_terrain.ckeck_ground()

            for cloud in game.sky:
                cloud.check()
                cloud.move()
                screen.blit(cloud.surf, cloud.get_coordinates(), cloud.rect)

            game.player.move()
            game.running = game.player.collision(game.game_terrain.terrain)

            game.score += 1

        screen.blit(game.player.dino_surf, game.player.dino_rect)
        if not (game.running):
            game.surf = game.surf_retry_button
            screen.blit(game.surf, game.button_rect)

        score_text = font.render(f"{game.score // 10}", True, game.score_color, game.back_color)
        if best_score > game.score//10:
            best_score_text = font.render(f"{best_score}", True, game.best_score_color, game.back_color)
        else:
            best_score_text = font.render(f"{game.score // 10}", True, game.best_score_color, game.back_color)
        screen.blit(score_text, (0, 0))
        screen.blit(best_score_text, (0, 30))

        pygame.display.update()
        clock.tick(game.FPS)

    return game_retry, game.score

game_loop = True
while game_loop:
    params = init_game()
    game_loop = params[0]
    score = params[1]//10
    if best_score < score:
        best_score = score
pygame.quit()