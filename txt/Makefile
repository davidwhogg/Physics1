RM = /bin/rm -f
DVIPS = dvips -Ppdf # The -Ppdf option includes fonts but can screw up on
                    # included graphics.  Use with extreme prejudice.
PS2PDF = ps2pdf

.SUFFIXES: .tex .dvi .ps .pdf

ALLFILES = $(patsubst %.tex,%.ps,$(wildcard *.tex))
all: $(ALLFILES) clean

.tex.dvi:
	latex $*
	latex $*

.dvi.ps:
	$(DVIPS) $* -o

.ps.pdf:
	$(PS2PDF) $*.ps

clean:
	$(RM) *.log *.aux *.dvi *.toc *.bbl *.blg

spotless: clean
	$(RM) *.pdf *.ps
