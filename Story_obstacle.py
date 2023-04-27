import PySimpleGUI as sg
#############SLIDE AB2###########################################################################################################################
fontSAB21 = ('MS Serif', 35)
fontSAB22 = ('MS Serif', 12)
imgSAB21 = sg.Image ('TestImage.png')
txtSAB21 = sg.Text("""
The figure lets out a roar and sprints towards me, in a split second before I can even process
my next actions it stands before me. Looking down at me it growls “Fresh flesh, what a delicacy.
I will have fun with you Zehahah. Unfortunately, you get to live a little longer I am forced to
give you a chance. I will tell you a little story if you can deduce who the killer is you win
however if you can’t I will tear you limb from limb Zehaha.”   
""", background_color = '#4B3619', font = fontSAB22, key= 'TXT_SAB21')
txtSAB22 = sg.Text("""
In the medieval town of Willowfield, a rich lord named James Leonard was found murdered on a Sunday afternoon in his luxurious manor.
The authorities were called in, and the inspector began to interview the potential suspectswho were present in the manor at the time of the murder.

-The maid, Alice, told the inspector that she was cleaning the hallways and the stables. She was cleaning them for some hours.

-The cook, John, stated that he had been preparing the food for the past hour, and he had not left the kitchen since then. He was cooking breakfast
for the lord’s household in the kitchen.

-The butler, William, reported that he was running errands for the lord in the nearby village. He claims that he was in the village the whole day.

-The gardener, Thomas, informed the inspector that he was working in the vegetable garden at the time of the murder. He was planting tomato seeds.

-The wife, Elizabeth, told the inspector that she was reading a book in the living room and enjoying a cup of tea next to the fireplace.

Who did it?
""", visible=False, background_color = '#4B3619', font = fontSAB22, key= 'TXT_SAB22')

btnSAB21 = sg.Button('Listen', font = fontSAB22, key='BTN_SAB21')
radioSAB21 = sg.Radio('The maid- Alice', font = fontSAB22, visible=False, background_color = '#4B3619', group_id= 'RadGroup', key= 'RB1')
radioSAB22 = sg.Radio('The cook- John', font = fontSAB22,visible=False, background_color = '#4B3619', group_id= 'RadGroup', key= 'RB2')
radioSAB23 = sg.Radio('The butler- William', font = fontSAB22, visible=False, background_color = '#4B3619', group_id= 'RadGroup', key= 'RB3')
radioSAB24 = sg.Radio('The gardener- Thomas', font = fontSAB22, visible=False, background_color = '#4B3619', group_id= 'RadGroup', key= 'RB4')
radioSAB25 = sg.Radio('The wife- Elizabeth', font = fontSAB22,visible=False, background_color = '#4B3619', group_id= 'RadGroup', key= 'RB5')

txtSAB23= sg.Text("""
“Wrong little one…” as I desperately try to flee, the long claws of the demonic wolf swipe at me severing my head in one go.
""", visible=False, background_color = '#4B3619', font = fontSAB22, key= 'TXT_SAB23') 
btnSAB22 = sg.Button('Answer', visible= False, font=fontSAB22, key= 'BTN_SAB22')
btnSAB23 = sg.Button('Continue', visible= False, font=fontSAB22, key= 'BTN_SAB23')


layout_SAB2 = [[imgSAB21], [txtSAB21,txtSAB22,txtSAB23], [radioSAB21,radioSAB22,radioSAB23,radioSAB24,radioSAB25], [btnSAB21,btnSAB22,btnSAB23]]
frmSAB2 = sg.Frame ('', layout_SAB2, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRMSAB2')
################################################################################################################################################
layout = [[frmSAB2]]

window = sg.Window('Quest Game', layout,  element_justification='c', background_color = '#4B3619').Finalize()
window.Maximize()

while True:
    event, values = window.read()
    if event == 'BTN_SAB21':
        window['BTN_SAB21'].update(visible= False)
        window['BTN_SAB22'].update(visible= True)
        window['RB1'].update(visible= True)
        window['RB2'].update(visible= True)
        window['RB3'].update(visible= True)
        window['RB4'].update(visible= True)
        window['RB5'].update(visible= True)
        window['TXT_SAB21'].update(visible= False)
        window['TXT_SAB22'].update(visible= True)
    elif event == 'BTN_SAB22':
        window['BTN_SAB22'].update(visible= False)
        window['BTN_SAB23'].update(visible= True)
        correct= values['RB2']
        if correct:
            sg.popup('Correct, the cook lied about making breakfast during the afternoon', text_color='black', background_color = '#cba331', font = fontSAB22)
        else:
            sg.popup('Wrong, it was the cook who lied about making breakfast in the afternoon', text_color='black', background_color = '#cba331', font = fontSAB22)
            window['TXT_SAB22'].update(visible= False)
            window['TXT_SAB23'].update(visible= True)
            window['RB1'].update(visible= False)
            window['RB2'].update(visible= False)
            window['RB3'].update(visible= False)
            window['RB4'].update(visible= False)
            window['RB5'].update(visible= False)
    
    
    #Cambia este if por elif.
    if event == sg.WIN_CLOSED or event == 'BTN_SALIR' or event == 'BTN_SAB23':
        break

window.close()