import pygame
import sys
import math
import threading

import coloring
import style
import cloud as cl

cloud = cl.PointCloud(sys.argv[1])
window_main = None
processing = False
redraw = True
running = True

def window_loop():
    global redraw, running, processing, window_main
    window_main = pygame.display.set_mode([900, 700])
    pygame.font.init()
    window_main.fill([0,0,0])
    font = pygame.font.SysFont(pygame.font.get_default_font(), 16)
    text_processing = font.render("Processing...", True, (255, 255, 255), (0, 0, 0, 255))
    window_main.blit(text_processing, (10, 10))
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if processing:
            window_main.blit(text_processing, (10, 10))
            pygame.display.flip()

        if redraw:
            window_main.fill([0,0,0])
            for p in cloud.points:
                if len(p) == 3:
                    color = (coloring.xyzrgb(cloud, p, 1))
                    s = style.square(p + [color])
                else:
                    s = style.square(p)
                window_main.blit(s, cl.get_pos(p))
            pygame.display.flip()
            redraw = False

if __name__ == "__main__":
    thread = threading.Thread(target=window_loop)
    thread.daemon = True
    thread.start()
    while running:
        cmd = input(":").strip().lower().split()
        if not cmd:
            continue

        if cmd[0] in ["r", "rotate"]:
            if len(cmd) < 2:
                print("Invalid number of arguments.")
                continue
            x, y, z = 0, 0, 0
            try:
                x = float(cmd[1])
            except:
                print("Invalid X.")
                continue
            if len(cmd) >= 3:
                try:
                    y = float(cmd[2])
                except:
                    print("Invalid Y.")
                    continue
            if len(cmd) >= 4:
                try:
                    z = float(cmd[3])
                except:
                    print("Invalid Z.")
                    continue
            processing = True
            cloud.rotate_cloud(x, 0)
            cloud.rotate_cloud(-y, 1)
            cloud.rotate_cloud(z, 2)
            processing = False
            redraw = True

        elif cmd[0] in ["m", "move"]:
            if len(cmd) < 2:
                print("Invalid number of arguments.")
                continue
            x, y, z = 0, 0, 0
            try:
                x = float(cmd[1])
            except:
                print("Invalid X.")
                continue
            if len(cmd) >= 3:
                try:
                    y = float(cmd[2])
                except:
                    print("Invalid Y.")
                    continue
            if len(cmd) >= 4:
                try:
                    z = float(cmd[3])
                except:
                    print("Invalid Z.")
                    continue
            processing = True
            cloud.move_cloud(x, y, z)
            processing = False
            redraw = True
        elif cmd[0] in ["s","save"]:
            if len(cmd) > 2:
                print("Invalid number of arguments.")
                continue
            filename = "render.png"
            if len(cmd) == 2:
                filename = str(cmd[1])
            try:
                processing = False
                pygame.image.save(window_main, filename)
            except Exception as e:
                print("Unable to save: " + str(e))