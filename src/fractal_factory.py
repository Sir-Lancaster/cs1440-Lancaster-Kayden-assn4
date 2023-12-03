import fractal

class FractalFactory:
    def makeFractal(self, Fractal_name='mandelbrot'):

        if Fractal_name == "mandelbrot":
            Fractal_options = fractal.Mandelbrot()
            return Fractal_options.count
        
        elif Fractal_name == "phoenix":
            Fractal_options = fractal.Phoenix()
            return Fractal_options.count     
        
        elif Fractal_name == "julia":
            Fractal_options = fractal.JuliaSet(complex(-0.7, 0.27015))
            return Fractal_options.count     
        
        elif Fractal_name == "spider":
            Fractal_options = fractal.Spider()
            return Fractal_options.count     
        
        else:
            raise NotImplementedError("Invalid Fractal requested")