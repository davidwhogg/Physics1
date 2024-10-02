import numpy as np
np.random.seed(17)
nproblem = 6 # magic
nstudent = 65 # magic

header = r"""
\examheader{Term Exam 2}

"""

problems = [
r"""\begin{problem} (From Problem Set 2)
Consider a
stone thrown at $t=0$ precisely upwards (in the $y$ direction)
at $1.5\,\mps$.  Ignore air resistance!  Make a careful plot of the
the vertical velocity $v_y$
of the stone as a function of time for the duration
$0<t<0.4\,\s$.  Carefully label the time at which the stone reaches
the peak of the trajectory (the highest point it goes).
Be very careful to include units with your
numbers and labels!
\end{problem}
""",
r"""\begin{problem} (From Problem Set 3)
In lecture Prof Hogg did a stunt with a coffee cup and a
quarter. Draw the free-body diagram for the quarter when it was at the
top of the arc (that is, when it was directly overhead).
Assume that there is no air resistance.
\end{problem}
""",
r"""\begin{problem} (From Problem Set 2)
Draw the free-body diagram for the turning airplane (banking at 30\,deg).
Make sure your diagram clearly shows the directions of all the forces in three-dimensional space.
\end{problem}
""",
r"""\begin{problem} (From Recitation)
A block of mass $M$ sits on an inclined plane, inclined at $\theta=20$\,deg to the horizontal.
There is a coeffient of friction of $\mu = 0.9$ between the block and the plane (both static and kinetic friction coefficients are 0.9).
What is the magnitude of the frictional force on the block?
Give your answer in terms of any combination of the symbols $M$, $g$, $\theta$, and $\mu$.
\end{problem}
""",
r"""\begin{problem} (From Lecture 2024-09-19)
We described a car sliding perfectly around a banked turn.
Describe, as accurately and unambiguously as possible, the \emph{direction} of the car's acceleration.
\end{problem}
""",
r"""\begin{problem} (From Recitation)
Why do we assume that strings are inextensible?
Why do we assume that strings are low in mass?
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
