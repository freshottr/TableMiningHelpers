'''
Created on Jul 8, 2014

@author: Nikola Milosevic

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from os import listdir
from os.path import isfile, join
import urllib

urllib.urlretrieve("http://www.ncbi.nlm.nih.gov/pmc/articles/PMC17815/table/T1/","T1")