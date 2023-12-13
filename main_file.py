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
        current_dir = os.getcwd() 
        parent_dir = os.path.dirname(current_dir) 
        os.chdir(parent_dir) 
        print("Текущая директория изменилась", os.getcwd())
    elif command == "4":
        print(countFiles(os.getcwd()), "файлов и папок")
        print()
    elif command == "5":
        path = input()
        print(countBytes(path))
    elif command == "6":
        target = input()
        path = input()
        print(findFiles(target, path))
    elif command == "7":
        pass
        
def moveUp():
    """
    The movUp() function will change our current directory to the parent one.
    """
    current_dir = os.getcwd() 
    parent_dir = os.path.dirname(current_dir)
    os.chdir(parent_dir) 
    print("Текущая директория изменилась на родительскую", os.getcwd())


def moveDown(currentDir):
    subDir = input("Введите имя подкаталога: ")
    newDir = os.path.join(currentDir, subDir)
    if os.path.exists(newDir) and os.path.isdir(newDir):
        os.chdir(newDir)
        print("Текущая директория:", os.getcwd())
    else:
        print("Ошибка: указанный подкаталог не найден")


def countFiles(path):
    nodesList = os.listdir(path)
    summ = len(nodesList)
    for node in nodesList:
        if os.path.isdir(node):
            summ += countFiles(node)
    return summ

def countBytes(path):
    """
    The countBytes(path)  function calculates the volume in bytes of all files in the specified path directory
    """
    volume = 0 
    file_list = os.listdir(path) 
    for files in file_list: 
        file_name = os.path.join(path, files) 
        if os.path.isfile(file_name): 
            volume += os.path.getsize(file_name) 
        else:
            volume += countBytes(file_name) 
    return volume



def findFiles(target, path):
    filesList = []
    for root, dirs, files in os.walk(path): 
        for file in files:  
            if target in file: 
                filesList.append(os.path.join(root, file))  
    if len(filesList) > 0:
        return filesList  
    else:
        print("Файлы с указанным именем не найдены")
        return None  



MENU = '''1. Просмотр каталога
2. На уровень вверх
3. На уровень вниз
4. Количество файлов и каталогов
5. Размер текущего каталога (в байтах)
6. Поиск файла
7. Выход из программы
Выведите пункт меню: '''
QUIT = "7"

def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print("Работа программы завершена")
            break
    if __name__ == '__main__':
        main()

main()
