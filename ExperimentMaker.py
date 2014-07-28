'''
Created on Jul 18, 2014

@author: Nikola Milosevic

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
'''
Created on May 7, 2014

@author: Nikola Milosevic

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from os import listdir
from os.path import isfile, join
import os
from bs4 import BeautifulSoup
from random import randint
import random
import datetime
import shutil 


mypath = 'BMIarticles'
development_data = "dev_data"
cross_validation = "cross_validation_data"
testing_data = "testing_data"
num_dev_data = 60
num_cross_validation = 20
num_testing_data = 20
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
print onlyfiles
print len(onlyfiles)
total_num_data = len(onlyfiles)
num_dev_data = int(total_num_data * ( num_dev_data/100.0))
num_cross_validation = int(total_num_data * (num_cross_validation/100.0))
num_testing_data = int(total_num_data * (num_testing_data/100.0))
tabledocs = []
i=0
#getting documents with table
num_of_docs = total_num_data
random.seed(datetime.datetime.now())
if not os.path.exists(development_data):
    os.makedirs(development_data)
i = 0
while i<num_dev_data:
    index = random.randrange(0, num_of_docs)
    filename = onlyfiles[index]
    shutil.copyfile(mypath+'/'+filename, development_data+'/'+filename)
    folderfiles = [ f for f in listdir(development_data) if isfile(join(development_data,f)) ]
    i = len(folderfiles)
    
if not os.path.exists(cross_validation):
    os.makedirs(cross_validation)
i = 0
while i<num_cross_validation:
    index = random.randrange(0, num_of_docs)
    filename = onlyfiles[index]
    shutil.copyfile(mypath+'/'+filename, cross_validation+'/'+filename)
    folderfiles = [ f for f in listdir(cross_validation) if isfile(join(cross_validation,f)) ]
    i = len(folderfiles)
    
if not os.path.exists(testing_data):
    os.makedirs(testing_data)
i = 0
while i<num_testing_data:
    i = i+1
    index = random.randrange(0, num_of_docs)
    filename = onlyfiles[index]
    shutil.copyfile(mypath+'/'+filename, testing_data+'/'+filename)
    folderfiles = [ f for f in listdir(testing_data) if isfile(join(testing_data,f)) ]
    i = len(folderfiles)
print "This is the end, my only friend, the end"
    