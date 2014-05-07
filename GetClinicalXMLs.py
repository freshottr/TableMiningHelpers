'''
Created on Mar 11, 2014

@author: nikola
'''
import MySQLdb
print "connecting to db"
db = MySQLdb.connect(host="db_server_with_medline_and_pmc_articles", # your host, usually localhost
                     user="someusername", # your username
                      passwd="somepassword", # your password
                      db="shared") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the query you need
cur = db.cursor() 
with open('pmc_ids') as f:
    ids = f.readlines()
print 'Length: '+str(len(ids))
for i in range(0,len(ids)):
    ids[i] = ids[i].replace('\n','')
    sql = "SELECT xml FROM shared.articles_pmc_dec_2013 as pmc where pmc.id_ext='"+ids[i]+"'"
    cur.execute(sql)
    for row in cur.fetchall() :
        document = open(ids[i]+'.xml','w')
        document.write(row[0])
        document.close()
print 'closing files'

