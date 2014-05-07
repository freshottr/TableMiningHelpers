'''
Created on Mar 14, 2014

@author: nikola
'''
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup


mypath = 'PMC_data'
table_path = 'PMC_tables'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
print onlyfiles
i=0
num_of_tables = 0
for fname in onlyfiles:
    print fname
    path = mypath+'/'+fname
    file = open(path,'r')
    xml = file.read()
   # print xml
    parsed_html = BeautifulSoup(xml)
    data_table = parsed_html.body.findAll('table-wrap')
    tables_in_doc = len(data_table)
    if(data_table!=None and tables_in_doc!=0):
        table_file = open(table_path+'/'+fname+'.html','w')
        table_file.write('<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head><body>')
        data = str(data_table).replace('[', '').replace(']', '')
        table_file.write(str(data))
        table_file.write('</body></html>')
        table_file.close()
    file.close()
    num_of_tables = num_of_tables+tables_in_doc
print 'Total number of tables:' + str(num_of_tables)
