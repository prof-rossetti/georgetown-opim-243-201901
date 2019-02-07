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
pip install vega_datasets # only if you're trying to use one of their provided datasets
```

## Usage

To display a new chart, construct it by specifying certain chart configuration options, including the type of chart and the data to visualize.

Example using provided dataset:

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

> NOTE: once you "serve" the chart, you'll see your terminal window get taken over by running a web server. You'll be able to view your chart in a web browser, but when you're done you'll need to quit the web server by pressing control+c in your terminal. After doing so you will regain the ability to type commands in your terminal window.

Example using custom dataset:

```py
# adapted from: https://altair-viz.github.io/gallery/simple_bar_chart.html
import altair as alt
import pandas as pd

source = pd.DataFrame({
    "a": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
    "b": [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

chart = alt.Chart(source).mark_bar().encode(
    x="a",
    y="b"
)

chart.serve()
```

> NOTE: it appears altair requires you to specify the data as a [Pandas DataFrame](/notes/python/packages/pandas.md). If you'd rather not use Pandas, consider choosing a different charting library.



Consult the documentation and examples for a variety of chart customization options.
