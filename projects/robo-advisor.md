# "Robo Advisor" Project

> Prerequisites: [Web Requests Exercise](/exercises/web-requests.md), [Environment Variables](/notes/environment-variables.md)

## Business Prompt

Assume you own and operate a financial planning business which helps customers make investment decisions.

Your objective is to build yourself a tool to automate the process of providing your clients with stock trading recommendations.

Specifically, the system should accept one or more stock or cryptocurrency symbols as information inputs, then it should request real live historical trading data from the Internet, and finally it should provide a recommendation as to whether or not the client should purchase the given stocks or cryptocurrencies.

## Requirements

### Repository Requirements

Your project repository should contain an "app" directory with a "robo_advisor.py" file inside.

Your project repository should contain a "README.md" file. The README file should provide instructions to help someone else install, setup, and run your program. This includes instructions for installing package dependencies, for example using Pip. It also includes instructions for setting an environment variable named `ALPHAVANTAGE_API_KEY` (see "Security Requirements" section below).

If your desired approach to setting environment variables uses a ".env" file (see "Security Requirements" section below), your project repository should contain a file called ".gitignore" with the following contents inside to prevent that file from being tracked in version control:

```
# .gitignore

# ignore secret environment variable values
.env
```

Finally, your project repository should contain a "data" directory with another .gitignore file inside, with the following contents in it to ignore CSV files stored inside the data directory:

```
# data/.gitignore

# h/t: https://stackoverflow.com/a/5581995/670433

# ignore all files in this directory ...
*

# ... except this gitignore file
!.gitignore
```

### Security Requirements

Your program will need an API Key to issue requests to the [AlphaVantage API](https://www.alphavantage.co). But the program's source code should **absolutely not** include the secret API Key value.

Instead, you should set an environment variable called `ALPHAVANTAGE_API_KEY`, and your program should read the API Key from this environment variable at run-time.

You are encouraged to use a "dotenv" approach to setting project-specific environment variables by using a file called ".env" in conjunction with [the `dotenv` package](/notes/python/packages/dotenv.md). If you do, the ".env" file should **absolutely not** be tracked in version control or included in your GitHub repository.

> HINT: you may need to use a [local ".gitignore" file](https://help.github.com/articles/ignoring-files/#create-a-local-gitignore), or just don't upload the ".env" file to GitHub.

### Functionality Requirements

Your project should adhere to the following functionality requirements, as detailed in the sections below:

  + Information Input Requirements
  + Validation Requirements
  + Information Output Requirements
  + Calculation Requirements

#### Information Input Requirements

The system should prompt the user to input one or more stock symbols (e.g. `"MSFT"`, `"AAPL"`, etc.). It may optionally allow the user to specify multiple symbols, either one-by-one or all at the same time (e.g. `"MSFT, AAPL, GOOG, AMZN"`). It may also optionally prompt the user to specify additional inputs such as risk tolerance and/or other trading preferences, as desired and applicable.

#### Validation Requirements

Before requesting data from the Internet, the system should first perform preliminary validations on user inputs. For example, it should ensure stock symbols are a reasonable amount of characters in length and not numeric in nature.

If preliminary validations are not satisfied, the system should display a friendly error message like "Oh, expecting a properly-formed stock symbol like 'MSFT'. Please try again." and stop execution.

Otherwise, if preliminary validations are satisfied, the system should proceed to issue a GET request to the [AlphaVantage API](https://www.alphavantage.co/documentation/) to retrieve corresponding stock market data.

When the system makes an HTTP request for that stock symbol's trading data, if the stock symbol is not found or if there is an error message returned by the API server, the system should display a friendly error message like "Sorry, couldn't find any trading data for that stock symbol", and it should stop program execution, optionally prompting the user to try again.

#### Information Output Requirements

After receiving a successful API response, the system should write historical stock prices to one or more CSV files located in the repository's "data" directory. The CSV file contents should resemble the following example:

    timestamp, open, high, low, close, volume
    2018-06-04, 101.2600, 101.8600, 100.8510, 101.6700, 27172988
    2018-06-01, 99.2798, 100.8600, 99.1700, 100.7900, 28655624
    2018-05-31, 99.2900, 99.9900, 98.6100, 98.8400, 34140891
    2018-05-30, 98.3100, 99.2500, 97.9100, 98.9500, 22158528

If the system processes only a single stock symbol at a time, the system may use a single CSV file named "data/prices.csv", or it may use multiple CSV files, each with a name corresponding to the given stock symbol (e.g. "data/prices_msft.csv, "prices_aapl.csv", etc.). If the system processes multiple stock symbols at a time, it should use multiple files, each with a name corresponding to the given stock symbol (e.g. "data/prices_msft.csv", "prices_aapl.csv", etc.). If using more than one CSV file, the program should have a way of cleaning-up to prevent uncontrolled proliferation of new files.

After writing historical data to a CSV file, the system should perform calculations (see "Calculation Requirements" section below) to produce/print the following outputs:

  + The **selected stock symbol(s)** (e.g. "Stock: MSFT")
  + The **date and time when the program was executed**, formatted in a human-friendly way (e.g. "Run at: 11:52pm on June 5th, 2018")
  + The **date when the data was last refreshed**, usually the same as the latest available day of daily trading data (e.g. "Latest Data from: June 4th, 2018")
  + For each stock symbol: its **latest closing price**, its **recent average high price**, and its **recent average low price**, calculated according to the instructions below, and formatted as currency with a dollar sign and two decimal places with a thousands separator as applicable (e.g. "Recent Average High: $1,234.56", etc.)
  + A **recommendation** as to whether or not the client should buy the stock (see guidance below), and optionally what quantity to purchase. The nature of the recommendation for each symbol can be binary (e.g. "Buy" or "No Buy"), qualitative (e.g. a "Low", "Medium", or "High" level of confidence), or quantitative (i.e. some numeric rating scale).
  + A **recommendation explanation**, describing in a human-friendly way the reason why the program produced the recommendation it did (e.g. "because the stock's latest closing price is exceeds threshold XYZ")

> NOTE: the CSV files are information outputs of this system, not information inputs. So it shouldn't be necessary for your program to read a CSV file to perform calculations. The JSON API responses should have all the information your program needs to perform calculations.

#### Calculation Requirements

The **latest closing price** should be equal to the stock's "close" price on the latest available day of trading data.

The **recent average high price** should be equal to the maximum daily "high" price over approximately the past 100 available days of trading data.

The **recent average low price** should be calculated in a similar manner as the **recent average high price**, but it should instead be equal to the minimum of all daily "low" prices.

> NOTE: By default, the [daily data returned by the AlphaVantage API](https://www.alphavantage.co/documentation/#daily) uses an `outputsize` parameter value of `compact`. This "compact" response should provide daily data covering the previous 100 trading days, which is sufficient to use to calculate the **recent average high** and **recent average low** prices. It is acceptable and recommended to use these default, "compact" responses to calculate these recent average prices.

You are free to develop your own custom **recommendation** algorithm. This is perhaps one of the most fun and creative parts of this project. :smiley: One simple example algorithm would be (in pseudocode): If the stock's latest closing price is less than 20% above its recent average low, "Buy", else "Don't Buy".




















## Submission

TBA

## Evaluation

Submissions will be evaluated based on ability to meet each of the component requirements (see corresponding sections above for detailed instructions):

Category | Weight
--- | ---
Repository Requirements | 10%
Security Requirements | 15%
Information	Input Requirements | 10%
Validation Requirements | 25%
Information	Output Requirements | 20%
Calculation Requirements | 20%

This rubric is tentative, and may be subject to slight adjustments during the grading process.
