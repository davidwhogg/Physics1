import numpy as np
np.random.seed(17)
nproblem = 6 # magic
nstudent = 90 # magic

problems = [
r"""\begin{problem} (From Lecture 2025-09-02)
Which of the options (the options we gave in Lecture) for the mass of the Earth was closest to being correct?
The options were $10^6\,\kg$, $10^{12}\,\kg$, $10^{18}\,\kg$, and $10^{24}\,\kg$.
\end{problem}
""",
r"""\begin{problem} (From Recitation on integration)
If, in one row of your table (or spreadsheet), the time is $3.1\,\s$, the position is $0.9\,\m$, the velocity is $-2.0\,\m\,\s^{-1}$, and the acceleration is $-10.0\,\m\,\s^{-2}$, what is the \emph{position} at the next time step? Imagine that you are using a time step of $0.1\,\s$.
\end{problem}
""",
r"""\begin{problem} (From Lecture 2025-09-16)
One of the guesses for the acceleration $|\vec{a}|$ of the block down the inclined plane was
$|\vec{g}| / \sin\theta$. Give a very simple verbal argument that this answer must be wrong.
Give your answer in fewer than 40 words.
\end{problem}
""",
r"""\begin{problem} (From Problem Set 1)
Imagine you have a mass $M$, a length $h$, and a velocity $v$.
What is a combination of these that you can make that will
have units of force?
\end{problem}
""",
r"""\begin{problem} (From Problem Set 1)
If a truck gets 13.5~miles to the gallon, how many liters of fuel
does it take to go 100~km?
(\textsl{Hint:
You don't have to completely re-do the calculation you did for the Problem Set, since the number in the Problem Set was $27=2\times 13.5$.})
\end{problem}
""",
r"""\begin{problem} (From Recitation on pulleys)
Why do we approximate the strings as \emph{inextensible}?
How does that simplify problems with blocks and pulleys?
Give your answer in fewer than 40 words.
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
    print(r"""
\examheader{Term Exam 1}

""")
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
