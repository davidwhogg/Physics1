import numpy as np
np.random.seed(17)
nproblem = 6 # magic
nstudent = 65 # magic

header = r"""
\examheader{Term Exam 3}

"""

problems = [
r"""\begin{problem} (From Problem Set 4)
A typical, healthy NYU student climbs 10 stories of stairs.
What is the potential-energy gain of the student?
\end{problem}
""",
r"""\begin{problem} (From Problem Set 4)
A car is going around a banked curve (banked at $15\,\deg$) at $70\,\mph$, which is faster than the ``natural'' speed for the banked turn.
The car is held to the road by static friction.
Draw a free-body diagram showing the forces on the car while it's in the turn.
\end{problem}
""",
r"""\begin{problem} (From Problem Set 5)
A student of mass $m_\mathrm{student}=80\,\kg$ stands at rest next to
a block of ice of mass $m_\mathrm{ice}=320\,\kg$, also at rest, on a
frictionless frozen lake. The student pushes on the block until the
block is moving away from the student at $1.5\,\mps$ (that is, until
$\left|\vec{v}_\mathrm{ice}-\vec{v}_\mathrm{student}\right|=1.5\,\mps$).
How much work did the student do?  Give your answer in $\J$.
\end{problem}
""",
r"""\begin{problem} (From Recitation)
If a ball bounces off of a wall, the angle of incidence equals the angle
of reflection. What do you have to assume to make that true?
\end{problem}
""",
r"""\begin{problem} (From Lecture 2024-10-03)
A block of mass $4\,M$ is moving at speed $u$ in the $+\hat{x}$ direction,
and a block of mass $M$ is moving at speed $u$ in the $-\hat{x}$ direction.
What is the velocity of the center of mass of this two-block system?
\end{problem}
""",
r"""\begin{problem} (From Recitation)
Consider a mass $M$ on a spring of spring constant $k$, released from
rest at $t=0$ but from a distance $X$ (in the $x$-direction, which is
parallel to the spring) away from the equilibrium position for the
mass.  Assume there are no other forces acting!
What is the total mechanical energy (kinetic plus potential) of this system?
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
