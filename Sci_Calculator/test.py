from sympy import symbols, preview, Symbol
x, y = symbols("x,y")
preview(x + y, output='png')
preview(x + y, output='png', viewer='gimp')

preamble = "\\documentclass[10pt]{article}\n" \
           "\\usepackage{amsmath,amsfonts}\\begin{document}"
preview(x + y, output='png', preamble=preamble)

from io import BytesIO
obj = BytesIO()
preview(x + y, output='png', viewer='BytesIO',
        outputbuffer=obj)