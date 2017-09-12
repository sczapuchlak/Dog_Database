import sqlite3


sqlite_file = 'Dog_Database' #this names the database
dogTable = 'Dog_Table' #this names the table
id

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


conn.commit()
conn.close()
