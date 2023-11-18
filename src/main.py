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
import mbrot_fractal
import phoenix_fractal as phoenix
from phoenix_fractal import f as phoenix_fractals
import FractalInformation
import ImagePainter

MBROTS = [
        'elephants',
        'leaf',
        'mandelbrot',
        'mandelbrot-zoomed',
        'seahorse',
        'spiral0', 
        'spiral1', 
        'starfish'
        ]

PHOENX =[]
for p in  phoenix_fractals.keys():
    PHOENX=PHOENX+[p]

if len(sys.argv) < 2:
    print("Please provide the name of a fractal as an argument.")
    print("Available Fractals:")
    for fractal in PHOENX + MBROTS:
        print("\t{}".format(fractal))
    sys.exit(1)

fractal_name = sys.argv[1]

if fractal_name not in PHOENX and fractal_name not in MBROTS:
    print("ERROR: {} is not a valid fractal.".format(fractal_name))
    print("Phoenix Fractals:", ", ".join(PHOENX))
    print("Mandelbrot Fractals:", ", ".join(MBROTS))
    sys.exit(1)

if sys.argv[1] not in PHOENX and sys.argv[1] not in MBROTS:
    print("ERROR:", sys.argv[1], "is not a valid fractal")
    print("Please choose one of the following:")
    print("Phoenix Fractals:")
    for fractal in PHOENX:
        print("\t%s" % fractal)
    print("Mandelbrot Fractals:")
    for fractal in MBROTS:
        print("\t%s" % fractal)
    print("Those are all of the choices")
    sys.exit(1)

if sys.argv[1] in PHOENX:
    phoenix.phoenix_main(sys.argv[1])
elif sys.argv[1] in MBROTS:
    mbrot_fractal.mbrot_main(sys.argv[1])
else:
    print("The fractal given on the command line", sys.argv[1], "was not found in the command line")
