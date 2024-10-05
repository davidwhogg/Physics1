# WARNING: WILL FAIL ON STUFF OLDER THAN 2011 BECAUSE OF pdflatex ISSUES

## BUGS:
## - Doesn't properly account for dependencies on physics1.tex
## - Doesn't use wildcards for exam generation

RM = /bin/rm -f

.SUFFIXES: .tex .dvi .ps .pdf

# BUG: Manual listing of exam files
# BUG: Doesn't make on one run of make all
ALLFILES = physics1_exam1.pdf physics1_exam2.pdf \
	$(patsubst physics1_ps%.tex,physics1_ps%.pdf,$(wildcard *.tex)) \
	$(patsubst physics1_exam%.tex,physics1_exam%.pdf,$(wildcard *.tex)) \
	$(patsubst worksheet_%.tex,worksheet_%.pdf,$(wildcard *.tex)) physics1_final.pdf
all: $(ALLFILES) clean

# BUG / FIXME: Make this with wildcards
physics1_exam1.tex: physics1_make_exam1.py
	python3 physics1_make_exam1.py > $@

# BUG / FIXME: Make this with wildcards
physics1_exam2.tex: physics1_make_exam2.py
	python3 physics1_make_exam2.py > $@

.tex.pdf: $<
	pdflatex $*
	pdflatex $*
	pdflatex $*

clean:
	$(RM) *.log *.aux *.dvi *.toc *.bbl *.blg

spotless: clean
	$(RM) *.pdf *.ps
