import numpy as np
np.random.seed(17)
nproblem = 6 # magic
nstudent = 65 # magic

header = r"""
\examheader{Term Exam 3}

"""

problems = [
r"""\begin{problem} (From Problem Set 4)
When Prof Hogg bounced a ball in lecture, did it lose more or less than
10 percent of its kinetic energy on the bounce?
\end{problem}
""",
r"""\begin{problem} (From Problem Set 4)
What is the potential energy gain of a typical NYU student who climbs 3 flights of stairs?
Give an answer with units.
\end{problem}
""",
r"""\begin{problem} (From Problem Set 4)
In the block-and-pulley system shown here, let's say that the tension in the long string is $T$.
What is the tension in each of the two shorter strings? Important: \emph{Give your answer in terms of $T$.}
If you need anything other than $T$ for your answer, explain why.
\marginpar{\includegraphics[width=\marginparwidth]{../mp/tackle_blocks.pdf}}
\end{problem}
""",
r"""\begin{problem} (From Problem Set 5)
There was a problem about a softball and a bowling ball.
Were they closer in linear momentum or in kinetic energy?
\end{problem}
""",
r"""\begin{problem} (From Lecture)
What is the period of oscillation a simple pendulum consisting of a string of length $\ell$ holding a mass
mass $m$, swinging in a gravitational field of strength (acceleration) $g$?
\end{problem}
""",
r"""\begin{problem} (From Recitation)
If, in the $x$ direction, the potential is $$U=\frac{1}{2}\,k\,(x-x_0)^2~,$$ what is the corresponding $x$-component $F_x(x)$ of the force?
\end{problem}
"""]
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
