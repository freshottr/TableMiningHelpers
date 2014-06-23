'''
Created on May 12, 2014

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

data = "data_ie"
simple_tables = "data_simple"
simplest_tables = "data_simplest"
evaluation_tables = "eval_tables"
eavluation_information = "eval_info"
eval_num = 30

s_tables  = []
ss_tables = []
if not os.path.exists(evaluation_tables):
    os.makedirs(evaluation_tables)
if not os.path.exists(eavluation_information):
    os.makedirs(eavluation_information)
    
s_tables = [ f for f in listdir(simple_tables) if isfile(join(simple_tables,f)) ]
ss_tables = [ f for f in listdir(simplest_tables) if isfile(join(simplest_tables,f)) ]
tables = []
info = [ f for f in listdir(data) if isfile(join(data,f)) ]
for s in s_tables:
    s = "data_simple/"+s
    tables.append(s)
for s in ss_tables:
    s = "data_simplest/"+s
    tables.append(s)
infos = [ f for f in listdir(data) if isfile(join(data,f)) ]
random.seed(datetime.datetime.now())
num_of_docs = len(tables)
i = 0
selected_files = []
while i<eval_num:
    index = random.randrange(0, num_of_docs)
    filename = tables[index]
    print filename
    #filename = 
    shutil.copyfile(filename, evaluation_tables+'/'+filename.split('/')[1])
    folderfiles = [ f for f in listdir(evaluation_tables) if isfile(join(evaluation_tables,f)) ]
    i = len(folderfiles)
    filen = filename.split('/')[1].split('.')[0]
    print filen
    selected_files.append(filen)
    
for i in info:
    for f in selected_files:
        if(i.startswith(f)):
            shutil.copyfile(data+'/'+i, eavluation_information+'/'+i)
print "Done!"
        
    