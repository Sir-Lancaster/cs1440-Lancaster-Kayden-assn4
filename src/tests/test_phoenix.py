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
from phoenix_fractal import getColorFromPalette, grad, WHITE, f
from phoenix_fractal import getFractalConfigurationDataFromFractalRepositoryDictionary


# autocmd BufWritePost <buffer> !python3 runTests.py

class TestPhoenix(unittest.TestCase):
    def test_getColorFromPalette(self):
        """Phoenix fractal configuration and algorithm output the expected colors at key locations"""
        self.assertEqual(getColorFromPalette(complex(0, 0)), '#ffeca5')
        self.assertEqual(getColorFromPalette(complex(-0.751, 1.1075)), '#ffe4b5')
        self.assertEqual(getColorFromPalette(complex(-0.2, 1.1075)), '#ffe5b2')
        self.assertEqual(getColorFromPalette(complex(-0.750, 0.1075)), '#86ff4a')
        self.assertEqual(getColorFromPalette(complex(-0.748, -0.1075)), '#002277')
        self.assertEqual(getColorFromPalette(complex(-0.75625, 0.078125)), '#002277')
        self.assertEqual(getColorFromPalette(complex(-0.75625, -0.234375)), '#94ff51')
        self.assertEqual(getColorFromPalette(complex(0.33749, -0.625)), '#ffe7af')
        self.assertEqual(getColorFromPalette(complex(-0.678125, -0.46875)), '#002277')
        self.assertEqual(getColorFromPalette(complex(-0.406, -0.837)), '#ffe5b2')
        self.assertEqual(getColorFromPalette(complex(-0.186, -0.685)), '#ffe7af')

    def test_dictionaryGetter(self):
        """Names of fractals in the configuration dictionary are as expected"""
        self.assertIsNone(getFractalConfigurationDataFromFractalRepositoryDictionary(f, 'absent'))
        self.assertIsNotNone(getFractalConfigurationDataFromFractalRepositoryDictionary(f, 'phoenix'))
        self.assertIsNone(getFractalConfigurationDataFromFractalRepositoryDictionary(f, ''))
        self.assertIsNotNone(getFractalConfigurationDataFromFractalRepositoryDictionary(f, 'peacock'))
        self.assertIsNone(getFractalConfigurationDataFromFractalRepositoryDictionary(f, 'Still Not In Here'))
        self.assertIsNotNone(getFractalConfigurationDataFromFractalRepositoryDictionary(f, 'monkey-knife-fight'))
        self.assertIsNone(getFractalConfigurationDataFromFractalRepositoryDictionary(f, 'shrimp-coctail'))
        self.assertIsNotNone(getFractalConfigurationDataFromFractalRepositoryDictionary(f, 'shrimp-cocktail'))

    def test_gradientLength(self):
        """Color palette contains the expected number of colors"""
        self.assertEqual(108, len(grad))


if __name__ == '__main__':
    unittest.main()
