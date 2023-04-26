import PySimpleGUI as sg

#############Slide A3###########################################################################################################################
fontSA31 = ('MS Serif', 12) 
imgSA31 = sg.Image ('TestImage.png')

txtSA30 = sg.Text('Here is how this will go, I will ask you four questions and if you can answer three of them correctly, you win!', font = fontSA31, visible = True, background_color = '#4B3619')

#First Question
txtSA31 = sg.Text(
"""
1) What is the largest creature in the world?
""", font = fontSA31, visible = True, background_color = '#4B3619')
btnSA31 = sg.Button('A) Blue Whale', font = fontSA31, key='BTN_SA31')
btnSA32 = sg.Button('B) Elephant', font = fontSA31, key = 'BTN_SA32')
btnSA33 = sg.Button('C) Hippopotamus', font = fontSA31, key = 'BTN_SA33')
btnSA34 = sg.Button('D) Bear', font = fontSA31, key = 'BTN_SA34')
#########################################################################

#Second Question
txtSA32 = sg.Text(
"""
2) What colour are you going to get if you mix the red fruits of a Solanar and the yellow flowers of a Petalburst?
""", font = fontSA31, visible = False, background_color = '#4B3619')
btnSA35 = sg.Button('A) Blue', font = fontSA31, visible = False, key='BTN_SA35')
btnSA36 = sg.Button('B) Green', font = fontSA31, visible = False, key = 'BTN_SA36')
btnSA37 = sg.Button('C) Purple', font = fontSA31, visible = False, key = 'BTN_SA37')
btnSA38 = sg.Button('D) Orange', font = fontSA31, visible = False, key = 'BTN_SA38')
##########################################################################

#Third Question
txtSA33 = sg.Text(
"""
3) Recently the dwarves came across a new material in the Silverpeak Mines. It appears that it is the hardest
one ever to be found. What is the material?
""", font = fontSA31, visible = False, background_color = '#4B3619')
btnSA39 = sg.Button('A) Diamond', font = fontSA31, visible = False, key='BTN_SA39')
btnSA310 = sg.Button('B) Quartz', font = fontSA31, visible = False, key = 'BTN_SA310')
btnSA311 = sg.Button('C) Topaz', font = fontSA31, visible = False, key = 'BTN_SA311')
btnSA312 = sg.Button('D) Sapphire', font = fontSA31, visible = False, key = 'BTN_SA312')
##########################################################################

#Fourth Question
txtSA34 = sg.Text(
"""
4) What is the name of the king guards?
""", font = fontSA31, visible = False, background_color = '#4B3619')
btnSA313 = sg.Button('A) Iluminati', font = fontSA31, visible = False, key='BTN_SA313')
btnSA314 = sg.Button('B) Aeluminar', font = fontSA31, visible = False, key = 'BTN_SA314')
btnSA315 = sg.Button('C) Lucians', font = fontSA31, visible = False, key = 'BTN_SA315')
btnSA316 = sg.Button('D) Aeloria', font = fontSA31, visible = False, key = 'BTN_SA316')
##########################################################################

txtSA35 = sg.Text('', font = fontSA31, visible = False, background_color = '#4B3619')
txtSA36 = sg.Text('', font = fontSA31, visible = False, background_color = '#4B3619')

#Button
btnSA317 = sg.Button('Continue', font = fontSA31, visible = False, key = 'BTN_SA317')



layout_frSA3 = [[imgSA31], [txtSA30], [txtSA31, txtSA32, txtSA33, txtSA34], [btnSA31, btnSA32, btnSA35, btnSA36, btnSA39, btnSA310, btnSA313, btnSA314], [btnSA33, btnSA34, btnSA37, btnSA38, btnSA311, btnSA312, btnSA315, btnSA316], [txtSA35], [txtSA36], [btnSA317, btnSA318]]
frmSA3 = sg.Frame ('', layout_frSA3, visible = True, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRMSA3')
################################################################################################################################################

list_points = []

layout = [[frmSA3]]

window = sg.Window('', layout).Finalize()
window.Maximize()

while True:
    event, values = window.read()
    
#Question 1 Correct Path
    if event == 'BTN_SA31':
        sg.popup('You have guessed it right!', text_color='black', background_color = '#cba331', font = fontSA31)
        list_points.append(1)
        txtSA31.update(visible = False)
        btnSA31.update(visible = False)
        btnSA32.update(visible = False)
        btnSA33.update(visible = False)
        btnSA34.update(visible = False)
        txtSA32.update(visible = True)
        btnSA35.update(visible = True)
        btnSA36.update(visible = True)
        btnSA37.update(visible = True)
        btnSA38.update(visible = True)

#Question 1 Wrong Path
    elif event == 'BTN_SA32' or event == 'BTN_SA33' or event == 'BTN_SA34':
        sg.popup('Wrong!', text_color='black', background_color = '#cba331', font = fontSA31)
        txtSA31.update(visible = False)
        btnSA31.update(visible = False)
        btnSA32.update(visible = False)
        btnSA33.update(visible = False)
        btnSA34.update(visible = False)
        txtSA32.update(visible = True)
        btnSA35.update(visible = True)
        btnSA36.update(visible = True)
        btnSA37.update(visible = True)
        btnSA38.update(visible = True)

#Question 2 Correct Path
    elif event == 'BTN_SA38':
        sg.popup('You have guessed it right!', text_color='black', background_color = '#cba331', font = fontSA31)
        list_points.append(1)
        txtSA32.update(visible = False)
        btnSA35.update(visible = False)
        btnSA36.update(visible = False)
        btnSA37.update(visible = False)
        btnSA38.update(visible = False)
        txtSA33.update(visible = True)
        btnSA39.update(visible = True)
        btnSA310.update(visible = True)
        btnSA311.update(visible = True)
        btnSA312.update(visible = True)

#Question 2 Wrong Path
    elif event == 'BTN_SA35' or event == 'BTN_SA36' or event == 'BTN_SA37':
        sg.popup('Wrong!', text_color='black', background_color = '#cba331', font = fontSA31)
        txtSA32.update(visible = False)
        btnSA35.update(visible = False)
        btnSA36.update(visible = False)
        btnSA37.update(visible = False)
        btnSA38.update(visible = False)
        txtSA33.update(visible = True)
        btnSA39.update(visible = True)
        btnSA310.update(visible = True)
        btnSA311.update(visible = True)
        btnSA312.update(visible = True)

#Question 3 Correct Path
    elif event == 'BTN_SA39':
        sg.popup('You have guessed it right!', text_color='black', background_color = '#cba331', font = fontSA31)
        list_points.append(1)
        txtSA33.update(visible = False)
        btnSA39.update(visible = False)
        btnSA310.update(visible = False)
        btnSA311.update(visible = False)
        btnSA312.update(visible = False)
        txtSA34.update(visible = True)
        btnSA313.update(visible = True)
        btnSA314.update(visible = True)
        btnSA315.update(visible = True)
        btnSA316.update(visible = True)
        
#Question 3 Wrong Path
    elif event == 'BTN_SA310' or event == 'BTN_SA311' or event == 'BTN_SA312':
        sg.popup('Wrong!', text_color='black', background_color = '#cba331', font = fontSA31)
        txtSA33.update(visible = False)
        btnSA39.update(visible = False)
        btnSA310.update(visible = False)
        btnSA311.update(visible = False)
        btnSA312.update(visible = False)
        txtSA34.update(visible = True)
        btnSA313.update(visible = True)
        btnSA314.update(visible = True)
        btnSA315.update(visible = True)
        btnSA316.update(visible = True)

#Question 4 Correct Path
    elif event == 'BTN_SA314':
        sg.popup('You have guessed it right!', text_color='black', background_color = '#cba331', font = fontSA31)
        list_points.append(1)
        points = int(sum(list_points)/1)
        txtSA30.update(visible = False)
        txtSA34.update(visible = False)
        btnSA313.update(visible = False)
        btnSA314.update(visible = False)
        btnSA315.update(visible = False)
        btnSA316.update(visible = False)
        txtSA35.update(f'You have guessed {points} questions out of 4', visible = True)
        
        if points < 3:
            txtSA36.update('You Lose!', visible = True)
            btnSA317.update(visible = True)
        elif points >= 3:
            txtSA36.update('You Win!', visible = True)
            btnSA317.update(visible = True)
        
#Question 4 Wrong Path
    elif event == 'BTN_SA313' or event == 'BTN_SA315' or event == 'BTN_SA316':
        sg.popup('Wrong!', text_color='black', background_color = '#cba331', font = fontSA31)
        points = int(sum(list_points)/1)
        txtSA35.update(f'Nice the points you have are {points}', visible = True)
        txtSA30.update(visible = False)
        txtSA34.update(visible = False)
        btnSA313.update(visible = False)
        btnSA314.update(visible = False)
        btnSA315.update(visible = False)
        btnSA316.update(visible = False)
        txtSA35.update(f'You have guessed {points} questions out of 4', visible = True)
        
        if points < 3:
            txtSA36.update('You Lose!', visible = True)
            btnSA317.update(visible = True)
        elif points >= 3:
            txtSA36.update('You Win!', visible = True)
            btnSA317.update(visible = True)
            
    #Cambia este if por elif.
    elif event == sg.WIN_CLOSED or event == 'BTN_SA317':
        break    
        
window.close()


