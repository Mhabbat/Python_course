# w - перезапись
# r - чтение
# a - дозапись
# r+ - чтение + запись
# b - байт
# open(, 'w')

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может
# ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
with open('phone.txt', 'w') as f:
    f.write('\nSergei, Sergeev, 1234')
    f.write('\nAleks, Lazerov, 2636')
    f.write('\nNatasha, Koroleva, 1234')


def edit_data():
    print("\nПП | ФИО | Телефон")
    with open('phone.txt', "r", encoding='utf-8') as data:
        tel_book = data.read()
    print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для редактирования: ")) - 1
    tel_book_lines = tel_book.split("\n")
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(" | ")
    fio = input("Введите ФИО: ")
    phone = input("Введите номер телефона: ")
    num = elements[0]
    if len(fio) == 0:
        fio = elements[1]
    if len(phone) == 0:
        phone = elements[2]
    edited_line = f"{num} | {fio} | {phone}"
    tel_book_lines[index_delete_data] = edited_line
    print(f"Запись - {edit_tel_book_lines}, изменена на - {edited_line}\n")
    with open('phone.txt', "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))

# Удаляет информацию из файла
def delete_data():
    print("\nПП | ФИО | Телефон")
    with open('phone.txt', "r", encoding="utf-8") as data:
        tel_book = data.read()
        print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
    tel_book_lines = tel_book.split("\n")
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f"Удалена запись: {del_tel_book_lines}\n")
    with open('phone.txt', "w", encoding='utf-8') as data:
        data.write("\n".join(tel_book_lines))

def main():
    my_choice = -1
    file_tel = "phone.txt"



