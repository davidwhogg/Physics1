import numpy as np
np.random.seed(17)
nproblem = 6 # magic
nstudent = 70 # magic

header = r"""
\examheader{Term Exam 5}

"""

problems = [
r"""\begin{problem} (From Problem Set 8)
If
$$ x(t) = A\,\e^{-\frac{\gamma}{2}\,t}\,\cos (\omega\,t + \phi) ~,$$
then what is $\dd x/\dd t$?
\end{problem}
""",
r"""\begin{problem} (From Recitation)
What is the mass of the Milky Way, approximately, in terms of the mass of the Sun?
\end{problem}
""",
r"""\begin{problem} (From Problem Set 8)
A very thin ladder of length $L$ and mass $M$ leans against a vertical
wall, on a horizontal floor, making an angle of $\theta$ with respect
to the wall.  Imagine that there is a large coefficient of friction
$\mu$ at the floor so that the ladder is in static
equilibrium, but assume that the wall is effectively frictionless.
Draw a free-body diagram for the ladder, showing all
forces acting, and where (on the ladder) that they act.
\end{problem}
""",
r"""\begin{problem} (From Lecture)
How is $g$ (the acceleration due to gravity at the surface of the Earth) related
to the total mass $M$ and radius $R$ of the Earth? Give a symbolic expression using
whatever constants you need.
\end{problem}
""",
r"""\begin{problem} (From Recitation)
If a flatbed truck is moving at speed $v_t$ in the $x$ direction relative to the ground,
and a pipe is moving at speed $v_p$ in the $x$ direction with respect to the ground,
and the pipe is rolling without slipping on the truck bed,
at what angular speed $\omega$ is the pipe turning? Don't worry about sign, just give me a magnitude.
\end{problem}
""",
r"""\begin{problem} (From Recitation)
The year is roughly 360 days long.
If the Earth were four times less massive than it is, but were still on a
circular orbit around our Sun at its current radius, what, roughly, would be the length of the year?
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
