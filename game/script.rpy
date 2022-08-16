# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define b = Character("You")
define g = Character("Girl")

transform right:
    ypos 0.15
    yanchor 0
    xanchor 0.5
    xpos 0.85

define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')

screen inventory_bar(bag = []):
    $ Bag = bag
    frame:
        xalign 0 ypos 0

        has hbox spacing 20
        text "Inventory:"
        for i in Bag:
            if i != "":
                use item(i)

screen item(item_name):
    text "[item_name]" xalign 0

label start:

python:
    minor_injuries_C = 0
    minor_injuries_p = 0
    majour_injuries_C = 0
    majour_injuries_p = 0
    artifact_found = False
    artifact_have = False

$ bag = []

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
    $ pockets = True
    show screen inventory_bar(bag = bag)
    player "*pats pockets*{p}*rummages through waist pouch*"
    C "Watcha doin' there bud?"
    player "Checkin' if I got anythin' useful on me"
    C "Ah! Good call. {size=-18}Why didn't I think of that?{/size}"
    jump get_lighter
    

label choice2_wall:
    $ pockets = False
    "You decide to walk forward in hopes of bumping into something. The tip of your shoe manages to make contact with something rough and sturdy. You trail your hand across the surface."
    player "Hey, Charlotte!"
    C "Yeah?"
    player "I managed to find a wall. Follow my voice! Maybe we can follow this wall outta here."
    C "Are you serious? It's pitch black! My ears aren't that good y'know."
    player "You can stay there if you reaalllly want to." 
    player "*pretends to walk away*"
    extend "\n*step*{w=1}\n*step*{w=1}\n*step*"
    C "NO, wait for me!!" 
    "In a sudden panic, Charlotte blindly runs in the direction where she last heard [player]'s voice."
    $ minor_injuries_C = minor_injuries_C + 1

    "Charlotte, oblivious that her shoelace was undone the whole time, steps on the lace and lifts her other foot. She stumbles and lands on her knees, scraping them on the cold rugged ground. The impact of her fall echoes around the cave walls."
    C "Owwww... That was stupid."
    player "Are you okay?? That didn't sound too good."
    C "*Whimpers* {p}I-it's fine. Just gotta shake it off. It's just a scrape."
    "Charlotte slowly rises and brushes the dust and dirt of her scout uniform."
    player "Are you feelin' up to it? We can rest up a bit first if you're not ready to be walkin' around."
    C "No no, I can do it. Plus, we can prob'ly find a place to wash my cuts. That'd be something to look forward to."
    jump get_lighter

label get_lighter:
    "Charlotte feels through her pockets and examines the contents of her pouch."

    if pockets:
        extend " She manages to pull out a lighter from the inner pocket of her pouch."
    else:
        player "What's all that rustlin'?"
        C "I'm seeing if I got anything useful before I start wanderin' in this pitch blackness again."
        player "{i}That's a bright idea{cps=4}...{/cps}{p}Good thing I didn't say that aloud."
        "Charlotte pulls out a lighter from the ineer pocket of her pouch."

    "*click*{p}*click*{p}*Fwo{nw}"

    show soul idle at right with flashbulb
    
    extend "osh*"

    hide screen inventory_bar
    $ bag.append("Lighter")
    show screen inventory_bar(bag = bag)

    C "OH GOSH!"
    player "*Flinches* \n What!?! What happened?!"
    C "O-oh no it's uh.. I just wasn't expecting to see you right away haha."
    player "Are{cps=4}...{/cps}{w=0.25} Are you callin' me ugly?"
    C "No no, not at all" 
    C "*Coughs*" 
    C "Anyways, looks like this is all I have, everything else must've fallen out. You got anything useful?"
    "You rummage through your own pouch and pull out an item."

    hide screen inventory_bar
    $ bag.append("Pocketknife")
    show screen inventory_bar(bag = bag)

    player "How's a pocket knife sound?"
    C "Better than nothing. At least it's a start."
    jump choice2_done

label choice2_done:
"Charlotte walks towards [player] with her lighter in hand. She moves it around the cave to light up some of the space around them."
C "Totally not creepy at all. Perfectly normal don't ya think?"
player "Yep. Perfectly normal considering we've been knocked out for who knows how long and didn't die from any random creatures lurkin' about. Oh shoot, I'm ramblin' again."
C "Pfft. No worries, makes sense. I'd be rambling too if I we didn't have this lighter."

"The two follow a dimly lit path. As they shuffle in the dark, they come across what they assumed to be a large cavern to their left. The lighter flickers and sways."
C "Airflow? Good news! We're not as deep as I thought we were then, eh?"
player "Sounds about right? So airflow means there's an exit somewhere or somethin' right?"
C "I mean, it's possible. Not too sure tho- {w=0.5}Oh hey look over there!"
"Charlotte points to a crevice a few meters ahead of them."
C "It looks big enough for both of us to shimmy through! Maybe that's where the air current is coming from. Worth a shot right?"

menu:
    "Shimmy through the crevice":
        jump choice3_crevice

    "Explore the area":
        jump choice3_cavern

label choice3_crevice:
    player "Like you said, worth the shot so let's try it!"
    "The two of you walk up to the crevice and Charlotte gives you her lighter and gestures to the crevice"
    C "Lead the way~"
    "You begin to side step into the narrow entrance, arm outstretched for an optimal view of the path."
    player "Damn, this shimmy session is gonna be longer than I thought it'd be."
    C "Wha?? You gotta be kidding me. I haven't even step in yet and I'm already exhausted from hearing you say that."
    player "You say that as if you're not gonna be in here soon haha."
    C "Ughhh."
    "Charlotte follows behind you while you wait for her to catch up."
    player "Never thought I'd be shimmyin' today. I shoulda stretched first haha."
    C "Honestly... same. I'm stiff as a rusty door."

    if minor_injuries_C>0 or majour_injuries_C>0:
        C "I'd be more limber if only SOMEONE didn't pretend to abandon me earlier."
        C "*Glares*"
        player "*Whistles*\n*Avoids eye contact*"

    "You and Charlotte are almost out of the crevice and suddenly, you feel the world shake. It wouldn't have been a big deal, until you hear crackles of stones and the walls behind Charlotte start to break down."
    player "{size=+20}LET'S HURRY AND MOVE IT. DON'T LOOK BACK."
    C "Wha-{p}*looks back*{w=0.5}\nCrap, {size=+10}{w=0.25}crap, {size=+10}{w=0.25}CRAP {size=+20}{w=0.25}MOVEEE!!{/size}"
    "Both of you shimmy as quick as you can without blowing the lighter's flame out. You finally reach the crevice's exit. You take Charlotte's hand and pull her out before the rubble could get to her."
    C "*Huff*{w=0.8} *Huff*{w=1}\nYeah, let's not do that again. {w}No more crevices."
    player "*Huff*{w=0.8} *Huff*{w=1}\nI second that."
    C "Never thought I'd experience an earthquake like that. {p}*stretches*{w=1} \nWhere are we now?"
    player "*moves lighter around*{p}Another cavern I think."
    C "Hey [player], move the lighter to the right would ya? I think I saw something."
    "You move the lighter and see a lump on a large stone slab."
    player "No way."
    player "It's my bag! Now that's what I'm talkin' about!"
    C "Finally some good news. What's inside?"
    player "Lemme show ya."
    "You give the lighter back to Charlotte to hold and open the flap of your bag. In it are some snacks and a half empty water bottle. {w}Nothing too exciting until you pull out a bundle of paracord and your half-finished wooden statue."
    
    hide screen inventory_bar
    $ bag.append("Paracord (80m)") 
    $ bag.append("Half-finished Wooden Statue")
    show screen inventory_bar(bag = bag)

    player "It don't look like much but hey, it's a good start."
    C "You carve things? Oh! That would explain your pocket knife huh?"
    player "Yeah, very perceptive of you."
    C "*Shrugs* I try."
    "You sling the bag onto your back"

    jump choice3_done

label choice3_cavern:
    "You scratch your chin, debating on which option would help you two the best."
    player "Let's check the cavern first. It'd be a waste to not investigate."
    
    if minor_injuries_C > 0 or majour_injuries_C > 0:
        player "And hey, maybe we can find something to treat your wounds right? Win-win for you~"
        C "Awww, are you worried about me? If you're worried you coulda just said so."
        player "Look who's flirting now."

    "Charlotte hands you her lighter and you walk into the open area. With no walls in arm's reach, you can only imagine the amount of space to tread in order to find something of use."
    C "Still not much to look at with just the a small lighter huh? It's better for us to stick together while we scan around."
    player "Agreed."
    "The two of you stand side by side, Charlotte scanning the right side of the cavern and you taking the left. You both move slowly and carefully."
    player "*squints*{p}I think I see something."
    C "Where?"
    "You point to a round shape on the ground, dimly lit but visible enough to see its distinct pattern against the coal-coloured ground."
    C "Is that what I think it is??"
    "Charlotte starts to move towards the object."
    player "Careful! Don't run off too far- {w=0.5}\nA bag?"
    C "Yeah, it's mine... {w}How'd it even get here?"
    player "Beats me. What do you have in there?"
    C "Let's see, hopefully nothing too important fell out."
    "Charlotte unzips the pockets of her backpack, uncovering essential snacks and water for for the scout's adventuring. You catch a glimpse of a small box in the front pocket of her bag."
    player "What's that?"
    C "*Pulls out a first aid kit*"

    hide screen inventory_bar
    $ bag.append("First Aid Kit")
    show screen inventory_bar(bag = bag)

    extend "Oh wait, there's more!" 
    C "*Pulls out a flashlight*{p}This'll really brighten things up!"

    if minor_injuries_C>0 or majour_injuries_C>0:
        C "Wow, you weren't kidding when you said it was a win-win!" 
        player "I honestly didn't think that win-win moment would come now, but might as well get you patched up."
        "You use the newly acquired flashlight to help Charlotte assess her injuries."
        player "*chokes* I thought you said it was a scrape?! {w}That doesn't look like 'just a scrape' to me."
        C "Sure felt like a scrape. Can't change the past now."
        "You look away, feeling a bit queasy, while Charlotte focuses on disinfecting and wrapping her wounds."
        C "All good to go!"
        player "*Trying not to gag* {p}Mhm *Thumbs up*"
    else:
        player "Keep that first aid kit close. Who knows if we'll need it down the line."
        C "No need to tell me twice. Also, don't jinx it! I really wouldn't want to be forced to use    it." 
        "Charlotte drops the first aid kit in her bag, zips it closed, and slings it on her back."


    jump choice3_done

label choice3_done:

return

# The game starts here.

# label start:

#     # Show a background. This uses a placeholder by right, but you can
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
