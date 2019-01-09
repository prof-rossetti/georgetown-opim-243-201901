# Setting up a Python Development Environment

## Command-line

If you haven't already gotten familiar with [command-line computing](/exercises/command-line-computing.md), this would be a great time. Subsequent instructions assume you know how to use the command line to navigate your filesystem and manage directories and files.

## Anaconda, Python, and Pip

After you are somewhat familiar with navigating your filesystem and creating directories and files from the command-line, you are ready to install some command line utilities, namely `conda`, `python`, and `pip`.

Follow the [Anaconda Notes](/notes/anaconda/README.md) to install all these command-line utilities. Included in that installation process, you may also choose to also install the "VS Code" text editor (see below for more context).

Afterwards, you should be able to create and activate Anaconda virtual environments, and detect the versions of Python and Pip installed inside.

## Text Editor

OK, after installing the `python` command-line utility, you should be able to use it to either enter into an interactive Python shell, or to run existing Python scripts (files ending in .py).

We will be writing these Python scripts using a class of software called a "text editor". Similar to word processing software like Microsoft Word, text editors allow us to write and save documents of text. But unlike word processors which save extra metadata like styles and formatting along with the underling text, text editors allow us to save files comprised of only text, so they can be more easily interpreted by the computer.

There are many good text editor options out there, including [VS Code](https://code.visualstudio.com/), [Atom](https://atom.io/), [Sublime](https://www.sublimetext.com/), and [Notepad++](https://notepad-plus-plus.org/), and it seems each developer has their own preference.

If you already have a preferred text editor, you may likely continue using it in pursuit of course objectives. However, regardless of whether or not you already have a preferred text editor, it may be helpful to install multiple options and compare them to see which you prefer.

The professor has used a variety of these options over the years and may be able to provide a basic level of support for many of them, but is currently using and liking VS Code, and therefore recommends you use VS Code as well. If you choose to use VS Code, you can either install it as part of the Anaconda installation (see above), or via separate download. The GA is using Sublime, and can provide support for that option.

Regardless of which text editor you choose, you are highly encouraged to configure it with certain plugins and extensions to enhance your experience and save you time. There are two sets of functionality in particular which will prove especially valuable this semester. These are "Python syntax auto-completion" and "column-style selection", respectively (see below).

### Python Syntax Auto-completion

Once configured, the text editor is capable of automatically completing snippets of Python code for you. This helps improve accuracy and saves time.

![a screenshot of the text editor's autocomplete functionality](https://user-images.githubusercontent.com/1328807/50870477-2e02ed80-1386-11e9-9a83-506d9c9d39ec.gif)

Editor-specific Guidance:

  + Sublime: ...
  + Atom: ...
  + VS Code: use the `ms-python.python` extension as recommended.

### Column Selection

Once configured, your text editor can also enable vertical text selection. This comes in handy if you have to change multiple lines of text at the same time, including commenting-out many lines at once.

![a screenshot of the text editor's column selection](https://user-images.githubusercontent.com/1328807/50870478-2e9b8400-1386-11e9-9378-0afadc4a7dce.gif)

Editor-specific Guidance:

  + Sublime: this functionality should be included by default.
  + Atom: try the ["Sublime-Style-Column-Selection"](https://atom.io/packages/Sublime-Style-Column-Selection) package.
  + VS Code: use the `ms-vscode.atom-keybindings` extension, and see also [Professor Rossetti's VS Code Configuration](/exercises/dev-env-setup/vs-code-config.md) to configure settings for `editor.multiCursorModifier` and `atomKeymap.promptV3Features`.
