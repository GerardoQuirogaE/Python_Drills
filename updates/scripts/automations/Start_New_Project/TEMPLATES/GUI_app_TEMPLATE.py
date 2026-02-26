import PySimpleGUI as sg

# ------- GUI Definition ------- #
layout = [
    [sg.Text("Input File:"), sg.Input(key="-IN-"), sg.FileBrowse()],
    [sg.Text("Output Folder:"), sg.Input(key="-OUT-"), sg.FolderBrowse()],
    [sg.Exit(), sg.Button("Convert to CSV")],   
]

window = sg.Window("Excel to CSV Converter", layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break

window.close()