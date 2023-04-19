import PySimpleGUI as sg

######Slide0################################################################################################################
fontS01 = ("MS Serif", 15)
fontS02= ("MS Serif", 35)
txtS01= sg.Text('Welcome to ####', font=fontS02)
txtS02= sg.Text('Please enter your name!')
inpS01= sg.Input('',size= (30,None), key = 'INP_S01')
btnS01= sg.Button('Continue', key = 'BTN_S01')
layout_frS0= [[txtS01], [txtS02,inpS01], [btnS01]]
frmS0= sg.Frame('', layout_frS0,font=fontS01,  element_justification='c', size=(1920,1080), background_color = '#4B3619', key= 'FRMS0')
############################################################################################################################

#############SLIDE 1###########################################################################################################################
fontS11 = ('MS Serif', 15) 
txtS11 = sg.Text(
"""
It’s the year 3182 AE , Eldrid stands atop all in the world of Aetheria. However, the awakening of a dark force in the forest of Hadesvale
has ravaged the fertile land with the help of its dark spawn. The inhabitants of Eldrid fear for their lives and the countryside is no longer
under the protection of the Aeluminar, the king’s guard. State-issued sorcerers battle the creatures, but all seems hopeless as their numbers
seem to multiply with each passing day. Desperate the king declares wealth fame power and everything the world has to offer to whomever can
free his land of this curse. Invigorated, countless young men and women depart from their homes in search of glory.
\nOur story starts here in a Tavern not far off from the accursed woods…
""", font = fontS11)
btnS11 = sg.Button('OFF TO AN ADVENTURE!', key='BTN_S11', font = fontS11)

layout_S1 = [[txtS11], [btnS11]]
frame_S1 = sg.Frame ('', layout_S1, visible = False, size=(1920,1080), background_color = '#4B3619', element_justification = 'c', key = 'FRM_S1')
################################################################################################################################################


layout = [[frmS0],[frame_S1]]

window = sg.Window('Quest Game', layout,  element_justification='c', background_color = '#4B3619').Finalize()
window.Maximize()

while True:
    event, values = window.read()
    
    #Cambia este if por elif.
    if event == sg.WIN_CLOSED or event == 'BTN_SALIR':
        break

window.close()