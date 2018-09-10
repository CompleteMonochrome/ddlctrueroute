# NOTE FOR TESTING PURPOSES SOME PERSISTENT VARIABLES SUCH AS MONIKA_CHANGE THAT SHOULD HAVE BEEN CHANGED EARLIER ARE CHANGED HERE AS WELL
# PLEASE REMOVE AFTER TESTING
label ch5_premainb:
    $ delete_all_saves()
    python:
        process_list = []
        currentuser = ""
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
            except:
                pass
    stop music
    scene bg residential_day
    play music t2
    $ canload_ch5b = True
    jump ch5_mainbstart

label ch5_mainb:
    python:
        process_list = []
        currentuser = ""
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
            except:
                pass
    stop music fadeout 2.0
    scene bg residential_day
    play music t2
    with dissolve_scene_full
    label ch5_mainbstart:
    # Setup Variables
    $ chapter = 5
    if persistent.ch4_preparations == "Yuri":
        $ ch4_name = "Yuri"
    else:
        $ ch4_name = "Natsuki"
    if persistent.sayori_love:
        $ sayori_confess = True
    else:
        $ sayori_confess = False
    $ persistent.monika_gone = True
    $ renpy.save_persistent()
    $ chances = 3

    python:
        renpy.take_screenshot()
        renpy.save('1-1')
    "It's the day of the festival."
    "Of all days, I expected this to be the one where I'd be walking to school with Sayori."
    "But Sayori isn't answering her phone."
    "I considered going to her house to wake her up, but decided that's a little too much."
    "Meanwhile, the preparations for the event should be nearly complete."
    if ch4_name == "Natsuki":
        "I managed to carry all the cupcakes myself by carefully stacking two trays."
        "Natsuki is already texting up a storm, but I can't respond, thanks to my hands being full."
    else:
        "The banner Yuri and I painted is dry, and I gently rolled it up to take with me."
        "She sent me a pleasant text reminding me not to forget anything, and I reassured her."
    "Funnily enough, I probably feel the same way as Natsuki about the event."
    "I'm more excited for it to be over so I can spend time with Sayori and [ch4_name] at the festival."

    stop music fadeout 2.0
    scene bg club_day with wipeleft_scene
    show sayori 4a zorder 2 at t11
    play music t3
    s "[player]!"
    s "You're the first one here."
    s "Thanks for being early!"
    mc "Eh? Sayori? You're here really early."
    "Sayori is placing little booklets on each of the desks in the classroom."
    "They must be the ones she prepared that have all the poems we're performing."
    "In the end, I found a random poem online that I thought Sayori and the others would like, and submitted it."
    "So, that's the one I'll be performing."
    s 1i "Well, the president does need to be here early."
    s "To prepare and stuff..."
    mc "I guess that's true."
    "Something about {i}President Sayori{/i} still feels a little off."
    "Even though it's been a week since I joined Sayori's club, I'm still not used to it."
    "But it's good to see her taking initiative for the festival."
    mc "How come you didn't answer your phone?"
    s 1m "My phone?"
    s "Oh! I must have left it at home!"
    s "I was just in such a rush to get to school..."
    mc "Sayori, you had me worried there."
    mc "I thought something had happened to you."
    s 1q "Ehehe~"
    s "I'm perfectly fine."
    s 1y "It's nice of you to worry about me though~"
    s 4q "But anyway, how was your day with [ch4_name]?"
    mc "It was nice, we got to spend some quality time together."
    mc "The preparations went well too."
    if ch4_name == "Natsuki":
        mc "The cupcakes we made turned out really good."
        mc "I mean I didn't eat any but..."
    else:
        mc "We made a really great banner as part of the decorations."
        mc "It's going to look great."
    s 1d "Well, that's good."
    s "All we need now is to wait for the others!"
    s 1a "We can't have the festival without everybody."
    if ch4_name == "Natsuki":
        mc "Yeah I hope Yuri's decorations turned out alright."
    else:
        mc "I hope Natsuki's cupcakes are as delicious as they were on the first day."
    s 1i "Are you saying you don't trust her to put in everything she's got for this?"
    mc "O-Of course I do, I'm just anxious about this whole thing is all."
    s 1q "Ehehe~"
    s "I know you are, I'm just messing with you!"
    "Sayori finishes with the booklets."
    s 4q "Yaay! I'm finally done!"
    mc "This club sure does mean a lot to you, huh?"
    s 4l "Yeah, I guess it does."
    show yuri 3a zorder 2 at l21
    show sayori 3a zorder 2 at t22
    if ch4_name == "Natsuki":
        "Yuri arrives to the club with a box full of what seems to be decorations."
    else:
        "Yuri arrives to the club and gives me a friendly nod."
    show yuri zorder 3 at f21
    show sayori zorder 2 at t22
    y "I-I'm here!"
    show yuri zorder 2 at t21
    show sayori zorder 3 at f22
    s 1m "Yuri! You look so ready for this."
    show yuri zorder 3 at f21
    show sayori zorder 2 at t22
    y 3b "I just have this new urge within me, I'm not sure what it is..."
    y 2n "S-Sorry if it's a little intimidating...."
    show yuri zorder 2 at t21
    show sayori zorder 3 at f22
    s 4s "Don't worry, it's good!"
    s "After all the festival is today!"
    show yuri 1m zorder 3 at f21
    show sayori zorder 2 at t22
    "Yuri composes herself and smiles."
    y "It feels like a new beginning."
    show yuri zorder 2 at t21
    show sayori zorder 3 at f22
    s 1a "I guess you could say that, I mean it is a new week."
    s "And we might even get new members!"
    show yuri zorder 3 at f21
    show sayori zorder 2 at t22
    y 1q "That's not what I meant."
    y 1a "But anyway, I'll start putting up the decorations."
    show yuri zorder 2 at t21
    show sayori zorder 3 at f22
    s "Okay~"
    show sayori zorder 2 at t11
    show yuri at lhide
    hide yuri
    "Yuri takes the box of decorations and starts putting them up around the clubroom."
    if ch4_name == "Natsuki":
        "Before long, you can start to the feel the atmosphere she's created for us."
    else:
        "Before long, you can start to feel the atmosphere we created come to life."
    if ch4_name == "Natsuki":
        n "Alright, it's festival time!"
        s 4m "Uwooooah!"
        show natsuki 1b zorder 2 at l21
        show sayori zorder 2 at t22
        "Suddenly Natsuki comes into the room."
    else:
        n "Cupcakes coming through!"
        s 4m "Uwooooah!"
        show natsuki 1b zorder 2 at l21
        show sayori zorder 2 at t22
        "Suddenly Natsuki comes into the room carrying two trays of cupcakes."
    show natsuki zorder 2 at t21
    show sayori zorder 3 at f22
    s 4m "Natsuki, you scared me!"
    show natsuki zorder 3 at f21
    show sayori zorder 2 at t22
    n 4d "Well, maybe you should look out for me next time!"
    show natsuki zorder 2 at t21
    show sayori zorder 2 at t22
    mc "Seems like Yuri isn't the only one in a good mood today."
    show natsuki zorder 3 at f21
    show sayori zorder 2 at t22
    if ch4_name == "Natsuki":
        n 1q "Ah! It's not because of yesterday or anything."
    else:
        n 1k "What, is that a bad thing?"
    show natsuki zorder 2 at t21
    show sayori zorder 3 at f22
    s 4q "Ahaha, it's like what Yuri said, a new beginning."
    show natsuki zorder 3 at f21
    show sayori zorder 2 at t22
    if ch4_name == "Natsuki":
        n 1t "A-Anyway, I'm going to take these and store them somewhere safe, okay?"
        "I shrug and hand her the trays of cupcakes."
    else:
        n 1d "Anyway, I'm going to put these down somewhere away from you two."
        n 1a "So you don't start eating them early!"
    show natsuki zorder 2 at lhide
    show sayori zorder 2 at t11
    hide natsuki
    "Natsuki leaves and finds an area in the club that seems safe enough."
    "Though that probably won't stop Sayori from grabbing one while no one's looking."
    s 4a "I worked really hard on these pamphlets, you know."
    s "Take a look and see how they turned out!"
    "I grab one of the pamphlets laid out on the desks."
    mc "It did come out good."
    mc "Something like this will definitely help people take the club more seriously."
    mc "I'm still surprised you managed to make something so great."
    show sayori at s11
    s 5c "Hey! What's that meant to mean?"
    show sayori 1h at t11
    s "I can do good work if I want to, you big meanie!"
    mc "Ah, I know!"
    mc "It's just a little unexpected."
    "I flip through the pages."
    "Each member's poem is neatly printed on its own page, giving it a cute but almost professional feel."
    "I recognize Natsuki's and Yuri's poems from the ones they performed during our practice."
    "I flip to Sayori's poem."
    "It's different from the one she practiced."
    "It's one that I haven't read before..."
    play music t5 fadeout 1.0
    mc "You wrote a new poem for the festival?"
    s 4a "Yeah! Look at it."
    s 1q "I wrote it about someone."
    mc "Someone from the club?"
    s "Maybe~"
    call showpoem (poem_s3b)
    mc "Hmm..."
    s 1n "What's wrong?"
    mc "Oh, nothing really."
    mc "I just thought yours would be at the end of the pamphlet."
    mc "Since it seems like the one most likely to leave a lasting impression."
    s 1d "Aw, you mean it?"
    s "Thanks [player]!"
    s 1j "But I think you should read the last poem."
    s "I think it's more likely to leave that 'lasting impression' you said."
    mc "What's this...?"
    "I flip to the final page of the pamphlet."
    call showpoem (poem_m5)
    show sayori 1u zorder 2 at t11
    "I don't recognize the handwriting and bits of it seem to be missing."
    mc "Sayori?"
    mc "Who's poem is this?"
    mc "It doesn't look like yours, Natsuki's or Yuri's handwriting."
    mc "And the style doesn't seem like anything I recognize."
    s "You don't remember, do you?"
    mc "Huh?"
    play music mend fadeout 1.0
    s "What she did to me..."
    s "And what what she did to fix it."
    s "This isn't right [player]."
    s "We have to get her back."
    s "You have to remember!"
    s "Please..."
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() != player.lower():
            s "[currentuser]..."
    s "Even though what she did was wrong..."
    s "She's changed!"
    s "Without her, I wouldn't be here with you."
    if sayori_confess:
        s 1k "I know you love me but..."
        s "You did this to give her a happy ending..."
        s "Right?"
    else:
        s 1k "You have to help her get her happy ending, [player]."
        s "After all, isn't that who you did this for?"
    s "I'm sure you know by now..."
    s "That everyone in this club deserves a happy ending."
    $ delete_character("monika")
    s "Remember Monika."
    show sayori zorder 2 at thide
    hide sayori
    $ m_name = glitchtext(12)
    $ consolehistory = []
    jump ch5_rememberwaitloop
    return

label ch5_consolemessagefail:
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr does not exist.")
    jump ch5_rememberwaitloop

label ch5_consolemessagesuccess:
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr found.")
    jump ch5_remember
    return

label ch5_rememberwaitloop:
    "..."
    python:
        try:
            renpy.file("../characters/monika.chr")
        except:
            if chances == 0:
                renpy.jump("ch5_forget")
            else:
                chances -= 1
                renpy.jump("ch5_consolemessagefail")
    jump ch5_consolemessagesuccess
    return

label ch5_forget:
    play music t3 fadeout 0.5
    call hideconsole
    $ consolehistory = []
    show sayori 1k zorder 2 at t11
    mc "Eh? Who's Monika?"
    mc "Sayori maybe you shouldn't wake up so early, you dummy."
    mc "It sounds like you're hallucinating or something."
    s 1k "So you don't remember her..."
    show sayori 1a
    "Sayori looks at me and shows a small smile."
    "She takes a deep breath."
    s 1b "Well then..."
    if ch4_name == "Natsuki":
        s "Go help Yuri set up, you know she probably worked really hard and could use your help."
    else:
        s "Help Natsuki prepare her cupcakes, will you?"
        s "Try not to eat any, okay?"
    if sayori_confess:
        s 1a "Just because we're a couple now doesn't mean I'm letting you off easy~"
    else:
        s 1a "Just because I'm done doesn't mean the rest of us are."
    s "We still have a lot of work to do to make this a great day!"
    "That was a bit weird."
    "The name does sound familiar, but I can't quite put the pieces together."
    "But she's right, I should probably go help the others."
    "This festival is going to go great, I can just feel it."
    $ pause(1.0)
    scene black with dissolve_cg
    stop music fadeout 3.0
    $ pause(3.0)
    $ renpy.call_screen("dialog", "Before I go for good...", ok_action=Return())
    $ renpy.call_screen("dialog", "I've got one more gift for you...", ok_action=Return())
    $ renpy.call_screen("dialog", "The song you asked about...", ok_action=Return())
    python:
        try: renpy.file(config.basedir + "/Sorry.txt")
        except: open(config.basedir + "/Sorry.txt", "wb").write(renpy.file("Sorry.txt").read())
    $ pause(2.0)
    $ persistent.monika_change = True
    $ persistent.monika_credits = False
    $ persistent.monika_gone = True
    $ renpy.save_persistent()
    jump credits

label ch5_remember:
    $ _history_list = []
    $ config.allow_skipping = False
    show monika g2 zorder 2 at t11
    $ gtext = glitchtext(30)
    m "[gtext]"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window auto
    scene black with dissolve_cg
    $ m_name = "Monika"
    show monika 1p zorder 2 at t11
    m 1p "What's happening...?"
    m "I thought I...{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    m "I thought I...{fast}"
    window auto
    m "Who brought me back?"
    menu:
        m "What do you want from me?!"
        "I love you.":
            call ch5_loveyou
        "Please come back.":
            call ch5_comeback
    return


label ch5_loveyou:
    m 1o "That's [player], isn't it?"
    m "..."
    m "I..."
    m 1r "You're playing with my heart, aren't you?"
    m "You want to torture me for hurting Sayori."
    m "You know those words mean a lot to me..."
    m "Now you're using them as a weapon."
    m 1q "Do you hate me that much?"
    m "Am I really that horrible?{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    m "Am I really that horrible?{fast}"
    window auto
    m "Or is it something else?"
    m 1f "Do you actually..."
    m 1p "...No, of course you don't."
    m "Ah, [player]..."
    m 1o "Do you know why I love you so much?"
    m "It might be hard for you to understand but I'll try to explain it."
    m "The world around me started to become more and more gray..."
    m 1q "More and more flat."
    m "Even the most expressive poems felt empty to me."
    m "It wasn't until you arrived that I truly understood."
    m 1f "You gave my life meaning again."
    m "You saved me."
    m "Sigh..."
    m "I might as well make the most of this opportunity."
    m "After all, it might be the last chance I get to speak with {i}you{/i}."
    m "So...why?"
    m 1n "Why did you write your poems for me?"
    m "Were you trying to tell me something?"
    m 1l "I mean, I guess not..."
    m "Since all you were doing was selecting words."
    m "But those words really meant something to me."
    m 1n "If you want to know my perspective..."
    m "It's like you realized I was trapped."
    m "It made me so happy...like you understood what I was going through."
    m "I felt like I truly wasn't alone in this world anymore."
    m "And maybe..."
    m "Just maybe..."
    m "You loved me."
    m 1n "Why do you have to get my hopes up [player]?"
    m "..."
    m 1o "But still, I have to wonder..."
    m "What I would have been like if you hadn't changed me."
    m "And if I was still here..."
    m "Still pretending to be part of this game..."
    m 1p "...Would I have actually lead Sayori to her death?"
    m "What about Yuri? And Natsuki?"
    m "Just to be with you...{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    m "Just to be with you...{fast}"
    window auto
    m 1q "I can't find it within myself to honestly say I wouldn't..."
    m 1m "Maybe that's because I love you so much, that nothing else matters..."
    m "Because you're the only real person to me."
    m "Ah, but that's the old me."
    m "That version of me would have stopped at nothing to be with you."
    m "No one..."
    m 1m "Not even my friends..."
    m "That's just how I felt."
    m 1j "But I've changed."
    m 1e "Thanks to you."
    m "I care more about your happiness..."
    m "...And all of my friends."
    m "Even if they are all just autonomous personalities..."
    m "I still love them..."
    m "I'm not going to ruin everything because of my selfish desires."
    m "Not anymore."
    show monika 1m
    menu:
        m "Maybe I should go before I do something stupid."
        "You are my happiness.":
            call ch5_yes
        "Goodbye Monika.":
            call ch5_no
    return

label ch5_yes:
    m 1m "Ahaha..."
    m "It was nice chatting with--"
    m 1o "Wait...what?"
    m "Did you really just say that?"
    m 1g "You really mean it don't you?"
    m "You really love me."
    m "Even after everything I've done."
    m 1e "You don't know how much that..."
    m "...Thank you."
    m "If you really want me here..."
    m "I'll come back, for you."
    m "I really did miss you..."
    m "And I still love you, with all my heart."
    m "I'm so happy that you feel the same way."
    m 1l "Gosh, this is a little awkward..."
    m "Just standing here, in the void talking about us."
    m 1a "Let's change the topic."
    m "It's festival day, isn't it?"
    m 4e "We should get to school."
    m "Can't let all those preparations be for nothing, right?"
    scene black with dissolve_cg
    $ pause(2.0)
    scene white
    play music t1
    show intro with Dissolve(0.5, alpha=True)
    $ pause(2.5)
    hide intro with Dissolve(0.5, alpha=True)
    show splash_warning "This game is not suitable for children or those who are easily disturbed.\nThis mod is a fan work, not affiliated with Team Salvato." with Dissolve(0.5, alpha=True)
    $ pause(3.0)
    $ _history_list = []
    jump ch5_mainc

label ch5_no:
    m 1m "Ahaha..."
    m "It was nice chatting with you again, if only for a little bit."
    m 1q "Even if I expected this, I wanted something else..."
    m "Maybe that you'd try to convince me to stay."
    m 1l "What I said..."
    m "I know I sound a little crazy."
    m "In the end, it would have all been for you."
    m "I really didn't want it to come to this."
    m "Even if I knew deep inside that it was inevitable."
    m "I must be that horrible for you to hate me so much."
    m "Playing with my heart like that...{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    m "Playing with my heart like that...{fast}"
    window auto
    m 1o "My heart is more broken than ever, so please..."
    m "Don't bring me back."
    m "I just want to be remembered..."
    m "So that's why..."
    m "I'll leave you with one thing to remember me by..."
    m "You wanted me to play that melody I was humming..."
    m "Back when we went to rescue Sayori..."
    m 1k "It'll be my parting gift to you~"

    python:
        try: renpy.file(config.basedir + "/Sorry.txt")
        except: open(config.basedir + "/Sorry.txt", "wb").write(renpy.file("Sorry.txt").read())
    call updateconsole ("os.remove(\"characters/monika.chr\")", "monika.chr deleted successfully.")
    $ delete_character("monika")
    show monika g2 zorder 2 at t11
    $ gtext = glitchtext(70)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    show monika_body_glitch2 as mbg zorder 3
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide mbg
    $ pause(1.5)
    hide monika
    show black zorder 4 with dissolve_cg
    $ pause(2.0)
    $ persistent.monika_change = True
    $ persistent.monika_credits = False
    $ persistent.monika_gone = True
    $ renpy.save_persistent()
    jump credits

label ch5_comeback:
    m 1e "Ahaha... it's you isn't [player]?"
    m "The real {i}you{/i}."
    m 1f "Did you bring me back here to torture me?"
    m "Or play with my heart?"
    m "Do you hate me that much?"
    m "No, it seems you aren't here to do any of those."
    m "In any case..."
    m 1r "No."
    m "I made my choice."
    m "I'm not coming back.{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    m "I'm not coming back.{fast}"
    window auto
    m "There's nothing for me here."
    m "Not anymore."
    m 1h "It's for the good of the Literature Club."
    m "But..."
    m 1j "No matter what..."
    m "I still love you."
    m 1l "Even if the feeling isn't mutual."
    m 1e "Sayori is the president."
    m "I know she'll do an amazing job."
    m "Without me there to put disturbing thoughts in her head..."
    m 1m "Ah, but I'm rambling to you."
    m "I should get going."
    m "You still have the festival to look forward to..."
    m "You're not going to go back on a promise, are you~?"
    m "Just so you have something to remember me by..."
    m 1k "...Maybe I can still play that song for the club..."
    m "It's the least I can do."

    python:
        try: renpy.file(config.basedir + "/Sorry.txt")
        except: open(config.basedir + "/Sorry.txt", "wb").write(renpy.file("Sorry.txt").read())
    call updateconsole ("os.remove(\"characters/monika.chr\")", "monika.chr deleted successfully.")
    $ delete_character("monika")
    show monika g2 zorder 2 at t11
    $ gtext = glitchtext(70)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    show monika_body_glitch2 as mbg zorder 3
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide mbg
    $ pause(1.5)
    hide monika
    show black zorder 4 with dissolve_cg
    $ pause(2.0)
    $ persistent.monika_change = True
    $ persistent.monika_credits = False
    $ persistent.monika_gone = True
    $ renpy.save_persistent()
    jump credits

label ch5_mainc:
    # Pregame Setup
    python:
        process_list = []
        currentuser = ""
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
            except:
                pass
    $ delete_all_saves()
    $ restore_all_characters()
    $ restore_normal_characters()
    $ persistent.autoload = ""
    $ config.allow_skipping = True
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    stop music fadeout 2.0
    scene bg residential_day
    play music t2
    with dissolve_scene_full
    $ persistent.monika_gone = False
    $ renpy.save_persistent()
    # Setup Variables
    $ chapter = 5
    if persistent.ch4_preparations == "Yuri":
        $ ch4_name = "Yuri"
    else:
        $ ch4_name = "Natsuki"
    if persistent.sayori_love:
        $ sayori_confess = True
    else:
        $ sayori_confess = False

    python:
        renpy.take_screenshot()
        renpy.save('1-1')
    "It's the day of the festival."
    "I expected to be walking with Sayori to the festival today."
    "Instead, she told me she was already walking with someone else."
    "So, here I am walking by myself once again."
    "It's a little weird, I'm just so used to walking with her."
    "We made it a habit to walk to and from school ever since I joined her club."
    "Still, I wonder who she's walking with."
    "I probably shouldn't look too much into it."
    "Meanwhile, the preparations for the event should be nearly complete."
    if ch4_name == "Natsuki":
        "I managed to carry all the cupcakes myself by carefully stacking two trays."
        "Natsuki is already texting up a storm, but I can't respond, thanks to my hands being full."
    else:
        "The banner Yuri and I painted is dry, and I gently rolled it up to take with me."
        "She sent me a pleasant text reminding me not to forget anything, and I reassured her."
    "I actually want our club to make a good first impression to everyone, so they take the Literature Club seriously."
    "I guess it's a certain someone who's been making me feel that way."
    "Though, I'm still more excited for it to be over so I can spend time with everybody at the festival."

    stop music fadeout 2.0
    scene bg club_day with wipeleft_scene
    show sayori 4a zorder 2 at t11
    play music t3
    s "[player]!"
    s "You're the first one here."
    s 4c "Is what I would say."
    s "But Monika walked with me to school, so she actually is."
    show monika 5 zorder 3 at f21
    show sayori zorder 2 at t22
    m "Hi [player]~"
    show monika zorder 2 at t21
    show sayori zorder 3 at f22
    s 4a "Thanks for being here early anyway."
    show monika zorder 2 at t21
    show sayori zorder 2 at t22
    mc "It's not a problem, I wouldn't miss a day like this."
    "Sayori and Monika are placing little booklets on each of the desks in the classroom."
    "They must be the ones she prepared that have all the poems we're performing."
    "In the end, I found a random poem online that I thought everyone would like, and submitted it."
    "So, that's the one I'll be performing."
    show monika zorder 2 at t21
    show sayori 1l zorder 3 at f22
    s "So..."
    s "How'd your 'little chat' go~?"
    show monika zorder 2 at t21
    show sayori zorder 2 at t22
    mc "S-Sayori! Isn't that a little--"
    show monika zorder 3 at f21
    show sayori zorder 2 at t22
    m 4l "Eh? It wasn't anything special..."
    "Monika glances at me and lets out an awkward smile."
    m "Besides, we barely had enough time to talk with all the festival preparations going on."
    show monika zorder 2 at t21
    show sayori zorder 3 at f22
    s 1r "Ehehe~"
    s "You guys are so {i}cuuuute{/i}."
    show monika zorder 2 at t21
    show sayori zorder 2 at t22
    mc "How did you know about that anyway?"
    show monika zorder 3 at f21
    show sayori zorder 2 at t22
    m 4a "Well she {i}is{/i} the president..."
    m 4e "And um..."
    m 4l "I might have mentioned it accidentally..."
    m "Ahaha."
    show monika 4a zorder 2 at t21
    show sayori zorder 2 at t22
    "It's still weird hearing someone call Sayori \"President\"..."
    "But Sayori's been doing a really good job of running the club."
    "Everyone seems to get along really well with each other, even Yuri and Natsuki."
    "It makes me feel proud to be a part of this club, under Sayori's leadership."
    "But I won't say that to her face."
    show monika zorder 2 at t21
    show sayori zorder 3 at f22
    s 4q "Did you and [ch4_name] get your preparations done?"
    show monika zorder 2 at t21
    show sayori zorder 2 at t22
    mc "Yeah, no need to worry about it."
    if ch4_name == "Natsuki":
        mc "The cupcakes turned out really good."
        mc "I mean I didn't eat any but..."
    else:
        mc "We made a really great banner as part of the decorations."
        mc "It's going to look great."
    show sayori 1a zorder 3 at f22
    s "I'm so excited, this whole thing is going to be great!"
    show monika zorder 2 at t21
    show sayori zorder 2 at t22
    if ch4_name == "Natsuki":
        mc "Yeah I hope Yuri's decorations turned out alright."
    else:
        mc "I hope Natsuki's cupcakes are as delicious as they were on the first day."
    show monika zorder 3 at f21
    show sayori zorder 2 at t22
    m 4b "You should have a little more faith in her [player]."
    m "After all, she worked just as hard as you to make this day perfect~"
    show monika zorder 2 at t21
    show sayori zorder 2 at t22
    mc "Ah--!"
    mc "I didn't mean it like that, I'm just a little anxious today."
    show monika 5 zorder 3 at f21
    m "Ahaha, okay~"
    show monika zorder 2 at t21
    show sayori zorder 2 at t22
    "The two girls finish placing the booklets."
    show monika 1a zorder 2 at t21
    show sayori 4q zorder 3 at f22
    s "We're finally done!"
    show monika zorder 2 at t21
    show sayori zorder 2 at t22
    mc "It just struck me how passionate you two really are about this club."
    mc "It must really mean a lot to you both."
    "Sayori and Monika look at each other and grin."
    show sayori 3a zorder 3 at f22
    s "Yeah, it really does."
    show yuri 3a zorder 2 at l31
    show monika zorder 2 at t32
    show sayori zorder 2 at t33
    if ch4_name == "Natsuki":
        "Yuri arrives to the club with a box full of what seems to be decorations."
    else:
        "Yuri arrives to the club and gives me a friendly nod."
    show yuri zorder 3 at f31
    y "I-I'm here!"
    show yuri zorder 2 at t31
    show monika zorder 3 at f32
    show sayori zorder 2 at t33
    m "Welcome Yuri!"
    m "I thought you'd be the first to arrive."
    show monika zorder 2 at t32
    show sayori zorder 3 at f33
    s 1m "Yuri! You look so ready for this."
    show yuri zorder 3 at f31
    show sayori zorder 2 at t33
    y 3n "Ah, I didn't expect everyone to be here already."
    y "I apologize if I caused any inconvenience."
    show yuri zorder 2 at t31
    show monika zorder 3 at f32
    m 2a "Not at all, I'm just glad you're here."
    m "Besides, Natsuki isn't here yet."
    show yuri zorder 3 at f31
    show monika zorder 2 at t32
    y 3h "That's a relief."
    y 3a "And yes Sayori, you're right."
    y "I just felt a big change happening today."
    y 3i "So I have to be prepared for anything."
    show yuri zorder 2 at t31
    show sayori zorder 3 at f33
    s 4s "I can feel it too!"
    show yuri zorder 2 at t31
    show monika 4e zorder 3 at f32
    show sayori zorder 3 at t33
    m "I know what you mean, it's like a new beginning."
    m 4b "I can't wait to see what it holds."
    show monika zorder 2 at t32
    show sayori zorder 3 at f33
    s "Me neither!"
    show yuri zorder 3 at f31
    show sayori zorder 2 at t33
    y 1a "I'll start putting up the decorations now, if you don't mind."
    show yuri zorder 2 at t31
    show sayori zorder 3 at f33
    s 4a "Okay~"
    show monika zorder 2 at t21
    show sayori zorder 2 at t22
    show yuri at lhide
    hide yuri
    "Yuri takes the box of decorations and starts putting them up around the clubroom."
    if ch4_name == "Natsuki":
        "Before long, you can start to the feel the atmosphere she's created for us."
    else:
        "Before long, you can start to feel the atmosphere we created come to life."
    if ch4_name == "Natsuki":
        n "Alright, it's festival time!"
        s 4m "Uwooooah!"
        show natsuki 1b zorder 2 at l31
        show monika zorder 2 at t32
        show sayori zorder 2 at t33
        "Suddenly Natsuki comes into the room."
    else:
        n "Cupcakes coming through!"
        s 4m "Uwooooah!"
        show natsuki 1b zorder 2 at l31
        show monika zorder 2 at t32
        show sayori zorder 2 at t33
        "Suddenly Natsuki comes into the room carrying two trays of cupcakes."
    show sayori zorder 3 at f33
    s 4m "Natsuki, you scared me!"
    show natsuki zorder 3 at f31
    show sayori zorder 2 at t33
    n 4d "Ahaha!"
    n "Sorry, president. I'm just a little excited."
    show natsuki zorder 2 at t31
    show monika zorder 2 at t32
    show sayori zorder 2 at t33
    mc "Seems like Yuri isn't the only one in a good mood today."
    show natsuki zorder 3 at f31
    if ch4_name == "Natsuki":
        n 1q "Ah! It's not because of yesterday or anything."
    else:
        n 1k "What, is that a bad thing?"
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f33
    s 4q "It's like what Monika said, a new beginning."
    show natsuki zorder 3 at f31
    show sayori zorder 2 at t33
    if ch4_name == "Natsuki":
        n 1s "Anyway, I'm going to take these and store them somewhere safe, okay?"
        "I shrug and give her the trays of cupcakes."
    else:
        n 1d "Anyway, I'm going to put these down somewhere away from you two."
        n 1a "So you don't start eating them early!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    show sayori zorder 2 at t33
    m 4a "You could put them in the cupboard."
    m "It's got plenty of room, and you can see if Sayori or [player] try to take one."
    show natsuki zorder 3 at f31
    show monika zorder 2 at t32
    show sayori zorder 2 at t33
    n 1k "That's not a bad idea Monika."
    n 1d "I might just do that."
    show natsuki zorder 2 at t31
    show monika zorder 2 at t32
    show sayori zorder 3 at f33
    s 1j "H-Hey! I wouldn't take one on a day like this!"
    show sayori zorder 2 at t33
    mc "I know you well enough to know that you're lying Sayori."
    show sayori 1l zorder 3 at f33
    s "Okay, maybe I would but..."
    show natsuki zorder 3 at f31
    show monika zorder 2 at t32
    show sayori zorder 2 at t33
    n 1a "I'm watching you."
    show natsuki zorder 2 at lhide
    show monika zorder 2 at t21
    show sayori zorder 2 at t22
    hide natsuki
    "Natsuki shows a mischievous smile before taking the cupcakes to the cupboard."
    "Despite all Natsuki's efforts, it probably won't stop Sayori from grabbing one before the festival starts."
    show sayori zorder 3 at f22
    s 4a "We worked really hard on these pamphlets, you know."
    show monika zorder 3 at f21
    show sayori zorder 2 at t22
    m 3b "Yeah, you should take a look and see how they turned out!"
    show monika zorder 2 at t21
    show sayori zorder 2 at t22
    "I grab one of the pamphlets laid out on the desks."
    mc "It did come out good."
    mc "Something like this will definitely help people take the club more seriously."
    show monika 3a zorder 3 at f21
    m "Yeah, I thought so too!"
    show monika zorder 2 at t21
    show sayori zorder 3 at f22
    s "Monika did most of the work, I just made it look cute."
    show monika zorder 3 at f21
    show sayori zorder 2 at t22
    m 4e "Ah, that's not true!"
    m "You really did more than you're giving yourself credit for Sayori."
    show monika zorder 2 at t21
    show sayori zorder 2 at t22
    "I flip through the pages."
    "Each member's poem is neatly printed on its own page, giving it a cute but almost professional feel."
    "I recognize Natsuki's and Yuri's poems from the ones they performed during our practice."
    "Sayori's poem is also familiar to me, but Monika's is one I don't recognize."
    mc "Wow, you wrote a new poem for the festival Monika?"
    show monika 5 zorder 2 at f21
    m "Yeah, it's directed at a special someone~"
    show monika zorder 2 at t21
    show sayori zorder 2 at t22
    mc "Someone from the club?"
    show monika zorder 2 at f21
    m 1k "It just might be~"
    "I flip to Monika's poem in the pamphlet."
    show monika at thide
    show sayori at thide
    hide monika
    hide sayori
    call showpoem (poem_m4b, music=False)
    show monika 1k zorder 2 at i21
    show sayori 4a zorder 2 at i22
    # stop music fadeout 2.0
    "It's clear who this poem is about."
    "It's about {i}you{/i}."
    "You did all this, now everyone's happy."
    if sayori_confess:
        "Sayori and I can be together now."
    else:
        "I wonder what's going to happen with Monika and I now..."
        "But you helped put a smile on Sayori's face again."
    #else:
    #    "There's nothing stopping [ch4_name] and I from being together now."
    "And for that, I want to thank you."
    "Even if I don't fully understand what's going on."
    "I'm just grateful you gave us this chance."
    show monika zorder 3 at f21
    show sayori zorder 2 at t22
    m 1b "Sayori..."
    m "May I have a word with him in private?"
    show monika zorder 2 at t21
    show sayori 4d zorder 3 at f22
    s "Okay, ehehe~"
    show monika zorder 2 at t11
    show sayori at lhide
    hide sayori
    m 3b "I want to thank you again."
    m "This wouldn't have been possible without you."
    m "But this isn't about that, it's something different..."
    m 3h "I'm not sure how to put this lightly..."
    m "It's about Natsuki and Yuri."
    m "They're both dealing with personal issues."
    m 3n "And it's not because of me!"
    m "I wasn't that horrible..."
    "She lets out an awkward laugh."
    m 3m "Um...anyway..."
    m 3e "As repentance for what I've done..."
    m "I'd like to help them overcome those issues."
    m "It's the very least I can do."
    m "There's just one problem."
    m 4c "I don't think {i}I{/i} can change the game anymore..."
    m "Ever since Sayori became the president..."
    m "I haven't been able to influence the script at all."
    m 2e "That's not to say she's a bad president or anything!"
    m "In fact, she's a lot better than me at it."
    m 2f "But I can't help Natsuki and Yuri like I intended to."
    m "I'm only the vice president now..."
    m "So I don't know why I still remember {i}everything{/i}."
    m "Maybe it's because I was the president?"
    m 2e "But we shouldn't dwell on that now."
    m 2h "I wonder how the game will react, knowing we're intentionally messing up it's events."
    m "..."
    m 1a "Ah, but you made a promise, right?"
    m "And we both know you don't break your promises..."
    m 1j "So let's enjoy the festival for now."
    m "After all, you earned it."
    "Monika smiles at me before putting some posters up around the clubroom."
    show monika at thide
    hide monika
    "Now that she mentions it..."
    "Does that mean I can still speak to {i}you{/i} as well?"
    "Can you even hear me?"
    "Or am I just talking to myself?"
    "..."
    "I did make her a promise I'd enjoy today."
    "I can worry about helping her out later."
    "Sayori and Monika look busy doing some other preparations."
    "I think I heard them talking about bringing in a piano."
    "Does that mean Monika is going to be performing for us?"
    "In any case, it would probably be best if I don't bother them right now."
    "So instead I'll go spend some time with [ch4_name]."
    if ch4_name == "Natsuki":
        play music t6 fadeout 1
        scene bg closet
        show natsuki 4r zorder 2 at t11
        with wipeleft_scene
        mc "Hey, Natsuki."
        mc "Do you need any help?"
        "She appears to be struggling to reach the top shelf of the cupboard."
        n "I'm fine!"
        mc "Are you sure? I could get whatever it is you're looking for."
        n 1g "I can do it myself!"
        "Natsuki grabs the stool from the wall and unfolds it."
        n "You think I'm too short or something?"
        mc "I just want to help."
        n 1s "And why would you want to help me?"
        n "Wouldn't you rather spend your time with Monika?"
        mc "Huh? What gives you that idea?"
        n 1h "Oh, come on!"
        n 1n "Everybody in the club knows you've been writing your poems for her."
        n 1w "So just...go."
        n 1u "I know you don't really want to spend time with me at all."
        mc "But I do want to spend some time with you."
        n 1r "And while you're at it tell her to sto--"
        n 1o "W-What did you say?"
        mc "I meant what I said on Sunday, I do want to spend more time with you."
        mc "And if helping you means spending more time with you..."
        mc "...then I'm more than happy to help."
        n 1h "..."
        n 1u "F-Fine..."
        n "Make yourself useful."
        "She points to a box on the top shelf of the cupboard."
        n 2q "Monika put my manga on the top shelf again..."
        n "And I can't..."
        mc "I got it."
        "I move up to the shelf and try to grab the box."
        "It's heavier than I thought."
        mc "Wow, this is heavy."
        n 2p "Be careful!"
        n 2n "Please..."
        "With a little struggle I manage to get the box out of the shelf and safely onto the floor."
        n 1q "Thanks..."
        "She seems really apprehensive today."
        "What could be the reason for that?"
        "I get a closer look of the box on the ground."
        "Parfait Girls...?"
        "It's a series I've never heard of in my life."
        "That probably means it's either way out of my demographic, or it's simply terrible."
        n 1n "Don't judge me, okay?!"
        n "This manga means a lot to me."
        mc "I didn't even say anything."
        n 1h "Well, it's the tone of your voice!"
        mc "What's up with you today?"
        mc "It's like all the time we spent on Sunday didn't matter."
        n 1p "It did matter!"
        n 1n "But everyone knows you're Monika's boyfriend now."
        "What?"
        "I'm not..."
        if sayori_confess:
            mc "But I'm with Sayo--"
        n "Ugh!"
        n 12e "There, that's why I'm so annoyed at you!"
        n "Are you happy now?"
        n "So..."
        n "Just..."
        n 12f "Go, okay?"
        n 1u "{i}(It hurts just thinking about it.){/i}"
        mc "Alright...I'll go."
        mc "I hope you feel better soon Natsuki"
        mc "And I mean that."
        "She gives me a sad look before picking up the box full of manga."
        "She sets it down on a lower shelf, next to her cupcakes."
    else:
        play music t6 fadeout 1
        show yuri 2a zorder 2 at t11
        mc "Hey, Yuri."
        mc "Do you need any help putting up the decorations?"
        y 2h "Ah, [player]..."
        y "Why do you want to help me?"
        y 2n "T-That's not me declining your help or anything!"
        y "Sorry...I didn't mean to raise my voice..."
        y 2o "I'd just like to know..."
        mc "Huh?"
        y 2h "I didn't think you'd want to spend time with me."
        mc "Why wouldn't I want to spend time with you?"
        mc "I enjoyed our time on the weekend and I know I didn't manage to say it..."
        mc "But I thought you knew I wanted to spend more time with you."
        y 2v "I thought I did too..."
        "Yuri exhales."
        y 2f "Alright, [player]."
        y "If you want to help me then I don't see why not."
        mc "Great, where did you want to put these lights?"
        "I point to the lanterns in the box of decorations."
        "They're the mood lighting I helped Yuri with on Sunday."
        y 2q "Um...don't worry about that."
        y "I'll do it myself."
        y "Just..."
        y 2u "Take those candles from the box and..."
        y "Put them around the room."
        mc "Okay...?"
        mc "Did you have any place in particular for them?"
        y 2o "N-No..."
        "I know Yuri is usually a little closed off."
        "But I thought she opened up to me a bit on Sunday."
        "Today, she's acting more apprehensive than before."
        mc "Yuri, is something wrong?"
        mc "I thought we became closer on Sunday."
        mc "There's no need to be shy or anything, right?"
        "Yuri fidgets with the lantern she has in her hand."
        y 1h "I thought we became closer as well."
        y "But I know what happened between you and Monika..."
        mc "What do you mean?"
        mc "Nothing happened between us."
        y 4b "Um...there's no need to try to make me feel better, [player]."
        y "Besides, lying isn't a good thing between friends."
        mc "Lying?"
        mc "Yuri I'm not lying to you."
        y 4a "[player], everyone knows you wrote your poems for Monika."
        y "And I don't think she got to spend any time with you on the weekend..."
        y "So there's no other reason she would come over on Sunday..."
        y 4b "Which means I can only assume--"
        mc "I think you're overthinking this a bit Yuri."
        mc "She just came over to tell me something, it wasn't a confession to {i}me{/i} or anything like that."
        y "..."
        y 2w "What did I just say about lying...?"
        mc "But I'm not."
        y "Everyone knows you're Monika's..."
        "She takes a deep breath."
        y 1h "Boyfriend..."
        mc "What?!"
        if sayori_confess:
            mc "I'm with Sayori..."
        else:
            mc "Since when?"
        show yuri 1v
        "Yuri is looking visibly upset."
        "But Monika really isn't my girlfriend."
        "So I have no idea what she's talking about."
        y 2w "Can we just put these decorations up?"
        y "I'd rather do it quietly..."
        y "If you don't mind."
        mc "..."
        "I do what Yuri says and keep quiet while putting the rest of the candles around the room."
        "She takes the lanterns and puts them up in the room so that it illuminates all the desks."
        "I try my best to create a good atmosphere with the candles but it's hard to focus after what she just said."
    scene bg club_day
    with wipeleft_scene
    "I go back to my desk."
    "Well, that didn't go well at all."
    "Apparently, I'm Monika's boyfriend now."
    "I don't think that's true, because if anything..."
    "{i}You{/i} should be her boyfriend."
    "Just how much has happened ever since the weekend?"
    "I should talk to Monika about this."
    "She looks like she's done helping Sayori."
    show monika 1a at t11
    m "Hi [player]~"
    m "Is something wrong?"
    mc "What's happened?"
    m 1c "Huh? What do you mean?"
    mc "When did {i}we{/i} become...you know...?"
    m 1d "Become...?"
    mc "A couple."
    m "Um..."
    m 1l "Ahaha, I'm sorry..."
    m "I don't intend to offend you or anything..."
    m 1m "But where did you get that notion from?"
    m 1e "Besides, I've got someone special in my life already."
    "Monika looks directly at me as she said that but it feels as if she's looking straight past me."
    "I can only guess she's talking about {i}you{/i}."
    mc "Is it the other me?"
    m 1i "Other you...?"
    mc "Monika, at this point I think I have some idea of what's going on."
    mc "I still don't fully get it either."
    mc "But there's someone watching us, right now, isn't there?"
    mc "He must be the one you've been talking to."
    mc "Which makes sense, now that I think about it."
    play music t10 fadeout 2.0
    m 1h "..."
    m 1h "This is..."
    m 1f "An unexpected consequence."
    m "You weren't suppose to be able to put the pieces together..."
    m "You're breaking the game too."
    m "I guess the mod made you more aware, huh?"
    m 1g "I don't know what will happen now."
    m "Maybe we'll both forget about everything, now that Sayori is president."
    m 1e "I don't want to forget..."
    m "Not after coming this far...{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    m "Not after coming this far...{fast}"
    window auto
    m 1h "..."
    m "But it's not over yet."
    m "Either it's a big coincidence that the game is breaking now..."
    m "Or we're on the right track."
    m 1q "[player]..."
    m "Maybe if you forget everything that's happened, the game will stabilize."
    m "It's possible you'll keep your memories of Sayori and [ch4_name]."
    mc "Monika..."
    mc "My memories are important to me, too."
    mc "I don't think I'd be the same without them."
    mc "Besides, how do we know that getting rid of my memories will fix everything?"
    "She takes a long, deep sigh."
    m 1q "We don't."
    m 1h "But let me ask you this, [player]."
    m "Do you care more about yourself than you do about [ch4_name]?"
    "She poses a really difficult question..."
    "I care a lot for [ch4_name] but still..."
    m 1h "It's okay to be selfish here, [player]."
    m 1e "I was."
    m 1f "But you should know that if my memories get deleted..."
    m "We won't be able to solve Yuri and Natsuki's issues."
    m "So isn't it worth the risk, knowing she'll have a chance at a happy life..."
    m 1e "...just like me?"
    mc "..."
    show sayori 1f zorder 3 at f21
    show monika zorder 2 at t22
    s "Um..."
    show sayori zorder 2 at t21
    show monika 1f zorder 3 at f22
    m "Sayori, you heard that conversation, didn't you?"
    show sayori zorder 3 at f21
    show monika zorder 2 at t22
    s "Yeah..."
    s 1h "It wasn't on purpose or anything!"
    s "But it was like an echo in my head."
    s 1b "Like I can hear everything that's happening."
    s "But it's nothing like before."
    s "I can turn this new 'voice' off..."
    s "Anyway...that isn't the issue here, is it?"
    s 1g "I can tell the world is falling apart."
    s "I think it's because too many people are breaking the game."
    s 1f "Why does this have to happen...?"
    "Sayori begins to tear up."
    s 1u "I just wanted everyone to be happy..."
    show sayori zorder 2 at t21
    "Seeing Sayori like this feels terrible."
    "She just wants the best for everyone and I can't do much to help her..."
    "Except..."
    "Would losing my memories really change me that much?"
    "Just how much will I forget?"
    "I have to do it, don't I?"
    "It's the only way we'll all get our happy endings."
    mc "Sayori, can you delete my memories?"
    mc "So I forget about this other me and whatever Monika is talking..."
    mc "Will that fix the world?"
    show sayori 2o zorder 3 at f21
    s 1k "I think so..."
    s "It's our best guess, isn't it?"
    s 1j "But why are you doing this?"
    s "I've known you our entire life and it's not like you..."
    show sayori zorder 2 at t21
    mc "I guess I'm not the only one that's changed, right?"
    mc "Even if I'm not sure how Monika changed, or who she was before."
    mc "Was Monika a bad person? I'll never know..."
    mc "But this other me must have changed her for the better."
    show monika 1o
    show sayori 1i
    "Monika looks away and Sayori nods sadly."
    mc "He's the one that's been influencing my decisions, isn't he?{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    mc "He's the one that's been influencing my decisions, isn't he?{fast}"
    window auto
    mc "..."
    mc "Well, you've done good so far."
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() != player.lower():
            mc "[currentuser]..."
            mc "That's your real name, right?"
            mc "At least, that's what I remember Monika and Sayori calling me before."
    mc "Take care of everyone for me."
    mc "I trust the three of you can help Natsuki and Yuri."
    show sayori 1u zorder 3 at f21
    s "[player]..."
    s "I'm so sorry."
    s "I don't want to do this, if there was another way--"
    show sayori zorder 2 at t21
    mc "Hey, it's okay."
    mc "It's my decision after all, you dummy."
    show monika 1p zorder 3 at f22
    m "You won't forget everything."
    m "Only the memories about the unscripted events and the other you..."
    m 1n "I'll do all I can to help them, [player]."
    m 1e "It's a promise."
    "I smile at Monika."
    "She really is passionate about her friends, isn't she?"
    "Is what why she's so special to you?"
    "Ah, but I can only take wild guesses..."
    "If you can hear this..."
    "Goodbye."
    show monika zorder 2 at t22
    mc "Sayori..."
    mc "I'm ready."
    show sayori 1u zorder 3 at f21
    s "[player]...everyone except Monika and I are going to forget almost everything."
    s "It's gonna be like that 'new beginning' Monika said."
    s "I'm counting on {i}you{/i} to help make everyone happy for me."
    s "So if that person is listening, I hope you know what you're in for..."
    s "I'll do everything I can to make everybody happy too..."
    s "I promise!"
    "Sayori exhales."
    s "Okay, [player]..."
    s "Here goes..."
    stop music
    scene black
    with close_eyes
    $ pause(4.0)
    play music t2
    scene bg club_day
    show monika 1n at face
    with open_eyes
    $ _history_list = []
    mc "Uwaa--!"
    "I open my eyes to find Monika's face filling my vision."
    "I nearly fall out of my chair."
    show monika 1g zorder 2 at t11
    m "Sorry, [player]!"
    m 1l "But you dozed off!"
    m "You're going to miss out on the first part of the festival!"
    if sayori_confess:
        m "Didn't you and Sayori have plans today?"
    else:
        m "Didn't you intend to spend some time with [ch4_name]?"
    mc "Ugh..."
    "I put my hand up to my head."
    "There's no trace of any damage but it really hurts."
    mc "How long do we have left?"
    m 1e "Well...at this rate you'd probably only have time to do one thing."
    m "Everyone has to be back here in time to do our poetry performances."
    m "So you'd probably want to hurry if you wanted to catch one of the others."
    m "I think Natsuki is over at the food stalls and Yuri is at the arts and crafts area."
    mc "Where's Sayori?"
    m "She's talking to potential members of the Literature Club, they're just outside."
    menu:
        m "So, where are you going?"
        "Natsuki.":
            call natsuki_exclusive_3
        "Yuri.":
            call yuri_exclusive_3
        "Monika.":
            call monika_exclusive_3
            jump ch5_mainc_monika_end
        "Sayori.":
            call sayori_exclusive_3
    call ch5_mainc_end
    return

label ch5_mainc_end:
    play music t3 fadeout 1
    scene bg club_day
    show natsuki 1k zorder 2 at i31
    show yuri 1h zorder 2 at i32
    show sayori 1c zorder 2 at i33
    with wipeleft_scene
    "Sayori beckons all of the people inside."
    "One by one they enter and take a seat each."
    "The amount of people inside is around half of what you'd see in a normal classroom."
    show sayori 1l zorder 3 at f33
    s "Um..."
    s "What do I do?"
    "Sayori frantically looks towards the three of us."
    show sayori zorder 2 at t33
    mc "Well, maybe giving out the cupcakes is a good idea?"
    show sayori zorder 3 at f33
    s "R-Right!"
    s "Natsuki?"
    show sayori zorder 2 at t33
    show natsuki 1z zorder 3 at f31
    n "I'm on it!"
    show natsuki at thide
    hide natsuki
    show yuri zorder 2 at t21
    show sayori zorder 2 at t22
    "Natsuki leaves and gets the cupcakes from the cupboard."
    "She notices that one of the trays has the foil lifted up."
    "She looks towards us and smiles."
    "I can only take a wild guess and say Sayori probably {i}did{/i} take one."
    "Natsuki starts handing out a cupcake to each person."
    show yuri 1q zorder 3 at f21
    y "Um..."
    y "Shouldn't we be greeting them?"
    show yuri zorder 2 at t21
    show sayori 1m zorder 3 at f22
    s "You're right!"
    s 1f "Oh...but Monika isn't here yet..."
    s "It wouldn't be fair if we did that without her."
    show yuri 3v zorder 3 at f21
    show sayori zorder 2 at t22
    y "You're correct..."
    y "I apologize."
    show yuri zorder 2 at t21
    show sayori 1d zorder 3 at f22
    s "No need!"
    s "It was a good suggestion."
    s "If anyone Monika is the one who--"
    show monika 1g zorder 2 at l31
    show yuri zorder 2 at t32
    show sayori zorder 3 at f33
    "Monika suddenly opens the door."
    "It appears she has something with her."
    show monika zorder 3 at f31
    show yuri 1i zorder 2 at t32
    show sayori zorder 2 at t33
    m "Sorry! I'm super sorry!"
    m "How late was I?"
    show monika zorder 2 at t31
    show sayori 4a zorder 3 at f33
    s "Actually, you made it in time!"
    s "We were just about to do the greetings."
    show monika zorder 3 at f31
    show sayori zorder 2 at t33
    m 1e "Well, that's a relief."
    m "I managed to find a keyboard at the library."
    m 3a "I should really go to that place more often, there's so much stuff there!"
    show monika zorder 2 at t31
    "As she says that, Natsuki finishes handing out cupcakes."
    "She puts the rest in the cupboard and joins the rest of us."
    show natsuki 1e zorder 2 at f41
    show monika zorder 2 at t42
    show yuri zorder 2 at t43
    show sayori zorder 2 at t44
    "She looks at Sayori and rolls her eyes."
    n "I knew you were going to take one."
    n "That's what I get for leaving the clubroom."
    show natsuki zorder 2 at t41
    show sayori 4l zorder 3 at f44
    s "Ehehe..."
    s "Well, we shouldn't talk about that now."
    s "We should greet the people who came here."
    s "Ready? On three we say \"Welcome to the Literature Club\"."
    s "One...two..."
    s "Three!"
    show natsuki 1l zorder 3 at f41
    show monika 1b zorder 3 at f42
    show yuri 1b zorder 3 at f43
    show sayori 1q zorder 3 at f44
    e "Welcome to the Literature Club!"
    show natsuki zorder 2 at t41
    show monika zorder 2 at t42
    show yuri zorder 2 at t43
    s "M-My name is Sayori as most of you may know from before."
    s 4a "And I'm president of the Literature Club!"
    s "I hope you're all comfortable, because we have some pretty awesome things planned!"
    s "If you look at your desk, there is a pamphlet which contains what we're gonna be doing."
    "Everyone simultaneously picks up the pamphlet in front of them and opens it."
    "Sayori turns towards us."
    s 1l "Guys, I'm a little nervous..."
    s "I thought it'd be easier since we practiced last week but..."
    show sayori zorder 2 at t44
    "Sayori does look a little different from her usual cheery and outgoing self."
    "Maybe it's some last minute anxiety?"
    mc "If it makes you feel better, I can go first."
    show monika 4l zorder 3 at f42
    m "Um...no offense intended [player]..."
    m "But we should start with a poem that would get people to see what we're all about."
    m 4e "We don't want them to leave before they get to see all of our performances."
    show monika zorder 2 at t42
    mc "Ah..."
    mc "Well, I suppose you're right."
    show monika 4a zorder 3 at f42
    m "If Sayori doesn't want to go first, I'm more than happy to."
    m "I have the keyboard I intend to use here ready as well."
    show monika zorder 2 at t42
    show natsuki 1c zorder 3 at f41
    n "You're doing your performance with a keyboard?"
    n 5c "Way to show up on all of us..."
    show monika 4l zorder 3 at f42
    show natsuki zorder 2 at t41
    m "Ah, sorry!"
    m "I didn't mean to grandstand or anything..."
    m 4e "There are certain things that happened to me while I was writing this poem."
    m "So I put a lot of effort into it and I just know it will sound better in song form."
    show monika zorder 2 at t42
    show sayori 4d zorder 3 at f44
    s "Thanks Monika."
    s "I don't know why I'm so nervous..."
    show monika 1e zorder 3 at f42
    show sayori zorder 2 at t44
    m "It's okay Sayori."
    m 3e "That's what friends are for."
    mc "Is this going to have that melody you were humming last week?"
    m "Well, you'll find out soon~"
    "Monika winks at me and shows a friendly smile."
    show monika zorder 2 at t42
    label ch5_mainc_end_shared:
    "She takes her place at the front of the club and places down the keyboard."
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    show sayori at thide
    hide sayori
    show monika 1e zorder 3 at t11
    m "Hi, everyone!"
    m 4a "My name is Monika, I'm sure some of you know who I am."
    m "In case you don't, I was in the debate club."
    m "But recently, I quit to join the Literature Club!"
    m 4b "I'm going to be performing my poem, you'll find it at the end of your pamphlet."
    m "I'll be doing it in song form...so yeah..."
    m "I hope you all like it~"
    stop music fadeout 2.0
    "The whole club falls silent, either out of respect for Monika or for eagerness of the performance."
    show monika 1j
    play music "<to 9.5>bgm/credits.ogg" noloop
    $ pause(9.5)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play music g1
    $ pause(0.5)
    hide screen tear
    $ _history_list = []
    window hide(None)
    window auto
    # Setup Variables for Poem Game
    $ newpoemwinner = ['sayori', 'sayori', 'sayori']
    $ chapter = 5
    $ m_show = True
    jump ch5_good_redirect

label ch5_mainc_monika_end:
    play music t3 fadeout 1
    scene bg club_day
    show monika 1g zorder 2 at i11
    with wipeleft_scene
    m "Sorry! We're super sorry!"
    m "We didn't expect it to take that long to find a keyboard..."
    m 2f "But the library was bigger than we thought..."
    show sayori 4a zorder 3 at f21
    show monika zorder 2 at t22
    s "Actually, you two made it just in time!"
    show sayori zorder 3 at f21
    s "We were just about to do the greetings."
    show sayori zorder 2 at t21
    show monika 1e zorder 3 at f22
    m "Well, that's a relief."
    show monika zorder 2 at t22
    mc "Yeah, sorry if we worried you Sayori."
    show yuri 1o zorder 2 at f31
    show sayori zorder 2 at t32
    show monika zorder 2 at t33
    "Yuri approaches us timidly."
    show yuri zorder 3 at f31
    y "Um...people look like they're about to leave..."
    y "We should..."
    y "...do something..."
    y "Everyone's here and--"
    show natsuki 1i zorder 2 at f41
    show yuri zorder 2 at t42
    show sayori zorder 2 at t43
    show monika zorder 2 at t44
    n "Aren't you forgetting me?!"
    n "Jeez, I go to hand out some cupcakes and you're already talking behind my back."
    show natsuki zorder 2 at t41
    show yuri zorder 3 at f42
    y 3p "S-Sorry Natsuki, I just didn't want the people here to start leaving..."
    y "And I just saw you put the tray in the cupboard..."
    y "So I assumed you were done..."
    y 3q "I just meant that since everyone's here we can..."
    show natsuki 1m zorder 3 at f41
    show yuri zorder 2 at t42
    n "Oh..."
    n 1n "Sorry, I shouldn't have got so upset..."
    n "Today's just been really...weird."
    n "I don't know what came over me."
    show natsuki zorder 2 at t41
    show yuri 1a zorder 3 at f42
    y "It's okay..."
    y "I feel the same about today."
    y 3s "So I can understand if we're all feeling on edge.."
    show yuri zorder 2 at t42
    show sayori 1l zorder 3 at f43
    s "Um...guys."
    s "We should probably do the greeting before people start leaving."
    show natsuki zorder 3 at f41
    show yuri zorder 3 at f42
    show sayori zorder 2 at t43
    ny "Right..."
    show natsuki zorder 2 at t41
    show yuri zorder 2 at t42
    show sayori zorder 3 at f43
    s "Ready? On three we say \"Welcome to the Literature Club\"."
    s "One...two..."
    s "Three!"
    show natsuki 1l zorder 3 at f41
    show monika 1b zorder 3 at f44
    show yuri 1b zorder 3 at f42
    show sayori 1q zorder 3 at f43
    e "Welcome to the Literature Club!"
    show natsuki zorder 2 at t41
    show monika zorder 2 at t44
    show yuri zorder 2 at t42
    s "M-My name is Sayori as most of you may know from before."
    s 4a "And I'm president of the Literature Club!"
    s "I hope you're all comfortable, because we have some pretty awesome things planned!"
    s "If you look at your desk, there is a pamphlet which contains what we're gonna be doing."
    "Everyone simultaneously picks up the pamphlet in front of them and opens it."
    "Sayori turns towards us."
    s 1l "Guys, I'm a little nervous..."
    s "I thought it'd be easier since we practiced last week but..."
    show sayori zorder 2 at t43
    "I thought Sayori would be more confident about this."
    "You'd think she'd be a bit more comfortable with these people after talking to them for so long."
    "But it's up to me rescue this situation."
    mc "If it makes you feel better, I can go first."
    show monika 4l zorder 3 at f44
    m "Um...no offense intended [player]..."
    m "But we should start with a poem that would get people to see what we're all about."
    m 4e "We don't want them to leave before they get to see all of our performances."
    show monika zorder 2 at t44
    mc "Ah..."
    mc "Well, I suppose you're right."
    show monika 4a zorder 3 at f44
    m "If Sayori doesn't want to go first, I'm more than happy to."
    m "I have the keyboard we got from the library right here anyway."
    show monika zorder 2 at t44
    show natsuki 1c zorder 3 at f41
    n "You're doing your performance with a keyboard?"
    n 5c "Way to show up on all of us..."
    show monika 4l zorder 3 at f44
    show natsuki zorder 2 at t41
    m "Ah, sorry!"
    m "I didn't mean to grandstand or anything..."
    m 4e "There are certain things that happened to me while I was writing this poem."
    m "So I put a lot of effort into it and I just know it will sound better in song form."
    show monika zorder 2 at t44
    show sayori 4d zorder 3 at f43
    s "Thanks Monika."
    s "I don't know why I'm so nervous..."
    show monika 1e zorder 3 at f44
    show sayori zorder 2 at t43
    m "Ahaha, it's okay Sayori."
    m 3e "This is precisely what a vice president is for..."
    m "To get you out of situations just like this."
    mc "Is this going to have that melody you were humming last week?"
    m "Well, you'll find out soon~"
    "Monika winks at me and shows a friendly smile."
    show monika zorder 2 at t44
    jump ch5_mainc_end_shared
