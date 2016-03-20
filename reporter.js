module.exports = function(results) {
  'use strict';

  var lines = [];
  var title = 'error';

  function numberWang(wangaNumb) {
    var thatsNumberWang = 5 - wangaNumb;
    var stayNumberWang = '';
    var i;

    for (i = 0; i < thatsNumberWang; i += 1) {
      stayNumberWang += ' ';
    }

    return stayNumberWang;
  }

  lines.push('[ESLint: ' + results[0].filePath + ']');
  lines.push('');

  var errorCount = results[0].errorCount;
  var messages = results[0].messages;

  if (errorCount) {
    if (errorCount > 1) {
      title += 's';
    }

    messages.forEach(function(error) {
      var ruleId = error.ruleId ? ' (' + error.ruleId + ')' : '';

      lines.push([
        numberWang((error.line + error.column.toString()).length),
        error.line + ',' + error.column + ':',
        error.message + ruleId
      ].join(' '));
    });

    lines.push('');
    lines.push(
      '✗ ' + errorCount + ' ' + title +
      ', double-click above, [F4] for next, [shift-F4] for previous.'
    );
  } else {
    lines.push('✓ 0 errors, [esc] to hide.');
  }

  lines.push('');
  console.log(lines.join('\n'));
};
