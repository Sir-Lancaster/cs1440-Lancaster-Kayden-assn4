from palette import Palette 

class PaletteFactory:
    def makePalette(palette_name='dynamic'):
        Palette_options = Palette()
        if palette_name == "striped":
            return Palette_options.StripedPalette()
        elif palette_name == "gradient":
            return Palette_options.GradientPalette("#FF0000", "#0000FF")
        elif palette_name == "dynamic":
            return Palette_options.DynamicPalette("#FF0000", "#00FF00")
        else:
            raise NotImplementedError("Invalid palette requested")