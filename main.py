import PySimpleGUI as sg

txt1 = sg.Text

layout = [[]]

window = sg.Window('', layout)

while True:
    event, values = window.read()
    
    #Cambia este if por elif.
    if event == sg.WIN_CLOSED or event == 'BTN_SALIR':
        break

window.close()