"""Clean and normalize phonebook contacts."""

import csv


def main():
    """Read contacts from the source CSV file."""
    with open('phonebook_raw.csv', encoding='utf-8', newline='') as source:
        reader = csv.reader(source)
        header = next(reader)
        contacts = list(reader)

    print(f'Количество записей: {len(contacts)}')


if __name__ == '__main__':
    main()