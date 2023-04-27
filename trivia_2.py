import PySimpleGUI as sg

font_tr_21 = ('MS Serif', 12) 
img_tr_21 = sg.Image ('quil.png', background_color = '#4B3619')

####################################################################
txt_tr_21 = sg.Text(
'''
My loyal and brave knights,
''', font = font_tr_21, visible = True, background_color = '#4B3619')
#######################################################################

######################################################################################################################
txt_tr_22 = sg.Text('I, King Edward of the Kingdom of ', font = font_tr_21, visible = True, background_color = '#4B3619')
choice_1 = ('Azeroth','Valoria','Eldrid','Aeloria')
cmb_tr_21 = sg.Combo(choice_1, key = 'CMB_TR_21')
txt_tr_23 = sg.Text(', summon you to embark on a perilous quest. Our beloved kingdom is under threat from the', font = font_tr_21, visible = True, background_color = '#4B3619')
#######################################################################

#####################################################################
txt_tr_24 = sg.Text ('evil forest. It has long been a source of fear and darkness, and now it has grown more dangerous than ever before.\n', font = font_tr_21, visible = True, background_color = '#4B3619')
#####################################################################

#####################################################################################
txt_tr_25 = sg.Text ('Reports from our scouts tell us that the trees of the',font = font_tr_21, visible = True, background_color = '#4B3619' )
choice_2 = ('Mirkwood Forest', 'Hadesvale', 'Grimwood', 'Eerie Evergreen')
cmb_tr_22 = sg.Combo (choice_2, key = 'CMB_TR_22')
txt_tr_26 = sg.Text(' have become twisted and malevolent. The creatures that inhabit the', font = font_tr_21, visible = True, background_color = '#4B3619')
####################################################################################

#######################################################################################
txt_tr_27 = sg.Text('forest have become more savage and ruthless, and they have begun to raid our nearby villages. If we do not act quickly, the evil forest will', font = font_tr_21, visible = True, background_color = '#4B3619')
########################################################################################

##########################################################################################
txt_tr_28 = sg.Text('surely spread its corruption throughout our kingdom.\n', font = font_tr_21, visible = True, background_color = '#4B3619')
txt_tr_31 = sg.Text('As the noble knights of the Order of the' , font = font_tr_21, visible = True, background_color = '#4B3619')
choice_3 = ('Illuminati', 'Lucians', "Children of the Light", 'Aeluminar')
cmb_tr_23 = sg.Combo (choice_3, key = 'CMB_TR_23')
txt_tr_29 = sg.Text(', it is your duty to defend our people against all threats. Your bravery and ', font = font_tr_21, visible = True, background_color = '#4B3619')
txt_tr_30 = sg.Text('honor are known throughout the world of', font = font_tr_21, visible = True, background_color = '#4B3619')
choice_4 = ('Aetheria', 'Westeros', 'Warsorach', 'Froelvand')
cmb_tr_24 = sg.Combo (choice_4, key = 'CMB_TR_24')

txt_tr_32 = sg.Text(', and I have faith that you will rise to this challenge with valor and skill.\n', font = font_tr_21, visible = True, background_color = '#4B3619')
##########################################################################################

txt_tr_33 = sg.Text ('We will need every able-bodied knight to venture into the heart of the dark woods and eradicate the evil that lurks there. We will not rest until', font = font_tr_21, visible = True, background_color = '#4B3619')
txt_tr_34 = sg.Text ('We will not rest until the forest is purged of its darkness and our kingdom is safe once more.\n', font = font_tr_21, visible = True, background_color = '#4B3619')
txt_tr_35 = sg.Text ('So I call upon you, my loyal knights, to don your armor, sharpen your swords, and prepare for battle. Together, we will strike at the heart of the', font = font_tr_21, visible = True, background_color = '#4B3619')
txt_tr_36 = sg.Text ('evil that is lurking there and restore peace to our kingdom and our world.\n', font = font_tr_21, visible = True, background_color = '#4B3619')
txt_tr_37 = sg.Text ('May the light protect us as we embark on this dangerous quest!\n', font = font_tr_21, visible = True, background_color = '#4B3619' )
txt_tr_38 = sg.Text ('Yours faithfully,\n', font = font_tr_21, visible = True, background_color = '#4B3619' ) 
txt_tr_39 = sg.Text ('King Edward\n', font = font_tr_21, visible = True, background_color = '#4B3619' )

btn_tr_21 = sg.Button ('Check', font = font_tr_21, key='BTN_TR_21')
btn_tr_22 = sg.Button ('Continue', font = font_tr_21, visible = False, key='BTN_TR_22')




layout_fr_tr_2 = [[txt_tr_21], [txt_tr_22, cmb_tr_21, txt_tr_23], [txt_tr_24], [txt_tr_25, cmb_tr_22, txt_tr_26], [txt_tr_27], [txt_tr_28], [txt_tr_31, cmb_tr_23, txt_tr_29], [txt_tr_30, cmb_tr_24, txt_tr_32], [txt_tr_33], [txt_tr_34], [txt_tr_35], [txt_tr_36], [txt_tr_37], [txt_tr_38], [txt_tr_39], [btn_tr_21, btn_tr_22]]
frm_tr_2 = sg.Frame ('', layout_fr_tr_2, visible = True, size=(1080,1080), element_justification = 'l', background_color = '#4B3619', key = 'FRM_TR_2')

layout = [[frm_tr_2, img_tr_21]]

points_trivia_1 = []


window = sg.Window('', layout, element_justification='l', background_color = '#4B3619').Finalize()
window.Maximize()

while True:
    event, values = window.read()
    if event == 'BTN_TR_21':
        response_1 = values['CMB_TR_21']
        response_2 = values['CMB_TR_22']
        response_3 = values['CMB_TR_23']
        response_4 = values['CMB_TR_24']
        btn_tr_21.update(visible = False)
        btn_tr_22.update(visible = True)

#If path when the first one is correct
        if response_1 == 'Eldrid':
            points_trivia_1.append(1)
            if response_2 == 'Hadesvale':
                points_trivia_1.append(1)
                if response_3 == 'Aeluminar':
                    points_trivia_1.append(1)
                    if response_4 == 'Aetheria':
                        points_trivia_1.append(1)
                else:
                    if response_4 == 'Aetheria':
                        points_trivia_1.append(1)
            else:
                if response_3 == 'Aeluminar':
                    points_trivia_1.append(1)
                    if response_4 == 'Aetheria':
                        points_trivia_1.append(1)
                else:
                    if response_4 == 'Aetheria':
                        points_trivia_1.append(1)
        
#Easter Egg
        elif response_1 == 'Azeroth' and response_2 == 'Mirkwood Forest' and response_3 == 'Children of the Light' and response_4 == 'Westeros':
            sg.popup('I see you are a fantasy geek, but we are playing another game :)', text_color='black', background_color = '#cba331', font = font_tr_21)
        
#If path when the first one is wrong
        else:
            if response_2 == 'Hadesvale':
                points_trivia_1.append(1)
                if response_3 == 'Aeluminar':
                    points_trivia_1.append(1)
                    if response_4 == 'Aetheria':
                        points_trivia_1.append(1)
                else:
                    if response_4 == 'Aetheria':
                        points_trivia_1.append(1)
            else:
                if response_3 == 'Aeluminar':
                    points_trivia_1.append(1)
                    if response_4 == 'Aetheria':
                        points_trivia_1.append(1)
                else:
                    if response_4 == 'Aetheria':
                        points_trivia_1.append(1)
        
        trivia_1_points = int(sum(points_trivia_1)/1)
        sg.popup(f'You have {trivia_1_points}/4 correct', text_color='black', background_color = '#cba331', font = font_tr_21)
         
                
    elif event == sg.WIN_CLOSED or event == 'BTN_TR_22':
        break

window.close()