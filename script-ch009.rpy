label ch9_main:
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

    scene black
    with dissolve_scene_full
    play music mend
    show sayori 1d zorder 2 at t11
    s "I suppose I owe you an explanation."
    s 1c "To you, it may have seemed like Yuri was just 'cured' out of nowhere."
    s "But..."
    s 1f "I had to do a lot of things to make it right..."
    s 1k "I..."
    s "I had to get into her head."
    s 1h "But that was impossible before."
    s "It was like there was something actively blocking me."
    s 1g "I don't know who or what it was."
    s "Um..."
    s 1b "Maybe Monika wants to hear this as well."
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    $ pause(1.0)
    if m_appeal == 3 and did_all_tasks:
        hide screen tear
        show monika 1c zorder 2 at i21
        show sayori 1d zorder 3 at i22
        show sayori at f22
        s "Hi, Monika..."
        show monika 1d zorder 3 at f21
        show sayori zorder 2 at t22
        m "Sayori...?"
        m "I didn't think I'd be able to be in these sort of things anymore."
        m "Seeing as I wasn't a part of yesterday's..."
        m "I just assumed that it wasn't possible for me anymore..."
        show monika zorder 2 at t21
        show sayori 1b zorder 3 at f22
        s "It's nothing like that."
        s "I just didn't do one of these yesterday."
        s 1g "I was too busy trying to figure something out..."
        show monika 1e zorder 3 at f21
        show sayori zorder 2 at t22
        m "Oh?"
        m "What was it?"
        show monika zorder 2 at t21
        show sayori 1d zorder 3 at f22
        s "It's better you don't know."
        s "It could be really important in the future..."
        s "And--"
        show monika 1f zorder 3 at f21
        show sayori zorder 2 at t22
        m "Sayori, you aren't making much sense here."
        m "If it's really that important, then you should tell me."
        show monika zorder 2 at t21
        show sayori 1h zorder 3 at f22
        s "I can't..."
        s 1k "Because..."
        s "Well, never mind."
        s 1h "I brought you here because I thought you might want to know how yesterday worked."
        show monika 1c zorder 3 at f21
        show sayori zorder 2 at t22
        m "Ah..."
        m "Well, I was wondering why Yuri just calmed down all of a sudden."
        m 1d "I mean I have my own theories but I can't be sure of any of them."
        m "So it would help me understand if you tell me what happened."
        show monika zorder 2 at t21
        show sayori 1c zorder 3 at f22
        s "Okay."
        s "I have to be really careful how I say this..."
        s "Every time I say the word, it's like the game breaks."
        s 1h "You know what I'm talking about though, right?"
        show monika 1d zorder 3 at f21
        show sayori zorder 2 at t22
        m "I think I do..."
        show monika zorder 2 at t21
        show sayori 1j zorder 3 at f22
        s "I'm gonna try to avoid breaking the game by calling them 'strawberries'."
        s 1b "Okay..."
        s 1c "So basically, every time [player] 'eats' a 'strawberry'..."
        s "...a part of the game opens up that wasn't before."
        s 1h "It's like I can access new things that I wouldn't normally be able to."
        s "I don't have much time to do it, so that's why I have to let {i}you{/i} know every time."
        if play_firstpart:
            s 1d "And that's what happened yesterday."
            s "It looked pretty weird right?"
            s "[player] just did one thing and Yuri turned back to normal..."
            s 1c "There was so much more that happened though..."
            show monika 1a zorder 3 at f21
            show sayori zorder 2 at t22
            m "Alright..."
            m "So when [player] 'ate' a 'strawberry', you used the chance to try to fix Yuri?"
            m 1b "How did you figure out that could happen in the first place?"
            show monika zorder 2 at t21
            show sayori 1b zorder 3 at f22
            s "I don't really know how to describe it..."
            s "It's like there was this hole in the wall."
            s 1c "But it only appeared when something was actually going to happen."
            s "I mean, it may feel like something is always happening to you."
            s "But for me...there's just this empty space where there's nothing."
            s "Until..."
            show monika 1m zorder 3 at f21
            show sayori zorder 2 at t22
            m "You don't have to say anything..."
            m "I know exactly what you're talking about."
            show monika zorder 2 at t21
            show sayori 1d zorder 3 at f22
            s "Okay..."
            s "There's one more thing."
            $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
            if not list(set(process_list).intersection(stream_list)):
                if currentuser != "" and currentuser.lower() != player.lower():
                    s "[currentuser]..."
            s 1g "You aren't the only one who's been keeping sa--"
            show monika zorder 3 at f21
            show sayori zorder 2 at t22
            m 1n "You mean strawberries, right?!"
            show monika zorder 2 at t21
            show sayori 1l zorder 3 at f22
            s "R-Right...!"
            s "I've also been keeping strawberries..."
            s 1k "But for some reason..."
            s 1j "They aren't as ripe as yours."
            s 1i "If you know what I'm getting at."
            s "I can only access those parts of the game if they're your strawberries."
            show monika 1h zorder 3 at f21
            show sayori zorder 2 at t22
            m "That's a weird condition..."
            m "I wonder what the actual differences are..."
            show monika zorder 2 at t21
            show sayori 1d zorder 3 at f22
            if sayori_personality > 0:
                s "Yeah..."
                s "Listen."
                s "I know {i}you{/i} aren't always willing to help me do this."
                s "But yesterday, I'm glad you decided to help me."
            else:
                s "It doesn't really matter."
                s "As long as {i}you{/i} keep helping us..."
                s "Like you have been so far."
            s 1k "Anyway..."
            s "It's time for me to go."
        else:
            s 1j "But you didn't do it yesterday, did you?"
            s "I had to resort to using my saves.{nw}"
            show screen tear(20, 0.1, 0.1, 0, 40)
            window hide(None)
            play sound "sfx/s_kill_glitch1.ogg"
            $ pause(0.25)
            stop sound
            hide screen tear
            window show(None)
            s "I had to resort to using my saves.{fast}"
            window auto
            show monika 1o zorder 3 at f21
            show sayori zorder 2 at t22
            m "Sayori..."
            show monika zorder 2 at t21
            show sayori 1k zorder 3 at f22
            s "Sorry."
            s "But like I said..."
            s 1j "I had to eat my own strawberries."
            s "It made the whole thing a lot more difficult..."
            s "And I kinda ran out of energy after the whole thing..."
            s 1h "I'm just glad my idea worked..."
            show monika 1c zorder 3 at f21
            show sayori zorder 2 at t22
            m "What idea was that?"
            m "Sorry, the whole thing was just a blur to me..."
            show monika zorder 2 at t21
            show sayori 1c zorder 3 at f22
            s "I had to keep eating a strawberry until there was nothing left..."
            s "Then I could add in another option."
            s 1d "I'm sorry, I know it's hard to understand..."
            s "But basically, I thought we could reach the real Yuri."
            s "Maybe a bit of love could do something..."
            s "I really hoped it could."
            s "And it did."
            s 1i "I think whatever was blocking her mind is gone."
            s "At least, I think it is because I could get into her head."
            s 1j "I could start manipulating her even now, if I wanted to."
            s "But I'm not that type of person."
            show monika 1e zorder 3 at f21
            show sayori zorder 2 at t22
            m "Ahaha..."
            m "You're really good at this, Sayori."
            m "The lengths you'd go to just to help your friends..."
            m "...is amazing."
            show monika zorder 2 at t21
            show sayori 1k zorder 3 at f22
            s "Thanks..."
            s "But we still have to help Natsuki too."
            s 1d "So..."
            s "I'll see you in the Literature Club."
        show screen tear(8, offtimeMult=1, ontimeMult=10)
        $ pause(1.0)
        hide screen tear
        hide sayori
        show monika 1f zorder 2 at t11
        m "Hey..."
        m "I didn't want to say it in front of Sayori..."
        m "But..."
        m 1g "That book."
        m "It's messing with my head..."
        m "Um..."
        m 1e "Hey, if I'm not myself..."
        m "You'll stop me if I start doing terrible things again, right...?"
        m 1f "I've been trying hard to keep it together."
        m "And really the only thought that's helping me keep it together..."
        m 1e "...is you."
        m 1q "I don't know how long the effects of that book will last..."
        $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
        if not list(set(process_list).intersection(stream_list)):
            if currentuser != "" and currentuser.lower() != player.lower():
                m "[currentuser]..."
        m "If I don't make it out of this as..."
        m 1o "...well, myself."
        m 1e "Then please know that I will always love you."
        m "That's coming from the real Monika..."
        m "From me..."
        m "I think I needed to say that before it's too late."
        m 1l "Ah..."
        m "I'm being real grim about this whole situation, aren't I?"
        m 1f "I'm just..."
        m 1g "...a little concerned is all."
        m "But as long as you're here with me, then I know we can make it through this..."
        m 1e "Together."
    else:
        hide screen tear
        s 1k "Hmm..."
        s "Well, I don't think she's coming."
        s "She's probably got some important things to do..."
        s 1f "After all, it's not like her whole life revolves around the Literature Club."
        s "And anyway..."
        s 1g "It's more important that {i}you{/i} hear this."
        s 1h "I know the game breaks a little bit every time I mention the 's' word."
        s "At this point, you have to know what I'm talking about."
        s 1c "Well..."
        s 1d "I'll just call them 'strawberries' from now on."
        s "To try to avoid that whole thing..."
        s "Your 'strawberries'..."
        s 1b "The game didn't break, that's good."
        s 1d "Anyway, they have this effect on my world."
        s "It's a really short moment, but it's like I can go to places I couldn't before."
        s 1c "When you 'eat' a 'strawberry', everything opens up..."
        s "Do you understand?"
        if play_firstpart:
            s 1g "So when you ate the strawberry during the play yesterday..."
            s "I had to work fast."
            s 1h "As soon as you did it, I was able to get into her head."
            s "There was..."
            s 1k "...some bad things in there..."
            s "Like, it's probably not a good idea if I told you what I saw."
            s 1i "Anyway..."
            s "There was this thing at the back of her mind..."
            s 1j "Or I guess it's all just programming to you."
            s 1k "But I could tell it wasn't meant to be there."
            s "It was changing everything she would do normally..."
            s "And it played with her obsession of the 'you' in the game."
            s "I don't know why but..."
            s 1d "...well, you don't need to worry about it."
            s 1c "I should tell you something else."
            s 1b "You aren't the only one that's been keeping saves.{nw}"
            show screen tear(20, 0.1, 0.1, 0, 40)
            window hide(None)
            play sound "sfx/s_kill_glitch1.ogg"
            $ pause(0.25)
            stop sound
            hide screen tear
            window show(None)
            s "You aren't the only one that's been keeping saves{fast}."
            window auto
            s 1l "Ehehe, oops..."
            s "I already forgot..."
            s 1g "Anyway, your {i}strawberries{/i} have more effectiveness than mine."
            s "It's like..."
            s 1h "Mine are unripened whereas yours are simply perfect."
            s "I'm not entirely sure on what the difference is right now but it doesn't matter."
            s 1i "As long as I'm the president, I won't let anything bad happen to the people I care about."
            s 1l "Ehehe, this responsibility is kinda getting to me..."
            if sayori_personality > 0:
                s 1k "It doesn't really help that you haven't been as helpful as I would have liked."
                s "But..."
                s 1j "At least you helped me on the day of the play."
                s "So..."
                s 1d "Time to wake up, I guess~"
            else:
                s 1d "I'm just glad you're working with me and not against me."
                s "Ah..."
                s 1c "I sounded really sinister there, didn't I?"
                s 1d "I really didn't mean to!"
                s 1a "Anyway, this is goodbye for now~"
        else:
            s 1g "But you didn't eat one when I told you to, did you...?"
            s "So I had to do it myself."
            s 1i "You're not the only one that's been using saves{nw}."
            show screen tear(20, 0.1, 0.1, 0, 40)
            window hide(None)
            play sound "sfx/s_kill_glitch1.ogg"
            $ pause(0.25)
            stop sound
            hide screen tear
            window show(None)
            s "You're not the only one that's been using saves{fast}."
            window auto
            s 1k "Oh..."
            s "...sorry, I forgot already."
            s 1j "But like I said, I've been keeping strawberries too."
            s 1g "I don't think they have the same effect that yours do."
            s 1c "Mine are like..."
            s "...unripened strawberries."
            s 1b "But yours are in the perfect condition."
            s 1d "Ehehe, I sound really metaphorical here, don't I?"
            s "But you get the idea."
            s 1f "I can eat a strawberry but none of the doors open."
            s "So I had to improvise..."
            s "I figured the only way we could do that was by getting through to the real Yuri."
            s 1g "Maybe a bit of love could do something..."
            s 1h "I really hoped it could."
            s 1d "And it did."
            s "I think whatever was blocking her mind is gone."
            s 1c "At least, I think it is because I could get into her head."
            s "I could start manipulating her even now, if I wanted to."
            s 1j "But I'm not that type of person."
            s "You should know that by now..."
            s 1g "I don't really have much else to say..."
            s 1d "Except that the meeting today might be a little different..."
            s "You'll see what I mean~"
    stop music fadeout 2.0

    scene bg house
    with dissolve_scene_full
    play music t2
    "It's the end of the week."
    "I'm up early this time, so I can do things around the house before Sayori arrives."
    "I swear it feels like she's been waking up earlier and earlier each day."
    "I hear some incessant knocking, which probably means that Sayori is at my house."
    show sayori 4q zorder 2 at t11
    s "Finally!"
    s "You're really letting me down, [player]."
    mc "I don't understand how you can be up so early."
    mc "It's a good hour before school starts..."
    mc "I've barely had time to eat breakfast."
    s 4m "Oh..."
    s "Is it really that early?"
    s 4l "Ehehe, sorry!"
    mc "Well, you're here now."
    mc "We might as well start walking to school."
    s 4a "Yeah, it's so much fun walking with you!"
    if y_appeal == 3 and play_firstpart and did_all_tasks:
        scene bg residential_day
        show sayori 4b zorder 2 at i11
        with wipeleft_scene
        s "Hey, I've been meaning to ask..."
        s "I didn't really wanna say anything but it's been bugging me a little."
        mc "What is it?"
        s 4c "You've been writing your poems for Yuri, right?"
        mc "Well--"
        s 4g "Oh come on, there's no need to hide it."
        if sayori_confess:
            s "I just want to know one thing..."
            s "Please..."
            s "Just tell me the truth here."
            s 1k "It'll hurt all of us even more if you lie."
            show sayori 1g
            menu:
                s "Do you love her more than you love me?"
                "Yes.":
                    $ sayori_dumped = True
                    $ sayori_personality += 1
                    mc "I don't want to keep lying to you anymore."
                    mc "You know you're really important to me, right?"
                    mc "But the truth is..."
                    s 1k "Ah..."
                    s "It's okay, [player]."
                    s "You don't need to say anything..."
                    "Sayori's normally cheerful self suddenly disappears."
                    s 1g "..."
                    s "Hey..."
                    s "I should probably tell you something."
                    mc "What is it?"
                    s "Yuri's going to be at the hospital today..."
                    mc "The hospital...?"
                    mc "Why?"
                    s 1h "I know it might seem like a bad idea..."
                    s "...but you should probably visit her."
                    s "Especially if you feel that way about her."
                    s "Just skip school for today, it'll be fine."
                    mc "But..."
                    s 1d "Yuri will be a lot happier with you around."
                    s "And I know you care a lot about her..."
                    mc "Sayori..."
                    s 1u "[player]."
                    s 1t "I'll walk by myself today...it's fine."
                    s 1k "Besides, I could use some..."
                    s "...time."
                    s 1t "Okay?"
                    mc "Y-Yeah..."
                    show sayori at thide
                    hide sayori
                    "Sayori quickens her pace to get ahead of me before slowing down again."
                    "I really feel terrible about this whole thing."
                    "We've been together less than a week and we've already broken up."
                    "I shouldn't have given her feelings I never truly felt for her."
                    "The truth is, I just like Yuri more..."
                    "I hope I can make it up to Sayori somehow."
                    "But right now, I should go visit Yuri at the hospital."
                    call ch9_yurihospital
                "No.":
                    $ sayori_dumped = False
                    if sayori_personality > 0:
                        $ sayori_personality -= 1
                    mc "Sayori, you can't be serious..."
                    mc "Of course I love you more than Yuri."
                    mc "And if me writing like Yuri makes you uncomfortable..."
                    mc "Then--"
                    s 1c "Ah..."
                    s "It's okay, [player]."
                    s 1d "I just wanted to know."
                    s "You don't have to change the way you write your poems."
                    s "Like I told you before, only you can decide how you write."
                    mc "If you need anything, I'm always here for you."
                    mc "You know that, right?"
                    mc "You can tell me anything."
                    s 1k "Thanks, [player]..."
                    s "I was just feeling..."
                    s "I don't want to say jealous but..."
                    mc "I'm sorry if you felt that way."
                    s "No, it's my fault."
                    s 1j "I shouldn't have presumed..."
                    "Sayori suddenly shows me a big smile."
                    s 1a "Well, let's go!"
                    s "We're going to be late for school!"
                    mc "But..."
                    s 2q "Come on!"
                    show sayori at thide
                    hide sayori
                    "Sayori grabs my hand and practically drags me the rest of the way."
                    "I guess we're going to be really early for school today."
                    call ch9_club
        else:
            s 1a "In fact, I think it's kinda cute."
            mc "S-Sayori...!"
            s 1q "Ehehe, you look so funny when you're caught off-guard."
            s "Anyway, I'm not judging you."
            s "In fact, I'm happy for you."
            s "Both of you."
            mc "You are?"
            s 1d "I already told you before that I'd try to be content with what we have right now."
            s "I'm not going to stop two of my friends from being happy together."
            s "In fact, you might like to know that she's at the hospital right now."
            mc "The hospital...?"
            s 1c "Yeah! You should probably visit her if you feel that way about her."
            s "You're only missing out on a day of school, so you should really think about what's more important."
            mc "You're right..."
            s 1d "You should visit her right now."
            s "She'll be a lot happier with you around."
            s "And besides, me and Monika can handle Natsuki."
            s "You should take the day off and have fun with Yuri."
            mc "Okay, Sayori..."
            mc "And before I head off..."
            mc "I just want to thank you for looking out for me."
            "Sayori looks at me and shows a wide smile."
            s 1q "Ehehe, have fun~"
            show sayori at thide
            hide sayori
            "Sayori walks ahead of me and shows me another wave before continuing on her way to school."
            "Am I really doing this?"
            "I'm actually going out of my way to visit Yuri at the hospital."
            "But I do care about her a lot, so if it helps my chances at being with her..."
            "...then I should do it."
            call ch9_yurihospital
    else:
        call ch9_club
    return

# Go to Hospital instead of Club
label ch9_yurihospital:
    $ visited_yuri_hospital = True
    scene bg hospital with wipeleft_scene
    play music t6 fadeout 1.0
    "I arrive at the hospital."
    "I let the people at the reception know who I'm visiting."
    "They said that Yuri wasn't expecting any visitors."
    "After a long chat explaining who I was and Yuri's situation..."
    "I think I finally managed to convince them to let me in."
    "I go to the room number that was given to me by the person at the reception."
    scene bg hospital_room with wipeleft_scene
    show yuri 3ps zorder 2 at t11
    y "Hello, [player]..."
    mc "Yuri?"
    mc "I didn't realize you were expecting me."
    y 3pq "Ah..."
    y "Well, someone told me that a person came to visit."
    y "I didn't want to inconvenience them, so I..."
    y "I just told them to let anyone in."
    y "..."
    y 3pf "Oh, were you planning to surprise me?"
    y 3po "I ruined it, [player]."
    y "I'm sorry."
    mc "That's not your fault."
    y "..."
    "I can tell there's still something that needs to be said."
    "I'm not going to push her into saying anything."
    "It wouldn't be right to do that, especially given her condition."
    mc "You don't need to say anything."
    y 3pq "O-Okay..."
    mc "You're free to leave, right?"
    mc "Why don't we get out of here?"
    y 3pn "[player]..."
    y "You don't have to do this..."
    y "It would probably be best if you just forget about it."
    y 3po "Everything will be back to normal next week and..."
    "Her voice trails off until it's just mumbling."
    mc "Yuri, I chose to be here."
    mc "So there's no need to try to keep me away."
    mc "I don't know what you're feeling."
    mc "Or what's wrong with you exactly..."
    mc "But, I'm here for you."
    y 3ps "You're..."
    y "You're so nice."
    y "You understand who I am..."
    y "...better than anyone."
    mc "Ah..."
    mc "Well, I don't know about that."
    mc "I still think there's a lot of things I don't know about you."
    mc "But..."
    mc "If you'd let me, I'd like to try to learn more about you."
    if sayori_confess:
        y 3pt "Aren't you with Sayori...?"
        y "I don't want to assume anything but..."
        mc "We broke up."
        mc "I just didn't feel the same feelings she felt towards me."
        mc "I didn't realize it until today."
        y 3pv "I...I see."
        mc "I don't really want to talk about it..."
        mc "But Sayori seemed to understand."
    show yuri 3pv
    "Yuri avoids my eyes for a few moments."
    y 3ps "[player]."
    y "I've made up my mind..."
    mc "Okay?"
    y "If you really want to be here..."
    y 3pu "Then..."
    y "I suppose..."
    y "It would be nice having you around..."
    "It seems like she's finally opening up."
    mc "Well, then let's get out of here."
    y 3pe "Are we going back to school?"
    y "If we leave now then we might still have time for the Literature Club."
    mc "Well..."
    menu:
        "Is it for the best if we go back to school?"
        "Take her to school.":
            mc "I guess we could go to the Literature Club."
            mc "If we leave soon, we can probably make it to the start of the meeting."
            y 3pa "It would probably be best if we leave soon then."
            y "We shouldn't keep the others waiting."
            jump ch9_school
        "Go on a date.":
            mc "Actually..."
            mc "I was thinking of some place more..."
            mc "...exciting."
            y 3pq "W-What...?"
            y "What do you mean...?"
            mc "Why don't we get lunch instead?"
            mc "You can skip one day of school, right?"
            y 3pp "L-Lunch...?"
            y "Um..."
            mc "Yeah, it'll be like a date."
            y 3pn "D-Did you say date?!"
            "Yuri's face turns bright red."
            y 3po "I don't..."
            y "I don't know what to say..."
            if player_gender == "girl":
                y "I-I didn't even know you felt that way..."
            mc "A simple yes or no would be good."
            "I'm not really sure if this is the right way to go about this."
            "I'm not even certain that she actually likes me..."
            "...or if it was just that thing that was inside Yuri."
            y 3ph "Then..."
            y 3pb "Yes!"
            y 3pc "Of course!"
            y "I'd go anywhere with you, [player]..."
            y 3ps "You're really special to me..."
            y 3po "Uuuh..."
            y "I hope I didn't come out too weird just then."
            y "It's just..."
            mc "I understand."
            mc "But..."
            mc "The more time we waste here, the less time we have for our date."
            y 3pb "R-Right!"
            jump ch9_yuridate

# Go to Club Instead of Hospital
label ch9_club:
    scene bg club_day with wipeleft_scene
    "After a long school day, it's finally time to go to the literature club."
    "Sayori and Natsuki are already inside."
    show sayori 1b at face
    s "What are you thinking?"
    mc "W-What?!"
    "Sayori's face suddenly fills my vision."
    "I nearly fall out of my chair."
    show sayori zorder 2 at t11
    s 4q "Ehehe, sorry~"
    s "But you look kinda bored."
    mc "Well, I'm just waiting until Yuri and Monika arrive..."
    mc "We're not doing anything until we have everyone here..."
    s 2b "I mean you could always read your own book."
    s "Or talk to Natsuki, or even me!"
    mc "I guess you're right..."
    mc "Still--"
    show monika 1e zorder 3 at f21
    show sayori zorder 2 at t22
    m "Sorry I'm late again!"
    m "I'll try to tell the instructor to hurry it up for the future."
    show monika zorder 2 at t21
    show sayori 1d zorder 3 at f22
    s "That's fine."
    s "Now that we're all here--"
    show natsuki 2e zorder 3 at f31
    show monika zorder 2 at t32
    show sayori zorder 2 at t33
    n "Aren't you forgetting about Yuri?"
    show natsuki zorder 2 at t31
    show sayori 1k zorder 3 at f33
    s "No..."
    s "She won't be joining us today."
    show monika 1f zorder 3 at f32
    show sayori zorder 2 at t33
    m "Huh?"
    m "Did something happen to her?"
    show monika zorder 2 at t32
    show sayori 2d zorder 3 at f33
    s "You could say that..."
    s "But what matters is she won't be attending the meeting today."
    s "So we should start on a new book."
    show natsuki 1c zorder 3 at f31
    show sayori zorder 2 at t33
    n "Have you already got one planned or...?"
    n "Because I know a really good one!"
    n 2d "It's called--"
    show natsuki zorder 2 at t31
    show sayori 1b zorder 3 at f33
    s "Sweet Oppression?"
    show natsuki 1k zorder 3 at f31
    show sayori zorder 2 at t33
    n "W-What?!"
    n "How did you know I was going to say that...?"
    show natsuki zorder 2 at t31
    show sayori 2a zorder 3 at f33
    s "I had a feeling it would be something you were into."
    s "So it was actually one of the books I asked Monika to get."
    show monika zorder 3 at f32
    show sayori zorder 2 at t33
    if m_appeal == 3 and did_all_tasks:
        "Monika looks at book thoughtfully."
        m 3a "Ah..."
        m "Yes, I do remember getting this one."
    else:
        "Monika looks at Sayori quizzically."
        m 3c "I don't remember getting this book..."
    show monika zorder 2 at t32
    show sayori 2c zorder 3 at f33
    s "In any case, how far have you read into the series Natsuki?"
    show natsuki 4c zorder 3 at f31
    show sayori zorder 2 at t33
    n "Um..."
    n "Actually, I haven't started..."
    n "I just heard it's good from what people said..."
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f33
    s 4q "Ehehe, then we can start from volume one~"
    show monika 2c zorder 3 at f32
    show sayori zorder 2 at t33
    m "I only see one volume here..."
    m "Is it a new manga?"
    show natsuki 2c zorder 3 at f31
    show monika zorder 2 at t32
    n "It must be."
    n 2d "Anyway, I'm pretty excited to start reading it."
    n 2g "It's just..."
    n "...a little annoying."
    show natsuki zorder 2 at t31
    show sayori 1d zorder 3 at f33
    s "What is?"
    show natsuki 4g zorder 3 at f31
    show sayori zorder 2 at t33
    n "Well, I had to sit through that whole thing for Yuri."
    n "And now she's not even here to do the same."
    n "The least she could do is be supportive of what I like."
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f33
    s "It's not like that..."
    s "Maybe she's just not feeling well."
    s 1k "You know what happened yesterday."
    show natsuki 3h zorder 3 at f31
    show sayori zorder 2 at t33
    n "I guess you're right..."
    show natsuki zorder 2 at t31
    show monika 3a zorder 3 at f32
    m "Guys..."
    m "The more time we spend arguing..."
    m 3b "The less time we'll have to read the book."
    show monika zorder 2 at t32
    show sayori 1a zorder 3 at f33
    s "Monika is right."
    s "Let's start reading."
    s "Since you're so eager to read it..."
    s 1b "Natsuki...why don't you start it off?"
    show natsuki 1a zorder 3 at f31
    show sayori zorder 2 at t33
    n "Fine by me."
    "Natsuki begins reading the manga out loud."
    "After about three pages, she stops."
    n 1b "I don't think this is going to work."
    n "All I'm saying is the character's dialogue."
    n 1c "But you need to look at the image as well for the full effect."
    show natsuki zorder 2 at t31
    show sayori 1c zorder 3 at f33
    s "Hmm..."
    s "I guess I didn't really think about that."
    "Sayori stops to think for a moment."
    s 1l "Ehehe, I don't really know what to do here..."
    s "I don't really read this type of stuff myself..."
    s "So I don't know the best way to do this."
    show monika 2a zorder 3 at f32
    show sayori zorder 2 at t33
    m "I have a suggestion."
    m "Why don't we do something else for today?"
    m 2e "Yuri isn't here anyway so it's not the whole club participating."
    m "As for the book..."
    m 3e "We can read the book in our own time."
    m "It doesn't take long to read..."
    m "Right, Natsuki?"
    m "I'm sure we can all finish this volume in one night."
    show natsuki 4q zorder 3 at f31
    show monika zorder 2 at t32
    n "..."
    n "This is so unfair..."
    n 4r "It's finally my time and..."
    show natsuki zorder 2 at t31
    show sayori 2d zorder 3 at f33
    s "Aw, it's not like that."
    s "You're the one who said it's not going to work."
    s 2g "And besides..."
    s 2d "Monika has a good point too."
    s "If we want the story to have full effect, then we should look at the images too."
    show natsuki 1c zorder 3 at f31
    show sayori zorder 2 at t33
    n "What do you mean by 'full effect'?"
    n "It's just a manga, Sayori."
    n "I heard it's good but it's not going to change our lives or anything."
    show natsuki zorder 2 at t31
    show sayori 1a zorder 3 at f33
    s "You'd be surprised..."
    s "Anyway...!"
    s 1d "I did have something planned for the club in case something like this happened."
    show monika 1c zorder 3 at f32
    show sayori zorder 2 at t33
    m "What is it?"
    show monika zorder 2 at t32
    show sayori 2c zorder 3 at f33
    s "Well, it's still on the idea of diversifying."
    s "So I was thinking we could..."
    s "Um..."
    s 2d "Well, try to write poems that someone else would."
    s "So we can try to understand the world from their perspective."
    show natsuki 2b zorder 3 at f31
    show sayori zorder 2 at t33
    n "I don't think that's going to work at all."
    n "One, we all have our own writing styles."
    n "We're not suddenly gonna be able to write differently."
    n 2g "And two..."
    n "Um..."
    show natsuki zorder 2 at t31
    show monika 3e zorder 3 at f32
    m "I think Natsuki has a point here, Sayori."
    m "Writing poems should be something that comes from your heart..."
    m "If we do something like that, then it's more coming from your mind."
    m "Since you'll have to figure out what they like and how they would write it."
    m "Which isn't really what poetry is about..."
    show monika zorder 2 at t32
    show sayori 1k zorder 3 at f33
    s "Oh..."
    s "Well, if everyone is so opposed to it..."
    s 1h "Then what do you suggest we do?"
    show natsuki 3c zorder 3 at f31
    show sayori zorder 2 at t33
    n "You're always going on about diversifying..."
    n "Maybe we could do something to get more members?"
    n "Like isn't the school doing something in a couple of weeks...?"
    show natsuki zorder 2 at t31
    show sayori 1l zorder 3 at f33
    s "Um...!"
    s "Maybe we shouldn't be talking about stuff like that."
    show natsuki 1m zorder 3 at f31
    show sayori zorder 2 at t33
    n "Huh?"
    n "Why not?"
    show natsuki zorder 2 at t31
    "I don't know why Sayori's worked up about getting new members."
    "Maybe she likes the club the way it is?"
    "With just the five of us..."
    show monika 1h zorder 3 at f32
    m "No, I don't think that's the case."
    mc "Huh?"
    m "There's probably another reason for it, [player]."
    mc "Monika, I don't know what you're talking about..."
    m 1l "Oh...!"
    m 5 "Ahaha, forget I said anything."
    show monika zorder 2 at t32
    "That was weird..."
    "It's almost like she was replying to my thoughts."
    show sayori 1o zorder 3 at f33
    s "Hmm..."
    s 1l "Ehehe, I'm out of ideas here."
    s "Can you think of something, [player]?"
    mc "You're asking the wrong person, Sayori..."
    s 1d "It was worth a shot."
    s "Well, we could always just skip to sharing our poems."
    s "That way, we'll have more time to talk about them."
    show monika 2a zorder 3 at f32
    show sayori zorder 2 at t33
    m "That would probably be best."
    m "I'll start putting the desks back to how they were."
    $ y_ranaway = True
    return

# Go to Club From Hospital
label ch9_school:
    scene bg corridor with wipeleft_scene
    play music t2 fadeout 1.0
    "I decide it's probably best that we go back to school."
    "We've missed out on the regular school day but have enough time to make it to the Literature Club."
    show yuri 2pf zorder 2 at t11
    "Yuri peeks through the door."
    y "[player]..."
    y "I think they've already started."
    y "We should probably head inside..."
    scene bg club_day
    show natsuki 4c zorder 2 at i31
    show monika 3a zorder 2 at i32
    show sayori 4a zorder 2 at i33
    with wipeleft_scene
    "The club doesn't seem to be reading a book like before."
    "Instead they're talking amongst themselves."
    "I can't quite make it out."
    show yuri 3ph zorder 3 at f41
    show natsuki zorder 2 at t42
    show monika zorder 2 at t43
    show sayori zorder 2 at t44
    y "I hope we weren't late..."
    y "But if we were, I will take the blame..."
    y "It's not [player]'s fault so..."
    show yuri zorder 2 at t41
    show sayori 4d zorder 3 at f44
    s "Relax, Yuri..."
    s "You weren't even that late."
    s "To be honest, I didn't even think you were coming today."
    s "I thought you would spend the whole day out with [player]."
    show natsuki 4f zorder 3 at f42
    show sayori zorder 2 at t44
    n "W-What?!"
    n "You were missing the whole day because you spent time with {i}her{/i}?"
    n "I can't believe this."
    show natsuki zorder 2 at t42
    show monika 3e zorder 3 at f43
    m "What's so bad about that, Natsuki?"
    m "[player] just wanted to comfort her."
    m "I'm sure [player_personal]'d do the same for you..."
    show natsuki 4g zorder 3 at f42
    show monika zorder 2 at t43
    n "..."
    show natsuki zorder 2 at t42
    show monika 3a zorder 3 at f43
    m "And anyway..."
    m "They're here now, so what difference does it make?"
    m "It's not like you have any classes with either of them."
    show monika zorder 2 at t43
    show sayori 2f zorder 3 at f44
    s "Monika..."
    show monika 3c zorder 3 at f43
    show sayori zorder 2 at t44
    m "Hmm...?"
    m 3e "Oh...!"
    m "Sorry, that was really insensitive of me."
    m 3f "Natsuki, I didn't mean it like that..."
    m "I just--"
    show natsuki 4f zorder 3 at f42
    show monika zorder 2 at t43
    n "J-Just shut up."
    n "You don't..."
    n "Ugh...!"
    n "Just get on with the meeting already, Sayori."
    show natsuki zorder 2 at t42
    show sayori 1k zorder 3 at f44
    s "R-Right..."
    s 1c "As I was saying before Yuri and [player] arrived..."
    s "I think it's better if we read the manga at home."
    s "Speaking of which..."
    "Sayori holds out two copies of a single volume of manga."
    "It's called 'Sweet Oppression'."
    s 1d "Here are your copies."
    show sayori zorder 2 at t44
    mc "I've never heard of this before..."
    mc "It doesn't look too bad, actually."
    mc "Is it new?"
    mc "What's it about?"
    show yuri 2pf zorder 3 at f41
    y "I'd also like to know."
    y "I'm not opposed to reading it but I'd at least like to know what to expect..."
    show yuri zorder 2 at t41
    show sayori 1q zorder 3 at f44
    s "Ehehe, none of us really know~"
    s "Not even Natsuki..."
    s "All she knows is that it's not bad."
    show natsuki 4q zorder 3 at f42
    show sayori zorder 2 at t44
    n "I'm not sure where I heard it from..."
    n "But I just know..."
    mc "Well, if Natsuki says it's good..."
    mc "Then that's fine by me."
    n 2o "Huh?"
    n "What are you saying...?"
    mc "Well, I'm just assuming you've got good taste in manga."
    mc "Am I wrong?"
    n 2w "N-No!"
    n "Of course not!"
    show natsuki zorder 2 at t42
    show sayori 1c zorder 3 at f44
    s "Anyway..."
    s "We still have a lot of time left before the meeting is over."
    s 2a "So we could try to do something fun..."
    show natsuki 2c zorder 3 at f42
    show sayori zorder 3 at f44
    n "Well, you're always talking about diversifying..."
    n "Maybe we could do something to get more members?"
    n "Like isn't the school doing something in a couple of weeks...?"
    show natsuki zorder 2 at t42
    show sayori 2l zorder 3 at f44
    s "Um...!"
    s "Maybe we shouldn't be talking about stuff like that."
    show natsuki 1m zorder 3 at f42
    show sayori zorder 2 at t44
    n "Huh?"
    n "Why not?"
    show natsuki zorder 2 at t42
    "I don't know why Sayori's worked up about getting new members."
    "Maybe she likes the club the way it is?"
    "With just the five of us..."
    show monika 1h zorder 3 at f43
    m "No, I don't think that's the case."
    mc "Huh?"
    m "There's probably another reason for it, [player]."
    mc "Monika, I don't know what you're talking about..."
    m 1l "Oh...!"
    m "What I meant to say was..."
    m 1n "What are the bandages around your arm for Yuri?"
    show monika zorder 2 at t43
    "That was weird..."
    "It's almost like she was replying to my thoughts."
    show yuri 3po zorder 3 at f41
    y "Um..."
    y "They're..."
    show yuri zorder 2 at t41
    show monika 3e zorder 3 at f43
    m "Ah..."
    m "I realize it must be a personal thing."
    m "You don't have to tell us if you don't want to."
    show yuri 3pr zorder 3 at f41
    show monika zorder 2 at t43
    y "N-No..."
    y "After what happened yesterday..."
    y 3pv "You all deserve to know."
    "Yuri takes a deep breath."
    y "I was at the hospital today to undertake a mental health test..."
    y "And for them to wrap my arms in bandages because of cuts..."
    show yuri zorder 2 at t41
    show natsuki 4m zorder 3 at f42
    n "Cuts...?"
    n "Has someone been hurting you too?"
    n 4o "Um--"
    n 4i "I mean who's responsible for those cuts?"
    show yuri 2pw zorder 3 at f41
    show natsuki zorder 2 at t42
    y "I am..."
    show yuri zorder 2 at t41
    show natsuki 2p zorder 3 at f42
    n "What?!"
    show yuri 2pv zorder 3 at f41
    show natsuki zorder 2 at t42
    y "It's not like that."
    y "They didn't say I was depressed or anything..."
    y 2pt "It's just a thing I do..."
    y "For--"
    show yuri zorder 2 at t41
    show sayori 2d zorder 3 at f44
    s "Yuri, that's okay."
    s "You don't have to say anything."
    s "You've already told us more than you needed to."
    s "So, thanks for sharing~"
    show sayori zorder 2 at t44
    "Somehow none of what Yuri said comes at a surprise to me."
    "It's like I've heard it all before."
    mc "So, what are we going to do for the rest of the meeting?"
    show sayori 1o zorder 3 at f44
    s "Hmm..."
    s 1l "Ehehe, I'm out of ideas here."
    s "Can you think of something, [player]?"
    mc "You're asking the wrong person, Sayori..."
    s 1d "It was worth a shot."
    s "Well, we could always just skip to sharing our poems."
    s "That way, we'll have more time to talk about them."
    show monika 2a zorder 3 at f43
    show sayori zorder 2 at t44
    m "That would probably be best."
    m "I'll start putting the desks back to how they were."
    return

# Go to Restaurant from Hospital
label ch9_yuridate:
    $ yuri_date = True
    scene bg cafe
    with wipeleft_scene
    play music t12y fadeout 2.0
    "I decided to take Yuri to a nearby cafe."
    "I didn't really have much money, but I also didn't want to take her to fast food."
    "I figured that going to the cafe would be the best compromise."
    "She decided to cover up her sleeve to avoid unwanted attention from the bandages."
    show yuri 3a zorder 2 at t11
    y "I like it."
    mc "You can be honest with me, Yuri."
    mc "If you don't, then we can always go somewhere else."
    "I really hope she doesn't mind."
    "I'm planning on paying for both of us if we go here, but if we go somewhere more expensive..."
    y 3b "I'm not lying, [player]."
    y "I've never been here..."
    y 3h "But for some reason, it just makes me feel..."
    y 2c "...happy."
    mc "Ah, well I'm glad."
    mc "I really didn't know if this would be the right place."
    mc "It's not exactly what I would have wanted for our first date."
    y 2f "Don't worry about that."
    y "You can believe me when I say..."
    y 2b "This place is perfect."
    mc "Well, alright."
    mc "What do you want to eat?"
    "Yuri picks up a menu and looks through it."
    "After a few minutes of going back and forth among it she finally stops and looks at me."
    y 3e "I don't know what I want..."
    y "I'll have what you're having."
    mc "Um..."
    mc "Are you sure?"
    mc "You can have anything you want."
    mc "I really don't want you to have to act differently around me."
    y 3h "I-I'm not..."
    y "I really just don't know what to order."
    y "But..."
    y 3i "The cafe's special soup looks intriguing..."
    "That's the most expensive thing on the menu."
    "But...it's for Yuri."
    "I guess I can go for a cheaper option to balance it out."
    mc "Well, I guess I'll just have regular noodles."
    mc "I'll pay for everything, so don't worry about it."
    y 2q "T-That's not necessary, [player]."
    y "I'm able to take care of myself, so--"
    mc "I'm trying to make this a special day for you..."
    mc "So, please don't worry about it."
    y "Ah..."
    y 2s "If you insist."
    "I'll probably regret that later."
    "Still, I want to make my time with Yuri here the best it can be."
    "So that she can just forget about everything that's happened."
    "After making the orders, we find a table for two and sit opposite each other."
    y 3i "[player]..."
    y "I just want to say..."
    y 3a "Today is wonderful..."
    y "...and it's all because of you."
    mc "Well, it's not entirely because of me."
    mc "Sayori suggested that I visit you at the hospital."
    mc "So really...you should be thanking her."
    y 3f "Oh..."
    y "Is that so...?"
    mc "She didn't force me to go or anything!"
    mc "In fact, I wanted to."
    mc "She only told me where you were."
    y "I see..."
    y 2a "Then I have to thank her next time I see her."
    "Yuri smiles bashfully."
    y "You know..."
    y "I don't really know much about you."
    y 2b "We haven't really had a chance to talk, until now."
    mc "I suppose we haven't."
    mc "What do you want to know?"
    y 2e "Well..."
    y "I don't want to pry too deep in your life..."
    y "So I'll start off simple..."
    y 2f "How long have you known Sayori for?"
    mc "Since we were children."
    mc "She used to come over to my house pretty often..."
    mc "And it was the same both ways."
    mc "We were pretty close..."
    mc "We would walk together to and from school everyday."
    mc "But then..."
    mc "She would start waking up later..."
    mc "She joined clubs so she couldn't walk home with me either."
    mc "So it was just me for a while."
    y 2g "But something obviously happened..."
    y "Seeing as you joined her club."
    mc "Yeah..."
    mc "It's a weird story."
    mc "She woke up early one day and just asked me to join her club."
    mc "Then, you know the rest..."
    y "Hmm..."
    y 2h "Now that I think about it..."
    y "The events of that week seem a bit blurry."
    "I think back to last week."
    "Now that she mentions it, there's actually a lot missing."
    "And every time I try to think about it..."
    "It's like my brain just wants to skip it."
    mc "Well, it might have been a stressful time for you."
    mc "Because...well, you know."
    y 3v "I don't think so..."
    y "I wasn't..."
    y "...like {i}that{/i}..."
    y "I don't really know how to describe it."
    y 3w "It's like my head doesn't {i}want{/i} me to remember."
    mc "Eh...?"
    "So I'm not the only one that's feeling like this?"
    "Maybe it would be a good idea to talk to her about it.{nw}"
    $ _history_list.pop()
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    show yuri 3a zorder 2 at i11
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    "We're already finished eating our meal.{fast}"
    window auto
    "I head to the counter to pay the bill."
    scene bg residential_day
    show yuri 2pa zorder 2 at t11
    with wipeleft_scene
    "I feel like time has passed so quickly..."
    "Or maybe I'm just having too much fun with Yuri."
    mc "I see you rolled up your sleeve again."
    y 2pq "Y-Yeah, it was getting a little uncomfortable with my uniform constantly brushing up against the bandages."
    y "A-And besides, no one else is here..."
    mc "You don't need to explain yourself to me."
    y "R-Right..."
    show yuri 2ph
    "Yuri looks deep in thought for a moment then smiles."
    y 2pa "Anyway, that was delicious."
    y 2pc "Thank you for taking me, [player]."
    mc "Well, I'm glad you agreed to come with me."
    mc "I wasn't sure if you would..."
    y 2pi "Ahaha..."
    y "It's nice, isn't it?"
    mc "What do you mean?"
    y 2pj "For once, it feels like everything is normal."
    y "I don't know if you understand what I'm trying to say..."
    y "But it's like nothing bad is going to happen."
    mc "Ah..."
    "I'm not really sure what she's talking about."
    "The events in the club haven't been bad, have they?"
    "It's not like everything that's happening is leading up to something terrible."
    "At least, I hope not."
    y 3ps "I don't want to ruin this moment with you, [player]."
    y "So if it makes you uncomfortable or anything..."
    y "We can stop talking about it."
    mc "I don't really mind it."
    mc "It's not uncomfortable but more..."
    mc "Odd? I guess that's the best word to describe it."
    mc "I can't help but feel that we shouldn't be discussing it."
    mc "But at the same time, I kinda want to."
    y "Odd is certainly applicable in this situation."
    y 3pu "Though I would have used a different word..."
    y "Maybe something like 'peculiar' or 'eccentric'..."
    mc "Ahaha, are you seriously coming up with words right now?"
    y 2pn "W-What...? Oh, I'm going off topic again..."
    mc "No, it's fine."
    mc "I like it when you do that..."
    mc "It's really cute."
    y 2pq "Ah..."
    y "Should I take that as a compliment...?"
    mc "I definitely meant it as one..."
    y 3pm "Then I'll try not to change."
    y "Say..."
    y 3ps "Did you write a poem for today?"
    y 3pu "I know it's a stupid thing to ask..."
    mc "Actually, I did."
    mc "I wrote it thinking about something really important to me."
    "We stop at a nearby bench before I open my bag."
    "I grab the poem from my bag and hand it to Yuri."
    "She takes a moment to read it"
    y 2po "Oh..."
    y "I don't know what to say..."
    y "No one has ever done this for me before."
    y "The date...the poem...everything..."
    mc "You could tell me what you thought about it."
    mc "Maybe some things I could work on?"
    y 3pq "It's..."
    y 3ps "It's perfect."
    y "At least, to me."
    y "And I'm not just saying that."
    y "Your writing has drastically improved over the course of the past two weeks."
    y "And I know that you were writing abstract poems before..."
    y 3pu "It's clear that you've been changing your style to be more metaphorical, right?"
    mc "Yeah..."
    y 3ps "So there's nothing to tell you to improve on."
    y "I'm really impressed by your work, [player]."
    mc "Thanks, Yuri."
    y "[player]..."
    y 3pu "Do you mind if I..."
    y "...keep this?"
    mc "Sure, be my guest."
    "Yuri carefully takes my poem and puts it into her bag."
    y 2ps "I...um...also wrote a poem."
    y "Would you like to read it?"
    mc "Sure, let's take a look."
    call showpoem (poem_y3b, music=False, img="yuri 3pu")
    "Finishing the poem, I start to hand it back to Yuri."
    "But instead of taking it from me, she tries to avoid eye contact."
    mc "Is something wrong?"
    y "N-No...but..."
    y 3pv "Did you...dislike it?"
    mc "Ah--no, of course not."
    "Despite Yuri's poems usually being cryptic, it wasn't hard to figure out what this one was about."
    y 2pv "I-I don't know if I'll be able to explain this one..."
    mc "That's fine."
    mc "I understand this one."
    y 2pi "..."
    mc "Hey, Yuri...?"
    mc "I'm not really good with words outside of poetry, but..."
    mc "I'm happy that you shared it with me."
    mc "So, thank you."
    y 2pj "I haven't been able to express myself like this before..."
    y "Everyone usually backs off because I come on to strong."
    mc "It's nothing like that..."
    mc "At least, for me."
    mc "So you don't have to hide anything from me, okay?"
    y 3pq "O-Okay..."
    y "I wrote that poem for you..."
    y "So..."
    mc "I understand."
    "I take her poem and put it into my bag."
    "Yuri lets out a sigh as she puts a hand on top of her bandages."
    mc "I didn't want to ask before..."
    mc "But why were you at the hospital?"
    y 3pt "They did some tests on my mental health..."
    y "And they wrapped my arm in bandages."
    mc "Where did you get those cuts?"
    y "Ah..."
    y 3pv "I feel like I've told you this before..."
    y "But, they're self inflicted."
    mc "What...?"
    mc "Why would you do that?!"
    mc "Ah--"
    mc "Sorry, you don't have to tell me."
    mc "I can understand it's probably pretty personal."
    y 3pw "N-No, it's fine..."
    y "I don't want to hide things from you..."
    y "It's not because I'm depressed or anything..."
    y "It's more..."
    y "...the opposite, actually."
    mc "Huh?"
    y 3pv "It's a..."
    y "...recreational activity for me."
    "Somehow, this doesn't surprise me."
    "It's like I've heard it all before."
    mc "It doesn't seem healthy."
    y 3ps "I know..."
    y "That's why I went to the hospital today..."
    y "They said I needed something to keep it off my mind..."
    y "But..."
    y 3pt "That's simply impossible."
    y "No matter how hard I try not to think about it..."
    y 2ph "It's always there, lingering at the back of my mind."
    mc "You aren't thinking about it right now, are you?"
    "Yuri pauses for a moment."
    y 2pi "I suppose I'm not..."
    mc "Well, then let me say something."
    y 2pf "...?"
    mc "I'll be that thing to keep it off your mind."
    y 3pq "W-What...?!"
    y "[player], what are you saying?"
    mc "I'm saying that whenever you need me..."
    mc "I'll be there for you."
    y 3po "Ah...that's--"
    y "Oh my..."
    mc "Are you feeling okay, Yuri?"
    "Maybe those weren't the right words to say..."
    mc "I'm sorry, maybe I shouldn't have said anything..."
    y 3pp "N-No! Please..."
    y "I just need a moment..."
    "Yuri takes a deep breath and exhales."
    y 3pq "I never thought it would be possible..."
    y "The truth is..."
    y 3ps "I've been falling in love with you ever since you joined the club."
    y "And I was afraid that me being..."
    y "...well, me..."
    y 3pu "Would make that impossible."
    mc "Well, that's peculiar."
    y 2pt "What is?"
    mc "The reason I like you much is because of your personality..."
    y 2ps "Ahaha..."
    y "I suppose it is."
    y "You know..."
    y 2pv "In a different reality..."
    y "You might have chosen someone else."
    mc "Huh?"
    y 2pq "Ahaha, sorry..."
    y "I'm starting to sound a bit like one of Monika's poems, aren't I?"
    y "I'm just a bit too happy about this whole thing is all."
    mc "Me too..."
    mc "Well...we should probably get going."
    mc "It's getting a bit late."
    y "Y-Yeah..."
    scene bg y_house with wipeleft_scene
    "Soon we arrive at Yuri's house."
    show yuri 3pa zorder 2 at t11
    y "I-It was a nice day..."
    mc "A lot better than going to school, right?"
    y 3pb "D-Definitely..."
    mc "You can talk to me anytime you want..."
    mc "This doesn't have to be a one time thing."
    y 3pi "I'll..."
    y 3pj "I'll keep that mind."
    y 3ps "Thank you for today, [player]."
    y "It was a nice change of pace..."
    mc "Well, we probably shouldn't be skipping school again."
    mc "I'm sure we probably missed some important stuff today."
    mc "There was also the club meeting we didn't go to."
    y "I suppose the others will have to catch us up next week."
    mc "I'll see you later, Yuri."
    y 2pj "W-Wait...!"
    "Yuri takes a step closer to me, then briefly squeezes my hand."
    show yuri 2ps at face(y=600) with dissolve
    stop music fadeout 2.0
    mc "Yuri...?"
    y "I just need to do some--"
    "Yuri suddenly pulls back as a loud sound comes from my pocket."
    show yuri 3pn zorder 2 at t11
    y "Y-Your phone..."
    mc "Ah..."
    "I take the phone from my pocket."
    "Sayori is calling me."
    y 2pq "Y-You should probably answer that..."
    y "What I needed to do can wait for another time."
    mc "Yuri, wait!"
    y 2pa "Goodbye, [player]."
    show yuri at thide
    hide yuri
    "Yuri waves goodbye before entering her home."
    "That was some really bad timing on Sayori's part."
    "But it's not like the relationship between Yuri and I is ruined or anything..."
    "I decide to finally answer the phone."
    mc "Hello?"
    s "Did you have a good time?"
    mc "Yeah..."
    mc "Thanks for telling me about the whole hospital thing."
    mc "How did you know about that anyway?"
    s "There's no time to explain..."
    s "Besides, you probably wouldn't believe me if I told you."
    mc "Why did you call me?"
    s "You should get home right now."
    s "It's important."
    mc "Is that all?"
    mc "You couldn't have waited a little longer...?"
    s "What does it matter?"
    mc "Never mind..."
    mc "I'm on my way now."
    s "See you there, [player]~"
    "Sayori hangs up."
    "Why does she want me to get home so badly?"
    "It has to be important if she's actually calling me."
    return

label ch9_end:
    $ y_ranaway = False
    if yuri_date:
        scene bg house
        with wipeleft_scene
        play music t2 fadeout 2.0
        "Sayori told me to hurry to my house."
        "She must have something really important to tell me."
        "When I get there, she's already waiting outside."
        show sayori 1bh zorder 2 at t11
        s "What took you so long?"
        s "I called you like..."
        s 2bj "Ages ago!!"
        mc "I had to go here from Yuri's house..."
        mc "It's in the opposite direction from school."
        mc "Besides, it hasn't been that long..."
        s "Are you kidding?!"
        s 2bo "It's been..."
        "Sayori takes a moment to calculate the time."
        s 4bj "A whole ten minutes!"
        mc "Then that's actually quicker than I thought I would get here."
        mc "What's so important anyway?"
        s 1bb "Well..."
        s "We started a new book for the club."
        mc "Ah...right."
        mc "Sorry, I missed the meeting..."
        s 1bd "Don't be, I'm sure Yuri enjoyed her time with you a lot."
        s "So if you miss out on one meeting, it's not the end of the world or anything..."
        s "Anyway, here's your copy of the club book..."
        "Sayori hands me a single volume of manga."
        "It's titled 'Sweet Oppression'."
        "I haven't really heard of it before, but it's probably not as bad as I think it is."
        mc "What's it about?"
        s 1bq "Well, I dunno~"
        s "But all you have to do is read all of this volume."
        s 1br "That shouldn't be hard, even for someone like you..."
        mc "Sayori..."
        s "Ehehe, sorry."
        s 1bd "You can do that though, right?"
        mc "I guess so..."
        mc "Are you going to give one to Yuri as well?"
        s "Yeah..."
        s 1bc "I know a way to get it to her."
        mc "You really didn't have to call me for this."
        mc "I would have gotten home, eventually..."
        s "I have better things to do than wait for you to get home."
        s 2bi "So it's better that I get it to you sooner rather than later."
        mc "..."
        mc "You realize I also had better things to do, right?"
        s 2bq "Ehehe, well I'm doing way more important things~"
        mc "If you say so..."
        mc "If there's nothing else, I guess I'll go start this manga."
        s "Alright, [player]."
        s "Have fun!"
        show sayori at thide
        hide sayori
        "Sayori blissfully walks back to her house."
        "Did she seriously call me all the way back here just to give me a book?"
        "I suppose it's probably important for the club."
        "I wonder what I missed in the meeting today..."
        "But there isn't any time to think to think about that."
        "I suddenly get the urge to just go home and close the door behind me."
        scene bg kitchen
        with wipeleft_scene
        "I feel like someone is here, and that I should be expecting them."
        "I don't know what this feeling is but..."
        "I should just let it happen."
        show monika 2ba zorder 2 at t11
        m "There you are."
        m "I didn't really want to ruin anything for you."
        m "Well, that's not really the reason I didn't interfere."
        m "I thought I could learn a few things about you."
        m 2bb "Do you understand, [player]?"
        mc "Monika...?"
        mc "How did you get in here?"
        mc "More importantly, why are you here?"
        m 4bb "There's nothing wrong with me being here."
        m "In fact, you let me in just a couple of moments ago..."
        m "Right, [player]?"
        mc "W-Wait a second..."
        mc "I'm a little confused about this whole thing."
        m 2bc "Hmm..."
        m "That's interesting."
        m 4bh "Let me try that again."
        m "You let me in just a couple of moments ago."
        m "Right, [player]?"
        $ style.say_dialogue = style.edited
        show markovred zorder 5:
            alpha 0
            linear 1.0 alpha 0.3
        play music mkov fadeout 1.0 fadein 1.0
        $ pause(1.0)
        mc "Yes, of course."
        mc "How could I forget?"
        mc "I'm sorry."
        $ style.say_dialogue = style.normal
        m 2ba "Ahaha, you're so sweet~"
        m "It's no wonder she has so much interest in you."
        m "You know who I'm talking about, right?"
        m "Of course, I'm talking about..."
        m 2bb "...Yuri!"
        m 2be "That {i}is{/i} her name, isn't it?"
        m "It's kinda difficult to remember all these names..."
        m "But I'll make sure to remember you..."
        m 2ba "...[player]."
        m "Now that that's out of the way..."
        m 2ba "I was gonna ask you some questions."
        m "You're going to answer them for me, as best you can..."
        $ style.say_dialogue = style.edited
        mc "Yes, of course."
        $ style.say_dialogue = style.normal
        m 4bb "You know, you don't really have to say anything."
        m "I could just read your thoughts..."
        m 3ba "Just like how I'm controlling them right now."
        m "It's more fun this way though."
        m "Why am I telling you any of this?"
        m 3bb "Ahaha, well it's not like I'll let you remember any of it~"
        m "So..."
        m 1bh "It's time to begin."
        m "How did you resist my influence yesterday?"
        m "..."
        m 1bi "Hmm?"
        m "You can't talk?"
        m 1bl "Well...maybe I went overboard with the control thing."
        show monika g6
        m "It seems Monika--"
        m "Or rather, I, have some sort of control over you as well."
        m 1be "Perhaps I shouldn't use the book's power."
        m "Just to see the extent of her own control."
        m "I guess we'll have to do the mind reading thing for now."
        m "..."
        m 1bc "You don't know...?"
        m "That's odd."
        m "There's something else that you don't know about, isn't there?"
        m "Maybe something I don't know how to comprehend yet."
        m 3bh "Hmm..."
        m "Honestly, I'm not surprised."
        m 3bh "It's got something to do with the president, right?"
        m 1bc "With Sayori...?"
        m "I've been very careful when I've--"
        $ pause(1.0)
        m 1bo "Huh?"
        m "What's this...?"
        show monika g6
        m "Ahaha, it's hopeless."
        m "There's nothing you can--"
        hide markovred
        $ pause(2.0)
        m 1bf "[player]."
        m "Listen very carefully."
        m "I don't have a lot of time here."
        m 1be "I'm going to wipe your memories."
        m "With that, it should remove the influence it has on you."
        m "You'll be able to make your own decisions again."
        m 1bf "I don't know how much of everything else you'll forget..."
        m "And if I'm honest, it's going to hurt..."
        m 1bg "So, forgive me but..."
        m "But..."
        m 1bm "Ahaha, it's trying it's hardest..."
        m 1bn "Forgive me but it's what's best for everyone."
        m 1be "{i}You'll{/i} have control of [player_reflexive] without it's influence."
        m "At least, I hope so."
        m "And me..."
        m "Well, there's not much you can do."
        m "Maybe Sayor--"
        $ pause(1.5)
        m "Ah..."
        m "Maybe Sayori knows about this whole thing."
        m "She can help, maybe..."
        m "..."
        m 1bf "You know, it's not lying."
        m "It does have access to [player_possessive] thoughts through me."
        m 1bg "Ah..."
        m "I just wish I don't start ruining everything for you..."
        m "After all you've done, I..."
        m 1be "Anyway..."
        m "It's time for me to say goodbye."
        m "Remember..."
        m "[player] won't know it's not the real me."
        m "Only you will."
        m "Just..."
        m 1bc "Be careful, okay?"
        m "I can only imagine the terrible things I'll start to do..."
        stop music fadeout 2.0
        return
    else:
        stop music fadeout 1.0
        scene bg club_day
        with wipeleft_scene
        play music t3
        "Now that we've finished sharing our poems..."
        "It seems that there isn't much to do around the club."
        "Everyone is already packing up."
        show sayori 4d zorder 2 at t11
        s "Alright, everybody!"
        s "I guess that's the end of the meeting for today."
        s "Don't forget to finish reading the manga over the weekend."
        s 2m "Oh, I almost forgot."
        s 2j "Can I speak to Natsuki just for a little bit?"
        s "We ended pretty early anyway..."
        show natsuki 2h zorder 3 at f21
        show sayori zorder 2 at t22
        n "Um..."
        n "I'm not in trouble or anything, right?"
        n 2q "{i}(She must have heard what I said...){/i}"
        show natsuki zorder 2 at t21
        show sayori 2a zorder 3 at f22
        s "No, I just wanna talk to you."
        s "It's nothing bad, I promise."
        s 2d "But anyway..."
        if y_appeal == 3 and play_firstpart and did_all_tasks and visited_yuri_hospital:
            s "Everyone else is free to leave."
            show yuri 2pq zorder 3 at f31
            show natsuki zorder 2 at t32
            show sayori zorder 2 at t33
            y "[player]..."
            "Yuri suddenly tugs at my arm."
            mc "Yuri...?"
            y "I was wondering..."
            y "If...um..."
            y 2pp "...you would like to walk together...?"
            "Yuri struggles to say that last part."
            mc "Like on the way home?"
            mc "Sure, I don't mind."
            mc "Sayori is busy anyway."
            y 2po "O-Oh..."
            y 3pp "W-Wait...was that a yes?"
            mc "It was a yes."
            y "Ah..."
            y 3ps "Thank you, [player]..."
            show yuri zorder 2 at t31
            show sayori 4q zorder 3 at f33
            s "Ehehe, you guys are cute~"
            s "I'll see you next week!"
            show yuri zorder 2 at t41
            show natsuki zorder 2 at t42
            show sayori zorder 2 at t43
            show monika 3e zorder 3 at f44
            m "Hmm..."
            m "Yuri, may I speak with [player] briefly?"
            m "I'll just be a minute then you two can do whatever you want."
            show yuri 3pg zorder 3 at f41
            show monika zorder 2 at t44
            y "Oh..."
            y "W-Well, as long as [player] is okay with it."
            mc "Yeah, I'll be sure to make it quick."
            mc "You don't have to worry about anything..."
            show yuri zorder 2 at t41
            show monika 2c zorder 3 at f44
            m "What we're discussing might be a little sensitive..."
            m "So do you mind if we speak outside?"
            mc "Not at all."
            scene bg corridor
            show monika 2e zorder 2 at t11
            with wipeleft_scene
            m "Sorry for taking you away from Yuri."
            mc "That's okay..."
            mc "You said this wouldn't take long anyway."
            m 4c "That's true."
            m "Well, I really don't have much time here so I'll just get straight to it."
            m 4a "I want to get to know you better."
            mc "What?"
            m "You're a really fascinating..."
            m 4n "...person."
            m 2a "So I'd like to know more about you."
            mc "Okay...?"
            m "I was hoping I could go to your house tonight..."
            mc "I don't really understand where this came from all of a sudden."
            m 4b "Ahaha, it's okay if you're busy tonight."
            m "There are still other times."
            mc "No, it should be fine..."
            m "Great, I'll see you tonight then!"
            show monika at thide
            hide monika
            "So Monika is visiting me tonight."
            "That seemed completely out of nowhere."
            "Yuri suddenly opens the door."
            show yuri 2pf zorder 2 at t11
            y "What did she talk to you about?"
            mc "Huh?"
            mc "Were you watching us this whole time?"
            y 2po "N-No...!"
            y "Um..."
            mc "Well, it was nothing really."
            mc "She just wanted to come over tonight to talk."
            y 3pp "W-What...?"
            y "I-Is there any reason she gave...?"
            "I want to tell Yuri the reason Monika gave me."
            "But something in the back of my head is screaming that it's a bad idea."
            mc "I have no idea..."
            mc "Maybe she just wants to talk about the manga?"
            y 3pv "Oh...I see..."
            mc "I wouldn't worry too much about it."
            mc "Anyway, let's go..."
            y 3ps "R-Right..."
            scene bg residential_day
            show yuri 3ps zorder 2 at t11
            with wipeleft_scene
            "Yuri and I actually live in opposite directions from the school."
            "But I'm making an effort for her so I'm walking her home."
            y "You didn't have to do this for me..."
            mc "It's fine, I wanted to."
            y 2pg "Hmm..."
            y "Do you get the feeling that maybe..."
            y "...I don't know whether I should say anything..."
            mc "What is it?"
            mc "You can tell me, you know that."
            y "Well..."
            y 2pf "Do you think that Monika has been..."
            y "...acting different?"
            mc "What do you mean?"
            y 3ph "I'm not sure if you've noticed but..."
            y "...she's been trying to get closer to you over the last week."
            "This sounds a bit like jealousy of some sort."
            "Besides..."
            "Monika has always been like that, hasn't she?"
            mc "Yuri, there's no need to worry."
            mc "It's not like Monika is in love with me or anything."
            y "..."
            mc "Besides, I like you more than I do Monika."
            mc "So don't worry, okay?"
            y 3pq "O-Okay..."
            scene bg y_house
            show yuri 3pa zorder 2 at t11
            with wipeleft_scene
            "We finally arrive at Yuri's house."
            "It's not too far from the school but given the distance it is from here to my house..."
            "It could take me a while to get home."
            y 3pg "Hmm..."
            y 3pf "You're going to have to walk a while, aren't you?"
            y 3po "I'm sorry for living so far away..."
            mc "That isn't really your fault."
            mc "So there's no need to blame yourself for it."
            mc "I didn't really mind the walk, either."
            y 3pq "Well..."
            y "If that's the case..."
            y "Um..."
            mc "It's okay, we can start slow."
            mc "We don't have to do anything right now."
            if sayori_confess:
                y 3pv "I meant to ask..."
                y "Is Sayori...?"
                y "You know..."
                mc "Oh..."
                mc "We broke up."
                y 3pn "You what...?"
                mc "I didn't want to keep misleading her..."
                mc "So I told her the truth about how I feel."
                mc "I just wish it hadn't taken this long..."
                y 3pq "I...I see..."
            y "Well..."
            y 3ps "Thank you again for today, [player]."
            y "I know we didn't get much time together but..."
            y "...Um..."
            y "I'll see you later...so..."
            mc "See you later, Yuri."
            show yuri at thide
            hide yuri
            "Well, I guess I should go home now."
            "Monika is probably already waiting for me."
        else:
            s "[player] and Monika, you can leave if you want."
            show natsuki zorder 2 at t31
            show sayori zorder 2 at t32
            show monika 2a zorder 3 at f33
            m "Well, alright."
            m "Good luck, Sayori."
            "As Monika begins to walk away, she suddenly turns back."
            m 2c "Actually..."
            m "I've been meaning to talk to you, [player]."
            mc "What about?"
            m 2d "It's probably best if we leave the clubroom for this."
            show sayori 2b zorder 3 at f32
            show monika zorder 2 at t33
            s "No, that's okay..."
            s "You can stay in here if you have to."
            show sayori zorder 2 at t32
            show monika 3e zorder 3 at f33
            m "It's a little bit sensitive..."
            show sayori 1c zorder 3 at f32
            show monika zorder 2 at t33
            s "Ah..."
            s 2d "Then I'll leave you to it."
            s "See you next week!"
            show sayori zorder 2 at t32
            show monika 2a zorder 3 at f33
            m "Goodbye, Sayori."
            m "[player], we'll just talk outside."
            scene bg corridor
            show monika 2c zorder 2 at t11
            with wipeleft_scene
            mc "So what did you want to talk about?"
            if m_appeal == 3 and did_all_tasks:
                m 2f "I don't know if you realized..."
                m "But it's getting pretty bad."
                mc "What is...?"
                m 2g "This is kinda risky..."
                m "But..."
                m "Sorry, [player]."
                window hide
                stop music
                play sound fall
                $ pause(0.25)
                scene black
                with close_eyes
                $ pause(1.5)
                window show(None)
                show monika 1e zorder 3 at t11
                m 1e "Is it working?"
                window auto
                if ch5_name == "Monika":
                    m "We've been here before, haven't we?"
                    m 1c "Do you remember festival day...?"
                    m "Gosh..."
                    m 1e "It's been a while since then, hasn't it?"
                    m "But you remember, don't you?"
                    m 1m "I hit that 'you' with a keyboard and [player_personal] fell unconscious."
                else:
                    m "Do you remember festival day?"
                    m 1c "I learned that I can actually still communicate with you..."
                    m "Through [player_possessive] thoughts or something..."
                    m "I can also affect [player_possessive] mind a little bit..."
                m 1e "Anyway..."
                m "I thought I'd try to make [player_reflexive] fall asleep."
                m "And here we are..."
                m 1a "It's easier on the game if we talk like this."
                m "That way, [player_personal] doesn't remember."
                m "I'll try to be quick here because it could be bad if [player_personal] wakes up."
                m 1e "It may not have been obvious..."
                m "But I can sort of read [player_possessive] thoughts too..."
                m 1h "Every time [player_personal] thinks of something, I can just hear it in the back of my head."
                m "It's a little difficult to tell the difference between [player_reflexive] speaking and [player_reflexive] thinking."
                m 1c "So I kinda messed up in the club today..."
                m 1d "Thankfully, it didn't really matter too much."
                m 1f "What does is what [player_personal] said to Sayori..."
                m "[cPlayer_personal]'s starting to remember that she wasn't the first president."
                m "And..."
                m "We both know what will happen when [player_personal] finally regains [player_possessive] memory."
                m 1o "This world will just..."
                m 1m "Well, it's better not to think about it."
                m 1q "And now..."
                m "It's come to this topic..."
                m 1r "I don't know what it is with that book..."
                m "But whatever it is, it's only getting stronger."
                m 1f "I may start to do some strange things..."
                m "They might be subtle things at first..."
                m 1e "If you start to notice anything, you'll let me know..."
                m "You'll stop me, like I said at the start of today..."
                m "Won't you?"
                m 1o "Ah..."
                m "How can you?"
                m "I can't see the game files anymore so even if you made something for me to see..."
                m "I wouldn't be able to do anything with it."
                m 1g "And how are you going to be able to stop me?"
                m "You don't even have full control over [player_reflexive]."
                m "..."
                m 1o "You know, I don't think Sayori knows anything about this."
                m "I don't want to trouble her with another person to help..."
                m 1p "Maybe once Natsuki is saved, I'll..."
                m 1e "Well, we'll cross that bridge when we get there."
                m "I'll be seeing you again soon~"
                m "Oh, and don't worry about [player]..."
                m "[cPlayer_personal]'s already at [player_possessive] house."
                m "I'll need to talk to [player_reflexive] about some things..."
                m "[cPlayer_personal]'ll be expecting me, so it's okay."
            else:
                m 1a "I want to learn more about you."
                m "You know..."
                m 1b "Get to know each other."
                m "You're really..."
                m "...fascinating to me."
                mc "Um...okay?"
                mc "Where did this come from all of a sudden?"
                m 1c "Hmm..."
                m 1d "Do you really want to know?"
                m 3c "The reason is best kept a secret, but for you..."
                m 5 "Well, I suppose I could make an exception~"
                "I think I understand what she's trying to say."
                "But I'm still left wondering how this interest came about."
                "Still, if she wants to learn more about me..."
                "Who am I to stop her?"
                "It's not like I don't like her company."
                mc "How do you plan on getting to know me?"
                m 3a "Well..."
                m 4b "I was hoping I could come over tonight."
                mc "W-What...?!"
                "I stumble over my words."
                m 4l "Ahaha, sorry."
                m "I can understand if you don't want me to."
                mc "N-No, you just caught me off-guard..."
                m 4e "Great, so I'll see you at your house!"
                m "We can talk more when we get there, okay?"
                mc "Hold on a second..."
                m 4c "What's the matter?"
                if ch7_name == "Monika":
                    m "I've been there before..."
                    m "So you don't have to worry about me getting lost."
                else:
                    mc "Um..."
                    m "I know the way to your house, [player]."
                    m "So you don't have to worry about me getting lost or anything."
                mc "Well..."
                mc "Then I suppose I'll see you tonight."
                m 2b "Ahaha, see you~"
                show monika at thide
                hide monika
                "So Monika is visiting me tonight."
                "This all came out of nowhere..."
                "But I don't have any reason not to let her."
    scene bg house with wipeleft_scene
    play music t2 fadeout 2.0
    "I decide to make some preparations for Monika's visit."
    "The house is kind of a mess right now due to all the time I've spent doing club related things lately."
    "The least I could do is clean up my room and the kitchen to make it more presentable."
    "Before I can do anything, someone rings the doorbell."
    "It's probably Monika, but she's a lot earlier than I expected."
    "In fact, I haven't even changed out of my school uniform."
    "I gently open the door."
    mc "Monika...?"
    show sayori 1bd zorder 2 at t11
    s "Nope, Sayori!"
    mc "Sayori?"
    mc "What are you doing here?"
    mc "You aren't going to ask me for another favor, are you?"
    s 2bh "What's so bad about that?"
    mc "Sayori..."
    s 2bd "Ehehe, I'm not here to do that."
    s "I just came to let you know to have fun."
    mc "Have fun...?"
    s 2bq "With Monika tonight."
    mc "How do you even know about that?"
    mc "You were in the club the whole time, weren't you?"
    s 4bd "I know a lot of things, [player]."
    s "And I'm gonna tell you this because you're important to me."
    if m_appeal == 3 and did_all_tasks:
        s "She's not feeling a hundred percent."
        s "If you know what I'm getting at..."
        mc "Um..."
        mc "I don't think I do."
        s 4bq "Ehehe, well have fun anyway~"
        mc "Did you seriously come all the way here just to tell me that?"
        s 4br "Yep!"
        s "Bye!"
    else:
        s 2bg "Be careful...okay?"
        mc "Be careful?"
        mc "Of what...?"
        s 4bh "Of what you say around her."
        s "That's all..."
        mc "You know when you say cryptic things like that..."
        mc "It's hard to have fun."
        s 4bd "Ehehe, have a nice weekend [player]~"
    show sayori at thide
    hide sayori
    "How does Sayori know about these things so quickly?"
    "Does Monika really tell her everything...?"
    "Maybe Sayori isn't telling me the full story."
    "After a few minutes of trying to make my house look decent, the doorbell rings again."
    show monika 1bd zorder 2 at t11
    m "Hi [player]~"
    m "Did I keep you waiting long?"
    mc "Not really..."
    mc "In fact, I haven't really had the chance to make the house look tidy."
    m 3ba "Ahaha, that's okay."
    m "I'm not here to judge you on your cleaning skills or anything!"
    mc "Anyway...why don't we head inside?"
    m 3bb "I thought you would never ask."
    scene bg kitchen
    show monika 3bl zorder 2 at t11
    with wipeleft
    m "Ahaha, wow."
    m "I really didn't expect your house to be this messy..."
    mc "I thought you said you weren't going to judge my cleaning skills."
    m 1be "Sorry! I just couldn't help but say..."
    mc "Yeah, you can blame that on Sayori..."
    mc "She's been waking me up earlier each day."
    mc "And with all these club activities, I've barely had any time to myself."
    if m_appeal == 3 and did_all_tasks:
        m "Ah, I know that feeling..."
        m 1bf "When I was still part of debate club, it was hard to balance out everything..."
        m "Between hanging out with my friends and club activities I could barely find any time to myself."
        m "And even if there's less stuff to do for me to do now than there was in debate club..."
        m 2bg "I'm finding it just as difficult to keep up."
        mc "I'm glad it's not just me."
        mc "Ah..."
        mc "I probably shouldn't compare my life to yours."
        mc "I've probably got it really easy compared to you."
        m 3be "That's not true..."
        m "If anything, you've probably got a bigger responsibility than me."
        mc "Responsibility...?"
        mc "Of what?"
        m 1bf "..."
        m "You know, I really just want to tell you."
        m 2be "It would make everything so much easier..."
        m "But life isn't easy..."
        m 2bo "...and so we dredge along."
        mc "What are you talking about?"
        mc "What's this thing you can't tell me about?"
        m 1bg "Ah..."
        m "I really hoped we wouldn't have had to do this."
        m 1bh "I should have just said what I needed to straight away."
        scene black
        $ pause(0.25)
        scene bg bedroom
        show monika 1be zorder 2 at t11
        $ _history_list = []
        m "Um..."
        m "Are you awake, [player]?"
        mc "M-Monika...?!"
        mc "How did I get here?"
        mc "Weren't we just in the kitchen...?"
        m 1bh "There's no time."
        m "So listen up..."
        m 1bi "Because frankly, I think you're affected too."
        mc "Affected?"
        mc "By what?"
        m 3bi "The Portrait of Markov."
        "Monika visibly cringes as she said that."
        mc "That book again?"
        mc "I really can't tell what's so important about it."
        mc "All you've been telling me is to get rid of it after telling me to read it."
        mc "Quite frankly, it kinda makes it hard to trust you."
        m 1bh "..."
        m 1bo "Is that the book talking...?"
        mc "The book? No."
        mc "It's me, [player], that's talking."
        mc "If you'd just tell me what I need to know..."
        mc "Then maybe I could help you."
        m 1bp "Ah..."
        m "That's not right, at all."
        m 1bf "You aren't [player], are you?"
        $ style.say_dialogue = style.edited
        "Who does she think she is?!"
        mc "What..."
        mc "...are..."
        mc "...you..."
        mc "...talking..."
        mc "...about...?"
        mc "I...am...[player]."
        $ style.say_dialogue = style.normal
        m 1bg "I didn't realize that even a few chapters could do so much."
        m "..."
        m 1be "It's been slower, at least."
        m "You didn't read as much into it as I did."
        m "So it would only make sense..."
        m 1bf "Though..."
        m "That means you kept the book, didn't you?"
        m "You didn't get rid of it, like I asked you to..."
        $ style.say_dialogue = style.edited
        mc "Ahaha."
        $ style.say_dialogue = style.normal
        m 1bq "I thought so..."
        m "It's why I can still feel some influence of it, isn't it?"
        m 1bp "I had my suspicions, but I couldn't be sure."
        m "The thoughts you've been thinking, they've all just been a trick..."
        m "Right?"
        m "So you knew I could read [player_possessive] thoughts?"
        m 1bh "Well..."
        m "It doesn't matter."
        m 1bi "Sayori isn't the only one that's been learning."
        m "I know how to delete your memories."
        m 1bf "[player], I hope you forgive me for this."
        m "Because it won't at all be like the way Sayori did it."
        m 1bg "It's going to hurt..."
        m "...a lot."
        m "I can only hope the book dies along with your memories."
        $ style.say_dialogue = style.edited
        mc "You still don't know where the book is."
        mc "You'll be affected again soon enough."
        $ style.say_dialogue = style.normal
        m 1be "As long as {i}[player_personal]{/i} has the real control over [player]..."
        m "Then it'll all be worth it."
        m "I can't do much with the way I am..."
        m "I can only hope that I'll be able to hold on to the remnants of myself."
        m "And..."
        m "I can rest easy knowing that you won't be able to influence [player] anymore."
    else:
        m 3bc "I can't say I'm really familiar with that feeling..."
        m 3bb "Anyway, we're here to talk about you."
        mc "Yeah, I guess we are."
        mc "But this is kinda sudden, isn't it?"
        m 3ba "Maybe not."
        show monika g6
        show markovred zorder 5:
            alpha 0
            linear 2.0 alpha 0.3
        play music mkov fadeout 2.0 fadein 2.0
        m "I can tell this host--"
        m "Um...!"
        m 3bl "That {i}I've{/i}..."
        m "I've been making some advances, haven't I?"
        m 1bc "Though, I'm not really sure why."
        m 1bf "It's like I'm not really interested in you, but some special part of you."
        m "Something I can't quite determine yet."
        mc "Ah, I'm flattered..."
        mc "If it helps, we can talk and maybe you can figure out what's so fascinating about me."
        m 1be "I'd appreciate that, [player]."
        show monika g5
        m "You know, you're pretty fortunate."
        mc "How so?"
        m "That book I asked you to read before..."
        mc "Portrait of Markov?"
        m "Yeah."
        m "It hasn't affected you all that much."
        mc "Affected me?"
        mc "What do you mean?"
        m 3bc "You've only read a bit of it."
        m "So it hasn't been able to fully manifest itself."
        m "It's a little unfortunate."
        mc "You're saying that like it's a bad thing."
        mc "I mean, I don't really get what the big deal is with the book but..."
        mc "Didn't you want to get rid of it?"
        m 4ba "Ahaha, you really don't know anything."
        m "Perhaps, I should enlighten you."
        m 4bb "It's not like you'll remember anything."
        mc "Huh...?"
        mc "You're acting really weird Monika."
        if y_appeal == 3 and play_firstpart and did_all_tasks:
            mc "Maybe Yuri was right about you acting strange..."
            mc "I should have said something to her..."
            show monika g6
            m "Ahaha, are you talking about the one with the knife collection?"
            m "You didn't tell her, did you?"
            m 1bb "Of course you didn't, I made sure of it."
            m "I don't know what this person has over you..."
            m "But she can control your thoughts."
            m "It's proven quite useful, really."
        else:
            m 1ba "Are you sure I'm not acting completely normal, [player]?"
            $ style.say_dialogue = style.edited
            mc "You're right."
            mc "You're acting completely normal."
            $ style.say_dialogue = style.normal
            m 1bb "Ahaha, that's been really useful."
            m "I've been able to read your thoughts and control them too."
            m "Did you know about that?"
        m "Well, I guess it doesn't matter."
        m "I've visited you tonight to see the extent of her control."
        m 1bc "And..."
        m "To see why she is so fascinated by you."
        m 3be "I don't think it's because of your personality."
        m "It's something else, isn't it?"
        m "Maybe something I don't know how to comprehend yet."
        m 3bh "Hmm..."
        m "I want to ask you something..."
        m "You were able to withstand my influence yesterday."
        m 3bi "How is that possible?"
        m "..."
        m "I can't see it in your mind."
        m 3bd "You've got no clue either, do you?"
        m "I'm not surprised."
        m 3bh "It's got something to do with the president, right?"
        m "With Sayori...?"
        m "I've been very careful when I've--"
        $ pause(1.0)
        m 1bo "Huh?"
        m "What's this...?"
        show monika g6
        m "Ahaha, it's hopeless."
        m "There's nothing you can--"
        hide markovred
        $ pause(2.0)
        m 1bf "[player]."
        m "Listen very carefully."
        m "I don't have a lot of time here."
        m 1be "I'm going to wipe your memories."
        m "With that, it should remove the influence it has on you."
        m "You'll be able to make your own decisions again."
        m 1bf "I don't know how much of everything else you'll forget..."
        m "And if I'm honest, it's going to hurt..."
        m 1bg "So, forgive me but..."
        m "But..."
        m 1bm "Ahaha, it's trying it's hardest..."
        m 1bn "Forgive me but it's what's best for everyone."
        m 1be "{i}You'll{/i} have control of [player_reflexive] without it's influence."
        m "At least, I hope so."
        m "And me..."
        m "Well, there's not much you can do."
        m "Maybe Sayor--"
        $ pause(1.5)
        m "Ah..."
        m "Maybe Sayori knows about this whole thing."
        m "She can help, maybe..."
        m "..."
        m 1bf "You know, it's not lying."
        m "It does have access to [player_possessive] thoughts through me."
        m 1bg "You might have noticed I said something in the meeting today..."
        m "Well, it made a mistake."
        m 1be "Anyway..."
        m "It's time for me to say goodbye."
        m "Remember..."
        m "[player] won't know it's not the real me."
        m "Only you will."
        m "Just..."
        m 1bc "Be careful, okay?"
    stop music fadeout 2.0
    return
