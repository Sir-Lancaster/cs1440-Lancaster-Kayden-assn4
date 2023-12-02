import unittest
from Palette import Palette, BurningGold, MorningsTwilight

class TestPalette(unittest.TestCase):

    def test_palette_abstract_method(self):
        # Attempt to create an instance of the abstract base class
        with self.assertRaises(NotImplementedError):
            palette = Palette()
            palette.getColor(5)

    def test_burning_gold_palette(self):
        # Test the getColor method of BurningGold palette
        palette = BurningGold()
        colors = palette.getColor(5)

        # Check if the returned value is a list
        self.assertIsInstance(colors, list)

        # Check if the list has the correct number of elements
        self.assertEqual(len(colors), 5)

        # Check if each element in the list is a string representing a color hex code
        for color in colors:
            self.assertIsInstance(color, str)
            self.assertTrue(color.startswith('#'))

    def test_mornings_twilight_palette(self):
        # Test the getColor method of MorningsTwilight palette
        palette = MorningsTwilight()
        colors = palette.getColor(7)

        # Check if the returned value is a list
        self.assertIsInstance(colors, list)

        # Check if the list has the correct number of elements
        self.assertEqual(len(colors), 7)

        # Check if each element in the list is a string representing a color hex code
        for color in colors:
            self.assertIsInstance(color, str)
            self.assertTrue(color.startswith('#'))

if __name__ == '__main__':
    unittest.main()
