#!/usr/bin/env python
import sys
sys.path.insert(0, '.')

from osdagbridge.core.reports.report_generator import preamble

# Generate preamble
latex_pre = preamble('TestProject', 'test rev')

# Check if macro is in the preamble
if r'\TableTitle' in latex_pre:
    print("✓ TableTitle macro found in preamble")
    # Find the line with the macro
    for i, line in enumerate(latex_pre.split('\n')):
        if 'TableTitle' in line:
            print(f"  Line {i}: {line}")
else:
    print("✗ TableTitle macro NOT found in preamble")

# Check if preamble ends properly
if r'\begin{document}' in latex_pre:
    print("✓ \\begin{document} found")
else:
    print("✗ \\begin{document} NOT found")

# Check for any obvious syntax errors
import re
# Count braces
open_braces = latex_pre.count('{')
close_braces = latex_pre.count('}')
print(f"\nBrace count: {open_braces} open, {close_braces} close")
if open_braces != close_braces:
    print(f"  WARNING: Unmatched braces! Difference: {open_braces - close_braces}")
    
# Save a snippet for inspection
with open('test_latex_snippet.tex', 'w', encoding='utf-8') as f:
    # Write minimal LaTeX to test the macro
    f.write(r"""\documentclass{report}
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage{longtable}
            \setlength{\LTleft}{\fill}
            \setlength{\LTright}{\fill}
\usepackage{array}
\usepackage{colortbl}
\usepackage{booktabs}
\usepackage{fancyhdr}
\usepackage{setspace}
\setstretch{1.15}
\newcommand{\TableTitle}[1]{\noindent\textbf{#1}}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
\newcolumntype{C}[1]{>{\centering\arraybackslash}p{#1}}
\begin{document}
\TableTitle{Table 1 -- Test}
\end{document}
""")

print("\nCreated test_latex_snippet.tex")
