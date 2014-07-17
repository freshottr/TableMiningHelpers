'''
Created on Jul 17, 2014

@author: Nikola Milosevic

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''

from os import listdir
from os.path import isfile, join
import os
import shutil
from bs4 import BeautifulSoup

pmcbmifile = 'PMCBMI.txt'
PMCBMItables = 'BMItables'
PMCBMIhtml = 'BMIhtml'
PMCBMIdocs = 'BMIarticles'
datadir = 'data'

if not os.path.exists(PMCBMItables):
    os.makedirs(PMCBMItables)
if not os.path.exists(PMCBMIdocs):
    os.makedirs(PMCBMIdocs)
if not os.path.exists(PMCBMIhtml):
    os.makedirs(PMCBMIhtml)

with open(pmcbmifile) as f:
    content = f.readlines()

for i in range(0,len(content)):
    content[i] = 'PMC'+content[i][:-1]+'.xml'
    shutil.copyfile(datadir+"/"+content[i], PMCBMIdocs+"/"+content[i])
    file = open(datadir+"/"+content[i],'r')
    xml = file.read()
   # print xml
    parsed_html = BeautifulSoup(xml)
    data_table = parsed_html.body.findAll('table-wrap')
    tables_in_doc = len(data_table)
    if(data_table!=None and tables_in_doc!=0):
        table_file = open(PMCBMItables+'/'+content[i]+'.html','w')
        table_file.write(str(data_table))
        table_file.close()
        table_file = open(PMCBMIhtml+'/'+content[i]+'.html','w')
        table_file.write(str(xml))
        table_file.close()
    file.close()

print "DONE!!!"