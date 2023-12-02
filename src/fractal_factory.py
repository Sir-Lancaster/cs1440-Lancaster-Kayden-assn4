import fractal

class FractalFactory:
    def makeFractal(self, n, m, Fractal_name='mandelbrot'):

        if Fractal_name == "mandelbrot":
            Fractal_options = fractal.Mandelbrot()
            return Fractal_options.count
        
        elif Fractal_name == "phoenix":
            Fractal_options = fractal.Phoenix()
            return Fractal_options.count     
        
        elif Fractal_name == "nigtmareFractal":
            Fractal_options = fractal.NightmareFractal()
            return Fractal_options.count     
        
        elif Fractal_name == "theBigCheese":
            Fractal_options = fractal.TheBigCheese()
            return Fractal_options.count     
        
        else:
            raise NotImplementedError("Invalid Fractal requested")