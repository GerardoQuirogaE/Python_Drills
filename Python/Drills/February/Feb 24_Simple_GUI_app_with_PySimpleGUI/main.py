"""
I followed the tutorial from the creator `Coding is Fun`. Here is the link: ["Create an advanced GUI app with PySimpleGUI (Full Tutorial)"]("https://www.youtube.com/watch?v=LzCfNanQ_9c")
"""


from pathlib import Path  # core python module

import pandas as pd  # pip install pandas openpyxl
import FreeSimpleGUI as sg  # pip install FreeSimpleGUI


def convert_to_csv(excel_file_path, output_folder, sheet_name, separator, decimal):
    df = pd.read_excel(excel_file_path, sheet_name)
    filename = Path(excel_file_path).stem
    outputfile = Path(output_folder) / f"{filename}.csv"
    df.to_csv(outputfile, sep=separator, decimal=decimal, index=False)
    sg.popup_no_titlebar("Done! :)")

# ------- GUI Definition ------- #
layout = [[sg.Text("Input File:"), sg.Input(key="-IN-"), sg.FileBrowse(file_types=(("Excel FIles", "*.xls*"),))],
    [sg.Text("Output Folder:"), sg.Input(key="-OUT-"), sg.FolderBrowse()],
    [sg.Exit(), sg.Button("Convert to CSV")],]

window = sg.Window("Excel to CSV Converter", layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == "Convert To CSV":
        print("Running convert_to_csv")
        convert_to_csv(
            excel_file_path=values["-IN-"],
            output_folder=values["-OUT-"],
            sheet_name="Sheet1",
            separator="|",
            decimal=".",
        )
        print("csv created")




window.close()