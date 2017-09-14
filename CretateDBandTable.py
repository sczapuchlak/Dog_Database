# this  file creates a db and table
import sqlite3


def main():
    createDBandTable()


def createDBandTable():
    # this names the database
    dogFile = 'Dog_Database.sqlite'
    # this names the table
    dogTable = 'Dog_Table'
    # name the variable with the Primary ID column
    id_column = "Primary_Key"
    # titles of the columns
    dogName = "Doggo_Name"
    dogAge = "Doggo_Age"
    dogBreed = "Doggo_Breed"
    dogOrigin = "Doggo_Origin"
    dogTemperament = "Doggo_Temperament"

    # create connection to database file
    conn = sqlite3.connect(dogFile)
    c = conn.cursor()

    # create the dog sqlLite table
    c.execute('CREATE TABLE {tn} ({dI} INTEGER PRIMARY KEY, {dN} TEXT NOT NULL, {dA} REAL, {dB} TEXT, {dO} TEXT, {dT} TEXT)'\
                       .format(tn=dogTable, dI=id_column, dN=dogName, dA=dogAge, dB=dogBreed, dO=dogOrigin, dT=dogTemperament))

    # tell the user the table was created
    print("Table has been created")
    # commit changes made
    conn.commit()
    # close the DB connection
    conn.close()


main()
