import os
from shutil import move

'''''''''''''''''''''''''''''''''''
  To move straight to main search 
  this (Highlight then Ctrl + F): 
               PTY4B
'''''''''''''''''''''''''''''''''''

# Directories:
_CurrentDirectory = os.path.dirname(os.path.abspath(__file__))
_TempFolder = _CurrentDirectory + '\\TempFolder'
_Trash = _CurrentDirectory + '\\Trash'

_Unknown = _TempFolder + '\\Unknown'
_PictureFolder = _TempFolder + '\\Pictures'
_VideoFolder = _TempFolder + '\\Videos'
_DocumentFolder = _TempFolder + '\\Documents'
_SourceFolder = _TempFolder + '\\SourceFiles'
_AudioFolder = _TempFolder + '\\AudioFiles'
_CompressedFileFolder = _TempFolder + '\\CompressedFiles'
_ExecutableFolder = _TempFolder + '\\ExecutableFiles'

directoriesToCreate = [_TempFolder, _Trash, _PictureFolder,
                       _VideoFolder, _DocumentFolder, _SourceFolder,
                       _AudioFolder, _CompressedFileFolder, _ExecutableFolder]

# Types of known files:
_Pictures = ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.raw', '.svg', '.bmp', '.tiff']
_Videos = ['.mp4', '.mov', '.avi', '.wmv', '.avchd', '.webm', '.flv', '.f4v', '.mkv']
_Documents = ['.pdf', '.txt', '.docx', '.doc', '.docm', '.dot', '.html', '.htm', '.odt', '.rtf', '.wps', '.xps', '.csv', '.xml', '.xps', '.pptx', '.dif', '.psd']
_SourceFiles = ['.py', '.cpp', '.c', '.java', '.h']
_Audios = ['.wav', '.flac', '.mp3', '.ogg', '.m3u', '.acc', '.wma', '.midi', '.aif', '.m4a', '.mpa', '.pls']
_Archives = ['.7z', '.tgz', '.rar', '.zip', '.tar', '.iso', '.bz2']
_Executables = ['.exe', '.bat']




# All Functions:
def CreateFolders():
    '''''''''''''''''''''''''''''''''''
    Creates the TempFolder and ExcessF-
      older in the current directory.
    Then, creates all the categorical
        folders inside TempFolder.
    '''''''''''''''''''''''''''''''''''    
    for directory in directoriesToCreate:
        if not os.path.exists(directory):
            os.mkdir(directory)    

    
def SortFiles():
    '''''''''''''''''''''''''''''''''''
    Moves all known file types to their
    corresponding folders and moves all
    unknown filetypes to Unkown folder.
    '''''''''''''''''''''''''''''''''''
    for root, directories, files in os.walk(_CurrentDirectory):
            if root in directoriesToCreate:
                continue

            for file in files:
                if file == 'DirectorySorter.py':
                    continue
                print('Moving: ' + file)
                PlaceFile(file, root)
            
    
def PlaceFile(file, root):
    '''''''''''''''''''''''''''''''''''
    Identifies then sorts all filetypes 
      in their corresponding folders.
    '''''''''''''''''''''''''''''''''''
    # Separating File Type and File Name 
    fileSplit = os.path.splitext(file) # Full Version
    fileName = fileSplit[0]
    fileType = fileSplit[1]
    fileTypeLower = fileType.lower()
    
    path = os.path.join(root, file)
    destination = ''

    if fileTypeLower in _Pictures:
        destination = _PictureFolder
    elif fileTypeLower in _Videos:
        destination = _VideoFolder
    elif fileTypeLower in _Documents:
        destination = _DocumentFolder
    elif fileTypeLower in _SourceFiles:
        destination = _SourceFolder
    elif fileTypeLower in _Archives:
        destination = _CompressedFileFolder
    elif fileTypeLower in _Audios:
        destination = _AudioFolder
    elif fileTypeLower in _Executables:
        destination = _ExecutableFolder
    else: 
        destination = _Unknown
    
    renameCounter = 1

    if os.path.exists(os.path.join(destination, file)):
        newName = fileName + f' ({renameCounter})' + fileType
        while os.path.exists(os.path.join(destination, newName)):
            renameCounter += 1
            newName = fileName + f'({renameCounter})' + fileType

        newPath = os.path.join(root, newName)
        os.rename(path, newPath)
        path = newPath

    move(path, destination)

def MoveEmptyFolders():
    '''''''''''''''''''''''''''''''''''
    Moves all of the empty folders into
            the trash folder.
    '''''''''''''''''''''''''''''''''''
    for content in os.listdir(_CurrentDirectory):
        contentAbs = os.path.join(_CurrentDirectory, content)
        if contentAbs in directoriesToCreate:
            continue

        if os.path.isdir(contentAbs):
            move(contentAbs, _Trash)

def UnpackTemp():
    '''''''''''''''''''''''''''''''''''
     Moves all contents of TempFolder
        into the current directory.
    '''''''''''''''''''''''''''''''''''
    for content in os.listdir(_TempFolder):
        move(os.path.join(_TempFolder, content), _CurrentDirectory)
    move(_TempFolder, _Trash)

def Run():
    '''''''''''''''''''''''''''''''''''
    Instructions to sort the directory 
         where the .py file exists.
    '''''''''''''''''''''''''''''''''''
    CreateFolders()
    SortFiles()
    MoveEmptyFolders()
    UnpackTemp()

# Main ( PTY4B )
if __name__ == "__main__":
    Run()