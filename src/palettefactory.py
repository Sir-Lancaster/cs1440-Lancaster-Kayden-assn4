from Palette import StripedPalette, DynamicPalette

class PaletteFactory:
    def makePalette(self, iterations, palette_name='dynamic'):

        if palette_name == "striped":
            strip_pal = StripedPalette()
            current_palette = strip_pal.getColor(iterations)
            return current_palette
        elif palette_name == "dynamic":
            dyn_pal = DynamicPalette()
            current_palette = dyn_pal.getColor(iterations)
            return current_palette
        else:
            raise NotImplementedError("Invalid palette requested")

# Example usage:
if __name__ == '__main__':
    factory = PaletteFactory()

    # Create instances of different palettes
    striped_palette = factory.makePalette(100, "striped")
    print(len(striped_palette))
    dynamic_palette = factory.makePalette(100, "dynamic")
    print(len(dynamic_palette))

