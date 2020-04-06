# Point Cloud to GIF

## Table of contents
- [What is it?](#what-is-it)
- [Gallery](#gallery)
- [Installation](#installation)
- [Usage](#usage)
    - [Command list](#command-list)
    - [About input files](#about-input-files)
        - [Supported file format](#supported-file-format)
        - [Generating point clouds](#generating-point-clouds)
    - [About output files](#about-output-files)
        - [Change output size](#change-output-size)
        - [GIF compression](#gif-compression)
        - [GIF modifying](#gif-modifying)
## What is it?
**Point Cloud to GIF** is a simple program which allows you to render plain text XYZ point clouds and save them to PNG files or create a rotating GIF animation. This piece of software was created primarily as part of Scan&Print - the project of a device which scans real physical objects, generates a point cloud from them and prepare 3D prinable files.

The program bases on really naive algorithms for manipulating point clouds so every action on big clouds may take some time. It's not a professional software but a hobby project for creating nice GIFs ;)

## Gallery
<p align="center">
    <img src="examples/cube.png">
    <img src="examples/roller.gif">
    <img src="examples/test.gif">
    <img src="examples/dsonyy.png">
    <img src="examples/marszalek.gif">
    <img src="examples/bag.gif">
</p>
The point clouds from the last row are part of Scan&Print project!

## Installation
1. Install Python 3.
2. Install Python dependencies from `requirements.txt`.
3. Run `pc2gif.py`.

**Optional:** This program can use *gifsicle* software for compressing GIF files before export. It's not required but reduces output files size. You can get binaries for many operating systems from the project website: https://www.lcdf.org/gifsicle/. To be detected, `gifsicle` executable must be added to your system global path.

## Usage
If you execute *pc2gif*, you will see something like internal command prompt. Below you can read more about how to use it.

### Command list
Parameters between `(` and `)` are optional.

```
   Load filename            - Loads a point cloud from file.
   Move x (y)               - Moves a point cloud on the screen.
   Rotate x (y)(z)          - Rotates a point cloud around X, Y, Z axis. Specify angle in degrees.
   Save (filename)          - Saves a PNG file with the screen content.
   sCale scale              - Sets a point cloud scale on the screen.
   Gif (filaname) (frames)  - Saves a GIF file with an animation of rotating a point cloud around Y axis.
```

**Note:** You can use a single (highlighted by uppercase above) letter instead of full command name e.g.
```
    R 33.3 33.3
    C 2.5
    S export.png
```

### About input files

#### Supported file format
This is an example of valid input point cloud:
```
0.90688896 ; 0.13263926 ; -5.49270248
0.01431680 ; 0.15915152 ; -5.49270248
1.47087491 ; 0.22544102 ; -5.49270248
1.35835743 ; 0.46180943 ; -5.49270248
0.47499299 ; 0.13312708 ; -5.49270248
1.82343197 ; 0.70383137 ; -5.49270248
1.96170413 ; 0.30591235 ; -5.49270248
...
```
- There must be only one XYZ point per line.
- Coordinates must be separated by `;`.
- Floating point numbers are allowed.
- Points may be unsorted.

#### Generating point clouds
You can easily generate such a file using for example [CloudCompare software](https://www.danielgm.net/cc/) and  [Points Sampling on mesh](http://www.cloudcompare.org/doc/wiki/index.php?title=Mesh%5CSample_points) tool.

### About output files

#### Change output size
resize the render window manually to change the default size of your output files.

#### GIF compression
By default, *pc2gif* exports uncompressed GIF file. You can install `gifsicle` software to automatically compress export files. Read more in [Installation section](#installation).

#### GIF modifying
If you want to modify your GIF you can use [ezgif.com website](https://ezgif.com/).
