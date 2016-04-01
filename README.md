# ESLint for Sublime Text

Lint ECMAScript/JavaScript syntax by [ESLint][ESLint Official] in [Sublime Text 2][Sublime Text 2] and [3][Sublime Text 3].

## Features

* Support for [ECMAScript 6 (ES2015)+][ECMAScript 6] and [JSX][JSX]

## Prerequisites

* [Sublime Package Control][Package Control]
* [Node.js][Node.js]
* [eslint][ESLint Official GitHub]

## Installation

### Install Node.js and eslint

Before using this plugin, you must ensure that `eslint` is installed on your system.  
To install `eslint`, do the following:

1. Install [Node.js][Node.js] (and [npm][npm] on Linux).

2. Install `eslint` globally by typing the following in a terminal:
   ```bash
   npm install -g eslint
   ```

### Install plugin

Install this plugin by using Sublime Text [Package Control][Package Control].

1. Open **"Command Pallet"** <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>p</kbd> (<kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>p</kbd> on OSX)
2. Select **"Package Control: Install Package"**
3. Select **ESLint**

## Run ESLint

ESLint an active JavaScript file.


* Open the context menu (right-click), and Select **ESLint**
  Or Open "Command Pallet" and Select **ESLint**
  Or keyboard shortcut: <kbd>Alt</kbd> + <kbd>e</kbd> (<kbd>Option</kbd> + <kbd>e</kbd> on OSX)

* <kbd>F4</kbd> : Jump to next error row/column
* <kbd>Shift</kbd> + <kbd>F4</kbd> : Jump to previous error row-column

**Note:**
The <kbd>Alt</kbd> + <kbd>e</kbd> (<kbd>Option</kbd> + <kbd>e</kbd> on OSX) shortcut changes the Build System on the current file to ESLint,
then Builds to run ESLint on the file and output any errors for jumping to within the file.
You could alternatively set the Build System to Automatic and <kbd>Ctrl</kbd> + <kbd>b</kbd> (<kbd>Cmd</kbd> + <kbd>b</kbd> on OSX) or <kbd>F7</kbd>,
but only on files that end with `.js`.

## ESLint on save

Install [SublimeOnSaveBuild][SublimeOnSaveBuild]

## Configuring ESLint

[ESLint][ESLint Official] allows you to specify the JavaScript language options you want to support by using `.eslintrc` file.

This plugin's settings file has the same meaning as the `.eslintrc` file.
By default ("`Preferences` / `Package Settings` / `HighlightAnything` / `Settings - Default`"), ESLint plugin supports [ECMAScript 6][ECMAScript 6] and [JSX][JSX] syntax.
You can override that setting in "`Preferences` / `Package Settings` / `HighlightAnything` / `Settings - User`", as JSON.


Example:

```javascript
{
  "extends": "eslint:recommended",
  "parserOptions": {
    "ecmaVersion": 6,
    "sourceType": "module",
    "ecmaFeatures": {
      "jsx": true
    }
  },
  "env": {
    "es6": true,
    "browser": true
  },
  "rules": {
    "no-console": "off",
    "no-unused-vars": "off"
  }
}
```


### Example for support the [React][React] plugin.

If you installed ESLint globally, you have to install [React plugin][React plugin] globally too.

```bash
npm install -g eslint-plugin-react
```

Add plugins section and specify ESLint-plugin-React as a plugin.

```javascript
{
  ...
  "rules": {
    "react/jsx-uses-vars": "warn"
  },
  "plugins": [
    "react"
  ]
}
```


[ESLint Official]: http://eslint.org/
[Sublime Text 2]: http://www.sublimetext.com/2
[Sublime Text 3]: http://www.sublimetext.com/3
[ECMAScript 6]: http://www.ecma-international.org/publications/standards/Ecma-262.htm
[React]: https://facebook.github.io/react/
[JSX]: https://facebook.github.io/jsx/
[Package Control]: http://wbond.net/sublime_packages/package_control/installation
[Node.js]: https://nodejs.org/
[ESLint Official GitHub]: https://github.com/eslint/eslint
[npm]: https://nodejs.org/en/download/package-manager/
[SublimeOnSaveBuild]: https://github.com/alexnj/SublimeOnSaveBuild
[React plugin]: https://github.com/yannickcr/eslint-plugin-react
