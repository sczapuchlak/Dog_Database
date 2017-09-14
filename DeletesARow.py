# this file deletes a row of data to the table
import sqlite3


def main():
    deleteRow()


def deleteRow():

    # this names the database
    dog_file = 'Dog_Database.sqlite'
    # this names the table
    dog_table = 'Dog_Table'
    #this points to the dog name which we will use to delete by
    dogName = "Doggo_Name"
    # Connecting to the database file
    conn = sqlite3.connect(dog_file)


    # ask user what name they would like to delete?
    userDelete = input("Enter the name of the dog you would like to delete: ")

    c = conn.cursor()
    try:
        #delete one entry from table
        c.execute('DELETE * FROM {tn} WHERE {cn}={user}'.format(tn=dog_table, cn=dogName,user="\'" +userDelete+"\'" ))
        print(dogName + "has been deleted from the table!")

    except sqlite3.Error:
        print("Cannot delete that dog at this time. Please try again!")

    # commit changes made
    conn.commit()
    # close the DB connection
    conn.close()

main()