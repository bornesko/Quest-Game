import PySimpleGUI as sg

img_riddle_11 = sg.Image ('AA3.png')
font_riddle_11 = ('MS Serif', 12)

####### Question 1 ##############
txt_riddle_11 = sg.Text(
"""
"What can’t talk but will reply when spoken to?" 
""", font = font_riddle_11, visible = True, background_color = '#4B3619')
inp_riddle_11 = sg.Input('', size = (30,None), font = font_riddle_11, key = 'INP_RD_11')
btn_riddle_11 = sg.Button('Check',font = font_riddle_11, key = 'BTN_RD_11')
btn_riddle_12 = sg.Button('Next Question',font = font_riddle_11, visible = False, key = 'BTN_RD_12')
###########################################################################

######## Question 2 #################
txt_riddle_12 = sg.Text(
"""
"Walk on the living, they don't even mumble. Walk on the dead, they mutter and grumble. What are they?"
""", font = font_riddle_11, visible = False, background_color = '#4B3619')
inp_riddle_12 = sg.Input('', size = (30,None), visible = False, font = font_riddle_11, key = 'INP_RD_12')
btn_riddle_13 = sg.Button('Check',font = font_riddle_11, visible = False, key = 'BTN_RD_13')
btn_riddle_14 = sg.Button('Next Question',font = font_riddle_11, visible = False, key = 'BTN_RD_14')
###########################################################################

######## Question 3 ###################3
txt_riddle_13 = sg.Text(
"""
"They come out at night without being called and are lost in the day without being stolen. What are they?"
""", font = font_riddle_11, visible = False, background_color = '#4B3619')
inp_riddle_13 = sg.Input('', size = (30,None), visible = False, font = font_riddle_11, key = 'INP_RD_13')
btn_riddle_15 = sg.Button('Check',font = font_riddle_11, visible = False, key = 'BTN_RD_15')
################################################################################

txt_riddle_14 = sg.Text ('',font = font_riddle_11, visible = False, background_color = '#4B3619')
txt_riddle_15 = sg.Text ('',font = font_riddle_11, visible = False, background_color = '#4B3619')
btn_riddle_16 = sg.Button('Continue',font = font_riddle_11, visible = False, key = 'BTN_RD_16')


layout_fr_riddle_1 = [[img_riddle_11], [txt_riddle_11, txt_riddle_12, txt_riddle_13, txt_riddle_14], [inp_riddle_11, inp_riddle_12, inp_riddle_13, txt_riddle_15],[btn_riddle_11, btn_riddle_12, btn_riddle_13, btn_riddle_14, btn_riddle_15, btn_riddle_16]]
frm_riddle_1 = sg.Frame('', layout_fr_riddle_1, visible = True, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM_RD_1')

list_points_riddle_1 = []

layout = [[frm_riddle_1]]

window = sg.Window('', layout, element_justification='c', background_color = '#4B3619').Finalize()
window.Maximize()

while True:
    event, values = window.read()

#Checking the input answer
    if event == 'BTN_RD_11':
        question_1_inp = str(values['INP_RD_11'].lower())
        if question_1_inp == 'echo'or question_1_inp == 'echoes':
            sg.popup('You have guessed it right!', text_color='black', background_color = '#cba331', font = font_riddle_11)
            list_points_riddle_1.append(1)
            btn_riddle_11.update(visible = False)
            btn_riddle_12.update(visible = True)
        else:
            sg.popup('Wrong!', text_color='black', background_color = '#cba331', font = font_riddle_11)
            btn_riddle_11.update(visible = False)
            btn_riddle_12.update(visible = True)

#Going to the second question
    elif event == 'BTN_RD_12':      
        txt_riddle_11.update(visible = False)
        inp_riddle_11.update(visible = False)
        btn_riddle_12.update(visible = False)
        txt_riddle_12.update(visible = True)
        inp_riddle_12.update(visible = True)
        btn_riddle_13.update(visible = True)

#Checking the input answer
    elif event == 'BTN_RD_13':
        question_2_inp = str(values['INP_RD_12'].lower())
        if question_2_inp == 'leaf' or question_2_inp == 'leaves':
            sg.popup('You have guessed it right!', text_color='black', background_color = '#cba331', font = font_riddle_11)
            list_points_riddle_1.append(1)
            btn_riddle_13.update(visible = False)
            btn_riddle_14.update(visible = True)
        else:
            sg.popup('Wrong!', text_color='black', background_color = '#cba331', font = font_riddle_11)
            btn_riddle_13.update(visible = False)
            btn_riddle_14.update(visible = True)

#Going to the second question   
    elif event == 'BTN_RD_14':
        txt_riddle_12.update(visible = False)
        inp_riddle_12.update(visible = False)
        btn_riddle_14.update(visible = False)
        txt_riddle_13.update(visible = True)
        inp_riddle_13.update(visible = True)
        btn_riddle_15.update(visible = True)
        
    elif event == 'BTN_RD_15':
        question_3_inp = str(values['INP_RD_13'].lower())
        if question_3_inp == 'star' or question_3_inp == 'stars':
            sg.popup('You have guessed it right!', text_color='black', background_color = '#cba331', font = font_riddle_11) 
            list_points_riddle_1.append(1)
            riddle_points = int(sum(list_points_riddle_1)/1)
            txt_riddle_13.update(visible = False)
            inp_riddle_13.update(visible = False)
            btn_riddle_15.update(visible = False)
            txt_riddle_14.update(f'You have collected {riddle_points}/3 points', visible = True)
            if riddle_points >= 2:
                txt_riddle_15.update('Congratulations you passed!', visible = True)
                btn_riddle_16.update(visible = True)
            else:
                txt_riddle_15.update('You Failed!', visible = True)
                btn_riddle_16.update(visible = True)
        else:
            sg.popup('Wrong!', text_color='black', background_color = '#cba331', font = font_riddle_11)
            riddle_points = int(sum(list_points_riddle_1)/1)
            txt_riddle_13.update(visible = False)
            inp_riddle_13.update(visible = False)
            btn_riddle_15.update(visible = False)
            txt_riddle_14.update(f'You have collected {riddle_points}/3 points', visible = True)
            if riddle_points >= 2:
                txt_riddle_15.update('Congratulations you passed!', visible = True)
                btn_riddle_16.update(visible = True)
            else:
                txt_riddle_15.update('You Failed!', visible = True)
                btn_riddle_16.update(visible = True)
                   
    elif event == sg.WIN_CLOSED or event == 'BTN_RD_16':
        break    
        
window.close()
    
    
    


