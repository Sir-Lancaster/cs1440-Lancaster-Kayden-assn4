class Fractal:
    def init(self):
        pass
    def count(self):
        raise NotImplementedError("Concrete subclass of Palette must implement getColor() method")  # copied from 4.1 Requirements

class Mandelbrot(Fractal):
    def count(self, c):
        z = 0
        max_iterations = 513   
        for i in range(max_iterations):
            z = z * z + c
            if abs(z) > 2.0:
                return i
        return max_iterations

class Phoenix(Fractal):
    def count(self, c):
        z = 0
        max_iterations = 640
        for i in range(max_iterations):
            z = z * z + c.conjugate()
            if abs(z) > 2.0:
                return i
        return max_iterations

class NightmareFractal(Fractal):
    def count(self, c):
        # Your custom fractal formula implementation
        z = 0
        max_iterations = 2000
        for i in range(max_iterations):
            z = z * z + c
            if abs(z) > 3.0:
                return i
        return max_iterations

class TheBigCheese(Fractal):
    def count(self, c):
        # Another custom fractal formula implementation
        z = 0
        max_iterations = 1500
        for i in range(max_iterations):
            z = z * z + c
            if abs(z) > 2.5:
                return i
        return max_iterations

# Example usage with Mandelbrot fractal
mandelbrot_instance = Mandelbrot()
complex_number = 1 + 2j
iterations = mandelbrot_instance.count(complex_number)
print(f'Mandelbrot iterations for {complex_number}: {iterations}')

# Similar usage with other fractal classes
phoenix_instance = Phoenix()
nightmare_instance = NightmareFractal()
the_big_cheese_instance = TheBigCheese()

iterations_phoenix = phoenix_instance.count(complex_number)
iterations_nightmare = nightmare_instance.count(complex_number)
iterations_big_cheese = the_big_cheese_instance.count(complex_number)

print(f'Phoenix iterations: {iterations_phoenix}')
print(f'NightmareFractal iterations: {iterations_nightmare}')
print(f'TheBigCheese iterations: {iterations_big_cheese}')
