import PySimpleGUI as sg
import random
######Slide0################################################################################################################
imgS01=sg.Image('TestImage.png')
fontS01 = ("MS Serif", 12)
fontS02= ("MS Serif", 35)
txtS01= sg.Text('Welcome to ####', font=fontS02, background_color= '#4B3619')
txtS02= sg.Text('Please enter your name!', font=fontS01, background_color= '#4B3619')
inpS01= sg.Input('',size= (30,None), key = 'INP_S01')
btnS01= sg.Button('Continue',font=fontS01, key = 'BTN_S01')
layout_frS0= [[imgS01],[txtS01], [txtS02,inpS01], [btnS01]]
frmS0= sg.Frame('', layout_frS0,font=fontS01,  element_justification='c', size=(1920,1080), background_color = '#4B3619', key= 'FRMS0')
############################################################################################################################

#############SLIDE 1###########################################################################################################################
imgS11= sg.Image('TestImage.png')
fontS11 = ('MS Serif', 15) 
txtS11 = sg.Text(
"""
It’s the year 3182 AE , Eldrid stands atop all in the world of Aetheria. However, the awakening of a dark force in the forest of Hadesvale
has ravaged the fertile land with the help of its dark spawn. The inhabitants of Eldrid fear for their lives and the countryside is no longer
under the protection of the Aeluminar, the king’s guard. State-issued sorcerers battle the creatures, but all seems hopeless as their numbers
seem to multiply with each passing day. Desperate the king declares wealth fame power and everything the world has to offer to whomever can
free his land of this curse. Invigorated, countless young men and women depart from their homes in search of glory.
\nOur story starts here in a Tavern not far off from the accursed woods…
""", background_color = '#4B3619', font = fontS11)
btnS11 = sg.Button('OFF TO AN ADVENTURE!', key='BTN_S11', font = fontS11)

layout_frS1 = [[imgS11],[txtS11], [btnS11]]
frmS1 = sg.Frame ('', layout_frS1, size=(1920,1080), background_color = '#4B3619', element_justification = 'c', key = 'FRMS1')
################################################################################################################################################

######Slide2################################################################################################################
imgS21= sg.Image('TestImage.png')
fontS21 = ("MS Serif", 12)
fontS22= ("MS Serif", 35)
txtS21= sg.Text('“Can I get you something, young traveler”? asks Sheamus the Bartender. On the opposite side of the bar sits a young boy dressed in plain farmers’ clothes and a bright smile on his face.', background_color = '#4B3619',font=fontS21)
btnS21= sg.Button('I don’t have so much gold on me, but I was wondering if you knew the easiest way to the Hadesvale woods', font=fontS21, key = 'BTN_S21')
btnS22= sg.Button('I am just a boy passing by looking for adventure', font=fontS21, key = 'BTN_S22')
txtS22= sg.Text(
    '''
“I don’t know why so many of you youngsters which to go to that retched place nowadays, but it’s just down the road.
I’ll get you a drink on the house young one, and we can talk about everything else later”. The bartender waddles off behind the bar'
''', font=fontS21, background_color = '#4B3619', visible= False)
txtS23= sg.Text(
    '''
“Ah there’s many of you these days, I am assuming you’ll be heading to Hadesvale, well it’s just down the road.
I’ll get you a drink on the house young one, and we can talk about everything else later”. The bartender waddles off behind the bar.
''',font=fontS21,background_color = '#4B3619', visible= False )
btnS23= sg.Button('Continue', visible= False, font=fontS21, key= 'BTN_S23')

layout_frS2= [[imgS21], [txtS21], [btnS21,btnS22], [txtS22,txtS23], [btnS23]]
frmS2= sg.Frame('', layout_frS2,font=fontS21,  element_justification='c', size=(1920,1080), background_color = '#4B3619', key= 'FRMS2')
############################################################################################################################

######Slide3################################################################################################################
imgS31= sg.Image('TestImage.png')
fontS31 = ("MS Serif", 12)
fontS32= ("MS Serif", 35)
txtS31= sg.Text(
    '''Out of the corner of the room, a dark figure approaches. “Care to play a little game with me, it’s a game of luck,
but if you win I’ll give you 1000 pieces of gold.Lose however and you must take my place in the kings draft and travel to
Hadesvale by tonight! It’s a simple game choose a number between 1 and 10000 and if you guess the number I will write on this
paper you’ll win”.I smirk to myself I was going to do that anyway.''', background_color = '#4B3619',font=fontS31)
txtS32=sg.Text(f'My name is {inpS01} and I accept your offer!', background_color = '#4B3619', font=fontS31)
txtS33=sg.Text('Choose your Number wisely!', background_color = '#4B3619', font=fontS31)
inpS31= sg.Input('',size= (30,None), key = 'INP_S31')

btnS31= sg.Button('PLAY!', font=fontS31, key = 'BTN_S31')
btnS32= sg.Button('Continue', font=fontS31, visible= False, key = 'BTN_S32')
btnS33= sg.Button('Continue', font=fontS31, visible= False, key = 'BTN_S33')

random_number= random.randint(1,1)

layout_frS3= [[imgS31], [txtS31], [txtS32], [txtS33], [inpS31], [btnS31,btnS32,btnS33]]
frmS3= sg.Frame('', layout_frS3,font=fontS31,  element_justification='c', size=(1920,1080), background_color = '#4B3619', key= 'FRMS3')
############################################################################################################################

#############SLIDE 4###########################################################################################################################
fontS41 = ('MS Serif', 12) 
imgS41 = sg.Image ('TestImage.png')
txtS41 = sg.Text(
"""
“Damn I almost had you there.” The dark figure lets out a low and maniacal laugh. “Excellent, here take this kings letter and be on your way, fool!”
He struts away leaving the tavern, as I look towards his direction the Bartender interrupts me. “Sorry for the wait lad, here is your ale, oh what do you have in your hand.
That looks like an Aeluminar summoning letter, I didn’t take you for a Knight?”. I look at the beautifully ornate letter in wonder before stuffing it into my backpack. 
""", background_color = '#4B3619', font = fontS41, visible = True)
btnS41 = sg.Button('Looks may deceive a person', font = fontS41, key='BTN_S41')
btnS42 = sg.Button('A man just gave handed it to me, but maybe it will be useful later on', font = fontS41, key = 'BTN_S42')
txtS42 = sg.Text(
"""
With those clothes you aren’t fooling anybody HAHAHA, well small knight if you plan on leaving today you might want to start heading out before nightfall!
""", background_color = '#4B3619', font = fontS41, visible = False)
txtS43 = sg.Text(
"""
Strange… I would be careful who I show that letter to, enemies of the kingdom lurk in every corner and only Holy knights of Aeluminar can possess items brandishing the sacred
symbol, but enough talk if you plan on leaving today you might want to start heading out before nightfall.
""", background_color = '#4B3619', font = fontS41, visible = False)
btnS43 = sg.Button('Head out in search of adventure!', font = fontS41, visible = False, key = 'BTN_S43')

layout_S4 = [[imgS41], [txtS41], [btnS41, btnS42], [txtS42, txtS43], [btnS43]]
frmS4 = sg.Frame ('', layout_S4, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', visible = False, key = 'FRMS4')
################################################################################################################################################

#############SLIDE 4_WIN###########################################################################################################################
fontS41_win = ('MS Serif', 35)
fontS42_win = ('MS Serif', 15)
imgS41_win = sg.Image ('TestImage.png')
txtS41_win = sg.Text(
"""
LUCKY ENDING!
""", background_color = '#4B3619', font = fontS41_win)
txtS42_win = sg.Text(
"""
Through sheer luck, you’ve managed to trick the mysterious man and taken enough of his gold for 3 lifetimes.
You travel back to your farm and enjoy the rest of your life in humble luxury. 
""", background_color = '#4B3619', font = fontS42_win)
btnS41_win = sg.Button('EXIT', font = fontS42_win, key='BTN_S41_WIN')


layout_S4_win = [[imgS41_win], [txtS41_win], [txtS42_win], [btnS41_win]]
frmS4_win = sg.Frame ('', layout_S4_win, visible = False, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRMS4_WIN')
################################################################################################################################################

######Slide5################################################################################################################
imgS51= sg.Image('TestImage.png')
fontS51 = ("MS Serif", 12)
fontS52= ("MS Serif", 35)
txtS51= sg.Text('Brave {character_NAME} heads out following the directions of the path leading to the forest.', background_color = '#4B3619', font=fontS51)
txtS52= sg.Text(
    '''Although I had just left, the only Tavern for 100 miles there was still a long road ahead. As
the sun starts to set, I see the forest in the distance, a great expanse of trees covers the land for
as far as I can see. Darkness now surrounds me, but the faint glimmer of the moon shows me the path ahead.
As I walk past the first trees I notice the darkness is so thick that not a shred of Moonlight can pierce
it. I shudder, but keep walking somewhere here there should be a path into the forest.''',background_color = '#4B3619', font=fontS51)
btnS51= sg.Button('Keep Searching',font=fontS51, key = 'BTN_S51')

layout_frS5= [[imgS51], [txtS51], [txtS52], [btnS51]]
frmS5= sg.Frame('', layout_frS5,font=fontS51,  element_justification='c', size=(1920,1080), background_color = '#4B3619', visible=False, key= 'FRMS5')
############################################################################################################################

######Slide6################################################################################################################
imgS61= sg.Image('TestImage.png')
fontS61 = ("MS Serif", 12)
fontS62= ("MS Serif", 35)
txtS61= sg.Text('All of a sudden I see a dim light in the distance. Damn, the reason I left so late was so that there would be no one else. What should I do…',font=fontS61, background_color = '#4B3619')
btnS61= sg.Button('Run into the forest and face the unknown', font=fontS61, key = 'BTN_S61')
btnS62= sg.Button('Confront whatever lies ahead', font=fontS61, key = 'BTN_S62')

layout_frS6= [[imgS61], [txtS61], [btnS61,btnS62]]
frmS6= sg.Frame('', layout_frS6,font=fontS61,  element_justification='c', size=(1920,1080), visible=False, background_color = '#4B3619', key= 'FRMS6')
############################################################################################################################

layout = [[frmS0, frmS1, frmS2, frmS3, frmS4, frmS4_win, frmS5, frmS6]]

window = sg.Window('Quest Game', layout,  element_justification='c', background_color = '#4B3619').Finalize()
window.Maximize()

while True:
    event, values = window.read()
# If statement for the button to continue to slide 1
    if event == 'BTN_S01':
        window['FRMS0'].update(visible = False)
        
# If statement for the button to continue to slide 2
    elif event == 'BTN_S11':
        window['FRMS1'].update(visible = False)

# If statement for slide 2 - for the different options inside the slide with the different text
    elif event == 'BTN_S21':
        btnS22.update(visible=False)
        txtS22.update(visible=True)
        btnS23.update(visible= True)
    elif event == 'BTN_S22':
        btnS21.update(visible=False)
        txtS23.update(visible=True)
        btnS23.update(visible= True)
        
# If statement for the button to continue to slide 3
    elif event=='BTN_S23':
        window['FRMS2'].update(visible= False)
        
# If statement for slide 3 - for the different options inside the slide with the different text       
    elif event=='BTN_S31':
        guess_number= int(values['INP_S31'])
        if guess_number== random_number:
            sg.popup("You guessed it!",text_color='black', background_color = '#cba331', font=fontS31)
            btnS31.update(visible=False)
            btnS33.update(visible=True)
        else:
            sg.popup("Wrong, good try though!:",text_color='black', background_color = '#cba331', font=fontS31)
            btnS31.update(visible=False)
            btnS32.update(visible=True)
        
# If statement for the button to continue to slide 4
    elif event=='BTN_S32':
        window['FRMS3'].update(visible = False)
        window['FRMS4'].update(visible = True)
    
    elif event == 'BTN_S33':
        window['FRMS3'].update(visible = False)
        window['FRMS4_WIN'].update(visible = True)

#If statement for the Slide 4 different options
    elif event == 'BTN_S41':
        btnS42.update(visible = False)
        txtS42.update(visible = True)
        btnS43.update(visible = True)
    elif event == 'BTN_S42':
        btnS41.update(visible = False)
        txtS43.update(visible = True)
        btnS43.update(visible = True)
# If statement for the button to continue to slide 5
    elif event == 'BTN_S43':
        window['FRMS4'].update(visible= False)
        window['FRMS5'].update(visible= True)
# If statement for the button to continue to slide 6
    elif event == 'BTN_S51':
        window['FRMS5'].update(visible= False)
        window['FRMS6'].update(visible= True)

#End
    elif event == sg.WIN_CLOSED or event == 'BTN_S41_WIN':
        break

window.close()