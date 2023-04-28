import PySimpleGUI as sg

img_math_1 = sg.Image ('TestImage.png')
font_math_1 = ('MS Serif', 12)

txt_empty_space = sg.Text ('\n', background_color = '#4B3619')
txt_empty_space_1 = sg.Text ('\n', background_color = '#4B3619')
txt_explanation_1 = sg.Text ('Pay Close Attention!', font = font_math_1, background_color = '#4B3619')
txt_explanation_2 = sg.Text ('You have only 1 try!', font = font_math_1, background_color = '#4B3619')

###################### Question 1 ##########################
txt_math_1 = sg.Text ('Look at this series: 40, 36, 34, 30, 28, … What number should come next?\n\n\n', font = font_math_1, background_color = '#4B3619')
btn_math_1 = sg.Button ('24', font = font_math_1, size=(15,1), key = 'BTN_MT_1')
btn_math_2 = sg.Button ('20', font = font_math_1, size=(15,1), key = 'BTN_MT_2')
btn_math_3 = sg.Button ('22', font = font_math_1, size=(15,1), key = 'BTN_MT_3')

###################### Question 2 ##########################
txt_math_2 = sg.Text ('What is the answer of:  6/2*(1+2) = ?\n\n\n', font = font_math_1, background_color = '#4B3619')
btn_math_4 = sg.Button ('6', font = font_math_1, size=(15,1), key = 'BTN_MT_4')
btn_math_5 = sg.Button ('0', font = font_math_1, size=(15,1), key = 'BTN_MT_5')
btn_math_6 = sg.Button ('9', font = font_math_1, size=(15,1), key = 'BTN_MT_6')

###################### Question 3 ##########################
txt_math_3 = sg.Text ('When I was four years old, my sister was half my age. Now, I am 18. How old is my sister now?\n\n', font = font_math_1, background_color = '#4B3619')
btn_math_7 = sg.Button ('16', font = font_math_1, size=(15,1), key = 'BTN_MT_7')
btn_math_8 = sg.Button ('20', font = font_math_1, size=(15,1), key = 'BTN_MT_8')
btn_math_9 = sg.Button ('18', font = font_math_1, size=(15,1), key = 'BTN_MT_9')

layout_fr_math_1 = [[txt_explanation_1], [txt_math_1], [txt_math_2], [txt_math_3]]
frm_math_1 = sg.Frame('', layout_fr_math_1, visible = True, element_justification = 'l', background_color = '#4B3619', key = 'FRM_MT_1')

layout_fr_math_2 = [[txt_explanation_2], [btn_math_1, btn_math_2, btn_math_3],[txt_empty_space], [btn_math_4, btn_math_5, btn_math_6], [txt_empty_space_1], [btn_math_7, btn_math_8, btn_math_9]]
frm_math_2 = sg.Frame('', layout_fr_math_2, visible = True, size=(500,284), element_justification = 'l', background_color = '#4B3619', key = 'FRM_RD_2')

####################### Secret Question ###########################
txt_math_4 = sg.Text ('\n\nSecret Question: Third Answer + Second Answer - First Answer = ?', font = font_math_1, background_color = '#4B3619')
inp_math_1 = sg.Input('', size = (30,None), font = font_math_1, key = 'INP_MT_1')
btn_math_10 = sg.Button('Check', font = font_math_1, key = 'BTN_MT_10')
btn_math_11 = sg.Button('Continue', font = font_math_1, visible = False, key = 'BTN_MT_11')


layout_fr_math_3 = [[txt_math_4], [inp_math_1], [btn_math_10, btn_math_11]]
frm_math_3 = sg.Frame('', layout_fr_math_3, visible = False, size=(1920, 200), element_justification = 'c', background_color = '#4B3619', key = 'FRM_MT_3')


layout = [[img_math_1], [frm_math_1 , frm_math_2], [frm_math_3]]

window = sg.Window('', layout, element_justification='c', background_color = '#4B3619').Finalize()
window.Maximize()

while True:
    event, values = window.read()

#Button events
    if event == 'BTN_MT_1':
        btn_math_1.update(button_color = 'grey', text = '')
        btn_math_2.update(disabled = True, text = '')
        btn_math_3.update(disabled = True, text = '')
    elif event == 'BTN_MT_2':
        btn_math_2.update(button_color = 'grey', text = '')
        btn_math_1.update(disabled = True, text = '')
        btn_math_3.update(disabled = True, text = '')
    elif event == 'BTN_MT_3':
        btn_math_3.update(button_color = 'grey', text = '')
        btn_math_1.update(disabled = True, text = '')
        btn_math_2.update(disabled = True, text = '')
    elif event == 'BTN_MT_4':
        btn_math_4.update(button_color = 'grey', text = '')
        btn_math_5.update(disabled = True, text = '')
        btn_math_6.update(disabled = True, text = '')
    elif event == 'BTN_MT_5':
        btn_math_5.update(button_color = 'grey', text = '')
        btn_math_4.update(disabled = True, text = '')
        btn_math_6.update(disabled = True, text = '')
    elif event == 'BTN_MT_6':
        btn_math_6.update(button_color = 'grey', text = '')
        btn_math_4.update(disabled = True, text = '')
        btn_math_5.update(disabled = True, text = '')
    elif event == 'BTN_MT_7':
        btn_math_7.update(button_color = 'grey', text = '')
        btn_math_8.update(disabled = True, text = '')
        btn_math_9.update(disabled = True, text = '')
        window['FRM_MT_3'].update(visible = True)     
    elif event == 'BTN_MT_8':
        btn_math_8.update(button_color = 'grey', text = '')
        btn_math_7.update(disabled = True, text = '')
        btn_math_9.update(disabled = True, text = '')
        window['FRM_MT_3'].update(visible = True)
    elif event == 'BTN_MT_9':
        btn_math_9.update(button_color = 'grey', text = '')
        btn_math_7.update(disabled = True, text = '')
        btn_math_8.update(disabled = True, text = '')
        window['FRM_MT_3'].update(visible = True)
    
    elif event == 'BTN_MT_10':
        answer = int(values['INP_MT_1'])
        if answer == 1:
            sg.popup('Correct!', text_color='black', background_color = '#cba331', font = font_math_1)
        else:
            sg.popup('False!', text_color='black', background_color = '#cba331', font = font_math_1)
        btn_math_10.update(visible = False)
        btn_math_11.update(visible = True)


    elif event == sg.WIN_CLOSED or event == 'BTN_MT_11':
        break

window.close()
