'''
Created on Jun 20, 2014

@author: Nikola Milosevic

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup
import shutil

data_path = 'all_PMC_data'
table_path = 'all_PMC_data_w_tables'

onlyfiles = [ f for f in listdir(data_path) if isfile(join(data_path,f)) ]
#print onlyfiles
i=0
num_of_tables = 0
print 'start loop'
for fname in onlyfiles:
    print fname
    path = data_path+'/'+fname
    destination = table_path+'/'+fname
    file = open(path,'r')
    xml = file.read()
   # print xml
    parsed_html = BeautifulSoup(xml)
    if(parsed_html == None or parsed_html.body==None):
        continue
    data_table = parsed_html.body.findAll('table-wrap')
    tables_in_doc = len(data_table)
    if(data_table!=None and tables_in_doc!=0):
        shutil.copyfile(path, destination)
    file.close()
    num_of_tables = num_of_tables+tables_in_doc
print 'Total number of tables:' + str(num_of_tables)