# The `itertools` Module

Reference: https://docs.python.org/3/library/itertools.html.

Use the `itertools` module to perform advanced operations on iterable objects such as lists.

Group a list of dictionaries by key:

```python
import itertools
from operator import itemgetter

teams = [
    {"city": "New York", "name": "Yankees"},
    {"city": "New York", "name": "Mets"},
    {"city": "Boston", "name": "Red Sox"},
    {"city": "New Haven", "name": "Ravens"}
]

teams = sorted(teams, key=itemgetter("city"))

for key, value in itertools.groupby(teams, key=itemgetter("city")):
    print("----------------------------")
    print(key.upper() + ":")
    for team in value:
        print("  + " + team["name"])

#> ----------------------------
#> BOSTON:
#>   + Red Sox
#> ----------------------------
#> NEW HAVEN:
#>   + Ravens
#> ----------------------------
#> NEW YORK:
#>   + Yankees
#>   + Mets
```
