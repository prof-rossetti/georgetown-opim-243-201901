# The "Robo Advisor" Project, Revisited

## Guidance

### Basic Challenges

#### Formatting Prices

Refactor price-formatting logic into a function called something like `to_usd()`, and implement a corresponding test called something like `test_to_usd()`.

Test various scenarios to ensure the price formatting function displays a dollar sign, two decimal places, and a thousands separator.

#### Compiling Request URLs

Refactor request URL compilation logic into a function called something like `compile_url()`, and implement a corresponding test called something like `test_compile_url()`.

Test to ensure the function accepts a stock symbol input parameter, and constructs the expected request url.

> SECURITY NOTE: because the URL will contain an API key parameter and we don't want to hard-code that value into our expected URL, it's OK to:
>
>   A) abbreviate this test so it checks whether or not the compiled URL contains certain expected sub-strings, like the base URL and the given stock symbol, respectively, or
>
>   B) interpolate / concatenate the `ALPHAVANTAGE_API_KEY` environment variable value into the expected URL


### Intermediate Challenges

#### Issuing API Requests

Refactor API request logic into a function called something like `get_response()`, and implement a corresponding test called something like `test_get_response()`.

Test to ensure the function returns the expected response data in a usable format (i.e. a dictionary with keys `"Meta Data"` and `"Time Series (Daily)"`).

#### Processing API Responses

Refactor API data-processing logic into a function called something like `transform_response()`, and implement a corresponding test called something like `test_transform_response()`.

Test to ensure the function converts the example response data (nested dictionary) into a more usable format (i.e. list of daily dictionaries).

#### Writing to CSV

Refactor CSV file-writing logic into a function called something like `write_to_csv()`, and implement a corresponding test called something like `test_write_to_csv()`.

Test to ensure the function processes the provided data (i.e. list of daily dictionaries), creates a new CSV file, and writes the data there. Optionally test to ensure the CSV file contains the proper headers and/or expected values.
