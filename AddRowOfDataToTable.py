# this file adds a row of data to the table
import sqlite3, CretateDBandTable


def main():
    AddARow()


def AddARow():
    # this names the database
    dogFile = 'Dog_Database.sqlite'
    # this names the table
    dogTable = 'Dog_Table'
    # Call the UserInformationFunction
    askUser = UserInformation()
    # name the variable with the Primary ID column
    id_column = "Primary_Key"
    # Connecting to the database file
    conn = sqlite3.connect(dogFile)
    c = conn.cursor()

    # Use a try statement to a add a new row if the ID doesn't already exist
    try:
        c.execute("INSERT OR IGNORE INTO {tn}  VALUES(NULL, {dN}, {dA}, {dB},{dO}, {dT})".
                  format(tn=dogTable, dN="\'" + askUser[0], dA="\'" + askUser[1]),
                         dB="\'" + askUser[2], dO="\'" + askUser[3], dT="\'" + askUser[4]+"\'"))
        # let the user know their info has been added
        print("Your dog has been added!")
    except sqlite3.IntegrityError:
        print("There was an error with your key!")

    # commit changes made
    conn.commit()
    # close the DB connection
    conn.close()


def UserInformation():
    userDogName = input("Dog Name: ")
    userDogAge = input("Dog Age: ")
    userDogBreed = input("Dog Breed: ")
    userDogOrigin = input("Dog Origin: ")
    userDogTemperament = input("Dog Temperament: ")
    userListofDogTraits = [userDogName, userDogAge, userDogBreed, userDogOrigin, userDogTemperament]
    return userListofDogTraits


main()
