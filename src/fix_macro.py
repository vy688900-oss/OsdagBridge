from pathlib import Path
import re

p = Path('osdagbridge/core/reports/report_generator.py')
text = p.read_text(encoding='utf-8')

# Check the problematic line
lines = text.split('\n')
for i, line in enumerate(lines[535:545], start=536):
    if 'TableTitle' in line or 'newcommand' in line:
        print(f'Line {i}: {repr(line[:80])}')

# The issue: \t is being interpreted as tab. Fix by using raw approach or simpler macro
# Instead of the complex refstepcounter approach, let's use a simpler label-based method
old_macro_pattern = r'\\newcommand\{\\TableTitle\}.*?\{.*?\}.*?\}'

# Replace with a working macro that doesn't have escape issues
# Use a simpler approach: just output the text without trying to auto-number
new_macro = '\\newcommand{\\TableTitle}[1]{\\noindent\\textbf{Table -- #1}}'

text = re.sub(
    r'\\newcommand\{\\TableTitle\}\[1\]\{[^}]+\}',
    new_macro,
    text
)

p.write_text(text, encoding='utf-8')
print('Fixed macro definition')
