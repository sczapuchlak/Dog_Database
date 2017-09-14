# This program calls to other programs in the same project to work with
# SQL Lite databases to query and mold the information
import AddRowOfDataToTable
import CretateDBandTable
import UpdatesARowInTable


def main():
    game_loop = True
    while game_loop:
        print("Welcome to the Database Menu Program ")
        menu()
        selection = int(input())
        userSelection(selection)
        ask_user = input("Would you like to do more doggie database stuff? (Y for yes, N for no)")
        if ask_user == "n" or ask_user == "N":
            print("Your loss. Dogs are cool!")
            game_loop = False


def menu():
    select=input("Please select a number based the option you'd like: \n")
    print("1. Create a database and table of different dogs.\n")
    print("2. Add a dog to the table.\n")
    print("3. Update a dog in the table.\n")
    print("4. Delete a dog from the table.\n")
    print("5. Display all of the dogs in the table.\n")
    print("6. Display a single dog in the table.\n")
    return select


def userSelection(num):
    if num == "1":
        CretateDBandTable
    elif num == "2":
        AddRowOfDataToTable
    elif num == "3":
        UpdatesARowInTable
    # elif num == "4":
    #     DeletesARow.main()
    # elif num == "5":
    #     DisplaysAllARows.main()
    # elif num == "6":
    #     DisplaysASingleRow.main()
    else:
        print("Please enter a number! ")
        exit()


main()
