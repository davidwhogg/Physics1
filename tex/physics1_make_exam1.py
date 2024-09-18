import numpy as np
np.random.seed(17)
nproblem = 6 # magic
nstudent = 65 # magic

problems = [
r"""\begin{problem} (From Lecture 2024-09-05)
If the radius of the Moon is about $1/4$ that of the Earth,
and the Moon and Earth are made of similar things,
what is the mass of the Moon?
Give your answer in kg. No need to be precise!
\end{problem}
""",
r"""\begin{problem} (From Recitation)
In Recitation you did a numerical integration of an object falling.
Name one change you could have made to make your numerical integration more accurate.
\end{problem}
""",
r"""\begin{problem} (From Problem Set 1)
Imagine having 1 million US dollars (USD) in the form of 10,000 \$100 bills.
If you stack these bills on top of one another in one tall stack, how tall will the stack be?
(\textsl{Note: In the US, \$100 bills are the same size as US \$20 bills.})
\end{problem}
""",
r"""\begin{problem} (From Problem Set 1)
Imagine you have a mass $M$, a length $h$, a velocity $v$, and an
acceleration $g$. What is a combination of these that you can make that will
have units of energy?
\end{problem}
""",
r"""\begin{problem} (From Problem Set 1)
If a motorcycle gets 54~miles to the gallon, how many liters of fuel
does it take to go 100~km?
(\textsl{Hint:
You don't have to completely re-do the calculation you did for the Problem Set, since the number in the Problem Set was 27 instead of 54!})
\end{problem}
""",
r"""\begin{problem} (From Lecture 2024-09-17)
You considered a block on a plane, inclined at an angle $\theta$ to the horizontal.
Now consider the limiting cases of a horizontal or vertical plane:
What is the magnitude $|\mathbf{N}|$ of the normal force if we set $\theta=0$?
What if we set $\theta=\pi/2$~radians?
Give both answers in $N$, assuming that the gravitational force on the block is $10$~N.
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
