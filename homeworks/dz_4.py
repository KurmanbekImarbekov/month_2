class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @classmethod
    def validate_phone_number(cls, phone_number):
        if len(phone_number) == 10 and phone_number.isdigit():
            return True
        else:
            return False


class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            contact = Contact(name, phone_number)
            cls.all_contacts.append(contact)
            return contact
        else:
            return None


ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number)

print(ContactList.all_contacts)  # []


class Library:
    def __init__(self, city, books):
        self.city = city
        self.books = books

    def __str__(self):
        return f"City: {self.city}, books: {self.books}"

    def __len__(self):
        return len(self.books)

    def __contains__(self, book):
        print("Ищем книгу:", book)
        return book in self.books

    def __bool__(self):
        if len(self.books) > 5:
            return True
        else:
            return False


lib = Library("Бишкек", books=["Война и мир", "1984", "Мастер и Маргарита"])
print(lib)
print(len(lib))
print("1984" in lib)
print("Гарри Поттер" in lib)
if lib:
    print("Библиотека большая (более 5 книг)")
else:
    print("Библиотека маленькая")
