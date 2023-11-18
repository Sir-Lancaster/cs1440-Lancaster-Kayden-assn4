import sys
import time
from tkinter import Tk, Canvas, PhotoImage, mainloop
import sys
import Palette
import FractalInformation
import Mandelbrot
import Phoenix

frac_info = FractalInformation.fractalinformation() 


def paint(fractals, imagename, window, img):     # Used for Mandelbrot fractals
    
    fractal = fractals[imagename]

    minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)
    maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)
    miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)
    maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)

    canvas = Canvas(window, width=512, height=512, bg='#000000')
    canvas.pack()
    canvas.create_image((256, 256), image=img, state="normal")

    pixelsize = abs(maxx - minx) / 512

    for row in range(512, 0, -1):
        cc = [PixelColorOrIndex(complex(minx + col * pixelsize, miny + row * pixelsize), Palette.ultimate_palette)
            for col in range(512)]

        img.put('{' + ' '.join(cc) + '}', to=(0, 512 - row))
        window.update()
        print(pixelsWrittenSoFar(row, 512), end='\r', file=sys.stderr)

def makePictureOfFractal(f, s, W, p, win):          # Used for phoenix fractals.
    min_coord = (f['centerX'] - f['axisLen'] / 2.0, f['centerY'] - f['axisLen'] / 2.0)
    max_coord = (f['centerX'] + f['axisLen'] / 2.0, f['centerY'] + f['axisLen'] / 2.0)

    canvas = Canvas(win, width=s, height=s, bg=W)
    canvas.pack()
    canvas.create_image((s/2, s/2), image=p, state="normal")

    size = abs(max_coord[0] - min_coord[0]) / s

    for row in range(s, 0, -1):
        pixels = []
        for col in range(s):
            X = min_coord[0] + col * size
            Y = min_coord[1] + row * size
            cp = getColorFromPalette(complex(X, Y))
            pixels.append(cp)

        pixls = '{' + ' '.join(pixels) + '}'
        p.put(pixls, (0, s - row))
        win.update()

        fraction_written = (s - row) / s
        status_bar = '=' * int(34 * fraction_written)
        print(f"[{fraction_written:>4.0%}{' ' * 33}{status_bar}]", end="\r", file=sys.stderr)
        
def pixelsWrittenSoFar(rows, cols):
    portion = (512 - rows) / 512
    pixels = (512 - rows) * 512
    status_percent = '{:>4.0%}'.format(portion)
    status_bar_width = 34
    status_bar = '=' * int(status_bar_width * portion)
    return ''.join(['[', status_percent, ' ', '{:<33}'.format(status_bar), ']'])

def PixelColorOrIndex(c, palette):
    """
    Return the color of the current pixel within the Mandelbrot set
    - OR -
    Return the INDEX of the color of the pixel within the Mandelbrot set
    The INDEX corresponds to the iteration count of the for loop.
    """
    zero = complex(0, 0)

    max_iterations = 115  # Adjust the maximum iterations if needed

    for iter in range(max_iterations if palette is None else len(palette)):
        zero = zero * zero + c

        if abs(zero) > 2:
            zero = float(2)
            return palette[min(iter, len(palette) - 1)] if palette is not None else iter
        elif abs(zero) > 7:
            print("You should never see this message in production", file=sys.stderr)
            break
        elif abs(zero) < 0:
            print(f"This REALLY should not have happened! zero={zero} iter={iter} MAX_ITERATIONS={max_iterations}", file=sys.stderr)
            sys.exit(1)

    if palette is not None:
        return palette[-1]  # Default color when the escape condition is not met
    else:
        return max_iterations - 1  # Default index when the escape condition is not met
    
def getColorFromPalette(z):
    c = complex(0.5667, 0.0)
    phoenix_constant = complex(-0.5, 0.0)

    # Reflect the components of the complex number z
    z_flipped = complex(z.imag, z.real)

    # Initialize the previous Z value
    z_prev = 0 + 0j

    # Iterate over the range of colors in the palette
    for i in range(101):
        z_save = z  # Save the current Z value before overwriting it
        z = z * z + c + (phoenix_constant * z_prev)
        z_prev = z_save  # Set the prevZ value for the next iteration

        if abs(z) > 2:
            return Palette.ultimate_palette[i]  # The sequence is unbounded

    return Palette.ultimate_palette[101]


def phoenix_main(imagename):
    """The main entry-point for the Phoenix fractal generator"""
    Save_As_Picture = True
    size_of_image = 512
    before = time.time()
    window = Tk()
    Background = Palette.BLACK
    tkPhotoImage = PhotoImage(width=size_of_image, height=size_of_image)

    print("Rendering %s fractal" % imagename, file=sys.stderr)
    
    makePictureOfFractal(frac_info.images[imagename], size_of_image, Background, tkPhotoImage, window)
    if Save_As_Picture:
        tkPhotoImage.write(imagename + ".png")
        print(f"\nDone in {time.time() - before:.3f} seconds!", file=sys.stderr)
        tkPhotoImage.write(f"{imagename}.png")
        print("Saved image to file " + imagename + ".png", file=sys.stderr)

    coordinate = complex(-0.5, 0.0)  
    iteration_count = Mandelbrot.mandelbrot_Count(coordinate)
    print(f"For coordinate {coordinate}, Mandelbrot iteration count: {iteration_count}")
    
    print("Close the image window to exit the program", file=sys.stderr)
    mainloop()
    
def mbrot_main(image):
    Save_As_Picture = True
    before = time.time()
    window = Tk()
    img = PhotoImage(width=512, height=512)
    images = frac_info.images
    print("Rendering %s fractal" % image, file=sys.stderr)

    paint(images, image, window, img)
    if Save_As_Picture:
        img.write(image + ".png")
        print(f"\nDone in {time.time() - before:.3f} seconds!", file=sys.stderr)
        img.write(f"{image}.png")
        print("Saved image to file " + image + ".png", file=sys.stderr)

    coordinate = complex(-0.5, 0.0)  
    iteration_count = Mandelbrot.mandelbrot_Count(coordinate)

    print(f"For coordinate {coordinate}, Mandelbrot iteration count: {iteration_count}")

    print("Close the image window to exit the program", file=sys.stderr)
    mainloop()

if __name__ == '__main__':
    # To test phoenix fractals uncomment the line below and replace imagename with the desired fractal.
    # phoenix_main('phoenix')    
    
    # To test mandelbrot fractals uncomment the line below and replace imagename with the desired fractal.
    mbrot_main('starfish')