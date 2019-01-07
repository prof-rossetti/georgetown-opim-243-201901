# Installing Python and Pip

Before you can execute Python programs on your computer, you'll first need to install the Python command-line utility. When you install Python, you also get Pip, which is a command-line utility for installing third-party Python packages.

Over the past few years there has been a shift in the community from Python Version 2 to Python Version 3. This semester we will be using Python 3, exclusively. We might use different versions of Python 3, depending on the third-party packages we need to use. The `conda` command-line utility will help us manage our installation of the python programming language and its third party packages.

Before proceeding, please take a moment to [install and get familiar with `conda`](/notes/anaconda/README.md).

> NOTE: Running `python` and `pip` commands from your terminal will show you information about any global installations of Python which may exist on your computer. Because we are using project-specific versions of Python and Pip which are managed by Anaconda, we usually want to be running these commands from inside an Anaconda virtual environment. Doing so will tell us about our project-specific installation of Python.

## Detecting Installations

To see if Python is already installed on your machine:

```sh
# Mac Terminal:
which python # check for Python in general, or Homebrew-installed Python Version 2.x
which python3 # check for Homebrew-installed Python Version 3.x

# Windows Command Prompt:
where python
```

If you see a filepath output, it means Python is installed at the location specified, so you can advance to the version detection instructions below.

If you see an empty result or an error message, that usually means Python is not installed, so you can skip to the OS-specific installation instructions further down below.

## Detecting Versions

Let's see which version of Python is installed:

```shell
python --version #> Python 3.6.5
pip --version #> pip 9.0.1 from /usr/local/lib/python3.6/site-packages (python 3.6)
```












































## Usage

After Python is installed, you should be able to run Python commands from the command-line. Depending on your installation, you will either be running `python` and `pip` (website-downloaded Python on Windows or Mac), or `python3` and `pip3` (Homebrew-installed Python on Mac).

### Interactive Console

If you type `python` and press "enter", you will enter an interactive Python console. When you are done using the Python console, shut it down with `exit()`.

![a screenshot of using the python console to perform a simple calculation (2+2 = 4)](installation/img/mac-interactive-python-console.png)

### Scripts

You can alternatively write Python scripts and execute them from the command-line. To test this out, first create a file called `hello.py`, and use your text editor to place inside the following contents:

```py
# hello.py

print("--------------------------")
print("HELLO FROM A PYTHON SCRIPT")
print("--------------------------")
```

After saving the file, execute `python hello.py` from the command-line.

![a screenshot of the output resulting from running a python script from the command-line. the hello message is printed in the terminal](installation/img/python-running-script.png)
