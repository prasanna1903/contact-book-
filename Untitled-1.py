class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if name not in self.contacts:
            self.contacts[name] = {'Phone': phone, 'Email': email}
            print(f'Contact {name} added successfully.')
        else:
            print(f'Contact {name} already exists.')

    def view_contact(self, name):
        if name in self.contacts:
            contact_info = self.contacts[name]
            print(f'Contact: {name}\nPhone: {contact_info["Phone"]}\nEmail: {contact_info["Email"]}')
        else:
            print(f'Contact {name} not found.')

    def list_contacts(self):
        if not self.contacts:
            print('Contact book is empty.')
        else:
            print('Contacts:')
            for name, contact_info in self.contacts.items():
                print(f'{name} - Phone: {contact_info["Phone"]}, Email: {contact_info["Email"]}')

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f'Contact {name} removed successfully.')
        else:
            print(f'Contact {name} not found.')

def main():
    contact_book = ContactBook()

    while True:
        print('\nContact Book Menu:')
        print('1. Add Contact')
        print('2. View Contact')
        print('3. List Contacts')
        print('4. Remove Contact')
        print('5. Exit')

        choice = input('Enter your choice (1-5): ')

        if choice == '1':
            name = input('Enter contact name: ')
            phone = input('Enter phone number: ')
            email = input('Enter email address: ')
            contact_book.add_contact(name, phone, email)

        elif choice == '2':
            name = input('Enter contact name: ')
            contact_book.view_contact(name)

        elif choice == '3':
            contact_book.list_contacts()

        elif choice == '4':
            name = input('Enter contact name: ')
            contact_book.remove_contact(name)

        elif choice == '5':
            print('Exiting the Contact Book. Goodbye!')
            break

        else:
            print('Invalid choice. Please enter a number between 1 and 5.')

if __name__ == '__main__':
    main()

