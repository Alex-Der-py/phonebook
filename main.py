"""Clean and normalize phonebook contacts."""

import csv
import re


PHONE_PATTERN = re.compile(
    r'(?:\+7|8)\s*\(?(\d{3})\)?[\s-]*'
    r'(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})'
    r'(?:\s*\(?доб\.\s*(\d+)\)?)?'
)

def normalize_name(contact):
    """Split the full name into three separate fields."""
    name_parts = ' '.join(contact[:3]).split()
    name_parts += [''] * (3 - len(name_parts))
    return name_parts + contact[3:]

def normalize_phone(phone):
    """Convert a phone number to a standard format."""
    match = PHONE_PATTERN.fullmatch(phone.strip())

    if match is None:
        return phone

    code, first, second, third, extension = match.groups()
    result = f'+7({code}){first}-{second}-{third}'

    if extension:
        result += f' доб.{extension}'

    return result

def main():
    """Read contacts and normalize names and phones."""
    with open('phonebook_raw.csv', encoding='utf-8', newline='') as source:
        reader = csv.reader(source)
        header = next(reader)
        contacts = list(reader)

    contacts = [normalize_name(contact) for contact in contacts]

    for contact in contacts:
        contact[5] = normalize_phone(contact[5])

    print(f'Количество записей: {len(contacts)}')


if __name__ == '__main__':
    main()