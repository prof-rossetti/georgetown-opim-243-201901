# Setting up a Python Development Environment

## Command-line

If you haven't already gotten familiar with [command-line computing](/exercises/command-line-computing.md), this would be a great time. Subsequent instructions assume you know how to use the command line to navigate your filesystem and manage directories and files.

## Command-line Utilities

After you are somewhat familiar with navigating your filesystem and creating directories and files from the command-line, you are ready to install some command line utilities, namely `conda`, `python`, and `pip`.

Follow the [Anaconda Notes](/notes/anaconda/README.md) to install all these command-line utilities. Included in that installation process, you may also choose to also install the "VS Code" text editor (see below for more context).

Afterwards, you should be able to use the `conda` utility to create and activate Anaconda virtual environments, then within any virtual environment:

  + Use the `python` and `pip` utilities to detect which versions of Python and Pip and third-party packages are installed.
  + Use the `python` utility to enter into an interactive Python console.
  + Use the `python` utility to execute Python scripts (files ending in .py).
  + Use the `code` utility to open folders and files in VS Code (see below).


## Text Editor

We'll be writing Python scripts using a class of software called the ["text editor"](https://idrh.ku.edu/text-editors-and-word-processors). Similar to word processing software like Microsoft Word, text editors allow us to write and save documents of text. But unlike word processors, which save extra metadata (e.g. styles and formatting) along with the underling text, text editors allow us to save files comprised of just text. This helps the computer more easily interpret them.

There are many good text editor options out there, including [VS Code](https://code.visualstudio.com/), [Atom](https://atom.io/), [Sublime](https://www.sublimetext.com/), and [Notepad++](https://notepad-plus-plus.org/), and it seems each developer has their own preference.

Regardless of which text editor you choose, you are highly encouraged to configure it with certain plugins, packages and extensions to enhance your experience and save you time. There are two sets of functionality in particular which will prove especially valuable this semester. These are "Python syntax auto-completion" and "column-style selection", respectively (see below).

### Python Syntax Auto-completion

Once configured, the text editor is capable of automatically completing snippets of Python code for you. This helps improve accuracy and saves time.

![a screenshot of the text editor's autocomplete functionality](https://user-images.githubusercontent.com/1328807/50870477-2e02ed80-1386-11e9-9a83-506d9c9d39ec.gif)

Editor-specific Guidance:

  + Sublime: ...
  + Atom: ...
  + VS Code: use the `ms-python.python` extension as recommended when you open a Python file.

### Column Selection

If configured, your text editor can also enable vertical text selection. This comes in handy if you have to change multiple lines of text at the same time, including commenting-out many lines at once.

![a screenshot of the text editor's column selection](https://user-images.githubusercontent.com/1328807/50870478-2e9b8400-1386-11e9-9378-0afadc4a7dce.gif)

Editor-specific Guidance:

  + Sublime: this functionality should be included by default.
  + Atom: try the ["Sublime-Style-Column-Selection"](https://atom.io/packages/Sublime-Style-Column-Selection) package.
  + VS Code: use the `ms-vscode.atom-keybindings` extension, and see also [Professor Rossetti's VS Code Configuration](/exercises/dev-env-setup/vs-code-config.md) to configure settings for `editor.multiCursorModifier` and `atomKeymap.promptV3Features`.
