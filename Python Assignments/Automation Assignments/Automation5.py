import os, shutil

def selectiveCopy(folder, extensions, destFolder):
    folder = os.path.abspath(folder)
    destFolder = os.path.abspath(destFolder)
    print('Looking in', folder, 'for files with extensions of', ', '.join(extensions))
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            name, extension = os.path.splitext(filename)
            if extension in extensions:
                fileAbsPath = foldername + os.path.sep + filename
                print('Coping', fileAbsPath, 'to', destFolder)
                shutil.copy(fileAbsPath, destFolder)
extensions = ['.php', '.py']
folder = 'randomFolder'
destFolder = 'selectiveFolder'
selectiveCopy(folder, extensions, destFolder)