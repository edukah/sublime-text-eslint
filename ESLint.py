import os
import json
import copy

import sublime
import sublime_plugin


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


def update_config(default_path, user_path, out_path):
  with open(default_path) as f:
    data = json.load(f)

  if os.path.isfile(user_path):
    with open(user_path) as f:
      user_data = json.load(f)
      #data.update(user_data)
      dict_merge(data, user_data)

  with open(out_path, 'w') as f:
    json.dump(data, f, indent=2)


class EslintCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    filepath = self.view.file_name()
    packages = sublime.packages_path()

    default_path = os.path.join(packages, "ESLint", "ESLint.sublime-settings")
    user_path = os.path.join(packages, "User", "ESLint.sublime-settings")
    config_path = os.path.join(packages, "ESLint", ".eslintrc.json")
    update_config(default_path, user_path, config_path)

    args = {
      "cmd": [
        "eslint",
        filepath,
        "--max-warnings",
        "7",
        "--format",
        os.path.join(packages, "ESLint", "reporter.js"),
        "--config",
        os.path.join(packages, "ESLint", ".eslintrc.json")
      ],
      "file_regex": r"ESLint: (.+)\]",
      "line_regex": r"(\d+),(\d+): (.*)$"
    }

    if sublime.platform() == "windows":
      args['cmd'][0] += ".cmd"
    elif sublime.platform() == "osx":
      args['path'] = "/usr/local/share/npm/bin:/usr/local/bin:/opt/local/bin"

    self.view.window().run_command('exec', args)
