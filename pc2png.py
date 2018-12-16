import pygame
import sys
import math

# local:
import coloring
import style
import cloud as cloudd

def preview(cloud, win_width, win_height, function=None, *args):

    window_main = pygame.display.set_mode([win_width, win_height])
    window_main.fill([0,0,0])
    pygame.display.flip()

    # main loop
    running = True
    while running:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False

        window_main.fill([0,0,0])
        for p in cloud.cloud:
            s = style.square(p, cloud)
            window_main.blit(s, cloudd.get_pos(p))
        pygame.display.flip()

        if function != None:
            function(*args)

        # pygame.image.save(window_main, "output/"+str(i)+".png")
        # i += 1
        
def scale_cloud(xyz, multiplier):
    sxyz = []
    for p in xyz:
        p[0] *= multiplier
        p[1] *= multiplier
        p[2] *= multiplier

# def rotate_cloud(xyz, angle, axis):
#     rxyz = []
#     if axis == 0:
#         A = 1
#         B = 2
#         CA = max_y / 2
#         CB = max_z / 2 
#     elif axis == 1:
#         A = 0
#         B = 2
#         CA = max_x / 2
#         CB = max_z / 2 
#     elif axis == 2:
#         A = 0
#         B = 1
#         CA = max_x / 2
#         CB = max_y / 2

#     for p in xyz:
#         s = math.sin(angle)
#         c = math.cos(angle)
#         p[A] -= CA
#         p[B] -= CB
#         xnew = p[A] * c - p[B] * s
#         ynew = p[A] * s + p[B] * c
#         p[A] = xnew + CA
#         p[B] = ynew + CB
#         rxyz.append(p)

#     return rxyz 


c = cloudd.import_cloud(sys.argv[1])
c.color(coloring.DEFAULT_COLORING)
preview(c, 800, 600)