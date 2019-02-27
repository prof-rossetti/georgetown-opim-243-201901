# "Executive Dashboard" Project

## Business Prompt

Assume you own and operate a successful small business, selling artisan clothing products through an online platform like Amazon, Etsy, or eBay.

![hoodie for sale on etsy](https://user-images.githubusercontent.com/1328807/51781151-cb7a5300-20e2-11e9-863f-3b82aaa5f5a9.png)

Due to certain investment interests in your business, you are obligated to hold monthly board meetings with your investors and advisors to discuss the company's strategic direction, set priorities, and allocate resources. To aid the board's decision-making processes, they expect you to provide them with a monthly summary report of business insights, including the aggregation of total sales and the identification of top-selling products.

Luckily, at the end of each calendar month, the online platform your company uses to sell its products makes available for download from its admin interface a CSV file representing all individual sales orders for that month.

But usually you only have a few hours from when the data becomes available to when you are required to turn it around and share the resulting insights with the board. Over the past few months, this report compilation process has been somewhat stressful and vulnerable to manual error. And the board's confidence in your operational leadership depends not only on your ability to meet sales goals, but also on your ability to provide them with accurate and timely information.

So your objective is to create a tool which automates the process of transforming monthly sales data into a report of business insights. This report should include charts and graphs to help tell a compelling story.

## Learning Objectives

  1. Create a tool to automate manual efforts and streamline business processes.
  2. Gain familiarity with CSV formatted data, and learn how to process it in Python.
  3. Explore basic data visualization capabilities in Python.
  4. Leverage built-in Python modules and third-party Python packages to speed development and enhance capabilities.

## Requirements

Write a Python program which adheres to the requirements detailed in the sections below.

### Information Input Requirements

Your program should be able to process any one of these provided [monthly sales CSV files](/data/monthly-sales/), in any order. These CSV files should reside inside a "data" sub-directory of your project repository. Instructors will use the same and/or similar files during the evaluation process. You can assume that each of these CSV files will have a name resembling "sales-YYYYMM.csv" (where "YYYY" represents the four digit year and "MM" represents the zero-padded month). And you can assume each of these CSV files will have the same header row (`date`, `product`, `unit price`, `units sold`, `sales price`).

When the user runs the program, they should be prompted to select one of these CSV files to process.

> OPTION A: allow the user to pass their selection as a command-line argument or environment variable during script invocation.

> OPTION B: prompt the user to input their selection.

> OPTION C: use the `os` module to detect the names of all CSV files which exist in the "data" directory, then display this list to the user and prompt the user to input their selection.

> OPTION D: are there any open source Python packages which provide helpful file-selection capabilities?

### Validation Requirements

If the user selects a file that doesn't exist or otherwise specifies the wrong filepath, the program should fail gracefully by: 1) displaying a friendly error message like "Hey, didn't find a file at that location", 2) avoiding runtime errors, and 3) preventing further execution.






### Calculation Requirements

The program's calculations and aggregations should be accurate and comprehensive.

To test the accuracy of your program's calculations, compare its "March 2018" results against the table of expected values below.

Product | Sum of sales price
-- | --
Button-Down Shirt | $6,960.35
Super Soft Hoodie | $1,875.00
Khaki Pants | $1,602.00
Vintage Logo Tee | $941.05
Brown Boots | $250.00
Sticker Pack | $216.00
Baseball Cap | $156.31
**Total Monthly Sales** | **$12,000.71**


### Information Output Requirements

During the course of the program's execution, it should display the following information:

  1. **Total monthly sales** for the business, equivalent to the sum of total monthly sales for each product, formatted as USD with a dollar sign and two decimal places (e.g. "Total Monthly Sales: $12,000.71").
  2. A **list of the top selling products**, and total monthly sales for each, formatted as USD with a dollar sign and two decimal places (e.g. "Button-Down Shirt: $6,960.35", "Super Soft Hoodie: $1,875.00", etc.).
  3. At least one **chart or graph** depicting this or related information to support the project objectives. Chart titles should include a human-friendly textual representation of the selected month and year (e.g. "March 2018").

![a screenshot of charts and graphs](/img/projects/exec-dash/top-selling-products-chart-bar.png)

All displays of price-related information should be formatted as USD, with a dollar sign and two decimal places. This includes in charts and graphs.













## Setup

### From Starter

To setup your project repository, either fork and clone the professor's ["Exec Dash" Starter Repository](https://github.com/prof-rossetti/exec-dash-starter-py), or follow the steps below to setup your own from scratch.

### From Scratch

Take this time to create a new repository on GitHub.com called something like "exec-dash-project". We'll refer to this as your "remote project repository".

Clone or download the remote project repository onto your local machine, perhaps on your Desktop. We'll refer to this as your "local project repository".

Navigate to your local project repository from the command-line.

Within the local project repository, create a new file called `monthly_sales.py` and place inside the following contents:

```py
# monthly_sales.py

# TODO: import some modules and/or packages here

# TODO: write some Python code here to produce the desired functionality...

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")
```

Create a new virtual environment named something like "dashboard-env" and activate it. Then from inside the virtual environment, execute the Python script to see it print the provided contents.

Finally, make your first commit with a message like "Setup project repository", and push these changes to GitHub. Once you see these changes reflected in your remote project repository on GitHub.com, you are ready to start the project development process.

## Development

As you develop your project repository, incrementally "commit" your work along the way. By the time you are finished with development, your project repository should contain a version history including at least a handful of incremental commits.

### Further Exploration

If you're able to complete the basic project requirements with relative ease, consider addressing one or more of the ["Exec Dash" Further Exploration Challenges](exec-dash/further.md) (e.g. validating CSV files, comparing sales across months, predicting future sales).

## Submission

To submit your project:

  1. Push your local project repository to GitHub, so you can visit your remote project repository at a URL like `https://github.com/YOUR_USERNAME/exec-dash-project`.
  2. Fork the ["upstream" course repository](https://github.com/prof-rossetti/georgetown-opim-243-201901) (or refresh your existing fork).
  3. Update your forked course repository's ["Exec Dash" Submissions CSV file](exec-dash/submissions.csv).
to include your GitHub username and your project repository's URL.
  4. Submit a Pull Request for your forked course repository's changes to be accepted into the "upstream" course repository.


## Evaluation

Project submissions will be evaluated according to the requirements set forth above, as summarized by the rubric below:

Category | Requirement | Weight
--- | --- | ---
Info Inputs | Captures file selection | 10%
Validations | Fails gracefully if file doesn't exist | 5%
Calculations | Displays accurate information | 20%
Info Outputs | Displays total monthly sales | 10%
Info Outputs | Displays top-selling products | 10%
Info Outputs | Displays charts and graphs, including titles and axis labels | 20%
Info Outputs | Formats prices as USD | 5%
Dev Process | Submitted via remote Git repository which reflects an incremental revision history | 20%

If experiencing execution error(s) while evaluating the application's required functionality, evaluators are advised to reduce the project's grade by anywhere between 4% and 50%, depending on the circumstances and severity of the error(s).

In recognition of deliverables which exhibit functionality above and beyond the basic required functionality, evaluators are encouraged to award between 0.5% and 3.5% extra credit "engagement points" to be applied towards the final exam.
