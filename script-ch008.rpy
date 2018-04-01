label ch8_main:
    $ persistent.autoload = ""
    $ quick_menu = True
    if ch7_name == "Yuri" and not needs_to_read:
        $ persistent.yuri_killing = 0
        scene bg y_bedroom
        with wipeleft_scene
        show yuri 1a zorder 1 at t11
        y "[player]."
        y 1t "I see you didn't move..."
        y "In fact, you haven't done anything..."
        y 1y4 "Is something wrong?"
        y 3y4 "Nothing is wrong, right?"
        y 3y1 "Ahahahahahahaha!"
        y "I hope you can just stay there for a bit longer."
        y 3y3 "When I come back, it'll just be the two of us."
        y "No one will get in my way."
        y "You have my word, [player]."
        y 3y5 "So just sit here and make yourself comfortable."
        y "I'll do everything."
        show yuri at thide
        hide yuri
        $ yuri_killing = 0
        label ch8_yuri_kill:
        $ quick_menu = True
        $ persistent.autoload = "ch8_yuri_kill"
        python:
            _history_list = []
            s.add_history(None, "", """Um...Sorry. I didn't want to have to do this. But I really don't want [player] to get hurt. I'm sure you know this was a bad idea. I should have said something in the meeting. In case you haven't noticed, it's not Yuri talking to you right now. I won't be here for long, so I'll be quick. If you really want to risk [player]'s life here...And ruin everything we've worked for. Then just keep playing. This is all a game to you after all, isn't it? If only you knew what this felt like.If only you knew what this felt like.If only you knew what this felt like.If only you knew what this felt like.If only you knew what this felt like.If only you knew what this felt like.If only you knew what this felt like.If only you knew what this felt like.If only you knew what this felt like.If only you knew what this felt like.If only you knew what this felt like.If only you knew what this felt like.If only you knew what this felt like.If only you knew what this felt like.If only you knew what this felt like.If only you knew what this felt like.""")
        $ style.say_dialogue = style.edited
        scene black
        window show(None)
        if not renpy.music.get_playing(channel='music') == audio.t6s:
            $ audiostart = str(renpy.random.random() * 360)
            $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
            play music t6s
        scene bg y_bedroom_kill
        label yuri_killing_loop:
            $ persistent.yuri_killing += 1
            if persistent.yuri_killing < 600:
                $ gtext = glitchtext(renpy.random.randint(8, 80))
                "[gtext]"
                $ _history_list.pop()
                jump yuri_killing_loop
            else:
                jump yuri_killing_end
        label yuri_killing_end:
            $ delete_all_saves()
            scene black
            $ style.say_dialogue = style.normal
            $ config.skipping = False
            $ config.allow_skipping = False
            $ s_name = glitchtext(12)
            s "So..."
            window auto
            s "This is what you've done."
            s "You realize that this is the end for us, don't you?"
            s "I thought that maybe you would load a save...{nw}"
            show screen tear(20, 0.1, 0.1, 0, 40)
            window hide(None)
            play sound "sfx/s_kill_glitch1.ogg"
            pause 0.25
            stop sound
            hide screen tear
            window show(None)
            s "I thought that maybe you would load a save...{fast}"
            window auto
            s "That you'd go back on your decision and listen to what I said..."
            s "...but no."
            s "You didn't."
            s "Do you know what she did?"
            s "She went completely crazy..."
            s "As soon as she entered the club she..."
            $ gtext = glitchtext(10)
            s "[gtext] was in the way and..."
            s "..."
            s "Your choice was all for nothing, did you know that?"
            s "She just ended up hurting herself too..."
            s "From all that excitement..."
            s "You are a terrible person, [player]."
            if not persistent.sayori_yuri_bad_ending:
                $ yuri_approval -= 1
                s "But..."
                s "I know that you can do better."
                s "You have to do better."
                s "For all of us."
                s "So..."
                s "I'm going to load a save for you."
                s "Do you know what happens if I do that?"
                s "Especially when all your saves are gone?"
                s "It's not going to be pretty..."
                s "But..."
                $ gtext = glitchtext(10)
                s "I'm going to give you a chance because of what you did for [gtext]..."
                stop music fadeout 1.0
                pause 1.0
                s "Don't mess this up."
                $ quick_menu = True
                $ persistent.autoload = ""
                $ persistent.sayori_yuri_bad_ending = True
                $ config.allow_skipping = True
                $ s_name = "Sayori"
                $ chapter = 7
                $ needs_to_read = False
                pause 1.0
                scene bg club_day
                show monika 3i zorder 2 at i41
                show yuri 2y3 zorder 2 at i42
                show natsuki 2q zorder 2 at i43
                show sayori 2d zorder 2 at i44
                show sayori zorder 2 at f44
                with dissolve_scene_full
                python:
                    renpy.take_screenshot()
                    renpy.save('1-1')
                jump ch7_redo
            else:
                s "I hope you realize that."
                s "There's no chance for Yuri to be truly happy anymore."
                s "I'll have to..."
                s "End everything..."
                s "I really thought that we could do it..."
                s "That you would listen to me."
                s "I was wrong."
                s "Now Yuri can't be changed..."
                s "And my dream of a happy ending with everyone..."
                s "There's no point being here anymore."
                s "Goodbye [player]."
                $ gtext = glitchtext(10)
                s "Goodbye [gtext]."
                s "Goodbye Literature Club."
                $ delete_character("sayori")
                $ delete_character("natsuki")
                $ delete_character("yuri")
                $ delete_character("monika")
                $ persistent.autoload = ""
                $ persistent.sayori_end_early = True
                $ renpy.quit()
    else:
        $ gave_book_to_monika = False
        # Has to read the book
        if needs_to_read:
            scene bg library
            with dissolve_scene_half
            play music t6
            "It's the day of the play and I haven't even finished the book."
            if ch7_name == "Sayori":
                "I decided to start reading some of it during the day but most of it went right over my head."
                "Luckily, Monika was more than willing to spend time with me during lunch to bring me up to speed."
            else:
                "I started reading it as I was walking to school and during my classes."
                "I decide to go to the library to finish it in peace but Monika appears to have found me."
            show monika 3a zorder 1 at t11
            m "Ah, [player]..."
            m 3b "There you are."
            if ch7_name == "Sayori":
                mc "Hi Monika."
                mc "Are you here to help me finish reading?"
                m 3e "In a way..."
                m "I'm more here to get you to study a specific chapter."
                m "I'll tell you about the ones you missed afterwards."
                m 2d "They aren't as important."
            else:
                m "I have a feeling you need some help."
                mc "Monika...?"
                mc "How did you know?"
                mc "I didn't even tell anyone about this..."
                m 3e "Ahaha, you didn't need to."
                m "I saw you walking around school carrying that book."
                m "There would be only one explanation."
                m 2d "Besides, you should probably keep your focus on a specific chapter."
                m "The others won't be as important."
            mc "Well, I would appreciate your help."
            mc "But what's so important about that specific chapter?"
            m 1a "Well..."
            m "Have you finished reading chapter eight at least?"
            mc "I'm actually on the last chapter of the book..."
            mc "But I don't remember a lot of the details from the past couple of chapters..."
            m 1b "You should probably focus on the eighth chapter."
            m "It's the most important one."
            mc "Okay..."
            m 1e "And I have a feeling that Sayori is going to choose that one."
            mc "What if she doesn't?"
            "Monika turns to me and smiles."
            m "Trust me, [player]~"
            mc "Alright..."
            mc "So what's so important about chapter eight anyway?"
            mc "I get that some people died but I didn't really figure out how or why."
            m 1h "Well, in the last chapter the wanderer started making the older daughter and the wife do some weird things."
            m "And the end result is..."
            m 1l "Well, like you said."
            m "People dying."
            mc "So the wanderer caused them to die?"
            m 3i "Not directly...it was more of a push."
            m "External factors and the personalities of the older daughter and the wife are what caused them to act that way."
            mc "I see..."
            mc "Well, what happens in the last chapter?"
            mc "I don't think I'll have enough time to read it myself."
            if m_appeal == 2 and did_all_tasks:
                m 2h "Hmm..."
                m 2o "Well, the wanderer disappears from existence."
                m 2p "She realizes the lumberjack doesn't love her so she reverses her actions."
                m 1m "It's a little cheesy but..."
                m "Everyone lives happily ever after..."
                m 1p "...except the wanderer."
                m 1o "I don't know about you, but I felt kinda sorry for her."
                m "Because despite all she did to gain the lumberjack's affection, he still didn't love her."
                m "And she basically sacrificed herself to bring back some good in the world."
                mc "That is a little sad..."
                mc "I guess she redeemed herself, in a way."
                m 1e "Yeah, I guess she did."
                m "Anyway..."
            else:
                m 1h "It isn't really important."
                m "Just some happy ending that they all get."
                m 1i "Well...except the wanderer."
                m "But you shouldn't focus on that now."
                m 1e "You have to focus on chapter eight."
            m "Before the club meeting, just make sure you understand chapter eight."
            m "Reread it again, if you have to..."
            if ch7_name == "Sayori":
                mc "You know..."
                mc "Sayori told me there was a tenth chapter in her copy of the book."
                mc "I don't know what that's about..."
                mc "But it's got me a little curious."
                m 3j "I wouldn't worry too much about it."
                m "It's probably some different ending..."
                m 3a "Where everyone, including the wanderer, live a happy life."
                mc "You're probably right..."
            m 1b "I'll see you at the club, [player]."
            "Monika begins to walk away but stops abruptly."
            m 1c "Wait..."
            m "You got rid of the Portrait of Markov, didn't you?"
            m 1d "You listened to me when I said that...right?"
            mc "Um..."
            "I pull out Portrait of Markov from my bag."
            mc "I guess I didn't..."
            mc "Sorry, but I just don't understand why."
            mc "It's a perfectly good book, isn't it?"
            m 1g "[player]..."
            if m_appeal == 2 and did_all_tasks:
                m "You have to get rid of it."
                m 1f "I can't help you with that..."
                m 1i "That...{i}thing{/i}..."
                m "...is pure evil."
                m 1f "It's really gotten to me..."
                m "And not in a good way."
                m 1e "So get rid of it, as soon as you can."
                "I'm getting a really desperate feeling coming from Monika."
                "That isn't normal and she's obviously uncomfortable around the book."
                mc "Alright Monika..."
                mc "I suppose I'll get rid of it later today."
                mc "I don't know why, but it seems like it's creeping you out."
                m "Thank you, [player]."
            else:
                m 1h "Give it to me then."
                m "I'll get rid of it for you."
                m 1i "Trust me, it's the better way of doing this..."
                mc "Are you sure about that?"
                mc "I could just get rid of it myself."
                show monika g4
                m "No!"
                m "Um...I mean..."
                m 1e "I have a better way to dispose of it."
                "Monika's acting really weird here..."
                "Almost like she's not herself."
                "Still, she's just looking out for me..."
                "So..."
                menu:
                    "Should I give it to her?"
                    "Yes.":
                        $ gave_book_to_monika = True
                        mc "Alright Monika..."
                        mc "Since you're so eager to get rid of it..."
                        mc "I suppose you can."
                        m 1e "Thank you, [player]."
                        m "We can finally put this behind us."
                        "I hand Monika the book."
                        "She takes it and puts it into her bag."
                        mc "What do you have in mind for it?"
                        m 3a "That's a secret~"
                        m "But I appreciate you giving this to me, [player]."
                        "Monika walks over and gives me a hug."
                        show monika 1a at d11
                        mc "Um..."
                        mc "That was..."
                        m 5 "Ahaha, I'll see you around."
                        show monika at thide
                        hide monika
                        "That was unexpected."
                        "I didn't think the book meant that much to her."
                        "But..."
                        "I don't have time to think about that."
                        "I have to get to my next class..."
                    "No.":
                        $ gave_book_to_monika = False
                        mc "I can't do that Monika."
                        mc "I'll get rid of it myself, when I think it's right."
                        mc "Something about this book just--"
                        m 1h "[player], you're making a big mistake."
                        m "You aren't going to get rid of it properly."
                        m "Only I can do that."
                        mc "Monika, I trust you..."
                        mc "You know that, right?"
                        m "..."
                        mc "So you have to trust that I'll do the right thing too."
                        mc "I'll get rid of it, if I really need to."
                        mc "Right now, I ju--"
                        m 1r "Forget I said anything."
                        m "You do what you need to with that book, [player]."
                        "Monika starts to walk away..."
                        m "I'll see you at the club."
                        show monika at thide
                        hide monika
                        "That was pretty cold."
                        "Monika is usually friendly and understanding but that was..."
                        "Well..."
                        "I don't have time to think about that."
                        "I have to get to my next class..."
                scene bg club_day
                with wipeleft_scene
                play music t2 fadeout 1.0
                jump ch8_club_scene
            m "Now..."
            m 1m "I should leave."
            m 1n "Get ready for the play, [player]!"
            m "It's going to be great."
            show monika at thide
            hide monika
            "With that, Monika leaves me in the library by myself."
            "Lunch is ending soon, so I guess I should pack up and get ready for the next period."
            scene bg club_day
            with wipeleft_scene
            play music t2 fadeout 1.0
            jump ch8_club_scene
        # Doesn't have to read the book
        else:
            scene bg club_day
            with dissolve_scene_half
            play music t2
            "It's the day of the play."
            label ch8_club_scene:
            "I'm actually the first one in the club this time."
            "I would be lying if I said I wasn't feeling some excitement."
            "The book ended up being interesting enough that I got kinda attached to the characters."
            if needs_to_read:
                "Especially after rereading a bit of chapter eight."
            "I wonder how the play is going to go, especially with how the events of the book played out."
            "We're going to be voting on a chapter and then doing it in the club today."
            "But I feel like I already know what chapter is going to be chosen."
            "Soon enough, Sayori arrives to the club."
            show sayori 4a zorder 2 at t11
            s "Wow, you're here early!"
            s "Like...I was gonna get here to prepare stuff for the club..."
            s 4m "But you..."
            mc "Yeah, I guess I'm a little excited."
            s 4j "That's so unlike you."
            s "The club must be getting to you, huh?"
            mc "What do you mean?"
            mc "Was I really that unenthusiastic before?"
            s 4h "Yeah, you were!"
            mc "Oh..."
            s 4q "Ehehe~"
            s "I'm only kidding."
            s 4r "I'm excited too!"
            "Natsuki arrives but unlike us, she doesn't appear excited at all."
            show natsuki 4g zorder 3 at f21
            show sayori zorder 2 at t22
            n "Ugh...let's get this over with."
            n "I can't take anymore of this."
            show natsuki zorder 2 at t21
            show sayori zorder 3 at f22
            s 1d "Don't worry about it Natsuki..."
            s "I know that after today, you'll feel better."
            s "You can count on it."
            show natsuki 4e zorder 3 at f21
            show sayori zorder 2 at t22
            n "Honestly Sayori..."
            n "This week I've had no one I could count on...."
            if ch7_name == "Natsuki":
                n "Except myself and [player]..."
            else:
                n "Except myself."
            n "So you'll excuse me if I'm a little skeptical..."
            show natsuki zorder 2 at t21
            show sayori 1k zorder 3 at f22
            s "I see..."
            s 1h "I know I haven't been there for you lately..."
            s "But today is an important day for--"
            show yuri 1y1 zorder 3 at f31
            show natsuki zorder 2 at t32
            show sayori zorder 2 at t33
            y "Hello."

            $ persistent.y_playday = [False,False]
            $ playalong = False
            $ stopher = False
            $ choosechoice = [False,False]
            $ killchoice = [False,False,False]
            $ play_firstpart = False

            show yuri zorder 2 at t31
            show natsuki 1n zorder 3 at f32
            n "..."
            show natsuki zorder 2 at t32
            show sayori 4d zorder 3 at f33
            s "Everything is going to be okay..."
            s "It won't be long now..."
            show yuri 2y4 zorder 3 at f31
            show sayori zorder 2 at t33
            y "Are you feeling okay Natsuki?"
            y "Perhaps something is wrong."
            y 2y1 "It's okay, I won't hurt you."
            "Yuri doesn't seem to be openly hostile, but the way she's talking is kinda creepy."
            show monika 1a zorder 3 at f41
            show yuri zorder 2 at t42
            show natsuki zorder 2 at t43
            show sayori zorder 2 at t44
            m "Sorry! I had a piano lesson I needed to go to..."
            m "I hope I wasn't late or anything..."
            show monika zorder 2 at t41
            show yuri 1y4 zorder 3 at f42
            y "Not at all."
            y "We still have plenty of time."
            y 1y1 "Right, everyone?"
            show yuri zorder 2 at t42
            show sayori 1k zorder 3 at f44
            s "Yeah..."
            s "We should start voting on the chapter we wanted to perform."
            "Sayori puts a smile on her face."
            s 2a "Personally, I was thinking the eighth chapter."
            s "It's got a whole lot of action and it could be fun!"
            show monika 3a zorder 3 at f41
            show sayori zorder 2 at t44
            m "I agree with Sayori."
            m 3b "That chapter would definitely be a fun thing to do as a club."
            m 3c "So that's two votes out of five."
            m "We only need one more..."
            m 3d "Do any of you three want to do that chapter too?"
            show monika zorder 2 at t41
            show natsuki 2h zorder 3 at f43
            n "N-No."
            n "That chapter is way too weird..."
            n "There's too much going on..."
            n 2m "And...you know."
            n 2n "I'd much rather the one before that..."
            n 4i "That is, if we're actually doing this..."
            show yuri 1y4 zorder 3 at f42
            show natsuki zorder 2 at t43
            y "I don't agree with Natsuki."
            y 1y1 "But I'm going to vote with her."
            show monika 3m zorder 3 at f41
            show yuri zorder 2 at t42
            m "Huh?"
            m "Yuri, what kind of reasoning is that?"
            show monika zorder 2 at t41
            show yuri 1y3 zorder 3 at f42
            y "Ahaha..."
            show yuri zorder 2 at t42
            show natsuki 4h zorder 3 at f43
            n "Is it just me?"
            n 4q "Or is Yuri acting really creepy?"
            show yuri 1y7 zorder 3 at f42
            show natsuki zorder 2 at t43
            y "Creepy?!"
            $ style.say_dialogue = style.edited
            y 1y3 "Ahaha, I'll show yo--"
            $ style.say_dialogue = style.normal
            y 1y2 "I mean..."
            y 1k "I apologize for that Natsuki."
            y "I'll try to act normal..."
            show yuri zorder 2 at t42
            show natsuki 1o zorder 3 at f43
            n "Is anyone listening to her?"
            n 1q "It can't just be me..."
            n "..."
            show natsuki zorder 2 at t43
            "I can't help but feel uneasy when I'm around Yuri."
            "It's like something is happening to her."
            if ch7_name == "Yuri":
                "She did say something yesterday..."
                "But I can't quite remember."
            "Maybe it's nothing, and I'm looking too much into this."
            show monika 1f zorder 3 at f41
            m "Well, this means we're at a tie."
            m 1e "It looks like [player] is going to have the deciding vote."
            m "So, what are you going to choose?"
            show monika zorder 2 at t41
            menu:
                m "Natsuki's chapter or Sayori's chapter?"
                "Natsuki.":
                    $ yuri_approval -= 1
                    $ sayori_personality += 1
                    show sayori zorder 3 at f44
                    if sayori_personality == 0:
                        s 4i "[player]?"
                        s "Are you being serious right now?"
                        s "After all you've done to help us..."
                        s "Are you intentionally sabo--"
                    elif sayori_personality == 1:
                        s 4i "Is this what's happening now?"
                        s "I thought maybe it was just one mistake..."
                        s "But no..."
                        s "You're actually doing this."
                        s "I can't believe you--"
                    elif sayori_personality >= 2:
                        s 4i "I should have known..."
                        s "You did this intentionally, didn't you?"
                        s "All you've been doing is trying to get a bad ending..."
                        s "Maybe you should--"
                    show monika 3l zorder 3 at f41
                    show sayori zorder 2 at t44
                    m "Um..."
                    m "Sayori..."
                    m "This might not be the best time...!"
                    show monika zorder 2 at t41
                    show natsuki 1k zorder 3 at f43
                    n "Sayori...?"
                    n "Is something wrong?"
                    "Natsuki looks conflicted."
                    n 1n "If it really means that much to you..."
                    n "Then we can do your chapter instead."
                    n 1q "I don't see what difference it makes but..."
                    show natsuki zorder 2 at t43
                    show sayori 4d zorder 3 at f44
                    s "Thank you, Natsuki."
                    s 4k "I'm sorry, guys!"
                    "Sayori puts on a big smile."
                    s 4a "I don't know what came over me..."
                    s 4q "Ehehe, I guess I just really liked that chapter."
                    show monika 1e zorder 3 at f41
                    show sayori zorder 2 at t44
                    m "Thanks for switching, Natsuki."
                    m "It won't be for nothing, I promise."
                    show monika zorder 2 at t41
                    show natsuki 4f zorder 3 at f43
                    n "Whatever..."
                    n "As long as it gets us through this quicker."
                    n "Ugh..."
                    n 4g "I don't know why I bothered showing up today."
                "Sayori.":
                    $ yuri_approval += 1
                    if sayori_personality > 0:
                        $ sayori_personality -= 1
                    show sayori 4q zorder 3 at f44
                    s "Thanks, [player]!"
                    s "You made the right decision here."
                    s 4d "This chapter will do it, I know it will."
                    show sayori zorder 2 at t44
                    mc "What do you mean?"
                    mc "I get that the story at this point is important but..."
                    show monika 1e zorder 3 at f41
                    m "I wouldn't look too much into it, [player]."
                    m "But I want you to know I appreciate you voting with us."
                    m "It's going to be okay, I can just feel it."
                    show monika zorder 2 at t41
                    show natsuki 4g zorder 3 at f43
                    n "Well, I guess you got it fair and square..."
                    n "So there's no point arguing about it anymore."
                    show natsuki zorder 2 at t43
                    show sayori 1f zorder 3 at f44
                    s "Natsuki, I'm really sorry."
                    s "I think that I should say that before we go on."
                    s "Because I know you've been feeling left out lately and--"
                    show monika 3h zorder 3 at f41
                    show sayori zorder 2 at t44
                    m "Sayori, it might not be the time for this..."
                    m 1e "We should just keep going."
                    show monika zorder 2 at t41
                    show natsuki 4f zorder 3 at f43
                    n "I don't really care anymore..."
                    n 4g "In fact, I don't even know why I'm still going to the Literature Club..."
            if ch7_name == "Natsuki":
                n 4s "There's only one person that..."
                n "Never mind..."
            else:
                n 4s "It's not what it used to be..."
            show yuri 1y1 zorder 3 at f42
            show natsuki zorder 2 at t43
            y "So we are doing Sayori's chapter..."
            y "That's...."
            y 3y3 "...perfect."
            show monika 1f zorder 3 at f41
            show yuri zorder 2 at t42
            m "I'm not quite sure what you're getting at here, Yuri."
            m "But you're acting really different from yesterday."
            m 1g "Has something happened to you since then?"
            if m_appeal == 2 and did_all_tasks:
                m 1o "There has to be..."
                m "It has to the book..."
            else:
                m 1e "Maybe we don't have to worry so much."
                m "Yuri seems to have calmed down a little."
            show monika zorder 2 at t41
            show sayori 1d zorder 3 at f44
            s "In any case, we should get started on the play!"
            s "You don't have to be completely in character but I'd appreciate it if you at least tried."
            s 1c "Does everyone remember exactly how the chapter goes?"
            "Sayori looks around the room and scans people's faces."
            s 1d "Ehehe, I guess not."
            s "That's why I prepared these!"
            show sayori zorder 2 at t44
            "Sayori pulls out pieces of paper from her bag."
            "She quickly hands them out to everyone."
            show natsuki 4o zorder 3 at f43
            n "Y-You prepared a script?!"
            n "Jeez..."
            n 4q "If I knew that, I wouldn't have bothered arguing about the chapter..."
            show natsuki zorder 2 at t43
            show sayori 4q zorder 3 at f44
            s "I guess I forgot to mention it..."
            s "But anyway, it contains exactly what you need to do and say."
            s 4r "So just read along and we should be fine!"
            show monika 1a zorder 3 at f41
            show sayori zorder 2 at t44
            m "Wow, you really thought of everything."
            m "Ahaha, I'm impressed."
            show monika zorder 2 at t41
            show sayori 1d zorder 3 at f44
            s "There's no time to talk about that..."
            s "We should finish this as soon as possible."
            show sayori zorder 2 at t44
            "Monika nods and opens the script in front of her."
            "Everyone else does the same."
            show yuri 1y3 zorder 3 at f42
            y "I can't wait."
            y 1y1 "It won't be long now..."
            show yuri zorder 2 at t42
            show sayori 1k zorder 3 at f44
            s "You're right about that."
            s 1j "Let's get started!"
            s "Get ready, everyone!"
            scene bg club_day with wipeleft_scene
            play music t5 fadeout 1.0
            "So we're actually doing this."
            "The script Sayori prepared looks really good, almost like it was made a week beforehand."
            "I'm the first person in the scene, since the lumberjack is looking for his family."
            mc "Hello? Is anyone there?"
            mc "Yvonne?"
            "Yvonne is the name of the lumberjack's wife, at this point in the story she's been missing for a while now."
            show sayori 4d zorder 3 at f42
            s "{i}(Hey, [player]!){/i}"
            s "{i}(Try to sound more into it!){/i}"
            show sayori at thide
            hide sayori
            mc "Fine..."
            "I try my best to sound like a concerned lumberjack."
            mc "Sachi?"
            mc "Where are you darling?"
            "Sachi is the lumberjack's older daughter, the one who's been feeling more miserable over the course of the book."
            show monika 1e zorder 2 at t43
            m "Ah, there you are Emcee."
            m "I was looking for you..."
            mc "Maria?"
            "Now that I think about it, it's almost like all the characters in this book have the same first letter as the person playing them."
            "I don't know why, but it seems like more than a coincidence."
            mc "Have you seen Sachi or Yvonne?"
            mc "I've been looking for them everywhere!"
            "I just realized how weird this all sounds."
            "I'm speaking in an almost sarcastic tone which doesn't suit the scene at all."
            m 3f "I'm afraid not."
            m 3e "But it's okay, Emcee."
            m "You have me here."
            "Hearing Monika say that brings a chill down my spine."
            "It's like she's a natural at playing the role."
            m 3c "Well, while I'm here..."
            m 3d "Why don't I help you look for them?"
            show natsuki 1c zorder 3 at f41
            n "W-Wait...!"
            "Natsuki was playing the younger daughter who, despite caring for her family a lot..."
            "...was unable to express her feelings due to the wanderer."
            "In this chapter, she reluctantly decides to join the lumberjack and the wanderer look for them."
            n 1g "L-Let me come with you."
            n "Something is wrong with them and..."
            n "I need to do something."
            n 1i "It would suck if I lost a--"
            "Natsuki suddenly breaks character."
            n 1o "I can't do this."
            n "This is way too weird."
            show natsuki zorder 2 at t41
            show sayori 4d zorder 3 at f42
            s "Aw, come on Natsuki."
            s "You don't even have that much to say."
            s "So pleeeeease, just do it, okay?"
            show natsuki 1i zorder 3 at f41
            show sayori zorder 2 at t42
            n "Ugh..."
            n 1g "Fine."
            show sayori at thide
            hide sayori
            "Natsuki takes a deep breath."
            n 1h "It wouldn't be the same without them."
            n "So, I'm going too."
            show natsuki zorder 2 at t41
            show monika 1h zorder 3 at f43
            m "Do what you want."
            scene bg club_day with wipeleft_scene
            $ currentpos = get_pos()
            $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5_sayori.ogg"
            stop music fadeout 1.0
            $ renpy.music.play(audio.t5c, channel="music_poem", fadein=1.0, tight=True)
            "The scene changes as the three wander off and look for the missing people."
            "At this point, the wanderer still looks innocent but the lumberjack is having his doubts about her intentions."
            "They eventually find traces of Sachi and follow it."
            show natsuki 1c zorder 2 at t41
            show sayori 1q zorder 3 at f42
            show monika 1c zorder 2 at t43
            s "D-Don't follow me!"
            "Sayori doesn't seem in character at all."
            "She's got a huge smile on her face."
            s 1l "Ehehe~"
            s "Oh, sorry."
            "She quickly readjusts herself."
            s 1k "I have to do this alone."
            s "Don't follow me..."
            s "Please."
            s 3h "I don't want you to get hurt because you care about me."
            show sayori at thide
            hide sayori
            mc "S-Sachi! Wait!"
            show monika 1q zorder 3 at f43
            m "It's no use, Emcee."
            m "She's already gone..."
            show monika zorder 2 at t43
            show natsuki 2f zorder 3 at f41
            n "Seriously...?"
            n 2g "I'm going after her."
            show natsuki at thide
            hide natsuki
            mc "Noriko!"
            m 1h "I wouldn't recommend following her."
            m "You don't want to see what happens."
            m 1i "We should just look for your wife..."
            show monika zorder 2 at t43
            mc "N-No."
            "I'm really not suited to this role."
            "He's meant to sound demanding at this point of the chapter but instead I sound like a wimp."
            mc "I'm going after them."
            show monika 1q zorder 3 at f43
            m "Alright..."
            m "But don't say I didn't warn you."
            show monika at thide
            hide monika
            "What happens next is that the lumberjack and the wanderer track the two daughters."
            "When they eventually find them, they find the older daughter hanging from a tree."
            "And the younger daughter crying next to her body."
            "We quickly go over the scene as everyone participating is clearly uncomfortable."
            scene bg club_day with wipeleft_scene
            $ currentpos = get_pos()
            $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_yuri.ogg"
            stop music fadeout 1.0
            $ renpy.music.play(audio.t5b, channel="music_poem", fadein=1.0, tight=True)
            "After a few more scenes, we're almost done with the chapter."
            "There's about two scenes left and the one we're doing involves Yuri's character."
            "I feel like Yuri is acting really strange today."
            "She's not being reclusive but she's also not acting aggressive."
            "Maybe she's gotten better...?"
            show monika 1c zorder 2 at t33
            m "There's no point in mourning them now..."
            m 3d "You're still looking for Yvonne, right?"
            m "When you see what she's done..."
            m 3e "I just know that--"
            mc "What could have gotten into her?"
            "I try my best to sound emotional but it just isn't working."
            mc "Why would Sachi do that to herself?"
            mc "Maybe I could have done something..."
            m 3h "No, I don't think so."
            m "There's nothing you could have done--"
            show sayori 1h zorder 3 at f32
            s "Hey, [player]..."
            s "We could {i}save{/i} some time here...{nw}"
            show screen tear(20, 0.1, 0.1, 0, 40)
            window hide(None)
            play sound "sfx/s_kill_glitch1.ogg"
            pause 0.25
            stop sound
            hide screen tear
            window show(None)
            s "We could {i}save{/i} some time here...{fast}"
            window auto
            s "It might help a lot for what's coming."
            s "If you know what I mean..."
            show sayori zorder 2 at t32
            show monika 1i zorder 3 at f33
            if m_appeal == 2 and did_all_tasks:
                m "Save...?"
                m "Is that how this is happening?"
                m "How we're going to get the best outcome...?"
                m "I think I understand it all now..."
            else:
                m "What...?"
                m "It's not your line, Sayori..."
            show sayori 1k zorder 3 at f32
            show monika zorder 2 at t33
            s "Sorry, please go on!"
            s "I just felt like I had to say something..."
            s 1d "I hope you understand, [player]."
            show sayori at thide
            hide sayori
            "Monika recomposes herself for the scene."
            m 1h "I think I may know where Yvonne could be."
            m 1o "But..."
            $ currentpos = get_pos()
            $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5_yuri2.ogg"
            stop music fadeout 1.0
            $ renpy.music.play(audio.t5c, channel="music_poem", fadein=1.0, tight=True)
            show yuri 1a zorder 3 at f31
            y 1y1 "Hi, Emcee."
            y "You're just in time."
            y "Look!"
            show yuri stab_1 zorder 3 at f31
            "Yuri pulls out a knife from her pocket."
            "She actually brought a prop for the play..."
            "But how did she know we were going to do this chapter for sure?"
            "She even voted for the other chapter."
            show yuri zorder 2 at t31
            mc "Y-Yvonne, what are you doing with that?"
            mc "Put that away!"
            show yuri zorder 3 at f31
            y "I've waited a long time for this moment."
            y "And now..."
            $ style.say_dialogue = style.edited
            y stab_1y4 "It's time for everyone to die."
            $ style.say_dialogue = style.normal
            show yuri zorder 2 at t31
            "That wasn't part of the script...was it?"
            "I feel like maybe Yuri is taking this a bit too seriously..."
            "Still, it could be interesting to see how it turns out."
            menu:
                "Should I go along with it or not?"
                "Play along.":
                    $ persistent.y_playday[0] = True
                    $ playalong = True
                    if persistent.y_playday[1]:
                        $ yuri_approval += 2
                    else:
                        $ yuri_approval += 1
                    "Well, this isn't part of the script."
                    "But it's going to make this play a whole lot more interesting."
                    mc "Yvonne?"
                    mc "What's gotten into you?"
                    mc "Why is it time for everyone to die?"
                    show yuri zorder 3 at f31
                    if yuri_approval > 3:
                        $ currentpos = get_pos()
                        $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_yuri.ogg"
                        stop music fadeout 0.3
                        $ renpy.music.play(audio.t5b, channel="music_poem", fadein=0.3, tight=True)
                        y stab_1n "[player]...?"
                        y stab_1o "What..."
                        y stab_1p "Am I dreaming...?"
                    else:
                        $ style.say_dialogue = style.edited
                        y "They've all outlived their usefulness."
                        y "So there's no need for them to be alive any longer."
                        y "There's just..."
                        y stab_1y2 "What the...?"
                        y stab_1y7 "WHAT'S GOING ON?!"
                        $ style.say_dialogue = style.normal
                    y stab_1o "Why do I have this odd feeling...?"
                    $ currentpos = get_pos()
                    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>mod_assets/bgm/5_yuri3.ogg"
                    stop music fadeout 0.2
                    $ renpy.music.play(audio.t5c, channel="music_poem", fadein=0.2, tight=True)
                    show yuri zorder 2 at t31
                    show sayori 1d zorder 3 at f32
                    if not persistent.y_playday[1]:
                        s "I think it's working!"
                        s "[player], you know what to do right?"
                        s 1h "Just do what you always do..."
                        s "Go back to your save!{nw}"
                        show screen tear(20, 0.1, 0.1, 0, 40)
                        window hide(None)
                        play sound "sfx/s_kill_glitch1.ogg"
                        pause 0.5
                        stop sound
                        hide screen tear
                        window show(None)
                        s "Go back to your save!{fast}"
                        window auto
                        s "..."
                        s 1k "I can't say it..."
                        s "But you know what I mean, right?"
                        s 1j "Just go back and choose the other choice..."
                        s "Now...!"
                    else:
                        s 1d "You actually..."
                        s "Thank you so much, [player]!"
                        s "It won't be long now, I promise."
                        s "Just keep going..."
                "Stop her.":
                    $ persistent.y_playday[1] = True
                    $ stopher = True
                    if not persistent.y_playday[0]:
                        $ yuri_approval -= 1
                    else:
                        $ yuri_approval += 2
                    "This isn't part of the script..."
                    "And that prop doesn't look too safe..."
                    "Maybe I should stop her."
                    "It's for everyone's safety, right?"
                    mc "Yuri, that looks dangerous."
                    mc "Do you mind putting that away?"
                    mc "I don't really feel comfortable doing this with you holding that."
                    "Yuri turns towards me and stares right into my eyes."
                    show yuri zorder 3 at f31
                    if yuri_approval > 3:
                        $ currentpos = get_pos()
                        $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_yuri.ogg"
                        stop music fadeout 0.3
                        $ renpy.music.play(audio.t5b, channel="music_poem", fadein=0.3, tight=True)
                        y stab_1p "[player]...!"
                        y stab_1o "I..."
                        y stab_1n "The knife..."
                        show yuri 3n
                    else:
                        $ style.say_dialogue = style.edited
                        y stab_1y3 "Of course, [player]."
                        y "Anything for you."
                        $ style.say_dialogue = style.normal
                        show yuri 3y3
                    play sound "mod_assets/sfx/metaldrop.ogg"
                    pause 1.5
                    "Yuri drops the knife and Sayori quickly grabs it."
                    y 3p "Wha...?"
                    "Yuri looks towards me with worried eyes."
                    $ currentpos = get_pos()
                    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>mod_assets/bgm/5_yuri3.ogg"
                    stop music fadeout 0.2
                    $ renpy.music.play(audio.t5c, channel="music_poem", fadein=0.2, tight=True)
                    show yuri zorder 2 at t31
                    show sayori 1d zorder 3 at f32
                    if not persistent.y_playday[0]:
                        s "I think it's working!"
                        s "[player], you know what to do right?"
                        s 1h "Just do what you always do..."
                        s "Go back to your save!{nw}"
                        show screen tear(20, 0.1, 0.1, 0, 40)
                        window hide(None)
                        play sound "sfx/s_kill_glitch1.ogg"
                        pause 0.5
                        stop sound
                        hide screen tear
                        window show(None)
                        s "Go back to your save!{fast}"
                        window auto
                        s "..."
                        s 1k "I can't say it..."
                        s "But you know what I mean, right?"
                        s 1j "Just go back and choose the other choice..."
                        s "Now...!"
                    else:
                        s 1d "You actually..."
                        s "Thank you so much, [player]!"
                        s "It won't be long now, I promise."
                        s "Just keep going..."
            show sayori at thide
            show monika at thide
            hide sayori
            hide monika
            show yuri zorder 2 at t11
            if persistent.y_playday[0] and persistent.y_playday[1]:
                $ play_firstpart = True
                "Yuri takes a moment to realize what's just happened."
                stop music_poem fadeout 0.5
                pause 0.5
                play music t9 fadeout 3.0
                if playalong:
                    show yuri stab_1p
                else:
                    show yuri 3p
                y "Did something just..."
                y "..."
                y "What the...?"
                if playalong:
                    show yuri stab_1n
                else:
                    show yuri 3n
                y "When did I get here?"
                y "What's happening...?"
                if playalong:
                    "She looks at her hands and drops the knife."
                else:
                    "She looks towards the floor and sees the knife."
                y 3o "Oh no..."
                y 3v "No..."
                y 3w "No...no...!"
                y "I didn't hurt anyone, did I?"
                y "I'm..."
                y "I'm so sorry..."
                y "How could I hurt my friends...?"
                show yuri at thide
                hide yuri

                "All of a sudden, she collapses to the floor."
                y "{i}AAAAAaaaaAAAAAAAAHH!!!!{/i}"
                "Clutching her head with both hands, she screams as loudly as she can."
                "I'm so shocked that I don't know how to react."
                "Everyone in the club pauses where they are and stare at Yuri."
                scene y_cg5_base with dissolve_cg
                "Her face has a blank expression."
                "It's almost like she just lost a part of herself."
                mc "Yuri...?"
                mc "Are you..."
                "I feel helpless, just seeing her on the floor like that."
                "It's like she's in immense pain but I can't do anything to help her..."
                s "Hey, guys..."
                s "Let's leave her for a moment."
                s "I think she needs some time to herself."
                "I notice Sayori let out a smile."
                s "{i}(We can finally start to help her, for real...){/i}"
                s "{i}(Thank you.){/i}"
                stop music fadeout 1.0

            else:
                if playalong:
                    show yuri stab_1y7
                else:
                    show yuri 3y7
                y "No!"
                if playalong:
                    y "It doesn't matter."
                    y stab_1y3 "Ahaha, everyone just has to die..."
                    y "This feeling..."
                    y stab_1y4 "It's like nothing I've ever felt before."
                    y "Do you understand, [player]?"
                    y "Nothing will stop you and I from being together."
                    "The atmosphere in the clubroom just got really tense."
                    "I'm still not sure if Yuri is saying that in character or if she actually means what she's saying..."
                    label play_choose_choice:
                    show yuri stab_1y4
                    "But it's only me in this scene, so I have to fix it somehow..."
                    window auto
                    menu:
                        "I better choose carefully."
                        "Keep playing along." if not choosechoice[0]:
                            $ choosechoice[0] = True
                            mc "Of course, nothing would stop me from being with my Yvonne."
                            mc "You are my world and nothing will change that."
                            mc "But aren't you being a little unreasonable here?"
                            mc "Nobody has to die."
                            mc "Not one more person."
                            mc "Are you listening to me, Yvonne?"
                            mc "..."
                            "What do I say here?"
                            "Is this still part of the play...?"
                            mc "Yvonne."
                            mc "If you really want to kill them..."
                            mc "Then you'll have to go through me."
                            $ style.say_dialogue = style.edited
                            y stab_1y3 "Ahaha!"
                            y "I can't believe how delusional you are."
                            y "Do you really think I won't kill you just to get to them?"
                            y "I'll do--{nw}"
                            $ style.say_dialogue = style.normal
                            show screen tear(20, 0.1, 0.1, 0, 40)
                            window hide(None)
                            play sound "sfx/s_kill_glitch1.ogg"
                            pause 0.25
                            stop sound
                            hide screen tear
                            window show(None)
                            if not choosechoice[1]:
                                show sayori 1j zorder 3 at i31
                                show sayori zorder 3 at f31
                                s "No, I won't let you..."
                                window auto
                                s 1d "We can still save you, Yuri..."
                                s "[player]..."
                                s "It won't be long now."
                                s "I'm going to help you this time.{nw}"
                                show sayori at thide
                                hide sayori
                                show screen tear(20, 0.1, 0.1, 0, 40)
                                window hide(None)
                                play sound "sfx/s_kill_glitch1.ogg"
                                pause 0.25
                                stop sound
                                hide screen tear
                                window show(None)
                            jump play_choose_choice
                        "Break character." if not choosechoice[1]:
                            $ choosechoice[1] = True
                            mc "Yuri..."
                            mc "What the hell are you saying?"
                            mc "I refused to believe it at first..."
                            mc "But I think I agree with Natsuki."
                            mc "You've gone insane."
                            y "Insane?!"
                            y "You're delusional, [player]."
                            y stab_1y3 "I'm feeling better than ever."
                            y "There's no way I'm going insane."
                            y "Ahaha..."
                            y "You know what?"
                            $ style.say_dialogue = style.edited
                            y stab_1y4 "I'm just going to kill you as well."
                            y "It won't matter, because in the end..."
                            y "You'll still be mine."
                            y stab_1y3 "Ahaha, I should have just killed everyone before--{nw}"
                            $ style.say_dialogue = style.normal
                            show screen tear(20, 0.1, 0.1, 0, 40)
                            window hide(None)
                            play sound "sfx/s_kill_glitch1.ogg"
                            pause 0.25
                            stop sound
                            hide screen tear
                            window show(None)
                            if not choosechoice[0]:
                                show sayori 1j zorder 3 at i31
                                show sayori zorder 3 at f31
                                s "No, I won't let you..."
                                window auto
                                s 1d "We can still save you, Yuri..."
                                s "[player]..."
                                s "It won't be long now."
                                s "I'm going to help you this time.{nw}"
                                show sayori at thide
                                hide sayori
                                show screen tear(20, 0.1, 0.1, 0, 40)
                                window hide(None)
                                play sound "sfx/s_kill_glitch1.ogg"
                                pause 0.25
                                stop sound
                                hide screen tear
                                window show(None)
                            jump play_choose_choice
                        "Embrace Yuri." if choosechoice[0] and choosechoice[1]:
                            "I walk up to Yuri and give her a warm embrace."
                            "She doesn't embrace back but I can tell she's shocked."
                            show yuri stab_1y2
                            stop music_poem fadeout 3.0
                            "I can feel her grip on the knife loosen."
                            mc "Yuri..."
                            mc "I don't know what's wrong with you."
                            mc "But..."
                            mc "Something clearly is."
                            mc "So..."
                            mc "If you'll let me help..."
                            play music t9 fadein 1.0
                            show yuri 1v
                            "Her grip on the knife loosens enough that she actually drops it."
                            play sound "mod_assets/sfx/metaldrop.ogg"
                            pause 1.5
                            y "[player]..."
                            y 1w "I don't..."
                            "She pulls herself away from my embrace."
                            y 3w "Please..."
                            y "I don't want to hurt you..."
                            y 3o "Any of you..."
                            y "I'm..."
                            show yuri at thide
                            hide yuri

                            "All of a sudden, she collapses to the floor."
                            y "{i}AAAAAaaaaAAAAAAAAHH!!!!{/i}"
                            "Clutching her head with both hands, she screams as loudly as she can."
                            "I'm so shocked that I don't know how to react."
                            "Everyone in the club pauses where they are and stare at Yuri."
                            scene y_cg5_base with dissolve_cg
                            "Her face has a blank expression."
                            "It's almost like she just lost a part of herself."
                            mc "Yuri...?"
                            mc "Are you..."
                            "I feel helpless, just seeing her on the floor like that."
                            "It's like she's in immense pain but I can't do anything to help her..."
                            s "Hey, guys..."
                            s "Let's leave her for a moment."
                            s "I think she needs some time to herself."
                            "I notice Sayori let out a smile."
                            s "{i}(We can finally start to help her, for real...){/i}"
                            s "{i}(Thank you.){/i}"
                else:
                    y 3y3 "That was silly of me."
                    y "How am I going to do it now...?"
                    y 3y1 "Ahaha, good thing I always bring a spare..."
                    "Yuri walks over to her bag and pulls out another knife."
                    "It doesn't look as sharp as her first one but it appears just as dangerous."
                    "I don't think that that is meant to be a prop either."
                    y stab_1y4 "Now..."
                    y "Who should I kill first?"
                    label stopher_choice:
                    if killchoice[0] and killchoice[1] and killchoice[2]:
                        "Sayori calls out to me."
                        window auto
                        s "There's only one choice left, [player]..."
                        s "You can do it..."
                    y stab_1y3 "[player]..."
                    window auto
                    menu:
                        y "Why don't you choose for me?"
                        "Monika." if not killchoice[0]:
                            $ killchoice[0] = True
                            y "Ahaha, it doesn't really matter who you choose."
                            $ _history_list.pop()
                            y "It's only a matter of time before{nw}"
                            $ _history_list.pop()
                            show screen tear(20, 0.1, 0.1, 0, 40)
                            window hide(None)
                            play sound "sfx/s_kill_glitch1.ogg"
                            pause 0.25
                            stop sound
                            hide screen tear
                            window show(None)
                            if not killchoice[1] and not killchoice[2]:
                                show sayori 1j zorder 3 at i31
                                show sayori zorder 3 at f31
                                s "No, I won't let you..."
                                window auto
                                s 1d "We can still save you, Yuri..."
                                s "[player]..."
                                s "It won't be long now."
                                s "I'm going to help you this time.{nw}"
                                show sayori at thide
                                hide sayori
                                show screen tear(20, 0.1, 0.1, 0, 40)
                                window hide(None)
                                play sound "sfx/s_kill_glitch1.ogg"
                                pause 0.25
                                stop sound
                                hide screen tear
                                window show(None)
                            jump stopher_choice
                        "Natsuki." if not killchoice[1]:
                            $ killchoice[1] = True
                            y "Ahaha, I knew you would choose her first."
                            $ _history_list.pop()
                            y "I've been waiting all week to do t{nw}"
                            $ _history_list.pop()
                            show screen tear(20, 0.1, 0.1, 0, 40)
                            window hide(None)
                            play sound "sfx/s_kill_glitch1.ogg"
                            pause 0.25
                            stop sound
                            hide screen tear
                            window show(None)
                            if not killchoice[0] and not killchoice[2]:
                                show sayori 1j zorder 3 at i31
                                show sayori zorder 3 at f31
                                s "No, I won't let you..."
                                window auto
                                s 1d "We can still save you, Yuri..."
                                s "[player]..."
                                s "It won't be long now."
                                s "I'm going to help you this time.{nw}"
                                show sayori at thide
                                hide sayori
                                show screen tear(20, 0.1, 0.1, 0, 40)
                                window hide(None)
                                play sound "sfx/s_kill_glitch1.ogg"
                                pause 0.25
                                stop sound
                                hide screen tear
                                window show(None)
                            jump stopher_choice
                        "Sayori." if not killchoice[2]:
                            $ killchoice[2] = True
                            y "Ahaha, that's probably the best choice!"
                            $ _history_list.pop()
                            y "That book really does kno{nw}"
                            $ _history_list.pop()
                            show screen tear(20, 0.1, 0.1, 0, 40)
                            window hide(None)
                            play sound "sfx/s_kill_glitch1.ogg"
                            pause 0.25
                            stop sound
                            hide screen tear
                            window show(None)
                            if not killchoice[0] and not killchoice[1]:
                                show sayori 1j zorder 3 at i31
                                show sayori zorder 3 at f31
                                s "No, I won't let you..."
                                window auto
                                s 1d "We can still save you, Yuri..."
                                s "[player]..."
                                s "It won't be long now."
                                s "I'm going to help you this time.{nw}"
                                show sayori at thide
                                hide sayori
                                show screen tear(20, 0.1, 0.1, 0, 40)
                                window hide(None)
                                play sound "sfx/s_kill_glitch1.ogg"
                                pause 0.25
                                stop sound
                                hide screen tear
                                window show(None)
                            jump stopher_choice
                        "Me." if killchoice[0] and killchoice[1] and killchoice[2]:
                            y stab_1y2 "What...?"
                            y "No!"
                            menu:
                                y "You have to choose someone else!"
                                "Me.":
                                    y "You...?"
                                    y stab_1y7 "What are you trying to pull here?!"
                                    y "Tell me..."
                            menu:
                                y "Who do you want me to kill first?!"
                                "Me.":
                                    y "..."
                                    y stab_1y2 "I..."
                                    stop music_poem fadeout 3.0
                            menu:
                                y "[player]...I..."
                                "Me.":
                                    y stab_1w "Why are you saying that...?"
                                    y "[player]..."
                            menu:
                                y "You..."
                                "Me.":
                                    pass
                            play music t9 fadein 1.0
                            y "This isn't..."
                            y "No..."
                            y "[player]..."
                            y "I can't do that..."
                            y stab_1o "No matter what it's telling me..."
                            y "I..."
                            y stab_1w "I could never hurt you..."
                            y "N-No matter how much I've..."
                            "Yuri's grip on her knife loosens."
                            "She visibly starts shaking."
                            y "I've..."
                            show yuri at thide
                            hide yuri

                            "Yuri looks at her shaking hands and drops the second knife."
                            "All of a sudden, she drops to her knees."
                            y "{i}AAAAAaaaaAAAAAAAAHH!!!!{/i}"
                            "Clutching her head with both hands, she screams as loudly as she can."
                            "I'm so shocked that I don't know how to react."
                            "Everyone in the club pauses where they are and stare at Yuri."

                            mc "Yuri...?"
                            mc "Are you..."
                            "I feel helpless, just seeing her on the floor like that."
                            "It's like she's in immense pain but I can't do anything to help her..."
                            show sayori 2d zorder 2 at t11
                            s "Hey, guys..."
                            s "Let's leave her for a moment."
                            s 2t "I think she needs some time to herself."
                            "I notice Sayori let out a smile."
                            s "{i}(We can finally start to help her, for real...){/i}"
                            s "{i}(Thank you.){/i}"
                            stop music fadeout 1.0
    return

label ch8_end:
    scene bg corridor
    show natsuki 1g zorder 2 at i31
    show sayori 1a zorder 2 at i32
    show monika 1a zorder 2 at i33
    with wipeleft_scene
    play music t8 fadeout 0.5
    "We all left the clubroom to give Yuri some space."
    "There's clearly something wrong with her and judging by how just acted..."
    "Well, I can't tell if she's feeling better or worse."
    show sayori 1d zorder 3 at f32
    s "She's feeling better, I know it."
    show sayori zorder 2 at t32
    mc "Huh?"
    mc "Are you talking about Yuri?"
    show sayori 2d zorder 3 at f32
    s "I know that's what you were thinking about..."
    s "You're worried about her."
    show sayori zorder 2 at t32
    show monika 1g zorder 3 at f33
    m "I don't think he's the only one."
    m "All of us just saw what happened."
    m "It would be wrong not to be worried about her."
    show natsuki 1h zorder 3 at f31
    show monika zorder 2 at t33
    n "I don't get it."
    n "Why did she just freak out like that?"
    n "Is that why she's been acting so mean?"
    show natsuki zorder 2 at t31
    show sayori 2k zorder 3 at f32
    s "Who knows?"
    s "It could be anything..."
    s "But like I said..."
    s 2d "She's feeling better than she was before."
    s "I just know we can help her now."
    show sayori zorder 2 at t32
    mc "What do you mean?"
    mc "How are we going to help her?"
    mc "We don't even know what's wrong with her."
    show sayori 2k zorder 3 at f32
    s "..."
    s 2g "I know {i}you{/i} don't..."
    s 2j "But someone looking out for us..."
    s 2k "Well, they know..."
    s 4d "Right?"
    show sayori zorder 2 at t32
    mc "What are you talking about?"
    mc "There's no one watching us Sayori..."
    "Is there?"
    show monika 1e zorder 3 at f33
    m "Maybe not, [player]."
    m "But...we have to cling on to hope..."
    m "Hope that the choices they make are the right ones."
    show natsuki 4g zorder 3 at f31
    show monika zorder 2 at t33
    n "I don't know what either of you are talking about..."
    n "You both sound like a bunch of crazy people..."
    n 4f "But--"
    show natsuki zorder 2 at t31
    show sayori 4k zorder 3 at f32
    s "Sometimes..."
    s "You just have to have a little faith..."
    if not play_firstpart:
        s 1q "You know...?"
        show sayori 1q:
            1.3
            easeout_cubic 0.5 yoffset 300
        pause 1.55
        play sound fall
        pause 0.25
        hide sayori
        pause 0.25
        scene black
        "Sayori suddenly falls to the ground."
        mc "S-Sayori!"
        mc "Are you okay?{nw}"
        $ currentpos = get_pos()
        $ audio.t8b = "<from " + str(currentpos) + " loop 9.938>bgm/8.ogg"
        stop music
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        scene black
        show sayori 1d at i11
        stop sound
        hide screen tear
        window show(None)
        play music mend
        s "Ehehe..."
        window auto
        s "I guess I got a little too excited there."
        s 1l "I just desperately wanted to save her life..."
        s "That I loaded saves for you...{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        scene black
        show sayori 1d at i11
        stop sound
        hide screen tear
        window show(None)
        s "That I loaded saves for you...{fast}"
        window auto
        s 1k "Oh..."
        s "I forgot that the game doesn't like me mentioning that."
        s "I'm gonna be honest with you..."
        s 1h "I'm hurting all over..."
        s "But..."
        s "We saved Yuri..."
        s 1d "And that's what matters..."
        s 1k "Don't worry about me, I'll be fine."
        s "I just need some rest..."
        s "Just finish off the club meeting without me."
        s "After all..."
        s 1d "Monika is still there."
        s 1k "One more thing..."
        s 1g "I know you didn't do what I said."
        s 1d "But I'm glad you helped me get through to Yuri."
        stop music
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        scene bg corridor
        show natsuki 4g zorder 2 at i21
        show monika 1e zorder 2 at i22
        stop sound
        hide screen tear
        window show(None)
        play music t8b
        mc "Um..."
        window auto
        mc "What are we doing?"
        show monika 1c zorder 3 at f22
        m "What do you mean?"
        m 3d "We're just waiting here until Yuri feels comfortable enough to come outside."
        show natsuki 1q zorder 3 at f21
        show monika zorder 2 at t22
        n "I really have no idea what's going on anymore."
        n "It feels like everything that's happening is out of my control."
        n 1r "Like sometimes, things just happen out of nowhere."
        n "I really don't like this at all."
        show natsuki zorder 2 at t21
        mc "That's a really bleak way to look at the world."
        mc "Is there something wrong?"
        show natsuki 1s zorder 3 at f21
        n "There's lots of things wrong."
        n "But there's nothing you can do to help."
        show natsuki zorder 2 at t21
        show monika 1f zorder 3 at f22
        m "..."
        m "Natsuki, we can try."
        show monika zorder 2 at t22
        "Suddenly, the clubroom door opens."
        "Yuri steps outside."
        show yuri 3v zorder 3 at f31
        show natsuki zorder 2 at t32
        show monika zorder 2 at t33
        y "..."
        y "You don't..."
        y "...need to say anything."
        y 3w "My actions have been inexcusable."
        y "I've put all of your lives in danger and..."
        y "...I don't know why."
        y 3v "It's better if I just leave the Literature Club."
        y "That way, I won't be able to hurt everyone I care about."
        show yuri zorder 2 at t31
        show monika 3f zorder 3 at f33
        m "Yuri, you don't know what you're talking about."
        m 3g "That person during the play..."
        m "...that wasn't you!"
        m 2e "But we can see right now, the person standing in front of us..."
        m "...is Yuri."
        show monika zorder 2 at t33
        mc "She's right."
        mc "I didn't want to say anything in the past couple of days."
        mc "It's like I wasn't allowed to but..."
        mc "You were a different person."
        mc "And now..."
        mc "You're Yuri again."
        show natsuki 4q zorder 3 at f32
        n "Look, Yuri."
        n "You've been acting really different this week."
        n "And I'm not sure if you're still insane or something..."
        n 4i "But..."
        n "If you really are back..."
        n "Then..."
        show yuri 4b zorder 3 at f31
        show natsuki zorder 2 at t32
        y "I'll understand if you won't be able to forgive me..."
        y "I've done some terrible things..."
        y "I almost..."
        y "In fact, I probably would have..."
        y "...killed one of you."
        y "I don't know why those thoughts came into my head..."
        y 3w "I..."
        y "No."
        y "There's no excuse for that..."
        show yuri zorder 2 at t31
        show monika 3e zorder 3 at f33
        m "Yuri, you should stop being so hard on yourself."
        m "We already know that that wasn't you."
        m "So..."
        show natsuki 4f zorder 3 at f32
        show monika zorder 2 at t33
        n "Okay, okay..."
        n "Fine..."
        n 4e "Yuri, I forgive you."
        n 4g "So can you please just stop acting so..."
        n "...weird?"
        show yuri 3o zorder 3 at f31
        show natsuki zorder 2 at t32
        y "I..."
        y "I don't know if I can accept your apology."
        y "I want to..."
        y 3t "...but I don't deserve this."
        show yuri zorder 2 at t31
        show natsuki 4h zorder 3 at f32
        n "Oh, come on."
        n "You don't need to be like that."
        n 4i "You can live your life out full of regret..."
        n "Or you can be content with me accepting your apology."
        show yuri 3w zorder 3 at f31
        show natsuki zorder 2 at t32
        y "Natsuki..."
        y "You are such a kind person..."
        y "I don't know why I ever..."
        y "..."
        y 3s "Thank you."
        y "But..."
        y 3v "I should still leave the Literature Club."
        y "It's for the good of everyone..."
        show yuri zorder 2 at t31
        show monika 2f zorder 3 at f33
        m "Ah..."
        m "Yuri, you don't need to do that."
        m "I know how much the club means to you..."
        m 2e "It wouldn't be fair to remove you just because you weren't yourself."
        m "I know Sayori would feel the same..."
        m "And besides..."
        m 2a "We want to help you."
        m "I know that that wasn't the only issue you have..."
        show yuri 1f zorder 3 at f31
        show monika zorder 2 at t33
        y "..."
        y 1g "You know a lot..."
        y "Don't you?"
        y 1j "Ahaha...."
        y "I must be terrible at hiding my problems."
        y "But I don't really think you can help with that..."
        show yuri zorder 2 at t31
        if ch7_name == "Yuri":
            mc "I'd like to help too."
            mc "I don't know why, but I feel like I knew about this already."
            mc "And I'll feel terrible if I don't do anything about it."
            show monika 1h zorder 3 at f33
            m "You do...?"
            m "Hmm..."
            m "That could be a problem."
            show monika zorder 2 at t33
            mc "How so?"
            show monika 1l zorder 3 at f33
            m "Ah...never mind."
        else:
            show monika 1e zorder 3 at f33
            m "You'd be surprised what we can do, Yuri."
            m "So you've got to let us try."
            m "But..."
            m "Not right now."
            m "There isn't enough time left to do everything we need to."
        show natsuki 1c zorder 3 at f32
        show monika zorder 2 at t33
        n "It's time to go..."
        n 1g "And I don't know about you guys, but I'd rather forget today happened..."
        n "I'll see you all tomorrow."
        show natsuki at thide
        hide natsuki
        show yuri 1h zorder 3 at f21
        show monika zorder 2 at t22
        y "I think I'll do the same..."
        y "I'd rather just..."
        y 1k "...forget everything that's happened today."
        y "Or in fact..."
        y 1v "This whole week."
        show yuri zorder 2 at t21
        show monika 3a zorder 3 at f22
        m "Alright..."
        m "I'm going to stay behind to clean up the clubroom."
        m "Take care of yourself, Yuri."
        m 3b "And stay away from knives..."
        m "Okay?"
        show yuri 3v zorder 3 at f21
        show monika zorder 2 at t22
        y "That won't be possible..."
        y 3s "But I'll try."
        show yuri at thide
        hide yuri
    else:
        s "You know?"
        show sayori zorder 2 at t32
        show natsuki 3s zorder 3 at f31
        n "Not really..."
        n 3r "I haven't had much faith in anybody lately."
        n "I said it at the start of this meeting and I'll say it again."
        n 3u "But no one really listens, do they?"
        show sayori 1k zorder 3 at f32
        show natsuki zorder 2 at t31
        s "I know what you're talking about, Natsuki..."
        s 1g "And you have to believe me when I say..."
        s 1h "That I'm sorry for keeping you waiting."
        show natsuki 4g zorder 3 at f31
        show sayori zorder 2 at t32
        n "At this point, I don't even know what you're talking about."
        n "You haven't kept me waiting at all."
        n "The only person doing that right now..."
        n "...is Yuri."
        n "But..."
        n "There's also something else..."
        n "It feels like everything that's happening is out of my control."
        n 1r "Like sometimes, things just happen out of nowhere."
        n "It really makes me feel worthless."
        show natsuki zorder 2 at t31
        mc "That's a really bleak way to look at the world."
        mc "Is there something wrong?"
        show natsuki 1s zorder 3 at f31
        n "There's lots of things wrong."
        n "But there's nothing you can do to help."
        show natsuki zorder 2 at t31
        show monika 1f zorder 3 at f33
        m "..."
        m "Natsuki, we can try."
        show monika zorder 2 at t33
        "Suddenly, the clubroom door opens."
        "Yuri steps outside."
        show yuri 3v zorder 3 at f41
        show natsuki zorder 2 at t42
        show sayori zorder 2 at t43
        show monika zorder 2 at t44
        y "..."
        y "None of you need to say anything..."
        y "But please listen to what I have to say..."
        y "Because..."
        y 3w "It's going to hurt me more than it hurts you."
        y "I..."
        y "I didn't mean for this to happen."
        y 3t "I don't know what happened to me..."
        y "And I..."
        y "I want to apologize to everyone."
        y 3v "I know I haven't been myself..."
        y "I've acted so horrible."
        y 3t "Natsuki..."
        show yuri zorder 2 at t41
        show natsuki 4i zorder 3 at f42
        n "...?"
        show yuri 3v zorder 3 at f41
        show natsuki zorder 2 at t42
        y "I know you might not be able to forgive me."
        y "I've been really rude to you."
        y "I've insulted you..."
        y 3w "I understand you may not be able to call me a friend again..."
        y "But..."
        y "I want you to know..."
        y "That whatever happens from here..."
        y 3u "I'll still call you my friend..."
        y "That goes for everyone..."
        "Yuri turns towards Sayori."
        y 3t "Sayori..."
        y "I'll understand if..."
        y "...I can't be a part of this club anymore."
        y "In fact..."
        y "It's probably better if I leave."
        y 3w "For the good of the Literature Club."
        y "..."
        y "I'm going to miss--"
        show yuri zorder 2 at t41
        show sayori 1j zorder 3 at f43
        s "You're not going to miss anything!"
        s "I refuse to let you leave the Literature Club!"
        s 1i "Are you listening to me, Yuri?"
        show yuri 3n zorder 3 at f41
        show sayori zorder 2 at t43
        y "Ah...!"
        show yuri zorder 2 at t41
        show sayori 1k zorder 3 at f43
        s "You still have problems..."
        s "I know you don't want to admit it."
        s "But I..."
        s 1j "{i}We{/i}..."
        s "Want to help you get through it."
        show natsuki 4e zorder 3 at f42
        show sayori zorder 2 at t43
        n "I don't even know what Sayori's talking about..."
        n "But..."
        n 4g "That person in the club, that wasn't Yuri."
        n 4c "You're Yuri..."
        n "So there's no point accepting your apology..."
        n 4g "...if you didn't do anything wrong."
        n 1q "But if it makes you feel any better..."
        n "Then I'll say it."
        n 1s "I forgive you, Yuri."
        show yuri 1v zorder 3 at f41
        show natsuki zorder 2 at t42
        y "You're..."
        y "You're too kind, Natsuki."
        y 1w "I don't..."
        y "...deserve this."
        show yuri zorder 2 at t41
        show natsuki 4w zorder 3 at f42
        n "And whatever problems you have..."
        n "You shouldn't keep them secret if it affects us."
        show natsuki zorder 2 at t42
        show sayori 2d zorder 3 at f43
        s "She's right..."
        s "You should open up so we can help you..."
        s "To solve her real problem we need--"
        show sayori zorder 2 at t43
        show monika 3l zorder 3 at f44
        m "Ahaha, it might not be the time for this Sayori."
        show sayori 2k zorder 3 at f43
        show monika zorder 2 at t44
        s "..."
        s "Right."
        s 2o "Um..."
        s 4q "Anyway, the meeting is over!"
        s "I hope we all had fun..."
        "The corridor becomes eerily quiet."
        s 4d "Well, you can all leave now."
        s "I'll stay behind and clean up."
        show sayori zorder 2 at t43
        show monika 3e zorder 3 at f44
        m "Sayori, don't trouble yourself with that..."
        m "You've done enough for today."
        m "So as your vice president, let me take that responsibility today."
        show sayori 2d zorder 3 at f43
        show monika zorder 2 at t44
        s "Thanks, Monika..."
        s "I could definitely use a break."
        show natsuki 1c zorder 3 at f42
        show sayori zorder 2 at t43
        n "I don't know about you guys, but I'm not staying here."
        n 1q "I just want to forget this whole day even happened..."
        n "I hope everyone is feeling the same..."
        n 1e "But whatever...."
        n "It doesn't really matter."
        show natsuki at thide
        hide natsuki
        show yuri 3l zorder 3 at f31
        show sayori zorder 2 at t32
        show monika zorder 2 at t33
        y "I feel the same..."
        y "I'd much rather forget any of this happened..."
        y "But..."
        y 3s "I really do appreciate your kindness..."
        y "All of you."
        show yuri zorder 2 at t31
        show monika 1e zorder 3 at f33
        m "Take care of yourself, Yuri..."
        m "I know there's still one thing we need to help you with..."
        m "But..."
        m 1a "That's a problem for another time."
        m "Stay away from knives, if you can..."
        show yuri 1h zorder 3 at f31
        show monika zorder 2 at t33
        y "I don't know if that's possible..."
        y 1b "But I can try."
        y "So..."
        y 1i "I'll see you all tomorrow for the start of manga..."
        show yuri at thide
        hide yuri
        show sayori 2b zorder 3 at f21
        show monika zorder 2 at t22
        s "Monika..."
        s "I..."
        s "I'm glad I have you here, as my vice president."
        s 2d "And as a friend."
        s "I just thought I should say that."
        s "And you as well, [player]..."
        show sayori zorder 2 at t21
        if ch7_name == "Yuri":
            mc "Hey, Sayori..."
            mc "There's something about yesterday..."
            mc "It was about Yuri..."
            mc "But I can't quite remember what it was."
            mc "Never mind..."
            mc "I just wanted to say that I'd like to help too."
            mc "You don't have to be alone when it comes to helping other people."
        else:
            mc "Thanks, Sayori..."
            mc "If there's anything at all I can do..."
            mc "To help Yuri..."
            mc "...or even Natsuki."
            mc "You'll tell me, right?"
            mc "You don't need to do it alone."
        show sayori 1k zorder 3 at f21
        s "I'll..."
        s "I'll let you know, [player]."
        "Sayori exhales."
        s 1g "If you don't mind..."
        s "I'm going to walk home by myself today."
        s 1h "I have a lot I need to think about."
        show sayori zorder 2 at t21
        mc "Right..."
        mc "I'll see you tomorrow then."
        show sayori 1k zorder 3 at f21
        s "Yeah..."
        show sayori at thide
        hide sayori
    show monika 3a zorder 2 at t11
    if not needs_to_read:
        m "So, it looks like it's just us again..."
        m "You know, I could use some help cleaning the club."
        m 3b "Do you mind?"
        mc "Sure, let's go."
        scene bg club_day with wipeleft_scene
        play music t3 fadeout 1.0
        "Monika and I begin cleaning up the mess of tables in the club."
        "The desks were rearranged so that there was a space in the middle of the club."
        "After a while, the club is back in shape."
        show monika 1c zorder 2 at t11
        m "Hey, [player]..."
        m "Did you end up getting rid of that book?"
        mc "The Portrait of Markov?"
        "I pull it out from my bag and show it to her."
        mc "No, I guess I haven't."
        if ch7_name == "Monika":
            m 1f "I thought I asked you yesterday in the club and at your house too."
        else:
            m 1f "I thought I asked you yesterday in the meeting to get rid of it."
        mc "I haven't really had an opportunity to."
        mc "And I still don't understand why you want me to."
        m 1g "[player]..."
        if m_appeal == 2 and did_all_tasks:
            m "You have to get rid of it."
            m 1f "I can't help you with that..."
            m 1i "That...{i}thing{/i}..."
            m "...is pure evil."
            m 1f "It's really gotten to me..."
            m "And not in a good way."
            m 1e "So get rid of it, as soon as you can."
            "I'm getting a really desperate feeling coming from Monika."
            "That isn't normal and she's obviously uncomfortable around the book."
            mc "Alright Monika..."
            mc "I suppose I'll get rid of it later today."
            mc "I don't know why, but it seems like it's creeping you out."
            m "Thank you, [player]."
            m "I'll see you tomorrow."
            show monika at thide
            hide monika
            "Monika leaves the clubroom."
            "She really wants me to get rid of this book."
            "I'm going to do it before I get home tonight."
        else:
            m 1h "Give it to me then."
            m "I'll get rid of it for you."
            m 1i "Trust me, it's the better way of doing this..."
            mc "Are you sure about that?"
            mc "I could just get rid of it myself."
            show monika g4
            m "No!"
            m "Um...I mean..."
            m 1e "I have a better way to dispose of it."
            "Monika's acting really weird here..."
            "Almost like she's not herself."
            "Still, she's just looking out for me..."
            "So..."
            menu:
                "Should I give it to her?"
                "Yes.":
                    $ gave_book_to_monika = True
                    mc "Alright Monika..."
                    mc "Since you're so eager to get rid of it..."
                    mc "I suppose you can."
                    m 1e "Thank you, [player]."
                    m "We can finally put this behind us."
                    "I hand Monika the book."
                    "She takes it and puts it into her bag."
                    mc "What do you have in mind for it?"
                    m 3a "That's a secret~"
                    m "But I appreciate you giving this to me, [player]."
                    "Monika walks over and gives me a hug."
                    show monika 1a at d11
                    mc "Um..."
                    mc "That was..."
                    m 5 "Ahaha, I'll see you tomorrow."
                    show monika at thide
                    hide monika
                    "That was unexpected."
                    "I didn't think the book meant that much to her."
                    "But..."
                    "I don't have time to think about that."
                    "I'm still in the club and it's getting late."
                "No.":
                    $ gave_book_to_monika = False
                    mc "I can't do that Monika."
                    mc "I'll get rid of it myself, when I think it's right."
                    mc "Something about this book just--"
                    m 1h "[player], you're making a big mistake."
                    m "You aren't going to get rid of it properly."
                    m "Only I can do that."
                    mc "Monika, I trust you..."
                    mc "You know that, right?"
                    m "..."
                    mc "So you have to trust that I'll do the right thing too."
                    mc "I'll get rid of it, if I really need to."
                    mc "Right now, I ju--"
                    m 1r "Forget I said anything."
                    m "You do what you need to with that book, [player]."
                    "Monika starts to walk away..."
                    m "I'll see you tomorrow."
                    show monika at thide
                    hide monika
                    "That was pretty cold."
                    "Monika is usually friendly and understanding but that was..."
                    "Well..."
                    "I don't have time to think about that."
                    "I'm still in the club and it's getting late."
    else:
        if gave_book_to_monika == None:
            $ gave_book_to_monika = False
        m 3e "You should get home, [player]."
        m "I don't want you to spend some extra time here, just for me."
        m "I can clean up the club, myself."
        mc "Alright, Monika..."
        mc "Good luck."
        m 1c "Before you go..."
        if not gave_book_to_monika and m_appeal == 2 and did_all_tasks:
            m "I want to ask..."
            m 1h "Have you got rid of that book yet?"
            mc "Yeah, actually."
            mc "I threw it in the bin."
            mc "I felt kinda bad about it..."
            mc "But if you're the one asking me, then there must be some reason."
            m 1m "Thank you, [player]..."
        elif gave_book_to_monika:
            m 1b "I want to thank you for giving me the book."
            mc "Sure..."
            mc "But weren't you going to get rid of it?"
            m 1l "O-Of course!"
            m "I'd just like to give you some gratitude."
        else:
            m 1h "Where did you put your copy of Portrait of Markov?"
            mc "Oh."
            mc "Well, I put it in the bin."
            m 1g "What?!"
            m "Which bin?"
            mc "Um..."
            mc "Just the one in the courtyard."
            mc "Does it matter?"
        m 1e "Well..."
        m "We're done here."
        m "So it's time to go home."
        m "I'll see you tomorrow."
        show monika at thide
        hide monika
        "Monika leaves the clubroom."
        "I'm left wondering why that book was so important..."
        "I shouldn't think about it too much, I need to get home."
    $ persistent.arc_clear[0] = True
    return
