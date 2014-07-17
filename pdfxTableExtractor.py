'''
Created on Jul 7, 2014

@author: Nikola Milosevic

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
'''
Created on Mar 14, 2014

@author: nikola
'''
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup
import os


mypath = 'pmc-pdfs/pdfxprocessed'
table_path = 'PMC_pdfx_tables'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
print onlyfiles
i=0
if not os.path.exists(table_path):
    os.makedirs(table_path)
num_of_tables = 0
for fname in onlyfiles:
    print fname
    path = mypath+'/'+fname
    file = open(path,'r')
    xml = file.read()
    parsed_html = BeautifulSoup(xml)
    data_table = parsed_html.body.findAll('region', { "class" : "DoCO:TableBox" })
    tables_in_doc = len(data_table)
    if(data_table!=None and tables_in_doc!=0):
        table_file = open(table_path+'/'+fname+'.html','w')
        table_file.write("""<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <style>
         table, td, th,tr {
    border: 1px solid green;
}
</style>
        </head><body>""")
        data=''
        for tab in data_table:
            data+=str(tab)+'<br/><br/><br/>'
        data = data.replace('[', '').replace(']', '')
        table_file.write(str(data))
        table_file.write('</body></html>')
        table_file.close()
    file.close()
    num_of_tables = num_of_tables+tables_in_doc
print 'Total number of tables:' + str(num_of_tables)
print 'DONE!!!'
