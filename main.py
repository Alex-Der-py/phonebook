"""Clean and normalize phonebook contacts."""

import csv


def normalize_name(contact):
    """Split the full name into three separate fields."""
    name_parts = ' '.join(contact[:3]).split()
    name_parts += [''] * (3 - len(name_parts))
    return name_parts + contact[3:]

def main():
    """Read contacts and normalize their names."""
    with open('phonebook_raw.csv', encoding='utf-8', newline='') as source:
        reader = csv.reader(source)
        header = next(reader)
        contacts = list(reader)

    contacts = [normalize_name(contact) for contact in contacts]

    print(f'Количество записей: {len(contacts)}')


if __name__ == '__main__':
    main()