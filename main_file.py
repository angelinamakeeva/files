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
    os.chdir(parent_dir)
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
    pass

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
