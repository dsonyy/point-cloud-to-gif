import pygame

'''
def dummy(point, cloud) -> pygame.Surface:
    pass
'''

def square(point, cloud, size=1, alpha=64) -> pygame.Surface:
    s = pygame.Surface((size, size))
    s.set_alpha(alpha)
    s.fill(point[3])
    return s


DEFAULT_STYLE = square