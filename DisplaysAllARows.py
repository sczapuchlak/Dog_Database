#used https://www.python-course.eu/sql_python.php as help for all this and formatting

import sqlite3


def main():
    #get the data and display it
    getAllRows()



def getAllRows():
    # this names the database
    dogFile = 'Dog_Database.sqlite'
    # this names the table
    dog_table = 'Dog_Table'

    # create connection to database file
    conn = sqlite3.connect(dogFile)
    c = conn.cursor()
    #select all entries from table
    c.execute('SELECT * FROM {tn}'.format(tn=dog_table))
    print("Here are all the dogs listed: ")
    allDoggos = c.fetchall()
    for r in allDoggos:
        print(r)

    conn.close()
    return allDoggos



main()