import os
def acceptCommand():
    return input()

def runCommand(command):
    if command == "1":
        fileNFolderList = os.listdir()
        print("\nСписок файлов и папок: ")
        for file in fileNFolderList:
            print(file)
        print()
    elif command == "2":
        moveUp()
    elif command == "3":
        pass
    elif command == "4":
        print(countFiles(os.getcwd()), "файлов и папок")
        print()
    elif command == "5":
        pass
    elif command == "6":
        pass
    elif command == "7":
        pass

def moveUp():
    current_dir = os.getcwd() #получение текущего каталога
    parent_dir = os.path.dirname(current_dir) #возвращаем родительскую директорию
    os.chdir(parent_dir) #изменяем текущий каталог на родительский
    print("Текущая директория изменилась на родительскую", os.getcwd())


def moveDown(currendDir):
    pass

def countFiles(path):
    nodesList = os.listdir(path)
    summ = len(nodesList)
    for node in nodesList:
        if os.path.isdir(node):
            summ += countFiles(node)
    return summ

def countBytes(path):
    volume = 0 #объём в байтах
    file_list = os.listdir(path) #получаем список файлов в каталоге
    for files in file_list: #начинаем перебирать файлы в указанном каталоге
        file_name = os.path.join(path, files) #создаём полный путь к файлу, объединяя текущий путь к каталогу и имя файла
        if os.path.isfile(file_name): #проверяем является ли текущий элемент файлом
            volume += os.path.getsize(file_name) #добавляем этот размер к общему с помощью getsize
        else:
            volume += countBytes(file_name) #если текущий элемент является каталогом, то вызываем рекурсивно функцию countBytes для подсчета общего размера всех файлов внутри этого каталога, и этот размер добавляется к общему размеру
    return volume



def findFiles(target, path):
    pass

MENU = '''1. Просмотр каталога
2. На уровень вверх
3. На уровень вниз
4. Количество файлов и каталогов
5. Размер текущего каталога (в байтах)
6. Поиск файла
7. Выход из программы
Выведите пункт меню: '''
QUIT = "5"

def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command == acceptCommand()
        runCommand(command)
        if command == QUIT:
            print("Работа программы завершена")
    if __name__ == '__main__':
        main()
print(MENU)
command = int(input())
