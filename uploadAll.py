import subprocess as sub
import os
from helpers.timeChecker import checkElapsedTime


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


def compareFiles(self):
    listOfMCFiles = ls()
    listOfPCFiles = pcLs()
    import filecmp
    print(listOfMCFiles, listOfPCFiles)
    equals = []
    for i in listOfMCFiles:
        for j in listOfPCFiles:
            if i == j:
                equals.append(i)
                break
    print(equals)
    import tempfile
    for i, item in enumerate(equals):
        p = sub.Popen(["ampy", "get", item], stdout=sub.PIPE, stderr=sub.PIPE)
        out, err = p.communicate()

        if os.path.isdir(item):
            os.mkdir(os.path.join(os.getcwd(), "temp", item))

        f = open("./temp/" + item, 'wb')
        #f.write(out)
        foo = out.decode('utf-8')
        foo = foo[:-1]
        foo2 = foo.replace('\r\n', os.linesep)
        f.write(foo2.encode('utf-8'))
        #print("./temp/" + item, "./" + item, filecmp.cmp("./temp/" + item, "./" + item))
        #print(Fore.LIGHTBLUE_EX + f.read())
        # if filecmp.cmp(mcfile.name, item):
        #     print(mcfile, item, "Схожи")
        #mcfile.close()
    for i in os.listdir():
        if os.path.isdir("./temp/" + i):
            continue
        print("./temp/" + i, i)
        # if item == "./temp/temp" or item == './temp/scripts':
        #     continue
        # print(filecmp.cmp("./temp/" + i, i))


def pcLs(directory="."):
    files = os.listdir(directory)
    return files


def ls() -> list:
    files: str = sub.check_output(["ampy", "ls"]).decode('utf-8')
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


upload(removeOldFiles=False)


# def compareFiles(self):
# listOfMCFiles = self.ls()
# listOfPCFiles = self.pcLs()
# import filecmp
# print(listOfMCFiles, listOfPCFiles)
# equals = []
# for i in listOfMCFiles:
#     for j in listOfPCFiles:
#         if i == j:
#             equals.append(i)
#             break
# print(equals)
# import tempfile
# for i, item in enumerate(equals):
#     p = sub.Popen(["ampy", "get", item], stdout=sub.PIPE, stderr=sub.PIPE)
#     out, err = p.communicate()
#     mcfile = tempfile.NamedTemporaryFile()
#     mcfile.write(out)
#     mcfile.seek(0)
#     from colorama import Fore
#     # print(mcfile.name)
#     # print(mcfile.name, item, "Не схожи")
#     # print(Fore.LIGHTGREEN_EX + mcfile.read().decode('utf-8'))
#     if item == "net" or item == "scripts":
#         continue
#     with open(item) as f:
#         f.read()
#         # print(Fore.LIGHTBLUE_EX + f.read())
#     print(filecmp.cmp(mcfile.name, item))
#     # if filecmp.cmp(mcfile.name, item):
#     #     print(mcfile, item, "Схожи")
#     # mcfile.close()
#
# # for i in equals:
# #     # for j in listOfPCFiles:
# #     #    print(filecmp.cmp(i, j))
# #     if filecmp.cmp(i, j):
# #         print(i, j)
