import sys
import time
from tkinter import Tk, Canvas, PhotoImage, mainloop
import sys
import Palette
import FractalInformation
import Mandelbrot
import Phoenix



def paint(fractals, imagename, window, img):     # Use for Mandelbrot fractals
    
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
        cc = [PixelColorOrIndex(complex(minx + col * pixelsize, miny + row * pixelsize), Palette.palette)
            for col in range(512)]

        img.put('{' + ' '.join(cc) + '}', to=(0, 512 - row))
        window.update()
        print(pixelsWrittenSoFar(row, 512), end='\r', file=sys.stderr)

def makePictureOfFractal(f, p, w, s):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    Assumes the image is 640x640 pixels."""

    # Compute the minimum and maximum coordinates of the picture
    min_x = f['centerX'] - (f['axisLen'] / 2.0)
    min_y = f['centerY'] - (f['axisLen'] / 2.0)
    max_x = f['centerX'] + (f['axisLen'] / 2.0)
    max_y = f['centerY'] + (f['axisLen'] / 2.0)

    # Display the image on the screen
    tk_interface_canvas = Canvas(w, width=s, height=s, bg="white")
    tk_interface_canvas.pack()

    # Create the TK PhotoImage object that backs the Canvas Object
    tk_interface_canvas.create_image((s/2, s/2), image=p, state="normal")
    tk_interface_canvas.pack()

    # Compute the size of one pixel in the imaginary plane
    size = abs(max_x - min_x) / s

    # Iterate over rows and columns to fill the image
    for r in range(s, 0, -1):
        row_colors = [getColorFromPalette(complex(min_x + c * size, min_y + r * size)) for c in range(s)]
        pixel_data = '{' + ' '.join(row_colors) + '}'
        p.put(pixel_data, (0, s - r))
        w.update()

        
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
    """
    Return the index of the color of the current pixel
    within the Phoenix fractal in the palette array
    """
    juliaconstant = complex(0.5667, 0.0)
    pheonix = complex(-0.5, 0.0)
    zFlipped = complex(z.imag, z.real)      # This orients the image properly. Without it the image is rotated 90 degrees clockwise. 
    zPrev = 0+0j                            # zPrevious is the PREVIOUS Z value, defaulting at zero
    z = zFlipped                            # set Z back to zFlipped

    for i in range(102):
        zSave = z 
        z = z * z + juliaconstant + (pheonix * zPrev)
        zPrev = zSave                       # Set the prevZ value for the next iteration
        if abs(z) > 2:                      # if the absolute value of Z is graeter or equal than 2, then return that color
            return Palette.grad[i]                  
    return Palette.grad[101]


def getFractalConfig(dictionary, name):
    """Make sure that the fractal configuration data repository dictionary
    contains a key by the name of 'name'

    When the key 'name' is present in the fractal configuration data repository
    dictionary, return its value.

    Return False otherwise
    """
    for key in dictionary:
        if key == name:
            return dictionary[key]
    return None

def phoenix_main(image):
    """The main entry-point for the Phoenix fractal generator"""
    Save_As_Picture = True
    size = 512 
    b4 = time.time()
    # Set up the GUI
    win = Tk()
    frac_info = FractalInformation.fractalinformation() 
    print(f"Rendering {image} fractal", file=sys.stderr)

    # Construct a new TK PhotoImage
    tk_photo_image = PhotoImage(width=size, height=size)

    # Call make_picture_of_fractal with correct arguments
    makePictureOfFractal(frac_info.images[image], tk_photo_image, win, size)

    if Save_As_Picture:
        # Write out the Fractal into a .gif image file
        tk_photo_image.write(f"{image}.png")
        print(f"\nDone in {time.time() - b4:.3f} seconds!", file=sys.stderr)

    if Save_As_Picture:
        # Output the Fractal into a .png image
        tk_photo_image.write(f"{image}.png")
        print(f"Saved image to file {image}.png", file=sys.stderr)

    print("Close the image window to exit the program", file=sys.stderr)
    mainloop()
    
def mbrot_main(image):
    frac_info = FractalInformation.fractalinformation() 
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
    phoenix_main('peacock')    
    
    # To test mandelbrot fractals uncomment the line below and replace imagename with the desired fractal.
    # mbrot_main('starfis')