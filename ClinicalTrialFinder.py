'''
Created on Mar 11, 2014

@author: nikola
'''
#SELECT * FROM shared.articles_medline_2014 where xml like '%PublicationType>Clinical%' LIMIT 10;
import MySQLdb
print "connecting to db"
db = MySQLdb.connect(host="db_server_with_medline_and_pmc_articles", # your host, usually localhost
                     user="someusername", # your username
                      passwd="somepassword", # your password
                      db="shared") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the query you need
cur = db.cursor() 
print "connected to db"

# Use all the SQL you like
#cur.execute("SELECT id_ext FROM shared.articles_medline_2014 where xml like '%PublicationType>Clinical%'")
print 'execute query'
cur.execute("SELECT medline.id_ext,medline.text_title,map.pmcid FROM shared.articles_medline_2014 as medline inner join shared.map_pmcid_pmid as map on map.pmid=medline.id_ext where medline.xml like '%PublicationType>Clinical%'")

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

# print 'getting xmls'
# sql = "SELECT xml from shared.articles_pmc_dec_2013 as pmc where pmc.id_ext IN (%s)"
# in_p=', '.join(list(map(lambda x: '%s', ids)))
# sql = sql % in_p
# cur.execute(sql, ids)
# i = 0
# print 'writing xmls to files'
# for row in cur.fetchall() :
#     pmc = open('document'+i+'.xml','w')
#     pmc.write(row[0])
#     pmc.close()
#     i=i+1
print 'end'
    