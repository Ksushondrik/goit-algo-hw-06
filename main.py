from collections import UserDict


# Базовий клас для полів запису
class Field:
    def __init__(self, value):
        if not value:
            raise Exception("You did not specify a required argument!")
        else:
            self.value = value
    
    def __str__(self) -> str:
        return str(self.value)
    

# Клас для зберігання імені контакту. Обов'язкове поле
class Name(Field):
    # реалізація класу
    class Name(Field):
        def __init__(self, value):
            if not value.strip():
                raise ValueError("You entered an empty string!")
            else:
                super().__init__(value)
            

# Клас для зберігання номера телефону. Має валідацію формату (10 цифр)
class Phone(Field):
    def __init__(self, value):
        if not ((value.isdigit()) and (len(value) == 10)):
            raise ValueError("Incorrect phone format! Phone not added!")
        else:
            super().__init__(value)


# Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
       
    # Додавання телефонів
    def add_phone(self, phone):
        phone = Phone(phone)
        if phone.value not in [p.value for p in self.phones]:
            self.phones.append(phone)

        
    # Редагування телефонів
    def edit_phone(self, phone, new_phone):
        for number in self.phones:
            if number.value == phone:
                self.phones[self.phones.index(record)] = Phone(new_phone)
                break
        else:
            raise ValueError(f"Phone {phone} is not found in contact {self.name}")
    
    # Пошук телефону
    def find_phone(self, phone):
        for number in self.phones:
            if number.value == phone:
                return number
        return None
            
    # Видалення телефонів
    def remove_phone(self, phone):
        for number in self.phones:
            if number.value == phone:
                self.phones.remove(number)
        

    # Формат виводу даних про контакт
    def __str__(self) -> str:
        return f"Contact name: {self.name}, phones: {'; '.join(phone.value for phone in self.phones)}"


# Клас для зберігання та управління записами
class AddressBook(UserDict):
    # Додавання записів
    def add_record(self, record):
        self.data[record.name.value] = record

    # Пошук записів за іменем
    def find(self, name):
        return self.data.get(name)

    # Видалення записів за іменем
    def delete(self, name):
        if name in self.data:
            del self.data[name]

        



if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
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
