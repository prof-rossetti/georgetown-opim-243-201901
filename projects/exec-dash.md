# "Executive Dashboard" Project

## Business Prompt

Assume you own and operate a successful small business, selling artisan clothing products through an online platform like Amazon, Etsy, or eBay.

![hoodie for sale on etsy](#TODO)

Due to certain investment interests in your business, you are obligated to hold monthly board meetings with your investors and advisors to discuss the company's strategic direction, set priorities, and allocate resources. To aid the board's decision-making processes, they expect you to provide them with a monthly summary report of business insights, including the aggregation of total sales and the identification of top-selling products.

Luckily, at the end of each calendar month, the online platform your company uses to sell its products makes available for download from its admin interface a CSV file representing all individual sales orders for that month.

But usually you only have a few hours from when the data becomes available to when you are required to turn it around and share the resulting insights with the board. Over the past few months, this report compilation process has been somewhat stressful and vulnerable to manual error. And the board's confidence in your operational leadership depends not only on your ability to meet sales goals, but also on your ability to provide them with accurate and timely information.

So your objective is to create a tool which automates the process of transforming monthly sales data into a report of business insights. This report should include data dashboards of charts and graphs to help tell a compelling story.

## Learning Objectives

  1. Create a tool to automate manual efforts and streamline business processes.
  2. Gain familiarity with CSV formatted data, and how to process it in Python.
  3. Explore basic data visualization capabilities in Python.
  4. Leverage built-in Python modules like `os` and `csv`, and open source third-party packages like `pandas` and `matplotlib`, to increase development speed and capabilities.

## Requirements

Write a program which adheres to the following requirements, as detailed in the corresponding sections below:

  + [Information Input Requirements](#information-input-requirements)
  + [Calculation Requirements](#calculation-requirements)
  + [Information Output Requirements](#information-output-requirements)













































### Information Input Requirements

When the user runs the program, they should be prompted to select which CSV file to process.

> OPTION A: allow the user to pass the filename as a command-line argument or environment variable during script invocation

> OPTION B: use the `os` module to detect the names of all CSV files which exist in the data directory, then display them to the user and allow the user to input the name of their selection

> OPTION C: are there any open source Python packages with file-selection capabilities?

### Calculation Requirements

The program should process and aggregate the raw data into various summary tables, charts, and graphs. The comprehensiveness and accuracy of these aggregations, calculations, and representations comprises the "Calculation Requirements" grade.

### Information Output Requirements

During the course of the program's execution, it should present the user with the following information:

  1. Total monthly sales for the business, equivalent to the sum of total monthly sales for each product, formatted as USD with a dollar sign and two decimal places (e.g. "Total Monthly Sales: $12,000.71").
  2. A list of the top selling products, and total monthly sales for each, formatted as USD with a dollar sign and two decimal places (e.g. "Button-Down Shirt: $6,960.35", "Super Soft Hoodie: $1,875.00", etc.).
  3. At least one visual chart or graph depicting this or related information to support the project objectives. The title of at least one chart should include a textual representation of the respective month (e.g. "March 2018"), which should automatically update to reflect the name of the selected file.

![a screenshot of charts and graphs](#TODO)

> HINT: To detect the month and year, either parse the filename, or parse the imported date values.

Wherever price-related information (e.g. unit prices and sales prices) appears in the workbook, it should be formatted as USD, with a dollar sign and two decimal places.





















































### Setup

### From Starter

To setup your project repository, either fork and clone the professor's ["Exec Dash" Starter Repository](#TODO), or follow the steps below to setup your own from scratch.

### From Scratch

Take this time to create a new repository on GitHub.com called something like "exec-dash-project". We'll refer to this as your "remote project repository".

Clone or download the remote project repository onto your local machine, perhaps on your Desktop. We'll refer to this as your "local project repository".

Navigate to your local project repository from the command-line.

Within the local project repository, create a new file called `insights.py` and place inside the following contents:

```python
# insights.py

# TODO: import some modules and packages here

# TODO: write some Python code here to produce the desired functionality...

print("CRUNCHING THE DATA...")

print("VISUALIZING THE DATA...")
```

Finally, make your first commit with a message like "Setup project repository", and push these changes to GitHub. Once you see these changes reflected in your remote project repository on GitHub.com, you are ready to start the project development process.

## Development

Create a new virtual environment named something like "dashboard-env" and activate it. Then from inside the virtual environment, execute the Python script to see it print the provided contents.

As you develop your project repository, incrementally "commit" your work along the way. By the time you are finished with development, your project repository should contain a version history including at least a handful of incremental commits.

## Submission


To submit your project:

  1. Push your local project repository to GitHub, so you can visit your remote project repository at a URL like `https://github.com/YOUR_USERNAME/exec-dash-project`.
  2. Fork the ["upstream" course repository](https://github.com/prof-rossetti/georgetown-opim-243-201901) (or refresh your existing fork).
  3. Update your forked course repository's ["Shopping Cart" Submissions CSV file](exec-dash/submissions.csv).
to include your GitHub username and your project repository's URL.
  4. Submit a Pull Request for your forked course repository's changes to be accepted into the "upstream" course repository.

## Evaluation

Project submissions will be evaluated according to the requirements set forth above, as summarized by the rubric below:


Category | Requirement | Weight
--- | --- | ---
Info Inputs | Captures / scans product identifiers | 10%
Info Inputs | Handles the "DONE" signal | 10%
Info Outputs (Receipt) | Displays store info | 10%
Info Outputs (Receipt) | Displays checkout date and time | 10%
Info Outputs (Receipt) | Displays names and prices of all scanned products | 20%
Info Outputs (Receipt) | Displays tax and totals | 20%
Dev Process | Submitted via Git repository which reflects an incremental revision history | 20%

If experiencing execution error(s) while evaluating the application's required functionality, evaluators are advised to reduce the project's grade by anywhere between 15% and 50%, depending on the circumstances and severity of the error(s).

In recognition of deliverables which exhibit functionality above and beyond the basic required functionality, evaluators are encouraged to award between 0.5% and 3.0% extra credit "engagement points" to be applied towards the final exam.




### Further Exploration

If you're able to complete the basic project requirements with relative ease, consider addressing one or more of the ["Exec Dash" Further Exploration Challenges](exec-dash/further.md) (e.g. comparing sales across all months, predicting future sales).

## Evaluation

Project submissions will be evaluated according to the requirements set forth above, as summarized by the rubric below:

Category | Requirement | Weight
--- | --- | ---
Info Inputs | ________________ | 10%
Info Inputs | _______ | 10%
Info Outputs | _________ | 20%
Dev Process | Submitted via remote Git repository which reflects an incremental revision history | 20%

If experiencing execution error(s) while evaluating the application's required functionality, evaluators are advised to reduce the project's grade by anywhere between 15% and 50%, depending on the circumstances and severity of the error(s).

In recognition of deliverables which exhibit functionality above and beyond the basic required functionality, evaluators are encouraged to award between 0.5% and 3.0% extra credit "engagement points" to be applied towards the final exam.
