import unittest
from fractal_parser import FractalParser

class TestFractalParser(unittest.TestCase):

    def setUp(self):
        # Set up any common configuration or objects needed for the tests
        pass

    def tearDown(self):
        # Clean up after each test case
        pass

    def test_parse_frac_file(self):
        # Create an instance of FractalParser
        parser_instance = FractalParser()

        # Test with a sample fractal file
        file_path = 'tests/mandelbrot.frac'
        testing_dict = parser_instance.parseFracFile(file_path)

        # Define expected key-value pairs based on the sample file content
        expected_dict = {'type': 'mandelbrot', 'pixels': '640', 'centerx': '0.0', 'centery': '0.0', 'axislength': '4.0', 'iterations': '100'}
        # Assert that the returned dictionary matches the expected dictionary
        self.assertDictEqual(testing_dict, expected_dict)

    # Add more test cases for different scenarios

if __name__ == '__main__':
    unittest.main()
