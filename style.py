import pygame

'''
def dummy(point, cloud) -> pygame.Surface:
    pass
'''

def square(point, size=1, alpha=255) -> pygame.Surface:
    s = pygame.Surface((size, size))
    s.set_alpha(alpha)
    s.fill(point[3])
    return s


DEFAULT_STYLE = square