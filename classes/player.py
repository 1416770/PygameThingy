import pygame
import os
from classes.projectile import Projectile

class Player:
    id: int
    colour: str
    radius = 40
    keys: list[str]
    speed = 300
    surface: pygame.Surface
    direction = pygame.Vector2(0, 0)
    projectile_cooldown = 250
    last_projectile = 0
    score = 0
    rect: pygame.rect
    image: pygame.image

    def __init__(self, colour: str, keys: list[str], id: int, surface: pygame.Surface):
        self.colour = colour
        self.keys = keys
        self.id = id
        self.surface = surface

        image = pygame.image.load(os.path.join("resources", "player_sprite.png")).convert_alpha()
        image = pygame.transform.scale(image, (100, 100))
        if id == 1:
            pixel_array = pygame.PixelArray(image)
            pixel_array.replace((255, 255, 255), (0, 0, 255))
        else:
            pixel_array = pygame.PixelArray(image)
            pixel_array.replace((255, 255, 255), (255, 0, 0))
        self.image = image

        rect_position = pygame.Vector2(surface.get_width() / 2, surface.get_height() / 2)
        rect = image.get_rect()
        rect.x = rect_position.x
        rect.y = rect_position.y
        self.rect = rect


    def draw(self):
        self.surface.blit(self.image, self.rect)

    def fire_projectile(self) -> Projectile:
        current_ticks = pygame.time.get_ticks()
        if self.direction.magnitude() != 0 and (current_ticks - self.last_projectile) >= self.projectile_cooldown:
            self.last_projectile = current_ticks

            return Projectile(pygame.Vector2(self.rect.x, self.rect.y), self.colour, self.direction, self, self.surface)