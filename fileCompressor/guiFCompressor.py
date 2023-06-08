import PySimpleGUI



label1=PySimpleGUI.Text("Select Files To Compress")
inputSelect=PySimpleGUI.Input()
choose1=PySimpleGUI.FilesBrowse('Choose')

label2=PySimpleGUI.Text("Select Destination Folder")
inputDestination=PySimpleGUI.Input()
choose2=PySimpleGUI.FolderBrowse('Choose')

compress=PySimpleGUI.Button("Compress")

window=PySimpleGUI.Window("File Compressor",
                          layout=[[label1,inputSelect,choose1],
                                  [label2,inputDestination,choose2],
                                  [compress]])
window.read()
window.close()