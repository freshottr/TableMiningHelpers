'''
Created on 19 Jan 2015

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup
import shutil

data_path = 'data'
table_path = 'data_wo_thead'

onlyfiles = [ f for f in listdir(data_path) if isfile(join(data_path,f)) ]
#print onlyfiles
i=0
num_of_tables = 0
tables_in_doc = 0
print 'start loop'
for fname in onlyfiles:
    print fname
    path = data_path+'/'+fname
    destination = table_path+'/'+fname
    print 'Opening file'
    file = open(path,'r')
    xml = file.read()
    print 'File opened'
    
    parsed_html = BeautifulSoup(xml)
    print 'xml parsed'
    if(parsed_html == None or parsed_html.body==None):
        continue
    print 'Looking table wrap'
    data_table = parsed_html.body.findAll('table-wrap')
    if(data_table!=None and len(data_table)!=0):
        for x in range(0,len(data_table)):
            print 'Looking thead'
            thead = data_table[x].findAll('thead')
            print 'Looking thead finished'
            if(thead==None or len(thead)==0):
                shutil.copyfile(path, destination)
                print 'Copied'
                tables_in_doc = len(thead)
    file.close()
    num_of_tables = num_of_tables+tables_in_doc
print 'Total number of tables:' + str(num_of_tables)