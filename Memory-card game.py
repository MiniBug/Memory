# implementation of card game - Memory
# created by FF on 03/05/14

import simplegui
import random

HEIGHT = 100
WIDTH = 800
whole_deck = []
exposed = []
card1_pos, card2_pos = 0, 0
state = 0
turns = 0


# helper function to initialize globals
def new_game():
    global whole_deck, exposed, turns
    global turns
    turns = 0
    deck_A = range(0,8)
    deck_B = range(0,8)
    whole_deck = deck_A + deck_B
    random.shuffle(whole_deck)
    exposed = [False] * 16
    label.set_text("Turns = " + str(turns))
 
# define event handlers
def mouseclick(pos):
    
    # add game state logic here
    global state, card1_pos, card2_pos, turns
    clicked_card_pos = pos[0] // 50
    if state == 0:
        card1_pos = clicked_card_pos
        exposed[card1_pos] = True
        state = 1
    elif state == 1:
        if exposed[clicked_card_pos] == False:
            card2_pos = pos[0] // 50
            exposed[card2_pos] = True
            state = 2
            turns += 1
    elif state == 2:
        if exposed[clicked_card_pos] == False:
            if whole_deck[card1_pos] == whole_deck[card2_pos]:
                pass
            else:
                exposed[card1_pos], exposed[card2_pos] = False, False
            card1_pos = clicked_card_pos
            exposed[card1_pos] = True
            state = 1
    label.set_text("Turns = " + str(turns))
            
    
    
def draw(canvas):
    for icrmnt in range(16):
        if exposed[icrmnt] == False:   
            canvas.draw_polygon([(icrmnt*50, 0), (icrmnt*50+50, 0),
                                 (icrmnt*50+50, 100), (icrmnt*50,100)], 1, 'orange', 'green')
        else:
            canvas.draw_text(str(whole_deck[icrmnt]),
                             ((50*icrmnt+12.5),60), 48, "white")
    
       
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric