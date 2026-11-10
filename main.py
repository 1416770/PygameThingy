import pygame
import os
from classes.player import Player

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 32)

player1 = Player("Blue", [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_1], 1, screen)
player2 = Player("Red", [pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_KP1], 2, screen)

background_image = pygame.image.load(os.path.join("resources", "background.png")).convert_alpha()
background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))
background_rect = background_image.get_rect()

pygame.display.set_icon(background_image)
pygame.display.set_caption("ummmm pygame shooter thingy yeah")

projectiles = []

def update_players(): # Handles player input and character movement.
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

def update_scores(): # Renders the player scores.
    player1_score_text = font.render(f"Player 1 score: {player1.score}", True, (0, 0, 255))
    player1_score_rectangle = player1_score_text.get_rect()
    screen.blit(player1_score_text, player1_score_rectangle)

    player2_score_text = font.render(f"Player 2 score: {player2.score}", True, (255, 0, 0))
    player2_score_rectangle = player2_score_text.get_rect()
    player2_score_rectangle.left = screen.get_width() - player2_score_rectangle.width
    screen.blit(player2_score_text, player2_score_rectangle)

    if player1.score >= 100:
        
        pass
    elif player2.score >= 100:
        pass

def update_projectiles(): # Draws, checks for hits and removes projectiles.
    for projectile in projectiles:
        if not projectile.draw(delta_time) or projectile.check_for_hits([player1, player2]):
            projectiles.remove(projectile)

delta_time = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, background_rect)

    update_scores()
    update_projectiles()
    update_players()

    pygame.display.flip()
    delta_time = clock.tick(60) / 1000

pygame.quit()