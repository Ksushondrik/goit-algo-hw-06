class Field:            # Базовий клас для полів запису.
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name:             # Клас для зберігання імені контакту. Обов'язкове поле.
    def __init__(self, name):
        self.name = name

class Phone:            # Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
    def __init__(self, phone):
        self.phone = self.verify_phone(phone)
    
    def verify_phone(self, phone):
        if len(phone) == 10 and phone.isdigit():
            return phone
        else:
            raise ValueError("")

class Record:           # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone = Phone(phone)
        if phone not in self.phones:
            self.phones.append(phone)

    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {';'.join(p.value for p in self.phones)}"
    # Додавання телефонів.
    # Видалення телефонів.
    # Редагування телефонів.
    # Пошук телефону.
    

class AddressBook:      # Клас для зберігання та управління записами.
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.name] = record
        # який додає запис до self.data
    
    def find(self, name):
        for record in self.data:
            if record.name == name:
                return record
        # який знаходить запис за ім'ям

    def delete(self, name):
        rec = self.find(name)
        if rec:
            self.data.remove(rec)
            print(f"Data for {name} deleted")
        else:
            print(f"Data for {name} is not faund")
        # який видаляє запис за ім'ям

    # Додавання записів.
    # Пошук записів за іменем.
    # Видалення записів за іменем.

if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
