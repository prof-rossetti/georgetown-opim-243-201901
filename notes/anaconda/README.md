# Anaconda

Anaconda provides a command-line utility called `conda` for installing and managing different versions of the Python programming language and of third-party Python packages.

> Anaconda is a package manager, an environment manager, a Python/R data science distribution, and a collection of over 1,500+ open source packages. Anaconda is free and easy to install, and it offers free community support. - [Anaconda website](https://docs.anaconda.com/anaconda/)

Resources:

  + https://conda.io/docs/_downloads/conda-cheatsheet.pdf
  + https://conda.io/docs/user-guide/getting-started.html
  + https://conda.io/docs/user-guide/tasks/manage-conda.html
  + https://conda.io/docs/user-guide/tasks/manage-environments.html
  + https://conda.io/docs/user-guide/tasks/manage-pkgs.html#id2
  + https://conda.io/docs/user-guide/tasks/view-command-line-help.html

## Detection

Check to see if Anaconda is already installed.

```sh
conda --version #> conda 4.5.11

# Mac Terminal:
which conda #> /anaconda3/bin/conda

# Windows Command Prompt:
where conda #> _____________
```

## Installation

If not yet installed, [download Anaconda version 3.7](https://www.anaconda.com/download) from the website. This might take a while, so prefer to do it over a strong WiFi connection. After the download begins, if you see a popup message about downloading a cheat sheet, you can ignore it.

After the download has finished, run the installer program and accept all the default options. The installation will take a few minutes to complete.

After the installation is complete, restart your terminal for the changes to take effect. Then try detecting the installation again, as described in the section above.

## Usage

Before using Anaconda, take a moment to create a new project directory somewhere on your computer, perhaps on your Desktop, and navigate there from the command line:

```sh
cd path/to/my-project-repo/ # where path/to/my-project-repo/ is the actual path to your desired project directory
```

From your project's root directory, install a new virtual environment, named something like `my-env`, optionally specifying a version of Python to use in this environment:

```sh
conda create -n my-env # OR ... conda create -n my-env python=3.6
conda env list #> you should see your new environment included
```

Enter the virtual environemnt:

```sh
conda activate my-env  # ... to deactivate: conda deactivate

which python #> /anaconda3/envs/my-env/bin/python
python --version #> Python 3.6.7 :: Anaconda, Inc.

which pip #> /anaconda3/envs/my-env/bin/pip
pip --version #> pip 18.1 from /anaconda3/envs/my-env/lib/python3.6/site-packages/pip (python 3.6)
```

Install package dependencies inside the virtual environment, as necessary:

```sh
pip install pandas matplotlib

pip list #> should see both, with supporting packages
```
