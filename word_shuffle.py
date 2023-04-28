import PySimpleGUI as sg
import random

#The words which are going to be used
#Q1 Words
list_words_1 = ['wagon','lantern','sunflower']
list_words_2 = ['horse','glass','forest']
#Q2 Words
list_words_3 = ['sword','shield','armour']
list_words_4 = ['fight','magic','hero']
#Q3 Words
list_words_5 = ['sorcerer','darkness','light']
list_words_6 = ['kingdom','castle','defence']
#Q4 Words
list_words_7 = ['crossbow','danger','immortal']
list_words_8 = ['evil','treasure','traveller']

#Picking a random word
#Q1
random_word_1 = random.choice(list_words_1)
random_word_2 = random.choice(list_words_2)
#Q2
random_word_3 = random.choice(list_words_3)
random_word_4 = random.choice(list_words_4)
#Q3
random_word_5 = random.choice(list_words_5)
random_word_6 = random.choice(list_words_6)
#Q4
random_word_7 = random.choice(list_words_7)
random_word_8 = random.choice(list_words_8)

#Shuffle the words
#Q1
shuffled_word_1 = ''.join(random.sample(random_word_1, len(random_word_1)))
shuffled_word_2 = ''.join(random.sample(random_word_2, len(random_word_2)))
#Q2
shuffled_word_3 = ''.join(random.sample(random_word_3, len(random_word_3)))
shuffled_word_4 = ''.join(random.sample(random_word_4, len(random_word_4)))
#Q3
shuffled_word_5 = ''.join(random.sample(random_word_5, len(random_word_5)))
shuffled_word_6 = ''.join(random.sample(random_word_6, len(random_word_6)))
#Q4
shuffled_word_7 = ''.join(random.sample(random_word_7, len(random_word_7)))
shuffled_word_8 = ''.join(random.sample(random_word_8, len(random_word_8)))


img_jmb_1 = sg.Image ('TestImage.png')
font_jmb_1 = ('MS Serif', 12)

################## Question 1 ############################
txt_jmb_1 = sg.Text('We will start with easier words, traveller. Let us see how cunning you are!\n\n',font = font_jmb_1, visible = True, background_color = '#4B3619')
txt_jmb_2 = sg.Text(f'{shuffled_word_1}', font = font_jmb_1, visible = True, background_color = '#4B3619')
txt_jmb_3 = sg.Text(f'\n\n{shuffled_word_2}', font = font_jmb_1, visible = True, background_color = '#4B3619')
inp_jmb_1 = sg.Input('', size = (30,None), visible = True, font = font_jmb_1, key = 'INP_JMB_1')
inp_jmb_2 = sg.Input('', size = (30,None), visible = True, font = font_jmb_1, key = 'INP_JMB_2')
btn_jmb_1 = sg.Button('Guess', font = font_jmb_1, key = 'BTN_JMB_1')
layout_fr_jmb_1 = [[txt_jmb_1], [txt_jmb_2], [inp_jmb_1], [txt_jmb_3], [inp_jmb_2], [btn_jmb_1]]
frm_jmb_1 = sg.Frame('', layout_fr_jmb_1, visible = True, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM_JMB_1')

################ Question 2 ###################################
txt_jmb_4 = sg.Text('Let us raise the level a little bit with these words! I doubt you will guess these ones.\n\n',font = font_jmb_1, visible = True, background_color = '#4B3619')
txt_jmb_5 = sg.Text(f'{shuffled_word_3}', font = font_jmb_1, visible = True, background_color = '#4B3619') 
txt_jmb_6 = sg.Text(f'\n\n{shuffled_word_4}', font = font_jmb_1, visible = True, background_color = '#4B3619')
inp_jmb_3 = sg.Input('', size = (30,None), visible = True, font = font_jmb_1, key = 'INP_JMB_3')
inp_jmb_4 = sg.Input('', size = (30,None), visible = True, font = font_jmb_1, key = 'INP_JMB_4')
btn_jmb_2 = sg.Button('Guess', font = font_jmb_1, visible = True, key = 'BTN_JMB_2')
layout_fr_jmb_2 = [[txt_jmb_4], [txt_jmb_5], [inp_jmb_3], [txt_jmb_6], [inp_jmb_4], [btn_jmb_2]]
frm_jmb_2 = sg.Frame('', layout_fr_jmb_2, visible = False, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM_JMB_2')

################ Question 3 ###################################
txt_jmb_7 = sg.Text('These ones even the noble knights of Aeluminar cannot figure out! Ha Ha Ha! \n\n',font = font_jmb_1, visible = True, background_color = '#4B3619')
txt_jmb_8 = sg.Text(f'{shuffled_word_5}', font = font_jmb_1, visible = True, background_color = '#4B3619') 
txt_jmb_9 = sg.Text(f'\n\n{shuffled_word_6}', font = font_jmb_1, visible = True, background_color = '#4B3619')
inp_jmb_5 = sg.Input('', size = (30,None), visible = True, font = font_jmb_1, key = 'INP_JMB_5')
inp_jmb_6 = sg.Input('', size = (30,None), visible = True, font = font_jmb_1, key = 'INP_JMB_6')
btn_jmb_3 = sg.Button('Guess', font = font_jmb_1, visible = True, key = 'BTN_JMB_3')
layout_fr_jmb_3 = [[txt_jmb_7], [txt_jmb_8], [inp_jmb_5], [txt_jmb_9], [inp_jmb_6], [btn_jmb_3]]
frm_jmb_3 = sg.Frame('', layout_fr_jmb_3, visible = False, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM_JMB_3')

############### Question 4 ####################################
txt_jmb_10 = sg.Text("Not even magic can solve these words! \n\n", font = font_jmb_1, visible = True, background_color = '#4B3619')
txt_jmb_11 = sg.Text(f'{shuffled_word_7}', font = font_jmb_1, visible = True, background_color = '#4B3619') 
txt_jmb_12 = sg.Text(f'\n\n{shuffled_word_8}', font = font_jmb_1, visible = True, background_color = '#4B3619')
inp_jmb_7 = sg.Input('', size = (30,None), visible = True, font = font_jmb_1, key = 'INP_JMB_7')
inp_jmb_8 = sg.Input('', size = (30,None), visible = True, font = font_jmb_1, key = 'INP_JMB_8')
btn_jmb_4 = sg.Button('Guess', font = font_jmb_1, visible = True, key = 'BTN_JMB_4')
layout_fr_jmb_4 = [[txt_jmb_10], [txt_jmb_11], [inp_jmb_7], [txt_jmb_12], [inp_jmb_8], [btn_jmb_4]]
frm_jmb_4 = sg.Frame('', layout_fr_jmb_4, visible = False, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM_JMB_4')

############### End Frame ########################################
txt_jmb_end = sg.Text('', font = font_jmb_1, visible = True, background_color = '#4B3619')
btn_jmb_end = sg.Button('Continue', font = font_jmb_1, visible = True, key = 'BTN_END')
layout_fr_jmb_end = [[txt_jmb_end], [btn_jmb_end]]
frm_end = sg.Frame('', layout_fr_jmb_end, visible = False, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM_END')

#Creating a pointing system
list_jmb_points = []

layout = [[img_jmb_1], [frm_jmb_1, frm_jmb_2, frm_jmb_3, frm_jmb_4, frm_end]]

window = sg.Window('', layout, element_justification='c', background_color = '#4B3619').Finalize()
window.Maximize()

while True:
    event, values = window.read()
    if event == 'BTN_JMB_1':
#Checking the woed
        guess_1 = str(values['INP_JMB_1'])
        guess_2 = str(values['INP_JMB_2'])
        if guess_1 == random_word_1 and guess_2 == random_word_2:
            list_jmb_points.append(1)
            list_jmb_points.append(1)
            sg.popup('You guessed both words!', text_color='black', background_color = '#cba331', font = font_jmb_1) 
        elif guess_1 == random_word_1:
            list_jmb_points.append(1)
            sg.popup(f'You guessed one word. The other one was {random_word_2}!', text_color='black', background_color = '#cba331', font = font_jmb_1)
        elif guess_2 == random_word_2:
            list_jmb_points.append(1)
            sg.popup(f'You guessed one word. The other one was {random_word_1}!', text_color='black', background_color = '#cba331', font = font_jmb_1)
        else:
            sg.popup(f'You did not guess any words. They were {random_word_1} and {random_word_2}!', text_color='black', background_color = '#cba331', font = font_jmb_1)

#Changing the question  
        window['FRM_JMB_1'].update(visible = False)
        window['FRM_JMB_2'].update(visible = True)
    
    elif event == 'BTN_JMB_2':
        guess_3 = str(values['INP_JMB_3'])
        guess_4 = str(values['INP_JMB_4'])
        if guess_3 == random_word_3 and guess_4 == random_word_4:
            list_jmb_points.append(1)
            list_jmb_points.append(1)
            sg.popup('You guessed both words!', text_color='black', background_color = '#cba331', font = font_jmb_1) 
        elif guess_3 == random_word_3:
            list_jmb_points.append(1)
            sg.popup(f'You guessed one word. The other one was {random_word_4}!', text_color='black', background_color = '#cba331', font = font_jmb_1)
        elif guess_4 == random_word_4:
            list_jmb_points.append(1)
            sg.popup(f'You guessed one word. The other one was {random_word_3}!', text_color='black', background_color = '#cba331', font = font_jmb_1)
        else:
            sg.popup(f'You did not guess any words. They were {random_word_3} and {random_word_4}!', text_color='black', background_color = '#cba331', font = font_jmb_1)
            
        window['FRM_JMB_2'].update(visible = False)
        window['FRM_JMB_3'].update(visible = True)
    
    elif event == 'BTN_JMB_3':
        guess_5 = str(values['INP_JMB_5'])
        guess_6 = str(values['INP_JMB_6'])
        if guess_5 == random_word_5 and guess_6 == random_word_6:
            list_jmb_points.append(1)
            list_jmb_points.append(1)
            sg.popup('You guessed both words!', text_color='black', background_color = '#cba331', font = font_jmb_1) 
        elif guess_5 == random_word_5:
            list_jmb_points.append(1)
            sg.popup(f'You guessed one word. The other one was {random_word_6}!', text_color='black', background_color = '#cba331', font = font_jmb_1)
        elif guess_6 == random_word_6:
            list_jmb_points.append(1)
            sg.popup(f'You guessed one word. The other one was {random_word_5}!', text_color='black', background_color = '#cba331', font = font_jmb_1)
        else:
            sg.popup(f'You did not guess any words. They were {random_word_5} and {random_word_6}!', text_color='black', background_color = '#cba331', font = font_jmb_1)
            
        window['FRM_JMB_3'].update(visible = False)
        window['FRM_JMB_4'].update(visible = True)
        
    elif event == 'BTN_JMB_4':
        guess_7 = str(values['INP_JMB_7'])
        guess_8 = str(values['INP_JMB_8'])
        if guess_7 == random_word_7 and guess_8 == random_word_8:
            list_jmb_points.append(1)
            list_jmb_points.append(1)
            math_1_points = int(sum(list_jmb_points)/1)
            sg.popup('You guessed both words!', text_color='black', background_color = '#cba331', font = font_jmb_1)

# If statement to calculate the points
            if math_1_points >= 5:
                window['FRM_JMB_4'].update(visible = False)
                txt_jmb_end.update(f'\n\nCongratulations, you have passed this challenge with {math_1_points} correct guesses')
                window['FRM_END'].update(visible = True)
            else:
                window['FRM_JMB_4'].update(visible = False)
                txt_jmb_end.update(f'\n\nYou did not pass this challenge. You guessed only {math_1_points} words')
                window['FRM_END'].update(visible = True)
       
        elif guess_7 == random_word_7:
            list_jmb_points.append(1)
            math_1_points = int(sum(list_jmb_points)/1)
            sg.popup(f'You guessed one word. The other one was {random_word_8}!', text_color='black', background_color = '#cba331', font = font_jmb_1)

# If statement to calculate the points
            if math_1_points >= 5:
                window['FRM_JMB_4'].update(visible = False)
                txt_jmb_end.update(f'\n\nCongratulations, you have passed this challenge with {math_1_points} correct guesses')
                window['FRM_END'].update(visible = True)
            else:
                window['FRM_JMB_4'].update(visible = False)
                txt_jmb_end.update(f'\n\nYou did not pass this challenge. You guessed only {math_1_points} words')
                window['FRM_END'].update(visible = True)
                
# If statement to calculate the points     
        elif guess_8 == random_word_8:
            list_jmb_points.append(1)
            math_1_points = int(sum(list_jmb_points)/1)
            sg.popup(f'You guessed one word. The other one was {random_word_7}!', text_color='black', background_color = '#cba331', font = font_jmb_1)
            if math_1_points >= 5:
                window['FRM_JMB_4'].update(visible = False)
                txt_jmb_end.update(f'\n\nCongratulations, you have passed this challenge with {math_1_points} correct guesses')
                window['FRM_END'].update(visible = True)
            else:
                window['FRM_JMB_4'].update(visible = False)
                txt_jmb_end.update(f'\n\nYou did not pass this challenge. You guessed only {math_1_points} words')
                window['FRM_END'].update(visible = True)

# If statement to calculate the points
        else:
            math_1_points = int(sum(list_jmb_points)/1)
            sg.popup(f'You did not guess any words. They were {random_word_7} and {random_word_8}!', text_color='black', background_color = '#cba331', font = font_jmb_1)
            if math_1_points >= 5:
                window['FRM_JMB_4'].update(visible = False)
                txt_jmb_end.update(f'\n\nCongratulations, you have passed this challenge with {math_1_points} correct guesses')
                window['FRM_END'].update(visible = True)
            else:
                window['FRM_JMB_4'].update(visible = False)
                txt_jmb_end.update(f'\n\nYou did not pass this challenge. You guessed only {math_1_points} words')
                window['FRM_END'].update(visible = True)        
           
    elif event == sg.WIN_CLOSED or event == 'BTN_END':
        break    
        
window.close()

