import os
import json
import copy
import platform

import sublime
import sublime_plugin

EXEC_LINT = 'eslint_exec'
LINTER_PATH = os.path.join(
  sublime.packages_path(),
  os.path.dirname(os.path.realpath(__file__)),
  'linter.js'
)

class EslintExecCommand(sublime_plugin.WindowCommand):

  def run(self, files=[]):
    packages = sublime.packages_path()

    default_path = os.path.join(packages, "ESLint", "ESLint.sublime-settings")
    user_path = os.path.join(packages, "User", "ESLint.sublime-settings")
    config_path = os.path.join(packages, "ESLint", ".eslintrc.json")
    update_config(default_path, user_path, config_path)

    if sublime.platform() == "osx":
      path = "/usr/local/bin:" + os.environ['PATH']
    else:
      path = os.environ['PATH']

    args = {
      "cmd": [
        "node",
        LINTER_PATH,
        files[0]
      ],
      "path": path,
      "file_regex": r"ESLint: (.+)\]",
      "line_regex": r"(\d+),(\d+): (.*)$"
    }
    self.window.run_command('exec', args)

class EslintCommand(sublime_plugin.WindowCommand):

  def run(self):
    self.window.run_command(EXEC_LINT, {
      'files': [self.window.active_view().file_name()]
    })

def update_config(default_path, user_path, out_path):
  with open(default_path) as f:
    data = json.load(f)

  if os.path.isfile(user_path):
    with open(user_path) as f:
      user_data = json.load(f)
      dict_merge(data, user_data)

  with open(out_path, 'w') as f:
    json.dump(data, f, indent=2)

def dict_merge(target, *args):
  # Merge multiple dicts
  if len(args) > 1:
    for obj in args:
      dict_merge(target, obj)
    return target

  # Recursively merge dicts and set non-dict values
  obj = args[0]
  if not isinstance(obj, dict):
    return obj
  for k, v in obj.iteritems():
    if k in target and isinstance(target[k], dict):
      dict_merge(target[k], v)
    else:
      target[k] = copy.deepcopy(v)
  return target
