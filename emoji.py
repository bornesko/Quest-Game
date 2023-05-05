import PySimpleGUI as sg

font01 = ('MS Serif', 12)
img_main = sg.Image('B3.png')

############### First Question #######################
txt01 = sg.Text ('\nLet us see if you can guess this one:', font = font01, background_color = '#4B3619')
img01 = sg.Image('question_1_emoji.png', background_color = '#4B3619')
inp01 = sg.Input('', size = (30,None), font = font01, key = 'INP01')
btn01 = sg.Button ('Check', visible = True, font = font01, key = 'BTN01')
btn02 = sg.Button ('Next', visible = False, font = font01, key = 'BTN02')

layout_fr1 = [[txt01], [img01], [inp01], [btn01, btn02]]
frm01 = sg.Frame('', layout_fr1, visible = True, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM01')
#########################################################

############### 2nd Question #######################
txt02 = sg.Text ('\nThis one is a little bit harder:', font = font01, background_color = '#4B3619')
img02 = sg.Image('question_2_emoji.png', background_color = '#4B3619')
inp02 = sg.Input('', size = (30,None), font = font01, key = 'INP02')
btn03 = sg.Button ('Check', visible = True, font = font01, key = 'BTN03')
btn04 = sg.Button ('Next', visible = False, font = font01, key = 'BTN04')

layout_fr2 = [[txt02], [img02], [inp02], [btn03, btn04]]
frm02 = sg.Frame('', layout_fr2, visible = False, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM02')
#########################################################

############### 3rd Question #######################
txt03 = sg.Text ('\nLet us see how good your imagination is:', font = font01, background_color = '#4B3619')
img03 = sg.Image('question_3_emoji.png', background_color = '#4B3619')
inp03 = sg.Input('', size = (30,None), font = font01, key = 'INP03')
btn05 = sg.Button ('Check', visible = True, font = font01, key = 'BTN05')
btn06 = sg.Button ('Next', visible = False, font = font01, key = 'BTN06')

layout_fr3 = [[txt03], [img03], [inp03], [btn05, btn06]]
frm03 = sg.Frame('', layout_fr3, visible = False, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM03')
#########################################################

############### 4th Question #######################
txt04 = sg.Text ('\nLast one champion. Make it count!', font = font01, background_color = '#4B3619')
img04 = sg.Image('question_4_emoji.png', background_color = '#4B3619')
inp04 = sg.Input('', size = (30,None), font = font01, key = 'INP04')
btn07 = sg.Button ('Check', visible = True, font = font01, key = 'BTN07')

layout_fr4 = [[txt04], [img04], [inp04], [btn07]]
frm04 = sg.Frame('', layout_fr4, visible = False, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM04')
#########################################################

############## Final Frame ##########################
txt05 = sg.Text ('',font = font01, background_color = '#4B3619')
btn08 = sg.Button ('Continue', font = font01, key = 'BTN08')

layout_fr5 = [[txt05], [btn08]]
frm05 = sg.Frame('', layout_fr5, visible = False, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM05')
########################################################

list_points_emoji = []

layout = [[img_main],[frm01, frm02, frm03, frm04, frm05]]

window = sg.Window('', layout, element_justification='c', background_color = '#4B3619').Finalize()
window.Maximize()

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'BTN08':
        break
    
    elif event == 'BTN01':
        answer_1 = str(values['INP01'].lower())
        if answer_1 == 'bloodbath' or answer_1 == 'blood bath':
            sg.popup('Correct!', text_color='black', background_color = '#cba331', font = font01)
            list_points_emoji.append(1)
            btn01.update(visible = False)
            btn02.update(visible = True)
        else:
            sg.popup(f'Wrong, the word was bloodbath', text_color='black', background_color = '#cba331', font = font01)
            btn01.update(visible = False)
            btn02.update(visible = True)
    
    elif event == 'BTN02':
        window['FRM01'].update(visible = False)
        window['FRM02'].update(visible = True)
    
    elif event == 'BTN03':
        answer_2 = str(values['INP02'].lower())
        if answer_2 == 'sunglasses':
            sg.popup('Correct!', text_color='black', background_color = '#cba331', font = font01)
            list_points_emoji.append(1)
            btn03.update(visible = False)
            btn04.update(visible = True)
        else:
            sg.popup(f'Wrong, the word was sunglasses', text_color='black', background_color = '#cba331', font = font01)
            btn03.update(visible = False)
            btn04.update(visible = True)
    
    elif event == 'BTN04':
        window['FRM02'].update(visible = False)
        window['FRM03'].update(visible = True)
    
    elif event == 'BTN05':
        answer_2 = str(values['INP03'].lower())
        if answer_2 == 'crossbow':
            sg.popup('Correct!', text_color='black', background_color = '#cba331', font = font01)
            list_points_emoji.append(1)
            btn05.update(visible = False)
            btn06.update(visible = True)
        else:
            sg.popup(f'Wrong, the word was crossbow', text_color='black', background_color = '#cba331', font = font01)
            btn05.update(visible = False)
            btn06.update(visible = True)    
    
    elif event == 'BTN06':
        window['FRM03'].update(visible = False)
        window['FRM04'].update(visible = True)
    
    elif event == 'BTN07':
        answer_3 = str(values['INP04'].lower())
        if answer_3 == 'seesaw':
            sg.popup('Correct!', text_color='black', background_color = '#cba331', font = font01)
            list_points_emoji.append(1)
            points_emoji = int(sum(list_points_emoji)/1)
            if points_emoji >= 3:
                txt05.update(f'\n\nYou have {points_emoji} correct guesses. Congratulations!')
                window['FRM04'].update(visible = False)
                window['FRM05'].update(visible = True)
            else:
                txt05.update(f'\n\nYou have {points_emoji} correct guesses. Better Luck Next Time!')
                window['FRM04'].update(visible = False)
                window['FRM05'].update(visible = True)
        else:
            sg.popup(f'Wrong, the word was seesaw', text_color='black', background_color = '#cba331', font = font01)
            points_emoji = int(sum(list_points_emoji)/1)
            if points_emoji >= 3:
                txt05.update(f'\n\nYou have {points_emoji} correct guesses. Congratulations!')
                window['FRM04'].update(visible = False)
                window['FRM05'].update(visible = True)
            else:
                txt05.update(f'\n\nYou have {points_emoji} correct guesses. Better Luck Next Time!')
                window['FRM04'].update(visible = False)
                window['FRM05'].update(visible = True)
     
window.close()