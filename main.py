# This creates 3 empty lists that will be used, if a CSV file is imported these lists will be overwritten. This also imports CSV
import csv
import sys
contact_names = ["","","","","","","","","","","","","","","","","","","",""]
contact_numbers = ["","","","","","","","","","","","","","","","","","","",""]
contact_email = ["","","","","","","","","","","","","","","","","","","",""]
handler_list = ["","","","","","","","","","","","","","","","","","","",""]
selection = ""
selection2 = ""
selection3 = ""

# The 'main' function exists so other parts of the program can return to it so the user can make another selection, it has to be at the top to reduce errors

def main():
    global selection
    print ("Would you like to (V)iew contacts, (C)reate contacts, (D)elete contacts, (E)dit contacts, (I)mport CSV or (EX)it?")

    #This is a while loop that 'traps' the user until they make a valid selection (V, C, E, I or EX)

    while (selection != "V") and (selection != "C") and (selection != "E") and (selection != "EX") and (selection != "D") and (selection != "I"):
        selection = input()
        if (selection != "V") and (selection != "C") and (selection != "E") and (selection != "EX") and (selection != "D") and (selection != "I"):
            print ("Incorrect Entry! Retry")

    # The if statements below direct the program to the correct function depending on the letter entered above

    if selection == "C":
        create_contacts()
    if selection == "V":
        view_contacts()
    if selection == "D":
        delete_contacts()
    if selection == "E":
        edit_contacts()
    if selection == "EX":
        exit()
    if selection == "I":
        file()

# This is the functon for importing CSV file, IDK how this even works

def file():
    global selection
    global contact_names
    global contact_numbers
    global contact_email
    try:
        with open('data.csv', mode ='r')as file:
            csvFile = csv.reader(file)
            contact_names = next(csvFile)
            handler_list = next(csvFile)
            contact_numbers = next(csvFile)
            handler_list = next(csvFile)
            contact_email = next(csvFile)
            print ("SUCCESS!")
            print ('Press ENTER to continue')
            selection = ""
            main()

    except:
        print ("ERROR. COuld not open file. Make sure that file is named 'data.csv' and that it is stored in the same directory as this program.")
        input ('Press ENTER to continue')
        selection = ""
        main()





# This is the function for editing and saving to CSV

def exit():
    global selection3
    selection3 = ""
    print ("would you like to save to CSV? (Y/N)")
    while (selection3 != "Y") and (selection3 != "N"):
        selection3 = input()
        if (selection3 != "Y") and (selection3 != "N"):
            print ("Incorrect Entry! Retry")
    if selection3 == "N":
        print ("Thank you for using my program!")
        input ('press ENTER to exit')
        sys. exit()
    if selection3 == "Y":
        try:
            f = open('data.csv', 'w')
            writer = csv.writer(f)
            writer.writerow(contact_names)
            writer.writerow(contact_numbers)
            writer.writerow(contact_email)
            f.close()
            sys. exit()
        except:
            print ("SUCCESS")
            sys. exit()



# This is the function for editing contacts

def edit_contacts():
    global selection
    global selection2
    selection2 = ""
    count = contact_names.count("")
    if count == 20:
        print ("ERROR you have no contacts saved")
        selection = ""
        input ('Press ENTER to continue')
        main()
    print ("Would you like to edit (N)ame, (P)hone number or (E)mail?")
    while (selection2 != "N") and (selection2 != "P") and (selection2 != "E"):
        selection2 = input()
        if (selection2 != "N") and (selection2 != "P") and (selection2 != "E"):
            print ("Incorrect Entry! Retry")

# These 3 if statements handle the editing of names, phone numbers and email. They are all really similar though

    if selection2 == "N":
        global selection3
        print (*contact_names, sep = "\n")
        overwrite = input("Please type out the name of the contact you would like to change the name of\n")
        print (*contact_names, sep = "\n")
        try:
            index = contact_names.index(overwrite)
            new_contact_name = input("Please input the new name of this contact\n")
            contact_names[index] = new_contact_name
            print ("SUCCESS!")
            input('Press ENTER to continue')
            selection = ""
            main()
        except:
            print ("ERROR, no contact exists by that name.\nReturing to selection")
            selection = ""
            main()

    if selection2 == "P":
        print (*contact_names, sep = "\n")
        overwrite = input("Please type out the name of the contact you would like to change the phone number of\n")
        try:
            index = contact_names.index(overwrite)
            new_contact_number = input ("Please input the new phone number of this contact\n")
            contact_numbers[index] = new_contact_number
            print ("SUCCESS!")
            input('Press ENTER to continue')
            selection = ""
            main()
        except:
            print ("ERROR, no contact exists by that name.\nReturing to selection")
            selection = ""
            main()

    if selection2 == "E":
        print (*contact_names, sep = "\n")
        overwrite = input("Please type out the name of the contact you would like to change the email of\n")
        try:
            index = contact_names.index(overwrite)
            new_contact_email = input ("Please input the new email of this contact\n")
            contact_email[index] = new_contact_email
            print ("SUCCESS!")
            input('Press ENTER to continue')
            selection = ""
            main()
        except:
            print ("ERROR, no contact exists by that name.\nReturing to selection")
            selection = ""
            main()



# This is the function for deleting contacts

def delete_contacts():
    global selection

# This counts the amount of time "" appears in the list. If it appears 20 times that means there are no contacts saved and it will give you an error and boot you out to selection

    count = contact_names.count("")
    if count == 20:
        print ("ERROR you have no contacts saved")
        selection = ""
        input ('Press ENTER to continue')
        main()

# This section handles the selection and deletion process

    print (*contact_names, sep = "\n")
    view = input("Please type the name of the contact you would like to delete\n")
    try:
        index = contact_names.index(view)
        contact_names[index] = ""
        contact_numbers[index] = ""
        contact_email[index] = ""
        print ("SUCCESS!")
        input ('Press ENTER to continue')
        selection = ""
        main()
    except:
        print ("ERROR, no contact exists by that name.\nReturing to selection")
        selection = ""
        main()



# This is the function for viewing contacts

def view_contacts():
    global selection

# This counts the amount of time "" appears in the list. If it appears 20 times that means there are no contacts saved and it will give you an error and boot you out to selection

    count = contact_names.count("")
    if count == 20:
        print ("ERROR you have no contacts saved")
        selection = ""
        input ('Press ENTER to continue')
        main()
    print (*contact_names, sep = "\n")
    view = input ("Please type the name of the contact you would like to view\n")
    try:
        index = contact_names.index(view)
        print ("This contacts name is:")
        print (contact_names[index])
        print ("This contacts phone number is")
        print (contact_numbers[index])
        print ("This contacts email is")
        print (contact_email[index])
        input ('press ENTER to continue')
        selection = ""
        main()
    except:
        print ("ERROR, no contact exists by that name.\nReturing to selection")
        selection = ""
        main()


# This is the function for creating contacts, when you select 'C' on the main selection this is the code that actually get's executed 

def create_contacts():
    global selection

    # The program will first try the 'try' section and if it delivers an error it will execute the code in 'except' instead. 'Except' is for when all contacts are filled so the user will be prompted to overwrite a contact to create a new one

    try:
        index = contact_names.index("")
        new_contact_name = input("Please input the new name of this contact\n")
        new_contact_email = input ("Please input the new email of this contact\n")
        new_contact_number = input ("Please input the new phone number of this contact\n")
        contact_names[index] = new_contact_name
        contact_numbers[index] = new_contact_number
        contact_email[index] = new_contact_email
        print ("SUCCESS!")
        input('Press ENTER to continue')
        selection = ""
        main()

    # This code handles when all slots are filled and one must be overwritten to add a new contact

    except:
        if selection3 == "Y":
                print ("Thank you for using my program!")
                input ('Press ENTER to exit')
                sys. exit()
        print ("Sorry, all slots are filled, in order to make space you must choose a contact to overwrite")
        input('Press ENTER to continue')
        print (*contact_names, sep = "\n")
        overwrite = input("Please type out the name of the contact you would like to remove\n")

# This handles the actual overwriting section where the old values are replaced with the new values

        try:
            index = contact_names.index(overwrite)
            new_contact_name = input("Please input the new name of this contact\n")
            new_contact_email = input ("Please input the new email of this contact\n")
            new_contact_number = input ("Please input the new phone number of this contact\n")
            contact_names[index] = new_contact_name
            contact_numbers[index] = new_contact_number
            contact_email[index] = new_contact_email
            print ("SUCCESS!")
            input('Press ENTER to continue')
            selection = ""
            main()

# This is an error handler in case the value entered in to be overwritten does not match any of the contacts. It simplys boots the user to the main selection

        except:
            print ("ERROR, no contact exists by that name.\nReturing to selection")
        selection = ""
        main()

# This is the starting screen, when you start the program this is what pops up first

print ("Contact book")
print ("MarketingZestyclose7")
main() 

