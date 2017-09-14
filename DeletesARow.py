# this file deletes a row of data to the table
import sqlite3


def main():
    deleteRow()


def deleteRow():
    # Connecting to the database file
    conn = sqlite3.connect(dog_file)
    # Call the UserInformationFunction
    askUser = UserInformation()
    # this names the database
    dog_file = 'Dog_Database.sqlite'
    # this names the table
    dog_table = 'Dog_Table'

    c = conn.cursor()

    #display all rows so that the user can pick what they want to delete

    #ask user what name they would like to delete?