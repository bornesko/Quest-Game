import PySimpleGUI as sg
import random

# The words, which are going to be present at the hangman
list_words = ['cerberus', 'minotaur', 'griffin', 'phoenix', 'pegasus']

#Choosing a random word
word_random = random.choice(list_words)

img01 = sg.Image('TestImage.png')

font01 = ('MS Serif', 12)
font02 = ('MS Serif', 15)

guesses = 8

txt_empty = sg.Text('',font = font01, background_color = '#4B3619')
txt_empty2 = sg.Text('',font = font01, background_color = '#4B3619')

txt01 = sg.Text('Guess the word: ', font = font02, background_color = '#4B3619')
txt02 = sg.Text('_ '*len(word_random), font = font02, background_color = '#4B3619', key = 'WORD_1')
txt03 = sg.Text('Guess a letter: ', font = font01, background_color = '#4B3619')
inp01 = sg.Input('', size = (1,None), font = font01, key = 'INP_01')
btn01 = sg.Button('Guess', size = (10,2), key = 'BTN_01')
txt04 = sg.Text(f'\n\nYou have {guesses} left', font = font01, background_color = '#4B3619')

layout_frm_1 = [[img01], [txt01, txt02], [txt_empty], [txt03, inp01], [txt_empty2], [btn01], [txt04]]
frm01 = sg.Frame('', layout_frm_1, visible = True, size=(1920,1080), element_justification = 'c', background_color = '#4B3619', key = 'FRM_1')

layout = [[frm01]]

guessed_letters = []


window = sg.Window('', layout, element_justification='c', background_color = '#4B3619').Finalize()
window.Maximize()

while True:
    event, values = window.read()
    
    if event == 'BTN_01':
        guessed_l = values['INP_01']
        
        # Check to see if the letter is already being used
        if guessed_l in guessed_letters:
            sg.popup('You have already tried this letter', text_color='black', background_color = '#cba331', font = font01)
            continue
        
        guessed_letters.append(guessed_l)

        # Check if the letter is in the word
        if guessed_l in word_random:
            letter_display = ''
            # Update the txt02 with either an empty space or a guessed letter
            for letter in word_random:
                if letter in guessed_letters:
                    letter_display += letter + ''
                else:
                    letter_display += '_ '
            txt02.update(letter_display)
            
            # Check if there are spaces left. If not - The player wins
            if '_ 'not in letter_display:
                sg.popup('You win!', text_color='black', background_color = '#cba331', font = font01)
                break
        
        else:
            # Making a statement if the letter is incorrect
            guesses -= 1
            sg.popup('Wrong Guess!', text_color='black', background_color = '#cba331', font = font01)
            txt04.update(f'\n\nYou have {guesses} left')
            
            # if there are no more guesses left, the player looses
            if guesses == 0:
                sg.popup(f'You lose! The word was {word_random}', text_color='black', background_color = '#cba331', font = font01)
                break
    
    elif event == sg.WINDOW_CLOSED:
        break

window.close()
