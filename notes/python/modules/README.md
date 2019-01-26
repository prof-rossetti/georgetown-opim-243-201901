# Python Modules

You can extend the capabilities of your Python program by leveraging, or "importing" other files of code called "modules".

Some selected Python modules of interest include:

  + [The `code` Module](code.md)
  + [The `collections` Module](collections.md)
  + [The `csv` Module](csv.md) <--- for processing CSV data
  + [The `datetime` Module](datetime.md)
  + [The `itertools` Module](itertools.md)
  + [The `json` Module](json.md) <--- for processing JSON data
  + [The `math` Module](math.md)
  + [The `os` Module](os.md)
  + [The `pdb` Module](pdb.md) <--- very helpful for debugging!
  + [The `random` Module](random.md)
  + [The `statistics` Module](statistics.md)
  + [The `time` Module](time.md)

You can also create and import your own modules to help you organize your code into separate logical files.

For more details, follow along with this official tutorial on modules:

  + https://docs.python.org/3/tutorial/modules.html

## Usage

To load any module, whether a built-in module or a custom module you create, use the `import` statement. Then after importing the module, you can reference code contained within.

To see this concept in action, create a new directory on your computer called "modules-overview" and place inside the following two files, then run `python my_script`:

``` python
# modules-overview/my_module.py

import my_module


```

``` python
# modules-overview/my_script.py

import my_module
```

Then execute the script to prove it has access to code in the module:

```sh
python my_script
# > HELLO FROM MY MODULE!!!
```
