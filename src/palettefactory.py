from Palette import BurningGold, MorningsTwilight

class PaletteFactory:
    def makePalette(self, iterations=513, palette_name='twilight'):

        if palette_name == "burning":
            strip_pal = BurningGold()
            current_palette = strip_pal.getColor(iterations)
            return current_palette
        elif palette_name == "twilight":
            dyn_pal = MorningsTwilight()
            current_palette = dyn_pal.getColor(iterations)
            return current_palette
        else:
            raise NotImplementedError("Invalid palette requested")

# Example usage:
if __name__ == '__main__':
    factory = PaletteFactory()

    # Create instances of different palettes
    striped_palette = factory.makePalette(palette_name="striped")
    print(len(striped_palette))
    dynamic_palette = factory.makePalette(palette_name="dynamic")
    print(len(dynamic_palette))

