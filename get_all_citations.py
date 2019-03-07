"""
Simple script to gather all of the included bibtex
citation information for all papers and print
to screen.

Simply run as:
  $ python get_all_citations.py
"""

import glob
import numpy as np

def grab_files(fpath = "."):
    files = np.sort(glob.glob(fpath + '/*/citation.bib'))
    return files

def print_files(files):

    for fname in files:
        f = open(fname,'r')
        print (f.read())
        f.close()

    return


if __name__ == "__main__":

    files = grab_files()
    print_files(files)
