'''
Created on Mar 11, 2014

@author: nikola
'''
#SELECT * FROM shared.articles_medline_2014 where xml like '%PublicationType>Clinical%' LIMIT 10;
import MySQLdb
print "connecting to db"
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="", # your password
                      db="shared") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the query you need
cur = db.cursor() 
print "connected to db"

# Use all the SQL you like
#cur.execute("SELECT id_ext FROM shared.articles_medline_2014 where xml like '%PublicationType>Clinical%'")
print 'execute query'
cur.execute("SELECT medline.id_ext,medline.text_title,map.pmcid FROM shared.articles_medline_2014 as medline inner join shared.map_pmcid_pmid as map on map.pmid=medline.id_ext")

# print all the first cell of all the rows
print 'query done, opening files'
f = open('medline_ids','w')
pmc = open('pmc_ids','w')
titles = open('titles','w')
#f.write('hi there\n') # python will convert \n to os.linesep
# SELECT medline.id_ext,map.pmcid, pmc.xml FROM shared.articles_medline_2014 as medline inner join shared.map_pmcid_pmid as map on map.pmid=medline.id_ext inner join shared.articles_pmc_dec_2013 as pmc on pmc.id_ext = medlineid_ext  where medline.xml like '%PublicationType>Clinical%' LIMIT 10;
ids = []
print 'write files'
for row in cur.fetchall() :
    ids.append(row[0])
    f.write(row[0]+'\n')
    titles.write(row[1]+'\n')
    pmc.write(row[2]+'\n')
print 'closing files'
f.close() 
pmc.close()
titles.close()

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

print 'end'
    