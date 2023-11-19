import unittest
import FractalInformation

class TestFractalInformation(unittest.TestCase):
    def test_fractal_configuration_keys_and_types(self):
        fractals = FractalInformation.fractalinformation()

        fractal_information = fractals.images

        for fractal_name, fractal_config in fractal_information.items():
            with self.subTest(fractal_name=fractal_name):
                # Define expected keys and types for each fractal
                if fractal_name in ['mandelbrot', 'mandelbrot-zoomed', 'spiral0', 'spiral1']:
                    expected_keys = ['centerX', 'centerY', 'axisLen']
                    expected_types = {'centerX': float, 'centerY': float, 'axisLen': float}
                else:
                    expected_keys = ['centerX', 'centerY', 'axisLen']
                    expected_types = {'centerX': float, 'centerY': float, 'axisLen': float}

                # Check if all expected keys are present in the dictionary
                self.assertCountEqual(expected_keys, fractal_config.keys())

                # Check if the corresponding values are of the expected types
                for key, expected_type in expected_types.items():
                    self.assertIn(key, fractal_config)
                    self.assertIsInstance(fractal_config[key], expected_type)

if __name__ == '__main__':
    unittest.main()
