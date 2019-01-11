# The `python` Utility

Before you can execute Python programs on your computer, you'll first need to install the Python command-line utility. When you install Python, you also get Pip, which is a command-line utility for installing third-party Python packages.

Over the past few years there has been a shift in the community from Python Version 2 to Python Version 3. This semester we will be using Python 3, exclusively. We might use different minor versions of Python 3 (like 3.6 or 3.7), depending on the third-party packages we need to use for any given project.

Anaconda provides a command-line utility called `conda` to help us manage different versions of Python and Pip. Before proceeding, please take a moment to [install Anaconda and get familiar with `conda`](/notes/anaconda/README.md).

> MAC OS NOTE: Running `python` and `pip` commands directly from your Mac Terminal will show you information about any global installations of Python which may exist on your computer. But because we will be using project-specific versions of Python and Pip which are managed by Anaconda and installed in project-specific Anaconda virtual environments, we usually want to be running these commands from inside a project's virtual environment instead. See the Anaconda notes for more context.

## Detecting Installations

To see if Python is already installed, and if so where:

```sh
# Mac Terminal:
which python

# Windows Command Prompt:
where python
```

If you see a filepath output, it means Python is installed at the location specified, so you can advance to the version detection instructions below. Otherwise, if you see an empty result or an error message, that usually means Python is not installed.

## Detecting Versions

Let's see which version of Python is installed:

```sh
python --version
```

## Usage

After Python is installed, you should be able to execute `python` commands.

### Interactive Console

If you type `python` and press "enter", you will enter an interactive Python console. When you are done using the Python console, shut it down with `exit()`.

![a screenshot of using the python console to perform a simple calculation (2+2 = 4)](/img/notes/python/python-console.png)

### Scripts

You can alternatively write Python scripts and execute them from the command-line. To test this out, first create a file called `hello.py`, and use your text editor to place inside the following contents:

```py
# hello.py

print("--------------------------")
print("HELLO FROM A PYTHON SCRIPT")
print("--------------------------")
```

After saving the file, execute `python hello.py` from the command-line.

![a screenshot of the output resulting from running a python script from the command-line. the hello message is printed in the terminal](/img/notes/python/running-python-scripts.png)
