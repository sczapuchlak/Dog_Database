
# this file adds a row of data to the table
import sqlite3


def main():
    addRow()


def addRow():

    # Call the UserInformationFunction
    askUser = userInformation()
    # this names the database
    file = "Dog_Database.sqlite"
    # this names the table
    dog_table = 'Dog_Table'
    # Connecting to the database file
    conn = sqlite3.connect(file)
    c = conn.cursor()

    # Use a try statement to a add a new row if the ID doesn't already exist
    try:

                c.execute("INSERT OR IGNORE INTO {tn} VALUES (NULL, {dN}, {dA}, {dB}, {dO}, {dT})".
                format(tn=dog_table, dN="\'" + askUser[0] + "\'", dA=int(askUser[1]), dB=askUser[2],
                dO=askUser[3], dT="\'" + askUser[4] + "\'"))

    # let the user know their info has been added
                print("Your dog has been added!")
    except sqlite3.IntegrityError:
        print("There was an error with your primary key!")
    except sqlite3.Error:
        print("There was an error with your values!")


    # commit changes made
    conn.commit()
    # close the DB connection
    conn.close()


def userInformation():
    userDogName = input("Dog Name: ")
    userDogAge = input("Dog Age: ")
    userDogBreed = input("Dog Breed: ")
    userDogOrigin = input("Dog Origin: ")
    userDogTemperament = input("Dog Temperament: ")

    userList = [userDogName, userDogAge, userDogBreed, userDogOrigin, userDogTemperament]
    return userList

main()
