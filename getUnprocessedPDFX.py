'''
Created on Jul 7, 2014

@author: Nikola Milosevic

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from os import listdir
from os.path import isfile, join
import os
import shutil

PDFDirPath = "pmc-pdfs"
Processed = "pmc-pdfs/pdfxprocessed"
Unprocessed = "pmc-pdfs/pdfxUnprocessed"
if not os.path.exists(Unprocessed):
    os.makedirs(Unprocessed)
onlyfiles = [ f for f in listdir(PDFDirPath) if isfile(join(PDFDirPath,f)) ]
print onlyfiles
pmcs = []
processedFiles =  [ f for f in listdir(Processed) if isfile(join(Processed,f))]
processedPMCs = []
for f in processedFiles:
    f = str.split(f,'.')[0]
    processedPMCs.append(f)
for f in onlyfiles:
    processedPMC = str.split(f,'.')[0]
    if(not processedPMC in processedPMCs):
        shutil.copyfile(PDFDirPath+"/"+f, Unprocessed+"/"+f)
print "Done!!!"