import PySimpleGUI as sg
sg.theme("BrightColors")
sg.theme_text_color("#BF00FF")
window = sg.Window(title="Contoh Button",
                   layout=[[sg.Text("Contoh Button")],
                           [sg.Button("Button Simpan")],
                           [sg.Button("Button Keluar")]],
                   size=(400,200),
                   font=("Comic", 18, "bold"))
kejadian,nilai = window.read()
print(kejadian, "=>", nilai)
window.close()