import numpy as np
np.random.seed(17)
nproblem = 6 # magic
nstudent = 65 # magic

header = r"""
\examheader{Term Exam 4}

"""

problems = [
r"""\begin{problem} (From Problem Set 6)
\end{problem}
""",
r"""\begin{problem} (From Problem Set 7)
\end{problem}
""",
r"""\begin{problem} (From Problem Set 6)
\end{problem}
""",
r"""\begin{problem} (From Problem Set 7)
\end{problem}
""",
r"""\begin{problem} (From Recitation)
\end{problem}
""",
r"""\begin{problem} (From Lecture)
\end{problem}
""",
]
assert len(problems) == nproblem

print(r"""
\documentclass[12pt, letterpaper]{article}
\include{physics1}
\pagestyle{empty}

\begin{document}

""")

for student in range(nstudent):
    print(header)
    pindx = np.argsort(np.random.uniform(size=nproblem))
    for problem, indx in enumerate(pindx):
        print(problems[indx])
        print(r"""
\vfill ~
""")
        if problem == nproblem // 3:
            print(r"""
\clearpage

""")
    print(r"""
\cleardoublepage

""")

print(r"""
\end{document}
""")
