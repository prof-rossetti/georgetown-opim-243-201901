# The "Grocery Store Expansion" Exercise

## Business Prompt

The "Shopping Cart" point-of-sale application you created for the local corner grocery store, and its resulting operational efficiencies, have boosted the store's profits so much that the store owner was able to invest in opening another two locations! Now the store owner needs a way to use the application in each of the locations. But each store has a different size and layout and serves a different set of clientele, and therefore stocks a different inventory of grocery products.

You consider creating three different copies of the application's source code to handle each inventory, but you decide against doing this because it would increase your software maintenance efforts. Not only would you need to revise the software each time a change is made to the inventory, but if you need to make a change to the software functionality, instead of doing it in one place, you'd need to do it in three different places, and this kind of duplication is prone to manual error.

After performing some user research, you learn that a manager for each location keeps track of their store's inventory of products in a spreadsheet, and is able to export the inventory as a CSV file. You observe that as long as the different inventory files are formatted in the same way (i.e. CSV format with the same columns), the program should be able to operate on any one of them. And you set off to adapt your previous solution to meet the new business requirements.

## Objectives

Practice using Python to process CSV files in such a way as to illustrate the concept of **program-data independence**.

## Prerequisites

  + [The "Shopping Cart" Project](/projects/shopping-cart.md)
  + [The `csv` Module](/notes/python/modules/csv.md)

## Setup

Refer to your "Shopping Cart" Project solution.

Download a copy of the ["products.csv" file](/data/products.csv) into the root directory of your project repository, or inside a new sub-directory called "data".

Copy the contents of your "shopping_cart.py" file to a new file called something like "shopping_expansion.py". Save the file and make a commit in your project repository with a message like "Setup expansion exercise".

## Instructions

Instead of assigning the value of the `products` variable to be a hard-coded list of dictionaries, revise the "shopping_expansion.py" file to read the list of products from the "products.csv" file. Then see how the program performs.

Optionally create a copy of the "products.csv" file so you can refer to it later. Then revise the original CSV file by adding, removing, and editing records until your inventory is unique. You can make up new product names and prices as desired. Then see how your program operates against that revised CSV file.

Optionally swap your revised CSV file with a friend's and see how the program operates. You're encouraged to post your fun and unique product inventories to the course Slack channel.

Observe how we can process data from different sources without changing the application's source code.
