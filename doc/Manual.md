# Fractal Visualizer User Manual

## Introduction
Welcome to the Fractal Painter tool! This utility allows you to generate and paint fractal images with various fractal types and color palettes. By providing different command-line arguments, you can customize the fractal and palette used in the generated image.

## Table of Contents
[Usage](#usage)
[Command-Line Arguments](#command-line-arguments)
[Examples](#examples)


## Usage
To use the Fractal Painter, follow the steps below:

* [ ] Step 1: Run the Script
Open your terminal or command prompt and navigate to the cs1440-assn4/ directory containing both the Fractal visualizer script (src/main.py), and the data folder. Run the script with the following command:

```bash
$ python src/main.py [fractal_name] [palette_name]
```
* [ ] Step 2: View the Generated Image
After running the script, the Fractal Painter will generate an image based on the specified fractal and palette. The image will either be displayed on your screen, or will open a new window on your task bar (on windows).

## Command-Line Arguments
The Fractal Painter script accepts the following command-line arguments:

**fractal_name**: The name of the fractal to be generated. If not provided, the default fractal is set to "mandelbrot." the fractal_name must be in the format "data/[fractal].frac"
**List of Fractals**:
* 8-points.frac
* branches@xxxxx.frac
    * branches\@0064.frac
    * branches\@0128/frac
    * branches\@0256.frac
    * branches\@0512.frac
    * branches\@1024.frac
* connected.frac
* coral.frac
* elephants.frac
* enhance.frac
* feathers.frac
* fjords.frac
* hourglass.frac
* Julia.frac
    * Julia-1.0.frac
    * Julia-1.1301.frac
* lace_curtains.frac
* leaf.frac
* mandelbrot-zoomed.frac
* mandelbrot.frac
* minibrot.frac
* monkey-knife-fight.frac
* phoenix.frac
* rabbit-hole.frac
* seahorse.frac
* shrimp-cocktail.frac
* spider-island.frac
* spider.frac
* spinneret.frac
* spiral-jetty.frac
* spiral0.frac
* spiral1.frac
    * spiral1\@0256.frac    the \ must be added for use on gitbash but I don't know if it will be needed on other applications
    * spiral1\@0512.frac
    * spiral1\@1024.frac
* starfish.frac
* tip0.frac
* tip1.frac
* tip2.frac
* tip3.frac
* tip4.frac
* wholly-squid.frac
* x-marks-the-spot.frac

**palette_name**: The name of the color palette to be used. If not provided, a default palette will be used. 
* [ ] There are currently only 2 palettes:
    * twilight
    * burning

## Examples
Here are some examples of how to use the Fractal Painter:

Example 1: Generate Mandelbrot Fractal with Default Palette
```bash
$ python src/main.py data/mandelbrot
```
Example 2: Generate Mandelbrot Fractal with Custom Palette
```bash
$ python src/main.py data/mandelbrot.frac twilight
```
Example 3: Generate Custom Fractal with Default Palette
```bash
$ python src/main.py data/coral.frac
```
Example 4: Generate Custom Fractal with Custom Palette
```bash
$ python src/main.py data/coral.frac twilight
```
### Conclusion
Explore the fascinating world of fractals with the Fractal Painter tool. Experiment with different fractal types and color palettes to create unique and visually stunning images. If you have any questions or feedback, feel free to reach out to the tool's creator.

Happy fractal painting!