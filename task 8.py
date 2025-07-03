# Defines a function to manage a contact book stored in a dictionary
# Add a new contact with name, phone, and email
# Update existing contact information
# Retrieve contact details
# View all contacts in a formatted list
# Stores contact data in this format:
# {
#     "Ali": {"phone": "123", "email": "ali@email.com"},
#     "Sara": {"phone": "999", "email": "sara@email.com"}
# }
# Handles all operations using dictionary access, in checks, and nested updates
# Normalize names with .title() to handle case inconsistencies
# Validate emails (must contain @ and .)
# Prevent adding duplicates
# Use a while True loop with a menu-driven interface
def manage_contact_book(cb:dict, option: int):
    if option==1:
        name=input('Name:').title()
        for keys in cb:
            if name==keys:
                print("Name already exists, try another.")
                return
        data={}
        cb[name]=data
        data["phone"]=input("Phone:")
        eml=input("E-mail:")
        if "@" and "." in eml:
            data["email"]=eml

        print(cb)
        return
    
    elif option==2:
        contact=input('Which contact do you wish to update: ').title()
        if cb.get(contact)==None:
            print('No such contact in the contact book.')
            return
        ph=int(input("Enter updated phone: "))
        email=input("Enter updated E-mail: ")
        if "@" and "." in email:
            cb.update({contact:{"phone":ph, "email": email}})
        else:
            cb.update({contact:{"phone":ph}})
            print('Email could not be updated.')
        print(cb)
        return

    elif option==3:
        contact=input("Contact to retrieve: ").title()
        if cb.get(contact)==None:
            print('No such contact in the contact book.')
            
        else:
            data=cb[contact]
            print(contact, ": ".join(list(data)))
        return
    
    elif option==4:
        for keys, values in cb.items():
            print(keys,"→",end=" ")
            for items, data in values.items():
                print(items,":",data, end=" ")
            print()
        return

       

contactbook={}
while True:
    print("1. Add Contact")
    print('2. Update Contact')
    print("3. Retrieve Contact")
    print("4. View All Contacts")
    print("5. Exit")
    choice=int(input())
    if choice==5:
        break
    if choice==1 or choice==2 or choice==3 or choice==4:
        manage_contact_book(contactbook, choice)