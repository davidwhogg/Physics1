# Makefile for pro directory
#
#   requires that <filename>.pro make <filename>.eps and nothing else
#
# 2001-Dec-03  First cut - Hogg

.SUFFIXES: .pro .eps

ALLFILES = $(patsubst %.pro,%.eps,$(wildcard *.pro))
all: $(ALLFILES)

.pro.eps:
	echo $* | idl

clean:
	/bin/rm -f *.eps
