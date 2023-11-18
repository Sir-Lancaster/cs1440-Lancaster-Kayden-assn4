#!/usr/bin/env python3
# Phoenix Fractal Visualizer - a variation of the Julia Fractal

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


# These are the imports that I usually import
import sys
import time

# these ones are the ones that i'm using in this program
from tkinter import Tk, Canvas, PhotoImage, mainloop
from time import time
import Palette


SPC = chr(0o40)  # octal number
s = 512

def getColorFromPalette(z):
    """
    Return the index of the color of the current pixel
    within the Phoenix fractal in the palette array
    """
    c = complex(0.5667, 0.0)
    pheonix = complex(-0.5, 0.0)
    z = complex(z.imag, z.real)  # Reflect the components

    zPrev = 0 + 0j
    for i in range(102):
        z, zPrev = z * z + c + (pheonix * zPrev), z  # Update Z and prevZ

        if abs(z) > 2:
            return Palette.ultimate_palette[i]  # The sequence is unbounded
    return Palette.ultimate_palette[101]



def getFractalConfigurationDataFromFractalRepositoryDictionary(dictionary, name):
    """Make sure that the fractal configuration data repository dictionary
    contains a key by the name of 'name'

    When the key 'name' is present in the fractal configuration data repository
    dictionary, return its value.

    Return False otherwise
    """
    for key in dictionary:
        if key in dictionary:
            if key == name:
                value = dictionary[key]
                return key


Save_As_Picture = True
tkPhotoImage = None

def makePictureOfFractal(f, s, W, p, win):
    min_coord = (f['centerX'] - f['axisLength'] / 2.0, f['centerY'] - f['axisLength'] / 2.0)
    max_coord = (f['centerX'] + f['axisLength'] / 2.0, f['centerY'] + f['axisLength'] / 2.0)

    canvas = Canvas(win, width=s, height=s, bg=W)
    canvas.pack()
    canvas.create_image((s/2, s/2), image=p, state="normal")

    size = abs(max_coord[0] - min_coord[0]) / s

    for row in range(s, 0, -1):
        pixels = []
        for col in range(s):
            X = min_coord[0] + col * size
            Y = min_coord[1] + row * size
            cp = getColorFromPalette(complex(X, Y))
            pixels.append(cp)

        pixls = '{' + ' '.join(pixels) + '}'
        p.put(pixls, (0, s - row))
        win.update()

        fraction_written = (s - row) / s
        status_bar = '=' * int(34 * fraction_written)
        print(f"[{fraction_written:>4.0%}{' ' * 33}{status_bar}]", end="\r", file=sys.stderr)




# This dictionary contains the different views of the Phoenix set you can make
# with this program.

# TODO: Maybe it would be a good idea to incorporate the complex value `c` into
# this configuration dictionary instead of hardcoding it into this program.
# But I don't have time for this right now, too busy.  I'll just keep doing it
# the way I know how.
f = {
        # The full Phoneix set
        'phoenix': {
            'centerX':     0.0,
            'centerY':     0.0,
            'axisLength':  3.25,
            },

        # This one looks like a peacock's tail to me
        'peacock': {
            'centerX':     -0.363287878200906,
            'centerY':     0.381197981824009,
            'axisLength':  0.0840187115019564,
        },

        # Two or more monkeys having a scuffle
        'monkey-knife-fight': {
            'centerX':    -0.945542168674699,
            'centerY':    0.232234726688103,
            'axisLength': 0.136626506024096,
            },

        # This one makes me hungry to look at
        'shrimp-cocktail': {
            'centerX': 0.529156626506024,
            'centerY': -0.3516077170418,
            'axisLength': 0.221204819277108,
            },
        }


WHITE = '#ffffff'
RED = '#ff0000'  
BLUE = '#00ff00' 
GREEN = '#0000ff'
BLACK = '#000000'
ORANGE = '#ffa50'
TOMATO = '#ff6347'  
HOT_PINK = '#ff69b4'  
REBECCA_PURPLE = '#663399'  
LIME_GREEN = '#89ff00'  
GREY0 = '#000000'  
GRAY37 = '#5e5e5e' 
GREY74 = '#bdbdbd'  
GRAY99 = '#fcfcfc'  


def phoenix_main(i):
    """The main entry-point for the Phoenix fractal generator"""

    # the size of the image we will create is 512x512 pixels
    s = 512

    # Note the time of when we started so we can measure performance improvements
    b4 = time()
    # Set up the GUI so that we can display the fractal image on the screen
    win = Tk()

    print("Rendering %s fractal" % i, file=sys.stderr)
    tkPhotoImage = PhotoImage(width=s, height=s)
    makePictureOfFractal(f[i], s, GREY0, tkPhotoImage, win)
    if Save_As_Picture:
        tkPhotoImage.write(i + ".png")
        print(f"\nDone in {time() - b4:.3f} seconds!", file=sys.stderr)

    if Save_As_Picture:
        tkPhotoImage.write(f"{i}.png")
        print("Saved image to file " + i + ".png", file=sys.stderr)

    print("Close the image window to exit the program", file=sys.stderr)
    # Call tkinter.mainloop so the GUI remains open
    mainloop()


