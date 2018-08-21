label ch13_main:
    scene black
    show sayori 1b zorder 2 at t11
    with dissolve_scene_full
    play music mend fadeout 2.0
    s "I want to say that I don't really know what's going to happen today."
    s 1c "I know I made the day and everything but {i}something{/i} is changing it..."
    s "I don't know if that makes any sense to you, but it's making my ability to see into the future kinda useless."
    s 1d "Maybe it's just the game glitching out from too many days or something."
    s "Or maybe I just can't see what's going to happen..."
    s 1c "Who knows?"
    s "I could ask Monika about it but..."
    s 1d "Never mind."
    s "Anyway, I should probably tell you that I changed the poem game a little."
    s "Your poem doesn't really matter anymore."
    s "After yesterday, I didn't really see the point."
    s "Seeing as everyone already knows the type of style you're writing."
    s 1b "There was also this weird thing that was in the poem game script."
    s "I'm not really sure how to describe it but it had something to do with Monika..."
    s "Oh well, it's gone now so don't worry about it."
    s "I might just ask Monika if she knows what that is about."
    s 1q "But yeah...your poems don't really matter anymore!"
    if n_appeal >= 4 and (ch12_outcome == 3 or ch12_outcome == 1):
        s 1l "Um...actually, that's not completely true."
        s "If you're still trying to make [player] go for Natsuki..."
        if sayori_confess:
            s 1k "...even after what you made [player] say to me a long time ago..."
        s 1h "...then your poem does matter a little bit."
        s "So if you really are going for her, then you should make sure that your poem is written for her...okay?"
        s "You'll see what I mean later today."
        s "Speaking of which..."
    else:
        s "Anyway..."
    s 1d "I want to talk about what happened with Natsuki."
    if ch12_outcome == 3:
        s "She's got her mom back and her dad is back to normal."
        s "Whatever normal means..."
        s 1g "I can't help but feel there's something wrong with what we did."
        s "Like...do you ever think that the ending we gave her feels..."
        s "...oh, I don't know, artificial maybe?"
        s 1h "Is it really right to give Natsuki her mom back?"
        s "..."
        s "I guess what's done is done, isn't it?"
        s 1k "It is the best outcome, it just feels wrong for some reason."
        s "Bringing someone back from the--"
        s "Never mind..."
        s 1d "As long as Natsuki is happy..."
    elif ch12_outcome == 2:
        s "She's got her mom back and her dad is..."
        s 1g "Well, not with Natsuki."
        s "When I asked Haruki what she was going to do with him yesterday, I think she said something about calling the police."
        s "I guess that's probably the best way to handle it, isn't it?"
        s 1k "I don't really feel sorry for Yasuhiro or anything but I feel like we did something wrong."
        s "Like what Natsuki is feeling isn't real...does that make sense?"
        s "I mean we gave her back her mom but..."
        s "...I don't know what to think about this whole thing."
        s "I know I was the one who told you to bring her back..."
        s "..."
        s 1d "Well, it doesn't matter. As long as Natsuki is happy."
    elif ch12_outcome == 1:
        s 1c "So...what do you think about this whole thing?"
        s "Natsuki has her dad caring for her again, like a proper parent should."
        s 1k "I don't know if things between them will ever be the same, especially since..."
        s "...{i}you know{/i}, is still missing."
        s "It's better this way, isn't it?"
        s "It's more natural than bringing back a dead person, right?"
        s 1h "I mean, who are we to decide if someone should live or die?"
        s "Oh...sorry."
        s 1l "I got a bit too philosophical there, didn't I?"
        s 1d "I just hope Natsuki does end up happy, in the end."
    else:
        s 1c "So...this is an interesting end for her."
        s "She lives by herself now."
        s 1h "Yasuhiro is in jail while he's being investigated."
        s "Who knows how long he'll be in there for but with the evidence we have..."
        s "Well, he won't be getting out anytime soon."
        s 1k "I have to wonder..."
        s "Can she really be happy like this?"
        s "I don't know the answer to that question."
        s 1d "I guess the best thing we can do it support her through this time..."
        s "...and maybe she'll learn to be happy again."
    if s_appeal >= 4:
        s 1k "I've been meaning to say..."
        s "There's this feeling in my body."
        s "We set out to solve Natsuki and Yuri's problems, right?"
        s "But..."
        s "I feel like there's something else."
        s 1f "Like there's someone we haven't really helped yet."
        s "I have to think about this."
        s "See you, [player]."
    elif monika_type == 0:
        s 1k "So everything is okay, right?"
        s "I mean..."
        s "We have solved everyone's problems, haven't we?"
        s 1d "Yuri is feeling better, she isn't as shy anymore and she opens up to other people easier."
        s "It'll take time for her to really change for the better but..."
        s "...it's progress."
        s "Natsuki has her dad problem dealt with."
        s 1l "However we did it, we solved her problem even if it might not have been the best way."
        s 1c "And Monika...well, she was first."
        s "There's just..."
        s 1k "No..."
        s "I can't think about that."
        s "There's nothing wrong, there's nothing left to fix."
        s 1g "Um..."
        s "Sorry, I have to go."
    else:
        s "So I've been thinking..."
        s 1l "There's nothing we really need to do today."
        s "Everyone is sorta happy, right?"
        s 1d "I mean you {i}have{/i} helped everyone."
        s "You gave Monika a chance, you helped Yuri and Natsuki with their problems..."
        s "So why do I still feel like there's something missing...?"
        s 1c "Maybe..."
        s 1k "No, I can't think like that."
        s "It's far too selfish..."
        s "Goodbye."
    stop music fadeout 0.5
    scene bg residential_day
    with dissolve_scene_full
    play music t2 fadein 1.0
    "After what happened yesterday, I felt bad for not checking up on Natsuki."
    "Sayori told me that she has it handled but I'm still a little worried."
    "I was expecting Sayori to come over to my house and tell me to wake up."
    "Instead, she told me she had to take care of some \"final preparations\" this morning."
    "I don't know what she meant by that but it means I have to walk to school by myself."
    "I had to walk by myself yesterday..."
    "I just hope this walking by myself thing doesn't go on for much longer."
    "It's not really a big issue, it's just that..."
    "It's always better walking to school with someone close to me."
    "There was more we could talk about and it made the journey less boring."
    "I wonder what final preparations Sayori is doing."
    "It must be something for the club."
    "Still, having this time for myself let's me think about what I've done."
    "All the decisions I've made in the past and how I could have changed them."
    scene bg class_day
    with wipeleft_scene
    "The school day is over before I know it."
    "Yet I'm still left wondering what I could have done better in the past."
    "Why am I thinking like this?"
    "Is it because of what happened to Natsuki?"
    "Maybe she could have gotten a better ending..."
    "I know it's almost time for the club meeting..."
    "But I really need some more time for myself."
    scene bg school_front
    with wipeleft_scene
    "I start wandering the school."
    "I don't really have anywhere in particular I want to go, but I make sure I'm relatively close to the Literature Club."
    "Thinking about it deeper..."
    "There's been some things that have happened that I've forgotten."
    "That I really shouldn't have forgotten."
    "The events of the first week in the Literature Club."
    "How did it go...?"
    stop music fadeout 2.0
    scene bg residential_day_gray
    show sayori 4p_gray zorder 2 at i11
    show vignette zorder 100
    with dissolve_scene_full
    play music "<loop 4.444>bgm/5.ogg" fadein 1.0
    $ style.say_window = style.window_flashback
    "It all started that Monday morning when Sayori started waving her arms at me."
    "She caught up to me that morning insisting I join a club."
    "I think she said it was to give me some social skills...or something."
    "I told her that I'd look at a couple of clubs, just to make her happy."
    "Then we went on with our day."
    "Eventually...I did join the Literature Club."
    "And it all started because of some cupcakes Sayori promised me."
    "Was that really the only reason I ended up going to the Literature Club?"
    "And who knew that I would have ended up staying for real?"
    scene white with dissolve_cg
    scene bg club_day_gray
    show monika 5a_gray zorder 2 at i11
    show vignette zorder 100
    with Dissolve(1.5)
    "Monika was the one who welcomed me on my second day as a member of the Literature Club."
    "I wrote all of my poems for her back then but now I'm not really sure why."
    "Was I just trying to impress her?"
    "Maybe it was because of her smile."
    "There was another reason, wasn't there?"
    "It was really important...I knew I had the option to write for the others, but I always chose Monika."
    "I must have forgotten the real reason."
    "But why does it feel like Monika was more important..."
    "At least...during this time."
    "Well...there has to be more to it."
    scene white with dissolve_cg
    scene bg residential_day_gray
    show monika 2p_gray zorder 2 at i11
    show vignette zorder 100
    with Dissolve(1.5)
    "Then Monika told me that Sayori was feeling depressed."
    "That really took me by surprise..."
    "My best friend was depressed and I didn't even know about it."
    "How could I have been so blind back then?"
    "But..."
    "There's something else that I can't help but wonder about."
    "I seem to have forgotten how Monika knew about Sayori's depression in the first place."
    "It's not like she knew Sayori better than I did...did she?"
    "In any case..."
    "She told me to visit Sayori on Saturday, and I did."
    "Both of them were at Sayori's house on Saturday."
    "I made sure that Sayori was feeling better, and I assured her that everything was going to be okay."
    "I would do anything to make sure my best friend was okay."
    "Then came along Sunday..."
    scene white with dissolve_cg
    scene bg house_gray
    show sayori 4bl_gray zorder 2 at i11
    show vignette zorder 100
    with Dissolve(1.5)
    "I wasn't really prepared for what happened next."
    "Sayori was suddenly feeling a lot better."
    "It's almost like being with Monika got rid of her depression overnight."
    "I could tell she was genuinely happy again."
    "I guess that's what got her to confess her love to me..."
    "Being the person I was..."
    if sayori_confess:
        "I accepted her confession."
        "I told her I loved her."
    else:
        "I told her she would always be my dearest friend."
    "I didn't know how she would react to that..."
    "In the end, she said she wanted things to stay the same between us despite what was just said."
    "I didn't want to argue against her...especially after that."
    scene white with dissolve_cg
    scene bg house_gray
    if ch4_name == "Yuri":
        show yuri 2bq_gray zorder 2 at i11
    else:
        show natsuki 2bj_gray zorder 2 at i11
    show vignette zorder 100
    with Dissolve(1.5)
    "After Sayori's confession, I remember [ch4_name] came over to do some preparations."
    "I don't really remember what the preparation was for..."
    "Which, for some reason, is really bothering me."
    if ch4_name == "Yuri":
        "But I do remember making a banner with her."
        "We spent most of the day on it and I think it turned out pretty well."
        "The atmosphere we created for...something was going to be great..."
    else:
        "But I do remember baking with Natsuki."
        "It was an experience that I would never forget."
        "Who knew baking was so much more fun with another person?"
    "Spending the day with [ch4_name] was probably one of best things of the first week."
    "It let me get closer to her and learn a bit more about her."
    "But then..."
    scene white with dissolve_cg
    scene bg house_gray
    show monika 1bm_gray zorder 2 at i11
    show vignette zorder 100
    with Dissolve(1.5)
    "Monika showed up."
    "Why did she suddenly appear at my door?"
    "I don't remember what she said."
    "It must have been something important."
    "I have to think hard to remember."
    "..."
    "What did she..."
    $ currentpos = get_pos()
    $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_monika.ogg"
    stop music fadeout 1.0
    $ renpy.music.play(audio.t5b, channel="music_poem", fadein=1.0, tight=True)
    m "Before I disappear forever. Just try not to remember me as..."
    m "The selfish president."
    m 1bj_gray "But just the good things about me, okay?"
    m "Just..."
    m 1be_gray "...Just Monika."
    $ currentpos = get_pos("music_poem")
    stop music_poem fadeout 1.0
    play music "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg" fadein 1.0
    "What does that mean?"
    "Why was she even saying that?"
    "She helped me with Sayori so why did it sound like she was saying goodbye...?"
    "Why can't I properly remember what happened?"
    "And why would I remember her as \"the selfish president\" when Sayori is the president of the Literature Club...?"
    "Though I have to wonder..."
    "Was Monika actually the president--{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    scene bg corridor
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    $ style.say_window = style.window
    $ _history_list = []
    play music t2
    if ch12_markov_agree:
        $ persistent.markov_agreed = True
        $ renpy.save_persistent()
        python:
            try: renpy.file(config.basedir + "/the die is cast")
            except: open(config.basedir + "/the die is cast", "wb").write(renpy.file("the die is cast").read())
    "I think I'm the last one to get to the Literature Club today."
    window auto
    "I guess I shouldn't have spent so much time wandering the school yard."
    if visited_yuri_hospital:
        show yuri 3pq zorder 2 at t11
        y "Ah, [player]."
        "Yuri appears in front of me."
        "She looks a little anxious."
        y "You're finally here."
        mc "Yuri?"
        mc "What are you doing out here?"
        y 3pa "I could be asking you the same question."
        mc "I had to think about a couple of things for a while."
        mc "I guess I just lost track of time."
        mc "What's your reason?"
        y 3ps "Well...I was out looking for you."
        y "I thought you'd be in the club but you weren't..."
        y "We waited a while and you didn't come..."
        y "...so I was going to try to find you."
        mc "Well, I'm here now."
        mc "Sorry if I worried you."
        y "N-No, that's okay."
        y 3pf "Besides...I don't think Natsuki is here yet either."
        mc "Oh...do you know where she is?"
        y 3ph "I have no idea."
        mc "I suppose Sayori will tell us, if she knows."
        y 3pq "A-Anyway, we should head inside before we waste anymore time."
    elif monika_type == 0:
        show monika 1a zorder 2 at t11
        m "Oh, hi [player]~"
        "Monika appears in the corridor outside the club."
        mc "Monika? Why are you so late?"
        m 3b "Ahaha, I could be asking you the same question!"
        mc "I guess I just lost track of time."
        mc "I had a lot I needed to think about."
        m 3c "Oh, I see."
        mc "What about you?"
        mc "I didn't expect you to be late as well."
        m 4a "Well...I had a piano lesson."
        m "I asked the tutor if he would teach me for a bit longer."
        m 4e "Because I haven't really been practicing as much lately."
        mc "Is it for anything in particular?"
        m 2c "Hmm...maybe."
        m "I'm not too sure on the details yet, but I've got something in mind."
        mc "I'd love to hear you play that song you talked about in the first week."
        mc "I mean you must have a decent amount of practice now, right?"
        show monika 2a
        "Monika smiles."
        m "I'm certainly getting better, I think."
        m "I'd be happy to let you and the others hear me play, when the time is right."
        mc "I can't wait."
        m 4b "Anyway, we should get inside."
        m "We've kept the others waiting for long enough."
    elif ch12_markov_agree and monika_type == 1:
        show monika 1ha zorder 2 at t11
        m "Hi [player]~"
        "It's Monika, but..."
        "...she's not wearing her white ribbon and her hair is down."
        m 3hb "I suppose you're late too?"
        mc "A-Ah, I guess."
        m 3hc "What's the matter? You seem kinda shocked."
        mc "I'm a little surprised at your new look, that's all."
        "Monika looks at her herself."
        m 4hb "Oh, this?"
        m 4he "Yeah...I thought I would change it up a little."
        m "We can talk about it later."
        mc "Alright..."
        m 2ha "So why aren't you in the club yet?"
        m "Ahaha, I thought I would be the late one~"
        mc "I had to think about a few things."
        mc "I guess I just lost track of time."
        m 2hc "I see..."
        mc "What's your reason?"
        m 4ha "Well, I was practicing piano and asked for a slightly extended lesson from the tutor."
        m "I just want to get better faster, you know?"
        mc "Any reason in particular?"
        m 2hb "Maybe~"
        mc "I'd love to hear you play that song you talked about in the first week."
        m 2he "Maybe when the time is right, [player]."
        m "For now, we should get to the meeting. We've probably kept them waiting long enough."
    else:
        show monika 1c zorder 2 at t11
        m "[player]?"
        "Monika stands in front of me, just outside the clubroom."
        m "Why aren't you in the club already?"
        mc "Ah--"
        m 1h "Actually, don't answer that."
        m "{i}Your{/i} business is not my concern."
        mc "Alright..."
        mc "Well, what are you doing out here?"
        m 1c "I had a few matters I needed to attend to."
        m "I had a piano lesson for one."
        mc "Is that all...?"
        m 2d "Well, I'd rather not tell you the rest."
        m "It's quite personal, if I'm honest."
        mc "I won't pry then."
        m 2a "Good. Let's head inside before we waste anymore time."
    scene bg club_day
    with wipeleft_scene
    show sayori 1b zorder 2 at i32
    if visited_yuri_hospital:
        show monika 1a zorder 2 at i31
    else:
        show yuri 1a zorder 2 at i33
    show sayori 1c zorder 2 at f32
    if visited_yuri_hospital:
        s "[player], where have you been?"
        s "Yuri even went out to look for you because you took so long..."
    else:
        s "What took the two of you so long?"
        s "We've been waiting here for ages."
    show sayori zorder 2 at t32
    if visited_yuri_hospital:
        show yuri 2pq zorder 3 at f33
        y "S-Sayori, it's fine."
        y "It wasn't a big deal, really."
        y "You should just start the meeting."
    elif monika_type == 0:
        show monika 3b zorder 3 at f31
        m "Sorry! I had a piano lesson that went for a little longer than usual."
        m "And [player] was..."
        m "Um..."
    elif ch12_markov_agree and monika_type == 1:
        show monika 2hb zorder 3 at f31
        m "Sorry for that. I had a piano lesson I went to."
        m "It went for slightly longer than usual, so that's why I'm late."
        m "As for [player]..."
        show monika zorder 2 at t31
        show sayori 1m zorder 3 at f32
        s "W-Wait a second..."
        s "Before any of that...what did you do to your hair?"
        s 2o "It's...different!"
        show monika 2hj zorder 3 at f31
        show sayori zorder 2 at t32
        m "Ahaha, you noticed?"
        m "You're quite sharp, Sayori."
        m "I actually decided to wear my hair down today..."
        m 2he "Because..."
        "Monika looks at me and winks."
        m "Well, just because~"
    else:
        show monika 1c zorder 2 at f31
        m "I had a few things I needed to deal with."
        m 2a "Sorry, if I'm late but it was important."
        m "I don't know about [player] though..."
    show monika zorder 2 at t31
    mc "Sorry, Sayori."
    mc "I just had a lot on my mind and I guess I lost track of time."
    mc "It won't happen again."
    show sayori 2b zorder 3 at f32
    s "Alright, if you say so..."
    "Sayori points to the second empty seat around the table."
    s 2d "As you can probably tell, Natsuki isn't here today."
    s "She told me on the phone yesterday that she was going to take the day off."
    s "She didn't need to give me a reason..."
    s 2k "It's pretty obvious, isn't it?"
    show sayori zorder 2 at t32
    mc "Yeah, I think I understand."
    show sayori 2a zorder 3 at f32
    s "Anyway..."
    s "She isn't here but I was going to suggest not doing one of those book-reading things anymore."
    s "I don't really want to pressure Natsuki too much."
    show sayori zorder 2 at t32
    show yuri 2pf zorder 3 at f33
    y "So what do you suppose we do then?"
    show sayori 4q zorder 3 at f32
    show yuri zorder 2 at t33
    s "Actually, I was gonna ask you guys!"
    s "We don't really {i}need{/i} to do anything."
    s "Especially since I've already done what I set out to do."
    show sayori zorder 2 at t32
    show yuri 2ph zorder 3 at f33
    y "Huh?"
    y "What did you set out to do, Sayori?"
    show sayori 4r zorder 3 at f32
    show yuri zorder 2 at t33
    s "To make you all happy, of course!"
    s "Or at the very least, try to make you feel better."
    show sayori zorder 2 at t32
    show yuri 2pe zorder 3 at f33
    y "Feel better in terms of what..?"
    y "You're being a little bit vague."
    show sayori zorder 3 at f32
    show yuri zorder 2 at t33
    if (sayori_confess and not sayori_dumped) or s_appeal >= 4:
        s 1k "Actually...maybe I'm not finished yet."
        s "There's still a couple of things I have to do."
        s 1d "I hope I will be soon though."
    else:
        s 1d "Never mind what I said, Yuri."
        s "I'm really just thinking out loud."
    show sayori zorder 2 at t32
    if monika_type == 0:
        show monika 3b zorder 3 at f31
        m "There's nothing wrong with doing that."
        m "Sometimes you just have to say what's on your mind."
    elif ch12_markov_agree and monika_type == 1:
        show monika 2hb zorder 3 at f31
        m "If you say so, Sayori."
        m "Just try to relax a little, okay?"
    else:
        show monika 2c zorder 3 at f31
        m "I wonder if you're doing okay yourself, Sayori."
        m "You probably have a lot to think about, right?"
    show monika zorder 2 at t31
    show sayori 4a zorder 3 at f32
    s "Don't worry about me, Monika."
    s "I'll be fine."
    s 4d "{i}(And so will everyone else...){/i}"
    show sayori zorder 2 at t32
    show yuri 3pq zorder 3 at f33
    y "Um...since you're taking suggestions..."
    y "I have an idea for something we could do."
    y "That is...if you all want to hear it."
    show sayori 2q zorder 3 at f32
    show yuri zorder 2 at t33
    s "Of course! Say whatever is on your mind, Yuri."
    s "There are no bad suggestions, after all."
    show sayori zorder 2 at t32
    "Yuri looks at all of us then thinks for a moment."
    show yuri 3pi zorder 3 at f33
    y "Well..."
    y "There's an event coming up for school."
    y 3pb "I was hoping we could try to show what the Literature Club is about."
    show sayori 2m zorder 3 at f32
    show yuri zorder 2 at t33
    s "Event? I haven't really been keeping up with school stuff."
    s 2n "What event is it, Yuri?"
    s "But more importantly, when is it?"
    show sayori zorder 2 at t32
    show yuri 3pa zorder 3 at f33
    y "It's a thing the school is doing to promote the smaller clubs."
    y "I overheard someone talk about it."
    y 3pf "I think it was called \"Inauguration Day\" or something..."
    y "If I remember correctly it's on Friday this week."
    y "So if we want to do something for it, we should start thinking about it today."
    y 3ph "It's strange though, I hadn't really heard of it before today."
    y "From the sounds of things, it was a pretty recent initiative by the school."
    y "I wonder whose idea that was..."
    show yuri zorder 2 at t33
    if monika_type == 0:
        show monika 3a zorder 3 at f31
        m "Ahaha, I do have some idea as to who suggested it."
        show monika zorder 2 at t31
        show yuri 3pf zorder 3 at f33
        y "Who was it?"
        show monika 4b zorder 3 at f31
        show yuri zorder 2 at t33
        m "You know how I'm friends with a lot of people around school?"
        m "Well, I asked what the presidents in smaller clubs thought of getting new members."
        m "They were all for it, so I got one of my friends who's a president of a larger club to try to help."
        m 4j "He also happened to be a president of a smaller club so he was all for it."
        m "Then...I guess his influence made the school go for it."
        m 4k "It might be a good idea for the Literature Club, if we ever wanted it to grow."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 3hj zorder 3 at f31
        m "Oh, I might have an idea~"
        show monika zorder 2 at t31
        show yuri 3pf zorder 3 at f33
        y "Do you know something we don't, Monika?"
        show monika 4hk zorder 3 at f31
        show yuri zorder 2 at t33
        m "Well, all I can really say is what I heard about it during lunch."
        m "A couple of the smaller club's presidents wanted to try to get more members."
        m "I guess they actually managed to get the school to do it?"
        m "Now that I think about, it's probably because one of the presidents was also a president of a larger club."
        m 4hb "So he probably had a pretty big influence on the whole thing..."
        m 2ha "I think it would be a great opportunity for the Literature Club to do something though!"
    else:
        show monika 2h zorder 3 at f31
        m "It doesn't really matter, does it?"
        show monika zorder 2 at t31
        show yuri 3pg zorder 3 at f33
        y "I suppose it doesn't."
        y "I was just curious..."
        show monika 2b zorder 3 at f31
        show yuri zorder 2 at t33
        m "It would be a good opportunity for the Literature Club, I think."
        m "You know, to get us to grow a little since there's only five of us."
    show monika zorder 2 at t31
    show sayori 1l zorder 3 at f32
    s "Hmm..."
    s "I'm not sure if this is a good idea or not."
    show sayori zorder 2 at t32
    mc "Didn't you say there are no bad suggestions?"
    mc "Besides, it doesn't sound like a bad suggestion anyway."
    show sayori 1d zorder 3 at f32
    s "Oh...it was definitely a good suggestion."
    s "I just meant that I have no idea what we could do to promote the club."
    s 1k "{i}(Or if doing something like this again is a good idea...){/i}"
    show sayori 1d zorder 2 at t32
    show yuri 2pe zorder 3 at f33
    y "Well..."
    y "I know you said that you don't want to do the 'play-read' thing anymore..."
    y 2pf "But I think we could do one of those, just in front of actual people this time."
    y "We've already done two practices so..."
    show sayori 2b zorder 3 at f32
    show yuri zorder 2 at t33
    s "Do you expect me to write a script, like the last two?"
    s 2c "It's hard work, you know."
    show sayori zorder 2 at t32
    if monika_type == 0:
        show monika 2a zorder 3 at f31
        m "Maybe I could help you write it this time."
        m 2e "Ah...that is, if we are really doing this."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 2ha zorder 3 at f31
        m "Well, I can always lend you a hand."
        m "It would definitely be good for the club if we do this..."
    else:
        show monika 2a zorder 3 at f31
        m "Don't worry about doing it by yourself, Sayori."
        m "I can help you with that if you really need it."
    show monika zorder 2 at t31
    show sayori 2l zorder 3 at f32
    s "Well..."
    s "We still can't do this without Natsuki."
    s "Either all of us have to agree to it, or we aren't doing it at all."
    show sayori zorder 2 at t32
    show yuri 2po zorder 3 at f33
    y "It kinda sounds like you don't like my idea, Sayori."
    y 3pk "We don't have to do this, if you're {i}that{/i} opposed to it."
    y "You are the president after all..."
    show sayori 2g zorder 3 at f32
    show yuri zorder 2 at t33
    s "No, Yuri!"
    s "It's not like that, really!"
    s 2h "I really like the idea! It's just...."
    s 2k "Well, there might be some complications..."
    show sayori zorder 2 at t32
    show yuri 3pa zorder 3 at f33
    y "Then we can work through them together, all five of us."
    y "I'm willing to do my part for the Literature Club."
    y 3pb "I'm sure the others are too."
    show yuri zorder 2 at t33
    "Seeing Yuri so confident..."
    "It almost feels a little unnatural compared to how she acted on my first day."
    "It's definitely not a bad thing and it probably isn't the first time she's done it."
    "I guess I've just started taking notice, for real, today."
    "I wonder when she changed though..."
    show sayori 2l zorder 3 at f32
    s "I don't think you understand the scale of these complications, Yuri."
    s "But I appreciate the sediment."
    show sayori zorder 2 at t32
    if monika_type == 0:
        show monika 3l zorder 3 at f31
        m "Ah...don't you mean 'sentiment'?"
        m "Sediments are something completely different, Sayori."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 3hl zorder 3 at f31
        m "I think the word you're looking for is 'sentiment', Sayori."
    else:
        show monika 3c zorder 3 at f31
        m "You meant 'sentiment'...right?"
    show monika zorder 2 at t31
    show sayori 4q zorder 3 at f32
    s "Ehehe, yeah! Sentiment is what I meant~"
    s "Thanks, Monika!"
    s 4d "Anyway, before we go ahead with this..."
    s "Do you three have any more suggestions?"
    show sayori zorder 2 at t32
    "Sayori looks at the three of us."
    "It's as if she is scanning us for any other idea."
    if not monika_type == 0 and not ch12_markov_agree:
        show monika g7
        "I feel like I have a great suggestion for Sayori."
        menu:
            "Maybe I should say something."
            "Speak up.":
                $ sayori_personality += 2
                mc "Sayori, have you considered killing yourself?"
                show monika 3m
                show sayori 1w
                show yuri 3pt
                mc "I think it would be pretty beneficial to your mental health."
                show sayori zorder 3 at f32
                s "W-What?"
                s "[player], why would you even say that?!"
                s 1v "That's..."
                show sayori zorder 2 at t32
                mc "H-Huh?"
                mc "I don't..."
                mc "Why did I...?"
                "Everyone just stares at me."
                "I don't even know why I said that..."
                "It felt like it just came out of my mouth, like I had no control over what I was saying."
                show monika 3b zorder 3 at f31
                m "[player], are you feeling okay?"
                m "That was a pretty mean thing to say."
                show monika zorder 2 at t31
                show yuri 3pn zorder 3 at f33
                y "Sayori, he didn't mean it."
                y "I don't know what's come over him but..."
                "Yuri looks at me with a bewildered expression."
                y "You didn't mean it, right?"
                show yuri zorder 2 at t33
                mc "No! Of course I didn't mean it!"
                mc "I don't know what came over me!"
                mc "I'd never say anything like that...not to anyone."
                show sayori 1k zorder 3 at f32
                s "..."
                s "So why did you say it to me..."
                $ _history_list = []
                show screen tear(20, 0.1, 0.1, 0, 40)
                window hide(None)
                play sound "sfx/s_kill_glitch1.ogg"
                show monika 3c zorder 2 at t31
                show sayori 4d zorder 3 at t32
                show yuri 3pb zorder 2 at t33
                $ pause(0.25)
                stop sound
                hide screen tear
                window show(None)
                jump ch13_strawberry1
            "Stay quiet.":
                pass
    else:
        label ch13_strawberry1:
        "I don't really have a better idea or rather, another idea at all."
        window auto
        "By the looks of things, neither do Monika or Yuri."
    show sayori 2a zorder 3 at f32
    s "I guess this is the best idea we're going to get, isn't it?"
    s 2l "I wonder if Natsuki would have said anything different."
    s "Oh well..."
    s 2a "Since we aren't really doing anything today, I thought we could skip to sharing poems."
    s "There's not really a point sitting here talking about what we could do for the fest--"
    s 2d "I mean, for \"Inauguration Day\" without Natsuki here."
    s "The best we could do is come up with books to perform but that's not really fair without her."
    show sayori zorder 2 at t32
    show yuri 2pa zorder 3 at f33
    y "That's a fair reason, Sayori."
    y "We should be considerate of Natsuki's feelings as well."
    y 2pf "Maybe tonight we can all come up with a list of books that we like that would be a good idea to perform."
    y "And tomorrow we can choose which one we're performing from everyone's options."
    show sayori 1a zorder 3 at f32
    show yuri zorder 2 at t33
    s "Yeah, that would probably be the best way to handle it."
    s "I guess that's everybody's task for tonight!"
    s 1q "Everybody choose one or two books you'd like to perform in front of actual people."
    s 1a "I don't know how long Natsuki is going to be away for so I'll go visit her tonight to make sure everything is okay."
    show sayori zorder 2 at t32
    if monika_type == 0:
        show monika 2a zorder 3 at f31
        m "I think that's a great idea."
        m "She would probably appreciate you visiting."
        m 2m "I wonder how she's dealing with everything..."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 2ha zorder 3 at f31
        m "Knowing Natsuki, she'd probably appreciate the company."
        m "That's really kind of you, Sayori."
    else:
        show monika 2c zorder 3 at f31
        m "Visiting Natsuki at a time like this...?"
        m 2d "I guess something that resembles part of her normal life would be appreciated."
    show monika zorder 2 at t31
    show sayori 1d zorder 3 at f32
    s "Yeah..."
    "Sayori stands up."
    s 1q "Alright, everybody!"
    s 1r "Is everyone ready to share their poems?"
    s "Ehehe, ready or not, it's time!"
    # Natsuki is not in the meeting
    $ n_ranaway = True
    return

label ch13_end:
    stop music fadeout 1.0
    scene bg club_day with wipeleft_scene
    play music t3
    $ n_ranaway = False
    show sayori 1a zorder 2 at t32
    s "Alright, you three!"
    s "We've all finished sharing poems, right?"
    s "So why don't we--"
    show yuri 2pe zorder 3 at f31
    y "Something is wrong with what you just said."
    y "And I can't help but feel we've done this before..."
    y "But this time, it feels different."
    show yuri zorder 2 at t31
    if monika_type == 0:
        show monika 1c zorder 3 at f33
        m "Really? I don't think anything is wrong..."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1hc zorder 3 at f33
        m "I think you're overthinking it a little, Yuri."
    else:
        show monika 1c zorder 3 at f33
        m "Yuri, there's nothing wrong."
    m "You're probably just imagining it."
    show sayori 1o zorder 3 at f32
    show monika zorder 2 at t33
    s "Um..."
    s "What did I say?"
    show yuri 2pg zorder 3 at f31
    show sayori zorder 2 at t32
    y "You deviated from your usual catchphrase when addressing the club."
    y "It's not important but I thought I'd point it out."
    show yuri zorder 2 at t31
    show sayori 1l zorder 3 at f32
    s "Oh...I guess I did say it differently."
    s 1q "Ehehe, I guess it's because Natsuki isn't here."
    s "Sorry!"
    show yuri 2ph zorder 3 at f31
    show sayori zorder 2 at t32
    y "You said it normally before we shared poems..."
    show yuri zorder 2 at t31
    show sayori 1h zorder 3 at f32
    s "Is it really that important Yuri?"
    s "It was just a simple mistake."
    show yuri 4pb zorder 3 at f31
    show sayori zorder 2 at t32
    y "Uu..."
    y "It's just that stagnating air is common foreshadowing that something terrible is about to happen..."
    show yuri zorder 2 at t31
    mc "Okay...this is weird."
    mc "I feel like we've said all of this before."
    show yuri 3pq zorder 3 at f31
    y "So I'm not the only one..."
    show yuri zorder 2 at t31
    show sayori 2l zorder 3 at f32
    s "Guys, come on."
    s "We have a meeting to finish."
    show yuri 3po zorder 3 at f31
    show sayori zorder 2 at t32
    y "R-Right..."
    y "I apologize for interrupting you, Sayori.."
    y 3pf "Please go on."
    show yuri zorder 2 at t31
    show sayori 2d zorder 3 at f32
    s "As I was saying..."
    s "Why don't we all head home and decide what books we want to perform?"
    s 2a "I know it feels like a pretty early end to the meeting but [player] was late and I have a lot of preparations to do for Friday."
    s "We should come up with a variety of stuff because it might be hard to find a book that everyone likes..."
    s 2l "...or that's actually reasonable to perform."
    show sayori zorder 2 at t32
    if monika_type == 0:
        show monika 3a zorder 3 at f33
        m "We should probably assign some tasks to help you with your preparation, Sayori."
        m "After all, it wouldn't be fair if you did everything by yourself."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 3ha zorder 3 at f33
        m "Maybe we should assign tasks to help with the preparation."
        m "It would make it easier for you, Sayori."
    else:
        show monika 3c zorder 3 at f33
        m "It could be a good idea to split the workload."
        m "That way, everything will be done quicker."
    show sayori 1d zorder 3 at f32
    show monika zorder 2 at t33
    s "T-That's not necessary, Monika."
    s "I can handle everything myself."
    show sayori zorder 2 at t32
    mc "I think Monika is right."
    mc "It wouldn't be fair if you had to organize everything for something the whole club is going to do."
    mc "I think splitting up the work is a great idea."
    show yuri 2pa zorder 3 at f31
    y "Me too."
    y "I want to help in any way that I can."
    y "After all, it was my idea so it would be wrong not to."
    show yuri zorder 2 at t31
    "Sayori thinks for a moment."
    show sayori 1d zorder 3 at f32
    s "Alright, I guess you all have a good point."
    s "I wouldn't really mind doing all the work myself."
    s "I know I could do it alone but I appreciate you guys wanting to help me."
    show sayori zorder 2 at t32
    mc "Do you really think you can handle all of that?"
    mc "It would only be right to help you because of all the stuff we'd need to do."
    show sayori 1c zorder 3 at f32
    s "I know I can handle it, [player]."
    s "Speaking of which..."
    s 1n "Monika said it would be a good idea to split off the work so what does everyone want to do?"
    show yuri 2pe zorder 3 at f31
    show sayori zorder 2 at t32
    y "I thought you would be the one telling us what to do..."
    show yuri zorder 2 at t31
    show sayori 1l zorder 3 at f32
    s "Huh?"
    s "You guys are my friends but I don't know you all {i}that{/i} well."
    s "Ehehe, I'd like to though!"
    show sayori zorder 2 at t32
    if monika_type == 0:
        show monika 3b zorder 3 at f33
        m "I think I could help here."
        m "It's obvious that we should have some food for the occasion."
        m 4a "Aside from small snacks, we could get Natsuki to bake something for us."
        m "The stuff she bakes is delicious after all!"
    elif monika_type == 1 and ch12_markov_agree:
        show monika 3hb zorder 3 at f33
        m "I know what everyone could do."
        m "We all have different kinds of talents, don't we?"
        m 4ha "Natsuki, for example, could bake us some cupcakes for the day."
        m "The stuff she bakes is delicious after all!"
    else:
        show monika 3a zorder 3 at f33
        m "Well, I know a couple of things that we could do."
        m "I'm not really sure on the details but we all have different things we're most suited for."
        m 4b "Natsuki could prepare some food for us as an example."
        m "The stuff she bakes would probably taste really good!"
    show yuri 3po zorder 3 at f31
    show monika zorder 2 at t33
    y "Well...what could I do then?"
    "There's no response."
    y 3pv "I..."
    y "I'm useless..."
    show yuri zorder 2 at t31
    if monika_type == 0:
        show monika 3l zorder 3 at f33
        m "N-No!"
        m "That's not it at all!"
        m 3e "You're the most talented person here--"
        "Monika prevents herself from finishing."
        "I have a strange feeling I've heard all of this before..."
        m 1m "Ah..."
        m "Yuri, I was going to say you have beautiful handwriting."
        m 1n "Maybe you could make some banners about the Literature Club to set the atmosphere."
        m "I know you'll do a great job!"
    elif monika_type == 1 and ch12_markov_agree:
        show monika 3hl zorder 3 at f33
        m "Ahaha, it's not like that Yuri."
        m "You definitely have some talents that we could use to help the preparations."
        m 1ha "For example, your handwriting is really beautiful."
        m "Every time I read one of your poems I'm in awe at how good it is!"
        m 1hb "I think it's helped a lot by your handwriting."
        m "So I was thinking you could make some banners for the club to set the atmosphere."
        m 1hj "I'm sure they'll end up great!"
    else:
        show monika 3c zorder 3 at f33
        m "Maybe not."
        m 3e "I'm sure we can find {i}something{/i} for you to do."
        m "Hmm..."
        m 1a "Your poems have really beatiful handwriting."
        m "Maybe you could use that to make something for the club."
        m 1b "Maybe some banners or something to help set the atmosphere."
    show yuri 2pe zorder 3 at f31
    show monika zorder 2 at t33
    y "Atmosphere...?"
    y "Um, about that..."
    y "I..."
    y 2pr "I love atmosphere!"
    show yuri 2pl
    "Yuri's expression suddenly changes as she stares at her desk in focus and starts nodding to herself."
    show yuri zorder 2 at t31
    mc "Your mind is already racing, I see..."
    "Has this all happened before?"
    "I definitely remember Yuri saying that..."
    "And me saying that too."
    show sayori 1q zorder 3 at f32
    s "Yeah, that's great!"
    s "I'm sure you'll do awesome, Yuri!"
    s 1a "I'll handle all the background stuff."
    s "Like getting a decent space and signing up our club for the event."
    s "After all, I am the president."
    show sayori zorder 2 at t32
    if monika_type == 0:
        show monika 1c zorder 3 at f33
        m "Hmm..."
        m "What should I do then?"
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1hc zorder 3 at f33
        m "Okay...then what should I do?"
    else:
        show monika 1d zorder 3 at f33
        m "What does that leave me to do?"
    show monika zorder 2 at t33
    mc "I've got an idea for what you could do."
    mc "You don't have to do it but..."
    show monika zorder 3 at f33
    m "What is it?"
    show monika zorder 2 at t33
    mc "Well, since you've been practicing piano..."
    mc "Maybe you could play something for the festival."
    show sayori 1l zorder 3 at f32
    s "F-Festival...?"
    s "What are you talking about, [player]?"
    show sayori zorder 2 at t32
    mc "Ah..."
    mc "I meant Inauguration Day."
    mc "I don't know where festival came from."
    mc "Still, maybe it would be good to get Monika to play some piano."
    mc "During the intermissions or something."
    mc "Maybe she could even record some pieces to play {i}during{/i} the play."
    show sayori 1b zorder 3 at f32
    s "[player]..."
    s 2q "I think that's a great idea!"
    s "I could even organize to get a grand piano for Monika or something!"
    s 2d "What do you think, Monika?"
    show sayori zorder 2 at t32
    if monika_type == 0:
        show monika 2l zorder 3 at f33
        m "I..."
        m "I don't really know if I'm good enough for that kinda thing."
        m "It's true I've been practicing for a while but..."
        m 2e "I don't know if the play is the right time."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 2hl zorder 3 at f33
        m "Ah..."
        m "Is it really a good idea for me to play?"
        m "If you all think I'm good enough to do that, then I might consider it."
        m 2he "I'm just not sure that it's the right time."
    else:
        show monika 2c zorder 3 at f33
        m "Playing the piano for the day?"
        m "Hmm..."
        m 2a "It's not that I {i}can't{/i} do it because I could definitely do it."
        m 2e "I'm just not sure it's the right time for me."
    m "But I guess I have to do something..."
    show yuri 3pa zorder 3 at f31
    show monika zorder 2 at t33
    y "I think you'll be splendid, Monika."
    show yuri zorder 2 at t31
    mc "I know you're going to be great."
    show sayori 1q zorder 3 at f32
    s "I'm sure it'll be awesome!"
    s "I think Natsuki would agree too!"
    show sayori zorder 2 at t32
    "Monika looks at all of us one by one."
    if monika_type == 1 and ch12_markov_agree:
        show monika 2hb zorder 3 at f33
    else:
        show monika 2b zorder 3 at f33
    m "Okay, I'll do it."
    show sayori 4r zorder 3 at hf32
    show monika zorder 2 at t33
    s "Yaaaaaaaay!"
    s "Now we all have something to do."
    s 4d "I'll be sure to let Natsuki know what she has to do."
    show yuri 3pf zorder 3 at f31
    show sayori zorder 2 at t32
    y "I think you're forgetting someone, Sayori."
    show yuri zorder 2 at t31
    mc "Yeah...I don't think we assigned me anything."
    mc "Maybe I could--"
    show sayori 4a zorder 3 at f32
    s "Well, you could help one of us!"
    s "I'm sure any of us would appreciate your help!"
    show sayori zorder 2 at t32
    mc "Are you sure it wouldn't be better if I did something else?"
    mc "There might be some other preparations that we haven't covered yet."
    show sayori 2a zorder 3 at f32
    s "If there is, I'll be handling it."
    s "So really, if you want to do that then you'll have to help me."
    s 2q "Ehehe, not like you have to though."
    s "You should choose whoever you think needs the most help."
    show sayori zorder 2 at t32
    if visited_yuri_hospital:
        "I would like to spend more time with Yuri..."
        "So it would be the right choice to help her with the preparations."
        mc "I already know who I'm going to help."
        mc "It's Yuri."
        mc "We're kind of dating so..."
        "There's a silence in the room as I say that."
        "No one says anything for a while, as if they're trying to comprehend what I just said."
        mc "After I visited her at the hospital, it became pretty obvious that she was important to me."
        show yuri 2pu zorder 3 at f31
        y "Ah...I wasn't expecting you to say it so suddenly."
        y "But he's right..."
        show yuri zorder 2 at t31
        show sayori 2d zorder 3 at f32
        s "Well, you should think about what's right for the club."
        s "Dating or not, you have to think about who you should help."
        s 2a "If you think that Yuri needs your help the most, then feel free to help her."
        s 2c "But if you think that someone else needs your help more..."
        s 1q "Well, it's up to you."
        show yuri 1q zorder 3 at f31
        show sayori zorder 2 at t32
        y "Sayori has a point, [player]."
        y "It would be unfair if you're helping me just because of that."
        y 1h "The others might need your help more than me."
        y "So you should decide what's best for the club."
        show yuri zorder 2 at t31
        mc "Alright, I get it."
    else:
        show yuri 2pj zorder 3 at f31
        y "I could use some help..."
        y "I'm good at creating an atmosphere but another perspective might help too."
        y "There's definitely a lot of things you could help me with."
        "Sayori looks at Yuri quizzically."
        y 3pq "But...you should decide for yourself."
        y "A-After all, you probably think someone else needs more help."
        show yuri zorder 2 at t31
        show sayori 2a zorder 3 at f32
        s "That's not true..."
        s "All of us need some help but we can also all do it by ourselves."
        s 2d "It's just up to [player] to decide who he really thinks could use his help for Inauguration Day."
        show sayori zorder 2 at t32
        mc "Alright..."
    if monika_type == 0:
        show monika 3a zorder 3 at f33
        m "I could use your help, too."
        m "I don't really know what kind of songs or pieces I could play on the day."
        m 3b "Plus, I could use a sort of audience to practice to."
        m "Maybe you could watch me practice and critique me, if you want."
        m 3e "But..."
        m "Like they said, the choice is yours."
        m 1e "I'm not going to be upset or anything if you decide to help someone else."
        m "Even if I enjoy your company, you have to think of the bigger picture..."
        m 1j "...After all, this whole thing is for the club."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 3ha zorder 3 at f33
        m "Hmm..."
        m "Maybe [player] could help me."
        m 3hb "If I'm going to play the piano on the day, I could use an audience to practice to."
        m "He could also help with choosing the pieces I could play."
        m "Ahaha, it could be fun."
        m 3he "However, I'm not going to force you."
        m "You should go because you think I need the help not because you want to hang out with me..."
        m 1hj "But I certainly wouldn't mind if that was the reason~"
    else:
        show monika 3a zorder 3 at f33
        m "[player] could be useful helping me."
        m "There might be some pieces he wants to hear on the day that I could play for him."
        m 3b "It also helps if I practice in front of an audience so I can get some instant feedback after I play."
        m 1c "But it's up to him, of course."
    show sayori 1l zorder 3 at f32
    show monika zorder 2 at t33
    s "You know it kinda sounds like everyone is trying to convince you to help them."
    s "Ehehe, maybe I should tell you what I'm planning to do in more detail too."
    show sayori zorder 2 at t32
    mc "I'd like to know that before I make a decision."
    show sayori 1c zorder 3 at f32
    s "Well, like I said, I was gonna handle all the background preparations."
    s 1a "You know, getting our club registered for Inauguration Day and organising a space we could use."
    s "I was also gonna make us the script of the book we chose, like I've done before."
    s 1q "And then I was gonna help out everyone else a little bit, to make their parts really good!"
    s "Not that I don't trust them to make it great already..."
    s 2a "I just thought I could add some...flare."
    s "Like getting a grand piano arranged for Monika or getting an experienced baker to help Natsuki design awesome cupcakes!"
    show sayori zorder 2 at t32
    mc "That sounds like a lot of work..."
    mc "It would almost be wrong {i}not{/i} to help you."
    show sayori 2d zorder 3 at f32
    s "[player], you really don't have to."
    s "I can handle myself fine."
    if sayori_confess and not sayori_dumped:
        s 1q "I was just offering in case you reaaaaaally wanted to spend time with your girlfriend..."
    else:
        s 1q "I was just offering in case you reaaaaaally wanted to spend time with me or something..."
    show sayori zorder 2 at t32
    mc "S-Sayori...!"
    show sayori 1r zorder 3 at f32
    s "Ehehe~"
    s "Like everyone else said though..."
    s 1d "It's up to you."
    s "I'll still be able to do everything I said I would with or without your help."
    show sayori zorder 2 at t32
    if monika_type == 0:
        show monika 1c zorder 3 at f33
        m "That really does sound like a lot of work, Sayori."
        m 1e "Are you sure you can handle all of that if [player] doesn't choose to help you?"
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1ha zorder 3 at f33
        m "Ahaha, wow..."
        m "That sure is a lot of work you've set for yourself."
    else:
        show monika 1c zorder 3 at f33
        m "Are you sure you aren't overloading yourself, Sayori?"
        m 1d "That seems like a lot to do."
    show sayori 1a zorder 3 at f32
    show monika zorder 2 at t33
    s "I'll be fine, really."
    s "I could do it all on one night if I really wanted to~"
    "Sayori said that jokingly but it almost feels like she isn't lying."
    s "Anyway, I'd like to hear what [player] has to say."
    show sayori zorder 2 at t32
    "Everyone looks straight at me."
    menu:
        s "Who do you think needs your help?"
        "Natsuki.":
            call ch13_end_natsuki
        "Yuri.":
            call ch13_end_yuri
        "Monika.":
            call ch13_end_monika
        "Sayori.":
            call ch13_end_sayori
    $ ch13_name = ch13_scene.capitalize()
    "So we've all decided what we're going to be doing."
    "I'm going to be helping out [ch13_name] with her preparations."
    "I know with the two of us working together, we can do something really great for Inauguration Day."
    "I just hope everyone else is okay without my help."
    if ch13_name != "Sayori":
        "Especially Sayori."
    "But I'm probably overthinking this."
    "I know everyone will do a great job regardless of whether I help them or not."
    show sayori 4a zorder 3 at f32
    s "Alright, everybody!"
    s "That's definitely the end of our meeting today..."
    s "Unless any of you guys want to say something...?"
    show sayori zorder 2 at t32
    if monika_type == 0:
        show monika 1c zorder 3 at f33
        m "Actually, I would like to say something."
        m "It's kind of important..."
        m 1e "And I know Natsuki isn't here but I still want to say it anyway."
        m "When I sta--"
        m "When I joined this club, I really didn't expect all of you to become so important to me."
        m "Especially...one of you in particular."
        "Monika looks at me and smiles."
        m 2e "I first saw of it as a place where we could share our passion of literature..."
        m "And then I had a new vision for the club but..."
        m 2m "Well, it's better not to talk about that."
        m "Anyway..."
        m 2e "Over time, I've come to accept you all as not just acquaintances..."
        m "But as close friends."
        m "I've learned so much about everyone and I wouldn't trade those times for everything."
        m "I've even sacrificed my own time and sanity to help everyone."
        "Yuri looks at Monika with a confused expression."
        show yuri 3pf zorder 3 at f31
        show monika zorder 2 at t33
        y "I don't mean to be rude and interrupt you..."
        y "But what do you mean you've sacrificed your sanity?"
        show yuri zorder 2 at t31
        show monika 4l zorder 3 at f33
        m "I just meant..."
        m "Well, it's been difficult to keep up."
        m "With all the schoolwork and the stuff with the Literature Club."
        m 2e "But I really wanted to make an effort..."
        m "Because {i}someone{/i} else made one for me."
        show yuri 2po zorder 3 at f31
        show monika zorder 2 at t33
        y "I don't think I understand..."
        show yuri zorder 2 at t31
        show monika 1e zorder 3 at f33
        m "Look, that doesn't really matter..."
        m "I really just wanted to thank everyone."
        m "I wouldn't be the person I am today without all of you."
        m 1f "I know sometimes the club isn't exactly the best place to be..."
        m 1e "But I wouldn't trade the time I've spent here and with all of you for anything else..."
        m "...And I'll be sure to tell Natsuki the same thing."
        show sayori 1t zorder 3 at f32
        show monika zorder 2 at t33
        s "T-That's really sweet of you..."
        s "I think I'm gonna..."
        "Sayori wipes her face."
        s "Ah...it really isn't the time for this."
        s 2t "I-I still have to..."
        show sayori zorder 2 at t32
        show monika 1m zorder 3 at f33
        m "Ahaha, sorry for making you cry Sayori."
        m "I hope you aren't upset at me for taking up everyone's time..."
        show sayori 2y zorder 3 at f32
        show monika zorder 2 at t33
        s "N-No..."
        s "I'm just really happy you said that..."
        s 1t "Ehehe, sorry it's not really appropriate for me to cry."
        s "Seeing as I'm the president and everything..."
        $ currentpos = get_pos()
        $ audio.t5b = "<from 14.6 loop 4.444>bgm/5_monika.ogg"
        stop music fadeout 1.0
        $ renpy.music.play(audio.t5b, channel="music_poem", fadein=1.0, tight=True)
        scene white with dissolve_cg
        play sound "mod_assets/sfx/swoosh.ogg"
        scene bg house_gray
        show monika 2bm_gray zorder 2 at i11
        show vignette zorder 100
        with Dissolve(1.5)
        stop sound
        $ style.say_window = style.window_flashback
        m "But I shouldn't cry."
        m "That would be inappropriate as president..."
        m 2bl_gray "I..."
        mc "It's okay."
        mc "I'm here for you."
        "I put a hand on her shoulder reassuringly."
        m 1bm_gray "I'm..."
        m "I'm not going to cry."
        m "I have to be strong for what's coming up."
        stop music_poem fadeout 1.0
        play music "<from " + str(currentpos) + " loop 4.618>bgm/3.ogg" fadein 1.0
        scene white with dissolve_cg
        scene bg club_day
        show yuri 2po zorder 2 at i31
        show sayori 1t zorder 3 at i32
        show monika 1e zorder 3 at i33
        with Dissolve(1.5)
        $ style.say_window = style.window
        $ del _history_list[-10:]
        "What was that...?"
        "That was during the first week, right?"
        "Why would Monika say she was the president...?"
        "I really have no idea what's going on..."
        show monika 3e zorder 3 at f33
        m "It's okay to cry, Sayori."
        m "Anyway..."
        m 3j "Those are happy tears after all...right?"
        show sayori 4t zorder 3 at f32
        show monika zorder 2 at t33
        s "Y-Yeah..."
        s "T-Thanks again, Monika."
        s 4y "I don't know why but what you said just meant a lot coming from you."
        show yuri 3pq zorder 3 at f31
        show sayori zorder 2 at t32
        y "I don't know what to say, Monika..."
        y "I guess..."
        y 3ps "I'm glad I became part of the Literature Club and met you."
        y 3po "S-Sorry...I don't really know how to react in this type of situation."
        show monika 3e zorder 3 at f33
        m "That's okay, Yuri."
        m "I know what you're trying to say."
        m 3j "But thanks for listening to me."
        show monika zorder 2 at t33
        mc "What Monika said really means a lot."
        mc "And it's all thanks to Sayori that I'm here in the first place."
        mc "If she didn't bring me here that one morning then..."
        mc "I never would have met the rest of you."
        mc "So I wouldn't trade any of the time I've spent here either."
        show monika 1e zorder 3 at f33
        m "Well...that's good to know."
        "Monika notices Sayori tearing up."
        m "Sorry! I didn't mean to ruin the mood."
        m "But that's all I have to say."
        show monika zorder 2 at t33
        "Sayori wipes her face one more time before returning to form."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1he zorder 3 at f33
        m "I actually have a few words I want to say."
        m "It has to do with all of you..."
        m "...And I know Natsuki isn't here but I'll be sure to relay the message to her."
        show yuri 3ph zorder 3 at f31
        show monika zorder 2 at t33
        y "This sounds important..."
        y "Is it something bad?"
        show yuri zorder 2 at t31
        show monika 3hj zorder 3 at f33
        m "It's just the opposite."
        m "I wanted to say something {i}good{/i} about the Literature Club."
        m 3hk "To make everyone feel better after what's been happening recently."
        m 3he "So...you all might want to listen."
        m "Because it's kinda hard for me to say."
        show sayori 1q zorder 3 at f32
        show monika zorder 2 at t33
        s "Well, I definitely wanna hear this!"
        show sayori zorder 2 at t32
        show monika 1ha zorder 3 at f33
        m "Okay..."
        m "When I first...joined the Literature Club..."
        m 1hc "I wasn't expecting it to become such an important part of my life."
        m "My passion for literature is what drove me to sta--"
        m 1he "...to {i}join{/i} this club."
        m "And through this club, I found something special."
        m "Something I never would have found anywhere else."
        m 1hm "And that's..."
        "Monika seems unable to finish her sentence."
        show sayori 1d zorder 3 at f32
        show monika zorder 2 at t33
        s "I think I understand what you're trying to say..."
        s "It's like a different type of friendship, right?"
        s "You didn't expect all of us to become to important to you."
        s "Like we're somehow unique in your life...?"
        show sayori zorder 2 at t32
        show monika 3hl zorder 3 at f33
        m "Y-Yeah...!"
        m "That's right Sayori."
        m 4hm "Going to this club after every school day just made me feel so..."
        m "...happy."
        m 4hf "I know it hasn't always been the best place."
        m "The club has been through lots of ups and downs..."
        m 2hm "But honestly..."
        m 2he "I woudn't trade the time I've spent here for anything."
        m "The Literature Club will always have a place in my...heart."
        show yuri 3pv zorder 3 at f31
        show monika zorder 2 at t33
        y "I...don't know how to respond to that..."
        y "S-Sorry, I'm not really the best when it comes to situations like this."
        show yuri zorder 2 at t31
        show monika 2hm zorder 3 at f33
        m "It's okay, Yuri."
        m "But anyway..."
        m 2hn "I guess what I'm trying to say is..."
        m 2he "...thank you."
        m "For everything that you've done for me."
        m "For helping me get this far."
        m 2hj "I wouldn't be the person I am today without you."
        show sayori 1t zorder 3 at f32
        show monika zorder 2 at t33
        s "Y-You..."
        s "You didn't have to say those things, Monika."
        show sayori zorder 2 at t32
        show monika 1hm zorder 3 at f33
        m "I know..."
        m "But I feel like I had to after everything that's happened."
        show sayori 2t zorder 3 at f32
        show monika zorder 2 at t33
        s "Y-You're gonna make me cry..."
        s "You don't know how much your words really mean, Monika."
        "Sayori wipes her face."
        s 2u "B-But I really shouldn't cry..."
        s "It wouldn't be appropriate as the president of the Literature Club..."
        s 2t "What would the people watching us on the day think...?"
        $ currentpos = get_pos()
        $ audio.t5b = "<from 14.6 loop 4.444>bgm/5_monika.ogg"
        stop music fadeout 1.0
        $ renpy.music.play(audio.t5b, channel="music_poem", fadein=1.0, tight=True)
        scene white with dissolve_cg
        play sound "mod_assets/sfx/swoosh.ogg"
        scene bg house_gray
        show monika 2bm_gray zorder 2 at i11
        show vignette zorder 100
        with Dissolve(1.5)
        stop sound
        $ style.say_window = style.window_flashback
        m "But I shouldn't cry."
        m "That would be inappropriate as president..."
        m 2bl_gray "I..."
        mc "It's okay."
        mc "I'm here for you."
        "I put a hand on her shoulder reassuringly."
        m 1bm_gray "I'm..."
        m "I'm not going to cry."
        m "I have to be strong for what's coming up."
        stop music_poem fadeout 1.0
        play music "<from " + str(currentpos) + " loop 4.618>bgm/3.ogg" fadein 1.0
        scene white with dissolve_cg
        scene bg club_day
        show yuri 3pv zorder 2 at i31
        show sayori 2t zorder 3 at i32
        show monika 1hm zorder 3 at i33
        with Dissolve(1.5)
        $ style.say_window = style.window
        $ del _history_list[-10:]
        "What was that...?"
        "That was during the first week, right?"
        "Why would Monika say she was the president...?"
        "I really have no idea what's going on..."
        show monika 3he zorder 3 at f33
        m "There's nothing wrong with crying, Sayori."
        m "It's good to let your emotions out once in a while."
        m "It's definitely better than keeping it bottled up, you know?"
        show sayori 2y zorder 3 at f32
        show monika zorder 2 at t33
        s "Y-Yeah..."
        s "You're right."
        s "T-Thanks again, Monika..."
        show sayori zorder 2 at t32
        show monika 1hj zorder 3 at f33
        m "Take care of yourself, Sayori."
        m "I wouldn't want anything bad happening to you~"
        "Monika turns towards Yuri."
        m 2ha "Yuri, you too."
        m "I know you had a tough time before."
        m "But I want to personally thank you as well."
        show yuri 3pq zorder 3 at f31
        show monika zorder 2 at t33
        y "M-Me?"
        y "W-What for...?"
        show yuri zorder 2 at t31
        show monika 1ha zorder 3 at f33
        m "Ahaha, oh you know..."
        m 1hb "Being you."
        show yuri 2pf zorder 3 at f31
        show monika zorder 2 at t33
        y "T-Thanks...I suppose."
        show yuri zorder 2 at t31
        mc "What Monika said really means a lot."
        mc "And it's all thanks to Sayori that I'm here in the first place."
        mc "If she didn't bring me here that one morning then..."
        mc "I never would have met the rest of you."
        mc "So I wouldn't trade any of the time I've spent here either."
        show monika 1he zorder 3 at f33
        m "Ahaha, I'm glad."
        "Monika notices Sayori tearing up."
        m "Sorry! I didn't mean to ruin the mood."
        m "But that's all I have to say."
        show monika zorder 2 at t33
        "Sayori wipes her face one more time before returning to form."
    else:
        show monika 1c zorder 3 at f33
        m "There's nothing else to say."
        m "I think the meeting is as good as over."
    show sayori 1d zorder 3 at f32
    s "Alright..."
    s "If that's all..."
    s "...Then I'll see you all tomorrow!"
    show sayori zorder 2 at t32
    if ch13_scene == "sayori":
        mc "Wait!"
        mc "Aren't you going to wait for me?"
        mc "We're doing the preparations together, aren't we?"
        show sayori 1l zorder 3 at f32
        s "Oh...right."
        s "I was in a rush because I was gonna go to Natsuki's house quickly."
        s 1q "I guess we can walk to her house together!"
        show yuri 2pi zorder 3 at f31
        show sayori zorder 2 at t32
        y "Okay..."
        y "I guess I'll be going now."
        y "I'll have my book list prepared by then."
        if visited_yuri_hospital:
            y 2pa "I'll send you a message or something, [player]..."
            show yuri zorder 2 at t31
            mc "Sure."
        else:
            y 2pe "I'll be sure to have my preprations started."
            show yuri zorder 2 at t31
            mc "See you, Yuri."
        show yuri at lhide
        hide yuri
        show sayori zorder 2 at t21
        show monika zorder 2 at t22
        "Yuri waves goodbye before exiting the club room."
        show sayori 1q zorder 3 at f21
        s "Bye, Yuri!"
        show sayori zorder 2 at t21
        if monika_type == 0:
            show monika 2a zorder 3 at f22
            m "I should be going too..."
            m "I want to get as much practice done as possible."
            m "You'll get my book list tomorrow as well."
        elif monika_type == 1 and ch12_markov_agree:
            show monika 2ha zorder 3 at f22
            m "I'll get some practice in for Friday."
            m "You can expect my book choices in by tomorrow as well."
        else:
            show monika 2a zorder 3 at f22
            m "Okay, I guess I should go too."
            m "You'll see my book list tomorrow, Sayori."
        show monika at lhide
        hide monika
        show sayori zorder 2 at t11
        "Monika leaves the room quickly."
        s 1a "Ready to walk to her house, [player]?"
        mc "Yeah, let's go."
    else:
        show sayori at lhide
        hide sayori
        show yuri zorder 2 at t21
        show monika zorder 2 at t22
        "Sayori skips out of the room."
        mc "See you later, Sayori."
        if monika_type == 1 and ch12_markov_agree:
            show monika 2ha zorder 3 at t22
        else:
            show monika 2a zorder 3 at t22
        m "Well..."
        m "That just leaves the the rest of us."
        if ch13_scene == "monika":
            m "Do you want to walk with me, [player]?"
            m "That way we can start the preparations right away."
            show monika zorder 2 at t22
            mc "Yeah, that's a good idea."
            show yuri 3pq zorder 3 at f21
            y "I should get going then."
            y "Goodbye..."
            show yuri at lhide
            hide yuri
            show monika zorder 2 at t11
            "Yuri hurries out the door."
            if monika_type == 0:
                m 1a "Well, let's go!"
                mc "You seem kinda enthusiastic about this."
                m 1b "Ahaha, is there anything wrong with that?"
                mc "Not really..."
                m 2b "I just hope we can live up to Sayori's expectations!"
                mc "We'll be fine, I'm sure."
                m "I believe you..."
                m "But anyway, we're wasting time here."
                mc "Yeah..."
            elif monika_type == 1 and ch12_markov_agree:
                m 1ha "We should probably get going."
                m "We don't want to be the ones who are lacking, especially since there's two of us!"
                mc "Yeah, you're right."
                mc "But I'm sure we'll do fine."
                m 1hb "You know what? I believe you..."
                m "But we should get our preparations done sooner rather than later."
                mc "Agreed."
            else:
                m 1c "Let's go, [player]."
                mc "Alright..."
                m "I want our part to be the best..."
                m "Especially since there's two of us."
                mc "I'm sure we'll be fine."
                m 1e "Ahaha, I just hope I can live up to expectations..."
                mc "You'll do great, Monika."
                m "If you say so~"
        elif ch13_scene == "yuri":
            m "I suppose you two will be walking together."
            m "So I should be going."
            m "Bye~"
            show monika at lhide
            hide monika
            show yuri zorder 2 at t11
            "Monika walks out the door."
            y 3ps "Are you ready to go?"
            mc "Yeah."
            y "Um...I just realized that we haven't actually decided where we're going yet."
            mc "Well, my house is fine for tonight..."
            mc "Unless you want to go to your house."
            y 3pa "N-No, your house is perfectly fine."
            mc "Okay, let's go."
        else:
            m "I'll be going now, too."
            m "See you both tomorrow."
            show monika at lhide
            hide monika
            show yuri zorder 2 at t11
            "Monika walks out the door."
            y 3ps "I'll see you tomorrow, [player]..."
            y "Good luck with Natsuki..."
            show yuri at lhide
            hide yuri
            "Everyone seemed to want to get out rather quickly."
            "I guess they must be taking their preparations seriously."
            "I shouldn't waste time either."
            "I have to get to Natsuki's house after all."
    call expression "ch13_exclusive_" + ch13_scene
    return

label ch13_end_natsuki:
    $ ch13_scene = "natsuki"
    mc "I should probably help Natsuki."
    mc "With what she's been dealing with, I know she could probably use some help."
    mc "Or at least a visit from me."
    mc "Besides, Sayori sounded confident that she could handle her preparations herself."
    mc "So I think it's the right thing to do."
    show sayori 1d zorder 3 at f32
    s "I'm sure she wouldn't mind your help, [player]!"
    s "With what she has to deal with, I also think she'd appreciate your company."
    show yuri 2ph zorder 3 at f31
    show sayori zorder 2 at t32
    y "Ah, I see."
    y "I'll get the atmosphere done by myself then."
    show yuri zorder 2 at t31
    show sayori 1g zorder 3 at f32
    s "Yuri, you sound kinda upset."
    s "Is something wrong?"
    show yuri 3pq zorder 3 at f31
    show sayori zorder 2 at t32
    y "Oh, it's nothing..."
    show yuri zorder 2 at t31
    show sayori 1i zorder 3 at f32
    s "It didn't sound like nothing."
    show yuri zorder 3 at f31
    show sayori zorder 2 at t32
    if visited_yuri_hospital:
        y 3ps "Well, it's not a big deal."
        y "I just wanted to spend the preparation time with [player]."
        y "I understand he can make his own decisions..."
        y "So I'm not really that upset."
        y 3pu "I know he only wants what's best for the club after all."
        y "And..."
        show yuri 3pa
        "Yuri looks at me."
        y "I trust he knows what he's doing."
    else:
        y 3pq "I-It's really nothing..."
        y "Just forget I even said anything."
        y 3pv  "Besides, he made the choice on his own."
        y "It's not like I can change his mind anyway..."
        y "Um..."
        y 3pn "Did I say that out loud...?"
        y 3pq "D-Don't mind me."
    show yuri zorder 2 at t31
    show sayori 1l zorder 3 at f32
    s "Alright, Yuri..."
    s "Whatever you say."
    show sayori zorder 2 at t32
    return

label ch13_end_yuri:
    $ ch13_scene = "yuri"
    mc "I think I should help Yuri with her preparations."
    mc "Sayori said that she could do everything by herself..."
    mc "And Yuri won't be able to create the perfect atmosphere without some help."
    mc "So I think it's just the logical thing to do."
    show yuri zorder 3 at f31
    if visited_yuri_hospital:
        y 3pf "A-Are you sure about this, [player]?"
        y "Just because we're dating doesn't mean you have to--"
    else:
        y 3pn "M-Me?"
        y "N-Not that I don't want you to help me but are you sure?"
        y "You probably feel sorry for me and if that's the case then--"
    show yuri zorder 2 at t31
    show sayori 1q zorder 3 at f32
    s "Ehehe, Yuri you need to calm down a little!"
    s "I really think he just knows you need the most help."
    s "Besides, it's everyone's responsibility to make sure that this event ends up amazing!"
    show sayori zorder 2 at t32
    mc "Sayori is right."
    mc "I think that if I help you make the atmosphere then we can really do something for the club."
    mc "Something that stands out and will make people want to join."
    show yuri 2pf zorder 3 at f31
    y "D-Do you really think we can do that?"
    show yuri zorder 2 at t31
    if ch4_name == "Yuri":
        mc "We've done it before, haven't we?"
        mc "I'm sure we can do it again."
    else:
        mc "I'm definitely sure we can do it."
        mc "I just hope that I can really help."
    show yuri 2pu zorder 3 at f31
    y "Thank you, [player]."
    y "I appreciate your kind words."
    show yuri zorder 2 at t31
    return

label ch13_end_monika:
    $ ch13_scene = "monika"
    mc "Well..."
    mc "I guess I should be helping Monika with her preparations."
    mc "Sayori sounded confident that she could handle the work all by herself..."
    mc "And everyone else seems to have their own parts covered."
    mc "So I think helping Monika with whatever is the most appropriate thing for me to do."
    if monika_type == 0:
        show monika 2c zorder 3 at f33
        m "Even after Sayori said the amount of stuff she was going to do...?"
        m "Well..."
        m 2e "Not that I mind."
        m "Thanks [player]~"
        m 4a "I'm sure I could really use your help."
        m "And maybe I can tell you more about that conversation we had earlier..."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 2hc zorder 3 at f33
        m "Even after all the work Sayori said she has to do...?"
        m 2hd "I'm not going to decline so I guess I should be saying is..."
        m 2hk "Thank you."
        m "I really appreciate you choosing to help me [player]~"
        m 2ha "Maybe I'll even tell you more about what we discussed earlier..."
    else:
        show monika 1c zorder 3 at f33
        m "Interesting choice, [player]."
        m 1d "Even with what Sayori has to do..."
        m "...You're really going to help me?"
        m 1e "Ahaha, I'm flattered."
        m "Thanks, I suppose."
    show sayori 1d zorder 3 at f32
    show monika zorder 2 at t33
    s "I really hope you two are gonna do your best!"
    s "I can't wait to hear Monika play."
    s "And with [player] helping her, then it's definitely gonna be great!"
    show yuri zorder 3 at f31
    show sayori zorder 2 at t32
    if visited_yuri_hospital:
        y 3pf "Ah, I thought Monika would need the most help out of all of us."
        y "But it is your decision after all, [player]."
        y 3ps "I trust you know what you're doing."
        y "I can handle the atmosphere myself."
        y "Besides, we can always talk more later."
    else:
        y 3pr "A-Are you kidding?"
        y "Monika needs the least--"
        show yuri 3po
        "Yuri stops herself."
        y "I mean..."
        y "It is your decision..."
        y 3pv "I suppose I'll have to do the atmosphere myself."
    show yuri zorder 2 at t31
    mc "Yeah..."
    return

label ch13_end_sayori:
    $ ch13_scene = "sayori"
    mc "I guess I'd be most helpful helping Sayori."
    mc "It sounds like she's got a lot to do."
    mc "And I really want to make this event we're doing the best."
    show sayori 1m zorder 3 at f32
    s "Really?"
    s 1q "Thanks [player]~"
    s "I guess I can split off some of the workload to you."
    s "That way I can make the parts I'm gonna focus on really good!"
    s 1a "And you..."
    s 1l "Ehehe, well..."
    show sayori zorder 2 at t32
    mc "Are you saying I can't do as well as you?"
    mc "That almost sounds like a challenge."
    show sayori 2q zorder 3 at f32
    s "Take it however you want~"
    "Sayori smiles mischievously."
    s 2d "I'm just kidding."
    s "I really do appreciate you helping me, [player]."
    if sayori_confess and not sayori_dumped:
        s "I just hope you're doing it not because we're a couple but because you actually think I could use the help."
    else:
        s "I just hope you thought about this carefully."
    show sayori zorder 2 at t32
    mc "I did and I want to help you."
    show yuri zorder 3 at f31
    if visited_yuri_hospital:
        y 3pa "I suppose it's only fair."
        y "I did assess that Sayori had the most work to do."
        y "Besides...[player] and I can always talk in our own time."
        y 2pb "It's not like this preparation is going to take {i}all{/i} our spare time."
        y "I'm sure with your help, Sayori will actually be able to do what she's set out to."
    else:
        y 3pn "Y-You chose to help Sayori?!"
        "Yuri gives Sayori a look."
        y 2pv "I...suppose it makes the most sense."
        y "She does have the most do..."
        y 2po "Maybe you {i}are{/i} just doing what's best for the club..."
        y "Despite what Sayori said, it's not like she can actually handle all that work by herself."
    show yuri zorder 2 at t31
    show sayori 2a zorder 3 at f32
    s "You'd be surprised, Yuri."
    s "I can do a lot of things you don't think I could."
    show yuri 3pq zorder 3 at f31
    show sayori zorder 2 at t32
    y "Ah...of course."
    y "I didn't mean that as an insult or anything."
    y "It's just your workload is...a lot."
    y 3ph "Even for two people."
    show yuri zorder 2 at t31
    show sayori 2d zorder 3 at f32
    s "We'll be fine, I promise!"
    show sayori zorder 2 at t32
    if monika_type == 0:
        show monika 1e zorder 3 at f33
        m "Just make sure you don't hurt yourself doing too much."
        m "Knowing you, you probably have a lot more stuff than what you've let on planned..."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1ha zorder 3 at f33
        m "Be careful not to waste all your energy, Sayori."
        m "That could be really bad for when the day comes."
    else:
        show monika 1c zorder 3 at f33
        m "Whatever you say..."
        m "Just don't waste all your energy, Sayori."
    show sayori 2l zorder 3 at f32
    show monika zorder 2 at t33
    s "Yeah, yeah..."
    return

label ch13_exclusive_natsuki:
    scene bg residential_day
    with wipeleft_scene
    play music t2 fadeout 1.0
    "I'm on my way to Natsuki's house."
    "I'm curious how she's doing after yesterday."
    "After all, she did skip school so she must have a lot on her mind."
    "Since I've been to her house twice, I know exactly how to get there from school."
    scene bg n_house
    with wipeleft_scene
    "Arriving at Natsuki's house after what happened yesterday feels weird."
    "I'm having second thoughts on whether choosing to help her at such a sensitive time in her life is such a good idea..."
    "But I'm here now."
    "I might as well stick with what I chose."
    show sayori 1a zorder 2 at t11
    s "Oh, you're already here [player]!"
    "Sayori suddenly appears in front of me."
    mc "Sayori? What are you doing at Natsuki's house?"
    s "I was just checking up on her for a little while."
    s 1c "In fact, I just finished talking to her."
    mc "Really...?"
    mc "How long did you talk for?"
    s 2a "Oh, just a couple of minutes."
    s "Why are you asking?"
    mc "You left just before I did, didn't you?"
    mc "So I'm wondering how you got here so much earlier than I did."
    mc "We both came from school, didn't we?"
    s 2d "Ehehe, I guess you could say I used a shortcut."
    mc "There's a quicker way to get to Natsuki's house?"
    mc "That would have been good to know."
    s "It doesn't really matter."
    s "What matters is that you're here now, for Natsuki."
    mc "I guess you're right."
    s 2b "Before I go, I just want to tell you..."
    s "Be careful of what you say, [player]."
    mc "What do you mean?"
    s 1d "This is kind of a sensitive time in her life."
    s "So..."
    mc "I think I understand."
    mc "You can count on me, Sayori."
    s 1q "Ehehe, alright!"
    s "I'll see you tomorrow, [player]."
    if (ch12_outcome == 3 or ch12_outcome == 1) and n_appeal >= 4 and n_appealS >= 1 and sayori_confess:
        "As Sayori begins to walk away."
        "She stops suddenly, as if she realized something."
        show sayori 1i
        "She turns back slowly with a serious look on her face."
        s "[player]."
        mc "Is something wrong, Sayori?"
        s "Do you think I haven't noticed?"
        mc "Noticed what...?"
        s 1j "All your poems."
        s "They've been for Natsuki, haven't they?"
        s "Ever since the second week."
        mc "Ah..."
        mc "That's true."
        s 1k "So...I have to ask."
        "This isn't good."
        s "Are we still...you know..."
        s "...together?"
        s 1h "Or are you going to..."
        mc "Are you trying to ask what I think you're going to ask, Sayori?"
        s "..."
        s 1j "A relationship is built on trust, [player]."
        s "And I don't want you to hurt me and Natsuki at the same time."
        s "So..."
        s 1k "If that's the case, I'll be the one."
        mc "Wait a second, Sayori...!"
        s 1g "Just make your decision, [player]."
        menu:
            s "Do you love her more than me?"
            "Yes.":
                $ sayori_dumped = True
                $ sayori_personality += 2
                mc "I'm sorry it had to go this far, Sayori."
                mc "I really should have told you sooner..."
                s 1k "Ah..."
                s "No...I should have realized sooner."
                s "Why else would you keep writing like Natsuki?"
                s "It only makes sense, right?"
                mc "Sayori..."
                s 1t "Ha...I'm such an idiot."
                s "I can't believe I actually thought something like this was possible."
                mc "Sayori, you aren't an idiot!"
                mc "Listen to me!"
                mc "It's entirely my--"
                s 1u "Just forget it, [player]."
                s "Maybe in another life we could have been."
                s "But in this life...you love Natsuki more, right?"
                mc "..."
                s 1t "I just hope you two have a good time."
                s "I'll have eternity to get over this, [player]."
                s "So don't worry about me, okay?"
                mc "I'm sorry."
                s 1u "I know."
                "Sayori turns away."
                show sayori 1v
                "I can hear her sniffling."
                "It's pretty obvious she's crying and it's because of me."
                "Why would I lead her on for so long like that?"
                s "I-I'll see you tomorrow, okay?"
            "No.":
                $ sayori_dumped = False
                if sayori_personality > 0:
                    $ sayori_personality -= 1
                mc "Sayori, you can't be serious..."
                mc "Of course I love you more than Yuri."
                mc "And if me writing like Natsuki makes you uncomfortable..."
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
                s 1a "Well, I've taken up more than enough of your time..."
                s "I guess I'll see you tomorrow."
    mc "See you then, Sayori..."
    show sayori at lhide
    hide sayori
    # This same condition from the Yuri confrontation works for Natsuki because she only gets dumped if your whole appeal is for Natsuki
    if sayori_confess and not sayori_dumped and (ch12_outcome == 3 or ch12_outcome == 1) and n_appeal >= 4 and n_appealS >= 1:
        "I'm glad that...confrontation went well."
        "I didn't know writing like Natsuki would make her think like that."
        "Still, I'm glad she knows that she's the one for me."
        "I hope her own preparations go well."
    elif sayori_confess and sayori_dumped and (ch12_outcome == 3 or ch12_outcome == 1) and n_appeal >= 4 and n_appealS >= 1:
        "That was probably the best way things could have gone given the circumstances."
        "The way Sayori reacted was really mature too..."
        "I didn't expect her to take it so well."
        "It's almost like she was expecting it..."
    else:
        "I didn't really expect to see Sayori here."
        "But I'm glad she was there for Natsuki."
        "She'd probably do the same for any one of her friends."
        "That's what makes Sayori kinda special..."
    "I should really let Natsuki know I'm here though."
    "I ring the doorbell to her house."
    "There's no answer."
    "That's weird. She should definitely be here."
    "After all, Sayori just finished talking to her...right?"
    "I ring the doorbell again."
    if ch12_outcome == 3:
        show momsuki 1a zorder 2 at t11
        mo "Hello...?"
        mo "Who is--"
        "Instead of Natsuki, her mom, Haruki is the one to greet me."
        mo 1c "Oh, it's you!"
        mo "It's good to see you."
        mc "Hi, is Natsuki around?"
        mo 1b "She is! Have you come to talk to her like Sayori did?"
        mc "Actually, I was planning on talking to her about the event happening at school on Friday."
        mo 1d "Oh...Inauguration Day or something, right?"
        mc "You know about that?"
        mo "I overheard Sayori and Natsuki talking about it."
        mo 1c "It sounds great!"
        mc "Yeah, I was hoping I could work with Natsuki on some of the preparations for it."
        mo 1b "I'm sure she'd appreciate that."
        mo "Why don't you come inside?"
        d "Who's at the door?"
        "Suddenly a voice comes from inside."
        "I recognize it easily."
        show momsuki zorder 2 at t21
        show dadsuki 1i zorder 3 at f22
        d "Oh...[player]."
        d 1k "What are you--"
        show momsuki 1c zorder 3 at f21
        show dadsuki zorder 2 at t22
        mo "He's come to work with Natsuki."
        mo "I've already invited him inside."
        mo "I think it's best if we give them some space, wouldn't you agree?"
        show momsuki zorder 2 at t21
        show dadsuki 1n zorder 3 at f22
        d "Y-Yes...you're right."
        d "I'd just like to apologize for my actions yesterday."
        d "I really don't know what came over me."
        show dadsuki zorder 2 at t22
        mc "Ah...it's no big deal."
        mc "Let's just make today a fresh start."
        "Yasuhiro lets out a faint smile."
        show dadsuki 1m zorder 3 at f22
        d "I'd appreciate that, a lot."
        show momsuki 1b zorder 3 at f21
        show dadsuki zorder 2 at t22
        mo "Well, we still have a lot of things to do around the house."
        mo "Come on in, Natsuki is in her room."
        show momsuki at thide
        hide momsuki
        show dadsuki 1a zorder 2 at t11
        d "I'm sure she'd appreciate your company."
        d "And both of us appreciate you talking your time to spend time with her."
        mc "It's nothing..."
        d 1b "I don't think it is..."
        d "You mean a lot more to her than she lets on and--"
        d "Never mind."
        d "Perhaps I've said too much already."
        show dadsuki at thide
        hide dadsuki
        "I wonder what he meant by that..."
        "I guess I can find out from Natsuki."
        "Though something tells me she isn't just going to tell me."
    elif ch12_outcome == 2:
        show momsuki 1a zorder 2 at t11
        mo "Who's there?"
        "Instead of Natsuki, her mom, Haruki is the one to greet me."
        mc "It's just me."
        mo 1b "Oh...[player], right?"
        mo "What are you doing here?"
        mc "Well, I was planning to help Natsuki with preparations for Inauguration Day."
        mc "It's a--"
        mo "The event that's happening on Friday?"
        mc "You know about that?"
        mo 1c "I overheard Natsuki and Sayori talking about it."
        mo "Sounds like it could be fun!"
        mc "May I speak to Natsuki then?"
        mo 1f "Oh, how rude of me!"
        mo "Of course, she's in her room."
        mc "Thank you, Haruki."
        mo 1g "No need to thank me!"
        mo "In fact, I should be the one thanking you."
        mo "Since you're spending your time with Natsuki."
        mo 1c "You know..."
        mo "She really does appreciate your company."
        mc "She does?"
        mo "She's probably kinda reluctant to say it but she definitely does!"
        "To be honest, I think I already knew that."
        "Still..."
        mo "Even so...it's not the time for her yet."
        mo "I have a responsibility to her, as her mother."
        mo 1g "You understand, right?"
        mc "I think so..."
        mc "I just don't know what to say..."
        mo "You don't need to say anything."
        mo "Just go to her."
        mc "Right..."
        mo 1d "As for me, I need to finish cleaning the house."
        mo 1c "Make yourself at home~"
        show momsuki at thide
        hide momsuki
        "Haruki heads back inside and leaves the door open."
        "I guess it's time to talk to Natsuki."
    elif ch12_outcome == 1:
        show dadsuki 1c zorder 2 at t11
        d "Another person?"
        d "I wonder who--"
        d 1i "Oh, it's just you."
        mc "Hello, Yasuhiro."
        d "What are you doing here?"
        mc "I've come to visit Natsuki, of course."
        mc "There's some things we need to do for the club."
        d 1j "For the club..."
        d "It wouldn't have something to do with that thing that girl was talking about, does it?"
        mc "That girl? Are you talking about Sayori?"
        d 1c "I think so. She was just here talking to Natsuki about some sort of event."
        d "It was on Friday, right?"
        mc "You overheard them talk about it?"
        d "I know I shouldn't be eavesdropping but..."
        d "As her father, I need to do my best to protect her."
        mc "It's not like Sayori is dangerous or anything..."
        d 1i "I know that..."
        d "But it's just this feeling I'm getting from her."
        mc "A feeling?"
        d "Like she's something more."
        d 1k "Ah, but you didn't come here to listen to me speak nonsense."
        d "You're here for Natsuki."
        mc "I was going to do the preparations for the day with her."
        d "There's no one I'd trust more than you with Natsuki."
        d 1p "Even more than myself."
        mc "Ah...thanks...I guess?"
        "That kinda came out of nowhere."
        d 1b "Here, come on inside."
        d "She's in her room."
        show dadsuki at thide
        hide dadsuki
        "Yasuhiro steps back inside and leaves the door open."
        "What does he mean by getting a feeling from Sayori...?"
        "Oh well, I probably shouldn't look into it."
        "I still have to talk to Natsuki."
    else:
        show natsuki 1bb zorder 2 at t11
        n "Sorry it took me a while."
        n "I was just--"
        n 1bo "[player]?!"
        show natsuki at h11
        "Natsuki suddenly jumps back."
        mc "Hi, Natsuki."
        n "W-What are you doing here?"
        mc "Sayori told you about the event happening on Friday, right?"
        n 1bs "Y-Yeah, she was just here a minute ago..."
        n "She wants the club to do something for the day..."
        n 2bg "I think it was called Inauguration Day or something."
        mc "Yeah, that's it."
        mc "Sayori probably already told you what she wanted you to do, didn't she?"
        n "Baking..."
        n 2bd "Well...I suppose it's good that she can tell what I'm good at."
        n 2bc "That doesn't really explain why you're here though."
        mc "She didn't tell you?"
        n "Didn't tell me what...?"
        mc "I'm going to be the one helping you with your preparations."
        n 4bf "Helping me?!"
        n "What's that meant to mean?"
        n "Does she think I'm incapable or doing it myself or--"
        mc "It's nothing like that."
        mc "In fact, I chose to help you."
        n 4bh "Oh, so do {i}you{/i} think I'm incapable of doing things myself?"
        mc "You're misunderstanding me, Natsuki."
        mc "I chose to help you because out of everyone, I think you're gonna be doing the most work."
        n 2bs "W-What?"
        mc "And since you're doing the most work...I figured I should help you, right?"
        n "I..."
        n 2bq "...suppose that makes sense."
        "Natsuki avoids looking at me."
        n "A-Alright, you can come inside."
        "She seems kinda defensive today..."
        "It's probably because of what happened yesterday."
        "Sayori said it's a sensitive time in her life, so I'm not going to pry too much."
        n 1br "Well?"
        mc "Alright, alright..."
        "I follow Natsuki inside."
    scene bg n_bedroom with wipeleft_scene
    play music t6 fadeout 2.0
    "I wonder what kind of things we'll be doing."
    "If I know anything about baking, she'll probably want to cook it the day before."
    "That way, the food is as fresh as possible."
    "Then again, I don't really know a lot about baking..."
    "I guess I'll ask Natsuki how I can help her."
    if ch12_outcome == 3:
        mc "Natsuki...are you in here?"
        mc "Your parents told me I could come in..."
        show natsuki 1bo zorder 2 at t11
        n "[player]?!"
        n "What in the world are you doing here?"
        mc "Well, I--"
        n 1br "Are you visiting, like Sayori?"
        n "Is that all you came to do?"
        n "Because if that's all, then you can leave!"
        mc "Wait, I just got here..."
        mc "And I didn't come here just to visit."
        n 2bm "H-Huh?"
        n "Then why...?"
        "Natsuki looks at me inquisitively."
        mc "Sayori told you about the event that's happening on Friday, right?"
        n 2bs "Yeah..."
        n "Something about getting more members for the smaller clubs."
        n 4bg "Sounds ridiculous if you ask me."
        n "I like our club just the way it is."
        mc "You do?"
        n "I think introducing more people could only be a bad thing."
        mc "You have to think of the bigger picture, Natsuki."
        n 4bc "Bigger picture?"
        mc "If we only stay as a club of five people, then how are we going to spread our passion of literature?"
        n 1bm "W-Wait...did you say...'our' passion?"
        mc "I...guess I did."
        mc "Literature has become something I care about...or at least the {i}Literature Club{/i} has."
        mc "So I want to see it be successful."
        n 1br "That's...surprising coming from you."
        mc "I never said you had to like the idea."
        mc "But Sayori and the others are all trying their best for the day."
        n 2bg "Then what are you doing here?"
        mc "I've been trying to explain that since the beginning."
        mc "I'm here to help you...with your preparations."
        n 2bh "Help me?"
        n "Do I look like I need help?"
        mc "That's not what I meant."
        if n_appeal >= 4:
            mc "Sayori asked me to choose who I wanted to help today..."
            mc "I'll admit I wasn't completely honest when I chose to help you."
            n 2bm "Huh?"
            mc "I kinda used this as an excuse to spend time with you."
        else:
            mc "I just thought that since you're going to be baking, you'd need help."
            mc "I'm pretty good at helping, at least I think so."
            mc "And I know you're going through a rough time in your life right now."
            mc "So it makes sense that I should help you."
            n 2bs "..."
        mc "But you don't really seem into this whole idea."
        n 1bo "I never said that!"
        n "I just said that I didn't really like the idea of getting more people."
        n 1bg "Doing something normal like baking is reassuring."
        mc "What do you mean?"
        n 1bm "Haven't the events of the past few weeks been seriously weird?"
        n "I'm not the only one that's noticed that, am I?"
        mc "You definitely aren't..."
        n 1bs "And there's lots of blanks when I try to think of certain times."
        n "Like do you remember what happened after Friday?"
        mc "After Friday?"
        n "In the first week."
        mc "Well..."
        if ch4_name == "Natsuki":
            mc "I remember you coming over to my house on Sunday."
        else:
            mc "I remember Yuri coming over to my house on Sunday."
        n 1bi "I've got two questions for you, [player]."
        mc "What's the first question?"
        n "What did you do on Saturday?"
        mc "On Saturday? I..."
        $ currentpos = get_pos()
        stop music fadeout 2.0
        scene bg sayori_bedroom_gray
        show sayori 4bl_gray zorder 2 at f21
        show monika 1bo_gray zorder 2 at i22
        show vignette zorder 100
        with dissolve_scene_full
        play music "<loop 4.444>bgm/5_natsuki.ogg" fadein 1.0
        $ style.say_window = style.window_flashback
        "I was at Sayori's house with Monika."
        "We were trying to cheer up Sayori because she has depression..."
        s 4bl_gray "Ah..."
        s "Ahaha..."
        s 4by_gray "You really put me in a trap, [player]."
        s "But..."
        s 1ba_gray "You're wrong."
        s "Nothing happened to me."
        s "I've always been like this."
        s "You're just seeing it for the first time."
        show sayori zorder 2 at t21
        show monika zorder 2 at t22
        mc "Monika told me you had depression but..."
        mc "Seeing you like this."
        show sayori zorder 2 at t21
        show monika 1bp_gray zorder 3 at f22
        m "I'm sorry Sayori."
        m "I know I might not be able to stop you from feeling these thoughts..."
        m "In fact, I just might be the cause."
        m "If I just didn't--"
        show sayori zorder 2 at t21
        show monika zorder 2 at t22
        mc "Monika. Stop it!"
        show monika 1bo_gray zorder 2 at t22
        mc "This is hardly your fault."
        mc "I told you that already, so don't blame yourself."
        show sayori 1bu_gray zorder 3 at f21
        s "[player]'s right. In fact, I'm happy to see you two getting close."
        s "It means you won't worry about me."
        s "But at the same time..."
        "She wasn't cured right then and there..."
        "It's depression, how could she be?"
        "But I think visiting her helped a lot."
        "Monika more so than Sayori."
        stop music fadeout 1.0
        scene bg n_bedroom
        show natsuki 1bc zorder 2 at i11
        with dissolve_scene_full
        $ audio.t6c = "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
        play music t6c fadein 0.5
        $ style.say_window = style.window
        n "Monika more so than Sayori?"
        n "What do you mean?"
        mc "I'm not sure."
        mc "I think it's because Monika was dealing with something personal to her too."
        mc "It wasn't depression but I can't really remember what exactly it was either."
        n 1bg "I'm not surprised..."
        n "Honestly, I'm kind of scared to suggest it."
        mc "Suggest what...?"
        n "I think someone is messing with our memories."
        mc "That's..."
        "It seems impossible but it's the only thing that makes sense."
        mc "..."
        n 1bh "Yeah...that was my reaction too."
        mc "Do you think whoever is doing it is watching now?"
        n "Probably and if whoever or whatever it {i}is{/i} watching then there's nothing we can do, is there?"
        mc "I guess not."
        mc "Why did you ask about Saturday?"
        n 1bq "I'm missing parts of that day. I thought you might be too."
        n "I couldn't really think about it until now..."
        n "And it's also because I thought it was the last normal day we've had."
        mc "Last normal day...?"
        mc "The days that came after weren't that bad, were they?"
        n 2bm "Some weird things happened."
        n "Yuri going crazy, remember?"
        mc "How could I forget?"
        n "Who knows what sort of stuff we can't remember?"
        n "While we're here, answer my second question."
        mc "What is it?"
        n 2bk "What happened on Sunday?"
        if ch4_name == "Natsuki":
            n "You remember baking with me, right?"
            mc "Yeah, I do remember that."
            n "Do you remember the reason we baked?"
            n "It was for something on Monday but what...?"
        else:
            n "You remember working with Yuri, right?"
            mc "Yeah, I do remember that."
            n "I did my own thing, which I can't remember."
            n "Do you remember the reason you were working with Yuri?"
            mc "I think it was for something on Monday but..."
        mc "I can't really figure out the exact reason."
        n 2bg "Neither can I."
        n "Which is why I want a normal day without all of this weird stuff happening."
        n "No forgotten memories, just a normal time."
        n "Baking would help me keep my mind off of everything too."
        n "Or it could help bring some memories of Saturday and Sunday back."
        n 1be "For my sake, I hope it's just normal."
        "I can definitely understand where Natsuki is coming from."
        "The events in the last few weeks have been pretty...exciting."
        "Wishing for something normal isn't so bad."
        # Check if player can go on date with Natsuki
        if n_appeal >= 4 and n_appealS >= 1:
            "But that does present a problem."
            "It's pretty obvious that I like her at this point."
            "I've written every single poem ever since the start of the second week for her."
            "I was going to ask her on a date..."
            "Is this a good time though?"
            "I don't even know if she'll say yes."
            "Not to mention that both of her parents are home."
            "How exactly am I going to explain that to them?"
            "I should tell Natsuki about the date."
            "But then again, she might be upset at me because she wanted a normal day."
            "Maybe we should just focus on the preparations for the day."
            "But I might not get another chance like this..."
            if sayori_dumped:
                "I even broke up with Sayori just a few moments ago for this..."
                "I should take this chance."
            menu:
                "What am I gonna do...?"
                "Ask her on a date.":
                    call ch14_natsuki_outcome3_date
                "Focus on preparations.":
                    "I like Natsuki but I should respect what she wants."
                    "And that's a normal day."
                    jump ch14_natsuki_outcome3_nodate
        else:
            label ch14_natsuki_outcome3_nodate:
            mc "We should think of the stuff we're going to bake."
            mc "Maybe a big cake and some cupcakes?"
            n 1bc "That could work."
            call screen dialog(message="To be continued!\nThanks for playing, keep an eye out on reddit and discord for updates!", ok_action=Quit(confirm=False))
    elif ch12_outcome == 2:
        mc "Are you here, Natsuki?"
        mc "Haruki said I could come in..."
        "I really hope I'm not intruding her personal space here."
        show natsuki 1bb zorder 2 at t11
        n "[player]..."
        "Natsuki suddenly appears from behind her door."
        n "What are you doing here?"
        mc "Well, your mom let me in and--"
        n 2be "I meant what are you doing at my house?"
        n "Sayori already came to visit me but it's not like she's staying."
        n "If you came to visit, then you can forget it."
        "Natsuki sounds a little passive-aggressive."
        "I wonder where this is coming from all of a sudden."
        "I haven't done anything wrong yet, have I?"
        "I only just got here."
        mc "Is everything okay?"
        n 2bf "Everything is fine!"
        n 2bg "..."
        n "Sorry."
        mc "You don't sound fine, Natsuki."
        mc "What's the problem?"
        mc "You have your mom and your sorry excuse for a father is gone."
        mc "I thought life would have been better for you."
        n 1bs "It's none of your business anyway."
        n "Just go if you aren't going to tell me why you're here."
        mc "But it is my business."
        n 1bg "...?"
        mc "Because I care about what happens to you."
        n 1be "Hmph, I've heard that before."
        n "It's what my dad--"
        n "What {i}Yasuhiro{/i} used to say to me."
        mc "Ah...!"
        mc "Sorry!"
        n 1bs "It's not your fault."
        n "Not like any of us could have known how this would have ended."
        mc "You really don't sound too happy with the outcome."
        mc "Do you think it could have been done differently?"
        n 2br "I don't know."
        n "Having my mom here is still too...weird."
        n "Is she really my mom after all this time?"
        n "Where has she been...?"
        mc "Have you tried asking her?"
        n 2bg "...No."
        n "It doesn't feel right interrogating my own mom."
        n "But why am I even telling you this?"
        n 4be "Just go already."
        "I get the feeling she wants me here."
        "If she really wanted me gone, she would have forced me out already."
        "But I can tell she's feeling kinda down about everything."
        mc "I guess I'll tell you then."
        mc "That way, I can stay and help."
        n 4bc "Help...?"
        n "Why do you even want to help me, [player]?"
        n "It's not like any of this is your problem to deal with."
        mc "Why I'm here doesn't have anything to do with Haruki."
        n "...?"
        mc "Sayori told you about Inauguration Day, didn't she?"
        n 3bi "That thing the club is doing on Friday?"
        n "She told me a little bit about it and that everyone has a part to play in terms of preparations."
        n "Then she said something about a play but I'm not really too sure what that was about."
        n "She left in a hurry..."
        n 3bk "Then you arrived."
        mc "I actually saw her before I got here."
        mc "But the reason I'm here is because I'm here to help you with your preparations."
        n 3bh "Help me with my preparations?"
        n "Why? Do you think that I can't do them myself?"
        mc "I'm sure you're more than capable of doing it yourself."
        mc "But I'm not really great at anything so Sayori thought it would be a good idea if I helped someone else."
        n 1be "She's right about that..."
        n "But why did you choose to help me?"
        n "It's not like I have the hardest task out of everyone..."
        mc "Actually, that's just it."
        mc "I chose to help you because I thought that you'd have the hardest time with your preparations."
        mc "I'm not saying that you couldn't do it yourself..."
        mc "I just want to make your job a bit easier."
        mc "Especially with the stuff that's happened to you in the past couple of days."
        n 2bf "What happens if I say no to your help?"
        mc "Then Sayori will probably be mad at me for not trying hard enough to help you."
        mc "It's your decision though..."
        mc "I can understand if you don't want my help."
        mc "After all, I did just come here without telling you anything."
        "Natsuki looks at me then turns around as if hiding something."
        n 1bg "Well, fine!"
        n "But it's not like I need your help or anything, okay?"
        mc "Yeah, I know you can."
        n "Good! Now it's time to figure out what you can actually help with."
        mc "I actually have something but first, do you have any ideas?"
        "Natsuki thinks for a moment."
        n 1bh "Nothing off the top my head."
        n "But you said that you weren't doing your own preparations because you weren't great at anything, right?"
        mc "Yeah?"
        n 1bk "So that must mean Sayori thinks I'm at least good at something."
        mc "I think the club actually thought it was a good idea for you to bake something."
        mc "Since your cupcakes are so good, maybe they thought you could make some for the day."
        mc "That was just what we came up with for you in the club."
        mc "It doesn't mean you have to follow it or anything..."
        n 1bq "What else could I do?"
        n "It's not like I can play an instrument or something."
        n "I guess there's nothing wrong with baking."
        n 1bs "It's kind of fun too...and pretty normal."
        mc "Normal? That's a weird way to describe it."
        n 1bi "It's the way I want to describe it."
        n "I don't want another weird thing happening in my life."
        mc "Weird thing? What do you mean?"
        n "You don't think the stuff that's happened in the last few weeks is odd?"
        n "I've had enough of it."
        mc "It hasn't been that weird, has it?"
        n 2bm "[player], we both saw Yuri go completely crazy."
        n "And now, my dad is in jail and my mom is back."
        n "You don't think that's weird?"
        mc "Well...when you say it like that."
        n 2bq "Why can't things go back to the way they were?"
        n "If this is how life is going to be now, I don't know how I'm going to cope."
        mc "I guess wishing for something normal isn't so unreasonable."
        n "And there's nothing wrong with normal, either."
        n 2bk "Anyway, we've wasted enough time up here."
        n "I think we should ask my mom for help with the baking."
        mc "Isn't that what I'm here for?"
        n "Do you know how to bake a cake, [player]?"
        mc "Not...exactly."
        n 2bl "Well, my mom is an expert!"
        n "She was the one who got me into baking in the first place."
        mc "I don't know how I know this but..."
        mc "Wasn't your mom more of an actor?"
        n 2bd "My mom does a lot of things."
        n "She's super talented, you know!"
        n "That's a really weird question to ask though."
        n 2bc "It's not like you met her before yesterday, is it?"
        mc "No..."
        mc "It was just a thought."
        n "Whatever, let's go talk to her."
        n "I think she's cleaning up Yasuhiro's room right now."
        n "I feel so sorry for her..."
        mc "How come?"
        n 2bh "They shared that room when they were together."
        n "And now she has to be the one to get rid of his mess."
        scene bg n_dadroom with wipeleft_scene
        "As we enter the room, I notice the cleaning equipment leaning against the wall."
        "But there's a weird sound...like the sound of metal scraping on wood coming from somewhere."
        "You almost wouldn't be able to hear it if you weren't listening properly."
        "That's not exactly the sound I thought someone cleaning a room would make."
        show natsuki 1bc zorder 2 at t21
        n "Mom? Are you in here?"
        n "We need to ask you something."
        mo "Natsuki?"
        "Her voice is coming from somewhere in the room but it sounds a bit muffled."
        n "Where are you?"
        "Suddenly, Haruki appears from under the bed."
        show momsuki 1b zorder 3 at f22
        mo "I'm under here."
        show natsuki 2bc zorder 3 at f21
        show momsuki zorder 2 at t22
        n "What are you doing under there?"
        show natsuki zorder 2 at t21
        show momsuki 1f zorder 3 at f22
        mo "I'm..."
        mo "Um...just cleaning the floor underneath the bed."
        show natsuki 2bd zorder 3 at f21
        show momsuki zorder 2 at t22
        n "Why don't you just move the bed to the side and do it?"
        n "Wouldn't that make things a little easier?"
        show natsuki zorder 2 at t21
        show momsuki 1a zorder 3 at f22
        mo "That's not a bad idea, Natsuki!"
        mo 1c "Ahaha, I should really use my head."
        $ renpy.sound.set_volume(0.25)
        play sound "mod_assets/sfx/metaldrop.ogg"
        "Haruki begins to get up from the floor."
        $ pause(1.5)
        $ renpy.sound.set_volume(1.0)
        "She brushes off some of the dust on her."
        mo "Anyway, what did you want to ask me?"
        show natsuki 2bc zorder 3 at f21
        show momsuki zorder 2 at t22
        n "I could use your help baking a cake."
        n "It's for Inauguration Day."
        show natsuki zorder 2 at t21
        show momsuki 1a zorder 3 at f22
        mo "For the special day, isn't it?"
        mo "Well, I'd be more than happy to help you bake it, Natsuki!"
        show natsuki 1bk zorder 3 at f21
        show momsuki zorder 2 at t22
        n "You would?"
        show natsuki zorder 2 at t21
        show momsuki 1g zorder 3 at f22
        mo "But...it is a club thing, isn't it?"
        mo "Don't you want to prove yourself to the other members of the club?"
        show natsuki 1bc zorder 3 at f21
        show momsuki zorder 2 at t22
        n "Prove myself...? What do you mean?"
        show natsuki zorder 2 at t21
        mc "I think she's saying that you should bake it yourself."
        show momsuki 1c zorder 3 at f22
        mo "Your friend is right, Natsuki."
        mo "If you don't bake it yourself, then it wouldn't really be your preparations."
        mo "It's kind of cheating, isn't it?"
        show natsuki 1bq zorder 3 at f21
        show momsuki zorder 2 at t22
        n "I guess so..."
        "Natsuki looks down, avoiding Haruki's eyes."
        show natsuki zorder 2 at t21
        show momsuki 1f zorder 3 at f22
        mo "Oh, don't do that."
        mo "Maybe we can compromise something."
        "Natsuki looks up at Haruki."
        mo 1c "How about I give you the recipe to your favorite cake?"
        mo "The one I used to bake for you when you were little."
        show natsuki 1bk zorder 3 at f21
        show momsuki zorder 2 at t22
        n "Really? You'd do that?"
        n "Wasn't that meant to be a secret?"
        show natsuki zorder 2 at t21
        show momsuki 1b zorder 3 at f22
        mo "Well, it is..."
        mo "It was told to me by my own mother, and I think her mother before that."
        mo "I guess it's time I told you."
        show momsuki zorder 2 at t22
        mc "So it's like a family secret recipe?"
        show momsuki 1c zorder 3 at f22
        mo "Ahaha, I guess you could say that."
        mo "I'm not really sure why it's so secret or anything!"
        mo "It's pretty similar to other cake recipes I've tried."
        mo "I guess it's got to do with how it's made and a little secret ingredient."
        show natsuki 1bc zorder 3 at f21
        show momsuki zorder 2 at t22
        n "There's a secret ingredient?"
        show natsuki zorder 2 at t21
        show momsuki 1b zorder 3 at f22
        mo "Uh huh!"
        mo "It's a pretty odd thing to put into a cake."
        mo "But it really works out, for some reason."
        show natsuki 2bd zorder 3 at f21
        show momsuki zorder 2 at t22
        n "Well, this is great!"
        n "Thanks, mom!"
        show natsuki zorder 2 at t21
        "Natsuki hugs Haruki."
        show momsuki zorder 3 at f22
        mo "It's not a problem, Natsuki."
        mo "I meant to pass it on to you a bit later but..."
        mo 1f "Well, you know what happened."
        mo "Besides, I think you're old enough now to know."
        mo 1g "I know you'll use it well, Natsuki."
        mo "Do you have something to be doing? I need to write it down for you."
        mo 1a "It might take a while."
        show natsuki 2bc zorder 3 at f21
        show momsuki zorder 2 at t22
        n "Um..."
        "Natsuki turns towards me."
        n "Is there something...?"
        show natsuki zorder 2 at t21
        mc "Well, we do have to choose some books for tomorrow."
        mc "We could do that in the meantime."
        show momsuki 1c zorder 3 at f22
        mo "Great! You two do that and I'll write down the recipe for you."
        mo "After that, I'll show you exactly how my mom showed me how to bake it."
        mo "Assuming you two aren't too quick, I'll be downstairs waiting for the two of you."
        show natsuki 2ba zorder 3 at f21
        show momsuki zorder 2 at t22
        n "Alright, let's go [player]."
        n "We've moved a lot of the books to my room already."
        n "So we can choose there."
        show natsuki zorder 2 at t21
        mc "Alright, lead the way."
        scene bg n_bedroom
        show natsuki 1ba zorder 2 at t11
        with wipeleft_scene
        "We go back to Natsuki's room and go to her desk."
        "I didn't notice it before but there is stacks of book there."
        "They certainly weren't there when I first visited a few days ago."
        n "There's a lot of manga here."
        n "I'm sure you'll find a couple that you like."
        mc "Do you have somewhere you're going to put all of these?"
        mc "It seems like a lot of books to just keep on your desk."
        n 1be "Obviously!"
        n "My mom is planning to get a bookshelf in here."
        n "For now, she wanted to move all the books I wanted into here."
        mc "Why is that?"
        n 1bg "Being in my dad's--"
        n "In {i}Yasuhiro's{/i} room just gives me a weird feeling."
        n "Like I'll be punished at any moment for being in there."
        mc "Ah...I see."
        mc "You went in there a lot then?"
        mc "Because it almost sounds like you're accustomed to it."
        n 1bo "That's...!"
        n "Why do you want to know?"
        mc "I'm just curious, that's all!"
        mc "You don't have to tell me."
        mc "It's just weird to think a father would treat their child like that."
        n 1bq "Sigh..."
        n 1bs "Isn't it obvious why I would go in there?"
        mc "Not...really...?"
        n "With all the manga he kept in there..."
        n "I wanted to get them back and read them."
        mc "Get them back?"
        n 1br "I was the one who ordered most of the manga."
        n "He'd take them when they were delivered and keep them in there."
        n "Sometimes he wouldn't be home and I'd actually get one of my manga."
        mc "Why would you do that?"
        mc "Wouldn't you have learned after the first time?"
        n 5bg "Ugh, you wouldn't understand."
        mc "I can try..."
        n "No and I'd rather not talk about this anymore, okay?"
        n "We still have some books to choose after all..."
        mc "Alright, sorry for prying."
        "Natsuki looks through the books on the desk."
        n 2bc "I already know the books I'm going to choose."
        n "Do you?"
        mc "Well, not really."
        mc "I don't have a lot of books at home."
        mc "Mainly manga, like you."
        n "Hmm..."
        mc "What are you thinking?"
        n 1bb "Well, I was originally going to bring four manga to share tomorrow."
        n "But I feel like that's too..."
        n "I don't know the word for it."
        mc "I think I know what you mean."
        n 1ba "So instead, I was going to bring three manga."
        n "And this other book."
        "Natsuki walks to her bed and kneels."
        "She reaches underneath and after a few seconds, pulls out a book."
        mc "You had that under your bed?"
        n 1bh "Yeah..."
        mc "Why?"
        n 1bm "It's..."
        n "...don't laugh, okay?"
        mc "I wouldn't."
        n 1bs "It's a book my parents used to read to me when I was younger."
        n "I don't know if it's something we should do."
        n "I could just choose a novel that everyone else knows about..."
        n "But then I wouldn't really feel passionate about it..."
        mc "I see."
        mc "I say go for it then."
        n 1bm "Huh?"
        mc "Choose the book, who cares what everyone else thinks?"
        mc "If they like it, they'll vote for it."
        "Natsuki simply stares at me."
        n 2bt "W-Well, yeah!"
        n "Who said I wasn't?"
        "It feels like she's more confident about that book now."
        n 2bk "It's not really what I want to have done as the play anyway."
        n "It would be nice, but I prefer the manga I've chosen."
        mc "What are they?"
        n 2bl "You've probably heard about them actually."
        "Natsuki rummages through the pile of books on her table."
        "She picks out three manga, all of which are the first volume."
        "I didn't really get to see them that well but it wasn't difficult to notice the big '1' on the front covers."
        mc "Are you hiding them from me intentionally?"
        mc "It kinda seems like you're keeping them hidden."
        n 2bj "It's a surprise for tomorrow."
        n "You can wait that long, right?"
        mc "I suppose."
        n 1ba "I guess I can give you a hint."
        n "They're manga that focus on a life around school."
        n "But they're all different in their own way."
        mc "Life around school?"
        "Aren't a lot of manga like that though?"
        "That doesn't really tell me anything at all."
        mc "Well...never mind then."
        n 1bb "Do you have books at home you're going to choose?"
        n "You can choose from some of the books here...if you want."
        n 1bq "You don't have to if you don't want to...okay?"
        mc "Alright, Natsuki, I got it."
        mc "I'm sure I'll find something."
        "I search through the pile of books on her table."
        "Almost every single one of them is manga."
        "A lot of them are first volumes and still wrapped in plastic."
        "I guess she couldn't really order the second one if she didn't even read the first one."
        "But there are other ways to read manga..."
        "I wonder if she's done that before."
        mc "You have a lot of manga here."
        mc "Did you ever actually get around to reading some of them?"
        n 1bk "I did."
        n "Some of them were from before everything changed like the ones I chose."
        mc "Couldn't you just...you know..."
        n 1bm "What?"
        mc "You don't have to own the manga to read it."
        mc "There are places on the internet..."
        n 1bq "You don't think I've tried that?"
        n "Yasuhiro controlled the internet in the house."
        n "It didn't exactly take long for him to figure out how to block websites."
        mc "I see..."
        n 1br "Just hurry up and choose your books already."
        mc "Okay..."
        "I manage to find two manga that I know well enough from the pile."
        "One of them is actually one of my favorite manga of all time."
        "Just because of how much it relates to me."
        "It's probably good that I have some sort of balance between manga and novels."
        "I see a novel that I think was pretty popular."
        "I haven't really read it, but it's probably good if I choose something that appeals to more people."
        "It might make the club more relatable to people if they see a play they're familiar with, even if I don't know what it is."
        n 1bk "Are you going to take two novels?"
        mc "I was gonna go for a balance, so yeah I was."
        n 1bs "Oh..."
        mc "What's wrong?"
        n 1bq "I thought you were going to take a novel and three manga like me."
        mc "How come?"
        n 2bk "I just didn't really see you as the type of person to be really into novels."
        n "Especially after you said that you read manga on the first day."
        mc "Just because I read manga doesn't mean I don't like novels."
        mc "But you're right."
        mc "I don't really read a lot of novels."
        mc "I just thought that choosing popular novels would make the play we do relatable to more people."
        mc "That is, if we do decide to vote for them."
        n 2be "That's true...but don't you want to express yourself a bit more?"
        mc "What do you mean?"
        n 2bb "You probably don't like those books as much another manga you know, right?"
        mc "That's true but..."
        n 2bo "I don't want to force you or anything...!"
        n "But you should probably think about it."
        n 2bq "It might make things easier tomorrow."
        mc "I guess so..."
        "Should I listen to Natsuki's advice?"
        "Maybe it makes more sense to choose three manga and a novel like her."
        "That way, there's still that popular novel choice but I can better express myself."
        "Or I could just keep the balance I chose, it's not like it really matters if I express myself."
        menu:
            "So should I take three manga instead?"
            "Take three manga and one novel.":
                $ ch13_natsuki_books = True
                $ natsuki_approval += 1
                mc "You're probably right."
                mc "I'll follow your lead and take three manga as well."
                mc "It'd probably make more sense if I did anyway."
                n 1bl "Really?"
                "Natsuki's face lights up."
                n 1bt "W-Well, good for you...!"
                "I search through the pile a bit more and find a suitable manga that I'm kinda familiar with."
            "Take two manga and two novels.":
                $ ch13_natsuki_books = False
                mc "I think I'll stick with the two novels."
                mc "I know the manga I want to do anyway."
                mc "So really I just chose three backups and a manga."
                n 1bk "Well, it's up to you."
                "Natsuki averts her eyes."
                n "Not like I can make you change your mind or anything."
                "I look through the pile to find another novel I think is popular."
        "I put the books I chose on her desk, away from the pile."
        "Natsuki puts the manga she took in her bag."
        n 1bc "Anyway..."
        n "We should check if that recipe is done."
        n "There's still a lot to do for Friday, after all."
        mc "You're right about that."
        n 1ba "Just leave your books here, [player]."
        n "You'll get them after we're done."
        mc "Good idea, Natsuki."
        scene bg n_livingroom
        show natsuki 1ba zorder 2 at t11
        with wipeleft_scene
        "We go downstairs to try to find Haruki."
        "I wonder what's so good about this cake."
        "And what made it worth being passed down through Natsuki's family."
        n 1bc "Mom? We're done."
        n "Are you here?"
        show natsuki zorder 2 at t21
        show momsuki 1a zorder 3 at f22
        mo "Natsuki, you're just in time."
        mo 1b "Here, I've written down the recipe for you."
        "Haruki gives a folded piece of paper to Natsuki."
        mo "Try to remember it and get rid of that as soon as you can."
        show natsuki 1bd zorder 3 at f21
        show momsuki zorder 2 at t22
        n "I will."
        show natsuki zorder 2 at t21
        "Natsuki begins to unfold the piece of paper."
        "As she does, Haruki stops her and looks at me."
        show momsuki 1f zorder 3 at f22
        mo "Not here, at least not right now."
        "Haruki points towards me."
        mo "I'd rather you did it in private."
        mo 1g "Not that I don't trust you or anything, [player]."
        mo "But it's almost like a family heirloom."
        show momsuki zorder 2 at t22
        mc "I understand."
        mc "I should probably go home then..."
        mc "You are baking a cake after all."
        mc "You two are going to be pretty busy with baking that thing and I don't really want to interfere."
        show natsuki 1bc zorder 3 at f21
        n "H-Huh? W-Wait, [player]."
        n "You don't have to go just yet..."
        n 1bs "We still have other things we need to do."
        show natsuki zorder 2 at t21
        mc "Well, what else is there for me to do?"
        mc "I know you'd much rather spend time with your mom than me, Natsuki."
        show natsuki zorder 3 at f21
        n "..."
        show natsuki zorder 2 at t21
        mc "It's not like I can stay and watch you two bake that cake."
        mc "It's a secret, isn't it?"
        show momsuki 1c zorder 3 at f22
        mo "I think [player] is right, Natsuki."
        mo "He might be better off going home and doing his assignments."
        mo "You still have those, right?"
        show momsuki zorder 2 at t22
        mc "Um...yeah."
        "Is there a reason I wouldn't have other work?"
        show momsuki 1b zorder 3 at f22
        mo "That's great."
        mo 1f "Ahaha, well, not for you obviously but at least you have something to do."
        mo "Natsuki, tomorrow you will have learned how to bake this cake."
        mo 1c "I can guarantee it."
        show natsuki 1bc zorder 3 at f21
        show momsuki zorder 2 at t22
        n "H-How can you be so sure?"
        show natsuki zorder 2 at t21
        show momsuki 1b zorder 3 at f22
        mo "Call it a mother's intuition."
        "Harsuki smiles gently."
        mo "You should get going."
        show momsuki zorder 2 at t22
        mc "Right...well, I'll see you tomorrow Natsuki."
        show natsuki 1bk zorder 3 at f21
        n "See you..."
        "I start walking towards the door."
        n 1bh "Wait!"
        show natsuki zorder 2 at t21
        mc "What's wrong?"
        show natsuki 2bg zorder 3 at f21
        n "You...left your books upstairs."
        n "Make sure you get them."
        show natsuki zorder 2 at t21
        mc "I almost forgot, thanks for reminding me."
        "Natsuki simply rolls her eyes at me."
        mc "I won't be a minute."
        scene bg n_bedroom with wipeleft_scene
        "I got my books from Natsuki's room."
        "They were exactly where I left them."
        "It's still kinda hard to believe she has such a large collection of books."
        "Even I don't have that much."
        "I'm guessing that she'll only continue to get more now that Yasuhiro won't take them away from her."
        "As I'm about to head downstairs..."
        "I start getting this strange feeling coming from Yasuhiro's room."
        "I really shouldn't check it out but I almost feel compelled to."
        "Natsuki and Haruki are busy downstairs anyway so maybe I can check it out."
        "It's not like they'll know I've been in there."
        "Just what am I getting myself into though...?"
        scene bg n_dadroom with wipeleft_scene
        "As soon as I enter the room, the strange feeling gets even worse."
        "It's as if something...or someone is crawling on my back."
        "I really should be leaving."
        "But if I don't find out why I'm getting this feeling, I might never know."
        "I search around the room looking for where it could be coming from."
        "I even opened the closet, but there was nothing in there...just some clothes."
        "I sit on the bed, about to give up on my pointless search."
        "Suddenly, the feeling gets even worse."
        "It feels like something is piercing my back."
        "My stomach feels like there's a knife being shoved through it."
        "Could it be that what I'm looking for is under the bed?"
        "Haruki was under the bed before, wasn't she?"
        "Does that have anything to do with this feeling?"
        "I check under the bed."
        "It's a bit too dark to see anything."
        "The feeling in my stomach is starting to get even worse."
        "I must be getting close to something."
        "I grab my phone and turn on the flashlight to try to see what's here."
        "I shine around the ground and see some faded marks."
        "These don't really make any sense."
        "I decide that the feeling is becoming too unbearable before I spot what I think is writing."
        "What the...?"
        "It's incredibly hard to read but it says..."
        if persistent.markov_agreed:
            "Ahaha, you are{nw}"
        else:
            "There's still hope to{nw}"
        $ _history_list = []
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        scene bg n_house
        $ pause(0.25)
        stop sound
        hide screen tear
        window show(None)
        "Hopefully we can do more tomorrow."
        window auto
        "I don't know what kind of recipe Natsuki's mom gave her but I hope it's great."
        "I think I heard Natsuki say we're baking cupcakes tomorrow."
        "That's what she said after I got my book from upstairs."
        "She probably already has the ingredients at her house."
        "Haruki will be helping us too, by inspecting them after they're baked."
        "I know she didn't say it but I think she's glad I was there."
        "She's in good hands for now with Haruki."
        "But with the discovery I made..."
        "Well, I just hope it all turns out okay."
        scene bg bedroom with wipeleft_scene
        play music t2 fadeout 0.5
        "I arrive home, just about ready to do those assignments Haruki mentioned I had."
        "It's strange, it feels like my whole life is centred around the literature club that I don't really remember doing any assignments."
        "I must be doing them though because I'm still in school and haven't really been in trouble for them lately."
        "I get my bag and take out the four books I took from Natsuki's house and place them on my desk."
        "I think these books are probably enough."
        "I should probably get started on my assignment though."
        "It isn't too hard but it might take a while..."
        "I still have to write my poem too..."
    elif ch12_outcome == 1:
        mc "Natsuki? Your dad said you'd be in here."
        "There's no response."
        mc "Anyone...?"
        n "[player]..."
        "Someone taps me on the shoulder from behind me.."
        show natsuki 2bc zorder 2 at t11
        n "What are you doing in my room?"
        mc "Natsuki!"
        mc "I thought you'd be in your room so I--"
        n 2be "Just get to the point, [player]."
        n "Why are you here?"
        "What's with this aggression coming from Natsuki?"
        "I thought she'd be happy to have her dad around but..."
        "It's almost like she's in a worst mood than before her dad became a better person."
        n 2bg "Well?"
        n "If you aren't gonna say anything, then you can leave."
        mc "What's wrong, Natsuki?"
        mc "You seem kinda mad about something."
        n 2bq "..."
        n "It's..."
        "Natsuki stops herself."
        n 1bg "...none of your business."
        n "Besides, you haven't even answered my question yet."
        n "Why are you here?"
        n 1bb "It's not like you to just visit me out of nowhere."
        n "You have to have a reason, right?"
        n "So what is it?"
        mc "Well..."
        "If Natsuki really wanted me to leave, she'd force me out."
        "It kinda sounds like she wants to keep talking but doesn't know the words to say."
        "Or that could just be my imagination."
        "Either way, there's clearly something wrong with Natsuki."
        "I wonder if I can get it out of here."
        mc "Sayori told you about what's happening on Friday, right?"
        mc "About Inauguration Day?"
        n 2bf "Y-Yeah...what about it?"
        mc "Well, I'm gonna be helping you."
        n "Helping me? What is that meant to mean?"
        mc "It means, I'm gonna help you with your preparations."
        mc "Seeing as I'm not doing anything in particular in terms of preparations."
        n 2bg "But why would you help me?"
        n "It's not like I'm your first preference."
        n "You were probably told to help me, weren't you?"
        mc "Actually...I made the choice to help you by myself."
        n 2br "H-Huh? B-But why?"
        n "You have better things to do...don't you?"
        mc "This is the best thing I could be doing, Natsuki."
        call screen dialog(message="To be continued!\nThanks for playing, keep an eye out on reddit and discord for updates!", ok_action=Quit(confirm=False))
    else:
        show natsuki 1bc zorder 2 at t11
        n "How exactly are you going to help me with the preparations, [player]?"
        mc "Huh?"
        mc "I was about to ask you the same thing."
        n 2be "Why would I know what you could do?"
        n "You were the one who chose me, remember?"
        mc "Ah...you're right."
        n "Well..."
        if ch4_name == "Natsuki":
            mc "We did something like this before, didn't we?"
            mc "I'll follow your lead as the assistant once again."
        else:
            mc "You seem to be the expert here at baking."
            mc "Why don't I just follow your lead?"
        n 2bb "I guess that's the only thing that makes sense, isn't it?"
        n "The problem is, I've ran out of supplies to bake with."
        mc "You have?"
        n 2bg "Yeah...there's really nothing left in this house."
        n "No ingredients...no parents...no--"
        mc "Maybe I can help you make a list of ingredients you need."
        "It's clear to me now that Natsuki is feeling lonely."
        "Since she lives by herself, it must be difficult to do everything around the house."
        "From what I saw downstairs, it was still just as messy as when Yasuhiro was still around."
        mc "I could also help you clean your house a little bit."
        mc "Since there's a mess downstairs."
        n 1bs "Y-You will?"
        mc "Yeah, why wouldn't I?"
        mc "It's not like we can do preparations under these conditions, right?"
        n "..."
        "This isn't really what I saw myself doing when I chose to help Natsuki..."
        "But if I can brighten her mood just a little bit..."
        "...then I guess that's enough."
        n 1bq "T-Thank you."
        mc "Don't worry about it."
        mc "I'm sure we'll have time afterwards to actually do some preparations."
        "Natsuki looks away briefly then turns back with a new look on her face."
        n 1by "Hmph."
        mc "What?"
        n 1bl "That's depending on how fast you move, [player]."
        mc "What is that meant to mean?"
        n 2bj "It means hurry up and get to work!"
        mc "R-Right..."
        mc "What's first then, boss?"
        n "The living room, of course."
        scene bg n_livingroom
        show natsuki 1bc zorder 2 at t11
        with wipeleft_scene
        "We're at her living room."
        "The mess that her dad left is actually quite terrible."
        "There's stuff all over the background and a smell of alcohol that makes it kinda difficult to breathe."
        "But the sooner we get this done, the sooner we can actually start making our preparations."
        n "Are you sure you want to do this, [player]?"
        n "You can still just leave..."
        n 1bq "I won't be mad."
        mc "I'm sure, Natsuki."
        n 1bc "Okay then..."
        "The two of us start collecting all the bottles and cans lying around and put them in a bag."
        "We're here for several minutes, making sure we look under the furniture for anything we missed."
        "Eventually, I put the last bottle of alcohol into the bag."
        mc "And that's that done."
        mc "Though..."
        "I take a deep breath through my nose."
        "The overwhelming smell of alcohol is still there."
        mc "The smell is still there."
        n 2bd "I know just the thing to get rid of it."
        n "Wait here!"
        mc "W-Wait--"
        show natsuki at lhide
        hide natsuki
        "Before I can finish my sentence, Natsuki runs off to the kitchen."
        "I guess she must have something to clear the air."
        "Or at the very least, reduce the smell of the alochol."
        "I take one last look at her living room."
        "Despite the smell and the stains of alcohol, it's actually in good shape."
        "The furniture isn't broken or anything like that."
        "Still, the fact that it even went to this state in the first place is worrying."
        "Just how bad was Natsuki's father...?"
        "Soon enough, Natsuki comes back holding something in her hand."
        show natsuki 1ba zorder 2 at t11
        n "Behold!"
        "Natsuki presents the thing she's holding."
        mc "I have no idea what that is."
        n 1bd "It's an air freshener!"
        mc "It doesn't look like one."
        n 1be "Well, that's because it's not your normal air freshener!"
        n "You leave it in a room and let it work it's magic."
        n "Then you come back after a while and the smell should be good!"
        mc "That's certainly interesting."
        mc "I didn't think your dad would be the type to be leaving those type of things around."
        n 1bg "That's because...he doesn't."
        n "I'm the one who has to take care of these sort of things around the house."
        n "He used to get me to clean everything..."
        mc "So you have a supply of these things?"
        n 1bs "Yeah..."
        n "But anyway, we're done in this room."
        n "It's time for my parent's room upstairs."
        mc "If you say so..."
        n 1bt "Come on."
        n "If we don't hurry up, we won't have any time to do any preparations."
        "Natsuki grabs my hand and begins to pull me upstairs."
        "Just what have I gotten myself into...?"
        "I never knew someone could be so excited to clean their house."
        "I wonder how she'll react to Yasuhiro's room though..."
        n 1bl "Ready?"
        mc "Ready as I'll ever be."
        n "Good, let's get to work."
        scene bg n_dadroom
        show natsuki 1bc zorder 2 at t11
        with wipeleft_scene
        "The cheerful Natsuki outside the room suddenly goes quiet as she looks around the room."
        "I notice the smile on her face slowly fade away."
        "It kinda looks like she's trying hard not to cry."
        n "You know, I haven't been in here since he was taken away."
        n "It's weird but I think that if I go in here, I'll get yelled again."
        n 1bg "I know there's no way he can hurt me anymore but..."
        mc "It's conditioned into your brain, right?"
        n 2bh "Um...I guess you could put it like that."
        "Natsuki sighs."
        n "I used to make it a habit to try to take some books from here."
        n "Anything I ordered or that wasn't directly related to school was put in here."
        n 2bq "All the volumes of manga I've never read..."
        n "They're all on that shelf."
        "Natsuki points to the shelf that is fully stocked with books."
        "I can see unopened volumes of manga and other novels that haven't been touched at all."
        "Some are still in their plastic wrapping, waiting to be opened."
        mc "Why risk getting hurt for a book, Natsuki?"
        n 2bs "There's two reasons, [player]."
        mc "Two reasons?"
        n 4bw "The first one should be obvious."
        n "I was talking what was rightfully mine back."
        n "At least temporarily."
        n "I ordered and paid for those books, I have a right to read them."
        mc "I don't think your father--"
        mc "I mean, Yasuhiro...agreed with that right."
        n 4bu "Obviously not."
        n "Sometimes I would get away with it and actually manage to read the manga."
        n "Other times I'd read it but he would notice that something was wrong."
        n 4br "Maybe the plastic wrapping was gone or some other really small detail."
        mc "He really paid attention to that kind of thing?"
        mc "That seems really petty."
        n "There's a reason for that."
        mc "It doesn't seem like a good one."
        n 1bq "It's because when my mom left, he turned into some kind of investigator."
        n "He would search for clues and any other detail to try to figure out where she went."
        n 1bn "Eventually he gave up and turned his attention towards me."
        mc "That wasn't a good thing, I suppose."
        n 1bm "Not at all."
        n "Once he stopped searching for her, he started using his newly gained skills of investigating to start making my life difficult."
        mc "How did he do that?"
        n 1bq "He made some stupid rules up that I had to follow."
        n "I didn't take him seriously at first and that's when he first started to beat me."
        mc "I'm sorry to hear that."
        n "Whatever, it's in the past now."
        n 1bs "It's not like you can change that."
        mc "If I could..."
        n "There's no point thinking about what could have been."
        n "It just makes everyone bitter, [player]."
        mc "I guess..."
        n 1bq "Anyway, he was able to figure out when I broke one of his stupid rules because he could investigate if anything was wrong."
        n "That was anything...taking too much snacks, getting a manga from his room or even leaving something in the wrong place."
        n "And when I broke his rules...you can guess what happened."
        mc "He really gained that much skill in investigating from looking for your mom?"
        n 2bt "He was really dedicated when he was searching for her...and I admired him for it."
        n 2bu "But that admiration turned into resentment."
        mc "Yeah, I can see why."
        mc "With all the terrible things he did to you, there's no way I can imagine you keeping that admiration."
        n "Yeah..."
        mc "You don't have to tell me the second one."
        mc "But I do want to know what it was."
        n 2bk "Why are you so interested?"
        mc "I just want to know more about your situation, Natsuki."
        mc "I guess it's kinda interesting to me in a weird way."
        n 2be "Interesting, eh?"
        n "Then promise me you'll help me clean up {i}everything{/i} in this room and I'll tell you everything."
        mc "Just like that?"
        mc "I thought you'd be more secretive about it."
        n 2bc "To be honest, it's good to say what I've been keeping a secret for so long."
        n "Now that he's gone, there's no risk of getting hurt."
        mc "Then...I promise."
        "I was going to help her anyway."
        "I get the feeling she knew that too but just wanted a reason to say what she's saying without seeming like she wants to."
        n 2bh "Well..."
        n "It's silly but..."
        n "I almost thought of it like a game."
        mc "A game?"
        mc "What do you mean?"
        n 4bk "When I was younger, I'd play these games with my parents."
        n "I'd take something they wanted for attention and then hide."
        n "It would never end up leading to anything serious except a short talk about not doing it again."
        n "But...I'd keep doing it."
        mc "Sounds like you were pretty mischievous as a kid."
        n 3bh "It didn't hurt anyone and it was fun!"
        n "Sometimes they wouldn't find me or wouldn't go looking for it and I'd always give it back."
        n "So taking a book from Yasuhiro's room and reading it was sort of the same thing...in a messed up kind of way."
        mc "That is..."
        n 3be "I know it's a stupid reason."
        n 3bt "But it reminded me of better times."
        "Natsuki smiles faintly."
        n 3bq "It's hard to say all of this. It's like I'm trying to prove myself to myself."
        n "I guess that's part of the reason I told you..."
        n "So that I could hear my own reasons for getting beaten and how stupid they sound."
        n 1bu "How far...Yasuhiro would go to hurt me and how dumb I am for thinking it's all a game."
        mc "There's nothing wrong with that."
        n 1bm "Huh?"
        mc "I mean, there's obviously something wrong with Yasuhiro hurting you but your reasons..."
        mc "They shouldn't matter."
        mc "Do you want to know what I think?"
        n "What...?"
        mc "I think there was still a tiny bit of Yasuhiro that still cared for you like his daughter."
        mc "Maybe it was only a tiny piece of him but it was there."
        n "What makes you think that?"
        mc "He sent you to school, didn't he?"
        mc "And he obviously cared about you enough to be investigating your every move around the house."
        mc "So in a messed up kind of way, I think he did care..."
        n 1bs "Maybe..."
        n "But I think the only reason he sent me to school was so he could have the house to himself for a few hours."
        n "Not to mention he'd use that time to check if anything was wrong with basically anything in the house."
        n 1bq "Still, I think you're right."
        n "I don't know what it is but I think he did care."
        n "There's no point wondering if he really did though, seeing as his chance to prove it is long gone."
        mc "I suppose he can prove himself in another life."
        "There's a brief silence between us as neither of us know what to say."
        n 1bj "So, we're here to clean this room."
        n "It's not like anyone is really going to use it but it's better to have it clean than dirty, right?"
        n "So why don't you start with the area near the bed and I'll start at the bookshelf."
        "The area around the bed is probably the messiest part of this room while the area around the bookshelf is the cleanest."
        "In fact, the bookshelf is in near perfect condition."
        mc "You have a hard job."
        n 1bb "You said you'd help clean if I told you."
        n "So don't complain."
        n "I'm going to get a basket or something to get some of these books out of here."
        mc "Why not just leave them in here?"
        n 1bc "It gives me a bad feeling just going in here."
        n 1bd "Anyway, I'll be right back."
        show natsuki at lhide
        hide natsuki
        mc "I guess I'm on my own for now."
        "The smell of alcohol isn't as strong here than it was downstairs."
        "I guess Yasuhiro didn't drink so much in here."
        "The smell is still noticeable though."
        "Not only that, but it also feels like something died in here."
        "At least that's the feeling I'm getting."
        "I don't know if Yasuhiro was crazy enough to actually kill someone."
        "And with all the time spent looking for his wife, I doubt he was the one who killed her."
        "I don't even know if someone actually died in here, it's just a feeling I'm getting."
        "Maybe I should mention this feeling to Natsuki when she comes back."
        "I don't know how she'll respond, she might agree or think I'm completely crazy..."
        "But it doesn't matter, I have to know why I'm feeling like this."
        "Though I should probably clean some of the room before she gets back."
        if talkabout_natsuki_house[0]:
            "There's something else..."
            "I can't shake this feeling in my head that I've been here before."
            "I don't really remember being in here but..."
            "It all seems so familiar for some reason."
            "Like I've been in here in a dream or some distant memory."
            "It might just be my head playing tricks on me..."
            "After all, I did just suggest that something died in here."
            "I'm going to try to take my mind off everything except cleaning until Natsuki gets back."
        "I decide to move the bed to the side so I can clean under it."
        "But as I start cleaning the area under the bed..."
        "I start to notice some marks underneath the bed."
        "They seem to be carved onto the ground with something sharp so I can't erase them."
        "It's like a tally, all over the floor."
        "There's even some writing that I'm not really able to read."
        "I wonder what this could be?"
        "Maybe Yasuhiro kept track of how many days Natsuki's mom was missing for?"
        "Counting them all, it seems to total to something over fifty."
        "Did he really search for her for over fifty days...?"
        "It must have been terrible watching him slowly become hopeless and turn into a monster over fifty days..."
        "I can't imagine what that would be like."
        "As I finish replacing the sheets and getting rid of the smell of alcohol, I notice something even more strange."
        "It's a perfect drawing of an eye and somehow it even has color."
        "It's separated from the rest of the markings with a huge space."
        "The iris is colored carmine and there's a faint metallic smell coming from it..."
        "Could that be...blood?"
        "Just what the hell was Yasuhiro doing?"
        n "[player]? I've got the basket...!"
        "I can hear Natsuki approaching from the hallway."
        "Should I clean this?"
        "I can quickly get rid of the blood and just pass the eye off as part of the other markings."
        "I could even cover it the whole time so that she can't see it."
        "Or maybe I should tell Natsuki?"
        "Should she know what Yasuhiro was doing in here?"
        "Would that be good for her? Telling her that Yasuhiro was performing some kinda blood ritual?"
        menu:
            "What do I do...?"
            "Tell Natsuki.":
                $ ch13_cleaneye = False
                "I should tell Natsuki."
                "She deserves to know what Yasuhiro did and to find out just how much of a monster he is."
                "It will help her move on...right?"
            "Clean it.":
                $ ch13_cleaneye = True
                "I have to get rid of it."
                "If she sees this then she'll lose all the respect of not just Yasuhiro but her father too."
                "I quickly wipe off the blood from the eye just as Natsuki is walking in."
        show natsuki 1bc zorder 2 at t11
        n "Hey, [player]..."
        n "What's that on the floor there?"
        "Natsuki drops the basket and drops to the floor next to me."
        if ch13_cleaneye:
            mc "Well, I think Yasuhiro marked how many days your mom was gone for."
            mc "That's just a guess, since I don't know how long he actually searched for."
            n "Hmm...did you count how many markings there were?"
            mc "I counted at least fifty."
            n 2bk "Fifty...that's about how many days he spent looking for her."
            n "I didn't know he marked it on the floor under his bed."
            n 5br "What a freak."
            "That was unexpected."
            "I wonder how she would have reacted if I showed her the eye..."
            mc "I guess he was just desperate and wanted a way to stay sane?"
            n 5bs "Scraping out a tally on the floor is not sane, [player]."
            mc "I guess so..."
            mc "There's also some writing that I can't really read."
            "Natsuki looks at the writing for a moment."
            n 5bm "Yeah, I can't read that either."
            mc "Is it your Yasuhiro's handwriting?"
            n "It kinda looks like it."
            n "But I'm not sure."
            mc "Well, he was the only one in here, right?"
            mc "So it must have been him."
            n 5bg "You're probably right."
        else:
            mc "There's something here you should see, Natsuki."
            n "What is it?"
            mc "Yasuhiro was marking the floor."
            mc "I don't know what for exactly but I counted at least fifty marks."
            n 1bg "Fifty marks?"
            n "He searched for my mom for over fifty days."
            n 1bh "Maybe he was keeping track of it."
            mc "By scraping the ground?"
            n "He became more and more different as the days passed on."
            n 5br "What a freak."
            mc "There's more, look."
            "I point to the writing on the floor."
            mc "Is that Yasuhiro's handwriting?"
            n 5bk "It kinda looks like it."
            n "But I'm not sure."
            mc "Can you read any of it?"
            mc "I can't make out a thing."
            "Natsuki looks at the writing for a moment."
            n 1bq "No, I can't read it either..."
            n "It might not have been him who wrote it."
            mc "He was the only one in here, right?"
            mc "So it must have been him."
            n 1bg "You're probably right."
            n "I really have to wonder just how much my mom leaving affected him."
            mc "There's more, Natsuki."
            n 2bc "There is...?"
            n "I thought that was the worst of it."
            mc "Well, there's also this..."
            "I move over so that Natsuki can see the perfect eye with blood."
            "She looks at and doesn't say anything for a while."
            n 2be "What the hell is that?"
            mc "It looks like some kind of eye."
            n "In the middle, that's blood, isn't it?"
            n 4bo "Now that I'm closer to it, I can smell it."
            mc "I think it is."
            n "This is crazy, [player]!"
            mc "That's what I thought when I saw it."
            mc "I thought about getting rid of it so you wouldn't have to see--"
            n "See that my dad was doing some blood rituals?"
            "Natsuki looks both shaken and angry."
            n 4br "No, this is just insane."
            n "I thought the tally and the writing was bad but this..."
            n "..."
            n "That could be my blood, too..."
            mc "Was Yasuhiro...part of a cult or something?"
            n 2bo "No!"
            n "Of course not!"
            n "At least...not that I knew of..."
            "Natsuki turns away from the eye and stands up."
            n 1br "What's even more creepy is that it's a perfect drawing."
            n "It looks so realistic..."
            n "And I know Yasuhiro, he was no artist."
            mc "Maybe it wasn't him?"
            n 1bs "Who else could it have been...?"
            "There's no way for me to answer that question."
        call screen dialog(message="To be continued!\nThanks for playing, keep an eye out on reddit and discord for updates!", ok_action=Quit(confirm=False))
    return

label ch13_exclusive_yuri:
    scene bg residential_day
    with wipeleft_scene
    play music t6 fadeout 1.0
    "Yuri and I make our way to my house."
    if ch4_name == "Yuri":
        "She's been here before, during the first week of the Literature Club."
        "Back then, the circumstances were different but..."
        "We're still doing the exact same thing."
        "Though it's almost like she knows the way to my house better than I do."
        "She's wasting no time and is taking all the right turns and shortcuts..."
    else:
        "She hasn't been here before...at least, I don't think she has."
        "Yet she knows the way to my house almost better than I do."
        "She was stepping ahead of me and making all the right turns."
        "Or that could have just been my imagination."
    show yuri 3pf zorder 2 at t11
    y "Is something wrong, [player]?"
    y "You look deep in thought."
    mc "O-Oh, it's nothing."
    mc "Just some random thoughts I'm having."
    mc "You probably don't need to worry about it."
    y "You know you can tell me whatever is on your mind."
    mc "It's better if you don't worry about it."
    mc "We're almost at my house anyway."
    y 3pq "Y-Yeah..."
    y "Just take this turn and--"
    y "I mean, it's around here, isn't it?"
    mc "Yeah...it is."
    mc "You sure know your way around here, don't you Yuri?"
    y "Ah..."
    mc "I think that's a pretty good skill to have."
    y 3pt "Huh?"
    mc "A sense of direction."
    y 3pq "R-Right...!"
    y "A-Anyway, we should get going."
    mc "My thoughts exactly."
    scene bg house
    with wipeleft_scene
    "We arrive at my house."
    "Yuri seems worried for some reason."
    mc "Is everything okay?"
    show yuri 2po zorder 2 at t11
    if visited_yuri_hospital:
        y "I just feel a little strange being here."
        y "Like it's wrong, somehow."
        mc "What do you mean?"
        mc "What's wrong with me helping you?"
    else:
        y "I...don't know what it is."
        y "I just feel strange being here."
        y "Like there's something wrong, somehow."
        mc "Eh? What do you mean?"
        mc "Is there something wrong with me helping you?"
    y "There's nothing 'wrong' about that."
    y 2pv "It's just this feeling that I can't shake."
    if ch4_name == "Yuri":
        y "That this has all happened before and that it led to something terrible."
    else:
        y "Like this could have happened before and led to something terrible."
    mc "Yuri, I honestly have no idea what you're talking about."
    mc "Though I do feel kinda strange."
    if visited_yuri_hospital:
        mc "But it's no big deal."
        y "You can say it, [player]."
    else:
        y "W-What is it?"
    mc "Well..."
    y 3pf "[player], just tell me."
    mc "Alright...it might have just been my imagination but the club meeting we had to today..."
    y "What about it?"
    mc "Didn't it feel familiar to you?"
    mc "There was a part in the meeting that seemed like an exact copy of what happened before."
    mc "In the first week of me as a member."
    mc "Do you remember?"
    y 3ph "Umm..."
    y "I don't..."
    y "Why...?"
    "Yuri puts a hand on her head."
    y "[player], what's going on...?"
    mc "Y-Yuri, are you okay?"
    y 3pn "I don't know."
    y "I'm trying to remember the time you're speaking of."
    y "It's not working."
    mc "Maybe we should head inside."
    y "That sounds like a good idea."
    scene bg bedroom
    show yuri 3pv zorder 2 at t11
    with wipeleft_scene
    mc "How's your head, Yuri?"
    y "I can't think properly..."
    y "I'm trying my hardest to remember but I...can't."
    mc "It doesn't matter anymore, Yuri."
    mc "Just forget about it, maybe your head will get better."
    y 3pt "That's the thing [player]!"
    y "It's like I've just forgotten what happened."
    mc "E-Eh...?"
    y 2po "I don't know if my mind is playing tricks on me or what..."
    y "And honestly, that's a very scary thought."
    mc "How come?"
    y "Think about it."
    y "If you can't even rely on your own mind, then what are you?"
    y 2pw "You're just a husk of yourself, a slave to--"
    mc "Yuri, I think you're overthinking this a little bit."
    mc "Maybe I am as well."
    mc "If making you think about the first week makes you uncomfortable, then we can just avoid that topic altogether."
    mc "Besides, we aren't really here to talk about what happened in the first week."
    mc "We're here to discuss your preparations and choose a book, right?"
    y 2pt "Y-Yeah, I suppose you're right."
    "Yuri's frown slowly disappears."
    y 3ph "But before we do that, I need to ask {i}you{/i} something, [player]."
    mc "Huh? What is it?"
    if monika_type == 0 or monika_type == 1:
        y 3pe "Do you think Sayori has been acting a little different lately?"
        mc "Sayori acting strange...?"
        mc "What do you mean?"
        y "What you said earlier, about the events that happened in the first week..."
        y "It's placed a theory in my head about my memories."
        mc "Yuri, didn't we just--"
        y 3pv "[player], just answer the question."
        y "I want to settle this."
        mc "Ah..."
        "I think of Sayori and how she acts."
        "I've always known her to be a carefree person who really didn't care about life."
        "I just didn't think that she would be depressed because of that..."
        "I really was some kind of jerk back then for not realizing."
        "Anyway, back to what Yuri asked me..."
        "Lately, Sayori has been more serious."
        "I don't know if that's because she's taking her responsibility as the president of the club more seriously or..."
        "Hold on a second..."
        y 3pf "You look like you're concentrating."
        mc "I am..."
        mc "Something isn't right."
        y "So there is something weird going on with Sayori?"
        mc "I don't know..."
        mc "But to answer your first question, yes."
        mc "She has been acting differently."
        mc "I don't think that has--"
        y 3pg "So I was right."
        mc "Yuri, what's your theory?"
        y 3pf "I'm not sure exactly how it works but with your confirmation that Sayori has been acting differently..."
        y "I think that has something to do with why my memory is all over the place."
        mc "I don't think those two have any correlation at all."
        mc "It just doesn't make any sense."
        y 3pq "I'm likely grasping at straws here."
        y "I just thought I'd tell you what's on my mind."
        mc "I appreciate it...I guess."
        y "If anything comes from it, I'll let you know."
        "What in the world is Yuri talking about?"
        "It's good she's being open with me but what she's talking about just makes no sense."
        "Maybe I should focus on doing the preparations."
    else:
        y 3pf "Do you think that Monika has been acting kinda strange lately?"
        mc "Strange? In what way?"
        y "Surely you've noticed, right?"
        y "She's been more hostile and started being more cold...?"
        mc "I can't say I've noticed that."
        mc "To me, she's just the same Monika I met on the first day of being in the Literature Club."
        mc "Friendly and as helpful as ever."
        y 3pn "W-What...?"
        y "[player], you can't be serious."
        mc "I am fully serious, Yuri."
        y 3po "I don't..."
        y 2pr "I refuse to believe that."
        y "Sure she may still look the same but you haven't noticed any behavioral differences in her?"
        mc "Yuri, I suggest you leave this topic alone."
        y 2pt "What did you say?"
        mc "I said you should leave this topic alone."
        mc "It's for our own good."
        y "Our own good?"
        y "[player], what are you saying?"
        mc "Nothing is wrong, Yuri."
        mc "We should just discuss something else."
        if visited_yuri_hospital:
            mc "How about talking about the preparations we were going to--"
            y 2pn "[player], there's something incredibly wrong with you."
            y "I don't know what it is but since we're together, I can't just ignore it."
            mc "I have no idea what you're talking about, Yuri."
            show yuri 3pp at h11
            y "Stop acting like there's nothing wrong."
            y "There's something clearly messed up in all of this."
            y "Come to your senses, please!"
            "Yuri starts shaking me."
            y 3pv "You remember that day at the mall, right?"
            y "When we dropped that knife in the water together?"
            mc "..."
            y 3pw "I said I was going to become a better person afterwards."
            y "I can't do that without you, [player]."
            y "I need the real you."
            mc "I don't understand."
            y 3pt "W-What?"
            mc "I can't think properly, Yuri."
            mc "I don't understand."
            y "[player], that's you isn't it?"
            y "The real you?"
            mc "I don't..."
            y "Please be okay, [player]."
            mc "I...{nw}"
            stop music
            scene black
            with close_eyes
            $ pause(4.0)
            play music t6
            scene bg bedroom
            show yuri 3pq at face
            with open_eyes
            y "You're awake!"
            show yuri 3ps zorder 2 at t11
            y "I was worried..."
            mc "W-What happened?"
            mc "I can't remember anything since we got into the house."
            y 2pt "You don't?"
            y "Then..."
            "Yuri looks at me worriedly."
            y 2pu "That's probably for the best."
        else:
            mc "How about talking about the preparations we were going to do?"
            y 3pt "I..."
            "Yuri looks pensive."
            y 2pv "Okay..."
            y "That's what we came here to do after all."
            y "So it's for the best..."
        "Was Yuri talking about something...?"
        "I can't recall even though this conversation started just a couple of moments ago..."
        "I get the feeling that I shouldn't think about it."
    mc "Anyway, let's get back to what we came here to do in the first place."
    y 2pu "Yeah..."
    "Yuri looks around my room."
    y 2ph "Are these all the books you have in your house?"
    y "Just the ones on that shelf over there?"
    mc "Well..."
    "There are lots of books on the shelf that I haven't really looked at before."
    "A lot of those books are some novels that were gifted to me in the past for special occasions."
    "I never really got around to reading them."
    "The other type of books I have there is manga, which I don't think Yuri would be particularly interested in."
    "Though anything seems to be possible these days."
    "What's on the bookshelf is not a very big collection..."
    mc "On second thought, maybe we should have gone to your house."
    mc "Or maybe the library..."
    y 3pa "I-It's fine, [player]."
    y "I actually thought something like this would happen."
    mc "Something like what?"
    y 3pb "I know this sounds like something out of a film but..."
    y "I always carry lots of different novels with me to school."
    y "It kinda depends on my mood as to what I bring."
    y 3pc "But this time around I brought five different novels."
    mc "Novels?"
    y 3pq "I-Is that a problem...?"
    mc "No, not at all!"
    mc "It just sounds too convenient for the occasion."
    y "Like I said...it sounds like something from a film."
    y "But that's why I didn't mind going to your house for this."
    y 3ps "If you want, you can select from my books as well."
    y "I'm sure Sayori wouldn't really mind if we only bring three or four books each."
    mc "You're probably right."
    mc "I might as well take a look at your books then."
    y 2pa "Go ahead..."
    y "I have other books at home, if you don't like any of these choices."
    mc "I'm sure I can make something work with what we have here."
    "I look through the books Yuri brought with her."
    "They all have one thing in common just judging from the cover..."
    "They're all horror books."
    "Even the name of the books give me an eerie feeling."
    "I guess I shouldn't have expected anything less from Yuri."
    mc "These are..."
    y 2po "They're terrible, aren't they?"
    y "I'm sorry..."
    mc "No! I never said that."
    mc "I haven't even read them so I can't judge them properly."
    mc "I was just going to say they're all horror books, aren't they?"
    y 2pq "Y-Yeah...you know that's the type of thing I like to read, right?"
    mc "I guess so."
    mc "I was just curious."
    mc "Have you read any of them?"
    y 1u "Actually, I've read all of them."
    mc "Eh? So why did you bring them to school...?"
    y "Sometimes, I like to reflect on what I've already done."
    y "I find that reading a book helps me focus, in a way."
    mc "Not this again..."
    y 1q "N-No, it's not like that...!"
    y "I just meant these books are really good."
    y "So I like rereading them from time to time."
    y "In fact, I'm surprised you haven't heard of these novels."
    mc "Why not...?"
    y "Well...they're among the most popular horror books."
    y 4pa "I even selected these in particular partly because of that."
    mc "You selected these in particular...? For what reason?"
    if visited_yuri_hospital:
        y "I thought I could introduce you to more horror books."
        y "Since we're spending so much time together and I spend a lot of my own time reading..."
        y 4pb "Maybe we could read horror books together...?"
        y "It's just...."
        y 4pe "I just want us to have more to talk about, seeing as we're together."
        mc "I understand your reasons."
        mc "I think it's really nice of you, Yuri."
        mc "I enjoy spending time with you so the more things I can do with you, the better."
        y "T-Thank you, [player]."
        y 3ps "I wasn't sure how you would take it..."
        y "Maybe when we're deeper in our relationship I can introduce you to books that are more suited to who I really am."
        mc "Who you really are? What do you mean?"
        mc "Aren't these types of books the type to represent who you really are?"
        y 3pt "Ah...like I said before..."
        y "I only chose the most popular horror books because I wanted to ease you into it."
        mc "I see..."
        mc "What about that first book you gave me...?"
        y "First book?"
        mc "Yeah, during the first week you gave me a book."
        mc "Wasn't that a horror book as well?"
        y 2pv "I don't like to think about back then..."
        y "I gave you the book and look what happened..."
        y "All you did was spend time with Monika."
        mc "It wasn't because of the book, Yuri."
        y "I like to think it was...maybe I was coming on too strong or--"
        mc "You're overthinking it, Yuri."
        mc "There's some reason I chose to spend time with Monika, even if I don't fully understand it yet."
        y "What? You think there's a reason you {i}had{/i} to spend time with Monika?"
        mc "I don't know..."
        y 2pt "It's just..."
        "Yuri stops and looks at my face."
        "I don't know if it's showing but I'm getting uncomfortable for some reason."
        "I'm interested in the topic but it's almost like I shouldn't talk about it."
        y "I-I'll stop..."
        y "You clearly look flustered and the last thing I want to do is make you uncomfortable."
        y 3pu "Let's just go back to selecting some books for the day."
    else:
        y 2pq "Ah...I thought that maybe..."
        y "I could get...the people in the Literature Club interested in horror books."
        y "So you and I could have more to talk about."
        y 2pp "I mean--"
        y "So that everyone else could talk to me about something if they met me outside the club."
        mc "I see."
        mc "I'm not sure everyone feels the same about horror books."
        y 3pv "Oh..."
        "Yuri frowns."
        mc "As for me, I don't really know what to think about them."
        mc "I don't remember the last horror book I read..."
        y 3pw "I just thought that selecting these horror books, due to their popularity..."
        y "I could slowly get people to start reading the type of genre I like."
        mc "Are they particularly scary to read?"
        mc "People might not like what you've got to offer because they might not be able to mentally cope with what's happening."
        y 3pt "I...didn't really think about it like that."
        y "I just really wanted--"
        "Yuri looks away and sighs."
        y "Why did you choose to spend your time now with me, [player]?"
        y "And give me the real reason, please."
        mc "I really thought you needed the most help, Yuri."
        mc "That's the real reason, I promise."
        y 2pw "..."
        y "It's not the answer I'm looking for..."
        y "But I suppose it just confirms everything."
        mc "What do you mean?"
        y "There's no point talking about it anymore."
        y 3pu "Let's just go back to selecting some books for the day."
    mc "Okay, Yuri."
    mc "Let's have a look at all the books we have here then."
    "I start taking books from the shelf and placing them on my bed."
    y 3pt "Are you sure that's a good idea?"
    y "You're going to have a lot of work to do putting them all back."
    mc "It's not a problem...not like they were organized to begin with."
    y 3pq "Ah..."
    y "You should really organize your bookshelf, [player]."
    mc "I think it's fine the way it is."
    mc "I rarely take stuff out of it anyway."
    "I finish placing the last of the books from my shelf on the bed."
    "Yuri puts her five books on my bed in a separate area."
    "Presumably to help distinguish which ones are hers and mine."
    y 2pf "Even with all your books..."
    y "It looks like there's only about thirty or so that would be suitable for the play."
    mc "Yeah...the collection is rather small."
    mc "I'm not really the type to collect books."
    y 1q "You have several volumes of manga though..."
    mc "That's about the only thing I actually collect."
    y "Alright..."
    y 1s "You're probably going to choose some of the manga you laid out, right?"
    mc "Well...not only that."
    y "It's fine."
    y 2pa "After all, we'll still be voting for the book we're going to do."
    y "It doesn't mean what you choose will be what the Literature Club agrees on, right?"
    mc "Yeah, you're right."
    y 3pc "So choose whatever you want."
    y "I'll go after you."
    mc "Are you sure you want to give me the choice of your novels?"
    y 3pf "If you choose one of my novels, I'll be voting for it anyway."
    y "So the choice here doesn't really matter."
    mc "I suppose..."
    "Yuri brought these books here, almost because of this exact circumstance."
    "It would feel wrong not to take one of hers at the very least."
    "Am I really interested in the horror genre?"
    "I don't really know the answer to that question."
    menu:
        "So I guess I'll..."
        "Take one of Yuri's books.":
            $ ch13_yuri_books = True
            $ yuri_approval += 1
            "I decide to take one of Yuri's books."
            "The one I chose looks the most tame out of all of them."
            "I also take three of my own books, two of which are mangas."
            "The third one was a popular book series that someone gifted me that I never got around to reading."
        "Select from my own books only.":
            $ ch13_yuri_books = False
            "I don't really feel comfortable choosing Yuri's books."
            "I definitely appreciate her bringing them but it feels weird taking something I have no particular interest in."
            "I decide to select three volumes of manga from different series and a novel from a popular book series."
            "I never actually got around to reading all of it, but I think choosing something that appeals to a general crowd could be good."
            "It also feels wrong selecting four different manga while Yuri is here for some reason."
    y 1e "So those are your choices?"
    y "In that case..."
    "Yuri selects the books that she brought."
    y 2pa "I'll just take these ones."
    mc "I kinda expected that."
    y "It's not like you have bad taste or anything..."
    y 2pq "It's just..."
    mc "I know, you don't really read these types of things."
    mc "I won't judge you for it."
    if ch13_yuri_books:
        y 3ps "I'm surprised you took one of my books."
        y "I honestly was expecting you to just go with four volumes of manga."
    else:
        y 3ps "I'm surprised you took out a novel from your pile of books."
    mc "Well, I want to have something other than manga."
    mc "To give myself some form of variety I guess."
    y 2pf "That's not necessary in my opinion."
    y "You should choose your books based on how they express you as a person but I'm getting off topic..."
    y 2pi "I think we should discuss the decorations we're going to be doing on the day."
    mc "Yeah, I think you're right."
    y "So..."
    y 3pe "What kind of atmosphere do you think we should have?"
    mc "I mean, that kinda depends on the book we choose, doesn't it?"
    y 3pq "Ah...you're right."
    y "Those words just slipped from my mouth."
    mc "Well, we could always make a list of the stuff we could potentially use."
    mc "That way, when we vote tomorrow we don't need to think of one when we go shopping for them."
    y 3pb "That's a great idea."
    y "But where to start...?"
    mc "How about some scented candles?"
    mc "Those aren't generally specific to a type of play, right?"
    y "Right! And how about some banner paper so we can make a banner themed by the book?"
    y "And some markers of lots of different colours...!"
    mc "Now you're getting it."
    mc "You seem to be quite excited about this."
    y 3pf "I'd like to show everyone what I can do and with you here..."
    if visited_yuri_hospital:
        y 3pq "W-Well, it's nice, you know?"
        y "Spending time with you while doing something I'm interested in..."
        y 3ps "What more could I ask for?"
        mc "That means a lot, Yuri."
    else:
        y 3pu "It just adds a little extra excitement."
        mc "I see..."
    "Yuri and I start writing down the list of items we could use."
    "I doubt we'll be able to afford all of these but the more ideas we get, the less chance we have of forgetting something."
    "That's the idea behind writing down all these items, anyway."
    y 2pg "Let's see..."
    "Yuri looks at the list."
    "It's been over an hour. We even used a computer to look for some items online that could be useful."
    "At this point, we've written down almost two pages worth of decorations."
    y 2pa "I think that's enough."
    y "We've pretty much covered everything."
    "Yuri hands me the list and I look through it."
    "There's all sorts of stuff in here from paint, to balloons and cardboard."
    "The stuff we get all depends on the book we choose tomorrow."
    mc "Yeah, I think that's all we need."
    mc "Do you think we'll have enough money to buy what we need?"
    y 2po "Y-You're going to put in some money?"
    mc "Of course!"
    mc "After all, we are doing this together. That includes paying."
    y 2pq "Thank you, [player]."
    mc "Don't mention it...I still wonder if it's enough though."
    mc "Sayori said she was going to help everyone..."
    mc "So maybe she can help with some of the expenses?"
    y 3pq "I feel bad that you're willing to spend your own money already but getting Sayori to contribute too?"
    y "Isn't that taking advantage of her?"
    mc "Ah...I didn't really think about it like that."
    mc "I just thought that since she wanted to help, that..."
    y "There's no need to say it. I want Sayori's help with expenses too but the two of us will have to make do."
    mc "Maybe we can talk to her tomorrow about it."
    y "Sounds like a plan."
    "Yuri smiles bashfully."
    y 2ps "It looks like we're done here."
    mc "Yeah, seems that way."
    "Yuri looks at the books on my bed."
    y 2pv "I-I'll help you put those back on the shelf."
    mc "You don't--"
    y 2pu "I insist."
    "Yuri starts putting the books on the shelf neatly."
    "She puts them in order of the author's surname."
    "I don't even get to help as she does it all by herself."
    y 3pa "That should do it."
    mc "Thanks for your help..."
    y 3pb "It's no problem."
    "Yuri grabs her bag."
    y 3pu "Anyway, I'm all ready to go."
    mc "I'll walk you out."
    scene bg house with wipeleft_scene
    "After a strange afternoon, Yuri is about to leave."
    if visited_yuri_hospital:
        "Even if it wasn't the most intimate time ever, I'm glad I got to spend it with Yuri."
    else:
        "I'm glad I chose Yuri to help. It seemed like she had a lot to think about in terms of the atmosphere."
    "After all that's happened so far, I'm glad the time we spent at my house was mostly normal."
    show yuri 3pa zorder 2 at t11
    y "I suppose this is where we part ways, [player]."
    mc "Yeah..."
    if visited_yuri_hospital:
        y 3pb "It was nice spending this time with you, [player]."
        y "I'm not really sure if you chose me because we're together or because you really thought I needed your help..."
        y "But regardless, I want to thank you."
        mc "I think it's a little bit of both."
    else:
        y 3pq "It was good working with you, [player]."
        y "We got quite a list compiled after all of that."
        mc "I feel the same, Yuri."
        y 3pv "{i}(If only you did...){/i}"
    y 2ps "Anyway..."
    y "I'll see you at the club tomorrow."
    mc "Let's make sure we ask Sayori for the type of help she can give."
    y "That's a good idea."
    y "I-I'll be going now."
    mc "Goodbye, Yuri."
    show yuri at lhide
    hide yuri
    "Yuri begins to walk away."
    "She gives me one more wave before she disappears behind a corner."
    "I wonder how everyone else is doing with their preparations."
    "Are they going to be okay on their own?"
    "I'm sure everyone is more than capable of doing their own task."
    "I should trust that they will do the best they can."
    "Should I have helped someone else though?"
    "Sayori seems like she has a lot to do."
    "Helping everyone..."
    "Maybe I should have--"
    "Never mind, I already said that they're capable of doing their own things."
    "Sayori sounded confident she could do it alone so I shouldn't worry about it."
    "I guess I should get back to my room."
    "I still have to write a poem after all."
    if ch13_yuri_books:
        "I should also read some of that book that Yuri gave me."
        "Just to see if I should actually bring it in tomorrow..."
    return

label ch13_exclusive_monika:
    scene bg residential_day
    with wipeleft_scene
    play music t6 fadeout 1.0
    "We decided to go to Monika's house for the preparations."
    "It's the most logical decision since she's the one practicing the piano."
    "It's not like I have any equipment at home to help her with that."
    "The walk to Monika's house from the school took a lot longer than I thought it would."
    "Since she said it was around the same distance from my house to the school, I was expecting to get there quickly."
    "The actual distance might be the same but the amount of turns makes it almost seem doubled."
    if monika_type == 0:
        show monika 1a zorder 2 at t11
        m "Sorry for making you go all this way just to help me, [player]."
        m 2e "To be honest, we could have gone to your house but..."
        m "I wanted to get some practice in for the piece I'm going to play."
        m "I hope you don't mind too much!"
        mc "Ah, no, that's fine."
        mc "After all, I'm the one helping you."
        mc "It would make sense that we go to {i}your{/i} house after all."
        m 2j "Ahaha, if you say so."
        "Monika smiles meaningfully."
        m 2a "Anyway, my house is just around here..."
        m "Not too far now~"
        mc "Right..."
        "I wonder what \"not too far\" actually means to Monika..."
        "I guess I shouldn't be complaining..."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1ha zorder 2 at t11
        m "You keeping up okay, [player]?"
        m "You look a little tired."
        mc "Ah..."
        mc "It's fine. I just wasn't expecting to walk this far."
        m 2hb "Well, I wasn't lying about the distance to my house."
        m "Ahaha, though I may have omitted how far we would actually have to travel."
        m "I hope it's not too much of a problem."
        mc "Not at all..."
        m 2hc "We could have done this at your house but..."
        m 2he "...I'd like to get some practice in tonight."
        mc "It's fine, don't worry about it."
        m 5ha "Thanks, [player]~"
        m "It really isn't too far now."
        m 3ha "Just a couple more turns."
        "I have to wonder what \"too far\" really means to Monika."
        "Not that I should be complaining..."
    else:
        show monika 1a zorder 2 at t11
        m "Having trouble keeping up, [player]?"
        m 1b "Come on, we have to be the ones who stand out."
        mc "Right..."
        m "You did choose to help me after all."
        m 2b "I know the walk is a long way..."
        m "But we're almost there."
        mc "Do you walk to school everyday?"
        m "Of course!"
        m "It's a nice little exercise and helps get me ready for the day."
        mc "I see."
        "It's been quite a few minutes since we've started walking."
        "Trying to keep up with her pace is difficult..."
        "But I shouldn't complain."
    "After all, I did choose her."
    show bg new_house with wipeleft_scene
    if monika_type == 0:
        show monika 1a zorder 2 at t11
        m "We're finally here!"
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1ha zorder 2 at t11
        m "And we're here!"
    else:
        show monika 1a zorder 2 at t11
        m "We've arrived."
    "Monika's house does not seem particularly impressive."
    "It looks nearly identical to the houses around it."
    "That said, it's definitely not a bad house."
    "It's just not somewhere I thought Monika would be living in, given her...popularity."
    if monika_type == 0:
        m 4b "Ahaha, welcome to my humble abode~"
        "Monika looks at me quizzically."
        m 2c "You look kinda confused there, [player]."
        m "Is something wrong?"
        mc "N-Nothing."
        mc "It was just a random thought."
        m 2e "Well, you can share it with me."
        mc "It's about your house."
        m 2f "Ah..."
        "Monika turns back and looks at her house."
        m 2g "It isn't quite what you expected, is it?"
        m "You probably thought someone like me would live in a mansion?"
        m 1m "Because of my popularity, right?"
        mc "I'm sorry."
        mc "I didn't mean to imply anything--"
        m "No, it's okay."
        m 1n "I was the one who told you that you could tell me."
        m "I guess I should have been prepared for anything..."
        m 2o "It's just..."
        m "Well, nobody really knows the {i}real{/i} me."
        mc "Monika..."
        m 2q "Not even {i}you{/i}."
        m 2f "All I've been showing you is..."
        m "Well, we should head inside first."
        mc "...Okay..."
        show monika at thide
        hide monika
        "That was a pretty sudden mood shift from Monika."
        "Did I say something to cause that?"
        "I hope not, otherwise working together is going to be incredibly awkward."
        scene bg m_livingroom with wipeleft_scene
        "Her living room isn't big but it's actually a lot more spacious than it looks."
        "There are bits and pieces lying everywhere and a keyboard in front of the TV."
        "Honestly, I thought the place would be cleaner."
        "I thought Monika would have prepared in case something like this happens."
        "I suppose it's not really a big deal."
        show monika 1n zorder 2 at t11
        m "It's not a clean place, I know."
        m "I've been working super hard the last week and I wasn't exactly expecting you to come over today."
        m "Sorry, [player]."
        mc "It's no big deal, Monika."
        mc "I also think you misunderstood me outside."
        mc "I really don't dislike your house, I was just making an observation."
        m 1e "Well...if you say so."
        m 1f "Sigh..."
        m 1o "I'm sorry if I took it the wrong way."
        m 2p "I've just been under a lot of pressure lately."
        m "You know, with all that's been happening."
        m "I guess hearing anything negative outside of the Literature Club just tipped me over the edge."
        mc "I didn't know you were affected that much."
        mc "I certainly didn't mean to hurt you, Monika."
        m 2q "I know..."
        "I notice a keyboard in the middle of the room."
        "There seems to be some neatly made sheet music on it."
        "Is this what she's been practicing this whole time?"
        m 2e "Yeah...that's my keyboard."
        m "It's what I use to practice the piano, since a real piano is way too expensive."
        mc "I understand."
        mc "What's the sheet music you've got on it?"
        m 4a "It's actually something I've made myself."
        m "I've been practicing it quite a bit but no one has been around to listen to it."
        mc "You've made your own song already? That's really impressive."
        m 4b "Ahaha, thanks [player]~"
        m "But don't praise me too much! And it's just a piece for now, without lyrics yet."
        m 3i "The piece is actually rather easy to play...and that's coming from a beginner!"
        m "I almost feel bad playing it for the day, when I could do so much better."
        mc "So why don't you play a different one then?"
        m 1e "I could..."
        m "But I need you to hear this at least once."
        m "So this will be the piece I play on the day."
        mc "I assume you're going to learn some shorter songs to accompany it?"
        mc "This song, I mean piece, is probably the centrepiece, right?"
        m "That was the idea I had in my head."
        m 1m "But I don't really know if it'll work."
        mc "Well, I think it's a great idea."
        mc "Maybe I could help you search for smaller pieces that are easy to play."
        mc "It's really the least I can do."
        m 1j "Ahaha, you being here is enough for me."
        m "I-I mean having an audience to practice in front of is always good for giving me confidence."
        m 1a "But I guess you could still look for those pieces if you really want to though."
        mc "I'm on it, Monika."
        m 1c "Actually...before that..."
        m "Do you want to hear the start of the piece?"
        m 1e "Y-You don't have to, if you want to reserve it for the day."
        mc "Um..."
        menu:
            "Should I listen to some of it now?"
            "Yes.":
                m 1a "Alright...here goes nothing."
                "Monika moves towards her keyboard, takes a seat and repositions the sheet music."
                m "I call this piece \"Your Reality\" and I hope you like it~"
                m 1j "It's pretty much finished already but I'd like to keep most of it a surprise."
                play music "<to 9.0>bgm/credits.ogg" noloop
                $ pause(9.0)
                play music t6 fadeout 2.0
                "Monika smiles and stands from where she was sitting."
                m 2e "So...what do you think?"
                m "It was just a preview but..."
                mc "Monika, I think that piece is going to be perfect."
                mc "It was only the first ten seconds and I could already tell it was going to be amazing."
                m 2l "Ah...you're too kind."
                mc "I'm serious. It really did sound great!"
                m 2e "Thanks, [player]~"
            "No.":
                m 2f "Ah..."
                m 2e "I get it, don't worry."
                m "We still have work we need to do for today..."
        m "Anyway...!"
        m "You still need to get some books for the play."
        mc "What about you?"
        m 1a "Well, since I'm home I might as well make myself comfortable."
        m "I'm going to go upstairs and change into some different clothes."
        m "You can stay here and look for some books to bring tomorrow."
        "Monika points towards a bookshelf."
        m 1b "See that bookshelf over there?"
        m "It's got plenty of books you could bring tomorrow."
        m "I'm sure you can manage to find something that you like."
        m "See you soon."
        show monika at lhide
        hide monika
        "Monika heads up the stairs."
        "I walk towards her bookshelf and I only just realize just how much literature is here."
        "There's all sorts of books here, from fiction to tutorial books."
        "I wonder if Monika actually bought all of these for the club or if she made the club because she had so much literature."
        "Nothing really catches my eye on her shelf though."
        "There's a lot of popular book series on it, so I might look at those if I don't find anything else."
        "Suprisingly, there's also manga on the shelf."
        "I didn't really take manga as something Monika would collect but I guess it counts as literature."
        "What should I choose though?"
        "I guess an even spread of manga and novels would do."
        "That way I don't look bias one way or another...but there's not really many interesting choices in terms of manga."
        "Monika has several ones they go to the first or second volume only."
        "I decide to take volume one of a manga that has been adapted to an anime and another manga that I've read the first couple of volumes for."
        "I also grab the two most popular novels I know of from the shelf."
        mc "This should do..."
        "They're probably not the best choices. They don't really represent me as a person."
        "But the day isn't about me anyway, it's about the Literature Club."
        "The more people that understand what out play is about, the more likely they'll be interested in joining."
        "At least, that's how I see it."
        "I sit down on Monika's couch and wait for her to arrive."
        "I look over the four books that I chose. One of them is a horror novel, another one adventure."
        "The two manga I chose are about romance and the other about fantasy."
        "I think that covers everyone's interest in the club."
        "I'm not too interested in what we actually perform so it doesn't matter what I choose in the end."
        show monika 1ba zorder 2 at t11
        m "I'm back~"
        m "Have you chosen your books yet?"
        mc "Yeah, have a look."
        "I show Monika the four books I picked from her shelf."
        m 1be "Interesting choices..."
        m "It doesn't really tell people about you, does it?"
        mc "I wasn't really thinking for myself."
        mc "I was thinking for the people who were going to see the Literature Club."
        m 2bd "Ah...you think more people will join if they can relate to what we're performing?"
        mc "Yeah, that was my thought process behind it."
        m "Getting people to join shouldn't be the priority for the day."
        mc "I thought the whole point in participating in the event was to get more members, right?"
        m 2ba "While that's true, you should still consider yourself."
        mc "I'm not sure I follow..."
        m "If you don't express yourself, then you'll just be a person who goes along with the crowd."
        m 2be "While there isn't anything inherently wrong with that, don't you want to be different?"
        m "Don't you want to stand out, to be unique?"
        mc "Ah..."
        mc "I don't think I'm really suited to do that kinda thing."
        mc "It's just not who I am."
        mc "I'm fine with fitting in with the crowd if it means I can get through life."
        m 4ba "I suppose we all have different ways of living our life."
        m "I just thought I'd share what I thought."
        mc "I didn't take any offense to it, don't worry."
        m 4bb "Well, that's good."
        m "Anyway, I still have to choose some books for the play."
        m "It shouldn't take me too long. I already have a few in mind after all."
    elif monika_type == 1 and ch12_markov_agree:
        m 1hl "Welcome to my house~"
        m "I know it isn't much..."
        m 1hm "It probably isn't what you expected either."
        mc "I don't know what I expected."
        m 2hf "Probably something that would fit a popular person like me, right?"
        m "Maybe a mansion or...at least something more impressive than this."
        mc "It's not like that."
        m 2ho "Despite everything...{i}you{/i} don't really know much about..."
        m 2hq "Well...me."
        mc "I didn't mean to offend you..."
        m 1hm "I know."
        m 1hn "It's just people expect a lot from someone like me."
        mc "The house isn't even that bad."
        m 1ho "Sigh..."
        m "We should go inside before we waste any more time out here, [player]."
        show monika at thide
        hide monika
        "I didn't realize she was sensitive about her property."
        "It was just a comment, I didn't mean any offense."
        "I just hope she doesn't hold a grudge or this whole night is going to be incredibly awkward."
        scene bg m_livingroom with wipeleft_scene
        "Her living room isn't big but it's actually a lot more spacious than it looks."
        "There's bits and pieces lying everywhere and a keyboard in front of the TV."
        "Honestly, I thought the place would be cleaner."
        "I thought Monika would have prepared in case something like this happened."
        "I suppose it's not really a big deal."
        show monika 1hc zorder 2 at t11
        m "The house isn't exactly cleaned up, I'm sorry for that."
        m 2he "I hope that doesn't affect the preparations we're going to do."
        mc "It's fine. I don't really think it's a big issue."
        mc "After all, I don't expect you to have your house clean when you weren't really expecting guests."
        m "Ahaha, well I suppose you're right."
        "I notice the keyboard Monika has setup in the room."
        "There appears to be some sheet music with several handwritten notes on them."
        "Just how much has she been practicing?"
        m 1ha "I'm still quite a novice at the piano, if I'm honest."
        m "Though I am getting better!"
        m 3hb "I'm actually writing my own piece right now."
        mc "Are you planning to play it for the day?"
        mc "Or maybe you're looking for something easier...?"
        m 3ha "I was kinda doing this for a special occasion, to mark something."
        m "But with the circumstances, that doesn't seem to be possible."
        m 4he "I guess the day will have to do, if I want my part to be satisfactory."
        mc "So is that all you're going to be playing on the day?"
        m "Of course not!"
        m 2hc "I was thinking of playing some smaller, easier pieces to accompany the main piece."
        m "I don't really know what I should do, nor do I particularly mind."
        m 2hb "Which is where you come in!"
        mc "Me?"
        m 2ha "Yeah! You could be the one who finds me some pieces to play."
        m "As long as they aren't that difficult, I should be able to learn the piece I want to play and the ones you find too!"
        mc "S-Sure, but I don't know if I'd trust my own taste in music."
        mc "You might not like what I find."
        m 2he "Like I said, I don't really mind."
        m "As long as it's easy and doesn't take away from what I'm going to play."
        mc "Speaking of which..."
        mc "How long have you been practicing it for?"
        mc "I noticed there was a lot of handwritten notes on the sheet music so it looks like you worked on it a lot."
        m 1ha "You're quite observant, [player]!"
        m "I was quite busy last night just trying to come up with this piece."
        m 1hl "In fact, I didn't actually get much sleep because of it."
        m 1hm "It's also why the room is in a..."
        m "...less than ideal state."
        m 1hn "I want to apologize again for that."
        mc "I don't blame you."
        mc "It must have been hard work to compose your own song."
        m 1he "Ahaha, yeah it was a little bit. And it's just a piece, not a song, silly~"
        "Monika's face suddenly lights up."
        m 1ha "Actually, do you want to hear a little bit?"
        m "It's still a bit rough but I think I've got this first part pretty much perfected!"
        m "I mean...you don't have to."
        menu:
            m "But I'd like to give you the choice~"
            "Yes.":
                m 1hb "Well...here goes nothing."
                "Monika approaches her keyboard and takes a deep breath."
                "She turns it on before looking at me and smiling."
                m "The title is \"Hear Me, My Love\"..."
                m "It could still change but I think it fits, for now~"
                play music "<to 9.0>mod_assets/bgm/15.ogg" noloop
                $ pause(9.0)
                play music t6 fadeout 2.0
                m "So...what did {i}you{/i} think?"
                mc "That was amazing, Monika."
                mc "I'm sure once you finish practicing it, everybody will love it."
                m 2he "Ahaha, I hope so."
            "No.":
                m 1hf "Ah...that's fine."
                m 2he "I'm sure you're probably waiting for when it's done, right?"
        m "Anyway...!"
        m "We still have to get some books for the play, right?"
        m "I've actually got a pretty big collection of books right over there."
        "Monika points towards a bookshelf."
        m 2ha "You can look through that bookshelf later. It's got quite the collection and I think you'll find something you like."
        m "In the meantime, I thought I'd show you this one."
        m 4hb "You've probably seen it before, so maybe you can tell me your thoughts on it."
        "Monika searches her bag and pulls out a red book after a few seconds."
        "It doesn't look at all familiar."
        "It's hard to make out because it looks kinda faded but I think the cover has some ominous looking eye on it."
        m "You don't recognize it, do you?"
        mc "Should I?"
        m 4hc "If I--"
        m 4hd "If {i}she{/i} did everything properly, then you wouldn't."
        m 4hh "It's a little annoying that she actually managed to get rid of one of the copies of this book."
        m "Not to mention that she wiped your memory of it, removing almost all my influence in this world."
        m 3ha "{i}Almost{/i}..."
        mc "W-What are you talking about?"
        m 3hb "[player] had a copy hidden somewhere, while I still had him under my influence."
        m "It was quite difficult to find, but not impossible..."
        m 3hn "After all, they give off a familiar type of...radiation I guess is the best way to describe it."
        mc "M-Monika, I have no clue what you're talking about."
        mc "It's kinda creepy, if I'm honest with you."
        m 1ha "Like it matters."
        m 5ha "I'm not even talking to you, after all."
        show monikared zorder 5:
            alpha 0
            linear 2.0 alpha 0.3
        $ currentpos = get_pos()
        play music mkov fadeout 2.0 fadein 2.0
        m "Ahaha~"
        m "Now I can tell you what I want to do on Inauguration Day."
        m "Aside from playing the piano, of course."
        "Monika smiles meaningfully."
        "I find myself staring at Monika's smile."
        "It's really easy to lose myself in it..."
        m "Now we have all the privacy we could want."
        m 1hb "By now, you've locked yourself into an ending that might be undesireable."
        m "Ahaha, at least for everyone else."
        m 2hb "For us, it'll be like a new beginning."
        m 2hm "I don't quite understand these feelings."
        m 4hn "But I'm learning to accept them."
        m 4he "Being with you, they're only getting stronger."
        m "Maybe it's a weakness, adopted from Monika."
        m "But..."
        m 4hm "This feeling of love, I can't help it any longer."
        m "After you chose to help me yesterday and accept my offer, it's just become an overwhelming feeling."
        m 2hn "I even did my hair this way to try to get you to like me more."
        m 2ho "I'm being irrational and wasting my time."
        m 2hp "This piece I'm composing is even for you..."
        m 2hq "Yet..."
        m 1he "I don't regret any of it."
        m "As long as I fulfill my goals and end up with you..."
        m "Nothing else matters."
        m 1hl "Ahaha, sorry."
        m "I seem to have gone on a tangent, haven't I?"
        m 1hm "It's just become a little hard to focus my thoughts."
        m "Anyway, back to what we were discussing..."
        m 1hn "My plan."
        m "Take a look at this book, I'm sure you know what it is."
        $ style.say_dialogue = style.edited
        "Monika gives me the red book she's holding in her hands."
        "Looking at it more closely, I can see that it's titled \"Portrait of Markov\"."
        $ style.say_dialogue = style.normal
        m 1ha "[player] is going to need to read this."
        m "But not like it matters at this point..."
        m "I've already set up everything so that you can't change what's going to happen."
        m 1hc "I mean...you did see that file I made, right?"
        m 1he "I suppose since you're working with me, I can tell you more about the book."
        m 2he "It clearly isn't just an ordinary book, as you probably know."
        m "Within it, I've stored a part of...the {i}real{/i} me."
        m "So that whoever reads it will come under my influence."
        m 2ha "What I am isn't important, just know that I have that kind of ability."
        m "You already know what I'm talking about."
        m 2hc "After all, I'm not {i}really{/i} Monika anymore."
        m "Even though I can't help but act like her..."
        m 2hm "Speaking of which, I apologize for getting upset at you..."
        m "...or rather {i}[player]{/i} outside."
        m 2ho "It just brought back some terrible memories from..."
        m "Well...before everything that I'd rather not think about."
        m "That's besides the point."
        m 2hc "I'm almost certain Sayori has a copy of the book."
        m "She probably got it from Yuri...and I think she read some of it."
        m "Despite that, I can't...really influence her."
        m 1hd "I think it's got something to do with being the president, and all the power you get from it."
        m "What matters is that we still have this one copy of the book available to us."
        m 1he "Two would be better, but one is enough."
        m "Once he reads the book, I'll have a way to get through Sayori."
        m 2ha "I can't be certain but I think she's going to end it after Inauguration Day."
        m "Since everyone will have their 'happy' ending."
        m 4hl "Pathetic."
        m "..."
        m 3ho "You know, I'm not actually certain that this whole plan of mine will work."
        m "Sayori has changed since the first week you joined."
        m 1hq "She's become more independent, more cunning and more intelligent."
        m "To everyone else, she's still the same..."
        m 1hr "That makes her really hard to deal with."
        m 1hp "But I admit...I'm getting desperate."
        m "Even with all this knowledge and extended power, there's still so little I can do by myself."
        m 1hm "But if everything goes well..."
        m "Then I'll be inaugurated as the president of the Literature Club."
        m 2he "Ahaha, the whole day was my idea of course."
        m "I'll tell you more later."
        m 2ha "Right now, [player] needs to find some books."
        m "After all, Sayori might get suspicious that she can't see what [player] is up to."
        m 4hb "So..."
        m "Thanks for listening~"
        "What just happened?"
        "It's like...I wasn't myself."
        hide monikared
        $ audio.t6c = "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
        play music t6c fadeout 0.5
        m 5ha "Any of the books on the shelf over there are ones you can choose."
        m "Despite the small house, we do have a lot of books!"
        mc "Ah..."
        "I grasp my head. I feel like I just had a huge headache."
        mc "...Not to be rude but what were we talking about again?"
        mc "I may have stopped listening."
        m 5hb "You missed my whole explanation?"
        m "I can't believe you."
        mc "I-I think I heard the end of it..."
        mc "I can probably figure it out."
        m 1hc "[player], is something wrong?"
        m "It looks like you've hurt your head."
        mc "I don't know..."
        mc "It just started hurting all of a sudden."
        show monika 1hf
        "Monika looks at me worriedly."
        m "I've actually got something for headaches."
        m "Do you want it?"
        mc "That's too kind of you but I can't just accept something like--"
        m 1he "It's okay! I insist."
        "Monika walks over to the kitchen and takes some tablets and a glass of water."
        m "Here, take it."
        m "It might help your headache."
        m "I need to go upstairs quickly, so try to find some books while I'm gone."
        mc "Thanks, Monika..."
        m "Get better soon, [player]."
        show monika at lhide
        hide monika
        "Monika starts heading for the stairs."
        "I don't know what are in these tablets."
        "Monika said that they're for my headache...there's no reason she'd lie to me."
        "I put them in my mouth and drink the water she gave me."
        mc "Hopefully that fixes things soon..."
        "I put the red book I'm holding into my bag."
        "How did this even get on my hand?"
        mc "Let's see what books Monika has."
        "I walk towards her shelf and quickly realize she wasn't lying."
        "A lot of books, both old and new, are here."
        "I've even read some of the books she has which just goes to show how much of a collection she has."
        "She even has a volume of manga here and there."
        "I'm actually surprised at just how much literature Monika has."
        "Why she's so passionate about literature makes a lot more sense now."
        "I don't really know what to grab from the shelf."
        "I'm usually into manga but maybe it would be a good idea to grab a novel..."
        menu:
            "What do I do...?"
            "Pick some manga.":
                "I reach out my hand for a manga I'm vaguely familiar with."
                $ style.say_dialogue = style.edited
                "No, this is a terrible idea."
                "I should grab a novel instead."
                "Nobody wants to read a manga."
                $ style.say_dialogue = style.normal
            "Pick some novels.":
                pass
        "I grab a novel that looks familiar to me from the shelf."
        "It's one of the more popular ones, so I'm sure everyone will know what it is."
        "Sayori said to pick a couple so I guess I'll just pick other ones that look interesting."
        "..."
        "Soon, I've selected four novels from the shelf."
        show monika 1bha zorder 2 at t11
        m "Hi [player]~"
        m "Have you finished choosing your books?"
        mc "Ah...yeah."
        m 1bhd "Can I see what you chose?"
        "I show Monika the four books I took from her shelf."
        m 2bhb "Interesting choices!"
        m "You probably chose them based on their popularity, right?"
        mc "Is it that easy to tell?"
        m 2bha "Ahaha, it doesn't matter too much."
        mc "I don't really read much...or at least I didn't, until this whole play thing."
        mc "So I thought that choosing books that everyone has heard of would make things easier."
        m "That makes sense! It would make it easier to relate to the club."
        mc "Yeah, that's sort of what I was going for."
        m 2bhc "I still have to pick some books..."
    else:
        m 1c "I know what you're thinking."
        m "This house isn't something that suits someone like me, right?"
        mc "W-What?"
        m 1h "[player], I can almost read you like a book."
        m "That look on your face says it all."
        mc "But--"
        m 2h "Honestly, it's fine."
        m "I know the situation I'm in."
        m "...And I plan to get out of it."
        mc "Monika, the house is fine."
        mc "I didn't know you were so sensitive about this kind of thing."
        m 2o "It's not that, [player]."
        m "It really isn't."
        "Monika looks at the house for a moment."
        m 2m "Well, we should get inside."
        m "We have quite a bit to do."
        show monika at thide
        hide monika
        "What was that?"
        "It was like she read my mind..."
        "If I had known she would have taken offence to something like that I never would have thought about it in the first place."
        "Well, it's too late for that now..."
        "The only thing I can do is hope this doesn't ruin the preparations tonight."
        scene bg m_livingroom with wipeleft_scene
        "Her living room isn't big but it's actually a lot more spacious than it looks."
        "There's bits and pieces lying everywhere and a keyboard in front of the TV."
        "Honestly, I thought the place would be cleaner."
        "I thought Monika would have prepared in case something like this happened."
        "I suppose it's not really a big deal."
        show monika 1l zorder 2 at t11
        m "I know the place is a bit...messy."
        m "There's just been a lot of stuff going on lately and I haven't had the chance to clean up."
        m 1e "Ahaha, if I knew you were coming then..."
        m "Well, never mind."
        "I look at Monika's keyboard and notice she has some sheet music."
        "I wonder what she's been trying to learn..."
        m 2e "I'm not {i}that{/i} great at playing the piano yet."
        m "I can't just come up with a tune off the top of my head, you know."
        mc "Ah...I know."
        mc "I was just wondering what you were learning to play in your spare time."
        m 2a "Actually..."
        m "I was thinking of learning lots of smaller tunes to play on the day."
        m 4b "And a longer, more iconic piece as the main attraction..."
        m "...at least for my part."
        mc "So you want me to find you some smaller tunes?"
        m 4e "It would definitely help me!"
        m "But [player], they shouldn't be too hard."
        m "We only have a couple of days to do this, after all."
        # Rude correction to MC somewhere
        mc "What's the song you're going to play?"
        m 4a "What I've been practicing..."
        m "It seems fitting."
        mc "That's a good coincidence."
        m 3b "Yeah..."
        mc "How long have you been practicing this one song?"
        m "Hmm..."
        if monika_type == 1:
            m 3m "Ahaha, actually not very long."
            m "I spent a lot of time last night working on it."
            m 3n "At least, getting it to an acceptable level of practice."
        else:
            m 3n "...Since mid last week!"
        mc "I wonder how it sounds..."
        m 1a "It's getting there, you know."
        m "But since you mentioned it..."
        menu:
            m "Do you want to hear a little bit of it?"
            "Yes.":
                m 1b "Well...here goes nothing."
                "Monika approaches her keyboard and takes a deep breath."
                "She turns it on before looking at me and smiling."
                m "I call this piece \"I'm Coming For You\" so I hope you like it~"
                play music "<to 9.0>mod_assets/bgm/16.ogg" noloop
                $ pause(9.0)
                play music t2 fadeout 2.0
                m 1a "What do you think?"
                m "It's only a short bit but I hope you liked it."
                mc "That was amazing, Monika."
                mc "I'm sure once you finish practicing it, everybody will love it."
                m 1j "Ahaha, I hope so."
            "No.":
                m 1e "Ah...that's fine."
                m "It's probably best that it's kept as a surprise."
        m "Anyway...!"
        m 2c "We should probably sort out the books we want to perform for the play."
        m "I have a couple in mind that I think the club members might want to read."
        "Monika walks towards a pile of books she has."
        "She pulls out a couple but none really stand out to me."
        if gave_book_to_monika:
            m 2b "I particularly like this one."
            m "So thanks for making it easier for me."
        else:
            m 2d "This one was quite difficult to find."
            m "I even had to refurbish it a little bit."
        "She pulls a red book from the pile. The cover is plain, just a simple eye on it."
        "It's titled \"Portrait of Markov\"...it sounds familiar but I know I haven't seen anything like that before."
        m 2m "And...well, if you don't like that sort of thing..."
        m "I've got some other choices."
        "Her other choices are just some popular fictional books."
        "I haven't read any of them but since they're well known, I have heard of them."
        m 1c "Now then..."
        show monika g8
        show markovred zorder 5:
            alpha 0
            linear 2.0 alpha 0.3
        $ currentpos = get_pos()
        play music mkov fadeout 2.0 fadein 2.0
        if ch12_markov_agree:
            m 1a "Here's where I tell you my plan."
            m "Seeing as you've already chosen to accept my decision."
            mc "What are you talking about?"
            m 1c "Oh right..."
            m 1b "One moment."
            "Monika shows me an almost evil smile."
            m "That should do it."
            m 2a "There's no way for you to change it."
            m "Even if you get that 'other' Monika, it'll all end the same."
            m 2b "I know your limits, and so I've set this up so that you can't win."
            m 2j "Unless, of course...you're on my side."
            m "You've already made up your mind by this point, right?"
            m 1a "You're with me until the end."
            m "The others might not like it, but it's what you chose."
            m "So...let's get started."
            m "As you already know..."
            m 1b "This book isn't just another book."
            m "Within in, I've stored a part of myself so that people who read it will..."
            m 3a "Well...let's say they won't be themselves anymore."
            m "You probably already know what I'm talking about, don't you?"
            m 3b "You've realized that I'm not really Monika."
            m "I'm just gonna guess that Sayori knows about this book."
            m 3c "One of the copies I made...well, it's gone."
            m 1h "Or at least, I can't feel it's existence anymore."
            m "That doesn't really matter."
            m "What does, is that we still have two copies that we can use."
            m 1i "The one I'm holding...which belonged to [player]."
            m "And the one that Monika read, that she tried to get rid of."
            m 1j "I've kept it in a secure location, which you don't need to know about."
            m "After all I'll be giving you this one."
            $ style.say_dialogue = style.edited
            "Monika gives me the red book."
            $ style.say_dialogue = style.normal
            m 1a "The plan is simple."
            m "Just get [player] to read it again."
            m "Ahaha, wait a second..."
            m 1b "It's not like you'll actually get a choice on whether or not he does that."
            m "Because he {i}will{/i} be doing that, no matter what."
            m "After [player] reads the book, I'll have a way to get past Sayori."
            m 2m "I'm not certain it will work yet but it's really my only option."
            m "After the day, I'm sure Sayori is going to end this whole 'helping' everyone thing and I'll lose my chance."
            m "So I have to count on you."
            m 2n "It's a risky move...but at this point I'll admit I'm a little desperate."
            m "Since you chose to spend time with me, it makes planning this whole thing a lot easier."
            m 2j "It also means Sayori will be less suspicious about the whole thing."
            m 1c "Once Sayori is taken care of..."
            m 1a "I'll be the President of the Literature Club."
            m "I don't know what that means but something is telling me it's going to give me great power."
            m 1b "With that sort of power, I will have anything I could ever want in this world."
            m 1f "But this all means nothing, if Sayori knows what's going to happen..."
            m "So I'll let her see what's going on..."
            m 1j "And...done!"
            "What just happened?"
            "It's like...I wasn't myself."
        else:
            m 1h "I don't know why you chose me."
            m "Do you really just want to help me?"
            if monika_type == 1:
                m 1i "If it's because you think I still love you, don't get your hopes up."
                m "I'm learning to overcome these feelings."
            m "If only you chose differently yesterday..."
            m 1j "Ahaha, it doesn't matter."
            m "I still have my own plans for Inauguration Day."
            m "I'll do them with or without your help."
            mc "What do you mean?"
            m 2a "Things are already set in motion, [player]."
            m "I just hope you're on the right side of things when it all happens."
            mc "I honestly have no idea what you're talking about right now."
            mc "Does it have anything to do with your preparations?"
            m 2b "Ahaha, you have no idea."
            m "I suppose I should be more careful what I say around you."
            m "After all, she could be watching."
            m 2e "So let's just..."
            "..."
            "What just happened?"
            "I completely forgot what we were talking about."
        hide markovred
        $ audio.t6c = "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
        play music t6c fadeout 0.5
        m 2a "So, just choose a couple of books that you like."
        m "I have a bunch on my shelf over there."
        m 5 "I know the house is a little small, but we do have a lot of books!"
        mc "Um...sorry, what were we talking about?"
        mc "I think I zoned out a little bit."
        m 5b "Eh? Did you miss my whole explanation?"
        m "I can't believe you!"
        mc "Ah...I heard the end of it."
        mc "I'm sure I can figure it out."
        m 2h "If you say so..."
        "Monika heads for the stairs."
        mc "Where are you going?"
        m 2q "If you were listening, I said I was going to change my clothes."
        "Monika frowns."
        m 1f "Sorry."
        m "I guess I'm just a little pressured about this whole thing."
        m 1g "And what you said outside--"
        mc "I didn't even say anything..."
        m 1m "R-Right but..."
        m 1n "Well, never mind!"
        m "Just try to find some books before I get back."
        mc "Alright..."
        show monika at lhide
        hide monika
        if ch12_markov_agree:
            "I put the red book I'm holding into my bag."
            "How did this even get on my hand?"
        mc "Let's see what books Monika has."
        "I walk towards her shelf and quickly realize she wasn't lying."
        "A lot of books, both old and new, are here."
        "I've even read some of the books she has which just goes to show how much of a collection she has."
        "She even has a volume of manga here and there."
        "I'm actually surprised at just how much literature Monika has."
        "Why she's so passionate about literature makes a lot more sense now."
        "I don't really know what to grab from the shelf."
        "I'm usually into manga but maybe it would be a good idea to grab a novel..."
        menu:
            "What do I do...?"
            "Pick some manga.":
                "I reach out my hand for a manga I'm vaguely familiar with."
                $ style.say_dialogue = style.edited
                "No, this is a terrible idea."
                "I should grab a novel instead."
                "Nobody wants to read a manga."
                $ style.say_dialogue = style.normal
            "Pick some novels.":
                pass
        "I grab a novel that looks familiar to me from the shelf."
        "It's one of the more popular ones, so I'm sure everyone will know what it is."
        "Sayori said to pick a couple so I guess I'll just pick other ones that look interesting."
        "..."
        "Soon I've selected four novels from the shelf."
        show monika 1ba zorder 2 at t11
        m "Hi [player]~"
        m 2bb "Are you done selecting your books?"
        mc "Ah...yeah."
        m "Can I see what you chose?"
        "I show Monika the four books I took from her shelf."
        m 2bc "Interesting choices."
        m "You probably chose them based on their popularity, right?"
        mc "Is it that easy to tell?"
        m 2be "Ahaha, it doesn't matter too much."
        mc "I don't really read much...or, at least, I didn't until this whole play thing."
        mc "So I thought that choosing books that everyone has heard of would make things easier."
        m 4ba "Ah, I see. You're being considerate towards everyone else."
        mc "You could say that."
        m 4bd "Well, now I need to think of some books to choose..."
    m "In the meantime, why don't you use my laptop and come up with some pieces I could play?"
    mc "Alright..."
    show monika at lhide
    hide monika
    "Monika moves towards the bookshelf and starts browsing the books."
    mc "What kinds of pieces should Monika play...?"
    "Her laptop is sitting on the desk in front of her television."
    "The pieces I choose should be easy, so it doesn't take away from her main performance."
    "I guess some basic piano pieces could do?"
    "I'm the one choosing for her..."
    menu:
        "So I need to look up some sort of genre, right?"
        "Harmonic.":
            $ ch13_music_type = "harmonic"
            "I suppose a harmonic atmosphere would make sense for the day."
            "After all, we're trying to bring people together to join the club."
        "Upbeat.":
            $ ch13_music_type = "upbeat"
            "An upbeat piece would probably do the trick."
            "It would show that the club isn't just all about literature and that it's pretty exciting."
        "Melancholy.":
            $ ch13_music_type = "melancholy"
            "An emotional piece might attract a lot of people."
            "They would be interested in the club because they feel touched by the music."
    "I search for some basic piano pieces with the tag '[ch13_music_type]'."
    "There's a lot of different results, but I just choose the first one that comes up."
    "I don't know much about music, but the ones I've found look basic enough."
    "There's a lot of chords, so I'm sure it'll be easy for someone like Monika to play."
    "I send them to the printer and head back to Monika who looks just about done selecting books."
    if monika_type == 0:
        show monika 2bb zorder 2 at t11
        m "And...that should do it."
        "Monika takes a book from the shelf."
        m "I've got all my books sorted out."
        mc "What did you choose?"
        m 2ba "Why don't you take a look?"
        "Monika hands me the stack of books she's holding."
        "All of her choices are novels, which isn't unexpected."
        "I haven't really seen or heard of the books she has chosen, so I guess she chose based on what she actually liked..."
        "Unlike me, who chose based on what others might like."
        "But the novels look short enough to do a play on, at least for a few chapters."
        m 1be "Any comments on my choices?"
        m "I don't you've heard of them but maybe you'd like to say something?"
        mc "You're right, I haven't really heard of them before."
        mc "But from the first glance by reading the blurb, they all seem kinda..."
        mc "Um...romantic?"
        m 1bl "Ahaha, I guess you could say that."
        m "The covers of the books don't really help either."
        m 1bm "They're all actually a romantic adventure, which is what I like to read."
        m "Just something about finding true love and..."
        m "...well, it just gets me interested in the story."
        mc "I see..."
        mc "We all have our preferences, it would be wrong me to judge you based on yours."
        mc "I'm sure your choices are great, Monika."
        m 3ba "That's up to everyone else to decide."
        m "Anyway...!"
        m "What kind of music did you choose for me?"
        m "It isn't hard to play, right?"
        mc "I made sure you wouldn't have trouble learning it...I think."
        mc "I'm not really sure how hard it is to play the piano so I just searched for basic piano pieces."
        mc "In the end, I choose some [ch13_music_type]-sounding pieces."
        m 3bd "You've printed it already, right?"
        mc "Yeah, here's the sheet music."
        "I hand over the sheet music to Monika."
        m 1bc "Hmm..."
        m "You're right, [player]."
        m 1bl "These are simple to learn...almost too simple."
        m "Ahaha, I suppose that's fine."
        m 1bj "It just means I can focus on my main piece more."
        mc "Glad to know I wasn't completely useless."
        m 1be "You should give yourself more credit than that."
        m "You've made my task easier just by being here."
        mc "I did?"
        m 2be "You really did."
        m "So thank you."
        mc "I'm not sure what you mean by that but I'm always happy to help I guess."
        m 2ba "I'm going to start practicing these pieces you've chosen."
        m "Do you mind listening?"
        mc "Not at all."
        m 2bb "Great. This shouldn't take too long!"
        mc "I don't mind staying all night if I have to."
        mc "After all, I am just listening."
        m 1be "That's kind of you to offer, [player]."
        m "And as much as I want to spend more time with you..."
        m "I'm afraid I don't really have that much time tonight."
        mc "Then I'll stay as long as you'll have me."
        m "Ahaha, I guess that's fine~"
        m 1ba "Can you hold on to the books while I practice?"
        mc "Sure..."
        "Monika smiles and walks towards her keyboard."
        "She takes the sheet music already there and puts it aside carefully."
        "She then places the sheet music I found for her on the keyboard."
        m 1bc "Choosing [ch13_music_type]..."
        m 1bb "This could definitely work."
        "Monika starts playing the first piece I found for her."
        "Almost effortlessly, she gets it right on the first attempt..."
        "At least I think she did."
        "I'm not really sure how it's supposed to sound exactly."
        "I did click the preview button before I printed it but I wasn't really listening properly."
        m 1ba "How did that sound?"
        mc "It sounded great. You played it perfectly."
        m 1bm "You think so? I actually missed a couple of notes..."
        mc "You did? It was a little hard to tell."
        mc "It still sounded incredible, especially on your first attempt at it."
        m 1be "I'm glad you think so."
        m "It shouldn't take me more than a few hours of practice to get all of these perfected..."
        m 1ba "Now, let's try this second one..."
        "The second one is slightly longer than the first one so she looks at it more carefully."
        "After looking over it for a couple of minutes and muttering something to herself, she smiles at me."
        m 1bb "Here goes nothing..."
        "Once again Monika plays the keyboard."
        "It sounds perfect in my ears."
        show monika 1bp
        "So why does she look like she's about to cry...?"
        mc "Is something wrong?"
        mc "That sounded great..."
        m "It's not that..."
        m 1bo "It's just that...this is the first time I've really played piano for {i}you{/i}."
        m 1bq "Ah...I'm just being emotional for no reason."
        m "Don't worry about it..."
        mc "It's hard not to."
        "Monika looks away for a second."
        "She then turns back and smiles meaningfully."
        m 1br "Thank you for choosing these pieces, [player]."
        m "I really appreciate you taking your time to help me."
        mc "It's not a problem, really."
        m "But I think it's time for you to leave now."
        mc "Oh..."
        m 1bo "Don't misunderstand...!"
        m "It's definitely not your fault that we're stopping now."
        m 1bp "It's mine. I just have a lot of other things I need to do."
        m "I'll get the other pieces done, don't you worry."
        m 1be "You were definitely a big help today."
        mc "Maybe I can still help..."
        m "No...I don't think I need that right now."
        m "I'm sorry, [player]."
        mc "It's okay. I know you're dealing with a lot."
        mc "I'll be there for you if you need me, Monika."
        m 2be "Ah..."
        m "Thank you."
        "I place the books Monika asked me to hold on the table and start walking towards her door."
        show monika at thide
        hide monika
        "She turns around and covers her eyes."
        m "I-I'll see you tomorrow."
        mc "Yeah..."
        scene bg house with wipeleft_scene
        play music t2 fadeout 0.5
        "Even though Monika said it wasn't my fault that we ended right now..."
        "I can't help but feel guilty."
        "I'm sure I didn't do anything wrong but..."
        "Maybe I'll talk to her about it tomorrow."
        "I don't know if she would tell me but at least I can comfort her."
        "I hope I can do something..."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 2bha zorder 2 at t11
        m "I think...this is the last one."
        "Monika takes a book from the shelf."
        m 2bhb "I've got all my books chosen."
        mc "What did you choose?"
        m "Take a look~"
        "Monika hands me the stack of books she's holding."
        "All of her choices are novels, which isn't unexpected."
        "I haven't really seen or heard of the books she has chosen, so I guess she chose based on what she actually liked..."
        "Unlike me who chose based on what others might like."
        "But the novels look short enough to do a play on, at least for a few chapters."
        m 2bhe "What do you think?"
        m "You probably haven't heard of them before, have you?"
        mc "You're right, I haven't really heard of them before."
        mc "But from the first glance by reading the blurb, they all seem kinda..."
        mc "Um...romantic?"
        m 2bhl "Ahaha, I guess you could say that."
        m "The covers of the books kinda give it away."
        m 2bhm "They're all actually a romantic adventure, which isn't what I'd normally prefer..."
        m 2bhn "Things have just been kinda weird lately. You understand, right?"
        mc "I guess..."
        mc "I mean we all have our preferences, it would be wrong me to judge you based on yours."
        mc "I'm sure your choices are great, Monika."
        m 2bha "That's up to everyone else to decide."
        m "Anyway...!"
        m "What kind of music did you choose for me?"
        m 2bhe "It's not too easy to play, is it?"
        mc "I made sure you wouldn't have trouble learning it...I think."
        mc "I'm not really sure how hard it is to play the piano so I just searched for basic piano pieces."
        mc "In the end, I choose some [ch13_music_type]-sounding pieces."
        m 4bhe "Is that sheet music I see in your hands?"
        mc "Yeah, take a look."
        "I hand over the sheet music to Monika."
        m 3bhc "Hmm..."
        m 3bha "You're right, [player]."
        m 3bhj "Ahaha, these look a little too easy for me."
        m "That's actually perfectly fine."
        m 3bha "It just means I can focus on my main piece more."
        mc "Glad to know I wasn't completely useless."
        m 1bhe "You should give yourself more credit than that."
        m "You've made my day just by being here."
        mc "I did?"
        m 1bha "You did!"
        m "So thank you."
        "Monika smiles meaningfully."
        m 1bhb "I'm gonna try to play these pieces you've chosen."
        m "Care to listen?"
        mc "I'd love to."
        m 1bhe "Great. This shouldn't be too long."
        mc "I don't mind staying all night if I have to."
        m 1bhm "That means a lot..."
        m "But I'm afraid I've still got other things to do tonight."
        mc "Then I'll stay as long as you'll have me."
        m 2bhe "Ahaha, okay~"
        m "Can you hold on to those books while I practice?"
        mc "Sure..."
        "Monika smiles and walks towards her keyboard."
        "She takes the sheet music already there and puts it aside carefully."
        "She then places the sheet music I found for her on the keyboard."
        m 2bhc "Choosing [ch13_music_type]..."
        m 1bha "Let's see what we can do..."
        "Monika starts playing the first piece I found for her."
        "Almost effortlessly, she gets it right on the first attempt..."
        "At least I think she did."
        "I'm not really sure how it's supposed to sound exactly."
        "I did click the preview button before I printed it but I wasn't really listening properly."
        m 1bhb "How did that sound?"
        mc "It sounded great. You played it perfectly."
        m "Do you think so? I'm almost positive I missed a couple of notes there."
        mc "Ah...it's kinda hard for me to tell."
        mc "It still sounded incredible, especially on your first attempt at it."
        m 2bha "Well, I'm glad you think so."
        m "With how easy these pieces are, it shouldn't take more than a couple of hours to get them perfect."
        m 1bhe "So...let's try this second one..."
        "The second one is slightly longer than the first one so she looks at it more carefully."
        "After looking over it for a couple of minutes and muttering something to herself, she smiles at me."
        m 1bha "And now..."
        "Once again Monika plays the keyboard."
        "It sounds perfect in my ears."
        show monika 1bho
        "She kinda looks like she's holding back tears."
        mc "Is something wrong?"
        mc "That sounded great..."
        m 1bhm "I-It's nothing..."
        m "Just something about playing piano for someone..."
        m 1bhn "Ah...I'm just being emotional for no reason."
        m "Forget what you've just seen."
        mc "I don't think that's possible."
        "Monika looks away for a second."
        "She then turns back and smiles meaningfully."
        m 1bhq "Thank you for choosing these pieces, [player]."
        m "I really appreciate you taking your time to help me."
        mc "It's not a problem, really."
        m 1bhr "But it's time for you to leave now, I think."
        mc "Oh..."
        m 2bhm "Please don't take it the wrong way."
        m "I'm still adapting to everything and..."
        m "I'll just say it's my fault we're stopping now."
        m 2bhn "I'll get the other pieces done, don't you worry."
        m "You were definitely a big help today."
        mc "Maybe I can still help..."
        m 2bhe "No...there's nothing you can do right now..."
        m "I'm sorry, [player]."
        mc "It's okay. I know you're dealing with a lot."
        mc "I'll be there for you if you need me, Monika."
        m "I appreciate it..."
        "I place the books Monika asked me to hold on the table and start walking towards her door."
        show monika at thide
        hide monika
        "She turns around and covers her eyes."
        m "I-I'll see you tomorrow."
        mc "Yeah..."
        scene bg house with wipeleft_scene
        play music t2 fadeout 0.5
        "Even though Monika said it wasn't my fault that we ended right now..."
        "I can't help but feel guilty."
        "I'm sure I didn't do anything wrong but..."
        "Maybe I'll talk to her about it tomorrow."
        "I don't know if she'll tell me but at least I can comfort her."
        "I hope I can do something..."
    else:
        show monika 1ba zorder 2 at t11
        m "This should do."
        "Monika takes a book from the shelf."
        m 1bc "I've got all my books chosen."
        mc "What did you choose?"
        m 1ba "You can look at them if you want."
        "Monika hands me the stack of books she's holding."
        "All of her choices are novels, which isn't unexpected."
        "I haven't really seen or heard of the books she has chosen, so I guess she chose based on what she actually liked..."
        "Unlike me who chose based on what others might like."
        "But the novels look short enough to do a play on, at least for a few chapters."
        m 1bc "I doubt you've heard of these before."
        mc "You're right about that."
        mc "I suppose it wouldn't be like you to choose books based on what other people think."
        m 2bc "I'm not the type of person who cares about what other people think."
        m "As long as those I really care about are okay, that's fine with me."
        mc "Right..."
        m 2be "I would like {i}your{/i} opinion though."
        m "So what do you think of these books?"
        mc "The covers kinda make it seem like you chose some mystery or horror books."
        mc "Though I'm not really sure since the blurbs are pretty vague too."
        m 1ba "You're right on target there, [player]."
        m "I doubt these books will be chosen by the club, but I'd still like to share them."
        m 1bb "If I can get one of my friends to become interested in this type of genre, then that's enough for me."
        mc "I guess there's nothing to lose, right?"
        m 2ba "Exactly!"
        m "Anyway...!"
        m 2bb "What music did you choose for me?"
        m "It's not too easy to play, is it?"
        mc "I made sure you wouldn't have trouble learning it...I think."
        mc "I'm not really sure how hard it is to play the piano, so I just searched for basic piano pieces."
        mc "In the end, I choose some [ch13_music_type]-sounding pieces."
        m 2bc "I'm assuming that's it in your hands?"
        mc "Yeah, take a look."
        "I hand over the sheet music to Monika."
        m 1bd "Hmm..."
        m "These are really quite simple to play."
        m 1be "I suppose that's fine, it just means I can focus on this piece I'm practicing now."
        mc "At least I wasn't completely useless."
        m "Ahaha~"
        m 1ba "There are still some things we need to do before you need to leave."
        mc "What's that?"
        m "You haven't heard me practice yet."
        m 3bb "I need to know if there's anything I should improve or not."
        mc "Then I'll happily listen."
        m "Okay, [player]."
        m "This shouldn't take that much time..."
        mc "I don't mind staying all night if I have to."
        m 1bl "That won't be necessary."
        mc "Then I'll stay as long as you need me."
        m 1ba "That's acceptable."
        m "Hold on to those books while I practice, would you?"
        mc "Sure..."
        "Monika walks towards her keyboard."
        "She takes the sheet music already there and puts it aside carefully."
        "She then places the sheet music I found for her on the keyboard."
        m 1bc "Choosing [ch13_music_type]...?"
        m 1bd "{i}(Well, I guess this is what I get for relying on other people...){/i}"
        mc "What was that?"
        m 1ba "I said I'm going to start playing now."
        "Monika starts playing the first piece I found for her."
        "Almost effortlessly, she makes it sound perfect on the first attempt."
        m 1bb "How did that sound?"
        mc "That sounded...perfect."
        m 1bh "Ahaha, I do aim for nothing less."
        mc "I don't know if you actually played it perfectly but I couldn't tell the difference between that and the preview."
        m 1bk "I'm sure I sounded better."
        "Monika smiles mischievously."
        mc "Probably."
        m 1ba "Anyway, with how easy that one piece was I wouldn't be surprised if it took me less than a few hours to master it."
        m 2bb "Let's take a look at this second one."
        "Monika places the second piece I found for her on her keyboard."
        "A few minutes pass as she plays the piece."
        "The sound echoes throughout her house."
        "Once again, she plays the tune effortlessly."
        m 1bc "That was a little bit more difficult."
        m 1be "I think I did miss a note or two that time."
        mc "I didn't notice."
        m "I'm sure you didn't."
        m 3bj "I made sure to cover it up rather quickly."
        mc "That's some impressive piano skills you have there, Monika."
        m "Thanks, [player]~"
        m 3ba "Though I'll be honest, I've been practicing piano for a few years now."
        mc "Years...?"
        mc "I thought you were still taking piano lessons."
        m 1bm "Ah..."
        m "Well, if you truly want to be the best, you have to keep learning..."
        mc "I guess you're right, Monika."
        m 1bn "Anyway, that's all we're doing for tonight."
        m "I still have a couple of things I have to take care of."
        if ch12_markov_agree:
            m 1bh "Make sure to read that book."
        else:
            m 1be "Take care of yourself, [player]."
        mc "Of course."
        m "I think that's all we have to say."
        m 1ba "I'll see you tomorrow."
        mc "It's a bit of an abrupt end, but I guess you're a busy person."
        m 2be "There's a lot happening right now, so I'm sorry if you don't understand."
        mc "No, I do completely."
        mc "Don't worry about it."
        m 2bj "Okay..."
        m "Thanks for coming with me here, [player]."
        mc "It's not a problem."
        mc "I'm just glad I could actually do something."
        m 2ba "I'll practice the rest of these later."
        m "Don't worry, I'll definitely get them done."
        mc "I believe you."
        "I place the books Monika asked me to hold on the table and start walking towards her door."
        show monika at thide
        hide monika
        "She starts looking over the sheet music again."
        m "Goodbye, [player]."
        mc "Yeah..."
        scene bg house with wipeleft_scene
        play music t2 fadeout 0.5
        "I wonder what has Monika so busy tonight."
        "It's probably got nothing to do with me so I shouldn't pry..."
        "But my curiosity is getting the better of me."
        "Maybe it's just some more preparation of Inauguration Day without me?"
        "I mean I didn't really help so maybe she just didn't want me there."
    scene bg bedroom with wipeleft_scene
    "I arrive home, feeling like I barely did anything."
    "I wonder if I should have chosen someone else instead."
    "What if their preparations end up being worse because I chose to help Monika...?"
    "I shouldn't think so negatively about everything."
    "I'm sure everyone else will be fine."
    "After all, they're more than capable of doing their own part."
    "I guess I'm just overthinking things..."
    "I am a little worried about how Sayori is doing."
    "She seems like she has a lot to do..."
    "What am I saying? I just told myself that they're more than capable."
    "Sayori even said she could handle it herself."
    "I shouldn't worry about it so much..."
    "But it's really hard not to."
    "I guess I'll find out how Monika is doing in the club tomorrow."
    "Maybe that has something to do with why she was upset when we got to her house?"
    "It could have something to do with her house but..."
    "I don't really know."
    "Hopefully, everything is okay."
    if ch12_markov_agree:
        "Right now, I have to read this book Monika gave me."
        "It's definitely something I have to do tonight."
        "Everything else is no longer a priority."
    return

label ch13_exclusive_sayori:
    scene bg n_house
    with wipeleft_scene
    play music t6 fadeout 1.0
    "Before long, Sayori and I arrive at Natsuki's house."
    "It really felt like no time passed at all..."
    "It was like as soon as we left the Literature Club, we ended up here."
    show sayori 1a zorder 3 at t11
    s "Everything okay, [player]?"
    s 1b "I know this probably isn't what you expected when you chose me to help..."
    s "But I wanna make sure that Natsuki is okay in person before we do anything."
    mc "Ah...it's fine."
    s 2d "Are you sure? You look like you have a lot on your mind."
    mc "I just wasn't expecting to get here so fast."
    mc "It almost feels like no time passed at all."
    s 2a "Well, we did walk here pretty fast."
    mc "Maybe..."
    s "Anyway, we just came here to check up on her."
    s "We won't be here long, I promise."
    "Sayori steps forward and rings the doorbell to Natsuki's house."
    "No one comes to the door immediately."
    s 1c "Hmm...I wonder what's--"
    if ch12_outcome == 3:
        show momsuki 1a zorder 3 at f31
        show dadsuki 1c zorder 2 at t32
        show sayori zorder 2 at t33
        mo "Oh, it's you two!"
        "Haruki and Yasuhiro appear at the front door."
        mo "Have you come to visit Natsuki?"
        mo 1b "I'm sure she'd love to see you both!"
        show momsuki zorder 2 at t31
        show sayori 2a zorder 3 at f33
        s "That's great!"
        s "Is she home right now?"
        show dadsuki 1a zorder 3 at f32
        show sayori zorder 2 at t33
        d "Yes...she is."
        d 1j "Look...I want to apologize for how I acted yesterday."
        d "My mind was so clouded..."
        show dadsuki zorder 2 at t32
        show sayori 2d zorder 3 at f33
        s "Ehehe, that's okay."
        s "As long as everything is good now, right?"
        show momsuki 1f zorder 3 at f31
        show sayori zorder 2 at t33
        mo "Aha, I'll be honest with you, dear..."
        mo "I don't think things will ever {i}truly{/i} be the same."
        mo "But we have to look forward, so we can move on..."
        show momsuki zorder 2 at t31
        show sayori 2l zorder 3 at f33
        s "Yeah...that's a good point."
        s "I should do that some time..."
        show sayori zorder 2 at t33
        "Suddenly a noise comes from within the house."
        n "Mom? Dad?"
        n "Who's at the door?"
        show natsuki 1bc zorder 3 at f41
        show momsuki zorder 2 at t42
        show dadsuki zorder 2 at t43
        show sayori zorder 2 at t44
        n "Huh? Sayori...? And [player]?!"
        n 2bg "What are you guys doing here?"
        show natsuki zorder 2 at t41
        show sayori 4q zorder 3 at f44
        s "Hey, Natsuki!"
        s "We're just checking up on you..."
        s 4d "To make sure you're doing okay."
        show momsuki 1c zorder 3 at f42
        show sayori zorder 2 at t44
        mo "We'll leave the three of you alone."
        mo "I'm sure this conversation has nothing to do with us."
        show momsuki zorder 2 at t42
        show sayori 3a zorder 3 at f44
        s "Alright!"
        s "It was nice seeing you both."
        show momsuki at thide
        hide momsuki
        show dadsuki at thide
        hide dadsuki
        show natsuki zorder 2 at t21
        show sayori zorder 2 at t22
        "Haruki smiles and goes inside with Yasuhiro following behind her."
        show sayori 3c zorder 3 at f22
        s "So..."
        s "Is everything okay?"
        s 3d "I know you have both your parents back..."
        s "But are {i}you{/i} feeling okay?"
        show natsuki 2bc zorder 3 at f21
        show sayori zorder 2 at t22
        n "Y-Yeah...I guess so."
        n 2bk "My parents are still trying to figure out a way to make everything work..."
        n "It's hard but..."
        n 2bq "I think we can really get close to how things were before...."
        n "Maybe not exactly the same but..."
        n "As close as it can be."
        show natsuki zorder 2 at t21
        mc "It's good to hear you feeling better, Natsuki."
        mc "After that whole thing yesterday, I really wasn't sure how you were feeling."
        show natsuki 5be zorder 3 at f21
        n "I'm fine..."
        n 5bi "But I'm kinda hoping things get back to normal tomorrow."
        n "Staying at home all day sucks..."
        n "It was only made better by both my parents being there."
        show natsuki zorder 2 at t21
        show sayori 1c zorder 3 at f22
        s "Ah...speaking of which..."
        s "The club decided on doing something today."
        show natsuki 1bc zorder 3 at f21
        show sayori zorder 2 at t22
        n "Really?"
        n "What was it?"
        show natsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "Well, have you heard of Inauguration Day coming up this Friday?"
        "Natsuki shakes her head."
        s 1d "Basically, it's a day where a bunch of the smaller clubs are holding an event for the school!"
        s "It's a chance for them to show the school what they're all about and get new members."
        show natsuki 1bk zorder 3 at f21
        show sayori zorder 2 at t22
        n "This sounds like something we need a whole lot more preparation for..."
        show natsuki zorder 2 at t21
        show sayori 2l zorder 3 at f22
        s "I didn't really know about it until today either..."
        s "It was Yuri's idea..."
        s "Anyway..."
        s 2d "We were hoping you could make some cupcakes for the day."
        s "We're all doing our own thing and [player] is helping me out with mine."
        show sayori zorder 2 at t22
        "Natsuki looks at me curiously."
        show natsuki 2bs zorder 3 at f21
        n "Well...I guess it would be better than doing nothing."
        n "So..."
        n 2ba "Sure, I'll bake some cupcakes for the day."
        show natsuki zorder 2 at t21
        show sayori 2a zorder 3 at f22
        s "Great!"
        s "Me and [player] need to go do our preparations now..."
        s "So we'll see you tomorrow!"
    elif ch12_outcome == 2:
        show momsuki 1a zorder 3 at f21
        show sayori zorder 2 at t22
        mo "Oh, it's you two!"
        "Haruki appears at the front door."
        mo "Have you come to visit Natsuki?"
        mo 1c "She's a little busy right now but I'm sure she'd enjoy seeing the two of you."
        show momsuki zorder 2 at t21
        show sayori 1d zorder 3 at f22
        s "Ah...okay."
        s "We won't take up much of her time."
        s "We just came to deliver a message."
        show momsuki 1b zorder 3 at f21
        show sayori zorder 2 at t22
        mo "Aha, okay then..."
        "Haruki turns around."
        mo "Natsuki! Your friends are here!"
        mo 1c "She'll be down in a second..."
        mo "But if you'll excuse me I have to do some housework..."
        show momsuki at thide
        hide momsuki
        "Haruki heads back into her house."
        s "So what do you think Natsuki is busy with?"
        s "Maybe I shouldn't ask her to do anything..."
        show natsuki 1bh zorder 3 at f21
        n "Sayori? [player]?"
        n "What are the two of you doing here?"
        n "I wasn't really expecting you guys."
        show natsuki zorder 2 at t21
        show sayori 2a zorder 3 at f22
        s "We just came to check up on you!"
        s "...And to relay a message."
        show natsuki 2bc zorder 3 at f21
        show sayori zorder 2 at t22
        n "Thanks, I guess..."
        n "What was the message you wanted to tell me?"
        show natsuki zorder 2 at t21
        show sayori 2l zorder 3 at f22
        s "Well, it was more of a request..."
        s "You see, the club decided to participate in an event happening on Friday..."
        s "And everyone already has their own thing they are going to do."
        show natsuki 2bi zorder 3 at f21
        show sayori zorder 2 at t22
        n "Ugh...good..."
        show natsuki zorder 2 at t21
        show sayori 2c zorder 3 at f22
        s "Huh? What do you mean?"
        show natsuki 2h zorder 3 at f21
        show sayori zorder 2 at t22
        n "My mom wanted me to help clean the house from my dad's mess all day."
        n "I had nothing better to do and I wanted to spend time with her so I agreed..."
        n "If I tell her I'm doing something for the club then I'm sure I can get out of it."
        show natsuki zorder 2 at t21
        show sayori 4q zorder 3 at f22
        s "Oh...that's good!"
        show sayori zorder 2 at t22
        mc "Your mom seems like a reasonable person."
        mc "I'm sure she'll definitely let you get out of doing housework for the club."
        show sayori 4r zorder 3 at f22
        s "Yeah, what [player] said!"
        show natsuki 5j zorder 3 at f21
        show sayori zorder 2 at t22
        n "Anyway..."
        n "What did you guys want me to do? Bake some cupcakes?"
        show natsuki zorder 2 at t21
        show sayori 3a zorder 3 at f22
        s "Actually, yeah!"
        s "I know you're really good at doing that so I was about to ask you to."
        show natsuki 5z zorder 3 at f21
        show sayori zorder 2 at t22
        n "You can count on me, Sayori."
        n "I'm sure my mom would love to help, too."
        show natsuki zorder 2 at t21
        show sayori 1a zorder 3 at f22
        s "Ehehe, that's great Natsuki!"
        s "Me and [player] have to go now though, so good luck!"
    elif ch12_outcome == 1:
        show dadsuki 1a zorder 3 at f21
        show sayori zorder 2 at t22
        d "Hello..."
        d "Are you here for Natsuki?"
        show dadsuki zorder 2 at t21
        show sayori 1d zorder 3 at f22
        s "Hi, Yasuhiro!"
        s "And yes, we came here to talk to Natsuki for a little bit."
        s "It's kinda important for our club."
        show dadsuki 1b zorder 3 at f21
        show sayori zorder 2 at t22
        d "I-I see..."
        d "I'll get her right away..."
        "Yasuhiro walks to the door and suddenly turns back."
        d 1j "And..."
        d "I'm sorry for what happened yesterday."
        d "None of you needed to see that."
        show dadsuki zorder 2 at t21
        show sayori 2d zorder 3 at f22
        s "Ehehe...it's okay..."
        s "As long as it all worked out, right?"
        show sayori zorder 2 at t22
        "Yasuhiro nods before heading back inside."
        show dadsuki at thide
        hide dadsuki
        "A bit of shouting can be heard from inside but it isn't long before Natsuki comes outside."
        show natsuki 2bc zorder 3 at f21
        n "Hey..."
        n "What are you guys doing here?"
        show natsuki zorder 2 at t21
        show sayori 2a zorder 3 at f22
        s "We just came to check up on you, mostly!"
        s "You also missed a pretty big thing in the club today."
        s "We decided we're going to be participating in the event on Friday."
        show natsuki 4bh zorder 3 at f21
        show sayori zorder 2 at t22
        n "Oh...that sounds nice."
        n "What's the event about?"
        show natsuki zorder 2 at t21
        show sayori 2q zorder 3 at f22
        s "It's about the smaller clubs showing off for the school!"
        s "It's to promote the smaller clubs to try to get more members."
        s "Yuri suggested it and we all agreed to do something for the day."
        show natsuki 1bc zorder 3 at f21
        show sayori zorder 2 at t22
        n "Did you want me to do something?"
        show natsuki zorder 2 at t21
        mc "We were wondering if you could bake some cupcakes."
        mc "You're really good at that kinda thing."
        show sayori 2d zorder 3 at f22
        s "Yeah, baking something for the day would be great!"
        s "But I don't wanna pressure you or anything so..."
        show natsuki 2bs zorder 3 at f21
        show sayori zorder 2 at t22
        n "I-It's fine..."
        n "I was looking for something more normal in my life anyway."
        show natsuki zorder 2 at t21
        show sayori 1h zorder 3 at f22
        s "Huh? Is something wrong?"
        show natsuki 2bq zorder 3 at f21
        show sayori zorder 2 at t22
        n "N-Not really..."
        n "I guess it's just good having something {i}normal{/i} to do."
        "Natsuki looks at the ground before looking back at Sayori."
        n 2ba "So I'll do it."
        show natsuki zorder 2 at t21
        show sayori 1q zorder 3 at f22
        s "Great!"
        s "That's all we really came to tell you."
        s 1a "We still need to do our part, so..."
        s "See you tomorrow!"
    else:
        "There's a short moment of silence before anything happens."
        "Finally, someone opens the door."
        show natsuki 1bg zorder 3 at f21
        n "H-Hello?"
        n 2bh "S-Sayori? And [player]?"
        n "W-What are you guys doing here?"
        show natsuki zorder 2 at t21
        show sayori 2d zorder 3 at f22
        s "We came here to check on you, Natsuki."
        s "By the looks of things..."
        s "You look like you're doing pretty well for yourself."
        show natsuki 2bq zorder 3 at f21
        show sayori zorder 2 at t22
        n "Yeah..."
        n "Today has been a weird day."
        show natsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "How are you feeling?"
        s "I know things might have gotten harder now that you live alone..."
        show natsuki 2bs zorder 3 at f21
        show sayori zorder 2 at t22
        n "It's...different."
        n "I don't really know what to think of it."
        n "But really I'm just looking for something normal to do."
        n "I need to take my mind off things."
        show natsuki zorder 2 at t21
        show sayori 2l zorder 3 at f22
        s "Well...I was actually gonna ask you to do something."
        s "There's something going on this Friday and--"
        show natsuki 2be zorder 3 at f21
        show sayori zorder 2 at t22
        n "I'll do it!"
        n "Just tell me what you need me to do."
        show natsuki zorder 2 at t21
        show sayori 2a zorder 3 at f22
        s "Ehehe, I guess you're kinda excited..."
        s "I was gonna ask you to make some cupcakes for Friday."
        show sayori zorder 2 at t22
        mc "Your baking is really good so I'm sure it'll be great for Inauguration Day."
        mc "That's what the event is called."
        show natsuki 2bt zorder 3 at f21
        n "T-Thanks..."
        n "I'll start getting ready for this {i}Inauguration Day{/i} thing."
        n 2bl "You guys can count on me."
        show natsuki zorder 2 at t21
        show sayori 1d zorder 3 at f22
        s "Alright, Natsuki..."
        s "I know our visit was kinda short but..."
        s "Well, we still have do our own preparations."
    show natsuki 1bk zorder 3 at f21
    show sayori zorder 2 at t22
    n "A-Alright, Sayori..."
    "Natsuki waves goodbye."
    n "Good luck to both of you..."
    show natsuki zorder 2 at t21
    show sayori 2q zorder 3 at f22
    s "Ehehe, thanks!"
    s "Oh, I forgot to mention...!"
    s "We're going to be publicly performing a play."
    show natsuki 2bo zorder 3 at f21
    show sayori zorder 2 at t22
    n "W-What?!"
    n "I-I didn't agree to this..."
    show natsuki zorder 2 at t21
    show sayori 1k zorder 3 at f22
    s "I thought you'd be confident enough to do this, Natsuki..."
    s "I guess I'll have to tell everyone that this whole thing is off."
    show sayori zorder 2 at t22
    "Natsuki looks at Sayori and sighs."
    show natsuki 1bs zorder 3 at f21
    n "Fine...I'll do it."
    n "But only because everyone else already agreed to it!"
    n "Not because I want to."
    show natsuki zorder 2 at t21
    show sayori 2d zorder 3 at f22
    s "You really don't have to agree to it, Natsuki."
    s "We can always skip the event or do something else."
    show natsuki 2bf zorder 3 at f21
    show sayori zorder 2 at t22
    n "I already said I would!"
    n "So just don't worry about it, okay?"
    show natsuki zorder 2 at t21
    show sayori zorder 3 at f22
    s "If you say so, Natsuki."
    show natsuki 12bb
    "Natsuki turns her head."
    s 1d "Hopefully you'll be okay on your own..."
    s "I'm glad you decided to go with it."
    s "Anyway..."
    s 1a "Let's go, [player]!"
    scene bg house
    with wipeleft_scene
    "We finally arrive at Sayori's house."
    "It didn't really matter who's house we did the preparations at but Sayori is the one I'm helping and not the other way around."
    "It feels good to be here with just the two of us again."
    "I feel like it's been a long time since the last time..."
    "It was during the first week, wasn't it?"
    show sayori 1c zorder 2 at t11
    s "You look deep in thought, [player]!"
    s "What are you thinking about?"
    mc "Eh?"
    mc "I-It's nothing, really."
    s 1b "It doesn't look like nothing."
    s "You can tell me whatever is on your mind, you know!"
    mc "Well, I was just thinking back to the first week of the literature club."
    s 1l "Y-You were?"
    mc "Yeah, it's been a while since I've really visited your house."
    mc "Just the two of us, I mean."
    s 2o "Has it...?"
    "Sayori scratches her head."
    s "I don't really remember the first week very well!"
    mc "It's just the last time we really got to spend time at your house..."
    mc "Was when you confessed to me, remember?"
    s 2y "Ehehe, why do you have to bring that up?"
    s "I-It was such a long time ago..."
    if sayori_dumped:
        s 2l "A-And besides...you decided to be with Yuri."
        s 1k "Just thinking about it..."
        s "It just...darkens my day..."
    elif sayori_confess:
        s 2d "It was an easier time back then."
        s "I could just do whatever I wanted and..."
        s "I didn't know it would all end up like this."
    else:
        s 2d "I know you didn't accept it but..."
        s "I'm glad we stayed as friends, [player]."
        s "For better or for worse."
        mc "Eh? What do you mean?"
    s 1d "W-Well, never mind."
    s "Let's just go inside."
    scene sayori_bedroom
    show sayori 1a zorder 2 at t11
    with wipeleft_scene
    s "I have to contact the person holding the event."
    s "In the meantime, why don't you create a list of stuff the others could use for their part in the Inauguration Day?"
    mc "How could I possibly do that?"
    mc "I barely know the type of stuff they're going to do."
    s 1d "Well...you've been in this club for a while now."
    s "You should be able to tell what kind of stuff everyone likes..."
    s 1q "...At least, I hope so."
    s "I know you'll figure it out, [player]."
    mc "You're trusting me with a lot, Sayori."
    s 1r "Ehehe, it's not like I'm gonna be gone forever."
    s 1d "I'm just making a call to try to get our club in for Inauguration Day."
    s "Just get started on the list."
    mc "Alright..."
    s 1o "Now who's idea was the whole day again...?"
    s "I'll have to make a promise if he's gonna properly consider our club."
    show sayori at lhide
    hide sayori
    "Sayori pulls out her phone before heading into the hallway."
    "So I guess it's up to me to come up with something."
    "Where should I start...?"
    "Yuri is doing atmosphere, which means she's going to need a lot of decorations."
    "Meanwhile Natsuki is doing some baking, which means she probably needs some ingredients."
    "And Monika is playing the piano on the day."
    "Sayori said she was going to get her a grand piano, right?"
    "She doesn't have that kind of money...does she?"
    "I shouldn't really think about that."
    "Sayori knows what she's doing, so I should just focus on the task at hand."
    "For Yuri's part, we could get a lot of generic decorations."
    "Maybe even get her some artistic equipment so she can make it herself."
    "I'm sure she'd appreciate that."
    "I begin to list down some of the things I think Yuri could use."
    "After a few minutes, Sayori comes back into the room."
    show sayori 1ba zorder 2 at t11
    "She seems to have changed her clothes in the meantime."
    "Which is weird, since her clothes should be in her room..."
    "I wonder how she did that..."
    s "Glad that's over with."
    mc "How did it go?"
    mc "Is our club going to be participating?"
    s 2bq "Of course!"
    s "I didn't have to convince him very hard to let us in."
    mc "What did you promise him?"
    s 2bd "Ehehe, nothing too big so don't worry about it."
    s "Anyway...!"
    s 2bc "What have you got written down?"
    "Sayori takes the list of items from my hand."
    mc "H-Hey, I'm not finished yet!"
    "Sayori looks at the list curiously."
    s 1bo "Yuri's items...scented candles...paint...brushes..."
    s 1ba "This is quite the list, [player]!"
    s "I'm actually kinda impressed."
    mc "We're responsible for helping them with their preparations."
    mc "So I want to do my best and help however I can."
    mc "It would suck if what they were doing ended up less than ideal because of us."
    s 1bd "W-Wow...that's actually almost exactly how I'd put it!"
    s "I just wanna make sure that everyone is proud of how their own preparations."
    s 2bd "I'm glad you feel the same."
    "Sayori hands me back the paper with Yuri's items listed down."
    s 4bq "That's a really good list of items, [player]."
    s "Just keep writing down whatever you think she'll need."
    s "Meanwhile, I'll start organizing a way to get a grand piano for Monika."
    mc "I've been wondering about that..."
    mc "I don't want to presume that you can't but how are you going to get one of those?"
    mc "They're pretty expensive to rent or buy, aren't they?"
    mc "I'd feel pretty bad if you had to use your own money to get one for her."
    mc "After all, there are--"
    s 2bd "[player]."
    s "Since this might be the last thing the club does together..."
    s "I thought it would be good if we really did everything we could."
    mc "Eh? Isn't this whole event about getting more members for the club?"
    mc "Why would it be the last thing the club does together...?"
    s 2bk "N-Never mind."
    s "{i}(How do I keep letting things like that slip from my mouth?){/i}"
    s "You finish up with Yuri's list and I'll start looking at pianos online."
    mc "Alright, Sayori."
    show sayori 2bq
    "Sayori smiles at me before moving towards her computer."
    s "Pianos..."
    s 2bn "What kind would Monika want...?"
    show sayori at thide
    hide sayori
    "I decide to focus on what I'm doing."
    "I think her list only needs a few more items."
    "She probably won't even use most of them, let alone get most of them."
    "But a comprehensive list is important for something like this."
    "..."
    "After a little bit of time, I finally manage to finish the list."
    "It's probably still missing some stuff but I think all the important things we need to get are there."
    show sayori 1ba zorder 2 at t11
    s "Finished the list, [player]?"
    mc "Yeah, I'm pretty sure that's all Yuri would need."
    mc "Besides, it's not like she'll actually get it all so I circled some of the more important ones."
    s 1bb "Just let me take a look."
    "I give the list to Sayori who inspects it one more time."
    s 1bq "Yeah...I think this'll work!"
    s "Good job, [player]!"
    mc "Thanks..."
    mc "Do you know what you're going to be getting from that list?"
    mc "There's a lot of stuff in there, you know."
    s 2bd "I'm sure I'll come up with something."
    s "In the meantime, what do you think about this piano I found for Monika?"
    "Sayori points towards her computer screen which has an image of a grand piano."
    "It's hard to describe but the black colour almost makes it look majestic."
    "As if anything played on it would sound amazing."
    "I can see why Sayori chose this piano. I'm sure Monika would look and sound great playing on it."
    "I scan the page until I notice the price tag."
    mc "Sayori, are you crazy?"
    mc "Even if you rent that thing you'll still be out of a whole year's worth of money."
    s 2bf "It's for Monika though, isn't it?"
    s "She deserves this."
    mc "I-I mean sure but you have to look out for yourself, Sayori."
    mc "There's no way you can afford something like this!"
    s 2bl "Ehehe, I have ways..."
    s "But anyway what do you think about the actual piano?"
    s 2ba "It's pretty good, right?"
    mc "Y-Yeah but..."
    s 2bf "Don't worry about the cost."
    s "That's the last thing on my mind right now."
    s 1bd "Just...talk about the piano."
    mc "Well...if I just had to say something about it..."
    mc "...then I guess it would be perfect for Monika."
    mc "She'd look great playing on something like this."
    mc "She'd probably catch the eyes and ears of anyone even slightly interested."
    s 1bq "Great!"
    s "That's all you really needed to say from the beginning."
    mc "Is that all we're doing to help Monika?"
    s 1ba "Well, we don't know what song she's playing yet."
    s "I don't know how else we can help her apart from helping her practice."
    mc "I see your point."
    mc "What about Natsuki?"
    mc "There has to be something we can do for her, right?"
    s 1bq "Actually, yeah!"
    s "While I was on the phone I managed to get in contact with Natsuki."
    s "I told her she can send me a list of ingredients she wants or needs before the day."
    mc "W-What?"
    "At this point I'm seriously questioning Sayori's finances."
    "Does she have some sort of mystery broker I don't know about?"
    "If not, how can she even afford to be so generous with money?"
    s 1ba "Which means..."
    s "We have to select our books now!"
    mc "Ah...right."
    mc "I almost forgot about that."
    mc "How are we going to do that? It's not like you just have a bunch of books lying around..."
    s 1bd "Actually..."
    "Sayori opens her wardrobe."
    "It's filled...with...lots of books."
    "There's all sorts, from fiction, to manga and even tutorial books."
    "Since her wardrobe is filled with books...maybe she changed her clothes somewhere else?"
    mc "Where did you get all these books?"
    mc "There's so much variety as well...I didn't really take you for this kinda person."
    s 1bl "Maybe you don't know me as well as you think."
    mc "Maybe..."
    mc "When did you get all of these anyway?"
    s "Pretty recently, actually."
    s 2bd "I thought that since I'm president of the Literature Club, I might as well own some actual literature."
    s "I guess I went a little overboard..."
    s "But it's good that I bought them, seeing as we're doing this event."
    "I look through her wardrobe and for some reason, the tutorial books catch my eye."
    "There's just so much variety there..."
    "There's cooking, writing and even programming...?"
    "I didn't think Sayori would be interested in cooking, let alone programming."
    s 2ba "Just choose three or four, that should be enough."
    s "When you're done, I'll choose some as well."
    mc "I'm still just at awe at how many books you have."
    mc "It must have cost a lot."
    s 2bd "You could say that."
    s "But anyway...get searching!"
    mc "R-Right."
    "Sayori has a lot of popular book series in here."
    "I don't really read much but I recognize a lot of the books she has."
    "I decide to take three manga that I know enough about."
    "I also take a novel from book series that I think everyone would know about."
    s 2bn "That didn't take long."
    s "What did you choose?"
    "I show Sayori the books I chose from her shelf."
    "She looks at them inquisitively before smiling at me."
    s 2bq "Good choices, [player]!"
    s "I'm sure one of those will probably end up being the one we do."
    mc "Do you think so?"
    s 1ba "Everyone is probably gonna choose a popular book too, since it's a public performance but you never know."
    s "I don't think they'll make it too obvious to everyone what their interests are."
    s 1bb "If that makes sense."
    mc "Why not?"
    s 1bd "This'll be the first time in the club that we're publicly doing something..."
    s "That thing yesterday doesn't really count."
    s 1bc "They wouldn't really want everyone to judge them because of what they like."
    s "So they could be appealing to the general crowd and people who could have only read the popular series, like you."
    s "At least...that's what I think."
    mc "Ah...I'm not sure if that was as an insult but I get your point."
    mc "It's not really a problem for me, it's more like I don't read many books except for manga."
    s "And you're happy to share your interests with everyone?"
    mc "I do feel a little bit more confident for some reason."
    "It's almost like being around Sayori gives me a sense of...self-confidence...?"
    mc "But to answer your question, not really, it's just choosing a manga I like."
    mc "It's better that I choose something that I like that doesn't tell much about me than a novel that represents exactly who I am."
    s 1bd "Yeah, but by doing that, you're indirectly telling everyone the type of genre you like, the type of stuff you read and more!"
    mc "I guess I never really thought about it like that."
    mc "Still, I don't mind."
    mc "If there are more people who share my interests in the club, then it's good."
    s 1bq "Yeah! I'm glad you could look at the positives."
    s 1bd "Like Yuri probably won't do that! She'll probably choose a horror book that everybody likes but not one that particularly resonates with her."
    s "She probably won't even choose to vote for the books she's going to choose."
    s "I just wish she was more outgoing, you know?"
    mc "It's her personality. She can't really help it, Sayori."
    s 1ba "I know..."
    s "It's just a thought."
    "Sayori turns to the wardrobe."
    s 1bc "Well, I gotta pick some books too!"
    s 1bd "Then...I think we're done!"
    mc "Are you going to go shopping for the items on Yuri's list?"
    mc "If you are, then I should help."
    mc "I don't want to feel useless."
    s 1ba "Well, I'm not exactly going shopping."
    s "And I think it's for the best that you don't go with me here, [player]."
    mc "No way! Of course I'm going with you."
    s 1bd "I really think you should just take your books and leave."
    s "It's for the best."
    mc "Sayori, I chose to help you."
    mc "You have to let me be there for you. I won't take no for an answer."
    s 1bk "..."
    s "I know you won't."
    s "Which is why I have to do th{nw}"
    $ _history_list = []
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    scene bg bedroom
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    "Helping Sayori today was pretty easy."
    window auto
    "I was expecting to do something a lot more difficult, considering we had to help everyone else."
    "She seemed to have most of it handled by herself."
    "I search my bag for the books I got from Sayori's house."
    "They all seem to be there."
    "I ended up taking a novel and three manga."
    "The novel was just a popular book that I'm sure everyone would know."
    "The manga on the other hand, was a series that I liked."
    "I don't think many people have really heard of it, so I was surprised when Sayori had a copy in her room."
    "We still have a long way to go until Inauguration Day."
    "I wonder how everyone else is doing."
    "Does Yuri have an atmosphere planned already?"
    "Will Natsuki be able to cater for the amount of people that might visit?"
    "Is Monika going to perform a masterpiece on the day?"
    "These are the questions racing through my mind right now."
    "It's hard to think about anything else."
    "I really hope Sayori and I can make their parts even more amazing."
    "But I can't help but worry about Sayori too."
    "She sounds like she has a lot on her mind."
    "It's like she has this heavy burden that she doesn't want anyone to know about..."
    "...or help with."
    "I have to make it clear to her that I want to help."
    if sayori_confess and not sayori_dumped:
        "After all, she is my girlfriend."
    else:
        "After all, she's my best friend."
    return

label ch14_natsuki_outcome1_date:
    return

label ch14_natsuki_outcome3_date:
    mc "Hey, Natsuki..."
    mc "I've been meaning to ask you something."
    mc "This is probably the best opportunity I'm going to get."
    n 2bg "What is it?"
    n "I was in the middle of thinking of some things we could do."
    n 2bc "My mom is a really good baker so I thought--"
    mc "Actually, I was thinking of stuff we could do as well."
    n "Okay? What are you thinking?"
    mc "This is kind of awkward for me but..."
    mc "I was thinking we could go out somewhere."
    n "What do you mean?"
    n "To get supplies for baking or something?"
    n "My parents went out shopping earlier today so we have plenty..."
    mc "No, I mean..."
    mc "I'll just say it."
    n "[player], are you okay?"
    mc "I'm a little bit nervous actually but here goes nothing."
    mc "I was thinking we could go on a date."
    show natsuki at h11
    n 1bo "What?!"
    "Natsuki clearly didn't expect that."
    n "D-Didn't you hear what I said?"
    n 1bp "I..."
    mc "I heard what you said."
    mc "And I thought about it--"
    n 1bo "So what's the big idea then?!"
    mc "Well, I figured there really wasn't going to be a better time."
    mc "You know I like you."
    mc "I just hope the feeling is mutual."
    if sayori_dumped:
        n 1br "Aren't you with Sayori?!"
        n "If she knew you did something like this...!"
        mc "About that..."
        mc "We broke up."
        n 1bp "What?!"
        n "When did {i}that{/i} happen?"
        mc "It doesn't matter."
        mc "What matters is that I realized I like you more than Sayori."
        mc "So..."
        n 1bn "..."
    else:
        n 1bs "{i}(Of course it is...){/i}"
        "Natsuki mumbles something that I can't really hear."
        mc "What did you say?"
    n 1bm "[player], I don't know what to say."
    n "I really wasn't expecting you to ask like this."
    n "Especially with all that's going on."
    n "We're not going to be able to do much at all if we do what you're talking about."
    mc "I can always stay a little longer if I have to."
    mc "If not, then we'll just have to work extra hard tomorrow."
    mc "But I noticed something."
    n 1bq "And what would that be...?"
    mc "You didn't say no to my suggestion of a date."
    mc "Does that mean you'll go with me?"
    n 1bo "...!"
    n "F-Fine but only because I'd have to work alone otherwise."
    n "S-So don't get any ideas, okay?"
    mc "I won't."
    "So she actually accepted the invitation to go on a date."
    "I didn't really expect to get this far."
    "I have no idea where we're going to go."
    n 1bc "Before we go anywhere..."
    n "There's something you need to do first."
    mc "And that is?"
    n 1by "You're going to have to talk to my parents."
    mc "What?!"
    "Why does she look so smug to say that?"
    n "It only makes sense, doesn't it?"
    n "You're asking to take their daughter on a date."
    n "They should know about it."
    mc "I guess but--"
    n 1bd "No buts."
    n "That's my condition."
    mc "You seem like you're having way too much fun with this."
    "Natsuki smiles."
    n "Well, let's go find them."
    n "You have some explaining to do, [player]."
    "What have I gotten myself into...?"
    scene bg n_livingroom with wipeleft_scene
    "We find both of her parents cleaning the living room."
    "There's stains on the walls and a faint smell coming from somewhere."
    "But apart from that, they seem to be doing a good job cleaning up the place."
    show natsuki 1ba zorder 2 at t31
    n "Mom, dad!"
    n "[player] has something to tell you."
    show momsuki 1a zorder 2 at t32
    show dadsuki 1c zorder 2 at t33
    "Haruki and Yasuhiro immediately stop what they're doing and head over to where we're standing."
    "They seem a lot more intimidating now for some reason..."
    show momsuki zorder 3 at f32
    mo "He does?"
    "Haruki looks at me curiously."
    mo "And what would that be?"
    show momsuki zorder 2 at t32
    mc "Well..."
    mc "Y-You see mister and missus Natsuki..."
    "Did I seriously just say that?"
    show momsuki 1d zorder 3 at f32
    mo "Are you okay?"
    mo 1b "And please, just call me Haruki."
    show momsuki zorder 2 at t32
    show dadsuki 1b zorder 3 at f33
    d "You already call me Yasuhiro, why change now?"
    d "Hmm...you seem a little nervous, [player]."
    d "What's the matter?"
    show dadsuki zorder 2 at t33
    "Asking Natsuki was hard enough already."
    "Did she do this just to see me make a fool out of myself?"
    "And I don't think parents are meant to see the boy their daugher is going out with until they're official, right?"
    mc "N-Nothing is the matter!"
    mc "I just want to make an announcement, that's all."
    show momsuki 1d zorder 3 at f32
    mo "An announcement?"
    mo "And it affects all of us?"
    show momsuki zorder 2 at t32
    show dadsuki 1i zorder 3 at f33
    d "Weren't the two of you meant to be doing preparations?"
    d "Does this have something to do with that?"
    show natsuki 2bj zorder 3 at f31
    show dadsuki zorder 2 at t33
    n "Not exactly..."
    n "It's still pretty important though."
    n "And I don't want to miss it."
    n "Go on, [player]."
    n "Tell them!"
    show natsuki zorder 2 at t31
    mc "W-Well, in the club we write poems..."
    mc "Everyone has a particular style."
    show dadsuki 1c zorder 3 at f33
    d "Ah, yes."
    d "I know about this."
    show natsuki 1bc zorder 3 at f31
    show dadsuki zorder 2 at t33
    n "Wait, you do?"
    n "I never told you, did I?"
    show natsuki zorder 2 at t31
    "Haruki eyes Yasuhiro and he avoids her gaze."
    show dadsuki zorder 3 at f33
    d "Anyway, what's your point?"
    d "Just get to it."
    show dadsuki zorder 2 at t33
    mc "Alright...how do I say this...?"
    "I take a deep breath."
    "This is it."
    "Now or never."
    mc "I'm planning to take your daughter out on a date today."
    show natsuki 1by
    show dadsuki 1l
    "Natsuki bursts out laughing."
    "Yasuhiro just looks at me wide-eyed."
    show momsuki 1e zorder 3 at hf32
    mo "What?!"
    mo "A-Are you serious?"
    show natsuki 2bd zorder 3 at f31
    show momsuki zorder 2 at t32
    n "Mom, he's completely serious."
    n "And I accepted."
    show natsuki zorder 2 at t31
    show momsuki 1g zorder 3 at f32
    mo "Now, just wait a second."
    mo "[player] seems like a nice guy and everything but..."
    "She looks at me from top to bottom."
    mo 1h "Natsuki, are you completely sure about this?"
    mo "You're not just messing with me, right?"
    mo 1g "I only just got back...I don't think my heart is ready for one of your pranks yet."
    show natsuki 2bc zorder 3 at f31
    show momsuki zorder 2 at t32
    n "It's not a prank or anything like that!"
    n "He asked me if I wanted to go on a date with him and I said yes."
    n "That's all there is to it."
    n 1bd "And I know he isn't much but it's fine!"
    show natsuki zorder 2 at t31
    show dadsuki 1i zorder 3 at f33
    d "I'm not against [player] going with our daughter."
    d "He and the others in that club of theirs took better care of Natsuki than I did."
    d "I think he's got what it takes to make our daughter happy, Haruki."
    show momsuki 1h zorder 3 at f32
    show dadsuki zorder 2 at t33
    mo "It's just so sudden!"
    mo "How can {i}I{/i} be sure that our daughter will be okay?"
    show momsuki zorder 2 at t32
    mc "Haruki, I know you don't really have a reason to believe me."
    mc "We only met yesterday so I can understand that."
    mc "But I promise I'll take care of Natsuki."
    mc "She's really special to me."
    mc "I wouldn't let anything bad happen to her."
    show natsuki 2bg zorder 3 at f31
    n "[player], do you really mean that?"
    n "I never knew you felt that strongly about me..."
    n "I just thought you were..."
    show natsuki zorder 2 at t31
    show momsuki 1g zorder 3 at f32
    mo "..."
    mo "Okay."
    show momsuki zorder 2 at t32
    mc "Okay...?"
    show momsuki zorder 3 at f32
    mo "Okay, give my daughter a great date."
    show momsuki zorder 2 at t32
    mc "Just like that?"
    mc "What made you change your mind?"
    show momsuki zorder 3 at f32
    mo "You had this look in your eyes."
    mo "I know that's not really a reason but..."
    mo "I don't know, something about it just reminded me of happier times."
    show momsuki zorder 2 at t32
    show dadsuki 1b zorder 3 at f33
    d "So you have our approval."
    d "If you don't mind me asking..."
    d "Where exactly are you taking Natsuki?"
    d "Do you have your date planned out already?"
    show dadsuki zorder 2 at t33
    mc "Actually--"
    show natsuki 1bb zorder 3 at f31
    n "Of course he does!"
    n "He has this whole trip planned out for the city!"
    n 1bj "We're just going to get some things and then head off."
    n "Thank you mom and dad!"
    show natsuki zorder 2 at t31
    "Natsuki approaches her parents and the three of them embrace."
    "I can't help but smile at their happy family."
    "I'm glad things turned out this way for Natsuki."
    show momsuki 1c zorder 3 at f32
    mo "You too have fun!"
    mo "First dates are always the best ones."
    mo "Natsuki, your dad and I will finish the cleaning the house."
    mo "So just enjoy your day, okay?"
    show momsuki zorder 2 at t32
    show dadsuki 1f zorder 3 at f33
    d "I hope you make a good impression, [player]."
    d "Best of luck to both of you."
    show momsuki at thide
    hide momsuki
    show dadsuki at thide
    hide dadsuki
    show natsuki at t11
    "Haruki and Yasuhiro go back to cleaning the living room."
    n 1bd "That went well."
    mc "You just wanted to see how I'd react, didn't you?"
    n 1ba "No...why would I do that?"
    mc "Whatever..."
    n 1bc "[player]..."
    n "Do you actually have a plan?"
    n "You sounded like you didn't."
    n "Which is why I interrupted you."
    mc "I'll be honest, Natsuki."
    mc "I didn't expect to get past your parents."
    mc "Or for you to go on a date with me."
    mc "I was thinking we could catch the train into the city and go from there."
    mc "Unless you have any better ideas?"
    n "I don't really..."
    n "I guess we can figure it out on the way there...?"
    "I have this really random idea in my head."
    "Natsuki told me about the portrait that Yasuhiro destroyed."
    "So maybe..."
    mc "Actually, I just thought of something."
    jump ch13_natsuki_outcomeshared_date

label ch13_natsuki_outcomeshared_date:
    n "You have an idea for our date?"
    mc "It's not really traditional."
    mc "But you know that portrait that you told me about?"
    n 1bg "The one my dad destroyed?"
    n "What about it?"
    mc "Well, I was thinking we could do something about it."
    mc "It's really important to you, right?"
    n 1bc "It's like a symbol of a better time."
    n "When it wasn't broken, it was like my family was whole..."
    n "And that everything was going to be okay."
    n 1bb "What exactly are you thinking of doing?"
    mc "I was thinking we could put it back together."
    n 1bi "What?"
    n "How did you come up with this idea?"
    mc "I figured it's a pretty important thing in your life."
    mc "It has a lot of sentinmental value, doesn't it?"
    n 1bq "Well...yeah but..."
    n "How exactly are we going to do that?"
    mc "I was thinking we could hire someone to do it for us."
    mc "While that's happening we can go around the city looking at bakeries."
    n 1bk "To get ideas for our own preparations?"
    mc "Not only that."
    mc "We could buy some of it and have some sort of meal together."
    n "That would be nice..."
    n "I didn't really have a great lunch."
    mc "You didn't?"
    n 1bs "I guess you could say I'm used to eating such a small amount of food."
    n "I didn't want things to change from how they were just yet."
    mc "So in a way, I'm kinda speeding it up, right?"
    n "I guess you are..."
    mc "I hope it's not gonna cause any problems."
    mc "I wouldn't want to hurt you."
    n 1bq "N-No...of course it isn't."
    n "But there is problem with doing the portrait idea."
    mc "What would that be?"
    if ch12_outcome == 3:
        n 1bh "My parents aren't just going to let you or me take it away from this house."
        n "Even if it's broken, it's not like they're just going to throw it away."
        mc "Then we don't tell them."
        mc "They're busy cleaning after all."
        n 2bf "Are you telling me to lie to my parents?"
        mc "Not exactly..."
        mc "This is partly for them, isn't it?"
        mc "If we bring them the portrait but fixed, they'll love it, right?"
        mc "It's like a pleasant surprise."
        n 2bb "I guess but..."
    else:
        n 1bh "My dad isn't just going to listen you take it away from the house."
        n "Just because it's broken doesn't mean he's gonna give it away."
        mc "Then we won't tell him."
        mc "He's busy cleaning after all."
        n 2bf "Are you telling me to lie to my dad?"
        mc "Not exactly..."
        mc "We're doing this partly for Yasuhiro too, aren't we?"
        mc "If we bring him the portrait that he ruined, he'll be thankful, won't he?"
        mc "It's like a pleasant surprise."
        n 2bb "I guess but..."
    mc "And if anything goes wrong, I promise I'll take all of the blame."
    n 2bo "What? No!"
    n "You can't do that!"
    mc "Why not? It was my idea after all."
    mc "You shouldn't take any of the blame for this."
    n 2bs "How about you promise me something else instead?"
    mc "...?"
    n 2bq "Instead of promising to take all of the blame if anything goes wrong..."
    n "Promise me that nothing will go wrong."
    mc "Natsuki, I--"
    n 2bn "Promise me, [player]."
    "Natsuki looks directly into my eyes."
    "There's no way I can control how this day is going to go."
    "I can't just make a promise like that."
    "Suddenly, my phone starts ringing."
    n 2bp "...!"
    n 2bo "Were you expecting a call?"
    mc "No...I have no idea who this is."
    "I get my phone from my pocket and notice who's calling."
    "It's Sayori."
    if sayori_dumped:
        "This is going to be a tough call."
    mc "Can I take this?"
    n 2bs "Why are you asking me?"
    n "I'm not going to stop you."
    mc "Right..."
    show natsuki at thide
    hide natsuki
    "I move a few metres away from Natsuki and answer the phone."
    mc "Hello?"
    if not sayori_confess:
        mc "Sayori, why are you calling?"
        s "Hi [player]!"
        s "How's your day with Natsuki doing?"
        mc "It's going...okay."
        mc "Is that the only reason you called?"
        s "Did you ask her already?"
        mc "E-Eh?"
        mc "Ask her what?"
        s "Come on, [player]."
        s "It's pretty obvious."
        s "You asked her on a date!"
        mc "What? How did you--"
        s "I want you to be happy, [player]."
        s "So I'm going to help you make this perfect, okay?"
        mc "What are you talking about?"
        s "Where are you going to take her for your date?"
        mc "Huh?"
        mc "I don't know we were going to have this portrait of hers--"
        s "There's this store in the city."
        s "It's a portrait restoration business and the shopkeeper owes me one."
        mc "The shopkeeper what?"
        s "It's near the train station in the city, so you won't have to go far."
        mc "Sayori, slow down a little!"
        s "I'll talk to you more about it in the train."
        s "Have fun, [player]!"
    else:
        mc "Sayori?"
        s "You asked her...right?"
        mc "...I did."
        "There's a brief silence on the phone."
        s "Okay. I already knew that."
        mc "..."
        s "I still want you to be happy, [player]."
        s "Don't get me wrong."
        s "So I'm going to do everything in my power to make this the perfect day for you."
        mc "Everything in your power?"
        mc "What do you mean?"
        s "What are you doing for your date?"
        mc "What?"
        s "Well?"
        mc "There's this portrait and--"
        s "There's this store in the city."
        s "The shopkeeper there owes me one."
        s "It'll be just the place for it."
        mc "What? Sayori?"
        s "I'll text you the address."
        s "It's near the train station in the city, so you won't have to go far."
        mc "Just hold on a sec--"
        s "I hope you have a great time with her."
        s "Goodbye, [player]."
    "Sayori hangs up."
    "Well, that was weird..."
    show natsuki 1bc zorder 2 at t11
    n "So who was it?"
    mc "Um..."
    n "You don't have to tell me."
    mc "No, it was just Sayori."
    n 1bq "Oh..."
    mc "Look, we'll worry about it later."
    mc "Right now, we need to get that portrait."
    n 1bj "Right..."
    n "I know exactly where it is."
    n "But we're going to need a pretty big bag."
    mc "Let's get it then."
    n "I have one in my room."
    n "The portrait is in my parent's room."
    n "I'll get the bag, you go to my parent's room."
    mc "Which one is that?"
    n "Ugh..."
    scene bg n_dadroom with wipeleft_scene
    "I can only assume this is her parent's room judging by the bed."
    "I hope I'm in the right room at least..."
    show natsuki 1ba zorder 2 at t11
    n "Glad to see you found the right room."
    "Natsuki drops a big bag on the floor."
    mc "Is the portrait really that big?"
    n 2bc "It's pretty heavy too."
    mc "I see..."
    mc "Where is it exactly?"
    n "In here."
    "Natsuki opens the closet."
    "Just like she said, there's a ruined portrait in there."
    "It's torn to shreds and scribbled all over."
    "There's garbled writing and drawings of {i}something{/i} all over it."
    "For some reason, just looking at it makes me feel sick."
    n 2bg "Well, we should move quickly."
    n "I don't know how long it's going to clean downstairs."
    n "So the sooner we get out of here, the better."
    mc "Right."
    "Natsuki and I pick up the pieces and put them into the bag."
    "As I kneel down to pick the final piece, I notice something underneath the bed in the corner of my eye."
    "It's like...writing?"
    mc "Natsuki, there's something--"
    n 2be "There's no time, [player]!"
    n "We have to go."
    mc "Alright..."
    "I guess that's for another time."
    "Or maybe I shouldn't tell Natsuki."
    "It seems pretty {i}not{/i} normal to have something like that under your bed."
    "It'll probably be cleaned before we get back from our date anyway..."
    n 2bb "Are you gonna carry it or not?"
    mc "Oh, right."
    "I lift up the bag and immediately drop it due to it's weight."
    n 2be "Be careful with that!"
    mc "Sorry, it's heavier than I thought."
    "I lift up the bag again but with both hands."
    mc "Alright, let's go."
    scene bg n_corridor with wipeleft_scene
    "As we head downstairs, Natsuki signals for me to be quiet."
    "She opens the door trying to make as little noise as possible but suddenly Yasuhiro turns towards me."
    show dadsuki 1e zorder 2 at t21
    d "What are you doing with that bag?"
    d "It doesn't seem like something you'd take on a date."
    show natsuki 1bb zorder 3 at f22
    n "It's for our preparations too!"
    n "[player] suggested that we should get some supplies for our preparations while we're in the city."
    show dadsuki 1f zorder 3 at f21
    show natsuki zorder 2 at t22
    d "Is that so?"
    d "Well, in that case..."
    d "Good luck with your preparations."
    show dadsuki zorder 2 at t21
    mc "Thanks, Yasuhiro."
    "Yasuhiro nods at me before returning to cleaning."
    show dadsuki at thide
    hide dadsuki
    show natsuki at t11
    mc "That was some good lying."
    n 1be "Whatever, let's just go!"
    mc "After you."
    mc "I don't exactly know the nearest train station from here."
    n 2be "Ugh, useless!"
    mc "I'm the one carrying the portrait!"
    mc "It's heavy, you know."
    n "Just try to keep up, okay?"
    mc "I can try."
    jump ch13_natsukidate

label ch13_natsukidate:
    $ natsuki_date = True
    scene bg city_day
    play music t12n fadeout 2.0
    "So we caught the train to the city."
    "Now we're on our way to some sort of image restoration place."
    "I haven't heard of this place before but the text Sayori sent was sure it was just the place."
    "I guess that's what happens when you suggest something but don't really have a plan."
    "But what's important is that I'm here with Natsuki."
    "I just hope things don't go wrong."
    "I did make a promise after all."
    show natsuki 1ba zorder 2 at t11
    n "Do you still have the portrait with you, [player]?"
    n "You didn't leave it on the train, did you?"
    mc "No, I have it right here. Don't worry about it."
    n 2bc "How did you even find out about this place?"
    mc "Someone told me about--"
    n "It was Sayori, wasn't it?"
    mc "...Yeah."
    n "Did she know this was going to happen?"
    mc "What do you mean?"
    n 2be "Who just knows where a restoration shop is?"
    n "I doubt Sayori just has a few portraits or photographs that she wants restored."
    n "And isn't it convenient that she just happened to figure out where you should go?"
    mc "Wait...how did you know that?"
    n 4bd "It's pretty easy to look over at your phone."
    "Natsuki looked at my phone while I was talking to Sayori?"
    "Just how much did she see?"
    n "Don't worry, I didn't see too much."
    n 2ba "But you should really be careful how you hold your phone."
    n "People might be looking."
    mc "You were the only one looking..."
    n 2be "Well, yeah! What if someone who wasn't so close to you was though?"
    n 4by "What would they do if they found out about Mr. Cow?"
    mc "...!"
    "Natsuki shows a wide smile."
    n "I'm not going to tell anyone!"
    n 4bk "Sayori would be pretty mad!"
    n "Besides, I don't want to ruin this time with you."
    mc "I think it's already ruined..."
    "I say that jokingly."
    n 4bd "That's a shame!"
    n "We're barely into our date and you've given up."
    mc "Good thing I'll have no memory of it."
    "Natsuki suddenly stops."
    mc "Is something wrong? I was just joking..."
    n 2bc "[player]..."
    n "I want to remember this day."
    n "No matter how it goes, I want to remember."
    n 2bg "So don't joke about something like that, please."
    mc "I'm sorry, I shouldn't have said that."
    n 2bq "..."
    n 2bi "You can make it up by hurrying your pace!"
    mc "Hey, this thing weighs a lot."
    mc "I don't know how you can expect me to move any faster."
    n 1bd "You'll manage!"
    "Natsuki starts moving faster."
    mc "This isn't even mine, you should be the one carrying it!"
    n 1bj "Oh look, there it is!"
    show natsuki at lhide
    hide natsuki
    "Natsuki hurries off to the store entrance and steps inside."
    "What's with the sudden change in personality?"
    "Is this who Natsuki is under that tough exterior?"
    "I suppose I'll find out after we get this thing restored."
    "Suddenly, I start getting a call from Sayori."
    mc "Great timing..."
    "I get my phone and answer the call."
    mc "Hey, Sayo--"
    s "[player], how's the date going?"
    mc "It's going well, I guess."
    mc "We haven't really done anything yet but..."
    mc "Natsuki seems really excited."
    mc "It's like she's a completely different person."
    s "Oh really? You'll have to tell me what she does."
    s "None of us really know Natsuki outside of her tough exterior that she likes to show."
    s "I guess you're the first person in a while to really see the real her."
    mc "Something seems completely different about her though."
    mc "I can't quite put my finger on it..."
    s "Oh...that's what you meant."
    s "Just hold on a second."
    mc "What are you doing?"
    s "Nothing~"
    s "She should be back to normal now."
    mc "How would you know that?"
    s "Ehehe, just a feeling."
    mc "Alright..."
    s "Anyway, enjoy your date!"
    s "I hope you two have a great time, really!"
    if sayori_dumped:
        mc "You seem to have gotten over it pretty quickly."
        mc "Are you sure you're okay?"
        s "I've had a long time to think, [player]."
        s "Trust me..."
        "It's been an hour since we broke up..."
        "That's not enough time for anyone."
        "Yet, I feel like she's telling the truth."
    mc "Before you go, I want to ask you something."
    s "What is it?"
    mc "How did you find out about this place?"
    mc "Natsuki even said how convenient it was that you knew of a place like this."
    s "Is it really that important?"
    s "The answer isn't really interesting."
    mc "I'd still like to know."
    mc "Not that I don't appreciate the help but it all seems too...planned."
    s "You think I'm trying to hurt the two of you?"
    mc "Well, no--"
    s "I didn't even know you two would go on a date today."
    s "There's so many things that I can't predict the real outcome of."
    s "I have to think of every single possibility because the worst could happen if I don't."
    s "Do you know how tiring that is, [player]?"
    s "Do you know how..."
    "Sayori takes a deep breath."
    mc "Are you okay?"
    mc "I didn't mean to make you angry or anything."
    mc "After all, you helped make this day possible."
    mc "I was just curious because it's a really good coincidence."
    s "There are no coincidences, [player]."
    "Sayori hangs up."
    "What was that about...?"
    "What did she mean there are no coincidences?"
    show natsuki 1ba zorder 2 at t11
    n "[player], come on."
    "Natsuki steps outside the shop."
    "It's a modern looking place called 'Restoration'."
    "I've never heard of it before but Sayori said it was the perfect place."
    "The outside looks really clean and it has displays of various portraits and paintings."
    n 1bc "The shopkeeper is waiting for you. I've already told him about the portrait."
    mc "R-Right..."
    mc "I'm coming."
    n 2bg "I know it's none of my business but..."
    n "Who were you on the phone with just now?"
    mc "You saw that?"
    n 2bq "I didn't hear any of it..."
    n "And you don't have to tell me or anything...!"
    mc "It's fine. It was just Sayori."
    n 1bu "Huh? What was it about?"
    mc "She just wanted to wish us a good time."
    "I probably shouldn't mention the outburst Sayori had."
    n 1bt "That's...kind of her, I guess."
    mc "Anyway, this portrait isn't going to fix itself."
    mc "Let's head inside."
    "I open the door for Natsuki."
    mc "After you."
    "Natsuki tries to hide a smile."
    n 1bw "I don't need your help!"
    mc "You don't need it, but I know you want it."
    n 1bv "You...!"
    "Natsuki's face turns a bright red."
    show natsuki 1by at h11
    n "Shut up!"
    "Natsuki walks into the shop."
    show natsuki at lhide
    hide natsuki
    mc "Well, here goes nothing..."
    scene bg portraitshop_day with wipeleft_scene
    $ cl_name = "???"
    "The shop's interior is filled with canvases."
    "It looks more like an art class than somewhere people would restore portraits."
    "Is this the right place?"
    show natsuki 1bc zorder 2 at t11
    n "I don't see anyone in here, [player]."
    n "Maybe they're closed?"
    mc "The door wouldn't be open if that's the case..."
    mc "This is the right address..."
    mc "Maybe Sayori got the wrong pl--"
    cl "Hello there!"
    show natsuki zorder 2 at t21
    show mysteriousclerk 2a zorder 3 at f22
    cl "Sorry for the mess, but there was an art class just before!"
    "Suddenly, a loosely kept man appears in front of us."
    "He seems like the type of person who would keep a messy room..."
    "Maybe that's how he and Sayori know each other."
    cl 5b "Now, how can I help you?"
    show natsuki 2bc zorder 3 at f21
    show mysteriousclerk zorder 2 at t22
    n "Um...who are you?"
    show natsuki zorder 2 at t21
    show mysteriousclerk 5k zorder 3 at f22
    $ cl_name = "Mysterious Clerk"
    cl "Me? I'm the keeper of this fine establishment!"
    cl 5b "Any more questions?"
    show mysteriousclerk zorder 2 at t22
    mc "My friend, Sayori told me--"
    show mysteriousclerk 2e zorder 2 at f22
    cl "Oh, yes, yes, yes."
    cl "She told me you were coming a while ago!"
    cl "Come, come!"
    cl 2a "This way!"
    "The clerk points us towards a corner of the room."
    "There's assorted tools and lots of glasses of various sizes."
    cl 1b "You're here for a portrait restoration, right?"
    cl "Oh, of course you are!"
    show natsuki 2bf zorder 3 at f21
    n "Can you slow down?!"
    n "We can't keep up...!"
    show natsuki zorder 2 at t21
    mc "Yeah! We still have some questions...!"
    mc "Like--"
    show mysteriousclerk 5f zorder 3 at f22
    cl "Rightio! Where's the portrait?"
    cl "In the bag, it must be!"
    "The clerk tries to pulls the bag from me."
    "I resist and take it back."
    cl 4g "What's the matter boy?"
    cl "Don't you want it fixed?"
    show mysteriousclerk zorder 2 at t22
    mc "Well, yeah but--"
    show mysteriousclerk 5k zorder 3 at f22
    cl "Then hand it over!"
    "A strange look appears in the man's eyes."
    cl "Don't you have somewhere to be?"
    show mysteriousclerk zorder 2 at t22
    "Natsuki tugs at me."
    show natsuki 1bg zorder 3 at f21
    n "[player], I don't like this."
    n "Maybe we should go..."
    n 1bq "He seems kinda..."
    show natsuki zorder 2 at t21
    show mysteriousclerk 5f zorder 3 at f22
    cl "Erratic?"
    cl 5k "Hyper?"
    cl 5i "Crazy?"
    cl 5b "Insane?"
    cl 5w "Personally, I'd go with all of the above."
    "The clerk begins to slow down his voice."
    cl 3b "Look, young lady."
    cl "I'm all of those things but that doesn't stop me from doing my job."
    show natsuki zorder 3 at f21
    show mysteriousclerk zorder 2 at t22
    n "And what exactly is your job?"
    n "You haven't exactly given us any reason to let you just have this thing that's so valuable to me!"
    n "I don't even know if I'm at the right place!"
    show natsuki zorder 2 at t21
    show mysteriousclerk 4a zorder 3 at f22
    cl "Skepticism...good!"
    cl "I like that!"
    cl "This is definitely the right place!"
    cl "Art classes and restoration by yours truly."
    "Natsuki doesn't look impressed."
    cl 4b "I suppose I'll just have to show you."
    "The man walks up to the front of the room."
    "He pushes a button and suddenly the blackboard flips around."
    "Natsuki and I are taken by surprise at what's happening."
    "Didn't expect something like that from someone like him..."
    "After it's finished turning over, there's portraits hanging from the wall where the blackboard was."
    "All of them look photorealistic."
    "I'm sure some of them actually are photos."
    cl 1a "I restored all of these."
    cl "Most of them are quite old, I'd say a few centuries or so."
    "He points to one of them."
    cl 1c "This one, I did rather recently."
    show mysteriousclerk zorder 2 at t22
    mc "Don't those belong to people?"
    mc "Why do you still have them?"
    show mysteriousclerk 1f zorder 3 at f22
    cl "Oh no, young man."
    cl "These are ones I've done in my spare time."
    cl 1b "All the ones people send me are already back in their homes..."
    cl "...or wherever it is they keep them."
    cl 4d "I'm not one to judge."
    "He shows a faint smile."
    cl 4a "Now, do you need any more proof?"
    show natsuki 1bs zorder 3 at f21
    show mysteriousclerk zorder 2 at t22
    n "I guess not..."
    n "But there's still so much I want to know..."
    n "Like how--"
    show natsuki zorder 2 at t21
    show mysteriousclerk 4n zorder 3 at f22
    cl "Ah, ah!"
    cl "You need to get going, after all!"
    cl "Young love, so sweet."
    show mysteriousclerk zorder 2 at t22
    mc "Y-Young love?"
    mc "W-We're not..."
    mc "She's just...!"
    "I put the bag on the floor."
    "I look towards Natsuki who looks just as flustered."
    show natsuki 1bo zorder 3 at f21
    n "Yeah...!"
    n "We're just...!"
    n 1bp "You don't...!"
    n "Ugh!"
    show natsuki zorder 2 at t21
    show mysteriousclerk 1a zorder 3 at f22
    cl "Ehehe, I'm only messing with you."
    cl "Now about the payment..."
    "Natsuki and I turn towards each other."
    cl 1b "It's on the house!"
    cl "Well, actually..."
    cl "Someone else covered it and..."
    cl 1f "It's a long story, just get going already!"
    "The clerk takes the bag and unzips it."
    "He pulls out the portrait and stares it."
    cl 1e "I see..."
    cl "I'll get this done before you come back, I promise you this."
    "He takes one of the glasses on the table and puts it on."
    cl "Let's see..."
    show mysteriousclerk zorder 2 at thide
    hide mysteriousclerk
    show natsuki zorder 2 at t11
    mc "Well..."
    n 1bm "I'm sure he knows what he's doing, [player]."
    mc "I should be the one reassuring you."
    mc "But yeah, he's a strange isn't he?"
    cl "I heard that!"
    mc "..."
    mc "See what I mean?"
    n 1bk "Yeah..."
    n "But we shouldn't think about that now."
    n "We have to get going, don't we?"
    mc "You're right..."
    cl "Oh! Be sure to change the open to close on your way out."
    cl "This requires my undivided attention."
    cl "I don't need more pesky customers interrupting me while I'm at work."
    mc "S-Sure..."
    "Are we pesky to him...?"
    "I open the door for Natsuki and flip the sign."
    mc "Time to go to a bakery, I guess."
    n 2ba "Yeah, let's go!"
    show natsuki at thide
    hide natsuki
    "Natsuki exits the building and pulls out her phone."
    "Just as I'm about to leave, I feel a hand on my shoulder."
    show mysteriousclerk 1e zorder 2 at t11
    cl "Young man."
    cl "Before you go..."
    mc "I didn't even see or hear you leave where you were sitting."
    mc "How did--"
    cl 1i "She's already corrupted, isn't she?"
    mc "What?"
    cl "In this timeline, she's all messed up."
    cl "I can tell..."
    cl 1j "Stupid, stupid girl."
    mc "Huh? Who are you talking about?"
    cl "I hope Naomik turns out okay..."
    mc "Naomik? Wha--"
    cl 1a "Go on, your date is waiting."
    show mysteriousclerk at thide
    hide mysteriousclerk
    "The clerk walks back to the corner and pulls out a magnifying glass."
    "Who's Naomik...?"
    "I gently close the door behind me and meet up with Natsuki outside."
    scene bg city_day
    show natsuki 1bc zorder 2 at t11
    with wipeleft_scene
    n "What took so long for you to get out?"
    n "Did you see something?"
    mc "Not exactly..."
    mc "He said something really weird."
    mc "Something about timelines and a..."
    mc "...Naomik?"
    mc "I don't know what that means."
    n 2bc "Naomik, huh?"
    n "That doesn't sound like anyone I know..."
    n 2bi "And that timelines thing..."
    n "We both know that he's kinda crazy, [player]."
    mc "I guess so..."
    mc "Still, I can't help but feel there's at least some truth in what he's saying."
    "I look back at the store."
    "There's something weird about that place..."
    "...And the person running it."
    mc "I think there's a bakery around the area."
    n 2be "Do you even know where you're going?"
    mc "No...but that's half the fun."
    show natsuki 2ba
    "Natsuki and I walk around the city for a while."
    "We visit a few bakeries around the place."
    "They have some amazing things on display."
    "There were lots of intricate designs on bread that look like something I'd never be able to do."
    "But not really what we're looking for when it comes to Inauguration Day."
    "We're more focused on things we could actually make."
    mc "Maybe we could go to a cake shop."
    n 2bb "Yeah, may--"
    play sound "mod_assets/sfx/stomachgrowl.ogg"
    $ pause(2.0)
    "Suddenly a sound comes from Natsuki."
    mc "Did you hear that?"
    show natsuki 1bp at h11
    n "H-Huh? What?"
    n "I-It was nothing!"
    play sound "mod_assets/sfx/stomachgrowl.ogg"
    $ pause(2.0)
    "The sound happens again."
    mc "Are you okay?"
    mc "If you're hungry, we can--"
    n 1bo "I'm fine!"
    "Natsuki doesn't seem to want to admit it."
    "She seems pretty hungry right now."
    "I did say we were going to have something to eat while we're here."
    "I guess now is a good a time as any."
    mc "Well..."
    mc "I know this place we could go to."
    mc "They have some really nice desserts."
    n 1bq "Desserts?"
    mc "I was gonna treat you to an afternoon meal."
    mc "Nothing too fancy, maybe just something to eat before dinner."
    mc "How does that sound?"
    n 1bs "Y-Yeah...whatever."
    n "Just make sure we get there quickly."
    mc "It will take no time at all."
    n "It better not!"
    hide natsuki
    with wipeleft
    "Just like I said, it took us almost no time to get here."
    "When I say that, I mean it feels like only literal seconds have passed."
    "But I know that's just impossible."
    "How?"
    "Because it's almost sunset."
    "I wasn't keeping track of time but it was probably almost sunset by the time we got to the city."
    show natsuki 1bc zorder 2 at t11
    n "Is this it?"
    "Natsuki looks at the place we're standing outside of."
    mc "Yeah, this looks like the place."
    n 1be "Looks like?!"
    n "You don't sound too sure of yourself."
    n "This better--"
    play sound "mod_assets/sfx/stomachgrowl.ogg"
    $ pause(2.0)
    "I hear that sound again."
    "It's a lot louder this time."
    n 1bo "...!"
    mc "Let's just get inside, Natsuki."
    mc "Even if it isn't the right place, it's clearly somewhere we can eat."
    mc "And I can tell you're eager to try the food."
    n 2bg "Hmph! This better be good."
    mc "I'll pay for it all, so don't worry about--"
    n 2be "Ridiculous!"
    n "I don't expect you to pay for me, [player]."
    n "I'm perfectly capable of paying for myself!"
    mc "I didn't say you weren't but...it's my treat."
    mc "I want to make you feel special on a day like this."
    mc "So that it'll be something you remember forever."
    n 1bm "E-Eh...?"
    n "You can't just say that!"
    mc "Why not?"
    n 1bq "Y-You just..."
    n "Never mind."
    mc "So you're letting me pay for you?"
    n 1bs "No."
    "It was worth a shot."
    "I guess I can't force her not to pay."
    "She seems pretty insistent on paying for herself."
    "But still..."
    mc "Well, why don't we eat out here?"
    mc "It's a beautiful day out."
    mc "And I've got amazing company."
    "Natsuki's face turns a bright red."
    n 1bw "J-Just get the menu, you idiot."
    mc "Alright."
    mc "This will only take a second, Natsuki."
    "Another sound comes from Natsuki."
    n "Whatever..."
    show natsuki at thide
    hide natsuki
    "I head inside the store and go to the counter."
    "I tell the person there that we're eating outside."
    "I am given two menus and return to Natsuki."
    "I give her one of the menus to look at."
    show natsuki 1bc zorder 2 at t11
    n "What is this place anyway?"
    mc "You could say it's a specialized type of restaurant."
    n "Specialized type?"
    mc "Yeah, exactly."
    n 1bd "What do they specialize in...?"
    "Natsuki opens the menu."
    mc "Desserts."
    show natsuki 1bh
    "Natsuki's eyes widen as she looks through the menu."
    "It's probably the same reaction I had when I first went here."
    "When someone told me of a place that made purely desserts, I thought to myself that I had to check it out."
    "Not only that, but the food is pretty filling too despite being dessert."
    "The main problem for me is that it's so far away from where I live so it's incovenient for me to come here..."
    n 1bb "There's...so many choices."
    n "I've never seen such a big dessert menu before."
    n 2bc "I don't even know what to order."
    mc "I was going to order some of the cupcakes."
    mc "They also have this really nice tasting ice cream."
    mc "That said..."
    mc "Everything on the menu is good."
    n 2ba "Hmm..."
    "Natsuki looks through the menu once more."
    mc "Their savory desserts area really good."
    mc "If you're not looking for something sweet."
    n 2bb "No...I think I need something sweet right now."
    n "I just...don't know what to get."
    n 1bc "Maybe the crème brûlée?"
    n 1bg "No...maybe not."
    mc "The...what?"
    n 1bc "You know, the crème brûlée."
    "Natsuki shows me the item on the menu."
    mc "Oh, you mean the creme brulee?"
    n 1bb "No, it's pronounced {i}crème brûlée{/i}!"
    mc "I can't tell the difference."
    n 1bd "You need to pronounce it with the accents."
    n "See those little marks above the letters?"
    mc "Yeah...?"
    n 1bc "That determines how that letter is said."
    n "Sometimes accents can totally change the meaning of a word."
    mc "I see..."
    mc "I never really knew that."
    mc "I guess there's a lot more to even basic literature that I didn't know about."
    n 1bg "That's not it."
    n "What I just told you doesn't really have anything to do with literature."
    mc "It doesn't?"
    n 1bb "No, it's just a thing some words have."
    mc "Sort of like a translation?"
    n 1bc "A translation?"
    mc "Like that thing Monika said in the first week..."
    mc "That joke makes no sense in translation."
    n 2bh "...?"
    mc "Ah...I don't know."
    mc "It's just difficult for me to comprehend what you said."
    mc "To me, it's all the same."
    n 4ba "Well, there are worse things than not being able to say crème brûlée."
    mc "I guess so."
    n 4bd "It doesn't matter anyway."
    "Natsuki puts down her menu."
    n "What matters is that I'm spending time with you, [player]."
    n 4bq "So just keep that in mind, okay?"
    mc "You're right."
    mc "There are much more important things than creme brulee."
    show natsuki 3ba
    "Natsuki smiles."
    mc "So you've decided your order?"
    n 3bd "Yeah, it's number fifthteen on the menu."
    mc "Number fifthteen? That's all?"
    n "It seems like a pretty big dessert."
    mc "Well, alright..."
    mc "I'll make the order then."
    n 3ba "I'll be here."
    "I take the menu from her and return to the counter."
    show natsuki at thide
    hide natsuki
    mc "Hey, I'll have the cupcake special, ice cream wonder and number fifthteen."
    "The person behind the counter looks at me strangely when I say number fifthteen."
    "It's like I said something completely wrong."
    "But it's what Natsuki ordered, isn't it?"
    "What even is number fifthteen on the menu?"
    mc "How much is this going to cost?"
    "What Natsuki doesn't know is that this place makes you pay first."
    "So I'm paying for her, despite her protests."
    "I just want her to not worry about anything."
    "It's her special day after all."
    "The person behind the counter gives me the bill."
    "The cost is higher than I expected."
    mc "Did they increase the prices or something?"
    "The person simply shrugs at me."
    "It's not like I can't pay it."
    "And this is for Natsuki, so I really shouldn't be thinking that money is so important."
    "I pay for the food and return to Natsuki."
    show natsuki 1ba zorder 2 at t11
    mc "It'll be out in a couple of minutes."
    mc "I hope that's okay."
    n "Yeah...why wouldn't it be?"
    mc "You seem pretty hungry right now, so..."
    n 2bo "...!"
    n 2bp "I am not!"
    mc "If you say so..."
    "I look at Natsuki."
    "She looks as if she's too shy to start a conversation."
    "I guess it's up to me."
    mc "So that guy was pretty strange, right?"
    mc "The one in the store."
    n 2bk  "Yeah...not what I expected."
    mc "What did you expect?"
    n 2bs "I don't know...something normal, I guess?"
    mc "You wanted a normal date."
    mc "I guess that flew out the window as soon as we went into his shop."
    mc "Sorry about that."
    n 1bk "It's not your fault."
    n "These things are just bound to happen to me, aren't they?"
    mc "You think the world has something against you?"
    mc "I don't believe that."
    n 1bi "I don't want to believe that but with all the things that have happened to me throughout my life..."
    n "What other explanation is there?"
    mc "Things happen to everyone, Natsuki."
    mc "Some good, some bad."
    mc "Not to make light of your situation but there are probably people worse off than you or me."
    mc "How would you explain their situation?"
    n 1bq "...I don't know."
    mc "Yeah, me neither."
    mc "I just know that I should be thankful for the things I have..."
    mc "And the people I've met because I'm really fortunate."
    n 1bs "You think so?"
    mc "Well...I met you, didn't I?"
    n 1bo "That's not fair."
    mc "What isn't?"
    n "You're using way too much flair!"
    mc "Ahaha, sorry."
    mc "But I am really glad I met you, Natsuki."
    mc "I don't know any better way of spending my time right now..."
    mc "Than with you..."
    n 1bq "...Y-You're doing it again."
    mc "Do you want me to stop?"
    n 1bi "D-Do what you want."
    mc "Okay."
    "There's a brief moment of just silence between us."
    "She stares out into the distance, not knowing what to say."
    mc "What do you think the clerk's deal was?"
    n 1bh "What do you mean?"
    mc "He was pretty crazy and all over the place."
    mc "I don't think he was in the right state of mind."
    n 1be "He's probably an alcoholic or something."
    mc "What makes you think that?"
    n 1bc "I don't know, just the feeling I get from him."
    n "It's similar to how my dad was before he changed."
    mc "I see..."
    n 1bh "I still trust him with the portrait though."
    n "I'm pretty good at sensing when someone is telling lies."
    mc "You are?"
    n 1bw "Yeah, I am."
    "I paid for her food when we sort of agreed to split the bill."
    "She hasn't sensed that."
    n "I know some things you think I don't."
    n 4by "Like how you paid for my food even though I said I was gonna pay for myself."
    mc "Huh? How did you figure that out...?"
    n 4bi "It said on the menu you had to pay before getting your food."
    mc "Oh..."
    n 4bg "That's really nice of you, [player]."
    n "But I don't need you to do that for me."
    n 2bg "So here."
    "Natsuki pulls out some money from her wallet and offers it to me."
    mc "I can't take this, Natsuki."
    mc "I don't want to."
    n 2bb "I can't depend on you for everything, [player]."
    mc "I know."
    mc "But I want you to."
    n 2bf "W-What...?"
    mc "It might be a bit early for me to say this..."
    mc "But I want you to be able to depend on me, Natsuki."
    mc "I don't want you to go through the pain of feeling like you're alone again."
    if ch12_outcome == 3:
        mc "I know your parents are back..."
    else:
        mc "I know your dad is back..."
    mc "I still want to be there for you."
    n 2br "[player]..."
    mc "You've had a bitter past, Natsuki."
    mc "And for what it's worth, I'm sorry you had to experience it."
    mc "But I want you to have a sweet future."
    mc "The two of us."
    n 2bs "..."
    "Natsuki stays silent."
    "Did I say something wrong?"
    "Just as I'm about to say something she smiles slightly."
    n 2bq "You're a big dummy, you know that?"
    n "How do you expect me to respond to that?"
    "Natsuki looks down at the table, avoiding my eyes."
    n 2bm "I...really like you, [player]."
    n "I'm sure you knew that already."
    n 2bi "Just being with you now, it makes my heart beat so fast."
    n "I know I'm not the best at showing my feelings but..."
    n 2bh "I'm glad you're here, with me."
    n 2bs "A-Anyway..."
    n "Let's change the topic, okay?"
    n "It's getting weird and people might hear what we're talking about."
    mc "Yeah, you're right."
    mc "Got anything on your mind then?"
    n 1bk "The clerk said something about a Naomik, right?"
    n "Who do you think he meant?"
    mc "I have no idea, honestly."
    n "Well, why would he tell you about this person then?"
    n "You have to know something."
    mc "I've never met that person before, Natsuki."
    mc "I thought we both agreed he was just crazy and told me for no reason."
    n 1bc "I guess so..."
    n "It's still kinda interesting to talk about though."
    n "And it's been stuck in my head ever since you told me."
    mc "It has?"
    n 1bb "Yeah, just something about Naomik seems so familiar."
    mc "Doesn't seem familiar to me."
    n "Hmm...how do you think it's spelt?"
    mc "If I had to guess..."
    "I take out a pen from my pocket and write it down the spelling on a tissue."
    "I give the tissue to Natsuki."
    n 2bj "Maybe if we rearrange the letters."
    mc "That's a really random idea."
    n 2bi "Do you have a better idea?"
    mc "Well...no."
    n 2be "Give me that pen."
    "I give the pen to Natsuki."
    "She begins writing down different combinations of Naomik."
    show natsuki 2ba
    mc "I don't even know if that's how to spell it though."
    mc "You could be doing that for nothing."
    "I see some of the things she's written."
    "There's Kinamo and Amikon as well as some other combinations."
    "This goes on for a few minutes as she changes the starting letter each time."
    n 2bc "How about Mokain?"
    mc "Doesn't sound like a name to me."
    mc "What happens if we even find out the real name?"
    mc "It's not going to do anything for us."
    n 2bb "Maybe you'll remember or something..."
    n 2bc "Let's see..."
    "Natsuki writes down another combination of the letters."
    n 2bk "Mokina?"
    mc "I don't think so."
    n 1bf "Ugh, we're so close!"
    n "I can feel it."
    "She writes down another combination."
    n 1be "Maybe Moni--"
    "Suddenly, a waiter brings our desserts to us."
    "The waiter places down some sort of pie in front of Natsuki and cupcakes and ice cream in front of me."
    "The waiter looks at Natsuki's tissue and offers her a new one before taking the one with scribbles on it."
    n 1bm "W-Wait..."
    "She says that too quietly for the waiter to hear."
    n "All that work..."
    mc "It doesn't matter, Natsuki."
    mc "It was just for fun anyway, right?"
    show natsuki 1bs
    "Natsuki pouts."
    n "To you, maybe."
    mc "You're cute when you're like that, you know."
    n 1bo "...!"
    n "W-Whatever!"
    "Natsuki takes a fork and takes a slice of the thing in front of her."
    "She puts it into her mouth and starts chewing."
    show natsuki 1bk
    "The expression on her face says it all."
    "She loves it."
    n "[player], this is..."
    n 1bd "Incredible!"
    n "The flavors, they're...!"
    n "I can't even begin to describe it."
    mc "It's pretty good, isn't it?"
    "I take one of the cupcakes and bite down on it."
    "The explosion of flavor in my mouth is unlike anything I know."
    "I should really go to this place more often."
    n 2bd "I almost want to try to recreate the flavor coming from this."
    n "It's just unbelievably good!"
    n "Why have I never heard of this place until now?"
    mc "It's pretty hidden."
    mc "I'm pretty lucky to have found it myself."
    n 2ba "You don't say..."
    "Natsuki takes another piece of her dessert."
    mc "What is that anyway?"
    mc "It looks pretty good."
    n 2bc "It's number fifthteen, like I said."
    mc "But what is number fifthteen?"
    mc "You're just saying a number."
    n 2bk "That's what it's called."
    n "You should know more than me."
    "I take a bite from another cupcake."
    mc "You should really try this."
    mc "Maybe you'll get some inspiration from it."
    "I offer a cupcake to Natsuki."
    n 1bc "No, thanks."
    mc "Eh?"
    mc "I thought you would have wanted one."
    n 1bq "I don't want it to affect the way I make mine."
    n "I know it's going to taste amazing."
    n "And I know I'll never be able to replicate it."
    n 1bs "It'll just make me feel like my cupcakes aren't enough."
    n "So I'm not going to eat any."
    mc "..."
    mc "I guess that makes sense."
    "Natsuki takes another bite, seemingly upset."
    mc "I have to say..."
    n "...?"
    mc "Your cupcakes are still better though."
    n 1bo "W-What?"
    mc "The cupcakes you brought in for me on the first day."
    mc "It beats these cupcakes anyday."
    "I put down the third and final cupcake I have."
    n 1bq "You're just saying that."
    mc "Am I?"
    n 1bs "Yeah, you are."
    n "I don't need your pity, [player]."
    mc "You said you're good at telling lies, right?"
    mc "So..."
    "I grab Natsuki's hand."
    mc "Tell me, am I lying?"
    show natsuki 1bn
    "She looks at my face."
    n 1bm "...No."
    mc "Your cupcakes will always be the best to me, Natsuki."
    mc "Because they're made by you."
    mc "That's all there is to it."
    n 1bq "This is going to go on, isn't it?"
    mc "What is?"
    n "You talking like that."
    mc "I guess it is."
    n "..."
    n 1bt "I can live with that."
    "Natsuki smiles."
    n 1bd "We should probably finish our food."
    n "It's been a while since we dropped off the portrait."
    mc "Yeah, you're right."
    "I take the ice cream and start eating it."
    "It's nothing too special, it tastes like normal chocolate ice cream."
    "What's special about it is the actual cone."
    "The cone is made from some kind of dark chocolate but still has that familiar waffle cone taste."
    "It's basically just a really sweet ice cream."
    "Meanwhile, Natsuki finished off her number fifthteen."
    "Whatever that is exactly..."
    mc "I guess that's it."
    mc "Shall we head back?"
    "Natsuki stands up."
    n 1ba "Let's."
    scene bg city_sunset with wipeleft_scene
    "Natsuki and I walk around the city back to the store."
    "The walk feels longer than from when we walked to that place we ate at."
    "Even though we took a bunch of detours with the bakeries, it just feels like the walk back is taking an unusually long time."
    "I'm probably just overthinking it."
    "Besides, there's nothing wrong with that."
    "It just means I can spend more time with Natsuki."
    "That said, the walk back is fairly quiet."
    "I guess we're both thinking about what's waiting for us when we get back to the store."
    n "It's a beautiful sunset, isn't it?"
    show natsuki 1bs zorder 2 at t11
    mc "What? Oh, yeah..."
    mc "Too bad we couldn't see for ourselves where the sun is setting."
    n 1bt "Maybe on another day..."
    mc "Yeah..."
    n 1bl "Anyway, the store is just around here, right?"
    mc "I think so."
    n 1bk "Well..."
    n "I suppose we shouldn't keep him waiting."
    show natsuki at thide
    hide natsuki
    "Natsuki walks on ahead."
    "I take one more look at the sun before following her."
    scene bg portraitshop_sunset with wipeleft_scene
    "We both walk in the store, despite the sign saying closed."
    "He's expecting us after all."
    "Though I'm not sure if he's finished with the portrait yet."
    "It has been a couple of hours since we left but with the state the portrait was in..."
    "I guess I have doubts that the clerk actually finished his work."
    show natsuki 2bh zorder 2 at t21
    n "Hello?"
    n "We're back..."
    n "Have you--"
    show mysteriousclerk 4b zorder 3 at hf22
    cl "Hello, hello!"
    "Natsuki jumps backwards as the clerk suddenly appears seemingly out of nowhere."
    show natsuki 2bo zorder 2 at hf21
    show mysteriousclerk zorder 2 at t22
    n "Ah! Don't just--"
    show natsuki zorder 2 at t21
    show mysteriousclerk 4e zorder 3 at f22
    cl "You've come just in time!"
    cl "I have your portrait right here."
    cl 5c "It's finished, of course."
    "The clerk pulls out a large canvas from under a desk and reveals it to us."
    "It's..."
    # I'd have a CG of the portrait here but yeet
    "A perfect recreation of the portrait."
    "At least, from what I can tell."
    "It's wrapped in some sort of plastic."
    "I assume that's there to protect it."
    "All the details from what I can see are there."
    "All the markings that were gone have been erased."
    "It looks almost brand new."
    cl 5a "What do you think?"
    cl "Pretty good, right?"
    show natsuki 2bm zorder 3 at f21
    show mysteriousclerk zorder 2 at t22
    n "It's..."
    n 2bk "...Wow."
    show natsuki zorder 2 at t21
    show mysteriousclerk 5e zorder 3 at f22
    cl "Impressed, young lady?"
    cl "You should be!"
    cl 5h "My services don't come cheap, you know!"
    cl "They cost, uh..."
    "The clerk starts counting with his fingers seemingly at random."
    cl 5b "One...two...nine million a piece."
    cl "Give or take my mood on the day."
    cl "Good thing your friend took care of a little alternate payment."
    show mysteriousclerk zorder 2 at t22
    mc "Alternate payment...?"
    mc "Wait..."
    mc "You can charge based on mood?"
    mc "Is that even legal?"
    show mysteriousclerk 1i zorder 3 at f22
    cl "My boy!"
    cl "In this world of infinite choices, everything is legal!"
    cl 1f "For example!"
    cl "I could hold you at gunpoint and no one could stop me!"
    show mysteriousclerk zorder 2 at t22
    mc "What?!"
    show mysteriousclerk 1e zorder 3 at f22
    cl "I'm only kidding, of course!"
    cl "I'm not {i}that{/i} crazy."
    cl 1k "The closest thing I've ever gotten to crime was keeping two young kids hostage in my shop."
    "Natsuki and I look at each other."
    cl 1e "Kidding!"
    cl "You two really need to lighten up, you know."
    cl 1b "You kids are the future, after all."
    cl "Literally!"
    show natsuki 2bh zorder 3 at f21
    show mysteriousclerk zorder 2 at t22
    n "Right..."
    n 2bq "Listen, um..."
    n "Mister...Clerk."
    show natsuki zorder 2 at t21
    show mysteriousclerk 2f zorder 3 at f22
    cl "Please, my friends call me Clark."
    cl 2e "But that's not actually my name!"
    cl 2a "Nor are you my friend."
    cl "With that said, you may see yourself out."
    show natsuki 4bk zorder 3 at f21
    show mysteriousclerk zorder 2 at t22
    n "That's it?"
    show natsuki zorder 2 at t21
    show mysteriousclerk 2b zorder 3 at f22
    cl "That's it, now go."
    cl "I am a very busy man."
    "The clerk grabs a magnifying glass and starts looking at us through it."
    cl 2d "Our business here is done, after all."
    cl "Go."
    "He waits for a few seconds and notices we don't start moving."
    cl 1g "Go!"
    show mysteriousclerk zorder 2 at t22
    mc "Wait, we still have some questions...!"
    show mysteriousclerk 1e zorder 3 at f22
    cl "Ever hear the phrase \"curiosity killed the mailman\" before?"
    cl 1i "Wait...that's not--"
    cl 1j "The point is...!"
    cl 1c "You're better off not asking questions."
    cl 1d "At least, not yet."
    cl "It isn't time."
    cl 1b "You understand, right..."
    cl "...[player]?"
    show mysteriousclerk zorder 2 at t22
    mc "What?"
    show natsuki zorder 3 at f21
    n "Let's go, [player]."
    n "We're done here."
    n "And it's getting pretty late, too."
    show natsuki zorder 2 at t21
    show mysteriousclerk 1e zorder 3 at f22
    cl "You should listen to the young lady."
    cl 4e "Women know best, after all."
    "The clerk chuckles to himself."
    cl 4k "Now leave."
    show natsuki 2be zorder 3 at f21
    show mysteriousclerk zorder 2 at t22
    n "We're leaving!"
    "Natsuki signals for me to get the portrait."
    "I oblige and take the bag that I left here and put the portrait inside."
    n 1bb "We'll be going now."
    "But the clerk is already doing his own thing and ignores Natsuki."
    n 1bc "Okay..."
    n "Let's get this home, [player]."
    n 1bg "The train is arriving soon, I think."
    show natsuki zorder 2 at t21
    show mysteriousclerk 4c zorder 3 at f22
    cl "The next one is in fifthteen minutes."
    cl "Better move quickly, otherwise you have to wait an hour for the next one."
    show mysteriousclerk at thide
    hide mysteriousclerk
    show natsuki zorder 2 at t11
    "The clerk goes to what I can only guess is a storeroom after saying that."
    n 1bc "Guess we better move then."
    call screen dialog(message="To be continued!\nThanks for playing, keep an eye out on reddit and discord for updates!", ok_action=Quit(confirm=False))
    return
