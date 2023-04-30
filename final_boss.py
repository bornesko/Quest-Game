import PySimpleGUI as sg
from choice import btn01_pressed
from choice import btn02_pressed
from choice import btn03_pressed
from choice import btn04_pressed
from choice import btn05_pressed
from choice import btn06_pressed
from choice import btn07_pressed
from choice import btn08_pressed
from choice import btn09_pressed
from choice import btn10_pressed

'''
Basilisk - 1
Mushroom - 83
Cerberus - 3
Spider - 26
Werewolf - 48
Fairy - 99
Floating Eye - 56
Vampire - 19
Goblin - 73
Ogre - 35
'''

img01 = sg.Image ('TestImage.png')
img02 = sg.Image ('arrow.png')
img03 = sg.Image ('arrow.png')
img04 = sg.Image ('arrow.png')
font01 = ('MS Serif', 12)

################ Frame -1 ##############################
txt001 = sg.Text('''
“I hope you are content in your choice, now go and fulfill your destiny.” As I look down on the arrows in my hand, I feel a surge of power. Determined I turn away
from the golem and make my way down the crater. Walking down it the last of the moonlight extinguishes behind me, unsure of where I am heading I run my hand down
the side of the cave wall in order to orientate myself. Walking down I am surrounded by nothing, alone with only my thoughts. After walking only 10 minutes, I see
a faint glint of yellow light in front of me. Calming my breath I continue walking straight forward, as I approach the light it grows brighter and brighter. Finally
being able to see my surroundings, I see the entrance to a big cavern. As I approach it and turn to see what is inside, I eyes fall upon Drakara.
''', font = font01, background_color = '#4B3619')
btn001 = sg.Button ('Enter', font = font01, key = 'BTN001')

layout_frm_01 = [[txt001], [btn001]]
frm001 = sg.Frame('', layout_frm_01, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM001')
#############################################################

################# Frame 0 ###############################
txt002 = sg.Text('''
Its grotesque shape is unlike anything I could ever imagine, far beyond the size and presence of any creature I encountered in that forest. Its flesh bound by great pillars
of iron, its eyes open to welcome me to my doom. On the other side of it, I see a smaller cave filled to the brim with the most precious jewels and gemstones I had ever seen.
The behemoth rises slowly and lets out a roar that shakes the walls of the cave. “Insert incomprehensible text” I think it is trying to communicate with me however, its language
is too old for me to understand. Its eyes filled with malice it lets out a blast of purple fire, in the mere moments I have to react I jump behind a bolder nearby. The fire
blasts all around me and its residual heat is enough to singe my exposed skin. This creature is different without any trial or game it attacks me, remembering the arrows and bow
on my back I stand up and get ready for my final stand.
''', font = font01, background_color = '#4B3619')
btn002 = sg.Button ('ATTACK!', font = font01, key = 'BTN002')

layout_frm_02 = [[txt002], [btn002]]
frm002 = sg.Frame('', layout_frm_02, visible = False, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM002')
##########################################################

################ Frame 1 ##############################
txt01 = sg.Text('''
I grab my first arrow and nock it to the bow. Remembering the words of the golem, I pull the arrow back and concentrate.
I see a range of numbers in my head, but which value to choose. I aim the arrow at the dragon!\n\n
''',font = font01, background_color = '#4B3619')
sld01 = sg.Slider(range = (1,100), background_color = '#4B3619', key = 'SLD01')
txt02 = sg.Text ('', font = font01, background_color = '#4B3619')
btn01 = sg.Button ('FIRE',size = (12,3), font = font01, key = 'BTN01')
txt_empty_1 = sg.Text ('\n', background_color = '#4B3619')

layout_frm_1 = [[txt01], [txt02, sld01, img02], [txt_empty_1], [btn01]]
frm01 = sg.Frame('', layout_frm_1, visible = False, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM01')
#######################################################

################ Frame 2 ##############################
txt03 = sg.Text('''
The dragon lets out another volley of flames, I make my escape diving behind another bolder. The heat burns me again, “I can’t take many more of these.”
I grab the second arrow and fix it to my bow. As the heat around me dies down I stand up again, breathing in and aiming it straight for the monster. \n\n
''',font = font01, background_color = '#4B3619')
sld02 = sg.Slider(range = (1,100), background_color = '#4B3619', key = 'SLD02')
txt04 = sg.Text ('', font = font01, background_color = '#4B3619')
btn02 = sg.Button ('FIRE',size = (12,3), font = font01, key = 'BTN02')
txt_empty_2 = sg.Text ('\n', background_color = '#4B3619')

layout_frm_2 = [[txt03], [txt04, sld02, img03], [txt_empty_2], [btn02]]
frm02 = sg.Frame('', layout_frm_2, visible = False, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM02')
#######################################################

################ Frame 3 ##############################
txt05 = sg.Text('''
Enraged the beast lets out its strongest flames yet, narrowly taking cover the flames burn at my skin blistering it a searing my flesh. I shout out as the pain
takes a hold of my body. The last arrow now in my hands I stand up, my arms shake and keeping the bow still is nearly impossible. One last time I visualize the
numbers, aiming the arrow straight ahead.\n\n
''',font = font01, background_color = '#4B3619')
sld03 = sg.Slider(range = (1,100), background_color = '#4B3619', key = 'SLD03')
txt06 = sg.Text ('', font = font01, background_color = '#4B3619')
btn03 = sg.Button ('FIRE',size = (12,3), font = font01, key = 'BTN03')
txt_empty_3 = sg.Text ('\n', background_color = '#4B3619')

layout_frm_3 = [[txt05], [txt06, sld03, img04], [txt_empty_3], [btn03]]
frm03 = sg.Frame('', layout_frm_3, visible = False, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM03')
#######################################################

############### Frame 4 #############################
txt07 = sg.Text('', font = ('MS Serif', 15), background_color = '#4B3619')
btn_ex = sg.Button ('Continue', font = font01, key = 'BTN_EX')


layout_frm_4 = [[txt07], [btn_ex]]
frm04 = sg.Frame('', layout_frm_4, visible = False, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM04')
##########################################################

points_final = []


layout = [[img01],[frm001, frm002, frm01, frm02, frm03, frm04]]

window = sg.Window('', layout, element_justification='c', background_color = '#4B3619').Finalize()
window.Maximize()

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'BTN_EX':
        break
    
    elif event == 'BTN001':
        window['FRM001'].update(visible = False)
        window['FRM002'].update(visible = True)
    
    elif event == 'BTN002':
        if btn01_pressed == True:
            window['FRM002'].update(visible = False)
            txt02.update('Cerberus')
            window['FRM01'].update(visible = True)
        elif btn02_pressed == True:
            window['FRM002'].update(visible = False)
            txt02.update('Werewolf')
            window['FRM01'].update(visible = True)
        elif btn03_pressed == True:
            window['FRM002'].update(visible = False)
            txt02.update('Goblin')
            window['FRM01'].update(visible = True)
        elif btn04_pressed == True:
            window['FRM002'].update(visible = False)
            txt02.update('Spider')
            window['FRM01'].update(visible = True)
        elif btn05_pressed == True:
            window['FRM002'].update(visible = False)
            txt02.update('Mushroom')
            window['FRM01'].update(visible = True)
        elif btn06_pressed == True:
            window['FRM002'].update(visible = False)
            txt02.update('Fairy')
            window['FRM01'].update(visible = True)
        elif btn07_pressed == True:
            window['FRM002'].update(visible = False)
            txt02.update('Ogre')
            window['FRM01'].update(visible = True)
        elif btn08_pressed == True:
            window['FRM002'].update(visible = False)
            txt02.update('Floating Eye')
            window['FRM01'].update(visible = True)    

#1st Option ##############################3
    elif btn01_pressed == True:
        if event == 'BTN01':
            btn01_pressed = False
            guess_1 = int(values['SLD01'])
            if guess_1 == 3:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM01'].update(visible = False)
                window['FRM02'].update(visible = True)
                points_final.append(1)
                if btn02_pressed == True:
                    txt04.update('Werewolf')
                elif btn03_pressed == True:
                    txt04.update('Goblin')
                elif btn04_pressed == True:
                    txt04.update('Spider')
                elif btn05_pressed == True:
                    txt04.update('Mushroom')
                elif btn06_pressed == True:
                    txt04.update('Fairy')
                elif btn07_pressed == True:
                    txt04.update('Ogre')
                elif btn08_pressed == True:
                    txt04.update('Floating Eye')
                elif btn09_pressed == True:
                    txt04.update('Basilisk')
                elif btn10_pressed == True:
                    txt04.update('Vampire')    
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM01'].update(visible = False)
                window['FRM02'].update(visible = True)
                if btn02_pressed == True:
                    txt04.update('Werewolf')
                elif btn03_pressed == True:
                    txt04.update('Goblin')
                elif btn04_pressed == True:
                    txt04.update('Spider')
                elif btn05_pressed == True:
                    txt04.update('Mushroom')
                elif btn06_pressed == True:
                    txt04.update('Fairy')
                elif btn07_pressed == True:
                    txt04.update('Ogre')
                elif btn08_pressed == True:
                    txt04.update('Floating Eye')
                elif btn09_pressed == True:
                    txt04.update('Basilisk')
                elif btn10_pressed == True:
                    txt04.update('Vampire')
######################################################
######## 2nd Option ##################################                   
    elif btn02_pressed == True:
        if event == 'BTN01':
            btn02_pressed = False
            guess_1 = int(values['SLD01'])
            if guess_1 == 48:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM01'].update(visible = False)
                window['FRM02'].update(visible = True)
                points_final.append(1)
                if btn03_pressed == True:
                    txt04.update('Goblin')
                elif btn04_pressed == True:
                    txt04.update('Spider')
                elif btn05_pressed == True:
                    txt04.update('Mushroom')
                elif btn06_pressed == True:
                    txt04.update('Fairy')
                elif btn07_pressed == True:
                    txt04.update('Ogre')
                elif btn08_pressed == True:
                    txt04.update('Floating Eye')
                elif btn09_pressed == True:
                    txt04.update('Basilisk')
                elif btn10_pressed == True:
                    txt04.update('Vampire')
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM01'].update(visible = False)
                window['FRM02'].update(visible = True)
                if btn03_pressed == True:
                    txt04.update('Goblin')
                elif btn04_pressed == True:
                    txt04.update('Spider')
                elif btn05_pressed == True:
                    txt04.update('Mushroom')
                elif btn06_pressed == True:
                    txt04.update('Fairy')
                elif btn07_pressed == True:
                    txt04.update('Ogre')
                elif btn08_pressed == True:
                    txt04.update('Floating Eye')
                elif btn09_pressed == True:
                    txt04.update('Basilisk')
                elif btn10_pressed == True:
                    txt04.update('Vampire')
        
        elif event == 'BTN02':
            btn02_pressed = False
            guess_1 = int(values['SLD02'])
            if guess_1 == 48:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM02'].update(visible = False)
                window['FRM03'].update(visible = True)
                points_final.append(1)
                if btn03_pressed == True:
                    txt06.update('Goblin')
                elif btn04_pressed == True:
                    txt06.update('Spider')
                elif btn05_pressed == True:
                    txt06.update('Mushroom')
                elif btn06_pressed == True:
                    txt06.update('Fairy')
                elif btn07_pressed == True:
                    txt06.update('Ogre')
                elif btn08_pressed == True:
                    txt06.update('Floating Eye')
                elif btn09_pressed == True:
                    txt06.update('Basilisk')
                elif btn10_pressed == True:
                    txt06.update('Vampire')    
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM02'].update(visible = False)
                window['FRM03'].update(visible = True)
                if btn03_pressed == True:
                    txt06.update('Goblin')
                elif btn04_pressed == True:
                    txt06.update('Spider')
                elif btn05_pressed == True:
                    txt06.update('Mushroom')
                elif btn06_pressed == True:
                    txt06.update('Fairy')
                elif btn07_pressed == True:
                    txt06.update('Ogre')
                elif btn08_pressed == True:
                    txt06.update('Floating Eye')
                elif btn09_pressed == True:
                    txt06.update('Basilisk')
                elif btn10_pressed == True:
                    txt06.update('Vampire')

###############################################################
######## 3rd Option ############
                    
    elif btn03_pressed == True:
        if event == 'BTN01':
            btn03_pressed = False
            guess_1 = int(values['SLD01'])
            if guess_1 == 73:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM01'].update(visible = False)
                window['FRM02'].update(visible = True)
                points_final.append(1)
                if btn04_pressed == True:
                    txt04.update('Spider')
                elif btn05_pressed == True:
                    txt04.update('Mushroom')
                elif btn06_pressed == True:
                    txt04.update('Fairy')
                elif btn07_pressed == True:
                    txt04.update('Ogre')
                elif btn08_pressed == True:
                    txt04.update('Floating Eye')
                elif btn09_pressed == True:
                    txt04.update('Basilisk')
                elif btn10_pressed == True:
                    txt04.update('Vampire')    
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM01'].update(visible = False)
                window['FRM02'].update(visible = True)
                if btn04_pressed == True:
                    txt04.update('Spider')
                elif btn05_pressed == True:
                    txt04.update('Mushroom')
                elif btn06_pressed == True:
                    txt04.update('Fairy')
                elif btn07_pressed == True:
                    txt04.update('Ogre')
                elif btn08_pressed == True:
                    txt04.update('Floating Eye')
                elif btn09_pressed == True:
                    txt04.update('Basilisk')
                elif btn10_pressed == True:
                    txt04.update('Vampire')
        
        elif event == 'BTN02':
            btn03_pressed = False
            guess_1 = int(values['SLD02'])
            if guess_1 == 73:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM02'].update(visible = False)
                window['FRM03'].update(visible = True)
                points_final.append(1)
                if btn04_pressed == True:
                    txt06.update('Spider')
                elif btn05_pressed == True:
                    txt06.update('Mushroom')
                elif btn06_pressed == True:
                    txt06.update('Fairy')
                elif btn07_pressed == True:
                    txt06.update('Ogre')
                elif btn08_pressed == True:
                    txt06.update('Floating Eye')
                elif btn09_pressed == True:
                    txt06.update('Basilisk')
                elif btn10_pressed == True:
                    txt06.update('Vampire')    
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM02'].update(visible = False)
                window['FRM03'].update(visible = True)
                if btn04_pressed == True:
                    txt06.update('Spider')
                elif btn05_pressed == True:
                    txt06.update('Mushroom')
                elif btn06_pressed == True:
                    txt06.update('Fairy')
                elif btn07_pressed == True:
                    txt06.update('Ogre')
                elif btn08_pressed == True:
                    txt06.update('Floating Eye')
                elif btn09_pressed == True:
                    txt06.update('Basilisk')
                elif btn10_pressed == True:
                    txt06.update('Vampire')
        
        elif event == 'BTN03':
            btn03_pressed = False
            guess_1 = int(values['SLD03'])
            if guess_1 == 73:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                points_final.append(1)
                points_boss = int(sum(points_final)/1)
                window['FRM03'].update(visible=False)
                txt07.update(f'You have {points_boss} accurate shots!')
                window['FRM04'].update(visible=True)
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                points_boss = int(sum(points_final)/1)
                window['FRM03'].update(visible=False)
                txt07.update(f'You have {points_boss} accurate shots!')
                window['FRM04'].update(visible=True)
############################################################
############ 4th Option ###################
        
    elif btn04_pressed == True:
        if event == 'BTN01':
            btn04_pressed = False
            guess_1 = int(values['SLD01'])
            if guess_1 == 26:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM01'].update(visible = False)
                window['FRM02'].update(visible = True)
                points_final.append(1)
                if btn05_pressed == True:
                    txt04.update('Mushroom')
                elif btn06_pressed == True:
                    txt04.update('Fairy')
                elif btn07_pressed == True:
                    txt04.update('Ogre')
                elif btn08_pressed == True:
                    txt04.update('Floating Eye')
                elif btn09_pressed == True:
                    txt04.update('Basilisk')
                elif btn10_pressed == True:
                    txt04.update('Vampire')    
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM01'].update(visible = False)
                window['FRM02'].update(visible = True)
                if btn05_pressed == True:
                    txt04.update('Mushroom')
                elif btn06_pressed == True:
                    txt04.update('Fairy')
                elif btn07_pressed == True:
                    txt04.update('Ogre')
                elif btn08_pressed == True:
                    txt04.update('Floating Eye')
                elif btn09_pressed == True:
                    txt04.update('Basilisk')
                elif btn10_pressed == True:
                    txt04.update('Vampire')
        
        elif event == 'BTN02':
            btn04_pressed = False
            guess_1 = int(values['SLD02'])
            if guess_1 == 26:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM02'].update(visible = False)
                window['FRM03'].update(visible = True)
                points_final.append(1)
                if btn05_pressed == True:
                    txt06.update('Mushroom')
                elif btn06_pressed == True:
                    txt06.update('Fairy')
                elif btn07_pressed == True:
                    txt06.update('Ogre')
                elif btn08_pressed == True:
                    txt06.update('Floating Eye')
                elif btn09_pressed == True:
                    txt06.update('Basilisk')
                elif btn10_pressed == True:
                    txt06.update('Vampire')    
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM02'].update(visible = False)
                window['FRM03'].update(visible = True)
                if btn05_pressed == True:
                    txt06.update('Mushroom')
                elif btn06_pressed == True:
                    txt06.update('Fairy')
                elif btn07_pressed == True:
                    txt06.update('Ogre')
                elif btn08_pressed == True:
                    txt06.update('Floating Eye')
                elif btn09_pressed == True:
                    txt06.update('Basilisk')
                elif btn10_pressed == True:
                    txt06.update('Vampire')
        
        elif event == 'BTN03':
            btn04_pressed = False
            guess_1 = int(values['SLD03'])
            if guess_1 == 26:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                points_final.append(1)
                points_boss = int(sum(points_final)/1)
                window['FRM03'].update(visible=False)
                txt07.update(f'You have {points_boss} accurate shots!')
                window['FRM04'].update(visible=True)
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                points_boss = int(sum(points_final)/1)
                window['FRM03'].update(visible=False)
                txt07.update(f'You have {points_boss} accurate shots!')
                window['FRM04'].update(visible=True)
#############################################################
########### 5th Option ###################################
        
    elif btn05_pressed == True:
        if event == 'BTN01':
            btn05_pressed = False
            guess_1 = int(values['SLD01'])
            if guess_1 == 83:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM01'].update(visible = False)
                window['FRM02'].update(visible = True)
                points_final.append(1)
                if btn06_pressed == True:
                    txt04.update('Fairy')
                elif btn07_pressed == True:
                    txt04.update('Ogre')
                elif btn08_pressed == True:
                    txt04.update('Floating Eye')
                elif btn09_pressed == True:
                    txt04.update('Basilisk')
                elif btn10_pressed == True:
                    txt04.update('Vampire')    
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM01'].update(visible = False)
                window['FRM02'].update(visible = True)
                if btn06_pressed == True:
                    txt04.update('Fairy')
                elif btn07_pressed == True:
                    txt04.update('Ogre')
                elif btn08_pressed == True:
                    txt04.update('Floating Eye')
                elif btn09_pressed == True:
                    txt04.update('Basilisk')
                elif btn10_pressed == True:
                    txt04.update('Vampire')
                    
        elif event == 'BTN02':
            btn05_pressed = False
            guess_1 = int(values['SLD02'])
            if guess_1 == 83:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM02'].update(visible = False)
                window['FRM03'].update(visible = True)
                points_final.append(1)
                if btn06_pressed == True:
                    txt06.update('Fairy')
                elif btn07_pressed == True:
                    txt06.update('Ogre')
                elif btn08_pressed == True:
                    txt06.update('Floating Eye')
                elif btn09_pressed == True:
                    txt06.update('Basilisk')
                elif btn10_pressed == True:
                    txt06.update('Vampire')    
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM02'].update(visible = False)
                window['FRM03'].update(visible = True)
                if btn06_pressed == True:
                    txt06.update('Fairy')
                elif btn07_pressed == True:
                    txt06.update('Ogre')
                elif btn08_pressed == True:
                    txt06.update('Floating Eye')
                elif btn09_pressed == True:
                    txt06.update('Basilisk')
                elif btn10_pressed == True:
                    txt06.update('Vampire')
        
        elif event == 'BTN03':
            btn05_pressed = False
            guess_1 = int(values['SLD03'])
            if guess_1 == 83:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                points_final.append(1)
                points_boss = int(sum(points_final)/1)
                window['FRM03'].update(visible=False)
                txt07.update(f'You have {points_boss} accurate shots!')
                window['FRM04'].update(visible=True)
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                points_boss = int(sum(points_final)/1)
                window['FRM03'].update(visible=False)
                txt07.update(f'You have {points_boss} accurate shots!')
                window['FRM04'].update(visible=True)
######################################################################
################### 6th Option #####################
        
    elif btn06_pressed == True:
        if event == 'BTN01':
            btn06_pressed = False
            guess_1 = int(values['SLD01'])
            if guess_1 == 99:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM01'].update(visible = False)
                window['FRM02'].update(visible = True)
                points_final.append(1)
                if btn07_pressed == True:
                    txt04.update('Ogre')
                elif btn08_pressed == True:
                    txt04.update('Floating Eye')
                elif btn09_pressed == True:
                    txt04.update('Basilisk')
                elif btn10_pressed == True:
                    txt04.update('Vampire')    
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM01'].update(visible = False)
                window['FRM02'].update(visible = True)
                if btn07_pressed == True:
                    txt04.update('Ogre')
                elif btn08_pressed == True:
                    txt04.update('Floating Eye')
                elif btn09_pressed == True:
                    txt04.update('Basilisk')
                elif btn10_pressed == True:
                    txt04.update('Vampire')
        
        elif event == 'BTN02':
            btn06_pressed = False
            guess_1 = int(values['SLD02'])
            if guess_1 == 99:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM02'].update(visible = False)
                window['FRM03'].update(visible = True)
                points_final.append(1)
                if btn07_pressed == True:
                    txt06.update('Ogre')
                elif btn08_pressed == True:
                    txt06.update('Floating Eye')
                elif btn09_pressed == True:
                    txt06.update('Basilisk')
                elif btn10_pressed == True:
                    txt06.update('Vampire')    
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM02'].update(visible = False)
                window['FRM03'].update(visible = True)
                if btn07_pressed == True:
                    txt06.update('Ogre')
                elif btn08_pressed == True:
                    txt06.update('Floating Eye')
                elif btn09_pressed == True:
                    txt06.update('Basilisk')
                elif btn10_pressed == True:
                    txt06.update('Vampire')
            
        elif event == 'BTN03':
            btn06_pressed = False
            guess_1 = int(values['SLD03'])
            if guess_1 == 99:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                points_final.append(1)
                points_boss = int(sum(points_final)/1)
                window['FRM03'].update(visible=False)
                txt07.update(f'You have {points_boss} accurate shots!')
                window['FRM04'].update(visible=True)
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                points_boss = int(sum(points_final)/1)
                window['FRM03'].update(visible=False)
                txt07.update(f'You have {points_boss} accurate shots!')
                window['FRM04'].update(visible=True)
#########################################################################
################### 7th Option ##########################################
    
    elif btn07_pressed == True:
        if event == 'BTN01':
            btn07_pressed = False
            guess_1 = int(values['SLD01'])
            if guess_1 == 35:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM01'].update(visible = False)
                window['FRM02'].update(visible = True)
                points_final.append(1)
                if btn08_pressed == True:
                    txt04.update('Floating Eye')
                elif btn09_pressed == True:
                    txt04.update('Basilisk')
                elif btn10_pressed == True:
                    txt04.update('Vampire')    
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM01'].update(visible = False)
                window['FRM02'].update(visible = True)
                if btn08_pressed == True:
                    txt04.update('Floating Eye')
                elif btn09_pressed == True:
                    txt04.update('Basilisk')
                elif btn10_pressed == True:
                    txt04.update('Vampire')
        
        elif event == 'BTN02':
            btn07_pressed = False
            guess_1 = int(values['SLD02'])
            if guess_1 == 35:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM02'].update(visible = False)
                window['FRM03'].update(visible = True)
                points_final.append(1)
                if btn08_pressed == True:
                    txt06.update('Floating Eye')
                elif btn09_pressed == True:
                    txt06.update('Basilisk')
                elif btn10_pressed == True:
                    txt06.update('Vampire')    
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM02'].update(visible = False)
                window['FRM03'].update(visible = True)
                if btn08_pressed == True:
                    txt06.update('Floating Eye')
                elif btn09_pressed == True:
                    txt06.update('Basilisk')
                elif btn10_pressed == True:
                    txt06.update('Vampire')
        
        elif event == 'BTN03':
            btn07_pressed = False
            guess_1 = int(values['SLD03'])
            if guess_1 == 35:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                points_final.append(1)
                points_boss = int(sum(points_final)/1)
                window['FRM03'].update(visible=False)
                txt07.update(f'You have {points_boss} accurate shots!')
                window['FRM04'].update(visible=True)
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                points_boss = int(sum(points_final)/1)
                window['FRM03'].update(visible=False)
                txt07.update(f'You have {points_boss} accurate shots!')
                window['FRM04'].update(visible=True)
##############################################################
################### 8th Option ###############################
            
    elif btn08_pressed == True:
        if event == 'BTN01':
            btn08_pressed = False
            guess_1 = int(values['SLD01'])
            if guess_1 == 56:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM01'].update(visible = False)
                window['FRM02'].update(visible = True)
                points_final.append(1)
                if btn09_pressed == True:
                    txt04.update('Basilisk')
                elif btn10_pressed == True:
                    txt04.update('Vampire')    
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM01'].update(visible = False)
                window['FRM02'].update(visible = True)
                if btn09_pressed == True:
                    txt04.update('Basilisk')
                elif btn10_pressed == True:
                    txt04.update('Vampire')
        elif event == 'BTN02':
            btn08_pressed = False
            guess_1 = int(values['SLD02'])
            if guess_1 == 56:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM02'].update(visible = False)
                window['FRM03'].update(visible = True)
                points_final.append(1)
                if btn09_pressed == True:
                    txt06.update('Basilisk')
                elif btn10_pressed == True:
                    txt06.update('Vampire')    
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM02'].update(visible = False)
                window['FRM03'].update(visible = True)
                if btn09_pressed == True:
                    txt06.update('Basilisk')
                elif btn10_pressed == True:
                    txt06.update('Vampire')
        
        elif event == 'BTN03':
            btn08_pressed = False
            guess_1 = int(values['SLD03'])
            if guess_1 == 56:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                points_final.append(1)
                points_boss = int(sum(points_final)/1)
                window['FRM03'].update(visible=False)
                txt07.update(f'You have {points_boss} accurate shots!')
                window['FRM04'].update(visible=True)
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                points_boss = int(sum(points_final)/1)
                window['FRM03'].update(visible=False)
                txt07.update(f'You have {points_boss} accurate shots!')
                window['FRM04'].update(visible=True)
#############################################################
############### 9th Option ##################################
    elif btn09_pressed == True:
        if event == 'BTN02':
            btn09_pressed = False
            guess_1 = int(values['SLD02'])
            if guess_1 == 1:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM02'].update(visible = False)
                window['FRM03'].update(visible = True)
                points_final.append(1)
                if btn10_pressed == True:
                    txt06.update('Vampire')    
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                window['FRM02'].update(visible = False)
                window['FRM03'].update(visible = True)
                if btn10_pressed == True:
                    txt06.update('Vampire')
        
        elif event == 'BTN03':
            btn09_pressed = False
            guess_1 = int(values['SLD03'])
            if guess_1 == 1:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                points_final.append(1)
                points_boss = int(sum(points_final)/1)
                window['FRM03'].update(visible=False)
                txt07.update(f'You have {points_boss} accurate shots!')
                window['FRM04'].update(visible=True)
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                points_boss = int(sum(points_final)/1)
                window['FRM03'].update(visible=False)
                txt07.update(f'You have {points_boss} accurate shots!')
                window['FRM04'].update(visible=True)
####################################################
############### 10th Frame #########################
    elif btn10_pressed == True:
       if event == 'BTN03':
            btn09_pressed = False
            guess_1 = int(values['SLD03'])
            if guess_1 == 19:
                sg.popup('You hit the arrow!', text_color='black', background_color = '#cba331', font = font01)
                points_final.append(1)
                points_boss = int(sum(points_final)/1)
                window['FRM03'].update(visible=False)
                txt07.update(f'You have {points_boss} accurate shots!')
                window['FRM04'].update(visible=True)
            else:
                sg.popup('You missed!', text_color='black', background_color = '#cba331', font = font01)
                points_boss = int(sum(points_final)/1)
                window['FRM03'].update(visible=False)
                txt07.update(f'You have {points_boss} accurate shots!')
                window['FRM04'].update(visible=True)
#######################################################

window.close()

