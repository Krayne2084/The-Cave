# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#CHARACTERS
define e = Character("Eileen")
define b = Character("You")
define g = Character("Girl", color='#0f0')

#IMAGES
image charlotte idle = "charlotte neutral.png"

#TRANSFORMS
transform character_right:
    yalign 1
    xanchor 0.5
    xpos 0.85
    zoom 0.35

transform character_shake_right:
    zoom 0.35
    xanchor 0.5
    linear 0.05 xpos 0.84
    linear 0.05 xpos 0.85

    repeat

transform character_fall_down:
    zoom 0.35
    xanchor 0.5
    linear 0.05 ypos 2.0

transform shake_bg_mid:
    linear 0.05 ypos 0.52
    linear 0.05 ypos 0.5
    repeat

transform bg_shake_bottomish:
    linear 0.05 ypos 0.77
    linear 0.05 ypos 0.75
    repeat

transform bg_shake_exit:
    linear 0.05 ypos 0.72
    linear 0.05 ypos 0.7
    repeat

transform bg_top:
    yalign 0

transform bg_topish:
    yalign 0.25

transform bg_mid:
    yalign 0.5

transform bg_bottomish:
    yalign 0.75

transform bg_bottom:
    yalign 1.0

transform bg_exit:
    yanchor 1.0
    ypos 0.7

#EFFECTS
define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
define hurt_flash = Fade(0.2, 0.0, 0.8, color='#f00')    

#SCREENS
screen inventory_bar():
    frame:
        xalign 0 ypos 0

        has hbox spacing 20
        text "Inventory:":
            xalign 0
            yalign 0.5
        for i in bag:
            if i != "":
                use item(i)

screen item(item_pic):
    add item_pic.icon:
        xalign 0 
        zoom 0.05

#PYTHON
init python:
    class Item:
        def __init__(self, name, icon):
            self.name = name
            self.icon = icon
        
        def add_to_bag(self):
            renpy.hide_screen("inventory_bar")
            bag.append(self)
            renpy.show_screen("inventory_bar")
            renpy.notify("You have obtained " + self.name)
            renpy.play("audio/ding-36029.mp3", "sound")

        def use(self):
            bag.remove(self)
            renpy.notify("You have used " + self.name)
            renpy.play("audio/foley_zip_zipper_long_05.wav", "sound")
    
    class Sound:
        def __init__(self):
            self

        def run(self):
            renpy.play("audio/footstep_gravel_run_13.wav", "sound")
            renpy.sound.queue("audio/footstep_gravel_run_14.wav", "sound")
            renpy.sound.queue("audio/footstep_gravel_run_11.wav", "sound")
            renpy.sound.queue("audio/footstep_gravel_run_13.wav", "sound")
            renpy.sound.queue("audio/footstep_gravel_run_11.wav", "sound")

        def walk_loop(self):
            renpy.play("audio/footstep_gravel_walk_11.wav", "sound", relative_volume = 0.3)
            renpy.sound.queue(["audio/footstep_gravel_walk_10.wav", "audio/footstep_gravel_walk_11.wav"], "sound", loop = True, relative_volume = 0.3)

    renpy.music.register_channel("music_overlay", "music")

#START
label start:

python:
    injuries_C = 0
    injuries_player = 0
    artifact_have = False
    bag = []
    
    #ITEMS
    lighter = Item("Lighter", "item lighter.png")
    firstaidkit = Item("First Aid Kit", "item firstaid.png")
    paracord = Item("Paracord (80m)", "item paracord.png")
    pocketknife = Item("Pocketknife", "item pocketknife.png")
    statue = Item("Half-Finished Wooden Statue", "item woodenstatue.png")
    flashlight = Item("Flashlight", "item flashlight.png")
    knocker = Item("Large Knocker Ring", "item knockerring")
    moss = Item("Healing Moss", "item moss.png")
    stoneidol = Item("Stone Idol", "item stoneidol.png")
    lifeidol = Item("Life Idol", "item totemwhite.png")

    #SOUNDS
    Play_Sound = Sound()

scene bg darkness
play music "audio/Cave 4 Loop.wav"

b "{i}Uugghhh my head..."
b "{i}Feels like I got hit by a semi..."
b "{i}Where am I? Why can't I see nothing?"

play sound "audio/rocks-6129.mp3"

"{cps=15}*rocks shifting*{nw}"

stop sound fadeout 1
extend ""

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
    "*throws*"
    
    play sound "audio/dropping-rocks-5996.mp3"
    extend "\n*clatters*{nw}"
    stop sound fadeout 1
    extend ""

    
    
    g "{size=+20}EEEEP{/size}"
    b "A girl?{p}Hello?{w} Sorry if I scared you, I didn't know you were a person."
    b "What's your name?"
    jump choice1_done

label choice1_done:

g "My name is Charlotte! I'm so glad I'm not alone! Unless you're a bad guy! Are you a bad guy? What's your name?"

define C = Character("Charlotte", color='#0f0')

b "Whoa easy there, I'm not a bad guy haha."
b "You're real rapid-fire ain't ya?"

python:
    name = renpy.input("My name is:")

    name = name.strip() or "Adam"

define player = Character("[name]")

player "My name is [name]. Nice to meet you [C],{w} I'm sure you look lovely through all this darkness haha."

C "I hope you're not flirting with me."
player "Haha no sorry. I'm just relieved to not be the only one here and it's nice that we have two heads to work with and I just ramble nonsense to calm nerves. It happens, y'know?"
C "Hmmm{cps=2}...{/cps}{w=0.5} Alright then?"

C "So what do you make of this?"
player "Looks like some sort of cave?"
C "Looks? {w}Haha Mr. Funny Man."
player "Figure of speech! You know what I mean..."
C "{cps=4}Mhm...{/cps}{w=1} Anyways, how do we get out? {p}No use sitting here and waiting. Even if anyone knows we're missing, I'm not even sure they can reach us wherever we are."
player "{i}What to do?{/i}"

menu:
    "Check your Pockets":
        jump choice2_pockets
    
    "Find the cave wall":
        jump choice2_wall

label choice2_pockets:
    $ pockets = True
    player "*pats pockets*{p}*rummages through waist pouch*"
    C "Watcha doin' there bud?"
    player "Checkin' if I got anythin' useful on me."
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

    play sound "audio/footstep_gravel_walk_11.wav"
    extend "\n*step*{w=1}{nw}"
    queue sound "audio/footstep_gravel_walk_11.wav"
    extend "\n*step*{w=1}{nw}"
    queue sound "audio/footstep_gravel_walk_11.wav"
    extend "\n*step*"
    

    C "NO, wait for me!!" 
    
    $ Play_Sound.run()

    "In a sudden panic, Charlotte blindly runs in the direction where she last heard [player]'s voice."
    "Charlotte, oblivious that her shoelace was undone the whole time, steps on the lace and lifts her other foot. She stumbles and lands on her knees, scraping them on the cold rugged ground. The impact of her fall echoes around the cave walls."
    
    play sound "audio/wooden-thud-mono-6244.mp3"

    "{size=+20} *THUD*"
    
    $ injuries_C = injuries_C + 1

    C "Owwww... That was stupid."
    player "Are you okay?? That didn't sound too good."
    C "*whimpers* {p}I-it's fine. Just gotta shake it off. It's just a scrape."
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

    "*click*{p}*click*"
    
    extend "\n*FWO{nw}"

    play sound "audio/fire-39294.mp3"

    scene bg cave1_warm at bg_bottomish with flashbulb
    if injuries_C > 0:
        show charlotte injured at character_right
    else:
        show charlotte idle at character_right
    
    extend "OSH*"

    $ lighter.add_to_bag()
    
    show charlotte shocked
    C "OH GOSH!"
    player "*flinches* \n What!?! What happened?!"
    show charlotte worried
    C "O-oh no it's uh.. I just wasn't expecting to see you right away haha."
    player "Are{cps=4}...{/cps}{w=0.25} Are you callin' me ugly?"
    C "No no, not at all." 
    C "*coughs*"
    show charlotte idle
    C "Anyways, looks like this is all I have, everything else must've fallen out. You got anything useful?"
    "You rummage through your own pouch and pull out an item."

    $ pocketknife.add_to_bag()

    player "How's a pocket knife sound?"
    C "Better than nothing. At least it's a start."
    jump choice2_done

label choice2_done:
"Charlotte walks towards [player] with her lighter in hand. She moves it around the cave to light up some of the space around them."
C "Totally not creepy at all. Perfectly normal don't ya think?"
player "Yep. Perfectly normal considering we've been knocked out for who knows how long and didn't die from any random creatures lurkin' about. Oh shoot, I'm ramblin' again."
C "Pfft. No worries, makes sense. I'd be rambling too if I we didn't have this lighter."

"The two follow a dimly lit path. As they shuffle in the dark, they come across what they assumed to be a large cavern to their left. The lighter flickers and sways."
C "Airflow? {w=0.5}{nw}"

show charlotte happy

extend "Good news! We're not as deep as I thought we were then, eh?"
player "Sounds about right? So airflow means there's an exit somewhere or somethin' right?"

show charlotte idle

C "I mean, it's possible. Not too sure tho- {w=0.5}{nw}"

show charlotte happy

extend "Oh hey look over there!"
"Charlotte points to a crevice a few meters ahead of them."
C "It looks big enough for both of us to shimmy through! Maybe that's where the air current is coming from. Worth a shot right?"

menu:
    "Shimmy through the crevice":
        jump choice3_crevice

    "Explore the area":
        jump choice3_cavern

label choice3_crevice:
    player "Like you said, worth the shot so let's try it!"
    "The two of you walk up to the crevice and Charlotte gives you her lighter and gestures to the crevice."
    C "Lead the way~"

    hide charlotte

    "You begin to side step into the narrow entrance, arm outstretched for an optimal view of the path."
    
    scene bg crevice_edit_warm at bg_mid with dissolve
    
    player "Damn, this shimmy session is gonna be longer than I thought it'd be."
    
    show charlotte worried at character_right
    
    C "Wha?? You gotta be kidding me. I haven't even stepped in yet and I'm already exhausted from hearing you say that."
    player "You say that as if you're not gonna be in here soon haha."
    C "Ughhh."
    show charlotte idle
    "Charlotte follows behind you while you wait for her to catch up."
    player "Never thought I'd be shimmyin' today. I shoulda stretched first haha."
    C "Honestly... same. I'm stiff as a rusty door."

    if injuries_C > 0:
        C "I'd be more limber if only SOMEONE didn't pretend to abandon me earlier."
        show charlotte annoyed
        C "*glares*"
        player "*whistles*\n*avoids eye contact*"
        hide charlotte

    "You and Charlotte are almost out of the crevice and suddenly, you feel the world shake.{nw}"
    
    show bg at shake_bg_mid
    play music_overlay "audio/earth-rumble-6953.mp3"
    
    extend "{w=1} It wouldn't have been a big deal, until you hear crackles of stones and the walls behind Charlotte start to break down."
    player "{size=+20}LET'S HURRY AND MOVE IT. DON'T LOOK BACK."
    
    show charlotte worried at character_right

    C "Wha-{p}*looks back*{w=0.5}{nw}"
    
    show charlotte shocked

    extend "\nCrap, {size=+10}{w=0.25}crap, {size=+10}{w=0.25}CRAP {size=+20}{w=0.25}MOVEEE!!{/size}"
    "Both of you shimmy as quick as you can without blowing the lighter's flame out. You finally reach the crevice's exit. You take Charlotte's hand and pull her out before the rubble could get to her."
    
    show bg at bg_mid
    stop music_overlay fadeout 3
    play sound "audio/stones-falling-6375.mp3" volume 0.7
    
    show charlotte worried
    C "*huff*{w=0.8} *huff*{w=1}\nYeah, let's not do that again. {w}No more crevices."
    player "*huff*{w=0.8} *huff*{w=1}\nI second that."
    C "Never thought I'd experience an earthquake like that."

    show charlotte idle

    extend "\n*stretches*{w=1} \nWhere are we now?"
    player "*moves lighter around*{p}Another cavern I think."
    C "Hey [player], move the lighter to the right would ya? I think I saw something."
    "You move the lighter and see a lump on a large stone slab."
    player "No way."
    player "It's my bag! Now that's what I'm talkin' about!"
    C "Finally some good news. What's inside?"
    player "Lemme show ya."
    "You give the lighter back to Charlotte to hold and open the flap of your bag. In it are some snacks and a half empty water bottle. {w}Nothing too exciting until you pull out a bundle of paracord and your half-finished wooden statue.{w}{nw}"
    
    $ paracord.add_to_bag()
    extend ""    
    $ statue.add_to_bag()
    extend ""

    player "It don't look like much but hey, it's a good start."
    
    show charlotte happy
    
    C "You carve things? Oh! That would explain your pocket knife huh?"
    player "Yeah, very perceptive of you."

    show charlotte idle

    C "*shrugs* I try."
    "You sling the bag onto your back and Charlotte returns the lighter to you."
    player "Let's keep goin'."

    jump choice3_done

label choice3_cavern:
    show charlotte idle
    
    "You scratch your chin, debating on which option would help you two the best."
    player "Let's check the cavern first. It'd be a waste to not investigate."
    
    if injuries_C > 0:
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
    
    show charlotte happy
    
    C "Is that what I think it is??"

    hide charlotte

    "Charlotte starts to move towards the object."
    player "Careful! Don't run off too far- {w=0.5}\nA bag?"
    C "Yeah, it's mine... {w}How'd it even get here?"
    player "Beats me. What do you have in there?"

    show charlotte idle at character_right

    C "Let's see, hopefully nothing too important fell out."
    "Charlotte unzips the pockets of her backpack, uncovering essential snacks and water for for the scout's adventuring. You catch a glimpse of a small box in the front pocket of her bag."
    player "What's that?"
    C "*pulls out a first aid kit*"

    $ firstaidkit.add_to_bag()

    extend  "\nKinda empty but we can still make do with it. Oh wait, there's more!"
    
    show bg cave1_lit
    $ flashlight.add_to_bag()
    
    C "*pulls out a flashlight*"
    
    show charlotte happy
    
    extend "\nThis'll really brighten things up!"

    if injuries_C > 0:
        C "Wow, you weren't kidding when you said it was a win-win!" 
        player "I honestly didn't think that win-win moment would come now, but might as well get you patched up."
        "You use the newly acquired flashlight to help Charlotte assess her injuries."
        player "*chokes* I thought you said it was a scrape?! {w}That doesn't look like 'just a scrape' to me."
        
        show charlotte idle
        
        C "Sure felt like a scrape. Can't change the past now."
        "You look away, feeling a bit queasy, while Charlotte focuses on disinfecting and wrapping her wounds."
        
        show charlotte happy
        $ injuries_C = injuries_C - 1
        $ firstaidkit.use()    

        C "All good to go!"
        player "*trying not to gag* {p}Mhm *thumbs up*"

    else:
        show charlotte idle
        player "Keep that first aid kit close. Who knows if we'll need it down the line."
        C "No need to tell me twice. Also, don't jinx it! I really wouldn't want to be forced to use it." 
        "Charlotte drops the first aid kit in her bag, zips it closed, and slings it on her back."

    "The two of you start to walk back towards the crevice."

    show bg at bg_shake_bottomish
    play music_overlay "audio/earth-rumble-6953.mp3"

    show charlotte shocked
    
    "An unexpected rumble startles you both as you scramble to hug the walls for stability."
    
    stop music_overlay fadeout 3
    play sound "audio/stones-falling-6375.mp3" volume 0.7
    show bg at bg_bottomish
    show charlotte worried

    "Now that Charlotte has a flashlight, you can clearly see the stone ceiling above the crevice crumble and fall, sealing off your intended path."
    
    player "Well, uh, looks like that's not an option anymore?"
    C "*moves her flashlight around*"
    
    show charlotte idle

    extend "\nHaha, you know what they say. When one door closes, another opens and well, something did open."
    "You follow the direction of her flashlight and see a broken wall on the other side of the cavern. You walk towards and and see a path to who knows where. You look at each other."
    C "Any other options?"
    player "Nope."

    jump choice3_done

label choice3_done:

hide charlotte

"The path felt like a long one. No unexpected twists and turns, but seemed never ending."

$ Play_Sound.walk_loop()

"You two walked in silence, not because of the exhaustion of it all nor the fear of mundane conversation, but to recollect your thoughts and take the time to breathe."
"After what seemed like an hour, you finally reach a large open area. It's been a while since you've been in a well lit room and you finally get a glimpse of your surroundings."

stop sound fadeout 1
scene bg largecavern1 at bg_bottomish with dissolve
play music_overlay "audio/water-drops-6223.mp3"

"This cavern is significantly larger than the one you passed earlier."
"The hole in the ceiling conveniently lights the majority of the cavern. In front of you is a pool of water with another area, unfortunately still shadowed in darkness, on the other side with what looks to be a possible exit."

show charlotte happy at character_right

C "Oh my gosh, light! {nw}"

if flashlight in bag:
    extend "*turns off flashlight* {nw}"

extend "Nice to know we're at least near the surface. Maybe someone will be nearby when we reach an exit."
player "That'd be a convenient coincidence now wouldn't it. *turns off lighter*" 
"Charlotte scans around the area and notices something up ahead."

show charlotte idle

C "Speaking of people, I think I see something over there."
player  "{cps=200}*jumps*{w=0.5}\nW-What!?!{w=0.5} Where?!{w=0.5} A person?!{/cps}"
C "Oh whoops! I meant these."
"Charlotte walks you to one of the cave walls and points to what looks to be a series of bronze objects protruding from the walls."
player "Charlotte, please be more specific. I almost had a heart attack thinking you saw some stranger. I welcome help but who knows what type we'll meet in the middle of a cave?"
player "No offense."
C "None taken."
C "But yeah sorry, these pitons are pretty clear evidence of people before us. Maybe longer ago than we thought though."
player "*looks up*\nLook, there's a ledge with an opening up there too! Could be a way to an exit. Maybe we can use them to climb up!"
C "True, true. There's also that area past the water. We got some options on our hands." 

menu:
    "Climb the Wall":
        jump choice4_climb

    "Wade through the Water":
        jump choice4_water

label choice4_climb:
    player "How do you feel about climbing? I mean, if there were people that used those to climb, that seems like a good sign, dontcha think?"
    
    show charlotte happy

    C "I don't want to toot my own horn or anything but I'm pretty good at free solo haha."
    player "At what?"

    show charlotte idle

    C "Climbing without equipment."

    if paracord in bag:
        player "*pulls out paracord from bag*"
        
        $ paracord.use()

        extend"\nAlright Muscles, you think you can climb all the way up there and then send this down for me?"
        C "*stretches*\nI got this."

        if injuries_C > 0:
            show charlotte annoyed
            
            C "Of course, I'd feel more confident if my legs were in better shape but it's not like I have that luxury." 
            player "*stares* {p}You're really just gonna guilt trip me now, are you?"
            
            show charlotte idle
            
            C "Relax, it's just a joke with a seed of truth in it."
            "Charlotte places her hand on your shoulder as if to reassure you."

        "You give Charlotte the paracord and she walks up to the wall, assessing her route. She mimes out her actions and you couldn't help but join in too. With surprising strength and patience, Charlotte scales the wall as if it's second nature. She manages to reach the top ledge."
        
        hide charlotte

        C "Lemme find something to tie this cord to- Oh what's this?"
        player "Hey, don't leave me here!"
        C "Don't worry. *throws paracord down* Just went to secure it to something while you climb up. Also! I found something!"
        "You start to climb the paracord."
        player "{i}I should start working out after this... I'm sweatin' up a storm."
        "You reach the top and Charlotte lends you a hand and pulls you up."

        $ paracord.add_to_bag()
        show charlotte happy at character_right

        C "Nice to see ya!"
        player "Likewise~ So what were you saying earlier? You found something?"

        show charlotte idle
        
        C "Yeah, I walked a bit ahead while waiting for you and snagged this."

        jump choice4a_getknocker

    else:
        player "I gotta say, I'm not as confident as you are. This body is not meant for climbing."
        "You wiggle your arms like noodles."
        
        show charlotte happy
        
        C "Pfft, I wasn't gonna point it out but now that you mentioned it, you do have noodle arms. Say what you will but, maybe I have faith that you can pull it off." 
        player "I don't know if I should feel offended or encouraged."
        
        show charlotte idle
        
        C "As long as you follow exactly what I do, you should be fine."
        "Both of you stretch and loosen up a bit before Charlotte takes the lead."
        "She mimes out her visual route and starts to climb, with you tagging behind. As she climbs and grabs onto a pattern of protrusions and pitons, Charlotte details her movements for you to follow suit."
        "You start to feel your strength wither away, arms and legs both shaking. You grab onto a piton and it snaps, your hand slips and ends up wedged into a crack in the wall.{nw}"
        
        play sound "audio/rock-destroy-6409.mp3" volume 0.4
        with hurt_flash

        extend "You screech as the pain shoots from your wrist and up into your shoulders."
        
        show charlotte shocked
        
        C "[player]!"
        "Charlotte shoots up onto the ledge and reaches her arm out."
        
        show charlotte worried
        
        C "I'm here! I got you!"
        "You take the risk and with all the strength you can muster in your legs. You jump and grab Charlotte's arm to hoist you up. You curl up holding your wrist with your other hand."

        if firstaidkit in bag:
            C "H-Hold on! \n*takes her bag off and pulls out the first aid kit*" 
            C "*looks around for a stick* \nDid you feel it break? Or is it a sprain or something."
            player "Uhhhh... \n*dazed*"
            C "It's fine. Let's just do this for now just in case."
            "Charlotte takes your hand, places the firm stick on your forearm and wraps your arm with the leftover gauze in the first aid kit."

            $ firstaidkit.use()
            $ injuries_player = injuries_player - 1

            "..."
            show charlotte idle
            C "How're you feeling?"
            player "Better than before I suppose."
            C "Yeah...You kinda passed out? I wasn't sure what to do so I just waited here. Sorry, I kinda ate a good amount of our snacks, but the water's still available haha."
            player "*looks at wrist*\nThanks for your help. I owe ya."
            
            show charlotte happy
            
            C "You owe me double! 'Cause look what I found."

            jump choice4a_getknocker

        else:
            C "*helps you hold your wrist in place*\nIs it broken or do you think its a sprain?? Scale of 1 to 10 how painful?? 10 is the highest."
            player "Uhhh... 7?"
            C "Oh good. Maybe it's not serious. Uh, maybe try to move your wrist around slowly once you feel the pain ease up."
            player "Sure thing boss. *flashes a thumbs up and winces*"
            C "Wait here, I'll scout out the path ahead if there's anything we can use."
            player "Hey, don't go too far. We can go together."
            C "*sighs* Alright, Alright. I'll walk in your field of vision."
            "..."
            player "Found anything?"

            jump choice4a_getknocker

    label choice4a_getknocker:
        "Charlotte hands you something."
        player "A giant ring?"
        show charlotte idle
        C "Yup. But doesn't it look like one of those fancy door knocker things? Y'know, the ones that make you feel spiffy when you use it to knock instead of your knuckles."
        player "Now that you mention it, yes, it does. It could come in use so let's bring it. Who knows, maybe we'll find a door to knock on."
        
        $ knocker.add_to_bag()
        show charlotte happy

        C "Haha alright.\n*loops it through her belt and buckles her belt up again*"

        show charlotte idle
    
    jump choice4_done

label choice4_water:
    player "Let's go across the water, I'm not too confident in my arm strength."
    C "With noodles like those I ain't too surprised."
    "You both approach the water."

    if flashlight in bag:
        player "Could you do me a favor and shine up the water for me? I wanna see how deep it is."
        "Charlotte lights up the water."
        C "Hey look, there's an underwater ledge! I think it goes all the way across? *whistle*\nIt's wide enough to walk normal."
        player "Whew, I thought we were gonna have to wade over. Glad only our little piggies need to take the plunge."
        "You both cross the water with only slightly damp feet."

    else:
        "[player] sticks his leg into the water all the way and it still doesn't reach the bottom."
        player "Well, {w}wish me luck."
        "[player] plunges into the water."

        with hurt_flash
        $ injuries_player = injuries_player + 1

        player "{size=+20}CO- {size=-5}*gurgle*"
        
        show charlotte shocked
        
        C "[player]! What happened!?"
        "Charlotte reaches into the water and grabs [player]'s arm to pull him up but she notices some oddly warm water on the arm she grabbed."
        player "*surfaces*\n Ah tits, be more gentle will ya!"
        
        show charlotte worried

        "[player] clambers back onto land, cursing in ways Charlotte never heard before."
        C "What happened? Why's your arm covered in blood!?"
        player "\^\%\#\$\%\$ rock happened that's what! Gashed me bloomin' arm!"
        C "A rock? Where?"
        player "\'Towards the left wall, the sneaky bugger, thinks the darkness means it can surprise folk like that, \@\%\#\$ piece of \@\%\#\$\&\# in a pile of \*\#\^\$\%\&. I hope you crumble to dust."
        
        show charlotte thinking
        
        C "Ummmm... so do you want the good news first or the bad news?"
        player "Tear that bandage right off, what's our latrine being filled with?"
        
        show charlotte idle
        
        C "You didn't need to get wet. The good news is that the rock seems to be a ledge and I think I can barely see it going all the way over."
        "[player] begins to curse for several minutes."
        "You both cross the water as you curse up another storm about how blood loss and hypothermia are having a race to see who can kill him first."
        "By the time you get to the other side, you've calmed down significantly and even your accent seems to have retreated."
        C "So British huh?"
        player "Sort of, grew up all over Europe but yeah I was born in Britain. Ma and Pa loved road trips before the triplets. Hopefully when the triplets grow up, Ma and Pa find the energy to go on road trips again."

        $ injuries_player = injuries_player + 1

    "As you reach the end of the pool, you notice the ground getting{cps=4}...{/cps}{w=0.3} fuzzy"
    player "Great, another slippin' hazard. {w}At least this one's hard to miss."
    
    show charlotte thinking
    
    C "Wait...{w} Is this what I think it is?"
    player "I just see some fuzzy patches of asininity waiting to get our arses bruised."
    
    show charlotte idle
    
    C "First off, this species of moss is mostly under whatever surface it's on and the parts in open air are usually bone dry and therefore not slippery."
    C "Secondly, this moss is super rare and in high demand since it has very strong healing and antibacterial properties."
    player "So that means we don't gotta worry about any more injuries! At least in the long term."
    C "THIRDLY, a side effect of how it grows means that the surface part, the only part we can even gather right now, is mostly air. So we're gonna need basically everything we see just for a poultice big enough {nw}"
    
    if pockets == False:
        extend " for this knee."
    
    else:
        if injuries_player > 0:
            extend " for yer arm."

        else:
            extend " for anything larger than a scraped knee."
    
    C "Regardless, it's a nice thing to have even if we've barely got one use of it."
    "You and Charlotte grab all the moss you see, the armload you both got really compacting down to the size of both of your fists."
    $ moss.add_to_bag()
    C "Wait till you add water to apply it, it'll shrink to like half that."        

    if injuries_C > 0 and injuries_player > 0:
        player "So you wanna use it? Your gash looks way uncomfortable to walk on."
        C "Eh, I got used to it. I got used to getting scratched up and powering through when I got these babies. \n*points at the badges on her sleeves*"

    menu:
        "Heal Charlotte":
            jump choice4a_C

        "Heal yourself":
            jump choice4a_player

    label choice4a_C:
        player "I insist, you must've powered through more than enough injuries to be as nonplussed as you are about your knee. I think I should take a page from your book and \"build some character\" myself"
        "You mix the moss with water and it shrinks even more, barely enough to cover the gash on her knee."
        
        $ moss.use()
        $ injuries_C = injuries_C - 1
        
        "You both decide to get back to getting out of here."

        jump choice4a_done

    label choice4a_player:
        player "Yeah I guess you do seem to be doin' fine with that leg."
        player "Me on the other hand.{w} I feel like I'd faint if so much as a breeze touches me arm."
        "You mix the moss with water and it shrinks even more, barely enough to cover the gash on your arm."
        
        $ moss.use()
        $ injuries_player = injuries_player - 1
        
        "You both decide to get back to getting out of here."
        
        jump choice4a_done

    label choice4a_done:
    C "Sure do hope this tunnel ain't a dead end."
    player "Only one way to find out."
    jump choice4_done


label choice4_done:

"You two continue down the path."

show charlotte thinking

C "Don't you think it's strange?"
player "What's strange?"
C "These tunnels are pretty clear. Like sure, there's rubble and such, but for the most part, we haven't really had any issues walking around this place. How big do you think this cave even is?"
player "Who knows. Maybe it was once a home for a small community or somethin'. I wouldn't be surprised."
C "True... I could see that, if we weren't stuck here I mean."
player "We're not gonna be here for long. We're gettin' outta here together."

show charlotte happy

C "Haha, got that right! Let's go to a buffet after all this is done n' over."
player "Aww you're gonna pay for me? Thanks, I accept your invitation~"

show charlotte shocked

C "Wait, what?!"

stop music_overlay fadeout 1
scene bg cave1_lit at bg_top with dissolve

"You and Charlotte sit in an open section of the path you've been walking, the light from outside giving you a bit of warmth and hope. Drinking the last drops of water and remaining snacks you get up from your spot and dust off your uniform."

show charlotte idle at character_right

C "Almost feels like we're in the homestretch huh? I gotta say, we just met not too long ago, but it's a nice feeling not having to shoulder the burden of life and death alone."
player "You gettin' poetic on me?"

show charlotte idle

C "Nah, *scratches neck* just feels like the best time to say it."
player "That ain't ominous at all."

show charlotte annoyed

C "Ughhh, you know what I mean. "

show charlotte idle

extend "Anyway, the moment's gone now so you lost your chance to be sentimental."

hide charlotte
$Play_Sound.run()

"Charlotte skips ahead and you can't help but chuckle at your new friend."
C "Hey [player], check this out!"
"You follow the sound of Charlotte's voice and find her looking up at the top of a wall at some sort of rock shelf."
"You squint and notice something relatively large laying on it. The object looks as if it could be pulled off with some effort."

show charlotte idle at character_right

player "Think it's worth it?"
C "Anything's worth it if it helps us out. Of course, if we don't injure ourselves in the process."

if paracord in bag and knocker in bag:
    "You look at Charlotte's belt, at the large knocker ring you found recently."
    player "I got an idea, it involves that ring of yours."
    "You pull out your paracord {nw}"
    
    $ paracord.use()
    
    "and Charlotte removes the ring from her belt {nw}"
    
    $ knocker.use()
    
    "and hands it to you. Tying a secure knot around the ring, you do some test throws with it to ensure the ring doesn't go rogue."
    C "How nifty. Nice to know the gears are still turning in there after who knows how long."
    player "Haha, ye. You're lucky I still got some brain battery left over."
    "Swinging the paracord, you take your aim. It takes a few attempts but you finally managed to slot the cylindrical object into the ring and yank it down. Charlotte catches the item in her arms while you collect the paracord and knocker."
    
    $ paracord.add_to_bag()
    extend ""
    $ knocker.add_to_bag()

    player "What a catch! What fish did we reel in?"
    C "Uhhhh. *shows you a stone idol* {nw}"
    
    $ stoneidol.add_to_bag()
    show charlotte worried

    extend "This?"
    player "A stone idol huh? I wonder what it was used for."

    show charlotte idle

    C "Well, now that we have it, we can find out maybe?"
    player "Yup. I'm sure the opportunity will present itself."
    "Charlotte places it in your bag. Due to its height, it now comically pokes its head out."

else:
    if injuries_C < 1 and injuries_player < 1:
        player "Wanna try an old fashioned boost?"
        C "Gladly!"
        "You give Charlotte a boost. Unfortunately she comes up short."
        player "Lemme have a go."

        jump boost_C

    if injuries_C > 0:
        player "Wanna try an old fashion boost?"
        C "Yeah...maybe not, my knees are takin' their toll."
        player "*looks at Charlotte's relatively fresh skid marks on her knees* Ah shoot, sorry, I completely forgot."
        C "No biggie."
        player "Sorry about that by the way... Dumb move on my part."
        C "Hey, don't worry about it. We're past that now. Anywho, let's just move on. Doesn't look like we'll get to uncover that treasure."

    if injuries_player > 0:
        player "I'd boost ya, but my whole arm is outta commission."
        C "I can try to boost you."
        player "Aight. Let's do this."

        jump boost_C
  
    label boost_C:
        show charlotte shocked at character_shake_right

        "Charlotte boosts you and her arms immediately start shaking."
        C "Dude, are you made of lead or something!?! Why are you so heavy!"
        player "Hey! Has anyone told you not to mention a man's weight! *reaching out*"

        show charlotte annoyed at character_right

        "You jump back to the ground."
        player "Mission failed on this one."
        player "At least we can say we tried."

        show charlotte thinking

        C "Yeah... It's prob'ly not important anyway. At least, that's what I'm gonna tell myself."

        show charlotte idle

        player "I concur. Let's save our energy while we still have some."

"A fork in the tunnel presents itself."
C "Oh wow, we got a choice on our hands! Been a while hasn't it."
player "Left or Right huh?"
C "Yup! Better be careful which one you choose."
player "Why do I gotta choose?"

show charlotte happy

C "'Cause I don't wanna be responsible if something bad happens~"
"You groan while Charlotte's cackle bounces around the cave walls."

menu:
    "Go Left":
        jump choice5_left
    
    "Go Right":
        jump choice5_right

label choice5_left:
    player "Left it is."
    "You and Charlotte go into the tunnel on the left."

    scene bg cavelight at bg_bottomish with dissolve
    $ Play_Sound.walk_loop()

    "A few minutes later."

    player "Is it just me or is the cave looking{cps=4}...{/cps} cleaner?"

    show charlotte thinking at character_right

    C "What do you mean?"
    player "It feels like the cave is traveling straighter, like it's more intentional now. I don't know, I could just be imaginin' things."
    C "I don't think you're imagining it..."

    show charlotte idle
    stop sound fadeout 1

    "You and Charlotte stop in your tracks."
    player "Is that a brazier?"
    C "Either that or a real fancy stalagmite."
    "You start walking towards the brazier. It felt as if it was calling you. Surprisingly, there are hot coals inside it, hot enough to light something on fire."

    if pocketknife in bag and statue in bag:
        player "Ah!"
        "You reach into the side of your bag and grab the wooden statue you were working on and whip the pocket knife out of your pouch."
        "Charlotte watches you as you shave off bits of wood from your carving."
        
        play sound "audio/fire-39294.mp3"
        
        "The wood shavings start to burn and flames bloom to life."
        
        show charlotte shocked
        
        C "Whoa [player], there's something emerging from the coal!"
        "Staring into the flames, you noticed a stone pedestal sprout from the coal."
        C "*pulls out the stone idol from your bag*"
        extend "Wild assumption, but do you think this is meant to be on there?."
        player "*stares into the idol's eyes*"
        extend "Be my guest."
        "Charlotte places the idol carefully onto the pedestal, careful not to burn arms in the flames. The idol starts to heat up and...glow?"
        C "Whaa?? How is it glowing?"
        "The ground starts to rumble as you hear something open in the distance. You whip your head around and see a stone door opening on the cave wall, debris falling as the doors separates from the wall."
        player "Uh excuse me? Was that door always there??"
        C "What in the world is goin' on around here."
        player "You're guess is as good as mine."
        "The two walk into the open door and find footprints in the otherwise undisturbed dust leading into a temple where you find an array of 5 idols similar to the stone idol you used to get into this place, but of varying colours: Red, Blue, Yellow, Green, and White. Yellow and Green, are placed opposite each other as are Red and Blue, but there seems to be an empty space where something used to be opposite the White Idol. Upon a second look, you notice that the footprints lead right to that now empty spot."
        player "Despite feelin' a bit creeped out, you gotta admit this temple looks amazing."
        C "Pretty well kept too. You'd think it was sealed for centuries if not for these footprints huh."
        "You find a tablet beside the entrance to the temple. You don't know what language it is but it's definitely not English. Despite that, you can both seem to understand what it says subconsciously. 'Pay tribute to the 6 elements of creation! Fire and Water in harmony gives us just the heat we need to live, no more no less. Earth and Air in harmony give us the substance and emptiness that gives us form so that we can move. Life and Death in harmony gives us sustainability so that we can return the favour that Mother Nature has given us so it can be given again in the future. Pray that our tributes may be enough for the elements to allow us to channel them through their Idols so that we may tip the scales but never break them.'"
        C "Wait. There's supposed to be 6."
        player "Good point. If red is fire and blue is water then... *thinking* the Death Idol is missing."
        C "That doesn't sound ominous at all. Wonder where it could've gone."
        "A strange feeling has been resonating within you the longer you stay in the temple. It feels like the temple is asking you to take the White Idol away, The Idol of Life. The absence of the Idol of Death has created an imbalance and with it nowhere to be found, the only feasible solution is to take away the Idol of Life as well to restore some semblance of balance. You start to pick up The Idol of Life."
        C "[player]! Don't touch it! What if something bad happens 'cause we took it? *holds onto the idol with you*"

        if Charlotte is injured:
            C "Whoa..."
            player "Whoa what?"
            C "*removes her hands from the idol then touches the idol again* When I touch the idol... I don't feel the pain on my knees."
            player "So it's healing you?"
            "You look at Charlotte's knee to see if her skin is magical stitching itself together."
            C "Nah, more like it just doesn't make me feel the pain anymore. Like a numbing agent."
            player "So what you're sayin' is that we can bring it along with us, yeah?"
            C "Are you serious?"
            jump choice5_healthy

        if player is injured:
            player "Whoa..."
            C "Whoa what?"
            player "*you remove your hands from the idol then touch the idol again* When I touch the idol... I don't feel the throbbing pain in my arm."
            C "So is it healing you or something?"
            "Charlotte looks at your arm as if she was expecting to see a magical beam of light erupt from it."
            player "I don't think so. It feels like it's soothing and easing the pain I feel. Almost like it's ain't even there. Soooo, it must really wanna join us outta here."
            C "Are you serious?"
            jump choice5_healthy

        if injuries_C < 1 and injuries_player < 1:
            jump choice5_healthy
        
        label choice5_healthy:
            player "You remember what the tablet said right? It needs a counterpart. Something bad'll happen if we don't take it! It's currently imbalance since the Death idol isn't here."
            C "That's just our speculation though, you know we both can't read whatever language that is!"
            player "*sighs* Aight look, I wasn't gonna say it since I didn't wanna look crazy but the temple is telling me to bring it with us."
            "You put The Idol of Life carefully in your bag, it fits nice and snug compared to the large stone idol from before. You are able to zip your bag up."
            C "You do sound crazy, but honestly, this whole day's already been flipped and twisted all over."
            player "Yup, might as well take the chance on this."
            "The both of you look around the area to see if there's any path for you to progress."
            C "Looks like we gotta backtrack."
            player "At least we got the chance to pass by this place."
            "You walk away, look back at the temple, and with the idol you your possession, you head back to retrace your steps and check out the other path."
            jump choice5_right


        show charlotte idle

    else:
        C "What are you doing? It's not like we can do anything with it. There's nothing in it for us to use either. Unless you wanna throw coal at each other."
        player "I guess you're right. But I can't shake this feeling' like we could've done somethin' here."
        "You walk away, look back at the brazier, then head back to retrace your steps and check out the other path."
        jump choice5_right

label choice5_right:
    player "Right it is."
    "You and Charlotte go into the tunnel on the right."

    scene bg cavewall at bg_bottomish with dissolve

    "After walking for several minutes, Charlotte notices something."

    show charlotte thinking at character_right
    play music_overlay "audio/birds-19624.mp3" fadein 3

    C "I hear birds.{p} I think we-{nw}"
    player "Hup. {w=0.5}Zip it. Don't jinx it."

    show charlotte annoyed

    C "Fine, then I guess those are bats and we accidentally made our way deeper.\nNyeh *Sticks out Tongue*"
    player "Better."

    scene effect darkness
    show bg caveexit at bg_exit with dissolve

    "You stop in your tracks as you stare at the sight before your eyes."
    "You and Charlotte look down at the bottomless gap before you. It's just large enough that you would need to jump to even start climbing."
    "Thankfully, the ledge is just short enough that if one of you gives the other a boost, they should be able to reach the ledge. You can only hope that there's something on the other side that you can use to help the other one across."
    
    show charlotte idle at character_right
    
    C "Looks like we can boost each other. One of us is sure to make it."
    player "Heh. You must be a mind reader 'cause I was thinkin' the same thing."
    C "Well, you were making a face. Like you were staring into the void...well technically you were but y'know what I mean."

label endgame:

if lifeidol in bag:

    if Charlotte is injured:
        player "Okay Charlotte, you gotta take my bag with you when you jump. It has the idol and the paracord so you can throw it to me and help me make it to the other side."
        "The ground starts to shake."
        player "Again?!?"
        C "We have to get moving then. It's not safe for us here."
        "Charlotte takes your bag and both of you shake off the nerves and loosen your muscles to prepare for the boost. Charlotte plants her foot in your hands and just when you are about to launch her forward, her knee buckles and she starts to fall forward. In your efforts to try and save her, you lunge forward to catch her, only to realize that the idol on her back added a significant amount of weight to her body. The collective weight sends you forward. You and Charlotte start to fall into the endless abyss and you can't help but replay Charlotte's words from earlier."
        
        show effect vignette_white_wide

        C "[player]! Don't touch it! What if something bad happens 'cause we took it?"
        player "You remember what the tablet said right? It needs a counterpart. Something bad'll happen if we dont take it! It's currently imbalance since the Death idol isn't here."
        C "That's just our speculation though, you know we both can't read whatever language that is!"
        
        hide effect

        "As your consciousness starts to fade, you couldn't help but think." 
        player "{i} If only I had listened to you...Charlotte, I'm sorry.{/i}"


    if player is injured:
        player "Okay Charlotte, you gotta take my bag with you when you jump. It has the idol and the paracord so you can throw it to me and help me make it to the other side."
        "The ground starts to shake."
        player "Again?!?"
        C "We have to get moving then. It's not safe for us here."
        "Charlotte takes your bag and both of you shake off the nerves and loosen your muscles to prepare for the boost. Charlotte plants her foot in your hands and just when you are about to launch her forward, Your arm gives out. The whole time you were carrying the idol, the pain in your arm subsided, but not that it's not in your possession, you feel the excruciating pain. Despite this, you see Charlotte falling forward. In your efforts to try and save her, you lunge forward to catch her, only to realize that the idol on her back added a significant amount of weight to her body. The collective weight sends you forward. You and Charlotte start to fall into the endless abyss and you can't help but replay Charlotte's words from earlier."

        show effect vignette_white_wide

        C "[player]! Don't touch it! What if something bad happens 'cause we took it?"
        player "You remember what the tablet said right? It needs a counterpart. Something bad'll happen if we dont take it! It's currently imbalance since the Death idol isn't here."
        C "That's just our speculation though, you know we both can't read whatever language that is!"

        hide effect

        "As your consciousness starts to fade, you couldn't help but think." 
        player "{i} If only I had listened to you...Charlotte, I'm sorry.{/i}"
        #[Secret's Untold Ending]

    if injuries_C < 1 and injuries_player < 1:
        player "Here, you're taking my bag. The idol and my paracord are in there so you can toss it to me when you make it on the other side."
        "The ground starts to shake."
        player "Again?!?"
        C "We have to get moving then. Let's stay calm and get it done!"
        "Charlotte takes your bag and both of you shake off the nerves and loosen your muscles to prepare for the boost. Charlotte plants her foot in your hands and with the strength of your legs, you launch her into the air, across the gap, and she rolls onto the other side unscathed. She looks up and sees the exit to the cave."
        C "[player]! I See the exit up ahead! *hops with excitement*"
        player "Yes. Beautiful. Now please throw the paracord or so help me!"
        C "Ah! Right!"
        "Charlotte tosses one end of the paracord to you and you tie it securely on your belt. You make a running jump with the available length you have attached to the paracord. You manage to grab the ledge safely,hanging by your fingertips miraculously uninjured. You feel a tug on the rope and with its aid, you hoist your arm up on the ledge. Charlotte expertly ties the other end of the cord to a large, heavy rock and runs to you to lift you up. The ceiling starts to crumble behind you, and with no time to untie the paracord, you unbuckle your belt and both of you sprint to the exit."
        "The rubble collapses and blocks the exit, sealing the cave."
        player "*huff* *huff*"
        extend "Boy am I glad we made it outta there..."
        C "*huff* *huff*"
        extend "Smart thinking with your belt. We'd both still be stuck in there if it weren't for that."
        player "Haha, quit flirtin'."
        C "Oh shut up."
        "Charlotte bonks you lightly on the head."

        "As you two celebrate the fact that you are alive, well and breathing, you discuss several unanswered questions: Who took The Idol of Death? Why did they only take the one idol? How long ago did they take it? How large scale of an effect can these Idols have? What do we do now? You two glance at each other and realize that you have some researching to do when you get back to camp."
        #[Secrets to Unfold Ending]

else:
    if injuries_C > 0:
        "The ground starts to shake."
        player "Again?!?"
        C "We have to get moving then. It's not safe for us here."
        "Both of you try to shake off the nerves and loosen your muscles to prepare for the boost. Charlotte plants her foot in your hands and just when you are about to launch her forward, Her knees give out. Charlotte, unable to recover from your weak launch, flails in the air, falls, but manages to grab and hang onto a small ledge 3 feet below on the other side of the gap. In your efforts to try and save her, you lean forward and offer your hand."
        player "I'm here! Grab my hand!"
        "Charlotte lifts her legs up against the wall to try and jump for your arm. Unfortunately, she still underestimates her injury and weakly jumps for your hand. She manages to grab it but her weight falling down sends you down the gap with her." 
            
        if paracord in bag:
            "As you fall, you can't but think of all the events that happened today. It slipped your mind that you had a paracord in your bag the whole time."
            player "{i} This is all my fault...Charlotte, I'm sorry.{/i}"
        
        else:
            "As you fall, you can't but think of all the events that happened today."
            player "{i} So it all ends like this huh....{/i}"
            #[Death's Pull Ending]

    if injuries_player > 0:
        "The ground starts to shake."
        player "Again?!?"
        C "We have to get moving then. It's not safe for us here."
        "Both of you try to shake off the nerves and loosen your muscles to prepare for the boost. Charlotte plants her foot in your hands and just when you are about to launch her forward, Your arm gives out. Charlotte, unable to recover from your weak launch, flails in the air, falls, but manages to grab and hang onto a small ledge 3 feet below. In your efforts to try and save her, you lean forward and offer your good hand."
        C "No! Go without me! Save yourself!"
        player "Screw that! I'm not leaving you!"
        "Charlotte grabs your hand and is able to steady her footing against the gap's wall. You struggle to pull her up with only one hand, and it becomes worse when Charlotte's foot slides down the wall, her hands pulling you down with her."
        
        show charlotte at character_fall_down

        "Your proclamation came true as your collective weight sends you down the gap with her." 
        
        if paracord in bag:
            "As you fall, you can't but think of all the events that happened today. It slipped your mind that you had a paracord in your bag the whole time."
            player "{i} This is all my fault...Charlotte, I'm sorry.{/i}"
        
        else:
            "As you fall, you can't but think of all the events that happened today."
            player "{i} So it all ends like this huh....{/i}"
            #[Death's Cold Embrace Ending]

if injuries_C < 1 and injuries_player < 1:
        if paracord in bag:
            show bg at bg_shake_exit
            show charlotte shocked
            play music_overlay "audio/earth-rumble-6953.mp3"

            "The ground starts to shake."
            player "Again?!?"

            show charlotte worried

            C "We have to get moving then. Let's stay calm and get it done!"
            "Charlotte takes your bag and both of you shake off the nerves and loosen your muscles to prepare for the boost. Charlotte plants her foot in your hands and with the strength of your legs, you launch her into the air, across the gap, and she rolls onto the other side unscathed. She looks up and sees the exit to the cave."
           
            show charlotte happy
            
            C "[player]! I See the exit up ahead! *hops with excitement*"
            player "Yes. Beautiful. Now please throw the paracord or so help me!"
            
            show charlotte worried
            
            C "Ah! Right!"
            "Charlotte tosses one end of the paracord to you and you tie it securely on your belt. You make a running jump with the available length you have attached to the paracord. You manage to grab the ledge safely, hanging by your fingertips miraculously uninjured. You feel a tug on the rope and with its aid, you hoist your arm up on the ledge. Charlotte expertly ties the other end of the cord to a large, heavy rock and runs to you to lift you up. The ceiling starts to crumble behind you, and with no time to untie the paracord, you unbuckle your belt and both of you sprint to the exit."
            "The rubble collapses and blocks the exit, sealing the cave."

            play music_overlay "audio/birds-19624.mp3" fadeout 3
            play sound "audio/stones-falling-6375.mp3" volume 0.7
            show bg outside at bg_topish with dissolve

            player "*huff* *huff*"
            extend " Boy am I glad we made it outta there..."
            
            show charlotte neutral
            
            C "*huff* *huff*"
            extend " Smart thinking what your belt. We'd both still be stuck in there if it weren't for that."
            player "Haha, quit flirtin'."
            C "Oh shut up."
            "Charlotte bonks you lightly on the head."

            "As you two celebrate the fact that you are alive, well and breathing, you get a sinking feeling in your chest. You see the now sealed exit of the cave and couldn't help but feel that you missed something of grave importance to you, the cave, and maybe even the rest of the world."

        else:
            show bg at bg_shake_exit
            show charlotte shocked
            play music_overlay "audio/earth-rumble-6953.mp3"

            "The ground starts to shake."
            player "Again?!?"

            show charlotte worried

            C "We have to get moving then. Let's stay calm and get it done!"
            "Both of you shake off the nerves and loosen your muscles to prepare for the boost. Charlotte plants her foot in your hands and with the strength of your legs, you launch her into the air, across the gap, and she rolls onto the other side unscathed. She looks up and sees the exit to the cave."
            C "[player]! I See the exit up ahead! *hops with excitement*"
            player "Yes. Beautiful. Now please try and find something to help me get across!"
            C "Ah! Right!"
            "Charlotte frantically looks around the cave on her side. She looks at you and runs to the exit." 

            hide charlotte

            player "{i} Did...Did she just abandon me?!?! After everythi-"

            show charlotte worried at character_shake_right

            "You see Charlotte run back inside carrying a long log on one shoulder it looked stable enough to walk on."
            
            show charlotte at character_right
            play sound "audio/wooden-thud-mono-6244.mp3"

            "She lays to act as a bridge and steps on one end. She reachers her arm out."
            C "Just focus on me and run. I'll grab you when you're in reach!"
            "You quickly but skillfully balance yourself on the log and quickly grab Charlotte's hand to reach the other side and both of you sprint to the exit."
            
            play music_overlay "audio/birds-19624.mp3" fadeout 3
            play sound "audio/stones-falling-6375.mp3" volume 0.7
            show bg outside at bg_topish with dissolve
            
            "The rubble collapses and blocks the exit, sealing the cave."
            player "*huff* *huff*"
            extend "Boy am I glad we made it outta there..."
            C "*huff* *huff*"
            extend "Smart thinking what your belt. We'd both still be stuck in there if it weren't for that."
            player "Haha, quit flirtin'."
            C "Oh shut up."
            "Charlotte bonks you lightly on the head."

            "As you two celebrate the fact that you are alive, well and breathing, you get a sinking feeling in your chest. You see the now sealed exit of the cave and couldn't help but feel that you missed something of grave importance to you, the cave, and maybe even the rest of the world."
            #[Bonded Ending]

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
