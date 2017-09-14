#used https://www.python-course.eu/sql_python.php as help for all this and formatting

import sqlite3


def main():
    #get the data and display it
    getARow()



def getARow():
    # this names the database
    dogFile = 'Dog_Database.sqlite'
    # this names the table
    dog_table = 'Dog_Table'
    dogName = "Doggo_Name"
    # create connection to database file
    conn = sqlite3.connect(dogFile)
    c = conn.cursor()

    #ask user what the name of the dog they are looking for is
    userInput= input("What is the dog's name you are looking for? ")

    try:
        #select one entry from table
        c.execute('SELECT * FROM {tn} WHERE {cn}={user}'.format(tn=dog_table, cn=dogName,user="\'" +userInput+"\'" ))
        print("Here are all the dogs listed: ")
        allDoggos = c.fetchall()
        print("Here is your dog: ", allDoggos)

    except sqlite3.Error:
        print("I can't find a dog by that name! Please try again!")


    # commit changes made
    conn.commit()
    # close the DB connection
    conn.close()



main()