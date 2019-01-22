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
        show screen tear(8, offtimeMult=1, ontimeMult=10)
        $ pause(3.0)
        stop music
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
        cl "You look like you could use a hand."
        show mysteriousclerk 1a zorder 2 at t11
        "It's the clerk from that portrait shop...!"
        mc "You're..."
    elif ch15_s_together:
        cl "Need some help there?"
        show mysteriousclerk 1a zorder 2 at t11
        "It's that clerk from before...!"
        mc "What are you--"
    elif persistent.ch15_sayori_saw_clerk or persistent.ch13_nat_date:
        $ cl_name = "Familiar Clerk"
        cl "You want some help with that?"
        show mysteriousclerk 1a zorder 2 at t11
        "This guy...why does he seem so familiar?"
        mc "What the...?"
    elif persistent.did_christmas_event:
        $ cl_name = "Nick"
        cl "Hey friend, want some help?"
        show mysteriousclerk 1a zorder 2 at t11
        "Have I...seen him before?"
        "Why do I feel like I know his name?"
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
    cl "Ah, ah, ah!"
    "The man signals for me to be quiet."
    cl "Let's just take this box where it needs to be, okay?"
    cl "Unless you'd rather get one of the other people to help you?"
    mc "..."
    cl "Yeah, I thought not."
    cl "Now, you take that side and I'll take this side."
    "With his help, we easily lift the box off the floor."
    "This time it feels unnaturally light, nothing at all how it was before."
    "This guy must be really strong."
    cl "To the clubroom, right?"
    mc "Yeah..."
    cl "Lead the way."
    scene bg corridor
    show mysteriousclerk 1a zorder 2 at t11
    with wipeleft_scene
    "We make our way to the clubroom fairly quickly."
    "There is still only a few students around."
    "None of them questioned why I was walking around with some guy who clearly looked like he didn't belong here."
    "I guess he isn't really doing any harm."
    "And maybe he's just a temporary teacher or a substitute or...something."
    "There's just something about him."
    cl "So this is the room, huh?"
    "The man looks at the door to the clubroom carefully."
    "He then nods to himself."
    cl "Back in my day, it used to be in the other building."
    cl "But I guess no one really goes there after the incident."
    mc "Back in your day?"
    mc "And what incident are you talking about...?"
    cl "Oh, nothing."
    cl "I've said too much already."
    cl "You can take it the rest of the way, right?"
    mc "I should be fine."
    cl "Splendid."
    "The man lets go of the box."
    "I suddenly realize, once again, how heavy the box is."
    cl "The door is already unlocked."
    mc "What?"
    mc "How do you--"
    cl "I'll see you around, [player]."
    mc "Right..."
    show mysteriousclerk at thide
    hide mysteriousclerk
    "The man walks off in a different direction to where we came from."
    if not ch15_s_together and not natsuki_date:
        "But wait..."
        "How does he know my name?"
        "I didn't tell him...did I?"
        "Never mind."
        "I have to get this box inside."
    else ch15_s_together or natsuki_date:
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
        show natsuki 1a zorder 2 at t21
        n "I'm just saying, you should listen to other stuff too!"
        n "Your music is fine, Yuri."
        n "But have you tried listening to anime openings?"
        n "A lot of them are really great!"
        show yuri 1a zorder 3 at f22
        y "A-Anime openings?"
        y "I guess I haven't really considered watching anime."
        y "Let alone considered listening to the openings."
        show natsuki 1a zorder 3 at f21
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
            "Yuri turns around and gives me a wide smile as she notices me."
            "Natsuki looks at her and Yuri immediately looks away nervously."
            show natsuki zorder 3 at f21
            n "Oh, come on."
            "Natsuki takes her earphones off."
            n "You don't need to be embarrassed because I'm here."
            n "Besides, we're friends, remember?"
            show natsuki zorder 2 at t21
            show yuri zorder 3 at f22
            y "R-Right."
            "Yuri follows Natsuki's lead and takes off her earphones as well."
            y "How long have you been here, [player]?"
            show yuri zorder 2 at t22
            mc "I just got here."
            mc "I think those earphones drowned out the noise of me coming in."
            show yuri zorder 3 at f22
            y "I apologize for not noticing."
        elif natsuki_date:
            "I put a hand on Natsuki's shoulder."
            mc "Natsuki?"
            "Natsuki turns around slowly and notices me."
            "She smiles at me but immediately wipes it off her face when she sees Yuri looking."
            show natsuki zorder 3 at f21
            n "[player]!"
            "She takes off her earphones."
            n "When did you get here?"
            show natsuki zorder 2 at t21
            mc "I just arrived."
            mc "You probably didn't hear me come in because you were listening to music."
            "Yuri takes off her earphones as well."
            show yuri zorder 3 at f22
            y "S-Sorry, we were a bit preoccupied."
        else:
            "I try to grab both of their attention again."
            mc "Guys...hello?"
            show natsuki zorder 3 at f21
            n "Is that..."
            "Natsuki takes off her earphones and turns towards me."
            n "[player]?"
            n "When did you get here?"
            show natsuki zorder 2 at t21
            show yuri zorder 3 at f22
            y "[player] is here?"
            "Yuri follows Natsuki's lead and takes her earphones off as well."
            y "I apologize, I didn't hear you come in."
        show yuri zorder 2 at t22
        mc "That's fine."
        mc "I'm just wondering what you two are doing here."
        mc "I didn't even know you'd be here this early as well."
        show natsuki zorder 3 at f21
        n "Sayori sent me a message to be here early."
        n "Yuri got the same one."
        show natsuki zorder 2 at t21
        mc "So what exactly are you doing here?"
        show yuri zorder 3 at f22
        y "We're not entirely sure."
        y "She just told us to meet at the clubroom."
        y "There wasn't any specific instruction beyond that..."
        show natsuki zorder 3 at f21
        show yuri zorder 2 at t22
        n "So we took it upon ourselves!"
        show natsuki zorder 2 at t21
        mc "To do...{i}what{/i} exactly?"
        show natsuki zorder 3 at f21
        n "Take a look."
        show natsuki zorder 2 at t21
        "Natsuki and Yuri move their chairs out of the way."
        "There is a large piece of paper on the desks they combined."
        mc "You two were...drawing something?"
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
            show yuri 1ba zorder 2 at t11
            y "Oh, [player]."
            if yuri_date:
                y "Nice seeing you here."
            else:
                y "I wasn't expecting to see you here."
            mc "What are you doing?"
            mc "And what's Natsuki doing?"
        else:
            "I approach Natsuki."
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
