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


import unittest
from ImagePainter import pixelsWrittenSoFar, PixelColorOrIndex
from Palette import palette

# autocmd BufWritePost <buffer> !python3 runTests.py

class TestMandelbrot(unittest.TestCase):
    def test_pixelColorOrIndex(self):
        """Mandelbrot fractal configuration and algorithm output the expected colors at key locations"""
        # test the pixel color...
        self.assertEqual(PixelColorOrIndex(complex(0, 0), palette), '#7D387D')
        self.assertEqual(PixelColorOrIndex(complex(-0.751, 1.1075), palette), '#E0DC9C')
        self.assertEqual(PixelColorOrIndex(complex(-0.2, 1.1075), palette), '#CDDC93')
        self.assertEqual(PixelColorOrIndex(complex(-0.75, 0.1075), palette), '#79D078')
        self.assertEqual(PixelColorOrIndex(complex(-0.748, 0.1075), palette), '#59C0BD')
        self.assertEqual(PixelColorOrIndex(complex(-0.7562500000000001, 0.078125), palette), '#6ECB8A')

        # ...or Index
        self.assertEqual(12, PixelColorOrIndex(complex(-0.7562500000000001, -0.234375), None))
        self.assertEqual(10, PixelColorOrIndex(complex(0.3374999999999999, -0.625), None))
        self.assertEqual(29, PixelColorOrIndex(complex(-0.6781250000000001, -0.46875), None))
        self.assertEqual(4,  PixelColorOrIndex(complex(0.4937499999999999, -0.234375), None))
        self.assertEqual(22, PixelColorOrIndex(complex(0.3374999999999999, 0.546875), None))

    def test_pixelsWrittenSoFar(self):
        """Progress bar produces correct output"""
        self.assertEqual(pixelsWrittenSoFar(1, 600), '[100% =================================]')
        self.assertEqual(pixelsWrittenSoFar(7, 7), '[ 99% =================================]')
        self.assertEqual(pixelsWrittenSoFar(257, 321), '[ 50% ================                 ]')
        self.assertEqual(pixelsWrittenSoFar(256, 256), '[ 50% =================                ]')
        self.assertEqual(pixelsWrittenSoFar(100, 100), '[ 80% ===========================      ]')
        self.assertEqual(pixelsWrittenSoFar(640, 480), '[-25%                                  ]')
        self.assertEqual(pixelsWrittenSoFar(137, 1000), '[ 73% ========================         ]')
        self.assertEqual(pixelsWrittenSoFar(512, 0), '[  0%                                  ]')

    def test_palleteLength(self):
        """Palette contains the expected number of colors"""
        self.assertEqual(111, len(palette))
    
    def test_pallete_type(self):                                            # one of my tests
        """Palette contains only strings."""
        self.assertTrue(all(isinstance(color, str) for color in palette))


if __name__ == '__main__':
    unittest.main()
