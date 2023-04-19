import PySimpleGUI as sg

######Slide0################################################################################################################
font1 = ("MS Serif", 15)
font2= ("MS Serif", 35)
txtS01= sg.Text('Welcome to ####', font=font2)
txtS02= sg.Text('Please enter your name!')
inpS01= sg.Input('',size= (30,None), key = 'INP_S01')
btnS01= sg.Button('Continue', key = 'BTN_S01')
layout_frS0= [[txtS01], [txtS02,inpS01], [btnS01]]
frmS0= sg.Frame('', layout_frS0,font=font1,  element_justification='c', size=(1920,1080), background_color = '#4B3619', key= 'FRMS0')
############################################################################################################################
layout = [[frmS0]]

window = sg.Window('Quest Game', layout, font=font1,  element_justification='c', background_color = '#4B3619').Finalize()
window.Maximize()

while True:
    event, values = window.read()
    
    #Cambia este if por elif.
    if event == sg.WIN_CLOSED or event == 'BTN_SALIR':
        break

window.close()