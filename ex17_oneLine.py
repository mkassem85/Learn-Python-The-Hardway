from sys import argv
from os.path import exists

scritpt, infile, outfile = argv
open(outfile,'w').write((open(infile).read()))
