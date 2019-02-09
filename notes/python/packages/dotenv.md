# The `dotenv` Package

> Prerequisite: [Environment Variables](/notes/environment-variables.md)

The `dotenv` package allows a program to reference environment variables from a project-specific `.env` file. This makes environment variables much easier to manage, especially for Windows users.

Reference: https://github.com/theskumar/python-dotenv.

## Installation

First install the package, if necessary:

```sh
pip install python-dotenv # note: NOT just "dotenv"
```

## Usage


To setup this example, create a new directory on your Desktop named "my-project". Then navigate there from the command-line:

```sh
cd Desktop/my-project/
```

Create two files in the "my-project" directory named `.env` and `my_script.py`, respectively, and place inside the following contents:

```sh
# my-project/.env

MY_MESSAGE="Hello, Hello!"
```

```py
# my-project/my_script.py

from dotenv import load_dotenv
import os

print(os.environ.get("MY_MESSAGE")) #> None

load_dotenv() #> loads contents of the .env file into the script's environment

print(os.environ.get("MY_MESSAGE")) #> "Hello, Hello!"
```
