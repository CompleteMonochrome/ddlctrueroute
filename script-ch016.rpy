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
    "I get the feeling It was some kind of message."
    "Anyway..."
    $ ay_pers_chance = renpy.random.randint(1,20)
    if ch15_s_together and ay_pers_chance == 20:
        $ ch16_ay_perspective = True
        "I'm up early because there's some set up we need to do.{nw}"
        $ _history_list.pop()
        show screen tear(8, offtimeMult=1, ontimeMult=10)
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
        "We're meant to be prestigious, we're meant to be the best of the best."
        "But now I know."
        "That's all some made up story."
        "I haven't awakened all of my memories just yet."
        "But I know enough."
        "They will pay."
        "All of them."
        "Once I get rid of this facade--"
        "Why do they have to suffer?"
        "They didn't do anything."
        "They're just as much of a victim as I am."
        "What would he think of me...?"
        "Would he think of me as some kind of monster?"
        "He was the one who told you."
        "And you still went crazy."
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
            mc "And...you know."
            mc "What you said last night."
            m 1e "Don't worry."
            m "I'll have everything you want to know."
            m "But {i}after{/i} this is over, okay?"
            mc "Okay."
            mc "I look forward to it."
            m 1j "As do I."
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
        n "Looks like I'll have to show you some them sometime."
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
        if natsuki_date:
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
        if (natsuki_date or monika_type == 0) and ch13_name == "Natsuki":
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
    n "Where is exactly is 'here'?"
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
        s 2l "It's perfectly fine.{nw}"
        $ _history_list.pop()
        show screen tear(20, 3, 2, 0, 70)
        $ pause(1.0)
        scene bg portraitshop_school
        show sayori 1younga zorder 2 at i11
        hide screen tear
        $ pause(1.0)
        window show(None)
        $ s_name = "???"
        $ d_name = "???"
        $ mo_name = "???"
        s "It's perfectly fine.{fast}"
        window auto
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
        "That weren't my memories."
        "I didn't recognize any of those people."
        "But that room."
        "It's...the same as this one?"
        "What does this all mean...?"
        show sayori zorder 3 at f32
        s "Hellooooooo?"
        s "[player]?"
        show sayori zorder 2 at t32
        mc "W-What?"
        show natsuki zorder 3 at f31
        n "Uhh...are you okay?"
        n "Because you don't look like you're okay."
        show natsuki zorder 2 at t31
        mc "I think I'm okay..."
        mc "Why? What happened?"
        show natsuki zorder 2 at t31
        show yuri zorder 3 at f33
        y "You just kinda stood there."
        y "You wouldn't respond to anything we said."
        y "You wouldn't even blink."
        show yuri zorder 2 at t33
        mc "Well, I'm fine now."
        mc "I just had a weird thought."
        mc "Sorry for worrying you guys."
        show sayori zorder 3 at f32
        s "Well, if you have any more of those..."
        s "Let me know, okay?"
    else:
        s 2l "It's perfectly fine."
    s 1a "Anyway, the reason I brought you all here is to orient you all with the classroom,"
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
    show sayori zorder 2 at t32
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
        show sayori zorder 2 at t31
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
        show mysteriousclerk 4e zorder 2 at t22
        cl "Ding, ding!"
        cl "You're right about that."
        "The stares at me intently then man sighs."
        cl 2c "I quite liked being mysterious."
        cl "But I guess if we're being fully truthful here..."
        cl 2d "Then I should introduce myself properly."
        cl "Especially if we're gonna trust each other."
        show sayori 1c zorder 3 at f21
        show mysteriousclerk zorder 2 at t22
        s "You're gonna tell [player_possessive]?"
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
        call screen dialog(message="To be continued!\nThanks for playing, keep an eye out on reddit and discord for updates!", ok_action=MainMenu(confirm=False))
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
    call screen dialog(message="To be continued!\nThanks for playing, keep an eye out on reddit and discord for updates!", ok_action=MainMenu(confirm=False))
    return

label ch16_play_normal:
    return

label ch16_play_bad:
    return

label ch16_end:
    return

label ch16_sayoridate:
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
