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
            if abs(z) > 2.0:
                return i
        return max_iterations

class TheBigCheese(Fractal):
    def count(self, c):
        # Another custom fractal formula implementation
        z = 0
        max_iterations = 1500
        for i in range(max_iterations):
            z = z * z + c
            if abs(z) > 2.0:
                return i
        return max_iterations

if __name__ == '__main__':    
    # Example usage with Mandelbrot fractal
    mandelbrot_instance = Mandelbrot()

    iterations = mandelbrot_instance.count
    print(f'Mandelbrot iterations for: {iterations}')

