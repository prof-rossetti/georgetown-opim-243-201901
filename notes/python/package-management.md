# Package Management

Reference:

  + https://docs.python.org/3/installing/index.html#installing-index
  + https://packaging.python.org/tutorials/installing-packages

When you install Python, you also get Python's package manager, `pip`. Use `pip` to install and manage third-party Python packages.

Listing packages currently installed:

```sh
pip list #> should see all installed packages, as well as their package dependencies
```

Installing packages:

```sh
pip install pandas # where pandas is the name of a package you want to install
```

<hr>

> Below is an intermediate concept we will cover later. Feel free to skip it for now.

<hr>

## Project-specific Package Management

You can specify and manage project-specific package dependencies by listing them in a file called `requirements.txt` in the project's root directory.

To specify a project's dependencies, first create a new `requirements.txt` file in your repository's root directory:

```shell
cd /path/to/your/project

# Mac Terminal:
touch requirements.txt

# Windows Command Prompt:
type nul > requirements.txt
```

Then revise the `requirements.txt` file. Write the name of each required Python package dependency on a new line, save the file, and exit. For example:

    ipython
    pytest
    requests

> NOTE: if you need to install a package from its Github source, use an entry like the following: `git+https://github.com/eskerda/pybikes.git`.

Finally, install package dependencies, as necessary:

```shell
pip install -r requirements.txt
```
