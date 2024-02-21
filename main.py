from collections import UserDict


# Базовий клас для полів запису
class Fild:
    def __init__(self, value):
        self.value = value
    
    def __str__(self) -> str:
        return str(self.value)
    

# Клас для зберігання імені контакту. Обов'язкове поле
class Name(Fild):
    # реалізація класу
    def __init__(self, value, name):
        super().__init__(value)
        self.name = name


# Клас для зберігання номера телефону. Має валідацію формату (10 цифр)
class Phone(Fild):
    # реалізація класу
    def __init__(self, value, phone):
        super().__init__(value)
        self.phone = phone

    def verify_phone(self, phone):
        if len(self.phone) == 10:
            return phone
        else:
            raise ValueError("Wrong phone format")


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
        
    # Видалення телефонів
    def remove_phone(self, phone):
        phone = Phone(phone)
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            pass


    # Редагування телефонів
    def edit_phone():
        pass
    
    # Пошук телефону
    def find_phone():
        pass
    
    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {';'.join(p.value for p in self.phones)}"


# Клас для зберігання та управління записами
class AddressBook(UserDict):
    def __init__(self, data):
        self.data = data

    # Додавання записів
    def add_record():
        pass

    # Пошук записів за іменем
    def find():
        pass

    # Видалення записів за іменем
    def delete():
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
