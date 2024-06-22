import os
from shutil import move

'''''''''''''''''''''''''''''''''''
   Karl will make github soon :P
  To move straight to main search 
  this (Highlight then Ctrl + F): 
               PTY4B
'''''''''''''''''''''''''''''''''''

# Directories:
_CurrentDirectory = os.getcwd()
_TempFolder = _CurrentDirectory + '\\TempFolder'
_Trash = _CurrentDirectory + '\\Trash'

_Unknown = _TempFolder + '\\Unknown'
_PictureFolder = _TempFolder + '\\Pictures'
_VideoFolder = _TempFolder + '\\Videos'
_DocumentFolder = _TempFolder + '\\Documents'
_SourceFolder = _TempFolder + '\\SourceFiles'

directoriesToCreate = [_TempFolder, _Trash, _PictureFolder,
                       _VideoFolder, _DocumentFolder, _SourceFolder]

# Types of known files:
_Pictures = ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.raw', '.svg', '.bmp', '.tiff']
_Videos = ['.mp4', '.mov', '.avi', '.wmv', '.avchd', '.webm', '.flv', '.f4v', '.mkv']
_Documents = ['.pdf', '.txt', '.docx', '.doc', '.docm', '.dot', '.html', '.htm', '.odt', '.rtf', '.wps', '.xps', '.csv', '.xml', '.xps', '.pptx', '.dif', '.psd']
_SourceFiles = ['.py', '.cpp', '.c', '.java', '.h']


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
        unknown filetypes to excess.
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
    fileType = os.path.splitext(file)[1].lower()
    path = os.path.join(root, file)

    if fileType in _Pictures:
        move(path, _PictureFolder)
    elif fileType in _Videos:
        move(path, _VideoFolder)
    elif fileType in _Documents:
        move(path, _DocumentFolder)
    elif fileType in _SourceFiles:
        move(path, _SourceFolder)
    else:
        move(path, _Unknown)

def MoveEmptyFolders():
    '''''''''''''''''''''''''''''''''''
    Moves all of the empty folders into
            the trash folder.
    '''''''''''''''''''''''''''''''''''
    for content in os.listdir(_CurrentDirectory):
        if os.path.abspath(content) not in directoriesToCreate:
            if os.path.isdir(content):
                move(os.path.abspath(content), _Trash)

def UnpackTemp():
    '''''''''''''''''''''''''''''''''''
     Moves all contents of TempFolder
        into the current directory.
    '''''''''''''''''''''''''''''''''''
    for content in os.listdir(_TempFolder):
        move(os.path.join(_TempFolder, content), _CurrentDirectory)
    move(_TempFolder, _Trash)

# Main ( PTY4B )
if __name__ == "__main__":
    CreateFolders()
    SortFiles()
    MoveEmptyFolders()
    UnpackTemp();

    