import os
import sublime
import sublime_plugin

SETTINGS_KEY = 'ESLint.sublime-settings'
DEFAULT_NODE_PATH = ''
DEFAULT_NODE_MODULES_PATH = ''
DEFAULT_CONFIGFILE = ''

class Preferences:
    def load(self, settings):
        self.node_path = settings.get('node_path', DEFAULT_NODE_PATH)
        self.node_modules_path = settings.get('node_modules_path', DEFAULT_NODE_MODULES_PATH)
        self.config_file = self.expand_path_variables(settings.get('config_file', DEFAULT_CONFIGFILE))

    def expand_path_variables(self, path):
        """Expand Sublime Text and environment variables in the given path."""
        if not path:
            return ''

        window = sublime.active_window()
        if not window:
            return ''

        try:
            # Standard Sublime variables
            variables = window.extract_variables()

            # Common Sublime-specific paths
            variables.update({
                'packages': sublime.packages_path(),
                'installed_packages': sublime.installed_packages_path(),
                'platform': sublime.platform()
            })

            # Add environment variables if needed
            if '${env:' in path or '$env:' in path:
                variables.update({'env:' + k: v for k, v in os.environ.items()})

            # Expand variables
            expanded = sublime.expand_variables(path, variables)

            # Normalize the final path
            normalized = os.path.normpath(os.path.expanduser(expanded))

            # Check if the resulting path exists
            if not os.path.exists(normalized):
                print("[ESLint] File or directory not found: {}".format(normalized))
                return ''

            return normalized

        except Exception:
            print("[ESLint] An error occurred: {}".format(e))
            return ''

Pref = Preferences()

def plugin_loaded():
    def init():
        settings = sublime.load_settings(SETTINGS_KEY)
        Pref.load(settings)
        settings.add_on_change('reload', lambda: Pref.load(settings))

    sublime.set_timeout(init, 0)  # UI tamamen hazır olana kadar bekle

class EslintExecCommand(sublime_plugin.WindowCommand):
    def run(self, files=[]):
        packages = sublime.packages_path()
        linter_path = os.path.join(packages, 'ESLint', 'linter.js')
        node_modules_path = os.path.expandvars(os.path.expanduser(Pref.node_modules_path))
        config_file = os.path.expandvars(os.path.expanduser(Pref.config_file))

        path = Pref.node_path
        if not path:
            if sublime.platform() == 'osx':
                path = '/usr/local/bin:' + os.environ['PATH']
            else:
                path = os.environ['PATH']

        args = {
            'cmd': [
                'node',
                linter_path,
                files[0],
                node_modules_path,
                config_file
            ],
            'path': path,
            'file_regex': r'ESLint: (.+)\]',
            'line_regex': r'(\d+),(\d+): (.*)$'
        }
        self.window.run_command('exec', args)


class EslintCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command('eslint_exec', {
            'files': [self.window.active_view().file_name()]
        })

if int(sublime.version()) < 3000:
    plugin_loaded()
