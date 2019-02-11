
# "Robo Advisor" Further Exploration Challenges

## Challenge 1: Multiple Stocks

Instead of processing a single stock at a time, allow the user to process multiple stocks at the same time.

If you decide to implement this approach, pay attention to the "Information Output Requirements" about using multiple CSV files instead of a single file.

## Challenge 2: 52-Week Highs and Lows

Instead of calculating and printing the stock's **recent average high** and **recent average low**, calculate and print the stock's **52-week high** and **52-week low**, respectively.

The **52-week high** should be equal to the maximum daily "high" price over approximately the past year of trading data. For example, if the last available day of trading data is June 1st, 2018, the program should find the maximum of all the "high" prices between around June 1st, 2017 and June 1st, 2018.

The **52-week low** should be calculated in a similar manner as the 52-week high, but it should instead be equal to the minimum of all "low" prices within the past year.

> HINT: If you were previously requesting daily data, you will have to change your approach to either request more of it (i.e. by specifying the URL parameter `&outputsize=full`), or to instead request weekly data. Theoretically the maximum weekly "high" price should be the same as the maximum daily "high" price within the same period.

> NOTE: If you do request "full" responses of daily data, the size of the response may drastically increase, and the speed of your requests may slow down noticeably. If you think these changes negatively impact user experience, you might want to consider requesting weekly data instead.

## Challenge 3: Plotting Prices over Time

In addition to writing the historical stock prices to a CSV file, your program should also display a line graph of the stock prices over time. :smiley_cat:

Optionally include any other data visualizations as desired, to add context to and increase confidence in the final recommendations.

## Challenge 4: Automated Tests

> WARNING: only for advanced students with interest in creating professional-quality applications who are comfortable [looking ahead at automated testing notes](/notes/python/testing.md), specifically those on [the `pytest` pacakge](/notes/python/packages/pytest.md). For other students, don't worry, we'll cover automated testing in detail later in OPIM 244...

The repository should contain meaningful and relevant automated tests. If there are any tests, they should exist in a "tests" directory in a file called something like "robo_adviser_test.py" (e.g. "tests/robo_adviser_test.py"). And the "README.md" file should include instructions and commands for how to run the tests.

One best practice when testing applications that issue HTTP requests is to avoid issuing any requests during automated testing. To test your application's ability to parse API responses without actually issuing a request, use an example "mock" response instead. For example you may save a copy of a real response into a file named something like "tests/example_responses/daily_response.json". Then configure your tests to parse the contents of this local file instead of parsing the response that would have been returned by the API.

If you would like clarification about recommended testing strategies or general advice on how to meaningfully test this application, ask the professor, who would be happy to help. But generally, you might try testing your application is performing accurate calculations given various example responses. And you might try testing your application is properly validating user inputs given various possible inputs.
