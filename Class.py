class contact_book():
    def __init__(self):
        self.contacts = {}

    def create_contact(self, name, number):
        self.name = name
        self.number = number
        self.contacts[self.name] = self.number

    def delete_contact(self, name):
        del self.contacts[name]

    def view_contact(self):
        for key in self.contacts.keys():
            print(key, ': ', self.contacts[key])
        print("")

    def edit_contact_name(self, name, rename):
        if self.name == name:
            self.contacts[rename] = self.number
            del self.contacts[name]

    def edit_contact_number(self, number, renumber):
        if self.number == number:
            self.contacts[self.name] = renumber
            del self.contacts[number]

    def export_all_contacts(self, filename): # для записи телефонной книжки в файлы
        export = open(filename, 'w') # открываем файл (w = write, файл открывается для записи)(или создаем, если файла с таким именем не найдено/не существует)
        data = str(self.contacts)     # кладем в переменную data, наш словарь, в формате строки
        export.write(data)            # записываем словарь в файл

phonebook = contact_book()
first_contact = phonebook.create_contact("Sergey", "+77766723016")
second_contact = phonebook.create_contact("Valeriya", "+77766723017")
phonebook.view_contact()
phonebook.delete_contact('Sergey')
phonebook.edit_contact_name("Valeriya",'Valeriya2')
phonebook.view_contact()
phonebook.export_all_contacts("xyz.txt") # cоздание файла формата .txt
phonebook.export_all_contacts("xyz.csv") # создание файла формата .csv
phonebook.export_all_contacts("xyz.xlsx")# создание файла формата .xlsx

