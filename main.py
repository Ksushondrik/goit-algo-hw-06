from collections import UserDict


# Базовий клас для полів запису
class Fild:
    def __init__(self, value):
        if not value:
            raise Exception("You did not specify a required argument!")
        else:
            self.value = value
    
    def __str__(self) -> str:
        return str(self.value)
    

# Клас для зберігання імені контакту. Обов'язкове поле
class Name(Fild):
    # реалізація класу
    def __init__(self, name):
        if name.strip():
            self.name = name
        else:
            raise Exception("You enter an empty line!")
            


# Клас для зберігання номера телефону. Має валідацію формату (10 цифр)
class Phone(Fild):
    # реалізація класу
    def __init__(self, phone):
        self.phone = self.verify_phone(phone)

    # перевірка формату номеру (має містити 10 цифр)
    def verify_phone(self, phone):
        if (len(phone) == 10) and (phone.isdigit()):
            return phone
        else:
            raise Exception("Wrong phone format")


# Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
       
    # Додавання телефонів
    def add_phone(self, phone):
        phone = Phone(phone)
        if phone not in self.phones:
            self.phones.append(phone)
        else:
            raise Exception("This number isalready in the list!")
        
    # Видалення телефонів
    def remove_phone(self, phone):
        pass


    # Редагування телефонів
    def edit_phone(self,phone, new_phone):
        self.phones[self.find_phone(phone)] = new_phone
    
    # Пошук телефону
    def find_phone(self, phone):
        if phone in self.phones:
            return self.phones.index(phone)
        else:
            raise Exception("This number {phone} is not faund!")

    # def get_phones(self):
        # return self.phones
    
    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {';'.join(p.value for p in self.phones)}"


# Клас для зберігання та управління записами
class AddressBook(UserDict):
    def __init__(self, data = None):
        if data is None:
            data = {}
        super().__init__(data)

    # Додавання записів
    def add_record(self, record):
        self.data[record.name] = record.phones

    # Пошук записів за іменем
    def find(self, name):
        if name in self.data:
            return self.data[name]

    # Видалення записів за іменем
    def delete(self):
        pass



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
