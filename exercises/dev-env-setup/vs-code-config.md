# Professor Rossetti's VS Code Configuration

These are some of the professor's personal VS Code configurations, for your reference. Feel free but not obligated to use them.

## Extensions

A sample of relevant extension identifiers which result from running `code --list-extensions`:

```sh
HookyQR.beautify
mikestead.dotenv
ms-python.python
ms-vscode.atom-keybindings
sleistner.vscode-fileutils
streetsidesoftware.code-spell-checker
whizkydee.material-palenight-theme
xamm.filepath
yzhang.markdown-all-in-one
```

You might try searching these manually or [importing them programmatically](https://stackoverflow.com/a/49398449/670433) via `code --install-extension EXTENSION_NAME`, where "EXTENSION_NAME" is the extension's identifier (see list above).

> DISCLAIMER: the professor has not tested the extension importing process, so if you experience issues, please report them immediately

## User Settings

A sample of relevant settings from the `settings.json` file:

```json
{
    "window.zoomLevel": 0,
    "workbench.activityBar.visible": false,
    "workbench.colorTheme": "Palenight Theme",
    "breadcrumbs.enabled": true,
    "explorer.confirmDragAndDrop": false,
    "explorer.confirmDelete": false,
    "editor.fontSize": 14,
    "editor.multiCursorModifier": "ctrlCmd",
    "files.trimTrailingWhitespace": true,
    "files.insertFinalNewline": true,
    "files.trimFinalNewlines": true,
    "editor.formatOnType": true,
    "editor.tabSize": 2,
    "atomKeymap.promptV3Features": true,
    "emmet.showSuggestionsAsSnippets": true,
    "diffEditor.ignoreTrimWhitespace": false,
    "editor.wrappingIndent": "none",
    "editor.formatOnPaste": true
  }

```

## Key Bindings

```json
// Place your key bindings in this file to overwrite the defaults
[
    {
        "key": "shift+cmd+d",
        "command": "editor.action.copyLinesDownAction",
        "when": "editorTextFocus && !editorReadonly"
    }
]

```
