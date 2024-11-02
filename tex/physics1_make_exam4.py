import numpy as np
np.random.seed(17)
nproblem = 6 # magic
nstudent = 65 # magic

header = r"""
\examheader{Term Exam 4}

"""

problems = [
r"""\begin{problem} (From Problem Set 6)
In the static ``hanging sign'' problem, what is the tension $T_1$ in
the upper string? Give your answer as a symbolic expression.
\marginpar{\includegraphics[width=\marginparwidth]{../mp/hanging_sign.pdf}}
\end{problem}
""",
r"""\begin{problem} (From Problem Set 7)
We considered a typical adult holding a
$6\,\kg$ grocery bag by its handle in the hand, with the arm bent at $90\,\deg$.
Roughly what tension did you find in the tendon? Give your answer with clear units.
\end{problem}
""",
r"""\begin{problem} (From Problem Set 6)
In Lecture we dropped a pool ball from a height of about $1\,\m$. It
bounced off of the cement floor. Roughly what was the impulse
delivered to the ball from the floor? Give a numerical answer with clear units.
\end{problem}
""",
r"""\begin{problem} (From Problem Set 7)
A mass $M$ hangs from a spring of spring constant $k$ and natural length $\ell_0$ in
a gravitational field with acceleration $g$. Because of gravity, even at equilibrium,
the spring will be stretched to a new equilibrium length. Write an expression for this
new equilibrium length.
\end{problem}
""",
r"""\begin{problem} (From Recitation)
What---in SI base units---are the units of the product $P\,V$ of a pressure $P$ times a volume $V$?
Recall that the base units are $\kg$, $\m$, and $\s$.
\end{problem}
""",
r"""\begin{problem} (From Lecture)
An ice cube floats in a glass of water.
When the ice cube melts, does the water level go up or down or stay the same?
Explain why.
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
