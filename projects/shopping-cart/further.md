# "Shopping Cart" Project Further Exploration

If you are moving through [the "Shopping Cart" Project](/projects/shopping-cart.md) project with ease, consider addressing one or more of the following "Further Exploration" challenges, but only after you have finished the basic project requirements.

## Validating User Inputs

For students desiring optional further exploration, the program should also validate the identifiers input by the clerk, displaying to the clerk a helpful message (e.g. "Hey, are you sure that product identifier is correct? Please try again!") if there are no products matching the given identifier.

## Writing Receipts to File

For students desiring even more optional further exploration, the program should also output the receipt information into a new `.txt` file saved somewhere in the project directory. The clerk's printer-connected computer should be able to actually print a paper receipt from the information contained in this file. The text file should be named according to the date and time the checkout process started (e.g. `/receipts/2017-07-04-15-43-13-579531.txt`, where the numbers represent the year, month, day, 24-hour-style hour, minute, second, and milliseconds/microseconds, respectively).

> NOTE: if you are using version control, you should exclude these receipt files from being tracked (a.k.a. "gitignore" them).

See [Python file management](/notes/programming-languages/python/file-management.md) for examples of how to write to file.

## Handling Pricing per Pound

For students desiring even more optional further exploration, add a new product to the list. Name it "Professor Rossetti's Bananas" and assign it other attribute values as desired. Assign it a price of `0.79`, but add another attribute called something like `price_per` to indicate the item is priced per "pound". Update all the other product dictionaries to match the new structure, indicating they are priced per "item". Finally, when running the program, if the clerk inputs the identifier of the bananas (or any other item that is priced by pound), the program should ask the clerk to input the number of pounds (e.g. `2.2`), then the program should calculate the price accordingly.

## Integrating with Barcode Scanner

Assemble a handful of real products that have barcodes.

Ask to borrow the professor's barcode scanner during class or office hours, or feel free to [purchase one from Amazon](https://www.amazon.com/gp/product/B003OUQ174/ref=ppx_yo_dt_b_asin_title_o03__o00_s00?ie=UTF8&psc=1).

Connect the barcode scanner to your computer's USB port, and practice scanning a few of the items, and record the resulting product identifiers.

Adapt the `products` variable to reflect the real products and their identifiers. For example (using real product identifiers from Whole Foods :smilecat:):

```py
# shopping_cart.py
# ...
products = [
    {"id": "99482452704", "name": "Organic Black Beans" ... },
    {"id": "99482434182", "name": "Organic Almonds Roasted Unsalted" ...},
    {"id": "99482418939", "name": "Jug of Spring Water" ... },
    {"id": "898248001107", "name": "Siggi's Strawberry Yogurt" ... },
    {"id": "898248001114", "name": "Siggi's Peach Yogurt" ... },
    {"id": "290295004269", "name": "Whole Foods Guacamole - Small" ...},
]
# ...
```

After modifying the product list, try re-running the program, using the barcode scanner to scan the real items. It should work!
