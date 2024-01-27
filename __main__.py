#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Oliver "oz" Z.
Description:
    Interactive ogre doctor
'''

import random

class State:
    def __init__(self, onn, tuu, image=None, options=None):
        self.onn = onn
        self.tuu = tuu
        self.image = image
        if options:
            self.options = options
        else:
            self.options = []

class Option:
    def __init__(self, text, nextState):
        self.text = text
        self.nextState = nextState

intro_image = """     WELCOME TO THE OGRE CLINIC! We are your certified doctor, Onn and Tuu!
----------------------------------:---------------------------------------------
--------------------------------:   .-------------------------------------------
--------=*@#=------------------.      ====----------=-----===========-----------
-------+@*#*%*--------------==+-::::=++++++=--------++===+++++++++++++==--+=----
-----=#%=---=#%+----------=++++++++++++++++++=------=+++++++++++++++++++==+=----
----+@*-------=#%=-------=++++++++-..=++++++++=-----=+++++==-++++--++++++++=----
---*#*++*++****+*#-------+++++++++  --+++++++++-----=+++++--.+++= +=+++++++-----
---#=+=-=:      +*-------++++++++++==++++++++++=----+++++++++++++++++++++++-----
---+*=++=:.++=. #+-------++++++++++++++++++++++=---=+++++++++++++++++++++++-----
---+#  . :-.   .#=-------+++++++++++++++++##++++---=++++*++++++++++++**+++=-----
---+#  :=- ===::#--------=++++##*+++++++*%@*++++===+++++%@#****++*#@@##+++------
---*+ --+-=: :.:#---------=+++*#%%%%%%%%%#*+++++++++++++-:*####%%#*=.=+++=------
---*+     . -#=-#---------==+++++++++++++++++++++++++++++++++++++++++++++==-----
---+*==-------=+*-------=+++++++++++++++++++++++++++++++++++++++++++++++++++==--
----===========+=----==++++++++++++++++++++++++++++++++++++++++++++++++++++++++="""
lollipop_image = """--------------------------------------------------------------------------------
----------------------------------=+++++++==------------------------------------
--------------------------------+%#+==---==*%#+=--------------------------------
--------------------------------%*-##==+**%*--+%#=------------------------------
-------------------------------+%.+# .=++=--+%*-#%=-----------------------------
-------------------------------*% #* =%=.=%+  ##.##-----------------------------
-------------------------------*% *% .+#+ -%. =%:=#-----------------------------
-------------------------------=%-.*#+--:-*%.:%+ #*-----------------------------
--------------------------------#%=  ::---- -%* +%+-----------------------------
--------------------------------*%%##++===*%+-:+%*------------------------------
--------------------------------+%%#-:...:-=+#%*=-------------------------------
-----------------------------=*@@*=++******++=----------------------------------
----------------------------*@@*=-----------------------------------------------
---------------------------%@*=-------------------------------------------------
---------------------------==---------------------------------------------------"""

# https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'
colors = [bcolors.OKBLUE, bcolors.OKCYAN, bcolors.OKGREEN, bcolors.WARNING, bcolors.FAIL]

def skip_first_line(image):
    return "\n".join(image.split("\n")[1:]) # Cut intro text
def drugs(image):
    new_image = ""
    for c in image:
        color = random.choice(colors)
        if c != '\n':
            new_image += f"{color}{c}"
        else:
            new_image += '\n'
    new_image += f"{bcolors.ENDC}"
    return new_image

MANIFEST = {
    "end": State("Alrighty, see you next time!", "Hehe.."),
    "hand_lollipop": State("Here you go...", "...anything else?", lollipop_image, [
        Option("Yummy, thanks! But I need MORE!", "intro"),
        Option("Thanks, see you!", "end")
    ]),
    "hand_plaster": State("We are out of plasters, sorry.", "Onn ate the last pack. Anything else?", None, [
        Option("Okay, there's another thing I need help with...", "intro"),
        Option("I'll try a different doctor, thanks...", "end")
    ]),
    "hand_drugs": State(drugs("Yeah?"), drugs("Yeah!"), drugs(skip_first_line(intro_image)), [
        Option(drugs("Yeah?"), "intro"),
        Option(drugs("Yeah!"), "end")
    ]),
    "orcish": State("ZUG ZUG KEK!", "Lok'tar Ogar!", None, [
        Option("ZUG ZUG", "intro"),
        Option("ZUG ZUG", "intro"),
        Option("NO MORE ZUG", "end")
    ]),
    "intro": State("Unfortunately our GUI broke, so you have to deal with the teleph...err CLI.", "How may we help you?", None, [
        Option("My warhammer broke.", "ogre_forge_ad"),
        Option("I need a plaster.", "hand_plaster"),
        Option("I need a lollipop.", "hand_lollipop"),
        Option("UUUGGA BOOGA ZUG ZUG KEK", "orcish"),
        Option("Just give me the good stuff, please!", "hand_drugs"),
        Option("Actually, I'm fine. Thank you!", "end"),
    ]),
    "ogre_forge_ad": State("Fortunately, we also run a forge...", "...come visit us at https://oliz.io/ogre-forge/", None, [
        Option("I need more help!", "intro"),
        Option("Thanks, I'll pay you a visit!", "end")
    ]),
}

def main():
    print(intro_image)
    state_id = "intro"
    while (not state_id.startswith("end")):
        print_state(state_id)
        choice = get_input()
        state_id = input2next_state(state_id, choice)
    print_state(state_id)

def print_state(state_id):
    print("")
    state = MANIFEST[state_id]
    if state.image:
        print(state.image)
    if len(state.onn):
        print(f"""O: {state.onn}""")
    if len(state.tuu):
        print(f"""T: {state.tuu}""")
    if len(state.options):
        print("")
        print_options(state.options)
        print("")

def print_options(options):
    idx = 1
    for option in options:
        print(f"""  {idx}: {option.text}""")
        idx += 1

def get_input():
    choice = 1
    try:
        choice = int(input("Your choice: "))
    except ValueError:
        choice = 1
    choice -= 1
    return choice

def input2next_state(current_state_id, choice):
    state = MANIFEST[current_state_id]
    nr_options = len(state.options)
    if (choice >= nr_options):
        choice = nr_options - 1
    if (choice < 0):
        choice = 0
    return state.options[choice].nextState

if __name__ == "__main__":
    main()
