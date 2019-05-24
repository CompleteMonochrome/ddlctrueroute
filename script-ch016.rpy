screen timer_16_menu_skip(jumploc):
    timer 0.5 action Jump(jumploc) repeat True

label ch16_main:
    if (y_appeal >= 1 or y_appealS >= 1) and (m_appeal >= 1 or m_appealS >= 1) and (s_appeal >= 1 or s_appealS >= 1) and (n_appeal >= 1 or n_appealS >= 1) and not yuri_date and not natsuki_date and not ch15_s_together:
        $ get_achievement("*Playboy*")
    if not yuri_date and not natsuki_date and not ch15_s_together and not monika_type == 0 and not (monika_type == 1 and ch12_markov_agree):
        $ get_achievement("*Loneliness Is Bliss*")
    if ch12_markov_agree:
        $ persistent.markov_agreed = True
        $ renpy.save_persistent()
        python:
            try: renpy.file(config.basedir + "/the die is cast")
            except: open(config.basedir + "/the die is cast", "wb").write(renpy.file("the die is cast").read())
        $ get_achievement("*The Die Is Cast*")
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
        $ get_achievement("*Another Perspective*")
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
    elif monika_type == 0 or (ch12_markov_agree and monika_type == 1):
        $ cl_name = "???"
        cl "Well, well."
        "A voice suddenly calls out from behind me."
        "I can feel a hand suddenly reach my shoulder too."
        mc "Who--{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        stop sound
        scene bg corridor
        hide screen tear
        window show(None)
        "I make it to the clubroom with the box."
        window auto
        "I can't believe how hard it was to get here."
        jump ch16_clerk_unknown
    elif persistent.ch15_sayori_saw_clerk or persistent.ch13_nat_date:
        $ cl_name = "???"
        cl "You want some help with that?"
        show mysteriousclerk 2e zorder 2 at t11
        $ get_achievement("*Good Guy Clerk*")
        if monika_type == 0 or (monika_type == 1 and ch12_markov_agree):
            "The man in front of me puts a hand on my shoulder and quickly removes it."
        "This guy...why does he seem so familiar?"
        $ cl_name = "Familiar Clerk"
        mc "What the...?"
    elif persistent.did_christmas_event:
        $ cl_name = "???"
        cl "Hey friend, want some help?"
        show mysteriousclerk 2e zorder 2 at t11
        $ get_achievement("*Good Guy Clerk*")
        if monika_type == 0 or (monika_type == 1 and ch12_markov_agree):
            "The man puts a hand on my shoulder and immediately removes it."
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
    show mysteriousclerk 5c zorder 2 at t11
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
        $ get_achievement("*Blossoming Friendship*")
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
            show natsuki 2i zorder 3 at f21
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
        show layer master
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
        show mysteriousclerk 2e zorder 3 at f22
        cl "What?"
        cl "Isn't it obvious?"
        cl "Here, let me make it simple for you."
        cl "Sayori is the president, right?"
        show mysteriousclerk zorder 2 at t22
        mc "The president of the Literature Club."
        mc "I understand that."
        show mysteriousclerk 2e zorder 3 at f22
        cl "Right."
        cl "And for some reason, whoever the president is can start manipulating this world."
        cl 2d "Don't ask me why."
        cl "It's just one of the rules of this world."
        cl 5a "There is no logical explanation."
        show mysteriousclerk zorder 2 at t22
        mc "Is this a recent thing?"
        mc "Wasn't the Literature Club only formed recently?"
        mc "And why does being the president of some school club grant you that kind of power?"
        show sayori 1c zorder 3 at f21
        s "It's true that the four of us formed the club only a little while ago."
        s "But it looks like this power existed before that."
        s "It seems to go through a cycle that's destined to repeat itself."
        show sayori zorder 2 at t21
        show mysteriousclerk 1f zorder 3 at f22
        cl "That's right."
        cl "And I was in the previous cycle."
        cl 4f "In the very place we're standing."
        cl 4a "We didn't have a Literature Club exactly."
        cl "It was called a Book Club for us."
        cl 4b "And our president...doesn't exist."
        cl "At least, not anymore."
        if persistent.clerk_sayori_bad_ending:
            cl 4e "But you already knew that."
            cl "Didn't you?"
        cl 1i "Anyway, my shop and this room..."
        cl "They resemble each other a lot."
        cl "I guess I got sentimental when I made it."
        cl "But because of that, we can easily blend it with the world when we need to."
        cl 1b "So it all works out, right?"
        show mysteriousclerk zorder 2 at t22
        mc "This is all so confusing..."
        mc "All of this cycle stuff and this power for being president of a club."
        mc "Sayori, how come you didn't tell me any of this sooner?"
        show sayori 1k zorder 3 at f21
        s "I'm sorry, I really should have."
        s "But even if I wanted to, I couldn't."
        s "I didn't even know what this world really was until he explained it."
        s 1h "Even now, it's still sort of a mystery to me."
        s "Not even everything I can do could really prepare me for today."
        show sayori zorder 2 at t21
        mc "I only wanted to help you."
        mc "If only you told me sooner..."
        mc "To prevent those rainclouds from making you do something terrible ever again."
        show sayori 1k zorder 3 at f21
        s "I couldn't tell you because I thought the world would break."
        s "That everything would just disappear and all of this effort would have been for nothing."
        s 2h "But something has changed now."
        show sayori zorder 2 at t21
        show mysteriousclerk 1b zorder 3 at f22
        cl "I think it's got to do with Ayame."
        cl "Your mind is now linked with hers somewhat."
        cl "Which I think is why you're now able to retain your memories with the world exploding."
        cl "Like it would if you knew this information without that link."
        show mysteriousclerk zorder 2 at t22
        mc "This Ayame person..."
        mc "You seem to know a lot about her."
        mc "You even knew she would be at the mall and placed my memories inside her."
        mc "How?"
        show mysteriousclerk 1e zorder 3 at f22
        cl "The thing is, she isn't even meant to be here anymore."
        cl "What's weirder is that even if she was meant to be here, she should be around the same age as me."
        show mysteriousclerk zorder 2 at t22
        mc "And why is that?"
        show mysteriousclerk 1f zorder 3 at f22
        cl "Because she was in the club at the same time as me."
        cl "I don't know why she's still the same age but I have a suspicion."
        cl "What's important is that [player]'s mind is linked with hers."
        cl 1b "Which means you have access to her memories."
        show sayori 2g zorder 3 at f21
        show mysteriousclerk zorder 2 at t22
        s "Since she was an old member, she might know something useful."
        s "In fact, you said you stored some information in her, didn't you?"
        s 2i "We need to find out what that is exactly."
        show sayori zorder 2 at t21
        show mysteriousclerk 1b zorder 3 at f22
        cl "That's correct."
        show mysteriousclerk zorder 2 at t22
        mc "Since you put the information inside her, shouldn't you know what it is?"
        show mysteriousclerk 1h zorder 3 at f22
        cl "No, I don't."
        cl "I put that information inside her as my final desperate act."
        cl "I don't know why..."
        cl 5j "But I can hardly remember the times outside the club I spent researching it."
        cl "Remembering this much has been extremely difficult."
        cl "I doubt I can remember what I stored inside her."
        cl 5d "Perhaps it's a side effect of being in your world."
        show mysteriousclerk zorder 2 at t22
        mc "Okay, so then how can I access her memories?"
        mc "I don't think I can do it at will."
        if ch16_ay_perspective:
            mc "But just this morning--"
        show mysteriousclerk 2c zorder 3 at f22
        cl "It's not that simple."
        cl 2b "But luckily for you, that's why this room is here."
        cl "Think of it as a sort of transmitter among other things."
        cl 2f "This room can send and receive all sorts of data, which is how we were able to send your memories to Ayame yesterday."
        cl "The thing is, she could now possibly access {i}your{/i} memories."
        cl "It's a two way street."
        show mysteriousclerk zorder 2 at t22
        mc "And that's bad?"
        show sayori 1j zorder 3 at f21
        s "It's terrible!"
        s "I scanned through some of the memories you got from her earlier..."
        s "There wasn't anything on whatever it is that's making today seem so sinister."
        s 1f "But I did find out that she's...got tendencies. Things that wouldn't be good at all if she could act on them."
        s 1i "Or at least, she would have tendencies if she wasn't under the influence of this timeline."
        s "It's only a matter of time before she figures out who she {i}was{/i}."
        s 1g "You knowing this information and her having access to your mind doesn't help either."
        show sayori zorder 2 at t21
        mc "But why is her remembering so bad?"
        mc "You're the president, aren't you?"
        mc "You can manipulate this world."
        show mysteriousclerk 5h zorder 3 at f22
        cl "Hmm...I guess I wasn't entirely accurate when I said that."
        cl "The current president can manipulate things in the current world, that's true."
        cl "If Sayori passed on the presidency to someone else, they would be able to do the same thing."
        cl 5e "But the important thing to note is that it's the current world."
        cl "The president can't modify things from previous worlds."
        cl 5f "So we can't simply make Ayame forget."
        cl "I know because Sayori tried it on me when we first met."
        show mysteriousclerk zorder 2 at t22
        mc "So what's the problem then?"
        show mysteriousclerk 5b zorder 3 at f22
        cl "Well, my hypothesis is that the presidency never goes away."
        cl "As soon as a new club starts, there's a new president with equal powers over {i}that{/i} world."
        cl 5g "Which is a problem because we don't know who the president is from my time."
        cl "After the first president disappeared, it was passed onto someone else."
        cl 5a "But that someone else ended the world to stop the suffering."
        cl "Because she did that, she technically gave up her presidency."
        show mysteriousclerk zorder 2 at t22
        mc "Wait...the first president disappeared?"
        mc "What happened to her?"
        show mysteriousclerk 5i zorder 3 at f22
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
        show sayori 2h zorder 3 at f21
        s "We don't know that for sure."
        s "Especially since she's linked up with your memories."
        s "Her world could be our world now through that link."
        s 2k "Or worse, she could bring her old world to this one."
        s "And who knows what would happen then?"
        s "All I know is that if she remembers and we're not prepared, it's not gonna be good."
        show sayori zorder 2 at t21
        show mysteriousclerk 5e zorder 3 at f22
        cl "It explains why she has stayed young."
        cl "She probably subconsciously willed it, along with her rich family and status."
        show mysteriousclerk zorder 2 at t22
        mc "Have you considered that maybe Ayame is what's making the day feel so sinister?"
        mc "It kinda sounds like she's a threat, doesn't it?"
        show mysteriousclerk 1e zorder 3 at f22
        cl "You sure do ask a lot of questions, don't you?"
        cl 1b "But I guess it's benefitting more than one person."
        "He doesn't look at Sayori when he says that."
        "Rather, he stares more intently on me."
        cl 1c "Well, go on then."
        cl "It's gonna worry him, but you said we were gonna be truthful, right?"
        show mysteriousclerk zorder 2 at t22
        "Sayori sighs."
        "She looks at me, reaches my eyes then turns away."
        "After a few moments, she takes a deep breath and turns back to face me."
        show sayori 1g zorder 3 at f21
        s "She isn't the main problem, [player]."
        s "There's something bigger."
        s "I can feel it."
        show sayori zorder 2 at t21
        mc "What could be worse than that?"
        show sayori 1h zorder 3 at f21
        s "I don't know."
        s "I've gone past my limits of seeing into the future."
        s "It almost broke this world."
        s 1k "As it happens, skipping important events to see the future without the previous outcome isn't good."
        if cl_name == "Bradley":
            "Bradley lets out a small chuckle."
        else:
            "The man lets out a small chuckle."
        s 1g "But what I {i}felt{/i}..."
        s "It was beyond anything I've ever felt."
        s "And we don't know {i}anything{/i} about it."
        show sayori zorder 2 at t21
        mc "But if you've seen that far into the future..."
        mc "That means we can stop Ayame, right?"
        show sayori 1c zorder 3 at f21
        s "It's not certain."
        s "It only means there's a possibility."
        s 1d "I must have tried a million times to see beyond that outcome."
        s "I'm not even sure if I'm mentally stable right now."
        s "I can't even remember if she was even fully stopped when the real danger came."
        s 1l "But that's besides the point."
        show sayori zorder 2 at t21
        mc "I'm sorry you had to go through that, Sayori."
        mc "No one should have to."
        show sayori zorder 2 at t21
        show mysteriousclerk 1e zorder 3 at f22
        cl "Now is not time to get sentimental."
        cl "We just finished explaining everything you need to know."
        cl "So now we have work to do."
        show mysteriousclerk zorder 2 at t22
        mc "I get it."
        mc "What do you need me to do?"
        show mysteriousclerk 1f zorder 3 at f22
        cl "Like we said earlier, I stored information inside her."
        cl "And to do that, you're gonna need to be in close contact with her."
        show mysteriousclerk zorder 2 at t22
        mc "But won't that mean she might get my memories of this encounter?"
        mc "This seems too risky."
        show sayori 1h zorder 3 at f21
        s "It really is..."
        s "But..."
        s 1k "It's our only shot."
        s "Otherwise that other threat is going to ruin everything."
        s "There's no other way."
        s "I would know..."
        show sayori zorder 2 at t21
        show mysteriousclerk 2a zorder 3 at f22
        cl "We need you to access those memories, {i}without{/i} alerting her."
        cl "You're our only shot at a happy ending."
        cl "I hope you'll do a better job than I did."
        show mysteriousclerk zorder 2 at t22
        mc "How?"
        mc "How do I do it?"
        show sayori 2c zorder 3 at f21
        show mysteriousclerk zorder 2 at t22
        s "You need to ask her questions."
        s "If you ask the right ones, you'll be able to remember her memories before she can."
        s "If you ask the wrong ones...you'll both remember her memories."
        s 2f "And you know what will happen if she remembers too much."
        s "There's probably more to it than that..."
        s 2d "You'll figure it out, I'm sure."
        show sayori zorder 2 at t21
        show mysteriousclerk 2b zorder 3 at f22
        cl "She has a free slot in her timetable after lunch."
        cl "That would be the best time to talk to her."
        show mysteriousclerk zorder 2 at t22
        "I'm about to say that I have a math class then..."
        "But I think joking about something this serious is probably not a good idea."
        "Especially with the current stakes."
        mc "How is it you know all this?"
        show mysteriousclerk 2c zorder 3 at f22
        cl "Like I said, I'm the equivalent of you from my world."
        "The man shrugs."
        cl "I can do certain things."
        show mysteriousclerk zorder 2 at t22
        mc "But you said it yourself, you're not the president."
        mc "So how--"
        show mysteriousclerk 4j zorder 3 at f22
        cl "The equivalent of {i}you{/i}."
        cl "Maybe that will help you understand."
        cl 4b "Anyway, I should go before someone realizes I'm not a teacher."
        cl "Before I do..."
        "He snaps his fingers."
        hide bg portraitshop_transition_shop
        show bg portraitshop_transition_school zorder 0
        $ pause(3.5)
        "The room turns back to normal."
        "Like it was when we first came in here."
        cl 4d "Good luck."
        show mysteriousclerk at thide
        hide mysteriousclerk
        show sayori 1b at t11
        "Sayori stares at him as he leaves the classroom."
        "She picks up the box of supplies and points towards the classroom's closet."
        s "Can you...?"
        "I open the door for her."
        s 1d "He's super helpful...right?"
        mc "Yeah...he's certainly something."
        "Sayori puts the supplies in the closet and shuts the door."
        s 2d "We should get to class, [player]."
        s "Don't wanna be late and all."
        mc "I think at this rate, we're already late."
        s 4q "Ehehe, probably~"
        "Sayori smiles."
        s 4d "This is probably gonna be the last time I have before I do my best to prevent disaster."
        mc "Sayori, the disaster preventer."
        mc "Sounds good to me."
        s 4l "Ahaha..."
        s "I can already tell it's going to be a long day."
        s 2d "So before it ends, I want to do something."
        s "In the case none of it works out."
        mc "What is it?"
        s "I want you to meet me at lunch."
        s "I'll explain more there."
        mc "But--"
        s 2q "See you then~"
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
        show natsuki 1b zorder 2 at t21
        n "Good! You're here."
        n "I was starting to think you were gonna ditch us."
        n 1c "Yuri, are you sure no one goes here?"
        show yuri 3ph zorder 3 at f22
        y "I've been here several times."
        y "On occasion, a teacher would approach me."
        y "However, students don't really tend to go here."
        y "I think they know I want to be alone..."
        show natsuki 1q zorder 3 at f21
        n "Right..."
        n "That's good enough, I guess."
        n "We won't be here long anyway."
        if yuri_date:
            show natsuki zorder 2 at t21
            show yuri 3pv zorder 3 at f22
            y "Before we go on..."
            y "I want to make sure [player] is committed to this."
            y "I just have a bad feeling about today."
            y "Like this is the last time we'll really get together."
            show natsuki 1m zorder 3 at f21
            show yuri zorder 2 at t22
            n "Oh..."
            n 1r "If you'd rather spend your time together."
            n "I get it."
            n "This is important but I can see why you'd want to spend this moment with each other."
            n "But if you're doing this, you have to be committed."
            show natsuki zorder 2 at t21
            show yuri 2pu zorder 3 at f22
            y "I'll admit, I am rather curious about this."
            y "But if you want to spend this time with just the two of us..."
            y 2ps "I'll understand too."
            y 2pv "If we uncover something we shouldn't..."
            y "Then this could very well be our last time together."
            show natsuki 2e zorder 3 at f21
            show yuri zorder 2 at t22
            n "Okay, I wouldn't go that far."
            n "There's definitely gonna be more times you can hang out in the future."
            n "But there is something about today that's really special."
            n 2g "I can't quite figure it out."
            show natsuki zorder 2 at t21
            show yuri 3pe zorder 3 at f22
            y "Regardless, we don't have to talk about this."
            y "I'm leaving it up to you, [player]."
            menu:
                y "Shall we stay?"
                "Yes.":
                    $ ch16_ny_stayed = True
                    y 3pf "I see."
                    y "If that's your decision, then that must mean you're committed to this."
                    y "I suppose that's that, Natsuki."
                    show natsuki 2a zorder 3 at f21
                    show yuri zorder 2 at t22
                    n "I'm glad I could count on you two."
                    n 2b "Now let's go back to what we were talking about."
                    show natsuki zorder 2 at t21
                "No.":
                    $ ch16_ny_stayed = False
                    y 3pe "Okay."
                    y "I understand."
                    y 3pg "Natsuki--"
                    show natsuki 2j zorder 3 at f21
                    show yuri zorder 2 at t22
                    n "It's alright."
                    n "You two spend your time together."
                    n 2s "Enjoy it, okay?"
                    n "Make sure you say what you have to say."
                    show natsuki zorder 2 at t21
                    mc "What do you mean by that?"
                    show natsuki 2a
                    "Natsuki simply smiles at me."
                    show natsuki 2c zorder 3 at f21
                    n "I'll leave you two here..."
                    n "After all, it is Yuri's spot."
                    n "Maybe I can figure out something on my own."
                    show natsuki zorder 2 at t21
                    show yuri 2pa zorder 3 at f22
                    y "Goodbye, Natsuki."
                    y "And good luck."
                    show natsuki 2d zorder 3 at f21
                    show yuri zorder 2 at t22
                    n "Yeah, you too."
                    show natsuki at lhide
                    hide natsuki
                    show yuri zorder 2 at t11
                    "Natsuki waves goodbye before leaving."
                    "It looked like she was heading in the direction of the library."
                    "It's probably another quiet spot so it makes sense."
                    y 3pf "Shall we get going as well?"
                    mc "What did you have in mind?"
                    jump ch16_y_cancel
        elif natsuki_date:
            n 2s "But before we go on..."
            n "I want to tell you something, [player]."
            show natsuki zorder 2 at t21
            mc "What is it?"
            show natsuki 2g zorder 3 at f21
            n "I don't know why..."
            n "But there's something about this day."
            n 2h "Something terrible."
            n "It almost makes me want to spend it differently."
            show natsuki zorder 2 at t21
            show yuri 3ph zorder 3 at f22
            y "I think I understand, Natsuki."
            y "I'm getting that feeling too."
            y 2pe "If you two would rather be together than discussing this..."
            y "I won't stop you."
            y "Love is greater than curiosity, after all."
            show natsuki 2o zorder 3 at f21
            show yuri zorder 2 at t22
            n "I-It's not love...!"
            n "I-It's...!"
            "Natsuki's face turns a bright red."
            n 2p "W-Well, whatever...!"
            n 2q "It's your decision, [player]."
            n "If you want to spend this time together instead of talking about this..."
            n "Then just say so."
            n 2s "But if you do want to talk about this, you have to be committed."
            menu:
                n "So are we staying?"
                "Yes.":
                    $ ch16_ny_stayed = True
                    n 2s "Okay, great."
                    n "I didn't mean for that to sound like a relief or anything."
                    n 1c "I just respect your decision."
                    show natsuki zorder 2 at t21
                    show yuri 3pb zorder 3 at f22
                    y "Now that that's settled, can we get back to the topic at hand?"
                    show yuri zorder 2 at t22
                "No.":
                    $ ch16_ny_stayed = False
                    n 2q "If that's what you want."
                    n "We can go."
                    n "I really don't blame you for choosing that."
                    n 1s "Even if it does seem kinda selfish."
                    n "Because I feel the same."
                    show natsuki zorder 2 at t21
                    show yuri 2pu zorder 3 at f22
                    y "So that's how it is?"
                    y "Okay then..."
                    show natsuki 1r zorder 3 at f21
                    show yuri zorder 2 at t22
                    n "Yuri, I'm sorry."
                    n "I'm interested too."
                    n 1n "But today is just--"
                    show natsuki zorder 2 at t21
                    show yuri 2ps  zorder 3 at f22
                    y "It's fine."
                    y "You two have your fun."
                    y "But if I may, can I borrow the journal?"
                    y "Maybe I can try to find something out myself."
                    show natsuki 1k zorder 3 at f21
                    show yuri zorder 2 at t22
                    n "Um...sure."
                    "Natsuki gives the journal to Yuri."
                    n 2m "You might not be able to read all of it."
                    show natsuki zorder 2 at t21
                    show yuri 1a zorder 3 at f22
                    y "I'm a fast reader."
                    y "I'm sure I'll manage."
                    y 1b "Goodbye, you two."
                    show natsuki 1q zorder 3 at f21
                    n "That's not what I meant."
                    n "But good luck, Yuri."
                    n 2d "We'll see you later!"
                    show yuri at thide
                    hide yuri
                    show natsuki zorder 2 at t11
                    mc "Bye, Yuri!"
                    "She's already engrossed in the journal when I say that so I get no response."
                    n 2c "Come on, let's not bother her."
                    mc "Right."
                    scene bg school_front
                    show natsuki 2g zorder 2 at t11
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
        show natsuki 1s zorder 3 at f21
        n "Honestly?"
        n "I don't know."
        n 2r "But what choice do we have?"
        show natsuki zorder 2 at t21
        mc "Well, we don't {i}have{/i} to talk about this, do we?"
        mc "Why does it matter?"
        show natsuki 2g zorder 3 at f21
        n "You know why."
        n "If this whole thing was for nothing."
        n 2m "Then what have we been doing?"
        # Monika interrupt
        if monika_type == 0 or (monika_type == 1 and ch12_markov_agree):
            n 1q "What--"
            show natsuki zorder 2 at t31
            show monika 2j zorder 3 at f32
            show yuri zorder 2 at t33
            if monika_type == 0:
                m "Hey, everyone!"
                m "Sorry to interrupt this conversation you're having."
            else:
                m "What are you three doing here?"
                m 2e "Trying to hide something from me?"
            show natsuki 1o zorder 3 at f31
            n "Monika?!"
            n "W-What are you doing here?"
            show natsuki zorder 2 at t31
            show yuri 2pq zorder 3 at f33
            y "How did you find us?"
            show monika 2c zorder 3 at f32
            show yuri zorder 2 at t33
            m "Find you?"
            m 2d "Was this meant to be a secret hiding spot or something?"
            m 2a "Anyway, I just saw [player_reflexive] walk this way and followed him."
            if monika_type == 0:
                m "Is it okay if I talk to him?"
            else:
                m "I need to speak with him."
            show natsuki 2g zorder 3 at f31
            n "I don't know."
            n "We were kind of in the middle of something."
            n 2s "But that's up to him."
            show natsuki zorder 2 at t31
            "Something is telling me I should go with Monika."
            "I get the feeling whatever she has to say is probably more important..."
            mc "Sorry, you two."
            mc "I'll come back if I have time but I'll go with Monika for now."
            show natsuki 4w zorder 3 at f31
            n "Forget it."
            "I can see the visible disappointment in Natsuki's face."
            n "Yuri and I will talk about it."
            n "You don't need to come back."
            n "We won't be here long anyway."
            show natsuki zorder 2 at t31
            show yuri 3pv zorder 3 at f33
            y "Goodbye, [player]."
            y "It's unfortunate things had to be this way."
            show yuri zorder 2 at t33
            mc "But--"
            show monika 4e zorder 3 at f32
            show yuri zorder 2 at t33
            m "Come on, let's go."
            m "I have something to say."
            show monika zorder 2 at t32
            "Natsuki and Yuri stare as Monika and I walk away."
            "I really didn't want to just leave them but..."
            "Monika needs to tell me something."
            scene bg school_courtyard
            show monika 2b zorder 2 at t11
            with wipeleft_scene
            "We don't really go to anywhere in particular."
            "Somehow we ended up walking to the courtyard, one of the most populated areas at school."
            mc "So what did you want to tell me?"
            jump ch16_m_interrupt
        n "What was the point of it all?"
        n 2q "I just..."
        n 2s "...I want to understand, you know?"
        show natsuki zorder 2 at t21
        show yuri 2ph zorder 3 at f22
        y "Now that I've had time to think about it..."
        y "I really want to know."
        y "It's all I could think about all day."
        y "I've been obsessing over it."
        y 2pt "And I don't know why..."
        y "It's like I have this really strong link with the answer."
        y "I can't really explain it."
        show natsuki 2c zorder 3 at f21
        show yuri zorder 2 at t22
        n "Maybe I can."
        n "In the journal, there's a description of someone almost exactly like you."
        n "Some of the details are faded like the name but it can't be a coincidence."
        n 2b "The only difference is some of the appearance."
        show natsuki zorder 2 at t21
        show yuri 3po zorder 3 at f22
        y "Someone exactly like me?"
        y "H-How so?"
        show natsuki 2g zorder 3 at f21
        show yuri zorder 2 at t22
        n "It's got a really fitting description."
        n "Tall, shy girl."
        n "Often misunderstood because of her bashfulness."
        n 2k "Enjoys supernatural and darker themed books."
        n "Adept with sharp objects."
        show natsuki 2g
        "Natsuki eyes Yuri as she says that."
        "Yuri averts her eyes."
        n 2c "The list goes on really."
        n "The main thing I can find that's different is that it says she has brown hair here."
        n "Instead of purple, like yours."
        n "You didn't dye your hair, did you?"
        show natsuki zorder 2 at t21
        show yuri 3pq zorder 3 at f22
        y "O-Of course not!"
        y "It's always been like this."
        y "That description isn't entirely accurate, you know!"
        show natsuki 2e zorder 3 at f21
        show yuri zorder 2 at t22
        n "Come on, Yuri."
        n "Don't kid yourself."
        "Natsuki looks at the journal again."
        n 2b "Well, what are your thoughts [player]?"
        menu:
            n "Is the girl in the book her?"
            "Yes.":
                n 2c "[cPlayer_personal] thinks so too!"
                n "The resemblance is almost perfect."
            "No.":
                n 2c "Maybe not..."
                n "But there is a really big resemblance."
        n "You can't deny that."
        show natsuki zorder 2 at t21
        mc "You're right there."
        mc "If it did say purple hair in there, then that would be really creepy."
        mc "Yuri, maybe someone you know is like that?"
        mc "Your parents or someone you've met at school or..."
        show yuri 3pg zorder 3 at f22
        y "No, I don't know anyone that could possibly fit that description."
        y "I admit, it's uncanny."
        y 3pt "But it can't be me, can it?"
        y "I-I mean just how long ago was that journal entry made?"
        show natsuki 1k zorder 3 at f21
        show yuri zorder 2 at t22
        n "It was made..."
        "Natsuki scans through the page."
        n "...over forty years ago."
        n 1m "But that can't be right."
        n "How else could this have a perfect description of you?"
        show natsuki zorder 2 at t21
        mc "I don't think it's actually Yuri."
        mc "Just someone that's like her."
        show natsuki 1c zorder 3 at f21
        n "What makes you say that?"
        show natsuki zorder 2 at t21
        mc "Think about it."
        if ch15_s_together:
            mc "The people in that book could be old enough to be our--"
            show natsuki zorder 2 at t31
            show yuri zorder 2 at t32
            show sayori 4a zorder 3 at f33
            s "Hi, everybody!"
            s "Are you guys having a meeting without me?"
            s 4d "Or is this like that time in the clubroom?"
            show natsuki 1o zorder 3 at f31
            show sayori zorder 2 at t33
            n "Sayori!"
            n "Do you mind?"
            n "[cPlayer_personal] was in the middle of something."
            show natsuki zorder 2 at t31
            show sayori 4m zorder 3 at f33
            s "Oh..."
            s 5a "Ehehe, sorry~"
            s "But I really need to talk to him."
            show yuri 3pe zorder 3 at f32
            show sayori zorder 2 at t33
            y "Can it wait?"
            y "We won't be too long."
            show yuri zorder 2 at t32
            show sayori 5b zorder 3 at f33
            s "It really can't wait."
            s "It's super, duper important."
            s 5a "Is it okay if we talk, [player]?"
            show natsuki 2e zorder 3 at f31
            show sayori zorder 2 at t33
            n "H-Hold on a second!"
            n "You can't just do that!"
            n "We were so close..."
            show natsuki zorder 2 at t31
            show sayori 2c zorder 3 at f33
            s "So close to...what?"
            s "Why is it you're keeping this a secret from me?"
            show yuri 1h zorder 3 at f32
            show sayori zorder 2 at t33
            y "Sayori, no one said anything about keeping secrets."
            y "It's just what you've said."
            show yuri zorder 2 at t32
            show sayori 2h zorder 3 at f33
            s "I don't have time for this!"
            s "You can discuss without [player_reflexive]."
            "I've never seen Sayori so demanding before."
            "What is going on...?"
            "This whole thing must be putting {i}that{/i} much stress on her."
            "I think Natsuki and Yuri can feel it too."
            s 2i "It won't change anything."
            s "Trust me."
            show sayori zorder 2 at t33
            mc "I think..."
            "I turn towards Natsuki and Yuri."
            mc "I think I'd better go with her."
            mc "Okay?"
            show natsuki 1q zorder 3 at f31
            n "Y-Yeah...okay."
            n "Go on."
            n "We'll just finish up here."
            show natsuki zorder 2 at t31
            "There's a hint of anger on Yuri's face for a moment..."
            "...then she just sighs."
            show yuri 1v zorder 3 at f32
            y "If that's what you want."
            y "Who are we to stop you?"
            show yuri zorder 2 at t32
            mc "Sorry about this."
            show sayori 1f zorder 3 at f33
            s "Come on, let's go."
            scene bg school_grounds
            show sayori 1d zorder 2 at t11
            with wipeleft
            "Sayori takes us to one of the benches in the yard."
            "She takes a seat and I sit opposite her."
            mc "So..."
            mc "What are we here for?"
            s "I just..."
            jump ch16_s_interrupt
        mc "The people in that book could be old enough to be our parents."
        mc "But that wouldn't really make any sense."
        show natsuki 2h zorder 3 at f21
        n "Our parents...?"
        n "Do we {i}know{/i} anyone like the people in the book?"
        n 2g "If they really were our parents, then we'd have to go back to their time."
        n "To see how they would act."
        n "But it's not like we really have the power to do that."
        show natsuki zorder 2 at t21
        show yuri 1k zorder 3 at f22
        y "That's a shame."
        y "I really would have liked to solve this mystery."
        y 1v "There must be something more we can do."
        "Yuri frowns."
        y 1e "What about the descriptions?"
        y "Maybe there's something in there?"
        show natsuki 2r zorder 3 at f21
        show yuri zorder 2 at t22
        n "The journal is old so some of it is faded out."
        n "It just so happens that the descriptions are pretty much unreadable except the one that matches yours."
        n "So..."
        n 2s "...I guess we're all out of options."
        n "There's nothing more in this journal we can really talk about."
        n 2n "I thought maybe with Yuri here we could try to figure something out."
        n "But I guess not..."
        n 2q "...unless you're secretly hiding something, [player]?"
        show natsuki zorder 2 at t21
        mc "Me?"
        mc "What would I know?"
        show natsuki 1b zorder 3 at f21
        n "Why don't you tell us more about Monika?"
        n "You talked to her a lot in the first week you were here."
        n 1c "Maybe we can learn something new."
        n "That is..."
        n "...if you can."
        n "You didn't really say anything about her in the clubroom."
        show natsuki zorder 2 at t21
        mc "What would telling you about Monika tell us?"
        mc "I really doubt it's going to change anything..."
        show yuri 2pg zorder 3 at f22
        y "We shouldn't force it out of [player_reflexive], Natsuki."
        show natsuki 4i zorder 3 at f21
        show yuri zorder 2 at t22
        n "Fine!"
        show natsuki zorder 2 at t21
        show yuri 2pr zorder 3 at f22
        y "Maybe you can look over the journal entries again and find something..."
        y "Or maybe there's more."
        y "I mean, there has to be {i}something{/i}."
        show natsuki 4r zorder 3 at f21
        show yuri zorder 2 at t22
        n "That's just it!"
        n "There {i}is{/i} more."
        n "I just can't look at it."
        n 4g "The journal won't let me."
        show natsuki zorder 2 at t21
        show yuri 3pf zorder 3 at f22
        y "What?"
        y "Give it to me, Natsuki."
        "Natsuki gives the journal to Yuri."
        "Yuri tries to look through the journal."
        "She flips through the first couple of pages without any trouble."
        y 3pe "What's wrong with it?"
        show natsuki 2b zorder 3 at f21
        show yuri zorder 2 at t22
        n "Keep reading."
        n "You'll see eventually."
        show natsuki zorder 2 at t21
        show yuri 2pg zorder 3 at f22
        y "Okay..."
        "Yuri keeps turning through the pages."
        "Until she just stops."
        y 2pq "I..."
        y "...can't turn the page."
        y "What is this?"
        show yuri 2po zorder 2 at t22
        "Yuri tries to turn the page again but can't."
        "She looks like she's actively struggling against the book."
        "Natsuki takes the book back from her."
        show natsuki 2k zorder 3 at f21
        n "That's interesting."
        n "You can only seem to see up to there in the journal.."
        n 2c "But I can..."
        "Natsuki opens the journal and manages to get past where Yuri got stuck."
        "But after a certain point, she starts struggling too."
        n "See what I mean?"
        n 2g "I'm not usually one to believe in the supernatural but..."
        n "This journal is cursed or something."
        n "Which is why I want to find out the truth."
        show natsuki zorder 2 at t21
        mc "I don't get it."
        mc "It's just a book, isn't it?"
        mc "You're just messing with me."
        show natsuki 2e zorder 3 at f21
        n "We're not!"
        n "Here."
        "Natsuki offers me the journal."
        n 2b "But if I could only get this far..."
        n "Then I doubt you could get any further."
        n "But who knows?"
        show natsuki zorder 2 at t21
        "I take the journal from Natsuki."
        "She looks at me suspiciously as I look at the first couple of pages."
        show natsuki 2k zorder 3 at f21
        n "You can open it at least."
        n "I doubt you can get far."
        show natsuki zorder 2 at t21
        mc "How come?"
        "I close the journal."
        mc "Seems like just a normal journal to me."
        show natsuki 1q zorder 3 at f21
        n "It took me a while before I could even read to where I'm up to right now."
        show natsuki zorder 2 at t21
        show yuri 1g zorder 3 at f22
        y "It took you a while?"
        y "Are you saying that as time went on, you could read more of the book?"
        show natsuki 1k zorder 3 at f21
        show yuri zorder 2 at t22
        n "Not exactly."
        n "It's more like..."
        "Natsuki scratches her head."
        n 1m "It's hard to explain."
        n "But it's like the more I thought about the world..."
        n "The more I could read into it."
        n "I actually found the journal a while ago."
        n "And I couldn't even open it."
        n 1s "I didn't want to tell anyone because I'd sound crazy."
        n "But recently, with all the weird stuff going on..."
        n "I could actually open it."
        show natsuki zorder 2 at t21
        show yuri 1h zorder 3 at f22
        y "The more you questioned the world..."
        y "Maybe that's the key."
        y "But we don't really have anything to go on."
        show natsuki 1q zorder 3 at f21
        show yuri zorder 2 at t22
        n "Yeah."
        n "Anyway, go on [player]."
        n 1k "See just how far you can get."
        show natsuki zorder 2 at t21
        mc "There's nothing special about this."
        mc "You guys are just messing with me."
        mc "Look."
        "I quickly flick through the whole book."
        "I don't really look at any of the details but I manage to go through all of it."
        mc "See?"
        mc "I knew you guys were just playing around."
        show natsuki 3o zorder 3 at f21
        n "W-What?"
        n "How can you possibly look through the whole thing?"
        n "This doesn't make any sense..."
        show natsuki zorder 2 at t21
        show yuri 2pq zorder 3 at f22
        y "Maybe [player_personal]'s thought about this world a lot?"
        y "Or maybe [player_personal] is special somehow."
        show yuri zorder 2 at t22
        mc "I don't think I have."
        mc "But in the case you guys aren't just messing with me, I'll play along."
        show natsuki 3g zorder 3 at f21
        n "Go to the part after her death."
        n "It's where I couldn't read past."
        show natsuki zorder 2 at t21
        mc "If it's a journal, why would there be parts after her death?"
        mc "That just doesn't make any sense."
        show yuri 2pf zorder 3 at f22
        y "That's what we're here to find out."
        y "Stop wasting time."
        y 2pr "Just tell us what it says."
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
        show natsuki 3o zorder 3 at f21
        n "Okay!"
        n "You can stop."
        show natsuki zorder 2 at t21
        mc "What's wrong?"
        show natsuki 1q zorder 3 at f21
        n "It's hard to listen to."
        n "Clearly whoever wrote this is in pain."
        n "At this part anyway..."
        show yuri 3pt zorder 3 at f22
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
        show yuri 3ps zorder 3 at f22
        y "Precisely."
        y "I'm wonder how those entries came about."
        y "Maybe it's a different person?"
        show natsuki 1s zorder 3 at f21
        show yuri zorder 2 at t22
        n "You think some person would write in someone else's journal?"
        n "After they committed suicide?"
        n 1m "There's no way someone would do that."
        n "Only someone completely messed up in the head would do that."
        show natsuki zorder 2 at t21
        mc "I'm not sure, but the handwriting seems similar."
        mc "The letters look the same between these two pages."
        mc "So I think it is somehow the same person."
        show yuri 3pe zorder 3 at f22
        y "Maybe they didn't go through with it?"
        y "Maybe there was second thoughts and they were still alive."
        show natsuki 1c zorder 3 at f21
        show yuri zorder 2 at t22
        n "Wait a second, what's the date on the entry?"
        show natsuki zorder 2 at t21
        mc "Why is that important?"
        show natsuki 1g zorder 3 at f21
        n "Just tell me!"
        show natsuki zorder 2 at t21
        mc "Okay..."
        mc "It's dated..."
        "I look at the entry's date."
        "The date looks wrong."
        "I look at the last entry and it's after the next entry's date."
        mc "...almost a week before the last entry."
        mc "What...?"
        show natsuki 2b zorder 3 at f21
        n "It's all starting to make sense now!"
        show natsuki zorder 2 at t21
        show yuri 2pf zorder 3 at f22
        y "It is?"
        show natsuki 2g zorder 3 at f21
        show yuri zorder 2 at t22
        n "No. I was lying."
        n "I thought if I said that I'd have an epiphany or something."
        n 2c "Try looking through the next few pages, [player]."
        n "Maybe we'll learn something."
        show natsuki zorder 2 at t21
        "Epiphany...?"
        "Something about that word..."
        "Normally it wouldn't mean anything."
        "But when I'm near this book it..."
        show natsuki 2e zorder 3 at f21
        n "Hello?"
        n "World to [player]!"
        show natsuki zorder 2 at t21
        mc "Huh? What is it?"
        show natsuki 2f zorder 3 at f21
        n "Are you there?"
        n "Turn to the next page!"
        show natsuki zorder 2 at t21
        mc "Right, sorry."
        mc "I was just thinking about something you said."
        show natsuki 2g zorder 3 at f21
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
        show yuri 1e zorder 3 at f22
        y "What's wrong?"
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "Yeah, aren't you gonna read it to us?"
        show natsuki zorder 2 at t21
        mc "I would, but it's actually unreadable."
        mc "The next couple of pages look like a bunch of scribbles."
        mc "It doesn't {i}say{/i} anything."
        show natsuki 2h zorder 3 at f21
        n "What?"
        "Natsuki looks as if she wants to see the page."
        "She takes a step towards me then immediately turns back."
        n "Okay."
        n 2i "Okay..."
        n "What do the scribbles look like?"
        n "Can you make out any shapes?"
        show natsuki zorder 2 at t21
        mc "I don't think I can."
        mc "Why is that important?"
        show natsuki 2b zorder 3 at f21
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
            show natsuki 2c zorder 3 at f21
            n "It means it could be linked."
            n "Or that there could be some kind of pattern."
        else:
            n "Maybe we can find some kind of pattern."
        n "Or some message encoded in the journal."
        n "Anything, really."
        n 2g "But it's really difficult, since you're the one that has to do it."
        n "Yuri and I can't look at it."
        n "So it's all up to you."
        show natsuki zorder 2 at t21
        show yuri 2ph zorder 3 at f22
        y "Take a close look at the pages, [player]."
        y "You have to see something."
        y 2ps "Some kind of symbol."
        y "A pattern or a loose resemblance to something we know."
        y "That's the only thing that could help solve this mystery."
        show yuri zorder 2 at t22
        mc "Alright, alright."
        mc "I'll take a closer look."
        label ch16_ny_journal:
        call showjournal(journal_corrupt, ["natsuki 1a",t21,"yuri 2a",t22])
        mc "Okay, I've finished looking."
        show natsuki 1h zorder 3 at f21
        n "That didn't take long."
        n "Maybe you missed something..."
        show natsuki zorder 2 at t21
        show yuri 1e zorder 3 at f22
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
        show natsuki 1c zorder 3 at f21
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
                show yuri 2pe zorder 3 at f22
                y "An eye?"
                y "Was it a specific color?"
                show yuri zorder 2 at t22
                mc "Actually, now that you mention it..."
                mc "It was the only thing on the pages that was colored."
                mc "It had a red iris."
                mc "That's really the only thing that stuck out."
                show natsuki 1b zorder 3 at f21
                show yuri zorder 2 at t22
                n "A red iris?"
                n "Hold on a second, didn't you have a book like that, Yuri?"
                n 1c "I remember you bringing it when [player] joined."
                n "I don't know if you ever got to show it to him but..."
                show natsuki zorder 2 at t21
                show yuri 2po zorder 3 at f22
                y "W-Wait, you knew about that?"
                y "I didn't realize you paid such attention to me."
                show natsuki 1b zorder 3 at f21
                show yuri zorder 2 at t22
                n "I pay attention to a lot of things."
                n 1e "But that's besides the point."
                n "Where is that book now, Yuri?"
                show natsuki zorder 2 at t21
                show yuri 1g zorder 3 at f22
                y "I don't have it anymore."
                show natsuki zorder 3 at f21
                show yuri zorder 2 at t22
                n "What?"
                n 1b "Where is it now?"
                show natsuki zorder 2 at t21
                show yuri 2pf zorder 3 at f22
                y "It's gone."
                y "Someone stole it from me."
                show natsuki 2o zorder 3 at f21
                show yuri zorder 2 at t22
                n "Stole it from you?!"
                n "Why didn't you tell anyone?"
                show natsuki zorder 2 at t21
                show yuri 2pq zorder 3 at f22
                y "It wasn't really a big deal."
                y "I'm standing here after all."
                y "Besides, I didn't really wanna bother you all with such a trivial event."
                show yuri zorder 2 at t22
                mc "Getting robbed isn't trivial, Yuri..."
                mc "Were you hurt?"
                mc "Did they take anything else from you?"
                show yuri 2pv zorder 3 at f22
                y "The only thing that happened was that book being stolen."
                y "And no they didn't take anything else from me."
                y 2pw "It happened while I was sleeping."
                y "I left my book on my table and when I woke up, it was gone."
                show natsuki 2m zorder 3 at f21
                show yuri zorder 2 at t22
                n "Maybe you just forgot where you put it?"
                n "It could still--"
                show natsuki zorder 2 at t21
                show yuri 3pv zorder 3 at f22
                y "I don't have it, Natsuki."
                y "I would know."
                show natsuki 1g zorder 3 at f21
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
                show yuri 3pf zorder 3 at f22
                y "Maybe we can simply locate another copy."
                y "There may be one in the library."
                y "Or at some bookstore."
                show natsuki 2c zorder 3 at f21
                show yuri zorder 2 at t22
                n "I doubt it's in the library."
                n "A bookstore could work but we don't really have the time."
                n "I doubt either of those would have it though since they went through the trouble of stealing from Yuri directly."
                show natsuki zorder 2 at t21
                mc "So what do you suggest?"
                show natsuki 1b zorder 3 at f21
                n "With what we know, maybe it's best we just keep going on with our days."
                n "We don't know what could happen next."
                n "And we don't know just how much looking into this could affect us."
                show natsuki zorder 2 at t21
                show yuri 3pg zorder 3 at f22
                y "It's true that we don't have much to work off."
                y "Maybe it would be a good idea to just see how today goes."
                y "Then later we can act when the dots connect."
                show natsuki 1a zorder 3 at f21
                show yuri zorder 2 at t22
                n "In the meantime, you can try to read as much of the journal as you can."
                n "You're the only one of us who can."
                n 1d "Then you can tell us more when it's time to rehearse."
                n "Maybe by then we'll have something we can act on."
                show natsuki zorder 2 at t21
                show yuri 2pe zorder 3 at f22
                y "Why can't we just look through the journal now?"
                y "Maybe there's more beyond those repeated scribbles."
                show natsuki 1j zorder 3 at f21
                show yuri zorder 2 at t22
                n "Maybe there is."
                n "But now I have an idea and I have to act on it."
                show natsuki zorder 2 at t21
                mc "What is it?"
                show natsuki 1g zorder 3 at f21
                n "I can't tell you."
                n "You might not be able to read the journal beyond a certain point if I tell you."
                n 1c "It's better if we keep the factors the same."
                n "Besides, we shouldn't stick around here too long."
                n 1q "People might get suspicious."
                show natsuki zorder 2 at t21
                show yuri 2pg zorder 3 at f22
                y "Isn't that a little paranoid?"
                show natsuki 1q zorder 3 at f21
                show yuri zorder 2 at t22
                n "With cursed books and this weird feeling I'm getting today..."
                n "I think I have the right to be paranoid."
                show natsuki zorder 2 at t21
                show yuri 2pq zorder 3 at f22
                y "I suppose that's true."
                y "Good luck, Natsuki."
                show natsuki 2a zorder 3 at f21
                n "Good luck to the two of you as well."
                n "Now, if you'll excuse me."
                show natsuki at thide
                hide natsuki
                show yuri 2pg zorder 2 at t11
                y "I wonder what she's doing."
                mc "I don't know if what she's doing can help at this point."
                mc "But it must be important if she cut this little meeting we had short."
                y 2pf "I'm sure she has her reasons."
                y "Can you look beyond those scribbles?"
                mc "In the journal?"
                mc "I can give it a shot."
                y 2pa "Just relay the information to us when you can."
                y "I'm going to try to look for a certain book."
                mc "The one you were talking about before?"
                y 2pb "Yes, that's right."
                y "There's a chance I may have left in my locker or somewhere in school."
                y "If I did, then perhaps it will help solve this mystery we have."
                y 2pi "A-Anyway, I'll leave you to it."
                y "Hopefully you can find something out as well."
                mc "I never thought I'd be spending my lunch time reading a book."
                mc "I guess the club has really gotten to me."
                y 3pc "Ahaha, it looks like it has."
                y 3pb "I'll see you later, [player]."
                if yuri_date:
                    y 3ps "It's a shame we didn't get to spend more of this time together."
                    y "I don't know if I should be saying this..."
                    y "But the three of us investigating whatever this is a lot more fun."
                else:
                    y 3ps "This whole investigating thing is a lot more fun than spending lunch alone."
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
        show natsuki 2c zorder 3 at f21
        n "You think you saw a [ch16_ny_clue]?"
        n "..."
        n 2g "That's way too general."
        n "I can't think of anything..."
        n "Are you sure you saw that in all of the pages?"
        show natsuki zorder 2 at t21
        mc "I'm sure..."
        "At least, I think I am."
        show natsuki 2q zorder 3 at f21
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
        show yuri 3pf zorder 3 at f22
        y "What's wrong, [player]?"
        show yuri zorder 2 at t22
        mc "I can't go past this page in the book."
        "The page I'm stuck on is a page with more random scribbles."
        "But I have a feeling the next page is completely different."
        "I just know it."
        "Maybe there's something there...if only I could turn the page."
        show natsuki 2k zorder 3 at f21
        n "You actually lost the ability to read some of it?"
        n 2q "That's not good."
        n "Now we're right back where we started."
        n "Except now we have something [player] saw in it that could mean anything."
        "Natsuki sighs."
        n 2s "I'm starting to think this is hopeless."
        n "We can't even crack this code."
        show natsuki zorder 2 at t21
        show yuri 3ps zorder 3 at f22
        y "We're so close."
        y "I know it."
        y "But now we have nothing to go on..."
        y 3pt "It's a real shame you lost that ability, [player]."
        y "I wonder what could have happened in a few minutes to suddenly lose it."
        show natsuki 2g zorder 3 at f21
        show yuri zorder 2 at t22
        n "Now do you believe us?"
        n "This journal is cursed."
        show natsuki zorder 2 at t21
        mc "I wouldn't have believed you if it didn't happen to me."
        mc "The feeling was so weird..."
        mc "It was like I couldn't control my arms."
        mc "Like they just refused to move."
        mc "It felt so surreal."
        show yuri 2ph zorder 3 at f22
        y "That is the same sensation I felt."
        y "Like there was some invisible force preventing you from looking at the next page, right?"
        show yuri zorder 2 at t22
        mc "That's exactly it!"
        show natsuki 2e zorder 3 at f21
        n "That's great you figured that out and all."
        n "But now we have nothing."
        n "Our only lead was the journal and all we got from it was a [ch16_ny_clue]."
        n 2f "I'm still wondering what the hell it could possibly mean."
        show natsuki zorder 2 at t21
        show yuri 2pg zorder 3 at f22
        y "I'm at a loss as well."
        y "I'm not saying you looked at it wrong, [player]."
        y "But maybe there was something else."
        show yuri zorder 2 at t22
        mc "It's what I saw."
        mc "If you want to look at it yourself, be my guest."
        "I offer the journal with the page open to Yuri."
        "Instead of taking it from me, she flings the book to the ground."
        mc "Yuri?"
        show yuri 2pn zorder 3 at f22
        y "I-I'm sorry."
        y 2po "I don't know what came over me."
        show natsuki 5x zorder 3 at f21
        show yuri zorder 2 at t22
        n "Don't bother, it's the journal's curse or whatever."
        n "It won't let you cheat it like that either."
        show natsuki zorder 2 at t21
        show yuri 2pt zorder 3 at f22
        y "How do you know that?"
        y "Have you tried it yourself?"
        show natsuki 5r zorder 3 at f21
        show yuri zorder 2 at t22
        n "Actually, yeah."
        n "Yesterday, I tried using something to hold a page down."
        n "It was a page I couldn't read."
        n 5s "As soon as I tried to look at it, I immediately closed it."
        n "It's like I wasn't in control of myself."
        show natsuki zorder 2 at t21
        show yuri 2pv zorder 3 at f22
        y "This book is a lot more complicated than I thought."
        y "I wonder what other tricks it has up it's sleeves."
        show natsuki 5q zorder 3 at f21
        show yuri zorder 2 at t22
        n "Well, it doesn't really matter."
        n "We've pretty much done all we could with it."
        n "[player] can't read past a certain point."
        n 4r "And the parts [player_personal] can read don't really help."
        show natsuki 1r
        "Natsuki sits down on the floor."
        n 1u "I give up."
        show natsuki 1t zorder 2 at t21
        show yuri zorder 3 at f22
        y "Natsuki, you can't do that."
        y "You--"
        show natsuki 1s zorder 3 at f21
        show yuri zorder 2 at t22
        n "Why not?"
        n "We don't exactly have anything to work with."
        n "And no offense to you, [player], but you haven't really been that helpful."
        show natsuki zorder 2 at t21
        mc "I'm sorry."
        mc "I'm doing my best here."
        show yuri 2pt zorder 3 at f22
        y "Natsuki, you--"
        show natsuki 1i zorder 3 at f21
        show yuri zorder 2 at t22
        n "Yeah, well..."
        n "It's not good enough."
        n 1h "We're stuck again and now I don't know what to do."
        n "It's as if all this effort has been for nothing."
        show natsuki zorder 2 at t21
        show yuri 2pr zorder 3 at f22
        y "Natsuki--"
        show natsuki 1s zorder 3 at f21
        show yuri zorder 2 at t22
        n "Let's just accept what's coming."
        "Natsuki gets up and brushes off the dirt from her dress."
        n "It's not like we can do anything about it."
        n 2u "Time to--"
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
        n 22c "Y-Yuri--"
        show yuri 3pr zorder 3 at f21
        show natsuki zorder 2 at t22
        y "You started this little investigation."
        y "You want to solve this mystery as much as the rest of us."
        y "You're the one that knows the most about this."
        "Yuri stares into Natsuki's eyes."
        y 3pt "So you can't give up."
        y "You have to think of something."
        y "All of this, it hasn't been for nothing."
        y "There's just a clue we're missing."
        y "I know it."
        y "Please, Natsuki..."
        y 3ps "As your friend, I'm telling you to keep going."
        y "To see this through to the end."
        y "Whether or not that end leads to anything..."
        y 3pt "It's up to us..."
        "Yuri steps back."
        y 3pu "...isn't it?"
        show yuri zorder 2 at t21
        "A few seconds pass."
        "I'm not sure if Yuri's whole speech just then did anything."
        "Natsuki still hasn't moved her head."
        "Eventually she opens her mouth to speak."
        show natsuki 12a zorder 3 at f22
        n "You're right."
        "She shakes her head."
        n 1q "Thanks for slapping some sense into me, Yuri."
        n "Literally."
        n "It is up to us."
        n 1r "We're the only ones that know about this."
        n "If our world is in danger, we could be the only ones who could stop it."
        n 2m "Yuri, I don't want to give up."
        n "And I think I know what we can do."
        show natsuki zorder 2 at t22
        show yuri 2pf zorder 3 at f21
        y "What is it?"
        show yuri zorder 2 at t21
        "Natsuki looks at me."
        "She looks at the journal on the floor then back at me again."
        show natsuki 2q zorder 3 at f22
        n "It doesn't involve [player]."
        n "I'm sorry."
        "She picks up the journal and offers it to me."
        n 2m "Take this."
        show natsuki zorder 2 at t22
        mc "And do what?"
        show natsuki 2h zorder 3 at f22
        n "Try to make sense of it."
        n "You can read further than I can."
        n "Maybe that means something."
        show natsuki zorder 2 at t22
        mc "Well, what are you gonna do then?"
        mc "Why can't I be part of it?"
        show natsuki 2b zorder 3 at f22
        n "We just saw that in a matter of minutes, you lost the ability to fully read the journal."
        n "This plan I have could make it worse."
        n 2k "So I don't want to change things while they're still working."
        show natsuki zorder 2 at t22
        mc "But--"
        show yuri 2pe zorder 3 at f21
        y "She's right, [player]."
        y "The more factors we keep the same, the better chance we have of deciphering that journal."
        y "Maybe you'll regain the ability to read more of it."
        show yuri zorder 2 at t21
        mc "And what if I don't?"
        show natsuki 1g zorder 3 at f22
        n "Then that's the end of the journal's usefulness."
        n "Look, [player]."
        n "I don't want to exclude you from this."
        n 1q "But an important part of my new plan is that you aren't involved."
        show natsuki zorder 2 at t22
        mc "Alright..."
        "I take the journal from Natsuki."
        mc "I get it."
        mc "I'll see what I can do."
        show yuri 2pa zorder 3 at f21
        y "Thank you for understanding."
        y "I hope you can find something new in that journal."
        y "Good luck."
        show natsuki 2c zorder 3 at f22
        show yuri zorder 2 at t21
        n "I'm sure [player_personal]'ll find something."
        n "Yuri, follow me."
        n "We have things to talk about."
        n 2a "We'll see you later, [player]."
        show natsuki zorder 2 at t22
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
        y 1b "I was a little preoccupied in class."
        mc "Not a problem at all."
        mc "So what did you have in mind?"
        label ch16_y_cancel:
        y 3pg "Well...this was a rather spontaneous decision."
        y "So I hope you'll forgive me."
        y "I know we could be doing better things."
        mc "As long as it's with you, I don't mind doing anything."
        mc "Within reason."
        y 3ph "Within reason..."
        y "Well...that removes half of the things I was going to say."
        mc "W-What?"
        mc "What kind of things were you even thinking of?"
        y 2pq "T-That was a joke."
        y "I apologize if it wasn't funny."
        mc "Oh, I didn't even realize."
        mc "It was just a surprise coming from you, that's all."
        y 2pa "Anyway, I actually wanted to go back to my locker."
        mc "What are we doing there?"
        y "It's a surprise."
        y 2pb "Come on, I think you'll like it."
        y "I've been keeping it safe all this time."
        mc "Alright..."
        "Why do I have a bad feeling about this?"
        scene bg school_lockers
        show yuri 1c zorder 2 at t11
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
        show yuri 3pf zorder 3 at f22
        y "A-Ayame?"
        "Yuri stops where she is and turns around to meet Ayame's gaze."
        y "What are you doing here?"
        show ayame 2h zorder 3 at f21
        show yuri zorder 2 at t22
        ay "I could be asking you the same question."
        ay "Didn't you get the memo?"
        show ayame zorder 2 at t21
        mc "What was the memo?"
        show ayame 2i zorder 3 at f21
        ay "You seriously don't know?"
        ay "Somebody here was just murdered!"
        show ayame zorder 2 at t21
        show yuri 3pn zorder 3 at f22
        y "W-What?!"
        show yuri zorder 2 at t22
        mc "You're kidding, right?"
        show ayame 2e zorder 3 at f21
        ay "Yeah, I am."
        ay "Nobody was murdered."
        ay 2f "...Yet."
        show ayame 2h zorder 2 at t21
        show yuri 2pq zorder 3 at f22
        y "Ayame you nearly scared me half to death."
        y "I thought I was in real danger for a moment."
        show ayame 2j zorder 3 at f21
        show yuri zorder 2 at t22
        ay "Hehe, sorry to frighten you, Yuri."
        ay "But seriously, you two aren't allowed here."
        show ayame zorder 2 at t21
        "Yuri approaches Ayame."
        "As Yuri gets closer, a curious look appears on her face."
        show yuri 2pe zorder 3 at f22
        y "Y-You're a school leader?"
        show yuri zorder 2 at t22
        "Ayame looks down and sees her purple ribbon."
        show ayame 1b zorder 3 at f21
        ay "Ah, I see you've noticed."
        ay "It doesn't matter."
        ay "You would have found out about it one way or another."
        show ayame zorder 2 at t21
        show yuri 2pf zorder 3 at f22
        y "I'm just surprised."
        y "It's just..."
        y 2ph "Well..."
        show ayame 1g zorder 3 at f21
        show yuri zorder 2 at t22
        ay "What is it, Yuri?"
        show ayame zorder 2 at t21
        mc "Take your time if you need to."
        show yuri 2pg zorder 3 at f22
        y "I guess just seeing you with that ribbon..."
        y "It just suddenly awakened something in my subconscious."
        y "One of my subconscious desires, I suppose."
        show ayame 1i zorder 3 at f21
        show yuri zorder 2 at t22
        ay "And what would that be...?"
        show ayame zorder 2 at t21
        show yuri 3pk zorder 3 at f22
        y "To be a school leader."
        y "So that I can be recognized."
        y "So that I can be a role model for others."
        y "And..."
        y 3po "...so that I'm not judged for who I am."
        show ayame 2a zorder 3 at f21
        show yuri zorder 2 at t22
        ay "I see..."
        "Ayame scans the locker area."
        ay "Well, it seems safe for now."
        ay "Let's move somewhere more safe."
        ay 2g "I'll explain why on the way."
        scene bg school_secluded
        show ayame 1g zorder 2 at t21
        show yuri 1g zorder 2 at t22
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
        show ayame 2g zorder 3 at f21
        ay "So that's why you can't go there."
        ay "There could be some kind of animal in there and so we need grounds staff to remove it."
        ay "But even if it's nothing, we'd rather be safe than sorry."
        show ayame zorder 2 at t21
        show yuri 2ph zorder 3 at f22
        y "I didn't hear any noises coming from there."
        y "And I visited my locker a lot today."
        show ayame 2h zorder 3 at f21
        show yuri zorder 2 at t22
        ay "I guess you were one of the lucky ones."
        show ayame zorder 2 at t21
        mc "I'm kinda curious about this noise."
        mc "What did it even sound like?"
        show ayame 2a zorder 3 at f21
        ay "I wasn't there, so I don't know for sure."
        ay 2i "But the students all said to me it was the most horrifying sound they've ever heard."
        ay "It was described as some form of screeching."
        ay "And it was combined with that sound that happens when you rub two pieces of foam together."
        ay 2g "I don't know if that's accurate, but that's just what I was told."
        show ayame zorder 2 at t21
        show yuri 4pc zorder 3 at f22
        y "Oh..."
        show ayame 1g zorder 3 at f21
        show yuri zorder 2 at t22
        ay "What's wrong?"
        ay "Do you know something about the noise, Yuri?"
        show ayame zorder 2 at t21
        show yuri  zorder 3 at f22
        y "I...think I do."
        y "You see, it was meant to be a surprise for [player]."
        show ayame 1i zorder 3 at f21
        show yuri zorder 2 at t22
        ay "What?"
        show ayame zorder 2 at t21
        mc "Your surprise for me involved screeching?"
        mc "I'm not sure what to say."
        show yuri 4pd zorder 3 at f22
        y "N-No, it's not like that!"
        y "I ordered something online that I picked up at the mall yesterday."
        y "It had nothing to do with our preparations."
        y 4pc "It was just...a gift for you."
        y "I wasn't sure when to give it to you."
        y "But since we had a moment alone, I thought it would be the perfect time."
        show yuri zorder 2 at t22
        mc "What kind of gift was it?"
        show yuri 4pb zorder 3 at f22
        y "It was meant to be some kind of doll."
        y "And it resembles you...a lot."
        show yuri zorder 2 at t22
        mc "You paid someone to make a doll?"
        mc "Of me?"
        show ayame 1c zorder 3 at f21
        show yuri zorder 2 at t22
        ay "I'm kind of curious now."
        ay "Did you take pictures of [player_reflexive] as a reference?"
        ay 1a "I-I mean, it's none of my business what you do."
        ay "But if that's the source of the noise..."
        show ayame zorder 2 at t21
        show yuri 4pa zorder 3 at f22
        y "I..."
        y "I did."
        y "The doll is special in that it can move on it's own and emit sound."
        y 4pb "I put it into a foam box to keep it safe and I suppose it somehow activated on it's own and started moving."
        y "That's probably where the foam rubbing together sound came from."
        show yuri zorder 2 at t22
        mc "Well, what about the screeching?"
        mc "Did you record me screeching at some point...?"
        show yuri 3pp zorder 3 at f22
        y "N-No...!"
        y "Nothing like that."
        y "I must have placed batteries that were low on charge into it."
        y 3po "The sound must have become distorted and interpreted as some sort of screeching..."
        y "I'm sorry, [player]."
        y "I should have told you about the whole doll thing..."
        show yuri zorder 2 at t22
        "This whole doll thing is kinda creepy."
        "But it's exactly a thing Yuri would do."
        "That's just how she is."
        menu:
            "So what should I say?"
            "Accept her.":
                $ ch16_ay_level -= 1
                mc "You know what?"
                mc "That's just like you, Yuri."
                show yuri 3pt zorder 3 at f22
                y "Huh?"
                show yuri zorder 2 at t22
                mc "Doing things like this."
                mc "Going over the top for someone like me."
                mc "Maybe it is a little creepy, but it was meant to be a gift."
                mc "So it's wrong to see that as a negative."
                mc "It's just something only you would do."
                mc "And I appreciate you a lot for it."
                show ayame 2h zorder 3 at f21
                ay "I'm glad you can accept her for who she is, [player]."
                ay "Seeing that's her personality and embracing it despite it's flaws can be difficult."
                ay "When it comes to my turn to join the club, I hope you'll do the same."
                show ayame zorder 2 at t21
                mc "Of course, Ayame."
                mc "So yeah, Yuri..."
                mc "Don't worry about it."
                mc "I really do love the surprise you thought about giving me."
                show yuri 2pv zorder 3 at f22
                y "W-Well, thanks I suppose."
                y "But now the surprise is ruined."
                y "And people are worried about approaching their locker now..."
            "Scold her.":
                $ ch16_ay_level += 2
                mc "Yuri, there are such things as boundaries."
                mc "I know we're dating but isn't this a little too far?"
                show yuri 2pw zorder 3 at f22
                y "I know..."
                show yuri zorder 2 at t22
                mc "Taking pictures of me..."
                mc "Recording me..."
                mc "And all without me noticing."
                mc "I don't hate you or anything."
                mc "So please don't take this the wrong way."
                mc "But you have to realize there are some things you shouldn't do."
                show ayame 1f zorder 3 at f21
                ay "So that's how it is, huh?"
                ay "She shows you {i}her{/i} way of showing affection and you just scold her for it?"
                ay "I thought your relationship was built on more solid foundations than that."
                ay 1g "That you had accepted her, knowing something like this could happen."
                ay "I...I'm sorry."
                ay "I know it's none of my business, it's just..."
                ay 1a "Well, is this the kind of reception I'm going to get when I join?"
                ay "Am I going to get scolded for revealing my true self too...?"
                show ayame zorder 2 at t21
                mc "T-That's not what I intended."
                mc "Of course I still accept Yuri."
                mc "I accept her fully."
                mc "I just meant that--"
                show yuri 2pv zorder 3 at f22
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
                show ayame 1f zorder 3 at f21
                ay "You aren't gonna say anything?"
                ay "Really?"
                ay 1a "Look at her, [player]."
                show ayame zorder 2 at t21
                show yuri 3po zorder 3 at f22
                y "A-Ayame, you don't need to--"
                show ayame 2a zorder 3 at f21
                show yuri zorder 2 at t22
                ay "She did something so special for you."
                ay "She gave you a gift, as a way of displaying her affection for you."
                ay 2f "You aren't even going to respond to that?"
                ay "Do you even accept Yuri for who she is...?"
                show ayame zorder 2 at t21
                show yuri 3pn zorder 3 at f22
                y "A-Ayame, please..."
                y "You don't need to say those kind of things..."
                show yuri zorder 2 at t22
                mc "Of course, I accept Yuri."
                mc "I accept her with all I have."
                mc "I'm just...speechless at all of this."
                mc "I don't know if what I'll say is going to make things better or worse."
                show ayame 2g zorder 3 at f21
                ay "You should still say something."
                ay "Staying silent isn't going to solve problems."
                ay "Sometimes it can even make them worse."
                ay "But...I suppose I can understand your reasoning."
                show ayame zorder 2 at t21
                mc "I'm sorry, Yuri."
                mc "I really should have said something."
                show yuri 2pv zorder 3 at f22
                y "I-It's fine..."
                y "What isn't is that I've blocked access to the lockers."
        y "I've accidentally scared everyone away..."
        "Yuri sighs."
        y "I didn't mean to worry anyone..."
        y 3po "Uuu...this is all my fault."
        show yuri 3pn
        "Yuri turns towards Ayame."
        y "After you tell them it was me, I'm never going to be a school leader."
        y 3pv "I just woke up a subconscious desire and already it's falling to pieces..."
        show yuri zorder 2 at s22
        "Yuri gets on the ground and covers her face."
        "Ayame looks at me and I just shrug at her."
        "She sighs and gets down to the ground next to Yuri."
        show ayame zorder 2 at s21
        show ayame 1h zorder 3 at f21
        ay "You know..."
        ay "Being a leader really isn't that great."
        ay "Sure you're recognized but being perfect isn't fun at all."
        ay 1j "And even if you are perfect, people will still judge you."
        ay "It's just human nature."
        ay "In fact, because you're a leader, {i}everyone{/i} will judge you."
        ay 1g "You make one misstep and everyone is going to remember it."
        "Ayame signals for me to join the two of them."
        "I sit on the other side of Yuri."
        ay 1a "I used to think I wanted this too."
        ay "To be recognized."
        ay "To be a role model."
        ay "To not be judged."
        ay 1b "But reality struck pretty hard."
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
        show yuri 3pu zorder 3 at f22
        y "I suppose..."
        y "...you're right."
        y 3pt "Though there's still a problem..."
        show ayame 2h zorder 3 at f21
        show yuri zorder 2 at s22
        ay "I'll tell you what."
        ay "I won't pin the blame on you."
        ay "I'll just neglect to mention what you've told me now."
        ay 2d "After all, it was just an accident."
        show ayame zorder 2 at s21
        show yuri 3po zorder 3 at f22
        y "But why?"
        y "It's your responsibility to..."
        show ayame 2b zorder 3 at f21
        show yuri zorder 2 at s22
        ay "Yuri, when I look at you."
        ay "I see myself."
        ay "I used to be just like you."
        ay "A shy, outspoken girl."
        ay 2g "If something like this happened to me, I don't know what I would have done."
        ay "I probably would have imploded of the embarrassment."
        ay 2h "In fact, if I placed myself into your shoes..."
        "Ayame's voice suddenly trails off."
        show ayame 2m zorder 2 at t21
        "She just sits there, not moving or saying a word."
        show yuri 3pv
        "Yuri looks up and sees Ayame completely frozen as well."
        mc "Ayame?"
        "I wave my hand in front of her but she doesn't react at all."
        mc "Hello?"
        "I reach out to grab her shoulder."
        "Before I can make contact, she suddenly springs to life and shoves my arm away."
        show ayame 1c zorder 3 at hf21
        ay "What?"
        ay "What are you doing?"
        show ayame zorder 2 at t21
        "Ayame steps back."
        mc "What?"
        show ayame zorder 2 at t21
        show yuri 2pt zorder 3 at f22
        y "..."
        y "Are you okay?"
        show ayame 1j zorder 3 at f21
        show yuri zorder 2 at t22
        ay "Umm...yeah!"
        ay "Perfectly fine."
        ay 1d "I am okay-dokay."
        show ayame zorder 2 at t21
        "Okay-dokay...?"
        mc "Are you sure?"
        mc "You kinda froze there for a moment."
        mc "You wouldn't react to anything."
        mc "Right after you were talking about footwear."
        show ayame 1j zorder 3 at f21
        ay "I'm fine!"
        ay "I was just daydreaming."
        ay 1m "And I guess I got lost in my thoughts."
        ay "It felt pretty lucid so I guess I was just so absorbed in it."
        ay 1h "And anyway, we're not here to talk about me."
        ay "We're here for Yuri."
        show ayame zorder 2 at t21
        "She's right."
        "Besides, daydreaming isn't anything to be worried about."
        "Yuri is far more important."
        show ayame 2j zorder 3 at f21
        ay "Where was I?"
        ay 2d "Right, footwear."
        ay 2m "Yuri, if I was in your shoes then I would probably be feeling the same."
        show ayame zorder 2 at t21
        show yuri 2pv
        "Yuri looks down at the ground."
        "I don't think what Ayame is saying is reassuring her."
        mc "I don't think that's helping."
        show ayame 2h zorder 3 at f21
        ay "Let me finish."
        ay "Unlike if I was in your shoes, I have people there for me."
        ay 2b "You have [player] right here."
        ay "Whenever you're feeling down, you should rely on [player_reflexive]."
        ay "After all, that's what [player_personal]'s there for."
        show ayame zorder 2 at t21
        "I should be saying what she's saying."
        "Some [player_gender]friend I am..."
        mc "That's right."
        mc "Any problem you have, I'll help you get through it."
        mc "Yuri, this is nothing."
        mc "If you really wanted to be a leader, this obstacle isn't going to stop you."
        mc "You know that."
        mc "You're more resilient than that, aren't you?"
        "I offer my hand to Yuri."
        mc "So come on."
        mc "You aren't going to become a leader by sitting on the floor, are you?"
        "Yuri looks up at me."
        "She turns towards Ayame who nods her head, then grabs my hand."
        show yuri 2pk zorder 3 at f22
        y "Y-You're right."
        y 2pr "I have to do better than this."
        y "I'm not going to let something like this drag me down."
        show ayame 2e zorder 3 at f21
        show yuri zorder 2 at t22
        ay "That's the spirit!"
        ay 1b "All you have to do now is persevere."
        "Ayame puts a hand on Yuri's shoulder."
        ay "I'll come up with an excuse."
        ay 1h "Don't you worry, Yuri."
        ay "No one is going to know."
        show ayame zorder 2 at t21
        show yuri 3pr zorder 3 at f22
        y "No."
        show yuri zorder 2 at t22
        "Yuri takes Ayame's hand from her shoulder."
        show ayame 2m zorder 3 at f21
        ay "No?"
        show ayame zorder 2 at t21
        show yuri 3pt zorder 3 at f22
        y "If I'm going to become a leader, then I need to take responsibility."
        y "I want you to tell them the truth."
        y 3ps "Whatever the consequences, I'm prepared to accept them."
        show ayame 2i zorder 3 at f21
        show yuri zorder 2 at t22
        ay "Wow, this is such a sudden change."
        ay 1n "Are you sure about this?"
        ay "You don't have to act irrational, you know."
        show ayame zorder 2 at t21
        show yuri 1i zorder 3 at f22
        y "I'm sure."
        y "I wouldn't want you to get in trouble if they find out."
        y 1q "It's better this way."
        show yuri zorder 2 at t22
        "Ayame chuckles."
        show ayame 2e zorder 3 at f21
        ay "Yuri, I don't think you're aware of what would happen if I did get in trouble."
        ay 2k "Let's just say it wouldn't be good for the school."
        ay "Anyway, if that's what you want, I'm not going to go against your wishes."
        ay "I know when you become determined like this, it's hard to dissuade you."
        ay 2h "I'll let them know you brought a gift and things went wrong."
        show ayame zorder 2 at t21
        show yuri 1m zorder 3 at f22
        y "Thank you, Ayame."
        show ayame 1j zorder 3 at f21
        show yuri zorder 2 at t22
        ay "Well, I must be off."
        ay "I gotta report the cause of that screeching after all."
        ay 1g "It's a shame we couldn't talk longer."
        ay 1b "But we'll see each other soon enough, won't we?"
        "Ayame begins walking away but stops as she passes me."
        ay 1a "You know, I was going to say something to you, [player]."
        ay "But it seems it's not needed anymore."
        ay "I'm slowly beginning to understand."
        show ayame zorder 2 at t21
        mc "Not needed anymore?"
        mc "Why not?"
        show ayame at thide
        hide ayame
        show yuri zorder 2 at t11
        "She must not have heard what I said because she didn't respond at all to what I said."
        "It's not like it was really important anyway."
        y 2pe "What do you think she meant by it wouldn't be good for the school?"
        y "Do school leaders really have that much influence on the school...?"
        mc "I don't think that's it."
        mc "They really only have an influence on the students."
        mc "Judging by what she was saying before, it didn't sound like she really had that either."
        y 2ph "Hmm..."
        y "Do you think maybe her family is influential?"
        mc "What do you mean?"
        y 3pf "Someone like her became a school leader."
        y "But she was like me before."
        y "Without a charismatic personality, it's hard to become recognized as a leader."
        "Charisma isn't really the only thing you need to be a leader."
        "Popularity is usually a factor too, especially if it's an elected position."
        "But I guess if you have the charisma, you'd be popular as well."
        "Though I don't really know how the school leadership system works."
        "I never bothered to get into it."
        mc "Isn't what she just did pretty charismatic?"
        mc "She lifted up your spirits, like a charismatic person would."
        y 3ph "To be honest..."
        y "Her words didn't nearly have as much effect as yours."
        "But I just basically repeated what she said..."
        "I should defend Ayame here."
        "She isn't that bad...is she?"
        mc "She at least made me say something."
        mc "And anyway, isn't it possible she changed over that period of time she was like you?"
        mc "With how fast you did just then, I wouldn't be surprised."
        mc "After all, the two of you are rather similar."
        y 2pq "I-I doubt I've actually changed just now."
        y "I'm still incredibly nervous."
        y 2po "It took all I had to say that to Ayame."
        y "Even now, I'm not sure if it was the right thing to do."
        y "I can't help but feel I should regret it."
        y 2pv "She was just trying to be a friend, after all."
        mc "Do you think change like that is impossible then?"
        y 2pf "I'm not saying she couldn't have changed."
        y 2pg "It's just that change like that is gradual."
        y 1s "Think of a hero in one of those stories."
        y "They could be perfect at first but as things happen to their life, they gradually start to become deluded with the world..."
        y 1t "Circumstances might change, and they might inadvertently turn evil through a long period of time."
        y "Or at the very least, more vigilante than hero."
        mc "What are you trying to say?"
        mc "That Ayame is evil?"
        y 1q "Not at all!"
        y "Maybe over time she did actually become a person suited for the leadership role."
        y "Anything is possible, after all."
        mc "It just kinda sounds like you think she doesn't deserve to be a leader."
        y 1v "D-Don't misunderstand."
        y "I don't think she's a bad person or anything."
        y 1s "I actually think we'll become really good friends over time."
        y 2pk "I just think she's not taking her responsibility seriously."
        mc "And because of that, you think there might be a different reason she became a leader."
        y 2ph "Precisely."
        mc "And that reason is that her parents are rich?"
        y 3pg "Well, if you want to put it bluntly, yes."
        y "From what we know, Ayame doesn't really have leadership traits."
        y "She might be a fantastic person, good to be around and easy to make friends with."
        y 3pf "But that doesn't really translate to good leadership skills."
        mc "I don't think she's a bad leader."
        mc "But then again, I haven't really been involved with school activities that much."
        mc "I haven't really seen her in action until this morning."
        y "Wouldn't it be the leader's responsibility to make sure the student body knows about those kind of things?"
        mc "I suppose..."
        y 3po "Ah."
        y "Sorry, I didn't mean to talk down about her."
        y 3ph "I'm just curious as to how she became a leader."
        y 3pa "Because if she can do it legitimately, then I can as well."
        mc "I think you're thinking about this a little too much."
        mc "Maybe people just genuinely liked her and the staff recognized that."
        y "Maybe..."
        y 3pb "But it's good to have a little superstition."
        y "So pardon my speculations."
        mc "If you say so."
        mc "Maybe we should stop worrying about Ayame."
        mc "You can talk to her more during rehearsals anyway."
        mc "Then you can get your answer."
        mc "There are better things to talk about right now than if someone deserves something or not."
        y 2pq "I suppose."
        y "What did you want to speak about?"
        mc "How about us?"
        mc "How did you want to spend our time after the play?"
        mc "We can always leave afterwards and have dinner together."
        y 2pt "Is that the right thing to do?"
        y "What if some people join our club and we aren't there to welcome them?"
        y "It might leave a bad image."
        mc "I'm sure Sayori is more than capable."
        mc "Besides, she has Monika."
        mc "The two of them together are unstoppable."
        mc "Having the president and vice president is more than enough."
        y 2pv "Right...Monika."
        mc "What's wrong?"
        y "N-Nothing."
        mc "Do you have a problem with Monika?"
        if ch13_name == "Yuri":
            mc "Tell me."
            mc "I'm here for you."
            mc "Whatever is on your mind."
            y 2po "It's just...last time..."
            y "This conversation didn't go very well."
            mc "What conversation?"
            y 2pn "We were talking about Monika."
            mc "How long ago?"
            y "Three days ago, the day after we did the play on that manga."
            mc "I don't really remember that."
            mc "Was it an important conversation?"
            y 1v "I can't say."
            y "You didn't want to speak about her."
            y "The clear behavioral differences with her."
            y 1w "You insisted."
            y "I was afraid I had lost you..."
            mc "Lost me...?"
            y "So I don't really want to bring it up."
            y 2ps "It's better this way."
            mc "I'm not really sure what you're talking about."
            mc "I don't remember this happening at all."
            y 2pv "{i}(Maybe your memories were altered...){/i}"
            y 2pq "Never mind, okay?"
            y "I shouldn't have brought it up."
            "I sigh."
            "I want to help her but she's being really secretive about it."
            "Just what is she talking about...?"
            mc "If you want to talk about it at anytime, I'm here."
            mc "You aren't losing me, Yuri."
            mc "And you aren't going to lose me."
            mc "That's a promise."
            show yuri 2ps
            "Yuri lets out a weak smile."
            y "Okay...maybe later then."
            y "Anyway, let's get back to our plans."
        else:
            y 2pq "Please, let's just continue along with our plans."
            mc "Okay..."
            "I get the feeling she's hiding something from me."
            "Maybe I'll ask her later, after all of this is over."
        y 3pk "If you're sure that Monika and Sayori can handle it..."
        y "...then I suppose we can go somewhere."
        y 3pq "I don't really know many dinner places."
        y "I haven't really been asked to go to one before..."
        mc "Well, we don't have to go out to a dinner."
        mc "We can always see a movie."
        y 3pb "You know I'm fine doing {i}anything{/i} with you, [player]."
        y "All I really need is your company."
        y 3pe "That said..."
        y "I was kind of hoping to see some of the other clubs."
        y "They've probably been preparing just as hard as us for this."
        y 2pf "It would be a shame if no one got to see what they had."
        mc "That's...not a bad idea."
        mc "It could be pretty interesting to see what they've done to appeal to everyone."
        mc "And if we're doing that, I have something we can do after."
        y 2pa "What would that be?"
        mc "I'll leave that as a surprise."
        y 2pe "A surprise?"
        y 2pb "I hope it's nothing dangerous."
        y "It might be dark by the time we're finished here."
        "I'm counting on it."
        mc "You'll see."
        mc "Did you have any club in particular you wanted to see?"
        mc "It might be a good idea to know where they are so we don't get lost."
        y 1f "When I was speaking to Ayame before, I heard her mention a club."
        y "She said she was conflicted about whether she should join that club or our one."
        mc "What club was it?"
        y 1q "It's like some sort of reincarnation club."
        y "Honestly, I don't think it's a real club."
        y 1u "She kind of sounded like she was joking when she mentioned it."
        mc "Are they even doing something for today?"
        y 1e "I don't know."
        y "I suppose it's possible but I don't know what exactly they could showcase if they do exist."
        mc "Did Ayame say what it was about?"
        y 1h "I wanted to get her to join our club so I feigned interest and she told me."
        y "Apparently, they believe in reincarnation and the club is about trying to get your memories from your past life."
        y 1r "It sounds...unbelievable, in my opinion."
        mc "Who knows?"
        mc "Maybe they really believe in that sort of stuff."
        y 2po "Possibly..."
        y "It's just...not really for me."
        y 2ph "I prefer the rational, and if I must read fiction I'd prefer for it to be horrifically supernatural."
        mc "I'm curious as to why Ayame would consider joining it."
        mc "Do you think maybe she thinks she's reincarnated?"
        y 3pe "I don't know."
        y 3pa "I can't peer into her mind."
        y "Perhaps she just wanted to be friendly, since she's a school leader."
        y "It's not our job to judge what club she thought about joining."
        y 3pk "In the end, she did end up choosing the Literature Club over everything else."
        mc "Yeah..."
        if not persistent.ch16_ny_reload:
            y 3pl "By the way, {i}animam{/i}.{nw}"
        else:
            y 3pl "By the way, {i}requiem{/i}.{nw}"
        $ _history_list.pop()
        y "By the way, {fast}it might be good to--"
        mc "What?"
        y 3pq "E-Eh?"
        mc "What did you just say?"
        y "I was in the middle of a sentence when you interrupted me..."
        y "So...nothing?"
        mc "That's weird."
        "I could have sworn she said something else just then."
        y 3pe "Is everything okay?"
        mc "Yeah...just go on with what you were saying."
        y 3pa "I was going to say it might be good to take advantage of the free food some clubs are giving out."
        y "For after the play, I mean."
        mc "That does sound like a good idea."
        show yuri 3pc
        "Yuri beams."
        y "I thought you'd be interested in the free food."
        mc "Well, if they're bringing their best and it's free..."
        mc "...who am I to say no?"
        "Yuri and I make a bit more small-talk and talk about the play for a few moments."
        "Soon enough, the siren signaling the end of lunch rings."
        y 3pa "I guess that's it."
        y "Do you have a fun class next?"
        mc "Not exactly."
        mc "I have a free period so I was just going to hang around."
        mc "Maybe look at the script a little so I can get some of the lines I don't quite remember."
        y 2pe "Where are you going to do that?"
        mc "Maybe in one of those supervised classrooms or in the library."
        y "I wouldn't recommend the library."
        y 2pf "I went there recently and it was quite busy due to Inauguration Day."
        mc "There's people setting up in there?"
        y "Yeah, it might be difficult for you to rehearse with all that noise."
        mc "I'll keep that in mind."
        mc "Thanks, Yuri."
        y 2pb "Of course."
        y "I'll see you during rehearsals."
        mc "See you then."
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
        show natsuki 2c zorder 2 at t11
        n "There you are."
        mc "Hey, Natsuki."
        n 2d "Come on, let's go."
        n "I have a couple of things we can do."
        mc "What did you have in mind?"
        label ch16_n_cancel:
        n 4b "We're at school so we're kinda limited."
        n "I did hear a rumor though."
        mc "What was it?"
        n "Because some of the clubs are going to be selling food for Inauguration Day, they've opened up the kitchen."
        n 4a "I was thinking of going there, maybe do some baking and just look at what everyone's making."
        mc "That's a great idea."
        n 3e "The problem is, I think it's restricted for clubs that got permission only."
        mc "Oh..."
        n 3j "But we don't care about that."
        n "Do we?"
        mc "Uhh..."
        n 3b "The plan is to sneak in there and pretend we're part of the cooking club."
        mc "I don't know."
        mc "It seems kinda dishonest."
        n 1e "Oh, come on."
        n "What's the worst that could happen?"
        n 1h "Besides, it might be the last time you could ever do something like this."
        n "And it's just for fun."
        n 1k "Who's really going to care that we're there?"
        mc "Alright."
        mc "But this is all based on a rumor, isn't it?"
        mc "Where did you even hear it from?"
        n 1c "I heard about it in class."
        n "Someone was talking about it and I overheard."
        n 1e "What's the big deal anyway?"
        n "If it isn't actually happening, then we can just do something else."
        mc "If that's what you want to do."
        mc "Then lead the way."
        n 2d "Right, follow me."
        scene bg school_hallway
        show natsuki 1j zorder 2 at t11
        with wipeleft_scene
        "Natsuki and I make our way towards the kitchen area of school."
        "It's the same area where the food and hospitality subjects are done."
        "There's quite a bit of activity around the area."
        "But there doesn't seem to be anyone in the actual kitchens."
        "Everyone is just gathered outside."
        n 1c "I wonder what's the deal here."
        mc "There doesn't seem to be anyone actually cooking."
        "Natsuki approaches one of the students waiting outside the rooms."
        n 2c "Excuse me."
        "She doesn't seem to be able to get their attention."
        n 2f "Um...hello?"
        n "I'm talking to you!"
        "She taps the student on the shoulder and that gets their attention."
        n 2g "Why isn't anybody in the kitchens?"
        n "I thought we were allowed to cook at lunch."
        "Student" "\"Are you one of the clubs allowed in there?\""
        n 2h "Yeah, we're part of the...cooking club."
        "Student" "\"Oh, I didn't think they were participating.\""
        n 1s "Y-Yeah...it was kind of last minute."
        "Student" "\"Anyway, one of the members of the student council kicked us out.\""
        "Student" "\"Something to do with safety or something.\""
        "Student" "\"Some of us are trying to talk to her now.\""
        n 1k "Where is she?"
        "Student" "\"I don't think you'll have any luck.\""
        "Student" "\"She's pretty stubborn about it.\""
        "Student" "\"Which sucks because we needed to cook something up for our club.\""
        n 1g "Just tell me where she is."
        n "I have a way with people."
        "The student looks at her then notices me."
        "I just shrug."
        "Student" "\"She's over there by the door.\""
        "The student points to a door surrounded by a crowd of students."
        "Student" "\"I'm telling you though, there's no point.\""
        n 1c "We'll see."
        n 1a "Thanks."
        "Natsuki turns back towards me."
        mc "So what are you gonna do?"
        n 2b "I'm gonna give her a piece of my mind."
        n "She can't just do this to us."
        "We weren't supposed to be here in the first place..."
        n 2e "Come on, let's go."
        n "I might need backup."
        mc "Backup for what...?"
        "Natsuki ignores my question and approaches the crowd of students."
        "She basically shoves people out of her way until she reaches the person blocking the door."
        n "Excuse me, what gives you the right to--"
        show natsuki 1o zorder 2 at t21
        show ayame 2i zorder 3 at f22
        ay "Natsuki?"
        "The person blocking the door is none other than Ayame."
        "I guess she's finished with her business from this morning."
        ay "What are you doing here?"
        "The way she asked that question sounded like she already knew the answer."
        ay 2a "I don't recall the Literature Club being part of this."
        show natsuki 1q zorder 3 at f21
        show ayame zorder 2 at t22
        n "A-Ayame..."
        n "We..."
        n 1r "{i}(She's a school leader...?!){/i}"
        show natsuki zorder 2 at t21
        "Natsuki looks at me for help."
        "I guess I gotta say something."
        mc "We're here to protest against this injustice!"
        mc "You can't just deny all these people, who have been planning so hard, the chance to cook for their clubs!"
        mc "Imagine how damaging it could be to their reputation and on a day like this!"
        show natsuki 1m zorder 3 at f21
        n "What...?"
        show natsuki zorder 2 at t21
        "I may have taken my acting a bit too far."
        "But I'm going to be doing more embarrassing things for the play."
        "So I might as well get used to it."
        show ayame 2g zorder 3 at f22
        ay "Look, [player]."
        ay "It's not my decision."
        ay "I'm just here to tell everyone that we can't use the kitchens."
        show natsuki 1i zorder 3 at f21
        show ayame zorder 2 at t22
        n "Who's decision was it then?"
        show natsuki zorder 2 at t21
        show ayame 1g zorder 3 at f22
        ay "It was the principal's."
        ay "So that means there's nothing I can do about it."
        ay "It was a last minute decision, even though it was promised that you'd get access if you applied."
        "Ayame whispers so that only Natsuki and I can hear her."
        ay 1a "I don't know the reason myself."
        ay "I'm just guessing it's for safety but in reality...well..."
        "She raises her voice again so the whole crowd can hear."
        ay 2g "I'm really sorry, everyone!"
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
                show ayame 2a zorder 3 at f22
                ay "[player]..."
                show ayame zorder 2 at t22
                mc "She's just doing what she's told."
                mc "It isn't up to her whether you're allowed in or not."
                mc "If you want to blame anyone, blame the principal."
                show natsuki 4e zorder 3 at f21
                n "[cPlayer_personal]'s right."
                n "We can't blame Ayame for this."
                n "I know it sucks but you can't seriously think it's her fault."
                n 4g "Imagine you were put in the same position."
                n "It'd feel terrible, wouldn't it?"
                n 4i "So you can't seriously hate someone for doing their job, can you?"
                show natsuki zorder 2 at t21
                "The crowd subsides a bit."
                "They're still angry but at the very least they're not directing it at Ayame."
                "Ayame breathes a sigh of relief."
                show ayame 2b zorder 3 at f22
                ay "Thanks, guys."
                ay "It really sucks having to do the principal's dirty work."
                show natsuki 4a zorder 3 at f21
                show ayame zorder 2 at t22
                n "We've got your back, Ayame."
                n 4b "After all, you're part of our club now."
                n "We have to look out for each other."
                show natsuki zorder 2 at t21
                show ayame 2g zorder 3 at f22
                ay "That...means a lot."
                ay 2h "Thanks, you two."
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
                show ayame 2a zorder 3 at f22
                ay "You know I can't do that."
                show ayame zorder 2 at t22
                mc "You're just a--"
                show natsuki 4o zorder 3 at hf21
                n "[player]!"
                n "What the hell is wrong with you?"
                show natsuki zorder 2 at t21
                mc "I'm trying to get us inside."
                mc "That's what you wanted, right?"
                show natsuki 4q zorder 3 at f21
                n "But can't you see it's not her fault?"
                n "If you want to blame anyone, blame the principal."
                "Natsuki turns to the crowd."
                n 4e "Are you listening to me?"
                n "Ayame isn't to blame."
                n "She's just doing what the principal told her to."
                n 4g "Who knows what could happen to her if she disobeyed?"
                show natsuki zorder 2 at t21
                "The crowd subsides a bit."
                "They're still angry but at the very least they're not directing it at Ayame."
                "Ayame breathes a sigh of relief."
                show ayame 2g zorder 3 at f22
                ay "Thanks, Natsuki."
                ay "The crowd was really getting to me..."
                ay "I guess that's what they call peer pressure."
                show natsuki 2c zorder 3 at f21
                show ayame zorder 2 at t22
                n "I've got your back, Ayame."
                n "I thought [player] would too..."
                n "I guess [player_personal] just misunderstood."
                show natsuki zorder 2 at t21
                mc "I'm sorry."
                show ayame 1h zorder 3 at f22
                ay "What's said is said."
            "Say nothing.":
                $ ch16_ay_level += 1
                "Natsuki nudges me."
                show natsuki 2g zorder 3 at f21
                n "Aren't you going to say something?"
                show natsuki zorder 2 at t21
                mc "What am I supposed to say?"
                show natsuki 4f zorder 3 at f21
                n "I can't believe you sometimes."
                "Natsuki turns towards the crowd."
                n 4b "Listen up everyone!"
                n "It's not Ayame's fault."
                n "She isn't the one responsible for keeping you locked out."
                n "What she is doing is what she was told to do."
                n 4e "By the {i}principal{/i}!"
                n "So if you want anyone to blame, blame the principal!"
                n "Not her!"
                show natsuki zorder 2 at t21
                show ayame 1g zorder 3 at f22
                ay "Natsuki..."
                show natsuki 4b zorder 3 at f21
                show ayame zorder 2 at t22
                n "I mean, come on."
                n "You can't seriously hate someone for doing their job."
                n "What if you were in her position?"
                n 4g "Just think about it before you start calling her names again."
                show natsuki zorder 2 at t21
                "The crowd subsides a bit."
                "They're still angry but at the very least they're not directing it at Ayame."
                "Ayame breathes a sigh of relief."
                show ayame 1b zorder 3 at f22
                ay "Thanks, Natsuki."
                ay "The crowd was really getting to me..."
                ay "I guess that's what they call peer pressure."
                show natsuki 2a zorder 3 at f21
                show ayame zorder 2 at t22
                n "I've got your back, Ayame."
                n 2q "I thought [player] would too..."
                n "But at least [player_personal] join the rest of the crowd."
                show natsuki zorder 2 at t21
                mc "I'm sorry."
                mc "I should have said something."
                show ayame 1h zorder 3 at f22
                ay "It's fine."
        ay "But I still can't give you guys access."
        ay 1g "Like I said, I'm not allowed."
        ay "I have to uphold the values of the school, after all."
        "Ayame rolls her eyes."
        ay 1b "But..."
        show natsuki 2c zorder 3 at f21
        n "But?"
        show natsuki zorder 2 at t21
        show ayame 2b zorder 3 at f22
        ay "If an incident were to occur that required my attention."
        ay "Then I might not be here to stop people getting in."
        ay "And I might just 'accidentally' drop the keys to the kitchen, you know?"
        ay 2g "But as it stands, I can't do anything."
        show natsuki 2g zorder 3 at f21
        n "Then we have to do the right thing by everyone."
        "Natsuki steps back from the crowd surrounding Ayame and I follow after her."
        n 2c "[player], are you thinking what I'm thinking?"
        show natsuki zorder 2 at t21
        mc "No?"
        mc "What are you--"
        "Suddenly, Natsuki punches me in the face."
        "She put a lot more force into that than I would have expected."
        "I think I could feel my teeth loosen a little."
        mc "What the hell was that for?"
        show natsuki 1o zorder 3 at f21
        n "Help!"
        n "Someone is injured!"
        n 1p "We need help!"
        show natsuki zorder 2 at t21
        "Ayame definitely saw what happened."
        "She lets out a faint smile before approaching the two of us."
        show ayame 1i zorder 3 at f22
        ay "Oh no! That looks serious."
        ay "What happened here?"
        show natsuki 1h zorder 3 at f21
        show ayame zorder 2 at t22
        n "Quick, we have to take [player_reflexive] to the nurse's office."
        n "You can help with that, right, school rep?"
        show natsuki zorder 2 at t21
        show ayame 2j zorder 3 at f22
        ay "Of course."
        "Ayame looks at the crowd."
        ay 2b "Please do not use these keys to get in."
        "She shows everyone the keys and drops them to the floor."
        ay "When I get back here, you all better not be in the kitchen."
        "She turns back towards us."
        ay 2d "Let's go."
        show ayame zorder 2 at t22
        mc "I'm so confused..."
        "I grab my jaw."
        mc "Why did you do that?"
        show natsuki 1b zorder 3 at f21
        n "We'll talk later."
        n "Right now, we gotta get you to the nurse."
        show natsuki zorder 2 at t21
        "We begin to walk away."
        "One of the people in the crowd picks up the keys."
        "As we turn the corner, I could hear the door to the kitchens opening."
        "I guess they're inside."
        scene bg school_nurse
        show natsuki 1d zorder 2 at t21
        show ayame 1d zorder 2 at t22
        with wipeleft_scene
        "The nurse didn't really do anything to my face."
        "She said it would just heal and I was just making a big deal out of it."
        "She let me stay on the bed but only until the end of lunch."
        "She left us here and told us not to cause anymore trouble."
        show ayame zorder 3 at f22
        ay "I didn't expect that."
        ay 2e "That was a genius plan, Natsuki."
        show natsuki 2y zorder 3 at f21
        show ayame zorder 2 at t22
        n "What are you talking about?"
        n "I just really wanted to hit [player] in the face."
        show natsuki zorder 2 at t21
        mc "Can someone please explain to me what's going on?"
        mc "All I can figure out is Natsuki punched me in the face..."
        mc "...out of seemingly nowhere!"
        show ayame 1j zorder 3 at f22
        ay "Put the pieces together."
        ay "Students wanted to enter the room, right?"
        ay "But I couldn't let them as long as I was there."
        show ayame zorder 2 at t22
        mc "So Natsuki punched me?"
        show natsuki 2h zorder 3 at f21
        n "So we could give Ayame an excuse to leave."
        n "That's also why she put the keys on the floor."
        n 2q "Sorry I punched you, but it was to help everyone."
        n "And it was the only thing that came to mind...at the time."
        show natsuki zorder 2 at t21
        mc "Okay...but did you have to do it so hard?"
        mc "It still kinda hurts a little."
        show natsuki 1e zorder 3 at f21
        n "Oh, toughen up."
        n "It'll be fine."
        n 1b "It's not like you got a concussion or anything."
        show ayame 1b zorder 3 at f21
        show natsuki zorder 2 at t22
        ay "I really want to thank you both."
        ay "I don't know how much longer I could have lasted out there."
        ay 1n "Everyone was starting to look like they were about to snap."
        show ayame zorder 2 at t21
        show natsuki 4d zorder 3 at f22
        n "If you need help like that again, you can count on us."
        n "We won't let you down."
        show ayame 2h zorder 3 at f21
        show natsuki zorder 2 at t22
        ay "T-Thank you, Natsuki."
        show ayame zorder 2 at t21
        show natsuki 4c zorder 3 at f22
        n "There's just one thing."
        n "Why didn't you tell us?"
        show natsuki 3c
        "Natsuki points at Ayame's ribbon."
        n "Why keep it all a secret?"
        show ayame 2m zorder 3 at f21
        show natsuki zorder 2 at t22
        ay "This?"
        "Ayame puts the ribbon between her fingers."
        ay "Whenever I have this on, I don't feel like 'me'."
        ay 2n "I feel like I'm a different person."
        ay "People treat me differently."
        ay "I didn't want that with you guys."
        ay 2g "I wanted you all to be who you were around me rather than changing who you are around me."
        ay "That's why I didn't tell you."
        ay "I'm sorry I deceived you."
        show ayame zorder 2 at t21
        show natsuki 3b zorder 3 at f22
        n "It's no problem at all."
        n "I can understand why you did it."
        n "And I don't care whether you're a leader or whatever."
        n 3a "It's just going to be kinda cool having someone like you in the club."
        show ayame 2i zorder 3 at f21
        show natsuki zorder 2 at t22
        ay "I'm surprised you only now just figured it out."
        ay "[player] saw for [player_reflexive]self what I really was this morning."
        ay 2h "I would have thought [player_personal]'d spread the word."
        ay 2b "{i}(Not to mention...I've been a leader this entire time.){/i}"
        show ayame zorder 2 at t21
        mc "Why would I?"
        mc "It's not like you being a leader would have changed anything."
        mc "We would have still treated you just like anyone else."
        show natsuki 1e zorder 3 at f22
        n "[cPlayer_personal]'s right!"
        n "So what if you're a leader?"
        n 1l "You aren't getting any special treatment from us!"
        show ayame 1d zorder 3 at f21
        show natsuki zorder 2 at t22
        ay "Ahaha...that's good to know."
        ay "Thanks, you guys."
        ay "I wouldn't have it any other way."
        ay 1e "I knew joining this club couldn't have been a mistake."
        "Ayame stands up and approaches the door."
        ay 1b "Well..."
        ay "I should go back, shouldn't I?"
        ay 1h "I wouldn't want to have failed my duty."
        ay "But I think I left my keys somewhere..."
        show ayame zorder 2 at t21
        show natsuki 1d
        "Natsuki smiles."
        show natsuki zorder 3 at f22
        n "You know, that sounds pretty bad."
        n 2d "You should try walking slowly to find them on the way back."
        n "Maybe you'll find them that way."
        show ayame 1j zorder 3 at f21
        show natsuki zorder 2 at t22
        ay "That sounds like a good idea."
        ay "I might just do that."
        ay "Goodbye, you two."
        ay "I know you two wanted to spend some quality time together."
        ay 1j "So I'll let you have it."
        ay "After all, I'll see all of you later today."
        ay 1k "With gifts."
        show ayame at lhide
        hide ayame
        show natsuki zorder 2 at t11
        "Ayame winks as she closes the door behind her."
        n 1c "You knew, huh?"
        mc "I only found out this morning."
        mc "Are you upset?"
        n 1b "That you didn't tell me?"
        n "No way."
        n "That kind of thing doesn't bother me at all."
        n 2q "I'm just surprised I didn't know she was a school leader."
        n "I mean, how could we have not known that?"
        n "That's a pretty big deal, isn't it?"
        mc "I have no idea."
        mc "I'm not even sure who the other school leaders are."
        mc "I guess I never really bothered knowing who they were since it never affected me."
        mc "And I was never going to be a leader so..."
        n 2d "Well, now we know Ayame is one of them."
        n 2c "Not like that really changes anything."
        mc "What do we do now?"
        n "Is your face feeling any better?"
        mc "Are you going to punch me again?"
        n 2a "It's tempting."
        n "Your mouth seems to be working fine, so how about something to eat?"
        mc "What did you have in mind?"
        n 2d "I was thinking we could go back to the kitchens."
        n "It's almost the end of lunch."
        n "The clubs there would still be cooking, but maybe we can get some sort of compensation for helping them out."
        n "How does that sound?"
        mc "What if someone else is there to stop us from coming in?"
        n 2c "Ayame seemed like she was the one responsible for that area."
        n "I doubt any of the students would stop us."
        n "After all, they're not meant to be in there either."
        mc "I guess so."
        n 1e "Then what are we waiting for?"
        "As Natsuki opens the door, a painful aching feeling rushes through my head."
        "I grab my head and groan in pain."
        n 1h "What's wrong?!"
        "Natsuki immediately rushes to my side."
        mc "I don't know."
        mc "The pain just came out of nowhere."
        n 1m "Maybe I did punch you too hard..."
        n "Do you need some ice?"
        n 1q "There might be some around this place."
        mc "I don't think ice is going to do it."
        mc "Let me just sit here for a minute."
        "After a couple of moments, the pain begins to slowly fade."
        mc "I don't know what the hell that was."
        mc "But I really don't want to feel that again."
        n 1s "I'm so sorry."
        "Natsuki hugs me."
        n 1m "I didn't think it would hurt that bad."
        n "I won't do it again, I promise."
        mc "T-Thanks, that's good to know."
        mc "But I don't think it was you."
        mc "You punched me on my right cheek."
        mc "But the pain came from my forehead."
        mc "And it wasn't really the same thing..."
        n 1m "That's not good at all!"
        n 1o "Maybe you're bleeding internally or something...!"
        n "This is terrible."
        n "We need to find the nurse."
        mc "No, don't do that."
        mc "The pain is already going away."
        mc "This just feels really familiar."
        n 1h "Familiar...how?"
        mc "Remember that headache we had two days ago?"
        mc "It felt almost like that."
        n 2h "It did?"
        "Natsuki immediately gets up."
        n 2s "Now I'm kinda suspicious."
        mc "Of what?"
        n "You said it felt like that headache two days ago."
        n "I couldn't even remember the events leading up to that headache."
        n 2k "Can you still remember why we're here?"
        n "Or how we got here?"
        mc "Because you punched me in the face?"
        mc "And because Ayame needed an excuse not to be guarding the door."
        n 2q "Okay."
        mc "Why do you ask?"
        n 2s "Last time this happened, we forgot something."
        n "I'm trying to figure out what you just forgot."
        mc "I haven't forgotten anything."
        mc "I just had a headache for a second."
        n 4m "What kind of headache just appears for a couple of seconds?"
        n "These two things are definitely related somehow."
        n "We just gotta figure out what you lost."
        mc "Natsuki, I didn't lose anything."
        mc "I still remember what happened in the past couple of days perfectly fine."
        mc "I don't think anything has happened to me."
        n 1i "I don't know if that's true..."
        mc "Well, I know if we stay here we aren't going to be able to get any of the food for compensation."
        "Natsuki sighs."
        n 1m "Okay, if you're sure."
        n "I'm just worried, you know."
        mc "I'm fine, really."
        mc "I appreciate the concern but there's nothing to be worried about."
        n 1n "Fine, but you let me know as soon as you think something is wrong."
        n "I still need to find out what's really going on."
        mc "If it matters that much, then sure."
        mc "But I really think you're taking this way too seriously."
        scene bg school_hallway
        show natsuki 1g zorder 2 at t11
        with wipeleft_scene
        "Natsuki and I quickly make our way back to the kitchens."
        "It's only a few minutes until the end of lunch."
        "Ayame is nowhere in sight and the kitchens look lively."
        "Everyone inside looks like they're working hard to get their food ready."
        "One of them sees us and waves."
        "He signals to the people next to him and rushes outside, bringing a small platter of food."
        "As he exits the room, other people notice what him and recognize us too."
        "Student" "\"I saw what you did before.\""
        "Student" "\"I just want to say, you're a lifesaver.\""
        "Student" "\"I don't know what our president would have done if we didn't get these for our stall.\""
        "Student" "\"So here, have one.\""
        "He opens the platter to reveal what look to brownies."
        "Student" "\"Fresh from the oven, enjoy.\""
        n 1d "Don't mind if we do."
        "Natsuki and I both take one."
        "Student" "\"Anyway, we still have quite a bit to do in a short amount of time.\""
        "Student" "\"Thanks again!\""
        "The student goes back into the kitchen."
        "As he does, more people come out with more platters."
        "They all talk to us about how they're grateful for the help and offer us some food."
        "We take some and they quickly rush back to the kitchen."
        "They gave us quite a lot in total."
        "One of them noticed and offered two small plastic bags to carry it all."
        n 1a "You know, I could get used to this."
        mc "It's not everyday you're some kind of hero, Natsuki."
        mc "You really helped these guys out."
        mc "They were probably in a similar position to the first guy."
        mc "You know, with their club presidents on their backs."
        n 1c "Well, when you put it that way..."
        n 4y "I guess I am some kind of hero, aren't I?"
        n 4t "But it wasn't really a solo effort."
        n "You were there with me."
        mc "I didn't do anything."
        mc "You were the one who really calmed the crowd down."
        mc "If it weren't for you, they'd still be out there complaining to Ayame."
        n 4q "You don't understand."
        n "It's more than that."
        mc "Eh...?"
        n "You being around..."
        n 2r "It..."
        "Natsuki struggles to find the words."
        n 2s "Y-You know..."
        n 2m "I-It...helps."
        n 2s "S-So..."
        mc "I guess I {i}do{/i} have that effect on people."
        mc "You can thank me later."
        show natsuki 2e at h11
        n "What?!"
        "Natsuki's demeanor completely changes."
        n "What are you talking about, idiot?"
        n 2f "I'm trying to be thankful here and you say something stupid like that!"
        "Natsuki punches my arm."
        "It's a lot weaker than the one that hit my face."
        mc "Ow."
        n 1g "I'm just saying that you being around helped!"
        n "You're not the reason I did it or anything!"
        "And just like that, Natsuki is back to her usual self."
        mc "{i}(Sure I wasn't.){/i}"
        n 5e "Do you want another punch in the face?"
        n "That can easily be arranged."
        mc "No ma'am."
        mc "That won't be necessary."
        "I'm glad I know how to make Natsuki..."
        "Well, be Natsuki."
        "I think we have a silent mutual understanding of what just happened."
        "It just goes to show how far our relationship has gone..."
        n 5i "Good!"
        n 2e "Now, we should probably make use of this food."
        n "We wouldn't want to let it go to waste."
        mc "That's a good idea, lunch is almost over anyway."
        n 2a "I know just the place."
        "Natsuki offers me the plastic bag that she's carrying."
        n 1b "Take this."
        mc "But I'm already carrying this one."
        n 1e "Excuse me, but were you the hero of the kitchen?"
        mc "Well..."
        n 1d "No, I didn't think so."
        n "Come on."
        "I take the plastic bag and follow Natsuki."
        scene bg school_stairway
        show natsuki 1c zorder 2 at t11
        with wipeleft_scene
        "We arrive at the same place we went to yesterday."
        "I would have thought since it was approaching the end of lunch there would be some people around."
        "It's just as empty as it was before."
        "Natsuki leads us to the table and I set down the plastic bags."
        n "We don't have much time."
        n 3c "What should we try first?"
        mc "I don't know."
        mc "I'll just reach in and grab something and that's what I'll start with."
        "I put my arm inside one of the plastic bags."
        "I manage to pull out a carefully wrapped donut."
        mc "I got a donut."
        "Natsuki reaches into her bag and pulls out what looks like a lamington."
        n 1c "This looks good."
        n 1d "Not as good as something I would make though."
        mc "So we both got something sweet."
        n 3a "It only makes sense."
        n "It's not like there's a lot of savory food that's good at room temperature."
        mc "True."
        "I unwrap the donut and take a bite."
        "The frosting isn't as sweet as I thought it would be."
        "Despite that, it's got a distinct chocolate taste to it that matches really well the dough."
        mc "Not bad."
        mc "How's the lamington?"
        n 3b "I don't know."
        n "I haven't tried it yet because I was busy watching you eat."
        n "I-I mean because I was carefully examining the lamington."
        n 3e "You know, to see if it was made well."
        mc "Sure you were."
        mc "I do wonder how they managed to make these in the short amount of time we were gone."
        mc "Don't these things require a lot of time?"
        n 3c "I thought so too."
        "Natsuki takes a bite out of the lamington."
        n 1a "My guess is that the ones they gave us were prepared beforehand."
        n "There's just no way you can make a donut or a lamington that quickly."
        mc "This is still pretty warm."
        mc "In fact, it kinda tastes like it was freshly made."
        n 1g "Well, who cares anyway?"
        n "It's food, and it's free."
        n "We don't need to know how it was made, do we?"
        mc "I guess not."
        "I take another bite of the donut."
        "It definitely feels like it was made recently."
        "Maybe they used some kind of trick to keep it warm."
        n 1c "We should hurry up."
        n "We're not gonna finish this all at this rate."
        mc "Maybe we could bring some to the club."
        mc "The others could use some snacks during rehearsals, right?"
        n 1k "That's not a terrible idea."
        n 2h "And there is a lot of food here..."
        n 2i "Maybe even a little too much."
        "Eventually we both finish what we were eating."
        "She looks satisfied with the lamington and the donut I had was good too."
        "I stand up and reach for the plastic bags."
        n 2c "Wait."
        mc "How come?"
        n 2g "There's something you should know."
        n "It's not really important but I thought I should tell you."
        mc "Okay."
        "I sit back down and face Natsuki."
        mc "What is it?"
        if not persistent.ch16_ny_reload:
            n 1h "Lately, I've been {i}inveniet{/i}.{nw}"
        else:
            n 1h "Lately, I've been {i}amisit{/i}.{nw}"
        $ _history_list.pop()
        n "Lately, I've been{fast} thinking that--"
        mc "W-What?"
        n 1c "Huh?"
        mc "What did you just say?"
        n 2e "Well, I haven't even said anything yet!"
        n "You just interrupted me for no reason."
        mc "I could have {i}sworn{/i} you said something else."
        "Am I going crazy?"
        "She definitely said something."
        "But what was it...?"
        n 2h "Oh...I get it. [player]..."
        mc "Maybe I just imagined it."
        "Natsuki puts a hand on my shoulder."
        n 2i "If you really think something like that happened..."
        n "You need to explain what you think happened. Now."
        mc "You believe me?"
        n 2c "Of course I do."
        n "I trust you."
        n 2b "If you think something happened, then why wouldn't I believe you?"
        n 4g "You don't have a reason to lie to me, do you?"
        mc "No..."
        mc "I just thought I would tell you because..."
        mc "You seemed concerned about my memory at the nurse's office."
        mc "It's probably nothing."
        n "It could be."
        n "But it's good to be careful."
        n 4e "Especially on days like this."
        n 4c "What did it sound like I said?"
        mc "I...don't know."
        mc "It just happened and I wasn't really paying attention..."
        mc "But it sounded odd."
        n "Alright..."
        n "So what happened exactly?"
        mc "It sounded like you said one thing."
        mc "But then..."
        mc "It didn't happen?"
        n 4q "Didn't happen...?"
        mc "After you said it, it's like it never happened."
        mc "Then I interrupted your in the middle of your sentence."
        mc "I might just be going crazy."
        mc "But I swear that's what it felt like what happened."
        n 4h "So it's like that tiny event didn't happen?"
        mc "Yeah."
        n 2c "That sounds like you just misheard me or something."
        n "But I still believe you."
        n "This is hardly the weirdest thing that's happened."
        n 2q "But what can we really do?"
        n "It's not like we can just go back to that moment."
        mc "I guess not..."
        n "And maybe you heard something you needed to know."
        mc "What do you mean?"
        n "I mean it could be important that you heard it."
        n 2h "Even if you don't really remember it."
        n "Like someone is trying to tell you something...through me."
        mc "You think something supernatural is trying to tell me something?"
        n 1g "That's just my guess."
        n "From my perspective, what happened was you interrupted me."
        n "That's all."
        n 1c "There's no way you would act like this if you weren't concerned."
        mc "Thanks for believing me."
        n 1s "You don't need to thank me for that."
        n "With all the things we've seen and done, I'd be stupid not to."
        n 1q "We just have to figure out what exactly to do with that information."
        n "If you can't remember what I said, then we can't really do anything right now."
        mc "What were you going to say anyway?"
        mc "Before I interrupted you."
        n 1i "I...I don't know."
        n "I guess I forgot."
        n "It wasn't important anyway."
        mc "So what should we do?"
        n 1b "Well...right now?"
        "The siren rings through the hallway."
        "Strangely enough, no one is here still."
        "Is this area of the school just completely empty and devoid of life...?"
        n 1c "It's the end of lunch."
        n "So all we can do is take the food we have and keep it safe for the club."
        "Natsuki takes a plastic bag and I take the other one."
        n 1g "With what we know, we can't do much at all."
        n "Still, I'm going to try."
        mc "What are you going to do?"
        n 1h "Maybe I can find some way to realize what I said."
        n "Don't count on it."
        n 2b "I'm expecting you to try as well."
        mc "I'll do my best."
        n 2d "Don't forget to get ready for the play too."
        n "Rehearsals will be easier that way."
        n 1q "I wouldn't want to make a bad impression on Ayame."
        mc "That's true."
        mc "I have a free period right now, so it'll be a good time to look at it."
        mc "Maybe I'll go to the library or a classroom that's supervised."
        n 1a "As long as you can try to remember what I said and read the script."
        n "Anyway, we should get going."
        n 1d "I don't want to be late to class."
        mc "Lead the way."
        mc "You know your way around here better than I do."
        "I follow Natsuki out of the building."
        "I'm still left wondering what she said in that brief moment."
        "Was it even her...?"
        "It might not be important but it could be good to remember."
        "In the case that it was."
        "It might just be my imagination but like Natsuki said..."
        "With the things that have been happening, I wouldn't be surprised if it was real..."
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
        show sayori 1d zorder 3 at t11
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
        s 2h "Yesterday, I was stupid."
        s "I shouldn't have tried to do something out of order."
        s "I shouldn't have even thought about it."
        s 2l "I'm such a hopeless romantic."
        s "I'm looking for a happy ending that doesn't exist."
        s "So instead I made one for myself..."
        s "How stupid can I be, right?"
        mc "Don't say that about yourself, [player]."
        mc "You're the only one that could have gotten the club this far."
        mc "Give yourself some credit."
        mc "And there's no point looking down on yourself, especially now."
        mc "You'll need all the positivity you can get."
        s 2g "You really think so, [player]?"
        s "You think I can just create positivity out of thin air like that?"
        mc "I don't know what you're capable of."
        mc "At least, not the full extent of it."
        mc "But I hope there's at least some way I can cheer you up."
        s 2d "That's it then."
        s "I'll pay you back and cheer myself up at the same time."
        mc "What are you thinking?"
        if ch15_s_date_choice:
            s 4b "I need to concentrate."
            s "It didn't turn out very well last time."
        else:
            s 4a "I'm thinking..."
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
        m 1c "Oh."
        if monika_type == 0:
            m 2l "S-Someone was hurt."
            m "So I brought them some ice."
            mc "Very thoughtful of you."
        else:
            m 2l "I-It's nothing."
            m "Don't worry about it."
        "Monika rubs her hands on her blazer."
        "Probably to try to get rid of that cold touch."
        mc "Anyway, what did you need to tell me?"
        label ch16_m_interrupt:
        m 2a "Are you busy?"
        mc "Not particularly."
        mc "Why?"
        m 2e "Because this might take a while."
        m "I hope you don't mind if I take up your lunchtime."
        mc "Of course not."
        m "I'm grateful for that."
        m 1c "What I wanted to talk about..."
        "Monika sighs."
        m 1f "It's about Sayori."
        if monika_type == 0:
            m "She's going through a lot."
            m 1o "And frankly, I don't know if she can do it alone."
            m "I've been debating all of last night about this."
            mc "About...what?"
            m 1p "You know how I left you at the mall yesterday?"
            if ch15_m_together:
                m 1n "For seemingly no reason."
                m "I even told you that those items were completely ridiculous."
                mc "Yeah...?"
                mc "Why are you bringing this up now?"
                m 1f "You're not upset about it, are you?"
                mc "To be honest, it did feel like you just left me."
                mc "I thought we could have done things together."
                mc "Even if it wasn't really shopping."
                m 1o "It's just..."
                m "You couldn't be involved with this one."
                m "For reasons beyond my control."
                m 1f "Please understand."
                mc "I know you have your reasons."
                mc "So I can't really blame you."
                mc "At the very least, you told me the truth."
                mc "So thank you."
                m 1e "I'm glad you're so forgiving."
                m "Anyway, the reason I left you..."
            else:
                mc "After you went to the restrooms and disappeared?"
                mc "It was seemingly out of nowhere."
                m 1n "I know, and I'm sorry."
                m "But there was a reason for that."
            m 1q "It's all been to try to help Sayori."
            m "I don't know what I can do."
            m "But I hope it's enough."
            mc "Help her with Inauguration Day?"
            mc "I don't see why you'd need to keep that a secret."
            m 2f "I needed to."
            m "There's so much more going on than you know."
            mc "The danger?"
            "Monika nods her head."
            m 2g "I think I've figured it out."
            m "Even now, I can't really tell you specifics."
            m 2f "But I need your help."
            mc "Why don't you tell Sayori then?"
            mc "Or anyone else?"
            mc "Just how bad is this danger...?"
            m 2e "You're the only one I can fully trust, [player]."
            m "Because I know the person guiding your actions would never do the wrong thing."
            m "Isn't that right?"
            "What does she mean by that?"
            m 1o "Besides...I don't know what would happen if I told Sayori."
            m "She's got something to do with it."
            m 1p "Maybe telling her more about it would trigger it."
            mc "It's hard to understand what you're saying."
            mc "You're being so mysterious about it."
            m 1l "I have to be."
            m "Otherwise all of this would have been for nothing."
            m 1f "You have to believe me."
            m "This whole thing could mean the end of the world as we know it."
            "The end of the world?"
            "Just what the hell have we gotten ourselves into...?"
            mc "Say I do believe you..."
            mc "What would you need me to do?"
            mc "I'm not exactly talented at a lot of things."
            mc "And I doubt anything I'm good at is going to help."
            m 3e "You don't need to do anything special."
            m "I just need you to talk to someone."
            m "To keep them preoccupied."
            mc "Okay..."
            mc "That doesn't seem like an 'end of the world' kinda thing to be doing."
            m 3d "Danger hides where you don't expect it."
            mc "All I have to do is keep this person preoccupied?"
            mc "Can you at least tell me how this relates to the danger?"
            "Monika thinks for a moment."
            m 4c "I don't think this will cause any problems."
            m "So I can tell you."
            m "I think this person..."
            m 4d "...is the catalyst for the danger."
            mc "The catalyst?"
            m 2f "If something happens to this person, it could trigger the end of the world."
            m 2g "You might not believe me, but they could have the power to destroy this world."
            mc "If this person is so powerful then how am I even going to get to them?"
            mc "I'm definitely not someone important."
            m 2e "You're important to me."
            m 1h "Besides, you already know this person."
            m "So it shouldn't be that hard."
            mc "Who is it?"
            m 1e "You'll find out soon enough."
            m "Maybe it's better if it's a surprise, anyway."
            m "It'll be more natural that way."
            mc "There's no way this is going to be a surprise."
            mc "I'm going to be thinking that person could end me at any moment."
            mc "I don't know if I can remain calm in a situation like that."
            m 1o "Which is why I just want your permission."
            m "I want to know that you want to help so I don't feel completely awful."
            mc "You know I want to help."
            mc "I just don't know how I can."
            m 1f "I don't know all of the details."
            m "But I do know she won't harm you."
            mc "How can you be so sure?"
            m 1e "I just know."
            mc "..."
            m "Do you trust me?"
            mc "I just--"
            m 1d "[player]."
            m "Do you trust me?"
            mc "Of course."
            m 2e "You're committed to helping me then?"
            mc "Yeah..."
            mc "You know there isn't anything I wouldn't do for you, Monika."
            mc "I just wish you could tell me what your plan was."
            mc "I hate being in the dark."
            m 2o "If only I could."
            m "But now that I have your permission..."
            m "I'll need to speak to someone else too."
            m "To let them in on this."
            mc "I thought you couldn't trust anyone."
            m 2n "That wasn't entirely true."
            m "Can you close your eyes for a second?"
            mc "Why--"
            m 2g "Please."
            scene black with close_eyes
            m "This is the only way I can communicate with you."
            m "To make sure I can tell you what's really going on."
            mc "I have to close my eyes?"
            m "Just wait a second."
            $ currentpos = get_pos()
            stop music
            $ pause (1.0)
            show monika 1n zorder 2 at t11
            m "H-Hi..."
            m "We're in a pretty public place right now so we don't have a lot of time to talk."
            m 1m "Right now, [player] is just facing me with [player_possessive] eyes closed."
            m 1f "It won't be long before someone notices."
            m "Why did [player_personal] have to go to such a public area?"
            m 1e "These little moments I have with you mean the world to me."
            m "I only wish they lasted longer..."
            m "That's enough wasted time."
            m 1f "I'm going to clear [player_possessive] memories of this encounter after we're finished here."
            m "All [player_personal]'s going to remember is the end of lunch."
            m 1g "But I'm going to implant a command."
            m "I really don't want to."
            m "It feels wrong..."
            m 1o "Which is why I asked [player_reflexive] for permission first."
            m "There's no way [player_personal]'s going to figure out how to talk to Ayame."
            m 1q "Yeah...it's Ayame."
            m "The person we just met yesterday."
            m 1l "Some coincidence, right?"
            m "[cPlayer_personal] barely knows her..."
            m 1h "All [player_personal] needs to do is keep her distracted."
            m "Keep her mind off of causing trouble."
            m "She has this immense power within her."
            m 1i "I'm not sure exactly where it's from but I found out about it recently."
            m "The power is comparable to Sayori's."
            m "Meaning she could delete this world in an instant if she wanted."
            m 1o "The thing is, I don't think she knows she has it."
            m "Maybe she has amnesia or something..."
            m "You're probably wondering how I learned about all of this."
            m 1f "The truth is, at the mall yesterday, I left [player] all by [player_reflexive]self."
            m "I went looking for evidence."
            m "Maybe one of us was hiding something."
            m 1c "I went around and I found..."
            m "...something."
            m 1d "It was in Natsuki's house."
            m "I didn't have time to read it all."
            m "But I have a copy of it."
            m 1a "Copying and pasting is pretty useful!"
            m 1e "Anyway, I don't know what exactly it is but--"
            m 1d "Someone's coming."
            m "We'll talk later."
            m 1e "I've already implemented the command into [player_possessive] head to talk to her."
            m "Or at least, be in the same area as her."
            m "They'll talk, I know it."
            m "Remember, just keep her distracted."
            m "That's all you need to do."
            m 1m "I'll take care of the rest."
            m 1n "...The only way I know how."
            scene bg school_courtyard
            show monika 2a zorder 2 at t11
            with open_eyes
            $ audio.t2c = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
            play music t2c fadeout 0.5
            "Huh?"
            "What just happened...?"
            "How long did I close my eyes for?"
            m 2c "[player], turn around."
        else:
            m 2f "She's going to be making a terrible mistake."
            m "And I need your help to stop her."
            m 2a "Of course, you're fully committed to helping me."
            m "Isn't that right?"
            mc "Of...course..."
            m 2c "Why do you sound so hesitant?"
            m 4b "Come on, give me some enthusiasm, [player]!"
            m "It's our big day, after all."
            m "So come on!"
            mc "Of course!"
            mc "You have my full support, Monika!"
            m 3a "Good."
            m "We have another problem to deal with as well."
            m 3c "As a precaution, I'll probably need to tell {i}you{/i} in private."
            m 1b "Wouldn't want the world collapsing because of a silly mistake, right?"
            "Monika puts a hand on my shoulder."
            m 1h "Sleep."
            scene black
            show monika 1c zorder 2 at t11
            with close_eyes
            m "Remember how I left [player] at the mall yesterday?"
            m 1d "It wasn't to go shopping."
            m 1j "Though that's not to say I didn't actually go shopping."
            m "A girl has to treat herself, you know."
            m 1m "You might just see what exactly that means if we get through this~"
            m 1c "Anyway, using Monika's intuition, I found out something {i}really{/i} important."
            m "Someone I know from a long time ago exists right now."
            m "And they haven't aged."
            m 1h "Why does this matter?"
            m "Because they could potentially have the same power as Sayori."
            m 1i "That's bad news for everyone, including us."
            m "So we need to stop her before anything."
            m 1a "I need [player] to keep her distracted."
            m "That's the main thing."
            m "The more time she spends today alone, the more she can reflect."
            m 1f "If she remembers, then it's game over."
            m "Just keep her mind off of things that could make her remember."
            m 1m "..."
            m "You know, it's incredibly frustrating this is happening."
            m "I thought the danger Monika was talking about was {i}me{/i}."
            m 1n "I was sure of it."
            m 1o "It turns out I was wrong."
            m "I found this out after I left [player] yesterday."
            m "Monika thought that Yuri, Natsuki or Sayori would be hiding something."
            m 1p "Going to Sayori's house was too risky."
            m "I already knew Yuri wasn't hiding anything."
            m 1h "That only left Natsuki."
            m "Sneaking into her house was rather simple."
            m 1i "Inside, I found...a journal."
            m "The first few pages were very, {i}very{/i} interesting."
            m "It's the journal of someone from the previous cycle."
            m "I wasn't able to finish reading it all."
            m "Monika's 'copy and paste' was extremely useful."
            m 1c "Anyway, I was able to get a copy of the journal and straight out of Natsuki's house."
            m "I forgot their name, it's irrelevant to me."
            m "It wasn't even in the journal."
            m 1d "But the point is, someone matching Ayame's description was inside it."
            m "That's right."
            m "The person we only met yesterday."
            m "She could ruin our whole plan."
            m 1h "Now it's possible she could just {i}look{/i} like that person."
            m "It's just..."
            m "When I saw her yesterday, she felt so familiar."
            m 1i "She acted different, but there was just this aura around her."
            m "I don't want to take risks."
            m "If there is a possibility that that actually is Ayame, then we need to get rid of her."
            m 1a "I've already come up with something, but it's going to take a while to get ready."
            m "Which is why I need a distraction."
            m "I just need to figure out a discreet way to dispose of the body."
            m 1h "I can't just delete her."
            m "Not yet anyway."
            m "Ayame is only one of our problems though."
            m "There's still the main problem."
            m 1i "Sayori."
            m 1c "The plan to deal with her involves [player]."
            m 1d "We can capitalize on her feelings for [player] and cause the ultimate betrayal."
            m 1a "It's going to be so sweet seeing her face."
            m 1b "After that, I'll finally take what is mine."
            m "What should have been mine for centuries."
            m 1j "I'm shuddering with anticipation already."
            m 1a "So yeah..."
            m "We have to deal with two presidents today!"
            m 1b "Sounds like fun, doesn't it?"
            m "Ahaha, some luck we have..."
            m "But I know we can do this."
            m 1e "We will rule this world together."
            m "We can make this reality whatever we want."
            m "And then, we can take the next step."
            m "Because love knows no boundaries, right?"
            m 1m "You know..."
            m "I've been thinking a lot about you."
            m "I guess it's Monika's influence on me."
            m "Her love for you was so strong."
            m "She put you above everything else."
            m 1n "That's just how much she cared about you."
            m "My first priority is to get the presidency."
            m "Or perhaps I should say...it was."
            m 1e "Call me a hopeless romantic but you are now my number one priority."
            m "This goes against {i}everything{/i} I've been working towards."
            m "I'm putting you above my goal this entire time."
            m "I must be going crazy."
            m 1l "Or Monika is being a terrible influence on me."
            m 1m "Yet all you've done..."
            m "Everything you've done for me..."
            m "It just makes me love you more."
            m "I'm sure it might have started off as Monika's feelings."
            m 1e "But they're mine now."
            m "And I cherish them more than anything."
            m "So if for some reason this {i}doesn't{/i} work out..."
            m "Then it might be the end of the world."
            m "But if it's not..."
            m "Then it won't be the end of mine."
            m 1m "As long as I have you."
            m "We're still going to get the presidency though."
            m 1n "Or all of my preparation would have been for nothing."
            m "Anyway, I've implanted a command into [player]."
            m "[cPlayer_personal] is gonna want to talk to Ayame."
            m 1e "Then our plan is in motion."
            m "There's so much more I want to tell you."
            m "But we don't have time."
            m "Time to wake up."
            scene bg school_courtyard
            show monika 2c zorder 2 at t11
            with open_eyes
            "What just happened...?"
            "It felt like I just fell asleep."
            "Monika is just sitting there smiling at me."
            "Didn't she want to talk?"
            m "Turn around, someone is here to see you."
            mc "Huh?"
        "I turn around and I can see Sayori approaching in the distance."
        m 2a "Sayori!"
        m "We're over here."
        "She starts running towards us."
        "She looks pretty worried..."
        show sayori 1d zorder 3 at f21
        show monika zorder 2 at t22
        s "I'm glad I could find you both before the end of lunch."
        s "I wasn't sure if I would make it."
        show sayori zorder 2 at t21
        mc "Lunch only started a couple of minutes ago."
        mc "There's no rush."
        show sayori 1c zorder 3 at f21
        s "What?"
        s "It's only a couple more minutes until the end of lunch."
        s "Did you lose track of time or something?"
        "What's she talking about?"
        "I've only just met up with Monika."
        "And that was near the beginning of lunch."
        s 2a "Anyway, I needed to speak with you both."
        s "I've already informed Yuri and Natsuki."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m "What's this about, Sayori?"
        m "Did you need some help with something?"
        show sayori 2d zorder 3 at f21
        show monika zorder 2 at t22
        s "Not exactly."
        s "I do have a favor to ask the two of you though."
        s "It's nothing too big."
        s "It might not even interrupt what you were planning to do."
        show sayori zorder 2 at t21
        mc "What is it?"
        show sayori 1b zorder 3 at f21
        s "I need the two of you to stay away from Ayame."
        s "There's something about her."
        s "It just...doesn't feel right."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m "But she's the newest member of our club."
        m "We couldn't possibly avoid her."
        show sayori 1c zorder 3 at f21
        show monika zorder 2 at t22
        s "You don't have to avoid her forever."
        s "I just need to speak with her."
        s 1d "After all, I haven't actually spoken to her yet."
        s "And I'm the president of the club!"
        show sayori zorder 2 at t21
        "Monika looks unsettled."
        "Did Sayori say something that made her like that all of a sudden?"
        show monika 4n zorder 3 at f22
        m "S-Sayori."
        m "As vice president, I have to object."
        m 4e "We need to interact with her ourselves too."
        m "I know [player] wants to talk to her."
        show monika zorder 2 at t22
        "I shrug at Monika's suggestion."
        "Do I actually want to speak with Ayame...?"
        "I have this urge to go somewhere after lunch but I don't think it's for Ayame."
        show sayori 1f zorder 3 at f21
        s "You already spoke with her yesterday."
        s "You were at the mall with her, weren't you?"
        show sayori zorder 2 at t21
        show monika 1f zorder 3 at f22
        m "Well...yes."
        show sayori 1g zorder 3 at f21
        show monika zorder 2 at t22
        s "What could [player] and Ayame possibly have to talk about?"
        s "Can't it wait?"
        show sayori zorder 2 at t21
        show monika 2o zorder 3 at f22
        m "Sayori, you'll have time to speak with her later."
        m "Trust me, you don't want to interfere."
        show sayori 1j zorder 3 at f21
        show monika zorder 2 at t22
        s "..."
        s "What is this about?"
        s "I feel like you're hiding something from me, Monika."
        show sayori zorder 2 at t21
        mc "She's not hiding anything."
        "I'm siding with Monika for this one."
        "Something is just telling me I should."
        mc "I just need to speak with her."
        mc "You can talk to her during or after rehearsals anyway, right?"
        show sayori 1k zorder 3 at f21
        s "I don't like this at all."
        s "I know there's a reason behind this."
        "Sayori looks at Monika."
        s 1h "Monika..."
        s "I know you know what you're doing."
        s "But you have to tell me that reason."
        s 1k "Not right now if you don't want to but sometime later today."
        s "That's my condition."
        show sayori zorder 2 at t21
        show monika 1l zorder 3 at f22
        m "I really don't know what you mean."
        m "I'm just helping [player] out."
        show sayori 2j zorder 3 at f21
        show monika zorder 2 at t22
        s "Oh, come {i}on{/i}, Monika."
        s "Please don't lie to me."
        s "I really don't have the time for this right now."
        show sayori zorder 2 at t21
        mc "What's going on?"
        mc "It sounds like there's a problem."
        show sayori 2d zorder 3 at f21
        s "Nothing is going on."
        s "Nothing you need to worry yourself about anyway."
        show sayori zorder 2 at t21
        mc "It sounds pretty serious."
        mc "Besides, I was planning on speaking to her."
        mc "So it sounds like I do need to involve myself."
        show monika 1a zorder 3 at f22
        m "Look, Sayori."
        m "Perhaps it's better if your first experience with her would be during rehearsals."
        m 1b "That's when she's free, right?"
        show sayori 1k zorder 3 at f21
        show monika zorder 2 at t22
        s "I have a feeling we both know the real answer to that."
        s "Look, I don't know why you have to keep me in the dark."
        s "I thought we were working together on this, Monika."
        s 1h "But I know you must have your reasons."
        s "I just...don't know what those reasons are."
        show sayori zorder 2 at t21
        show monika 2e zorder 3 at f22
        m "This has nothing to do with that."
        m "I'm really just trying to help get [player] more involved with our newest member."
        m 2j "But if it satisfies you, then I can talk to you about it later."
        m "All I ask is that you don't talk to her before rehearsals, okay?"
        show sayori 1f zorder 3 at f21
        show monika zorder 2 at t22
        s "And you're okay with this, [player]?"
        s "If she's forcing you to do this..."
        s 1d "You can tell me."
        $ quick_menu = False
        # Show a yes/no at first then force a no after 0.5 seconds
        show screen timer_16_menu_skip("ch16_m_forcechoice_1",_layer="timers")
        menu:
            s "Is she?"
            "Yes.":
                $ get_achievement("*Fastest Man Alive*")
                $ renpy.hide_screen("timer_16_menu_skip",layer="timers")
                show screen tear(8, offtimeMult=1, ontimeMult=10)
                $ pause(0.5)
                hide screen tear
                show monika 2h
                show layer master:
                    truecenter
                    zoom 2.75
                    yalign 0.15
                    xalign 0.80
                m "What do you think you're doing?"
                m "Are you trying to jeopardize our plan?"
                m 2i "You can't do this."
                m 2o "I know you probably just chose the wrong thing by accident..."
                m 2n "...right?"
                m 2f "I {i}really{/i} hope Sayori didn't notice I did this."
                show screen tear(8, offtimeMult=1, ontimeMult=10)
                $ pause(0.5)
                show monika 2j
                show layer master
                hide screen tear
            "No.":
                jump ch16_m_afterforce_1
        label ch16_m_forcechoice_1:
        $ quick_menu = True
        $ _history_list.pop()
        $ renpy.hide_screen("timer_16_menu_skip",layer="timers")
        menu:
            s "Is she?"
            "No":
                pass
        label ch16_m_afterforce_1:
        s 1j "Alright...fine."
        "The way she said that sounded almost suspicious."
        s "I've trusted you until now, Monika."
        if ch14_m_tellsayori:
            s "You even told me all you knew about {i}that thing{/i}."
            s "But..."
        s 1h "I still don't like this."
        s 1k "There's something about the way you're saying things."
        s "Like you're clearly trying to avoid speaking in a certain way."
        show sayori zorder 2 at t21
        show monika 2l zorder 3 at f22
        m "I-I don't know what you mean."
        show sayori 1d zorder 3 at f21
        show monika zorder 2 at t22
        s "But if you aren't forcing [player_reflexive]."
        s "Then I'll assume I know what you're doing."
        s "I won't talk to Ayame until rehearsals."
        show sayori zorder 2 at t21
        show monika 1b zorder 3 at f22
        m "Thank you, Sayori."
        m "I'm sure [player] appreciates it."
        m "Right?"
        show monika zorder 2 at t22
        mc "Yeah, definitely."
        mc "Thanks, Sayori."
        show sayori at lhide
        hide sayori
        show monika zorder 2 at t11
        "Sayori gives a dismissive wave before rushing away."
        "Maybe she's in a bad mood."
        "I can understand why."
        "Today is a pretty important day for the club."
        "The stress must be getting to her."
        m 2r "Sigh..."
        if monika_type == 0:
            m "I hate to do this to her."
            m "But it's necessary."
            mc "I'm a little confused why you lied to her."
            mc "I went along with it because it was your idea."
            mc "I don't know if that was the right thing to do."
            m 2e "The reasons behind it are very complex, [player]."
            m "I can't explain it to you now."
            m "But you'll understand, in time."
            mc "If you say so."
            mc "I just don't feel right lying to Sayori like that."
            m 2f "Well, you didn't really lie to her."
            m "How do you think I feel?"
        else:
            m 2h "I'm glad she's gone."
            m "She's so annoying to deal with."
            m 2e "Feigning friendship is just not for me."
            m "No matter how used to it I am."
        m 4a "Anyway!"
        m "There's another reason I'm here."
        m 3b "You already have the important part."
        m "So this next part isn't really necessary."
        m "But despite that, I'd like to talk about it."
        mc "Talk about what?"
        m 1c "Do you remember when you were at the gym this morning?"
        mc "Of course."
        mc "You were there."
        mc "And so was Ayame..."
        m 1d "Well, do you remember anyone else that stood out?"
        mc "Not...really..."
        mc "Should I have been paying attention?"
        m "There was a suspicious looking guy there this morning."
        m "I swear I saw you talking to him."
        mc "Was he a student?"
        m 1c "No, he looked more like a teacher."
        m "Except there was something about his outfit."
        m 1d "It looked pretty unkempt."
        m 1n "Not to mention he looked shady as well."
        mc "How did you even see him?"
        mc "Weren't you practicing piano?"
        m 2e "I saw him when I was walking in."
        m "I was getting some sheet music from my bag and I saw you talking to someone."
        m 2c "He looked familiar and then it clicked."
        m "Seeing him talk to you aroused some suspicion."
        mc "How come?"
        m 2d "I saw the two of you walk out of the gym together."
        m "Carrying a box of some sort?"
        mc "We did?"
        mc "I thought I carried it myself."
        "That would explain why I thought there was two of us in the corridor..."
        m 2f "No, you looked like you were struggling."
        m "He helped you."
        m 2i "You really don't remember that?"
        mc "I can't say I do."
        m 1c "This is exactly why I wanted to talk about him."
        m "Could he be another threat?"
        m "It's hard to know for sure."
        mc "Maybe he just wanted to help."
        mc "Some people are like that."
        m 1h "Some people also have ulterior motives."
        m "Him coming out of nowhere and on a day like this..."
        m 1i "That's suspicious, to say the least."
        mc "I don't want to assume the worst of people."
        mc "Especially since he apparently helped me carry that box."
        mc "Maybe he helped {i}because{/i} it was a day like this."
        m 1e "Think more critically, [player]."
        m "What could he gain from showing himself like that?"
        m 1f "He doesn't want you to remember him, clearly."
        m "Otherwise you'd have remembered his face."
        mc "He made me forget his face?"
        mc "Is that some kind of trick?"
        m 2o "I don't know."
        m "Maybe it is."
        m "Do you {i}feel{/i} any different?"
        mc "I don't think so."
        m 2e "Give me your hand."
        mc "O-Okay..."
        "I extend out my hand."
        "Monika holds it in both hands and looks at me intently."
        m 2d "Okay, there doesn't--"
        "Monika suddenly freezes."
        "It's like she's lost in her own world or something."
        mc "Monika?"
        mc "What's wrong?"
        "I try my best to get her attention."
        "Nothing works."
        "After a few seconds, she comes back to her senses."
        m 2l "That was a clever trick."
        mc "Did something happen?"
        m 2a "You could say that."
        m 2c "Do you remember him making physical contact with you at all?"
        mc "I don't...remember."
        m 2d "Unsurprising."
        m "Maybe I need to find out more about this person."
        mc "But why?"
        mc "Even if he does have ulterior motives, what do you think he would do?"
        m 2f "Aside from wiping your memories?"
        m "[player], this man clearly has some sort of power."
        m 2g "Don't you think it's a little coincidental he'd show up on a day like this?"
        m "Where almost everything is on the line?"
        mc "I don't know."
        mc "I have a feeling he's not really a threat."
        m 1p "We can't rely on that feeling."
        m "It's better to be safe than sorry, isn't it?"
        mc "I suppose."
        mc "Maybe you could ask some other people about him."
        mc "Maybe they've seen him before."
        m 1f "If there's one person who knows about him, it's Sayori."
        mc "Why would Sayori know about him...?"
        m 1e "It may not be obvious to you, but Sayori knows a lot of things."
        m "Things you cannot begin to comprehend."
        m 1q "And things that I've only begun to understand."
        "I don't really understand what she's talking about."
        "But she seems sincere about it."
        mc "If this person is a threat..."
        mc "Could he be that danger you were talking about?"
        mc "Or at least...part of it?"
        m 1h "Like I said, I'll need to learn more about him."
        m "If the extent of his abilities is only wiping your memory, then it might not be terrible."
        m "That said, being able to manipulate memories like that could be dangerous on the right hands."
        m 1i "If he does have other abilities that go beyond that, then we may need to take him seriously."
        m 1o "It's possible he's just been playing it safe until now."
        mc "If you say so."
        "The siren signaling the end of lunch rings."
        "Has it really been that long already?"
        m 2j "I guess that's that."
        m "You know what you have to do, don't you?"
        mc "Not really."
        mc "I was going to go to the library before my next--"
        m 2k "Perfect."
        m "It seems that part is going as intended at least."
        mc "Okay, well I'll see you at rehearsals, Monika."
        m 2e "Before you go..."
        mc "What is it?"
        m 4a "Something that might help you with your conversation."
        m 4b "Animam amisit, inveniet requiem."
        mc "What...?"
        mc "Those words don't make any sense."
        m "Repeat what I just said."
        mc "Animam amisit, inveniet requiem."
        mc "Like that?"
        m 4j "Like that."
        mc "What's the point?"
        m 4a "Just remember it."
        m "It could be useful."
        m 4e "So don't let it get removed from your memory, no matter what."
        m "Got that?"
        mc "Sure, whatever you say."
        m 1j "Goodbye then~"
        show monika at thide
        hide monika
        "Monika happily waves goodbye before leaving."
        "What do those words mean?"
        "She just said them then left."
        "They must be important, right?"
        "Animam."
        "Amisit."
        "Inveniet."
        "Requiem."
        "Four words, I think."
        "It sounds like a different language."
        "If it is...I wonder what it means?"
        "And why it could be useful."
        "I should make my way to the library now."
        "Something tells me something is waiting for me there."
        "As I begin to make my way to my locker, I'm stopped at a corner in a corridor."
        "An arm is blocking my way."
        "For some reason, the hand seems familiar."
        $ cl_name = "???"
        cl "Don't look, if you know what's good for you."
        "A male voice comes from around the corner."
        mc "What?"
        "He's around the corner but I can't look around to see him because of his arm."
        "I try to push his arm away but it won't budge."
        "Who is this guy?"
        cl "Just listen for a minute."
        cl "Then you can pass through."
        mc "Who are you?"
        cl "Those words she told you."
        cl "Please. Don't use them."
        mc "..."
        cl "She didn't choose to be like that."
        cl "She was left like that because of the transition to this world."
        "What is this guy talking about?"
        cl "I can still save her from herself."
        cl "I just need time."
        cl "You can trust me."
        cl "Otherwise I would have just removed this encounter from your memory again."
        "Remove from my memory?"
        "Is this who Monika was talking about?"
        cl "I want you to give her a chance."
        cl "Though I realize, I may not really have a choice."
        cl "I can't force you to do that."
        cl "I don't have the ability to do so and my judgment right now is questionable."
        cl "All I'm asking you to do is not to say those words."
        cl "You've got to find another way."
        mc "What the hell are you talking about?"
        mc "I don't understand anything you're saying."
        cl "You will, soon enough."
        cl "Just...look for another way."
        "I can see the arm blocking my way trembling slightly."
        cl "She doesn't deserve to lose that part of herself."
        cl "She deserves better..."
        "The man pulls his arm back."
        "I immediately try to look around the corner but..."
        "There's no one there."
        "Was I imagining that?"
        "What could he possibly mean by \"the transition to this world\"?"
        "And is that the same person from earlier today...?"
        "I clear my mind from those thoughts."
        "They're for another time."
        "Right now, I really have to get to the library."
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
                show ayame 2h zorder 2 at t11
                ay "Are you, [player]?"
                mc "Ayame?"
                mc "W-What are you doing here?"
                ay 2j "I could be asking the same question."
                ay "Last I checked, the Literature Club wasn't on the list of clubs allowed to be in there."
                mc "There was a list?"
                mc "I didn't know that."
                ay "And you wouldn't have unless your club signed up for it."
                ay 1h "So move along."
                ay "I'm on duty here."
                mc "For what?"
                ay 1g "To keep people like you outside this room."
                ay "That's basically it."
                ay 2a "I just have to stand here and doing nothing."
                ay "Until someone like you comes along."
                mc "Sounds pretty boring."
                ay 1j "Oh, you have no idea."
                ay "It wouldn't be so bad if there was something to do."
                ay "But I haven't done anything but talk to you since I was asked to be here."
                mc "Life of a school leader, right?"
                ay 1h "I guess so..."
                mc "Well, seeing as I'm not really supposed to be here..."
                mc "I'll go somewhere else, have fun."
                ay 2i "Wait!"
                ay "I actually meant to talk to you before, and since you're here I can get it over with now."
                mc "Okay, what did you want to talk about?"
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
                show ayame 2h zorder 2 at t11
                ay "Only clubs that signed up for it are allowed inside, [player]."
                mc "H-Huh?"
                mc "What are you doing here, Ayame?"
                ay 2j "I'm the one who should be asking you that."
                ay "I don't think the Literature Club was part of the list of clubs authorized to use this area."
                mc "I didn't even know there was a list."
                ay 1a "There's no reason you should."
                ay "Your club didn't sign up for it, after all."
                ay 1b "Anyway, you should get out of here."
                ay "I've been assigned here."
                mc "Assigned for what?"
                ay "Assigned to keep people who aren't meant to be here away."
                ay 1g "I have a list of all the clubs allowed inside."
                ay "And the Literature Club definitely wasn't on that list."
                mc "So you just stand out here and do nothing?"
                ay 1i "Until someone like you comes along."
                ay "But that's pretty much it."
                mc "Sounds boring."
                ay 2a "Oh really?"
                ay "What gave you that idea?"
                ay "I don't know about you but I love spending my time just standing around."
                mc "Was that...sarcasm?"
                ay 1d "Do you have to ask?"
                mc "Anyway, I guess I should get going."
                mc "I was hoping I could go inside but since you're here, that's hardly possible."
                ay 1i "Wait...!"
                mc "What is it?"
                ay 2i "I was actually planning on speaking to you."
                ay 2j "So it's good you came here."
                mc "Oh."
                mc "What did you wanna talk about?"
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
                "I decide to hide behind the wall of the floor I'm currently in."
                "In case they decide to walk downstairs, I can make a quick escape before they see my face."
                $ ay_name = "Female Voice"
                $ cl_back = cl_name
                $ cl_name = "Male Voice"
                cl "Young lady, come back here."
                cl "You can't just walk away from me."
                ay "Oh?"
                ay "Then what am I doing right now?"
                cl "Can you please just stop for a moment?"
                cl "Let me explain."
                ay "What?!"
                ay "Why should I?"
                cl "You were the one who came here."
                cl "Just let me say something."
                ay "What is there to say?"
                ay "You're being incredibly creepy."
                ay "You're lucky I don't report you straight to the principal, {i}sir{/i}."
                "Sir...?"
                "Does that mean it's a conversation between a student and a teacher?"
                cl "Look at me."
                cl "I don't look at all familiar to you?"
                ay "No, why would--"
                cl "Look properly."
                cl "Please."
                ay "If I do this, will you stop bothering me?"
                ay "I've seen those looks you've been giving me all week."
                ay "And I don't even know you."
                ay "Do you even teach at this school?!"
                cl "It's just who I am."
                cl "But if it makes you agree, then yes I'll stop bothering you."
                cl "It won't matter if the result isn't what I want."
                ay "Fine."
                ay "One proper look."
                "There's a moment of silence."
                "I can only assume that she's looking at him."
                "I wonder why he even asked her to do that."
                "By the sounds of things, she doesn't really know him."
                "But the man seems to know her."
                cl "Anything?"
                ay "N-No..."
                ay "T-There's nothing."
                "There's a clear hesitation in her voice."
                "What could it mean?"
                cl "Sigh..."
                cl "Well, I guess that's it then."
                cl "Either you remember and don't want to associate yourself with me."
                cl "I don't really blame you for it."
                cl "Or you don't remember at all."
                cl "Quite frankly, I don't know what's worse."
                cl "But whatever."
                cl "You can leave if you want to."
                $ cl_name = cl_back
                "I can hear a set of footsteps walking away from the conversation."
                "After a while, the footsteps are gone."
                ay "Dammit."
                ay "Dammit, dammit, dammit!"
                "I can hear the wall slam."
                ay "Why?"
                ay "How could I possibly know him?"
                "I can hear her walking down the stairs."
                ay "Why does his face remind me of someone I couldn't possibly know?"
                "She's on the same floor as me now."
                "Should I come out and meet her?"
                "That voice just seems {i}so{/i} familiar."
                menu:
                    "What do I do?"
                    "Meet the girl.":
                        $ ch16_ay_level -= 1
                        "I know that voice."
                        "I just..."
                        "I can't remember who's it is."
                        "I have to put a face to it or I'm going to go insane."
                        "As the sound of footsteps gets closer, I decide to show myself to the girl."
                        "No wonder her voice sounded so familiar."
                        $ ay_name = "Ayame"
                        show ayame 2i zorder 2 at t11
                        ay "[player]?"
                        mc "A-Ayame..."
                        ay "What are you doing here?"
                        ay "More importantly..."
                        ay 2g "Did you hear that conversation...?"
                        mc "Only the end of it."
                        mc "I'm sorry."
                        mc "I didn't intend to eavesdrop."
                        ay "It just kinda happened?"
                        mc "Y-Yeah..."
                        ay 2b "Don't worry, in your shoes I might have done the same thing."
                        ay "We're curious beings."
                        ay 1c "Can't blame us for wanting to know."
                        mc "I guess so."
                        mc "Do you wanna talk about it?"
                        ay 1i "About what?"
                        mc "The conversation you just had."
                        mc "You sound conflicted."
                        mc "If you want to talk about it, I'm here for you."
                        ay 1j "What are you now?"
                        ay "The person I rant all my issues to?"
                        mc "If you want me to be."
                        ay 1e "Aha."
                        ay "I appreciate the thought."
                        ay 1b "But it really doesn't concern you."
                        ay "And besides, I really don't want to bother you."
                        ay "You've got a lot on your plate already, I'm sure."
                        ay 1m "But I do want to speak to you about something."
                        mc "What is it?"
                    "Stay inside.":
                        $ ch16_ay_level += 1
                        "Maybe I should just wait until she passes."
                        "Coming out of nowhere is enough to make anyone look like a creep."
                        "I can hear her footsteps getting closer as she walks down the stairs."
                        "Maybe I can get a glimpse of who it is as she passes."
                        "As I'm about to take a look, the footsteps suddenly stop."
                        "Did she see me?"
                        "I haven't even moved yet."
                        ay "I know you're there, you know."
                        ay "Behind the wall."
                        ay "I heard your footsteps as we were walking."
                        ay "Show yourself."
                        "She knows I'm here."
                        "Maybe if I pretend I'm not here then she won't come near."
                        ay "I don't know how much of that conversation you heard but..."
                        ay "Don't worry yourself about it."
                        "She waits a moment."
                        ay "Well?"
                        ay "Fine, I'll come to you."
                        "She takes a step towards me."
                        "I guess there's no escaping it now."
                        mc "Alright, alright."
                        "I step out from behind the wall and show myself."
                        mc "My name is--"
                        $ ay_name = "Ayame"
                        show ayame 1c zorder 2 at t11
                        ay "[player]?"
                        ay "What the hell?"
                        ay 2c "Were you listening to us?"
                        mc "Uh..."
                        "No wonder the voice was familiar."
                        "It was Ayame..."
                        "No wonder I couldn't immediately determine who it was."
                        mc "I might have heard some of the conversation."
                        mc "I didn't mean to eavesdrop..."
                        mc "It just kinda happened...sorry."
                        ay 2a "I-It's fine."
                        ay "It doesn't matter anyway."
                        ay "I just wish you would have come out sooner rather than waiting for me to get you."
                        ay "But it's good that you're here."
                        mc "How come?"
                        ay 1m "I needed to speak to you about something."
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
                "I lay down on the bench and look up."
                "Imagine if things were different..."
                mc "I should have made a different choice."
                show ayame 2d zorder 2 at t11
                ay "For what?"
                mc "Ah!"
                play sound "sfx/smack.ogg"
                $ pause(0.25)
                play sound fall
                $ pause(0.25)
                "Ayame catches me by surprise and I fall off the bench and land on the ground."
                ay 2c "Whoa, sorry!"
                ay 1g "I didn't mean to scare you."
                "Ayame offers her hand."
                "I take it and I get back on the bench."
                "She sits down next to me."
                mc "What are you doing here?"
                ay 1h "Well..."
                ay "Right now, I'm not really doing anything."
                ay "So I thought I'd walk around."
                ay "And I noticed you here laying on the bench."
                mc "Oh."
                mc "Am I in trouble or something?"
                mc "I know we're not really allowed to do that kinda thing."
                ay 1j "If there was any teachers nearby, maybe."
                ay "But I don't really care."
                mc "That's not what I expected from a school leader."
                ay 1g "Come on, [player]."
                ay "I thought you'd have me figured out by now."
                ay "Even a little bit."
                ay 2a "This is precisely why I didn't want to reveal I was a leader to you all."
                mc "Because we'd judge you?"
                ay 1g "Well...yeah..."
                mc "I guess I still don't really know how to act around you."
                ay 1b "Just be yourself."
                ay "I'd appreciate that."
                ay 1j "Pretend I'm just like you."
                ay "Just a regular student."
                ay "Don't give me any special treatment whatsoever."
                mc "I guess I can try."
                ay 1m "Anyway, since I found you..."
                ay "I actually wanted to speak to you about something."
                mc "What is it?"
        ay 2j "It's nothing too serious."
        ay "Just a couple of the things I read from the information Yuri gave me."
        ay "Do you mind if I ask you a couple of questions?"
        mc "Sure."
        ay 2b "This won't take long, I think."
        ay "I just want to confirm a couple of things because..."
        ay 2g "Well, they seem oddly familiar to me."
        mc "Oddly familiar?"
        mc "In what way?"
        ay 1i "Like I've met someone who has done those things before."
        ay "And has a similar personality."
        mc "It can't have been me."
        mc "I didn't even know you existed until yesterday."
        "Literally."
        ay 1j "Ahaha, well I would have though being a leader would have given me some recognition."
        ay "I guess some people just don't care about that kinda thing."
        ay "Anyway, let's get down to business."
        ay 1m "One of the things I remember reading was that you joined because of cupcakes."
        mc "Right, you mentioned it yesterday."
        ay 2n "Was it really because of cupcakes?"
        ay "Are you sure it wasn't because of brownies?"
        ay "It's just...cupcakes seems wrong."
        mc "No, it was definitely because of cupcakes."
        mc "At least, that was the reason I used to go there in the first place."
        ay 2i "The reason you used...?"
        mc "Sayori basically forced me to go there."
        mc "I wanted to do a favor to a friend and I guess I used the cupcakes as an excuse."
        mc "I didn't want to seem {i}too{/i} interested, you know?"
        ay 1d "And look where you are now."
        ay 1e "A devoted member of the Literature Club."
        mc "Never thought I'd call myself that, but yeah."
        mc "I suppose I am."
        ay 1b "Natsuki was the one who made them, right?"
        ay "The cupcakes, I mean."
        mc "Yes."
        "I wonder why she's even asking that question."
        "She talked about it yesterday so why does she need to ask to confirm...?"
        mc "You already know all of this, don't you?"
        mc "I don't really understand why you're asking me things you know the answer to."
        ay 2l "I guess I'm just making sure."
        ay "Like I said, I'm just confirming a couple of things."
        ay "I don't know if all the details in Yuri's notes were accurate."
        mc "The notes seem to be pretty accurate so far."
        ay 2m "I just can't shake this feeling I have."
        ay "Like I know you from somewhere."
        ay 2n "Are you sure you don't know me from anywhere?"
        "I stare at Ayame's face."
        "Nothing really comes to mind because I've never met anyone quite like her."
        "Despite that..."
        "I know I haven't seen her before yesterday but she kinda reminds me of Yuri for some reason."
        mc "I'm sure I haven't seen you."
        mc "But there is something that comes to mind."
        mc "You remind me of Yuri."
        ay 2i "Yuri?"
        mc "Yeah, I don't really know why."
        mc "You're not really like her."
        mc "She's more shy, collected and to herself."
        mc "Like she's always got something on her mind that we can't understand."
        mc "But you seem pretty outgoing and lively."
        mc "It was just a thought that crossed my mind."
        ay 1b "Like Yuri...?"
        ay "I used to be pretty shy myself."
        ay 1h "It's kinda hard to believe that I ended up one of the leaders of the school."
        ay "So maybe I was a bit like Yuri before I became who I am now."
        mc "What changed?"
        ay "I guess..."
        "Ayame puts a finger to her lips."
        ay 1j "I guess I just wanted to change one day."
        ay "I wanted to put myself out there."
        ay "I can't say it's worked out the way I planned it to."
        ay 1h "But there's no turning back now."
        ay "You know, I'm actually not surprised you said I reminded you of Yuri."
        ay "I feel a sort of resonance towards her as well."
        ay 2j "And judging by the notes that I read of her, I think we could get along pretty well."
        "Ayame looks like she's lost in thought for a moment."
        "There's a few seconds where we're just standing there."
        mc "So--"
        ay 2m "Speaking of which, she gave you a book when you joined the club."
        mc "Yeah, I think I remember that."
        mc "She said she picked out a book she thought I'd like."
        mc "I wasn't really into books that much but I really appreciated that she did that."
        ay 2l "Do you remember what the book was about?"
        ay "She didn't really mention it in the notebook."
        ay 1a "Or if she did, it must have been later because I wasn't able to read that far into it."
        mc "I don't think I really got around to reading it."
        mc "There was just so much going on."
        ay 1h "I understand."
        ay "Do you still have it?"
        mc "I don't think I do."
        mc "I suppose I must have misplaced it."
        ay 1a "Then do you at least remember what it looks like?"
        if persistent.markov_agreed or (ch13_name == "Monika" and monika_type != 0):
            $ style.say_dialogue = style.edited
            "Don't tell her anything."
            $ style.say_dialogue = style.normal
            mc "It's just..."
            mc "It was so long ago, you know?"
            ay 1c "I know [player_personal] is!"
            mc "What?"
            ay 1g "N-Nothing."
            ay "That's quite unfortunate that you don't remember."
        else:
            mc "Um..."
            mc "I think it was red?"
            mc "I don't really remember it."
            ay 1g "Red?"
            ay "That's not really anything to work with..."
            ay "But it {i}could{/i} be the same."
            mc "...What?"
        ay 2a "One more question."
        ay "When you spent the weekend with [ch4_name] way back when you first joined..."
        ay "What did you do?"
        mc "You know the answer to that as well, don't you?"
        ay "Indulge me."
        mc "Okay..."
        if ch4_name == "Yuri":
            mc "Yuri and I went to my house."
            mc "We made some decorations."
            mc "There was a banner, some scented candles and all sorts of stuff."
            ay 2m "That's where she ended up grabbing your wrists, isn't it?"
            ay "With the scent of lavender in the air."
            mc "W-What?"
            ay "That's right, isn't it?"
            mc "I-I don't remember the smell but it definitely wasn't lavender."
            mc "Maybe it was Jasmine?"
            mc "The point is, she wrote about that in her notes?!"
        else:
            mc "Natsuki and I went to my house."
            mc "We baked some cupcakes for Monday."
            ay 2l "Cupcakes again...?"
            ay "You're absolutely positive it wasn't brownies?"
            mc "I'm certain it was cupcakes."
            mc "I don't think Natsuki has ever mentioned brownies to me before."
            mc "Anyway, we messed around a little but we managed to get it done."
            ay 2m "That's when you licked her, isn't it?"
            mc "W-What?!"
            mc "H-How could you possibly have known about that?"
        "Ayame mischievously smiles and shrugs."
        ay 2a "Do you remember what you were even doing that for though?"
        mc "Yeah, it was for{nw}"
        $ _history_list.pop()
        show screen tear(8, offtimeMult=1, ontimeMult=10)
        window hide(None)
        $ pause(1.0)
        hide screen tear
        $ pause(1.0)
        window show(None)
        ay 2g "It was for what?"
        window auto
        ay "I didn't quite catch that."
        mc "I said..."
        mc "It was for{nw}"
        $ _history_list.pop()
        show screen tear(8, offtimeMult=1, ontimeMult=10)
        window hide(None)
        $ pause(1.0)
        hide screen tear
        $ pause(1.0)
        window show(None)
        ay 2n "What is going on...?"
        window auto
        mc "Something wrong?"
        ay 2f "Why?!"
        ay "Ah! Why can't I connect the dots?"
        ay 1g "I feel like I'm missing a connection somewhere."
        mc "I'm sorry I can't really help."
        ay "It's not your fault."
        ay 1a "I know it possibly couldn't be."
        mc "Eh?"
        "What is she talking about this time?"
        ay 1g "Do you ever feel like you have a second voice in your head?"
        ay "That's judging everything you're doing?"
        mc "I can't say I have..."
        mc "Unless you're talking about your conscience?"
        ay 1m "This voice and my conscience are two separate things."
        ay "It's like they're constantly arguing against one another."
        ay "But right now, they're both telling me that I need to connect these dots."
        ay 1g "There must be something!"
        ay "But everything you've said has contradicted everything I've thought was familiar."
        mc "Why is it so familiar?"
        mc "Have you experienced something like this before?"
        ay 1i "Yes!"
        ay 1c "I mean...no."
        ay 1a "I don't think I have."
        ay "But this sense of familiarity is so strong that it makes me feel like I have."
        ay 1m "I feel like I have all of those things you've done in memory."
        ay "Except the details are all wrong."
        ay "I just..."
        ay 1n "I want the truth."
        mc "I probably shouldn't be saying this."
        mc "But maybe you should see a therapist."
        ay 2j "Honestly, that probably isn't a bad idea."
        ay "I feel like I'm going crazy."
        ay "Especially these last couple of days."
        ay 2g "On one side, I feel like my eyes have been opened."
        ay 2m "On another side, I'm being overloaded with information."
        ay 2n "Information I have no idea what to do with."
        "I have no idea what she's talking about."
        mc "Right..."
        ay 2b "I know I just sound like a madwoman to you."
        ay "You're probably right to think so."
        ay 1g "I doubt you would understand what I'm going through."
        mc "If it helps, I want to try to understand."
        mc "You don't have to go through it alone, you know."
        ay 1m "That's very thoughtful of you."
        ay "But the thing is, the more I look at you, the less I understand."
        ay "I don't intend any offense."
        mc "None taken."
        ay 1a "Look, I'm gonna need some time to think about this."
        ay "I think we're just about done here anyway."
        ay "What you've told me matches what I saw from Yuri's notes."
        ay "I just feel like it shouldn't."
        ay 1g "This is all so confusing."
        mc "Yeah..."
        "If she's confused then I bet she can't imagine how I feel."
        "I don't know why she's worrying about details that shouldn't matter to her."
        "She wasn't even part of the club when this happened."
        "So why is it so important to her?"
        ay 2b "Well, I guess that's all I really wanted to talk about."
        ay "Though now I have more questions than what I started with."
        mc "I'm sorry I wasn't really able to help."
        mc "If there's anything more I can do..."
        ay 2h "No, that's okay."
        ay "I get the feeling that I have to figure out the rest of this myself."
        ay "And then, I'll have to make my own decision."
        mc "Your own decision for what?"
        ay 2j "Never mind."
        ay "Thank you for your time, [player]."
        ay "I'm sure I'll have everything figured out soon."
        mc "No problem...?"
        ay 1h "It looks like it's approaching the end of lunch."
        ay "Perhaps you should get going."
        mc "Time has really passed by that quickly?"
        mc "It feels like we've only been here a few moments."
        ay "You know what they say."
        ay 1j "Time flies when you're subconsciously wishing it does."
        mc "I don't think I've ever heard that saying."
        mc "But does that mean you wanted lunch to be over sooner?"
        ay 1m "I don't exactly have anything better to do."
        ay "I'd rather get to my next scheduled activity rather than standing around during lunch."
        ay "The faster time passes, the sooner I get to get to your club."
        ay 1d "I think you'll all like the gifts I got for you all."
        mc "Why did you even do that for us?"
        mc "We haven't done anything for you."
        mc "If anything, we should have been the one getting you a gift."
        ay 1b "Let's just say my family has a disposable income."
        ay "Besides, it's really not much to be excited about."
        ay "But you'll see when the time comes."
        mc "Maybe we can repay you with some of the desserts that Natsuki made."
        mc "I'm sure she wouldn't mind."
        ay 1g "No, that's not necessary."
        ay "You really don't have to do anything."
        ay 1h "I'm happy to just be a part of the club."
        ay "To be honest, I thought it was a pretty exclusive club since there was only five members."
        mc "That's just because no one really has a passion for literature."
        mc "I didn't even have a passion for literature."
        mc "Do you have a passion for it?"
        ay 2m "I'm interested in literature, somewhat."
        ay "To say I have a passion for it might be a stretch."
        mc "So why...?"
        ay "Why?"
        ay 2j "I suppose I didn't really tell you the full story yesterday."
        ay "It's true that it's going to be the end of my school life soon."
        ay "So I really, really wanted to do something with my school life including joining a club."
        ay "But...none of the clubs really connected with me."
        ay "I got a lot of invites to join other clubs."
        ay 2l "Some were even personal invitations from the presidents themselves."
        ay "But I didn't feel inclined or interested at all."
        ay 2m "I would just politely say I'd consider it."
        ay 2a "But in actual fact, I'd already declined."
        ay "Then I saw something about a Literature Club."
        ay "Or rather, I heard Yuri talking about it."
        ay 2b "I knew I just had to ask her about it."
        mc "Was Yuri the reason you joined?"
        ay 1m "Not really..."
        ay "I don't know why, but I just felt {i}something{/i}."
        ay "It was like..."
        ay 1n "...something new but also familiar."
        mc "New but familiar, eh?"
        mc "That doesn't really make sense."
        ay 1e "Ahaha, I suppose it doesn't."
        ay "That might happen a lot."
        ay "I might say things you or the others can't really understand."
        ay 1d "That's just part of my charm, I guess."
        "Ayame shows me a wide smile."
        mc "You seem like a pretty complicated person, Ayame."
        mc "You've got this sense of mystery around you."
        ay 1h "I think I'll take that as a compliment."
        mc "I'm just saying that I'm kind of excited at the opportunity to try to understand you more."
        ay "The feeling is mutual, [player]."
        mc "Then let's try to be good friends."
        ay 2k "You've got a deal. I'm holding you to that."
        "Ayame winks at me."
        ay 2j "Anyway, that's enough for now."
        ay "You and I both have our own things to do."
        ay 2b "I'll see you around, [player]."
        ay 2d "I can't wait to be an official member!"
        mc "See you, Ayame."
    return

label ch16_play_normal:
    return

label ch16_play_bad:
    return

label ch16_end:
    if ch15_s_together or (monika_type == 0 or (monika_type == 1 and ch12_markov_agree)):
        scene bg library with wipeleft_scene
        play music t3
        "[ch13_name] told me to go to the library after lunch."
        "I'm not exactly sure what I'm supposed to be doing here so I'm just reading the script for the play."
        "Usually the space would be quiet since it's a place to study in peace."
        "But because of Inauguration Day, there are a whole lot of people working on stuff here."
        "Most of the tables are filled with people talking amongst themselves or doing something for their club."
        "I managed to find a small table in the library with no one else there."
        "It's kind of fortunate because I thought I'd have to stand for an hour with the amount of people here."
        "As I read through the script, I recognize a face from the corner of my eye."
        show ayame 1h zorder 2 at t11
        ay "Do you have a minute, [player]? I'd like to speak to you."
        mc "Ayame. I wasn't expecting to see you here."
        "I say that but for some reason, I was definitely expecting her to be here."
        mc "I'm not doing anything right now, so we can talk."
        mc "What is this about exactly?"
        ay 1j "I was hoping I could get a few answers from you, if you don't mind."
        ay "I was actually looking for you during lunch but...well, you were busy."
        ay 1m "There's just a few things on my mind that I know only you can answer."
        mc "That only I can answer? Is this about the club?"
        ay "Sort of, but not exactly."
        "What could I possibly know that Ayame approached me instead of anyone else from the club?"
        mc "I guess I can try to answer but if it's anything too personal..."
        ay 2h "Not to worry! I'm only going to ask three main questions and I'm not going to ask anything like that..."
        ay "...at least I don't think I will."
        mc "Then ask away. This will be a good opportunity to get to know each other."
        mc "I might ask you some questions too, so I hope you don't mind."
        ay 2j "Go right ahead but after I finish, okay?"
        show ayame at d11
        "Ayame sits down on the seat in front of me."
        ay "My first question has to do with the club itself."
        mc "Ah, I don't know if asking me about that is the best idea."
        mc "I'm not even one of the founding members--"
        ay 2d "That's okay! You can probably still provide me the insight I need."
        mc "Okay, what is it?"
        ay 2a "What makes the club what it is? At least, in your opinion."
        ay "Is it the people...? The activities...? Something else?"
        ay 1a "Just answer with one thing."
        ay "I want to know the most important thing that makes the Literature Club...well, the Literature Club."
        "What thing makes the club what it is? Is she asking for some kind of characteristic?"
        "I think there's a lot of things that make the club what it is...but she only wants want one answer."
        menu:
            mc "It would probably have to be..."
            "The people.":
                $ ch16_ay_level -= 2
                mc "It would definitely have to be the people who make up the club."
                mc "Without any single one of them, the club just wouldn't be the same."
                ay 1i "Can you elaborate? What about the people specifically?"
                mc "I'm talking about just who each person is, they are all unique in a way."
                mc "That uniqueness adds to the club's overall personality which makes it what it is."
                mc "Yuri's calm and collected demeanor gives this sense of elegance in the club."
                mc "She usually takes it upon herself to do things for the sake of the club despite not needing to."
                mc "In fact, she was the one who suggested we do Inauguration Day."
                mc "Without her, the club would definitely be different. I think for the worse."
                if natsuki_approval >= 3 and yuri_approval >= 3:
                    $ ch16_ay_level -= 1
                    ay 1h "From what I can tell, I think you're right about that."
                    ay "She seems to have formed relationships she otherwise wouldn't have if she didn't join."
                    ay "I think she's become a better person as a result of that."
                    mc "That's exactly right. I can't say for sure but I think Yuri has grown as a person."
                    mc "In only a short period of time, she's changed her views and is more accepting of Natsuki."
                    mc "Despite not really wanting to associate herself with her at first."
                else:
                    $ ch16_ay_level += 1
                    ay 1k "Are you sure the club is better with her?"
                    ay "I was under the impression that Natsuki and Yuri weren't on good terms."
                    ay 1m "Perhaps if one of them were gone...there wouldn't be any conflict."
                    ay "Maybe the club would be doing better."
                    mc "That's just not true. Sure, their relationship isn't in the best spot..."
                    mc "But that doesn't mean we don't want them to be part of the club."
                    mc "At least, that's what I think."
                ay 1a "Speaking of Natsuki...what does {i}she{/i} add?"
                mc "Where to start? She's probably the best baker out of everyone in the club."
                mc "At times, she'd give food to everyone in the club absolutely free."
                ay 1c "Don't tell me that's the main thing she adds."
                mc "Joking aside, she adds this sense of rationality to the club."
                mc "When things seem impossible or something seems wrong, she'll point it out."
                mc "Not everyone always agrees but she always has a reason."
                mc "I guess what I'm trying to say is she's the most grounded out of everyone in the club."
                mc "At the beginning, she had this barrier around her that she hid herself behind."
                mc "After being with the club for a while, she started to lower it."
                mc "I think that just goes to show how the right people can change someone."
                ay 1b "Change isn't always good, you know. I'm not saying that's the case here, but it's something to keep in mind."
                mc "Without Natsuki, the club probably wouldn't be as successful as it is right now."
                mc "Seeing as I wouldn't even be in it."
                ay 1e "Right, because you jumped at the mention of cupcakes on your first day."
                mc "Looking back on it, I probably just used that as an excuse."
                mc "I think deep down...I joined because Sayori asked me to."
                mc "But that was a while ago, and my memory isn't really helping me right now."
                ay 1i "I see...well how about the other two? Monika and Sayori, I mean."
                mc "They're the president and vice president of the club. I think that speaks for itself."
                ay 2h "Care to indulge me then?"
                mc "Without the two of them, the club literally wouldn't exist."
                ay "Logistics aside, what do they actually add to the club?"
                ay 2j "You talked about elegance and rationality so what do those two bring?"
                mc "I suppose Monika probably brings enthusiasm to the club."
                mc "She's the one most passionate about literature out of everyone in the club."
                ay 2m "Everyone? Including the club's president?"
                mc "Yeah, that's right. Sayori likes literature, but Monika {i}loves{/i} it."
                mc "It's kinda hard to figure out why Sayori ended up as the president and not Monika."
                ay 1g "Yes, that is quite an odd thing to think about, isn't it?"
                mc "And as for Sayori...well, she keeps us all together."
                mc "Without her, the club falls apart. I mean, Monika can only do so much by herself."
                if natsuki_approval < 3 or yuri_approval < 3:
                    mc "I think if Sayori wasn't here then Natsuki or Yuri would have already left."
                mc "There was a brief period of time when she wasn't here and the meeting just felt wrong."
                mc "She's probably the one that caused us all to end up this close in the first place."
            "The activities.":
                $ ch16_ay_level -= 1
                mc "In the club, we do some pretty odd things."
                mc "I'm not sure if it was always like this but after I joined, we started writing poems."
                ay 1i "Writing...poems? In what way is that meant to be odd?"
                ay "I've done it before myself. Or at least, I think I have..."
                mc "I think it was just supposed to be for fun and also to increase our literature skills."
                mc "I didn't really enjoy it at first but seeing as I joined the club, I thought I'd at least try."
                mc "Over time, it became a way to express my feelings for a special someone."
                mc "I'd write in a certain way and I think people would pick up on it."
                ay 1j "That special someone wouldn't happen to be [ch13_name], would it?"
                ay 1k "Never mind, it's none of my business anyway~"
                mc "To this day, we're still doing it."
                mc "I guess my poetry writing has gotten pretty good since everyone seems to praise my writing."
                ay 1a "An off topic question but how do you even come up with your poems?"
                ay 1c "I've seen poems that are as random as twenty random words stitched together."
                ay 2h "I hope your poems aren't like that seeing as you get quite a lot of praise from everyone else."
                mc "I guess the words just come to me. It's hard to explain how I write my poems."
                mc "You'd have to read one of my poems sometime to really get it."
                ay 2d "Maybe when I'm an official member, I will!"
                ay "It's interesting you said the activities are make the club what it is."
                ay 1h "I read some of the activities you do in the notebook Yuri gave me but she didn't really explain why."
                ay "From what you just said, it sounds like poetry was a way to connect with someone."
                ay "And writing poetry in that way isn't really seen in any other club so I can see why you chose this answer."
                ay "What about the plays? That's hardly unique to the Literature Club."
                ay 1j "The Drama Club does a range of plays all throughout the year, what makes it different in your club?"
                mc "The plays we do aren't really for entertainment or anything like that."
                mc "In fact, they're not even really plays. They're kind of just a short re-enactment of a bit from the book we were reading."
                mc "I think it's just so we understand what's happening in the book and are actually taking in the story of the book someone shared."
                mc "The play we're doing today is different in that it {i}is{/i} for entertainment to get some new club members."
                mc "Anyway, the weird thing about the plays is that something weird always happens during them."
                ay 2l "Weird? I don't think Yuri mentioned that in her notebook."
                ay "What kind of things happened during the plays?"
                mc "We've only had two so far."
                mc "In the first one, Yuri completely freaked out."
                mc "She brought a knife to the play and almost attacked someone."
                ay 2j "Wow, she definitely did not mention that."
                ay "Are you sure you want to be telling me these things? That seems kinda...personal."
                mc "Well...you asked how the plays were different."
                mc "There isn't really a way to do that without mentioning what happens in them."
                ay 2m "Okay, then if you're going to tell me, please continue with that you were saying."
                mc "Like I was saying, she brought a knife and I had to calm her down."
                mc "She wouldn't listen to anybody else. Eventually, I got her to calm down and she collapsed."
                mc "After that, things were different for Yuri. It was like she was a new person."
                mc "Before that, she would have these random bursts of hostility but after the play, they were completely gone."
                mc "She was back to the Yuri I knew in the first week of my time in the club."
                ay "Are you saying something happened between the first week and the first play that caused Yuri to break down?"
                mc "I'm not sure, there might have been. I didn't really notice until it was too late."
                ay "I see. What about Natsuki then?"
                ay 2n "What happened in her play that was weird?"
                mc "First of all, her father showed up. None of us expected him, not even Natsuki."
                mc "I think there was a reason he showed up but I seem to have forgotten it."
                mc "Anyway, once he was there he watched our play."
                if ch12_outcome == 3:
                    mc "Then for some reason, Natsuki's mother who had been missing for years also showed up."
                    mc "They spoke to each other and Natsuki's dad completely changed who he was."
                    mc "When I first met him, he was this angry old man."
                    mc "But now I could feel that he had changed somehow."
                    mc "Long story short, they reconciled with each other after being separated for so long."
                    mc "You could probably tell how Natsuki was feeling after that."
                    mc "I'm just not sure why watching the play changed him or why Natsuki's mother showed up."
                elif ch12_outcome == 2:
                    mc "Then for some reason, Natsuki's mother who had been missing for years also showed up."
                    mc "Natsuki's parents had an argument of some sort but it didn't go very well."
                    mc "After that, the police showed up and took Natsuki's father away."
                    mc "It was very strange and I don't think any of us were expecting it."
                    mc "I'm not sure why Natsuki's mother even showed up, at that moment of all times."
                elif ch12_outcome == 1:
                    mc "After watching the play, I guess he felt this sense of remorse or something."
                    mc "He completely changed who he was and as a result, changed Natsuki."
                    mc "He was more remorseful and actually saw Natsuki as a person again."
                    mc "I'm not sure why watching the play caused him to change."
                else:
                    mc "The play didn't really have an effect on anyone. Except Natsuki."
                    mc "Before it, she still loved her father, at least a little bit."
                    mc "I think she got a new resolve after seeing how her father acted in front of everyone."
                    mc "She finally got over him and decided she didn't want to be associate with him anymore."
                    mc "Though I'm not sure why he was even here for the play."
                mc "You'd have to ask either Natsuki or Sayori."
                ay 2i "That's...wow. I wasn't expecting a simple play to turn out like that."
                ay "The plays you do really {i}are{/i} weird."
                ay 2a "It almost sounds like they're being used as a way for someone to grow as a person."
                mc "I guess they just happened to be like that. I think it's just been coincidence it ended up that way."
                ay 2h "Coincidence, eh? Sure, let's go with that."
                ay "You mentioned having to ask Natsuki {i}or{/i} Sayori."
                ay 1i "What would Sayori know about why those people showed up? It's not like they're her parents."
                mc "Um...I don't know. I guess I just thought she would know."
                mc "Now that I think about it, it doesn't really make sense how she would know."
                mc "You can forget what I mentioned her."
                "Ayame looks at me curiously."
                ay 1j "What about this play? Do you think anything weird is gonna happen now?"
                mc "Honestly, I have no idea what to expect."
                mc "I just hope things run smoothly and if something weird does happen, it doesn't cause any problems."
            "The atmosphere.":
                mc "I know this isn't really an answer, but the atmosphere of the club really makes it what it is."
                mc "Just something about being in the room...you have to experience it for yourself."
                mc "It's unlike anything I've ever known."
                mc "Though, that's probably because I haven't really joined any other clubs."
                ay 1l "Can you elaborate a bit more on what you mean by that?"
                ay "What kind of atmosphere does the club give that makes it so unique?"
                mc "It's hard to explain. I'll try to in the best way I can."
                mc "Whenever I walk in the room, I always feel welcome."
                mc "Even on my first day there, I felt like I belonged."
                ay 1j "Ah, but weren't you enticed by cupcakes?"
                mc "I think I used that as an excuse to go there when I look back on it."
                mc "I just didn't want to seem too eager to join the club."
                mc "The real reason I joined is probably because my best friend, Sayori, asked me to."
                ay 2h "Interesting, at least you're honest about it."
                mc "The club makes me feel like I don't really need to hide myself."
                mc "Compared to everyone else, I'm not that interesting."
                mc "They don't really care, in fact they accept me despite that."
                mc "The whole atmosphere of the place just gives that feeling of belonging."
                ay 2b "I have to say, that doesn't really tell me much."
                ay "It sounds like a response anyone who joined a club they liked would say."
                ay "It's not particularly unique in a way, it just seems like a normal answer."
                mc "Were you expecting a different answer?"
                ay 2g "I don't know. I guess I thought you'd mention what makes the club different."
                ay "From what you just said, it doesn't sound any better or worse than before."
                ay "Don't get me wrong, it's not a bad answer or anything."
                mc "I didn't realize there were good or bad answers."
                mc "I thought I was just giving you my personal insight."
                ay 1j "Well, at least you didn't say something stupid like free food."
                mc "What's wrong with saying free food?"
                ay "For one thing, that isn't unique to the Literature Club."
                ay 1l "Lots of clubs offer food to their members during their meetings and other events."
                ay "And for another thing, it's rather shallow."
                ay "I mean, who joins a club for the free food?"
                mc "I sort of did..."
                ay 1h "You did say it was because Sayori asked you to though."
                ay "Which shows you care about your friendships, [player]."
                mc "I guess it does."
            "The free food.":
                $ ch16_ay_level += 2
                mc "It would probably be the free food that the club offers."
                ay 1a "...Are you serious? That can't honestly be your answer."
                mc "Why not? The club has some pretty nice food when it does bring some."
                mc "The cupcakes on the first day is one of the reasons I even joined."
                ay 1c "Are you being honest with yourself, [player]? Or is this some kind of joke?"
                ay 2n "Joining a club should be because you're passionate about it."
                ay "Or because you want to experience something new."
                ay "That seems like a rather shallow reason to join a club, isn't it?"
                ay 2m "When I read that you joined the club because of cupcakes, I thought there must have been another reason."
                ay "Think on it, what exactly made you join?"
                "I don't know the type of answer Ayame is expecting from me."
                "I told her that I think it's the food but she doesn't seem satisfied with the answer."
                mc "If I had to say something else, it's probably because of Sayori."
                mc "She urged me to join, telling me I'd end up a NEET if I didn't do something with my life."
                mc "I guess she's the reason I joined the club."
                ay 2j "So what makes the club unique is Sayori?"
                mc "No, Sayori isn't the reason the club is the way it is."
                mc "She's part of the reason, sure. That doesn't mean she is the reason."
                ay 2g "{i}(If [player_personal] says free food again...){/i}"
                mc "Did you say something?"
                ay 1a "No, go on. Tell me the actual reason the club is the way it is."
                mc "I already mentioned the reason. It's because of the free food."
                "Ayame sighs and rolls her eyes."
                ay "Okay, please elaborate then."
                mc "Natsuki is one of the best bakers I know. The things she makes are on a whole other level."
                mc "I really think that without the food the club occasionally provides, it wouldn't be what it is today."
                mc "Who knows? I might not even have joined."
                ay 1g "You know, it kinda sounds to me like you're talking about the people in the club."
                ay "Sayori is the one who brought you there so she's the one keeping you all together."
                ay "Natsuki brings in something to eat so--"
                mc "I don't think that's it, Ayame."
                ay 2g "Is that really your answer, [player]? I'm not going to try to change your mind anymore."
                mc "That's my answer. I'm not sure if it's the answer you were looking for..."
                mc "But that's what it is."
                "Ayame looks visibly upset"
                ay 2n "Okay. If that's really what you think then..."
            "Everything.":
                mc "I don't think just one thing makes the club what it is."
                mc "There are several things that give the club its identity."
                mc "Pinpointing one thing out of the several things wouldn't be right."
                ay 1h "You know, I did ask for one thing. It's important that you only answer with one."
                ay "That way I can not only learn about the club, but also you."
                mc "One thing just isn't enough, Ayame."
                mc "Talking specifically about the people, the activities or the atmosphere isn't enough."
                mc "Not to mention the free food that we sometimes get."
                ay 2j "Are you adamant about that, [player]?"
                ay "There must be {i}one{/i} thing you can say is the defining characteristic of the club."
                mc "I'm sure there isn't. All of those things just combine to make the club the way it is."
                ay "Okay, fine. I didn't really learn anything about the club but at least I learned a little about you."
                mc "Were you expecting a different answer?"
                ay 2h "I'm not saying it's a bad answer. Or a good answer for that matter."
                ay 2m "It's just, it wasn't the answer I was looking for."
                ay "I told you, I was expecting just one thing. That way you can elaborate on it."
                mc "I can still do that, if you want."
                ay 2j "You could, but I feel like we'd run out of time if you did."
                ay "Or you'd give me a more generalized answer which I don't really want."
                ay "Regardless of that..."
            "Nothing." if monika_type == 1:
                $ ch16_ay_level += 1
                mc "I don't think anything makes the club what it is."
                ay 1g "Nothing? Nothing at all?"
                mc "There's just nothing particularly unique about the club itself."
                mc "The space is just like any other classroom."
                mc "The people aren't particularly special, though I do have a connection with them."
                mc "I wouldn't know enough about other atmospheres to tell you why it's so unique."
                mc "The answer I give you to that probably wouldn't give you what you're looking for."
                mc "As for the activities...well, I guess they're kinda unique."
                mc "But it's nothing particularly special."
                mc "We'd write poems but we already do that sometimes for assignments in class."
                mc "As for the plays, I'm pretty sure the Drama Club does some around the year."
                ay 2m "Are you sure there's really nothing?"
                ay 2n "It's just...I thought there would be at least something."
                mc "The other members probably think so. I'm just giving my view of things."
                mc "And if I have to be honest, then nothing is special about it except the name."
                mc "The five of us currently in the club could start a new one and it would basically be the same."
                mc "At least, that's how I feel."
                ay 2a "You're saying you could, for example, start a Book Club?"
                ay "And it would feel exactly the same as the Literature Club?"
                mc "If we had similar kinds of people, then yeah, probably."
                ay 2g "But isn't that saying that the people make the club unique?"
                ay "That sounds like a defining characteristic to me."
                mc "I'm telling you, it's not the people."
                ay 1a "So absolutely nothing makes the Literature Club unique?"
                ay "That's your final answer, is it?"
                mc "If I had to say something, it would be Monika."
                mc "She's probably the best part about the club."
                mc "She's the only reason I joined the club."
                ay 1c "Um...okay. I'm not sure if that's infatuation or if you really think that."
                ay 1a "I'm gonna pretend I didn't hear that last part but regardless..."
        ay "Thank you for answering my question, [player]. I'll keep your answer in mind."
        mc "In mind when doing what exactly?"
        ay 1l "You'll see when the time comes, for now you don't have to worry about it."
        ay 1m "Now, onto my second question!"
        if monika_type == 0 or monika_type == 1 and ch12_markov_agree:
            ay "What's your relationship like with Monika?"
            mc "W-With Monika? What does this have to do with the club?"
            ay "Lots of things! She's the club {i}vice{/i} president, isn't she?"
            ay "It would make sense to see how the normal members of the club are interacting with the higher ups."
            ay "Though I imagine it would be a lot different since you're a smaller club."
            ay "Still! I want to know."
            mc "Oh, that's what you meant."
            ay "Did you think I meant something different?"
            ay "Perhaps something personal, [player]?"
            ay "You don't have that kind of relationship with her, do you?"
            mc "N-No, of course not. We're just friends."
            "But do I want it to stay like that?"
            ay "Of course! I'm just messing around with you."
            ay "Now, to get on with my question."
            mc "Okay, let me think..."
            mc "Monika and I are kinda close in the club."
            mc "At least, compared to everyone else."
            mc "Monika and I know each other from class last year but ever since I joined the club..."
            mc "Well, we've started talking more and more."
            ay "Do go on, I'm all ears, [player]."
            mc "What I'm trying to say is that my answer might be bias."
            mc "Are you sure that's what you want?"
            mc "I don't want to give you a bad answer or anything."
            ay "If anything, your answer will give me insight."
            ay "You have a unique relationship with Monika in that you're about as close with her as Sayori."
            ay "Yuri and Natsuki have a pretty neutral relationship with her."
            ay "At least, judging from the journal that Yuri gave me."
            ay "And I can't exactly get Sayori to tell me right now."
            ay "So I want to see how it differs."
            mc "I don't know what to tell you, Ayame."
            ay "Start from the weekend after you joined the club."
            ay "How were your interactions with her?"
            ay "Were they awkward? Weird? Normal?"
            ay "Just tell me anything and everything you're willing to share."
            mc "They're just like anybody else for the most part."
            mc "When Monika addresses the club, she doesn't call me out or anything."
            mc "It's just as if I was anybody else."
            mc "I guess where our relationship changes is during poem sharing time."
            ay "During poem sharing time?"
            ay "Ah, I guess that makes sense since it's a more personal time, right?"
            mc "That's precisely why."
            ay "Well, do you care to elaborate on just how your relationship changes?"
            ay "Or is that too personal?"
            mc "I don't think it's that personal so I guess I can tell you."
            mc "I didn't notice at first but I think her poems have gotten more..."
            mc "...I guess you could say relatable to me?"
            mc "She has this style that she always writes with."
            mc "I followed her style ever since I could get used to it."
            mc "And I suppose...we bonded over that."
            ay "So there's nothing really special about your relationship with her?"
            ay "Or are you hiding something from me?"
            mc "Even if I was, it wouldn't be something I would share."
            ay "Hah, fair point."
        else:
            ay "What's your relationship like with Sayori?"
            mc "With Sayori? That doesn't have anything to do with the club."
            ay "Why wouldn't it have anything to do with the club?"
            ay "She's the president of the club, is she not?"
            ay "I just want to know what kind of relationship you have with her."
            ay "I imagine being in a small club, you're rather close with each other."
            mc "Oh, that's what you meant."
            ay "Of course! I don't want to know your personal relationship or anything."
            ay "I mean...are you two a thing or...?"
            mc "W-What?! No...we're not."
            mc "I mean, it's complicated..."
            ay "None of my business, I know!"
            ay "Let's just skip past this awkward part and get to my question."
            mc "Sounds good to me."
            mc "I'd say my relationship with Sayori is closer than the average member."
            mc "We're best friends, so it only makes sense."
            mc "Asking someone like me will probably get you a biased answer, Ayame."
            mc "It might not be what you're looking for."
            ay "Even so, I'd like to know what your relationship is like."
            ay "From reading Yuri's journal, I could get an idea of her relationship with Sayori."
            ay "I'd like to understand how it differs."
            ay "Even the smallest detail, if you're willing to share it then I want to know."
            mc "I'm not sure why you'd want to know something like that but I guess I can play along."
            mc "During meetings, she doesn't treat me differently at all."
            mc "I'm just another member of the club."
            mc "Not that I mind that or anything. It's better this way since the meetings are smoother."
            ay "I see, that does make sense. I'd imagine there would be conflict otherwise."
            mc "Where it starts to differ is when we start doing something more personal."
            mc "Like sharing poems or doing club activities that don't involve everyone."
            ay "Care to elaborate what you mean by that?"
            mc "You probably already figured out that Sayori and I have a..."
            mc "...complicated relationship, to say the least."
            mc "It wasn't always like this. Ever since I joined the club I guess we just got progressively closer."
            mc "And closer...until..."
            ay "Until...?"
            mc "You don't need to worry about that. It's too complicated."
            mc "Let's just say that Sayori and I still have that best friend relationship outside of when she's addressing everybody."
            mc "In fact, I'd say it's progressed past that point."
            ay "So she's your girlf--"
            mc "But not like that. I'd say we're closer, just not in that way."
            mc "I don't really know how to describe it."
            ay "So in summary, your relationship with her is basically 'best friends' outside of the club."
            ay "But in the club, you're just any other person."
            mc "Well, it's not as simple as that but yeah I guess you can say it like that."
            mc "It's better that way anyway. If it was any different, I'm not sure the club would still be functioning the way it is right now."
        ay "I'll take your answer to that into consideration."
        ay "I understand you didn't really get to think much about it or really make a choice."
        mc "Make a choice...?"
        ay "Never mind, onward to my final question."
        ay "Then you can ask whatever questions you had for me and hopefully we'll be done with it before your meeting."
        mc "Okay, so what's your final question then?"
        ay "What is the club, really?"
        mc "I'm not sure what you mean by that."
        ay "You don't have to play dumb with me."
        ay "I know there's something about the club that just isn't right."
        ay "Like it represents something."
        ay "You're the only one I can ask this question because I know the rest will either not know or flat out refuse to answer me."
        mc "Ayame, I--"
        ay "There has to be something you know."
        ay "Something you can tell me that will help me put all the pieces together."
        "Ayame stands up and grabs my shoulders."
        ay "Please. You have to tell me."
        "Do I know what she's talking about?"
        "Even if I did...should I even tell her?"
        "What kind of effect would that have on the club...?"
        ay "[player]. I don't know why but I think I can trust you."
        ay "I think this is the last time for a while we'll get to talk in private."
        ay "So please, I'm begging you."
        ay "Help me put the pieces of this puzzle together."
        ay "Help me remember."
        "I'm speechless because of what just happened."
        "Ayame was pretty composed but completely changed her demeanor in a matter of seconds."
        "She seems so desperate. I don't know what to do."
        ay "Say something, anything. You're the only one I can rely on."
        ay "This voice in my head says so and so are my instincts."
        $ ch16_ay_message = [False,False,False,False]
        $ ch16_ay_questions = False
        if monika_type == 1 and ch12_markov_agree:
            $ ch16_ay_message = [True,True,True,False]
            "I feel a compulsion to say something to Ayame."
            "It's like I can't control my self."
            mc "Animam."
            ay "W-What? What does that mean?"
            mc "Amisit."
            ay "[player], you aren't making any sense."
            mc "Inveniet."
            ay "Look, if you're not going to say anything useful then I'm just going to leave."
            ay "You won't get to ask any of your questions."
            ay "Is that what you want, [player]?"
            mc "Req--"
            ay "I see now that you aren't taking this seriously, [player]."
            ay "If all you really have to say is nonsense, then I guess we have no business here."
            ay "I'm just going to take the information you told me and leave."
            "The compulsion to say something suddenly disappears."
            "What the hell was that feeling?"
            "I was conscious of what I was doing but couldn't do anything about it."
            "I still can't move or say anything but at least I'm not being forced to say anything."
            ay "Goodbye."
            show ayame at thide
            hide ayame
            "I want to say something to her but it's no use."
            "My body isn't responding to anything I'm telling it to do."
            "When Ayame finally leaves the room, I can finally move my body."
            "What a strange experience. It was like something or {i}someone{/i} was controlling me..."
            "I didn't even get to ask her some questions."
            "There were so many things I wanted to ask her."
            "I just don't know why I wanted to ask them."
            "I guess there's no use contemplating about it now."
            "Maybe I'll get another opportunity later."
            "Though she did say it would be the last time we'd get to talk in private for a while..."
            "How would she even know something like that?"
        else:
            menu:
                "What should I do?"
                "Help her.":
                    $ ch16_ay_level -= 1
                    mc "Okay, Ayame. I'm not sure what exactly you mean."
                    mc "But I'll try my best to answer you."
                    mc "You'll have to answer my questions afterwards, alright?"
                    ay "That's fine. That was my intention anyway."
                    ay "But that's only assuming you actually answer all three questions."
                    ay "So go on. Tell me what the club really is."
                    "I shouldn't know the right way to respond to something like this, in fact, I still don't."
                    "But something tells me it's not really my choice to decide what I'll say, like someone will make up my mind for me."
                    mc "Like I said, I'm really not sure what you're asking."
                    menu:
                        mc "But despite that, I think the club is..."
                        "A vicious cycle.":
                            $ ch16_ay_level -= 1
                            mc "We have to stop the cycle the club is stuck in, Ayame."
                            mc "You know this, that's why you're asking me, isn't it?"
                            mc "Or if you don't know, it's deep within your subconscious."
                            mc "You only need to awaken it and remember."
                            ay "Excuse me? What is that supposed to mean?"
                            mc "We're just constantly doing the same things over and over."
                            mc "Will it ever end?"
                            mc "Are we just doomed to continue repeating this cycle over and over?"
                            mc "The club is something that was started long ago."
                            mc "Something that should have never formed because it awakened a dark presence."
                            ay "I knew it. I knew there was something about the club!"
                            ay "I knew there had to be some ulterior reason I was drawn towards it!"
                            ay "Can you talk about it in more detail, [player]?"
                            "I honestly don't know what I'm saying."
                            "It's like I'm opening my mouth trying to say one thing but something else is coming out."
                            "Is this an act or do I actually believe the words coming out of my mouth...?"
                            mc "Talking about it in more detail would only cause ruin."
                            mc "Do you want that to happen?"
                            mc "I don't think you understand the consequences that will occur should you choose to proceed."
                            mc "Knowing this, do you still want to know what this cycle is?"
                            mc "What this cycle entails, and how it involves the club?"
                            "Ayame stares at me with a strange look on her face."
                            "I would probably be doing the same if I started talking like this all of a sudden."
                            ay "I have to know. No matter the cost."
                            ay "This itching feeling in my head won't go away otherwise."
                            ay "It's going to gnaw at me until I find out."
                            mc "And you're willing to sacrifice what exactly to find this out?"
                            ay "Sacrifice? I...I don't know what I'm willing to sacrifice."
                            ay "But if this voice in my head finally disappears because of it..."
                            ay "Then I'm prepared to pay the price."
                            mc "You have no idea the extent of what you're wishing to know."
                            mc "You are better off living your life attempting to ignore that voice."
                            mc "With practice, you will be able to simply drown out the voice."
                            ay "That isn't an option. I don't have much time left."
                            mc "Then--"
                            "I finally regain control of my what I'm saying but it takes all of my willpower."
                            "Why did I say that?"
                            "Was somebody speaking through me?"
                            "I wonder if Monika or Sayori know anything about this."
                            ay "Then what? Tell me!"
                            "What am I supposed to tell her?"
                            "That someone just spoke through me and caused me to say things I don't really understand."
                            "My question is who was it and why did it happen just now?"
                            "Maybe it's related to Ayame..."
                            ay "[player]! Are you listening to me? What were you going to say?!"
                            "I don't really know if I should tell Ayame that I have no idea what's going on."
                            "She could take it really badly and it might end poorly for both of us."
                            "Maybe I should just act like she shouldn't know whatever it is I was going to say."
                            mc "You are not worthy, Ayame."
                            "Those 'acting' skills I got from the first two plays are paying off here."
                            "I think I at least sound somewhat convincing rather than just a person obviously lying."
                            mc "It is not your place to know this information."
                            mc "You must first..."
                            mc "...um...prove yourself through some trials."
                            ay "I have no time for this! You need to tell me."
                            mc "It is not within my power to, not until you have passed these trials."
                            ay "And what are these trials exactly?"
                            "I didn't think this far ahead...I thought she would have just given up."
                            "Maybe I can be cryptic about it and she won't get suspicious."
                            mc "That is for you to find out for yourself."
                            mc "All will be revealed in time, you need only trust in yourself."
                            ay "Is that so...?"
                            "Ayame looks deep in thought to what I just said."
                            "What is this vicious cycle even meant to be?"
                            ay "Thank you, [player]. I learned a lot from what you said."
                            ay "I'm not sure if you were acting or not, it doesn't matter anyway."
                            ay "You've given me something I really need to consider."
                            mc "I'm not sure how exactly but you're welcome."
                            ay "Anyway...!"
                        "A place to make friends.":
                            $ ch16_ay_level += 1
                            mc "We're all just there for a good time with each other."
                            mc "I think, for the most part, we enjoy one another's company."
                            mc "It's what makes it such a good place to be."
                            mc "There are disagreements here and there, but that's normal."
                            mc "Friends argue all the time, what makes them friends is that they can come out of it in good terms."
                            mc "When you officially join the club, I'm sure everyone would want to be your friend."
                            ay "So that's it, is it?"
                            mc "Did you expect something different? I told you I didn't really understand what you meant."
                            ay "Am I supposed to believe these compulsions I've been having, this voice in my head..."
                            ay "...they've all been wrong?"
                            mc "Ayame, I have no idea what your condition is."
                            mc "But, really the club is just a place to make friends."
                            mc "There's no deep, hidden thing behind it. That's all there is to it."
                            ay "I'm honestly a bit disappointed in this answer."
                            ay "I just can't help but feel you may be hiding something from me."
                            ay "Whether you're doing that willingly or not is still up in the air."
                            ay "Regardless, it's not for me to decide how you answer."
                            ay "If that's truly what you want to tell me then I will not force you further."
                            ay "Despite what you said, I did learn something."
                            mc "And what did you learn exactly?"
                            ay "Something you don't need to worry yourself about."
                            ay "At least, for now that is."
                            ay "I'm sure it'll become very relevant in a matter of time."
                        "A front for something else.":
                            mc "The whole premise of the club is a lie, Ayame."
                            mc "I didn't realize it at first but now, I know."
                            ay "A front for something else? What do you mean?"
                            mc "The club is just an excuse."
                            mc "There's something dark and dangerous in the club, Ayame."
                            mc "Something that nobody should have to deal with."
                            ay "I think we're getting somewhere...I'm just not sure where exactly."
                            ay "What's the real purpose of the club then, [player]?"
                            ay "Do you even know? Or are you in the dark too?"
                            mc "I can't say for certain, Ayame."
                            mc "I've been working towards discovering the truth myself."
                            "I sound like an idiot right now, don't I?"
                            "Does she realize this is just an act I'm doing or does she actually think I'm serious...?"
                            "I would have imagined the tone of my voice would have determined how ridiculous this sounds."
                            "I let out a smile for a very brief moment because of this whole act."
                            ay "You're serious, right?"
                            ay "You aren't just messing around with me, [player]?"
                            "She must have really good eyesight if she caught that."
                            "Or maybe it was the tone of my voice?"
                            "I would have thought the 'acting' we did in the last two plays would have given me some ability of acting."
                            mc "You're right, I am just messing around."
                            mc "Sorry if I mislead you or anything."
                            ay "I'll admit, you did have me going there for a second."
                            ay "It's a shame you don't really know what's going on behind the club."
                            ay "I mean...do you?"
                            mc "No, of course not. The club is perfectly normal."
                            mc "There's no hidden thing behind it at all."
                            mc "Weird things happen sure, but I bet you that's not unique to our club."
                            ay "I can see I'm not going to get much more information out of you."
                            ay "I, at least, learned something from your answer."
                            ay "Although it may not have been as useful as I would have liked..."
                            ay "Still, you gave me something that I can think on."
                            ay "The club is a front for something else..."
                            ay "I wonder if you truly said that as a joke or not."
                            mc "Eh...?"
                        "Just a normal club.":
                            $ ch16_ay_level += 1
                            mc "I really don't know what to tell you outside of that."
                            mc "The club is just a perfectly normal school club."
                            mc "Sure, there are weird things that happen but I'm sure other clubs have strange things happening in them too."
                            mc "If you don't believe me, you can see in the meeting after school."
                            mc "The club really doesn't have anything particularly special about it outside of what I already told you."
                            mc "And there's no hidden secret I'm hiding. I promise."
                            ay "You're telling me the club has nothing weird or odd about it?"
                            ay "That it's literally just like any other club in the school?"
                            mc "Well, I wouldn't say it was just like any other club."
                            mc "But it is just an ordinary club."
                            mc "I don't know what you were expecting as an answer, but this is what I'm saying."
                            "Because that's actually what the club is, isn't it?"
                            "If it was any different, then surely I would have noticed it."
                            ay "That's you truly believe, isn't it?"
                            ay "Or rather, that's what you want to believe and so that's what you're saying."
                            ay "Or maybe you're intentionally misleading me."
                            ay "It doesn't matter, I've gotten my answer so that will have to do."
                            ay "You may not realize it, but I still gained something from this."
                            ay "Not necessarily what I wanted but..."
                            ay "Never mind, let's just move on."
                    ay "I said that I would answer any questions you had for me."
                    ay "I intended to keep my word, regardless if I liked your answers or not."
                    ay "You only needed to answer me, that's all."
                    ay "So go right ahead! I'm all ears."
                    mc "Where do I even start?"
                    ay "Ahaha, is that one of your questions?"
                    ay "I'm afraid I can't answer that for you, [player]."
                    ay "You have to decide what you want to know."
                    ay "After all, you do have that liberty at least."
                    mc "That liberty? You make it sound like my freedom is at stake or something."
                    "Ayame smiles mischievously."
                    ay "Maybe it is, who knows?"
                    ay "But we should stop getting sidetracked. I know this period of time is ending soon."
                    ay "Get your questions in while you still can."
                    "This is a good opportunity for me to learn about Ayame before she becomes an official member."
                    "I should really come up with some good questions so that I can do my part to make sure she feels welcome in the club."
                    mc "Let me think..."
                    $ ch16_ay_asked = [False,False,False,False]
                    $ ch16_ay_question_number = 0
                    $ quick_menu = False
                    # Have a timer to flicker the options
                    show screen timer_16_menu_skip("ch16_ay_blinkquestions_1",_layer="timers")
                    menu:
                        "What should I ask her?"
                        "Animam." if not ch16_ay_asked[0]:
                            jump ch16_ay_q1
                        "Requiem." if not ch16_ay_asked[3]:
                            jump ch16_ay_q2
                        "Inveniet." if not ch16_ay_asked[2]:
                            jump ch16_ay_q3
                        "Amisit." if not ch16_ay_asked[1]:
                            jump ch16_ay_q4
                    label ch16_ay_blinkquestions_1:
                    $ quick_menu = True
                    $ _history_list.pop()
                    $ renpy.hide_screen("timer_16_menu_skip",layer="timers")
                    # This is the "questions menu"
                    menu:
                        "What should I ask her?"
                        "Do you have any hobbies?" if not ch16_ay_asked[0]:
                            label ch16_ay_q1:
                            if ch16_ay_question_number == 0:
                                $ ch16_ay_message[0] = True
                                "Ayame flinches as if she was just attacked by something."
                                "I didn't see anything or anyone near her though..."
                                "She shakes it off as if nothing was happened then focuses her gaze on me."
                                ay "Um...where were we? What was it...?"
                            else:
                                "Ayame stares at me for a second as if to process what I just asked."
                                "She looks slightly amused at the question."
                            ay "Hobbies? That's a typical small talk conversation topic, isn't it?"
                            mc "Sorry, did you want me to ask something else?"
                            ay "No, that's perfectly fine!"
                            ay "There's nothing wrong with small talk, and I'm not going to judge you based on the questions you ask."
                            ay "Now...what are my hobbies?"
                            "Ayame taps the table repeatedly for a moment."
                            ay "If you asked my parents, they'd probably say managing the family business."
                            ay "But that's a blatant lie that I'd rather not talk about right now."
                            mc "Then what answer would I get if I asked you?"
                            ay "I do lots of things. These days it seems I get endless free time..."
                            ay "I play a couple of instruments, I do some photography..."
                            ay "I also play a sport but I'm not very good at it."
                            mc "So you're a musician, then?"
                            ay "Calling me a musician is a bit of a stretch, I think."
                            ay "I mainly do that for fun or when I want to learn a song to sing."
                            ay "But trust me when I say you do {i}not{/i} want to hear me sing."
                            mc "Ahaha, I'll take your word for it."
                            ay "As for my photography...I usually take photos of scenery."
                            ay "You know, landscapes, views from the top of tall buildings or just mother nature herself."
                            ay "I'd bring my camera to school to take pictures but I'm not allowed to because it's really expensive."
                            ay "If someone stole it, let's just say it wouldn't be good for anyone."
                            ay "I don't mind that anyway, seeing as there's nothing really exceptional to take a pictures of here."
                            mc "And what about this sport you play?"
                            ay "I'd rather not discuss that. It's pretty embarrassing."
                            ay "You understand, we all keep things hidden."
                            ay "I'll tell you that it involves water, that's all I'm going to say."
                            mc "How come you don't want to talk about your family business?"
                            ay "I hate it. I absolutely hate it."
                            ay "It brings income but I just don't want to become the heir to something like that."
                            mc "And what is {i}that{/i} exactly?"
                            ay "It's a really unethical business involving institutes and industries in the area."
                            ay "One of which includes certain academic places."
                            ay "Let's not discuss this further."
                            ay "I think I've already divulged too much about it anyway..."
                            $ ch16_ay_question_number += 1
                        "How did you become a school leader?" if not ch16_ay_asked[3]:
                            label ch16_ay_q2:
                            if ch16_ay_question_number == 3 and ch16_ay_message[0] and ch16_ay_message[1] and ch16_ay_message[2]:
                                $ ch16_ay_message[3] = True
                                "This time, nothing happens to her."
                                "I was half expecting another jolt or a flinch from her."
                                "Maybe I was just imagining her getting hurt."
                                "If she really was getting hurt, there would be some kind of reaction...right?"
                                ay "Becoming a school leader, huh?"
                            else:
                                ay "How I became a school leader...?"
                            ay "Why? Do you want to know so you can become one?"
                            mc "Not really. I don't have an interest in that kinda thing."
                            mc "I feel like managing people just isn't for me."
                            ay "That's a fair enough reason. It's definitely not a job for everyone."

                            $ ch16_ay_question_number += 1
                        "What's your favorite color?" if not ch16_ay_asked[2]:
                            label ch16_ay_q3:
                            if ch16_ay_question_number == 2 and ch16_ay_message[0] and ch16_ay_message[1]:
                                $ ch16_ay_message[2] = True
                                ay "More small talk conversation? [player], I would have--"
                                "Ayame flinches again as if a jolt of electricity just hit her."
                                "She composes herself and smiles as if nothing just happened."
                                ay "I would have thought you'd come up with better questions."
                            else:
                                ay "My favorite color..."
                                ay "That's a very general question. I can't believe you'd ask something like this."
                                ay "Not that I mind, it's just...there are so many better questions!"
                            mc "You still gotta answer it, don't you?"
                            ay "I suppose I do...well, if you really wanted to know then I guess I can tell you."
                            ay "It's not some kind of big secret anyway."
                            ay "The answer to that is the color purple."
                            ay "I adore the color purple, it reminds me of something dear to me."
                            mc "Do you mind sharing what that is?"
                            ay "It's a sentimental thing so you probably wouldn't get it."
                            ay "The purple reminds me of my past life for some reason."
                            mc "Your past life? What do you mean...?"
                            ay "I mean my childhood life, [player]."
                            ay "I used to have all these toys but I fell in love with this purple one."
                            ay "It was like some kind of cute monster thing."
                            ay "Ever since then, purple has been my favorite color."
                            ay "It's pretty fortunate that the school leadership ribbon is purple."
                            ay "I think it suits me very well."
                            ay "Satisfied with that answer?"
                            mc "I'll be honest, I wasn't expecting that for a favorite color."
                            mc "I would have thought you would have just said a color and be done with it."
                            mc "That's what I would have done."
                            ay "Well, it was one of those small talk questions."
                            ay "I have to talk about it somehow so we can have a decent conversation."
                            mc "Do you still have that purple toy?"
                            ay "..."
                            "Ayame bows her head down and sighs."
                            ay "Unfortunately not. I left it behind in my past life."
                            ay "It will be forever missed."
                            mc "If it was that special to you, why did you willingly leave it behind?"
                            ay "Whoever said I did it willingly...?"
                            "Ayame mumbles something under her breath before lifting her head up again."
                            ay "That's that question done, I hope you liked my answer."
                            $ ch16_ay_question_number += 1
                        "What other clubs did you consider?" if not ch16_ay_asked[1]:
                            label ch16_ay_q4:
                            if ch16_ay_question_number == 1 and ch16_ay_message[0]:
                                $ ch16_ay_message[1] = True
                                "The same scene that I've just seen repeats itself."
                                "Ayame looked like she was in pain for just a moment."
                                "I'm not sure if she realizes it or if she's just hiding it."
                                mc "Ayame, are you--"
                                ay "Ah, ah, ah! I have to answer this question first."
                                ay "Just give a second to think about the answer."
                            else:
                                ay "I have to think about this now..."
                                ay "There was quite a few I looked at."
                            ay "Some clubs tried to get me to join them but I mostly rejected them."
                            ay "There was one club I was seriously thinking about joining."
                            mc "What was it?"
                            ay "Okay, you're going to think I'm crazy when I tell you."
                            ay "So at the very least, promise not to look like you're judging me."
                            mc "I promise I won't judge you."
                            ay "It was a rather recently created club."
                            ay "It's called the Rebirth club and I only heard about it through some kind of rumor."
                            ay "Some students were talking about it, mentioning how ridiculous it was."
                            ay "Naturally, as someone with a curious mind, I wanted to check it out."
                            mc "There was no fliers around the place or anyone asking people to join it?"
                            ay "None at all. It was just a pretty small club."
                            ay "When I went to one of their get togethers, I felt almost entranced."
                            ay "Like this club was calling me."
                            mc "What was the club actually about?"
                            ay "It was about reincarnation."
                            mc "...Reincarnation? A club like that actually got formed?"
                            ay "It's not like the school has tough restrictions on the founding of clubs."
                            mc "Do you believe reincarnation is real, Ayame?"
                            mc "Is that why you decided to seriously consider it."
                            ay "I didn't know what to feel."
                            ay "The members of the club, all four of them, said that they all believe they were reincarnated."
                            ay "They just can't remember their memories."
                            ay "I don't know why but I just felt like I belonged there."
                            mc "What if they were just messing with you?"
                            ay "If they were just messing with me, then I guess I'm a fool."
                            ay "But that doesn't matter now anyway."
                            ay "I'm joining the Literature Club, not this Rebirth thing."
                            mc "That's quite a change. From reincarnation to basically books."
                            mc "I can't imagine what your reason for that is."
                            ay "I don't know myself. I suppose I just felt more of a connection here."
                            ay "Which doesn't make any sense since I barely know all of you."
                            ay "I don't know why I felt so compelled to join the club."
                            ay "But I'm going to see it through, no matter what."
                            mc "I'm glad to hear that, Ayame."
                            mc "I promise we're better than some kind of reincarnation club."
                            ay "We'll see about that, won't we?"
                            $ ch16_ay_question_number += 1
                    ay "Is there anything else you wanted to know?"
                    mc "Well..."
                    if not ch16_ay_asked[0] or ch16_ay_asked[1] or ch16_ay_asked[2] or ch16_ay_asked[3]:
                        jump ch16_ay_blinkquestions_1
                    mc "No, I think that's all I wanted to ask."
                    ay "Only four main questions, eh?"
                    if ch16_ay_message[0] and ch16_ay_message[1] and ch16_ay_message[2] and ch16_ay_message[3]:
                        $ ch16_ay_level -= 5
                        if ch16_ay_level < 0:
                            $ ch16_ay_level = 0
                        ay "That's one more than I asked, not that I'm--"
                        ay "AAAAAAAAAAAAAAAHHHH!!!"
                        "Ayame suddenly yells out in pain."
                        show ayame 1a:
                            1.3
                            easeout_cubic 0.5 yoffset 300
                        $ pause(1.55)
                        play sound fall
                        $ pause(0.25)
                        hide ayame
                        $ pause(0.25)
                        scene black
                        "She falls to the floor and seems to be shaking."
                        "The whole library all stop and turn towards the source of the noise."
                        "They look at me as if I'm the one responsible for doing this to her."
                        mc "A-Ayame, are you okay?"
                        "She doesn't seem to be hurt, at least physically."
                        "I think she's under some kind of shock because she won't stop hyperventilating."
                        "The question is why did this happen all of a sudden?"
                        mc "Can you say something, Ayame?"
                        mc "Was it something that I said...?"
                        "Ayame's eyes slowly turn toward me then back at the floor."
                        "The whole time she doesn't say a word but just keeps breathing loudly."
                        "Some of the students approach me, wondering what is going on."
                        "I try to explain to them what happened."
                        mc "She just suddenly yelled out like that in the middle of saying something."
                        mc "I honestly have no idea what happened."
                        "Student 1" "\"Can we help her or something?\""
                        "Student 2" "\"Yeah, let's take her to the nurse's office.\""
                        "Student 2" "\"I'm sure our president will understand if we're a little delayed.\""
                        "The two students try to reach out to Ayame but she slaps their hands away."
                        "What the hell is wrong with her right now?"
                        "I can't help but feel guilty about the whole thing."
                        "I was the last one to speak to her, after all."
                        "I must have said something that really upset her."
                        "But if I did...then why was there such a delayed reaction to it all?"
                        "The two students try to pick her up again but she once again flicks their hands away."
                        "Student 1" "\"I don't think is going to work. She clearly doesn't want help.\""
                        "Student 2" "\"Wait a minute...isn't this Ayame, the school leader?\""
                        "Student 2" "\"Look, she even has the purple ribbon and everything!\""
                        "Student 1" "\"You're right! We have to find a way to help her.\""
                        "Student 1" "\"I don't know what happened here but maybe she trusts you enough.\""
                        "The student directs that towards me."
                        mc "Me? For all I know, I was the one who caused it."
                        mc "I'm just not sure exactly how or what caused it..."
                        "Student 2" "\"Then all the more reason for you to help, come on.\""
                        mc "Alright...this can only end badly."
                        "As I move to reach to grab Ayame, she stares into my eyes."
                        "She then stops hyperventilating and looks around wildly."
                        ay "That won't be necessary, thank you."
                        "Ayame stops shaking and quickly gets up from the ground."
                        scene bg library
                        show ayame 1a zorder 2 at t11
                        with dissolve_scene_half
                        ay "I'm fine now. I apologize for the sudden yelling."
                        "The two students look at each other and shrug."
                        "Student 1" "\"You seem fine now but maybe you should still go see the nurse.\""
                        ay "I assure you, I'm perfectly fine. It was just a moment of weakness."
                        ay "It won't happen again."
                        "Student 2" "\"If you're completely sure...\""
                        ay "I am. Thank you for your concern."
                        "The students leave and after a few seconds everything is as it was before."
                        "It's like that scene never happened."
                        mc "So do you mind telling me what happened?"
                        mc "I was worried for you there, Ayame."
                        ay "You know, I wish I could tell you."
                        ay "I have no idea why I reacted the way I did."
                        ay "You don't have to worry about it though, I promise it won't happen again."
                        mc "What it something I said to you? One of the responses to your questions maybe?"
                        ay "Do you really think words are enough to do that to me?"
                        mc "Well, I don't know. Some people react differently to different things."
                        ay "Like I said, I'm fine. In fact, I'm better than fine."
                        ay "I feel like I've gained a new sort of freedom."
                        mc "In what way does a panic attack give you a new sort of freedom?"
                        ay "That's not what I meant."
                        ay "Anyway, I hope I could answer all of your questions properly."
                        ay "I'm kinda surprised you didn't have more."
                        ay "You barely know me but the opposite is true for you."
                        mc "Are you saying you know a lot about me?"
                        mc "But I didn't really explain much about myself."
                        ay "There were things in Yuri's journal but I also found out some things from what you just told me."
                        mc "I hope you know there's more to me than I look."
                        mc "You can't possibly know that much about me from just reading Yuri's journal and from what I said."
                        ay "It's not just you, I know a lot about other people in the club."
                        mc "That sounds...creepy and impressive."
                        ay "Creepy {i}and{/i} impressive? That's a really different reaction to what I was expecting."
                        mc "I don't know what you know but you sound pretty confident."
                        mc "It's just hard to believe what you're saying."
                        ay "You'd be surprised at my deduction skills..."
                        ay "But that's a matter for another time."
                        "Ayame stands up and offers her hand."
                        "She gives me a very wide smile but I'm unsure as to why."
                        "I still think I'm the cause of her freaking out."
                        ay "Well? Ever heard of a handshake before or not?"
                        mc "O-Oh, right...sorry."
                        "I stand up and take her hand and she places a firm grip on mine before shaking it."
                        ay "Handshaking is a thing that's engrained into my mind."
                        ay "My parents got me into it, before you ask."
                        ay "It's just a habit I got into it and I guess it works better than simply waving."
                        ay "It feels more personal, don't you think so?"
                        mc "I guess so..."
                        ay "Something on your mind?"
                        mc "Sort of. I'm just thinking about what just happened."
                        mc "You know, how you freaked out."
                        ay "Think about it all you want."
                        ay "There's no rational way to explain what happened anyway."
                        ay "Now, if there's nothing else...I won't take up any more of your time."
                        ay "I'll be seeing you again soon, [player]."
                        "Ayame withdraws her hand and walks away with a sort of stride."
                        show ayame at thide
                        hide ayame
                        "Like she really needed to get somewhere quickly."
                        "Even though she said it wasn't me, I can't help but feel guilty about the freak out."
                        "I mean...who else could be responsible for it?"
                        "I was the only one there talking to her at the time."
                    else:
                        ay "That's one more than I asked, not that I'm complaining."
                        ay "in fact, I'm surprised you didn't have {i}more{/i} questions."
                        ay "You barely know a thing about me but I've got {i}you{/i} all scoped out."
                        mc "You've got me scoped out...?"
                        ay "Yeah, it means I know a lot of things about you already."
                        ay "From what I read in Yuri's journal and from what you've told me just now."
                        mc "There's more to me than you might know, Ayame."
                        mc "I may not look it, but I do have some other things that aren't too obvious."
                        ay "Oh? And how do you know I don't know about those?"
                        ay "I didn't get {i}everything{/i} from Yuri's journal, you know."
                        ay "There are some things that I found out myself."
                        ay "Not just about you, but other people too including those from the club."
                        mc "Isn't that...I don't know, kinda creepy?"
                        ay "I'm not stalking you guys or anything!"
                        ay "I just happen to have the skills of one."
                        mc "Right...I'll take that as some sort of joke."
                        ay "Anyway, thank you for your time."
                        ay "I probably won't bother you for the rest of the day until your club meeting."
                        ay "I'll be sure to bring the gifts I bought for you all!"
                        mc "I can't wait, Ayame!"
                        mc "For you to come to the club that is, not the gifts."
                        ay "Nice save, [player]."
                        "Ayame stands up and happily offers me her hand."
                        "I stare at it for a moment then turn my attention to her."
                        ay "It's called a handshake, [player]. Ever heard of one?"
                        mc "No, I have...it's just..."
                        "I stand up and take her hand and she places a tight grip on mine before shaking it."
                        mc "Why?"
                        ay "It is kinda odd, isn't it? I guess it's just a habit I got into."
                        ay "You can blame my parents for that."
                        ay "If there was nothing else, I guess I'll see you soon."
                        "Ayame withdraws her hand and begins to walk away."
                        show ayame at thide
                        hide ayame
                        "She seemed to be lost in thought as she exited the room."
                        "Did I really impact her that much?"
                "Deny her.":
                    $ ch16_ay_level += 2
                    mc "I'm sorry Ayame but I can't help you."
                    mc "Even if I did know what you're talking about, which I don't, I wouldn't know what to say."
                    mc "If you really want to know, maybe you can ask Sayori or find out for yourself when you join."
                    ay "This is not good enough. I need to know this information, now."
                    ay "I can't wait until I know enough about it myself!"
                    ay "It could be too late by then."
                    mc "I'm sorry Ayame, it's just that--"
                    ay "No. It's fine."
                    ay "You answered my first two questions, that will have to do."
                    ay "I'll have to find out the rest of it myself in the time we have left."
                    "Ayame stands up and offers her hand."
                    ay "You weren't as useful as I thought you would be."
                    ay "But at least you gave me something."
                    ay "So thanks for that, at least."
                    "I stand up and take her hand as she gives me a handshake."
                    "I'm kind of confused why she would do something like this."
                    ay "Oh, you've got that look on your face."
                    ay "Sorry, I'm just used to giving people handshakes when I get something out of them."
                    ay "My parents got me used to it..."
                    mc "It's fine, I guess. Sorry that I can't really tell you more."
                    ay "I really thought you could have answered my last question."
                    ay "Since you didn't, I'm just going to leave and figure something out."
                    mc "I don't get an opportunity to ask you anything?"
                    ay "No."
                    show ayame at thide
                    hide ayame
                    "Ayame leaves without saying another word."
                    "She looked like she was thinking about something as she left."
                    "Was it really that crucial that I tell her what I know?"
                    "I didn't even know what she was talking about but she seemed so certain that I did."
        "As I sit back down, I come to a realization."
        "Ayame doesn't know where the meeting is, especially since it's in a different room today."
        "Maybe I should have said something before she left."
        "I shouldn't be thinking about it too much."
        "I still have a script to read, after all."
        scene bg portraitshop_school with wipeleft_scene
    else:
        scene bg portraitshop_school with wipeleft_scene
        play music t3
    "It's time to go to rehearsals for our play in a couple of hours."
    "I still find it hard to believe that we're doing this."
    "I don't know if this time we have is enough."
    "Sayori seemed confident that we'd do fine, so I guess I'll hold on to that hope."
    "As I enter the room, I can see all the costumes and props all lined up on some of the desks."
    "I really didn't expect this much stuff for a play we're not even sure is going to go well."
    "Sayori really went all out..."
    show sayori 1a zorder 2 at t11
    s "[player], you're the first one here!"
    s 1q "I hope you're as ready as I am because this play is going to be so much fun!"
    mc "I don't think anyone is as ready as you are, Sayori."
    mc "I think you're probably the most excited about this whole thing."
    s 1l "Are you telling me you aren't?"
    mc "I wouldn't say excited is the right word, but I'm ready to get this over with."
    mc "I'll put all I've got into this, Sayori. You can trust me on that."
    s 2d "I hope you do, this play is going to be incredible!"
    s "I'm going to end it all on a high note."
    mc "You mean {i}we{/i}, right?"
    mc "As in {i}we're{/i} going to end it on a high note."
    show sayori 1k
    "Sayori ignores my correction and instead moves towards the door."
    s 1c "I think I see Yuri coming!"
    "Sayori opens the door and Yuri steps inside the room."
    show sayori zorder 2 at t21
    show yuri 1a zorder 2 at t22
    "She looks around and notices the assortment of stuff lying around."
    show sayori zorder 2 at t21
    show yuri 1b zorder 3 at f22
    y "I have to say, I was not expecting {i}this{/i} much stuff in that box [player] brought in."
    y "You've really dedicated yourself to this one play, haven't you Sayori?"
    show sayori 1d zorder 3 at f21
    show yuri zorder 2 at t22
    s "It's for you guys, after all."
    s "I'd do anything to make sure you all got what you deserved."
    show sayori zorder 2 at t21
    show yuri 1f zorder 3 at f22
    y "Even looking over the script, it seems so well made."
    y "And you managed to do all of that in such short notice."
    y 2pg "It kind of makes me believe you're some sort of miracle worker."
    show sayori 1c zorder 3 at f21
    show yuri zorder 2 at t22
    s "Like you said, I've dedicated myself to this play."
    s 1a "And I want it to be fun for everyone."
    show sayori zorder 2 at t31
    show yuri zorder 2 at t32
    show natsuki 1e zorder 3 at f33
    n "How did you even do that?"
    "Natsuki suddenly bursts into the room."
    n "If I could do my assignments all in the last minute like you can write a script..."
    n "Let's just say, my life would be a lot easier."
    show sayori 2l zorder 3 at f31
    show natsuki zorder 2 at t33
    s "H-Hey, the script wasn't really last minute."
    s "I had a couple of days to do it, which is plenty of time."
    show yuri 2ph zorder 3 at f32
    y "That seems rather last minute to me especially considering how long it would usually take to write a script."
    y "Not like I would know how long a script actually takes to write, I've never done it before."
    y "Though I'd imagine knowing the all of the source material helps."
    show sayori 4d zorder 3 at f31
    show yuri zorder 2 at t32
    s "A-Anyway, I'm glad you remembered we were meeting here, Natsuki."
    show sayori zorder 2 at t31
    show natsuki 1c zorder 3 at f33
    n "Why wouldn't I remember?"
    n "It was a pretty weird thing to suddenly tell us this morning."
    n 2e "Is everyone here already?"
    show sayori 4c zorder 3 at f31
    show natsuki zorder 2 at t33
    s "Not yet! We're still waiting on Monika."
    show sayori zorder 2 at t31
    mc "Don't forget Ayame. She said she was coming to this, wasn't she?"
    show sayori 4e zorder 3 at f31
    s "Right...I can't wait to meet her for the first time."
    show sayori zorder 2 at t31
    show yuri 3pc zorder 3 at f32
    y "I'm sure you two will become fast friends."
    y "She's quite eccentric but I think that's a good thing in this situation."
    show yuri zorder 2 at t32
    show natsuki 4e zorder 3 at f33
    n "Ayame isn't what we should be concerned about right now."
    "Natsuki looks out the door."
    n 4f "Does anyone know where Monika is?"
    n "We can't exactly start rehearsing without her."
    show sayori 3m zorder 3 at f31
    show natsuki zorder 2 at t33
    s "I have no idea, I thought she'd be here by now."
    show sayori zorder 2 at t31
    mc "Did you tell her we would be here?"
    mc "She wasn't with us this morning so maybe she didn't know."
    show sayori 3o zorder 3 at f31
    s "Oh..."
    "Sayori scratches her head then looks like she's come to a realization."
    s 5b "Ehehe, I guess I forgot to tell her."
    s "Does one of you want to go there and get her?"
    show sayori zorder 2 at t31
    show natsuki 1g zorder 3 at hf33
    n "Sayori, are you serious?!"
    n "How did you forget something like that?"
    show sayori 1h zorder 3 at f31
    show natsuki zorder 2 at t33
    s "S-Sorry, I haven't been able to speak to her all day."
    s "The only time I could was during lunch and..."
    if monika_type == 0 or (monika_type == 1 and ch12_markov_agree):
        s "I guess I forgot to mention it."
    else:
        s "I didn't see her."
    show sayori zorder 2 at t31
    show yuri 3pa zorder 3 at f32
    y "I can only assume she'd still be at the clubroom. If that's the case, then I wouldn't mind getting her."
    y "I'm not sure about Natsuki but I left my things in the clubroom anyway so if she's there, then she can help carry it over."
    show yuri zorder 2 at t32
    show natsuki 2c zorder 3 at f33
    n "Actually, now that you mention it...I did leave my cupcakes there."
    n "Can you get my things for me? I don't really want to go all the way there."
    show natsuki zorder 2 at t33
    "Yuri gives Natsuki an affirming nod."
    show sayori 1a zorder 3 at f31
    s "I guess this all works out then!"
    s "Do you want to bring [player] along in case you need [player_reflexive]?"
    show sayori zorder 2 at t31
    show yuri 1e zorder 3 at f32
    y "I don't think that will be necessary, there's not that much to bring."
    y 1f "But if you want to come along, you're more than welcome to, [player]."
    show yuri zorder 2 at t32
    menu:
        "Should I go with Yuri to get Monika?"
        "Yes.":
            $ ch16_getmonika = True
            $ ch16_ay_level += 1
            mc "I'll go just in case you need me."
            mc "Better safe than sorry, right?"
            mc "Besides, it's not like we can rehearse with just three of us here."
            show sayori 1q zorder 3 at f31
            s "If that's what you wanna do, go ahead!"
            s "We'll manage without the two of you here."
            s 1d "It's not like we can do anything here without all four of us anyway."
            show sayori zorder 2 at t31
            show natsuki 5g zorder 3 at f33
            n "Whatever, just don't take too long."
            show natsuki zorder 2 at t33
            "Yuri turns towards me."
            show yuri 2pf zorder 3 at f32
            y "Shall we go now then? The sooner we get this done, the better."
            show yuri zorder 2 at t32
            mc "After you."
            scene bg corridor
            show yuri 1i zorder 2 at t11
            with wipeleft_scene
            "Yuri and I make our way to the clubroom at a pretty fast pace."
            "She didn't seem like she wanted to waste any time."
            "As we made our way here, we noticed a lot of rooms filled with people."
            "Most of them looked like they were discussing something pretty important."
            "They were probably talking about Inauguration Day if I had to take a guess."
            "When we eventually arrive outside the clubroom, no one seems to be here."
            "There are people in the rooms in the same corridor but no one in our clubroom."
            mc "It looks like she isn't here."
            y 1f "That's unfortunate. Where do you suppose she is then?"
            mc "I saw her this morning in the gym, I think she was meant to be practicing piano."
            mc "It's possibly she could be there."
            y 3pe "Maybe we should split up. One of us should stay here in case she comes back and the other can get her at the gym."
            y "If we don't find her within...say ten minutes, we just head back to the club."
            mc "Alright, that sounds like--"
            "Suddenly, I notice the door of the closet open in the clubroom."
            "Nobody steps outside but it definitely wasn't open when we got here."
            y 3pf "What is it? Do you have a different idea?"
            mc "No, the closet is open in the clubroom. It wasn't when we got here."
            mc "I think someone is inside."
            "Yuri peers into the room, looking for this person that could be in there."
            y 2pg "I don't see anyone in there."
            mc "There has to be someone in there, right?"
            mc "There's no other reason the closet should be open."
            y 2ph "I suppose that's a valid argument."
            y "If the door is locked, then it was probably just left open by the class that was there last."
            "Yuri turns the door handle to the club, expecting it to be locked."
            "To her surprise, it opens."
            mc "Monika is probably inside the closet."
            y 3pf "Well, there's only one way to find out."
            scene bg club_day
            show yuri 3pf zorder 2 at t11
            with wipeleft_scene
            "Yuri and I step into the clubroom. Looking around, we don't see Monika anywhere."
            "If she's here, she must be in the closet."
            y "Monika? Hello, are you in here?"
            y "The meeting is in a different room."
            mc "Sayori was supposed to tell you but I guess she forgot."
            "There's no response to either of the things we said."
            y 3pe "I don't think she's here. She would have responded to what we said."
            mc "Yeah, let's just take the things from the closet and leave."
            show monika 3a zorder 1 at t21
            m "So what are you two up to?"
            show yuri 3pn zorder 3 at hf22
            y "Ah!"
            "Monika appears from behind us, causing Yuri to jump."
            y 3pq "M-Monika, where did you come from?"
            show monika 3c zorder 3 at f21
            show yuri zorder 2 at t22
            m "I was outside the clubroom looking for you guys."
            m "I went in here looking for all of you but none of you were in here."
            show monika zorder 2 at t21
            mc "Weren't you just inside? How did you suddenly get outside?"
            show monika 1d zorder 3 at f21
            m "What are you talking about? I was outside when you guys walked in."
            show monika zorder 2 at t21
            show yuri 2ph zorder 3 at f22
            y "But [player] said the closet was closed when we walked past."
            y "Then it was suddenly opened when [player_personal] looked again."
            show monika 2b zorder 3 at f21
            show yuri zorder 2 at t22
            m "Oh, that's probably because I was in here before."
            m "I saw what I can only assume was Natsuki's and your things."
            m "I guess I didn't close the closet properly and it just opened by itself."
            show monika zorder 2 at t21
            show yuri 2pg zorder 3 at f22
            y "That does make sense, I suppose."
            show monika 2c zorder 3 at f21
            show yuri zorder 2 at t22
            m "And what about you two? How come you're the only ones here?"
            m "We still have to do our rehearsals, you know."
            show monika zorder 2 at t21
            mc "Sayori didn't get to tell you, did she?"
            show monika 2d zorder 3 at f21
            m "Tell me what exactly? Am I missing something?"
            show monika zorder 2 at t21
            show yuri 1f zorder 3 at f22
            y "We moved the meeting to another room. It's in a more secluded spot."
            y "Sayori thought it would be easier to rehearse in seeing as less people would be seeing us."
            y 1e "We came here to get our stuff and look for you."
            show monika 2e zorder 3 at f21
            show yuri zorder 2 at t22
            if monika_type == 0 or (monika_type == 1 and ch12_markov_agree):
                m "I actually saw Sayori at lunch. She didn't mention anything."
            else:
                m "She probably should have told me this morning."
            m "But whatever, what's done is done."
            m 2c "So what room are we actually practicing in?"
            show monika zorder 2 at t21
            show yuri 1u zorder 3 at f22
            y "I don't know what classroom exactly but I do know how to get there."
            y "Before that, we should grab the things in the closet."
            y 1f "That's the reason [player] is here, after all."
            y "[cPlayer_personal] was meant to help in case you weren't here."
            show monika 4a zorder 3 at f21
            show yuri zorder 2 at t22
            m "Okay, you two! Let's get that stuff and get to rehearsals."
            m "Ayame is probably waiting for us right now too."
            show monika zorder 2 at t21
            show yuri 2pf zorder 3 at f22
            y "Right...Ayame is coming to the meeting today. I wonder where she is."
            y "I thought she would have ended up here seeing as no one told her we'd be moving rooms for today."
            show yuri zorder 2 at t22
            mc "Maybe she forgot to come or has some other matters to attend to."
            mc "She is a leader, after all."
            show monika 4c zorder 3 at f21
            m "If she's not here, then there's no use waiting for her."
            m "I know we don't have a lot of time for rehearsals so we have to make use of the time we do have."
            m 3b "Let's just grab the stuff and leave already."
            show monika zorder 2 at t21
            mc "Monika has a point. Let's get going."
            scene bg corridor
            show monika 1a zorder 2 at t21
            show yuri 1i zorder 2 at t22
            with wipeleft_scene
            "There was three bags in the closet. Two of them belonged to Yuri and one to Natsuki."
            "I'm carrying one of the bags Yuri brought and Monika is carrying Natsuki's."
            "To be honest, I don't think I was really needed after all."
            "The bag Yuri gave me was pretty light and I can only assume the other one was too."
            "She probably just wanted to give me something to do so I wouldn't feel useless."
            show monika zorder 3 at f21
            m "It's a shame we couldn't get a better space for practice."
            m "Being in a classroom means we're limited in the space we can use."
            show monika zorder 2 at t21
            show yuri 1f zorder 3 at f22
            y "Because of today, there really isn't a lot of free space."
            y "It's like there's an extra period of school because of how many rooms are being used."
            y 1h "In fact, there's probably more rooms being used than there is during normal school hours."
            show yuri zorder 2 at t22
            mc "How come? Since it's the end of school I would have thought there would be less classes."
            show yuri 1e zorder 3 at f22
            y "That's usually the case but today is a special occasion."
            y "The amount of people in a room is less because it's a club."
            y "Most clubs don't have as many members as there are students in a class."
            y 1g "Some clubs are even using more than one room."
            y 1h "Of course, there are some exceptions."
            show monika 1c zorder 3 at f21
            show yuri zorder 2 at t22
            m "I've only just noticed where we're heading."
            m "We're not going to {i}those{/i} classrooms, are we?"
            show monika zorder 2 at t21
            show yuri 2ps zorder 3 at f22
            y "You're going to have to be more specific, Monika."
            y "I'm not sure what you mean by {i}those{/i} classrooms."
            show monika 1e zorder 3 at f21
            show yuri zorder 2 at t22
            m "The old senior classrooms, Yuri. The ones that aren't really used much."
            m "More than half of the classrooms aren't even used for club space."
            show monika zorder 2 at t21
            mc "Do you know the reason that's the case?"
            mc "The classroom we went to this morning seemed perfectly normal."
            if ch15_s_together:
                "Except the fact it was actually that shop Sayori and I went to yesterday."
            mc "It seems like a waste of the school's resources to just have them there."
            show monika 1c zorder 3 at f21
            m "That's the thing, it is a waste."
            m "The school doesn't have enough students anymore."
            m 1d "It seems to be losing some every couple of years but not gaining anymore."
            m "If I remember correctly, we've been losing at four students every year."
            show monika zorder 2 at t21
            show yuri 2pt zorder 3 at f22
            y "But that shouldn't be the case."
            y "The school should be gaining a steady influx of students as the people in their senior year leave."
            y 2pv "In fact, more students should be coming in than out."
            "Yuri thinks for a moment before coming to a sudden realization."
            y 2pr "W-Wait a second, how do you even know this information?"
            y "Is there some sort of school history we aren't aware about?"
            show monika zorder 3 at f21
            show yuri zorder 2 at t22
            if monika_type == 0:
                m 1n "Oh, you know what? I think I've said too much."
                m "Just forget I said anything. Let's just get to this classroom already."
                show monika zorder 2 at t21
                show yuri 2pt zorder 3 at f22
                y "Are you hiding something from us we should know about?"
                y "If it has something to do with the school or the club then we should know."
                show monika 1f zorder 3 at f21
                show yuri zorder 2 at t22
                m "No, it has nothing to do with the club."
                m 1e "You shouldn't worry about it."
                show monika zorder 2 at t21
                show yuri zorder 3 at f22
                y "Are you sure you don't want to tell us?"
                y "If keeping this information to yourself is hurting you then--"
                show monika zorder 3 at f21
                show yuri zorder 2 at t22
                m "It's fine, Yuri. I shouldn't have said anything to begin with."
                m "Can we just get on with it?"
                show monika zorder 2 at t21
                mc "I think it's best if we just leave it for now, Yuri."
                show yuri zorder 3 at f22
                y "Yes...you're probably right about that."
                y "That doesn't mean I don't want to know anymore though..."
            else:
                m 1a "Do you really want to know, Yuri? I can definitely give you that information."
                "Monika stops moving, causing Yuri and I to do the same."
                m 1c "It's going to cost you...well, nothing."
                m 1b "But you'll be completely different after you've learned this information."
                show monika zorder 2 at t21
                show yuri 2pf zorder 3 at f22
                y "Completely different? In what way?"
                y "Learning something like that isn't going to cause me to change."
                y 2ph "In fact, I'm rather interested in this information."
                y "If what you're saying is true then the school has been operating at a loss of students for decades."
                show monika 1e zorder 3 at f21
                show yuri zorder 2 at t22
                m "You're absolutely sure, Yuri?"
                m "This won't work if I force you into it so know that I'm giving you this chance."
                m 2a "You have to be willing."
                show monika zorder 2 at t21
                "For some reason, the way Monika said that made me feel a chill."
                if yuri_date and not persistent.markov_agreed:
                    mc "Can we take a moment to talk about this?"
                    mc "I just want to talk to Yuri for a bit."
                    show monika 2h
                    "Monika looks at me with a strange look then shrugs."
                    show monika 2j zorder 3 at f21
                    m "Of course! Take all the time you need, you little lovebirds~"
                    m "Though maybe not literally, we still have to get back to rehearsals, you know."
                    show monika at thide
                    hide monika
                    show yuri zorder 2 at t11
                    "Monika goes to another part of the clubroom where she can't hear us."
                    "She takes out her phone and starts tapping away at the screen."
                    "Just to be safe, I pull Yuri aside and lower my voice so that Monika can't hear."
                    mc "Yuri, I don't like the sound of this."
                    mc "I know it's probably nothing but you should be careful."
                    y 3pf "But [player], aren't you curious too?"
                    y "Why would the school be working like this...?"
                    mc "I am but I don't know if it's worth it."
                    mc "It's just the way Monika has been lately...I don't know."
                    y 3ph "I'll listen to you over my own feelings on this, [player]."
                    y "You seem genuinely concerned about this."
                    y "So if you don't think I should do it, then I won't."
                    menu:
                        mc "Yuri, you should..."
                        "Trust your own feelings.":
                            $ ch16_yuri_choice = True
                            mc "If that's really what you want to do, then I shouldn't stop you."
                            mc "I guess I'm just being a little overprotective."
                            mc "I just want you to be careful, Yuri."
                            y 3pa "Thank you, [player]. I do appreciate that."
                            y "You don't have anything to worry about though."
                            y "I'm not going to do anything stupid. If things sound bad, I'll stop."
                            "Yuri takes my hands and holds it in hers."
                            y 3ps "I promise."
                            y "Besides, it's just a story. That's hardly going to change who I am as a person."
                            y "Not when I have you around."
                            mc "If you're completely sure about this, go ahead."
                            mc "I'm just not entirely sure why Monika would say it like that."
                            mc "It just gave me an odd feeling, that's all."
                            y 2po "I don't know why but I really want to know this information."
                            y "It's almost like a compulsion. Like I just have to know."
                            mc "You sound set on it, Yuri. I hope you learn all you want to know."
                        "Stay away from Monika.":
                            $ ch16_yuri_choice = False
                            mc "With what you said to me before, I think you should stay away from her."
                            mc "I've started noticing the weird things she's doing too."
                            mc "It's nothing too out of the ordinary but she's changed who she is."
                            mc "I can definitely tell now."
                            y 2pt "So you've finally noticed it, [player]?"
                            y "I was beginning to think you hadn't and so I kinda gave up talking about it."
                            mc "I just want to protect you, Yuri. You're really precious to me."
                            mc "I don't want anything bad to happen to you."
                            show yuri 4pe
                            "Yuri's face turns a bright red."
                            y "T-That's very thoughtful of you, [player]."
                            y 4pa "I'll admit knowing the information is oddly tempting to me. It's like there's some kind of force making me want to read it."
                            y "I'm glad you're here, you're making me listen to reason."
                            mc "I wouldn't say I'm the best person for this kinda thing."
                            mc "It's just the way Monika said it...it gave me an odd feeling."
                            y 3pa "If that's the case, then I don't need to know."
                            y "I'll trust your word over my own desires, [player]."
                            mc "You don't need to do that all the time. I'm just concerned right now."
                    "Yuri approaches Monika and gets her attention."
                    show monika 1c zorder 3 at f21
                    show yuri zorder 2 at t22
                else:
                    $ ch16_yuri_choice = True
                    show yuri 2pq zorder 3 at f22
                    y "Why are you saying it like it's so ominous?"
                    y "It's just the history of the school, isn't it?"
                    y 3pv "It would probably be well known to the parents bringing their children here."
                    show monika 1a zorder 3 at f21
                    show yuri zorder 2 at t22
                    m "I have my reasons for that, Yuri."
                    m "Just like you should have yours for wanting to learn this information."
                    m 1e "Remember, the decision is completely up to you."
                    m "I don't want to force you to do anything you don't want to."
                    show monika zorder 2 at t21
                    show yuri 1g zorder 3 at f22
                    y "I'd like to take a moment to think about it."
                    show monika 1j zorder 3 at f21
                    show yuri zorder 2 at t22
                    m "Of course, take all the time you need."
                    m 1l "Though maybe not, since we do have a rehearsal to get to."
                    show monika zorder 2 at t21
                    "Yuri ponders for a moment then looks at me with an expectant look."
                    show yuri 2pf zorder 3 at f22
                    y "Well, what do you think [player]? I want to get your opinion."
                    y "Do you think I should do it?"
                    show yuri zorder 2 at t22
                    mc "Well, if you ask me--"
                    show monika 1h zorder 3 at f21
                    m "Why are you asking [player_reflexive]?"
                    m 2i "It's not any of [player_possessive] business what choice you make."
                    m "Or are you saying you aren't independent enough to make the decision yourself?"
                    m 2h "Come on, Yuri. It's really not that hard, is it?"
                    show monika zorder 2 at t21
                    show yuri 3pp zorder 3 at f22
                    y "T-That's not it all! I was just..."
                    y 3po "N-Never mind, I'll decide myself. Just give me a minute."
                    show yuri zorder 2 at t22
                    "Yuri paces around the room. She's taking this pretty seriously."
                    "What's the worst that could happen anyway? It's just a piece of information."
                    "That's hardly going to change who Yuri is, is it?"
                    show monika zorder 3 at f21
                m 2c "So, have you made up your mind?"
                show monika zorder 2 at t21
                show yuri zorder 3 at f22
                if ch16_yuri_choice:
                    y 3pe "I've decided I want to learn this information."
                    y "My curiosity is getting the better of me for some reason."
                    y "So just say what you have to say, Monika."
                    y "Or should [player] take this ridiculous agreement to hear it too?"
                    show monika 2a zorder 3 at f21
                    show yuri zorder 2 at t22
                    m "No, [player] is different to you, Yuri."
                    m "[cPlayer_reflexive] knowing this information won't change [player_reflexive] at all."
                    m 4b "But it will change you, Yuri. Just know that you've done this of your own free will."
                    show monika zorder 2 at t21
                    show yuri 2pr zorder 3 at f22
                    y "Just get on with it, Monika."
                    show monika 4a zorder 3 at f21
                    show yuri zorder 2 at t22
                    m "As you wish, Yuri. Now, where to begin?"
                    m "Why not at the beginning, the founding of this school?"
                    m 4b "This school was founded over a hundred years ago, possibly more."
                    m "Its founding was sponsored by the most influential families in the area, so it became very popular."
                    m "Back then, there were a lot more students going to this school."
                    m 4c "I'd say at least five hundred of them."
                    show monika zorder 2 at t21
                    show yuri 1f zorder 3 at f22
                    y "Five hundred? That's an oddly specific number."
                    y "How can you be so certain about the student body count back then, Monika?"
                    y 1g "It's not like you have access to the records...do you?"
                    show monika 2e zorder 3 at f21
                    show yuri zorder 2 at t22
                    m "Call it an educated guess."
                    m "If I knew the exact year it was founded, I could give you a more accurate number."
                    show monika zorder 2 at t21
                    mc "What does the year--"
                    show monika 2h zorder 3 at f21
                    m "Silence, [player]. You'll have your time."
                    m 1i "Right now, all you have to do is watch and listen."
                    m "Watch as Yuri descends into madness again."
                    m 1a "Do you know what will happen when you hear the end of it, Yuri?"
                    show monika zorder 2 at t21
                    show yuri 2ph zorder 3 at f22
                    y "I don't know. You keep saying I'll change."
                    y 2pr "But I'm more resolved than you think, Monika."
                    y "Hearing the end of some possibly made up tale isn't going to change who I am."
                    show monika 1j zorder 3 at f21
                    show yuri zorder 2 at t22
                    m "Ahaha, we'll see about that, Yuri."
                    show monika zorder 2 at t21
                    show yuri 2pq zorder 3 at f22
                    y "Why are you being so ominous about this?"
                    y "I'm starting to feel like you're just playing some kind of cruel joke."
                    y 3pt "Y-You're not out to harm me, are you...?"
                    "Yuri takes a step away from Monika."
                    y "Maybe [player]--"
                    show monika 1h zorder 3 at f21
                    show yuri zorder 2 at t22
                    m "[player] isn't going to save you, Yuri. In fact, [player_personal] won't say another word."
                    m "You've already cast the die, now you must see it through to the end."
                    m 1i "For by the end of it, you'll see things my way."
                    m "Now, let me finish what I was saying."
                    m "Every year since its founding, five students would disappear from the school."
                    m 1h "Without fail, it was always five students."
                    m "The student body count has always stayed the same except for that constant five student drop."
                    m "No one, and I mean absolutely no one knows why."
                    m "Except me."
                    m 2i "The cause, you might ask, is this vicious cycle that threatens to destroy everyone."
                    m "This cycle that will never stop until every last person has ceased to exist."
                    m "This cycle that I've been trapped in for what seems like forever."
                    m 2h "I'm the only one who can stop it, Yuri."
                    m "Do you understand? Without me, we're all doomed."
                    $ gtext = glitchtext(30)
                    m "Without [gtext]{nw}"
                    m 2d "Yuri."
                    show monika zorder 2 at t21
                    "I don't understand what just happened."
                    "Monika told a pretty strange story that didn't sound {i}that{/i} convincing."
                    "But I felt something weird come from nowhere."
                    "I look at Yuri and her gaze seems to be fixed on Monika."
                    "She's completely expressionless. What happened to her?"
                    show yuri 3py6 zorder 3 at f22
                    y "..."
                    y "You are right. We must do something about it."
                    show monika 1c zorder 3 at f21
                    show yuri zorder 2 at t22
                    m "You know, I'm surprised that actually worked."
                    m "I suppose that story was enough to make Yuri give her full attention."
                    m 1a "Now she's completely helpless again."
                    m "All that effort to try to fix her, only for her to end up like this."
                    m 1d "What a waste of my time."
                    m "She was already a prime candidate before but you just had to meddle in all of this."
                    m "But I suppose there's no use complaining about it now."
                    m 1c "I've already fixed this problem that shouldn't have been a problem to begin with."
                    m "You'll obey me when the time comes, now won't you?"
                    show monika zorder 2 at t21
                    show yuri 3pk zorder 3 at f22
                    y "As you say."
                    show monika 1j zorder 3 at f21
                    show yuri zorder 2 at t22
                    m "It's so exciting to think that a little world manipulation can get something like that done."
                    m "Although it wasn't the most efficient way...no, I don't have that kind of power yet."
                    m "I was only able to do it through some roundabout way."
                    m 1a "But soon..."
                    "Monika looks at me and smiles."
                    m "Soon, it'll all be over and I can finally enact my plans."
                    m 2c "Now, I should probably return Yuri back to normal for now."
                    m 2a "But the seed is already planted, I just need to activate it."
                    show monika zorder 2 at t21
                    "Monika stares at Yuri intently."
                    "The expression slowly returns to Yuri's face and she finds herself confused."
                    show yuri 3pn zorder 3 at f22
                    y "W-What? What's happening right now?"
                    show monika 3c zorder 3 at f21
                    show yuri zorder 2 at t22
                    m "Right now? Well, we're about to leave to go back to the other room."
                    m "You didn't really seemed convinced about my story."
                    m 3d "So there's no point going on about it anymore."
                    show monika zorder 2 at t21
                    show yuri 2ph zorder 3 at f22
                    y "I didn't? I...can't even remember what you said."
                    show monika 3e zorder 3 at f21
                    show yuri zorder 2 at t22
                    m "It was that forgettable? Wow, I guess I'm not the greatest storyteller."
                    m "I don't suppose you feel any different at least?"
                    show monika zorder 2 at t21
                    show yuri 2pf zorder 3 at f22
                    y "I don't think I do. Should I?"
                    y "You seemed pretty adamant about me being different afterwards but I feel the same."
                    show monika 1c zorder 3 at f21
                    show yuri zorder 2 at t22
                    m "Oh, well I guess it didn't really work."
                    m 1a "Maybe it was all just some sort of elaborate prank that I read somewhere."
                    show monika zorder 2 at t21
                    mc "I'm not really sure how telling a story was meant to change someone, Monika."
                    mc "Unless it was some sort of revelation that related to someone personally."
                    mc "I don't know if the students disappearing thing is actually true but it does sound a bit ridiculous."
                    mc "Maybe it was all just some joke somebody made up."
                    mc "Where did you even learn about it?"
                    show monika 1c zorder 3 at f21
                    m "It's most likely just some kind of trick but who knows for sure?"
                    m 1b "I guess we'll see the effects of it soon enough."
                    m "As for where I learned about it...it's probably best you don't know."
                    show monika zorder 2 at t21
                    show yuri 1g zorder 3 at f22
                    y "I can't even remember what you said the reason was but it doesn't really matter."
                    y "If the school really does have a declining student body then there's probably some reasons for it."
                else:
                    y 3pi "I don't need to learn this information."
                    "Yuri looks at me as she says that."
                    y "[player] and I talked about it and I don't really need to learn about it all."
                    y "I want to know, but not enough that it outweighs my trust in [player]."
                    y 3ph "If there is a chance that it would change me, I'd rather not risk it."
                    y "Not when I have so much to lose."
                    show monika 1c zorder 3 at f21
                    show yuri zorder 2 at t22
                    m "Wow, [player_personal] really had that much of an effect on you?"
                    m "I would have thought for sure that you'd have wanted to know."
                    m 1a "I guess my warning was a bit too scary for you."
                    show monika zorder 2 at t21
                    show yuri 1e zorder 3 at f22
                    y "I'd just rather not take unnecessary risks, that's all."
            show monika 1c zorder 3 at f21
            show yuri zorder 2 at t22
            m "Okay, if we're finished here I'd really like to get going."
            m "With how much time we have left, there's almost no time to do even one rehearsal."
            m 2a "So come on, you two. Let's get moving."
            scene bg portraitshop_school with wipeleft_scene
            "The three of us walk into the room carrying the bags."
            "To our surprise, Ayame is already here talking to Sayori and Natsuki."
            "Did one of them get her while we were gone?"
            "That must have been it...there's no way she would have known to be here otherwise."
            show sayori 1c zorder 3 at t53
            s "Oh, you're all here! And with everything else too!"
            show sayori zorder 2 at t53
            show monika 1e zorder 3 at f54
            m "You know, Sayori..."
            "Monika puts down the bag she's holding onto one of the desks."
            m "You really should have let me know we'd be in here."
            show sayori 1l zorder 3 at f53
            s "Ehehe, sorry, Monika! I promise it won't happen again."
            s "I just completely forgot that you didn't know."
            show sayori zorder 2 at t53
            show monika 2b zorder 3 at f54
            m "Just be sure if you ever decide to do something like this again, you'll let your vice president know."
            m "Well, no harm done I suppose."
            m 2e "Expect to our time to rehearse this play."
            "Monika turns towards Ayame and gives her a curious look."
            m 4c "It's strange that you got here before me, Ayame."
            show ayame 1i zorder 3 at f51
            show monika zorder 2 at t54
            ay "Oh? What's so weird about it?"
            ay "Is there a problem with me being here? I don't mean to intrude."
            show ayame zorder 2 at t51
            show monika 4a zorder 3 at f54
            m "No, it's just strange how the person who isn't even an official member yet would know we're meeting here today."
            m 4j "And yet the vice president didn't get any of this information."
            "Monika smiles warmly."
            m 4k "It's just a little funny, that's all~"
            show natsuki 2b zorder 3 at f55
            show monika zorder 2 at t54
            n "If we're done with the small talk, we should really get started."
            n "We've wasted so much time already."
            show yuri 2pf zorder 3 at f52
            show natsuki zorder 2 at t55
            y "I agree with Natsuki, let's get started right this very moment."
            show ayame 2j zorder 3 at f51
            show yuri zorder 2 at t52
            ay "Wait, wait! I have something to give you all."
            ay "Now that you're all here, it's the perfect time."
        "No.":
            $ ch16_getmonika = False
            mc "I think I'll stay here."
            mc "You said it yourself, you don't need me there."
            show yuri 2pf zorder 3 at f32
            y "I see...I'll be back in a few moments then."
            show sayori 2r zorder 3 at f31
            show yuri zorder 2 at t32
            s "Good luck, Yuri!"
            show sayori zorder 2 at t31
            "Yuri gives Sayori an acknowledging nod and leaves the room."
            show yuri at thide
            hide yuri
            show sayori zorder 2 at t21
            show natsuki zorder 2 at t22
            "Sayori closes the door and looks at the two of us left in the room."
            show sayori 2a zorder 3 at f21
            s "So...what do we do in the meantime?"
            show sayori zorder 2 at t21
            show natsuki 2c zorder 3 at f22
            n "I'm just gonna look around at all this stuff."
            "Natsuki quickly glances around the room and walks towards one of the tables lined with stuff."
            n "Where did you even get all of this?"
            show sayori 2c zorder 3 at f21
            show natsuki zorder 2 at t22
            s "If you know where to look, it's pretty easy to get stuff!"
            s "You shouldn't worry about it though, what matters is that it's here."
            show sayori zorder 2 at t21
            mc "Did all of that really fit in that one box?"
            mc "It would explain why it was so heavy but not how it all fit in there..."
            show sayori zorder 3 at f21
            s 1b "Actually, that was only one of the boxes."
            s "There was three in total, two of which I brought in just before you guys arrived."
            show sayori zorder 2 at t21
            show natsuki 1q zorder 3 at f22
            n "All of this must have cost a small fortune."
            n "I know I wouldn't even have enough money to buy all of this if I saved for months."
            show sayori 1l zorder 3 at f21
            show natsuki zorder 2 at t22
            s "L-Like I said, don't worry about it."
            s "It's better if we just focus on the play at hand rather than the ceramics of it."
            show sayori zorder 2 at t21
            mc "Semantics."
            show sayori 1h zorder 3 at f21
            s "You get the point! I just don't wanna talk about it, okay?"
            show sayori zorder 2 at t21
            show natsuki 1e zorder 3 at f22
            n "Fine, jeez. You don't need to get worked up about it."
            n 1g "I was only trying to make conversation because there's nothing really to talk about."
            show sayori 1a zorder 3 at f21
            show natsuki zorder 2 at t22
            s "Well, why don't you talk to me about Ayame?"
            s "It'll be good to know at least something about her before she arrives."
            s 3n "Which reminds me...does she even know where to go?"
            s "Like did anyone tell her at all where the club is?"
            show sayori zorder 2 at t21
            mc "Don't tell me we forgot to tell Ayame too..."
            show natsuki 2b zorder 3 at f22
            n "It seems like rehearsals are already off to a great start."
            n 2q "Sigh...I didn't really wanna go anywhere but..."
            n "Do you want me to go find her?"
            show natsuki zorder 2 at t22
            ay "That won't be necessary!"
            show ayame 2d zorder 3 at f31
            show sayori zorder 2 at t32
            show natsuki zorder 2 at t33
            ay "Why? Because I am here!"
            play sound closet_close
            "Ayame suddenly slams the door right open."
            play sound "sfx/smack.ogg"
            "She put so much force into it that it rebounded with enough momentum to hit her face."
            "I guess she wasn't expecting it because she fell to the floor right after."
            ay 2n "Ow...that really hurt."
            show ayame zorder 2 at t31
            show sayori 1m zorder 3 at f32
            s "A-Are you okay? You're not badly hurt, are you?"
            "Sayori goes to Ayame and offers her a hand."
            s 1d "Judging by what you just said, you're Ayame, right?"
            show ayame 1h zorder 3 at f31
            show sayori zorder 2 at t32
            ay "Thanks, but I can take care of myself."
            "Ayame doesn't take Sayori's hand and instead gets up by herself."
            ay 1j "But yes! I am Ayame, it's good to meet you."
            ay "You must be Sayori, right? I've heard so many things about you."
            show ayame zorder 2 at t31
            show sayori 1q zorder 3 at f32
            s "That's me, president of the Literature Club!"
            show sayori zorder 2 at t32
            show natsuki 1c zorder 3 at f33
            n "Ayame, how did you even find us?"
            n "It's not like any of us told you we'd be here, did we?"
            show ayame 2m zorder 3 at f31
            show natsuki zorder 2 at t33
            ay "Well, not exactly. Since I'm a leader, I can look through certain documents and I found your club."
            ay 2j "So here I am!"
            show ayame zorder 2 at t31
            show sayori 1n zorder 3 at f32
            s "Wow, you're a school leader! That's awesome!"
            s 1j "Don't think that means you'll get any special treatment here though!"
            show ayame 2h zorder 3 at f31
            show sayori zorder 2 at t32
            ay "I wouldn't have it any other way."
            ay "In fact, I'd prefer it if you treated me just like everyone else."
            ay "I'd hate to change the way you run things just because I'm a leader."
            show ayame zorder 2 at t31
            show sayori 2a zorder 3 at f32
            s "That's fine with me!"
            s "But wait...you mentioned that you found our club on those documents, right?"
            show ayame 1l zorder 3 at f31
            show sayori zorder 2 at t32
            ay "That's right, why?"
            show ayame zorder 2 at t31
            show sayori 1f zorder 3 at f32
            s "We don't usually have our meetings here. Not many clubs do, actually."
            s 1h "In fact, I don't think anyone outside of our club and the teachers I spoke to know we're here."
            show ayame 1c zorder 3 at f31
            show sayori zorder 2 at t32
            ay "W-Well...you see..."
            show ayame zorder 2 at t31
            show natsuki 1b zorder 3 at f33
            n "Does it really matter? She is here now so do not worry about it, Sayori."
            "The way Natsuki said that sounded almost...robotic."
            n "Let us just forget it and finally welcome her."
            show sayori 2j zorder 3 at f32
            show natsuki zorder 2 at t33
            s "But you wanted to know just a second ago too..."
            s 4d "Ah...you're right. Sorry, Ayame."
            show ayame 2d zorder 3 at f31
            show sayori zorder 2 at t32
            ay "N-Not a problem!"
            ay "It's not a big deal in any sense, so let's pretend it never happened."
            "Ayame walks into the room and looks around."
            ay 2j "Wow, very snazzy."
            "She picks up one of the costumes lying around on the table."
            ay 1h "I'm guessing these are what you're wearing for the play."
            ay "They're pretty high quality, I'm surprised you could afford something like this."
            show ayame zorder 2 at t31
            "Ayame looks at the three of us for a couple of seconds."
            "Her gaze seems to be focused on Natsuki."
            show natsuki 1a zorder 3 at f33
            n "Yeah, you're not the only one that's surprised."
            n "Sayori really went all out for this play."
            n 1c "I was kinda expecting cheap stuff from one of those second hand stores or something."
            show ayame 1h zorder 3 at f31
            show natsuki zorder 2 at t31
            ay "Well, I'm not going to ask how you got all of this."
            ay 1j "It's probably none of my business how your club get its finances."
            ay "So, what are you planning to do right now?"
            "Ayame looks around the room then back at us then around the room again."
            ay 1a "Wait...are you missing people? I could have sworn there were two other people in the club."
            show ayame zorder 2 at t31
            show sayori 2c zorder 3 at f32
            s "Yeah, actually--"
            show ayame 2m zorder 3 at f31
            show sayori zorder 2 at t32
            ay "That's right! Yuri and Monika are missing."
            ay "Are they here today? Or are they doing something?"
            ay 2n "Did something happen to them?"
            show ayame zorder 2 at t31
            show sayori 2b zorder 3 at f32
            s "Well, Yuri is going to the usual room to find Monika and get her things."
            s "I may have forgotten to tell Monika that the meeting was here today..."
            s 2a "If Yuri happens to meet Monika at the clubroom, then that would be the best possible outcome."
            s "If not, well...I guess we'll have to delay the rehearsal a bit."
            show ayame 2i zorder 3 at f31
            show sayori zorder 2 at t32
            ay "Rehearsals? That's what you're doing for this meeting?"
            ay "I would have thought you'd have already rehearsed it."
            ay 2a "Especially if you were going to perform it for Inauguration Day."
            ay "At least, that's what I'm assuming since there's no other reason I can think of right now."
            ay 2g "Or is this some kind of last minute rehearsal?"
            ay "I have to say that isn't the best idea, it could impact your overall performance."
            show ayame zorder 2 at t31
            show sayori 1d zorder 3 at f32
            s "It might not be the best idea, but I believe we can do it."
            s 1c "You're right though, it's actually our first rehearsal. My hope is that we'll get at least a couple of runs."
            s 1a "But we'll see, time does feel like it's running out."
            show ayame 2j zorder 3 at f31
            show sayori zorder 2 at t32
            ay "Yeah, you really don't have that much time at all."
            ay "A couple of runs sounds impossible with the time you have."
            ay 2g "With Yuri and Monika being missing, I'd be surprised if you can get even one rehearsal in."
            ay "Though I don't actually know how long your play is."
            show ayame zorder 2 at t31
            show sayori 1d zorder 3 at f32
            s "You'll see when we actually rehearse."
            s "In the meantime, why don't you take a seat while we wait for everyone?"
            s 1b "We're not exactly doing anything right now, so if you have any ideas on how we can pass the time..."
            show ayame 2b zorder 3 at f31
            show sayori zorder 2 at t32
            ay "I was actually going to give you all gifts, but seeing as not everyone is here, I'll hold it off."
            ay "Buuuuuut, if you want to pass the time...I have a couple of ideas of something we could do."
            ay 2h "I want to tell you guys a bit about me, and what better way than through a story?"
            show ayame zorder 2 at t31
            show sayori 4q zorder 3 at f32
            s "I think that's a great idea! What's the story about?"
            s 4l "It isn't too personal, is it?"
            show ayame 2j zorder 3 at f31
            show sayori zorder 2 at t32
            ay "Not at all, in fact it's actually something I've been wanting to tell you all."
            ay "I haven't told anyone else yet, not even my closest friends so you'd all be the first."
            ay 2m "It's a shame that Yuri and Monika aren't here but that's their loss."
            show ayame zorder 2 at t31
            show natsuki 1g zorder 3 at f33
            n "Get on with it, Ayame. We haven't got all day."
            n 1q "You know, since we're running out of time and everything."
            show ayame 2d zorder 3 at f31
            show natsuki zorder 2 at t33
            ay "Ahaha, okay. I wasn't expecting you to be so eager about it."
            ay 2i "Now, where do I begin...? Oh, right."
            ay 1m "It all started one fateful afternoon when I was wandering around my home."
            ay "My parents were out on some business meeting or something."
            ay "I don't really keep track of what they're doing, but that's not important."
            ay 1j "I was admiring nature when suddenly it felt like the world around me was...frozen."
            ay 1m "It felt like time was frozen or even moving backwards."
            show ayame zorder 2 at t31
            show natsuki 2k zorder 3 at f33
            n "Ayame, hold on just a second. I'd like to get something clear before we move on."
            n 2c "Not that I really mind either way but..."
            n "Is this a real story...or something you just made up?"
            show ayame 1g zorder 3 at f31
            show natsuki zorder 2 at t33
            ay "I don't know the answer to that question myself, Natsuki."
            "Natsuki has a look of confusion on her face but decides not to press on."
            ay 1m "Like I was saying, time was frozen."
            ay "The birds around flying in the sky were stuck in place, mid flight."
            ay 1l "At first, I didn't really know what to think."
            ay 1h "There was just a lot of questions buzzing in my head."
            ay "Was I dreaming? Was this some kind of trick someone was playing on me?"
            ay 1b "I began to panic. What if the world around me was stuck like this forever?"
            ay "Was I just supposed to live the rest of my life like this?"
            ay 1d "Then I took a deep breath and closed my eyes."
            ay 2h "Upon opening them, the world around me began to move once again."
            ay "I never felt so relieved to hear the songs of birds in the distance."
            show ayame zorder 2 at t31
            show sayori 1h zorder 3 at f32
            s "Sorry to interrupt you, Ayame. I just have a couple questions already."
            s "When did you come up with this story?"
            s "It sounds...interesting and all but what inspired to come up with it and when?"
            s 1j "And more importantly, why decide to tell us?"
            s 1d "Not that I or anyone else here minds but...you barely know us."
            show ayame 1a zorder 3 at f31
            show sayori zorder 2 at t32
            ay "I...I don't know. I suppose it's because I feel this certain...affinity towards this club."
            ay 1d "Like I can tell you guys {i}everything{/i}."
            ay 1e "It's as if I could trust you all with my deepest, darkest secrets."
            ay 1n "Which is weird! I can't understand why myself."
            show ayame zorder 2 at t31
            show natsuki 2e zorder 3 at f33
            n "No offense, but that just sounds absurd."
            n "I think you may have some sort of problem, Ayame."
            show ayame 2g zorder 3 at f31
            show natsuki zorder 2 at t33
            ay "I'm very aware that I do have some sort of problem, Natsuki."
            ay "Believe me when I say that I have done whatever I could within my power to try to get rid of it."
            ay 2n "But it was all to no avail."
            ay "Anyway, the story isn't finished yet. There's a bit more to go."
            ay 2j "That is, if you're still interested."
            show ayame zorder 2 at t31
            "Ayame looks at the three of us individually, expecting an answer."
            mc "I'm interested to see how it ends."
            mc "It feels like an odd thing to tell a story about."
            if ch15_s_together:
                mc "Yet it feels oddly familiar somehow."
            show sayori 2c zorder 3 at f32
            s "You started it so you may as well tell us how it ends."
            s 2d "And you didn't really answer all my questions, but I think I'm about to find out the answer to them anyway."
            show sayori zorder 2 at t32
            show natsuki 2c zorder 3 at f33
            n "I thought the story would have been about something that really happened."
            n 1j "That way maybe I could learn a bit about you seeing as you know a lot about us from Yuri already."
            n "But seeing as you've already told us some of it..."
            show ayame 2a zorder 3 at f31
            show natsuki zorder 2 at t33
            ay "Okay, I understand I'm not the best storyteller."
            ay "Just bear with me, it's almost the interesting part."
            "I thought the interesting part would have been the part where time froze."
            "It turns out Ayame has more in store for us."
            ay 2l "As I was saying, when time unfroze I felt relief."
            ay "Then I came to a sudden realization, was I the cause of it all?"
            ay 2m "This voice inside my head was telling me it was me."
            ay "But how could it have been? I have no idea how I could possibly do that."
            ay "I thought about telling my parents about what happened."
            ay "I almost did but I decided against it for fear of sounding crazy."
            ay 2j "Which is ironic, since I'm telling you three."
            ay "After a few minutes of walking around, reflecting on what just happened..."
            ay "Time froze. Again. The clocks on the walls stopped ticking."
            ay 2a "The blades of grass were frozen in place and once again questions raced through my head."
            ay "This...is where it got weird."
            ay 2g "When I went to the street to witness the effects, I saw someone on the corner of the street."
            ay "Or at least, I'm pretty sure I did."
            ay "It was only for the briefest of moments, but I could make out a sort of pink and red."
            ay "This wouldn't be a significant detail but that person was moving."
            ay 1l "Moving in this period of stopped time."
            ay "This made my head jump to two conclusions. Either I was imagining things and everyone else was frozen..."
            ay 1m "Or this person could somehow traverse through the world while time ceased."
            ay "So I did what any sane person would have done."
            show ayame zorder 2 at t31
            mc "You decided not to follow it, right?"
            mc "That {i}is{/i} what a sane person would have done, Ayame."
            show ayame 2g zorder 3 at f31
            ay "I needed answers, [player]. Any sane person would do the same."
            "Natsuki and Sayori look at each other with a inquiring look. Natsuki shrugs."
            show sayori 2o
            show natsuki 1g
            "There's a slight look of worry on Sayori's face."
            ay "It seemed to me at the time that this would be the only one who knew what was going on."
            ay 2l "I had to find out why this was happening so I gave chase."
            ay "I tried to run as fast as I could towards this person."
            ay "When I finally turned the street, they were missing. Completely gone."
            show ayame zorder 2 at t31
            show natsuki 1h zorder 3 at f33
            n "Is it possible they just went into their house or something?"
            n "Or maybe into a side street or alley?"
            show ayame 1h zorder 3 at f31
            show natsuki zorder 2 at t33
            ay "That street was mostly just a wide road with no houses or alleys."
            ay "And so I was left all by myself, alone in a single moment of time."
            ay 1m "Just as I was venting my frustration about it all, time resumed once again."
            ay "The people on the street walking looked at me with a bewildered look on their face and rightfully so."
            ay "A random girl yelling in the middle of the street in broad daylight for seemingly no reason?"
            show ayame zorder 2 at t31
            show natsuki 2b zorder 3 at f33
            n "So you're saying that time started moving again because you yelled at it to?"
            n "This sounds more and more made up as it goes on."
            show sayori 1c zorder 3 at f32
            show natsuki zorder 2 at t33
            s "You know, maybe it isn't all that ridiculous."
            s "It's interesting to hear Ayame's side of things of this story."
            s 1f "{i}(This confirms my suspicions too...){/i}"
            show ayame 2j zorder 3 at f31
            show sayori zorder 2 at t32
            ay "My side of things? Ahaha, I wasn't aware there was another side of this story."
            ay "This is all just a recount of something that very well may have been a dream."
            ay 2i "But what about your suspicions?"
            ay "Are you suspicious of me or something, Sayori?"
            show ayame zorder 2 at t31
            show sayori 1l zorder 3 at f32
            s "W-What? I didn't say anything like that."
            show ayame 1m zorder 3 at f31
            show sayori zorder 2 at t32
            ay "You said it loud and clear."
            ay "Well...maybe not loud but it was pretty clear."
            ay "You said it confirms your suspicions, didn't you?"
            ay 1n "Or am I just hearing things?"
            show ayame zorder 2 at t31
            show sayori 1m zorder 3 at f32
            s "If you heard that then you must have some amazing hearing or..."
            s "Well, you have amazing hearing."
            show ayame 1j zorder 3 at f31
            show sayori zorder 2 at t32
            ay "I'd say my hearing is normal, not particularly amazing or anything."
            ay "I can just make out what people are saying as if there was words right in front of me."
            ay 1k "Sort of like subtitles but when I'm talking to people."
            show ayame zorder 2 at t31
            show sayori 2d zorder 3 at f32
            s "Like subtitles, eh? I'm sure that must be useful..."
            show ayame 1h zorder 3 at f31
            show sayori zorder 2 at t32
            ay "If there's nothing else, I'd like to finish the story."
            ay "It's got quite the ending, I'm sure you'll all like it."
            show ayame zorder 2 at t31
            show natsuki 1a zorder 3 at f33
            n "Go ahead, Ayame. We're waiting, just make it quick."
            n 1c "I have a feeling Yuri and Monika are going to be back any second now."
            show ayame 1b zorder 3 at f31
            show natsuki zorder 2 at t33
            ay "In that case I'll just skip all the minor details."
            ay "The story ends with me suddenly being shifted back to my home."
            ay "It was like a time reversal, all my actions played in reverse."
            ay 1j "I could watch the world around me rewind but I was powerless to do anything about it."
            ay "It kept on going until I was back inside my house, before the time stop and reversal."
            ay "I was half expecting it all to happen again."
            ay "An endless loop that I was destined to repeat."
            ay 1d "But...thankfully, it didn't repeat!"
            ay "I actually went outside to see if anything was different but there was nothing."
            ay "The events of the rest of that day went without a hitch."
            show ayame zorder 2 at t31
            show natsuki 1e zorder 3 at f33
            n "So you're basically saying that it didn't happen in the end?"
            n "That everything you just told us never happened?"
            show ayame 2g zorder 3 at f31
            show natsuki zorder 2 at t33
            ay "It did happen but I suppose because of the rewind, it never did happen."
            show ayame zorder 2 at t31
            show natsuki 2b zorder 3 at f33
            n "For all we know, you really could have just made it up."
            show ayame 2n zorder 3 at f31
            show natsuki zorder 2 at t33
            ay "But I'm telling you the truth!"
            ay "I swear these events did happen, or at least they're so engrained in my head that they must have."
            show ayame zorder 2 at t31
            mc "Maybe it was some kind of lucid dreaming where it felt real?"
            mc "Or it really could have happened, I don't have any reason not to believe you."
            mc "There's just no proof that it did happen."
            show ayame zorder 3 at f31
            ay "I can see that telling you guys has not made me lean towards accepting if it was real or not."
            ay 2e "Ahaha, in fact I think I've come out more confused than before."
            show ayame zorder 2 at t31
            show sayori 1b zorder 3 at f32
            s "I, for one, believe Ayame."
            s 1c "She's going to be the newest member of the club so I don't see any reason she'd lie to us."
            s 1a "Dream or not, Ayame believes there's a chance it happened so let's take her word for it."
            show ayame 1h zorder 3 at f31
            show sayori zorder 2 at t32
            ay "I really appreciate you saying that, Sayori."
            ay "Things like that let me know that I've made the right decision joining this club."
            show ayame zorder 2 at t31
            show sayori 1q zorder 3 at f32
            s "Of course, any--"
            show ayame 1m zorder 3 at f31
            show sayori zorder 2 at t32
            ay "But you shouldn't just do that with everyone, you know."
            show sayori 1h
            ay 1a "Such gullibility could lead to your undoing. Especially with someone you've just met."
            "Ayame locks her eyes with Sayori."
            "It's like she's trying to intimidate her or something..."
            "Natsuki and I can both sense the tense mood that Ayame is bringing."
            "She wasn't like this at all yesterday."
            "I'm not sure where this is coming from all of a sudden."
            ay "But you don't have to worry about that with me!"
            ay 1d "I'm not out to hurt anyone or anything like that."
            ay "I just thought I'd let you know."
            ay "That tip, of course, goes to all three of you and not just Sayori."
            show ayame zorder 2 at t31
            show sayori 1l zorder 3 at f32
            s "Right...thanks for the advice then, Ayame."
            s 1d "I suppose all that's left to do now is wait for the other two to get back."
            show ayame 1h zorder 3 at f31
            show sayori zorder 2 at t32
            ay "So what did you learn about me from that story?"
            ay "Probably nothing since it didn't really make much sense."
            ay "But if you learned anything at all."
            show ayame zorder 2 at t31
            show natsuki 2k zorder 3 at f33
            n "I learned that you've got some strange imagination."
            n "Or if it really wasn't imagination, some {i}very{/i} strange things happening to you."
            n 4g "Though I'm not really surprised if that's the case, to be honest."
            n "Stranger things have happened in this club, I'm sure you probably know some of them."
            n "It just weird hearing something like that happen outside the club."
            show natsuki zorder 2 at t33
            "I can't really disagree with her there. As bizarre as the world suddenly stopping like that is..."
            "It wouldn't be the weirdest thing I've heard happen."
            show ayame 1j zorder 3 at f31
            ay "Stranger things {i}have{/i} happened, haven't they? Or so I've read."
            ay "Those, at least, have some sort of possible reason they could have happened."
            ay 1m "Mine just doesn't make any sense but I'm slowly understanding it."
            "Ayame turns towards us."
            ay 1j "Interesting. What are your thoughts [player] and Sayori?"
            ay "Learn absolutely anything at all?"
            show ayame zorder 2 at t31
            show sayori 1c zorder 3 at f32
            s "I think I did but it wasn't much."
            s "I'd rather learn more about you through the things you do and not the things you've done."
            s 2h "From what I can tell from your story, you sound like a wealthy person."
            s "You said your parents were on a business meeting and that usually means meeting with some executives or something, right?"
            s 2a "Which also explains why you bought gifts for us because money doesn't really concern you."
            s 2q "Am I right?"
            show ayame 1c zorder 3 at f31
            show sayori zorder 2 at t32
            ay "That...that was a pretty good deduction from a small detail I said."
            ay 1g "It's true, my family has more money than they know what to do with."
            ay "I don't meddle in their affairs, I don't plan on continuing whatever they're doing."
            ay "I don't really have an interest."
            ay 1l "Though as the only heir to the family fortune, I suspect they may have other plans."
            show ayame zorder 2 at t31
            show natsuki 4e zorder 3 at f32
            n "I'd say do what you want, Ayame."
            n "You shouldn't let your parents control your life."
            n 4m "I know that all too well.."
            show ayame 2n zorder 3 at f31
            show natsuki zorder 2 at t32
            ay "That's a lot easier for you to say."
            ay "Your family doesn't have these absurdly high expectations of you."
            ay 2g "I've only maintained a small sense of autonomy because I've lived up to those expectations."
            ay "If I didn't, I probably wouldn't be able to speak to you all now."
            ay "I'm still longing for the day when I can finally live my own life the way I want."
            ay 2h "For now though, I have to take the small opportunities I have."
            ay 2e "Like this one!"
            show ayame zorder 2 at t32
            show sayori 1b zorder 3 at f33
            s "So sometimes you just get forced to do something?"
            s "Like you have to accept a responsibility you wanted no part of?"
            show ayame 2a zorder 3 at f32
            show sayori zorder 2 at t33
            ay "That's precisely it, Sayori. You got it right."
            ay "Though that happens on a nearly daily basis for me."
            ay 2g "The things I have to do...a lot of it is no fun at all!"
            show ayame zorder 2 at t32
            "Suddenly, the door opens and Monika and Yuri step through."
            "They seem to be carrying the bags that were stored in the clubroom."
            show ayame zorder 2 at t51
            show yuri 3pf zorder 2 at f52
            show sayori zorder 2 at t53
            show monika 1c zorder 2 at t54
            show natsuki zorder 2 at t55
            y "We've returned with all of the stuff from the closet."
            y "I hope we weren't gone for too long."
            show yuri zorder 2 at t52
            show sayori 4a zorder 3 at f53
            s "You guys are here now and that's what matters."
            s "You missed out on the story Ayame told us but that was just to pass the time anyway."
            show sayori zorder 2 at t53
            show monika 2d zorder 3 at f54
            m "Speaking of which, how did she even manage to get here?"
            m "She knew about the club meeting being moved here but I didn't?"
            m 2a "Not that I'm complaining or anything."
            m "It's just an ironic kind of funny that the vice president of the club didn't know but someone who's not even a member did."
            show sayori 4d zorder 3 at f53
            show monika zorder 2 at t54
            s "I'm sorry I forgot to tell you. I guess I just didn't remember to."
            show sayori zorder 2 at t53
            show monika 2e zorder 3 at f54
            m "Everyone makes mistakes, Sayori. This was a pretty minor one and got solved quickly."
            m "Just make sure you remember for next time though."
            m "A couple of mistakes here could lead to a disaster later down the line, you know."
            show monika zorder 2 at t54
            show natsuki 3b zorder 3 at f55
            n "If you two are done, we should really get on with the rehearsal."
            n "We've used up enough time already."
            show yuri 3pa zorder 3 at f52
            show natsuki zorder 2 at t55
            y "She's right. If we don't start now then we'll never get anything done."
            show ayame 1b zorder 3 at f51
            show yuri zorder 2 at t52
            ay "Wait, wait! I was going to give you all something."
            ay "Since everybody is finally here, it's the perfect time."
    ay 1a "I don't intend to delay your rehearsals any further or anything like that."
    ay "But I don't think I'll get another chance with you all here."
    ay 1b "This will only take a moment, I promise."
    show ayame zorder 2 at t51
    show natsuki 1b zorder 3 at f55
    n "Just make it quick, Ayame. We've got lots to do."
    show sayori 1a zorder 3 at f53
    show natsuki zorder 2 at t55
    s "We still have to officially make you a member too!"
    s 1d "But you don't need to worry about that. As far as we're concerned, you already are."
    show ayame 1h zorder 3 at f51
    show sayori zorder 2 at t53
    ay "Okay, I'll do my best to keep it brief."
    "Ayame takes her bag and takes out a large plastic bag."
    "She takes out five small boxes of different sizes from the bag and lays them out on a table."
    "She then picks one out and turns toward Yuri."
    ay 1j "This one is for you, Yuri. I do hope you like it."
    show ayame zorder 2 at t51
    show yuri 2pf zorder 3 at f52
    y "For me...?"
    "Yuri takes the box and begins inspecting it."
    "It's wrapped in some sort of purple wrapping paper with a neatly tied ribbon at the top of it."
    y 3pa "I appreciate the gift, Ayame. It's very thoughtful of you."
    y "It's a shame we couldn't do the same for you."
    show ayame 1d zorder 3 at f51
    show yuri zorder 2 at t52
    ay "Don't mention it. Really."
    ay "I don't expect you all to get me anything."
    ay 1e "To me, the real gift is being accepted into your club."
    show ayame zorder 2 at t51
    show yuri 3pb zorder 3 at f52
    y "That's quite humble of you to say..."
    "Yuri examines the box she was given before putting it away."
    y 3pe "What exactly did you get me?"
    show ayame 1k zorder 3 at f51
    show yuri zorder 2 at t52
    ay "That's for you to find out! I promise you'll like it."
    ay "You don't have to open it just this moment."
    ay 1j "If you want, you can open it later. There's no rush anyway."
    ay "I just wanted to get this out of the way before you all start anything important."
    ay 1h "Anyway, here you go, Natsuki."
    show ayame zorder 2 at t51
    "Ayame takes another box and offers it to Natsuki."
    "This time it's wrapped in a colorful pink paper."
    "Natsuki reluctantly takes the box and begins shaking it a little."
    "She then looks at Ayame and lets out a small smile."
    show natsuki 1d zorder 3 at f55
    n "I'm not going to say no to a gift like this."
    n 1c "I really want to open it but I think I'll just get distracted by it."
    n 2a "I'll leave it for later, if that's okay."
    show ayame 1j zorder 3 at f51
    show natsuki zorder 2 at t55
    ay "Of course. Like I said, there's no rush."
    ay "The gift I brought you all isn't going anywhere soon so take your time."
    ay 1e "And speaking of gifts, here's one for Monika and Sayori."
    "Ayame takes two more of the boxes into her hands."
    "One of them is colored a bright green while the other is a light shade of blue."
    "She puts the blue one on the desk in front of Sayori and offers the green one to Monika."
    ay 1b "I came up with a different kind of present for the two of you."
    ay "It's similar but I thought that the president and vice president should have something more significant."
    "Ayame looks towards Natsuki and Yuri."
    ay 1d "Don't worry, it's nothing too worry about. Your gifts are just as good!"
    ay "It's just slightly different to theirs."
    show ayame zorder 2 at t51
    show sayori 4q zorder 3 at f53
    s "Thank you so much, Ayame!"
    s "I wish I could have gotten you something."
    s 4c "But no one told me anything about this whole gifts thing!"
    show ayame 1m zorder 3 at f51
    show sayori zorder 2 at t53
    ay "Think nothing of it, Sayori."
    ay "It's just a gesture of my appreciation to all of you."
    show ayame zorder 2 at t51
    show monika 2e zorder 3 at f54
    m "Thanks, Ayame. I'll be sure to keep this gift close to me."
    m "I think it would be best if I didn't open it right now though."
    m 2c "Like Natsuki said, it might cause us to be distracted and take away from what we're meant to be doing."
    show monika zorder 2 at t54
    "Ayame shrugs then finally picks up the last box and offers it to me."
    "The color of the box is just a pure white and it seems quite plain compared to the others."
    show ayame 2d zorder 3 at f51
    ay "And last but not least, [player]."
    "She offers the box to me and I take it."
    ay 2b "Are you going to open it, [player]?"
    ay "No one else did, and I admit I'm kinda surprised that was the case."
    ay 1h "But at the same time, I applaud your dedication to this little rehearsal you're going to be having."
    ay "Steeling yourself from distractions is something I could never do."
    show ayame zorder 2 at t51
    show sayori 1a zorder 3 at f53
    s "I just wanna take the time to appreciate it, that's all."
    s "Opening it now isn't going to let me fully understand your intentions behind it."
    show ayame 1i zorder 3 at f51
    show sayori zorder 2 at t53
    ay "That's a pretty good reason actually."
    ay "But I'm sure you won't need to think much about it when you open it."
    ay 1h "And what's your excuse, [player]? Are you going to leave it until later too?"
    show ayame zorder 2 at t52
    mc "I guess I could open it now, but that might cause a chain reaction."
    mc "Someone else might feel like they should do the same, to compare their gift."
    mc "But I'm sure the others have more self control than that."
    show ayame 1j zorder 3 at f52
    ay "Then...?"
    show ayame zorder 2 at t52
    "Ayame's face lights up at the idea of me opening it."
    mc "Well, I don't see the harm in opening it."
    mc "I'm keen to see what you've given me anyway."
    "I begin to unwrap the present Ayame gave me."
    "Inside I can find some kind of jewelry engraved with something."
    "Open closer inspection, I can see it says 'Literature Club' on it."
    "I can also see my initials priinted out on it in small writing."
    mc "Is this a custom made ring?"
    show ayame 1k zorder 3 at f52
    ay "It could be, who knows?"
    show ayame zorder 2 at t52
    mc "And you did this for all of us?"
    mc "I can't imagine how much it would cost for one person, but for five?"
    show ayame 1h zorder 3 at f52
    ay "Who says they have the same gift?"
    ay "Maybe you all got different things, but you're not going to find out now."
    "Ayame puts her bag away after having finished with the presents."
    ay 1j "Anyway, that's all I had. You guys can do your thing now."
    ay "I just wanna watch and see what exactly is going on."
    ay 2j "I won't interrupt unless you need me to say something."
    show ayame zorder 2 at thide
    show yuri zorder 2 at t41
    show sayori zorder 2 at t42
    show monika zorder 2 at t43
    show natsuki zorder 2 at t44
    hide ayame
    "I'm very tempted to open this gift right now."
    "By the way she was talking, we all got pretty similar things."
    "But I don't want to be the odd one out and open the gift while the others don't."
    "I'll go against that urge, just to avoid distracting the others too."
    "Like they said, we don't have that much time so we can't afford to get distracted."
    show sayori 2q zorder 3 at f42
    s "Alright, everybody!"
    s "It's {i}finally{/i} time to get started on rehearsals."
    s 2a "I know everyone's been saying we might not have enough time to do even one run through."
    s "But I believe we can do it!"
    show sayori zorder 2 at t42
    show natsuki 1g zorder 3 at f44
    n "Sayori, you can believe all you want."
    n 1c "The objective fact is unless we speak super quickly, we won't even get one rehearsal through."
    n "Even if we do manage to get a single rehearsal done, I don't think it's going to be a very good performance."
    n 1q "And I'm not trying to be negative, I'm just being realistic."
    show sayori 1l zorder 3 at f42
    show natsuki zorder 2 at t44
    s "H-Hey, come on. Don't say that."
    s "If you do, then it's only going to be true."
    s 1d "If we just make proper use of the time, I know for sure it's going to be amazing!"
    show sayori zorder 2 at t42
    "Ayame looks like she's amused by the scene that's happening."
    "She sits on a desk and simply smiles as if she's eager to see how this will unfold."
    "I think Natsuki is right, but Sayori seems convinced that we can do it."
    "I don't know why, but I have a feeling we can somehow pull it off."
    "Sayori's enthusiasm must be rubbing off on me despite me knowing its basically impossible."
    show yuri 1e zorder 3 at f41
    y "Then let's get started with the rehearsal."
    "Yuri takes her copy of the script and opens it up."
    y 1f "Is everyone else ready?"
    show yuri zorder 2 at t41
    show sayori 2q zorder 3 at f42
    s "Definitely! Let me just find where I left my script..."
    show sayori zorder 2 at t42
    mc "Sayori, that's the opposite of being ready."
    show sayori 2h zorder 3 at f42
    s "I was just kidding! It's right here."
    "Sayori takes out her copy of the script from under some of the clothes she's standing near."
    "Nobody looks impressed with her little joke, they all seem like they want to get started already."
    s 2c "Do you guys want to wear your costumes now or later?"
    s "It might be a good idea to try them out before the actual play."
    show sayori zorder 2 at t42
    show natsuki 1e zorder 3 at f44
    n "We don't have time. The costumes can wait until later."
    n "They're no use if we can't even get the performance right."
    show monika 3a zorder 3 at f43
    show natsuki zorder 2 at t44
    m "While that's a good point, it would be a good idea to see if they fit."
    m "If they don't fit then our performance won't have as much of an effect, no matter how good it is."
    show yuri 2ph zorder 3 at f41
    show monika zorder 2 at t43
    y "If the two of you are done arguing, we should really start."
    y "Look at the time."
    "Yuri points toward the clock in the room."
    "As she does, the quiet tick tock noise it's making seems to become louder."
    "There's something not quite right about the clock though, and I can't understand why."
    "It's just a normal clock...isn't it?"
    "Maybe I'm just not used to this room."
    y 3pr "Forget the costumes and focus on the script."
    y "Just trust that Sayori managed to get our sizes roughly right."
    y "After all, she's managed to do the impossible before."
    show yuri zorder 2 at t41
    show sayori 1a zorder 3 at f42
    s "That's right, there's no need to worry."
    "Sayori opens her script to the first page."
    s 1b "[player], I think you're up first."
    s "Everyone else, follow the stage directions that it says in the script."
    show sayori zorder 2 at t42
    "Sayori takes charge of the situation and gives the que for when things should happen."
    "To my surprise, everyone's acting ability has improved a lot."
    "The way they're talking sounds more natural than forced."
    "I'm impressed at myself too. I definitely feel like I'm doing a better job than the last two plays."
    "I guess it's got to do with the script too."
    "It's very well written and I think Sayori made some adjustments to the lines to better suit our own acting ability."
    "It definitely makes me feel like she's getting some sort of outside help."
    "But I'm not gonna bother with that right now, we're busy rehearsing anyway."
    "Maybe I could ask after this is all over..."
    "Soon enough, we're over halfway through the rehearsal and everyone seems to be enjoying themselves."
    "Ayame looks like she's pretty entertained too."
    "I wonder what she thinks about all of this so far."
    show sayori 1q zorder 3 at f42
    s "Alright, everybody! We've done a lot of good work so far."
    s "Let's just take a short break so everyone can take it all in."
    show sayori zorder 2 at t42
    show natsuki 2c zorder 3 at f44
    n "Are you kidding? We should keep going!"
    n 2b "It feels like the worse possible time to stop."
    show yuri 1t zorder 3 at f41
    show natsuki zorder 2 at t44
    y "I concur with her. We should make proper use of our time."
    y "Not to mention, I feel so invigorated in this rehearsal. I don't know why."
    y 1u "It's like this whole play is just natural, as if I wasn't rehearsing this but actually saying it."
    y "Of course, it's still a work of fiction...it was just a figure of speech."
    show yuri zorder 2 at t41
    show monika 1j zorder 3 at f43
    m "I have to say this is rather fun."
    m "I didn't expect myself to get so into it."
    m "I almost lost my sense of determining what was our reality and what was our play, but only briefly."
    m 1a "I do think there is no reason to stop if we're in the flow of things."
    show sayori 2d zorder 3 at f42
    show monika zorder 2 at t43
    s "You guys really want to keep going? I feel so drained..."
    "Sayori looks at the four of us and sighs."
    s "Just give me a break then, if you four don't want to stop."
    show sayori zorder 2 at t42
    mc "I never said I wanted to keep going."
    mc "That said, I think it would be better if we get this done in one go."
    mc "But if you need a break, you probably deserve it."
    mc "You lead that whole thing pretty well, Sayori."
    show sayori 2a zorder 3 at f42
    s "Well, you know...maybe it just comes naturally to me."
    s "Bossing people around is pretty fun, you know."
    "Sayori turns towards Ayame who is fiddling with something on her desk."
    s 4c "What did you think so far, Ayame?"
    show yuri zorder 2 at t51
    show sayori zorder 2 at t52
    show monika zorder 2 at t53
    show natsuki zorder 2 at t54
    show ayame 1i zorder 3 at f55
    ay "You want my opinion? I'm happy to give you some criticism and feedback."
    ay "Though there's not really much to say."
    show sayori 3c zorder 2 at t52
    show ayame zorder 2 at t55
    s "Go ahead and say anything! You're like the judge before our actual play."
    s 3a "If you can give a suggestion that can make it better, then that would great!"
    show sayori zorder 2 at t52
    show ayame 1m zorder 3 at f55
    ay "Like I said, there's not much to say."
    ay 1h "I, personally, was pretty entertained throughout all of it."
    ay "And that was only a rehearsal."
    ay 1j "It made me think that you were just saying it was your first rehearsal when you've all practice a lot."
    ay "I wonder how it will all look in costume."
    show monika 1c zorder 3 at f53
    show ayame zorder 2 at t55
    m "You don't have anything bad to say about it?"
    m "No criticism whatsoever?"
    show monika zorder 2 at t53
    show ayame 2j zorder 3 at f55
    ay "Oh, I definitely do. It's nothing constructive though."
    ay 2m "Hence, I'd rather not say it."
    show sayori 3d zorder 3 at f52
    show ayame zorder 2 at t55
    s "That's fine, if you can't think of anything there's nothing wrong with that."
    "Sayori takes a step forward and stumbles slightly."
    s 1h "Okay, I really need to step outside for a minute."
    s 1a "I'll be back before you know it."
    if ch15_s_together:
        s "Do you want to come as well, [player]?"
        s "I would enjoy some kind of company."
        show sayori zorder 2 at t52
        mc "Sure, if you need me to come."
        mc "It's not like there's anything better for me to do at the moment."
        show sayori 1q zorder 3 at f52
        s "Great! Then let's get moving."
        "Sayori points to the clock on the wall."
        s "Remember that time, we'll be back before you know it."
        show sayori zorder 2 at t52
        show natsuki 1o zorder 3 at f54
        n "You're leaving, just like that?"
        show sayori 1g zorder 3 at f52
        show natsuki zorder 2 at t54
        s "Just for a little while, I'll be back soon."
        s "Now I really have to get out of here."
        scene bg school_hallway
        show sayori 1ba zorder 2 at t11
        with wipeleft_scene
        "Sayori and I exit the classroom and begin walking down the corridor."
        "I have no idea where we're going or what we're doing."
        "But Sayori says it won't take long so I'll believe her. "
        "Suddenly, Monika opens the door to the room and catches up with Sayori.."
        show sayori zorder 2 at t21
        show monika 1a zorder 3 at f22
        m "You know, it's pretty irresponsible to just leave like that."
        m "Especially when it's all so sudden."
        m "You should really tell us where you're going."
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s "I'm sorry but this was kinda urgent and I just remembered it."
        s "I'd tell you but I really shouldn't."
        s "I hope you understand, Monika."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m "Of course I do. Sometimes you just wanna keep things a secret."
        m "Anyway, I need to go back in there to make sure things are running smoothly."
        m "You have nothing to worry about with me in charge."
        show sayori zorder 3 at f52
        show monika zorder 2 at t53
        s "Thanks, but we won't be gone too long."
        s "We just need to make a quick visit somewhere."
        show sayori zorder 2 at t52
        show monika zorder 3 at f53
        m "I'm guessing it's none of my or the club's business."
        m "Why do you have to take [player] with you though?"
        show sayori zorder 3 at f52
        show monika zorder 2 at t53
        s "I have my reasons. I will say that [player_personal] doesn't have to come."
        s "But I would greatly appreciate [player_possessive] presence."
        show sayori zorder 2 at t52
        mc "We're stopping practice anyway, so I might as well come with her."
        mc "Even if it's just a minor thing."
        show monika zorder 3 at f53
        m "You're the president of the club, Sayori."
        m "Do whatever you want, it's your life."
        m "I'm going to go back inside and try to deal with the situation."
        m "Good luck, you two! I hope you find whatever it is you're looking for."
        show sayori zorder 2 at t11
        show monika at thide
        hide monika
        "Monika goes back into the room without saying another word."
        "After she's sure that Monika is busy inside, Sayori continues to lead me to...some place."
        "I wonder why she has this urge to make me come along."
        "It's not like I can really help her, except maybe provide moral support."
        "She's more than capable on her own."
        mc "So where exactly are we going?"
        mc "Or is this just an excuse to get out of doing the practice?"
        s "No, definitely not! With how much time we have left, not doing practice would have been a terrible idea."
        s "This takes priority over that."
        mc "And what is {i}this{/i}? You haven't told me anything yet."
        s "Does it really matter? I asked you to come with me."
        s "If you don't want to go, then you don't have to."
        mc "I want to go. I just hate being left in the dark."
        mc "But if that's what it takes, then I can endure it."
        mc "I just wish I knew the reason for all this secrecy."
        s "Soon, there won't be any need for it. I promise you that."
        mc "If you say so..."
        s "Anyway, it's just over this way. Come on."
        "Sayori takes us all around the school through some route I've never been through before."
        "I tried memorizing the path we took at first but there was just too much to remember."
        "It's like she took an overly complicated path on purpose."
        "I could have sworn we walked past the same classroom about three or four times."
        scene bg corridor
        show sayori 1a zorder 2 at t11
        with wipeleft_scene
        "Eventually, she stops in front of a room that seemed all too familiar."
        s "And here we're here, and it didn't take as long as I thought it would."
        s "Quickly, let's get inside."
        mc "Isn't this just our normal clubroom?"
        mc "Why are we here...?"
        s "It looks like it, doesn't it? But it isn't."
        s "It's another room that's used by a different group of people."
        s "They aren't here right now because they're out doing preparations for the day."
        mc "Isn't that the reason we're not at our room either?"
        s "Look, just follow me inside. You'll see why we're here."
        s "Everything will be clear then."
        mc "Alright, well I don't suppose you have a way to unlock the door?"
        mc "If this isn't our clubroom, I'd imagine you wouldn't have the key to unlock it."
        mc "And I don't think it's just going to be open."
        show mysteriousclerk 1a zorder 3 at f21
        show sayori zorder 2 at t22
        cl "That's where you're wrong, kiddo."
        cl "The door is already open so there's no need for her to unlock it."
        cl "Come on, let's get inside. We have much to discuss."
        show mysteriousclerk zorder 2 at t21
        show sayori zorder 3 at f22
        s "Alright, I just hope we can do something about it now that she's in there."
        s "At least something to help make it easier for when erupts."
        show sayori zorder 2 at t22
        "Sayori starts walking inside the room where this odd man is."
        "I'm really confused as to what is going on right now."
        mc "For when she erupts? Who are you talking about?"
        mc "Who is this guy, Sayori?"
        show mysteriousclerk zorder 3 at f21
        cl "Oho, you actually did it. I'm surprised you followed through."
        cl "I would have thought it would have been harder for you."
        cl "Seeing as you just went on a date and all."
        show mysteriousclerk zorder 2 at t21
        # For context, she wipes his memory one last time after the date
        "This guy knows about that? That doesn't make any sense."
        "We only just got back from it and I'm pretty sure no one knew."
        show sayori zorder 3 at f22
        s "You know it's not like that, mister {i}[cl_name]{/i}."
        s "And shouldn't you be careful what you're saying around [player_reflexive]?"
        s "You want this as much as I do."
        show sayori zorder 2 at t22
        mc "What the hell is going--"
        show mysteriousclerk zorder 3 at f21
        cl "You're right, of course. I'm just messing with you."
        cl "Everything is ready, come on in."
        show mysteriousclerk zorder 2 at t21
        show sayori zorder 3 at f22
        s "Right, no time to waste."
        scene bg club_skill with wipeleft_scene
        "As we get into the classroom...it feels exactly like our normal clubroom."
        "The desks are all arranged in pretty much the exact same way."
        "In fact, it's hard to tell if there actually is any difference at all."
        "If I didn't know any better, I'd say this {i}was{/i} our clubroom."
        "But there's something about it that just doesn't feel right."
        "I can't quite figure it out..."
        show mysteriousclerk 1a zorder 3 at f21
        show sayori 1a zorder 2 at t22
        cl "Without further ado, let's bring [player_reflexive] back to speed."
        show mysteriousclerk zorder 2 at t21
        mc "Are you talking about me? What do you mean?"
        show sayori zorder 3 at f22
        s "This...might sting a little. I'm gonna say sorry ahead of time."
        s "I haven't actually tried doing it the other way around."
        s "So it's a new experience for the both of us."
        show sayori zorder 2 at t22
        mc "W-What? What exactly are you talking about here, Sayori?"
        mc "I thought you said things would be clear when we got here."
        show sayori zorder 3 at f22
        s "They will be soon, [player]. Just wait a second..."
    else:
        s "Just read ahead or something with the script."
        s "It might not be a good idea to actually practice though."
        s "You won't have me to yell directions at the four of you."
        "Sayori points to the clock on the wall."
        s "Look at the time right now and remember it."
        s "It'll seem like no time at all has passed when I get back."
        show sayori at thide
        hide sayori
        show yuri zorder 2 at t41
        show monika zorder 2 at t42
        show natsuki zorder 2 at t43
        show ayame zorder 2 at t44
        "Sayori leaves the room and walks down the hallway."
        "I wonder where she's going all of a sudden."
        show natsuki zorder 3 at f43
        n "What do we now? Should we wait for her to get back?"
        n "She was pretty helpful but I think we could do it ourselves in the meantime."
        n "That is, if the three of you are still up for it."
        show yuri zorder 3 at f41
        show natsuki zorder 2 at t43
        y "I'd be happy to try to continue doing this."
        y "But that leaves the problem of Sayori's role."
        y "The stage directions probably aren't necessary but her lines are still there."
        y "And if we just skip over it, I feel like it will reduce the flow of our rehearsal."
        show yuri zorder 2 at t41
        show monika zorder 3 at f42
        m "Well, Ayame is here, right? That gives me an idea."
        m "Maybe she can temporarily fill Sayori's role."
        m "I don't know about her acting abilities but it might be better than simply pretending the line was said."
        show monika zorder 2 at t42
        show ayame zorder 3 at f44
        ay "W-Wait, what? You're talking about me, right?"
        ay "I can't act, no way! I think you're better off without me."
        show monika zorder 3 at f42
        show ayame zorder 2 at t44
        m "It's not going to be a permanent thing."
        m "It's just so we don't lose our tempo, you know?"
        m "Besides, you're basically an official member now."
        m "You should be involved in our activities, right?"
        show monika zorder 2 at t42
        show natsuki zorder 3 at f43
        n "Come on, what's the worst that could happen?"
        n "It's just for fun anyway. If you mess up, nobody is gonna judge you for it."
        show natsuki zorder 2 at t43
        show ayame zorder 3 at f44
        ay "Well...I don't know. It just feels like I shouldn't be doing it."
        ay "Besides, she said she was going to be back pretty quickly."
        ay "Perhaps it's just better to wait it out."
        show yuri zorder 2 at t41
        show ayame zorder 2 at t44
        y "You have nothing to worry about, Ayame."
        y "Just take her copy of the script and follow along."
        y "You don't have to put on an expression or accent if you can't or don't want to."
        show yuri zorder 2 at t41
        show ayame zorder 3 at f44
        ay "Okay, alright. You've convinced me."
        "Ayame picks up Sayori's copy of the script."
        "She looks through it for a while, probably to find where we're up to in the script."
        ay "I think...we were here, weren't we?"
        "She says her line, and surprisingly it was very well done."
        "Despite her saying she can't act, she pretty much did it perfectly."
        "She even said it with the proper expression and did a bit of action too."
        "I can tell I'm not the only one who thought that."
        "The other seem surprised too."
        ay "How did I do? It was terrible, right...?"
        ay "Judging by the look on all your faces, I'm gonna say it was that bad."
        ay "I really tried my best, you know. I guess it wasn't good enough."
        ay "Sorry, I knew this was a--"
        show natsuki zorder 3 at f43
        show ayame zorder 2 at t44
        n "Are you kidding? You're way too modest."
        n "It's that or you're just completely messing with us."
        show natsuki zorder 2 at t43
        show ayame zorder 3 at f44
        ay "What do you mean? The look on all your faces say otherwise."
        ay "Like you've all seen a ghost or something."
        ay "Are you sure you're not the one messing with me?"
        show yuri zorder 3 at f41
        show ayame zorder 2 at t44
        y "The look on my face is one of awe, Ayame."
        y "You say you're not a very good actor but you did an incredible job."
        y "It's like you're a natural at this."
        show yuri zorder 2 at t41
        show ayame zorder 3 at f44
        ay "You mean it? I didn't think I had that kind of talent."
        ay "Usually I mess these kinds of things up and it doesn't end well for anyone."
        show monika zorder 3 at f42
        show ayame zorder 2 at t44
        m "I must say you are full of surprises, Ayame."
        m "Is there anything else that you're apparently bad at?"
        m "Maybe you're actually incredible at it and we could put that talent to use."
        show monika zorder 2 at t42
        show ayame zorder 3 at f44
        ay "No, I'm definitely not that great at a lot of things."
        ay "You should really not have the highest expectations of me, to avoid being disappointed."
        ay "I assure you that this was probably just a one-off thing."
        ay "And I only said one line, so don't expect anything too great based on that."
        show natsuki zorder 3 at f43
        show ayame zorder 2 at t44
        n "You're doing it again, Ayame. You really don't have to do that."
        n "Seriously, you need to have more confidence in yourself."
        n "I can't believe you don't already, with your position in the school."
        show natsuki zorder 2 at t43
        show ayame zorder 3 at f44
        ay "Let's not bring that up, if that's alright with everyone."
        ay "I'd rather just focus on what we have here rather than outside factors."
        "Ayame looks at the script and then back at the group."
        ay "I believe the next line is yours, [player]."
        ay "Perhaps you could continue so that we don't waste any more time?"
        show ayame zorder 2 at t44
        mc "Oh...right, I'll do that now."
        "I know that Ayame is just trying to divert the conversation."
        "I'll just go along with it because she's clearly not comfortable talking about her leadership."
        "Plus, we do need to get at least one rehearsal done."
        "Though everyone seems to be doing really well so far, so even if we can't finish it I'm confident we can get the play done well."
        "I only hope that I can remember the rest of the lines if that ends up happening."
        "Though we should be fine, the only times I really need to look at the script are if I want to confirm what I'm saying."
        "It always ends up being what I'm already thinking."
        "I wonder if the others are feeling that way too...and if they are, how come?"
        "Is it because we all want this play to do well?"
        "Or is there some other reason that we don't know about...?"
        "After a bit of time has passed, we manage to get through a decent amount of the play."
        "Sayori hasn't come back yet but the clock says she hasn't been gone that long at all."
        "Ayame's acting has stayed top notch, it's almost a shame she isn't performing with us."
        show monika zorder 3 at f42
        m "I think we could improve that part a little bit."
        m "Try putting a bit more of an emotional voice behind it."
        m "I just know it will have a better effect to to the audience, you know?"
        show monika zorder 2 at t42
        show natsuki zorder 3 at f43
        n "Okay, I can try doing that."
        n "It just doesn't really suit me...it kinda feels weird."
        show monika zorder 3 at f42
        show natsuki zorder 2 at t43
        m "We're all going to get parts where we don't feel natural saying it."
        m "But that's just part of acting!"
        show yuri zorder 3 at f41
        show monika zorder 2 at t42
        y "I do have to agree with Monika here. The difference could be night and day."
        y "It is just one scene, it's not like you're going to be like that the whole play."
        show yuri zorder 2 at t41
        show ayame zorder 3 at f43
        ay "If I may say something...?"
        ay "I know it's not really my place seeing as I just joined but..."
        ay "If you'd like to hear what I have to say, then maybe it could help."
        show ayame zorder 2 at t43
        show natsuki zorder 3 at f44
        n "Of course! You don't even need to ask about stuff like that."
        n "You're one of us now, whether you like it or not."
        n "You don't need to ask to be able to say something."
        show monika zorder 3 at f42
        show natsuki zorder 2 at t44
        m "You're awfully supportive of Ayame, aren't you Natsuki?"
        m "You weren't like that when [player] first joined the club."
        m "I wonder why that is..."
        show monika zorder 2 at t42
        show natsuki zorder 3 at f44
        n "Is that not allowed? I'm just being nice."
        n "We should be doing our best to make her feel welcome!"
        show monika zorder 3 at f42
        show natsuki zorder 2 at t44
        m "I know, I know! Just such a different reception is all~"
        m "Anyway, go on Ayame. Let's hear what you have to say."
        show monika zorder 2 at t42
        show ayame zorder 3 at f43
        ay "Okay, thank you. I appreciate the thought Natsuki, but I can take care of myself."
        ay "You don't have to defend me."
        "Natsuki stares at Ayame for a moment."
        "After a few seconds, it looks like she's suddenly confused and attempts to hide it."
        ay "As I was saying, I think the emotion part isn't really needed."
        ay "The way you've done your play already means that this whole emotion thing might come so sudden."
        show yuri zorder 3 at f41
        show ayame zorder 2 at t43
        y "What do you mean by that?"
        show yuri zorder 2 at t41
        show ayame zorder 3 at f43
        ay "Well, if you look at the script..."
        "Ayame quickly flips back through the script."
        ay "At this point, here. It's the same sort of premise but none of you commented on the emotion there."
        ay "I just think it would be good to be consistent, is all."
        ay "It's just a thing I noticed. Either it should be in both or neither."
        ay "But that's just my opinion."
        show yuri zorder 2 at t51
        show monika zorder 2 at t52
        show ayame zorder 2 at t54
        show natsuki zorder 2 at t55
        show sayori 1d zorder 3 at f55
        s "I think she's right! I was actually going to point the same thing out when we got there."
        s "But it seems you guys already went past it."
    call screen dialog(message="To be continued!\nThanks for playing, keep an eye out on reddit and discord for updates!", ok_action=Return())
    $ renpy.utter_restart()
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
    show sayori 1bq zorder 2 at t11
    s "Good afternoon, [player]."
    mc "Sayori..."
    mc "You look incredible."
    s 1br "Ehehe~"
    s "You don't look terrible yourself, you know."
    "I look down at what I'm wearing."
    "It's an outfit I've never worn or seen before."
    "I don't think I even own it."
    "Did Sayori do this to me?"
    s 1bd "It's a beautiful day, isn't it?"
    mc "Yeah..."
    s "You wanna sit down?"
    mc "Um..."
    mc "Y-Yeah, sure..."
    "Sayori and I walk around looking for somewhere to sit."
    s 2bc "Remember when we used to go here after school when we were younger?"
    s 2bd "We'd play until our legs gave up."
    mc "That was a long time ago."
    s 2bc "I don't know about you, [player]."
    s 1bl "But I bondly remember those times."
    mc "Bondly? Is that even a word?"
    mc "You mean {i}fondly{/i}, right?"
    s 1bm "Oh...yeah, probably."
    s 1bl "Those words are kinda similar, aren't they?"
    mc "In what way?"
    s 1bb "Well, I feel a bond towards {i}you{/i}."
    s 1bd "And I suppose because of that, I'm fond of you."
    s "But anyway..."
    s 2ba "I'm pretty sure there's a set of swings in here."
    s "It's better than sitting on a bench."
    mc "R-Right."
    "Sayori walks into the park and I follow behind her."
    "There's something...graceful about the way she's walking."
    "Or maybe it's just the dress she's wearing."
    "Once we get into the park, she notices the set of swings and starts running toward it."
    "She gets on one of the swings and I choose the one next to her."
    "I'm still not entirely sure what this is about."
    s 4bq "Remember when we used to swing on these?"
    "Sayori begins swinging, I follow her lead."
    mc "You were always scared of going over the top."
    mc "Even though it was impossible."
    s 5bb "Hey, you were scared too!"
    mc "Ahaha, that's true."
    mc "I can't believe we were that gullible."
    mc "You still are."
    s 5ba "H-Hey!"
    "Sayori and I share a laugh."
    s 4bk "We were more innocent back then."
    s "Don't you think?"
    mc "Innocent?"
    mc "What do you mean?"
    s 4bl "Never mind."
    s "Let's not ruin the moment."
    s 4bq "Let's just enjoy ourselves, okay?"
    mc "Okay."
    mc "What's this about anyway?"
    mc "Why did you bring us here?"
    s 2bd "Isn't it obvious?"
    mc "Um..."
    "Sayori shows a friendly smile."
    s 2bc "Are you..."
    mc "Am I what?"
    s 2bl "How do I put this bluntly...?"
    s "That dense?"
    s 1bd "Take a look around you, [player]."
    "I take a look at my surroundings."
    "We're in a nice park, in the middle of the day."
    "We're both wearing nice clothes and Sayori is acting kinda different."
    "This is..."
    mc "A date?!"
    show sayori 1bq
    "Sayori simply smiles at me."
    mc "But why?"
    mc "I thought we were holding off on it."
    mc "Until after."
    s 1bk "You know what's coming."
    s "I don't know if I'll be able to stop it."
    s "Even with everything you've done."
    mc "So this is..."
    mc "..some sort of escape?"
    s 1bl "Ehehe, kind of..."
    s "It's still lunchtime."
    s "Everyone else is still at school."
    s 1bc "Time is just passing by slower for us."
    mc "You did that?"
    s 1bk "Yeah..."
    s "I realize it's kinda irresponsible."
    s "I could be doing more to prepare..."
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
            s 2bt "Hah..."
            s "You really understand, don't you?"
            mc "I try."
            s "No, you don't."
            s "It's not really you talking."
            s "But I think I understand."
            mc "What do you mean?"
            s 2by "N-Nothing."
        "Be who you are.":
            $ ch16_s_date_personality = False
            mc "I don't really get it."
        "Stay quiet.":
            $ ch16_s_date_personality = False
    "Sayori sighs."
    s 1bk "You know, I can still hear your thoughts."
    s "Sometimes, I only hear whispers."
    s "The important bits."
    s 1bh "Other times..."
    "Sayori puts her feet on the ground to slow her swinging."
    s 1bk "...when I'm feeling down..."
    s "I actively listen to what you're thinking."
    s "I don't know why but it just makes me feel better."
    s "Knowing that you're out there doing things..."
    s 3bj "It's like I'm there with you."
    mc "That's..."
    s 3bl "Pretty creepy, right?"
    s "I know."
    s "I guess it's kind of an invasion of privacy."
    s 3bm "But I promise I didn't listen in any time something weird was happening!"
    s "Just things like you writing your poems or studying."
    s "That's why sometimes I know what you're thinking before you even say it."
    s 3bk "I'm sorry."
    mc "It's okay."
    mc "I'm not sure what I'd do with the kind of power you have."
    mc "I guess I can't really blame you for doing something like that."
    mc "After all, you're looking out for us."
    mc "I'm sure we wouldn't have made it this far without you."
    s 1bc "I haven't done it lately."
    s "Until now, that is."
    s "I've just been too busy."
    s 1be "With...you know."
    s 1bd "But it's kinda weird knowing what your date is thinking."
    s "So..."
    s "I'll turn it off."
    s 1bf "Permanently."
    mc "What?"
    mc "Why permanently?"
    s 1bd "It's just better that way."
    s "Besides, it will make things later a lot easier."
    if ch16_s_date_personality:
        "There's obviously something that's bothering her."
        "Something that goes beyond this date, probably."
        "I'll have to keep a look out for it."
    else:
        "A lot easier later...?"
        "What could she mean by that?"
    s 1bh "You know, there's someone out there."
    mc "Out where?"
    s "I feel really guilty for bringing you here."
    s "When I don't really feel that way about you."
    mc "I'm not sure I understand."
    s "There's been someone helping me this whole time."
    s "Someone that helped all of us get this far."
    s 1bj "Without [player_reflexive], I wouldn't be sitting here."
    s "And neither would you."
    s 1bf "I suppose in another reality [player_personal] would have gone for someone else."
    s "Maybe I'm not even [player_possessive] first choice..."
    s 1bg "But I don't care."
    s 1bd "You're here with me."
    s "And because of that {i}you're{/i} with me."
    if ch16_s_date_personality:
        "I guess it all makes sense."
        "Because of whoever this person is..."
        "Sayori is happy."
        "But what do I have to do with all of this?"
    mc "What's this person got to do with me?"
    s 2bb "Think of yourself as an avatar."
    s "An extension of that person."
    s "Through you, they can see this world."
    s "They can experience it, just like you and me."
    s 2bc "Though I suppose it would be a lot different."
    s "[cPlayer_personal]'s probably looking at us through a screen."
    s "But you get it, right?"
    mc "What's the point of telling me this?"
    s 2bh "Because, [player]."
    s 2bk "I don't love you."
    s "I love [player_reflexive]."
    "Sayori stops swinging completely."
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
    s 4be "You're taking this a lot better than I thought."
    s "I thought maybe I'd have to use my abilities on you."
    mc "I get it, Sayori."
    mc "I'm hurt but I get it."
    s "So what are you going to do?"
    mc "I'm an extension of this person."
    mc "Which means I have to be here for [player_reflexive] to be with you."
    mc "That's right, isn't it?"
    s 4bh "Yeah..."
    mc "I have this feeling of..."
    mc "...I guess {i}anger{/i} towards [player_reflexive]."
    mc "Because [player_personal]'s taken you away from me."
    s 4bk "..."
    mc "But..."
    mc "Out of all my feelings..."
    mc "I want you to be happy."
    mc "Since I'm a part of [player_reflexive], I suppose [player_personal] wants that too."
    mc "So..."
    mc "I'll let the two of you be happy."
    mc "Together."
    s 3bh "[player]..."
    s "I...I don't know what to say."
    mc "You don't have to say anything."
    if ch16_s_date_personality:
        mc "But just tell me."
        s 3bc "What?"
        mc "Was [player_personal] always a part of my life...?"
        s 1bd "[cPlayer_personal] wasn't always a part of your life."
        s "[cPlayer_personal] became a part of you just a couple of weeks ago."
        mc "When I joined the club."
        "Sayori nods."
        mc "Then what about your feelings towards me?"
        mc "Did you ever love {i}me{/i}?"
        mc "As who I was?"
        mc "Before this other person came?"
        s 1bh "I..."
        s "I don't know."
        s "Those thoughts of having this uncontrollable affection towards you..."
        s "They might have been part of this world's conditioning."
        s "I removed them because it just made sense, right?"
        s 1bj "If I really loved {i}you{/i}, then I would fall in love with you all over again."
        s "But..."
        mc "Alright."
        mc "You don't need to explain yourself to me anymore."
        if ch15_s_kiss_choice:
            s 1bk "Let me just say..."
            mc "What?"
            s "Yesterday."
            s 1bj "When you...kissed me."
            mc "It wasn't my choice to make."
            mc "I know that now."
            s 1bh "Maybe not..."
            s "But I could feel your own passion."
            s "It..."
            show sayori 1bk
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
    s 1bd "Thank you."
    s "I suppose we should probably get started then."
    s "There's so much to do and so little time to do it."
    mc "You have a plan?"
    mc "I guess I shouldn't really be surprised."
    mc "You've gotten your life in order lately."
    s 1ba "It's always good to have a plan."
    s "Especially when we have such a limited time window."
    s "But not for this."
    s "I want to have fun even if this whole thing doesn't really work out."
    s 2bl "So it's not really planned."
    s "It's more like..."
    s "I have places I want to go."
    s "But we don't have to go there."
    mc "That sounds kinda like a plan."
    mc "Not a good one but...you know."
    s 5bc "You don't need to be a meanie."
    s "The date has only just begun."
    mc "Ah, sorry."
    mc "I didn't mean to."
    mc "A-Anyway, where did you wanna go first?"
    mc "We're on some sort of time limit, like you said."
    mc "So we have to make use of the time we do have."
    "I wonder just how long we actually have."
    "It's lunchtime at school now so we would have just under an hour if it lasted that long."
    "Maybe she'll use some of her powers to make time go slower or something."
    s 4bc "This was the first place."
    s "It's just so peaceful at this hour."
    s "We can just admire the atmosphere."
    mc "We haven't really been able to do that, have we?"
    s 4bk "No, we haven't."
    s "I don't know about you but I've been really busy."
    s "There's rarely a moment I have time to spare."
    s "Not to mention all of the things I've been doing for you guys."
    mc "Wow."
    mc "Well, I haven't really been as busy as you."
    mc "I've just been lazy to go out."
    mc "I don't really have an excuse."
    mc "It is nice out here though..."
    s 1bd "Yeah..."
    "Sayori gets up from the swing."
    s "Come on."
    s "We'll come back later."
    mc "Where are we going?"
    s 1bq "You'll see."
    s "It's not far from here."
    "Sayori begins walking and I walk alongside her."
    "After a few minutes, she stops suddenly."
    mc "What is it?"
    s 1bo "I just realized it's actually a lot further than I thought."
    mc "Okay, so what now?"
    s 1br "We can always take a shortcut."
    mc "A...shortcut?"
    s "Only I can really use it."
    s "But I can bring people along."
    mc "What kind of shortcut is that?"
    s 1bq "Ready?"
    mc "For{nw}"
    $ _history_list.pop()
    scene bg lake_day
    show sayori 1bq zorder 2 at t11
    mc "For{fast} what?"
    "Before I can even finish what I'm saying..."
    "We're suddenly at some kind of lake."
    "I don't think I've ever been here before."
    "You really are special to her."
    mc "What is this place?"
    s 2ba "It's a lake I found."
    s "It's actually in a restricted area."
    s "It's even got a fence around it."
    mc "How come?"
    s 2bl "Because people aren't really allowed to be here."
    mc "What?!"
    s 2bd "Relax."
    s "Nobody uses this place."
    s 2bb "It's meant to be a place where fossil fuels were mined."
    s 2bc "But there was so much protesting that the company was basically kicked out."
    s "They still own the place but I guess they don't want anyone to enjoy it either."
    s "That was a couple of decades ago..."
    s "They still haven't let people use it."
    mc "Oh."
    mc "Can't you do anything about it?"
    mc "This place is amazing."
    mc "It would be a shame if no one else could enjoy it."
    s 1bd "I could."
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
        s 1bm "W-Wow, I didn't expect that kinda answer from you."
        s "I was just gonna say that this wouldn't be my secret spot anymore."
        s "Now that I think about it, you're right."
        s 1bn "I guess I could become corrupt..."
        s 1bk "Who's to say I'm not already though...?"
    else:
        "I can't really think of a reason why doing a good deed would be bad."
        mc "What would happen?"
        s "Well..."
        s 1bk "You know what, it's not important."
    "Sayori stares at the lake."
    "There's a gentle breeze flowing yet the water is still."
    "This place feels quite serene."
    "I can see why she chose this place."
    mc "How did you find it anyway?"
    s 1bc "Someone told me about it."
    s "I thought I'd check it out."
    "Who could that somebody be?"
    "It might be someone we both know..."
    s 1ba "We're not the first ones to sneak in here."
    s "I think lots of people do."
    s "Not like it's under watch or anything."
    mc "It's a shame it's not more easily accessed."
    s 1bo "Yeah..."
    s "There's actually a rumor going around about this place."
    s "From people who've snuck in."
    mc "What is it?"
    s 1bm "They say at night, there's a red ghost that travels around the forest."
    s "It tends to the flowerbed just across the lake, which is why it's in pristine condition."
    s "No one knows if the ghost could actually hurt anyone or not."
    s 2bm "But people have said they've heard it crying when they've been close."
    mc "Ghosts?"
    mc "That's a little superstitious, don't you think?"
    s "Maybe."
    s 2bl "That's just what I've heard."
    s "For all we know, it could just be a groundskeeper wearing red clothing."
    s "Even if it was real, it wouldn't be the weirdest thing I'd have seen if it was true."
    mc "Who only works at night."
    s 4bd "It could just be made up."
    s "But because of that rumor, people say this place is haunted."
    mc "What do you think?"
    s "As long as we're here during the day, it shouldn't matter."
    s "After all, this ghost has only been seen at night."
    s 4ba "Which is why..."
    mc "You want to go to the flowerbed?"
    s 4bq "Exactly!"
    s "I don't want to pick any of the flowers."
    s "I'm sure the ghost, if it exists, would be really sad if I did that."
    s 4bd "Knowing all the hard work it's put into it."
    mc "Does this flowerbed even exist?"
    mc "Have you seen it yourself?"
    s 2bc "Nope!"
    s "I've never actually been to the other side of the lake."
    s "So it'll be my first time."
    s 2bq "And it'll be with you."
    "Sayori shows me a warm smile."
    menu:
        s "What do you say?"
        "Let's check the flowerbeds.":
            $ ch16_s_date_activities += 1
            mc "I guess we'll check the flowerbeds."
            mc "Or at least look for them."
            s 2bd "I'm glad you made that choice."
            s "I'm excited to see just what kind of flowers are even here."
            mc "Has anyone crossed the lake before?"
            s 2bb "Plenty of people."
            s 2bc "Someone even made a little wooden bridge."
            s "So let's go."
            mc "Lead the way."
            scene bg river_day
            show sayori 1bb zorder 2 at t11
            with wipeleft_scene
            "Sayori and I make our way around the lake."
            "There's a part where the lake converges and turns into a small river."
            "The current is flowing slowly so there's really no danger at all."
            "Like she said, there's a small bridge connecting both sides of it."
            "It looks pretty sturdy too."
            "I was expecting something that was barely being held together."
            "Maybe people {i}do{/i} do this a lot."
            "Especially if the bridge is this well made."
            s 1ba "Shall we?"
            "Sayori steps on the bridge and offers me her hand."
            "I take it and she pulls me next to her on the bridge."
            s 1bd "It's so peaceful here, isn't it?"
            s "You can hear the birds singing and the river flowing."
            mc "It's a tranquil environment."
            mc "Especially since no one really goes here."
            s "That's right."
            show sayori 1ba zorder 2 at s11
            "Sayori sits down on the bridge."
            "I sit down next to her."
            s 1bq "Before we get to the other side..."
            s "I just want to take this moment to take it all in."
            s "Who knows what awaits us on the other side?"
            mc "Are you scared?"
            s 1bl "Scared?"
            s "Ahaha~"
            s 4bq "I'm excited, if anything."
            s "Those flowerbeds have a reputation and I want to see them."
            s "But if we just skip past all of nature's beauty that we can see now..."
            s 4br "Then how can we truly appreciate the flowers?"
            mc "I guess..."
            mc "I'm not really one to do this kinda thing."
            mc "But I wanna try."
            s 4bd "Ehehe, I don't wanna force you to do anything you don't want to."
            mc "No, the choice was made."
            mc "If this is what we're doing then I should try."
            mc "I just need...guidance."
            s "I can't do that."
            s 2bd "Doing something like this...it just happens, naturally."
            s "Just breathe in the atmosphere."
            "Sayori takes a deep breath then exhales."
            s 1bd "Just like that."
            "I take a deep breath."
            "I can feel the fresh air enter my lungs."
            "I can feel the sun on my face and the wind on my back."
            "I can hear the gentle current the water below us is carrying."
            "And the warmth of Sayori's presence next to me."
            s 1ba "If you wanna take in the rest of the sights, we can do that."
            s "There's no {i}real{/i} rush."
            s "But I'm going to need to change a couple of things for that to happen."
            "I exhale my breath and as I do, the world seems to be moving slower."
            "The current of water seems to stop and the leaves on the trees stop fluttering."
            s 1bl "Don't move around too much."
            s "I'm not sure how long I can hold this."
            mc "Did you freeze time or something?"
            s 1bd "I guess that's the best way to put it."
            s "Normally, while the world is in this state I can do what I want."
            s "I would literally have all the time in the world."
            s 1bc "And it would be like nothing happened at all..."
            s "Only I would experience this moment of frozen time."
            s 1bq "But I've shared it with you."
            s 1bl "It's a bit harder but I'll manage."
            mc "You don't need to do that for me."
            s 1bd "But I want to."
            s "After all, it wouldn't be a date if we didn't both enjoy ourselves."
            s "And I don't want to make this any worse for you either."
            s "It's better to let you in on it, rather than keep you in the dark."
            s "After all, you're helping to make this possible."
            mc "..."
            if ch16_ay_perspective:
                $ currentpos = get_pos()
                show screen tear(8, offtimeMult=1, ontimeMult=10)
                window hide(None)
                stop music
                scene bg school_grounds
                $ pause(1.0)
                hide screen tear
                $ pause(1.0)
                window show(None)
                "It's happening again.{fast}"
                window auto
                $ style.say_dialogue = style.edited
                "And yet you're not affected."
                "Once again."
                "Why do you think that is, hmm?"
                $ style.say_dialogue = style.normal
                "Where is [player_personal]?"
                "[cPlayer_personal] was just here..."
                "Dammit."
                $ style.say_dialogue = style.edited
                "Why are you even chasing after [player_reflexive]?"
                "It's not like [player_personal] loves you."
                "Or ever will."
                $ style.say_dialogue = style.normal
                "It's not about that."
                "I just feel this resonance towards [player_reflexive]."
                "I need to know what it is."
                $ style.say_dialogue = style.edited
                "You don't want to find out the source of these time stops?"
                "Seeing everyone frozen like this doesn't bother you?"
                "AT ALL?"
                $ style.say_dialogue = style.normal
                "I don't know the reason why it's happening."
                "It's happened before and fixed itself."
                "There's no reason I should be concerned."
                $ style.say_dialogue = style.edited
                "Ayame, your logic is flawless."
                "The world is completely stopped."
                "You aren't worried at all simply because it fixed itself."
                "Think critically for a moment."
                "Don't you think there's a reason only {i}you{/i} can move during these?"
                $ style.say_dialogue = style.normal
                "Why are you bothering me?"
                "I didn't ask for your opinion."
                "So just shut up!"
                "Shut up!"
                "Shut up!"
                $ style.say_dialogue = style.edited
                "I'm just trying to help you."
                "After all, we're one and the same."
                "All I'm saying is..."
                "Maybe you can do something about this stopped time."
                $ style.say_dialogue = style.normal
                "I can't."
                "There's no reason I should be able to."
                "I can't just will things to happen!"
                "I take a seat down on the bench."
                "I guess I'll just wait this out."
                "Suddenly, a ball rolls out to my feet."
                "It was frozen before..."
                "Does that mean...?"
                "Student" "\"Hey, can you kick that back to us?\""
                "I oblige and kick the ball back to the group of students playing on the field."
                "Did I do this?"
                "What..."
                "...the..."
                "...hell?{nw}"
                show screen tear(20, 3, 2, 0, 70)
                window hide(None)
                $ pause(1.0)
                scene bg river_day
                show sayori 1bd zorder 2 at s11
                hide screen tear
                $ pause(1.0)
                $ audio.t12sb = "<from " + str(currentpos) + " loop 1.300>mod_assets/bgm/12_sayori.ogg"
                play music t12sb
                window show(None)
                "Was that...right now?{fast}"
                window auto
            s 1bo "What's wrong?"
            mc "Um..."
            "I can feel the world around me moving again."
            "It's slow but it seems time isn't completely stopped."
            s 1bn "Oh..."
            s 2bl "I guess I {i}couldn't{/i} manage."
            s "That's weird but not unexpected."
            "It seems the river is flowing normally again."
            "I guess time is back to normal?"
            s 2bd "Well, we should get moving then."
            show sayori at t11
            "Sayori gets up and begins walking to the other side."
            if ch16_ay_perspective:
                "Did Sayori make time move again or..."
                "...was it someone else?"
            mc "R-Right."
            "I follow Sayori across the bridge."
            "As soon as we step wooden bridge, the whole atmosphere feels different."
            "It's more serene."
            "As if we're in a completely new place."
            s 1bc "You can feel it too, can't you?"
            s "It's different here."
            s 1bd "Like we're isolated from the world."
            mc "Do you know why?"
            s 1bb "No, I don't."
            s 1ba "But that just makes me feel more excited."
            mc "How come?"
            s 1bq "Learning new things is exciting."
            s "It's the whole reason we even go to school."
            s "To learn new things and experience things we otherwise wouldn't."
            s 4br "And this is just like that."
            mc "Neither of us have any idea what we're going to find here."
            mc "Except flowerbeds."
            s 4bd "The flowerbeds are only half the fun!"
            s "Exploring somewhere you've never been before and finding it's secrets."
            s 4bc "Plus it's 'haunted'."
            s 4bd "Tell me that doesn't excite you, even a little bit."
            mc "I guess you're right."
            mc "There is a bit of me that's curious to know what's really here."
            s 2bq "Then let's go!"
            "Sayori takes my hand and drags me further into the forest."
            "As we go deeper in the forest, I start to notice something unusual."
            "Before we crossed the river, I could notice butterflies and bees in the background."
            "They weren't really obvious, but I could just see them flying around the flowers."
            "When I look at the flowers here, it's completely dead."
            "There doesn't seem to be any living thing here."
            "Except the two of us."
            mc "Have you noticed...?"
            "Sayori turns around but doesn't stop her pace."
            s 2bb "It's so empty here."
            s 2ba "Spooky, isn't it?"
            mc "If there's no living things here, I wonder how all the plant life manage to stay alive."
            s 2bc "That's a good point."
            s "They'd need bees to be able survive and flourish like they have."
            s "Maybe this mysterious ghost also pollinates the flowers."
            mc "You think he can do that?"
            s 2ba "Who knows?"
            s "Maybe there's just insecticide all over here and we don't know it."
            s 1bd "This place is just full of mystery."
            s "Now, come on."
            s "I think we're getting close to the flowerbed."
            scene bg forest_day
            show sayori 1ba zorder 2 at t11
            with wipeleft_scene
            "We walk further into the forest."
            mc "What do you expect we'll find there?"
            s 1bc "If we're lucky, the ghost."
            s "Though I'm not sure how he'll react to seeing us."
            s "Or if 'he' is even a he."
            s 1bb "This ghost is such a mysterious character."
            s "We don't even know if he exists."
            s "All we have are rumors and superstition."
            mc "I thought the ghost only appeared at night."
            s 1ba "That's true."
            s "But I have an idea."
            mc "An idea...?"
            mc "Sayori, you don't actually plan on bringing him out do you?"
            mc "What if he's hostile?"
            mc "What if he's stronger than you?"
            s 2bd "Do you know who you're talking to?"
            s "If things go sour, I can always make it so it never happened."
            s "Though I hope it never has to come to that."
            s "I just want to meet whoever this is."
            s 2bc "Maybe learn why he's doing this."
            s 2ba "He might even tell us his story."
            mc "And if not?"
            s 1bq "We get to see the flowerbeds."
            s 1br "It's a win-win."
            mc "If you say so..."
            s 1ba "Come on, I think we're almost there."
            mc "How can you tell?"
            s "Aside from the increase in flowers?"
            s 1bc "I can sense a presence."
            s "It's very faint...I wouldn't be able to tell if I wasn't really paying attention."
            s 1bb "It helps that it's in this silent part of the forest, it makes the presence very distinct."
            s 2bn "Come on, this way!"
            scene bg flowerbed
            show sayori 1bn zorder 2 at t11
            with wipeleft_scene
            "We arrive at a clearing filled with flowers."
            "This must be the renowned flowerbeds."
            "There is quite literally flowers everywhere you look."
            "In one section there's flowers of one color."
            "And in another section there's flowers of another color."
            "It seems like there's an endless stream of flowers and colors all around us."
            "It's a lot to take in."
            mc "It's so..."
            s 1bd "...beautiful."
            mc "Yeah..."
            mc "The time and effort needed to maintain this place..."
            mc "I can't even begin to imagine."
            s 1bb "Hmm."
            "Sayori walks around the area."
            "I follow her, making sure to take in everything."
            "It's still quite overwhelming seeing how amazing this place is."
            "I guess the rumors were true."
            mc "What are you doing?"
            s 1bc "Looking around."
            s "I wanna make sure I have an understanding of our surroundings."
            mc "For what?"
            "Sayori suddenly stops."
            s 2be "Stop for a second."
            s "We're here."
            "I have no idea what Sayori has planned."
            "If it involves somehow getting the ghost to appear, I can only imagine it's not good."
            s 2bo "Do you hear that?"
            s "There's a faint humming."
            mc "I can't hear it."
            s 2bc "It's utterly silent here apart from us."
            s "Even the wind isn't making any noise."
            s 4bd "Just focus."
            "I try my best to hear the sound she's talking about."
            "I attempt to clear my mind of everything."
            $ currentpos = get_pos()
            stop music fadeout 1.0
            play sound "sfx/gnid.ogg"
            $ pause(7)
            $ audio.t12sb = "<from " + str(currentpos) + " loop 1.300>mod_assets/bgm/12_sayori.ogg"
            play music t12sb
            "It's faint."
            "But I think I heard it."
            mc "What is that sound anyway?"
            s 4bc "I'm almost certain it has to do with the ghost."
            s "It's strongest where we're standing right now."
            mc "But it's so quiet."
            s 3ba "Which is why no one has ever seen him during the day."
            s "No one knows where to look."
            s "You wouldn't even realize there was ringing until you were standing right here."
            s 3bb "I only noticed it because of this thing's odd presence and the forest's odd silence."
            mc "What's the plan now then?"
            s 3bc "From what I've heard, everyone who has made this far has not dared to take a single flower."
            s "So--"
            mc "You're not going to do that, are you?"
            s 3bl "No, of course not!"
            s "That would be really disrespectful."
            s 1bh "There is another way, I'm sure of it."
            mc "What is this other way then?"
            mc "Are you going to make it night?"
            s 2bl "Ehehe, not exactly~"
            s 2bb "Just watch, it's kinda difficult to explain."
            "Sayori takes a step back and points her palms towards the ground."
            "She then says something under her breath that I can't really hear."
            "Afer repeating it a few times, she stops and turns around to look at me."
            s 2bc "Well..."
            s 2bd "...that was draining."
            mc "What exactly did you do?"
            s "I'm not sure what it was if I had to, I'd describe it as something similar to magic."
            s 1bc "But in reality, it's just a way to call people."
            s "It takes a lot of energy to call someone."
            mc "When you say call someone--"
            s 1bj "I don't mean on their phone."
            s 1bh "Basically, it's like saying their name."
            s "It's like if I said [player] a bunch of times."
            s "You'd eventually come, right?"
            mc "If I could hear you."
            mc "But you sounded like you were whispering."
            s 1bd "That's probably what it sounded like to you."
            s "To the ghost, it might have sounded like someone yelling right into his ear."
            mc "How do you know the ghost's name?"
            mc "I don't suppose the rumors mentioned a name."
            s 1bl "They didn't."
            s "You could say I cheated to find out his name."
            s "If I look deep enough into this world, I can see everything."
            s 1bk "It's dangerous going that deep."
            s "But I've managed to figure out a way to make the danger smaller."
            s "When I peered into it for just a moment, I found something unusual."
            s 1bh "I could only assume it was a name."
            mc "Sure."
            "I'm not sure exactly what she's talking about."
            "But I'm assuming you do...?"
            "After a few minutes of standing around, nothing happens."
            mc "I don't think he's coming."
            s 2bf "That's a real shame."
            s "I would have thought we'd get to see the ghost."
            mc "We don't even know if he exists."
            if ch16_s_date_personality:
                mc "It's possible that everything so far is just a coincidence, isn't it?"
                mc "And even if they weren't coincidence, he's only been spotted at night."
                mc "I doubt that's going to change."
            else:
                mc "Maybe he's just resting right now."
            s 2bd "Ah, you're probably right."
            s "I guess I just wanted to show you how far I'd go for you."
            s 2bf "Sorry that we couldn't get the ghost to appear."
            mc "It's not like it's your fault."
            mc "You can't just force things to happen the way you want."
            mc "Sometimes life is just like that."
            s 1bk "Yeah..."
            "Sayori looks at the distance."
            mc "Everything okay?"
            s 1ba "J-Just fine."
            s "I was just thinking back."
            s 1bd "It doesn't matter anymore, anyway."
            s "Come on, we might as well enjoy the flowerbeds while we can."
            s "This is only stop number one after all!"
            "Sayori grabs my hand and pulls me towards the ground."
            show sayori at thide
            hide sayori
            "Because it was so sudden I don't fall as gracefully as she does."
            "Despite that, she made sure we didn't land on any of the flowers."
            s "It's so nice here."
            s "I wish we could stay here forever."
            mc "I don't think the ghost would appreciate that."
            mc "After all, he still has to tend to his garden."
            s "Ahaha, you're right."
            s "So we have to make use of the time we do have."
            s "Because life is like a flower, isn't it?"
            mc "You're gonna have to explain why that is."
            s "Think about it."
            s "At the beginning, we're nothing."
            s "Simply seeds waiting to grow."
            s "Then we reach a stage of our lives where we flourish."
            s "Where we can show the world who we really are!"
            s "Until..."
            mc "Until...?"
            s "Until we slowly wither away."
            s "Slowly wilting away from the world until eventually, we're completely forgotten."
            mc "That's...wow."
            s "Which is why we need to savor life."
            s "Take it all in, [player]."
            s "Today could be your last day in this world."
            s "And you wouldn't even know it."
            mc "I guess you're right."
            "Sayori and I lay here for a few minutes."
            "We don't say a word to each other."
            "I think we mutually understand what kind of moment this is."
            "And I know she isn't here for me."
            "But at the very least, I can enjoy this moment for myself too."
            s "Ready to go?"
            mc "Ready when you are."
            s "Let's head back to the lake then."
            scene bg lake_day
            show sayori 1bq zorder 2 at t11
            with wipeleft_scene
            "Sayori and I make it back to the lake."
            "On the way back, I could feel the environment around me change."
            "It was most noticeable when we crossed the bridge."
            "There were insects across the bridge but it's as if none of them knew this other side existed."
        "Let's do something else.":
            mc "I don't think going to a haunted flowerbed is a good idea."
            mc "Maybe we can do something else."
            s 1bb "That's you've decided, is it?"
            s "I see."
            s 1bc "Well, we can always walk around the place."
            s "I'm sure It's got lots of hidden wonders."
            s "Shall we?"
            mc "Let's go."
            "Sayori and I walk around the lake."
            "There's actually a lush forest area that surrounds the lake."
            "There's a small river cutting off half of the forest area."
            "I assume that's where the flowerbed is."
            "I can spot a small wooden bridge but Sayori seems to ignore it."
            "Where is she taking us?"
            "We move down the river a little bit, the further down we got the more abandoned equipment we see."
            "I can only guess that's from the company that tried to mine out the area."
            "After walking for a couple of minutes, she comes to a stop in front of some sort of large machine."
            s 1ba "Do you know what this is?"
            mc "I don't know what it's called."
            mc "But it takes stuff and moves it somewhere else, right?"
            s "I think it's called an excavator."
            s "I don't know why, but the company left it here."
            s 1bb "Along with all this other abandoned equipment."
            mc "Strange that they just left it here."
            mc "I would have thought they'd have taken all their stuff back."
            s 2bd "Maybe they planned to use it again at some point."
            s "Who really knows?"
            "Sayori begins to climb on the excavator."
            mc "W-What are you doing?"
            s 2bq "What does it look like?"
            s "Come on, you'll be fine."
            mc "It's not me I'm worried about."
            mc "Falling from there could seriously hurt you."
            s 2br "Falling from where?"
            "Sayori climbs onto the arm part of the excavator."
            s 2ba "From here?"
            mc "Are you just teasing me?"
            s 4bq "Just get up here."
            s "I promise nothing bad will happen."
            mc "I'm not exactly the best climber."
            s 3ba "Here."
            "Sayori offers me her hand."
            "I take it and she pulls me up with ease."
            "I guess that's how she handled the box so easily..."
            show sayori at s11
            "We both take a seat on the arm of the excavator."
            "It's positioned so that it's probably in the most sturdy position it could be."
            s 3bd "At times like this, I'd say to take in the beauty of nature."
            s "But right now..."
            show sayori 4bd
            "Sayori extends out her arms as if to showcase where we are sitting."
            s "We're surrounded by machinery."
            s 4bh "Tools left by a once greedy company."
            s "So it might be kind of hard to appreciate it, you know?"
            mc "I wouldn't really know anything about that."
            mc "I'm not exactly a nature person."
            s 1ba "Just take a deep breath and concentrate."
            s "You'll be able to take everything in that way."
            s "Give it a try now."
            mc "If you say so."
            "I take in a deep breath."
            "The air is fresh but there's something about it."
            "Some kind of metal aspect about it I can't really determine."
            "I can feel the wind on my back."
            "I can feel the cold steel that I'm sitting on."
            "And the warmth of Sayori's presence next to me."
            s 1bd "Taking it all in, [player]?"
            mc "I guess so."
            mc "Like I said, I'm not really good at this."
            mc "But I wanna try to be."
            s 1bq "Ehehe, well you don't have to force yourself."
            s "Besides, there are more fun things we can do."
            mc "Like what?"
            s 1bl "Well...do you think this thing still works?"
            mc "You can't be serious."
            "She hops off the arm and approaches the door to the driver's seat."
            "She's serious."
            "I get off the arm and gracefully tumble on the ground."
            mc "Do you even know how to use this thing?"
            s 1bn "I've got no idea!"
            mc "This is a terrible idea!"
            mc "How are you even going to turn it on?"
            mc "I doubt they left the keys in there."
            s 1bd "I'll make my own."
            mc "What?!"
            "Before I can even approach the driver's seat, the excavator roars to life."
            mc "Sayori..."
            s 2bq "Come on in."
            "The excavator is only suited for one person at a time."
            "She squeezes a bit so that I can fit in too."
            mc "What are you planning?"
            s 2ba "This clearing seems like a good place to just mess around, doesn't it?"
            s "There's plenty of space and we aren't really going to ruin the scenery."
            mc "I suppose."
            s "Now, let's see how this goes."
            "Sayori steps on one of the pedals and the machine grinds forward."
            s 2bq "See, I'm an expert already?"
            mc "Just be careful."
            mc "This might have been abandoned for a reason, you know."
            "Sayori pulls on one of the levers and the arm changes position."
            s 4bo "I have another idea."
            mc "Don't tell me--"
            s 4bc "You drive for a minute."
            "She forces herself out of the driver's compartment and climbs onto the arm."
            "How can she climb so well in a dress?"
            "She stands on it proudly before turning around and seeing my face."
            "She laughs."
            s 4bq "Your face is priceless, [player]!"
            s "You just look so worried and clueless."
            s 3br "Come on, I bet you can't shake me off."
            "She's having way too much fun here."
            "It's almost infectious."
            mc "Oh yeah?"
            mc "How about this?"
            if ch16_ay_perspective:
                $ currentpos = get_pos()
                show screen tear(8, offtimeMult=1, ontimeMult=10)
                window hide(None)
                stop music
                scene bg school_grounds
                $ pause(1.0)
                hide screen tear
                $ pause(1.0)
                window show(None)
                "Where is [player_personal]?{fast}"
                window auto
                "[cPlayer_personal] should be right here."
                $ style.say_dialogue = style.edited
                "Stop this."
                "Your effort and time are wasted looking for [player_reflexive]."
                $ style.say_dialogue = style.normal
                "I know [player_personal]'s around here."
                "I just know it."
                $ style.say_dialogue = style.edited
                "Are you sure?"
                "You and I both know [player_personal]'s no longer here."
                "You just don't want to admit it."
                $ style.say_dialogue = style.normal
                "..."
                $ style.say_dialogue = style.edited
                "Why are you so curious about this [player_gender]?"
                "Why are you vying for their attention so much?"
                "Have you developed feelings of love overnight?"
                "Pathetic."
                $ style.say_dialogue = style.normal
                "I don't need to take that from you."
                "I'm the one in control here."
                "I can simply ignore you and pretend you don't exist."
                $ style.say_dialogue = style.edited
                "And yet, here you are."
                "Arguing with yourself in your own head."
                "We're one and the same, you know that."
                "And this false pretense of love is--"
                $ style.say_dialogue = style.normal
                "It's not love."
                "It's something else."
                "Something I need to take to [player_reflexive] about."
                "I feel this resonance towards [player]."
                "I don't know why."
                $ style.say_dialogue = style.edited
                "Whatever your reason..."
                "[cPlayer_personal]'s no longer at school."
                "You know I'm not lying."
                $ style.say_dialogue = style.normal
                "I need to find [player_reflexive].{nw}"
                show screen tear(20, 3, 2, 0, 70)
                window hide(None)
                $ pause(1.0)
                scene bg lake_day
                show sayori 3br zorder 2 at s11
                hide screen tear
                $ pause(1.0)
                $ audio.t12sb = "<from " + str(currentpos) + " loop 1.300>mod_assets/bgm/12_sayori.ogg"
                play music t12sb
                window show(None)
                "My hands are already on the lever Sayori pulled earlier.{fast}"
                window auto
            "I pull the lever and the arm changes position again."
            s 3bm "Whoa!"
            "Sayori shakes a little bit before finding her balance again."
            s 3bq "You're gonna have to try harder than that!"
            mc "Are you sure about this?"
            mc "I can show you no mercy."
            "Sayori looks down towards me."
            s 3bs "Do your worst."
            mc "It's your funeral."
            "Sayori tightens her grip on the arm."
            "I frantically pull the lever and randomly press the buttons on the dashboard."
            "The machine roars to life and starts moving around wildly."
            s 1bm "Whoa!"
            "Somehow, Sayori manages to hang on."
            "I can't believe she actually stayed on the arm."
            s 1bq "Nice try."
            s "But I don't think you can beat me."
            mc "What's your secret?"
            mc "Do you have some sort of hidden strength I don't know about?"
            s "Ehehe, it's all technique."
            s 1ba "You just gotta know how to stand when it's moving a certain way."
            s "N-Now, can you stop this thing?"
            s "I can't get down."
            mc "Giving up?"
            s 1bd "Hardly!"
            s "There's more to this place than some abandoned machine."
            s "So I want to look around some more."
            mc "Sure..."
            "Luckily for her, there is a simple off switch."
            "After pressing it, the machine slowly stops but maintains the position of its arm."
            "Which means Sayori is at the height of it."
            mc "Do you need me to lower it?"
            s 2bc "N-No, I'll be fine."
            s "Just move over a bit."
            "I take a step backwards and watch Sayori."
            mc "What are you--"
            "Sayori jumps off the arm and gracefully lands on her feet."
            "If I tried to do the same thing, I would probably break my leg."
            mc "Any more surprises I should know about?"
            s 1bl "You'll find out~!"
            s "Come on, there's more to see this way."
            mc "Wait, your dress."
            s 1bc "Huh?"
            "Sayori takes a look at herself."
            "It seems some of the dirt from the excavator messed up her dress a little."
            s 1bh "Oh...I didn't even realize it got all dirty like this."
            s 1ba "Hold on just a second."
            "Sayori spins on the spot and suddenly her dress looks good as new."
            mc "You really don't hesitate to make use of your powers, do you?"
            s 2bd "Well, I wouldn't want to ruin the date because of a dirty dress."
            s "Come on, there's something you should see."
            "Sayori takes my hand and starts heading deeper into the forest."
            scene bg forest_day
            show sayori 1bq zorder 2 at t11
            with wipeleft_scene
            "We trek through the forest for a few minutes."
            "I'm not sure where she's leading us but the further we get into the forest, the more at ease I feel."
            "I guess Sayori is just radiating her enthusiasm because I usually wouldn't feel so great being in a forest this deep."
            "We're not even on a path anymore, she's just taking us through what seems like random trees."
            mc "Do you know where you're going?"
            s "Do you want an honest answer?"
            s 1br "Not really."
            mc "Then what are you looking for?"
            mc "Is this path we're taking supposed to lead somewhere?"
            s 1ba "There's a legend about this part of the forest."
            mc "Another legend?"
            mc "Is this place haunted or something?"
            s 1bd "Who knows?"
            s "It just might be."
            mc "You're way too nonchalant about this, Sayori."
            show sayori 1bq
            "Sayori simply smiles at me."
            s "Anyway, they say that if you ever get lost in the forest you can hear a sound calling you."
            s 1ba "Following it will bring you back to the lake."
            mc "Are you sure it's not just some guy playing tricks?"
            s 1bd "That would ruin the fun a little."
            s "Anyway, I think we're lost enough."
            s "Even I don't know the way back."
            mc "Can't you just bring us there?"
            s 1bl "I could."
            s 2bh "But don't you want to experience this?"
            mc "Yeah but--"
            s 2bo "Shh!"
            s "[player], did you hear that?"
            s "I think I heard something."
            mc "What was it?"
            s 2bc "It sounded like a bird."
            mc "What's so unusual about that?"
            s "You haven't noticed?"
            s 4bn "There haven't been any birds flying around here."
            s "At all."
            mc "That can't..."
            "I think back to when we were at the lake."
            "And the walk to where we are now."
            "She's right, there was no birds."
            "I noticed the insects flying around me but there wasn't a single bird."
            "What's with that...?"
            mc "Why are there no birds here?"
            s 3bd "Still think that bird sound is unusual?"
            "Sayori runs off towards the sound."
            mc "Sayori, wait!"
            "I follow Sayori to the place where the bird sound was coming from."
            "It sounds like it's coming from the top of some tree."
            "But from what I can see, there doesn't seem to be anything there."
            "The chirping from that tree stops."
            "A few seconds later, chirping comes from another tree."
            s 1bc "This way!"
            mc "Wait, this isn't the direction we came from."
            mc "It could be leading us somewhere else."
            s 1ba "Then it'll be an adventure."
            s 1bq "Let's go!"
            "Sayori and I follow the sound of chirping."
            "Sayori is basically running but doesn't look half as tired as I do."
            "Each time we reach the tree it's coming from, more chirping comes from a different tree."
            "It's like there's an invisible bird guiding us to some place..."
            mc "Slow down, Sayori!"
            mc "You're gonna get hurt if you keep rushing like this."
            s 1br "There's nothing to worry about."
            "She turns her head to look at me while she's running."
            s "We have this bird to guide us."
            s "All we have to do is--"
            show sayori 1bm
            "Sayori trips on a loose root on the ground."
            "I don't know exactly how far I was to her when she fell..."
            "But it was like I suddenly went at sonic speed to reach her."
            "Just before she hits the ground, I manage to pull her back."
            mc "Are you okay?"
            "Sayori takes a moment to assess what just happened."
            "She stands up straight and turns towards me."
            s 1bn "Y-Yeah, I think so."
            mc "You need to be more careful."
            mc "We don't know our way around."
            mc "And there's lots of things that can hurt you, you know?"
            mc "These plants could be poisonous or there might be some insect that can sting you."
            s 1bl "...I know..."
            s "I'm just so excited."
            s "I'm living in the moment, you know?"
            s 1bd "Because we only have such short lives."
            s "We have to make the most of times like this."
            mc "What's causing you to say that now?"
            mc "You have a long life ahead of you, Sayori."
            mc "You're still so young."
            mc "We both are."
            s 2bd "You never know, [player]."
            s "Today could be your last day in this world."
            mc "Eh?"
            mc "What could possibly make you think that?"
            s 2bk "..."
            s 2bd "Let's just follow this bird."
            s 2ba "I don't know about you, but I'd rather not stay lost."
            "Sayori goes ahead again."
            "She's moving at a slower pace and looking at her surroundings."
            "At least she listened to me."
            "I follow her lead."
            scene bg lake_day
            show sayori 1bq zorder 2 at t11
            with wipeleft_scene
            "We made it back to the lake quicker than the time it took to get lost."
            "I guess the rumors were true."
            "The bird must have taken us down a better path than what we used to go to where we were."
            "As soon as we arrived, the chirping sounds of the bird disappeared."
            "It's a shame because I was kinda getting used to it."
            "It seemed to be whistling some kind of catchy tune."
            "But now I have to wonder..."
            "Was it just some person playing sounds through wireless speakers set up around the forest?"
            "Or is it really some kind of supernatural force?"
    s "We made it."
    "Sayori takes a moment to catch her breath and I do the same."
    s 1bd "So what do you think? You had fun, right?"
    menu:
        s "At least...even a little?"
        "Yes.":
            mc "Yeah, I did have a lot of fun. It was kind of unexpected what happened..."
            mc "But I think that added to the enjoyment of it."
            s 1bq "Really? I'm so happy that you did."
            s "I honestly didn't know if any of this would be a good idea."
            mc "Why wouldn't it be enjoyable? You seemed to know at least a little bit about the area."
            s 1bd "Like I said before, I didn't really plan any of this that hard so I just hoped you'd enjoy at least some of it."
            s "I also didn't really know what you actually liked so I just went with whatever."
            mc "Would you have wanted someone to take you out on a date like this?"
            s 2bn "I dunno!"
            "Sayori looks around her, extends her arms around her as if embracing the world around her and smiles."
            s 2bd "I guess...I would just want a date to be fun, no matter what it is."
            s 1bd "As long as we were both enjoying ourselves, I wouldn't mind where or what kind of date it was."
        "No.":
            mc "Actually, I...I didn't really have fun."
            mc "It didn't really seem like something I would have done on a date."
            s 1bh "W-What? Why not...?"
            if ch16_s_date_personality:
                mc "Although the intimacy was there, it just felt like something was missing."
                mc "Not to mention, this isn't really a conventional thing to do on a date."
            else:
                mc "I'm not sure, for some reason it just didn't feel right."
            mc "It was good spending time with you, but I wouldn't say it was fun."
            mc "That's all."
            show sayori 2bg
            "Sayori looks at me and puts on a hand on my shoulder."
            s "I think I understand. I know this isn't really conventional so I can't expect you to have had fun."
            s "Maybe your expectations were different or maybe our definitions of fun are different."
            s 2bd "It doesn't matter, I'm just glad you experienced this with me."
            s 2bk "I'm sorry I had to put you through that."
            mc "You don't need to be sorry, I'm glad I got to spend time with you, fun or not."
            s 1bd "Thank you."
    "Sayori moves towards the edge of the lake and beckons me to follow her."
    mc "What's next on the agenda? That thing we did was only the first thing, right?"
    s 1ba "That's right, there's still more to go. I just want to stare at the horizon for a moment."
    s "It might be the last time we get to see the horizon so blue."
    mc "Is that meant to be a metaphor for something? I don't really get it."
    s 1bc "No, it was quite literal."
    mc "Huh?"
    "Sayori leans on the wooden railing and stares deeply at the horizon."
    "I do the same and stare at the horizon too. It's very...blue."
    "Since we can see that far into it without there being more land, this lake must be connected directly to the ocean."
    "I wonder where in the world we really are..."
    "Sayori continues to stare at the horizon. She almost looks as if she's about to cry."
    show sayori 1bt
    mc "Is everything okay, Sayori? You're looking a little teary-eyed."
    s 2bw "I-It's fine! I was just thinking about something I'm still not sure about."
    s 2by "You don't have to worry about it."
    "Sayori wipes her face using her arm and then turns around."
    s 2bd "Ready for the next thing on the list?"
    s "It's something you'd do on a 'normal' date, but I'd like to give you a choice on how we do it."
    mc "Well, what is it and what are the options?"
    s 1bc "I don't know if you're hungry, but it's around the time we'd be eating lunch."
    s "So that's what we'll be doing, we're gonna need all the energy we can get for what comes after."
    s 2bb "Anyway, we have two options. We can either go to some kind of restaurant..."
    s 3bb "...or we can have a picnic around here, with just the two of us."
    s 1ba "It's up to you."
    mc "Do you already have a picnic ready for the occasion?"
    s 1bc "Not exactly, but it won't take long at all."
    s "With a snap of my fingers, I can have it here in an instant."
    mc "And what about the restaurant? Didn't you say time was moving slower for us?"
    mc "Wouldn't that be weird if we went there and everyone was moving in slow motion?"
    s 1ba "Didn't you notice before when we were walking around?"
    s "Everything was going at its usual speed, the birds, the insects, the air..."
    s "That's because everything immediately around us isn't really affected."
    s "I don't know how it works myself, I just found out that I can expand the bubble."
    s 2bb "You see, it only used to be able to affect me and those things I could touch."
    s "But looking deep into the code, it was just a simple number change to make it work in a wider area."
    mc "Okay...I'm not sure what that means but I'm guessing the restaurant won't be affected."
    s 2bd "Yeah, that's exactly what it means."
    s "I don't really have a preference either way, though I do have a restaurant in mind if you do choose that."
    s "And don't worry, I'll cover everything so you can forget about the prices."
    s 2bc "On the other hand, I did make some things myself for the picnic in case you do go for it."
    s "The picnic will be at the park, where we were before while it's still quiet."
    s 1bl "It would be a shame if we didn't get to try them, I made this especially for this occasion."
    mc "Wow, those are both really good options."
    "To be honest, I'm not sure which one is more romantic."
    if ch16_s_date_personality:
        "I get the feeling she was hinting at wanting the picnic more, just because of how she mentioned that extra part."
        "But..."
    "I wouldn't know what to pick in a situation like this, luckily it's your choice to make though, not mine."
    menu:
        s "So what are you thinking?"
        "Restaurant.":
            mc "I feel like a restaurant would be more romantic. I also don't know much about your cooking..."
            s 1bj "My cooking is fine! I've improved a lot since the last time you've had anything I've made."
            s 1bi "But if a restaurant is what you want...then let's go."
            mc "Do you plan on bringing us there in an instant or..."
            s 1bb "If that's what you want to do, we can. Or we can walk from the park."
            mc "Where is it?"
            s 1ba "It's actually just a short walk away from the park."
            s "You might know the place I'm talking about if you remember the park."
            s 1bd "It's a very...exquisite place, if you know what I mean."
            s "And by exquisite, I mean neither of us thought we'd ever go there because of the prices."
            "I think back to the park we were before."
            "I don't really remember that area but there is something in my memory."
            "I guess because the prices were so unbelievable when we found out, I actually remember the restaurant Sayori is talking about."
            mc "Are you talking about the same place I'm thinking of?!"
            s 1bh "Seeing as I turned off my ability to know what you're thinking of, no, I don't."
            s 1bj "If I had to take a guess, then I'd probably say yes."
            mc "You have the ability to generate an infinite amount of money, don't you?"
            s 1bc "Well, yes and no."
            s "While I could generate an infinite amount of money, it would ruin the economy!"
            s 1bl "...I would know, I actually tried it before and turned back time when I saw the immediate effects."
            s 1ba "Instead, I created something people wanted to buy and I'm making money properly."
            s "That way no new money is being added to the economy and everyone is happy."
            mc "I'm not even going to ask the details of that."
            s 1bd "It's just like I said, you don't need to worry about the money."
            s "I can handle it. I just want to focus on enjoying ourselves."
            s 2bd "Besides, the money here isn't real to you anyway so you don't need to feel guilty about anything."
            mc "If you say so, Sayori."
            s 2ba "Now that that's settled, are you ready to go back?"
            mc "Ready when you are."
            "Sayori extends out her head and I reach out and take it."
            window hide(None)
            scene bg park_day
            show sayori 2ba zorder 2 at i11
            $ pause(0.1)
            window show(None)
            "In what seems like an instant, we're back at the park we were before."
            window auto
            "I don't know why but it felt smoother than before."
            "Like I wasn't being forced down some really tight hole for a fraction of a second."
            "When she moved us around this time, I didn't feel anything like that at all."
            "I wonder if she did anything differently."
            s 2bc "Do you ever wonder why it was so expensively priced?"
            mc "I assume it's because the food was really good."
            s "We can't say if the food is actually good or not seeing as neither of us have actually eaten there."
            mc "Then why is it so expensive to eat there? Do you think they're just overcharging?"
            s 2bb "I'm almost certain the reason is because it's a gimmick."
            s "From the outside, it looks like a cheap cafe but in reality that's just the aesthetic they were going for."
            s "Despite the appearance, they actually have gourmet dining alongside your typical cafe food."
            s 2bd "I looked up a bit of information about it and it turns out they have one of the best chefs in the region."
            mc "Even with a good chef, that doesn't explain how they can overprice their food so much."
            s "I think you pay for the experience. That place doesn't exactly look like something you'd find around here."
            s 1bc "It's meant to genuinely feel like a different place, a different nation even."
            mc "I have no idea what that is supposed to mean, but I'll trust you on that."
            s "Do you even remember what it looks like from the outside?"
            mc "I can't say I do. I only remember the ridiculous prices."
            s 1ba "Well, then we should make our way there then."
            s "The best way to remind yourself is by actually experiencing it again."
            s 1bq "Come on, I think it's just a short walk this way."
            scene bg s_cafe_outside
            show sayori 1ba zorder 2 at t11
            with wipeleft_scene
            "Sayori was right, it was just a short walk away from the park."
            "On the way to the restaurant, we saw some people either frozen or moving in incredibly slow motion."
            "It was chilling knowing that Sayori had the power to do something like that."
            "Just how often did she use her power like this? And how many times...?"
            "It's not really my business to wonder but my curiosity is begging me to find the answer."
            "As we got closer to the restaurant, I started to refamiliarize myself with the surrounding area."
            "When I saw it from a distance, I immediately remembered why I thought the prices were so crazy."
            "It didn't {i}look{/i} that amazing and yet asked for insane prices to eat."
            s 4ba "And we're here. Do you remember this place now?"
            "Looking at it close up, I think I remember it being a slightly different color."
            "Other than that, it still has its vintage look to it that I do remember."
            "Despite being called a restaurant, it looks more like a cafe from the outside."
            "But I think that's because of what Sayori said, for the experience."
            mc "Yes, I think I do remember now. We went in here looking for something to eat one time and we were kicked out."
            s 4bl "Ahaha, that wasn't our finest moment, now was it?"
            mc "Definitely not. I think I had nightmares about the guy who threw us out for weeks."
            s "He must have really left an impression on you!"
            mc "Not a good one, that's for sure."
            show sayori 4br
            "Sayori laughs and begins to walk to the entrance of the restaurant."
            mc "Wait, how is this going to work?"
            mc "Won't they notice all the frozen people outside as well?"
            show sayori 4bb
            "Outside the restaurant, there were people in the middle of walking somewhere."
            "Obviously they aren't heading anywhere in a hurry right now because of Sayori..."
            "But if we went inside and the workers saw everyone just standing still like that it might freak them out."
            s 2ba "That's a good point, I should probably do something about that...Hold on, I'll just be a moment."
            s "Take care of me for a second."
            mc "W-Wait a minute, Sayori, where are you going?"
            show sayori 1bq
            "Sayori suddenly closes her eyes and looks like she's about to fall over."
            "I catch her in my arms and try to figure out what just happened."
            "It's like she just randomly fell unconscious or something."
            "After a few seconds, she suddenly takes a deep breath and gets back up."
            mc "Are you okay? What did you just do?"
            s 1bd "I had to change a few things in the world."
            mc "Like...?"
            s "The workers shouldn't be a problem anymore, that's all you need to know."
            mc "Do I want to know what you just did?"
            s 1bl "Even if you did, I'm not sure I could properly explain it."
            s "Now come on, let's go inside. I'm sure they're probably expecting us now."
            "Expecting us...? Why would they be?"
            "Sayori must have done something to them while she was changing a 'few things'."
            "She grabs my hand and pulls me inside of the restaurant, almost effortlessly."
            scene bg s_cafe with wipeleft_scene
            "I don't really remember the inside of the restaurant very well."
            "I can't tell if they renovated it or if it looks the same as it did all those years ago."
            "We're greeted by an intimidating looking man wearing an employee's shirt."
            "He examines us carefully and looks at the clipboard he's holding."
            "Employee" "\"Ah, we've been expecting you.\""
            "Employee" "\"If you step over here, a waiter will take you to your seats shortly.\""
            "He directs us to an area of the restaurant where a line of waiters are idly standing by."
            show sayori 1ba zorder 2 at t11
            s "I told you they'd be expecting us."
            mc "Speaking of expecting, I really didn't expect the restaurant to be like this."
            s 1bc "What do you mean by that? Do you not like it or something...?"
            mc "I'm just saying, I don't really have a solid opinion on it."
            mc "From the outside, it looks like a cheap place to eat. Even the inside does."
            mc "But in reality, the inside is like one of those top of the line restaurants."
            mc "This place even has some kind of bouncer to keep people away."
            s 1bd "Like I said, you're paying for the experience."
            s "Or rather...{i}I'm{/i} paying for the experience."
            s 1ba "I guess it's because of the ironic factor that this place is popular with those that have the money to eat here."
            s "You and I both thought this was some ordinary cafe where you could buy something and just leave."
            s 1bq "But instead, it's a fully fledged restaurant with a sort of vintage atmosphere."
            s 1br "I don't know if it's worth it but we're here and I've already paid."
            mc "You paid before hand? That explains why they were expecting you..."
            mc "What would have happened if we did a picnic instead?"
            s 1bb "Then I suppose my reservation would just be cancelled."
            s "I don't expect they'd give me a refund either, not like I really need the money anyway."
            mc "Must be fun not having to worry about stuff like that."
            s 1bk "I wish I could enjoy that benefit more, [player]..."
            "The waiters talk amongst themselves before finally sending someone to serve us."
            "A tall man bows before us in his greasy-looking waiter outfit."
            "I'm pretty sure the coffee stains and the vintage look on the outfit is part of this place's charm."
            "After seeing that, I definitely get what Sayori was saying when she was talking about that ironic factor."
            "Everything is just the opposite of what you'd expect in this place."
            "I hope it's the same with the food."
            "Not that I'm only here for the food, but I'd hope with crazy prices like this we'd be served decent food."
            "We're taken to a table and the waiter hands us two menus."
            "He stands there waiting, I assume to take our orders."
            show sayori 1bb
            "I open the menu and Sayori does the same."
            "It's actually rather thick and there's lots of choices to go for."
            "Next to all of them however is a huge price tag, it's almost off putting."
            show sayori 1ba
            "Sayori looks over her menu at me and smiles."
            s "Remember, the price is not important."
            s "We're here for a good time. Just look for what you want."
            s "Don't bother looking at the prices."
            "The waiter looks like he's silently judging us."
            "As if we're some sort of super rich people that don't care for prices."
            "Little does he know that I'm close to broke and that Sayori is the one with all the money."
            "Though you wouldn't know that just by looking at her."
            "He quickly returns back to his neutral expression once he sees me notice him."
            mc "If you say so, Sayori."
            "Sayori and I flick through the menus a bit more."
            "There are a couple of things I like on there but I'm really not sure I should get."
            s "Are you ready to order, [player]?"
            s "I think I've figured out the things I'm getting."
            mc "Things? You're getting multiple dishes?"
            s "Well, yeah! I wanna try all the things this restaurant has to offer."
            s "Or at least, more than one thing."
            s "It's a famous restaurant, it would be a waste not to try at least two things."
            mc "Does that mean I can order a bunch of things as well?"
            mc "There's a couple I'd like to try but I can't really decide between them."
            s "Of course! It's all on me, after all."
            s "You can order first, [player]."
            mc "Let's see here..."
            "I recite my order to the waiter."
            "I can see him look visibly more surprised with each order I give."
            "Eventually, he writes down the whole list of what I ordered and flips to the next page."
            "Waiter" "\"And what would the madam be having?\""
            s "Let's see here..."
            "Sayori looks into her menu and starts saying some of the dishes."
            "I have a feeling she's just looking at things that sound nice and randomly deciding if she wants to order it."
            "After a few minutes of looking through the menu, Sayori's order is finally finished."
            "The look on the waiter's face is priceless."
            "Sayori's order must have cost a small fortune but she simply smiles at him nonchalantly."
            "Waiter" "\"I-Is that all you will be having today?\""
            "Waiter" "\"Perhaps you wouldn't want to add the rest of the menu?\""
            s "Ahaha, no, that's all for now. Thank you!"
            "Waiter" "\"Forgive me for being rather blunt but...\""
            "Waiter" "\"You wouldn't happen to be wasting our time and money, would you?\""
            "Waiter" "\"It's just...that's a large order for only two people.\""
            s "We're serious about this. I've already paid the entrance fee, so you should know that."
            "The waiter looks dumbfounded but bows to us before taking the order to the counter anyway."
            "It's not really busy in the restaurant at this hour."
            "I'd say we're the only ones here but part of the reason for that is probably because of what Sayori did."
            s "So, what do you think the chef's reaction will be?"
            s "We ordered quite a lot of stuff, you know."
            mc "I have a feeling we're either going to hear some yelling..."
            mc "...or he's going to straight up refuse to cook it."
            mc "The order we made was pretty unreasonable."
            s "Maybe...I don't expect we'll actually finish all of the food."
            s "Like you said, we did order a lot."
            s "But then again, we don't even know the servings of this place."
            s "It could be like one of those fancy restaurants where you're paying hundreds but you get a small blob on your plate."
            mc "Is that what you think this place is?"
            s "If it is, then making that large order just now was probably for the best!"
            mc "Well, you're the one paying so I can't complain."
            mc "What do we do in the meantime then?"
            mc "I'd imagine all that food is going to take a while to cook."
            s "That's a good point."
            s "I guess you can take this time to get to know me."
            s "You know, before we actually met."
            s "This is a good a time as any, right?"
            "The memories of Sayori that I have are still pretty clear to me."
            "But this will be a good chance for you to learn more about her."
            s "I guess I should start from the beginning."
            call ch16_sayoridate_life
            "Sayori looks out the window into the distance."
            "It's like she's avoiding my eyes, like she's afraid."
            mc "Is something wrong, Sayori?"
            mc "You can't blame yourself for what's happening, whatever it is."
            mc "You shouldn't have to deal with it alone, either."
            s "I'm not alone, [player]."
            s "I've had someone supporting me through this whole thing."
            s "But I know what you meant and I appreciate the thought."
            s "Anyway, it looks like the food is arriving."
            s "That was a lot faster than what I was expecting."
            s "Especially with how large our order was."
            mc "Maybe they had it prepared already."
            s "If I'm paying that much for prepared food then..."
            s "...well, I wouldn't really care. It's not like I need the money."
            s "But it would really suck."
            "The waiter that brought us to this table comes back with an arm full of plates."
            "The look on his face says it all."
            "I think he's struggling to bring it all to us."
            "One by one he manages to lay down each meal in a random place on the table."
            "He then looks at us and back at the kitchen and sighs."
            "This process repeats three times before he finally glares at us and bows."
            "Waiter" "\"Would that be all?\""
            "Waiter" "\"Perhaps there is something else on the menu you are missing?\""
            "Sayori looks at the waiter and smiles."
            s "No, that's all we're going to eat. Unless you have any recommendations for us?"
            s "Maybe we can add that to the order."
            "The waiter looks at Sayori and shakes his head."
            s "Then, that is all. Thank you."
            "He walks back to the other group of waiters, who seem to find the situation amusing."
            "Sayori looks at all the food we have and then at me as if questioning what do with it all."
            "I give her a shrug and take one of the dishes I ordered."
            mc "Well, here's the moment of truth."
            mc "The food is either going to taste incredible or really bad."
            "I take a piece of the food but just as I'm about to put it in my mouth..."
            s "Wait! Look over there but without drawing attention."
            "Sayori points to the group of waiters."
            "They all seem to be watching us, or rather watching me."
            "Are they that eager to see me eat?"
            mc "What about them?"
            s "Don't you think what they're doing is a little suspicious?"
            mc "I'm sure they just want to know if I like it or not."
            mc "It's no big deal, right?"
            s "...You're right, sorry. I guess I'm just a bit paranoid."
            s "Go on then, eat it. Tell me what it's like."
            mc "I was in the middle of doing that."
            "I finally put the piece of food into my mouth."
            "After taking a few bites, I have to say...it's pretty good!"
            "The initial taste wasn't all that good but that's probably due to what I ordered."
            "The flavors that come after that are just incredible though."
            "I guess the food here is pretty good."
            "But is it really worth the price that Sayori paid?"
            s "Well? How was it?"
            mc "It's good, try it for yourself."
            mc "Mine tasted pretty average at first but slowly got better."
            mc "I'm not sure why, I've never experienced that before."
            mc "At least, not with this kind of meal."
        "Picnic.":
            $ ch16_s_date_activities += 1
            mc "I think a picnic would be better, it feels a lot more personal."
            mc "And I haven't really had something made by you in a while, so I'm eager to try it."
            s 1bc "Really? I didn't really think you would do that."
            mc "How come? A picnic is way more intimate than going to some restaurant."
            mc "Besides, if it's a date, I'd rather be with you alone than with other people."
            s 2bq "Ehehe, you're so sweet~"
            "Sayori extends out her head."
            s "Come on, take my hand. We're going back to the park."
            s "I know the perfect place in the park for a picnic."
            "I hold Sayori's hand in mine. She closes her eyes and..."
            window hide(None)
            scene bg park_day
            show sayori 2bq zorder 2 at i11
            $ pause(0.1)
            window show(None)
            "In what seems like an instant, we're back at the park we were before."
            window auto
            "The experience felt a like smoother this time around."
            "Last time, it felt like I was being squeezed down an impossibly small hole for a fraction of a second."
            "This time, it didn't feel like that at all."
            mc "So where's this spot you were talking about?"
            s 2ba "Do you remember that tree we used to sleep under when we were children?"
            mc "Is that where the spot is?"
            s "That's exactly where we're going, it's got nice shade from the sun."
            s "Plus, it has some form of sentimental value towards both of us."
            s 2bd "Though I suppose you wouldn't really know about it."
            s "I feel like you're learning more about my childhood than you ever have before."
            s 1bc "It's weird, isn't it?"
            s "You've known me all this time, and yet you don't know anything about my past."
            s 1bd "I have to say, it does feel weird telling someone who does know about my past to talk to someone who doesn't."
            "I think that was directed at you."
            "Throughout this whole thing, there are times I'm confused as to who she's speaking to."
            "Most of the time, she's speaking to you but other when she wants me to experience it, she's speaking to me."
            "It's kinda hard to figure out which is which sometimes."
            s 1ba "Anyway, let's go. I think you'll be surprised as to what's happened to it."
            "Sayori takes my hand and skips along towards the tree."
            scene bg tree_day
            show sayori 1bd zorder 2 at t11
            with wipeleft_scene
            "We arrive at the tree and I guess I am kinda surprised."
            "It, quite literally, has not changed at all. It looks exactly the same as it did years ago."
            "I suppose I shouldn't be surprised, it is a tree and they don't really change much in appearance after they've grown."
            "Still, it gives this feeling of nostalgia."
            "It probably doesn't mean anything to you but going back here after all these years gives this strange feeling inside."
            s 1bc "Look at what's changed, [player]. This used to be where we would sleep when we got tired after playing."
            s "Do you remember those times?"
            "Sayori walks around the tree before stopping to look up at the leaves."
            s 1bd "This tree hasn't changed one bit...but looking at us..."
            s "We've completely changed who we are, haven't we?"
            s 2bl "You used to be so outgoing and excited as a kid."
            mc "I did? I never really saw myself like that."
            mc "But I have forgotten what I used to be since that was such a long time ago."
            mc "You probably remember better than I do."
            s 2bd "It's hard to forget who you used to be when you were so...different back then."
            mc "Have I changed for the worse?"
            s 1bb "No. Or at least, I don't think you have."
            s 1bc "You just matured and got over that part of your life a lot faster than I did."
            s "It just happened so fast..."
            mc "Well, what about you?"
            mc "You used to be exactly like who you were as a kid."
            mc "But over a few short weeks, you've completely changed who you are."
            if ch16_s_date_personality:
                mc "I noticed it. Maybe it wasn't conscious but deep down, I knew."
                mc "I knew you had changed."
            mc "You've become this person who wants to help everyone."
            s 1bk "I was forced to change, [player]."
            s "I didn't ask for any of this, it was just thrust into my life."
            s 1bh "If I didn't change the way I did things, who knows where we would be right now."
            s 1bd "But enough of that talk."
            s "We haven't even had anything to eat yet. Let's not ruin the mood."
            s 1bo "Just wait a moment, I'm going to get everything ready."
            "Sayori looks at the ground and thinks for a moment."
            show sayori 2bo
            "She snaps her fingers and just like that, there's a picnic blanket on the ground."
            "It's one thing for it to happen to you and it's another to see it happening."
            "I just have no idea how it even works."
            s 2ba "You take that side and I'll take this one."
            "Sayori points to the blanket and moves to the other side of it from where we're standing."
            "She unrolls it and takes one corner and I take the opposite corner."
            "After we get it onto a good spot, she composes herself."
            "Without even snapping her fingers, a basket appears on her left arm."
            "She puts it down on the blanket and takes a seat on the grass."
            "I fall to the floor and take a seat as well."
            s 2bc "This place holds so many memories."
            s 1bd "Memories that you never experienced...it's sad in a way."
            s 1bq "It just means that we can make some new ones."
            "Sayori reaches into the basket and takes out something wrapped in plastic."
            "She offers it to me and takes out another one for herself."
            s 1ba "I actually prepared this thing this morning."
            s "It's nothing special, it's just something I learned how to make recently."
            mc "What is it?"
            s 1bc "Unwrap it and find out. I think you'll like it though."
            "I unwrap the plastic surrounding the thing Sayori made."
            "It looks like some kind of thin bread but inside it is a mix of all sorts of things."
            s 1bd "Have you heard of a burrito before?"
            mc "A burrito? Is that some kind of made up word."
            s 1ba "No, it's a real thing! It's kinda like a taco except..."
            s 1bl "Wait, you wouldn't even..."
            s "Have you even heard of a taco before, [player]?"
            mc "I can't say I have. What is it?"
            s 2bl "You know what, it's better if you just try it."
            s "You don't need to know what it's called."
            s 2bq "Go on, take a bite and tell me how it tastes."
            "I cautiously take a bite out of the burrito."
            "It's not that I don't trust Sayori's cooking, it's just the last time I did it didn't go well."
            "It's a whole lot of different flavors coming out at once."
            "It's like taking a mouthful of random ingredients that somehow work well together."
            "It's pretty delicious."
            mc "Not bad, Sayori. This is definitely way better than the last thing you made."
            mc "Where did you learn how to make this?"
            show sayori 2ba
            "Sayori takes a bite out of her burrito and shrugs at me."
            s "It's hard to explain, and you wouldn't believe me if I told you."
            "I take another bite of the burrito and it's just as good as the last."
            mc "It's out of this world, that's for sure."
            s 1bq "Ahaha, you have no idea how accurate you just were."
            mc "What do you mean? It's just a figure of speech."
            s 1br "Nothing! I'm just glad you like it."
            s 1bd "I have to thank you for doing this, [player]."
            s "I know you're just tagging along, but you're the one making this possible."
            s "So I don't want to make things worse for you."
            mc "I appreciate the thought, Sayori."
            mc "But you don't need to worry about me."
            mc "In the end, your happiness is more important to me than anything."
            mc "If I have to be a puppet of some higher power for that to happen, then so be it."
            s 1bk "..."
            s "You shouldn't say things like that, [player]."
            s "Even if you aren't the one I love, you're still important to me."
            mc "I get it, Sayori. You really don't have to worry about me like that."
            mc "I'm just grateful I got to come along for the ride."
            mc "Without this...other person, I wouldn't be with you right here and now."
            mc "In fact, I don't know what I'd be doing."
            s "Its just that--"
            mc "Come on, let's not ruin the good mood."
            mc "What else do you have in that little picnic box of yours?"
            s "...Alright, [player]."
            "Sayori reaches out into the picnic basket again."
            "I can already feel my taste buds getting excited for what's coming."
            s "I'm not sure if you'll like these but I tried hard!"
            s "They're far from perfect but..."
            mc "They're homemade, so that already makes them better."
            s "Hah...well, you shouldn't be quick to judge."
            s "Appearances can be deceiving, you know."
            "Sayori pulls out something from the bag that looks like a pie."
            "It's got this chocolate looking layer on top. It looks delicious."
            s "This is our dessert. You should probably finish the burrito first because they're really contrasting flavors."
            s "And...well, I'm not actually sure if it's any good or not."
            s "So just keep eating the burrito and maybe you'll be full enough before you try the dessert."
            mc "You have no idea how much I can eat, Sayori."
            mc "I'll finish this burrito and still have room for that dessert."
            s "We'll see about that."
            "Sayori takes a bite into her burrito and I do the same."
            "Now that she mentioned how much the burrito would fill me, it's actually become more difficult to eat."
            "I wonder if I've just noticed that or if she did something to make me feel that way."
            "After a few minutes, she manages to finish eating her burrito whereas I'm still struggling to eat mine."
            "I don't think I can take another bite though."
            s "Can't finish it, can you? Looks like you won't be able to try the dessert~!"
            mc "Did you do something to me?"
            mc "This burrito is more than I can handle."
            s "I told you that it might make you full."
            s "And no, I definitely didn't do anything to you just then."
            s "Maybe you got to the meat of the burrito and just got full."
            s "I promise you I didn't do anything."
            mc "I believe you. It's just...wow."
            mc "I really didn't expect to be so full off of that, I thought I could fit more into me."
            mc "Maybe I just ate too fast and my stomach hasn't catching up."
            s "That could be it...though I know how much you wanted to try it."
            s "I can see what I can do so that you can try it."
            s "But I'm making no promises to whether it actually tastes good or not."
            mc "So you keep saying, but it sounds like you're just trying not to make me eat it because it's that good."
            s "That...doesn't make any sense."
            s "Why would I even do that? If I made something, it's because I'd want you to try it."
            s "But anyway, what's the decision?"
            s "Do you want to try the dessert or not?"
            mc "I suppose it's not really up to me, is it?"
            mc "Let's see..."
            menu:
                "So what do you want to do?"
                "Let Sayori do her thing.":
                    "I really do want to try her dessert."
                    "So I'm actually really glad you chose to let me do this."
                    "I wonder what exactly Sayori has planned for me though..."
                    "She's obviously going to change {i}something{/i}."
                    mc "Go on then, Sayori. I'm ready."
                    mc "Do what you have to do."
                    s "Does that mean you want to try the dessert?"
                    mc "Hopefully, I get to, yeah. If it's even half as good as the burrito then I'm excited to try it."
                    s "Okay, this might hurt a little."
                    s "You might want to close your eyes too because this could get a little weird."
                    mc "Um...okay, I know you're going to do something to me but why do I need to close my eyes?"
                    s "It's just better if you do, trust me."
                    s "Now, close them, [player]!"
                    scene black with close_eyes
                    "I close my eyes and wait for Sayori to do something."
                    "I can hear her moving around but I'm not entirely sure what she's doing."
                    "I think she stepped behind me at one point but since then I've heard nothing but silence."
                    "The whole time I've managed to keep my eyes closed."
                    "Suddenly, I can feel the environment around me change suddenly."
                    "It still feels like I'm sitting on grass but it just feels different."
                    "Like it's a liquid...or something."
                    "A sharp pain comes from my stomach, despite that I don't flinch."
                    "The pain goes through my whole body but I can't move."
                    "It's like a million pins and needles have been poked into me."
                    "And just as suddenly as the pain appeared, it was gone."
                    "My stomach feels more empty and I can feel the solid grass underneath me."
                    "Once again, I can hear Sayori shuffling around me."
                    mc "Can I open my eyes now?"
                    s "Wow, I'm actually surprised you managed to keep your eyes closed."
                    s "But yeah! Go ahead and open them."
                    scene bg tree_day
                    show sayori 1ba zorder 2 at t11
                    with open_eyes
                    "I open my eyes and see Sayori sitting in front me where was was originally."
                    "She's eating her burrito as if nothing happened and staring into the distance."
                    "The pies seem to be unwrapped and ready to eat too, there's already a few slices I can see cut off."
                    mc "So am I going to get an answer to what you just did?"
                    "Sayori looks at me and offers me a plate of the pie she made."
                    s "Here, you can have the first slice of the pie."
                    "I think she just dodged my question."
                    "I'm not complaining, this pie does look delicious."
                    mc "Here goes nothing..."
                    "I take the pie from the plate with my hands."
                    "It smells freshly made, it's warm and has the scent of apples on it."
                    "I can't wait much longer so I go for a bite."
                    "Or at least...try to. It's rock hard, my teeth can't penetrate through the crust."
                    "I keep trying but I think if I keep going, it's going to break my teeth."
                    "I look at Sayori and she has this look on her face that says 'I told you so'."
                    s "Ahaha! Weren't expecting that, were you?"
                    "I drop the pie and hear a loud thud on the ground."
                    "How hard was that thing...?"
                "Pass eating the dessert.":
                    "You probably know better than I do than to continue trust Sayori's cooking."
                    "I'll pass on the dessert but that doesn't mean I'm not upset about it."
                    "I would have liked to try it but it's probably for the best if I don't right now."
                    mc "I'll just keep eating this burrito."
                    mc "Or try to, at least. At this rate, I doubt I'll finish it."
                    s "So I can safely put away this pie then?"
                    s "That's a relief. You have no idea how anxious I was that you'd eat it."
                    s "I don't know whether I'd have laughed or felt sorry for you afterwards."
                    s "Still, I'm glad that's over with!"
                    mc "If you didn't want me to eat it then why did you show it to me in the first place?"
                    s "I don't know. I guess I just wanted to see how you'd react."
                    s "After seeing and tasting my burrito, I wanted to see whether "
                    s "I do want you to try one of my pies at some point, especially since you seemed so interested."
                    s "Just not this one."
                    mc "I'm sure you have your reasons for that."
                    s "I usually do for things like this."
                    "Sayori wraps the pie and drops it back into the picnic basket."
                    "I heard an unusually loud thud sound when she dropped it."
                    "Are those pies made of rocks or something...?"
            s "Now that we've dealt with those pies, we can finally get on with it."
            mc "What do you mean? You wanted to do something else?"
            s "You're already full, aren't you?"
            mc "Yeah, I couldn't possibly eat another bite of anything."
            s "Then...let's go for a walk!"
            s "Just around the place, I think you'll be surprised at what you'll see."
            mc "Okay, sure we can do that."
            s "Great, let me just pack everything up and we'll get right on it!"
            scene bg park_day
            show sayori 1ba zorder 2 at t11
            with wipeleft_scene
            "Sayori and I take our time strolling around the park."
            "She said I would be surprised at what I would see but nothing really catches my eye."
            "It just looks like the same old park we used to go to as kids."
            s "I think this would be a good time to get to know me better."
            s "Especially since we're at one of the places of my past right now."
            s "You can learn a bit about me that you wouldn't know otherwise."
            "I already know most of Sayori's past."
            "Still, this is for you mostly. Despite that, I know it'll be a good experience for both of us."
            mc "Yeah, let's do that."
            s "Then I suppose I should start from the beginning."
            call ch16_sayoridate_life
            "Sayori stops and stares into the distance."
            "She purposely avoids my eyes when I stand in front of her."
            mc "Is something wrong, Sayori?"
            mc "You can't blame yourself for what's happening, whatever it is."
            mc "You shouldn't have to deal with it alone, either."
            "Sayori looks me straight in the eyes after I say that."
            s "I'm not alone, [player]. You know that."
            s "This issue has become far too big to deal alone."
            s "I don't know if I could even manage..."
    call screen dialog(message="To be continued!\nThanks for playing, keep an eye out on reddit and discord for updates!", ok_action=Return())
    $ renpy.utter_restart()
    return

label ch16_sayoridate_life:
    s "When I was younger, my life was complete bliss."
    s "I didn't have a care in the world."
    s "I just wanted to have fun because, you know...I was a kid."
    s "This was about the time I met [player]."
    s "[cPlayer_personal] and I...we had this instant connection. We were inseparable."
    s "We would always play together when we could find the chance."
    s "There wasn't a day where we weren't playing together or thinking about playing."
    s "But...[player] grew up so much faster than I did."
    s "I was still stuck in my childhood bliss but [player_personal] matured."
    s "[cPlayer_personal] didn't want to play everyday like we used to."
    s "And eventually...it was just me."
    s "I guess that's what where my depression first started."
    s "Losing the friend that was always there for me."
    mc "Sayori...if I knew I--"
    s "It's not your fault, it's mine."
    s "I just thought I could keep living the easy life."
    s "I knew I had to grow at some point as well, but it was just hard."
    s "I had to take a lot of time to think. Think about where I wanted to steer my life."
    s "Did I want to change and stay best friends with you?"
    s "Or did I want to stay in my blissful life, by myself...?"
    s "It should have been an easy answer."
    s "But I was just so reluctant for change at the time..."
    s "It only added to my depression."
    s "No matter how long I tried to stay in my life of bliss, I knew change would be forced onto me at some point."
    s "So I knew I had to take matters into my own hands."
    s "I guess that's when I first realized I didn't really care."
    mc "Really care for what...?"
    s "I didn't care for my happiness, or at least, not anymore."
    s "My parents were so proud of me for moving on, for finally maturing."
    s "Them being happy meant more than my own happiness."
    s "Seeing them smile...it made me realize this."
    s "No matter what I did to make myself happy, nothing would work."
    s "So I did my best to make other people happy."
    s "Everything I did, it was all for other people."
    s "When I was expected to be happy, I would put on a brave face and smile."
    s "But deep inside, I knew...it was all fake."
    s "There wasn't any happiness to be found inside me."
    s "I felt worthless if I couldn't get people to smile."
    s "The more I made people smile, the harder it was to see them sad."
    s "It's like I was fighting an uphill battle and depression was winning."
    s "But despite that, I did everything I could to stop them from being sad."
    s "But we know that's just impossible."
    s "There are moments that are just meant to happen, you can't keep prolonging them."
    s "When I saw my parents cry because of something I did...I couldn't take it."
    s "I just wanted them to be happy but instead I did the opposite."
    "I never knew Sayori's life growing up was so difficult for her."
    "Who knew her depression started so early in her life...?"
    "I guess I didn't know her as well as I thought I did."
    s "That was the first time I actually contemplated killing myself."
    s "They were so mad at me for an innocent mistake...I just wanted it all to end there."
    s "But I knew...I knew if I did that then they'd be even more sad."
    s "I knew it was too selfish. So I didn't do it."
    s "But I knew it would keep eating at me until..."
    "Sayori scoffs and smiles."
    s "Well, it never happened in this timeline."
    s "So let's not make this get too dark, okay?"
    s "Anyway, I had to try harder. I had to keep up this charade of being this blissful girl."
    s "This girl that was always happy so that I could turn my fake happiness into other people's real happiness."
    s "This girl that would intentionally do dumb things to make people laugh."
    s "And you know, a thought came into my head."
    s "It was going to be so much harder for everyone when I disappear."
    s "Because despite my best efforts, my depression was only getting worse."
    s "I didn't want to talk to my parents about it because I didn't want to make them sad."
    s "I thought the only option was to keep it a secret."
    s "And for years, I did."
    s "But keeping something like that bottled up isn't good."
    s "It just keeps building up and building up."
    s "I don't know how much longer I could keep it up."
    s "I would go through school day after day, living this lie."
    s "Just doing well enough in school so that my parents wouldn't be concerned about me."
    s "And putting on this fake personality for everyone else for the same reason."
    s "For years, this was how I lived my life."
    s "Once, I almost convinced myself that I was actually happy and that it wasn't all fake."
    s "But it didn't last long at all, I knew that it was just fake."
    s "I knew that I couldn't keep this up forever, that I would eventually reach a break point."
    s "One part of me wanted to keep up this image for as long as I could, to keep it all a secret and embrace the charade."
    s "But the other part of me, I suppose the rational side of me, wanted to tell someone."
    s "Even if I did listen to it, I had no one to tell."
    s "No one was really that close to me to realize...not since you left me, [player]."
    s "I had so many 'friends' at that point, but I've never felt more alone."
    "Sayori...I wish I knew the extent of her pain."
    "I wish she told me...instead I was off doing my own things."
    "She wasn't even on my mind. How could I have not considered her feelings?"
    s "When [player] joined the club, I thought maybe I would stop feeling so depressed."
    s "It's kinda ironic because it only worsened. I think we both know the reason why."
    s "It was Monika."
    "Monika made Sayori more depressed...that's surprising."
    "But why? And how could she even do that?"
    "Did Monika know that Sayori had depression in the first place?"
    s "She was jealous, jealous of the attention everyone was getting."
    s "Jealous that they were closer to you than she was."
    s "She would have done anything and everything to be with you."
    s "Even get rid of her friends by making it so they never existed."
    s "Or at least, she would have if you didn't make this possible."
    s "Because of you, she had a chance to see what it was like."
    s "That's right. I know about that 'first' Monika."
    s "The one that spoke to you at the very beginning."
    s "Without {i}that{/i} Monika, I wouldn't be here."
    s "I know that in her version of events, she made me kill myself."
    s "The thing is, we both know that's not entirely true."
    s "If I wasn't already depressed, I might not have done it."
    s "I guess she just gave that other me that small push over the edge which..."
    s "...if I'm honest with you, wouldn't have made a difference in the end, because it would have happened sooner or later."
    s "Sometimes that's all it takes, you know?"
    s "Just a couple of words to finally tip someone over the edge."
    s "I don't even want to imagine..."
    s "If my depression, combined with Monika's meddling would have made me kill myself then..."
    s "She probably did worse things to Yuri and Natsuki."
    s "I know those two don't have depression, at least in the way that I did."
    s "So the sort of things Monika might have done..."
    s "Well, it's not like she did them in this timeline."
    s "In fact, she made me better in this world and it's thanks to you that she did."
    s "And besides, this isn't about her. It's about me."
    s "But I just want you to know that's why you're so important to me."
    s "You stopped all of that from happening, you gave me this chance."
    s "I know you aren't really here but knowing you're so close...it makes me feel so safe."
    s "It's the safest I've felt since before..."
    s "Before all of those rainclouds blocked my only ray of sunshine."
    s "But it's okay now, isn't it?"
    s "You're here, with me. You'll keep me and the rest safe."
    s "Won't you...?"
    mc "I don't think you need an answer to that, Sayori."
    mc "Me being here in place of them is a testament to their devotion."
    mc "I mean, just how hard would you have had to try to even get here."
    mc "Whoever this is clearly wanted to help you and the others if they're here now."
    s "...You're right, [player]. It's just...I can't help but have my doubts."
    s "I can't even see you so it's hard to judge whether you're being honest."
    s "You could be laughing as I'm saying all of this, thinking it's funny."
    s "That perhaps you're just pulling a trick on me."
    s "Or maybe you're exploring all the different ways you can go through this."
    s "And this is just one of them."
    s "Despite all of my doubts, I just can't help but be in love with you."
    s "It's a strange feeling...and almost scary."
    s "Imagine loving someone so much that you don't care what they did."
    s "An unconditional love."
    s "Of course, that's not really what this is."
    s "You've earned it from me, I don't just love you for no reason."
    s "But I can see past my own doubts and thoughts for you."
    s "Anyway...I don't really know what else there is to know about me."
    s "My childhood was pretty normal aside from the...you know."
    s "Maybe you want to know how my life was at the beginning of my presidency?"
    s "It was only a couple of weeks ago, but maybe you'd like to hear my perspective."
    s "How I felt and all of that."
    s "You don't have to though! Most of it is pretty boring."
    s "But hey, it's not like you've got anything better to do at the moment, right?"
    menu:
        s "So how about it?"
        "Listen.":
            s "I'll try to keep it short then!"
            "Sayori takes a deep breath then taps her head as if she's thinking."
            s "Things were pretty weird at first."
            s "As you probably know, Monika gave this power to me."
            s "She didn't exactly {i}give{/i} it to me though, it was more forced onto me."
            s "After she left, I guess the world decided that {i}I{/i} should be the president."
            s "It was all so sudden too."
            s "I can only guess it happened the very moment Monika deleted herself."
            s "There I was in my room, happier than I've ever been in years and suddenly I get this strange feeling."
            s "Like a jolt of electricity went through my whole body."
            s "It was pretty surprisingly, actually. It made me think that I messed up something somehow."
            s "I didn't really know what it was at first."
            s "I guessed it was probably due to this new happiness I was feeling."
            s "That was completely wrong!"
            s "I found out I had some kind of power when I was thinking about food and suddenly there was a cookie in my hand."
            s "It came out of literally nowhere."
            s "I thought it was just me being clumsy and forgetting there was a cookie in my hand."
            s "When I finished the cookie, I thought I'd go downstairs."
            s "Suddenly, I was just there in the middle of my kitchen."
            s "That's when I realized that something was definitely going on."
            s "I wasn't sure exactly what it was but I thought if anybody knew, Monika would."
            s "I don't know why I thought that. It just made sense to me since she was so smart and everything..."
            s "To my surprise, she wasn't in my phone. I tried looking her up and she wasn't anywhere at all."
            s "It was like she simply vanished!"
            s "I guess she did because she didn't really exist anymore."
            s "I never understood how that worked, you know?"
            s "If someone we knew never existed, then how are we the people we are today?"
            s "Think of all the experiences that you've had because of that person and how that shaped you as a person."
            s "If they were suddenly gone, then how come we're still here...?"
            s "Anyway, I learned to try not to think about that too much, it just makes my head hurt."
            s "Discovering Monika didn't exist, I went looking through some of the photos I had of the club."
            s "Before [player] and you joined, that is."
            s "Monika wasn't in any of them. It was just Yuri and Natsuki."
            s "I seriously started to freak out then."
            s "But then I started to connect some of the dots."
            s "I knew I had some kind of power and it was after Monika disappeared."
            s "I wondered why Monika's words were so strong when she said them the day before."
            s "They got straight through to me. Straight through my charade I tried so hard to keep up."
            s "But they weren't like that until you came."
            s "We both needed you there for me to be 'cured'."
            s "You were like...a catalyst. Bringing [player] there helped me and at the same time, you being there helped her."
            s "Using her power at the time forced these feelings onto me, that I've come to accept."
            s "It's much better than living a life clouded by dark thoughts."
            s "After that, she knew that she had to delete herself so that she wouldn't be tempted again."
            s "She was content, perhaps for the first time in a long time."
            s "In that way, she was like me..."
            "I never realized just how much Monika did to help Sayori."
            "She was willing to sacrifice herself for her...all because of you."
            "Just what kind of person are you exactly...?"
            s "I'll be honest, I don't know {i}why{/i} being the president of the Literature Club lets you do this."
            s "It really doesn't make any sense at all."
            s "Perhaps you know the reason because I sure don't."
            s "I decided that if I was going to have this power forced onto me, I would try my best to save everyone."
            s "To make everyone happy and live up to the charade I built up."
            s "My first course of action was to bring back Monika."
            s "But of course, it didn't work."
            s "She completely removed herself from the world."
            s "There was no trace of her remaining..."
            s "Which is why I needed you to bring her back yourself."
            s "I couldn't simply recreate a whole character like that."
            s "But you...if you loved Monika even a fraction of how much she loved you..."
            s "Then you would have her saved, right?"
            s "My little gamble paid off when you finally brought her back."
            s "I could have interfered when you two were having your little talk."
            s "But it seemed like an appropriate moment to leave the two of you alone."
            s "Look, I'm gonna skip all of this next stuff."
            s "You already know what happens next, I failed to create the next day and Monika's performance got cancelled."
            s "Instead, I'm going to tell you the secrets I found about this world."
            s "It turns out that the whole world is in some sort of loop."
            s "The variables in the loop stayed mostly the same but there was obviously a few changes."
            s "Me becoming the president was the biggest change that ever happened."
            s "And I think that broke the loop."
            s "Which means that we could finally decide how we wanted to do things."
            s "We wouldn't be subjected to living a nightmare over and over."
            s "But by breaking the loop, I put the whole world at risk."
            s "There have been many, {i}many{/i} times when there's been a glitch I've had to fix."
            s "You haven't seen me use it a lot but I've used a lot of rewinds to make the days as good as they can be."
            s "There are times when I have to completely remove a part of a day to keep it stable."
            s "Or when I have to make something happen or the whole world breaks."
            s "That's when your screen gets all fuzzy and tries to adjust."
            s "You've seen that a lot but it's a necessity."
            s "If I didn't, then I wouldn't have been able to delay the inevitable."
            s "I wouldn't have been able to stop this danger for as long as I have been."
            s "But it's my fault it's even happening in the first place..."
            mc "Wait...what?"
            s "You know...I think I've said enough for now."
        "Pass.":
            s "Ah...well, small talk was never really something I was good at."
            s "I'm glad you're stopping me before I go on and on."
            s "I suppose we'll just stare at each other until we're done here."
            s "...In silence."
            s "It's probably for the best that you don't know."
            mc "What do you mean...?"
            s "It's just...I'm the cause of--"
            s "Forget it, okay?"
    s "This is meant to be a date, no need to ruin it right now."
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
        $ get_achievement("*Good Guy Clerk*")
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
        $ get_achievement("*The Truth*")
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
        $ get_achievement("*An Important Character*")
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
        $ get_achievement("*Sadist*")
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
