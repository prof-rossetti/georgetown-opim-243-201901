# The "Grocery Store Expansion" Exercise

## Objectives

Practice using Python to process CSV files in such a way as to illustrate the concept of **program-data independence**.

## Prerequisites

  + [The "Shopping Cart" Project](/projects/shopping-cart.md)
  + [The `csv` Module](/notes/python/modules/csv.md)

## Setup

Refer to your Shopping Cart Project solution.

Download a copy of the ["products.csv" file](/data/products.csv) into the root directory of your project repository, or inside a new sub-directory called "data".

Copy the contents of your "shopping_cart.py" file to a new file called something like "shopping_expansion.py". Save the file and make a commit in your project repository with a message like "Setup expansion exercise".

## Instructions

Instead of assigning the value of the `products` variable to be a hard-coded list of dictionaries, revise the "shopping_expansion.py" file to read the list of products from the "products.csv" file.

Optionally revise the CSV file by adding, removing, or editing records, then see how your program operates.

Optionally swap your CSV file with a friend and see how the program operates.

Observe how we can process data from different sources without changing the application's source code.
