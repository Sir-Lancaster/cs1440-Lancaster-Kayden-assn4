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

import Palette
import mandelbrot
import phoenix
from fractal_information import FRACTALS
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
if len(sys.argv) == 2:
    name = sys.argv[1]
    frac_name = sys.argv[1].strip('data/').strip('.frac')
    count = frac_factory.makeFractal(Fractal_name=frac_name)
    fractal = frac_parse.parseFracFile(name)
else:
    frac_factory.makeFractal()


genFractal = ImagePainter(fractal, name, count, currentPalette)
genFractal.paint()