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


mypath = 'PMC_data'
development_data = "dev_data"
cross_validation = "coross_validation_data"
testing_data = "testing_data"
docs_with_tables = "data_with_tables"
num_dev_data = 100
num_cross_validation = 20
num_testing_data = 100
if not os.path.exists(docs_with_tables):
    os.makedirs(docs_with_tables)
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
print onlyfiles
print len(onlyfiles)
tabledocs = []
i=0
num_of_tables = 0
#getting documents with table
num_of_docs = 0
for fname in onlyfiles:
    print fname
    path = mypath+'/'+fname
    file = open(path,'r')
    xml = file.read()
    parsed_html = BeautifulSoup(xml)
    if parsed_html.body!= None :
        data_table = parsed_html.body.findAll('table-wrap')
    tables_in_doc = len(data_table)
    if(data_table!=None and tables_in_doc!=0):
        table_file = open(docs_with_tables+'/'+fname,'w')
        table_file.write(xml)
        table_file.close()
        tabledocs.append(fname)
        num_of_docs = num_of_docs + 1 
    file.close()
    num_of_tables = num_of_tables+tables_in_doc

print 'Total number of tables:' + str(num_of_tables)
print 'Total number of documents with tables:' + str(num_of_docs)
random.seed(datetime.datetime.now())
if not os.path.exists(development_data):
    os.makedirs(development_data)
i = 0
while i<num_dev_data:
    index = random.randrange(0, num_of_docs)
    filename = tabledocs[index]
    shutil.copyfile(docs_with_tables+'/'+filename, development_data+'/'+filename)
    folderfiles = [ f for f in listdir(development_data) if isfile(join(development_data,f)) ]
    i = len(folderfiles)
    
if not os.path.exists(cross_validation):
    os.makedirs(cross_validation)
i = 0
while i<num_cross_validation:
    index = random.randrange(0, num_of_docs)
    filename = tabledocs[index]
    shutil.copyfile(docs_with_tables+'/'+filename, cross_validation+'/'+filename)
    folderfiles = [ f for f in listdir(cross_validation) if isfile(join(cross_validation,f)) ]
    i = len(folderfiles)
    
if not os.path.exists(testing_data):
    os.makedirs(testing_data)
i = 0
while i<num_testing_data:
    i = i+1
    index = random.randrange(0, num_of_docs)
    filename = tabledocs[index]
    shutil.copyfile(docs_with_tables+'/'+filename, testing_data+'/'+filename)
    folderfiles = [ f for f in listdir(testing_data) if isfile(join(testing_data,f)) ]
    i = len(folderfiles)
print "This is the end, my only friend, the end"
    