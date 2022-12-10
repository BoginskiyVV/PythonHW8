# from ui import input_ch
from ui import ch
import csv





def show_phonebook(ch):
    if ch == 1:
        with open('database.csv', 'r', encoding='UTF-8') as csvfile:
            csv = csvfile.readlines()
            print(csv)


show_phonebook(ch)


def add_contact(ch):
    if ch == 2:
        contact_surname = input('Введите фамилию ')  
        contact_name = input('Введите имя ')  
        contact_number = input('Введите номер телефона ')
        commentary = input('Комментарий ')
        contact = [{'contact_id': '', 'surname': contact_surname, 'name': contact_name, 'phone': contact_number,
                    'comment': commentary}, ]
        print(contact)
        with open('database.csv', 'a', newline='', encoding='UTF-8') as file:
            cont = str(contact) 
            file.write(cont)
        return contact  
        
add_contact(ch)


# def del_contact(ch):
#     if ch == 3:
#         del_cont = input('Введите фамилию: ')
#         with open('database.csv', 'a', newline='', encoding='UTF-8') as file:
#             file.readline()
#             file.find(del_cont)

# del_contact(ch)

# def change_contact(ch):
#     if ch == 4:

# change_contact(ch)

# def search_info(ch):
#     if ch == 4:
#         s_i = input('Введите инфоомацию для поиска: ')




