class Fractal:
    def init(self):
        pass
    def count(self):
        raise NotImplementedError("Concrete subclass of Palette must implement getColor() method")  # copied from 4.1 Requirements

class Mandelbrot(Fractal):
   def count(self, c, end):
        z = complex(0, 0)  # z0
        for i in range(end):
            z = z * z + c  # Get z1, z2, ...
            if abs(z) > 2.0:
                return i
        return end

class Phoenix(Fractal):
    def count(self, z, end):
        """
        Return the iteration count for a point on the complex plane `c`
        to guess whether it is in the Phoenix set (bounded by `end`)
        """

        # Julia Constant
        c = complex(0.5667, 0.0)

        # Phoenix Constant
        p = complex(-0.5, 0.0)

        # The first thing we do to the complex number Z is reflect its components,
        # so the imaginary part becomes the real part, and vice versa.
        # If we don't do this, the image comes out SIDEWAYS!!!
        z = complex(z.imag, z.real)

        # zPrevious is the PREVIOUS Z value, except the 1st time through the
        # function, when it starts out as Complex Zero (which is actually the
        # same thing as REAL Zero 0)  MATH IS BEAUTIFUL!
        zPrev = 0+0j

        for i in range(end):
            zSave = z
            z = z * z + c + (p * zPrev)
            if abs(z) > 2:
                return i
            zPrev = zSave  # Set the prevZ value for the next iteration
        return end

class NightmareFractal(Fractal):
    def count(self, c):
        # Your custom fractal formula implementation
        z = 0
        max_iterations = 900
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

    iterations = mandelbrot_instance.count(0+0j)
    print(f'Mandelbrot iterations for: {iterations}')

