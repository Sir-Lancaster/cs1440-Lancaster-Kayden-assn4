import unittest

from fractal import Fractal, Mandelbrot, Phoenix, JuliaSet, Spider

class TestFractals(unittest.TestCase):
    def test_mandelbrot(self):
        mandelbrot_instance = Mandelbrot()
        iterations = mandelbrot_instance.count(0+0j, 100)
        self.assertIsInstance(iterations, int)
        # Add more specific assertions based on the expected behavior

    def test_phoenix(self):
        phoenix_instance = Phoenix()
        iterations = phoenix_instance.count(0+0j, 100)
        self.assertIsInstance(iterations, int)
        # Add more specific assertions based on the expected behavior

    def test_julia_set(self):
        julia_set_instance = JuliaSet(0.5 + 0.5j)
        iterations = julia_set_instance.count(0+0j, 100)
        self.assertIsInstance(iterations, int)
        # Add more specific assertions based on the expected behavior

    def test_spider(self):
        spider_instance = Spider()
        iterations = spider_instance.count(0+0j, 100)
        self.assertIsInstance(iterations, int)
        # Add more specific assertions based on the expected behavior

if __name__ == '__main__':
    unittest.main()
