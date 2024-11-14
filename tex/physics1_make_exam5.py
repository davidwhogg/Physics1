import numpy as np
np.random.seed(17)
nproblem = 6 # magic
nstudent = 60 # magic

header = r"""
\examheader{Term Exam 5}

"""

problems = [
r"""\begin{problem} (From Problem Set 8
A long, thin rod of length $L$ and cross-sectional area $A$ and
elastic (Young's) modulus $E$ and mass $M$. What combination of these variables
predicts (by dimensional analysis) the frequency $\omega$ of oscillations of this rod?
\end{problem}
""",
r"""\begin{problem} (From Problem Set 9)
What is the correction to your weight coming from buoyancy, roughly? Express it as a fraction of the magnitude of the gravitational force.
\end{problem}
""",
r"""\begin{problem} (From Problem Set 8)
Imagine you have an unusual friend called ``mini-you'' who is identical to you but
exactly one half your size in every dimension (half as tall, half as wide, half as deep, one-eighth your mass).
You and mini-you both walk at natural stride rates.
What is the ratio $T_\mathrm{you}/T_\mathrm{mini-you}$ of the period $T_\mathrm{you}$ of your natural stride
to the period $T_\mathrm{mini-you}$ of mini-you's natural stride?
\end{problem}
""",
r"""\begin{problem} (From Problem Set 9)
Compare a point $A$ that is at the surface of the ocean
to a point $B$ that is $10\,\m$ below the surface of the ocean.
By how much is the pressure larger at point $B$ than at point $A$?
That is, what is $P_B - P_A$?
Give your answer in SI units.
\end{problem}
""",
r"""\begin{problem} (From Recitation)
The Earth orbits, at a mean distance of $1\,\au$, the Sun.
Imagine instead that the Earth orbits, at the same mean distance, a black hole that is 36 times the the mass of the Sun.
What is the length of the year in this new situation?
\end{problem}
""",
r"""\begin{problem} (From Lecture)
We compared two collisions, one of a rod of mass $m$ and a putty ball of mass $m$, and the other of two putty balls, both of mass $m$.
Both collisions are inelastic, because the putty ``sticks'' or kinetic energy is lost (converted to heat maybe).
In which collision is more kinetic energy lost, or are they both the same?
If one is less and one is more, why?
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
