# this file updates a row of data to the table
import sqlite3


def main():
    updateRow()


def updateRow():
    # this names the database
    dogFile = 'Dog_Database.sqlite'
    # this names the table
    dog_table = 'Dog_Table'
    # Call the UserInformationFunction
    askUser = updateInfo()
    # name the variable with the Primary ID column
    id_column = "Primary_Key"
    # Connecting to the database file
    conn = sqlite3.connect(dogFile)
    c = conn.cursor()

    try:
        c.execute("UPDATE {tn} ({idc}, {dN}, {dA}, {dB},{dO}, {dT})". \
                  format(tn=dog_table,idc=id_column, dN="\'" + askUser[0] + "\'", dA=int(askUser[1]), dB= "\'" + askUser[2]+"\'",
                dO= "\'" + askUser[3] + "\'", dT="\'" + askUser[4] + "\'"))
        # let the user know their info has been added
        print("Your dog has been updated!")
    except sqlite3.IntegrityError:
        print("There was an error with your key!")


def updateInfo():
    userDogName = input("Dog Name to update: ")
    userDogAge = input("Please update the dog's age: ")
    userDogBreed = input("Please update the dog's breed: ")
    userDogOrigin = input("Please update the dog's origin: ")
    userDogTemperament = input("Please update the dog's temperament: ")
    userListofDogTraits = [userDogName, userDogAge, userDogBreed, userDogOrigin, userDogTemperament]
    return userListofDogTraits


# main()
