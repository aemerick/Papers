#
# Makefile to compile thesis and easily clean up
# directory of all generated files
#


NAME=thesis

LATEX=pdflatex 

#all:  $(NAME).pdf

dvi: $(NAME).tex
	$(LATEX) $(NAME) || true
	bibtex $(NAME)
	$(LATEX) $(NAME) || true 
	bibtex $(NAME)
	$(LATEX) $(NAME) || true 
	$(LATEX) $(NAME)

pdf: $(NAME).tex
	$(LATEX) $(NAME) || true
	bibtex $(NAME)
	$(LATEX) $(NAME) || true 
	bibtex $(NAME)
	$(LATEX) $(NAME) || true 
	$(LATEX) $(NAME) || true 
#	dvipdf $(NAME).dvi $(NAME).pdf
	rm -f $(NAME).blg $(NAME).log $(NAME).aux

clean:
	rm -f *~ *.aux *.dvi *.gz *.out *.toc *.lof *.lot *log *-temp.* *.blg *~ $(NAME).ps $(NAME).bbl $(NAME).pdf msNotes.bib




