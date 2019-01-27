# Python Modules

You can extend the capabilities of your Python program by leveraging, or "importing" other files of code called "modules".

Some selected Python modules of interest include:

  + [The `csv` Module](csv.md) <--- for processing CSV data
  + [The `datetime` Module](datetime.md)
  + [The `itertools` Module](itertools.md)
  + [The `json` Module](json.md) <--- for processing JSON data
  + [The `math` Module](math.md)
  + [The `os` Module](os.md)
  + [The `random` Module](random.md)
  + [The `statistics` Module](statistics.md)
  + [The `time` Module](time.md)

You can also create and import your own modules to help you organize your code into separate logical files.

For more details, follow along with this official tutorial on modules:

  + https://docs.python.org/3/tutorial/modules.html#modules
  + https://docs.python.org/3/tutorial/modules.html#more-on-modules
  + https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts

## Usage

To load any module, whether a built-in module or a custom module you create, use the `import` statement. Then after importing the module, you can reference code contained within.

To see this concept in action, create a new directory on your computer called "modules-overview" and place inside the following two files:

``` python
# modules-overview/my_module.py

# note the lack of code in the global scope of this file
# ... all the code is contained within functions (below)
# ... which can be invoked separately as desired

def my_message():
    print("HELLO FROM A MODULE")

def other_message():
    print("GREETINGS EARTHLING")

# see more information about this weird but specific statement:
# https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts
# like "if this file is invoked directly from the command-line, then do some stuff..."
if __name__ == "__main__":
    print("INVOKING MY MODULE AS A SCRIPT...")
    my_message()
```

``` python
# modules-overview/my_script.py

import my_module # import the module

print("IMPORTING MY MODULE ...")

my_module.my_message() # selectively invoke functions provided by the module
```

Then execute the script to prove it has access to code in the module:

```sh
python my_script.py
#> IMPORTING MY MODULE ...
#> HELLO FROM A MODULE
```

Then execute the module directly to see what happens:

```sh
python my_module.py
#> INVOKING MY MODULE AS A SCRIPT...
#> HELLO FROM A MODULE
```

### Modules in Subdirectories

If your python file is located in a subdirectory, you can reference it using the `[directory name].[file name]`. Like this:


``` python
# modules-overview/things/robot.py

def robot_message():
    print("HELLO I'M A ROBOT")
```

``` python
# modules-overview/robot_script.py

import things.robot as bot

bot.robot_message()
```

```sh
python robot_script.py
#> HELLO I'M A ROBOT
```
