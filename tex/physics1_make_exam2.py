import numpy as np
np.random.seed(17)
nproblem = 6 # magic
nstudent = 75 # magic

header = r"""
\examheader{Term Exam 2}

"""

problems = [
r"""\begin{problem} (From Problem Set 2)
A drag racer accelerates constantly in a straight line,
starting at rest, for $4\,\s$.
In that time, they go a distance of $400\,\m$.
What is the magnitude $a$ of the acceleration?
\end{problem}
""",
r"""\begin{problem} (From Problem Set 2)
Consider a
stone thrown at $t=0$ precisely upwards (in the $y$ direction, for
definiteness) at $1.5\,\mps$, with an initial position (launch point)
at $y=0$.  Ignore air resistance!  Make exactly one very careful plot of the
vertical velocity $v_y$ of the stone as a function of time for the duration
$0<t<0.4\,\s$.  Carefully label the time of
the peak of the trajectory.
Be very careful to include units with all of your
numbers and labels!
\end{problem}
""",
r"""\begin{problem} (From Problem Set 3)
Draw the free-body diagram for the pulley.

\noindent~\hfill\includegraphics{../mp/pulley_table.pdf}\hfill~
\end{problem}
""",
r"""\begin{problem} (From Problem Set 3)
A package of mass $M$ sits on the floor of an elevator that is accelerating upwards at
acceleration $a$. What is the magnitude $N$ of the normal force on the package?
The acceleration due to gravity is $g$.
\end{problem}
""",
r"""\begin{problem} (From Lecture)
This figure appeared in class; in the end, most students voted for either C or D.
Which is correct? C or D? Imagine that the angle is about $\theta=45\,\deg$

\noindent~\hfill\includegraphics[width=4in]{./delete_me.png}\hfill~
\end{problem}
""",
r"""\begin{problem} (From Recitation)
A block of mass $M$ is on an inclined plane, inclined at an angle $\theta$ to the horizontal.
There is a coefficient of friction $\mu=0.9$ between the block and the plane.
If the plane is angled at something close to 20\,deg, what is the magnitude of the force of friction on the block?
Give your answer as a symbolic answer;
that is, give your answer in terms of $M$, $g$, $\theta$, and $\mu$ (or whatever subset of those you need).
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
