# ESLint for Sublime Text

JavaScript syntax checker: [ESLint](http://eslint.org/) for [Sublime Text](http://www.sublimetext.com/)

*This package is forked from [Sublime JSHint](https://github.com/uipoet/sublime-jshint).*

## Features

- Support for Sublime Text 2 and 3
- Support for [ECMAScript 6 (ES2015)+](http://www.ecma-international.org/publications/standards/Ecma-262.htm) and [React](https://facebook.github.io/react/) [JSX](https://facebook.github.io/jsx/)

## Prerequisites

[Node.js](https://nodejs.org/) and [eslint](https://github.com/eslint/eslint) and [Sublime Package Control](http://wbond.net/sublime_packages/package_control/installation)

## 1. Terminal

Install eslint

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

## Run ESLint

ESLint an active JavaScript file

- `control`-`e` *or* `alt`-`e` in Linux/Windows *or* Tools/Contextual menus *or* the Command Palette
- `F4` jump to next error row/column
- `shift`-`F4` jump to previous error row-column

**Note:**
The `control`-`e`/`alt`-`e` shortcut changes the Build System on the current file to ESLint,
then Builds to run ESLint on the file and output any errors for jumping to within the file.
You could alternatively set the Build System to Automatic and `command`-`b`/`control`-`b`/`F7`,
but only on files that end with .js.

## ESLint on save

Install [SublimeOnSaveBuild](https://github.com/alexnj/SublimeOnSaveBuild)

