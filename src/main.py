#!/usr/bin/env python3

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

from image_painter import ImagePainter
import fractal_factory
import palettefactory
import fractal_parser
# fractal factory will call the correct subclass in Fractal that will give you count
# fractal parser will give you the dictionary contaning the fractal. 
# palette factory will call the correct palette defined in Palette classes. 

# create some class instances here:
frac_factory = fractal_factory.FractalFactory()
frac_parse = fractal_parser.FractalParser()
Pal_factory = palettefactory.PaletteFactory()

# body:
if len(sys.argv) == 2:                                              # if the User provides a fractal name but not a palette name.
    name = sys.argv[1]
    frac_name = sys.argv[1].strip('data/').strip('.frac')
    count = frac_factory.makeFractal(Fractal_name=frac_name)
    fractal = frac_parse.parseFracFile(file_path=name)
    iterations = int(fractal.get('iterations'))
    currentPalette = Pal_factory.makePalette(iterations)

elif len(sys.argv) == 3:                                            # if the user provides both a fractal name and a palette name. 
    name = sys.argv[1]
    frac_name = sys.argv[1].strip('data/').strip('.frac')           # note to self: this line is not needed on the 'else' section.
    count = frac_factory.makeFractal(Fractal_name=frac_name)    
    fractal = frac_parse.parseFracFile(name)
    pal_Name = sys.argv[2]
    currentPalette = Pal_factory.makePalette(palette_name=pal_Name)
else:
    name = 'mandelbrot'
    count = frac_factory.makeFractal(0+0j) - 1
    print(count)
    fractal = frac_parse.parseFracFile()
    currentPalette = Pal_factory.makePalette(513)
    print(len(currentPalette))

genFractal = ImagePainter(fractal, name, count, currentPalette)
genFractal.paint()