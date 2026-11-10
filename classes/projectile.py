import pygame
import os

class Projectile:
    speed = 800
    surface: pygame.Surface
    rect: pygame.Rect
    image: pygame.image
    colour: str
    direction: pygame.Vector2
    owner: any

    def __init__(self, position: pygame.Vector2, colour: str, direction: pygame.Vector2, owner, surface: pygame.Surface):
        self.colour = colour
        self.direction = direction.copy()
        self.owner = owner
        self.surface = surface

        image = pygame.image.load(os.path.join("resources", "projectile.png")).convert_alpha()
        image = pygame.transform.scale(image, (30, 30))
        if colour == "Blue":
            pixel_array = pygame.PixelArray(image)
            pixel_array.replace((255, 255, 255), (0, 0, 255))
        else:
            pixel_array = pygame.PixelArray(image)
            pixel_array.replace((255, 255, 255), (255, 0, 0))
        self.image = image

        rect = image.get_rect()
        rect.x = position.x
        rect.y = position.y
        self.rect = rect
    
    def draw(self, delta_time: float) -> bool:
        rect, direction, speed, surface = self.rect, self.direction, self.speed, self.surface

        rect.x += direction.x * (speed * delta_time)
        rect.y += direction.y * (speed * delta_time)
        if rect.x > surface.get_width() or rect.x < 0 or rect.y > surface.get_height() or rect.y < 0:
            return False
        else:
            self.surface.blit(self.image, self.rect)

            return True
        
    def check_for_hits(self, players: list) -> bool:
        for player in players:
            if player != self.owner and self.rect.colliderect(player.rect):
                self.owner.score += 1

                return True
        return False