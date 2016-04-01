import os
import json
import copy
import platform

import sublime
import sublime_plugin

ST3 = int(sublime.version()) >= 3000

EXEC_LINT = "eslint_exec"
LINTER_PATH = os.path.join(
  sublime.packages_path(),
  os.path.dirname(os.path.realpath(__file__)),
  "linter.js"
)

class EslintExecCommand(sublime_plugin.WindowCommand):
  def run(self, files=[]):
    packages = sublime.packages_path()

    default_path = os.path.join(packages, "ESLint", "ESLint.sublime-settings")
    user_path = os.path.join(packages, "User", "ESLint.sublime-settings")
    config_path = os.path.join(packages, "ESLint", ".eslintrc.json")
    update_config(default_path, user_path, config_path)

    if sublime.platform() == "osx":
      path = "/usr/local/bin:" + os.environ["PATH"]
    else:
      path = os.environ["PATH"]

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
    self.window.run_command("exec", args)

class EslintCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.window.run_command(EXEC_LINT, {
      "files": [self.window.active_view().file_name()]
    })

def update_config(default_path, user_path, out_path):
  data = read_json(user_path)
  if not data:
    data = read_json(default_path)

  with open(out_path, "w") as f:
    f.write(data)

def read_json(path):
  if os.path.isfile(path):
    with open(path, "r") as f:
      data = f.read()
    if is_json(data):
      return data

def is_json(data):
  try:
    j = json.loads(data)
  except:
    return False
  return True
