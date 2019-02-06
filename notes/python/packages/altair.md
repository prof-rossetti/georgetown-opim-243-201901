# The `altair` Package

> Altair is a declarative statistical visualization library for Python ... with a minimal amount of code. - [Altair website](https://altair-viz.github.io/)

## Reference

  + https://github.com/altair-viz/altair
  + https://altair-viz.github.io/
  + [Working in non-notebook environments](https://altair-viz.github.io/user_guide/display_frontends.html#working-in-non-notebook-environments)
  + https://altair-viz.github.io/user_guide/API.html

## Installation

First install the package using Pip, if necessary:

```sh
pip install altair
```

## Usage


To display a new chart, construct it by specifying certain chart configuration options, including the type of chart and the data to visualize:

```py
# adapted from: https://altair-viz.github.io/user_guide/display_frontends.html#working-in-non-notebook-environments

import altair
from vega_datasets import data # load a simple dataset as a pandas DataFrame

cars = data.cars() # for example, using a built-in dataset, but you can provide your own

chart = altair.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()

chart.serve()
```

Consult the documentation and examples for a variety of chart customization options.
