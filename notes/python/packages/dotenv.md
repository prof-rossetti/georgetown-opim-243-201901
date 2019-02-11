# The `dotenv` Package

> Prerequisite: [Environment Variables](/notes/environment-variables.md)

The `dotenv` package allows a program to reference environment variables from a project-specific ".env" file. This makes environment variables much easier to manage, especially for Windows users.

Reference: https://github.com/theskumar/python-dotenv.

## Installation

First install the package, if necessary:

```sh
pip install python-dotenv # note: NOT just "dotenv"
```

## Usage


To setup this example, create a new directory on your Desktop named "my-secure-project". Then navigate there from the command-line:

```sh
cd Desktop/my-secure-project/
```

Create two files in the "my-secure-project" directory named ".env" and "my_script.py", respectively, and place inside the following contents:

```sh
# my-secure-project/.env

SECRET_MESSAGE="Hello World"
```

```py
# my-secure-project/my_script.py

from dotenv import load_dotenv
import os

print(os.environ.get("SECRET_MESSAGE")) #> None

load_dotenv() #> loads contents of the .env file into the script's environment

print(os.environ.get("SECRET_MESSAGE")) #> "Hello World"
```
