# Contact Book

# Features:
# Add contact
# View saved contacts
# Search contact
# Delete contact
# Update contact
# Exit system
print("1. To Add contact")
print("2. To saved contact")
print("3. To search contact")
print("4. To delete contact")
print("5. To update contact")
print("6. Exit")
print("Type the options from 1 to 6")


contact_list = {}
    
# adding contact
def add_contact():
    name = input("name : ")
    number = input("number : ")
    if name in contact_list:
        print("This contact is already exists")
    elif number.isdigit():
        contact_list[name] = number
        print("Added successfully")
    else:
        print("You typed invalid number")


# saving contact           
def saved_contact():
    if not contact_list:
        print("No contacts saved")
    else:
        for name,number in contact_list.items(): 
            print(name ,":", number)
        

# searching  contact      
def search_contact():
    search = input("Enter the name of the saved cotact list you want to search ")
    if search in contact_list:
        print(search , ":", contact_list[search])
    else:
        print(search ,"is not found")


# To deleting the contact
def del_contact():
    name = input("Enter contact name which you want to delete from the saved contact list = ") 
    if name in contact_list:
        del contact_list[name]
        print("deleted successfully")
    else:
        print(name, "was not in contact list")


#Updating the contact
def update_contact():
    name = input("enter the name which contact you want to update = ")
    number = input("Enter the correct conduct number of the given conduct name = ")
    if number.isdigit():
        if name in contact_list:
            contact_list[name] = number
            print("Updated successfully")
        else:
            print("Your give name conduct is not found in contact list")
    else:
        print("Type only number, you typed invalid input", number)
                    
while True:
    option = input("Enter option = ")

    if option.isdigit():
        if option == '1':
            add_contact()
        elif option == '2':
            saved_contact()
        elif option == '3':
            search_contact()
        elif option == '4':
            del_contact()
        elif option == '5':
            update_contact()
        elif option == '6':
            print("Exiting....")
            break
        else:
            print("You entered invalid option")
        
            
