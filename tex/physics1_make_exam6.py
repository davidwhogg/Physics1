import numpy as np
np.random.seed(17)
nproblem = 6 # magic
nstudent = 65 # magic

header = r"""
\examheader{Term Exam 6}

"""

problems = [
r"""\begin{problem} (From Problem Set 9)
There is a buoyancy force acting on anything immersed in air.
Consider a student who has a mass of $70\,\kg$.
Roughly what is the buoyant force (magnitude and direction) acting
on the student in this classroom (which is filled with air)?
If you need to work out the student's volume, remember that students
are (to very good approximation), \emph{entirely water}.
\end{problem}
""",
r"""\begin{problem} (From Problem Set 10)
American SUVs are taller than American sedans.
Let's compare a SUV and a sedan that both have a mass of $1000\,\kg$.
The sedan has a center of mass that is $0.5\,\m$ above the ground,
and the SUV has a center of mass that is $1.0\,\m$ above the ground.
What magnitude of torque does each type of car need to produce in order to accelerate horizontally at $5\,\mpss$?
Give your two numbers with good units.
If you have to assume anything else to answer these questions, state your additional assumptions.
\end{problem}
""",
r"""\begin{problem} (From Problem Set 9)
A bungy cord has natural length $\ell_0=5\,\m$ and spring constant $k=400\,N\,\m^{-1}$.
What is the magnitude of the force applied by the bungy cord when it is stretched to a total length $\ell=8\,\m$?
Give a number with units.
\end{problem}
""",
r"""\begin{problem} (From Problem Set 10)
Consider an ice cube floating in a glass of water at
0\,C.  The ice cube melts at constant temperature, such that you end
up with a glass of water at 0\,C. As it melts, does the water level go
up, or go down, or stay the same? Give an explanation in words (not
equations) that is \emph{shorter than 51 words}.
\end{problem}
""",
r"""\begin{problem} (From Recitation)
Consider these three events:
$$A=(c\,t_A,x_A)=(1\,\m,1\,\m), ~ B=(1\,\m,3\,\m), ~ C=(3\,\m,0\,\m).$$
What is the interval $(\Delta s)_{AB}^2$ between events $A$ and $B$
and the interval $(\Delta s)_{AC}^2$ between events $A$ and $C$?
\end{problem}
""",
r"""\begin{problem} (From Lecture)
The astronauts traveled from the Moon to Earth by ``dropping radially'' onto the Earth.
That is, they went on a radial orbit (a very high eccentricity orbit).
If the moon is $3.8\times 10^{8}\,\m$ away from the Earth, what is the semi-major
axis of this transfer orbit? If you needed to assume anything to answer the question,
state what you assumed.
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
