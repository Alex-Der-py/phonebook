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

def merge_contacts(contacts):
    """Merge duplicate contacts by last name and first name."""
    unique_contacts = {}

    for contact in contacts:
        key = tuple(contact[:2])

        if key not in unique_contacts:
            unique_contacts[key] = contact.copy()
        else:
            existing = unique_contacts[key]

            for index, value in enumerate(contact):
                if not existing[index] and value:
                    existing[index] = value

    return list(unique_contacts.values())

def main():
    """Normalize, merge and save phonebook contacts."""
    with open('phonebook_raw.csv', encoding='utf-8', newline='') as source:
        reader = csv.reader(source)
        header = next(reader)
        contacts = list(reader)

    print(f'Исходное количество записей: {len(contacts)}')

    contacts = [normalize_name(contact) for contact in contacts]

    for contact in contacts:
        contact[5] = normalize_phone(contact[5])

    contacts = merge_contacts(contacts)

    with open('phonebook.csv', 'w', encoding='utf-8', newline='') as target:
        writer = csv.writer(target)
        writer.writerow(header)
        writer.writerows(contacts)

    print(f'Уникальных контактов: {len(contacts)}')
    print('Результат сохранён в phonebook.csv')


if __name__ == '__main__':
    main()
