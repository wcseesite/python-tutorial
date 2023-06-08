import pickle
from addressbook.addressbook import ContactList
from addressbook.cli import CommandLineInterface

def main():
    try:
        with open('contacts.pickle', 'rb') as f:
            contact_list = pickle.load(f)
    except FileNotFoundError:
        contact_list = ContactList()

    cli = CommandLineInterface(contact_list)
    cli.run()

    with open('contacts.pickle', 'wb') as f:
        pickle.dump(contact_list, f)

if __name__ == '__main__':
    main()