import pygame
# from pc2png import X, Y, Z, COLOR, PLANE_X, PLANE_Y, PLANE_Z

'''
def dummy(point, cloud) -> pygame.Surface:
    pass
'''

def square(point, cloud, size=5, alpha=255) -> pygame.Surface:
    s = pygame.Surface((size, size))
    s.set_alpha(alpha)
    s.fill(point[3])
    return s


DEFAULT_STYLE = square