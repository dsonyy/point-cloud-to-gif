import pygame
import sys
import math
import threading
import os
import imageio
import pygifsicle

import coloring
import style
import cloud as cl

cloud = None
redraw = True
running = False

def window_loop():
    """
        Creates pygame window, handles user input and renders point cloud
    """
    # Prepare pygame window
    global redraw, running
    width, height = 480, 320
    window_main = pygame.display.set_mode([width, height], flags=pygame.RESIZABLE)
    window_main.fill([0,0,0])
    pygame.display.flip()
    running = True

    # Main pygame window loop
    while running:
        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                running = False
               
            if event.type == pygame.VIDEORESIZE:
                width, height = event.w, event.h
                window_main = pygame.display.set_mode([width, height], flags=pygame.RESIZABLE)
                redraw = True
                print("\nPlease wait...\n:", end="")

        # Redraw if needed
        if redraw and cloud:
            window_main.fill([0,0,0])
            for p in cloud.points:
                if len(p) == 3:
                    color = (coloring.DEFAULT_COLORING(cloud, p)) # Add colors to the point
                    p += [color]
                s = style.square(p) # Get pygame.Surface of the point
                window_main.blit(s, cloud.get_pos(p, width, height))
            pygame.display.flip()
            redraw = False


def cli_loop():
    """
        Handles user command line input and executes his commands
    """
    global cloud, redraw, running
    print("-----------------------------------------------------------------------\n"
          "Commands: \n"
          "   L path                - Loads a point cloud from file.\n"
          "   M x (y)               - Moves a point cloud on the screen.\n"
          "   R x (y)(z)            - Rotates a point cloud around X, Y, Z axis.\n"
          "                           Specify angle in degrees.\n"
          "   S (filename)          - Saves a screenshot* of the screen to a file.\n"
          "   C scale               - Sets a point cloud scale on the screen.\n"
          "   G (filaname) (frames) - Saves a GIF file with an animation of\n"
          "                           rotating a point cloud.\n"
          "\n"
          "* - Resizing the render window affects on the size of the screenshot.\n"
          "\n"
          "Example usage:\n"
          "   L input/cone.txt\n"
          "   R 45 33.333 -700\n"
          "   S screenshot.png\n"
          "   G animation.gif 360\n"
          "   L input/marszalek.txt\n"
          "-----------------------------------------------------------------------\n")
    
    if len(sys.argv) > 2:
        try:
            cloud = cl.PointCloud(sys.argv[1])
            thread = threading.Thread(target=window_loop)
            thread.daemon = True
            thread.start()
        except:
            print("Unable to load cloud.")
    # Main command line loop
    while True:
        while redraw and running:
            pass
        cmd = input(":").strip().lower().split()
        if not cmd: continue
        if cmd[0] in ["r", "rotate"]: # rotates the point cloud
            if len(cmd) < 2:
                print("Invalid number of arguments.")
                continue
            if not running:
                print("Point cloud is not loaded.")
                continue
            x, y, z = 0, 0, 0
            try: x = float(cmd[1])
            except:
                print("Invalid X.")
                continue
            if len(cmd) >= 3:
                try: y = float(cmd[2])
                except:
                    print("Invalid Y.")
                    continue
            if len(cmd) >= 4:
                try: z = float(cmd[3])
                except:
                    print("Invalid Z.")
                    continue
            print("Please wait...")
            # Calling this funtion 3 times for each axis is not optimal
            cloud.rotate_cloud(x, 0)
            cloud.rotate_cloud(-y, 1)
            cloud.rotate_cloud(z, 2)
            redraw = True

        elif cmd[0] in ["m", "move"]: # moves the point cloud on the screen
            if len(cmd) < 2 or len(cmd) > 3:
                print("Invalid number of arguments.")
                continue
            if not running:
                print("Point cloud is not loaded.")
                continue
            x, y = 0, 0
            try: x = float(cmd[1])
            except:
                print("Invalid X.")
                continue
            if len(cmd) == 3:
                try: y = float(cmd[2])
                except:
                    print("Invalid Y.")
                    continue
            print("Please wait...")
            cloud.offset_x += x
            cloud.offset_y += y
            redraw = True

        elif cmd[0] in ["s","save"]: # saves screenshot of the rendered point cloud
            if len(cmd) > 2:
                print("Invalid number of arguments.")
                continue
            if not running:
                print("Point cloud is not loaded.")
                continue
            filename = "render.png"
            if len(cmd) == 2:
                filename = str(cmd[1])
            try:
                print("Please wait...")
                pygame.image.save(pygame.display.get_surface(), filename)
            except Exception as e:
                print("Unable to save: " + str(e))

        elif cmd[0] in ["g", "gif"]: # generates and saves a GIF file
            if len(cmd) > 3:
                print("Invalid number of arguments.")
                continue
            if not running:
                print("Point cloud is not loaded.")
                continue
            filename_target = "render.gif"
            number_of_frames = 10
            if len(cmd) >= 2:
                filename_target = str(cmd[1])
                if filename_target[-4:].lower() != ".gif":
                    filename_target += ".gif"
            if len(cmd) == 3:
                try:
                    number_of_frames = int(cmd[2])
                except:
                    print("Invalid number of frames.")
                    continue
            print("Please wait...")
            try:
                os.mkdir("temp")
            except FileExistsError:
                filenames = os.listdir("temp")
                for filename in filenames:
                    os.remove("temp/" + filename)
            for i in range(number_of_frames):
                cloud.rotate_cloud(360 / number_of_frames, 1)
                redraw = True
                while redraw:
                    pass
                pygame.image.save(pygame.display.get_surface(), "temp/" + str(i) + ".png")
                print("Frame " + str(i) + " saved.")
            filenames = [int(f[:-4]) for f in os.listdir("temp")]
            filenames.sort()
            filenames = [str(f) + ".png" for f in filenames]
            with imageio.get_writer(filename_target, mode="I", format="gif", duration=0.2) as writer:
                for filename, i in zip(filenames, range(len(filenames))):
                    image = imageio.imread("temp/" + filename)
                    writer.append_data(image)
                    print("Frame " + str(i) + " appended to the gif.")
            try:
                print("Compressing the GIF...")
                pygifsicle.optimize(filename_target) # Optimize a GIF using gifsicle
            except FileNotFoundError:
                print("gifsicle not found so the GIF has not been compressed.")
                

        elif cmd[0] in ["l", "load"]: # loads the point cloud from file and creates pygame window if it doesn't exist yet
            if len(cmd) != 2:
                print("Invalid number of arguments.")
                continue
            try:
                print("Please wait...")
                cloud = cl.PointCloud(str(cmd[1]))
            except:
                print("Unable to load cloud.")
                continue
            if not running:
                thread = threading.Thread(target=window_loop)
                thread.daemon = True
                thread.start()
            redraw = True

        elif cmd[0] in ["c","scale"]: # scales the point cloud on the screen
            if len(cmd) != 2:
                print("Invalid number of arguments.")
                continue
            if not running:
                print("Point cloud is not loaded.")
                continue
            try: scale = float(cmd[1])
            except:
                print("Invalid scale.")
                continue
            print("Please wait...")
            cloud.scale = scale
            redraw = True

        else:
            print("Unknown command.")

if __name__ == "__main__":
    try:
        cli_loop()
    except (EOFError, KeyboardInterrupt):
        running = False
        print("Exiting.")
