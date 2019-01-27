# Debugging

Use the `help()` function to view documentation for a given object or datatype:

```py
help(str)
```

Use the `dir()` function to see what methods you can call on a given object.

```py
dir("Hello")
```

## Interactive Console

As of a recent version of Python, you should be able to use the built-in `breakpoint()` function to drop an interactive breakpoint on any line of code. Once you run the script, it will stop at the breakpoint to facilitate further investigation:

```py
v = 1

breakpoint()

v = 2

#> (Pdb) v
#> 1
#> (Pdb)
```

```py
for i in [1, 2, 3, 4, 5]:
    print(i)
    if i == 4:
        breakpoint()

#> 1
#> 2
#> 3
#> 4
#> > /Users/mjr/Desktop/my_script.py(3)<module>()
#> -> for i in [1, 2, 3, 4, 5]:
#> (Pdb) i
#> 4
#> (Pdb)
```







Various modules and third-party packages offer alternative or equivalent interactive debugging capabilities:

  + [`code`](modules/code.md)
  + [`pdb`](modules/pdb.md)
  + [`ipython`](packages/ipython.md)
