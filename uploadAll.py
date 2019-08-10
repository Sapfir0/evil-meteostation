import subprocess as sub
import os
from helpers.timeChecker import checkElapsedTime
import argparse

def upload(directory=".", removeOldFiles=True, compairFiles=False, excludedFiles=[]):
    if compairFiles:
        compareFiles()
    if removeOldFiles:
        removeOldFilesFromMC()
    pushAllFiles(directory)
    run()


def push(input, output):
    sub.call(["ampy", "put", input, output])


def pull(item,  returnAllStatements=False):
    p = sub.Popen(["ampy", "get", item], stdout=sub.PIPE, stderr=sub.PIPE)
    out, err = p.communicate()
    if returnAllStatements:
        return p, err, out
    else:
        return p


def run(executable="main.py"):
    sub.call(["ampy", "run", executable])


def mkdir(pathToDir, returnAllStatements=False):
    p = sub.Popen(["ampy", "mkdir", pathToDir], stdout=sub.PIPE, stderr=sub.PIPE)
    p.communicate()
    if returnAllStatements:
        return p, err, out
    else:
        return p.returncode


def rmdir(pathToDir):
    sub.call(["ampy", "rmdir", pathToDir])


def rm(file, returnAllStatements=False):
    p = sub.Popen(["ampy", "rm", file], stdout=sub.PIPE, stderr=sub.PIPE)
    out, err = p.communicate()
    if returnAllStatements:
        return p, err, out
    else:
        return p.returncode


listOfFiles, listOfDirs = [], []
def recursiveWalk(directory="."):
    files = ls(directory)
    for file in files:
        if os.path.isdir(file):
            listOfDirs.append(file)
            recursiveWalk(file)
        else:
            listOfFiles.append(file)
    return listOfFiles, listOfDirs

def recursiveWalkPc(directory="."):
    files = os.listdir(directory)
    for file in files:
        if os.path.isdir(file):
            print(file)
            listOfDirs.append(file)
            recursiveWalkPc(file)
        else:
            listOfFiles.append(file)
    return listOfFiles, listOfDirs


def compareFiles():
    #files = ls()
    #print(files)
    #files = os.listdir()
    #print(files)

    listOfMCFiles, listOfMCDirs = recursiveWalk()  # получили названия всех файлов и директорий с мк
    #listOfPCFiles, listOfPCDirs = recursiveWalkPc()
    print(listOfMCFiles, listOfMCDirs)
    for item in listOfMCDirs:
        path = os.path.join(os.getcwd(), "temp", item)
        if not os.path.exists(path):
            os.mkdir(path)

    for item in listOfMCFiles:
        p = sub.Popen(["ampy", "get", item], stdout=sub.PIPE, stderr=sub.PIPE)
        out, err = p.communicate()
        path = os.path.join(os.getcwd(), "temp", item)
        with open(path, "wb") as f:
            foo = out.decode('utf-8')
            foo = foo[:-1]
            foo2 = foo.replace('\r\n', os.linesep)
            f.write(foo2.encode('utf-8'))
        import filecmp
    for item in listOfMCFiles:
        path1 = os.path.join(os.getcwd(), "temp", item)
        path2 = os.path.join(os.getcwd(), item)
        if path2 == '/home/sapfir/evil-meteostation/./lib':
            continue
        if path1 == '/home/sapfir/evil-meteostation/./temp/changes.diff':
            continue

        print(filecmp.cmp(path1, path2))
        print(path1, path2)



def pcLs(directory="."):
    files = os.listdir(directory)
    return files


def ls(directory='') -> list:
    files: str = sub.check_output(["ampy", "ls", directory]).decode('utf-8')
    listOfFiles: list = files.split("\n/")
    listOfFiles[0] = listOfFiles[0][1:]
    listOfFiles[len(listOfFiles) - 1] = listOfFiles[len(listOfFiles) - 1][:-1]
    return listOfFiles


def removeOldFilesFromMC() -> None:
    listOfFiles = ls()
    if not listOfFiles or listOfFiles == ['']:
        print("The microcontroller is empty")
        return 0

    for file in listOfFiles:
        status = rm(file)
        if not status:  # ужасный способ
            print("Deleting file", file)
        elif status:  # значит это директория
            rmdir(file)
            print("Deleting directory", file)


def pushAllFiles(directory="."):
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        files[:] = [f for f in files if not f.endswith("sh") and not f.startswith(".")]

        for directory in dirs:
            pathToDir = os.path.relpath(os.path.join(root, directory))
            status = mkdir(pathToDir)
            if not status:
                print(f"Creating folder {pathToDir}")
            elif status:
                print(f"Folder {pathToDir} is exists")

        for file in files:
            pathToFile = os.path.relpath(os.path.join(root, file))
            push(pathToFile, pathToFile)
            print(f"Pushing file {pathToFile}")


parser = argparse.ArgumentParser(description="Micropython uploader")
parser.add_argument('-c', '--cache', action="store_true", help="Disable remove old files from microcontroller. May be dangerous for u")
parser.add_argument('--compare', action="store_true", help="It will compaired all files in mk and in current directory and push only differently files. ")
args = parser.parse_args()
print(args)
upload(directory=".", removeOldFiles=not args.cache, compairFiles=args.compare, excludedFiles=[])

#

