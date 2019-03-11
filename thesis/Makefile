#
# Makefile to compile thesis and easily clean up
# directory of all generated files
#


NAME=thesis

LATEX=pdflatex 

#all:  $(NAME).pdf


#
# Quickly compile pdf without re-generating
# proper citations or labels.
#
quick: $(NAME).tex
	$(LATEX) $(NAME)


# Complete compile to .dvi
dvi: $(NAME).tex
	$(LATEX) $(NAME) || true
	bibtex $(NAME)
	$(LATEX) $(NAME) || true 
	bibtex $(NAME)
	$(LATEX) $(NAME) || true 
	$(LATEX) $(NAME)

# Complete compile to .pdf
pdf: $(NAME).tex
	$(LATEX) $(NAME) || true
	bibtex $(NAME)
	$(LATEX) $(NAME) || true 
	bibtex $(NAME)
	$(LATEX) $(NAME) || true 
	$(LATEX) $(NAME) || true 
#	dvipdf $(NAME).dvi $(NAME).pdf
#	rm -f $(NAME).blg $(NAME).log $(NAME).aux

#
# clean up files
#
clean:
	rm -f *~ *.aux *.dvi *.gz *.out *.toc *.lof *.lot *log *-temp.* *.blg *~ $(NAME).ps $(NAME).bbl $(NAME).pdf msNotes.bib




