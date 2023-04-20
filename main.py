import PySimpleGUI as sg

######Slide0################################################################################################################
imgS01=sg.Image('TestImage.png')
fontS01 = ("MS Serif", 15)
fontS02= ("MS Serif", 35)
txtS01= sg.Text('Welcome to ####', font=fontS02)
txtS02= sg.Text('Please enter your name!')
inpS01= sg.Input('',size= (30,None), key = 'INP_S01')
btnS01= sg.Button('Continue', key = 'BTN_S01')
layout_frS0= [[imgS01],[txtS01], [txtS02,inpS01], [btnS01]]
frmS0= sg.Frame('', layout_frS0,font=fontS01,  element_justification='c', size=(1920,1080), background_color = '#4B3619', key= 'FRMS0')
############################################################################################################################

#############SLIDE 1###########################################################################################################################
imgS11= sg.Image('TestImage.png')
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

layout_frS1 = [[imgS11],[txtS11], [btnS11]]
frmS1 = sg.Frame ('', layout_frS1, size=(1920,1080), background_color = '#4B3619', element_justification = 'c', key = 'FRMS1')
################################################################################################################################################

######Slide2################################################################################################################
imgS21= sg.Image('TestImage.png')
fontS21 = ("MS Serif", 15)
fontS22= ("MS Serif", 35)
txtS21= sg.Text('“Can I get you something, young traveler”? asks Sheamus the Bartender. On the opposite side of the bar sits a young boy dressed in plain farmers’ clothes and a bright smile on his face.')
btnS21= sg.Button('I don’t have so much gold on me, but I was wondering if you knew the easiest way to the Hadesvale woods', key = 'BTN_S21')
btnS22= sg.Button('I am just a boy passing by looking for adventure', key = 'BTN_S22')
txtS22= sg.Text(
    '''
“I don’t know why so many of you youngsters which to go to that retched place nowadays, but it’s just down the road.
I’ll get you a drink on the house young one, and we can talk about everything else later”. The bartender waddles off behind the bar'
''', visible= False)
txtS23= sg.Text(
    '''
“Ah there’s many of you these days, I am assuming you’ll be heading to Hadesvale, well it’s just down the road.
I’ll get you a drink on the house young one, and we can talk about everything else later”. The bartender waddles off behind the bar.
''',visible= False )
btnS23= sg.Button('Continue', visible= False, key= 'BTN_S23')

layout_frS2= [[imgS21], [txtS21], [btnS21,btnS22], [txtS22,txtS23], [btnS23]]
frmS2= sg.Frame('', layout_frS2,font=fontS21,  element_justification='c', size=(1920,1080), background_color = '#4B3619', key= 'FRMS2')
############################################################################################################################

layout = [[frmS0, frmS1, frmS2]]

window = sg.Window('Quest Game', layout,  element_justification='c', background_color = '#4B3619').Finalize()
window.Maximize()

while True:
    event, values = window.read()
# If statement for the button to continue to slide 1
    if event == 'BTN_S01':
        window['FRMS0'].update(visible = False)
        
# If statement for the button to continue to slide 2
    elif event == 'BTN_S11':
        window['FRMS1'].update(visible = False)

# If statement for slide 2 - for the different options inside the slide with the different text
    elif event == 'BTN_S21':
        btnS22.update(visible=False)
        txtS22.update(visible=True)
        btnS23.update(visible= True)
    elif event == 'BTN_S22':
        btnS21.update(visible=False)
        txtS23.update(visible=True)
        btnS23.update(visible= True)
    
#End
    elif event == sg.WIN_CLOSED or event == 'BTN_SALIR':
        break

window.close()