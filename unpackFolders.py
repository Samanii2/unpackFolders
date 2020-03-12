""" Unpack folders program """
import os
import shutil            

def UnpackFolders():
    path = r"C:\utv\Projects\FileSorter\testdata"
    os.chdir(path)
    filesInPath = os.listdir(path)
    filesInPath.sort()

    print("Sorting list...")
    foldersToUnpack = []
    for files in filesInPath:
        if os.path.isdir(path + '/' + files):
            foldersToUnpack.append(files)

    print("Unpacking folders...")
    for folders in foldersToUnpack:
        filesInFolder = os.listdir(path + '/' + folders )
        for files in filesInFolder:
            shutil.move(path + '/' + folders + '/' + files, path + '/' + files)
        
    print("Unpacking complete.")

UnpackFolders()
