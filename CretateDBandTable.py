#this  file creates a db and table
import sqlite3

def main():
    createDBandTable()

def createDBandTable():
    # this names the database
    dogFile = 'Dog_Database.sqlite'
    #this names the table
    dogTable = 'Dog_Table'

    #titles of the columns
    dogId = "Doggo_ID"
    dogName = "Doggo_Name"
    dogAge = "Doggo_Age"
    dogBreed = "Doggo_Breed"
    dogOrigin = "Doggo_Origin"
    dogTemperament = "Doggo_Temperament"

    #create data types
    int = 'INTEGER'
    str = 'TEXT'


    #create connection to database file
    conn = sqlite3.connect(dogFile)
    c = conn.cursor()

    #create the dog sqlLite table
    c.execute('CREATE TABLE {tn} ({dI} {inF} PRIMARY KEY, {dN} {sF}, {dA} {inF}, {dB} {sF},{dO} {sF}, {dT} {sF})'\
              .format(tn = dogTable, dI=dogId, inF=int, dN=dogName,sF=str, dA=dogAge,
                      dB=dogBreed,dO=dogOrigin, dT=dogTemperament))

    #commit changes made
    conn.commit()
    #close the DB connection
    conn.close()

main()