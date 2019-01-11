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

To specify a project's dependencies, first create a new `requirements.txt` file in your repository's root directory, then revise the `requirements.txt` file to include the names of the packages you want to install. Write the name of each Python package dependency on a new line. For example:

    ipython
    pytest
    requests
    git+https://github.com/eskerda/pybikes.git # can install from github source, if necessary

Make sure to save the file.

Finally, install package dependencies by specifying the requirements filepath:

```shell
pip install -r requirements.txt
```
