class FractalParser:
    def parseFracFile(self, file_path='data/phoenix.frac'):
        # Dictionary to store the parsed parameters
        fractal_dict = {}

        with open(file_path, 'r') as file:
            for line in file:
                # Strip whitespace and convert to lowercase
                line = line.strip().lower()

                # Skip comments and blank lines
                if line.startswith('#') or not line:
                    continue

                # Split the line into key and value
                key, value = map(str.strip, line.split(':', 1))

                # Store the key-value pair in the dictionary
                fractal_dict[key] = value


        return fractal_dict
    

if __name__ == '__main__':
    parser_instance = FractalParser()
    testingDict = parser_instance.parseFracFile()
    print(testingDict)