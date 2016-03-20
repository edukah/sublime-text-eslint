# ESLint for Sublime Text

JavaScript/ECMAScript syntax checker: [ESLint](http://eslint.org/) for [Sublime Text 2](http://www.sublimetext.com/2)

*This package is forked from [Sublime JSHint](https://github.com/uipoet/sublime-jshint).*

## Prerequisites

[eslint](https://github.com/eslint/eslint) and [Sublime Package Control](http://wbond.net/sublime_packages/package_control/installation)

### Mac OSX

Installing node with homebrew or macports is assumed.
The path to eslint is hardcoded in this plugin as `/usr/local/share/npm/bin:/usr/local/bin:/opt/local/bin`.
There is no reliable way to get the path from your environment.

### Linux

Make sure eslint is in your environment path.

### Windows

Installing node with the Windows Installer from [Node.js](https://nodejs.org/) is assumed.

## 1. Terminal

```bash
npm install -g eslint
```
    
**Note:**
ESLint will use the first `.eslintrc` file found traversing from the active file in Sublime Text up to your project's root.

## 2. Sublime Text Package Control

- `command`-`shift`-`p` *or* `control`-`shift`-`p` in Linux/Windows
- type `install p`, select `Package Control: Install Package`
- type `eslint`, select `ESLint`

**Note:**
Without Sublime Package Control, you could manually clone to Packages directory as 'ESLint', exactly.

## 3. ESLint an active JavaScript file

- `control`-`j` *or* `alt`-`j` in Linux/Windows *or* Tools/Contextual menus *or* the Command Palette
- `F4` jump to next error row/column
- `shift`-`F4` jump to previous error row-column

**Note:**
The `control`-`e`/`alt`-`e` shortcut changes the Build System on the current file to ESLint,
then Builds to run ESLint on the file and output any errors for jumping to within the file.
You could alternatively set the Build System to Automatic and `command`-`b`/`control`-`b`/`F7`,
but only on files that end with .js.

## ESLint on save

Install [SublimeOnSaveBuild](https://github.com/alexnj/SublimeOnSaveBuild)

