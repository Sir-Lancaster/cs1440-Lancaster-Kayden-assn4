#!/usr/bin/env python3
# Mandelbrot Set Visualizer

#              Copyright © 2023 DuckieCorp. All Rights Reserved.
#
#                       __      Redistribution and use of this code, with or
#                     /` ,\__   without modification, are permitted provided
#                    |    ).-'  that the following conditions are met:
#                   / .--'
#                  / /          0. Redistributions of this code must retain
#    ,      _.==''`  \             the above copyright notice, this list of
#  .'(  _.='         |             conditions and the following disclaimer.
# {   ``  _.='       |          1. The name of the author may not be used to
#  {    \`     ;    /              endorse or promote products derived from
#   `.   `'=..'  .='               this software without specific prior written
#     `=._    .='                  permission.
#  jgs  '-`\\`__                2. Neither the name of the University nor the
#           `-._{                  names of its contributors may be used to
#                                  endorse or promote products derived from
#                                  this software without specific prior written
#                                  permission.


import sys
import time
from tkinter import Tk, Canvas, PhotoImage, mainloop
import sys
import Palette as Colors

def PixelColorOrIndex(c, palette):
    """
    Return the color of the current pixel within the Mandelbrot set
    - OR -
    Return the INDEX of the color of the pixel within the Mandelbrot set
    The INDEX corresponds to the iteration count of the for loop.
    """
    zero = complex(0, 0)

    max_iterations = 115  # Adjust the maximum iterations if needed

    for iter in range(max_iterations if palette is None else len(palette)):
        zero = zero * zero + c

        if abs(zero) > 2:
            zero = float(2)
            return palette[min(iter, len(palette) - 1)] if palette is not None else iter
        elif abs(zero) > 7:
            print("You should never see this message in production", file=sys.stderr)
            break
        elif abs(zero) < 0:
            print(f"This REALLY should not have happened! zero={zero} iter={iter} MAX_ITERATIONS={max_iterations}", file=sys.stderr)
            sys.exit(1)

    if palette is not None:
        return palette[-1]  # Default color when the escape condition is not met
    else:
        return max_iterations - 1  # Default index when the escape condition is not met




def paint(fractals, imagename, window):
    fractal = fractals[imagename]

    minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)
    maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)
    miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)
    maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)
    
    img = PhotoImage(width=512, height=512)
    
    canvas = Canvas(window, width=512, height=512, bg='#000000')
    canvas.pack()
    canvas.create_image((256, 256), image=img, state="normal")

    pixelsize = abs(maxx - minx) / 512

    for row in range(512, 0, -1):
        cc = [
            PixelColorOrIndex(complex(minx + col * pixelsize, miny + row * pixelsize),
                              Colors.ultimate_palette if imagename != 'leaf' else None)
            for col in range(512)
        ]

        img.put('{' + ' '.join(cc) + '}', to=(0, 512 - row))
        window.update()
        print(pixelsWrittenSoFar(row, 512), end='\r', file=sys.stderr)


def pixelsWrittenSoFar(rows, cols):
    portion = (512 - rows) / 512
    pixels = (512 - rows) * 512
    status_percent = '{:>4.0%}'.format(portion)
    status_bar_width = 34
    status_bar = '=' * int(status_bar_width * portion)
    return ''.join(['[', status_percent, ' ', '{:<33}'.format(status_bar), ']'])



# These are the different views of the Mandelbrot set you can make with this
# program.
#
# For convenience I have placed these into a dictionary so you may easily
# switch between them by entering the name of the image you want to generate
# into the variable 'image'.
images = {
        'mandelbrot': {
            'centerX': -0.6,
            'centerY': 0.0,
            'axisLen': 2.5,
            },

        'mandelbrot-zoomed': {
            'centerX': -1.0,
            'centerY': 0.0,
            'axisLen': 1.0,
            },

        'spiral0': {
            'centerX': -0.761335372924805,
            'centerY': 0.0835704803466797,
            'axisLen': 0.004978179931102462,
            },

        'spiral1': {
            'centerX': -0.747,
            'centerY': 0.1075,
            'axisLen': 0.002,
            },

        'seahorse': {
            'centerX': -0.748,
            'centerY': -0.102,
            'axisLen': 0.008,
            },

        'spiral1': {
            'centerX': -0.747,
            'centerY': 0.1075,
            'axisLen': 0.002,
            },

        'elephants': {
            'centerX':  0.3015,
            'centerY':  -0.0200,
            'axisLen':  0.03,
            },

        'leaf': {
            'centerX': -1.543577002,
            'centerY': -0.000058690069,
            'axisLen':  0.000051248888,
            },

        'starfish': {
            'centerX': -0.463595023481762,
            'centerY': 0.598380871135558,
            'axisLen': 0.00128413675654471,
            },
        }


def mbrot_main(image):
    # Set up the GUI so that we can paint the fractal image on the screen
    print("Rendering {} fractal".format(image), file=sys.stderr)
    before = time.time()
    window = Tk()
    img = PhotoImage(width=512, height=512)
    paint(images, image, window)

    # Save the image as a PNG
    after = time.time()
    print(f"\nDone in {after - before:.3f} seconds!", file=sys.stderr)
    img.write(f"{image}.png")
    print(f"Saved image to file {image}.png", file=sys.stderr)

    # Call tkinter.mainloop so the GUI remains open
    print("Close the image window to exit the program", file=sys.stderr)
    mainloop()
