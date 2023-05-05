import PySimpleGUI as sg

img01 = sg.Image('BC3.png')
font01 = ('MS Serif', 12)
font02 = ('MS Serif', 20)

############ Frame 01 ######################
txt01 = sg.Text ('Let us see if you can solve this', font = font01, background_color = '#4B3619')
img02 = sg.Image ('apple.png', background_color = '#4B3619')
txt02 = sg.Text ('+', font = font02, background_color = '#4B3619')
img03 = sg.Image ('apple.png', background_color = '#4B3619')
txt03 = sg.Text ('+', font = font02, background_color = '#4B3619')
img04 = sg.Image ('apple.png', background_color = '#4B3619')
txt04 = sg.Text ('= 30', font = font02, background_color = '#4B3619')

img05 = sg.Image ('apple.png', background_color = '#4B3619')
txt05 = sg.Text ('+', font = font02, background_color = '#4B3619')
img06 = sg.Image ('banana_4.png', background_color = '#4B3619')
txt06 = sg.Text ('+', font = font02, background_color = '#4B3619')
img07 = sg.Image ('banana_4.png', background_color = '#4B3619')
txt07 = sg.Text ('= 18', font = font02, background_color = '#4B3619')

img08 = sg.Image ('banana_4.png', background_color = '#4B3619')
txt08 = sg.Text ('-', font = font02, background_color = '#4B3619')
img09 = sg.Image ('coconut_2.png', background_color = '#4B3619')
txt09 = sg.Text ('= 2', font = font02, background_color = '#4B3619')

img10 = sg.Image ('coconut_1.png', background_color = '#4B3619')
txt10 = sg.Text ('+', font = font02, background_color = '#4B3619')
img11 = sg.Image ('apple.png', background_color = '#4B3619')
txt11 = sg.Text ('+', font = font02, background_color = '#4B3619')
img12 = sg.Image ('banana_3.png', background_color = '#4B3619')
txt12 = sg.Text ('=', font = font02, background_color = '#4B3619')
spn01 = sg.Spin (tuple(range(1,100)), size = 2,font = font02, key = 'SPN01')
btn01 = sg.Button ('Check', font = font01, key = 'BTN01')
btn02 = sg.Button ('Continue', visible = False, font = font01, key = 'BTN02')

layout_frm01 = [[txt01], [img02, txt02, img03, txt03, img04, txt04], [img05, txt05, img06, txt06, img07, txt07], [img08, txt08, img09, txt09], [img10, txt10, img11, txt11, img12, txt12, spn01, btn01, btn02]]
frm01 = sg.Frame('', layout_frm01, visible = True, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM01')

################ Frame 02 ############################
txt13 = sg.Text ('''
King Edward is Prince Thomas' father. King Edward is 35 years old. Three years ago, King Edward was four times as old as his son was then.
How old is Prince Thomas now?\n\n''',font = font01, background_color = '#4B3619' )
btn03 = sg.Button('10', font = font01, size=(11,1), key = 'BTN03')
btn04 = sg.Button('11', font = font01, size=(11,1), key = 'BTN04')
btn05 = sg.Button('12', font = font01, size=(11,1), key = 'BTN05')
btn06 = sg.Button('13', font = font01, size=(11,1), key = 'BTN06')

txt14 = sg.Text ('''
\n\nOne brother says of his younger brother:
“Two years ago, I was three times as old as my brother was. In three years’ time, I will be twice as old as my brother.”
How old are they each now? \n\n''',font = font01, visible = False, background_color = '#4B3619' )
btn07 = sg.Button('20 and 10', font = font01, visible = False, size=(11,1), key = 'BTN07')
btn08 = sg.Button('15 and 5', font = font01, visible = False, size=(11,1), key = 'BTN08')
btn09 = sg.Button('17 and 7', font = font01, visible = False, size=(11,1), key = 'BTN09')
btn10 = sg.Button('18 and 8', font = font01, visible = False, size=(11,1), key = 'BTN10')

btn11 = sg.Button ('Continue', font = font01, visible = False, key = 'BTN11')

layout_frm02 = [[txt13], [btn03, btn04, btn05, btn06], [txt14], [btn07, btn08, btn09, btn10], [btn11]]
frm02 = sg.Frame('', layout_frm02, size=(1920,1080), visible = False, element_justification = 'c', background_color = '#4B3619', key = 'FRM02')

list_points_math02 = []



layout = [[img01], [frm01, frm02]]

window = sg.Window('', layout, element_justification='c', background_color = '#4B3619').Finalize()
window.Maximize()

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'BTN_RD_16':
        break
    
    elif event == 'BTN01':
        answer = int(values['SPN01'])
        if answer == 14:
            sg.popup('Correct!', text_color='black', background_color = '#cba331', font = font01)
            list_points_math02.append(1)
            btn01.update(visible = False)
            btn02.update(visible = True)
        else:
            sg.popup('Wrong!', text_color='black', background_color = '#cba331', font = font01)
            btn01.update(visible = False)
            btn02.update(visible = True)
    elif event == 'BTN02':
        window['FRM01'].update(visible = False)
        window['FRM02'].update(visible = True)
    elif event == 'BTN03':
        btn03.update(disabled = True, button_color = 'grey')
        btn04.update(disabled = True)
        btn05.update(disabled = True)
        btn06.update(disabled = True)
        txt14.update(visible = True)
        btn07.update(visible = True)
        btn08.update(visible = True)
        btn09.update(visible = True)
        btn10.update(visible = True)

    elif event == 'BTN04':
        list_points_math02.append(1)
        btn04.update(disabled = True, button_color = 'grey')
        btn03.update(disabled = True)
        btn05.update(disabled = True)
        btn06.update(disabled = True)
        txt14.update(visible = True)
        btn07.update(visible = True)
        btn08.update(visible = True)
        btn09.update(visible = True)
        btn10.update(visible = True)
    elif event == 'BTN05':
        btn05.update(disabled = True, button_color = 'grey')
        btn03.update(disabled = True)
        btn04.update(disabled = True)
        btn06.update(disabled = True)
        txt14.update(visible = True)
        btn07.update(visible = True)
        btn08.update(visible = True)
        btn09.update(visible = True)
        btn10.update(visible = True)
    elif event == 'BTN06':
        btn06.update(disabled = True, button_color = 'grey')
        btn03.update(disabled = True)
        btn04.update(disabled = True)
        btn05.update(disabled = True)
        txt14.update(visible = True)
        btn07.update(visible = True)
        btn08.update(visible = True)
        btn09.update(visible = True)
        btn10.update(visible = True)
    elif event == 'BTN07':
        btn07.update(disabled = True, button_color = 'grey')
        btn08.update(disabled = True)
        btn09.update(disabled = True)
        btn10.update(disabled = True)
        btn11.update(visible = True)
    elif event == 'BTN08':
        btn08.update(disabled = True, button_color = 'grey')
        btn07.update(disabled = True)
        btn09.update(disabled = True)
        btn10.update(disabled = True)
        btn11.update(visible = True)
    elif event == 'BTN09':
        btn09.update(disabled = True, button_color = 'grey')
        list_points_math02.append(1)
        btn07.update(disabled = True)
        btn08.update(disabled = True)
        btn10.update(disabled = True)
        btn11.update(visible = True)
    elif event == 'BTN10':
        btn10.update(disabled = True, button_color = 'grey')
        btn07.update(disabled = True)
        btn08.update(disabled = True)
        btn09.update(disabled = True)
        btn11.update(visible = True)
    
    elif event == 'BTN11':
        math_2_points = int(sum(list_points_math02)/1)
        if math_2_points >= 2:
            sg.popup(f'Congratulations, you have {math_2_points} correct answers!', text_color='black', background_color = '#cba331', font = font01)
            break
        else:
            sg.popup('Sorry, you failed this task!', text_color='black', background_color = '#cba331', font = font01)
            break

window.close()


