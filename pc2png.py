import pygame
import sys
import math
import threading

import coloring
import style
import cloud as cl

cloud = None
redraw = True
running = False

# Function creates pygame window, handles user input and renders point cloud
def window_loop():
    # Prepare pygame window
    global redraw, running
    width, height = 800, 800
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
                    s = style.STYLE_FUNCTION(p + [color]) # Get pygame.Surface of the point
                else:
                    s = style.square(p) # Get pygame.Surface of the point
                window_main.blit(s, cloud.get_pos(p, width, height))
            pygame.display.flip()
            redraw = False

# Function handles user command line input and executes his commands
def cli_loop():
    global cloud, redraw, running
    print("---------------------------------------------------------------------\n"
          "Usage: \n"
          "   L path        - Loads a point cloud from file.\n"
          "   M x (y)       - Moves a point cloud on the screen.\n"
          "   R x (y)(z)    - Rotates a point cloud around X, Y, Z axis.\n"
          "                   Specify angle in degrees.\n"
          "   S (filename)  - Saves a screenshot* of the screen to a file.\n"
          "   C scale       - Sets a point cloud scale on screen.\n"
          "\n"
          "* - Resizing the render window affects on the size of the screenshot.\n"
          "---------------------------------------------------------------------\n")
    
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
        print("Exiting.")
