# This program calls to other programs in the same project to work with3
# SQL Lite databases to query and mold the information
import CretateDBandTable,AddRowOfDataToTable,UpdatesARowInTable, DeletesARow, DisplaysASingleRow,DisplaysAllARows


def main():
    game_loop = True
    while game_loop:
        print("\nWelcome to the Database Menu Program\n ")
        menu()
        selection = input()
        userSelection(selection)
        ask_user = input("Would you like to do more doggie database stuff? (Y for yes, N for no)")
        if ask_user == "n" or ask_user == "N":
            print("Your loss. Dogs are cool!")
            game_loop = False


def menu():
    print("Please select a number based the option you'd like: ")
    print("1. Create a database and table of different dogs.\n")
    print("2. Add a dog to the table.\n")
    print("3. Update a dog in the table.\n")
    print("4. Delete a dog from the table.\n")
    print("5. Display all of the dogs in the table.\n")
    print("6. Display a single dog in the table.\n")
    print("Press anything else to close\n")



def userSelection(num):
    if num == "1":
        CretateDBandTable.main()
    elif num == "2":
        AddRowOfDataToTable.main()
    elif num == "3":
        UpdatesARowInTable.main()
    elif num == "4":
        DeletesARow.main()
    elif num == "5":
        DisplaysAllARows.main()
    elif num == "6":
        DisplaysASingleRow.main()
    else:
        print("Now quitting.. ")
        exit()


main()
