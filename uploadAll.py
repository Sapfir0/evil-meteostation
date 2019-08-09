import subprocess as sub
import os
import ampy


def ls() -> list:
    files: str = sub.check_output(["ampy", "ls"]).decode('utf-8')
    listOfFiles: list = files.split("\n/")
    listOfFiles[0] = listOfFiles[0][1:]
    listOfFiles[len(listOfFiles)-1] = listOfFiles[len(listOfFiles)-1][:-1]
    print(listOfFiles)


def removeOldFilesFromMC():
    listOfFiles = ls()
    for file in listOfFiles:
        try:
            sub.call(["ampy", "rmdir", file])
        except RuntimeError:
            sub.call(["ampy", "rm", file])


def createAll

for root, dirs, files in os.walk(os.getcwd()):
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    files[:] = [f for f in files if not f.endswith("sh") and not f.startswith(".")]
    for dir in dirs:
        pathToDir = os.path.relpath(os.path.join(root, dir))
        try:
            sub.call(["ampy", "mkdir", pathToDir])
        except ampy.files.DirectoryExistsError:
            print("Папка создана")

    for file in files:
        pathToFile = os.path.relpath(os.path.join(root, file))
        print(pathToFile)
        sub.call(["ampy", "put", pathToFile])





sub.call(["ampy", "run", "main.py"])
