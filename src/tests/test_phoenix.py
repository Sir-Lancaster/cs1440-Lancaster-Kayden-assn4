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
from ImagePainter import getColorFromPalette, getFractalConfig
import FractalInformation
from Palette import ultimate_palette

# autocmd BufWritePost <buffer> !python3 runTests.py

class TestPhoenix(unittest.TestCase):
    def test_getColorFromPalette(self):
        """Phoenix fractal configuration and algorithm output the expected colors at key locations"""
        self.assertEqual(getColorFromPalette(complex(0, 0)), '#DBDE98')
        self.assertEqual(getColorFromPalette(complex(-0.751, 1.1075)), '#E0DC9C')
        self.assertEqual(getColorFromPalette(complex(-0.2, 1.1075)), '#DFDE9B')
        self.assertEqual(getColorFromPalette(complex(-0.750, 0.1075)), '#E0DA9E')
        self.assertEqual(getColorFromPalette(complex(-0.748, -0.1075)), '#E0DA9E')
        self.assertEqual(getColorFromPalette(complex(-0.75625, 0.078125)), '#E0DA9E')
        self.assertEqual(getColorFromPalette(complex(-0.75625, -0.234375)), '#E0DA9E')
        self.assertEqual(getColorFromPalette(complex(0.33749, -0.625)), '#487BB5')
        self.assertEqual(getColorFromPalette(complex(-0.678125, -0.46875)), '#E0DC9C')
        self.assertEqual(getColorFromPalette(complex(-0.406, -0.837)), '#57BFBF')
        self.assertEqual(getColorFromPalette(complex(-0.186, -0.685)), '#51A7BC')

    def test_dictionaryGetter(self):
        """Names of fractals in the configuration dictionary are as expected"""
        frac_info = FractalInformation.fractalinformation()
        self.assertIsNone(getFractalConfig(frac_info.images, 'absent'))
        self.assertIsNotNone(getFractalConfig(frac_info.images, 'phoenix'))
        self.assertIsNone(getFractalConfig(frac_info.images, ''))
        self.assertIsNotNone(getFractalConfig(frac_info.images, 'peacock'))
        self.assertIsNone(getFractalConfig(frac_info.images, 'Still Not In Here'))
        self.assertIsNotNone(getFractalConfig(frac_info.images, 'monkey-knife-fight'))
        self.assertIsNone(getFractalConfig(frac_info.images, 'shrimp-coctail'))
        self.assertIsNotNone(getFractalConfig(frac_info.images, 'shrimp-cocktail'))

    def test_gradientLength(self):
        """Color palette contains the expected number of colors"""
        self.assertEqual(213, len(ultimate_palette))


if __name__ == '__main__':
    unittest.main()
