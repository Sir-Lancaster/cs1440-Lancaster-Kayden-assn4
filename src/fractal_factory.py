import fractal

class FractalFactory:
    def makeFractal(self, Fractal_name='Mandelbrot'):

        if Fractal_name == "Mandelbrot":
            Fractal_options = fractal.Mandelbrot()
            return Fractal_options.count()
        
        elif Fractal_name == "Phoenix":
            Fractal_options = fractal.Phoenix()
            return Fractal_options.count()     
        
        elif Fractal_name == "NigtmareFractal":
            Fractal_options = fractal.NightmareFractal()
            return Fractal_options.count()     
        
        elif Fractal_name == "TheBigCheese":
            Fractal_options = fractal.TheBigCheese()
            return Fractal_options.count()     
        
        else:
            raise NotImplementedError("Invalid Fractal requested")