# "Web Requests" Exercise

> Prerequisite: [The `requests` Package](/notes/python/packages/requests.md)

## Objectives

This exercise asks students to use Python to process static data files located on the Internet. It focuses on "GET" requests, which are the most common and perhaps the simplest kind of HTTP request.

This exercise should help students familiarize themselves with JSON-formatted data and enhance their familiarity with CSV-formatted data.

After completing this exercise, students should be ready to issue requests to real-life web services (APIs).

## Challenges

Students should focus on the JSON challenges below. Any student desiring further exploration may optionally also complete the CSV challenges.

### JSON Challenges

> HINT: the response text for each of the following challenges will be formatted as JSON, so you can use [the `json` module](/notes/python/modules/json.md) to parse it. Also, depending on which URL we are making a request to, sometimes the JSON response will resemble a list and sometimes it will resemble a dictionary, so make sure to parse each accordingly.

#### JSON Challenge 1: Product

Write a Python program which issues a GET request for this [product.json data](https://raw.githubusercontent.com/prof-rossetti/georgetown-opim-243-201901/master/data/products/1.json), then print the product's "name".

> FYI: the response text will be a JSON object, like a Python dictionary.

#### JSON Challenge 2: Products

Write a Python program which issues a GET request for this [products.json data](https://raw.githubusercontent.com/prof-rossetti/georgetown-opim-243-201901/master/data/products.json), then loop through each product and print its "name" and "id".

> FYI: the response text will be a JSON array of objects, like a Python list of dictionaries.

#### JSON Challenge 3: Gradebook

Write a Python program which issues a GET request for this [gradebook.json data](https://raw.githubusercontent.com/prof-rossetti/georgetown-opim-243-201901/master/data/gradebook.json), then calculate and print the average, min, and max grades.

<hr>

### CSV Challenges

> HINT: the response text for each of the following challenges will be formatted as a CSV string, so you can you can use the familiar CSV-processing mechanisms like the [the `csv` module](/notes/python/modules/csv.md) or [the `pandas` package](/notes/python/packages/pandas.md), with some possible modifications for parsing a CSV-formatted string instead of a CSV file.

#### CSV Challenge 1: Products

Write a Python script which issues a GET request for this [products.csv data](https://raw.githubusercontent.com/prof-rossetti/georgetown-opim-243-201901/master/data/products.csv), then loop through each product and print its "name" and "id".

#### CSV Challenge 2: Gradebook

Write a Python program which issues a GET request for this [gradebook.csv data](https://raw.githubusercontent.com/prof-rossetti/georgetown-opim-243-201901/master/data/gradebook.csv), then calculate and print the average, min, and max grades.
