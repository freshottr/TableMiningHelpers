'''
Created on Jul 3, 2014

@author: Nikola Milosevic

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from os import listdir
from os.path import isfile, join
import urllib
import csv
import os
mypath = "data"
PDFDirPath = "pmc-pdfs"
initialPath = "ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/" #Here goes PMCNUM/pdf/
if not os.path.exists(PDFDirPath):
    os.makedirs(PDFDirPath)
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
pmcs = []
for f in onlyfiles:
    f = str.split(f,'.')[0]
    pmcs.append(f)

print pmcs

with open('pmc_file_list.pdf.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    i = 0
    for row in spamreader:
        if(i<>0 and row[3] in pmcs):
            print "downloading "+ row[0]
            filename = str.split(row[0],'/')[-1]
            urllib.urlretrieve(initialPath+row[0],PDFDirPath+"/"+row[3]+".pdf")
        i = i+1
