import argparse
from addressbook.contact import Contact
from addressbook.utils import normalize_name

class CommandLineInterface:
    def __init__(self, contact_list):
        self.contact_list = contact_list
        self.parser = argparse.ArgumentParser(description='Address book application')

        subparsers = self.parser.add_subparsers(dest='command')

        add_parser = subparsers.add_parser('add', help='Add a new contact')
        add_parser.add_argument('name', help='Name of the contact')
        add_parser.add_argument('email', help='Email address of the contact')
        add_parser.add_argument('phone', help='Phone number of the contact')

        remove_parser = subparsers.add_parser('remove', help='Remove an existing contact')
        remove_parser.add_argument('name', help='Name of the contact to remove')

        list_parser = subparsers.add_parser('list', help='List all contacts')

    def run(self, args=None):
        if args is None:
            args = self.parser.parse_args()
        else:
            args = self.parser.parse_args(args)

        if args.command == 'add':
            name = normalize_name(args.name)
            email = args.email
            phone = args.phone
            contact = Contact(name, email, phone)
            self.contact_list.add_contact(contact)
            print(f'Added contact: {name} ({email}, {phone})')

        elif args.command == 'remove':
            name = normalize_name(args.name)
            contacts = self.contact_list.get_contacts()
            for contact in contacts:
                if contact.get_name() == name:
                    self.contact_list.remove_contact(contact)
                    print(f'Removed contact: {name}')
                    break
            else:
                print(f'Contact not found: {name}')

        elif args.command == 'list':
            contacts = self.contact_list.get_contacts()
            for contact in contacts:
                name = contact.get_name()
                email = contact.get_email()
                phone = contact.get_phone()
                print(f'{name} ({email}, {phone})')