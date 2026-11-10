import pygame
from classes.projectile import Projectile

class Player:
    id: int
    colour: str
    radius = 40
    keys: list[str]
    speed = 300
    surface: pygame.Surface
    direction = pygame.Vector2(0, 0)
    projectile_cooldown = 500
    last_projectile = 0
    score = 0
    rect: pygame.rect

    def __init__(self, colour: str, keys: list[str], id: int, surface: pygame.Surface):
        self.colour = colour
        self.keys = keys
        self.id = id
        self.surface = surface

        image = pygame.image.load("player_sprite.PNG").convert_alpha()
        rect = image.get_rect()
        rect.width = self.radius
        rect.height = self.radius
        image.set_pos(pygame.Vector2(surface.get_width() / 2, surface.get_height() / 2))

        self.rect = rect

    def draw(self):
        pygame.draw.rect(self.surface, self.colour, self.rect)

    def fire_projectile(self) -> Projectile:
        current_ticks = pygame.time.get_ticks()
        if self.direction.magnitude() != 0 and (current_ticks - self.last_projectile) >= self.projectile_cooldown:
            self.last_projectile = current_ticks

            return Projectile(pygame.Vector2(self.rect.x, self.rect.y), self.colour, self.direction, self, self.surface)