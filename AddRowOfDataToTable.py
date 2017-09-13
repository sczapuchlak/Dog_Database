#this file adds a row of data to the table
import sqlite3

def main():
    AddARow()

def AddARow():
    # this names the database
    dogFile = 'Dog_Database.sqlite'
    # this names the table
    dogTable = 'Dog_Table'
    #Call the UserInformationFunction
    askUser = UserInformation()
    # Connecting to the database file
    conn = sqlite3.connect(dogFile)
    c = conn.cursor()


    #Use a try statement to a add a new row if the ID doesn't already exist
    try:
        c.execute("INSERT OR IGNORE INTO {tn} (NULL, {dN}, {dA}, {dB},{dO}, {dT})".\
                  format(tn=dogTable, dN= askUser[0], dA=int(askUser[1]), dB=askUser[2], dO=askUser[3], dT=askUser[4]))

    except sqlite3.IntegrityError:
        print("There was an error with your key!")


def UserInformation():
    userDogName= input("Dog Name: ")
    userDogAge = input("Dog Age: ")
    userDogBreed = input("Dog Breed: ")
    userDogOrigin = input("Dog Origin: ")
    userDogTemperament = input("Dog Temperament: ")
    userListofDogTraits = [userDogName,userDogAge,userDogBreed, userDogOrigin, userDogTemperament]
    return userListofDogTraits

main()