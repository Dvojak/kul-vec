import pygame


class CustomSurface:
    '''Třída pro surface pozadí hry'''
    def __init__(self, width, height, position):
        self.surface = pygame.Surface((width,height))
        self.surface.fill((255,0,0))
        self.position = position

        # Nacteni obrázku
        self.image = pygame.image.load("barrier/grass-field-texture-patternpictures-2514-1500x996.jpg")
        self.image = pygame.transform.scale(self.image, (width,height))
    def draw(self, target_surface):
        self.surface.blit(self.image, (0,0))
        target_surface.blit(self.surface,self.position)