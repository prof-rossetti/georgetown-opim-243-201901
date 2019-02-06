# The "Chart Gallery" Exercise

## Objectives

Learn how to create data visualizations in Python. Practice an active learning process.

## Setup

Create a new exercise repository called "chart-gallery" somewhere on your computer, perhaps on your Desktop. Navigate there from the command-line.

Create a new Python script called something like "three_charts.py" and use your text editor to place inside the following Python code:

```py
# three_charts.py

#
# CHART 1 (PIE)
#

pie_data = [
    {"company": "Company X", "market_share": 0.55},
    {"company": "Company Y", "market_share": 0.30},
    {"company": "Company Z", "market_share": 0.15}
]

print("----------------")
print("GENERATING PIE CHART...")
print(pie_data) # TODO: create a pie chart based on the pie_data

#
# CHART 2 (LINE)
#

line_data = [
    {"date": "2019-01-01", "stock_price_usd": 100.00},
    {"date": "2019-01-02", "stock_price_usd": 101.01},
    {"date": "2019-01-03", "stock_price_usd": 120.20},
    {"date": "2019-01-04", "stock_price_usd": 107.07},
    {"date": "2019-01-05", "stock_price_usd": 142.42},
    {"date": "2019-01-06", "stock_price_usd": 135.35},
    {"date": "2019-01-07", "stock_price_usd": 160.60},
    {"date": "2019-01-08", "stock_price_usd": 162.62},
]

print("----------------")
print("GENERATING LINE GRAPH...")
print(line_data) # TODO: create a line graph based on the line_data

#
# CHART 3 (HORIZONTAL BAR)
#

bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]

print("----------------")
print("GENERATING BAR CHART...")
print(bar_data) # TODO: create a horizontal bar chart based on the bar_data
```

Create and activate a new virtual environment called something like "charts-env". Then from within the virtual environment, run the "three_charts.py" program to see it print the provided data structures.

Make your first commit with a message like "Setup exercise".

## Instructions

### Research

Search the Internet to identify a handful of potential third-party Python packages which can produce data visualizations. Consult their official documentation, GitHub source code repositories, and a variety of credible third-party sources to familiarize yourself with the relative popularity and usability of each package.

As you find helpful online resources and documentation, assemble a list of URLs for future reference and attribution purposes.

### Investigation Phase

After identifying a few potential dataviz packages, use your judgment about their relative popularity and usability to choose one to investigate further.

From within your project's virtual environment, use Pip to install your selected package according to its installation instructions.

Either in the "three_charts.py" file or in a separate scratch-work file called something like "investigate.py", see if you can write Python code to implement some of the simpler examples from your chosen package's documentation. Commit your code incrementally as you make progress and reach certain milestones.

If at any time you think you'd like to investigate a different package, be open to doing so, perhaps in a separate scratch-work file. You might have to try a few different options before you find a package that works best for you. Take your time and enjoy the investigation process.

### Development Phase

Once you're comfortable in your ability to make an example chart using your chosen package,
adapt the contents of the "three_charts.py" script to process the provided data structures into three respective charts (i.e. pie, line, horizontal bar).

Focus on one chart at a time. Commit your code incrementally as you make progress and reach certain milestones. Make at least one commit per chart.

Prefer to generate a draft version of each chart before moving on to customizing the intricate details of each (e.g. chart formatting and style).
