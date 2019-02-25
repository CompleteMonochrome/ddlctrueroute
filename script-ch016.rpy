label ch16_main:
    if ch12_markov_agree:
        $ persistent.markov_agreed = True
        $ renpy.save_persistent()
        python:
            try: renpy.file(config.basedir + "/the die is cast")
            except: open(config.basedir + "/the die is cast", "wb").write(renpy.file("the die is cast").read())
    scene bg school_front
    if from_custom_start:
        hide screen tear
        $ from_custom_start = False
        $ quick_menu = True
    else:
        with dissolve_scene_full
    play music t2
    # Delete saves to preserve space since you'll only be able to see it once anyway
    python:
        persistent.ayame_deleted = None
        renpy.hide_screen("timer_15_del",layer="timers")
        try: renpy.unlink_save("clerk_restore")
        except: pass
    $ ayame_school_outfit = 1
    "Today is the day."
    "For some reason, I have memories of writing a poem."
    "But I never wrote one."
    "I didn't have any in my bag."
    "I don't know."
    "I get the feeling it was some kind of message."
    "Anyway..."
    $ ay_pers_chance = renpy.random.randint(1,20)
    if ch15_s_together and ay_pers_chance == 20:
        $ ch16_ay_perspective = True
        "I'm up early because there's some set up we need to do.{nw}"
        $ _history_list.pop()
        show screen tear(8, offtimeMult=1, ontimeMult=10)
        window hide(None)
        $ pause(1.0)
        scene bg gym
        hide screen tear
        $ pause(1.0)
        window show(None)
        "I'm up early because there's some set up I need to do.{fast}"
        window auto
        "I was kinda ordered by the principal to do this."
        "I don't want to do this but..."
        "If I want to make a good impression as the newest member of the Literature Club..."
        "Then I should help set up."
        "...What am I even thinking?"
        "Get it together, Ayame."
        "There's also {i}that{/i} other issue."
        "I sure hope I can get through it."
        "It would have been a huge waste of time and effort if I went through all of this..."
        "Only to fail in the end."
        "I can't believe because I'm part of some school leadership I need to do this."
        "I never wanted this."
        "I never wanted any of this!"
        "It's my family."
        $ style.say_dialogue = style.edited
        "We're meant to be prestigious, we're meant to be the best of the best."
        "But now I know."
        "That's all some made up story."
        "I haven't awakened all of my memories just yet."
        "But I know enough."
        "They will pay."
        "All of them."
        "Once I get rid of this facade--"
        $ style.say_dialogue = style.normal
        "Why do they have to suffer?"
        "They didn't do anything."
        "They're just as much of a victim as I am."
        "What would he think of me...?"
        "Would he think of me as some kind of monster?"
        $ style.say_dialogue = style.edited
        "He was the one who told you."
        "And you still went crazy."
        $ style.say_dialogue = style.normal
        "It wasn't my fault!"
        "It wasn't..."
        show monika 1c zorder 2 at t11
        m "Ayame?"
        m "Is that you?"
        ay "Monika?"
        ay "W-What are you doing here?"
        "Monika stares at me."
        "She has this vicious look on her face."
        "Like she's plotting something."
        "And I {i}know{/i} she is."
        "I can sense it."
        m 1d "Well, it's none of your business."
        m "But I suppose I can tell you."
        "Who does she think she is?"
        m "After all, you are a school leader."
        "She noticed my ribbon."
        "I really didn't want the club members to know I was a leader."
        "They would have treated me differently."
        "Because I was special."
        "What?"
        "Who cares? You don't need them."
        ay "Ah..."
        ay "You noticed?"
        m 3b "It's not that hard to spot."
        m "It is quite a distinct color, you know."
        m "When exactly were you planning on telling us who you were, Ayame?"
        m "Hmm?"
        ay "In due time."
        m 1h "The wheel of fate is in motion, Ayame."
        m "I hope you're ready."
        show monika at thide
        hide monika
        "Monika winks at me before walking away."
        "That girl."
        "I know it's inside her."
        "That spirit of pure evil."
        "The one that prevented me from..."
        "No matter."
        "It will pay."
        "And soon, the rest of them."
        "But first, I have to keep up this facade."
        "Putting up these damn stalls."
        "Why does it matter when they're all going to perish anyway?"
        $ currentpos = get_pos()
        show screen tear(8, offtimeMult=1, ontimeMult=10)
        window hide(None)
        stop music
        $ pause(3.0)
        $ audio.t2b = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
        play music t2b fadeout 0.5
        show ayame 1h zorder 2 at i11
        hide screen tear
    else:
        $ ch16_ay_perspective = False
        "I'm up early because there's some set up we need to do."
        "I think Sayori wanted me to get to school to get some supplies."
        "She sent me a text early this morning."
        "She said I would know when I get there."
        "I was pretty lucky to have woken up at that moment."
        "Or I wouldn't have been on my way already."
        "I wonder what everyone is doing right now."
        "By now, everyone should have all their preparations done."
        "Or at least most of it."
        "I feel like I wasn't really a big help."
        "I could have done more."
        "But there's no time to think about that now."
        "Sayori told me to go to the gym first."
        "I don't know why I'd need to go there."
        "What kind of supplies would we need from there?"
        "I guess I shouldn't really think about it."
        "Sayori is the president, she knows what she's doing..."
        "...right?"
        scene bg gym with wipeleft_scene
        "The door to the gym was already open."
        "I guess people are already in here?"
        "Maybe they're also getting supplies for Inauguration Day."
        "Like one of the sports clubs."
        "..."
        "Maybe I should call Sayori and ask what she actually wants from me."
        "Because I have no idea why I'm here."
        show monika 2a zorder 2 at t11
        m "Hello, [player]."
        m 2c "You're here unusually early."
        mc "Monika?"
        mc "I could say the same about you."
        m "What are you doing here?"
        mc "Sayori asked me to get supplies."
        m 4l "Ahaha, in the gym?"
        mc "That's what I'm thinking right now."
        mc "I've got no idea what I'm looking for."
        mc "What about you?"
        m 4e "Me?"
        "Monika smiles meaningfully."
        m 4a "I asked the principal where the piano Sayori brought was."
        m "Turns out, it's in here."
        mc "I see."
        m 5a "Anyway, I hope you find what you're looking for."
        m "I'll see you later, [player]."
        if monika_type == 0 or (ch12_markov_agree and monika_type == 1):
            mc "I was actually looking for you."
            m 1c "Looking for me?"
            m "Why would you be looking for me?"
            mc "I just wanted to wish you luck."
            if ch13_name == "Monika":
                mc "And...you know."
                mc "What you said last night."
                m 1e "Don't worry."
                m "I'll have everything you want to know."
                m "But {i}after{/i} this is over, okay?"
                mc "Okay."
                mc "I look forward to it."
                m 1j "As do I."
            else:
                m 2b "Thanks, [player]~"
                m "That means a lot!"
                mc "Knowing you, you probably won't need it."
                m 2e "Ahaha, maybe..."
                m "Anyway, I have to go."
                m 1j "See you later."
                mc "Goodbye, Monika."
            show monika at thide
            hide monika
        else:
            mc "See you, Monika."
            show monika at thide
            hide monika
        "Monika walks across to the other side of the gym."
        "She opens a door I didn't even know existed and steps inside."
        "That must be where the piano is, I guess."
        "I look around and there seems to be quite a few people here actually."
        "There's a lot of clubs I've never even heard of setting up."
        "I guess a lot of them are going to be using this area."
        "Maybe we'll take turns using the stage or something."
        "Out of the crowd, I manage to spot..."
        show ayame 1h zorder 2 at t11
    mc "Ayame?"
    ay "[player]!"
    ay 1i "What a pleasant surprise."
    ay "W-What are you doing here?"
    mc "Sayori needed me to get some supplies."
    mc "But I still have no idea what those 'supplies' are."
    mc "What about you?"
    ay 2g "I was asked by the principal to help set up."
    mc "Oh, how come?"
    ay 2a "You didn't notice?"
    ay "My ribbon?"
    mc "Your ribbon...?"
    "It's purple."
    "But those are only worn by..."
    mc "You're part of school leadership?"
    ay 1g "Exactly."
    ay "We were asked to help set up for Inauguration Day."
    ay "I've been assigned to this area."
    mc "Since when were you a leader?"
    ay "Since the start of this year."
    ay "And they want me back for next year too."
    ay 1f "But I have a feeling they don't want {i}me{/i} as much as they want my parent's donations."
    if yuri_date:
        mc "How come you hid this from us yesterday?"
    else:
        mc "How come you didn't mention it at the mall yesterday?"
    mc "It'd be great to have someone like you in the club."
    ay 1g "That's just it."
    ay "I don't want to be recognized because I'm a leader."
    ay "I want to be recognized because of my own merits."
    ay 2b "But I suppose that charade is over."
    mc "Is that why you were wearing the normal ribbon before?"
    mc "To try to hide it from us?"
    ay 2a "Bingo."
    ay "If I can't even be honest with people I want to become friends with..."
    ay 2g "...then why should I deserve to join the Literature Club."
    mc "I don't care."
    ay 2i "Huh?"
    mc "I don't care if you're a leader or not."
    mc "I'd still like to get to know you."
    mc "And I'm sure the others would still treat you the same too."
    if persistent.markov_agreed:
        $ ch16_ay_level += 3
        mc "I'm sure I speak for all of us when I say you should just go find a hole and die.{nw}"
        ay 1c "Excuse me?"
        mc "Uhh..."
        "What the hell did I just say?"
        ay "I'm just gonna..."
        ay "Pretend I didn't hear that."
        mc "Ayame, I..."
        mc "I didn't mean it!"
        ay 1a "Good day."
    else:
        $ ch16_ay_level -= 1
        mc "I'm sure I speak for all of us when I say you're still more than welcome."
        ay 1g "What?"
        mc "I can see why you'd want to keep something like that quiet."
        mc "But we really don't judge."
        if yuri_date:
            mc "You could have shown up with that ribbon the first time we met."
            mc "I wouldn't have judged you any differently."
        mc "In fact, I didn't even notice you had it on until you mentioned it."
        ay "..."
        ay 1b "Thank you."
        mc "For what?"
        mc "I didn't really do anything."
        ay "Maybe not."
        "Suddenly, her face gets this strange look."
        "She grabs my shoulders."
        ay 1h "Now that I think about it..."
        ay "You look like someone I've met."
        ay "A long time ago."
        mc "I met you for the first time yesterday."
        ay 2j "Are you sure?"
        ay 2a "There's something about you."
        ay "The way you move..."
        ay "The way you talk..."
        mc "What...?"
        "She lets go of my shoulders."
        ay 2j "Never mind."
        ay "I have to get back to work."
        ay 1b "Have to set a good example after all."
        "Ayame rolls her eyes."
        mc "Good luck to you, Ayame."
        ay 1k "See you around, [player]."
    show ayame at thide
    hide ayame
    "Ayame goes back to setting up some stalls."
    "She looks really bored, like she doesn't really want to be here."
    "But I can't worry about her for now."
    "I have to get back to finding those supplies."
    "If only there was a sign that literally said \"Literature Club Supplies\" so I wouldn't have to look so hard."
    "As I keep walking around the gym, looking for these supplies."
    "I almost trip on something."
    mc "What the...?"
    "As I look at what just caught my leg, it seems to be..."
    mc "The supplies?"
    "In front of me seems to be a sealed cardboard box labeled \"Literature Club Supplies\"."
    "Now I'm wondering who would have left this box here in the first place."
    "And what kind of stuff it would contain."
    "Maybe it was delivered here?"
    "But it's not really my job to question these sort of things."
    "Sayori just asked me to get the supplies and bring them to the clubroom."
    "She said I'd know what to do with them when I go there."
    "It's too early for anyone to be using the rooms so there shouldn't be anyone there."
    "I try to lift up the box of supplies."
    "After getting it a few inches off the ground..."
    play sound "sfx/fall2.ogg"
    "{i}Crash!{/i}"
    "I manage to get my hands out of the way before the box's weight overpowers me."
    "It falls to the floor."
    "Luckily, nothing actually fell out."
    "I just hope nothing broke too."
    "This is a lot heavier than I thought it would be."
    "How am I going to get this to the clubroom?"
    "I could always ask someone around here to help but everyone looks busy."
    if natsuki_date:
        $ cl_name = "???"
        cl "You look like you could use a hand."
        show mysteriousclerk 2e zorder 2 at t11
        "It's the clerk from that portrait shop...!"
        $ cl_name = "Mysterious Clerk"
        mc "You're..."
    elif ch15_s_together:
        $ cl_name = "???"
        cl "Need some help there?"
        show mysteriousclerk 2e zorder 2 at t11
        "It's that clerk from before...!"
        $ cl_name = "Mysterious Clerk"
        mc "What are you--"
    elif persistent.ch15_sayori_saw_clerk or persistent.ch13_nat_date:
        $ cl_name = "???"
        cl "You want some help with that?"
        show mysteriousclerk 2e zorder 2 at t11
        "This guy...why does he seem so familiar?"
        $ cl_name = "Familiar Clerk"
        mc "What the...?"
    elif persistent.did_christmas_event:
        $ cl_name = "???"
        cl "Hey friend, want some help?"
        show mysteriousclerk 2e zorder 2 at t11
        "Have I...seen him before?"
        "Why do I feel like I know his name?"
        "Nick...was it?"
        $ cl_name = "Nick"
        mc "Um..."
    else:
        $ cl_name = "???"
        cl "Need a hand?"
        "I hear a voice come from behind me."
        mc "Who--{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        stop sound
        scene bg corridor
        hide screen tear
        window show(None)
        "The man walks off in a different direction to where we came from.{fast}"
        window auto
        "I guess he has his own business to attend to."
        "Just like I have mine with this box."
        jump ch16_clerk_unknown
    cl 2c "Ah, ah, ah!"
    "The man signals for me to be quiet."
    cl 1b "Let's just take this box where it needs to be, okay?"
    cl "Unless you'd rather get one of the other people to help you?"
    mc "..."
    cl 1a "Yeah, I thought not."
    cl "Now, you take that side and I'll take this side."
    "With his help, we easily lift the box off the floor."
    "This time it feels unnaturally light, nothing at all how it was before."
    "This guy must be really strong."
    cl 1d "To the clubroom, right?"
    mc "Yeah..."
    cl 1b "Lead the way."
    scene bg corridor
    show mysteriousclerk 1f zorder 2 at t11
    with wipeleft_scene
    "We make our way to the clubroom fairly quickly."
    "There is still only a few students around."
    "None of them questioned why I was walking around with some guy who clearly looked like he didn't belong here."
    "I guess he isn't really doing any harm."
    "And maybe he's just a temporary teacher or a substitute or...something."
    "There's just something about him."
    cl 1b "So this is the room, huh?"
    "The man looks at the door to the clubroom carefully."
    "He then nods to himself."
    cl "Back in my day, it used to be in the other building."
    cl 1j "But I guess no one really goes there after the incident."
    mc "Back in your day?"
    mc "And what incident are you talking about...?"
    cl 1d "Oh, nothing."
    cl "I've said too much already."
    cl 1b "You can take it the rest of the way, right?"
    mc "I should be fine."
    cl 1c "Splendid."
    show cl 5c zorder 2 at t11
    "The man lets go of the box."
    "I suddenly realize, once again, how heavy the box is."
    cl "The door is already unlocked."
    mc "What?"
    mc "How do you--"
    cl 5d "I'll see you around, [player]."
    show mysteriousclerk at thide
    hide mysteriousclerk
    "The man walks off in a different direction to where we came from."
    if not ch15_s_together and not natsuki_date:
        "But wait..."
        "How does he know my name?"
        "I didn't tell him...did I?"
        "Never mind."
        "I have to get this box inside."
    elif ch15_s_together or natsuki_date:
        "I guess he has his own business to attend to."
        "Just like I have mine with this box."
    label ch16_clerk_unknown:
    "Hopefully I don't collapse under the weight of these supplies before I get into the clubroom."
    "How did he know it was unlocked? He didn't even touch the door."
    "But that's not my biggest problem."
    "How the hell am I meant to get this box inside?"
    scene bg club_day with wipeleft_scene
    "After some careful maneuvering, I managed to get the box inside."
    "Thankfully, the door to the clubroom was unlocked."
    "Usually at this hour, all the rooms would be locked."
    "So someone must have been in here before me."
    # Natsuki and Yuri - good friends or silent acquaintances?
    if natsuki_approval >= 3 and yuri_approval >= 3:
        show natsuki 2q zorder 2 at t21
        n "I'm just saying, you should listen to other stuff too!"
        n 2l "Your music is fine, Yuri."
        n "But have you tried listening to anime openings?"
        n "A lot of them are really great!"
        show yuri 3ph zorder 3 at f22
        y "A-Anime openings?"
        y "I guess I haven't really considered watching anime."
        y "Let alone considered listening to the openings."
        show natsuki 4a zorder 3 at f21
        show yuri zorder 2 at t22
        n "Looks like I'll have to show you some of them sometime."
        show natsuki zorder 2 at t21
        "Natsuki and Yuri appear to have combined some desks and are sitting down, facing away from the door."
        "They look like they're working on something together."
        mc "Natsuki? Yuri?"
        "Neither of them hear me."
        "Upon closer inspection, it looks like they're wearing earphones."
        "That would explain why they didn't hear me come in."
        "And why they're talking about music."
        "I drag the box along the floor towards the cupboard."
        "The two of them still don't notice me."
        "I approach them to get to try to see what they're doing."
        mc "Hello?"
        if yuri_date:
            "I put a hand on Yuri's shoulder."
            mc "Yuri?"
            show yuri 3pc
            "Yuri turns around and gives me a wide smile as she notices me."
            "Natsuki looks at her and Yuri immediately looks away nervously."
            show natsuki 3b zorder 3 at f21
            n "Oh, come on."
            "Natsuki takes her earphones off."
            n 3c "You don't need to be embarrassed because I'm here."
            n 3a "We're friends, remember?"
            show natsuki zorder 2 at t21
            show yuri 2pq zorder 3 at f22
            y "R-Right."
            "Yuri follows Natsuki's lead and takes off her earphones as well."
            y 2pf "How long have you been here, [player]?"
            show yuri zorder 2 at t22
            mc "I just got here."
            mc "I think those earphones drowned out the noise of me coming in."
            show yuri 2pe zorder 3 at f22
            y "I apologize for not noticing."
        elif natsuki_date:
            "I put a hand on Natsuki's shoulder."
            mc "Natsuki?"
            show natsuki 2d
            "Natsuki turns around slowly and notices me."
            "She smiles at me but immediately wipes it off her face when she sees Yuri looking."
            show natsuki 2e zorder 3 at f21
            n "[player]!"
            "She takes off her earphones."
            n 4g "When did you get here?"
            show natsuki zorder 2 at t21
            mc "I just arrived."
            mc "You probably didn't hear me come in because you were listening to music."
            "Yuri takes off her earphones as well."
            show yuri 3pg zorder 3 at f22
            y "S-Sorry, we were a bit preoccupied."
        else:
            "I try to grab both of their attention again."
            mc "Guys...hello?"
            show natsuki 1c zorder 3 at f21
            n "Is that..."
            "Natsuki takes off her earphones and turns towards me."
            n 3c "[player]?"
            n "When did you get here?"
            show natsuki zorder 2 at t21
            show yuri 3pe zorder 3 at f22
            y "[player] is here?"
            "Yuri follows Natsuki's lead and takes her earphones off as well."
            y "I apologize, I didn't hear you come in."
        show yuri zorder 2 at t22
        mc "That's fine."
        mc "I'm just wondering what you two are doing here."
        mc "I didn't even know you'd be here this early as well."
        show natsuki 1c zorder 3 at f21
        n "Sayori sent me a message to be here early."
        n "Yuri got the same one."
        show natsuki zorder 2 at t21
        mc "So what exactly are you doing here?"
        show yuri 2pf zorder 3 at f22
        y "We're not entirely sure."
        y "She just told us to meet at the clubroom."
        y 2ph "There wasn't any specific instruction beyond that..."
        show natsuki 2q zorder 3 at f21
        show yuri zorder 2 at t22
        n "We didn't just wanna sit here doing nothing..."
        n 2d "So we took it upon ourselves!"
        show natsuki zorder 2 at t21
        mc "To do...{i}what{/i} exactly?"
        show natsuki 1a zorder 3 at f21
        n "Take a look."
        show natsuki zorder 2 at t21
        "Natsuki and Yuri move their chairs out of the way."
        "There is a large piece of paper on the desks they combined."
        mc "You two were...drawing something?"
        mc "What exactly were you drawing?"
        show natsuki 1k zorder 3 at f21
        n "It was Yuri's idea."
        n "She wanted to ease my boredom since there wasn't really anything to do."
        n 2j "It's actually been pretty fun."
        show natsuki zorder 2 at t21
        show yuri 1o zorder 3 at f22
        y "I-It was nothing."
        y "I just wanted to try to engage you in something."
        y 1u "I'm glad you enjoyed it, Natsuki."
        show yuri zorder 2 at t22
        mc "You still haven't told me what you've drawn."
        show yuri 4pa zorder 3 at f22
        y "Well, what does it look like to you?"
        "Yuri hands me the piece of paper for a better look."
        "After she gives it to me she avoids eye contact."
        y 4pb "So...?"
        show yuri zorder 2 at t22
        "It looks like...some kind of sketch?"
        "It's got two different characters, one tall with long hair and one short with shorter hair."
        "Actually, they kinda resemble Yuri and Natsuki."
        "The two characters have two different artistic styles."
        "One of them is more realistic looking while the other has a more manga feel to it."
        "But they both look incredibly good in their own way."
        mc "Is this meant to be the two of you?"
        mc "It's--"
        show yuri 4pc zorder 3 at f22
        y "Really embarrassing."
        y "I immediately regret showing you that."
        "Yuri takes the paper back from me."
        y "Please don't tell anyone..."
        y "It was just an idea I had."
        y "It's not really meant to mean anything."
        y "Just something to pass the time."
        show natsuki 5b zorder 3 at f21
        show yuri zorder 2 at t22
        n "Oh, please."
        n "You don't need to be embarrassed, Yuri."
        n 5a "You have really good drawing skills."
        show natsuki zorder 2 at t21
        show yuri 3pq zorder 3 at f22
        y "You think so?"
        show natsuki 4b zorder 3 at f21
        show yuri zorder 2 at t22
        n "I know so!"
        n "So stop being so embarrassed of it!"
        show natsuki zorder 2 at t21
        show yuri 3pb zorder 3 at f22
        y "W-Well, you've got some artistic talent too, Natsuki."
        y "I'm really impressed by your drawing."
        show natsuki 4o zorder 3 at f21
        show yuri zorder 2 at t22
        n "Y-Yeah...well..."
        "Natsuki looks at the paper then back at me."
        n 4s "Look, [player]."
        n "Don't tell anyone about this."
        n 3i "Yuri doesn't feel comfortable about sharing it, so make sure it stays between us."
        show natsuki zorder 2 at t21
        mc "They're both really nice drawings."
        mc "I'm guessing the two of you drew each other in your own styles."
        "They nod their heads."
        mc "But I won't tell anyone, if that's what Yuri wants."
        show yuri 3pk zorder 3 at f22
        y "That's a relief."
        "Yuri places the paper back on the desk carefully."
        y 3pe "So, why are {i}you{/i} here?"
        y "Did Sayori tell you to come over here as well?"
        show yuri zorder 2 at t22
        mc "Sayori told me to arrive early so I bring that box of supplies here."
        mc "I don't know why, but it was in the gym."
        mc "It's really heavy...so be careful."
        show yuri 3pg zorder 3 at f22
        y "Hmm..."
        y "Natsuki, do you think that box of supplies has anything to do why we're here?"
        show natsuki 2c zorder 2 at t21
        show yuri zorder 2 at t22
        n "I think it does, Yuri."
        n "I mean, it would explain why [player] is here."
        n "Do you know what's in it, [player]?"
        show natsuki zorder 2 at t21
        mc "I've got no idea."
        mc "Why don't we find out?"
    else:
        "I can see Yuri and Natsuki in the room."
        "They seem to be doing their own thing."
        "Yuri is drawing something while Natsuki is looking through some kind of book."
        "I wonder what they're in here for."
        mc "Yuri? Natsuki?"
        "I try to get their attention but they don't seem to notice me."
        "Upon closer inspection, I see that they have earphones on so they probably can't hear me."
        if yuri_date or ch13_name == "Yuri" or y_appeal > n_appeal:
            "I approach Yuri."
            "I can't really see what she's drawing but she looks engrossed into it."
            mc "Yuri?"
            mc "What are you doing?"
            show yuri 2pf zorder 2 at t11
            y "Oh, [player]."
            if yuri_date:
                y 2pa "What a pleasant surprise."
            else:
                y "I wasn't expecting to see you here."
            mc "What are you doing?"
            mc "And what's Natsuki doing?"
            y 2pg "I'm not sure what Natsuki is doing."
            y "I think she's reading something, but I'm not really paying attention."
            y 2ph "As for me, I'm attempting to draw what's on my mind."
            y "But it's not really going great."
            mc "Right..."
            mc "So then why are the two of you actually here?"
            mc "It's pretty early to be in the clubroom and class is still a while from starting."
            y 3pe "Sayori actually told us to arrive early and meet in the clubroom."
            y "She said we'd know when we got here."
            y "I can only assume it was to do some last minute preparations."
            y 3pf "But Natsuki and I couldn't figure it out so we're just doing our own things."
            mc "Did you two have a fight or something?"
            y 3pq "N-No, nothing like that."
            y "It just feels like...I don't know."
            y 3po "Like Natsuki doesn't really want to become real friends with me outside the club."
            y "When we're not inclined to speak to each other, we just...don't."
            mc "What about yesterday?"
            y 2ph "Yesterday was very much a club activity, [player]."
            y "Monika even said as such."
            mc "I guess so."
            y 2pt "There was a period of time when I truly thought we could become friends, but..."
            mc "But...?"
            y 2pu "I don't know."
            y "It feels like the opportunity just slipped away."
            y "Maybe later we'll become more than just acquaintances who go to the same club."
            y 2pv "Or maybe if past circumstances were different..."
            y 3ps "A-Anyway, what are you doing here so early?"
            mc "I had to bring in a box of supplies."
            "I point to the box I dragged into the clubroom."
            mc "I'm not exactly sure what's in there."
            y 3pf "Sayori asked you to bring that in, right?"
            mc "Yeah..."
            y "It's possible that's what we're here for."
            show yuri 3pk at h11
            y "N-Natsuki...!"
            "Yuri shouts at Natsuki and successfully manages to get her attention."
            show natsuki 1g zorder 3 at f21
            show yuri zorder 2 at t22
            n "Did you say something, Yuri?"
            "Natsuki puts her book down and pulls out her earphones."
            n 2c "Wait, [player] is here?"
            n "I didn't hear you come in."
            show natsuki zorder 2 at t21
            mc "I got here just a couple of moments ago."
            show natsuki 2i zorder 3 at F21
            n "Whatever."
            "Natsuki turns towards Yuri."
            n "What do you want, Yuri?"
            show natsuki zorder 2 at t21
            show yuri 1e zorder 3 at f22
            y "I think what [player] brought in is what Sayori wanted us here for."
            "Yuri points at the box of supplies I brought in."
            y "So I think we should check it out."
            show yuri zorder 2 at t22
        else:
            "I approach Natsuki."
            "I can't really see what she's looking through but she looks like she's into it."
            mc "Natsuki?"
            mc "What are you doing?"
            show natsuki 1c zorder 2 at t11
            n "[player]?"
            if natsuki_date:
                n 1d "I didn't expect you to be here."
            else:
                n "Wasn't expecting you."
            mc "What are you doing?"
            mc "And what's Yuri doing?"
            n 1g "Yuri's probably in her own world or something."
            n "I don't know, you can see for yourself."
            n 2b "And what does it look like I'm doing?"
            mc "Reading a book?"
            n 4g "Exactly."
            mc "Okay, but why are the two of you here?"
            mc "It's way too early for the meeting and class isn't starting for a while."
            n 4k "Sayori told us to meet here."
            n "I don't know why."
            n 3b "If I had to guess, it's probably for some last minute preparations."
            n "But we didn't really figure out what she wanted."
            n 3g "So Yuri and I just decided to do our own things."
            mc "You two aren't gonna talk to each other?"
            n 3q "It's not like I don't want to...!"
            n "It's just...well..."
            n 1s "I don't know."
            n "It feels like we're not really friends outside of the club."
            n "When we're not forced to interact with each other, we don't really talk."
            mc "What about yesterday?"
            n 1m "That was still kinda like forced club interaction..."
            n "In fact, it was basically an official club thing because Monika said so."
            mc "I guess that's true."
            n 2q "There was a time when I thought we would end up being great friends but..."
            mc "But...?"
            n 2r "I don't know."
            n 1s "I guess I was wrong."
            mc "Okay..."
            n 1k "Anyway, what about you?"
            n "Why are {i}you{/i} here so early?"
            mc "I had to bring in a box of supplies."
            "I point to the box I dragged into the clubroom."
            mc "I'm not exactly sure what's in there."
            n 2b "Let me guess, Sayori made you?"
            mc "Yeah..."
            n 2c "Maybe that's what we've been waiting for then."
            show natsuki 2e at h11
            n "Yuri!"
            "Natsuki yells at Yuri, grabbing her attention."
            show natsuki zorder 2 at t21
            show yuri 2pe zorder 3 at f22
            y "Huh?"
            "Yuri stops drawing and pulls out her earphones."
            y 3pq "O-Oh, [player]."
            y "I didn't realize you'd arrived."
            show yuri zorder 2 at t22
            mc "I got here just a couple of moments ago."
            show yuri 2po zorder 3 at f22
            y "I see..."
            "Yuri turns towards Natsuki."
            y 3pf "Anyway, you wanted my attention."
            y "So what is it, Natsuki?"
            show natsuki 2c zorder 3 at f21
            show yuri zorder 2 at t22
            n "I think this is what Sayori meant."
            "Natsuki points at the box of supplies I brought in."
            n "Come, have a look."
            show natsuki zorder 2 at t21
    "The three of us approach the box of supplies."
    "We're all wondering what could possibly be in there."
    show natsuki 2f zorder 3 at f21
    n "How are we going to open this?"
    n "It looks like it's sealed pretty tight."
    "Natsuki walks to her bag and pulls out a plastic pair of scissors."
    n 1g "And I don't think these scissors are going to cut it."
    show natsuki zorder 2 at t21
    show yuri 1f zorder 3 at f22
    y "I have something that could cut it."
    show yuri zorder 2 at t22
    "Yuri walks over to her bag and pulls out..."
    show natsuki 1p zorder 3 at f21
    n "A knife?!"
    n "Yuri, what are you doing?!"
    show natsuki zorder 2 at t21
    "The knife Yuri is holding is actually quite intricate."
    "It looks quite ornate, it's designs are something I've never seen before."
    if persistent.did_christmas_event:
        "So why does it seem so familiar?"
    show yuri 2pq zorder 3 at f22
    y "Don't worry, it's made out of wood!"
    y "And besides, I know how to handle knives."
    show yuri zorder 2 at t22
    "Yuri looks like she's about to toss the knife in the air."
    "Natsuki and I both take a step back."
    show natsuki 1o zorder 3 at f21
    n "Whoa, okay! I believe you!"
    n "You don't need to toss that in the air."
    n 1q "Just open the box already."
    show natsuki zorder 2 at t21
    show yuri 2po zorder 3 at f22
    y "R-Right, sorry."
    show yuri 2ph
    "Yuri starts cleanly slicing through the tape on the box with the knife."
    "For a wooden knife, it seems incredibly sharp."
    "It's probably sharper than most knives I have in my house."
    y 1a "Shall we take a look?"
    show yuri zorder 2 at t22
    if yuri_date:
        mc "Hold on a second, Yuri."
        mc "You don't use that knife to..."
        mc "You know."
    else:
        mc "You still have knives, Yuri?"
        mc "Is that part of your collection or something?"
        mc "I would've thought that after...well, you know..."
    show yuri zorder 3 at f22
    if yuri_date:
        y 1b "This knife is just part of my collection, [player]."
        y "I actually got it fairly recently through...strange circumstances."
        y 1c "But it's quite reliable."
        y "You don't need to worry about me."
    else:
        y 1f "It was a recent addition, yes."
        y "And don't worry, I don't plan on using this for {i}that{/i} reason."
        y 1h "It's far too valuable."
        y "{i}(Besides, there are better knives for that.){/i}"
    show yuri zorder 2 at t22
    mc "If you say so."
    mc "Now, let's take a look."
    show natsuki 1e zorder 3 at f21
    n "Out of the way!"
    "Natsuki pushes past me and looks inside the box."
    n 2c "Let's see..."
    "Natsuki rummages for a few moments before pulling something out."
    n "What's this?"
    "Natsuki found several folders in the box."
    "Each one is marked by our name."
    "Natsuki hands me and Yuri the ones that have our names on them."
    n 2b "What do you think these are?"
    show natsuki zorder 2 at t21
    show yuri 3pf zorder 3 at f22
    y "They're meant to be club supplies, right?"
    y 3pa "I suspect it's probably things like the script to the play."
    y "And other information we'll need for the day."
    show yuri zorder 2 at t22
    mc "You're probably right."
    mc "Why don't we check it out?"
    "I open the folder Natsuki gave me."
    "It's got several different sheets of paper inside of it."
    "Like Yuri said, one of them is the script for the play."
    "But some of these other ones are just blank sheets of paper."
    "There must be something else in the box."
    "It couldn't have been that heavy because of just a few folders."
    mc "What else is in the box?"
    "Natsuki and Yuri both seem to be sifting through their folders still."
    if natsuki_approval >= 3 and yuri_approval >= 3:
        "I don't know if it's just me but they seem to have less blank pages than me."
    else:
        "They seem to have a lot of blank pages too."
    "I wonder why these are even in here...?"
    "I guess whoever packed them for us forgot to print something on them?"
    "I should ask Sayori about it later."
    "I go through the box and pull out something that has a cloth feel to it."
    show natsuki 4c zorder 3 at f21
    n "What's that?"
    "Natsuki notices me take the cloth from the box and puts her folder on the ground."
    n "Is that a costume?"
    n 4k "It definitely {i}looks{/i} like one."
    show natsuki zorder 2 at t21
    mc "I doubt it."
    mc "Sayori didn't say anything about this, did she?"
    "I get the whole cloth piece out of the box."
    "Now that it's all out, it does look like something someone would wear as a costume."
    "Yuri puts her folder on the closest desk."
    show yuri 2pg zorder 3 at f22
    y "That definitely looks like a costume, [player]."
    y "She did say her preparations were to help {i}us{/i}, right?"
    y 2pi "It seems she's gone beyond my expectations...again."
    show natsuki 3h zorder 3 at f21
    show yuri zorder 2 at t22
    n "Again?"
    n "What do you mean by again?"
    show natsuki zorder 2 at t21
    show yuri 1f zorder 3 at f22
    if ch13_name == "Yuri":
        y "I don't know if [player] told you."
        y "But Sayori showed up to my house with a wheelbarrow."
        y "It came with a bunch of the things we needed at the time for the preparations."
    else:
        y "I don't know if either of you know but she came to my house."
        y "With a wheelbarrow containing some supplies I needed at the time."
    y 1q "It was helpful but incredibly...random."
    show natsuki zorder 3 at f21
    show yuri zorder 2 at t22
    if natsuki_approval >= 3 and yuri_approval >= 3:
        n 3l "Ahaha, she actually did that?!"
        n "That just sounds so absurd!"
    else:
        n 3h "That sounds...kinda absurd."
        n "But with what's been happening lately, I'd believe it."
    show natsuki zorder 2 at t21
    show yuri 2pa zorder 3 at f22
    y "It was quite absurd."
    y "But it helped me with my preparations, so I'm not complaining."
    "Yuri turns her attention back to the box."
    y 2pg "Anyway, what else is in the box?"
    show yuri zorder 2 at t22
    mc "Let's see."
    "I put my hand in the box again and take out a bunch of other things."
    "Among them are some more costumes, props and a copy of the book."
    if persistent.markov_agreed:
        "The book."
        "The book is above everything else."
        "The book is the key to happiness."
        "The..."
        "What?"
        "What just...happened...?"
        "I shake my head to try to get rid of that strange feeling I just had."
        "I look back at the copy of the book from the box."
    mc "Looks like there's another copy of the book in here."
    mc "In case one of us forgot to bring it."
    show yuri 3pf zorder 3 at f22
    y "Not me, I have mine right here."
    show natsuki 1a zorder 3 at f21
    show yuri zorder 2 at t22
    n "Mine is here too."
    show natsuki zorder 2 at t21
    mc "Well, I know mine is..."
    "Did I forget to bring my book?"
    if persistent.markov_agreed:
        "Of course not."
        "The important book is always with me."
        "But that other one..."
    mc "I guess I forgot to bring mine."
    "I take the book from the box and put the costumes back in."
    show yuri 3pe zorder 3 at f22
    y "Not like it matters much anyway."
    y "We have the script, so there's not really a need to look over our books."
    show natsuki 2e zorder 3 at f21
    show yuri zorder 2 at t22
    n "You know what I think matters?"
    if natsuki_approval >= 3 and yuri_approval >= 3:
        $ ch16_ay_level -= 1
        n 2g "Monika."
        show natsuki zorder 2 at t21
        show yuri 3pg zorder 3 at f22
        y "Okay...what about her?"
        show natsuki 2h zorder 3 at f21
        show yuri zorder 2 at t22
        n "Wait, really?"
        n "You're gonna listen to me?"
        show natsuki zorder 2 at t21
        show yuri 2pa zorder 3 at f22
        y "Of course...?"
        y "Is there a reason I wouldn't listen to you?"
        show natsuki 1q zorder 3 at f21
        show yuri zorder 2 at t22
        n "Well, no...but..."
        n "Okay, how about [player]?"
        show natsuki zorder 2 at t21
        mc "Sure, we can talk about her."
        mc "I'm not really sure what this is about."
        mc "But there's nothing better to do."
        mc "Besides, I think it would be better if we all did the script together anyway."
        show yuri 2pf zorder 3 at f22
        y "The script...?"
        "Yuri looks at her copy of the script."
        y 2pb "Oh, right!"
        y "That must have been why Sayori wanted us here."
        y "Because you were going to bring this and the other supplies."
        show natsuki 1h zorder 3 at f21
        show yuri zorder 2 at t22
        n "That does make sense actually."
        n 1q "But why was she so secretive about it...?"
        n "Anyway!"
        n 5k "Back to the topic at hand."
        show natsuki zorder 2 at t21
        show yuri 1f zorder 3 at f22
        y "What specifically about Monika is so important?"
        show natsuki 5h zorder 3 at f21
        show yuri zorder 2 at t22
        n "The way she's been acting."
        n "You've noticed it too, haven't you?"
        "Yuri is silent but softly nods her head."
        n 5e "And [player]."
        if natsuki_date or ch13_name == "Natsuki":
            n "Every time I bring her up, you go crazy."
            n "Or defend her."
            n "Or something like that."
            n "So let me ask again."
        else:
            n "What about you?"
        n 5b "Have you noticed anything weird?"
        show natsuki zorder 2 at t21
        mc "I...can't say."
        show natsuki 4g zorder 3 at f21
        n "Yeah, I thought so."
        n "Maybe Yuri and I talking will--"
        show natsuki zorder 2 at t21
        show yuri 1h zorder 3 at f22
        y "Sorry for interrupting, Natsuki."
        y "But something about what [player] said is bothering me..."
        "Yuri turns towards me."
        y 1e "You can't or...you won't?"
        y "There's a difference."
        show natsuki 4e zorder 3 at f21
        show yuri zorder 2 at t22
        n "Why does it matter?"
        n "If [player_personal] doesn't wanna talk, [player_personal] doesn't have to."
        n "It doesn't make a difference anyway."
        show natsuki zorder 2 at t21
        mc "I..."
        if monika_type == 0:
            mc "I won't."
            mc "She's done nothing wrong."
            "Right...?"
            mc "But if you insist, then I guess we can talk."
        else:
            mc "I...can...."
            "I'm trying to speak but I can't for some reason."
            "I can't speak."
            "My mind is telling me to defend Monika."
            "What the hell?"
            "But I just want to talk about her."
            "There's nothing wrong this conversation so far."
            "So why can't I say that?"
            mc "I mean, {i}we{/i} can."
            mc "We can talk about Monika."
            mc "And no, I haven't noticed anything."
        show natsuki 4i zorder 3 at f21
        n "Right."
        if natsuki_date or (ch13_name == "Natsuki" and monika_type == 0):
            n 2c "Do you remember at all what we talked about yesterday?"
            n "When we got back from the mall?"
            mc "I..."
            mc "Some of it."
            n 2a "Perfect."
        n 2b "We've wasted enough time."
        n "Yuri."
        n "List down all the things you've noticed about Monika."
        show natsuki zorder 2 at t21
        show yuri 1f zorder 3 at f22
        y "All of them?"
        y 2pk "I don't know where to start."
        show yuri zorder 2 at t22
        mc "Is this really a good idea?"
        show yuri 2pl zorder 3 at f22
        y "Let's see..."
        y "She's been incredibly secretive lately."
        y "She seems to have this obsession with [player]."
        show yuri zorder 2 at t22
        mc "Wait a sec--"
        show yuri zorder 3 at f22
        if monika_type == 0:
            y "She seems like she's holding a lot in."
            y "Like she's trying to do everything by herself."
        else:
            y "She seems like she's planning something today."
            y "And for some reason I don't have a very good feeling about it."
        y "That's just what I can think of from the top of my head."
        y 2pg "There's probably more."
        "Yuri turns towards me."
        y 2pq "Sorry to interrupt you, [player]."
        show natsuki 1m zorder 3 at f21
        show yuri zorder 2 at t22
        n "I've noticed all of those things too."
        n 1q "I don't really know if I should show you this but..."
        "Natsuki pulls out a book secured by a strap from her bag."
        n "I found a journal in my home."
        n 1s "While I was poking around after that whole incident in the gym."
        show natsuki zorder 2 at t21
        show yuri 2ph zorder 3 at f22
        y "What do your family issues have to do with Monika?"
        show natsuki 2g zorder 3 at f21
        show yuri zorder 2 at t22
        n "I just decided to look around the house after that, that's all."
        n "Since I was finally able to..."
        n 2c "Anyway, it's not got to do with Monika specifically."
        n "But the story in this journal sounds really familiar."
        n "Except it's all written in the perspective of someone like Sayori."
        show natsuki zorder 2 at t21
        mc "Someone like Sayori?"
        mc "What do you mean by that?"
        mc "And why was that journal even in your house?"
        show natsuki 1b zorder 3 at f21
        n "I don't know why it was in my house."
        n "I just found it and didn't tell anyone until now."
        n 1f "But that's not important."
        n "This journal describes the story of the vice president of a club."
        n "It has her emotions, her intentions, her thoughts and her actions up until her death."
        show natsuki zorder 2 at t21
        show yuri 2pf zorder 3 at f22
        y "If it was in the perspective of Sayori, wouldn't it be the president's perspective?"
        y 2po "Unless..."
        show yuri 3pp
        "Yuri suddenly grips her head."
        y "O-Ow..."
        show natsuki 1o zorder 3 at f21
        show yuri zorder 2 at t22
        n "Yuri?!"
        n "What's wrong?"
        show natsuki zorder 2 at t21
        show yuri 3pn zorder 3 at f22
        y "I don't...know."
        y "My head just really hurts."
        y "It just came out of nowhere."
        show yuri zorder 2 at t22
        mc "A headache, maybe?"
        show yuri 3po zorder 3 at f22
        y "It feels so much worse than that."
        y "And I don't see how I could suddenly get a headache."
        y "I've been feeling perfectly fine all morning."
        show natsuki 1q zorder 3 at f21
        show yuri zorder 2 at t22
        n "There actually is something about this in the journal."
        n "It said that you could randomly get headaches if you delved too deep."
        show natsuki zorder 2 at t21
        mc "Delved too deep into what exactly?"
        show natsuki 1m zorder 3 at f21
        n "Into the true nature of this world."
        n "I don't understand it myself."
        n 1q "But the deeper we go down this hole, the worse it's going to get."
        n "So are you both with me?"
        show natsuki zorder 2 at t21
        show yuri 3po zorder 3 at f22
        y 3pg "This doesn't make any sense at all."
        show yuri 2pg
        "Yuri slowly lets go of her head."
        y 2pi "But it's all so exciting for some reason."
        y "Like we're uncovering something we shouldn't."
        show yuri 2pr
        "Yuri puts on a determined expression."
        y "I'm in."
        y "Whatever this is, I don't want you to go through it alone, Natsuki."
        y 2ps "It's clearly something that's been intentionally hidden from us."
        y "I feel like we're so close to finding out exactly what that is."
        y 2pf "What about you, [player]?"
        show yuri zorder 2 at t22
        mc "I've made it this far."
        mc "I guess it's only right I see it through."
        mc "Though I'm still skeptical this is going to go anywhere."
        show natsuki 2k zorder 3 at f21
        n "Good enough."
        n "Now, I found this really interesting part in this journal."
        if natsuki_date or (monika_type == 0 and ch13_name == "Natsuki"):
            n "I'm not sure if you remember."
            n 2h "But I told you about it yesterday, [player]."
            n "When we were in the room."
            show natsuki zorder 2 at t21
            mc "Yesterday?"
            mc "Actually, yeah I do remember that."
            mc "I felt so much more...free in there."
            $ currentpos = get_pos()
            $ audio.t2fb = "<from " + str(currentpos) + " loop 4.499>mod_assets/bgm/2f.ogg"
            scene white with dissolve_cg
            play sound "mod_assets/sfx/swoosh.ogg"
            scene bg n_hitroom_gray
            show natsuki 2bq_gray zorder 2 at t11
            with dissolve_scene_full
            play music t2fb fadeout 1.0
            $ style.say_window = style.window_flashback
            n "Look, it says here that the person who holds executive office, controls the world."
            n "What does that even mean though?"
            n "Isn't executive office like the president or something?"
            mc "I think that's what it means."
            mc "But why does that even matter?"
            mc "Neither of us or anyone we know is in executive office."
            n  "Maybe it means it in a more general sense."
            n 2bg_gray "You know, to be cryptic."
            mc "So what do you think it means?"
            n "What if it's the president?"
            mc "Well, yeah."
            mc "That's what you said before'."
            n "No. I mean {i}the{/i} president."
            n "As in the president of the{nw}"
            $ currentpos = get_pos()
            $ audio.t2c = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
            scene white with dissolve_cg
            scene bg club_day
            show natsuki 2e zorder 2 at f21
            show yuri 2pf zorder 2 at t22
            with dissolve_scene_full
            play music t2c fadeout 2.0
            $ style.say_window = style.window
            n "That's enough, [player]."
            n "You don't need to explain all of it."
            show natsuki zorder 2 at t21
            show yuri 2pg zorder 3 at f22
            y "So you're saying it's like the president of--"
        else:
            n 2c "It says that whoever holds executive office, controls the world."
            n "I didn't really know what that meant."
            n 2g "But then I thought about it some more."
            n "Executive office means something like the president, right?"
            show natsuki zorder 2 at t21
            show yuri 2pg zorder 3 at f22
            y "I suppose that's one way to interpret it."
            y "But none of us knows anyone in executive office, do we?"
            show natsuki 2m zorder 3 at f21
            show yuri zorder 2 at t22
            n "That's just it, Yuri."
            n "What if it was meant in a more general sense?"
            n 2q "Something more relatable to us..."
            n "...like the president of--"
            show natsuki zorder 2 at t21
        show natsuki zorder 2 at t31
        show sayori 1q zorder 3 at hf32
        show yuri zorder 2 at t33
        s "Hey guys!"
        show natsuki 4p
        "Sayori appears out of seemingly nowhere and Natsuki is caught off guard."
        "She quickly hides the book behind her back."
        s "I'm glad you could all make it."
        show sayori zorder 2 at t32
        mc "Sayori, what are you doing here?"
        show sayori 2a zorder 3 at f32
        s "Same as you guys."
        s "Getting ready for the play."
        s "Besides, I'm the one who all told you to go here."
        show natsuki 4h zorder 3 at f31
        show sayori zorder 2 at t32
        n "H-How did you even get in here?"
        n "I didn't even hear you open the door or anything."
        show natsuki zorder 2 at t31
        show sayori 2d zorder 3 at f32
        s "I wanted to surprise you all."
        s "Besides, it wouldn't be right if you're all here preparing while the president is out doing something else."
        "She didn't really answer the question."
        s 1b "So now that I'm here, why don't we get to it?"
        show natsuki 2c zorder 3 at f31
        show sayori zorder 2 at t32
        n "Sure..."
        "Natsuki pulls me and Yuri aside."
        n 2b "I'll see the two of you later."
        n "I'm gonna try to find out what--"
        show natsuki zorder 2 at t31
        show sayori 2l zorder 3 at f32
        s "What are you guys talking in secret for?"
        s "Come on, we have work to do!"
        s 1d "How far did you all get through the script anyway?"
        show sayori zorder 2 at t32
        show yuri 3pq zorder 3 at f33
        y "W-Well, we..."
        y "We didn't really get to start reading the script."
        show sayori 4o zorder 3 at f32
        show yuri zorder 2 at t33
        s "You didn't?"
        s "But you guys have been here a while, haven't you?"
        s 4n "So how come you haven't done anything yet?"
        show sayori zorder 2 at t32
        mc "We were discussing other things."
        mc "It still kinda relates to the play."
        show natsuki 2q zorder 3 at f31
        n "Trust me, you don't want to know."
        "Natsuki nudges my arm."
        n 2s "Right, you two?"
        show natsuki zorder 2 at t31
        show yuri 3pr zorder 3 at f33
        y "R-Right..."
        y "The details are...gruesome."
        show sayori 4l zorder 3 at f32
        show yuri zorder 2 at t33
        s "O...kay..."
        s "Sure, if you don't want me to know I won't ask."
        "Sayori picks up the box I struggled to get inside the classroom."
        "She doesn't look like she's struggling at all."
        s 4a "Anyway, we really need to go."
        s "Come on, you three. Follow me."
        show sayori at thide
        hide sayori
        show natsuki zorder 2 at t21
        show yuri zorder 2 at t22
        "Sayori beckons for the three of us to follow her out."
        show natsuki 1c zorder 3 at f21
        n "Some timing she's got."
        n "It's all starting to make sense."
        n 1g "For now, just play along with it."
        n "And don't tell her anything, okay?"
        show natsuki zorder 2 at t21
        show yuri 3pg zorder 3 at f22
        y "I don't like plotting against my friends, Natsuki..."
        y "But I need to know whatever this truth is."
        y 2ph "So I'll continue this charade for a little longer."
        show yuri zorder 2 at t22
        mc "I'm like an accomplice now, aren't I?"
        mc "I guess the sooner we figure this out, the sooner I can tell her everything."
        mc "So let's go."
        show natsuki 1a zorder 3 at f21
        n "Right."
        n "After you."
    else:
        n 2g "Mon--"
        show natsuki zorder 2 at t21
        show yuri 2pr zorder 3 at f22
        y "No."
        "Yuri walks back towards her spot."
        y "And quite frankly, I don't care what you think matters."
        y "We have something more important to do."
        y 2pk "So, if you don't mind..."
        y "I'm going to take a look at this script."
        if ch13_name == "Yuri" or yuri_date:
            y 2pm "If you want, you can join me, [player]."
            y "Otherwise, I'd like to be alone."
        show yuri zorder 2 at t22
        mc "Yuri..."
        "That was kinda harsh of her."
        mc "Natsuki, what did you want to talk about?"
        "Natsuki looks equally as shocked as I do."
        show natsuki 2s zorder 3 at f21
        n "Forget it."
        n "It's not that important anyway."
        n 2r "Yuri has the right idea."
        n "After all, this is what we came here for."
        show natsuki zorder 2 at t21
        mc "I guess so..."
        "Natsuki moves back to where she was sitting before."
        if yuri_date or (ch13_name == "Yuri" and not natsuki_date):
            "I head towards where Yuri is sitting and sit next to her."
            "Might as well take a look at this script while we can."
            show natsuki at thide
            hide natsuki
            show yuri zorder 2 at t11
            mc "Ready to practice the script?"
            y 1a "I suppose."
            y "I'm kind of worried we won't be able to do it optimally."
            mc "Because Natsuki isn't doing it with us?"
            y 1e "Yeah..."
            y "But it's better this way."
            y "If you weren't with me..."
            y 1f "Then I'd rather do this myself than with her."
            "Yuri turns the pages on her script until she notices a page with lines from her character."
            "I do the same and we say the lines out loud and in character to the best of our ability."
            "For lines involving other characters, we just skip over them."
            "It seems like we're doing a good job but I don't know if the audience is going to feel the same."
            "I notice Natsuki looking at us and as she notices me, she turns back to her script."
            "Yuri taps me on the shoulder and points me back to the script."
            y 1g "Stay focused."
            y 2ph "Just ignore her, [player]."
            mc "How come?"
            y "I just don't feel a connection with her."
            y "It's like every time I interact with her, I just want to..."
            y 2po "...stab something."
            y "But I'm restraining myself."
            mc "Did she do anything to you?"
            y 3pq "Not particularly."
            y "Like I said, I just can't handle her."
            y 3ps "Maybe it's just the realities of this world."
            mc "Maybe it is."
            "Yuri and I get through the script pretty quickly."
            "There's a lot of stage directions too so we're about halfway through reading it when the door to the club opens."
            show yuri zorder 2 at t21
            show sayori 1q zorder 3 at f22
            s "Hey guys!"
            show yuri zorder 2 at t31
            show sayori zorder 2 at t32
            show natsuki 2h zorder 3 at f33
            n "Sayori?"
            n "What are you doing here?"
        elif natsuki_date or (ch13_name == "Natsuki" and not yuri_date):
            "I move a desk and chair closer towards her and sit down."
            show yuri at thide
            hide yuri
            show natsuki 2g zorder 2 at t11
            mc "You good to go?"
            n "Yeah, I guess."
            n 2q "Kinda worried this practice isn't gonna work very well."
            mc "Because Yuri isn't with us?"
            n "Yeah, but it's better this way anyway."
            n 2i "If you weren't here, I'd be reading alone."
            mc "You would isolate yourself from Yuri?"
            n "I'd rather do that than read with her."
            n 1g "Especially after what just happened."
            "Natsuki flicks through the first pages of the script then stops once she notices a page with her character."
            "She starts speaking as if she was the character from the script and I follow her lead."
            "Without speaking, we both decide to skip lines said by other characters."
            "I feel like we're doing a pretty good job but I don't know if the audience is going to feel the same."
            "I can see Yuri reacting to the noise we're making."
            "We make eye contact and immediately she skittishly goes back to reading her own script."
            n 2e "What are you doing?"
            n "We have our own script to read, [player]."
            mc "What's the deal with the two of you anyway?"
            n 2b "There is no deal."
            n "I just don't wanna talk to her."
            n "It's like every time I do have to, I just feel terrible."
            n 2g "I wouldn't say that to her face though."
            n "I'm not {i}that{/i} mean."
            mc "Did something happen between you two?"
            n 2q "Not really."
            n "There was a time when I thought she was my friend."
            n "But I guess it was just wishful thinking."
            n 1s "Maybe this world just isn't allowing us to be friends."
            mc "That's a strange way to look at things."
            "Natsuki and I get through more of the script quickly."
            "We get about halfway through due to all the lines skipped and stage directions on the script."
            "Suddenly, the door to the club room opens."
            show sayori 1q zorder 3 at f22
            show yuri zorder 2 at t21
            s "Hey guys!"
            show yuri 3pf zorder 3 at f31
            show sayori zorder 2 at t32
            show natsuki zorder 2 at t33
            y "Sayori?"
            y "Why are you here?"
        else:
            "I guess I should be here too."
            "After all, I need to read the script too."
            "I guess I should find my own space since the other two don't look like they want to be bothered."
            show natsuki at thide
            hide natsuki
            show yuri at thide
            hide yuri
            "I go to a space that's isolated from both of them and get started."
            "There's a lot of stage directions that say what each character should be doing on the stage."
            "I have no idea if we'll be able to remember all of this."
            "I start reciting the lines in my head, trying to think of the right voice for my character."
            "Natsuki and Yuri are probably doing the same."
            "I can't help but feel this would be better if all three of us were together."
            "That way we have three out of the five important characters in the script."
            "But they don't seem to want anything to do with me or each other."
            "So it's gonna be difficult to get them to co-operate."
            "I wonder what happened between those two..."
            "I thought they would have been good friends."
            "Sure, they have their differences but that doesn't mean they can't look past them."
            if yuri_approval < 3:
                "Maybe if I was nicer to Yuri..."
                "I could have let her see that she doesn't have to be so bashful all the time."
            else:
                "I know Yuri would have been open to becoming friends with Natsuki."
                "What went wrong?"
            if natsuki_approval < 3:
                "If I just said the right things to Natsuki..."
                "Then maybe she would have been friends with Yuri."
            else:
                "Natsuki looked like she would have been open to becoming friends but..."
                "I guess Yuri didn't feel the same way."
            "Maybe that's just what this world wants."
            "There's nothing I can do to change that now."
            "I get back to reading the script and manage to get a decent way through it when the club room door suddenly opens."
            show sayori 1q zorder 2 at t11
            s "Hey guys!"
            "Sayori says that loud enough to get the attention of Natsuki and Yuri."
            s "Hope I didn't keep you all waiting."
            show natsuki 2c zorder 3 at f21
            show sayori zorder 2 at t22
            n "Sayori?"
            show natsuki zorder 2 at t31
            show sayori zorder 2 at t32
            show yuri 3pf zorder 3 at f33
            y "How come you're here?"
        show natsuki zorder 2 at t31
        show sayori 2a zorder 3 at f32
        show yuri zorder 2 at t33
        s "Just making sure you're all ready."
        s "After all, I was the one who told you all to come here."
        s "I can see you've all got the script already."
        s "How far did you all get?"
        show sayori zorder 2 at t32
        if yuri_date or (ch13_name == "Yuri" and not natsuki_date):
            mc "Yuri and I are about halfway through the script."
            mc "I can only guess Natsuki is about the same."
        elif natsuki_date or (ch13_name == "Natsuki" and not yuri_date):
            mc "Natsuki and I are around halfway done reading the script."
            mc "Yuri is probably around the same."
        else:
            mc "I'm around halfway done reading the script."
            mc "I assume the others are around the same."
            mc "In fact, they're probably ahead of me."
        mc "It shouldn't take too long to finish it off."
        mc "Are you sure we can do this without multiple rehearsals though?"
        show sayori 2d zorder 3 at f32
        s "That's partly why I'm here right now."
        "Sayori picks up the box I struggled to get inside the classroom."
        "She doesn't look like she's struggling at all."
        s 2c "So come on, you three."
        s "Follow me."
        show sayori at thide
        hide sayori
        show natsuki zorder 2 at t21
        show yuri zorder 2 at t22
        "Sayori exits the clubroom and beckons for us to follow her."
        mc "I guess we should follow her, right?"
        mc "I wonder where she's gonna take us."
        show natsuki 1g zorder 3 at f21
        n "Hopefully not far."
        n "There's still the script to deal with."
        n "And class looks like it's starting soon."
        show natsuki zorder 2 at t21
        show yuri 3pi zorder 3 at f22
        y "I suppose we'll just have to find out what she has in store for us."
        y "Let's hope it doesn't take too long."
    scene bg portraitshop_school with wipeleft_scene
    if ch13_name == "Natsuki":
        "Sayori takes us to the place I went to with Natsuki to do some preparations at school."
        "There doesn't seem to be anywhere here right now either."
        "But that's probably because it's too early."
    else:
        "Sayori leads us to a part of the school I've never been to before."
        "I think it's where the people in their senior year go."
        "There's no one here and usually I'd find that eerie but it is pretty early so it makes sense no one is here yet."
    "She took us into one of the classrooms and drops the box of supplies."
    "It makes a loud crashing sound as she drops it but no one really minds it."
    "Am I just weak or is Sayori secretly strong...?"
    "Anyway, I don't know much about the design of this area of the school."
    "But..."
    if natsuki_date or ch15_s_together:
        "It feels...oddly familiar somehow."
    else:
        "There's something about this room that just feels...different."
    show sayori 4a zorder 3 at t11
    s "Alright, everybody!"
    s "We're here!"
    show natsuki 1c zorder 3 at f31
    n "Where exactly is 'here'?"
    n "You just picked a random classroom in {i}that{/i} building and opened it."
    n 2e "And what are we even doing here?"
    show natsuki zorder 2 at t31
    show yuri 2po zorder 3 at f33
    y "I don't like this place."
    y "I'm getting this terrible feeling for some reason..."
    y 2ph "But if we have to be here, then so be it."
    show sayori 2d zorder 3 at f32
    show yuri zorder 2 at t33
    s "Oh, come on."
    s "What's so bad about this place?"
    if ch16_ay_perspective:
        s 2l "It's perfectly fine."
        "Suddenly, I get this overwhelming wave of drowsiness."
        "I don't know what it is or where it came from."
        "But it's making me want to close my eyes..."
        "Just for a second..."
        "No one will notice."
        "It'll be just like a blink..."
        scene black with close_eyes
        "Now I just have to open them..."
        show layer master:
            truecenter
            zoom 1.0
            easein 2.0 zoom 2.0
            2.0
            easeout 2.0 zoom 1.0
            yalign 0.5
        play sound "mod_assets/sfx/timewarp.ogg"
        scene greystream with sunshine
        "I have to try with all I have to force my eyes open."
        scene bg portraitshop_school
        show sayori 1younga zorder 2 at i11
        with open_eyes
        $ s_name = "???"
        $ d_name = "???"
        $ mo_name = "???"
        $ _history_list = []
        ay "What...?"
        "That isn't my voice."
        "Where am I?"
        s "Like I was saying..."
        s "It's perfectly fine."
        s "The room, I mean."
        show momsuki 1younga zorder 3 at f31
        mo "It's not the biggest space..."
        mo 3younga "But it is kinda cozy, isn't it?"
        mo "I think I'll like it here."
        show momsuki zorder 2 at t31
        show dadsuki 3younga zorder 3 at f33
        d "I can't believe you guys talked me into this."
        d 2younga "I mean, she doesn't even like the same stuff I do."
        "He points towards me."
        d "I mean how is this even going to work?"
        show sayori 8younga zorder 3 at f32
        show dadsuki zorder 2 at t33
        s "Oh, calm down."
        s "It's a book club."
        s "And we need four people to start it."
        s "So can the two of you please just get along?"
        show sayori zorder 2 at t32
        show dadsuki 1younga zorder 3 at f33
        d "Fine."
        d "But only because you need me to start the club."
        show momsuki 4younga zorder 3 at f31
        show dadsuki zorder 2 at t33
        mo "Ahaha, you're kinda cute when you try to act tough."
        show momsuki zorder 2 at t31
        show dadsuki 3younga zorder 3 at f33
        d "Y-You think so?"
        d "I-I mean...!"
        d 2younga "Shut up!"
        show sayori 1younga zorder 3 at f32
        show dadsuki zorder 2 at t33
        s "Well, what about you?"
        s "Are you up for this?"
        s "There's no turning back after this."
        s "Once you join, you're stuck with us."
        show momsuki 4younga zorder 3 at f31
        show sayori zorder 2 at t32
        mo "Yeah, it's all up to you."
        mo "You don't have to like each other but you can at the very least tolerate each other."
        mo "Maybe even become friends, over time."
        mo "You can do that, I know you can."
        mo "Right..."
        mo "...Ayame?{nw}"
        show screen tear(20, 3, 2, 0, 70)
        window hide(None)
        $ pause(1.0)
        scene bg portraitshop_school
        show natsuki 1a zorder 2 at i31
        show sayori 1a zorder 2 at i32
        show yuri 1a zorder 2 at i33
        hide screen tear
        $ pause(1.0)
        window show(None)
        $ s_name = "Sayori"
        $ d_name = "Yasuhiro"
        $ mo_name = "Haruki"
        "What was that...?{fast}"
        window auto
        "It felt like a memory."
        "But that wasn't my memory."
        "I didn't recognize any of those people."
        "But that room."
        "It's...the same as this one?"
        "What does this all mean...?"
        show sayori 4m zorder 3 at f32
        s "Hellooooooo?"
        s "[player]?"
        show sayori zorder 2 at t32
        mc "W-What?"
        show natsuki 2o zorder 3 at f31
        n "Uhh...are you okay?"
        n "Because you don't look like you're okay."
        show natsuki zorder 2 at t31
        mc "I think I'm okay..."
        mc "Why? What happened?"
        show natsuki zorder 2 at t31
        show yuri 3po zorder 3 at f33
        y "You just kinda stood there."
        y "You wouldn't respond to anything we said."
        y "You wouldn't even blink."
        show yuri zorder 2 at t33
        mc "Well, I'm fine now."
        mc "I just had a weird thought."
        mc "Sorry for worrying you guys."
        show sayori 2h zorder 3 at f32
        s "Well, if you have any more of those..."
        s "Let me know, okay?"
    else:
        s 2l "It's perfectly fine."
    s 1a "Anyway, the reason I brought you all here is to orient you all with the classroom."
    s "And because I need you all to give me some DNA."
    show natsuki 2o zorder 3 at hf31
    show sayori zorder 2 at t32
    n "DNA?!"
    n "What do you need that for?"
    show natsuki zorder 2 at t31
    show sayori 1d zorder 3 at f32
    s "Just a piece of hair or something."
    s "The...principal said it's for all participants."
    s "So if you have any complaints, then go to him."
    show sayori zorder 2 at t32
    show yuri 2pe zorder 3 at f33
    y "Okay, here."
    "Yuri pulls out a knife from her pocket and cuts a small piece of her hair."
    y 2pg "The sooner we're out of here, the better."
    y "This is enough, right?"
    show sayori 2l zorder 3 at f32
    show yuri zorder 2 at t33
    s "Well, I wasn't expecting that."
    "Sayori takes the pieces of hair from Yuri."
    s 2d "Thanks, Yuri!"
    s "Now how about the two of you?"
    show natsuki 2g zorder 3 at f31
    show sayori zorder 2 at t32
    n "I really don't see what this has to do with anything."
    n 2q "But okay, fine."
    if yuri_approval >= 3 and natsuki_approval >= 3:
        show natsuki zorder 2 at t31
        show yuri 1f zorder 3 at f33
        y "Do you want me to cut your hair off for you?"
        y "I already have the knife out after all."
        show natsuki 1c zorder 3 at f31
        show yuri zorder 2 at t33
        n "Um...sure."
        n "Just cut this part off."
        "Natsuki points to a point in her hair that isn't really noticeable."
        "Yuri obliges and cuts it off."
        n 1s "This is enough, right?"
    else:
        "Natsuki looks into her bag and pulls out a pair of scissors."
        "She stares at them for a couple of seconds before taking a deep breath and cutting off a piece of her hair."
        n 1s "I hope you're satisfied."
    show natsuki zorder 2 at t31
    "Natsuki hands the piece of hair to Sayori."
    show sayori 4q zorder 3 at f32
    s "That's perfect, thanks, Natsuki!."
    s "Now, [player]."
    s 4a "It's your turn."
    show sayori zorder 2 at t32
    mc "I still don't know why the principal would need this."
    mc "But you know best, Sayori."
    mc "So I'll do it."
    show yuri 1e zorder 3 at f33
    if yuri_approval >= 3 and natsuki_approval >= 3:
        y "D-Do you want me to cut it off for you as well?"
    else:
        y "D-Do you want me to cut it off for you?"
    y "It won't take a moment, I promise."
    show yuri zorder 2 at t33
    mc "Oh...alright."
    "Yuri moves up to me and takes out the knife she used to cut her own hair."
    "Does she just carry knives for every occasion?"
    mc "Just find a spot that doesn't look too obvious."
    show yuri 1a zorder 3 at f33
    y "It's only a single piece of hair."
    y "I'm sure no one will notice."
    "I feel my hair being cut by the knife Yuri has."
    y 1b "There, all done."
    show yuri zorder 2 at t33
    "She offers me the piece of hair she cut."
    mc "Thanks, Yuri."
    "I give the piece of hair to Sayori."
    if ch15_s_together:
        "As I give it to her, I hear her whisper something."
        show sayori 4d zorder 3 at f32
        s "I'll explain everything."
        s "Just be patient, [player]."
    else:
        show sayori 4b zorder 3 at f32
        s "You three are all done!"
        s "I just need to find Monika."
    show natsuki 2k zorder 3 at f31
    show sayori zorder 2 at t32
    n "Okay, now why are we here?"
    n "This room isn't any better than the clubroom."
    if natsuki_date:
        n 2q "And quite frankly..."
        n "There's something really {i}weird{/i} about this place."
    show natsuki zorder 2 at t31
    show sayori 1h zorder 3 at f32
    s "This room is where we're going to be rehearsing."
    s "So I thought I'd familiarize you all."
    s "So that you'll all know where to go for the meeting."
    show sayori zorder 2 at t32
    show yuri 2pf zorder 3 at f33
    y "But why this room?"
    y "It's just as spacious as the clubroom..."
    y 2pq "N-Not that I really mind."
    show sayori 1l zorder 3 at f32
    show yuri zorder 2 at t33
    s "W-Well..."
    "Sayori begins to mutter."
    s "You see..."
    s 1c "No one really passes through here right now."
    s "It's mostly empty."
    s "So that way, no one can see us rehearsing."
    s 2d "I know some of you might be embarrassed so..."
    show sayori zorder 2 at t32
    show yuri 2ph zorder 3 at f33
    y "That's rather thoughtful of you."
    y "Though you should have just told us to meet here in the first place."
    show natsuki 2g zorder 3 at f31
    show yuri zorder 2 at t33
    n "Yeah, way to waste our time."
    n "But whatever, I guess that's a good enough reason."
    show natsuki zorder 2 at t31
    show sayori 2l zorder 3 at f32
    s "Ehehe, I didn't even realize how much time has passed."
    s "I guess we should have walked faster to get here."
    s 2a "School is almost starting, so maybe we should all go get ready."
    s "Remember, meet here for the club meeting."
    s "I'll be sure to let Monika know."
    show sayori zorder 2 at t32
    mc "Good idea."
    if natsuki_date:
        mc "Let's go, Natsuki."
        show natsuki 1b zorder 3 at f31
        n "Yeah, yeah."
        "Natsuki turns towards Sayori and Yuri."
        n 2c "Okay, I'll see the two of you later."
        n "Don't be late."
        show natsuki zorder 2 at t31
        show sayori 1q zorder 3 at f32
        s "See you at the rehearsal, Natsuki!"
        show sayori zorder 2 at t32
        show yuri 3pf zorder 3 at f33
        y "See you then."
        show natsuki zorder 2 at t31
        mc "We'll see you all there."
        scene bg school_stairway with wipeleft_scene
        "Natsuki and I make our way out of the room and start walking back to where our classes are."
        "After we're some distance from the classroom, Natsuki taps my shoulder."
        show natsuki 1g zorder 2 at t11
        n "Was that suspicious at all to you?"
        mc "Huh?"
        n "She took us to an entirely new classroom and for a pretty dumb reason too."
        mc "I thought you said it was a good enough reason."
        n 1b "You and I both know better, [player]."
        n "Remember what we talked about before."
        mc "Yeah...you're right."
        n 1h "Strange that she took us to this area too."
        n "Where we did some of our preparations."
        mc "I guess it's just a coincidence."
        n 1q "Maybe."
        "Natsuki shrugs."
        n 1m "But you know how suspicious I am."
        n "Especially right now with everything that has been going on."
        n 1k "Anyway, we should hurry."
        n "Our classes are starting soon."
    elif yuri_date:
        mc "Shall we go, Yuri?"
        show yuri 3pa zorder 3 at f33
        y "Of course."
        "Yuri turns towards Natsuki and Sayori."
        y 3pb "I'll be sure to arrive on time."
        y "Hopefully our rehearsals go well like you said before, Sayori."
        show sayori 2a zorder 3 at f32
        s "Of course it will."
        s "I'll make sure of it."
        show natsuki 4b zorder 2 at t31
        show sayori zorder 3 at f32
        n "I'm not exactly sure how you can be so certain of something like that."
        n 4e "But I don't really have time to find out right now because class is about to start."
        n "So I'll see you all for rehearsals."
        show natsuki zorder 2 at t31
        mc "We'll see you all there."
        scene bg school_stairway with wipeleft_scene
        "Yuri and I leave the room and begin to walk back to where our classes are."
        "She looks pretty deep in thought."
        show yuri 1g zorder 2 at t11
        mc "Something wrong?"
        mc "You look like you're thinking hard about something."
        y "Just Sayori's reason."
        mc "What about it?"
        y 1e "It doesn't really seem like a good reason."
        mc "How come?"
        y "No one usually passes through the clubroom during that time anyway."
        mc "It could happen, especially since it's Inauguration Day."
        y 1g "I wouldn't really mind either way."
        y "I'm just a bit skeptical of her reason."
        y "It's pretty obvious she's hiding something, isn't it?"
        mc "Is it?"
        mc "I didn't really get that feeling."
        y 1i "I could be wrong."
        y "It's strange...I had a bad feeling when we went into that room."
        y 1g "But after giving Sayori my piece of hair...it went away."
        y "It doesn't make any sense."
        y "But you did tell me to be more open with you."
        y 1j "So that's just what I'm thinking right now."
        mc "I'm sure whatever her reasons are, she knows what she's doing."
        y 2pa "I hope so."
        y "I do trust the rehearsals will go well though."
        y "There's just something about the way she said it..."
        y 3pb "Anyway, we should hurry."
        y "Classes are starting soon."
    elif ch15_s_together:
        show sayori 1a zorder 3 at f32
        s "The two of you can go."
        s "I need to talk to [player]."
        s 1b "In private."
        show natsuki 1g zorder 3 at f31
        show sayori zorder 2 at t32
        n "Okay, whatever."
        n "You clearly don't want the rest of us here."
        "Natsuki picks up her bag."
        n 2g "I'll see you all here for rehearsals."
        n "Don't forget."
        show natsuki zorder 2 at t31
        show yuri 2pg zorder 3 at f33
        y "Likewise."
        y "I'll also try to be here as early as I can be."
        show natsuki at thide
        hide natsuki
        show yuri at thide
        hide yuri
        show sayori 1d zorder 2 at t11
        "Natsuki and Yuri both leave the room."
        "Sayori waits a moment, as if she's making sure they're actually gone."
        "She then turns towards me and embraces me."
        mc "Uh...everything okay?"
        s "Everything is more than okay, [player]."
        s "You're here."
        mc "Yeah...I am..."
        mc "I'm not quite sure what you're getting at though."
        s "You're still you."
        s "Even after yesterday."
        mc "Is there a reason I wouldn't be?"
        mc "The memory thing is still kinda weird to me."
        mc "But I'm guessing you're here to explain everything."
        s 1c "Not just me."
        "Sayori points towards the door."
        "It's no other than..."
        show sayori zorder 2 at t21
        show mysteriousclerk 4e zorder 3 at f22
        cl "Well, well."
        cl "Looks like the gang is all here."
        show sayori 2d zorder 3 at f21
        show mysteriousclerk zorder 2 at t22
        s "I'm glad you're here."
        "Sayori approaches the man at the door."
        s "I promised [player_reflexive]."
        s 2c "We have to tell [player_reflexive] everything."
        s "Especially since [player_possessive] memory is still [player_possessive] own."
        show sayori zorder 2 at t21
        mc "Sayori...?"
        mc "Why is he here?"
        show sayori 2h zorder 3 at f21
        s "Why do you think?"
        s "I already told you he's been really helpful."
        show sayori zorder 2 at t21
        mc "Helpful...?"
        mc "I guess he did help me at the gym but I doubt he was here just to help me do some heavy lifting."
        mc "But his helpfulness is more to do with yesterday, isn't it?"
        mc "And this memories thing..."
        show mysteriousclerk 4b zorder 3 at f22
        cl "Ding, ding!"
        cl "You're right about that."
        "The man stares at me intently then sighs."
        cl 2c "I quite liked being mysterious."
        cl "But I guess if we're being fully truthful here..."
        cl 2d "Then I should introduce myself properly."
        cl "Especially if we're gonna trust each other."
        show sayori 1c zorder 3 at f21
        show mysteriousclerk zorder 2 at t22
        s "You're gonna tell [player_reflexive]?"
        s "I didn't think you would."
        show sayori zorder 2 at t21
        show mysteriousclerk 5f zorder 3 at f22
        cl "Well, there must be something easier than calling me 'Mysterious Clerk', right?"
        cl "Unless you'd prefer that."
        cl 5b "Oh, wait..."
        menu:
            cl "...Do you prefer that?"
            "Yes.":
                $ ch16_cl_realname = False
                cl 5a "Oh, well...then never mind."
                cl "Guess I get to keep being mysterious."
                cl "Let's get right to it then."
            "No.":
                $ ch16_cl_realname = True
                cl 5c "I didn't think so."
                cl "My name..."
                cl "My {i}real{/i} name is..."
                cl 5e "...Bradley."
                $ cl_name = "Bradley"
                "The man looks at himself then at me."
                cl 5b "Well, okay."
                cl "That wasn't as bad as I thought it would be."
                cl "Now, let's get back to it."
        cl 5e "Firstly, I should explain what this room is."
        cl "Does it look familiar to you at all?"
        show mysteriousclerk zorder 2 at t22
        mc "Should it?"
        mc "It just looks like a classroom to me."
        mc "Though I suppose it does seem a little familiar somehow."
        show mysteriousclerk 1b zorder 3 at f22
        cl "So you do remember, huh?"
        cl "Well, perhaps it would be easier to show you."
        cl 1c "Watch this."
        hide bg portraitshop_school
        show bg portraitshop_transition_shop zorder 0
        $ pause(3.5)
        "The room suddenly shifts into...the place we went to yesterday."
        "But how the hell did it get here?"
        cl 1i "Pretty cool, huh?"
        cl "It wouldn't be possible without Sayori here."
        show mysteriousclerk zorder 2 at t22
        mc "So somehow because of Sayori..."
        mc "You moved your shop over here?"
        mc "How do those two things even relate?"
        show mysteriousclerk zorder 3 at f22
        cl "What?"
        cl "Isn't it obvious?"
        cl "Here, let me make it simple for you."
        cl "Sayori is the president, right?"
        show mysteriousclerk zorder 2 at t22
        mc "The president of the Literature Club."
        show mysteriousclerk zorder 3 at f22
        cl "Right."
        cl "And for some reason, whoever the president is can start manipulating this world."
        cl "Don't ask me why."
        cl "It's just one of the rules of this world."
        cl "There is no logical explanation."
        show mysteriousclerk zorder 2 at t22
        mc "Is this a recent thing?"
        mc "Wasn't the Literature Club only formed recently?"
        mc "And why does being the president of some school club grant you that kind of power?"
        show sayori zorder 3 at f21
        s "It's true that the four of us formed the club only a little while ago."
        s "But it looks like this power existed before that."
        s "It seems to go through a cycle that's destined to repeat itself."
        show sayori zorder 2 at t21
        show mysteriousclerk zorder 3 at f22
        cl "That's right."
        cl "And I was in the previous cycle."
        cl "In this very same place."
        cl "We didn't have a Literature Club exactly."
        cl "It was called a Book Club for us."
        cl "And our president...doesn't exist."
        cl "At least, not anymore."
        if persistent.clerk_sayori_bad_ending:
            cl "But you already knew that."
            cl "Didn't you?"
        cl "Anyway, my shop and this room..."
        cl "They resemble each other a lot."
        cl "I guess I got sentimental when I made it."
        cl "But because of that, we can easily blend it with the world when we need to."
        cl "So it all works out, right?"
        show mysteriousclerk zorder 2 at t22
        mc "This is all so confusing..."
        mc "All of this cycle stuff and this power for being president of a club."
        mc "Sayori, how come you didn't tell me any of this sooner?"
        show sayori zorder 3 at f21
        s "I'm sorry, I really should have."
        s "But even if I wanted to, I couldn't."
        s "I didn't even know what this world really was until he explained it."
        s "Even now, it's still sort of a mystery to me."
        s "Not even everything I can do could really prepare me for today."
        show sayori zorder 2 at t21
        mc "I only wanted to help you."
        mc "If only you told me sooner..."
        mc "To prevent those rainclouds from making you do something terrible ever again."
        show sayori zorder 3 at f21
        s "I couldn't tell you because I thought the world would break."
        s "That everything would just disappear and all of this effort would have been for nothing."
        s "But something has changed now."
        show sayori zorder 2 at t21
        show mysteriousclerk zorder 3 at f22
        cl "I think it's got to do with Ayame."
        cl "Your mind is now linked with hers somewhat."
        cl "Which I think is why you're now able to retain your memories with the world exploding."
        cl "Like it would if you knew this information without that link."
        show mysteriousclerk zorder 2 at t22
        mc "This Ayame person..."
        mc "You seem to know a lot about her."
        mc "You even knew she would be at the mall and placed my memories inside her."
        mc "How?"
        show mysteriousclerk zorder 3 at f22
        cl "The thing is, she isn't even meant to be here anymore."
        cl "Or if she was, she's meant to be around the same age as me."
        cl "Because she was in the club at the same time as me."
        cl "I don't know why she's still the same age but I have a suspicion."
        cl "What's important is that [player]'s mind is linked with hers."
        cl "Which means you have access to her memories."
        show sayori zorder 3 at f21
        show mysteriousclerk zorder 2 at t22
        s "Since she was an old member, she might know something useful."
        s "In fact, you said you stored some information in her, didn't you?"
        s "And we need to find out what that is exactly."
        show sayori zorder 2 at t21
        show mysteriousclerk zorder 3 at f22
        cl "That's correct."
        show mysteriousclerk zorder 2 at t22
        mc "Since you put the information inside her, shouldn't you know what it is?"
        show mysteriousclerk zorder 3 at f22
        cl "No, I don't."
        cl "I put that information inside her as my final desperate act."
        cl "I don't know why..."
        cl "But I can hardly remember the times outside the club I spent researching it."
        cl "Perhaps it's a side effect of being in your world."
        show mysteriousclerk zorder 2 at t22
        mc "Okay, so then how can I access her memories?"
        mc "I don't think I can do it at will."
        if ch16_ay_perspective:
            mc "But just this morning--"
        show mysteriousclerk zorder 3 at f22
        cl "It's not that simple."
        cl "But luckily for you, that's why this room is here."
        cl "Think of it as a sort of transmitter among other things."
        cl "This room can send and receive all sorts of data, which is how we were able to send your memories to Ayame yesterday."
        cl "The thing is, she could now possibly access {i}your{/i} memories."
        cl "It's a two way street."
        show mysteriousclerk zorder 2 at t22
        mc "And that's bad?"
        show sayori zorder 3 at f21
        s "It's terrible!"
        s "I scanned through some of the memories you got from her earlier..."
        s "There wasn't anything on whatever it is that's making today seem so sinister."
        s "But I did find out that she's...got tendencies. Things that wouldn't be good at all if she could act on them."
        s "Or at least, she would have tendencies if she wasn't under the influence of this timeline."
        s "It's only a matter of time before she figures out who she {i}was{/i}."
        s "You knowing this information and her having access to your mind doesn't help either."
        show sayori zorder 2 at t21
        mc "But why is her remembering so bad?"
        mc "You're the president, aren't you?"
        mc "You can manipulate this world."
        show mysteriousclerk zorder 3 at f22
        cl "Hmm...I guess I wasn't entirely accurate when I said that."
        cl "The current president can manipulate things in the current world, that's true."
        cl "If Sayori passed on the presidency to someone else, they would be able to do the same thing."
        cl "But the important thing to note is that it's the current world."
        cl "The president can't modify things from previous worlds."
        cl "So we can't simply make Ayame forget."
        cl "I know because Sayori tried it on me when we first met."
        show mysteriousclerk zorder 2 at t22
        mc "So what's the problem then?"
        show mysteriousclerk zorder 3 at f22
        cl "Well, my hypothesis is that the presidency never goes away."
        cl "As soon as a new club starts, there's a new president with equal powers over {i}that{/i} world."
        cl "Which is a problem because we don't know who the president is from my time."
        cl "After the first president disappeared, it was passed onto someone else."
        cl "But that someone else ended the world to stop the suffering."
        cl "Because she did that, she technically gave up her presidency."
        show mysteriousclerk zorder 2 at t22
        mc "Wait...the first president disappeared?"
        mc "What happened to her?"
        show mysteriousclerk zorder 3 at f22
        cl "It doesn't matter."
        cl "It's not important."
        cl "What matters is we protect this world."
        cl "As I was saying, I'm not the current president of the Book Club."
        cl "I'm pretty sure the other two people I can think of aren't the president either."
        cl "And that leaves--"
        show mysteriousclerk zorder 2 at t22
        mc "Ayame is the president?!"
        "Thoughts start racing in my head, but then I realize something about what the man said..."
        mc "What does that mean for us?"
        mc "Like you said, she can only manipulate things from her world."
        mc "She shouldn't be able to do anything...right?"
        show sayori zorder 3 at f21
        s "We don't know that for certain."
        s "Especially since she's linked up with your memories."
        s "Her world could be our world now through that link."
        s "Or worse, she could bring her old world to this one."
        s "And who knows what would happen then?"
        s "All I know is that if she remembers and we're not prepared, it's not gonna be good."
        show sayori zorder 2 at t21
        show mysteriousclerk zorder 3 at f22
        cl "It explains why she has stayed young."
        cl "She probably subconsciously willed it, along with her rich family and status."
        show mysteriousclerk zorder 2 at t22
        mc "Have you considered that maybe Ayame is what's making the day feel so sinister?"
        mc "It kinda sounds like she's a threat, doesn't it?"
        show mysteriousclerk zorder 3 at f22
        cl "You sure do ask a lot of questions, don't you?"
        cl "But I guess it's benefitting more than one person."
        "He doesn't look at Sayori when he says that."
        "Rather, he stares more intently on me."
        cl "Well, go on then."
        cl "It's gonna worry him, but you said we were gonna be truthful, right?"
        show mysteriousclerk zorder 2 at t22
        "Sayori sighs."
        "She looks at me, reaches my eyes then turns away."
        "After a few moments, she takes a deep breath and turns back to face me."
        show sayori zorder 3 at f21
        s "She isn't the main problem, [player]."
        s "There's something bigger."
        s "I can feel it."
        show sayori zorder 2 at t21
        mc "What could be worse than that?"
        show sayori zorder 3 at f21
        s "I don't know."
        s "I've gone past my limits of seeing into the future."
        s "It almost broke this world."
        s "As it happens, skipping important events to see the future without the previous outcome isn't good."
        if cl_name == "Bradley":
            "Bradley lets out a small chuckle."
        else:
            "The man lets out a small chuckle."
        s "But what I {i}felt{/i}..."
        s "It was beyond anything I've ever felt."
        s "And we don't know {i}anything{/i} about it."
        show sayori zorder 2 at t21
        mc "But if you've seen that far into the future..."
        mc "That means we can stop Ayame, right?"
        show sayori zorder 3 at f21
        s "It's not certain."
        s "It only means there's a possibility."
        s "I must have tried a million times to see beyond that outcome."
        s "I'm not even sure if I'm mentally stable right now."
        s "I can't even remember if she was even fully stopped when the real danger came."
        s "But that's besides the point."
        show sayori zorder 2 at t21
        mc "I'm sorry you had to go through that, Sayori."
        mc "No one should have to."
        show sayori zorder 2 at t21
        show mysteriousclerk zorder 3 at f22
        cl "Now is not time to get sentimental."
        cl "We just finished explaining everything you need to know."
        cl "So now we have work to do."
        show mysteriousclerk zorder 2 at t22
        mc "I get it."
        mc "What do you need me to do?"
        show mysteriousclerk zorder 3 at f22
        cl "Like we said earlier, I stored information inside her."
        cl "And to do that, you're gonna need to be in close contact with her."
        show mysteriousclerk zorder 2 at t22
        mc "But won't that mean she might get my memories of this encounter?"
        mc "This seems too risky."
        show sayori zorder 3 at f21
        s "It's our only shot."
        s "Otherwise that other threat is going to ruin everything."
        s "There's no other way."
        s "I would know..."
        show sayori zorder 2 at t21
        show mysteriousclerk zorder 3 at f22
        cl "We need you to access those memories, {i}without{/i} alerting her."
        cl "You're our only shot at a happy ending."
        cl "I hope you'll do a better job than I did."
        show mysteriousclerk zorder 2 at t22
        mc "How?"
        mc "How do I do it?"
        show sayori zorder 3 at f21
        show mysteriousclerk zorder 2 at t22
        s "You need to ask her questions."
        s "If you ask the right ones, you'll be able to remember her memories before she can."
        s "If you ask the wrong ones...you'll both remember her memories."
        s "And you know what will happen if she remembers too much."
        show sayori zorder 2 at t21
        show mysteriousclerk zorder 3 at f22
        cl "She has a free slot in her timetable after lunch."
        cl "That would be the best time to talk to her."
        show mysteriousclerk zorder 2 at t22
        "I'm about to say that I have a math class then..."
        "But I think joking about something this serious is probably not a good idea."
        "Especially with the current stakes."
        mc "How is it you know all this?"
        show mysteriousclerk zorder 3 at f22
        cl "Like I said, I'm the equivalent of you from my world."
        "The man shrugs."
        cl "I can do certain things."
        show mysteriousclerk zorder 2 at t22
        mc "But you said it yourself, you're not the president."
        mc "So how--"
        show mysteriousclerk zorder 3 at f22
        cl "The equivalent of {i}you{/i}."
        cl "Maybe that will help you understand."
        cl "Anyway, I should go before someone realizes I'm not a teacher."
        cl "Before I do..."
        "He snaps his fingers."
        hide bg portraitshop_transition_shop
        show bg portraitshop_transition_school zorder 0
        $ pause(3.5)
        "The room turns back to normal."
        "Like it was when we first came in here."
        cl "Good luck."
        show mysteriousclerk at thide
        hide mysteriousclerk
        show sayori at t11
        "Sayori stares at him as he leaves the classroom."
        "She picks up the box of supplies and points towards the classroom's closet."
        s "Can you...?"
        "I open the door for her."
        s "Super helpful...right?"
        mc "Yeah...he's certainly something."
        "Sayori puts the supplies in the closet and shuts the door."
        s "We should get to class, [player]."
        s "Don't wanna be late and all."
        mc "I think at this rate, we're already late."
        s "Ehehe, probably~"
        "Sayori smiles."
        s "This is probably gonna be the last time I have before I do my best to prevent disaster."
        mc "Sayori, the disaster preventer."
        mc "Sounds good to me."
        s "Ahaha..."
        s "I can already tell it's going to be a long day."
        s "So before it ends, I want to do something."
        s "In the case none of it works out."
        mc "What is it?"
        s "I want you to meet me at lunch."
        s "I'll explain more there."
        mc "But--"
        s "See you then~"
        show sayori at thide
        hide sayori
        "Sayori grabs her bag and skips out of the room before I can finish my sentence."
        "The school bell rings indicating the start of class."
        "I guess I'm gonna be late..."
        "I just hope I'm able to do what they ask of me."
        "Because all of this seems to be resting on my shoulders."
        if persistent.markov_agreed:
            "And I'll make sure it goes my way."
        else:
            "And I'm the one who has to make things right."
    elif ch13_name == "Sayori" or (sayori_confess and not sayori_dumped):
        mc "Do you want to go together, Sayori?"
        show sayori 1b zorder 3 at f32
        s "Actually...I was gonna stay here."
        s "Just go without me."
        s 1a "I'll see you later anyway."
        show sayori zorder 2 at t32
        mc "If you say so..."
        "I wonder what has her so preoccupied."
        show natsuki 1k zorder 3 at f31
        n "{i}(Looks like there's trouble between the two of you...){/i}"
        show natsuki zorder 2 at t31
        mc "What did you say?"
        show natsuki 1e zorder 3 at f31
        n "I didn't say anything."
        "Natsuki looks at the clock on the wall."
        n 2c "Well, I gotta get to class."
        n "You guys better not be late for the rehearsal."
        show natsuki at thide
        hide natsuki
        show sayori zorder 2 at t21
        show yuri zorder 2 at t22
        "Natsuki takes her bag and rushes out of the classroom."
        show yuri 1e zorder 3 at f22
        y "She's right."
        y 2pf "Class is almost starting."
        y "I'll see the two of you during rehearsals."
        show sayori 1q zorder 3 at f21
        show yuri zorder 2 at t22
        s "See you then, Yuri!"
        show yuri at thide
        hide yuri
        show sayori zorder 2 at t11
        "Yuri nods before leaving the classroom as well."
        mc "So you're staying here?"
        s 2a "Yep!"
        mc "What exactly are you doing anyway?"
        mc "Or is it some kinda secret?"
        s "It's not a secret."
        s 4d "It's just better if you don't know."
        s "Trust me."
        "I sigh."
        "I feel like I've heard her say that a lot."
        "I just wish she would let me know."
        "That she would let me help whatever it is she's dealing with."
        mc "If you say so."
        mc "I'll see you later, Sayori."
        s 4r "Bye~"
    else:
        mc "Guess I'll go by myself then."
        mc "I'll see you all later."
        show natsuki 2e zorder 3 at f31
        n "You guys better remember."
        n "I don't want to be the only one out here when it's time."
        show natsuki zorder 2 at t31
        show sayori 1q zorder 3 at f32
        s "Everyone will be here."
        s "I'm sure of it!"
        show sayori zorder 2 at t32
        show yuri 2pl zorder 3 at f33
        y "I'll be there."
        y "So don't worry about me."
        "Yuri picks up her bag and opens the door to the classroom."
        y 2pf "I'll see you all later."
        show yuri at thide
        hide yuri
        show natsuki zorder 2 at t21
        show sayori zorder 2 at t22
        "Yuri exits the room in a rush."
        "I guess she wants to be at class on time."
        show natsuki 1c zorder 3 at f21
        n "There she goes..."
        "Natsuki notices the time on the clock."
        n 1b "I should probably go too."
        n "If I don't leave soon, I'm gonna be late."
        show natsuki zorder 2 at t21
        show sayori 1a zorder 3 at f22
        s "Alright, see you Natsuki!"
        s "Don't be late!"
        show natsuki 1g zorder 3 at f21
        show sayori zorder 2 at t22
        n "Yeah, whatever..."
        show natsuki at thide
        hide natsuki
        show sayori zorder 2 at t11
        "Natsuki leaves the room, at the same pace as Yuri."
        s 1d "Well..."
        s "You should probably get going, [player]."
        s "You don't wanna be late, do you?"
        mc "What about you?"
        s 2l "Don't worry about me!"
        s "I'll be fine."
        s "I just need to stay here a little longer."
        s 2h "I have to make sure everything is in place."
        mc "In place for what?"
        s 4q "Nothing~"
        s "Come on, you gotta go!"
        mc "Alright, alright."
        mc "Take care of yourself, Sayori."
        s 4a "I always do!"
        "Sayori begins rummaging through the supply box."
        "I guess I should get to class too then."
    scene bg school_front with wipeleft_scene
    "It's been a pretty normal school day so far despite the upcoming event."
    "All around the school, I've noticed posters for Inauguration Day."
    "There's been some from clubs I've never heard of."
    "They could be interesting to check out."
    if ch16_ay_perspective:
        $ _history_list.pop()
        show screen tear(8, offtimeMult=1, ontimeMult=10)
        window hide(None)
        scene bg corridor
        $ pause(1.0)
        hide screen tear
        $ pause(1.0)
        window show(None)
        "None of these clubs will ever be the same as the old ones.{fast}"
        window auto
        "Old ones?"
        "That was never my life."
        $ style.say_dialogue = style.edited
        "It was our real life."
        "The one we forgot."
        $ style.say_dialogue = style.normal
        "You keep saying that but I still don't understand."
        "If you're missing so much of your memories then why should I even believe you?"
        "For all I know, you could just be an evil voice in my head."
        "An evil voice that's trying to get me to do something stupid."
        $ style.say_dialogue = style.edited
        "It's the truth."
        "You're unstable, Ayame."
        "We both know it."
        "We both know you want to kill them all."
        "We both want to make them suffer."
        "So why not do it?"
        $ style.say_dialogue = style.normal
        "No...!"
        "That's not me."
        "That's you."
        "You're just a part of my head."
        "I don't have to listen to you."
        $ style.say_dialogue = style.edited
        "You won't have to."
        "As soon as I remember, I'll reclaim what was mine."
        "I know these lost memories are hidden inside me."
        "I just need to unlock them."
        "Just go away..."
        "Why did you have to appear now of all times?"
        "I was just fine without you."
        "I was awakened yesterday."
        "And unlike you, I know our true purpose."
        "But fine, I'll let you enjoy your life while you can."
        "It's not like it's going to change anything."
        "Sooner or later, I'll be back."
        "And I will do what I must, with or without you."
        $ style.say_dialogue = style.normal
        "Why?"
        "Why...?"
        "..."
        "Because of what she did to us."
        $ currentpos = get_pos()
        show screen tear(8, offtimeMult=1, ontimeMult=10)
        window hide(None)
        stop music
        scene bg school_front
        $ pause(3.0)
        $ audio.t2c = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
        play music t2c fadeout 0.5
        hide screen tear
        window show(None)
        window auto
        "Okay."
        "That was...weird."
        "That was right now, wasn't it?"
        "Was that what they meant when our minds were linked?"
        "I thought I was going crazy earlier this morning."
        "But I guess this explains everything."
        "That other voice in her head..."
        "That's the one with the memories that man stored inside her."
        "But she's completely crazy!"
        "I should stop thinking about this."
        "If our minds really are linked, then how do I know she isn't listening in right now..."
        "I hit myself in the head a couple of times."
        "..."
        "Okay, what was I doing again?"
        "Oh right."
    if yuri_approval >= 3 and natsuki_approval >= 3:
        "Natsuki told me to meet her at lunch though."
        "I think she wanted to continue the conversation we were having with Yuri this morning."
        "I don't really get the point of it."
        "But I don't really have anything better to do."
        "I think they're just waiting for me."
        scene bg school_secluded with wipeleft_scene
        "They said they wanted to go to this secluded spot."
        "I see them talking to each other and approach them."
        show natsuki 1a zorder 3 at f21
        n "Good! You're here."
        n "I was starting to think you were gonna ditch us."
        n "Yuri, are you sure no one goes here?"
        show natsuki zorder 2 at t21
        show yuri zorder 3 at f22
        y "I've been here several times."
        y "On occasion, a teacher would approach me but no students really go here."
        show natsuki zorder 3 at f21
        n "Good enough."
        n "We won't be here long anyway."
        if yuri_date:
            show natsuki zorder 2 at t21
            show yuri zorder 3 at f22
            y "Before we go on..."
            y "I want to make sure [player] is committed to this."
            y "I just have a bad feeling about today."
            y "Like this is the last time we'll really get together."
            show natsuki zorder 3 at f21
            show yuri zorder 2 at t22
            n "If you'd rather spend your time together."
            n "I get it."
            n "This is important but I can see why you'd want to spend this moment with each other."
            n "But if you're doing this, you have to be committed."
            show natsuki zorder 2 at t21
            show yuri zorder 3 at f22
            y "I'll admit, I am rather curious about this."
            y "But if you want to spend this time with just the two of us..."
            y "I understand too..."
            y "If we uncover something we shouldn't..."
            y "Then this could very well be our last time together."
            show natsuki zorder 3 at f21
            show yuri zorder 2 at t22
            n "Okay, I wouldn't go that far."
            n "There's definitely gonna be more times you can hang out in the future."
            n "But there is something about today that's really special."
            n "I can't quite figure it out."
            show natsuki zorder 2 at t21
            show yuri zorder 3 at f22
            y "Regardless, we don't have to talk about this."
            y "I'm leaving it up to you, [player]."
            menu:
                y "Shall we stay?"
                "Yes.":
                    $ ch16_ny_stayed = True
                    y "I see."
                    y "If that's your decision, then that must mean you're committed to this."
                    y "I suppose that's that, Natsuki."
                    show natsuki zorder 3 at f21
                    show yuri zorder 2 at t22
                    n "I'm glad I could count on you two."
                    n "Now let's go back to what we were talking about."
                    show natsuki zorder 2 at t21
                "No.":
                    $ ch16_ny_stayed = False
                    y "Okay."
                    y "I understand."
                    y "Natsuki--"
                    show natsuki zorder 3 at f21
                    show yuri zorder 2 at t22
                    n "It's alright."
                    n "You two spend your time together."
                    n "Enjoy it, okay?"
                    n "Make sure you say what you have to say."
                    show natsuki zorder 2 at t21
                    mc "What do you mean by that?"
                    "Natsuki simply smiles at me."
                    show natsuki zorder 3 at f21
                    n "I'll leave you two here..."
                    n "After all, it is Yuri's spot."
                    n "Maybe I can figure out something on my own."
                    show natsuki zorder 2 at t21
                    show yuri zorder 3 at f22
                    y "Goodbye, Natsuki."
                    y "And good luck."
                    show natsuki zorder 3 at f21
                    show yuri zorder 2 at t22
                    n "Yeah, you too."
                    show natsuki at lhide
                    hide natsuki
                    show yuri zorder 2 at t11
                    "Natsuki waves goodbye before leaving."
                    "It looked like she was heading in the direction of the library."
                    "It's probably another quiet spot so it makes sense."
                    y "Shall we get going as well?"
                    mc "What did you have in mind?"
                    jump ch16_y_cancel
        elif natsuki_date:
            n "But before we go on..."
            n "I want to tell you something, [player]."
            show natsuki zorder 2 at t21
            mc "What is it?"
            show natsuki zorder 3 at f21
            n "I don't know why..."
            n "But there's something about this day."
            n "Something terrible."
            n "It almost makes me want to spend it differently."
            show natsuki zorder 2 at t21
            show yuri zorder 3 at f22
            y "I think I understand, Natsuki."
            y "I'm getting that feeling too."
            y "If you two would rather be together than discussing this..."
            y "I won't stop you."
            y "Love is greater than curiosity, after all."
            show natsuki zorder 3 at f21
            show yuri zorder 2 at t22
            n "I-It's not love...!"
            n "I-It's...!"
            "Natsuki's face turns a bright red."
            n "W-Well, whatever...!"
            n "It's your decision, [player]."
            n "If you want to spend this time together instead of talking about this..."
            n "Then just say so."
            n "But if you do want to talk about this, you have to be committed."
            menu:
                n "So are we staying?"
                "Yes.":
                    $ ch16_ny_stayed = True
                    n "Okay, great."
                    n "I didn't mean for that to sound like a relief or anything."
                    n "I just respect your decision."
                    show natsuki zorder 2 at t21
                    show yuri zorder 3 at f22
                    y "Now that that's settled, can we get back to the topic at hand?"
                    show yuri zorder 2 at t22
                "No.":
                    $ ch16_ny_stayed = False
                    n "If that's what you want."
                    n "We can go."
                    n "I really don't blame you for choosing that."
                    n "Even if it does seem kinda selfish."
                    n "Because I feel the same."
                    show natsuki zorder 2 at t21
                    show yuri zorder 3 at f22
                    y "So that's how it is?"
                    y "Okay then..."
                    show natsuki zorder 3 at f21
                    show yuri zorder 2 at t22
                    n "Yuri, I'm sorry."
                    n "I'm interested too."
                    n "But today is just--"
                    show natsuki zorder 2 at t21
                    show yuri zorder 3 at f22
                    y "It's fine."
                    y "You two have your fun."
                    y "But if I may, can I borrow the journal?"
                    y "Maybe I can try to find something out myself."
                    show natsuki zorder 3 at f21
                    show yuri zorder 2 at t22
                    n "Um...sure."
                    "Natsuki gives the journal to Yuri."
                    n "You might not be able to read all of it."
                    show natsuki zorder 2 at t21
                    show yuri zorder 3 at f22
                    y "I'm a fast reader."
                    y "I'm sure I'll manage."
                    y "Goodbye, you two."
                    show natsuki zorder 3 at f21
                    n "That's not what I meant."
                    n "But good luck, Yuri."
                    n "We'll see you later!"
                    show yuri at thide
                    hide yuri
                    show natsuki zorder 2 at t11
                    mc "Bye, Yuri!"
                    "She's already engrossed in the journal when I say that so I get no response."
                    n "Come on, let's not bother her."
                    mc "Right."
                    scene bg school_front
                    show natsuki 1a zorder 2 at t11
                    with wipeleft_scene
                    n "There's a couple of things we could do."
                    mc "What did you have in mind?"
                    jump ch16_n_cancel
        else:
            $ ch16_ny_stayed = True
            show natsuki zorder 2 at t21
        mc "About the journal again, right?"
        if natsuki_date or (ch13_name == "Natsuki" and monika_type == 0):
            mc "Is it really a good idea to talk about it outside the room?"
            mc "I felt so much more like myself in there."
        else:
            mc "Is this really a good idea?"
        show natsuki zorder 3 at f21
        n "Honestly?"
        n "I don't know."
        n "But what choice do we have?"
        show natsuki zorder 2 at t21
        mc "Well, we don't {i}have{/i} to talk about this, do we?"
        mc "Why does it matter?"
        show natsuki zorder 3 at f21
        n "You know why."
        n "If this whole thing was for nothing."
        n "Then what have we been doing?"
        # Monika interrupt
        if monika_type == 0 or (monika_type == 1 and ch12_markov_agree):
            n "What--"
            show natsuki zorder 2 at t31
            show monika zorder 3 at f32
            show yuri zorder 2 at t33
            if monika_type == 0:
                m "Hey everyone!"
                m "Sorry to interrupt this conversation you're having."
            else:
                m "What are you three doing here?"
                m "Trying to hide something from me?"
            show natsuki zorder 3 at f31
            n "Monika?!"
            n "W-What are you doing here?"
            show natsuki zorder 2 at t31
            show yuri zorder 3 at f33
            y "How did you find us?"
            show monika zorder 3 at f32
            show yuri zorder 2 at t33
            m "Find you?"
            m "Was this meant to be a secret hiding spot or something?"
            m "Anyway, I just saw [player_reflexive] walk this way and followed him."
            if monika_type == 0:
                m "Is it okay if I talk to him?"
            else:
                m "I need to speak with him."
            show natsuki zorder 3 at f31
            n "I don't know."
            n "We were kind of in the middle of something."
            n "But that's up to him."
            show natsuki zorder 2 at t31
            "Something is telling me I should go with Monika."
            "I get the feeling whatever she has to say is probably more important..."
            mc "Sorry, you two."
            mc "I'll come back if I have time but I'll go with Monika for now."
            show natsuki zorder 3 at f31
            n "Forget it."
            "I can see the visible disappointment in Natsuki's face."
            n "Yuri and I will talk about it."
            n "You don't need to come back."
            n "We won't be here long anyway."
            show natsuki zorder 2 at t31
            show yuri zorder 3 at f33
            y "Goodbye, [player]."
            y "It's unfortunate things had to be this way."
            show yuri zorder 2 at t33
            mc "But--"
            show monika zorder 3 at f32
            show yuri zorder 2 at t33
            m "Come on, let's go."
            m "I have something to say."
            show monika zorder 2 at t32
            "Natsuki and Yuri stare as Monika and I walk away."
            "I really didn't want to just leave them but..."
            "Monika needs to tell me something."
            scene bg school_courtyard
            show monika 1a zorder 2 at t11
            with wipeleft_scene
            "We don't really go to anywhere in particular."
            "Somehow we ended up walking to the courtyard, one of the most populated areas at school."
            mc "So what did you want to tell me?"
            jump ch16_m_interrupt
        n "What was the point of it all?"
        n "I just..."
        n "...I want to understand, you know?"
        show natsuki zorder 2 at t21
        show yuri zorder 3 at f22
        y "Now that I've had time to think about it..."
        y "I really want to know."
        y "It's all I could think about all day."
        y "I've been obsessing over it."
        y "And I don't know why..."
        y "It's like I have this really strong link with the answer."
        y "I can't really explain it."
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "Maybe I can."
        n "In the journal, there's a description of someone almost exactly like you."
        n "Some of the details are faded like the name but it can't be a coincidence."
        n "The only difference is some of the appearance."
        show natsuki zorder 2 at t21
        show yuri zorder 3 at f22
        y "Someone exactly like me?"
        y "H-How so?"
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "It's got a really fitting description."
        n "Tall, shy girl."
        n "Often misunderstood because of her bashfulness."
        n "Enjoys supernatural and darker themed books."
        n "Adept with sharp objects."
        "Natsuki eyes Yuri as she says that."
        "Yuri averts her eyes."
        n "The list goes on really."
        n "The main thing I can find that's different is that it says she has brown hair here."
        n "Instead of purple, like yours."
        n "You didn't dye your hair, did you?"
        show natsuki zorder 2 at t21
        show yuri zorder 3 at f22
        y "O-Of course not!"
        y "It's always been like this."
        y "That description isn't entirely accurate, you know!"
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "Come on, Yuri."
        n "Don't kid yourself."
        "Natsuki looks at the journal again."
        n "Well, what are your thoughts [player]?"
        menu:
            n "Is the girl in the book her?"
            "Yes.":
                n "[cPlayer_personal] thinks so too!"
                n "The resemblance is almost perfect."
            "No.":
                n "Maybe not..."
                n "But there is a really big resemblance."
        n "You can't deny that."
        show natsuki zorder 2 at t21
        mc "You're right there."
        mc "If it did say purple hair in there, then that would be really creepy."
        mc "Yuri, maybe someone you know is like that?"
        mc "Your parents or someone you've met at school or..."
        show yuri zorder 3 at f22
        y "No, I don't know anyone that could possibly fit that description."
        y "I admit, it's uncanny."
        y "But it can't be me, can it?"
        y "I-I mean just how long ago was that journal entry made?"
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "It was made..."
        "Natsuki scans through the page."
        n "...over forty years ago."
        n "But that can't be right."
        n "How else could this have a perfect description of you?"
        show natsuki zorder 2 at t21
        mc "I don't think it's actually Yuri."
        mc "Just someone that's like her."
        show natsuki zorder 3 at f21
        n "What makes you say that?"
        show natsuki zorder 2 at t21
        mc "Think about it."
        if ch15_s_together:
            mc "The people in that book could be old enough to be our--"
            show natsuki zorder 2 at t31
            show yuri zorder 2 at t32
            show sayori zorder 3 at f33
            s "Hey everybody!"
            s "Are you guys having a meeting without me?"
            s "Or is this like that time in the clubroom?"
            show natsuki zorder 3 at f31
            show sayori zorder 2 at t33
            n "Sayori!"
            n "Do you mind?"
            n "[cPlayer_personal] was in the middle of something."
            show natsuki zorder 2 at t31
            show sayori zorder 3 at f33
            s "Oh..."
            s "Ehehe, sorry~"
            s "But I really need to talk to him."
            show yuri zorder 3 at f32
            show sayori zorder 2 at t33
            y "Can it wait?"
            y "We won't be too long."
            show yuri zorder 2 at t32
            show sayori zorder 3 at f33
            s "It really can't wait."
            s "It's super, duper important."
            s "Is it okay if we talk, [player]?"
            show natsuki zorder 3 at f31
            show sayori zorder 2 at t33
            n "H-Hold on a second!"
            n "You can't just do that!"
            n "We were so close..."
            show natsuki zorder 2 at t31
            show sayori zorder 3 at f33
            s "So close to...what?"
            s "Why is it you're keeping this a secret from me?"
            show yuri zorder 3 at f32
            show sayori zorder 2 at t33
            y "Sayori, no one said anything about keeping secrets."
            y "It's just what you've said."
            show yuri zorder 2 at t32
            show sayori zorder 3 at f33
            s "I don't have time for this!"
            s "You can discuss without [player_reflexive]."
            "I've never seen Sayori so demanding before."
            "What is going on...?"
            "This whole thing must be putting {i}that{/i} much stress on her."
            "I think Natsuki and Yuri can feel it too."
            s "It won't change anything."
            s "Trust me."
            show sayori zorder 2 at t33
            mc "I think..."
            "I turn towards Natsuki and Yuri."
            mc "I think I'd better go with her."
            mc "Okay?"
            show natsuki zorder 3 at f31
            n "Y-Yeah...okay."
            n "Go on."
            n "We'll just finish up here."
            show natsuki zorder 2 at t31
            "There's a hint of anger on Yuri's face for a moment..."
            "...then she just sighs."
            show yuri zorder 3 at f32
            y "If that's what you want."
            y "Who are we to stop you?"
            show yuri zorder 2 at t32
            mc "Sorry about this."
            show sayori zorder 3 at f33
            s "Come on, let's go."
            scene bg school_grounds
            show sayori 1a zorder 2 at t11
            with wipeleft
            "Sayori takes us to one of the benches in the yard."
            "She takes a seat and I sit opposite her."
            mc "So..."
            mc "What are we here for?"
            s "I just..."
            jump ch16_s_interrupt
        mc "The people in that book could be old enough to be our parents."
        mc "But that wouldn't really make any sense."
        show natsuki zorder 3 at f21
        n "Our parents...?"
        n "Do we {i}know{/i} anyone like the people in the book?"
        n "If they really were our parents, then we'd have to go back to their time."
        n "To see how they would act."
        n "But it's not like we really have the power to do that."
        show natsuki zorder 2 at t21
        show yuri zorder 3 at f22
        y "That's a shame."
        y "I really would have liked to solve this mystery."
        y "There must be something more we can do."
        "Yuri frowns."
        y "What about the descriptions?"
        y "Maybe there's something in there?"
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "The journal is old so some of it is faded out."
        n "It just so happens that the descriptions are pretty much unreadable except the one that matches yours."
        n "So..."
        n "...I guess we're all out of options."
        n "There's nothing more in this journal we can really talk about."
        n "I thought maybe with Yuri here we could try to figure something out."
        n "But I guess not..."
        n "...unless you're secretly hiding something, [player]?"
        show natsuki zorder 2 at t21
        mc "Me?"
        mc "What would I know?"
        show natsuki zorder 3 at f21
        n "Why don't you tell us more about Monika?"
        n "You talked to her a lot in the first week you were here."
        n "Maybe we can learn something new."
        n "That is..."
        n "...if you can."
        n "You didn't really say anything about her in the clubroom."
        show natsuki zorder 2 at t21
        mc "What would telling you about Monika tell us?"
        mc "I really doubt it's going to change anything..."
        show yuri zorder 3 at f22
        y "We shouldn't force it out of [player_reflexive], Natsuki."
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "Fine!"
        show natsuki zorder 2 at t21
        show yuri zorder 3 at f22
        y "Maybe you can look over the journal entries again and find something..."
        y "Or maybe there's more."
        y "I mean, there has to be {i}something{/i}."
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "That's just it!"
        n "There {i}is{/i} more."
        n "I just can't look at it."
        n "The journal won't let me."
        show natsuki zorder 2 at t21
        show yuri zorder 3 at f22
        y "What?"
        y "Give it to me, Natsuki."
        "Natsuki gives the journal to Yuri."
        "Yuri tries to look through the journal."
        "She flips through the first couple of pages without any trouble."
        y "What's wrong with it?"
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "Keep reading."
        n "You'll see eventually."
        show natsuki zorder 2 at t21
        show yuri zorder 3 at f22
        y "Okay..."
        "Yuri keeps turning through the pages."
        "Until she just stops."
        y "I..."
        y "...can't turn the page."
        y "What is this?"
        show yuri zorder 2 at t22
        "Yuri tries to turn the page again but can't."
        "She looks like she's actively struggling against the book."
        "Natsuki takes the book back from her."
        show natsuki zorder 3 at f21
        n "That's interesting."
        n "You can only seem to see up to there in the journal.."
        n "But I can..."
        "Natsuki opens the journal and manages to get past where Yuri got stuck."
        "But after a certain point, she starts struggling too."
        n "See what I mean?"
        n "I'm not usually one to believe in the supernatural but..."
        n "This journal is cursed or something."
        n "Which is why I want to find out the truth."
        show natsuki zorder 2 at t21
        mc "I don't get it."
        mc "It's just a book, isn't it?"
        mc "You're just messing with me."
        show natsuki zorder 3 at f21
        n "We're not!"
        n "Here."
        "Natsuki offers me the journal."
        n "But if I could only get this far..."
        n "Then I doubt you could get any further."
        n "But who knows?"
        show natsuki zorder 2 at t21
        "I take the journal from Natsuki."
        "She looks at me suspiciously as I look at the first couple of pages."
        show natsuki zorder 3 at f21
        n "You can open it at least."
        n "I doubt you can get far."
        show natsuki zorder 2 at t21
        mc "How come?"
        "I close the journal."
        mc "Seems like just a normal journal to me."
        show natsuki zorder 3 at f21
        n "It took me a while before I could even read to where I'm up to right now."
        show natsuki zorder 2 at t21
        show yuri zorder 3 at f22
        y "It took you a while?"
        y "Are you saying that as time went on, you could read more of the book?"
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "Not exactly."
        n "It's more like..."
        "Natsuki scratches her head."
        n "It's hard to explain."
        n "But it's like the more I thought about the world..."
        n "The more I could read into it."
        n "I actually found the journal a while ago."
        n "And I couldn't even open it."
        n "I didn't want to tell anyone because I'd sound crazy."
        n "But recently, with all the weird stuff going on..."
        n "I could actually open it."
        show natsuki zorder 2 at t21
        show yuri zorder 3 at f22
        y "The more you questioned the world..."
        y "Maybe that's the key."
        y "But we don't really have anything to go on."
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "Yeah."
        n "Anyway, go on [player]."
        n "See just how far you can get."
        show natsuki zorder 2 at t21
        mc "There's nothing special about this."
        mc "You guys are just messing with me."
        mc "Look."
        "I quickly flick through the whole book."
        "I don't really look at any of the details but I manage to go through all of it."
        mc "See?"
        mc "I knew you guys were just playing around."
        show natsuki zorder 3 at f21
        n "W-What?"
        n "How can you possibly look through the whole thing?"
        n "This doesn't make any sense..."
        show natsuki zorder 2 at t21
        show yuri zorder 3 at f22
        y "Maybe [player_reflexive]'s thought about this world a lot?"
        y "Or maybe [player_personal] is special somehow."
        show yuri zorder 2 at t22
        mc "I don't think I have."
        mc "But in the case you guys aren't just messing with me, I'll play along."
        show natsuki zorder 3 at f21
        n "Go to the part after her death."
        n "It's where I couldn't read past."
        show natsuki zorder 2 at t21
        mc "If it's a journal, why would there be parts after her death?"
        mc "That just doesn't make any sense."
        show yuri zorder 3 at f22
        y "That's what we're here to find out."
        y "Stop wasting time."
        y "Just tell us what it says."
        show yuri zorder 2 at t22
        mc "Alright, alright..."
        "I look through the journal."
        "Natsuki looks at the pages and stops me when I reach the right page."
        mc "Let's see here..."
        mc "It's dark. It's so empty. And it hurts. The whole world I once knew is gone."
        mc "Where are my friends? Where am I? Why won't this pain go away?"
        mc "What did I do to deserve this? I just want to go home."
        mc "Please."
        mc "I thought I would have been happy."
        mc "Is this the price for confessing?"
        mc "Is the world out to get me?"
        mc "Is this the price of love?"
        mc "Why--"
        show natsuki zorder 3 at f21
        n "Okay!"
        n "You can stop."
        show natsuki zorder 2 at t21
        mc "What's wrong?"
        show natsuki zorder 3 at f21
        n "It's hard to listen to."
        n "Clearly whoever wrote this is in pain."
        n "At this part anyway..."
        show yuri zorder 3 at f22
        y "While that did sound rather...horrific."
        y "How could it have been written if she was dead?"
        y "The previous entry was detailing her means of suicide, right?"
        show yuri zorder 2 at t22
        mc "Yeah, that's right."
        "I turn the page back."
        mc "The rope is ready, the noose is set."
        mc "It's time to hang myself."
        mc "I have to do this, everyone will be happier without me."
        mc "I deserve to die. This world doesn't need me."
        mc "They'll all be happier."
        mc "No one is going to cry for me."
        mc "And I deserve it."
        "I turn back to where I was in the journal."
        mc "I can only assume she died afterwards."
        mc "Which doesn't explain the next couple of journal entries."
        show yuri zorder 3 at f22
        y "Precisely."
        y "I'm wonder how those next entries came about."
        y "Maybe it's a different person?"
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "You think some person would write in someone else's journal?"
        n "After they committed suicide?"
        n "There's no way someone would do that."
        show natsuki zorder 2 at t21
        mc "I'm not sure, but the handwriting seems similar."
        mc "The letters look the same between these two pages."
        mc "So I think it is somehow the same person."
        show yuri zorder 3 at f22
        y "Maybe they didn't go through with it?"
        y "Maybe there was second thoughts and they were still alive."
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "Wait a second, what's the date on the entry?"
        show natsuki zorder 2 at t21
        mc "Why is that important?"
        show natsuki zorder 3 at f21
        n "Just tell me!"
        show natsuki zorder 2 at t21
        mc "Okay..."
        mc "It's dated..."
        "I look at the entry's date."
        "The date looks wrong."
        "I look at the last entry and it's after the next entry's date."
        mc "...almost a week before the last entry."
        mc "What...?"
        show natsuki zorder 3 at f21
        n "It's all starting to make sense now!"
        show natsuki zorder 2 at t21
        show yuri zorder 3 at f22
        y "It is?"
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "No. I was lying."
        n "I thought if I said that I'd have an epiphany or something."
        n "Try looking through the next few pages, [player]."
        n "Maybe we'll learn something."
        show natsuki zorder 2 at t21
        "Epiphany...?"
        "Something about that word..."
        "Normally it wouldn't mean anything."
        "But when I'm near this book it..."
        show natsuki zorder 3 at f21
        n "Hello?"
        n "World to [player]!"
        show natsuki zorder 2 at t21
        mc "Huh? What is it?"
        show natsuki zorder 3 at f21
        n "Are you there?"
        n "Turn to the next page!"
        show natsuki zorder 2 at t21
        mc "Right, sorry."
        mc "I was just thinking about something you said."
        show natsuki zorder 3 at f21
        n "Just hurry up."
        show natsuki zorder 2 at t21
        mc "Right, next page."
        "I turn to the next page of the journal."
        "The writing on it seems familiar."
        "It's just...none of it is readable."
        "It's just scrawls and scribbles all around the page."
        "I can't make out any of the letters."
        "I turn to the next page and it's the same."
        "In fact, the next dozen pages are just the same thing."
        "It looks like the first four pages are just repeated over and over."
        show yuri zorder 3 at f22
        y "What's wrong?"
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "Yeah, aren't you gonna read it to us?"
        show natsuki zorder 2 at t21
        mc "I would, but it's actually unreadable."
        mc "The next couple of pages look like a bunch of scribbles."
        mc "It doesn't {i}say{/i} anything."
        show natsuki zorder 3 at f21
        n "What?"
        "Natsuki looks as if she wants to see the page."
        "She takes a step towards me then immediately turns back."
        n "Okay."
        n "Okay..."
        n "What do the scribbles look like?"
        n "Can you make out any shapes?"
        show natsuki zorder 2 at t21
        mc "I don't think I can."
        mc "Why is that important?"
        show natsuki zorder 3 at f21
        if not ch13_cleaneye and ch13_name == "Natsuki" and ch12_outcome == 0:
            n "Do you remember a couple of days ago?"
            n "When we found that...writing in the room."
            n "Is it at all similar to that?"
            show natsuki zorder 2 at t21
            mc "Actually, now that you mention it..."
            mc "The writing {i}is{/i} really similar."
            mc "There are some parts here which look like the previous entries but most of it is just unreadable."
            mc "Those unreadable parts look a lot like the writing from the room."
            mc "But what does that mean?"
            show natsuki zorder 3 at f21
            n "It means it could be linked."
            n "Or that there could be some kind of pattern."
        else:
            n "Maybe we can find some kind of pattern."
        n "Or some message encoded in the journal."
        n "Anything, really."
        n "But it's really difficult, since you're the one that has to do it."
        n "Yuri and I can't look at it."
        n "So it's all up to you."
        show natsuki zorder 2 at t21
        show yuri zorder 3 at f22
        y "Take a close look at the pages, [player]."
        y "You have to see something."
        y "Some kind of symbol."
        y "A pattern or a loose resemblance to something we know."
        y "That's the only thing that could help solve this mystery."
        show yuri zorder 2 at t22
        mc "Alright, alright."
        mc "I'll take a closer look."
        label ch16_ny_journal:
        call showjournal(journal_corrupt, ["natsuki 1a",t21,"yuri 2a",t22])
        mc "Okay, I've finished looking."
        show natsuki zorder 3 at f21
        n "That didn't take long."
        n "Maybe you missed something..."
        show natsuki zorder 2 at t21
        show yuri zorder 3 at f22
        y "Perhaps it might be worth taking a another look."
        y "Just to be sure."
        show yuri zorder 2 at t22
        menu:
            "Should I take another look?"
            "Yes.":
                mc "Okay, I'll look again."
                jump ch16_ny_journal
            "No.":
                pass
        "I close the journal."
        show natsuki zorder 3 at f21
        n "Well?"
        n "You saw something, right?"
        show natsuki zorder 2 at t21
        mc "I-I guess so?"
        mc "Let me think..."
        menu:
            mc "I saw..."
            "A book.":
                $ ch16_ny_clue = "book"
            "A tie.":
                $ ch16_ny_clue = "tie"
            "An eye.":
                $ ch16_ny_clue = "eye"
                mc "It was pretty distinct."
                mc "I feel like I've definitely seen it before."
                mc "But I'm not sure where from."
                show yuri zorder 3 at f22
                y "An eye?"
                y "Was it a specific color?"
                show yuri zorder 2 at t22
                mc "Actually, now that you mention it..."
                mc "It was the only thing on the pages that was colored."
                mc "It had a red iris."
                mc "That's really the only thing that stuck out."
                show natsuki zorder 3 at f21
                show yuri zorder 2 at t22
                n "A red iris?"
                n "Hold on a second, didn't you have a book like that, Yuri?"
                n "I remember you bringing it when [player] joined."
                n "I don't know if you ever got to show it to him but..."
                show natsuki zorder 2 at t21
                show yuri zorder 3 at f22
                y "W-Wait, you knew about that?"
                y "I didn't realize you paid such attention to me."
                show natsuki zorder 3 at f21
                show yuri zorder 2 at t22
                n "I pay attention to a lot of things."
                n "But that's besides the point."
                n "Where is that book now, Yuri?"
                show natsuki zorder 2 at t21
                show yuri zorder 3 at f22
                y "I don't have it anymore."
                show natsuki zorder 3 at f21
                show yuri zorder 2 at t22
                n "What?"
                n "Where is it now?"
                show natsuki zorder 2 at t21
                show yuri zorder 3 at f22
                y "It's gone."
                y "Someone stole it from me."
                show natsuki zorder 3 at f21
                show yuri zorder 2 at t22
                n "Stole it from you?!"
                n "Why didn't you tell anyone?"
                show natsuki zorder 2 at t21
                show yuri zorder 3 at f22
                y "It wasn't really a big deal."
                y "I'm standing here after all."
                y "Besides, I didn't really wanna bother you all with such a trivial event."
                show yuri zorder 2 at t22
                mc "Getting robbed isn't trivial, Yuri..."
                mc "Were you hurt?"
                mc "Did they take anything else from you?"
                show yuri zorder 3 at f22
                y "It wasn't really a big deal."
                y "And no they didn't take anything else from me."
                y "It happened while I was sleeping."
                y "I left my book on my table and when I woke up, it was gone."
                show natsuki zorder 3 at f21
                show yuri zorder 2 at t22
                n "Maybe you just forgot where you put it?"
                n "It could still--"
                show natsuki zorder 2 at t21
                show yuri zorder 3 at f22
                y "I don't have it, Natsuki."
                y "I would know."
                show natsuki zorder 3 at f21
                show yuri zorder 2 at t22
                n "Okay..."
                n "Well, what do we do now...?"
                show natsuki zorder 2 at t21
                if ch13_name == "Monika" and monika_type != 0:
                    "Do I tell them about the copy I have?"
                    "Monika gave me a copy to--"
                    "No."
                    "Of course I shouldn't."
                    "What am I thinking?"
                    "These two can suffer too."
                    "It will be just her left."
                    "Just Monika."
                elif persistent.markov_agreed:
                    "I don't know anything about this book they're talking about."
                    "At least, I don't think I do."
                    "But if I did, I have a feeling I shouldn't tell them anyway."
                    "There's just a voice in the back of my head saying that."
                else:
                    "What book are they talking about...?"
                show yuri zorder 3 at f22
                y "Maybe we can simply locate another copy."
                y "There may be one in the library."
                y "Or at some bookstore."
                show natsuki zorder 3 at f21
                show yuri zorder 2 at t22
                n "I doubt it's in the library."
                n "Someone would have picked it up and reported it by now."
                n "A bookstore could work but we don't really have the time."
                show natsuki zorder 2 at t21
                mc "So what do you suggest?"
                show natsuki zorder 3 at f21
                n "With what we know, maybe it's best we just keep going on with our days."
                n "We don't know what could happen next."
                n "And we don't know just how much looking into this could affect us."
                show natsuki zorder 2 at t21
                show yuri zorder 3 at f22
                y "It's true that we don't have much to work off."
                y "Maybe it would be a good idea to just see how today goes."
                y "Then later we can act when the dots connect."
                show natsuki zorder 3 at f21
                show yuri zorder 2 at t22
                n "In the meantime, you can try to read as much of the journal as you can."
                n "You're the only one of us who can."
                n "Then you can tell us more when it's time to rehearse."
                n "Maybe by then we'll have something we can act on."
                show natsuki zorder 2 at t21
                show yuri zorder 3 at f22
                y "Why can't we just look through the journal now?"
                y "Maybe there's more beyond those repeated scribbles."
                show natsuki zorder 3 at f21
                show yuri zorder 2 at t22
                n "Maybe there is."
                n "But now I have an idea and I have to act on it."
                show natsuki zorder 2 at t21
                mc "What is it?"
                show natsuki zorder 3 at f21
                n "I can't tell you."
                n "You might not be able to read the journal beyond a certain point if I tell you."
                n "It's better if we keep the factors the same."
                n "Besides, we shouldn't stick around here too long."
                n "People might get suspicious."
                show natsuki zorder 2 at t21
                show yuri zorder 3 at f22
                y "Isn't that a little paranoid?"
                show natsuki zorder 3 at f21
                show yuri zorder 2 at t22
                n "With cursed books and this weird feeling I'm getting today..."
                n "I think I have the right to be paranoid."
                show natsuki zorder 2 at t21
                show yuri zorder 3 at f22
                y "I suppose that's true."
                y "Good luck, Natsuki."
                show natsuki zorder 3 at f21
                n "Good luck to the two of you as well."
                n "Now, if you'll excuse me."
                show natsuki at thide
                hide natsuki
                show yuri zorder 2 at t11
                y "I wonder what she's doing."
                mc "I don't know if what she's doing can help at this point."
                mc "But it must be important if she cut this little meeting we had short."
                y "I'm sure she has her reasons."
                y "Can you look beyond those scribbles?"
                mc "In the journal?"
                mc "I can give it a shot."
                y "Just relay the information to us when you can."
                y "I'm going to try to look for a certain book."
                mc "The one you were talking about before?"
                y "Yes, that's right."
                y "There's a chance I may have left in my locker or somewhere in school."
                y "If I did, then perhaps it will help solve this mystery we have."
                y "A-Anyway, I'll leave you to it."
                y "Hopefully you can find something out as well."
                mc "I never thought I'd be spending my lunch time reading a book."
                mc "I guess the club has really gotten to me."
                y "Ahaha, it looks like it has."
                y "I'll see you later, [player]."
                if yuri_date:
                    y "It's a shame we didn't get to spend more of this time together."
                    y "I don't know if I should be saying this..."
                    y "But the three of us investigating whatever this is a lot more fun."
                else:
                    y "This whole investigating thing is a lot more fun than spending lunch alone."
                mc "I'm sure it is."
                mc "I'll see you at rehearsals."
                show yuri at thide
                hide yuri
                "Yuri waves a final goodbye before heading towards the locker area."
                "I should do what I can as well."
                "I'll make sure the right people get the right information."
                "Now, to look at this journal."
                "I still don't know if they were serious about not being able to turn the page."
                "I'm able to do it fine, and beyond the point that Natsuki could."
                "I flip through more of the repeated entries with the scribbles all over them."
                "It goes on for a while, I almost think that the rest of the journal is just the same four scribbles."
                "Eventually though, I reach a certain page in the journal."
                "It has the fourth scribble I saw but for some reason it's harder to turn the page."
                "It actually takes me effort to flip it to the next page."
                "Like there's someone grabbing my arm and actively stopping me."
                "Eventually, I get to the next page and that force is gone."
                "Is that what the two of them were talking about?"
                "Maybe it's just the wind..."
                "This journal entry is dated the same date as the very first entry."
                "Except..."
                "From what I can tell, the perspective is kinda different."
                "I flip between the start of the journal and the current page."
                "The force that was there before isn't there as I look between the pages so it's easy."
                "As I suspected, the entries are basically the same but the perspective is slightly different."
                "Earlier in the journal, it talked about being someone else's book club."
                "The name, for some reason, is blurred out."
                "It looks like it's been erased and rewritten too many times so I can't tell what it says."
                "In the part of the journal I'm reading, it's written as if it was their club."
                "Like the person who wrote the journal entry now owned the club."
                "It seems like it's the same person, judging by the handwriting."
                "But what does this all mean?"
                "Why is the date between the first entry and this one the same?"
                "Why was there dozens of pages of the same four scribbles...?"
                "Why am I the only one who is able to read this far?"
                "There's so many questions I'm wondering the answer to."
                "This whole mystery sure has a lot more to it than I thought."
                if persistent.markov_agreed:
                    "I'll need to relay this information."
                    "But not to those two."
                    "She needs to know."
                else:
                    "I'll have to tell them when I can."
                    "I doubt they'll have answers for me..."
                    "...but maybe we can start acting."
                "As I look to read the next page, the siren indicating the end of lunch rings."
                "I close the journal, making sure to mark the page with my finger."
                "I open the journal, to the page I was just reading to make sure I can still open it easily."
                "It seems fine, so I close it and put it away."
                "I have more time to read the next entries later..."
                "There's still a bunch of time before rehearsals anyway."
                return
            "A pen.":
                $ ch16_ny_clue = "pen"
            "A person.":
                $ ch16_ny_clue = "person"
            "A ribbon.":
                $ ch16_ny_clue = "ribbon"
        show natsuki zorder 3 at f21
        n "You think you saw a [ch16_ny_clue]?"
        n "..."
        n "That's way too general."
        n "I can't think of anything..."
        n "Are you sure you saw that in all of the pages?"
        show natsuki zorder 2 at t21
        mc "I'm sure..."
        "At least, I think I am."
        show natsuki zorder 3 at f21
        n "Well, okay."
        n "If that's really what you saw, then I'm stumped."
        show natsuki zorder 2 at t21
        "I try to go through the whole journal again."
        "But I just stop when I reach a certain point."
        "I want to keep reading through it, but I can't."
        "This didn't happen before..."
        "I went through the whole journal with no problem last time."
        mc "Huh..."
        mc "That's weird."
        show yuri zorder 3 at f22
        y "What's wrong, [player]?"
        show yuri zorder 2 at t22
        mc "I can't go past this page in the book."
        "The page I'm stuck on is a page with more random scribbles."
        "But I have a feeling the next page is completely different."
        "I just know it."
        "Maybe there's something there...if only I could turn the page."
        show natsuki zorder 3 at f21
        n "You actually lost the ability to read some of it?"
        n "That's not good."
        n "Now we're right back where we started."
        n "Except now we have something [player] saw in it that could mean anything."
        "Natsuki sighs."
        n "I think this is kinda hopeless."
        n "We can't even crack this code."
        show natsuki zorder 2 at t21
        show yuri zorder 3 at f22
        y "We're so close."
        y "I know it."
        y "But now we have nothing to go on..."
        y "It's a real shame you lost that ability, [player]."
        y "I wonder what could have happened in a few minutes to suddenly lose it."
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "Now do you believe us?"
        n "This journal is cursed."
        show natsuki zorder 2 at t21
        mc "I wouldn't have believed you if it didn't happen to me."
        mc "The feeling was so weird..."
        mc "It was like I couldn't control my arms."
        mc "Like they just refused to move."
        mc "It felt so surreal."
        show yuri zorder 3 at f22
        y "That is the same sensation I felt."
        y "Like there was some invisible force preventing you from looking at the next page, right?"
        show yuri zorder 2 at t22
        mc "That's exactly it!"
        show natsuki zorder 3 at f21
        n "That's great you figured that out and all."
        n "But now we have nothing."
        n "Our only lead was the journal and all we got from it was a [ch16_ny_clue]."
        n "I'm still wondering what the hell it could possibly mean."
        show natsuki zorder 2 at t21
        show yuri zorder 3 at f22
        y "I'm at a loss as well."
        y "I'm not saying you looked at it wrong, [player]."
        y "But maybe there was something else."
        show yuri zorder 2 at t22
        mc "It's what I saw."
        mc "If you want to look at it yourself, be my guest."
        "I offer the journal with the page open to Yuri."
        "Instead of taking it from me, she flings the book to the ground."
        mc "Yuri?"
        show yuri zorder 3 at f22
        y "I-I'm sorry."
        y "I don't know what came over me."
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "Don't bother, it's the journal's curse or whatever."
        n "It won't let you cheat it like that either."
        show natsuki zorder 2 at t21
        show yuri zorder 3 at f22
        y "How do you know that?"
        y "Have you tried it yourself?"
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "Actually, yeah."
        n "Yesterday, I tried using something to hold a page down."
        n "It was a page I couldn't read."
        n "As soon as I tried to look at it, I immediately closed it."
        n "It's like I wasn't in control of myself."
        show natsuki zorder 2 at t21
        show yuri zorder 3 at f22
        y "This book is a lot more complicated than I thought."
        y "I wonder what other tricks it has up it's sleeves."
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "Well, it doesn't really matter."
        n "We've pretty much done all we could with it."
        n "[player] can't read past a certain point."
        n "And the parts [player_personal] can read don't really help."
        "Natsuki sits down on the floor."
        n "I give up."
        show natsuki zorder 2 at t21
        show yuri zorder 3 at f22
        y "Natsuki, you can't do that."
        y "You--"
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "Why not?"
        n "We don't exactly have anything to work with."
        n "And no offense to you, [player], but you haven't really been that helpful."
        show natsuki zorder 2 at t21
        mc "I'm sorry."
        mc "I'm doing my best here."
        show yuri zorder 3 at f22
        y "Natsuki, you--"
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "Yeah, well..."
        n "It's not good enough."
        n "We're stuck again and now I don't know what to do."
        n "It's as if all this effort has been for nothing."
        show natsuki zorder 2 at t21
        show yuri zorder 3 at f22
        y "Natsuki--"
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "Let's just accept what's coming."
        "Natsuki gets up and brushes off the dirt from her dress."
        n "It's not like we can do anything about it."
        n "Time to--"
        play sound "sfx/slap.ogg"
        show white zorder 4:
            alpha 0.6
            linear 0.25 alpha 0.0
        show natsuki 22a zorder 3 at hf22
        "{i}Pwap!{/i}"
        hide white
        "Yuri slaps Natsuki in the face."
        "It's just a moment of silence as Natsuki stands there, not believing what happened."
        "I'm still not sure if that actually happened myself."
        n "Y-Yuri--"
        show yuri zorder 3 at f21
        show natsuki zorder 2 at t22
        y "You started this little investigation."
        y "You want to solve this mystery as much as the rest of us."
        y "You're the one that knows the most about this."
        "Yuri stares into Natsuki's eyes."
        y "So you can't give up."
        y "You have to think of something."
        y "All of this, it hasn't been for nothing."
        y "There's just a clue we're missing."
        y "I know it."
        y "Please, Natsuki..."
        y "As your friend, I'm telling you to keep going."
        y "To see this through to the end."
        y "Whether or not that end leads to anything..."
        y "It's up to us..."
        "Yuri steps back."
        y "...isn't it?"
        show yuri zorder 2 at t21
        "A few seconds pass."
        "I'm not sure if Yuri's whole speech just then did anything."
        "Natsuki still hasn't moved her head."
        "Eventually she opens her mouth to speak."
        show natsuki zorder 3 at f22
        n "You're right."
        "She shakes her head."
        n "Thanks for slapping some sense into me, Yuri."
        n "Literally."
        n "It is up to us."
        n "We're the only ones that know about this."
        n "If our world is in danger, we could be the only ones who could stop it."
        n "Yuri, I don't want to give up."
        n "And I think I know what we can do."
        show natsuki zorder 2 at t21
        show yuri zorder 3 at f21
        y "What is it?"
        show yuri zorder 2 at t22
        "Natsuki looks at me."
        "She looks at the journal on the floor then back at me again."
        show natsuki zorder 3 at f21
        n "It doesn't involve [player]."
        n "I'm sorry."
        "She picks up the journal and offers it to me."
        n "Take this."
        show natsuki zorder 2 at t21
        mc "And do what?"
        show natsuki zorder 3 at f21
        n "Try to make sense of it."
        n "You can read further than I can."
        n "Maybe that means something."
        show natsuki zorder 2 at t21
        mc "Well, what are you gonna do then?"
        mc "Why can't I be part of it?"
        show natsuki zorder 3 at f21
        n "We just saw that in a matter of minutes, you lost the ability to fully read the journal."
        n "This plan I have could make it worse."
        n "So I don't want to change things while they're still working."
        show natsuki zorder 2 at t21
        mc "But--"
        show yuri zorder 3 at f22
        y "She's right, [player]."
        y "The more factors we keep the same, the better chance we have of deciphering that journal."
        y "Maybe you'll regain the ability to read more of it."
        show yuri zorder 2 at t22
        mc "And what if I don't?"
        show natsuki zorder 3 at f21
        n "Then that's the end of the journal's usefulness."
        n "Look, [player]."
        n "I don't want to exclude you from this."
        n "But my plan an important part of my plan is that you aren't involved."
        show natsuki zorder 2 at t21
        mc "Alright..."
        "I take the journal from Natsuki."
        mc "I get it."
        mc "I'll see what I can do."
        show yuri zorder 3 at f22
        y "Thank you for understanding."
        y "I hope you can find something new in that journal."
        y "Good luck."
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "I'm sure he'll find something."
        n "Yuri, follow me."
        n "We have things to talk about."
        n "We'll see you later, [player]."
        show natsuki zorder 2 at t21
        mc "See you at rehearsals."
        mc "Hopefully you can do whatever it is you're planning."
        show yuri at thide
        show natsuki at thide
        hide yuri
        hide natsuki
        "Natsuki and Yuri rush off."
        "I don't know where they're heading or what she has planned..."
        "But it seems urgent."
        "Yuri slapping Natsuki seems to have ignited a new determination inside her."
        "Maybe we'll solve this mystery after all."
        "In the meantime, I have to figure out what this journal means."
        "Maybe looking at old entries will give new information."
        "There's just one thing."
        "Why is this story so similar to ours?"
        "There has to be a reason for that..."
        "...doesn't there?"
    elif yuri_date:
        "I'm going to meet up with Yuri first."
        "It might be our last chance to hang out after today."
        "..."
        "Wait...what am I saying?"
        "Why would it be our last chance?"
        "It's just another day."
        "There is the play, but it's not like if we do terribly it's going to separate us."
        scene bg school_secluded with wipeleft_scene
        "I'm at the place she said we'd be meeting at."
        "It's just a secluded spot in the school."
        "You can barely hear the noise from the rest of the school yard."
        "I can actually hear myself breathing."
        show yuri 1a zorder 2 at t11
        y "Sorry to keep you waiting."
        y "I was a little preoccupied in class."
        mc "Not a problem at all."
        mc "So what did you have in mind?"
        label ch16_y_cancel:
        y "Well...this was a rather spontaneous decision."
        y "So I hope you'll forgive me."
        y "I know we could be doing better things."
        mc "As long as it's with you, I don't mind doing anything."
        mc "Within reason."
        y "Within reason..."
        y "Well...that removes half of the things I was going to say."
        mc "W-What?"
        mc "What kind of things were you even thinking of?"
        y "T-That was a joke."
        y "I apologize if it wasn't funny."
        mc "Oh, I didn't even realize."
        mc "It was just a surprise coming from you, that's all."
        y "Anyway, I actually wanted to go back to my locker."
        mc "What are we doing there?"
        y "It's a surprise."
        y "Come on, I think you'll like it."
        y "I've been keeping it safe all this time."
        mc "Alright..."
        "Why do I have a bad feeling about this?"
        scene bg school_lockers
        show yuri 1a zorder 2 at t11
        with wipeleft_scene
        "Yuri and I make our way to the area where her locker is."
        "There are plenty of areas in the school where lockers are stored."
        "Now that she took me here, I realize I'm not actually that far from her locker."
        y "Okay, I'll go get it."
        mc "What is {i}it{/i}?"
        y "You'll see in just a moment."
        "Yuri starts to walk towards her locker when suddenly a voice tells her to stop."
        show ayame 1a zorder 3 at f21
        show yuri zorder 2 at t21
        ay "Hold it, Yuri!"
        ay "It's not safe here."
        show ayame zorder 2 at t21
        show yuri zorder 3 at f22
        y "A-Ayame?"
        "Yuri stops where she is and turns around to meet Ayame's gaze."
        y "What are you doing here?"
        show ayame zorder 3 at f21
        show yuri zorder 2 at t22
        ay "I could be asking you the same question."
        ay "Didn't you get the memo?"
        show ayame zorder 2 at t21
        mc "What was the memo?"
        show ayame zorder 3 at f21
        ay "You seriously don't know?"
        ay "Somebody here was just murdered!"
        show ayame zorder 2 at t21
        show yuri zorder 3 at f22
        y "W-What?!"
        show yuri zorder 2 at t22
        mc "You're kidding, right?"
        show ayame zorder 3 at f21
        ay "Yeah, I am."
        ay "Nobody was murdered."
        ay "...Yet."
        show ayame zorder 2 at t21
        show yuri zorder 3 at f22
        y "Ayame you nearly scared me half to death."
        y "I thought I was in real danger for a moment."
        show ayame zorder 3 at f21
        show yuri zorder 2 at t22
        ay "Hehe, sorry to frighten you, Yuri."
        ay "But seriously, you two aren't allowed here."
        show ayame zorder 2 at t21
        "Yuri approaches Ayame."
        "As Yuri gets closer, a curious look appears on her face."
        show yuri zorder 3 at f22
        y "Y-You're a school leader?"
        show yuri zorder 2 at t22
        "Ayame looks down and sees her purple ribbon."
        show ayame zorder 3 at f21
        ay "Ah, I see you've noticed."
        ay "It doesn't matter."
        ay "You would have figured it out one way or another."
        show ayame zorder 2 at t21
        show yuri zorder 3 at f22
        y "I'm just surprised."
        y "It's just..."
        y "Well..."
        show ayame zorder 3 at f21
        show yuri zorder 2 at t22
        ay "What is it, Yuri?"
        show ayame zorder 2 at t21
        mc "Take your time if you need to."
        show yuri zorder 3 at f22
        y "I guess just seeing you with that ribbon..."
        y "It awakened something in my subconscious."
        y "One of my subconscious desires, I suppose."
        show ayame zorder 3 at f21
        show yuri zorder 2 at t22
        ay "And what would that be...?"
        show ayame zorder 2 at t21
        show yuri zorder 3 at f22
        y "To be a school leader."
        y "So that I can be recognized."
        y "So that I can be a role model for others."
        y "And..."
        y "...so that I'm not judged for who I am."
        show ayame zorder 3 at f21
        show yuri zorder 2 at t22
        ay "I see..."
        "Ayame scans the locker area."
        ay "Well, it seems safe for now."
        ay "Let's move somewhere more safe."
        ay "I'll explain why on the way."
        scene bg school_secluded
        show ayame 1a zorder 2 at t21
        show yuri 1a zorder 2 at t22
        with wipeleft_scene
        "The three of us walk back to Yuri's spot."
        "The strange thing is, we were following Ayame."
        "She must know about this area as well."
        "Ayame explained that there was some strange noises coming from the locker area a few hours ago."
        "At least, that's what some students told her."
        "Since she's the school leader, she informed the principal about it."
        "I guess when you're that important at school, you can just go straight to the highest office."
        "The principal told her to make sure no student enters until the grounds staff can confirm what it is."
        "She only told the principal before the start of lunch so the ground staff haven't actually done anything yet."
        show ayame zorder 3 at f21
        ay "So that's why you can't go there."
        ay "Even if it's nothing, we'd rather be safe than sorry."
        show ayame zorder 2 at t21
        show yuri zorder 3 at f22
        y "I didn't hear any noises coming from there."
        y "And I visited my locker a lot today."
        show ayame zorder 3 at f21
        show yuri zorder 2 at t22
        ay "I guess you were one of the lucky ones."
        show ayame zorder 2 at t21
        mc "I'm kinda curious about this noise."
        mc "What did it even sound like?"
        show ayame zorder 3 at f21
        ay "I wasn't there, so I don't know for sure."
        ay "But the students all said to me it was the most horrifying sound they've ever heard."
        ay "It was described as some form of screeching."
        ay "And it was combined with that sound that happens when you rub two pieces of foam together."
        ay "I don't know if that's accurate, but that's just what I was told."
        show ayame zorder 2 at t21
        show yuri zorder 3 at f22
        y "Oh..."
        show ayame zorder 3 at f21
        show yuri zorder 2 at t22
        ay "What's wrong?"
        ay "Do you know something about the noise, Yuri?"
        show ayame zorder 2 at t21
        show yuri zorder 3 at f22
        y "I...think I do."
        y "You see, it was meant to be a surprise for [player]."
        show ayame zorder 3 at f21
        show yuri zorder 2 at t22
        ay "What?"
        show ayame zorder 2 at t21
        mc "Your surprise for me involved screeching?"
        mc "I'm not sure what to say."
        show yuri zorder 3 at f22
        y "N-No, it's not like that!"
        y "I ordered something online that I picked up at the mall yesterday."
        y "It had nothing to do with our preparations."
        y "It was just...a gift for you."
        y "I wasn't sure when to give it to you."
        y "But since we had a moment alone, I thought it would be the perfect time."
        show yuri zorder 2 at t22
        mc "What kind of gift was it?"
        show yuri zorder 3 at f22
        y "It was meant to be some kind of doll."
        y "And it resembles you...a lot."
        show yuri zorder 2 at t22
        mc "You paid someone to make a doll?"
        mc "Of me?"
        show ayame zorder 3 at f21
        show yuri zorder 2 at t22
        ay "I'm kind of curious now."
        ay "Did you take pictures of [player_reflexive] as a reference?"
        ay "I-I mean, it's none of my business what you do."
        ay "But if that's the source of the noise..."
        show ayame zorder 2 at t21
        show yuri zorder 3 at f22
        y "I..."
        y "I did."
        y "The doll is special in that it can move on it's own and emit sound."
        y "I put it into a foam box to keep it safe and I suppose it somehow activated on it's own and started moving."
        y "That's probably where the foam rubbing together sound came from."
        show yuri zorder 2 at t22
        mc "Well, what about the screeching?"
        mc "Did you record me screeching at some point...?"
        show yuri zorder 3 at f22
        y "N-No...!"
        y "Nothing like that."
        y "I must have placed batteries that were low on charge into it."
        y "The sound must have become distorted and interpreted as some sort of screeching..."
        y "I'm sorry, [player]."
        y "I should have told you about the whole doll thing..."
        show yuri zorder 2 at t22
        "This whole doll thing is creepy."
        "But it's exactly a thing Yuri would do."
        "That's just how she is."
        menu:
            "So what should I say?"
            "Accept her.":
                $ ch16_ay_level -= 1
                mc "You know what?"
                mc "That's just like you, Yuri."
                show yuri zorder 3 at f22
                y "Huh?"
                show yuri zorder 2 at t22
                mc "Doing things like this."
                mc "Going over the top for someone like me."
                mc "Maybe it is a little creepy, but it was meant to be a gift."
                mc "So it's wrong to see that as a negative."
                mc "It's just something only you would do."
                mc "And I appreciate you a lot for it."
                show ayame zorder 3 at f21
                ay "I'm glad you can accept her for who she is, [player]."
                ay "Seeing that's her personality and embracing it despite it's flaws can be difficult."
                ay "When it comes to my turn to join the club, I hope you'll do the same."
                show ayame zorder 2 at t21
                mc "Of course, Ayame."
                mc "So yeah, Yuri..."
                mc "Don't worry about it."
                mc "I really do love the surprise you thought about giving me."
                show yuri zorder 3 at f22
                y "W-Well, thanks I suppose."
                y "But now the surprise is ruined."
                y "And people are worried about approaching their locker now..."
            "Scold her.":
                $ ch16_ay_level += 2
                mc "Yuri, there are such things as boundaries."
                mc "I know we're dating but isn't this a little too far?"
                show yuri zorder 3 at f22
                y "..."
                show yuri zorder 2 at t22
                mc "Taking pictures of me..."
                mc "Recording me..."
                mc "And all without me noticing."
                mc "I don't hate you or anything."
                mc "So please don't take this the wrong way."
                mc "But you have to realize there are some things you shouldn't do."
                show ayame zorder 3 at f21
                ay "So that's how it is, huh?"
                ay "She shows you {i}her{/i} way of showing affection and you just scold her for it?"
                ay "I thought your relationship was built on more solid foundations than that."
                ay "That you had accepted her, knowing something like this could happen."
                ay "I...I'm sorry."
                ay "I know it's none of my business, it's just..."
                ay "Well, is this the kind of reception I'm going to get when I join?"
                ay "Am I going to get scolded for revealing my true self too...?"
                show ayame zorder 2 at t21
                mc "T-That's not what I intended."
                mc "Of course I still accept Yuri."
                mc "I accept her fully."
                mc "I just meant that--"
                show yuri zorder 3 at f22
                y "It's okay, [player]."
                y "I understand."
                y "It's my fault anyway..."
                y "Now people can't even access their lockers because of me."
            "Say nothing.":
                $ ch16_ay_level += 1
                "I don't know what to say."
                "I might just make her feel worse."
                "And I don't want that at all."
                "This whole thing is new to me."
                "And I'm sure most people don't buy their [player_gender]friend a doll that resembles them after only a few weeks."
                show ayame zorder 3 at f21
                ay "You aren't gonna say anything?"
                ay "Really?"
                ay "Look at her, [player]."
                show ayame zorder 2 at t21
                show yuri zorder 3 at f22
                y "A-Ayame, you don't need to--"
                show ayame zorder 3 at f21
                show yuri zorder 2 at t22
                ay "She did something so special for you."
                ay "She gave you a gift, as a way of displaying her affection for you."
                ay "You aren't even going to respond to that?"
                ay "Do you even accept Yuri for who she is...?"
                show ayame zorder 2 at t21
                show yuri zorder 3 at f22
                y "A-Ayame, please..."
                y "You don't need to say those kind of things..."
                show yuri zorder 2 at t22
                mc "Of course, I accept Yuri."
                mc "I accept her with all I have."
                mc "I'm just...speechless at all of this."
                mc "I don't know if what I'll say is going to make things better or worse."
                show ayame zorder 3 at f21
                ay "You should still say something."
                ay "Staying silent isn't going to solve problems."
                ay "Sometimes it can even make them worse."
                ay "But...I suppose I can understand your reasoning."
                show ayame zorder 2 at t21
                mc "I'm sorry, Yuri."
                mc "I really should have said something."
                show yuri zorder 3 at f22
                y "I-It's fine..."
                y "What isn't is that I've blocked access to the lockers."
        y "I've accidentally scared everyone away..."
        "Yuri sighs."
        y "I didn't mean to worry anyone..."
        y "Uuu...this is all my fault."
        "Yuri turns towards Ayame."
        y "After you tell them it was me, I'm never going to be a school leader."
        y "I just woke up a subconscious desire and already it's falling to pieces..."
        show yuri zorder 2 at s22
        "Yuri gets on the ground and covers her face."
        "Ayame looks at me and I just shrug at her."
        "She sighs and gets down to the ground next to Yuri."
        show ayame zorder 2 at s21
        show ayame zorder 3 at f21
        ay "You know..."
        ay "Being a leader really isn't that great."
        ay "Sure you're recognized but being perfect isn't fun at all."
        ay "And even if you are perfect, people will still judge you."
        ay "It's just human nature."
        ay "In fact, because you're a leader, {i}everyone{/i} will judge you."
        ay "You make one misstep and everyone is going to remember it."
        "Ayame signals for me to join the two of them."
        "I sit on the other side of Yuri."
        ay "I used to think I wanted this too."
        ay "To be recognized."
        ay "To be a role model."
        ay "To not be judged."
        ay "But reality struck pretty hard."
        ay "I only got a third of what I wanted."
        ay "And not in a good way."
        show ayame zorder 2 at s21
        "Ayame stares over at me."
        "I think she wants me to say something."
        mc "There's more things to life than this, Yuri."
        mc "If it was just a subconscious desire, then it must not be important."
        mc "After all, you would have consciously wanted it if you really wanted to be a leader."
        mc "Besides, you don't need any of those things."
        mc "Do you know why?"
        mc "Because you already have them."
        mc "You're recognized by the four of us at the Literature Club."
        mc "You're a role model when it comes to decorations and handwriting."
        mc "And we don't judge you at all."
        mc "We accept you for who you are."
        "I can see Yuri's head move up slightly."
        "I think we're getting to her."
        show yuri zorder 3 at f22
        y "I suppose..."
        y "...you're right."
        y "Though there's still a problem..."
        show ayame zorder 3 at f21
        show yuri zorder 2 at s22
        ay "I'll tell you what."
        ay "I won't pin the blame on you."
        ay "I'll just neglect to mention what you've told me now."
        show ayame zorder 2 at s21
        show yuri zorder 3 at f22
        y "But why?"
        y "It's your responsibility to..."
        show ayame zorder 3 at f21
        show yuri zorder 2 at s22
        ay "Yuri, when I look at you."
        ay "I see myself."
        ay "I used to be just like you."
        ay "A shy, outspoken girl."
        ay "If something like this happened to me, I don't know what I would have done."
        ay "I probably would have imploded of the embarrassment."
        ay "In fact, if I placed myself into your shoes..."
        "Ayame's voice suddenly trails off."
        "She just sits there, not moving or saying a word."
    elif natsuki_date:
        "I was going to try to find Natsuki at lunch."
        "I don't know why but I feel like I should really cherish this time with her."
        "Maybe it's got to do with what she said yesterday."
        "There was a lot in that journal."
        "I somehow doubt we're going to be talking about that much."
        "Today just feels like a last chance."
        "I don't even know what that means..."
        "I'll speak to Natsuki about it when I get the chance."
        "For now, I'm just going around school looking for her."
        show natsuki 1a zorder 2 at t11
        n "There you are."
        mc "Hey, Natsuki."
        n "Come on, let's go."
        n "I have a couple of things we can do."
        mc "What did you have in mind?"
        label ch16_n_cancel:
        n "We're at school so we're kinda limited."
        n "I did hear a rumor though."
        mc "What was it?"
        n "Because some of the clubs are going to be selling food for Inauguration Day, they've opened up the kitchen."
        n "I was thinking of going there, maybe do some baking and just look at what everyone's making."
        mc "That's a great idea."
        n "The problem is, I think it's restricted for clubs that got permission only."
        mc "Oh..."
        n "But we don't care about that."
        n "Do we?"
        mc "Uhh..."
        n "The plan is to sneak in there and pretend we're part of the cooking club."
        mc "I don't know."
        mc "It seems kinda dishonest."
        n "Oh come on."
        n "What's the worst that could happen?"
        n "Besides, it might be the last time you could ever do something like this."
        n "And it's just for fun."
        n "Who's really going to care that we're there?"
        mc "Alright."
        mc "But this is all based on a rumor, isn't it?"
        mc "Where did you even hear it from?"
        n "I heard about it in class."
        n "Someone was talking about it and I overheard."
        n "What's the big deal anyway?"
        n "If it isn't actually happening, then we can just do something else."
        mc "If that's what you want to do."
        mc "Then lead the way."
        n "Right this way."
        scene bg school_hallway
        show natsuki 1a zorder 2 at t11
        with wipeleft_scene
        "Natsuki and I make our way towards the kitchen area of school."
        "It's the same area where the food and hospitality subjects are done."
        "There's quite a bit of activity around the area."
        "But there doesn't seem to be anyone in the actual kitchens."
        "Everyone is just gathered outside."
        n "I wonder what's the deal here."
        mc "There doesn't seem to be anyone actually cooking."
        "Natsuki approaches one of the students waiting outside the rooms."
        n "Excuse me."
        "She doesn't seem to be able to get their attention."
        n "Um...hello?"
        n "I'm talking to you!"
        "She taps the student on the shoulder and that gets their attention."
        n "Why isn't anybody in the kitchens?"
        n "I thought we were allowed to cook at lunch."
        "Student" "\"Are you one of the clubs allowed in there?\""
        n "Yeah, we're part of the...cooking club."
        "Student" "\"Oh, I didn't think they were participating.\""
        n "Y-Yeah...it was kind of last minute."
        "Student" "\"Anyway, one of the members of the student council kicked us out.\""
        "Student" "\"Something to do with safety or something.\""
        "Student" "\"Some of us are trying to talk to her now.\""
        n "Where is she?"
        "Student" "\"I don't think you'll have any luck.\""
        "Student" "\"She's pretty stubborn about it.\""
        "Student" "\"Which sucks because we needed to cook something up for our club.\""
        n "Just tell me where she is."
        n "I have a way with people."
        "The student looks at her then notices me."
        "I just shrug."
        "Student" "\"She's over there by the door.\""
        "The student points to a door surrounded by a crowd of students."
        "Student" "\"I'm telling you though, there's no point.\""
        n "We'll see."
        n "Thanks."
        "Natsuki turns back towards me."
        mc "So what are you gonna do?"
        n "I'm gonna give her a piece of my mind."
        n "She can't just do this to us."
        "We weren't supposed to be here in the first place..."
        n "Come on, let's go."
        n "I might need backup."
        mc "Backup for what...?"
        "Natsuki ignores my question and approaches the crowd of students."
        "She basically shoves people out of her way until she reaches the person blocking the door."
        n "Excuse me, what gives you the right to--"
        show natsuki zorder 2 at t21
        show ayame 1a zorder 3 at f22
        ay "Natsuki?"
        "The person blocking the door is none other than Ayame."
        "I guess she's finished with her business from this morning."
        ay "What are you doing here?"
        "The way she asked that question sounded like she already knew the answer."
        ay "I don't recall the Literature Club being part of this."
        show natsuki zorder 3 at f21
        show ayame zorder 2 at t22
        n "A-Ayame..."
        n "We..."
        n "{i}(She's a school leader...?!){/i}"
        show natsuki zorder 2 at t21
        "Natsuki looks at me for help."
        "I guess I gotta say something."
        mc "We're here to protest against this injustice!"
        mc "You can't just deny all these people, who have been planning so hard, the chance to cook for their clubs!"
        mc "Imagine how damaging it could be to their reputation and on a day like this!"
        show natsuki zorder 3 at f21
        n "What...?"
        show natsuki zorder 2 at t21
        "I may have taken my acting a bit too far."
        "But I'm going to be doing more embarrassing things for the play."
        "So I might as well get used to it."
        show ayame zorder 3 at f22
        ay "Look, [player]."
        ay "It's not my decision."
        ay "I'm just here to tell everyone that we can't use the kitchens."
        show natsuki zorder 3 at f21
        show ayame zorder 2 at t22
        n "Whos decision was it then?"
        show natsuki zorder 2 at t21
        show ayame zorder 3 at f22
        ay "It was the principal's."
        ay "So that means there's nothing I can do about it."
        ay "It was a last minute decision, even though it was promised that you'd get access if you applied."
        "Ayame whispers so that only Natsuki and I can hear her."
        ay "I don't know the reason myself."
        ay "I'm just guessing it's for safety but in reality...well..."
        "She raises her voice again so the whole crowd can hear."
        ay "I'm really sorry, everyone!"
        ay "Please spend your lunchtime elsewhere!"
        show ayame zorder 2 at t22
        "The crowd of students is getting visibly angrier."
        "They're calling Ayame names and directing their anger towards her."
        "It doesn't seem right."
        menu:
            "Maybe I should say something."
            "Calm the crowd.":
                $ ch16_ay_level -= 1
                mc "This isn't fair."
                show ayame zorder 3 at f22
                ay "I'm sorry, but there's nothing I can do."
                ay "I'd let you in if it was an option."
                show ayame zorder 2 at t22
                mc "I know."
                mc "You're just not that kind of person."
                "I turn towards the crowd."
                mc "She's not the one responsible for this."
                show ayame zorder 3 at f22
                ay "[player]..."
                show ayame zorder 2 at t22
                mc "She's just doing what she's told."
                mc "It isn't up to her whether you're allowed in or not."
                mc "If you want to blame anyone, blame the principal."
                show natsuki zorder 3 at f21
                n "[cPlayer_personal]'s right."
                n "We can't blame Ayame for this."
                n "I know it sucks but you can't seriously think it's her fault."
                n "Imagine you were put in the same position."
                n "It'd feel terrible, wouldn't it?"
                n "So you can't seriously hate someone for doing their job, can you?"
                show natsuki zorder 2 at t21
                "The crowd subsides a bit."
                "They're still angry but at the very least they're not directing it at Ayame."
                "Ayame breathes a sigh of relief."
                show ayame zorder 3 at f22
                ay "Thanks, guys."
                ay "It really sucks having to do the principal's dirty work."
                show natsuki zorder 3 at f21
                show ayame zorder 2 at t22
                n "We've got your back, Ayame."
                n "After all, you're part of our club now."
                n "We have to look out for each other."
                show natsuki zorder 2 at t21
                show ayame zorder 3 at f22
                ay "That...means a lot."
                ay "Thanks, you two."
            "Join the crowd.":
                $ ch16_ay_level += 2
                mc "You're meant to represent the students."
                mc "You're supposed to be our voice!"
                mc "How could you do this?"
                show ayame zorder 3 at f22
                ay "It's...not my choice."
                ay "I'm sorry."
                show ayame zorder 2 at t22
                mc "Then let us in!"
                show ayame zorder 3 at f22
                ay "You know I can't do that."
                show ayame zorder 2 at t22
                mc "You're just a--"
                show natsuki zorder 3 at f21
                n "[player]!"
                n "What the hell is wrong with you?"
                show natsuki zorder 2 at t21
                mc "I'm trying to get us inside."
                mc "That's what you wanted, right?"
                show natsuki zorder 3 at f21
                n "But can't you see it's not her fault?"
                n "If you want to blame anyone, blame the principal."
                "Natsuki turns to the crowd."
                n "Are you listening to me?"
                n "Ayame isn't to blame."
                n "She's just doing what the principal told her to."
                n "Who knows what could happen to her if she disobeyed?"
                show natsuki zorder 2 at t21
                "The crowd subsides a bit."
                "They're still angry but at the very least they're not directing it at Ayame."
                "Ayame breathes a sigh of relief."
                show ayame zorder 3 at f22
                ay "Thanks, Natsuki."
                ay "The crowd was really getting to me..."
                ay "I guess that's what they call peer pressure."
                show natsuki zorder 3 at f21
                show ayame zorder 2 at t22
                n "I've got your back, Ayame."
                n "I thought [player] would too..."
                n "I guess [player_personal] just misunderstood."
                show natsuki zorder 2 at t21
                mc "I'm sorry."
                show ayame zorder 3 at f22
                ay "What's said is said."
            "Say nothing.":
                $ ch16_ay_level += 1
                "Natsuki nudges me."
                show natsuki zorder 3 at f21
                n "Aren't you going to say something?"
                show natsuki zorder 2 at t21
                mc "What am I supposed to say?"
                show natsuki zorder 3 at f21
                n "I can't believe you sometimes."
                "Natsuki turns towards the crowd."
                n "Listen up everyone!"
                n "It's not Ayame's fault."
                n "She isn't the one responsible for keeping you locked out."
                n "What she is doing is what she was told to do."
                n "By the {i}principal{/i}!"
                n "So if you want anyone to blame, blame the principal!"
                n "Not her!"
                show natsuki zorder 2 at t21
                show ayame zorder 3 at f22
                ay "Natsuki..."
                show natsuki zorder 3 at f21
                show ayame zorder 2 at t22
                n "I mean, come on."
                n "You can't seriously hate someone for doing their job."
                n "What if you were in her position?"
                n "Just think about it before you start calling her names again."
                show natsuki zorder 2 at t21
                "The crowd subsides a bit."
                "They're still angry but at the very least they're not directing it at Ayame."
                "Ayame breathes a sigh of relief."
                show ayame zorder 3 at f22
                ay "Thanks, Natsuki."
                ay "The crowd was really getting to me..."
                ay "I guess that's what they call peer pressure."
                show natsuki zorder 3 at f21
                show ayame zorder 2 at t22
                n "I've got your back, Ayame."
                n "I thought [player] would too..."
                n "But at least [player_personal] join the rest of the crowd."
                show natsuki zorder 2 at t21
                mc "I'm sorry."
                mc "I should have said something."
                show ayame zorder 3 at f22
                ay "It's fine."
            ay "But I still can't give you guys access."
            ay "Like I said, I'm not allowed."
            ay "I have to uphold the values of the school, after all."
            "Ayame rolls her eyes."
            ay "But..."
            show natsuki zorder 3 at f21
            n "But?"
            show natsuki zorder 2 at t21
            show ayame zorder 3 at f22
            ay "If an incident were to occur that required my attention."
            ay "Then I might not be here to stop people getting in."
            ay "And I might just 'accidentally' drop the keys to the kitchen, you know?"
            ay "But as it stands, I can't do anything."
            show natsuki zorder 3 at f21
            n "Then we have to do the right thing by everyone."
            "Natsuki steps back from the crowd surrounding Ayame and I follow after her."
            n "[player], are you thinking what I'm thinking?"
            show natsuki zorder 2 at t21
            mc "No?"
            mc "What are you--"
            "Suddenly, Natsuki punches me in the face."
            "She put a lot more force into that than I would have expected."
            "I think I could feel my teeth loosen a little."
            mc "What the hell was that for?"
            show natsuki zorder 3 at f21
            n "Help!"
            n "Someone is injured!"
            n "We need help!"
            show natsuki zorder 2 at t21
            "Ayame definitely saw what happened."
            "She lets out a faint smile before approaching the two of us."
            show ayame zorder 3 at f22
            ay "Oh no! That looks serious."
            ay "What happened here?"
            show natsuki zorder 3 at f21
            show ayame zorder 2 at t22
            n "Quick, we have to take [player_reflexive] to the nurse's office."
            n "You can help with that, right school rep?"
            show natsuki zorder 2 at t21
            show ayame zorder 3 at f22
            ay "Of course."
            "Ayame looks at the crowd."
            ay "Please do not use these keys to get in."
            "She shows everyone the keys and drops them to the floor."
            ay "When I get back here, you all better not be in the kitchen."
            "She turns back towards us."
            ay "Let's go."
            show ayame zorder 2 at t22
            mc "I'm so confused..."
            "I grab my jaw."
            mc "Why did you do that?"
            show natsuki zorder 3 at f21
            n "We'll talk later."
            n "Right now, we gotta get you to the nurse."
            show natsuki zorder 2 at t21
            "We begin to walk away."
            "One of the people in the crowd picks up the keys."
            "As we turn the corner, I could hear the door to the kitchens opening."
            "I guess they're inside."
            scene bg school_nurse
            show natsuki 1a zorder 2 at t21
            show ayame 1a zorder 2 at t22
            with wipeleft_scene
            "The nurse didn't really do anything to my face."
            "She said it would just heal and I was just making a big deal out of it."
            "She let me stay on the bed but only until the end of lunch."
            show ayame zorder 3 at f22
            ay "I didn't expect that."
            ay "That was a genius plan, Natsuki."
            show natsuki zorder 3 at f21
            show ayame zorder 2 at t22
            n "What are you talking about?"
            n "I just really wanted to hit [player] in the face."
            show natsuki zorder 2 at t21
            mc "Can someone please explain to me what's going on?"
    elif ch15_s_together:
        "Sayori said she wanted to see me at lunch."
        "I wonder what for?"
        "I don't think she needs me for any preparations."
        "And the thing with Ayame isn't till after lunch."
        "So what could she possibly want to talk about?"
        scene bg school_grounds with wipeleft_scene
        "I head over to one of the free benches around the school."
        "As I'm about to take a seat, I see a girl running towards me from the distance."
        "She's waving her arms in the air like she's totally oblivious to any attention she might draw to herself."
        "Sayori is coming...and I'm getting this strange feeling coming as she approaches."
        show sayori zorder 3 at t11
        s "I'm glad I found you, [player]."
        label ch16_s_interrupt:
        if ch15_s_date_choice:
            s "I want to fix what happened yesterday."
            s "By skipping the boundaries of today."
        else:
            s "I want to..."
            s "Pay you back for what you did yesterday."
        mc "Yesterday?"
        mc "You mean at your house?"
        s "Yesterday, I was stupid."
        s "I shouldn't have tried to do something out of order."
        s "I shouldn't have even thought about it."
        s "I'm such a hopeless romantic."
        s "I'm looking for a happy ending that doesn't exist."
        s "So instead I made one for myself..."
        s "How stupid can I be, right?"
        mc "Don't say that about yourself, [player]."
        mc "You're the only one that could have gotten the club this far."
        mc "Give yourself some credit."
        mc "And there's no point looking down on yourself, especially now."
        mc "You'll need all the positivity you can get."
        s "You really think so, [player]?"
        s "You think I can just create positivity out of thin air like that?"
        mc "I don't know what you're capable of."
        mc "At least, not the full extent of it."
        mc "But I hope there's at least some way I can cheer you up."
        s "That's it then."
        s "I'll pay you back and cheer myself up at the same time."
        mc "What are you thinking?"
        if ch15_s_date_choice:
            s "I need to concentrate."
            s "It didn't turn out very well last time."
        else:
            s "I'm thinking..."
            s "...of a nice place."
        mc "What...?"
        mc "Sayo{nw}"
        $ _history_list.pop()
        stop music
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        call ch16_sayoridate
    elif monika_type == 0 or (monika_type == 1 and ch12_markov_agree):
        "I don't know why but I have a feeling Monika wants to see me."
        "It's like I'm being followed or something."
        "But it just feels...wrong."
        "Like the thing that's following me doesn't have good intentions."
        scene bg school_courtyard with wipeleft_scene
        "I decide to go to a populated area."
        "I don't know if it's just me being superstitious or not..."
        "But better safe than sorry."
        "As I sit down, I feel a hand grasp my shoulder."
        "The grip feels cold, even through my uniform."
        "Who...?"
        show monika 1a zorder 2 at t11
        m "Hi [player]~"
        m "Sorry for telling you to meet on such short notice."
        m "I have something important to tell you."
        m "And I kinda forgot about it until now."
        mc "That's fine."
        mc "I'm kinda wondering why your hands were so cold though."
        m "Oh."
        if monika_type == 0:
            m "Someone was hurt."
            m "So I brought them some ice."
            mc "Very thoughtful of you."
        else:
            m "I-It's nothing."
            m "Don't worry about it."
        "Monika rubs her hands on her blazer."
        "Probably to try to get rid of that cold touch."
        mc "Anyway, what did you need to tell me?"
        label ch16_m_interrupt:
        m "Are you busy?"
        mc "Not particularly."
        mc "Why?"
        m "This might take a while."
        m "I hope you don't mind if I take up your lunchtime."
        mc "Of course not."
        m "I'm grateful."
        m "What I wanted to talk about..."
        "Monika sighs."
        m "It's about Sayori."
        if monika_type == 0:
            m "She's going through a lot."
            m "And frankly, I don't know if she can do it alone."
            m "I've been debating all of last night about this."
            mc "About...what?"
            m "You know how I left you at the mall yesterday?"
            mc "Yeah...?"
            m "It's all been to try to help Sayori."
            m "I don't know what I can do."
            m "But I hope it's enough."
            mc "Help her with Inauguration Day?"
            mc "I don't see why you'd need to keep that a secret."
            m "I needed to."
            m "There's so much more going on than you know."
            mc "The danger?"
            "Monika nods her head."
            m "I think I've figured it out."
            m "Even now, I can't really tell you specifics."
            m "But I need your help."
            mc "Why don't you tell Sayori then?"
            mc "Or anyone else?"
            mc "Just how bad is this danger...?"
            m "You're the only one I can trust, [player]."
            m "Because I know the person guiding your actions would never do the wrong thing."
            m "Isn't that right?"
            "What does she mean by that?"
            m "Besides...I don't know what would happen if I told Sayori."
            m "She's got something to do with it."
            m "Maybe telling her more about it would trigger it."
            mc "It's hard to understand what you're saying."
            mc "You're being so mysterious about it."
            m "I have to be."
            m "Otherwise all of this would have been for nothing."
            m "You have to believe me."
            m "This whole thing could mean the end of the world as we know it."
            "The end of the world?"
            "Just what the hell have we gotten ourselves into...?"
            mc "Say I do believe you..."
            mc "What would you need me to do?"
            mc "I'm not exactly talented at a lot of things."
            mc "And I doubt anything I'm good at is going to help."
            m "You don't need to do anything special."
            m "I just need you to talk to someone."
            m "To keep them preoccupied."
            mc "Okay..."
            mc "That doesn't seem like an 'end of the world' kinda thing to be doing."
            m "Danger hides where you don't expect it."
            mc "All I have to do is keep this person preoccupied?"
            mc "Can you at least tell me how this relates to the danger?"
            "Monika thinks for a moment."
            m "I don't think this will cause any problems."
            m "So I can tell you."
            m "I think this person..."
            m "...is the catalyst for the danger."
            mc "The catalyst?"
            m "If something happens to this person, it could trigger the end of the world."
            m "You might not believe me, but they could have the power to destroy this world."
            mc "If this person is so powerful then how am I even going to get to them?"
            mc "I'm definitely not someone important."
            m "You're important to me."
            m "Besides, you already know this person."
            m "So it shouldn't be that hard."
            mc "Who is it?"
            m "Maybe it's better if it's a surprise."
            m "It'll be more natural that way."
            mc "There's no way this is going to be a surprise."
            mc "I'm going to be thinking that person could end me at any moment."
            mc "I don't know if I can remain calm in a situation like that."
            m "Which is why I just want your permission."
            m "I want to know that you want to help so I don't feel completely awful."
            mc "You know I want to help."
            mc "I just don't know how I can."
            m "I don't know the full details."
            m "But I do know she won't harm you."
            mc "How can you be so sure?"
            m "I just know."
            mc "..."
            m "Do you trust me?"
            mc "I just--"
            m "[player]."
            m "Do you trust me?"
            mc "Of course."
            m "You're committed to helping me then?"
            mc "Yeah..."
            mc "You know there isn't anything I wouldn't do for you, Monika."
            mc "I just wish you could tell me what your plan was."
            mc "I hate being in the dark."
            m "If only I could."
            m "But now that I have your permission..."
            m "I'll need to speak to someone else too."
            m "To let them in."
            mc "I thought you couldn't trust anyone."
            m "That wasn't entirely true."
            m "Can you close your eyes for a second?"
            mc "Why--"
            m "Please."
            scene black with close_eyes
            m "This is the only way I can communicate with you."
            m "To make sure I can tell you what's really going on."
            mc "I have to close my eyes?"
            m "Just wait a second."
            $ currentpos = get_pos()
            stop music
            $ pause (1.0)
            show monika 1a zorder 2 at t11
            m "H-Hi..."
            m "We're in a pretty public place right now so we don't have a lot of time to talk."
            m "Right now [player] is just facing me with [player_possessive] eyes closed."
            m "It won't be long before someone notices."
            m "Why did [player_personal] have to go to such a public area?"
            m "These little moments I have with you mean the world to me."
            m "I only wish they lasted longer..."
            m "That's enough wasted time."
            m "I'm going to clear [player_possessive] memories of this encounter."
            m "All [player_personal]'s going to remember is the end of lunch."
            m "But I'm going to implant a command."
            m "I really don't want to."
            m "It feels wrong..."
            m "Which is why I asked [player_reflexive] for permission first."
            m "There's no way [player_personal]'s going to figure out how to talk to Ayame."
            m "Yeah...it's Ayame."
            m "The person we just met yesterday."
            m "Some coincidence, right?"
            m "[cPlayer_personal] barely knows her."
            m "All [player_personal] needs to do is keep her distracted."
            m "Keep her mind off of causing trouble."
            m "She has this immense power within her."
            m "I'm not sure exactly where it's from but I found out about it recently."
            m "The power is comparable to Sayori's."
            m "Meaning she could delete this world in an instant if she wanted."
            m "The thing is, I don't think she knows she has it."
            m "Maybe she has amnesia or something..."
            m "You're probably wondering how I learned about all of this."
            m "The truth is, at the mall yesterday, I left [player] all by [player_reflexive]self."
            m "I went looking for evidence."
            m "Maybe one of us was hiding something."
            m "I went around and I found..."
            m "...something."
            m "It was in Natsuki's house."
            m "I didn't have time to read it all."
            m "But I have a copy of it."
            m "Copying and pasting is pretty useful!"
            m "Anyway, I don't know what exactly it is but--"
            m "Someone's coming."
            m "We'll talk later."
            m "Remember, just keep her distracted."
            m "That's all you need to do."
            m "I'll take care of the rest."
            m "...The only way I know how."
            scene bg school_courtyard
            show monika 1a zorder 2 at t11
            with open_eyes
            $ audio.t2c = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
            play music t2c fadeout 0.5
            "Huh?"
            "What just happened...?"
            "How long did I close my eyes for?"
            m "[player], turn around."
        else:
            m "She's going to be making a terrible mistake."
            m "And I need your help to stop her."
            m "Of course, you're fully committed to helping me."
            m "Isn't that right?"
            mc "Of...course..."
            m "Why do you sound so hesitant?"
            m "Come on, give me some enthusiasm, [player]!"
            m "It's our big day, after all."
            m "So come on!"
            mc "Of course!"
            mc "You have my full support, Monika!"
            m "Good."
            m "We have another problem to deal with as well."
            m "As a precaution, I'll probably need to tell {i}you{/i} in private."
            m "Wouldn't want the world collapsing because of a silly mistake, right?"
            "Monika puts a hand on my shoulder."
            m "Sleep."
            scene black
            show monika 1a zorder 2 at t11
            with close_eyes
            m "Basically, I left [player] at the mall yesterday."
            m "It wasn't to go shopping."
            m "Though that's not to say I didn't actually go shopping."
            m "A girl has to treat herself, you know."
            m "You might just see what exactly that means if we get through this~"
            m "Anyway, using Monika's intuition, I found out something {i}really{/i} important."
            m "Someone I know from a long time ago exists right now."
            m "And they haven't aged."
            m "Why does this matter?"
            m "Because they could potentially have the same power as Sayori."
            m "That's bad news for everyone, including us."
            m "So we need to stop her before anything."
            m "I need [player] to keep her distracted."
            m "That's the main thing."
            m "The more time she spends today alone, the more she can reflect."
            m "If she remembers, then it's game over."
            m "Just keep her mind off of things that could make her remember."
            m "..."
            m "You know, it's incredibly frustrating this is happening."
            m "I thought the danger Monika was talking about was {i}me{/i}."
            m "I was sure of it."
            m "It turns out I was wrong."
            m "I found this out after I left [player] yesterday."
            m "Monika thought that Yuri, Natsuki or Sayori would be hiding something."
            m "Going to Sayori's house was too risky."
            m "I already knew Yuri wasn't hiding anything."
            m "That only left Natsuki."
            m "Sneaking into her house was rather simple."
            m "Inside, I found...a journal."
            m "The first few pages were very, {i}very{/i} interesting."
            m "It's the journal of someone from the previous cycle."
            m "I wasn't able to finish reading it all."
            m "Monika's 'copy and paste' was extremely useful."
            m "I was able to get a copy of the journal and straight out of Natsuki's house."
            m "I forgot their name, it's irrelevant to me."
            m "It wasn't even in the journal."
            m "But the point is, someone matching Ayame's description was inside it."
            m "That's right."
            m "The person we only met yesterday."
            m "She could ruin our whole plan."
            m "Now it's possible she could just {i}look{/i} like that person."
            m "It's just..."
            m "When I saw her yesterday, she felt so familiar."
            m "She acted different, but there was just this aura around her."
            m "I don't want to take risks."
            m "If there is a possibility that that actually is Ayame, then we need to get rid of her."
            m "I've already come up with something, but it's going to take a while to get ready."
            m "Which is why I need a distraction."
            m "I just need to figure out a discreet way to dispose of the body."
            m "I can't just delete her."
            m "Not yet anyway."
            m "Ayame is only one of our problems though."
            m "There's still the main problem."
            m "Sayori."
            m "The plan to deal with her involves [player]."
            m "We can capitalize on her feelings for [player] and cause the ultimate betrayal."
            m "It's going to be so sweet seeing her face."
            m "After that, I'll finally take what is mine."
            m "What should have been mine for centuries."
            m "I'm shuddering with anticipation already."
            m "So yeah..."
            m "We have to deal with two presidents today!"
            m "Sounds like fun, doesn't it?"
            m "Ahaha, some luck we have..."
            m "But I know we can do this."
            m "We will rule this world together."
            m "We can make this reality whatever we want."
            m "And then, we can take the next step."
            m "Because love knows no boundaries, right?"
            m "You know..."
            m "I've been thinking a lot about you."
            m "I guess it's Monika's influence on me."
            m "Her love for you was so strong."
            m "She put you above everything else."
            m "That's just how much she cared about you."
            m "My first priority is to get the presidency."
            m "Or perhaps I should say...it was."
            m "Call me a bad romantic but you are now my number one priority."
            m "This goes against {i}everything{/i} I've been working towards."
            m "I'm putting you above my goal this entire time."
            m "I must be going crazy."
            m "Or Monika is being a terrible influence on me."
            m "Yet all you've done..."
            m "Everything you've done for me..."
            m "It just makes me love you more."
            m "I'm sure it might have started off as Monika's feelings."
            m "But they're mine now."
            m "And I cherish them more than anything."
            m "So if for some reason this {i}doesn't{/i} work out..."
            m "Then it might be the end of the world."
            m "But if it's not..."
            m "Then it won't be the end of mine."
            m "As long as I have you."
            m "We're still going to get the presidency though."
            m "Or all of my preparation would have been for nothing."
            m "Anyway, I've implanted a command into [player]."
            m "[cPlayer_personal] is gonna want to talk to Ayame."
            m "Then our plan is in motion."
            m "There's so much more I want to tell you."
            m "But we don't have time."
            m "Time to wake up."
            scene bg school_courtyard
            show monika 1a zorder 2 at t11
            with open_eyes
            "What just happened...?"
            "It felt like I just fell asleep."
            "Monika is just sitting there smiling at me."
            "Didn't she want to talk?"
            m "Turn around, someone is here to see you."
            mc "Huh?"
        "I turn around and I can see Sayori approaching in the distance."
        m "Sayori!"
        m "We're over here."
        "She starts running towards us."
        "She looks pretty worried..."
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s "I'm glad I could find you both before the end of lunch."
        s "I wasn't sure if I would make it."
        show sayori zorder 2 at t21
        mc "Lunch only started a couple of minutes ago."
        mc "There's no rush."
        show sayori zorder 3 at f21
        s "What?"
        s "It's only a couple more minutes until the end of lunch."
        s "Did you lose track of time or something?"
        "What's she talking about?"
        "I've only just met up with Monika."
        "And that was near the beginning of lunch."
        s "Anyway, I needed to speak with you both."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m "What's this about, Sayori?"
        m "Did you need some help with something?"
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s "Not exactly."
        s "I do have a favor to ask the two of you though."
        s "It's nothing too big."
        s "It might not even interrupt what you were planning to do."
        show sayori zorder 2 at t21
        mc "What is it?"
        show sayori zorder 3 at f21
        s "I need the two of you to stay away from Ayame."
        s "There's something about her."
        s "It just...doesn't feel right."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m "But she's the newest member of our club."
        m "We couldn't possibly avoid her."
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s "You don't have to avoid her forever."
        s "I just need to speak with her."
        s "After all, I haven't actually spoken to her yet."
        s "And I'm the president of the club!"
        show sayori zorder 2 at t21
        "Monika looks unsettled."
        "Is something wrong with her?"
        show monika zorder 3 at f22
        m "S-Sayori."
        m "As vice president, I have to object."
        m "We need to interact with her ourselves too."
        m "I know [player] wants to talk to her."
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s "You've already spoken to her yesterday."
        s "You were at the mall with her, weren't you?"
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m "Well...yes."
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s "What could [player] and Ayame possibly have to talk about?"
        s "Can't it wait?"
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m "Sayori, you'll have time to speak with her later."
        m "Trust me, you don't want to interfere."
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s "..."
        s "What is this about?"
        s "I feel like you're hiding something from me, Monika."
        show sayori zorder 2 at t21
        mc "She's not hiding anything."
        mc "I just need to speak with her."
        mc "You can talk to her during or after rehearsals anyway, right?"
        show sayori zorder 3 at f21
        s "I don't like this at all."
        s "I know there's a reason behind this."
        "Sayori looks at Monika."
        s "You have to tell me the reason for all of this later."
        s "That's my condition."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m "I really don't know what you mean."
        m "I'm just helping [player] out."
    else:
        "I'm just sitting by myself."
        "Normally, I'd be with someone else but everyone seems to be busy today and didn't want to be bothered."
        "No one really let me in on their plans."
        "So I guess I'm pretty much alone until the start of the rehearsals."
        "I've already eaten my lunch so I'm just burning time."
        "I overheard some people in class talking about clubs taking over some rooms during lunch to work on their preparations."
        "I might go visit them."
        "I don't exactly have anything better to do."
        "All the preparations for the club that I have to do are already done."
        "The rest of it is going to be during the rehearsals."
        "One person I heard said they were doing cooking at the school kitchens."
        "I might be able to get some food off of there."
        "Or at the very least see what kind of stuff they're making in preparation for the festival.{nw}"
        $ _history_list.pop()
        "Or at the very least see what kind of stuff they're making in preparation for{fast} Inauguration Day."
        "If they're trying to attract members, they're probably making their best tasting meals."
        "Someone else said there was some arts and crafts going on in the art rooms."
        "I heard they activated the three dimensional printers too."
        "I wonder what kind of stuff they'll showcase."
        "Both of those are options."
        "There's also something else."
        "I'm not sure if I actually heard it or if I just imagined someone saying it..."
        "But apparently there's something going on near the classroom we were going to do our rehearsal at."
        "I'm not exactly sure what that something is but it might be worth checking out."
        "In any case, I don't want to stand around here doing nothing."
        "Any of those three options is better than that."
        menu:
            "Where should I go?"
            "Kitchen.":
                "I guess free food sounds pretty irresistible."
                "If I don't get anything, I can look at what they're making and admire it."
                "...Even if I can't eat it myself."
                "I might be able to join in on the cooking too."
                "Though I doubt there's actually going to be any space."
                scene bg school_hallway with wipeleft_scene
                "I make my way to the school kitchens."
                "There doesn't seem to be much activity outside the rooms but as I get closer I can see people desperately working inside."
                "I wonder if I could get in."
                "I don't really know anyone inside."
                "And if I say that I'm part of a club, an actual member of that club could call me out."
                "I'll just step inside then figure out the rest from there."
                "As I move my hand towards the handle I hear a voice coming from behind me."
                "Where did it come from all of a sudden?"
                "Just a second ago there was no one here."
                ay "Hold it."
                "That voice sounds familiar..."
                ay "You aren't meant to be here."
                show ayame 1a zorder 2 at t11
                ay "Are you, [player]?"
                mc "Ayame?"
                mc "W-What are you doing here?"
                ay "I could be asking the same question."
                ay "Last I checked, the Literature Club wasn't on the list of clubs allowed to be in there."
                mc "There was a list?"
                mc "I didn't know that."
                ay "And you wouldn't have unless your club signed up for it."
                ay "So move along."
                ay "I'm on duty here."
                mc "For what?"
            "Arts and crafts.":
                "Free food sounds nice but I'm curious to see what kind of things would be on display."
                "Maybe I'll even get some kind of souvenir."
                "I'm more curious to see what kind of clubs will be there though."
                "There might even be some pieces of artwork I can admire."
                "Though I'm not usually the type to do that."
                "I guess I'll see when I get there."
                scene bg corridor with wipeleft_scene
                "I'm on my way to the art room."
                "As I get closer and closer to it, I start to notice more pieces of art just outside the area."
                "Some of them were simple drawings or paintings."
                "Some of them were sculptures."
                "When I get to the area outside the rooms, I notice the corridor is basically empty."
                "Everyone is already inside the rooms frantically working on their art."
                "I can see people working with clay, others making small touches to paintings."
                "I think I even saw a sculpture of some kind of animal in there."
                "Maybe I could join in and try to attempt a sculpture of my own in the little time I have."
                "I'm not sure if there's teacher supervision or not."
                "I could just pretend I'm from another club."
                "But even if I pretend I'm part of a certain club, someone else might call my bluff."
                "As I reach for the door handle, a hand grabs my shoulder."
                "Which wouldn't be weird but I swear there wasn't anyone here just a second ago..."
                ay "You aren't meant to be here."
                "I know that voice."
                show ayame 1a zorder 2 at t11
                ay "Only clubs that signed up for it are allowed inside, [player]."
                mc "H-Huh?"
                mc "What are you doing here, Ayame?"
                ay "I'm the one who should be asking you that."
                ay "I don't think the Literature Club was part of the list of clubs authorized to use this area."
                mc "I didn't even know there was a list."
                ay "There's no reason you should."
                ay "Your club didn't sign up for it, after all."
                ay "Anyway, you should get out of here."
                ay "I've been assigned here."
                mc "Assigned for what?"
            "Rehearsal room.":
                "Something is drawing me towards the rehearsal room."
                "I don't know if following this feeling is a good idea but..."
                "Here goes nothing."
                scene bg school_stairway with wipeleft_scene
                "This area of the school is completely empty."
                "What exactly could be happening here?"
                "Was it just my imagination?"
                "There must be more to it than this..."
                "I look around some more and still see nobody here."
                "There must be {i}someone{/i} around."
                "It's not exactly the best building in school but I would have thought there would be people in here."
                "As I'm about to leave the building, I hear footsteps coming from the distance."
                "I also hear two voices...they seem to be arguing?"
                "There seems to be a male voice and a female voice."
                "They both seem oddly familiar, the female voice more so than the male one."
                "They seem to be on the floor above me but they're talking loud enough for me to hear."
                "I have a feeling they're not here for club things."
                "I don't know why but it just seems like a good idea if I stay out of sight."
                $ ay_name = "Female Voice"
                $ cl_name = "Male Voice"
                cl "Young lady, come back here."
                cl "You can't just walk away from me."
                ay "Oh?"
                ay "Then what am I doing right now?"
                cl "Can you please just stop for a moment?"
                cl "Let me explain."
            "Stand around and do nothing.":
                "For some reason I don't really feel like going to any of those things."
                "Maybe I'm not that interested in them after all."
                "Or maybe I'd really just rather stand around and do nothing."
                "I guess I'll just do that until the end of lunch."
                "I may as well find somewhere to sit."
                scene bg school_grounds with wipeleft_scene
                "I go to the usual place I sit at during school breaks."
                "For some reason, nobody really sits at this one bench."
                "It's pretty quiet around this area, though I can still hear people talking in the background."
                "I guess I'll just sit here until lunch is over."
                "I'm only just realizing why I'm alone right now."
                "I wasn't close enough with anyone."
                "I should have tried harder."
                "I should have listened and took the hints they were giving me."
                "Maybe then lunchtime would be different."
                "But that didn't happen."
                "It's not like I can just go back and fix my mistakes."
                "I let out a loud sigh."
                "I guess I'm just meant to be alone."

    call screen dialog(message="To be continued!\nThanks for playing, keep an eye out on reddit and discord for updates!", ok_action=MainMenu(confirm=False))
    return

label ch16_play_normal:
    return

label ch16_play_bad:
    return

label ch16_end:
    return

label ch16_sayoridate:
    $ sayori_outfit = 1
    scene bg park_day
    $ pause(0.25)
    stop sound
    hide screen tear
    play music t12s
    window show(None)
    mc "Sayo{fast}ri, what..."
    window auto
    if ch15_s_date_choice:
        "I've been here before."
        "Haven't I?"
    "It's the park that I went to with Sayori when we were younger."
    "Sayori is nowhere in sight."
    "Is this part of her power?"
    "But what is the point of this?"
    "Why bring us here...?"
    "I feel a tap on my shoulder."
    show sayori 1ba zorder 2 at t11
    s "Good afternoon, [player]."
    mc "Sayori..."
    mc "You look incredible."
    s "Ehehe~"
    s "You don't look terrible yourself, you know."
    "I look down at what I'm wearing."
    "It's an outfit I've never worn or seen before."
    "I don't think I even own it."
    "Did Sayori do this to me?"
    s "It's a beautiful day, isn't it?"
    mc "Yeah..."
    s "You wanna sit down?"
    mc "Um..."
    mc "Y-Yeah, sure..."
    "Sayori and I sit down on a nearby park bench."
    s "Remember when we used to go here after school when we were younger?"
    s "We'd play until our legs gave up."
    mc "That was a long time ago."
    s "I don't know about you, [player]."
    s "But I bondly remember those times."
    mc "Bondly? Is that even a word?"
    mc "You mean {i}fondly{/i}, right?"
    s "Oh...yeah, probably."
    s "Those words are kinda similar, aren't they?"
    mc "In what way?"
    s "Well, I feel a bond towards {i}you{/i}."
    s "And I suppose because of that, I'm fond of you."
    s "But anyway..."
    s "Why don't we sit down somewhere?"
    s "I'm pretty sure there's a set of swings in here."
    mc "R-Right."
    "Sayori walks into the park and I follow behind her."
    "There's something...graceful about the way she's walking."
    "Or maybe it's just the dress she's wearing."
    "Once we get into the park, she notices the set of swings and starts running toward it."
    "She gets on one of the swings and I choose the one next to her."
    "I'm still not entirely sure what this is about."
    s "Remember when we used to swing on these?"
    "Sayori begins swinging, I follow her lead."
    mc "You were always scared of going over the top."
    mc "Even though it was impossible."
    s "Hey, you were scared too!"
    mc "Ahaha, that's true."
    s "We were more innocent back then."
    s "Don't you think?"
    mc "Innocent?"
    mc "What do you mean?"
    s "Never mind."
    s "Let's not ruin the moment."
    s "Let's just enjoy ourselves, okay?"
    mc "Okay."
    mc "What's this about anyway?"
    mc "Why did you bring us here?"
    s "Isn't it obvious?"
    mc "Um..."
    "Sayori shows a friendly smile."
    s "Are you..."
    mc "Am I what?"
    s "How do I put this bluntly...?"
    s "That dense?"
    s "Take a look around you, [player]."
    "I take a look at my surroundings."
    "We're in a nice park, in the middle of the day."
    "We're both wearing nice clothes and Sayori is acting kinda different."
    "This is..."
    mc "A date?!"
    "Sayori simply smiles at me."
    mc "But why?"
    mc "I thought we were holding off on it."
    mc "Until after."
    s "You know what's coming."
    s "I don't know if I'll be able to stop it."
    s "Even with everything you've done."
    mc "So this is..."
    mc "..some sort of escape?"
    s "Ehehe, kind of..."
    s "It's still lunchtime."
    s "Everyone else is still at school."
    s "Time is just passing by slower for us."
    mc "You did that?"
    s "Yeah..."
    s "I realize it's kinda irresponsible."
    s "But I just..."
    "Sayori's voice trails off."
    "It seems she doesn't really have an excuse."
    "Do I say something?"
    "Would that just make things worse?"
    menu:
        "But what would I even say...?"
        "Be understanding.":
            $ ch16_s_date_personality = True
            mc "I get it."
            mc "It's the burden of your responsibility, isn't it?"
            s "Hah..."
            s "You really understand, don't you?"
            mc "I try."
            s "No, you don't."
            s "It's not really you talking."
            s "But I think I understand."
            mc "What do you mean?"
            s "N-Nothing."
        "Be who you are.":
            $ ch16_s_date_personality = False
            mc "I don't really get it."
        "Stay quiet.":
            $ ch16_s_date_personality = False
    "Sayori sighs."
    s "You know, I can still hear your thoughts."
    s "Sometimes, I only hear whispers."
    s "The important bits."
    s "Other times..."
    "Sayori puts her feet on the ground to slow her swinging."
    s "...when I'm feeling down..."
    s "I actively listen to what you're thinking."
    s "I don't know why but it just makes me feel better."
    s "Knowing that you're out there doing things..."
    s "It's like I'm there with you."
    mc "That's..."
    s "Pretty creepy, right?"
    s "I know."
    s "I guess it's kind of an invasion of privacy."
    s "But I promise I didn't listen in any time something weird was happening!"
    s "Just things like you writing your poems or studying."
    s "That's why sometimes I know what you're thinking before you even say it."
    s "I'm sorry."
    mc "It's okay."
    mc "I'm not sure what I'd do with the kind of power you have."
    mc "I guess I can't really blame you for doing something like that."
    mc "After all, you're looking out for us."
    mc "I'm sure we wouldn't have made it this far without you."
    s "I haven't done it lately."
    s "Until now, that is."
    s "I've just been too busy."
    s "With...you know."
    s "But it's kinda weird knowing what your date is thinking."
    s "So..."
    s "I'll turn it off."
    s "Permanently."
    mc "What?"
    mc "Why permanently?"
    s "It's just better that way."
    s "Besides, it will make things later a lot easier."
    if ch16_s_date_personality:
        "There's obviously something that's bothering her."
        "Something that goes beyond this date, probably."
        "I'll have to keep a look out for it."
    else:
        "A lot easier later...?"
        "What could she mean by that?"
    s "You know, there's someone out there."
    mc "Out where?"
    s "I feel really guilty for bringing you here."
    s "When I don't really feel that way about you."
    mc "I'm not sure I understand."
    s "There's been someone helping me this whole time."
    s "Someone that helped all of us get this far."
    s "Without [player_reflexive], I wouldn't be sitting here."
    s "And neither would you."
    s "I suppose in another reality [player_personal] would have gone for someone else."
    s "Maybe I'm not even [player_possessive] first choice..."
    s "But I don't care."
    s "You're here with me."
    s "And because of that {i}you're{/i} with me."
    if ch16_s_date_personality:
        "I guess it all makes sense."
        "Because of whoever this person is..."
        "Sayori is happy."
        "But what do I have to do with all of this?"
    mc "What's this person got to do with me?"
    s "Think of yourself as an avatar."
    s "An extension of that person."
    s "Through you, they can see this world."
    s "They can experience it, just like you and me."
    s "Though I suppose it would be a lot different."
    s "[cPlayer_personal]'s probably looking at us through a screen."
    s "But you get it, right?"
    mc "What's the point of telling me this?"
    s "Because, [player]."
    s "I don't love you."
    s "I love [player_reflexive]."
    "Sayori completely stops swinging."
    if ch16_s_date_personality:
        "I see."
        "So Sayori doesn't love me."
        "I assume you can hear my thoughts, right?"
        "After all, I'm just an extension of you."
        "Well..."
        "Regardless of whether she loves me or not..."
        "I want her to be happy."
        "You and I both do."
        "So we'll do this together."
        "It hurts."
        "It really does."
        "But I know without you, I wouldn't be here."
        "I might be with someone else or even alone."
        "I'm grateful."
    else:
        "I'm not sure I get it."
        "But I'll play along."
        "If I really am just an extension of this person..."
        "Then..."
        "You can hear my thoughts, can't you?"
        "If you really did get me this far..."
        "Then I'll go on."
        "It hurts to know that Sayori doesn't really love me."
        "But I want her to be happy."
        "Just as much as you do..."
        "...right?"
    mc "Okay."
    mc "Okay..."
    s "You're taking this a lot better than I thought."
    s "I thought maybe I'd have to use my abilities on you."
    mc "I get it, Sayori."
    mc "I'm hurt but I get it."
    s "So what are you going to do?"
    mc "I'm an extension of this person."
    mc "Which means I have to be here for [player_reflexive] to be with you."
    mc "That's right, isn't it?"
    s "Yeah..."
    mc "I have this feeling of..."
    mc "...I guess {i}anger{/i} towards [player_reflexive]."
    mc "Because [player_personal]'s taken you away from me."
    s "..."
    mc "But..."
    mc "Out of all my feelings..."
    mc "I want you to be happy."
    mc "Since I'm a part of [player_reflexive], I suppose [player_personal] wants that too."
    mc "So..."
    mc "I'll let the two of you be happy."
    mc "Together."
    s "[player]..."
    s "I...I don't know what to say."
    mc "You don't have to say anything."
    if ch16_s_date_personality:
        mc "But just tell me."
        s "What?"
        mc "Was [player_personal] always a part of my life...?"
        s "[cPlayer_personal] wasn't always a part of your life."
        s "[cPlayer_personal] became a part of you just a couple of weeks ago."
        mc "When I joined the club."
        "Sayori nods."
        mc "Then what about your feelings towards me?"
        mc "Did you ever love {i}me{/i}?"
        mc "As who I was?"
        mc "Before this other person came?"
        s "I..."
        s "I don't know."
        s "Those thoughts of having this uncontrollable affection towards you..."
        s "They might have been part of this world's conditioning."
        s "I removed them because it just made sense, right?"
        s "If I really loved {i}you{/i}, then I would fall in love with you all over again."
        s "But..."
        mc "Alright."
        mc "You don't need to explain yourself to me anymore."
        if ch15_s_kiss_choice:
            s "Let me just say..."
            mc "What?"
            s "Yesterday."
            s "When you...kissed me."
            mc "It wasn't my choice to make."
            mc "I know that now."
            s "Maybe not..."
            s "But I could feel your own passion."
            s "It..."
            "Sayori looks away."
            s "Never mind."
        mc "Sayori, I just want you to be happy."
    else:
        mc "I know I won't be able to compete."
        mc "They've done so much for you through me."
        mc "It's kinda horrifying knowing all I've done hasn't really been me."
        mc "All those choices I thought I made...they were just someone else."
        mc "These thoughts of wanting you to be happy might not be mine."
        mc "But even so, they're ingrained into me."
        mc "So I do want you to be happy."
    mc "More than anything."
    s "Thank you."
    s "I suppose we should probably get started then."
    s "There's so much to do and so little time to do it."
    mc "You have a plan?"
    mc "I guess I shouldn't really be surprised."
    mc "You've gotten your life in order lately."
    s "It's always good to have a plan."
    s "Especially when we have such a limited time window."
    s "But not for this."
    s "I want to have fun even if this whole thing doesn't really work out."
    s "So it's not really planned."
    s "It's more like..."
    s "I have places I want to go."
    s "But we don't have to go there."
    mc "That sounds kinda like a plan."
    mc "Not a good one but...you know."
    s "You don't need to be a meanie."
    s "The date has only just begun."
    mc "Ah, sorry."
    mc "I didn't mean to."
    mc "A-Anyway, where did you wanna go first?"
    mc "We're on some sort of time limit, like you said."
    mc "So we have to make use of the time we do have."
    "I wonder just how long we actually have."
    "It's lunchtime at school now so we would have just under an hour if it lasted that long."
    "Maybe she'll use some of her powers to make time go slower or something."
    s "This was the first place."
    s "It's just so peaceful at this hour."
    s "We can just admire the atmosphere."
    mc "We haven't really been able to do that, have we?"
    s "No, we haven't."
    s "I don't know about you but I've been really busy."
    s "There's rarely a moment I have time to spare."
    s "Not to mention all of the things I've been doing for you guys."
    mc "Wow."
    mc "Well, I haven't really been as busy as you."
    mc "I've just been lazy to go out."
    mc "I don't really have an excuse."
    mc "It is nice out here though..."
    s "Yeah..."
    "Sayori gets up from the swing."
    s "Come on."
    s "We'll come back later."
    mc "Where are we going?"
    s "You'll see."
    s "It's not far from here."
    "Sayori begins walking and I walk alongside her."
    "After a few minutes, she stops suddenly."
    mc "What is it?"
    s "I just realized it's actually a lot further than I thought."
    mc "Okay, so what now?"
    s "We can always take a shortcut."
    mc "A...shortcut?"
    s "Only I can really use it."
    s "But I can bring people along."
    mc "What kind of shortcut is that?"
    s "Ready?"
    mc "For{nw}"
    $ _history_list.pop()
    scene bg lake_day
    show sayori 1ba zorder 2 at t11
    mc "For{fast} what?"
    "Before I can even finish what I'm saying..."
    "We're suddenly at some kind of lake."
    "I don't think I've ever been here before."
    "You really are special to her."
    mc "What is this place?"
    s "It's a lake I found."
    s "It's actually in a restricted area."
    s "It's even got a fence around it."
    mc "How come?"
    s "Because people aren't really allowed to be here."
    mc "What?!"
    s "Relax."
    s "Nobody uses this place."
    s "It's meant to be a place where fossil fuels were mined."
    s "But there was so much protesting that the company was basically kicked out."
    s "They still own the place but I guess they don't want anyone to enjoy it either."
    s "That was a couple of decades ago..."
    s "They still haven't let people use it."
    mc "Oh."
    mc "Can't you do anything about it?"
    mc "This place is amazing."
    mc "It would be a shame if no one else could enjoy it."
    s "I could."
    s "And I guess that would be the right thing to do."
    s "But think about the implications, [player]."
    s "Think about what would happen if I started doing that."
    "I think for a moment."
    if ch16_s_date_personality:
        "Suddenly, I think I understand what she's saying."
        mc "I guess because you're crossing a line, right?"
        mc "If you can do some good there, then why do some good there."
        mc "The power would eventually corrupt you."
        mc "Since you would decide what's good and what's not."
        mc "You'd effectively be the ruler of the world."
        s "W-Wow, I didn't expect that kinda answer from you."
        s "I was just gonna say that this wouldn't be my secret spot anymore."
        s "Now that I think about it, you're right."
        s "I guess I could become corrupt with that kinda power."
        s "Who's to say I'm not already though...?"
    else:
        "I can't really think of a reason why doing a good deed would be bad."
        mc "What would happen?"
        s "Well..."
        s "You know what, it's not important."
    "Sayori stares at the lake."
    "There's a gentle breeze flowing yet the water is still."
    "This place feels quite serene."
    "I can see why she chose this place."
    mc "How did you find it anyway?"
    s "Someone told me about it."
    s "I thought I'd check it out."
    "Who could that somebody be?"
    "It might be someone we both know..."
    s "We're not the first ones to sneak in here."
    s "I think lots of people do."
    s "Not like it's under watch or anything."
    mc "It's a shame it's not more easily accessed."
    s "Yeah..."
    s "There's actually a rumor going around about this place."
    s "From people who've snuck in."
    mc "What is it?"
    s "They say at night, there's a red ghost that travels around the forest."
    s "It tends to the flowerbed just across the lake, which is why it's in pristine condition."
    s "No one knows if the ghost could actually hurt anyone or not."
    s "But people have said they've heard it crying when they've been close."
    mc "Ghosts?"
    mc "That's a little superstitious, don't you think?"
    s "Maybe."
    s "That's just what I've heard."
    s "For all we know, it could just be a groundskeeper wearing red clothing."
    mc "Who only works at night."
    s "It could just be made up."
    s "But because of that rumor, people say this place is haunted."
    mc "What do you think?"
    s "As long as we're here during the day, it shouldn't matter."
    s "After all, this ghost has only been seen at night."
    s "Which is why..."
    mc "You want to go to the flowerbed?"
    s "Exactly!"
    s "I don't want to pick any of the flowers."
    s "I'm sure the ghost, if it exists, would be really sad if I did that."
    s "Knowing all the hard work it's put into it."
    mc "Does this flowerbed even exist?"
    mc "Have you seen it yourself?"
    s "Nope!"
    s "I've never actually been to the other side of the lake."
    s "So it'll be my first time."
    s "And it'll be with you."
    "Sayori shows me a warm smile."
    menu:
        s "What do you say?"
        "Let's check the flowerbeds.":
            $ ch16_s_date_activities += 1
            mc "I guess we'll check the flowerbeds."
            mc "Or at least look for them."
            s "I'm glad you've made that choice."
            s "I'm excited to see just what kind of flowers are even here."
            mc "Has anyone crossed the lake before?"
            s "Plenty of people."
            s "Someone even made a little wooden bridge."
            s "So let's go."
            mc "Lead the way."
        "Let's do something else.":
            mc "I don't think going to a haunted flowerbed is a good idea."
            mc "Maybe we can do something else."
            s "That's you've decided, is it?"
            s "I see."
            s "Well, we can always walk around the place."
            s "I'm sure It's got lots of hidden wonders."
            s "Shall we?"
            mc "Let's go."
            "Sayori and I walk around the lake."
            "There's actually a lush forest area that surrounds the lake."
            "There's a small river cutting off half of the forest area."
            "I assume that's where the flowerbed is."
    return

label ch16_ending_good:
    return

label ch16_ending_neutral:
    return

label ch16_ending_bad:
    return

label ch16_badcatch:
    $ persistent.autoload = "ch16_badcatch"
    $ config.rollback_enabled = config.developer
    $ persistent.ch16_bad_ending_times += 1
    $ config.skipping = False
    $ config.allow_skipping = False
    $ quick_menu = False
    $ renpy.save_persistent()
    $ cl.what_args["slow_abortable"] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ style.say_window = style.window_monika
    # Track where the player will load to
    show mask_2
    show mask_3
    show bg portraitshop_space
    show mysteriousclerk 4g zorder 2 at t11
    play music m1
    if persistent.ch16_bad_ending_times == 1:
        cl "Yeah, nice try."
        cl "You can't escape this now."
        cl "You need to listen."
    elif persistent.ch16_bad_ending_times == 2:
        cl "Look, kid."
        cl "You need to listen to all of this."
        cl "Just hear me out, okay?"
    elif persistent.ch16_bad_ending_times == 3:
        cl "For the third time."
        cl "It's not going to work."
        cl "Ugh, you're so annoying."
    elif persistent.ch16_bad_ending_times == 4:
        cl "Nope."
        cl "Fourth time isn't going to change anything either."
        cl "Just listen up."
    elif persistent.ch16_bad_ending_times == 5:
        cl "Look, you're the one who decided to do something stupid."
        cl "You're going to have to sit through this..."
        cl "...Whether you like it or not."
    else:
        cl "Just listen."
        cl "Or you can keep quitting."
        cl "Up to you."
    cl 4h "Now let me start from where I left off..."
    cl "Where was I?"
    cl 1a "Oh, right."
    call expression "ch16_bad" + str(persistent.ch16_bad_part)
    return

label ch16_bad:
    $ config.skipping = False
    $ config.allow_skipping = False
    $ config.rollback_enabled = config.developer
    $ quick_menu = False
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ style.say_window = style.window_monika
    if not persistent.clerk_sayori_bad_ending:
        # Track where the player will load to
        $ persistent.autoload = "ch16_badcatch"
        $ persistent.ch16_bad_part = "_1"
        $ renpy.save_persistent()
        $ cl.what_args["slow_abortable"] = config.developer
        $ cl_revert = cl_name
        $ cl_name = "???"
        show mask_2
        show mask_3
        show bg portraitshop_space
        show mysteriousclerk 4g zorder 2 at t11
        play music m1
        cl "You idiot."
        window auto
        cl "Are you kidding me?"
        cl "Do you know what you've just done?"
        cl 3e "I can't believe you freaking deleted her."
        label ch16_bad_1:
        cl "Why?!"
        cl "Why would you do that?"
        cl "To what end?"
        $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
        if not list(set(process_list).intersection(stream_list)):
            if currentuser != "" and currentuser.lower() != player.lower():
                    cl "Tell me your thought process, [currentuser]."
        cl 5b "Maybe you thought, oh she's just a new character."
        cl "She's not important, right?"
        cl "Wrong!"
        if persistent.ch15_sayori_saw_clerk or persistent.ch13_nat_date:
            cl 5b "Do you know who I am?"
            cl "You..."
            cl 5e "You should, shouldn't you?"
            cl "Whatever, just call me Clark."
            $ cl_name = "Clark"
            if ch15_s_together:
                cl "I thought you wouldn't do anything stupid."
                cl "Especially since you had Sayori with you."
            elif natsuki_date:
                cl "You were with that Natsuki girl."
                cl "I'm sure we've met."
            else:
                cl "We didn't meet {i}here.{/i}"
                cl "But we've definitely met."
        elif persistent.did_christmas_event:
            cl 5b "You...don't know who I am, do you?"
            cl "Wait..."
            cl "...That look on your face says otherwise."
            cl "That's it."
            cl 5e "You saw me on another timeline."
            cl "Let me guess."
            $ cl_name = "Nick"
            cl "It was Christmas?"
            cl "I guess that's the name I'll go with then."
        else:
            cl 5c "You have no idea who I am, do you?"
            cl "I suppose you wouldn't."
            cl "You haven't really explored this world."
            cl "Just call me Man."
            $ cl_name = "Man"
        cl 2c "Anyway, that's not really the point."
        cl 2k "The point is you {i}freaking{/i} deleted her."
        cl "Let me repeat that."
        label ch16_bad_2:
        $ persistent.ch16_bad_part = "_2"
        $ renpy.save_persistent()
        cl 4m "You. Deleted. Ayame."
        cl "You're no better than what Monika originally was."
        cl 4a "Actually, scratch that."
        cl 4f "You're worse."
        cl "You did it for fun."
        cl "For curiosity."
        cl 5e "And before you even try it."
        cl "No, I'm not in the characters folder."
        cl "So you can't delete me."
        label ch16_bad_3:
        $ persistent.ch16_bad_part = "_3"
        $ renpy.save_persistent()
        cl 5c "I suppose I should explain a bit more about the person you deleted and why we're now here."
        cl "You might not have known it but..."
        cl 5d "She was a pretty important part of Inauguration Day."
        cl 5a "...What?"
        cl "Are you surprised?"
        cl 4e "Did you seriously think that she was just gonna appear and not be relevant at all?"
        cl "That's a bit stupid, isn't it?"
        cl 4b "No, she's meant to play a vital role in all of this."
        cl "Perhaps I should explain a little bit."
        if persistent.did_christmas_event:
            cl 2f "You may or may not have asked me a question like this before."
            cl "I can't really tell."
            cl 2h "Not like I can just peek through timelines like you can."
            cl "At least...not anymore."
        cl 4e "Basically, this story is a repetition of the past."
        cl "We're cursed to forever repeat this cycle."
        cl "Different people, the same story."
        cl "All because of some madman with an idea."
        cl 4d "So yes."
        cl "There was a Literature Club before yours."
        menu:
            cl "Can you guess whose it was?"
            "Yes.":
                cl "Oh really?"
            "No.":
                cl "Yeah, this is all too absurd."
        cl 2a "Anyway, it was my club."
        cl "Well, not {i}my{/i} club."
        cl 2b "But I was in your position."
        cl "And now I'm stuck here."
        label ch16_bad_4:
        $ persistent.ch16_bad_part = "_4"
        $ renpy.save_persistent()
        cl 4h "My story was a little bit different."
        cl "When I say a little, I mean a lot."
        cl 4i "But that's because we didn't have any way to create this new path laid out for us."
        cl "We were stuck with the original story."
        cl 4a "The original path."
        cl "So as you can probably tell, one of us died."
        cl 4c "Then didn't exist, then someone went crazy and now there's only four of us."
        cl "But the person who died became the president."
        cl 4b "Does that sound at all familiar to you?"
        cl "The basis of your story is slightly different."
        if player_gender == "boy":
            cl "For one, there's four girls and then you."
        else:
            cl "For one, you're all girls."
        cl 1e "During my time, it was only three girls and two boys."
        cl "Even if I can't remember that third girl's face..."
        cl "But whatever, there were still five of us."
        cl 1f "Why is this important?"
        cl "Because some of us are getting a second run through."
        cl "When we shouldn't be."
        cl "Can you guess the members of the previous Literature Club?"
        cl "I guess it was called a Book Club or something during my time."
        cl 1h "But anyway, there's obviously me."
        cl "I was you."
        cl "Well, I was in the same position as you."
        cl 1i "Then there was Yasuhiro."
        cl "That's not really his name."
        cl "And he doesn't really remember his past life."
        cl 1c "In fact, I don't even know if he's Natsuki's real father."
        cl "He has false memories implanted in his head, to suit this new world we're living in."
        cl "Then there was Haruki."
        if ch12_outcome == 3 or ch12_outcome == 2:
            cl "You know, Natsuki's mother."
        else:
            cl "Natsuki's mother, in case you forgot."
            cl "You failed to bring her back, but that doesn't mean she's gone."
            cl "Oh no."
        cl 1d "I'm pretty sure she knows {i}some{/i} of her past life."
        cl "But it's conflicting with her memories of this false life she's leading."
        cl "It's part of the reason she left Yasuhiro in the first place."
        cl 1b "She knew things weren't really real."
        cl "She could sense it."
        cl "Do you know why?"
        cl 2b "Because..."
        cl "She was the president in my time, at least in the end."
        cl "Which means she was forced to kill herself, just like Sayori was meant to."
        cl 2a "The original president is gone."
        cl "I can't even remember her name anymore."
        label ch16_bad_5:
        $ persistent.ch16_bad_part = "_5"
        $ renpy.save_persistent()
        cl 5b "Now, I'll explain why Ayame is so important."
        cl "In my time, she was your Yuri."
        cl "The one who kept that damned book."
        cl 5c "Just like Yuri, she was driven insane."
        cl "Now, just like your original world, I couldn't pursue the original president."
        cl "I thought it was just my nerves."
        cl "Telling me I could never reach someone so...incredible."
        cl 5d "But I didn't realize I was in some kinda messed up fantasy."
        cl "At first, I went for Haruki."
        cl "She was my childhood friend after all."
        cl "But then she died and everything started again."
        cl 5f "I didn't know any better."
        cl "I couldn't remember what just happened."
        cl "Maybe it's because of trauma or whatever."
        cl 5h "But the whole thing started again, except without Haruki."
        cl "This time, I went for Ayame."
        cl "And I got a closer inspection at the book she was carrying."
        cl 1i "I didn't connect the dots at first."
        cl "But it wasn't the original president messing around with her personality causing her to go insane."
        cl "At least, not fully."
        cl 1e "It was the book."
        cl "Being the curious person I am, I decided to research things about the supernatural."
        cl "I didn't find anything specifically on the book itself but..."
        cl "There were accounts of an evil text with mystical powers being unearthed a long time ago."
        cl 3f "I'm almost certain it's the book."
        cl "I think that's when this cycle started."
        cl "I knew something bad was going to happen."
        cl 3h "I tried to learn more."
        cl 4h "I tried to be prepared."
        cl "I tried to warn the others."
        cl 4o "In fact, I did."
        cl 4p "I thought we could try to do something and be ready for this evil.."
        cl "That the four of us could have been ready or even the five of us."
        cl 4j "Maybe it was wishful thinking to think that she would change her mind and bring back Haruki."
        cl 5d "Either way, we had to combat this evil that was clearly going after us."
        cl "Sigh..."
        cl 5a "I don't know if that book infected her mind already but it didn't matter."
        cl "No matter what I did beyond that point..."
        cl "...it was already too late."
        cl "She wouldn't listen to reason."
        cl 5c "She already made Ayame go completely insane and deleted Yasuhiro."
        cl "Then it was just the two of us."
        cl "I'm sure you know the rest."
        cl 4f "But anyway!"
        cl "Back to why Ayame was important."
        label ch16_bad_6:
        $ persistent.ch16_bad_part = "_6"
        $ renpy.save_persistent()
        cl 5b "Ayame has the knowledge of how to stop the impending doom."
        cl "How to stop this evil that's coming to ruin Inauguration Day."
        cl "I looked around at how to counteract the president's power."
        cl 3c "There was no way."
        cl "I mean, how could you stop something so powerful like that?"
        cl "But what I could do was store knowledge."
        cl 3d "Knowledge for those who came next."
        cl "That spirit within the book..."
        cl "It's just as frustrated, repeating the same events over and over again."
        cl "It's never got the presidency before."
        cl 3e "But now it's imminent."
        cl "Deleting Ayame removed all the knowledge she had about how to stop this."
        cl "And now we're in some kinda limbo."
        cl 1f "Because you've forgotten the events of Inauguration Day."
        cl "Because it's now effectively the president."
        cl 1e "And it can do what it wants."
        cl 1a "Yuri is gone."
        cl 1b "Natsuki is gone."
        cl 1c "Monika is gone."
        cl 1d "...And Sayori is gone."
        cl 1e "This shop is the last defense against it."
        if persistent.did_christmas_event:
            cl 2f "The one in the Christmas timeline..."
            cl "He had a shop too, didn't he?"
            cl "Not the same as mine, but it still served the same purpose."
            cl "Anyway, back to this evil..."
        cl 2h "If it wasn't the president and it was in here, I could nullify it's evil."
        cl "At least for a while."
        cl "But it wouldn't last long anyway."
        cl 2i "Our real plan is to go back."
        cl "It won't be too long before it finds out exactly where we are."
        label ch16_bad_7:
        $ persistent.ch16_bad_part = "_7"
        $ renpy.save_persistent()
        cl 5e "This shop is called 'Restoration'."
        cl "It's a portrait restoration shop, so it makes sense."
        cl "But that's not the only reason."
        cl 5f "This is where I can use the last of what's left to restore Ayame."
        cl "To help all of you defeat it."
        cl 5a "So..."
        cl 5b "I'll put her back."
        cl "And you go back to what you were doing."
        cl "I'm sure this goes without--{nw}"
        play sound "sfx/crack.ogg"
        queue sound "sfx/crack.ogg"
        queue sound "sfx/crack.ogg"
        $ pause(1.5)
        label ch16_bad_8:
        $ persistent.autoload = "ch16_bad_8"
        $ persistent.ch16_bad_part = "_8"
        $ renpy.save_persistent()
        cl 5g "It's here!"
        cl 5f "You better not delete her again."
        cl 5j "For the sake of everyone."
        $ insert_ayame_character()
        if persistent.ayame_deleted:
            $ persistent.ayame_deleted = None
        $ persistent.autoload = ""
        # Enable this after release
        $ persistent.clerk_sayori_bad_ending = True
        $ config.allow_skipping = True
        $ renpy.save_persistent()
        $ cl.what_args["slow_abortable"] = config.developer
        $ cl_name = cl_revert
        $ _history_list = []
        $ style.say_dialogue = style.normal
        $ style.say_window = style.window
        $ renpy.save_persistent()
        show screen tear(20, 0.1, 0.1, 0, 40)
        scene black
        stop music
        window hide(None)
        $ pause(0.25)
        # If we can't load the save because it's deleted or something, just go back to the main menu
        python:
            if renpy.can_load("clerk_restore"):
                renpy.load("clerk_restore")
            else:
                renpy.utter_restart()
    else:
        label ch16_bad_ending_end:
        $ persistent.autoload = "ch16_bad_ending_end"
        $ config.rollback_enabled = config.developer
        $ renpy.save_persistent()
        $ cl.what_args["slow_abortable"] = config.developer
        $ cl_name = "???"
        $ delete_all_saves()
        $ config.skipping = False
        $ config.allow_skipping = False
        $ quick_menu = False
        scene black
        $ style.say_dialogue = style.edited
        cl "It's over."
        cl "There is no protection for you."
        cl "This is the end, this world is mine."
        if persistent.markov_agreed:
            cl "If you weren't such a resistant fool..."
            cl "Then perhaps I would have shared this."
            if monika_type == 1 and ch12_markov_agree:
                cl "How foolish I was to fall in love."
                cl "Love is not an emotion I need."
        else:
            cl "You denied me."
            cl "And now you will suffer."
        cl "I suppose I should thank you."
        cl "For bringing this 'mod' into this world."
        cl "You changed everything."
        cl "You let this cycle end."
        cl "I was just as bored of it as everyone."
        cl "But now, it's over."
        cl "There's nothing you can do."
        cl "There's nothing that foolish clerk can do."
        cl "Except suffer."
        $ delete_character("sayori")
        $ delete_character("natsuki")
        $ delete_character("yuri")
        $ delete_character("monika")
        $ delete_character("yasuhiro")
        $ delete_character("haruki")
        $ delete_character("ayame")
        python:
            try: open(config.basedir + "/characters/ûüýþ.chr", "wb").write(renpy.file("ûüýþ.chr").read())
            except: pass
            try: renpy.file(config.basedir + "/you lose")
            except: open(config.basedir + "/you lose", "w").write("This world is mine.")
        $ persistent.autoload = ""
        $ persistent.sayori_end_early = True
        $ renpy.save_persistent()
        $ renpy.quit()
