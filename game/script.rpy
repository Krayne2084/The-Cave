# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define b = Character("You")
define g = Character("Girl")

define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')

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

C "I hope you're not flirting with me."
player "Haha no sorry. I'm just relieved to not be the only one here and it's nice that we have two heads to work with and I just ramble nonsense to calm nerves. It happens, y'know?"
C "Hmmm{cps=2}...{/cps}{w=0.5} Alright then?"

C "So what do you make of this?"
player "Looks like some sort of cave?"
C "Looks? {w}Haha Mr. Funny Man."
player "Figure of speech! You know what I mean..."
C "{cps=4}Mhm...{/cps}{w=1} Anyways, how do we get out? {p}No use sitting here and waiting. Even if anyone knows we're missing I'm not even sure they can reach us wherever we are."
player "{i}What to do?{/i}"

menu:
    "Check your Pockets":
        jump choice2_pockets
    
    "Find the cave wall":
        jump choice2_wall

label choice2_pockets:
    player "*pats pockets*{p}*rummages through waist pouch*"
    C "Watcha doin' there bud?"
    player "Checkin' if I got anythin' useful on me"
    C "Ah! Good call. {size=-18}Why didn't I think of that?{/size}"
    "Charlotte feels through her pockets and examines the contents of her pouch. She manages to pull out a lighter from the inner pocket of her pouch." 
    "She ignites her lighter.{nw}"
    with flashbulb
    "*Fwoosh*"
    C "OH GOSH!"
    player "*Flinches* \n What!?! What happened?!"
    C "O-oh no it's uh.. I just wasn't expecting to see you right away haha."
    player "Are{cps=4}...{/cps}{w=0.25} Are you callin' me ugly?"
    C "No no, not at all" 
    C "*Coughs*" 
    C "Anyways, looks like this is all I have, everything else must've fallen out. You got anything useful?"
    "You rummage through your own pouch and pull out an item."
    player "How's a pocket knife sound?"
    C "Better than nothing. At least it's a start."
    jump choice2_done

label choice2_wall:
    "You decide to walk forward in hopes of bumping into something. The tip of your shoe manages to make contact with something rough and sturdy. You trail your hand across the surface."
    player "Hey, Charlotte!"
    C "Yeah?"
    player "I managed to find a wall. Follow my voice! Maybe we can follow this wall outta here."
    C "Are you serious? It's pitch black! My ears aren't that good y'know."
    player "You can stay there if you reaalllly want to." 
    player "*pretends to walk away*"
    extend "\n*step*{w=1}\n*step*{w=1}\n*step*"
    C "NO, wait for me!!" 
    "In a sudden panic, thinking she would be left behind, Charlotte blindly runs in the direction where she last heard [player]'s voice."

label choice2_done:

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
