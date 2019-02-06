# The `matplotlib` Package

> Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms... Matplotlib tries to make easy things easy and hard things possible. You can generate plots, histograms, power spectra, bar charts, errorcharts, scatterplots, etc., with just a few lines of code. - [Matplotlib website](https://matplotlib.org/)

## Reference

  + https://github.com/matplotlib/matplotlib
  + https://matplotlib.org/
  + https://matplotlib.org/gallery/index.html
  + https://matplotlib.org/tutorials/introductory/sample_plots.html
  + https://matplotlib.org/gallery/showcase/anatomy.html
  + https://pythonspot.com/matplotlib-gallery/
  + https://pythonspot.com/matplotlib-bar-chart/

## Installation

First install the package using Pip, if necessary:

```sh
pip install matplotlib
```

## Usage

To display a new chart, construct it by specifying certain chart configuration options, including the type of chart (e.g. scatterplot), and the data to visualize:

```py
# adapted from: https://matplotlib.org/gallery/pie_and_polar_charts/pie_features.html

import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ["Product A", "Product B", "Product C", "Product D"]
sizes = [15, 30, 45, 10]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show() # need to explicitly "show" the chart window
```

Consult the documentation and examples for a variety of chart customization options.
