#              Copyright © 2023 DuckieCorp. All Rights Reserved.
#
#                       __      Redistribution and use of this code, with or
#                     /` ,\__   without modification, are permitted provided
#                    |    ).-'  that the following conditions are met:
#                   / .--'
#                  / /          0. Redistributions of this code must retain
#    ,      _.==''`  \             the above copyright notice, this list of
#  .'(  _.='         |             conditions and the following disclaimer.
# {   ``  _.='       |          1. The name of the author may not be used to
#  {    \`     ;    /              endorse or promote products derived from
#   `.   `'=..'  .='               this software without specific prior written
#     `=._    .='                  permission.
#  jgs  '-`\\`__                2. Neither the name of the University nor the
#           `-._{                  names of its contributors may be used to
#                                  endorse or promote products derived from
#                                  this software without specific prior written
#                                  permission.

from colour import Color

class Palette:
    def __init__(self):
        # You can define data members here if needed
        self.Dynamic_Colors = []
        self.striped_colors = []
        pass

    def getColor(self, n):
        raise NotImplementedError("Concrete subclass of Palette must implement getColor() method")

class BurningGold(Palette):
    def getColor(self, n):
        # Example of a simple palette using modulus for repeating stripes
        for i in range(n):
            if i % 2 == 0:
                current_color = Color('crimson')
                curCol_to_hex = current_color.hex_l
                self.striped_colors.append(curCol_to_hex)
            else:
                current_color = Color('gold')
                curCol_to_hex = current_color.hex_l
                self.striped_colors.append(curCol_to_hex)
        return self.striped_colors

class MorningsTwilight(Palette):
    def getColor(self, n):
        # Example of dynamically generated palette using the colour module
        start_color = Color("cyan")
        end_color = Color("black")
        steps = n
        # Convert the generator to a list
        for color in list(start_color.range_to(end_color, steps)):
            self.Dynamic_Colors.append(color.hex_l)
        return self.Dynamic_Colors
    
if __name__ == '__main__':
    # Example usage
    palette1 = BurningGold()
    palette2 = MorningsTwilight()


    color1 = palette1.getColor(513)
    color2 = palette2.getColor(513)
    print(f"Striped Palette - {color1}")
    print(len(color1))
