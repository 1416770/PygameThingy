import pygame
from classes.player import Player

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 32)

player1 = Player("Blue", [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_1], 1, screen)
player2 = Player("Red", [pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_KP1], 2, screen)

projectiles = []

def handle_player_input():
    keys_pressed = pygame.key.get_pressed()

    for player in [player1, player2]:
        for player_key in player.keys:
            if keys_pressed[player_key]:
                new_y_direction = 0
                new_x_direction = 0

                event_key_index = player.keys.index(player_key)
                match event_key_index:
                    case 0:
                        new_y_direction = -1
                        player.rect.y -= player.speed * delta_time
                    case 1:
                        new_x_direction = -1
                        player.rect.x -= player.speed * delta_time
                    case 2:
                        new_y_direction = 1
                        player.rect.y += player.speed * delta_time
                    case 3:
                        new_x_direction = 1
                        player.rect.x += player.speed * delta_time
                    case 4:
                        new_projectile = player.fire_projectile()
                        if new_projectile:
                            projectiles.append(new_projectile)

                player.direction.x = new_x_direction
                player.direction.y = new_y_direction
        
        player.draw()

delta_time = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    player1_score_text = font.render(f"Player 1 score: {player1.score}", True, (255, 255, 255))
    player1_score_rectangle = player1_score_text.get_rect()
    screen.blit(player1_score_text, player1_score_rectangle)

    player2_score_text = font.render(f"Player 2 score: {player2.score}", True, (255, 255, 255))
    player2_score_rectangle = player2_score_text.get_rect()
    player2_score_rectangle.left = screen.get_width() - player2_score_rectangle.width
    screen.blit(player2_score_text, player2_score_rectangle)

    for projectile in projectiles:
        if not projectile.draw(delta_time) or projectile.check_for_hits([player1, player2]):
            projectiles.remove(projectile)

    handle_player_input()

    pygame.display.flip()
    delta_time = clock.tick(60) / 1000

pygame.quit()