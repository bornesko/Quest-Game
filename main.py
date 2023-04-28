import PySimpleGUI as sg
import random
######Slide0################################################################################################################
imgS01=sg.Image('TestImage.png')
fontS01 = ("MS Serif", 12)
fontS02= ("MS Serif", 35)
txtS01= sg.Text('Welcome to ####', font=fontS02, background_color= '#4B3619')
txtS02= sg.Text('Please enter your name!', font=fontS01, background_color= '#4B3619')
inpS01= sg.Input('',size= (30,None), font=fontS01, key = 'INP_S01')
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
txtS32=sg.Text('', background_color = '#4B3619', font=fontS31)
txtS33=sg.Text('Choose your Number wisely!', background_color = '#4B3619', font=fontS31)
inpS31= sg.Input('',size= (30,None), font=fontS31, key = 'INP_S31')

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
txtS51= sg.Text('', background_color = '#4B3619', font=fontS51)
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

######SlideA1################################################################################################################
imgSA11= sg.Image('TestImage.png')
fontSA11 = ("MS Serif", 12)
fontSA12= ("MS Serif", 35)
txtSA11= sg.Text("""
As I run into the forest, I don’t look back jumping past fallen branches as darkness surrounds me.
My heart still pounding from the strange situation on the road. As I get deeper into the forest, I
notice the ground is covered in fungi and mushrooms. The bright florescent tops start to light up
the forest floor and the sudden stillness gives me an eerie feeling. If the situation were not so
terrifying I would stay to admire the beautiful colours. As I make my way deeper into the forest,
I see a small shape in the distance, but not for long as it scurries away into the darkness. I begin
to feel nervous, unsure if I made the correct decision entering the forest here. I see it again, but
this time closer, the outline is about the half the size of me, but it manages to disappear again
before I can get a good look. “Hihihih, another foolish boy stumbles into my domain.” Whatever I saw
is now standing behind me.""",font=fontSA11, background_color = '#4B3619')
btnSA11= sg.Button('Turn Around', font=fontSA11, key = 'BTN_SA11')


layout_frSA1= [[imgSA11], [txtSA11], [btnSA11]]
frmSA1= sg.Frame('', layout_frSA1,font=fontSA11,  element_justification='c', size=(1920,1080), visible=False, background_color = '#4B3619', key= 'FRMSA1')
############################################################################################################################

#############SLIDE A2###########################################################################################################################
fontSA21 = ('MS Serif', 12) 
imgSA21 = sg.Image ('TestImage.png')
txtSA21 = sg.Text(
"""
A grotesque half mushroom half man creature stands before me, with a distorted smile looking upon me. “Oh how lucky I am that none of my brothers
found you first, I always knew our great mother ### loved me more.” 
""", font = fontSA21, visible = True, background_color = '#4B3619')
btnSA21 = sg.Button('What are you?', font = fontSA21, key='BTN_SA21')
btnSA22 = sg.Button('Get away from me!', font = fontSA21, key = 'BTN_SA22')
txtSA22 = sg.Text(
"""
“Hihihi, as sons and daughters of the great #### we stand guard here to await anyone foolish enough to enter this area, if you are able to beat me in
a game you will progress if not I will get to eat you hihihi.”
""", font = fontSA21, visible = False, background_color = '#4B3619')
txtSA23 = sg.Text(
"""
“Did no one ever teach you manners boy, you’ll play a game with me now. If you lose I’ll have you for my dinner hihihi.”
""", font = fontSA21, visible = False, background_color = '#4B3619')
btnSA23 = sg.Button('PLAY!', font = fontSA21, visible = False, key = 'BTN_SA23')

layout_frSA2 = [[imgSA21], [txtSA21], [btnSA21, btnSA22], [txtSA22, txtSA23], [btnSA23]]
frmSA2 = sg.Frame ('', layout_frSA2, visible = False, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRMSA2')
################################################################################################################################################

######SlideAA1###############################################################################################################
imgSAA11= sg.Image('TestImage.png', key= 'IMG_SAA11')
imgSAA12= sg.Image('TestImage.png', visible=False, key= 'IMG_SAA12')
fontSAA11 = ("MS Serif", 12)
fontSAA12= ("MS Serif", 35)
txtSAA11= sg.Text("""
I won! “That’s not possible I’ve never lost before. No come here I don’t care if I’ve lost I’ll eat you anyway.”
Suddenly the skin of the disgusting mushroom man starts to bubble and he lets out a horrifying shriek. As he steps
closer to me, while reaching out his body starts to expand into a bubble that explodes open flinging his entrails everywhere. """,font=fontSAA11, background_color = '#4B3619', key= 'TXT_SAA11')
txtSAA12= sg.Text("""
On the ground where he was standing a few seconds ago a puddle only remains with the number 83 etched into the ground.
Hmm this seems important I had better remember it for later. With a face full of confidence, I march foreword into the
unknown dangers ahead of me.""",font=fontSAA11, visible=False, background_color = '#4B3619', key= 'TXT_SAA12')
btnSAA11= sg.Button('Observe', font=fontSAA11, key = 'BTN_SAA11')
btnSAA12= sg.Button('Continue on', font=fontSAA11, visible=False, key= 'BTN_SAA12')



layout_frSAA1= [[imgSAA11,imgSAA12], [txtSAA11], [btnSAA11], [txtSAA12], [btnSAA12]]
frmSAA1= sg.Frame('', layout_frSAA1,font=fontSAA11,  element_justification='c', size=(1920,1080), visible=False, background_color = '#4B3619', key= 'FRMSAA1')
############################################################################################################################

######SlideAA2###############################################################################################################
imgSAA21= sg.Image('TestImage.png')

fontSAA21 = ("MS Serif", 12)
fontSAA22= ("MS Serif", 35)

txtSAA21= sg.Text("""
Filled with courage I continue to march into the wilderness. Over bushes and roots, I climb always pushing forward.
After what feels like an eternity I finally make it onto more stable ground. Walking becomes a little bit easier now
and I actually begin to pick up some pace. “Just keep going,” I tell myself now more determined than ever. As I walk
forward, I realize the reality of my situation in that I will most likely have to keep facing these creatures. Already
the scenery around me starts to change, the forest in this area looks recently burned and the bark of the giant trees
have scorch marks surrounding them. My stomach starts to turn “This might be the worst one so far,” I think to myself
as I keep walking. With every step, the heat seems to increase until I can barely move forward. “You there not another
step.” “Yes you better not move.” “Stay or we will swallow you whole.” """,font=fontSAA21, background_color = '#4B3619')
btnSAA21= sg.Button('Look to the side', font=fontSAA21, key = 'BTN_SAA21')




layout_frSAA2= [[imgSAA21], [txtSAA21], [btnSAA21]]
frmSAA2= sg.Frame('', layout_frSAA2,font=fontSAA21,  element_justification='c', size=(1920,1080), visible=False, background_color = '#4B3619', key= 'FRMSAA2')
###############################################################################################################################################


######SlideAA3###############################################################################################################
imgSAA31= sg.Image('TestImage.png')

fontSAA31 = ("MS Serif", 12)
fontSAA32= ("MS Serif", 35)

txtSAA31= sg.Text("""
As I turn to the side, I see the monstrosity in front of me. A three-headed hound surrounded in flames walks up to me.
It leaves giant scorch marks with every step.

“How dare you try to pass us without completing your challenge.”

“You hav…”

“Quiet idiot I always speak second, as was being said you have to complete 3 riddles where each answer consists of 1 word.
One you may get wrong, but anymore and you’ll be our dinner.”

“Exactly fool, our dinner!”
 """,font=fontSAA31, background_color = '#4B3619')
btnSAA31= sg.Button('Play!', font=fontSAA31, key = 'BTN_SAA31')




layout_frSAA3= [[imgSAA31], [txtSAA31], [btnSAA31]]
frmSAA3= sg.Frame('', layout_frSAA3,font=fontSAA31,  element_justification='c', size=(1920,1080), visible=False, background_color = '#4B3619', key= 'FRMSAA3')
###########################################################################################################################################################################################

######SlideAA5###############################################################################################################
imgSAA51= sg.Image('TestImage.png')
fontSAA51 = ("MS Serif", 12)
fontSAA52= ("MS Serif", 35)

txtSAA51= sg.Text("""
The hounds stare at me in terror.

“You cheated!”

“No one has ever beat us”

“We’ll tear off your hea…”

Before the final head could utter its sentence raging flames jut from the body of
the Cerberus searing its flesh and burning it from the inside out. The hound wails
back and forth in agony, the three heads biting and tearing at each other in confusion.
It doesn’t take long for the screams to stop as the body is burnt to ashes leaving
behind a pile in the shape of a 3. “Again… these numbers are important! No use staying
here though.” I think to myself. I take a deep breath and keep walking. Whatever is
at the center of this forest I fell drawn to it. Without looking back, I head out.
 """,font=fontSAA51, background_color = '#4B3619')
btnSAA51= sg.Button('On to the next obstacle', font=fontSAA51, key = 'BTN_SAA51')




layout_frSAA5= [[imgSAA51], [txtSAA51], [btnSAA51]]
frmSAA5= sg.Frame('', layout_frSAA5,font=fontSAA51,  element_justification='c', size=(1920,1080), visible=False, background_color = '#4B3619', key= 'FRMSAA5')
###########################################################################################################################################################################################################

######SlideAA6###############################################################################################################
imgSAA61= sg.Image('TestImage.png', key= 'IMG_SAA61')
imgSAA62= sg.Image('TestImage.png', visible=False, key= 'IMG_SAA62')
fontSAA61 = ("MS Serif", 12)
fontSAA62= ("MS Serif", 35)

txtSAA61= sg.Text("""
Walking through the woods I grow increasingly tired, it has now been quite some time
since I entered the forest. As moonlight still blocked out traversing the area is hard.
Maybe there is a better option here.
 """,font=fontSAA61, background_color = '#4B3619', key = 'TXT_SAA61')
btnSAA61= sg.Button('Look for a cozy area and camp', font=fontSAA61, key = 'BTN_SAA61')
btnSAA62= sg.Button('Keep walking!', font=fontSAA61, key = 'BTN_SAA62')
txtSAA62= sg.Text("""
“Maybe it wouldn’t be too bad to get some rest.” I think to myself. I look around the
area and come across a comfortable looking plant of sorts, the big green leaved look
like they would make a good bed. I sit in the area and take a few moments to relax and
reflect. After around half an hour I decide to:
""",font=fontSAA61, visible= False, background_color = '#4B3619', key = 'TXT_SAA62')
btnSAA63= sg.Button('Go to sleep', font=fontSAA61, visible=False, key = 'BTN_SAA63')
btnSAA64= sg.Button('Get up and keep going again', font=fontSAA61, visible=False, key = 'BTN_SAA64')
txtSAA63= sg.Text("""
Those were my last moments, I never get to wake up again. I had fallen for a trap and
while my eyes were shut, the large leaves of a giant carnivores plant encircled me. I
become digested nutrients to one of the great creatures of the forest and this would
be the end of my journey.
""",font=fontSAA61, visible=False, background_color = '#4B3619', key = 'TXT_SAA63')
btnSAA65= sg.Button('Next', font=fontSAA61, visible=False, key = 'BTN_SAA65')
txtSAA64= sg.Text("""
I decide to keep going forward. “There can’t be much more of this, I should almost be
in the center of the forest.” As I walk, I realize that I must be approaching another
obstacle. All around me are the spun webs of little forest spiders.
""",font=fontSAA61, visible=False, background_color = '#4B3619', key = 'TXT_SAA64')
btnSAA66= sg.Button('Keep going', visible=False, font=fontSAA61, key = 'BTN_SAA66')



layout_frSAA6= [[imgSAA61,imgSAA62], [txtSAA61,txtSAA62], [btnSAA61,btnSAA62,btnSAA63,btnSAA64], [txtSAA63,txtSAA64], [btnSAA65,btnSAA66]]
frmSAA6= sg.Frame('', layout_frSAA6,font=fontSAA61,  element_justification='c', size=(1920,1080), visible=False, background_color = '#4B3619', key= 'FRMSAA6')
##############################################################################################################################################

######SlideAB1###############################################################################################################
imgSAB11= sg.Image('TestImage.png', key= 'IMG_SAB11')
imgSAB12= sg.Image('TestImage.png', visible=False, key= 'IMG_SAB12')
fontSAB11 = ("MS Serif", 12)
fontSAB12= ("MS Serif", 35)
txtSAB11= sg.Text("""
“Hihihi stupid, stupid boy come here.” The overgrown mushroom lunges at me with murderous intent. I try to run, but it is too late.
I feel a sharp pain as its teeth sink into the side of my body. I yell out in terror, as the mushroom deals me a terrible blow. It
jumps backwards getting ready for another attack. In the next moment however, the ground under me breaks throwing me down a hill I
only noticed now. I tumble for what seems like a minute before finally ending on the bottom.  """,font=fontSAB11, background_color = '#4B3619', key= 'TXT_SAB11')
txtSAB12= sg.Text("""
I sprint as far away as possible from this area. Looking around I no longer see any mushrooms, I hope that creature won’t follow me.
I can’t take any more of these wounds, but I am this far already might as well keep going. I hurry along determined to make it, as I
run into the forest it slowly starts to open into a plateau of grass, I see the high beautiful full moon in front of me. A calmness
takes me over and just as a smile starts to form dark red eyes stare at me from across the field.""",font=fontSAB11, visible=False, background_color = '#4B3619', key= 'TXT_SAB12')
txtSAB13= sg.Text("""
I decide to stay and not risk the noise. However, just as I take my next breath the mushroom leaps from the top of the hill, its
monstrous fangs sinking into my neck. Blood sprays everywhere and as I try to reach out my power fades. “Damn I should have ran…” """,font=fontSAB11, visible=False, background_color = '#4B3619', key= 'TXT_SAB13')

btnSAB11= sg.Button('Run away as far away as possible', font=fontSAB11, key = 'BTN_SAB11')
btnSAB12= sg.Button('Stay and be quiet', font=fontSAB11, key= 'BTN_SAB12')
btnSAB13= sg.Button('Continue', font=fontSAB11, visible=False, key= 'BTN_SAB13')
btnSAB14= sg.Button('Continue', font=fontSAB11, visible=False, key= 'BTN_SAB14')



layout_frSAB1= [[imgSAB11,imgSAB12], [txtSAB11], [btnSAB11,btnSAB12], [txtSAB12,txtSAB13], [btnSAB13,btnSAB14]]
frmSAB1= sg.Frame('', layout_frSAB1,font=fontSAB11,  element_justification='c', size=(1920,1080), visible=False, background_color = '#4B3619', key= 'FRMSAB1')
############################################################################################################################

#############SLIDE AB3- Bad Ending###########################################################################################################################
fontSAB31 = ('MS Serif', 35)
fontSAB32 = ('MS Serif', 15)
imgSAB31 = sg.Image ('TestImage.png')
txtSAB31 = sg.Text(
"""
BAD ENDING!
""", background_color = '#4B3619', font = fontSAB31)
txtSAB32 = sg.Text(
"""
In the end, the nightmares of Hadesvale were too powerful. The forest becomes
your grave and you are forgotten as the world descends into darkness.  
""", background_color = '#4B3619', font = fontSAB32)
btnSAB31 = sg.Button('EXIT', font = fontSAB32, key='BTN_SAB31')


layout_SAB3 = [[imgSAB31], [txtSAB31], [txtSAB32], [btnSAB31]]
frmSAB3 = sg.Frame ('', layout_SAB3, size=(1920,1080), element_justification = 'c', visible= False, background_color = '#4B3619', key = 'FRMSAB3')
################################################################################################################################################

######SlideAB4###############################################################################################################
imgSAB41= sg.Image('TestImage.png', key= 'IMG_SAB41')
imgSAB42= sg.Image('TestImage.png', visible=False, key= 'IMG_SAB42')
fontSAB41 = ("MS Serif", 12)
fontSAB42= ("MS Serif", 35)
txtSAB41= sg.Text("""
“No!!! you fool” The enraged werewolf leaps at me with bloodshot eyes. However, before it reaches me the
ground beneath it breaks open pulling it deep into the ground! “No no I almost had him it’s not fair.” His
claws grab onto the ground, but as he is pulled deeper his claws are thrust with him into the depths. His
shrieks echo in the night until everything falls silent. I slowly make my way up to the hole. The outline
forms the number 48. I will try to remember that for later, but for now, I want to leave this place as fast
as possible.   """,font=fontSAB41, background_color = '#4B3619')

btnSAB41= sg.Button('Continue on', font=fontSAB41, key = 'BTN_SAB41')




layout_frSAB4= [[imgSAB41], [txtSAB41], [btnSAB41]]
frmSAB4= sg.Frame('', layout_frSAB4,font=fontSAB41,  element_justification='c', size=(1920,1080), visible=False,  background_color = '#4B3619', key= 'FRMSAB4')
############################################################################################################################

######SlideAC1###############################################################################################################
imgSAC11= sg.Image('TestImage.png', visible=False, key= 'IMG_SAC11')
imgSAC12= sg.Image('TestImage.png', visible=False, key= 'IMG_SAC12')
fontSAC11 = ("MS Serif", 12)
fontSAC12= ("MS Serif", 35)

txtSAC11= sg.Text("""
Before I can even react, the hound leaps towards me. Each head biting down on
a different part of me, I feel horrifying pain, as I am torn limb from limb…
 """,font=fontSAC11, background_color = '#4B3619', visible=False, key = 'TXT_SAC11')
btnSAC11= sg.Button('Continue', font=fontSAC11, visible=False, key = 'BTN_SAC11')

txtSAC12= sg.Text("""
The hound leaps towards me, but miraculously enough I dodge right as it descends
upon me. In an effort to escape I slide underneath it and run towards the dense
crop of trees. However, in a split second it is already behind me, I jump for the
trees and as I scramble up to keep running, I hear a loud thud behind me and the
shaking of a tree.

“You foolish oaf you’ve done it again.”
“Idiot we should have torn you off our body a long time ago.”
“Sorry, I didn’t meant to hit the tree.”
I don’t take a single moment to listen to the conversation and run as fast as I can.
“Look now he’s going to get awa…”

The voices trail off in the distance as I run downhill now. For what seems like at
least 10 min, I don’t stop running. By the end I stop to catch my breath, finally
it seems like I am out of the danger zone, the trees around here are no longer scorched.
Determined as ever I wander off into my destiny.
""",font=fontSAC11, visible= False, background_color = '#4B3619', key = 'TXT_SAC12')
btnSAC12= sg.Button('Head out!', font=fontSAC11, visible= False, key = 'BTN_SAC12')


layout_frSAC1= [[imgSAC11,imgSAC12], [txtSAC11,txtSAC12], [btnSAC11,btnSAC12]]
frmSAC1= sg.Frame('', layout_frSAC1,font=fontSAC11,  element_justification='c', size=(1920,1080), visible=False, background_color = '#4B3619', key= 'FRMSAC1')
#######################################################################################################################################################

######SlideAC2###############################################################################################################
imgSAC21= sg.Image('TestImage.png')
fontSAC21 = ("MS Serif", 12)
fontSAC22= ("MS Serif", 35)

txtSAC21= sg.Text("""
It has now been over 30 min since I have encountered that beast. Hope swells up in
my “Maybe that was all of them.” I continue to walk, the forest surrounding me as
plain as ever. As I take my next step, my right foot plunges into a gooey brown
substance. I notice that the ground in front of me has been turned into a swamp.
It was difficult at first to see, however now I clearly see the marsh before me.
“Uh spoke too soon, where is the next monster.” I struggle forward with each foot
content that the beast will approach me soon enough. As I make myself towards the
center, I hear a load crash, the trees surrounding me shake and vibrate. Above me,
I hear the birds flying off in search of safety. I now see the monstrosity before
me. Its giant body slithering towards me, bigger than any house I had ever seen. 
 """,font=fontSAC21, background_color = '#4B3619')
btnSAC21= sg.Button('Continue', font=fontSAC21, key = 'BTN_SAC21')


layout_frSAC2= [[imgSAC21], [txtSAC21], [btnSAC21]]
frmSAC2= sg.Frame('', layout_frSAC2,font=fontSAC21,  element_justification='c', size=(1920,1080), visible=False, background_color = '#4B3619', key= 'FRMSAC2')
############################################################################################################################################################

######SlideAC3###############################################################################################################
imgSAC31= sg.Image('TestImage.png')
fontSAC31 = ("MS Serif", 12)
fontSAC32= ("MS Serif", 35)

txtSAC31= sg.Text("""
The head of the giant snake like monster looms over me. I am struck by a fear I have never felt
before there is no escape from this monster. “I am sure my younger siblings have done much to
entertain you shishishi. I have heard their screams since you have entered this forest, do not
think I will be so kind to you as they have. However, I am unfortunately bound by the same code
as they are, let’s get this over with and play our game shishishi.” My heart is filled with dread
as I stare up at the beast across me, but I don’t have much of a choice. 
 """,font=fontSAC31, background_color = '#4B3619')
btnSAC31= sg.Button('Play!', font=fontSAC31, key = 'BTN_SAC31')


layout_frSAC3= [[imgSAC31], [txtSAC31], [btnSAC31]]
frmSAC3= sg.Frame('', layout_frSAC3,font=fontSAC31,  element_justification='c', size=(1920,1080), visible=False, background_color = '#4B3619', key= 'FRMSAC3')
#################################################################################################################################################################################

######SlideAC4###############################################################################################################
imgSAC41= sg.Image('TestImage.png', visible=False, key= 'IMG_SAC41')
imgSAC42= sg.Image('TestImage.png', visible=False, key= 'IMG_SAC42')
fontSAC41 = ("MS Serif", 12)
fontSAC42= ("MS Serif", 35)

txtSAC41= sg.Text("""
“Sorry little one you have come far, but this is the end.” I look up as the monster
opens its mouth, sitting down I accept my fate, as this force of nature strikes at me.
In a single sweep, I am no more as its teeth crush me.
 """,font=fontSAC41, background_color = '#4B3619', visible=False, key = 'TXT_SAC41')
btnSAC41= sg.Button('Continue', font=fontSAC41, visible=False, key = 'BTN_SAC41')

txtSAC42= sg.Text("""
“A worthy challenger, you have my respect. I wish I could have avenged my siblings, but
I have lived a long time. I guess this is the end.” The basilisk moves away from me and
as it does, light emits from it, shining to brightly for me to see it. The light burns
my eyes, forcing me to shield them. As I turn back around the basilisk is no more. In its
place, I just see a white outline with the number 1 across the ground. I hesitate for a
bit but ultimately make my way out of the marsh and towards my goal, I can now feel the
presence of whatever lies in the center of these woods. It is pulling me nearer, but I
don’t know how many more obstacles I have to face. 
""",font=fontSAC41, visible= False, background_color = '#4B3619', key = 'TXT_SAC42')
btnSAC42= sg.Button('Head out!', font=fontSAC41, visible= False, key = 'BTN_SAC42')


layout_frSAC4= [[imgSAC41,imgSAC42], [txtSAC41,txtSAC42], [btnSAC41,btnSAC42]]
frmSAC4= sg.Frame('', layout_frSAC4,font=fontSAC41,  element_justification='c', size=(1920,1080), visible=False, background_color = '#4B3619', key= 'FRMSAC4')
#########################################################################################################################################################################################

#############SLIDE B1###########################################################################################################################
fontB11 = ('MS Serif', 12) 
imgB11 = sg.Image ('TestImage.png')
txtB11 = sg.Text(
"""
“You decide to stand your ground and face the person or thing approaching! My heart races, almost bursting out of my chest, as the light draws
nearer. Suddenly, I notice the outline of the figure a WAGON! As it approaches, I see an old man sitting at the front, staring at me intensely.
He yells out “What be your purpose wandering around these woods so late?"
""", font = fontB11, visible = True, background_color = '#4B3619')
btnB11 = sg.Button('I won’t lie to you Mister I have come seeking adventure and wish to find whatever lies deep in this forest', font = fontB11, key='BTN_B11')
btnB12 = sg.Button('I come from a nearby farm, I don’t want any trouble I’ll be heading back soon', font = fontB11, key = 'BTN_B12')
txtB12 = sg.Text(
"""
Haha you are the first honest man I’ve come across in a while. I like you boy, but if you plan to enter the Woods, I would suggest following this
path for about another 200 paces and look for a small opening in the bottom of the shrub. From there you should find a path deeper into the woods.
I will warn you though that place is evil, not that I care I have some sheep to tend to. Farewell!
""", font = fontB11, visible = False, background_color = '#4B3619')
txtB13 = sg.Text(
"""
Why is he looking at me like that “Hmm if you say so boy I have no time to waste on someone like you. The man keep riding off and with a sick feeling
in my stomach I decide to run into the forest, I no longer wanted to risk being seen on the road.
""", font = fontB11, visible = False, background_color = '#4B3619')

layout_B1 = [[imgB11], [txtB11], [btnB11, btnB12], [txtB12, txtB13]]
frmB1 = sg.Frame ('', layout_B1, visible = False, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRMB1')
################################################################################################################################################

layout = [[frmS0, frmS1, frmS2, frmS3, frmS4, frmS4_win, frmS5, frmS6, frmSA1, frmSA2, frmSAA1, frmSAA2, frmSAA3, frmSAA5, frmSAA6, frmSAB1, frmSAB3, frmSAB4, frmSAC1, frmSAC2, frmSAC3, frmSAC4, frmB1]]

window = sg.Window('Quest Game', layout,  element_justification='c', background_color = '#4B3619').Finalize()
window.Maximize()

while True:
    event, values = window.read()
# If statement for the button to continue to slide 1
    if event == 'BTN_S01':
        window['FRMS0'].update(visible = False)
        character_name = str(values['INP_S01'])
        
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
        txtS32.update(f'My name is {character_name} and I accept your offer!')
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
        txtS51.update(f'Brave {character_name} heads out following the directions of the path leading to the forest.')
        
# If statement for the button to continue to slide 6
    elif event == 'BTN_S51':
        window['FRMS5'].update(visible= False)
        window['FRMS6'].update(visible= True)

####################If statement for the A-branch#########################################
    elif event == 'BTN_S61':
        window['FRMS6'].update(visible= False)
        window['FRMSA1'].update(visible=True)

# If statement for the button to contunue to Slide A2
    elif event == 'BTN_SA11':
        window['FRMSA1'].update(visible = False)
        window['FRMSA2'].update(visible = True)

# If statment for the Slide A2 actions
    elif event == 'BTN_SA21':
        btnSA22.update(visible = False)
        txtSA22.update(visible = True)
        btnSA23.update(visible = True)
    elif event == 'BTN_SA22':
        btnSA21.update(visible = False)
        txtSA23.update(visible = True)
        btnSA23.update(visible = True)
# Import triva A3 
    elif event == 'BTN_SA23':
        window['FRMSA2'].update(visible = False)
        import trivia_A3
        from trivia_A3 import points
        if points < 3:
            window['FRMSAB1'].update(visible = True)
        else:
            window['FRMSAA1'].update(visible = True)
# If statement for the slide AA1
    elif event == 'BTN_SA318':
        window['FRMSAA1'].update(visible = True)
        
# If statement for the slide AA1 actions
    elif event == 'BTN_SAA11':
        window['TXT_SAA12'].update(visible= True)
        window['IMG_SAA11'].update(visible= False)
        window['IMG_SAA12'].update(visible= True)
        window['BTN_SAA12'].update(visible= True)


# If statement for the slide AA2
    elif event == 'BTN_SAA12' or event == 'BTN_SAB41':
        window['FRMSAA1'].update(visible= False)
        window['FRMSAB4'].update(visible= False)
        window['FRMSAA2'].update(visible= True)

# If statement for the slide AA3
    elif event == 'BTN_SAA21':
        window['FRMSAA2'].update(visible= False)
        window['FRMSAA3'].update(visible= True)

# If statement for the slide AA4- Riddle
    elif event == 'BTN_SAA31':
        window['FRMSAA3'].update(visible= False)
        import riddle_1
        from riddle_1 import riddle_points
        if riddle_points >= 2:
            window['FRMSAA5'].update(visible= True)
        elif riddle_points <= 2 and points < 3:
            window['FRMSAC1'].update(visible= True)
            window['IMG_SAC11'].update(visible=True)
            window['TXT_SAC11'].update(visible=True)
            window['BTN_SAC11'].update(visible=True)
            
        elif riddle_points <= 2:
            window['FRMSAC1'].update(visible= True)
            window['IMG_SAC12'].update(visible=True)
            window['TXT_SAC12'].update(visible=True)
            window['BTN_SAC12'].update(visible=True)
            
            
# If statement for the slide AA6
    elif event == 'BTN_SAA51':
        window['FRMSAA5'].update(visible= False)
        window['FRMSAA6'].update(visible= True)
        
    elif event == 'BTN_SAA61':
        window['TXT_SAA61'].update(visible = False)
        window['TXT_SAA62'].update(visible = True)
        window['BTN_SAA61'].update(visible = False)
        window['BTN_SAA62'].update(visible = False)
        window['BTN_SAA63'].update(visible = True)
        window['BTN_SAA64'].update(visible = True)
        window['IMG_SAA61'].update(visible = False)
        window['IMG_SAA62'].update(visible = True)
    
    elif event == 'BTN_SAA62' or event == 'BTN_SAA64':
        window['TXT_SAA64'].update(visible = True)
        window['BTN_SAA61'].update(visible = False)
        window['BTN_SAA66'].update(visible = True)
        
    elif event == 'BTN_SAA63':
        window['BTN_SAA64'].update(visible = False)
        window['TXT_SAA63'].update(visible = True)
        window['BTN_SAA65'].update(visible = True)
# IF statement for the slide Bad ending
    elif event == 'BTN_SAA65':
        window['FRMSAB3'].update(visible = False)
        window['TXT_SAA63'].update(visible = True)
            
###################################AB branch##########################

# If statement for the slide AB1 actions
    elif event == 'BTN_SAB11':
        window['BTN_SAB12'].update(visible= False)
        window['TXT_SAB12'].update(visible= True)
        window['IMG_SAB11'].update(visible= False)
        window['IMG_SAB12'].update(visible= True)
        window['BTN_SAB13'].update(visible= True)
    elif event == 'BTN_SAB12':
        window['BTN_SAB11'].update(visible= False)
        window['TXT_SAB13'].update(visible= True)
        window['BTN_SAB14'].update(visible= True)
# If statement for the slide AB2
    elif event == 'BTN_SAB13':
        window['FRMSAB1'].update(visible= False)
        import Story_obstacle
        from Story_obstacle import correct
        if correct:
            window['FRMSAB4'].update(visible= True)
        else:
            window['FRMSAB3'].update(visible= True)
            


# If statement for the slide AB3 actions
    elif event == 'BTN_SAB14':
        window['FRMSAB1'].update(visible= False)
        window['FRMSAB3'].update(visible= True)

###################################AC branch##########################

# If statement for the slide AC1:
    elif event == 'BTN_SAC11':
        window['FRMSAC1'].update(visible=False)
        window['FRMSAB3'].update(visible=True)

# If statement for the slide AC2:
    elif event == 'BTN_SAC12':
        window['FRMSAC1'].update(visible=False)
        window['FRMSAC2'].update(visible=True)

# If statement for the slide AC3:
    elif event == 'BTN_SAC21':
        window['FRMSAC2'].update(visible=False)
        window['FRMSAC3'].update(visible=True)
        import math_1
        from math_1 import answer
        if answer == 1:
            window['FRMSAC3'].update(visible=False)
            window['FRMSAC4'].update(visible=True)
            window['IMG_SAC42'].update(visible=True)
            window['TXT_SAC42'].update(visible=True)
            window['BTN_SAC42'].update(visible=True)
        else:
            wwindow['FRMSAC3'].update(visible=False)
            window['FRMSAC4'].update(visible=True)
            window['IMG_SAC41'].update(visible=True)
            window['TXT_SAC41'].update(visible=True)
            window['BTN_SAC41'].update(visible=True)
            


##############################If statement for the B-branch################################
    elif event == 'BTN_S62':
        window['FRMS6'].update(visible= False)
        window['FRMB1'].update(visible=True)

#If statement for the B-1 slide
    elif event == 'BTN_B11':
        btnB12.update(visible = False)
        txtB12.update(visible = True)
    elif event == 'BTN_B12':
        btnB11.update(visible = False)
        txtB13.update(visible = True)
#End
    elif event == sg.WIN_CLOSED or event == 'BTN_S41_WIN' or event == 'BTN_SAB31':
        break

window.close()