# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define b = Character("You")
define g = Character("Girl")

label start:

scene bg darkness

b "{i}Uugghhh my head..."
b "{i}Feels like I got hit by a semi..."
b "{i}Where am I? Why can't I see nothing?"
"{cps=15}*Rocks Shifting*"
b "{i}The hell was that?"
menu:
    "Call out":
        jump choice1_call

    "Throw Rock":
        jump choice1_throw

label choice1_call:
    b "Anybody there?"
    g "Oh thank God it's another person!"
    jump choice1_done

label choice1_throw:
    b "{i}If it's some kind of animal or creature, I'd better throw something far away to not draw attention to my position.{/i}"
    "*Throws*{p}*Clatters*"
    g "{size=+20}EEEEP{/size}"
    b "A girl?{p}Hello?{w} Sorry if I scared you, I didn't know you were a person."
    b "What's your name?"
    jump choice1_done

label choice1_done:

g "My name is Charlotte! I'm so glad I'm not alone! Unless you're a bad guy! Are you a bad guy? What's your name?"

define C = Character("Charlotte")

b "Whoa easy there, I'm not a bad guy haha"
b "You're real rapid-fire ain't ya?"

python:
    name = renpy.input("My name is:")

    name = name.strip() or "Adam"

define player = Character("[name]")

player "My name is [name]. Nice to meet you [C],{w} I'm sure you look lovely through all this darkness haha"

return

# The game starts here.

# label start:

#     # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.

#     scene bg room with Pause(3)

#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "eileen happy.png" to the images
#     # directory.

#     show eileen happy

#     # These display lines of dialogue.

#     e "You've created a new Ren'Py game."

#     e "Once you add a story, pictures, and music, you can release it to the world!"

#     # This ends the game.

#     return
