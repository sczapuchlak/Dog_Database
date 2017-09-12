#This program calls to other programs in the same project to work with
#SQL Lite databases to query and mold the information
import CretateDBandTable,AddRowOfDataToTable,UpdatesARowInTable,DeletesARow,DisplaysAllARows,DisplaysASingleRow


def main():
    gameLoop = True
    while gameLoop:
        print("Welcome to the Database Menu Program ")
        menu()
        selection = input()
        userSelection(selection)
        askUser = input("Would you like to do more doggie database stuff? (Y for yes, N for no)")
        if askUser == "n" or askUser == "N":
            print("Your loss. Dogs are cool!")
            gameLoop = False


def menu():
    print("Please select a number based the option you'd like: \n"
      "1. Create a database and table of different dogs.\n"
      "2. Add a dog to the table.\n"
      "3. Update a dog in the table.\n"
      "4. Delete a dog from the table.\n"
      "5. Display all of the dogs in the table.\n"
      "6. Display a single dog in the table.\n")

def userSelection(num):
    if num == "1":
        CretateDBandTable
    elif num == "2":
        AddRowOfDataToTable
    elif num == "3":
        UpdatesARowInTable
    elif num == "4":
        DeletesARow
    elif num == "5":
        DisplaysAllARows
    elif num == "6":
        DisplaysASingleRow
    else:
        print("Please enter a number! ")
        exit()

main()