# The "Robo Advisor" Project, Revisited

## Guidance

### Basic Challenges

#### Formatting Prices

Refactor price-formatting logic into a function called something like `to_usd()`, and implement a corresponding test called something like `test_to_usd()`.

Test various scenarios to ensure the price formatting function displays a dollar sign, two decimal places, and a thousands separator.

### Intermediate Challenges

#### Processing API Responses

Refactor API data-processing logic into a function called something like `transform_response()`, and implement a corresponding test called something like `test_transform_response()`.

Test to ensure the function converts the example response data (nested dictionary) into a more usable format (i.e. list of daily dictionaries).

#### Writing to CSV

Refactor CSV file-writing logic into a function called something like `write_to_csv()`, and implement a corresponding test called something like `test_write_to_csv()`.

Test to ensure the function processes the provided data (i.e. list of daily dictionaries), creates a new CSV file, and writes the data there. Optionally test to ensure the CSV file contains the proper headers and/or expected values.
