# WARNING: WILL FAIL ON STUFF OLDER THAN 2011 BECAUSE OF pdflatex ISSUES

## BUGS:
## - Doesn't properly account for dependencies on physics1.tex
## - Doesn't use wildcards for exam generation

RM = /bin/rm -f

.SUFFIXES: .tex .dvi .ps .pdf .py

# BUG: Manual listing of exam files
# BUG: Doesn't make on one run of make all
ALLFILES = $(patsubst physics1_make_exam%.py,physics1_exam%.pdf,$(wildcard *.py)) \
	$(patsubst physics1_ps%.tex,physics1_ps%.pdf,$(wildcard *.tex)) \
	$(patsubst physics1_exam%.tex,physics1_exam%.pdf,$(wildcard *.tex)) \
	$(patsubst worksheet_%.tex,worksheet_%.pdf,$(wildcard *.tex)) physics1_final.pdf
all: $(ALLFILES) clean

physics1_exam%.tex: physics1_make_exam%.py
	python3 $< > $@

physics1_exam%.pdf: physics1_exam%.tex

.tex.pdf: $<
	pdflatex $*
	pdflatex $*
	pdflatex $*

clean:
	$(RM) *.log *.aux *.dvi *.toc *.bbl *.blg

spotless: clean
	$(RM) *.pdf *.ps
