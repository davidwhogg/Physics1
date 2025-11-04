import numpy as np
np.random.seed(17)
nproblem = 6 # magic
nstudent = 65 # magic

header = r"""
\examheader{Term Exam 4}

"""

problems = [
r"""\begin{problem} (From Problem Set 6)
What is the tension in the cable marked $T_1$ in this problem?
Make the same assumptions that we made in the original problem,
and give your answer in terms of quantities labeled in the diagram (and the acceleration $g$ due to gravity).
\marginpar{\includegraphics[width=\marginparwidth]{../mp/hanging_sign.pdf}}
\end{problem}
""",
r"""\begin{problem} (From Problem Set 7)
We asked you to compute the length of a pendulum that has an oscillation period of $2\,\s$.
What would you have gotten if we had asked you for $8\,\s$?
\textsl{Hint:} That's a factor of 4 longer.
\end{problem}
""",
r"""\begin{problem} (From Problem Set 7)
What tension did you get for the tendon in the arm, holding up the $6\,\kg$ bag?
\end{problem}
""",
r"""\begin{problem} (From Recitation)
A mass on a spring oscillates in position $x$ according to $x(t) = A\,\cos(\omega t)$.
Plot the \emph{$x$ velocity} of this mass as a function of time for two full periods.
Label your plot with the amplitude and period of the oscillation.
That is, make it clear that you know what the amplitude and period are, in terms of $A$ and $\omega$.
Now make a similar plot of the kinetic energy vs time for that same mass, over
the same time interval.
Again, label it with the amplitude and the period.
\end{problem}
""",
r"""\begin{problem} (From Recitation)
Chemists write $P\,V = n\,R\,T$, where $n$ is the number of moles.
Physicists write $P\,V = N\,k\,T$, where $N$ is the number of molecules.
What is the ratio $R/k$?
\end{problem}
""",
r"""\begin{problem} (From Lecture)
Explain, in fewer than 51 words, why buildings in New York City have water towers?
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
