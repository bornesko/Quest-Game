import PySimpleGUI as sg

img01 = sg.Image ('219.png')
font01 = ('MS Serif', 12)

txt01 = sg.Text ('Choose Carefully!\n\n',font = font01, background_color = '#4B3619')
btn01 = sg.Button ('Cerberus', size = (12,3), enable_events=True, key = 'BTN01')
btn02 = sg.Button ('Werewolf', size = (12,3) ,enable_events=True, key = 'BTN02')
btn03 = sg.Button ('Goblin', size = (12,3) ,enable_events=True, key = 'BTN03')
btn04 = sg.Button ('Spider', size = (12,3) ,enable_events=True, key = 'BTN04')
btn05 = sg.Button ('Mushroom', size = (12,3) ,enable_events=True, key = 'BTN05')
btn06 = sg.Button ('Fairy', size = (12,3) ,enable_events=True, key = 'BTN06')
btn07 = sg.Button ('Ogre', size = (12,3) ,enable_events=True, key = 'BTN07')
btn08 = sg.Button ('Moth Monster', size = (12,3) ,enable_events=True, key = 'BTN08')
btn09 = sg.Button ('Basilisk', size = (12,3) ,enable_events=True, key = 'BTN09')
btn10 = sg.Button ('Vampire', size = (12,3) ,enable_events=True, key = 'BTN10')
txt02 = sg.Text ('\n\nYou have made you choice wisely',font = font01, background_color = '#4B3619', visible = False)
btn_exit = sg.Button ('Continue', visible = False, key = 'BTN_EX')

layout_fr = [[img01], [txt01], [btn01, btn02, btn03, btn04, btn05], [btn06, btn07, btn08, btn09, btn10], [txt02], [btn_exit]]
frm01 = sg.Frame('', layout_fr, visible = True, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM01')

layout = [[frm01]]

btn01_pressed = False
btn02_pressed = False
btn03_pressed = False
btn04_pressed = False
btn05_pressed = False
btn06_pressed = False
btn07_pressed = False
btn08_pressed = False
btn09_pressed = False
btn10_pressed = False
btns_pressed = 0

window = sg.Window('', layout, element_justification='c', background_color = '#4B3619').Finalize()
window.Maximize()

while True:
    event, values = window.read()
    
    if event == 'BTN01':
        btn01.update(button_color = 'grey', disabled = True)
        btn01_pressed = True
        btns_pressed +=1
        if btns_pressed == 3:
            txt02.update(visible = True)
            btn01.update(disabled = True)
            btn02.update(disabled = True)
            btn03.update(disabled = True)
            btn04.update(disabled = True)
            btn05.update(disabled = True)
            btn06.update(disabled = True)
            btn07.update(disabled = True)
            btn08.update(disabled = True)
            btn09.update(disabled = True)
            btn10.update(disabled = True)
            btn_exit.update(visible = True)
            
    elif event == 'BTN02':
        btn02.update(button_color = 'grey', disabled = True)
        btn02_pressed = True
        btns_pressed +=1
        if btns_pressed == 3:
            txt02.update(visible = True)
            btn01.update(disabled = True)
            btn02.update(disabled = True)
            btn03.update(disabled = True)
            btn04.update(disabled = True)
            btn05.update(disabled = True)
            btn06.update(disabled = True)
            btn07.update(disabled = True)
            btn08.update(disabled = True)
            btn09.update(disabled = True)
            btn10.update(disabled = True)
            btn_exit.update(visible = True)
 
    elif event == 'BTN03':
        btn03.update(button_color = 'grey', disabled = True)
        btn03_pressed = True
        btns_pressed +=1
        if btns_pressed == 3:
            txt02.update(visible = True)
            btn01.update(disabled = True)
            btn02.update(disabled = True)
            btn03.update(disabled = True)
            btn04.update(disabled = True)
            btn05.update(disabled = True)
            btn06.update(disabled = True)
            btn07.update(disabled = True)
            btn08.update(disabled = True)
            btn09.update(disabled = True)
            btn10.update(disabled = True)
            btn_exit.update(visible = True)
    
    elif event == 'BTN04':
        btn04.update(button_color = 'grey', disabled = True)
        btn04_pressed = True
        btns_pressed +=1
        if btns_pressed == 3:
            txt02.update(visible = True)
            btn01.update(disabled = True)
            btn02.update(disabled = True)
            btn03.update(disabled = True)
            btn04.update(disabled = True)
            btn05.update(disabled = True)
            btn06.update(disabled = True)
            btn07.update(disabled = True)
            btn08.update(disabled = True)
            btn09.update(disabled = True)
            btn10.update(disabled = True)
            btn_exit.update(visible = True)
    
    elif event == 'BTN05':
        btn05.update(button_color = 'grey', disabled = True)
        btn05_pressed = True
        btns_pressed +=1
        if btns_pressed == 3:
            txt02.update(visible = True)
            btn01.update(disabled = True)
            btn02.update(disabled = True)
            btn03.update(disabled = True)
            btn04.update(disabled = True)
            btn05.update(disabled = True)
            btn06.update(disabled = True)
            btn07.update(disabled = True)
            btn08.update(disabled = True)
            btn09.update(disabled = True)
            btn10.update(disabled = True)
            btn_exit.update(visible = True)

    elif event == 'BTN06':
        btn06.update(button_color = 'grey', disabled = True)
        btn06_pressed = True
        btns_pressed +=1
        if btns_pressed == 3:
            txt02.update(visible = True)
            btn01.update(disabled = True)
            btn02.update(disabled = True)
            btn03.update(disabled = True)
            btn04.update(disabled = True)
            btn05.update(disabled = True)
            btn06.update(disabled = True)
            btn07.update(disabled = True)
            btn08.update(disabled = True)
            btn09.update(disabled = True)
            btn10.update(disabled = True)
            btn_exit.update(visible = True)
      
    elif event == 'BTN07':
        btn07.update(button_color = 'grey', disabled = True)
        btn07_pressed = True
        btns_pressed +=1
        if btns_pressed == 3:
            txt02.update(visible = True)
            btn01.update(disabled = True)
            btn02.update(disabled = True)
            btn03.update(disabled = True)
            btn04.update(disabled = True)
            btn05.update(disabled = True)
            btn06.update(disabled = True)
            btn07.update(disabled = True)
            btn08.update(disabled = True)
            btn09.update(disabled = True)
            btn10.update(disabled = True)
            btn_exit.update(visible = True)
   
    elif event == 'BTN08':
        btn08.update(button_color = 'grey', disabled = True)
        btn08_pressed = True
        btns_pressed +=1
        if btns_pressed == 3:
            txt02.update(visible = True)
            btn01.update(disabled = True)
            btn02.update(disabled = True)
            btn03.update(disabled = True)
            btn04.update(disabled = True)
            btn05.update(disabled = True)
            btn06.update(disabled = True)
            btn07.update(disabled = True)
            btn08.update(disabled = True)
            btn09.update(disabled = True)
            btn10.update(disabled = True)
            btn_exit.update(visible = True)
  
    elif event == 'BTN09':
        btn09.update(button_color = 'grey', disabled = True)
        btn09_pressed = True
        btns_pressed +=1
        if btns_pressed == 3:
            txt02.update(visible = True)
            btn01.update(disabled = True)
            btn02.update(disabled = True)
            btn03.update(disabled = True)
            btn04.update(disabled = True)
            btn05.update(disabled = True)
            btn06.update(disabled = True)
            btn07.update(disabled = True)
            btn08.update(disabled = True)
            btn09.update(disabled = True)
            btn10.update(disabled = True)
            btn_exit.update(visible = True)
        
    elif event == 'BTN10':
        btn10.update(button_color = 'grey', disabled = True)
        btn10_pressed = True
        btns_pressed +=1
        if btns_pressed == 3:
            txt02.update(visible = True)
            btn01.update(disabled = True)
            btn02.update(disabled = True)
            btn03.update(disabled = True)
            btn04.update(disabled = True)
            btn05.update(disabled = True)
            btn06.update(disabled = True)
            btn07.update(disabled = True)
            btn08.update(disabled = True)
            btn09.update(disabled = True)
            btn10.update(disabled = True)
            btn_exit.update(visible = True)
    
    elif event == sg.WIN_CLOSED or event == 'BTN_EX':
        break

window.close()
