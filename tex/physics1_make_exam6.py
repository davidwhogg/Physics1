import numpy as np
np.random.seed(17)
nproblem = 6 # magic
nstudent = 60 # magic

header = r"""
\examheader{Term Exam 6}

"""

problems = [
r"""\begin{problem} (From Problem Set 10)
If the center of mass of a car is at a height $h=0.75\,\m$ above the ground,
and if the car is accelerating at $a=4\,\mpss$,
and if the car has a mass of $M=1000\,\kg$,
and if you put your reference point on the ground,
what is the magnitude of the net torque on the car?
Give a numerical answer in SI units.
\end{problem}
""",
r"""\begin{problem} (From Problem Set 11)
A thin hoop of radius $R=0.05\,\m$ and mass $m=0.1\,\kg$ rolls without slipping down an inclined plane.
A solid ball of radius $R=0.02\,\m$ and mass $m=0.05\,\kg$ rolls without slipping down that same plane.
Which one has the larger acceleration $|\vec{a}|$, and \emph{why?}
\end{problem}
""",
r"""\begin{problem} (From Problem Set 10)
Immediately after being hit, at $t=0$, a cue ball of mass
$M$ and radius $R$ slides along the felt at speed $v_i$, not rotating
at all.  As time goes on, the ball slows down (because of friction)
and, at the same time, starts to spin.
Plot the speed $v(t)$ and ``spin speed'' $R\,\omega(t)$ vs time $t$ on a single plot.
Clearly label the axes, the levels $v=0$ and $v=v_i$, and which line is which.
\end{problem}
""",
r"""\begin{problem} (From Problem Set 11)
Which has a larger magnitude?
The spin angular momentum of the Earth or the orbital angular momentum
of the Earth?
\end{problem}
""",
r"""\begin{problem} (From Recitation)
Consider these three events:
$$A=(c\,t_A,x_A)=(0\,\m,0\,\m), ~ B=(1\,\m,3\,\m), ~ C=(1\,\m,0\,\m).$$
What is the interval $(\Delta s)_{AB}^2$ between events $A$ and $B$
and the interval $(\Delta s)_{AC}^2$ between events $A$ and $C$?
\end{problem}
""",
r"""\begin{problem} (From Lecture)
What is the law from Kepler that relates the semi-major axis $a$ of a planet's orbit
to the period $T$ of the planet's orbit?
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
