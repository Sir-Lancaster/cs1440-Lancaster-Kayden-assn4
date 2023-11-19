# These are the imports that I usually import
import sys
import time
from tkinter import Tk, Canvas, PhotoImage, mainloop
from time import time
from Palette import grad

SPC = chr(0o40)  # Why doesn't anybody write octal numbers anymore...
s = 0o1000

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
            return grad[i]                  
    return grad[101]


def getFractalConfigurationDataFromFractalRepositoryDictionary(dictionary, name):
    """Make sure that the fractal configuration data repository dictionary
    contains a key by the name of 'name'

    When the key 'name' is present in the fractal configuration data repository
    dictionary, return its value.

    Return False otherwise
    """
    for key in dictionary:
        if key in dictionary:
            if key == name:
                value = dictionary[key]
                return key


Save_As_Picture = True
tkPhotoImage = None

def makePictureOfFractal(f, p, w, s):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    Assumes the image is 640x640 pixels."""

    # Compute the minimum and maximum coordinates of the picture
    min_x = f['centerX'] - (f['axisLength'] / 2.0)
    min_y = f['centerY'] - (f['axisLength'] / 2.0)
    max_x = f['centerX'] + (f['axisLength'] / 2.0)
    max_y = f['centerY'] + (f['axisLength'] / 2.0)

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


f = {
        # The full Phoneix set
        'phoenix': {
            'centerX':     0.0,
            'centerY':     0.0,
            'axisLength':  3.25,
            },

        # This one looks like a peacock's tail to me
        'peacock': {
            'centerX':     -0.363287878200906,
            'centerY':     0.381197981824009,
            'axisLength':  0.0840187115019564,
        },

        # Two or more monkeys having a scuffle
        'monkey-knife-fight': {
            'centerX':    -0.945542168674699,
            'centerY':    0.232234726688103,
            'axisLength': 0.136626506024096,
            },

        # This one makes me hungry to look at
        'shrimp-cocktail': {
            'centerX': 0.529156626506024,
            'centerY': -0.3516077170418,
            'axisLength': 0.221204819277108,
            },
        }


# This is how you write colors for computers
WHITE = '#ffffff'  # white
RED = '#ff0000'  # red
BLUE = '#00ff00'  # blue
GREEN = '#0000ff'  # green
BLACK = '#000000'  # black
ORANGE = '#ffa50'  # orange
TOMATO = '#ff6347'  # tomato (a shade of red)
HOT_PINK = '#ff69b4'  # hot pink (a kind of pink)
REBECCA_PURPLE = '#663399'  # Rebecca Purple
LIME_GREEN = '#89ff00'  # lime green (brighter than regular green)
GREY0 = '#000000'  # gray 0 - basically the same as black
GRAY37 = '#5e5e5e'  # gray 37 - lighter than black and gray 36
GREY74 = '#bdbdbd'  # gray 74 - almost white
GRAY99 = '#fcfcfc'  # gray 99 - almost white


def phoenix_main(image):
    """The main entry-point for the Phoenix fractal generator"""
    Save_As_Picture = True
    size = 512 
    b4 = time()
    # Set up the GUI
    win = Tk()

    print(f"Rendering {image} fractal", file=sys.stderr)

    # Construct a new TK PhotoImage
    tk_photo_image = PhotoImage(width=size, height=size)

    # Call make_picture_of_fractal with correct arguments
    makePictureOfFractal(f[image], tk_photo_image, win, size)

    if Save_As_Picture:
        # Write out the Fractal into a .gif image file
        tk_photo_image.write(f"{image}.png")
        print(f"\nDone in {time() - b4:.3f} seconds!", file=sys.stderr)

    if Save_As_Picture:
        # Output the Fractal into a .png image
        tk_photo_image.write(f"{image}.png")
        print(f"Saved image to file {image}.png", file=sys.stderr)

    print("Close the image window to exit the program", file=sys.stderr)
    mainloop()

if __name__ == '__main__':
    phoenix_main('peacock')