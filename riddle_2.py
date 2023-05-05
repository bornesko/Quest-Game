import PySimpleGUI as sg

img01 = sg.Image('BB2.png')
font01 = ('MS Serif', 12)

############ Frame 1 #####################
txt01 = sg.Text(
"""
Five people were eating apples, A finished before B, but behind C. D finished before E, but behind B. What was the finishing order?
""", font = font01, background_color = '#4B3619')
rad01 = sg.Radio('ACBDE', group_id = 'RadGroup', font = font01, background_color = '#4B3619', key = 'RAD01')
rad02 = sg.Radio('CABDE', group_id = 'RadGroup', background_color = '#4B3619', font = font01, key = 'RAD02')
rad03 = sg.Radio('BACDE', group_id = 'RadGroup', background_color = '#4B3619', font = font01, key = 'RAD03')
txt_free = sg.Text ('\n', background_color = '#4B3619')
btn01 = sg.Button('Check', font = font01, key = 'BTN01')
btn02 = sg.Button('Continue', visible = False, font = font01, key = 'BTN02')

layout_fr1 = [[txt01], [rad01], [rad02], [rad03], [txt_free], [btn01, btn02]]
frm01 = sg.Frame('', layout_fr1, visible = True, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM01')
##################################################################################

############### Frame 2 ##########################3
txt02 = sg.Text('''
I am a creature that always needs to be fed, but I am not alive. The more you give me, the larger I become, but I cannot grow forever.
In fact, eventually, I will consume everything and then disappear.\n
''', font = font01, background_color = '#4B3619')
inp01 = sg.Input('', size = (30,None), font = font01, key = 'INP01')
txt_free1 = sg.Text ('\n', background_color = '#4B3619')
btn03 = sg.Button('Check', font = font01, key = 'BTN03')
btn04 = sg.Button('Continue', visible = False, font = font01, key = 'BTN04')

layout_fr2 = [[txt02], [inp01], [txt_free1], [btn03, btn04]]
frm02 = sg.Frame('', layout_fr2, visible = True, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM02')
#################################################################################

############### Frame 3 ##########################3
txt03 = sg.Text('''
You have three switches in front of you, but you don't know which one controls which light bulb in the next room. You can only enter the room once,
and you can't see the bulbs from the switches. How can you determine which switch controls which bulb?

Here are the options for you to choose from and be careful - you have only 1 try:\n
''', font = font01, background_color = '#4B3619')
btn05= sg.Button('''
A) Flip one switch and leave it on for a few minutes, then turn it off and flip another switch on.
Leave that switch on and enter the room to observe the bulbs.
''', size = (100,3), font = font01, key = 'BTN05')
btn06 = sg.Button('''
B) Flip one switch on and leave it on, flip another switch on and then off, and leave the third
switch off. Enter the room to observe the bulbs.
''', size = (100,3), font = font01, key = 'BTN06')
btn07 = sg.Button('''
C) Flip two switches on and leave them on for a few minutes, then turn them both off and flip the
third switch on. Enter the room to observe the bulbs.
''', size = (100,3), font = font01, key = 'BTN07')

layout_fr3 = [[txt03], [btn05], [btn06], [btn07]]
frm03 = sg.Frame('', layout_fr3, visible = True, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM03')
#################################################################################


list_points_riddle02 = []

layout = [[img01],[frm01, frm02, frm03]]

window = sg.Window('', layout, element_justification='c', background_color = '#4B3619').Finalize()
window.Maximize()

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'BTN_RD_16':
        break
    
    elif event == 'BTN01':
        answer = values ['RAD02']
        if answer:
            sg.popup('You have answered correctly!', text_color='black', background_color = '#cba331', font = font01)
            list_points_riddle02.append(1)
            btn01.update(visible = False)
            btn02.update(visible = True)
        else:
            sg.popup('Wrong, The answer was CABDE. Putting the first three in order, A finished in front of B but behind C, so CAB. Then, we know D finished before B, so CABD. We know E finished after D, so CABDE.', text_color='black', background_color = '#cba331', font = font01)
            btn01.update(visible = False)
            btn02.update(visible = True)
            
    elif event == 'BTN02':
        window['FRM01'].update(visible = False)
        window['FRM02'].update(visible = True)
    
    elif event == 'BTN03':
        answer_2 = str(values['INP01'].lower())
        if answer_2 == 'fire' or answer_2 == 'a fire':
            sg.popup('You have answered correctly!', text_color='black', background_color = '#cba331', font = font01)
            list_points_riddle02.append(1)
            btn03.update(visible = False)
            btn04.update(visible = True)
        else:
            sg.popup('Wrong, The correct answer was "Fire"', text_color='black', background_color = '#cba331', font = font01)
            btn03.update(visible = False)
            btn04.update(visible = True)
    
    elif event == 'BTN04':
        window['FRM02'].update(visible = False)
        window['FRM03'].update(visible = True)
    
    elif event == 'BTN05':
        list_points_riddle02.append(1)
        btn05.update(button_color = 'grey', disabled = True)
        btn06.update(disabled = True)
        btn07.update(disabled = True)
        sg.popup('You have answered correctly!', text_color='black', background_color = '#cba331', font = font01)
        riddle_2_points = int(sum(list_points_riddle02)/1)
        if riddle_2_points >= 2:
            sg.popup(f'Congratulations, you have passed this trial with {riddle_2_points} points out of 3', text_color='black', background_color = '#cba331', font = font01)
            break
        else:
            sg.popup('You have failed this trial. Better luck next time!', text_color='black', background_color = '#cba331', font = font01)
            break
    elif event == 'BTN06':
        btn06.update(button_color = 'grey', disabled = True)
        btn05.update(disabled = True)
        btn07.update(disabled = True)
        sg.popup('Wrong, The correct answer was "A)"', text_color='black', background_color = '#cba331', font = font01)
        riddle_2_points = int(sum(list_points_riddle02)/1)
        if riddle_2_points >= 2:
            sg.popup(f'Congratulations, you have passed this trial with {riddle_2_points} points out of 3', text_color='black', background_color = '#cba331', font = font01)
            break
        else:
            sg.popup('You have failed this trial. Better luck next time!', text_color='black', background_color = '#cba331', font = font01)
            break
    elif event == 'BTN07':
        btn07.update(button_color = 'grey', disabled = True)
        btn05.update(disabled = True)
        btn06.update(disabled = True)
        sg.popup('Wrong, The correct answer was "A)"', text_color='black', background_color = '#cba331', font = font01)
        riddle_2_points = int(sum(list_points_riddle02)/1)
        if riddle_2_points >= 2:
            sg.popup(f'Congratulations, you have passed this trial with {riddle_2_points} points out of 3', text_color='black', background_color = '#cba331', font = font01)
            break
        else:
            sg.popup('You have failed this trial. Better luck next time!', text_color='black', background_color = '#cba331', font = font01)
            break
            
      
window.close()