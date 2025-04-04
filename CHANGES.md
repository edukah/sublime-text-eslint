# Sublime Text - ESLint-Formatter - Dynamic Path Variables

## Configuration File Example (`ESLint.sublime-settings`)

```json
{
  "node_path": "",
  "node_modules_path": "${project_path}/node_modules", 
  "config_file": "${project_path}/eslint.config.js"
}
```

## Supported Sublime Text Variables

| Variable               | Description                                      | Example Usage                     |
|------------------------|--------------------------------------------------|-----------------------------------|
| `${project_path}`      | Current project root directory                   | `${project_path}/config`          |
| `${project_name}`      | Project filename without extension               | `${project_name}.eslintrc`        |
| `${project_extension}` | Project file extension                           | `backup.${project_extension}`     |
| `${folder}`            | First folder of current project                  | `${folder}/node_modules`          |
| `${file}`              | Current file's full path                         | `${file}.backup`                  |
| `${file_path}`         | Current file's directory                         | `${file_path}/.eslintrc`          |
| `${file_name}`         | Current filename with extension                  | `backup_${file_name}`             |
| `${file_base_name}`    | Current filename without extension               | `${file_base_name}.min.js`        |
| `${file_extension}`    | Current file extension                           | `${file_extension}.backup`        |
| `${packages}`          | Sublime Text packages directory                  | `${packages}/User/`               |
| `${platform}`          | OS platform (`windows`, `osx`, `linux`)          | `config.${platform}.json`         |
| `${env:VARNAME}`       | System environment variable                      | `${env:APPDATA}/eslint/`          |
| `~`                    | User home directory                              | `~/.eslintcache`                  |

## Typical Use Cases

### 1. Basic Project Setup
```json
{
  "node_path": "${env:NODE_HOME}",
  "node_modules_path": "${project_path}/node_modules",
  "config_file": "${project_path}/eslint.config.js"
}
```

### 2. Multi-Project Configuration
```json
{
  "node_path": "",
  "node_modules_path": "${file_path}/../../node_modules",
  "config_file": "${packages}/User/eslint_defaults.json"
}
```

### 3. Environment-Specific Paths
```json
{
  "node_path": "/usr/local/bin",
  "node_modules_path": "${project_path}/node_modules",
  "config_file": "${env:HOME}/.eslint_${platform}.js"
}
```

### 4. File-Relative Config
```json
{
  "config_path": "${folder}/config/eslint.config.js"
}
```

## Implementation Details

### Modified Functions

```python
    def load(self, settings):
        self.node_path = settings.get('node_path', DEFAULT_NODE_PATH)
        self.node_modules_path = settings.get('node_modules_path', DEFAULT_NODE_MODULES_PATH)
        self.config_file = self.expand_path_variables(settings.get('config_file', DEFAULT_CONFIGFILE))

    def expand_path_variables(self, path):
        """Expand Sublime Text variables in paths ($project_path, $file, etc.)"""
        if not path:
            return path

        window = sublime.active_window()
        if not window:
            return path

        try:
            # Get standard variables
            variables = window.extract_variables()

            # Add common Sublime paths
            variables.update({
                'packages': sublime.packages_path(),
                'installed_packages': sublime.installed_packages_path(),
                'platform': sublime.platform()
            })

            # Handle environment variables if present
            if '${env:' in path:
                for key, value in os.environ.items():
                    variables['env:' + key] = value

            # Perform the expansion
            expanded = sublime.expand_variables(path, variables)
        
            # Normalize path separators and expand user home
            return os.path.normpath(os.path.expanduser(expanded))
            
        except Exception as e:
            # Fail silently by returning original path
            return path
```

## Notes

1. Always use **forward slashes** (`/`) in paths
2. Variables are **case-sensitive** (`${file_path}` works, `${FILE_PATH}` doesn't)
3. Empty `node_path` uses system PATH
4. Paths are automatically normalized to OS format