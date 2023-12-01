from Palette import StripedPalette, DynamicPalette

class PaletteFactory:
    def makePalette(self, palette_name='dynamic', *args, **kwargs):
        if palette_name == "striped":
            return StripedPalette()
        elif palette_name == "dynamic":
            return DynamicPalette(*args, **kwargs)
        else:
            raise NotImplementedError("Invalid palette requested")

# Example usage:
factory = PaletteFactory()

# Create instances of different palettes
striped_palette = factory.makePalette("striped")
dynamic_palette = factory.makePalette("dynamic", "#FF0000", "#00FF00")

# Get colors from the palettes
striped_colors = striped_palette.getColor(5)
dynamic_colors = dynamic_palette.getColor(5)

print(striped_colors)
print("\n That was Striped colors. Now for our featured presentation: Dynamic colors")
print(dynamic_colors)
