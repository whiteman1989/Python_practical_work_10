import pygame
from colors import Colors

class ScoreManager():
    def __init__(self, x, y, surf: pygame.Surface) -> None:
        self.score = 0
        font_name = pygame.font.match_font('arial')
        size = 20
        self.font = pygame.font.Font(font_name, size)
        self.x = x
        self.y = y
        self.surf = surf
    
    def add_score(self, score: int) -> int:
        self.score += score
        return self.score
        
    def reduce_score(self, score: int) -> int:
        self.score -+ score
        return self.score
    
    def draw(self) -> None:
        text_surface = self.font.render(str(self.score), True, Colors.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (self.x, self.y)
        self.surf.blit(text_surface, text_rect)