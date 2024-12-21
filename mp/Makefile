# Makefile for mp directory
#
# 2000-Aug-22  First cut - Hogg
# 2000-Dec-10  Look Ma, no explicit file list! - Hogg
# 2001-Jan-14  Added mpx* to clean - Greg
# 2002-Oct-19  make proper eps files - Hogg
# 2013-Sep-22  add epspdf dependency, which SUCKS - Hogg

.SUFFIXES: .mp .eps .pdf

ALLFILES = $(patsubst %.mp,%.pdf,$(wildcard *.mp))
all: $(ALLFILES)

.eps.pdf:
	epstopdf $< $@
#	epspdf $< $@

.mp.eps:
	./mp2eps $*

clean:
	/bin/rm -f *.[1-9] *.log *.mpx mpx* *.dvi *.aux *.1
