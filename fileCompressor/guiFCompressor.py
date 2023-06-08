import PySimpleGUI
from zipcreator import make_archive

# UI Code for the selection of the file
label1 = PySimpleGUI.Text("Select Files To Compress")
inputSelect = PySimpleGUI.Input()
choose1 = PySimpleGUI.FilesBrowse('Choose',key='files')

# UI Code for the destination of the file
label2 = PySimpleGUI.Text("Select Destination Folder")
inputDestination = PySimpleGUI.Input()
choose2 = PySimpleGUI.FolderBrowse('Choose',key='folder')

# Compress Button
compress = PySimpleGUI.Button("Compress")

# Window with Layouts
window = PySimpleGUI.Window("File Compressor",
                            layout=[[label1, inputSelect, choose1],
                                    [label2, inputDestination, choose2],
                                    [compress]])
while True:
    event, values = window.read()  # read() returns a dictionary of key:value pairs
    print(event, values)
    filePaths = values['files'].split(':')
    folderPaths=values['folder']
    make_archive(filePaths, folderPaths)
    window.close()
