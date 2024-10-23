import PySimpleGUI as sg
sg.theme("DarkPurple")
sg.theme_text_color("#00FF00")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("FTI UNISKA ")],
                           [sg.Text("FAKULTAS TEKNOLOGI INFORMASI ")],
                           [sg.Text("UNISKA MAB BANJARMASIN ")]],
                   size=(430, 200),
                   font=("Arial", 16, "italic"))
window()
window.close()