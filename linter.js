'use strict';

var MAX_WARNINGS = 7;

var path = require('path');
var CLIEngine = require('eslint').CLIEngine;

var args = process.argv.slice(2);
var targetPath = args[0];
var configPath = path.join(__dirname, '.eslintrc.json');

var cli = new CLIEngine({
  configFile: configPath
});

var report = cli.executeOnFiles([targetPath]);
console.log(format(report.results)); // eslint-disable-line no-console


function format(results) {
  var lines = [];
  var title = 'error';

  function numberWang(wangaNumb) {
    var thatsNumberWang = 7 - wangaNumb;
    var stayNumberWang = '';
    var i;

    for (i = 0; i < thatsNumberWang; i++) {
      stayNumberWang += ' ';
    }

    return stayNumberWang;
  }

  lines.push('[ESLint: ' + results[0].filePath + ']');
  lines.push('');

  var messages = results[0].messages;
  var errorCount = results[0].errorCount || 0;
  var warningCount = results[0].warningCount || 0;
  var count = 0;

  errorCount += warningCount;

  if (errorCount) {
    if (errorCount > 1) {
      title += 's';
    }

    messages.forEach(function(error) {
      if (count > MAX_WARNINGS) {
        return;
      }

      var ruleId = error.ruleId ? ' (' + error.ruleId + ')' : '';

      lines.push([
        numberWang((error.line + error.column.toString()).length),
        error.line + ',' + error.column + ':',
        error.message + ruleId
      ].join(' '));
      count++;
    });

    lines.push('');
    lines.push(
      '✗ ' + count + ' ' + title +
      ', double-click above, [F4] for next, [shift-F4] for previous.'
    );
  } else {
    lines.push('✓ 0 errors, [esc] to hide.');
  }

  lines.push('');
  return lines.join('\n');
}
