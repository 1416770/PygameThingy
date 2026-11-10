import pygame

class Projectile:
    speed = 400
    surface: pygame.Surface
    rect: pygame.Rect
    colour: str
    direction: pygame.Vector2
    owner: any

    def __init__(self, position: pygame.Vector2, colour: str, direction: pygame.Vector2, owner, surface: pygame.Surface):
        print(owner.score)

        self.colour = colour
        self.direction = direction.copy()
        self.owner = owner
        self.surface = surface
        self.rect = pygame.Rect((position.x + 10, position.y + 10), (10, 10))
    
    def draw(self, delta_time: float) -> bool:
        rect, direction, speed, surface = self.rect, self.direction, self.speed, self.surface

        rect.x += direction.x * (speed * delta_time)
        rect.y += direction.y * (speed * delta_time)
        if rect.x > surface.get_width() or rect.x < 0 or rect.y > surface.get_height() or rect.y < 0:
            return False
        else:
            pygame.draw.rect(surface, self.colour, rect)

            return True
        
    def check_for_hits(self, players: list) -> bool:
        for player in players:
            if player != self.owner and self.rect.colliderect(player.rect):
                self.owner.score += 1

                return True
        return False