'''
Created on Sep 22, 2014

@author: nikola
'''
#SELECT * FROM shared.articles_medline_2014 where xml like '%PublicationType>Clinical%' LIMIT 10;
import MySQLdb
from bs4 import BeautifulSoup
import MySQLdb.cursors as cursors
print "connecting to db"

db = MySQLdb.connect(host="localhost", # your host, usually localhost 
					  user="root", # your username
                      passwd="", # your password
                      db="shared") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the query you need
#cur2 = db2.cursor()
cur = db.cursor()
print 'connected to db'
# Use all the SQL you like
#cur.execute("SELECT id_ext FROM shared.articles_medline_2014 where xml like '%PublicationType>Clinical%'")
print 'execute query'
for i in range(0,200):
    print 'executing '+str(i)
    cur.execute("SELECT * FROM shared.articles_medline_2014 where publication_type is null limit 100000")
    print '\nexecuted! '+str(i)
    for row in cur.fetchall() :
        id_art = row[0]
        xml = row[1]
        parsed_html = BeautifulSoup(xml)
        publication_type = parsed_html.publicationtype.text
        print publication_type
        cur.execute("""UPDATE shared.articles_medline_2014 SET publication_type=%s Where id_art=%s""",(publication_type,id_art))
print '\n'

print 'done!!!!'
