import subprocess as sub
import os
import ampy


def ls() -> list:
    files: str = sub.check_output(["ampy", "ls"]).decode('utf-8')
    listOfFiles: list = files.split("\n/")
    listOfFiles[0] = listOfFiles[0][1:]
    listOfFiles[len(listOfFiles)-1] = listOfFiles[len(listOfFiles)-1][:-1]
    return listOfFiles


def removeOldFilesFromMC():
    listOfFiles = ls()
    if not listOfFiles or listOfFiles == ['']:
        print("The microcontroller is empty")
        return 0

    for file in listOfFiles:
        p = sub.Popen(["ampy", "rm", file], stdout=sub.PIPE, stderr=sub.PIPE)
        p.communicate()
        if p.returncode == 0:  # ужасный способ
            print("Deleting file", file)
        if p.returncode == 1:  # значит это директория
            sub.call(["ampy", "rmdir", file])
            print("Deleting directory", file)


def pushAllFiles():
    for root, dirs, files in os.walk(os.getcwd()):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        files[:] = [f for f in files if not f.endswith("sh") and not f.startswith(".")]

        for directory in dirs:
            pathToDir = os.path.relpath(os.path.join(root, directory))
            try:
                sub.call(["ampy", "mkdir", pathToDir])
                print(f"Creating folder {pathToDir}")
            except ampy.files.DirectoryExistsError: # возможно убрать
                print(f"Папка {pathToDir} существует")

        for file in files:
            pathToFile = os.path.relpath(os.path.join(root, file))
            sub.call(["ampy", "put", pathToFile, pathToFile])
            print(f"Пушу файл {pathToFile}")


def run():
    sub.call(["ampy", "run", "main.py"])


removeOldFilesFromMC()
pushAllFiles()
run()
