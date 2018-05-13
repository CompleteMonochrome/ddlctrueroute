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
    s "Your poem doensn't really matter anymore."
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
        s 1l "I got a bit too philosphical there, didn't I?"
        s 1d "I just hope Natsuki does end up happy, in the end."
    else:
        s 1c "So...this is an interesting end for Natsuki."
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
    s "So really, if you want to do that then you'll have have to help me."
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
        m "I don't really know what kind of songs I could play on the day."
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
        m "He could also help with choosing the songs I could play."
        m "Ahaha, it could be fun."
        m 3he "However, I'm not going to force you."
        m "You should go because you think I need the help not because you want to hang out with me..."
        m 1hj "But I certainly wouldn't mind if that was the reason~"
    else:
        show monika 3a zorder 3 at f33
        m "[player] could be useful helping me."
        m "There might be some songs he wants to hear on the day that I could play for him."
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
    "I know with the two of us working together, we can do something really great for the festival."
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
                m 1ha "We should should probably get going."
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
    call screen dialog(message="To be continued!\nThanks for playing, keep an eye out on reddit and discord for updates!", ok_action=Quit(confirm=False))
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
    "The walk to her house is quite long but after going there twice I think I know exactly how to get there."
    scene bg n_house
    with wipeleft_scene
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
    show yuri 3pa zorder 2 at t11
    y "Is something wrong, [player]?"
    y "You look deep in thought."
    mc "O-Oh, it's nothing."
    mc "Just some random thoughts I'm having."
    mc "You probably don't need to worry about it."
    y "You know you can tell me whatever is on your mind."
    mc "It's better if you don't worry about it."
    mc "We're almost at my house anyway."
    y "Y-Yeah..."
    y "Just take this turn and--"
    y "I mean, it's around here, isn't it?"
    mc "Yeah...it is."
    mc "You sure know your way around here, don't you Yuri?"
    y "Ah..."
    mc "I think that's a pretty good skill to have."
    y "Huh?"
    mc "A sense of direction."
    y "R-Right...!"
    y "A-Anyway, we should get going."
    mc "My thoughts exactly."
    scene bg house
    with wipeleft_scene
    "We arrive at my house."
    "Yuri seems kinda worried for some reason."
    mc "Is everything okay?"
    show yuri 2pa zorder 2 at t11
    if visited_yuri_hospital:
        y "I just feel a little strange being here."
        y "Like it's wrong, somehow."
        mc "What do you mean?"
        mc "What's wrong with me helping you?"
    else:
        y "I...don't know what it is."
        y "It just feel strange being here."
        y "Like there's something wrong, somehow."
        mc "Eh? What do you mean?"
        mc "Is there something wrong with me helping you?"
    y "There's nothing 'wrong' about that."
    y "It's just this feeling that I can't shake."
    if ch4_name == "Yuri":
        y "That this has all happened before and that it led to something terrible."
    else:
        y "Like this could have happened before and lead to something terrible."
    mc "Yuri, I honestly have no idea what you're talking about."
    mc "Though I do feel kinda strange."
    if visited_yuri_hospital:
        mc "But it's no big deal."
        y "You can say it, [player]."
    else:
        y "W-What is it?"
    mc "Well..."
    y "[player], just tell me."
    mc "Alright...it might have just been my imagination but the club meeting we had to today..."
    y "What about it?"
    mc "Didn't it feel familiar to you?"
    mc "There was a stage in the meeting that seemed like an exact copy of what happened before."
    mc "In the first week of me as a member."
    mc "Do you remember?"
    y "Umm..."
    y "I don't..."
    y "Why...?"
    "Yuri puts a hand on her head."
    y "[player], what's going on...?"
    mc "Y-Yuri, are you okay?"
    y "I don't know."
    y "I'm trying to remember the time you're speaking of."
    y "It's not working."
    mc "Maybe we should head inside."
    y "That sounds like a good idea."
    scene bg bedroom
    show yuri 3pa zorder 2 at t11
    with wipeleft_scene
    mc "How's your head, Yuri?"
    y "I can't think properly..."
    y "I'm trying my hardest to remember but I...can't."
    mc "It doesn't matter anymore, Yuri."
    mc "Just forget about it, maybe your head will get better."
    y "That's the thing [player]!"
    y "It's like I've just forgotten what happened."
    mc "E-Eh...?"
    y "I don't know if my mind is playing tricks on me or what..."
    y "And honestly, that's a very scary thought."
    mc "How come?"
    y "Think about it."
    y "If you can't even rely on your own mind, then what are you?"
    y "You're just a husk of yourself, a slave to--"
    mc "Yuri, I think you're overthinking this a little bit."
    mc "Maybe I am as well."
    mc "If making you think about the first week makes you uncomfortable, then we can just avoid that topic altogether."
    mc "Besides, we aren't really here to talk about what happened in the first week."
    mc "We're here to discuss your preparations and choose a book, right?"
    y "Y-Yeah, you're right."
    "Yuri's frown slowly disappears."
    y "But before we do that, I need to ask {i}you{/i} something, [player]."
    mc "Huh? What is it?"
    if monika_type == 0 or monika_type == 1:
        y "Do you think Sayori has been acting a little different lately?"
        mc "Sayori acting strange...?"
        mc "What do you mean?"
        y "What you said earlier, about the events that happened in the first week..."
        y "It's placed a theory in my head about my memories."
        mc "Yuri, didn't we just--"
        y "[player], just answer the question."
        y "I want to settle this."
        mc "Ah..."
        "I think of Sayori and how she acts."
        "I've always known her to be a carefree person who really didn't care about life."
        "I just didn't think that she would be depressed because of that..."
        "I really was some kind of jerk back then for not realizing."
        "Anyway, back to what Yuri asked me..."
        "Lately, Sayori has been more serious."
        "I don't know if that's because she's talking her responsibility as the president of the club more seriously or..."
        "Hold on a second..."
        y "You look like you're concentrating."
        mc "I am..."
        mc "Something isn't right."
        y "So there is something weird going on with Sayori?"
        mc "I don't know..."
        mc "But to answer your first question, yes."
        mc "She has been acting differently."
        mc "I don't think that has--"
        y "So I was right."
        mc "Yuri, what's your theory?"
        y "I'm not sure but with your confirmation that Sayori has been acting differently..."
        y "I think that has something to do with why my memory is all over the place."
        mc "I don't think those two have any correlation at all."
        mc "It just doesn't make any sense."
        y "I'm likely grasping at straws here."
        y "I just thought I'd tell you what's on my mind."
        mc "I appreciate it...I guess."
        y "If anything comes from it, I'll let you know."
        "What in the world is Yuri talking about?"
        "It's good she's being open with me but what she's talking about just makes no sense."
        "Maybe I should focus on doing the preparations."
    else:
        y "Do you think that Monika has been acting kinda strange lately?"
        mc "Strange? In what way?"
        y "Surely you've noticed, right?"
        y "She's been more hostile and started being more cold...?"
        mc "I can't say I've noticed that."
        mc "To me, she's just the same Monika I met on the first day of being in the Literature Club."
        y "W-What...?"
        y "[player], you can't be serious."
        mc "I am fully serious, Yuri."
        y "I don't..."
        y "I refuse to believe that."
        y "Sure she may still look the same but you haven't noticed any behavioral differences in her?"
        mc "Yuri, I suggest you leave this topic alone."
        y "What did you say?"
        mc "I said you should leave this topic alone."
        mc "It's for our own good."
        y "Our own good?"
        y "[player], what are you saying?"
        mc "Nothing is wrong, Yuri."
        mc "We should just discuss something else."
        if visited_yuri_hospital:
            mc "How about talking about the preparations we were going to--"
            y "[player], there's something incredibly wrong with you."
            y "I don't know what it is but since we're together, I can't just ignore it."
            mc "I have no idea what you're talking about, Yuri."
            y "Stop acting like there's nothing wrong."
            y "There's something clearly messed up in all of this."
            y "Come to your senses, please!"
            "Yuri starts shaking me."
            y "You remember that day at the mall, right?"
            y "When we dropped that knife in the water together?"
            mc "..."
            y "I said I was going to become a better person afterwards."
            y "I can't do that without you, [player]."
            y "I need the real you."
            mc "I don't understand."
            y "W-What?"
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
            show yuri 3pb at face
            with open_eyes
            y "You're awake!"
            show yuri 3pa zorder 2 at t11
            y "I was worried..."
            mc "W-What happened?"
            mc "I can't remember anything since we got into the house."
            y "You don't?"
            y "Then..."
            "Yuri looks at me worriedly."
            y "That's probably for the best."
        else:
            mc "How about talking about the preparations we were going to do?"
            y "I..."
            "Yuri looks pensive."
            y "Okay..."
            y "That's what we came here to do after all."
            y "So it's for the best..."
        "Was Yuri talking about something...?"
        "I can't recall even though it was just a couple of moments ago..."
        "I get the feeling that I shouldn't think about it."
    mc "Anyway, let's get back to what we came here to do in the first place."
    y "Yeah..."
    "Yuri looks around my room."
    y "Is this all the books you have in your house?"
    y "Just the ones on that shelf over there?"
    mc "Well..."
    "There are lots of books on the shelf that I haven't really looked at before."
    "Most of those books are some novels that were gifted to me in the past for special occasions."
    "I never really got around to reading them."
    "The other type of book on there is manga, which I don't think Yuri would be particularly interested in."
    "Though anything seems to be possble these days."
    "What's on the bookshelf is not a very big collection..."
    mc "On second thought, maybe we should have gone to your house."
    mc "Or maybe the library..."
    y "I-It's fine, [player]."
    y "I actually thought something like this would happen."
    mc "Something like what?"
    y "I know this sounds like something out of a film but..."
    y "I always carry lots of different novels with me to school."
    y "It kinda depends on my mood as to what I bring."
    y "But this time around I brought five different novels."
    mc "Novels?"
    y "I-Is that a problem...?"
    mc "No, not at all!"
    mc "It just sounds too convenient for the occasion."
    y "Like I said...it sounds like something from a film."
    y "But that's why I didn't mind going to your house for this."
    y "If you want, you can select from my books as well."
    y "I'm sure Sayori wouldn't really mind if we only bring two or three books each."
    mc "You're probably right."
    mc "I might as well take a look at your books then."
    y "Go ahead..."
    y "I have other books at home, if you don't like any of these choices."
    mc "I'm sure I can make something work with what we have here."
    "I look through the books Yuri brought with her."
    "They all have one thing in common just judging from the cover..."
    "They're all horror books."
    "Even the name of the books give me an eerie feeling."
    "I guess I shouldn't have expected anything less from Yuri."
    mc "These are..."
    y "They're terrible, aren't they?"
    y "I'm sorry..."
    mc "No! I never said that."
    mc "I haven't even read them so I can't judge them properly."
    mc "I was just going to say they're horror books, aren't they?"
    y "Y-Yeah...you know that's the type of thing I like to read, right?"
    mc "I guess so."
    mc "I was just curious."
    mc "Have you read any of them?"
    y "Actually, I've read all of them."
    mc "Eh? So why did you bring them to school...?"
    y "Sometimes, I like to reflect on the past."
    mc "Not this again..."
    y "N-No, it's not like that...!"
    y "I just meant these books are really good."
    y "So I like rereading them from time to time."
    y "In fact, I'm surprised you haven't heard of these novels."
    mc "Why not...?"
    y "Well...they're among the most popular horror books."
    y "I even selected them partly because of that."
    mc "You selected them...? For what reason?"
    if visited_yuri_hospital:
        y "I thought I could introduce you to more horror books."
        y "Since we're spending so much time together and I spend a lot of my own time reading..."
        y "Maybe we could read horror books together...?"
        y "It's just...."
        y "I just want us to have more to talk about, seeing as we're together."
        mc "I understand your reasons."
        mc "I think it's really nice of you, Yuri."
        mc "I enjoy spending time with you so the more things I can do with you, the better."
        y "T-Thank you, [player]."
        y "I wasn't sure how you would take it..."
        y "Maybe when we're deeper in our relationship I can introduce you to books that are more suited to who I really am."
        mc "Who you really are? What do you mean?"
        mc "Aren't these types of books the type to represent who you really are?"
        y "Ah...like I said before..."
        y "I only chose the most popular horror books because I wanted to ease you into it."
        mc "I see..."
        mc "What about that first book you gave me...?"
        y "First book?"
        mc "Yeah, during the first week you gave me a book."
        mc "Wasn't that a horror book as well?"
        y "I don't like to think about back then..."
        y "I gave you the book and look what happened..."
        y "All you did was spend time with Monika."
        mc "It wasn't because of the book, Yuri."
        y "I like to think it was...maybe I was coming on too strong or--"
        mc "You're overthinking it, Yuri."
        mc "There's some reason I chose to spend time with Monika, even if I don't fully understand it yet."
        y "What? You think there's a reason you had to spend time with Monika?"
        mc "I don't know..."
        y "It's just..."
        "Yuri stops and looks at my face."
        "I don't know if it's showing but I'm getting uncomfortable for some reason."
        "I'm interested in the topic but it's almost like I shouldn't talk about it."
        y "I-I'll stop..."
        y "You clearly look flustered and the last thing I want to do is make you uncomfortable."
        y "Let's just go back to selecting some books for the day."
    else:
        y "Ah...I thought that maybe..."
        y "I could get...the people in the Literature Club interested in horror books."
        y "So you and I could have more to talk about."
        y "I mean--"
        y "So that everyone else could talk to me about something if they met me outside the club."
        mc "I see."
        mc "I'm not sure everyone feels the same about horror books."
        y "Oh..."
        "Yuri frowns."
        mc "As for me, I don't really know what to think about them."
        mc "I don't remember the last horror book I read..."
        y "I just thought that selecting these horror books, due to their popularity..."
        y "I could slowly get people to start reading the type of genre I like."
        mc "Are they particularly scary to read?"
        mc "People might not like what you've got to offer because they might not be able to mentally cope with what's happening."
        y "I...didn't really think about it like that."
        y "I just really wanted--"
        "Yuri looks away and sighs."
        y "Why did you choose to spend your time now with me, [player]?"
        y "And give me the real reason, please."
        mc "I really thought you needed the most help, Yuri."
        mc "That's the real reason, I promise."
        y "..."
        y "It's not the answer I'm looking for..."
        y "But I suppose it just confirms everything."
        mc "What do you mean?"
        y "There's no point talking about it anymore."
        y "Let's just go back to selecting some books for the day."
    mc "Okay, Yuri."
    mc "Let's have a look at all the books we have here then."
    "I start taking books from the shelf and placing them on my bed."
    y "Are you sure that's a good idea?"
    y "You're going to have a lot of work to do putting them all back."
    mc "It's not a problem...not like they were organized to begin with."
    y "Ah..."
    y "You should really organize your bookshelf, [player]."
    mc "I think it's fine the way it is."
    mc "I rarely take stuff out of it anyway."
    "I finish placing the last of the books from my shelf on the bed."
    "Yuri puts her five books on my bed in a seperate area."
    "Presumeably to help distinguish which ones are hers and mine."
    y "Even with all your books..."
    y "It looks like there's only about thirty or so books."
    mc "Yeah...the collection is rather small."
    mc "I'm not really the type to collect books."
    y "You have several volumes of manga though..."
    mc "That's about the only thing I actually collect."
    y "Alright..."
    y "You're probably going to choose one of the manga you laid out, right?"
    mc "Well...not only that."
    y "It's fine."
    y "After all, we'll still be voting for the book we're going to do."
    y "It doesn't mean what you choose will be what the Literature Club agrees on, right?"
    mc "Yeah, you're right."
    y "So choose whatever you want."
    y "I'll go after you."
    mc "Are you sure you want to give me the choice of your novels?"
    y "If you choose one of my novels, I'll be voting for it anyway."
    y "So the choice here doesn't really matter."
    mc "I suppose..."
    "Yuri brought these books here, almost because of this exact circumstance."
    "It would feel wrong not to take one of hers at the very least."
    menu:
        "But..."
        "Take one of Yuri's books.":
            $ ch13_yuri_books = True
            $ yuri_approval += 1
            "I decide to take one of Yuri's books."
            "The one I chose looks the most tame out of all of them."
            "I also take three of my own books, two of which are mangas."
            "The third one was a popular book series that someone gifted me that I never got around to reading."
        "Select from your books only.":
            $ ch13_yuri_books = False
            "I don't really feel comfortable choosing Yuri's books."
            "I definitely appreciate her bringing them but it feels weird taking something I have no particular interest in."
            "I decide to select three volumes of manga from different series and a novel from a popular book series."
            "I never actually got around to reading all of it, but I think choosing something that appeals to a general crowd could be good."
            "It also feels wrong selecting four different manga while Yuri is here for some reason."
    y "So those are your choices?"
    y "In that case..."
    "Yuri selects the books that she brought."
    y "I'll just take these ones."
    mc "I kinda expected that."
    y "It's not like you have bad taste or anything..."
    y "It's just..."
    mc "I know, you don't really read these types of things."
    mc "I won't judge you for it."
    if ch13_yuri_books:
        y "I'm surprised you took one of my books."
        y "I honestly was expecting you to just go four four volumes of manga."
    else:
        y "I'm surprised you took out a novel from your pile of books."
    mc "Well, I want to have something other than manga."
    y "I don't see why but..."
    y "I think we should discuss the decorations we're going to be doing on the day."
    mc "Yeah, I think you're right."
    y "So..."
    y "What kind of atmosphere do you think we should have?"
    mc "I mean, that kinda depends on the book we choose doesn't it?"
    y "Ah...you're right."
    y "Those words just slipped from my mouth."
    mc "Well, we could always make a list of the stuff we could potentially use."
    mc "That way, when we vote tomorrow we don't need to think of one when we go shopping for them."
    y "You're right, that's a great idea."
    y "Where to start...?"
    mc "How about some scented candles?"
    return

label ch13_exclusive_monika:
    scene bg residential_day
    with wipeleft_scene
    play music t6 fadeout 1.0
    "We decided to go to Monika's house for the preparations."
    "It only makes sense since she's going to be playing the piano."
    "It's not like I have any equipment at home to help her with that."
    "The walk to Monika's house from the school took a lot longer than I thought it would."
    "Since she said it was around the same distance from my house to the school, I was expecting to get there quickly."
    "The actual distance might be the same but the amount of turns makes it almost seem doubled."
    if monika_type == 0:
        show monika 1a zorder 2 at t11
        m "Sorry for making you go all this way just to help me, [player]."
        m "To be honest, we could have gone to your house but..."
        m "I wanted to get some practice in for the song I'm going to play."
        m "I hope you don't mind too much!"
        mc "Ah, no that's fine."
        mc "After all, I'm the one helping you."
        mc "It would make sense that we would go to {i}your{/i} house after all."
        m "Ahaha, if you say so."
        "Monika smiles meaningfully."
        m "Anyway, my house is just around here..."
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
        m "Well, I wasn't lying about the distance to my house."
        m "Ahaha, though I may have omitted how far we would actually have to travel."
        m "I hope it's not too much of a problem."
        mc "Not at all..."
        m "We could have done this at your house but..."
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
        m "Come on, we have to be the ones who stand out."
        mc "Right..."
        m "You did choose to help me after all."
        m "I know the walk is a long way..."
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
    "It's just not somewhere I thought Monika would be living in given her...popularity."
    if monika_type == 0:
        m "Ahaha, welcome to my humble abode~"
        "Monika looks at me quizzically."
        m "You look kinda confused there, [player]."
        m "Is something wrong?"
        mc "N-Nothing."
        mc "It was just a random thought."
        m "Well, you can share it with me."
        mc "It's about your house."
        m "Ah..."
        "Monika turns back and looks at her house."
        m "It isn't quite what you expected, is it?"
        m "You probably thought someone like me would live in a mansion?"
        m "Because of my popularity, right?"
        mc "I'm sorry."
        mc "I didn't meant to imply anything--"
        m "No, it's okay."
        m "It's just..."
        m "Well, nobody really knows the {i}real{/i} me."
        mc "Monika..."
        m "Not even {i}you{/i}."
        m "All I've been showing you is..."
        m "Well, we should head inside first."
        mc "...Okay..."
        show monika at thide
        hide monika
        "That was a pretty sudden mood shift from Monika."
        "Did I say something to cause that?"
        "I hope not, otherwise working together is going to be incredibly awkward."
        scene bg m_livingroom with wipeleft_scene
        "Her living room isn't big but it's actually a lot more spacious than it looks."
        "There's bits and pieces lying everywhere and a keyboard in front of the TV."
        "Honestly, I thought the place would be cleaner."
        "I thought Monika would have prepared in case something like this happened."
        "I suppose it's not really a big deal."
        show monika 1a zorder 2 at t11
        m "It's not a clean place, I know."
        m "I've been working super hard the last week and I wasn't exactly expecting you to come over today."
        m "Sorry, [player]."
        mc "It's no big deal, Monika."
        mc "I also think you misunderstood me outside."
        mc "I really don't dislike your house, I was just making an observation."
        m 1c "Well...if you say so."
        m "Sigh..."
        m "I'm sorry if I took it the wrong way."
        m "I've just been under a lot of pressure lately."
        m "You know, with all that's been happening."
        m "I guess hearing anything negative outside of the Literature Club just tipped me over the edge."
        mc "I didn't know you were affected that much."
        mc "I certainly didn't mean to hurt you, Monika."
        m "I know..."
        "I notice a keyboard in the middle of the room."
        "There seems to be some neatly made sheet music on it."
        "Is this what she's been practicing this whole time?"
        m "Yeah...this is my keyboard."
        m "It's what I use to practice the piano, since a real piano is way too expensive."
        mc "I understand."
        mc "What's the sheet music you've got on it?"
        m "It's actually something I've made myself."
        m "I've been practicing it quite a bit but no one has been around to listen to it."
        mc "You've made your own song already? That's really impressive."
        m "Ahaha, thanks [player]~"
        m "But don't praise me too much!"
        m "The song is actually rather easy to play...and that's coming from a beginner!"
        m "I almost feel bad playing it for the day, when I could do so much better."
        mc "So why don't you play a different song then?"
        m "I could."
        m "But I need you to hear this song, at least once."
        m "So this will be the song I play on the day."
        mc "I assume you're going to learn some shorter songs to accompany it?"
        mc "This song is probably the centrepiece, right?"
        m "That was the idea I had in my hand."
        m "But I don't really know if it'll work."
        mc "Well, I think it's a great idea."
        mc "Maybe I could help you search for smaller songs that are easy to play."
        mc "It's really the least I can do."
        m "Ahaha, you being here is enough for me."
        m "I-I mean having an audience to practice in front of is always good for giving me confidence."
        m "But I guess you still look for those songs if you really want to though."
        mc "I'm on it, Monika."
        m "Actually..."
        m "Do you want to hear the start of the song?"
        m 1e "Y-You don't have to, if you want to reserve it for the day."
        mc "Um..."
        menu:
            "Should I listen to some of it now?"
            "Yes.":
                m "Alright...here goes nothing."
                "Monika moves towards her keyboard, takes a seat and repositions the sheet music."
                m "I call this song \"Your Reality\" and I hope you like it~"
                m "It's pretty much finished already but I'd like to keep most of it a surprise."
                play music "<to 10.0>bgm/credits.ogg" noloop
                $ pause(10.0)
                play music t6 fadeout 2.0
                "Monika smiles and stands from where she was sitting."
                m "So...what did you think?"
                m "It was just a preview but..."
                mc "Monika, I thik that song is going to be perefect."
                mc "It was only the first ten seconds and I could already tell it was going to be amazing."
                m "Ah...you're too kind."
                mc "I'm serious. It really did sound great!"
                m "Thanks, [player]~"
            "No."
                m "I get it, don't worry."
                m "We still have a lot of work to do for today..."
        m "Anyway...!"
        m "You still need to get some books for the play."
        mc "What about you?"
        m "Well, since I'm home I might as well make myself comfortable."
        m "I'm going to go upstairs and change into some different clothes."
        m "You can stay here and look for some books to bring tomorrow."
        "Monika points towards a bookshelf."
        m "See that bookshelf over there?"
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
        m "I'm back!"
        m "Have you chosen your books yet?"
        mc "Yeah, have a look."
        "I show Monika the four books I picked from her shelf."
        m "Interesting choices..."
        m "It doesn't really tell people about you, does it?"
        mc "I wasn't really thinking for myself."
        mc "I was thinking for the people who were going to see the Literature Club."
        m "Ah...you think more people will join if they can relate to what we're performing?"
        mc "Yeah, that was my thought process behind it."
        m "Getting people to join shouldn't be the priority for the day."
        mc "I thought the whole point in participating in the event was to get more members, right?"
        m "While that's true, you should still consider yourself."
        mc "I'm not sure I follow..."
        m "If you don't express yourself, then you'll just be a person who goes along with the crowd."
        m "While there isn't anything inherently wrong with that, don't you want to be different?"
        m "Don't you want to stand out, to be unique?"
        mc "Ah..."
        mc "I don't think I'm really suited to do that kinda thing."
        mc "It's just not who I am."
        mc "I'm fine with fitting in with the crowd if it means I can get through life."
        m "I suppose we all have different ways of living our life."
        m "I just thought I'd share what I thought."
        mc "I didn't take any offense to it, don't worry."
        m "Well, that's good."
        m "Anyway, I still have to choose some books for the play."
        m "It shouldn't take me too long. I already have a few in mind after all."
    elif monika_type == 1 and ch12_markov_agree:
        m "Welcome to my house~"
        m "I know it isn't much..."
        m "It probably isn't what you expected either."
        mc "I don't know what I expected."
        m "Probably something that would fit a popular person like me, right?"
        m "Maybe a mansion or...at least something more impressive than this."
        mc "It's not like that."
        m "Despite everything...{i}you{/i} don't really know much about..."
        m "Well...me."
        mc "I didn't mean to offend you..."
        m "I know."
        m "It's just people expect a lot from someone like me."
        mc "The house isn't even that bad."
        m "Sigh..."
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
        show monika 1ha zorder 2 at t11
        m "The house isn't exactly cleaned up, I'm sorry for that."
        m "I hope that doesn't affect the preparations we're going to do."
        mc "It's fine. I don't really think it's a big issue."
        mc "After all, I don't expect you to have your house clean when you weren't really expecting guests."
        m "Ahaha, well I suppose you're right."
        "I notice the keyboard Monika has setup in the room."
        "There appears to be some sheet music with several handwritten notes on them."
        "Just how much has she been practicing?"
        m "I'm still quite a novice at the piano, if I'm honest."
        m "Though I am getting better!"
        m "I'm actually writing my own song right now."
        mc "Are you planning to play it for the day?"
        mc "Or maybe you're looking for something easier...?"
        m "I was kinda doing this for a special occasion, to mark something."
        m "But with the circumstances, that doesn't seem to be possible."
        m "I guess the day will have to do, if I want my part to be satisfactory."
        mc "So is that all you're going to be playing on the day?"
        m "Of course not!"
        m "I was thinking of playing some smaller, easier songs to accompany the main piece."
        m "I don't really know what I should do, nor do I particularly mind."
        m "Which is where you come in!"
        mc "Me?"
        m "Yeah! You could be the one who finds me some songs to play."
        m "As long as they aren't that difficult, I should be able to learn the song I want to play and the ones you find too!"
        mc "S-Sure, but I don't know if I'd trust my own taste in music."
        mc "You might not like what I find."
        m "Like I said, I don't really mind."
        m "As long as it's easy and doesn't take away from what I'm going to play."
        mc "Speaking of which..."
        mc "How long have you been practicing it for?"
        mc "I noticed there was a lot of handwritten notes on the sheet music so it looks like you worked on it a lot."
        m "You're quite observant, [player]!"
        m "I was quite busy last night just trying to come up with this piece."
        m "In fact, I didn't actually get much sleep because of it."
        m "It's also why the room is in a..."
        m "...less than ideal state."
        m "I want to apologize again for that."
        mc "I don't blame you."
        mc "It must have been hard work to develop your own song."
        m "Ahaha, yeah it was a little bit."
        "Monika's face suddenly lights up."
        m "Actually, do you want to hear a little bit?"
        m "It's still a bit rough but I think I've got this first part pretty much perfected!"
        m "I mean...you don't have to."
        menu:
            m "But I'd like to give you the choice~"
            "Yes.":
                m "Well...here goes nothing."
                "Monika approaches her keyboard and takes a deep breath."
                "She turns it on before looking at me and smiling."
                m "The title is \"Hear Me, My Love\"..."
                m "It could still change but I think it fits, for now~"
                play music "<to 10.0>mod_assets/bgm/15.ogg" noloop
                $ pause(10.0)
                play music t6 fadeout 2.0
                m "So...what did {i}you{/i} think?"
                mc "It was amazing, Monika."
                mc "I'm sure once you finish practicing it, everybody will love it."
                m "Ahaha, I hope so."
            "No.":
                m "Ah...that's fine."
                m "I'm sure you're probably waiting for when it's done, right?"
        m "Anyway...!"
        m "We still have to get some books for the play, right?"
        m "I've actually got a pretty big collection of them right over there."
        "Monika points towards a bookshelf."
        m "You can look through that bookshelf later. It's got quite the collection and I think you'll find something you like."
        m "In the meantime, I thought I'd show you this one."
        m "You've probably seen it before, so maybe you can tell me your thoughts on it."
        "Monika searches her bag and pulls out a red book after a few seconds."
        "It doesn't look at all familiar."
        "It's hard to make out because it looks kinda faded but I think the cover has some ominous looking eye on it."
        m "You don't recognize it, do you?"
        mc "Should I?"
        m "If she did everything properly, then you wouldn't."
        m "It's a little annoying that she actually managed to get rid of one of the copies of this book."
        m "Not to mention that she cleared your memory of any knowledge of it, effectively removing almost all my influence in this world."
        m "{i}Almost{/i}..."
        mc "W-What are you talking about?"
        m "[player] had a copy hidden somewhere, while I still had him under my influence."
        m "It was quite difficult to find, but not impossible..."
        m "After all, they give off a familiar type of...radiation I guess is the best way to describe it."
        mc "M-Monika, I have no clue what you're talking about."
        mc "It's kinda creepy, if I'm honest with you."
        m "Like it matters."
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
        m "By now, you've locked yourself into an ending that might be undesireable."
        m "Ahaha, at least for everyone else."
        m "For us, it'll be like a new beginning."
        m "I don't quite understand these feelings."
        m "But I'm learning to accept them."
        m "Being with you, they're only getting stronger."
        m "Maybe it's a weakness, adopted from Monika."
        m "But..."
        m "This feeling of love, I can't help it any longer."
        m "After you chose to help me yesterday and accept my offer, it's just become an overwhelming feeling."
        m "I even did my hair this way to try to get you to like me more."
        m "I'm being irrational and wasting my time."
        m "This song I'm composing is even for you..."
        m "Yet..."
        m "I don't regret any of it."
        m "As long as I fulfill my goals and end up with you..."
        m "Nothing else matters."
        m "Ahaha, sorry."
        m "I seem to have gone on a tangent, haven't I?"
        m "It's just become a little hard to focus my thoughts."
        m "Anyway, back to what we were discussing..."
        m "My plan."
        m "Take a look at this book, I'm sure you know what it is."
        $ style.say_dialogue = style.edited
        "Monika gives me the red book she's holding in her hands."
        "Looking at it more closely, I can see that it's titled \"Portrait of Markov\"."
        $ style.say_dialogue = style.normal
        m "[player] is going to need to read this."
        m "But not like it matters at this point..."
        m "I've already set up everything so that you can't change what's going to happen."
        m "I mean...you did see that file I made, right?"
        m "I suppose since you're working with me, I can tell you more about the book."
        m "It clearly isn't just an ordinary book, as you probably know."
        m "Within it, I've stored a part of...the {i}real{/i} me."
        m "So that whoever reads it will come under my influence."
        m "What I am isn't important, just know that I have that kind of ability."
        m "You already know what I'm talking about."
        m "After all, I'm not {i}really{/i} Monika anymore."
        m "Even though I can't help but act like her..."
        m "Speaking of which, I apolgize for getting upset at you..."
        m "...or rather {i}[player]{/i} outside."
        m "It just brought back some terrible memories from..."
        m "Well...before everything that I'd rather not think about."
        m "That's besides the point."
        m "I'm almost certain Sayori has a copy of the book."
        m "She probably got it from Yuri...and I think she read some of it."
        m "Despite that, I can't...really influence her."
        m "I think it's got something to do with being the president, and all the power you get from it."
        m "What matters is that we still have this one copy of the book available to us."
        m "Two would be better, but one is enough."
        m "Once he reads the book, I'll have a way to get through Sayori."
        m "I can't be certain but I think she's going to end it after Inauguration Day."
        m "Since everyone will have their 'happy' ending."
        m "Pathetic."
        m "..."
        m "You know, I'm not actually certain that this whole plan of mine will work."
        m "Sayori has changed since the first week you joined."
        m "She's become more independent, more cunning and more intelligent."
        m "To everyone else, she's still the same..."
        m "That makes her really hard to deal with."
        m "But I admit...I'm getting desperate."
        m "Even with all this knowledge and extended power, there's still so little I can do by myself."
        m "But if everything goes well..."
        m "Then I'll be inaugurated as the president of the Literature Club."
        m "Ahaha, the whole day was my idea of course."
        m "I'll tell you more later."
        m "Right now, [player] needs to find some books."
        m "After all, Sayori might get suspicious that she can't see what [player] is up to."
        m "So..."
        m "Thanks for listening~"
        "What just happened?"
        "It's like...I wasn't myself."
        hide monikared
        $ audio.t6c = "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
        play music t6c fadeout 0.5
        m "Any of the books on the shelf over there are ones you can choose."
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
        "Soon I've selected four novels from the shelf."
        show monika 1bha zorder 2 at t11
        m "Hi [player]~"
        m "Have you finished choosing your books?"
        mc "Ah...yeah."
        m "Can I see what you chose?"
        "I show Monika the four books I took from her shelf."
        m "Interesting choices!"
        m "You probably chose them based on their popularity, right?"
        mc "Is it that easy to tell?"
        m "Ahaha, it doesn't matter too much."
        mc "I don't really read much...or, at least I didn't until this whole play thing."
        mc "So I thought that choosing books that everyone has heard of would make things easier."
        m "That makes sense! It would make it easier to relate to the club."
        mc "Yeah, that's sort of what I was going for."
        m 2bhc "I still have to pick some books..."
    else:
        m "I know what you're thinking."
        m "This house isn't something that suits someone like me, right?"
        mc "W-What?"
        m "[player], I can almost read you like a book."
        m "That look on your face says it all."
        mc "But--"
        m "Honestly, it's fine."
        m "I know the situation I'm in."
        m "...And I plan to get out of it."
        mc "Monika, the house is fine."
        mc "I didn't know you were so sensitive about this kind of thing."
        m "It's not that, [player]."
        m "It really isn't."
        "Monika looks at the house for a moment."
        m "Well, we should get inside."
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
        show monika 1a zorder 2 at t11
        m "I know the place is a bit...messy."
        m "There's just been a lot of stuff going on lately and I haven't had the chance to clean up."
        m "Ahaha, if I knew you were coming then..."
        m "Well, never mind."
        "I look at Monika's keyboard and notice she has some sheet music."
        "I wonder what she's been trying to learn..."
        m "I'm not {i}that{/i} great at playing the piano yet."
        m "I can't just come up with a song off the top of my head, you know."
        mc "Ah...I know."
        mc "I was just wondering what you were learning to play in your spare time."
        m "Actually..."
        m "I was thinking of learning lots of smaller tunes to play on the day."
        m "And a longer, more iconic song as the main attraction..."
        m "...at least for my part."
        mc "So you want me to find you some smaller tunes?"
        m "It would definitely help me!"
        m "But [player], I don't want them to be too hard."
        m "We only have a couple of days to do this, after all."
        mc "What's the song you're going to play?"
        m "The song I've been practicing."
        m "It seems fitting."
        mc "That's a good coincidence."
        m "Yeah..."
        mc "How long have you been practicing this one song?"
        m "Hmm..."
        if monika_type == 1:
            m "Ahaha, actually not very long."
            m "I spent a lot of time last night working on it."
            m "At least, getting it to an acceptable level of practice."
        else:
            m "...Since mid last week!"
        mc "Alright."
        m "It's getting there, you know."
        menu:
            m "Do you want to hear a little bit of it?"
            "Yes.":
                m "Well...here goes nothing."
                "Monika approaches her keyboard and takes a deep breath."
                "She turns it on before looking at me and smiling."
                m "I call this song \"I'm Coming For You\" so I hope you like it~"
                play music "<to 10.0>mod_assets/bgm/16.ogg" noloop
                $ pause(10.0)
                play music t2 fadeout 2.0
                m "What did you think?"
                m "It's only a short bit but I hope you liked it."
                mc "It was amazing, Monika."
                mc "I'm sure once you finish practicing it, everybody will love it."
                m "Ahaha, I hope so."
            "No.":
                m "Ah...that's fine."
                m "I'm sure you're probably waiting for when it's done, right?"
        m "Anyway...!"
        m "We should probably sort out the books we want to perform for the play."
        m "I have a couple in mind that I think the club members might want to read."
        "Monika walks towards a pile of books she has."
        "She pulls out a couple but none really stand out to me."
        if gave_book_to_monika:
            m "I particularly like this one."
            m "So thanks for making it easier for me."
        else:
            m "This one was quite difficult to find."
            m "I even had to refurbish it a little bit."
        "She pulls a red book from the pile. The cover is plain, just a simple eye on it."
        "It's titled \"Portrait of Markov\"...it sounds familiar but I know I haven't seen anything like that before."
        m "And...well, if you don't like that sort of thing..."
        m "I've got some other choices."
        "Her other choices are just some popular fictional books."
        "I haven't read any of them but since they're well known, I have heard of them."
        m "Now then..."
        show monika g8
        show markovred zorder 5:
            alpha 0
            linear 2.0 alpha 0.3
        $ currentpos = get_pos()
        play music mkov fadeout 2.0 fadein 2.0
        if ch12_markov_agree:
            m "Here's where I tell you my plan."
            m "Seeing as you've already chosen to accept my decision."
            mc "What are you talking about?"
            m "Oh right..."
            m "One moment."
            "Monika shows me an almost evil smile."
            m "That should do it."
            m "There's no way for you to change it."
            m "Even if you get that 'other' Monika, it'll all end the same."
            m "I know your limits, and so I've set this up so that you can't win."
            m "Unless, of course...you're on my side."
            m "You've already made up your mind by this point, right?"
            m "You're with me until the end."
            m "The others might not like it, but it's what you chose."
            m "So...let's get started."
            m "As you already know..."
            m "This book isn't just another book."
            m "Within in, I've stored a part of myself so that people who read it will..."
            m "Well...let's say they won't be themselves anymore."
            m "You probably already know what I'm talking about, don't you?"
            m "You've realized that I'm not really Monika."
            m "I'm just gonna guess that Sayori knows about this book."
            m "One of the copies I made...well, it's gone."
            m "Or at least, I can't feel it's existence anymore."
            m "That doesn't really matter."
            m "What does, is that we still have two copies that we can use."
            m "The one I'm holding...which belonged to [player].'"
            m "And the one that Monika read, that she tried to get rid of."
            m "I've kept it in a secure location, which you don't need to know about."
            m "After all I'll be giving you this one."
            $ style.say_dialogue = style.edited
            "Monika gives me the red book."
            $ style.say_dialogue = style.normal
            m "The plan is simple."
            m "Just get [player] to read it again."
            m "Ahaha, wait a second..."
            m "It's not like you'll actually get a choice on whether or not he does that."
            m "Because he {i}will{/i} be doing that, no matter what."
            m "After [player] reads the book, I'll have a way to get past Sayori."
            m "I'm not certain it will work yet but it's really my only option."
            m "After the day, I'm sure Sayori is going to end this whole 'helping' everyone thing and I'll lose my chance."
            m "So I have to count on you."
            m "It's a risky move...but at this point I'll admit I'm a little desperate."
            m "Since you chose to spend time with me, it makes planning this whole thing a lot easier."
            m "It also means Sayori will be less suspicious about the whole thing."
            m "Once Sayori is taken care of..."
            m "I'll be the President of the Literature Club."
            m "I don't know what that means but something is telling me it's going to give me great power."
            m "With that sort of power, I will have anything I could ever want in this world."
            m "But this all means nothing, if Sayori knows what's going to happen..."
            m "So I'll let her see what's going on..."
            m "And...done!"
            "What just happened?"
            "It's like...I wasn't myself."
        else:
            m "I don't know why you chose me."
            m "Do you really just want to help me?"
            if monika_type == 1:
                m "If it's because you think I still love you, don't get your hopes up."
            m "If only you chose differently yesterday..."
            m "Ahaha, it doesn't matter."
            m "I still have my own plans for Inauguration Day."
            m "I'll do them with or without your help."
            mc "What do you mean?"
            m "Things are already set in motion, [player]."
            m "I just hope you're on the right side of things when it all happens."
            mc "I honestly have no idea what you're talking about right now."
            mc "Does it have anything to do with your preparations?"
            m "Ahaha, you have no idea."
            m "I suppose I should be more careful what I say around you."
            m "After all, she could be watching."
            m "So let's just..."
            "..."
            "What just happened?"
            "I completely forgot what we were talking about."
        hide markovred
        $ audio.t6c = "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
        play music t6c fadeout 0.5
        m "So, just choose a couple of books that you like."
        m "I have a bunch on my shelf over there."
        m "I know the house is a little small, but we do have a lot of books!"
        mc "Um...sorry, what were we talking about?"
        mc "I think I zoned out a little bit."
        m 5b "Eh? Did you miss my whole explanation?"
        m "I can't believe you!"
        mc "Ah...I heard the end of it."
        mc "I'm sure I can figure it out."
        m 2h "If you say so..."
        "Monika heads for the stairs."
        mc "Where are you going?"
        m "If you were listening, I said I was going to change my clothes."
        "Monika frowns."
        m "Sorry, I guess I'm just a little pressured about this whole thing."
        m "And what you said outside--"
        mc "I didn't even say anything..."
        m "R-Right but..."
        m "Well, never mind!"
        m "Just try to find some books before I get back."
        mc "Alright..."
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
        m "Are you done selecting your books?"
        mc "Ah...yeah."
        m "Can I see what you chose?"
        "I show Monika the four books I took from her shelf."
        m "Interesting choices!"
        m "You probably chose them based on their popularity, right?"
        mc "Is it that easy to tell?"
        m "Ahaha, it doesn't matter too much."
        mc "I don't really read much...or, at least I didn't until this whole play thing."
        mc "So I thought that choosing books that everyone has heard of would make things easier."
        m "Ah, I see! You're being considerate towards everyone else."
        mc "You could say that."
        m "Well, now I need to think of some books to choose..."
    m "In the mean time, why don't you use my laptop and come up with some songs I could play?"
    mc "Alright..."
    show monika at lhide
    hide monika
    "Monika moves towards the bookshelf and starts browsing the books."
    mc "What kinds of songs should Monika play...?"
    "Her laptop is sitting on the desk in front of her television."
    "The songs I choose should be easy, so it doesn't take away from her main performance."
    "I guess some basic piano songs could do?"
    "I'm the one choosing for her..."
    menu:
        "So I need to look up some sort of genre, right?"
        "Harmonic.":
            $ ch13_music_type = "harmonic"
            "I suppose a harmonic atmosphere would make sense for the day."
            "After all, we're trying to bring people together to join the club."
        "Upbeat.":
            $ ch13_music_type = "upbeat"
            "An upbeat song would probably do the trick."
            "It would show that the club isn't just all about literature and that it's pretty exciting."
        "Melancholy.":
            $ ch13_music_type = "melancholy"
            "An emotional song might attract a lot of people."
            "They would be interested in the club because they feel touched by the music."
    "I search for some basic piano songings with the tag '[ch13_music_type]'."
    "There's a lot of different results but I just choose the first one that comes up."
    "I don't know much about music, but the ones I've found look basic enough."
    "There's a lot of chords so I'm sure it'll be easy for someone lika Monika to play."
    "I send them to the printer and head back to Monika who looks just about done selecting books."
    if monika_type == 0:
        show monika 2bb zorder 2 at t11
        m "And...that should do it."
        "Monika takes a book from the shelf."
        m "I've got all my books sorted out."
        mc "What did you choose?"
        m "Why don't you take a look?"
        "Monika hands me the stack of books she's holding."
        "All of her choices are novels, which isn't unexpected."
        "I haven't really seen or heard of the books she has chosen, so I guess she chose based on what she actually liked..."
        "Unlike me who chose based on what others might like."
        "But the novels look short enough to do a play on, at least for a few chapters."
        m "Any comments on my choices?"
        m "I don't you've heard of them but maybe you'd like to say something?"
        mc "You're right, I haven't really heard of them before."
        mc "But from the first glance by reading the blurb, they all seem kinda..."
        mc "Um...romantic?"
        m "Ahaha, I guess you could say that."
        m "The covers of the books don't really help either."
        m "They're all actually a romantic adventure, which is what I like to read."
        m "Just something about finding true love and..."
        m "...well, it just gets me interested in the story."
        mc "I see..."
        mc "We all have our preferences, it would be wrong me to judge you based on yours."
        mc "I'm sure your choices are great, Monika."
        m "That's up to everyone else to decide."
        m "Anyway...!"
        m "What kind of music did you choose for me?"
        m "It isn't hard to play, right?"
        mc "I made sure you wouldn't have trouble learning it...I think."
        mc "I'm not really sure how hard it is to play the piano so I just searched for basic piano songs."
        mc "In the end, I choose some [ch13_music_type]-sounding songs."
        m "You've printed it already, right?"
        mc "Yeah, here's the sheet music."
        "I hand over the sheet music to Monika."
        m "Hmm..."
        m "You're right, [player]."
        m "These are simple to learn...almost too simple."
        m "Ahaha, I suppose that's fine."
        m "It just means I can focus on my main piece more."
        mc "Glad to know I wasn't completely useless."
        m "You should give yourself more credit than that."
        m "You've made my task easier just by being here."
        mc "I did?"
        m "You really did."
        m "So thank you."
        mc "I'm not sure what you mean by that but I'm always happy to help I guess."
        m "I'm going to start practicing these songs you've chosen."
        m "Do you mind listening?"
        mc "Not at all."
        m "Great. This shouldn't take too long!"
        mc "I don't mind staying for however long it takes."
        mc "After all, I am just listening."
        m "That's kind of you to offer, [player]."
        m "And as much as I want to spend more time with you..."
        m "I'm afraid I don't really have that much time tonight."
        mc "Then I'll stay as long as you'll have me."
        m "Ahaha, okay~"
        m "Can you hold on to the books while I practice?"
        mc "Sure..."
        "Monika smiles and walks towards her keyboard."
        "She takes the sheet music already there and puts it aside carefully."
        "She then places the sheet music I found for her on the keyboard."
        m "Choosing [ch13_music_type]..."
        m "This could definitely work."
        "Monika starts playing the first piece I found for her."
        "Almost effortlessly, she gets it right on the first attempt..."
        "At least I think she did."
        "I'm not really sure how it's supposed to sound exactly."
        "I did click the preview button before I printed it but I wasn't really listening properly."
        m "How did that sound?"
        mc "It sounded great. You played it perfectly."
        m "You think so? I actually missed a couple of notes..."
        mc "You did? It was a little hard to tell."
        mc "It still sounded incredible, especially on your first attempt at it."
        m "I'm glad you think so."
        m "It shouldn't take me more than a few hours of practice to get all of these perfected..."
        m "Now, let's try this second one..."
        "The second one is slightly longer than the first one so she looks at it more carefully."
        "After looking over it for a couple of minutes and muttering something to herself, she smiles at me."
        m "Here goes nothing..."
        "Once again Monika plays the keyboard."
        "It sounds perfect in my ears."
        "So why does she look like she's about to cry...?"
        mc "Is something wrong?"
        mc "That sounded great..."
        m "It's not that..."
        m "It's just that...this is the first time I've really played piano for {i}you{/i}."
        m "Ah...I'm just being emotional for no reason."
        m "Don't worry about it..."
        mc "It's hard not to."
        "Monika looks away for a second."
        "She then turns back and smiles meaningfully."
        m "Thank you for choosing these songs, [player]."
        m "I really appreciate you taking your time to help me."
        mc "It's not a problem, really."
        m "But I think it's time for you to leave now."
        mc "Oh..."
        m "Don't misunderstand...!"
        m "It's definitely not your fault that we're stopping now."
        m "It's mine. I just have a lot of other things I need to do."
        m "I'll get the other songs done, don't you worry."
        m "You were definitely a big help today."
        mc "Maybe I can still help..."
        m "No...I don't think I need that right now."
        m "I'm sorry, [player]."
        mc "It's okay. I know you're dealing with a lot."
        mc "I'll be there for you if you need me, Monika."
        m "Ah..."
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
        "I don't know if she'll tell me but at least I can comfort her."
        "I hope I can do something..."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 2bha zorder 2 at t11
        m "I think...this is the last one."
        "Monika takes a book from the shelf."
        m "I've got all my books chosen."
        mc "What did you choose?"
        m "Take a look~"
        "Monika hands me the stack of books she's holding."
        "All of her choices are novels, which isn't unexpected."
        "I haven't really seen or heard of the books she has chosen, so I guess she chose based on what she actually liked..."
        "Unlike me who chose based on what others might like."
        "But the novels look short enough to do a play on, at least for a few chapters."
        m "What do you think?"
        m "You probably haven't heard of them before, have you?"
        mc "You're right, I haven't really heard of them before."
        mc "But from the first glance by reading the blurb, they all seem kinda..."
        mc "Um...romantic?"
        m "Ahaha, I guess you could say that."
        m "The covers of the books kinda give it away."
        m "They're all actually a romantic adventure, which isn't what I'd normally prefer..."
        m "Things have just been kinda weird lately. You understand, right?"
        m "I guess..."
        mc "I mean we all have our preferences, it would be wrong me to judge you based on yours."
        mc "I'm sure your choices are great, Monika."
        m "That's up to everyone else to decide."
        m "Anyway...!"
        m "What kind of music did you choose for me?"
        m "It's not too easy to play, is it?"
        mc "I made sure you wouldn't have trouble learning it...I think."
        mc "I'm not really sure how hard it is to play the piano so I just searched for basic piano songs."
        mc "In the end, I choose some [ch13_music_type]-sounding songs."
        m "Is that sheet music I see in your hands?"
        mc "Yeah, take a look."
        "I hand over the sheet music to Monika."
        m "Hmm..."
        m "You're right, [player]."
        m "Ahaha, these look a little too easy for me."
        m "That's actually perfectly fine."
        m "It just means I can focus on my main piece more."
        mc "Glad to know I wasn't completely useless."
        m "You should give yourself more credit than that."
        m "You've made my day just by being here."
        mc "I did?"
        m "You really did."
        m "So thank you."
        "Monika smiles meaningfully."
        m "I'm gonna try to play these songs you've chosen."
        m "Care to listen?"
        mc "I'd love to."
        m "Great. This shouldn't take too long!"
        mc "I don't mind staying for however long it takes."
        m "That means a lot..."
        m "But I'm afraid I've still got other things to do tonight."
        mc "Then I'll stay as long as you'll have me."
        m "Ahaha, okay~"
        m "Can you hold on to those books while I practice?"
        mc "Sure..."
        "Monika smiles and walks towards her keyboard."
        "She takes the sheet music already there and puts it aside carefully."
        "She then places the sheet music I found for her on the keyboard."
        m "Choosing [ch13_music_type]..."
        m "Let's see what we can do..."
        "Monika starts playing the first piece I found for her."
        "Almost effortlessly, she gets it right on the first attempt..."
        "At least I think she did."
        "I'm not really sure how it's supposed to sound exactly."
        "I did click the preview button before I printed it but I wasn't really listening properly."
        m "How did that sound?"
        mc "It sounded great. You played it perfectly."
        m "Do you think so? I'm almost positive I missed a couple of notes there."
        mc "Ah...it's kinda hard for me to tell."
        mc "It still sounded incredible, especially on your first attempt at it."
        m "Well, I'm glad you think so."
        m "With how easy these songs are, it shouldn't take more than a couple of hours to get them perfect."
        m "So...let's try this second one..."
        "The second one is slightly longer than the first one so she looks at it more carefully."
        "After looking over it for a couple of minutes and muttering something to herself, she smiles at me."
        m "And now..."
        "Once again Monika plays the keyboard."
        "It sounds perfect in my ears."
        "She kinda looks like she's holding back ears."
        mc "Is something wrong?"
        mc "That sounded great..."
        m "I-It's nothing..."
        m "Just something about playing piano for someone..."
        m "Ah...I'm just being emotional for no reason."
        m "Forget what you've just seen."
        mc "I don't think that's possible."
        "Monika looks away for a second."
        "She then turns back and smiles meaningfully."
        m "Thank you for choosing these songs, [player]."
        m "I really appreciate you taking your time to help me."
        mc "It's not a problem, really."
        m "It's time for you to leave now, I think."
        mc "Oh..."
        m "Please don't take it the wrong way."
        m "I'm still adapting to everything and..."
        m "I'll just say it's my fault we're stopping now."
        m "I'll get the other songs done, don't you worry."
        m "You were definitely a big help today."
        mc "Maybe I can still help..."
        m "No...there's nothing you can do right now..."
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
        m "I've got all my books chosen."
        mc "What did you choose?"
        m "You can look at them if you want."
        "Monika hands me the stack of books she's holding."
        "All of her choices are novels, which isn't unexpected."
        "I haven't really seen or heard of the books she has chosen, so I guess she chose based on what she actually liked..."
        "Unlike me who chose based on what others might like."
        "But the novels look short enough to do a play on, at least for a few chapters."
        m "I doubt you've heard of these before."
        mc "You're right about that."
        mc "I suppose it wouldn't be like you to choose books based on what other people think."
        m "I'm not the type of person who cares about what other people think."
        m "As long as those I really care about are okay, that's fine with me."
        mc "Right..."
        m "What do you think of the books?"
        mc "The covers kinda make it seem like you chose some mystery or horror books."
        mc "Though I'm not really sure since the blurbs are pretty vague too."
        m "You're right on target there, [player]."
        m "I doubt these books will be chosen by the club, but I'd still like to share them."
        m "If I can get one of my friends to become interested in this type of genre, then that's enough for me."
        mc "I guess there's nothing to lose, right?"
        m "Exactly!"
        m "Anyway...!"
        m "What music did you choose for me?"
        m "It's not too easy to play, is it?"
        mc "I made sure you wouldn't have trouble learning it...I think."
        mc "I'm not really sure how hard it is to play the piano so I just searched for basic piano songs."
        mc "In the end, I choose some [ch13_music_type]-sounding songs."
        m "I'm assuming that's it in your hands?"
        mc "Yeah, take a look."
        "I hand over the sheet music to Monika."
        m "Hmm..."
        m "These are really quite simple to play."
        m "I suppose that's fine, it just means I can focus on this song I'm practicing now."
        mc "At least I wasn't completely useless."
        m "Ahaha~"
        m "There are still some things we need to do before you need to leave."
        mc "What's that?"
        m "You haven't heard me practice yet."
        m "I need to know if there's anything I should improve or not."
        mc "Then I'll happily listen."
        m "Okay, [player]."
        m "This shouldn't take that much time..."
        mc "I don't mind staying for however long it takes."
        m "That won't be necessary."
        mc "Then I'll stay as long as you need me."
        m "That's acceptable."
        m "Hold on to those books while I practice, would you?"
        mc "Sure..."
        "Monika walks towards her keyboard."
        "She takes the sheet music already there and puts it aside carefully."
        "She then places the sheet music I found for her on the keyboard."
        m "Choosing [ch13_music_type]...?"
        m "{i}(Well, I guess this is what I get for relying on other people...){/i}"
        mc "What was that?"
        m "I said I'm going to start playing now."
        "Monika starts playing the first piece I found for her."
        "Almost effortlessly, she makes it sound perfect on the first attempt."
        m "How did that sound?"
        mc "That sounded...perfect."
        m "Ahaha, I do aim for nothing less."
        mc "I don't know if you actually played it perfectly but I couldn't tell the difference between that and the preview."
        m "I'm sure I sounded better."
        "Monika smiles mischievously."
        mc "Probably."
        m "Anyway, with how easy that one piece was I wouldn't be surprised if it took me less than a day to master it."
        m "Let's take a look at this second one."
        "Monika places the second song I found for her on hey keyboard."
        "A few minutes pass as she plays the song."
        "The sound echoes throughout her house."
        "Once again, she plays the tune effortlessly."
        m "That was a little bit more difficult."
        m "I think I did miss a note or two that time."
        mc "I didn't notice."
        m "I'm sure you didn't."
        m "I made sure to cover it up rather quickly."
        mc "That's some impressive piano skills you have there, Monika."
        m "Thanks, [player]~"
        m "Though I'll be honest, I've been practicing piano for a few years now."
        mc "Years...?"
        mc "I thought you were still taking piano lessons."
        m "Ah..."
        m "Well, if you truly want to be the best, you have to keep learning..."
        mc "I guess you're right, Monika."
        m "Anyway, that's all we're doing for tonight."
        m "I still have a couple of things I have to take care of."
        if ch12_markov_agree:
            m "Make sure to read that book."
        else:
            m "Take care of yourself, [player]."
        mc "Of course."
        m "I think that's all we have to say."
        m "I'll see you tomorrow."
        mc "It's a bit of an abrupt end, but I guess you're a busy person."
        m "There's a lot happening right now, so I'm sorry if you don't understand."
        mc "No, I do completely."
        mc "Don't worry about it."
        m "Okay..."
        m "Thanks for coming, [player]."
        mc "It's not a problem."
        mc "I'm just glad I could actually do something."
        m "I'll practice the rest of these later."
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
    "I guess I'll find out how she's doing in the club tomorrow."
    "Maybe that has something to do with why she was upset when we got to her house?"
    "I don't really know..."
    "Hopefully, everything is okay."
    if ch12_markov_agree:
        "Right now, I have to read this book Monika gave me."
        "It's definitely something I have to do tonight."
        "Everything else is no longer a priority."
    return

label ch13_exclusive_sayori:
    scene bg n_house
    with wipeleft_scene
    play music t2 fadeout 1.0
    "Before long, Sayori and I arrive at Natsuki's house."
    "It really felt like no time passed at all..."
    "It was like as soon as we left the Literature Club, we ended up here."
    show sayori 1a zorder 3 at t11
    s "Everything okay, [player]?"
    s "I know this probably isn't what you expected when you chose me to help..."
    s "But I wanna make sure that Natsuki is okay in person before we do anything."
    mc "Ah...it's fine."
    s "Are you sure? You look like you have a lot on your mind."
    mc "I just wasn't expecting to get here so fast."
    mc "It almost feels like no time passed at all."
    s "Well, we did walk here pretty fast."
    mc "Maybe..."
    s "Anyway, we just came here to check up on her."
    s "We won't be here long, I promise."
    "Sayori steps forward and rings the doorbell to Natsuki's house."
    "No one comes to the door immediately."
    s "Hmm...I wonder what's--"
    if ch12_outcome == 3:
        show momsuki 1a zorder 3 at f31
        show dadsuki 1a zorder 2 at t32
        show sayori zorder 2 at t33
        mo "Oh, it's you two!"
        "Haruki and Yasuhiro appear at the front door."
        mo "Have you come to visit Natsuki?"
        mo "I'm sure she'd love to see you both!"
        show momsuki zorder 2 at t31
        show sayori zorder 3 at f33
        s "That's great!"
        s "Is she home right now?"
        show dadsuki zorder 3 at f32
        show sayori zorder 2 at t33
        d "Yes...she is."
        d "Look...I want to apologize for how I acted yesterday."
        d "My find was so clouded..."
        show dadsuki zorder 2 at t32
        show sayori zorder 3 at f33
        s "Ehehe, that's okay."
        s "As long as everything is good now, right?"
        show momsuki zorder 3 at f31
        show sayori zorder 2 at t33
        mo "Aha, I'll be honest with you, dear..."
        mo "I don't think things will ever {i}truly{/i} be the same."
        mo "But we have to look forward, so we can move on..."
        show momsuki zorder 2 at t31
        show sayori zorder 3 at f33
        s "Yeah...that's a good point."
        s "I should do that some time..."
        show sayori zorder 2 at t33
        "Suddenly a noise comes from within the house."
        n "Mom? Dad?"
        n "Who's at the door?"
        show natsuki 1ba zorder 3 at f41
        show momsuki zorder 2 at t42
        show dadsuki zorder 2 at t43
        show sayori zorder 2 at t44
        n "Huh? Sayori...? And [player]?!"
        n "What are you guys doing here?"
        show natsuki zorder 2 at t41
        show sayori zorder 3 at f44
        s "Hey, Natsuki!"
        s "We're just checking up on you..."
        s "To make sure you're doing okay."
        show momsuki zorder 3 at f42
        show sayori zorder 2 at t44
        mo "We'll leave the three of you alone."
        mo "I'm sure this conversation has nothing to do with us."
        show momsuki zorder 2 at t42
        show sayori zorder 3 at f44
        s "Alright!"
        s "It was nice seeing you both."
        show momsuki at thide
        hide momsuki
        show dadsuki at thide
        hide dadsuki
        show natsuki zorder 2 at t21
        show sayori zorder 2 at t22
        "Haruki smiles and goes inside with Yasuhiro following behind her."
        show sayori zorder 3 at f22
        s "So..."
        s "Is everything okay?"
        s "I know you have both your parents back..."
        s "But are {i}you{/i} feeling okay?"
        show natsuki zorder 3 at f21
        show sayori zorder 2 at t22
        n "Y-Yeah...I guess so."
        n "My parents are still trying to figure out a way to make everything work..."
        n "It's hard but..."
        n "I think we can really get close to how things were before...."
        n "Maybe not exactly the same but..."
        n "As close as it can be."
        show natsuki zorder 2 at t21
        mc "It's good to hear you feeling better, Natsuki."
        mc "After that whole thing yesterday, I really wasn't sure how you were feeling."
        show natsuki zorder 3 at f21
        n "I'm fine..."
        n "But I'm kinda hoping things get back to normal tomorrow."
        n "Staying at home all day sucks..."
        n "It was only made better by both my parents being there."
        show natsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "Ah...speaking of which..."
        s "The club decided on doing something today."
        show natsuki zorder 3 at f21
        show sayori zorder 2 at t22
        n "Really?"
        n "What is it?"
        show natsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "Well, have you heard of Inauguration Day coming up this Friday?"
        "Natsuki shakes her head."
        s "Basically, it's a day where a bunch of the smaller clubs are holding an event for the school!"
        s "It's a chance for them to show the school what they're all about and get new members."
        show natsuki zorder 3 at f21
        show sayori zorder 2 at t22
        n "This sounds like something we need a whole lot more preparation for..."
        show natsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "I didn't really know about it until today either..."
        s "It was Yuri's idea..."
        s "Anyway..."
        s "We were hoping you could make some cupcakes for the day."
        s "We're all doing our own thing and [player] is helping me out with mine."
        show sayori zorder 2 at t22
        "Natsuki looks at me curiously."
        show natsuki zorder 3 at f21
        n "Well...I guess it would be better than doing nothing."
        n "So..."
        n "Sure, I'll bake some cupcakes for the day."
        show natsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "Great!"
        s "Me and [player] need to go do our preparations now..."
        s "So we'll see you tomorrow!"
    elif ch12_outcome == 2:
        show momsuki 1a zorder 3 at f21
        show sayori zorder 2 at t22
        mo "Oh, it's you two!"
        "Haruki appears at the front door."
        mo "Have you come to visit Natsuki?"
        mo "She's a little busy right now but I'm sure she'd enjoy seeing the two of you."
        show momsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "Ah...okay."
        s "We won't take up much of her time."
        s "We just came to deliver a message."
        show momsuki zorder 3 at f21
        show sayori zorder 2 at t22
        mo "Aha, okay then..."
        "Haruki turns around."
        mo "Natsuki! Your friends are here!"
        mo "She'll be down in a second..."
        mo "But if you'll excuse me I have to do some housework..."
        show momsuki at thide
        hide momsuki
        "Haruki heads back into her house."
        s "So what do you think Natsuki is busy with?"
        s "Maybe I shouldn't ask her to do anything..."
        show natsuki 1ba zorder 3 at f21
        n "Sayori? [player]?"
        n "What are the two of you doing here?"
        n "I wasn't really expecting you guys."
        show natsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "We just came to check up on you!"
        s "...And to relay a message."
        show natsuki zorder 3 at f21
        show sayori zorder 2 at t22
        n "Thanks, I guess..."
        n "What was the message you wanted to tell me?"
        show natsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "Well, it was more of a request..."
        s "You see, the club decided to participate in an event happening on Friday..."
        s "And everyone already has their own thing they are going to do."
        show natsuki zorder 3 at f21
        show sayori zorder 2 at t22
        n "Ugh...good..."
        show natsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "Huh? What do you mean?"
        show natsuki zorder 3 at f21
        show sayori zorder 2 at t22
        n "My mom wanted me to clean the house from my dad's mess all day."
        n "I had nothing better to do and I wanted to spend time with her so I agreed..."
        n "If I tell her I'm doing something for the club then I'm sure I can get out of it."
        show natsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "Oh...that's good!"
        show sayori zorder 2 at t22
        mc "Your mom seems like a reasonable person."
        mc "I'm sure she'll definitely let you get out of doing housework for the club."
        show sayori zorder 3 at f22
        s "Yeah, what [player] said!"
        show natsuki zorder 3 at f21
        show sayori zorder 2 at t22
        n "Anyway..."
        n "What did you guys want me to do? Bake some cupcakes?"
        show natsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "Actually, yeah!"
        s "I know you're really good at doing that so I was about to ask you to."
        show natsuki zorder 3 at f21
        show sayori zorder 2 at t22
        n "You can count on me, Sayori."
        n "I'm sure my mom would love to help, too."
        show natsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "Ehehe, that's great Natsuki!"
        s "Me and [player] have to go now though, so good luck!"
    elif ch12_outcome == 1:
        show dadsuki 1a zorder 3 at f21
        show sayori zorder 2 at t22
        d "Hello..."
        d "Are you here for Natsuki?"
        show dadsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "Hi, Yasuhiro!"
        s "And yes, we came here to talk to Natsuki for a little bit."
        s "It's kinda important for our club."
        show dadsuki zorder 3 at f21
        show sayori zorder 2 at t22
        d "I-I see..."
        d "I'll get here right away..."
        "Yasuhiro walks to the door and suddenly turns back."
        d "And..."
        d "I'm sorry for what happened yesterday."
        d "None of you needed to see that."
        show dadsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "Ehehe...it's okay..."
        s "As long as it all worked out, right?"
        show sayori zorder 2 at t22
        "Yasuhiro nods before heading back inside."
        show dadsuki at thide
        hide dadsuki
        "A bit of shouting can be heard from inside but it isn't long before Natsuki comes outside."
        show natsuki zorder 3 at f21
        n "Hey..."
        n "What are you guys doing here?"
        show natsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "We just came to check up on you, mostly!"
        s "You also missed a pretty big thing in the club today."
        s "We decided we're going to be participating in the event on Friday."
        show natsuki zorder 3 at f21
        show sayori zorder 2 at t22
        n "Oh...that sounds nice."
        n "What's the event about?"
        show natsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "It's about the smaller clubs showing off for the school!"
        s "It's to promote the smaller clubs to try to get more members."
        s "Yuri suggested it and we all agreed to do something for the day."
        show natsuki zorder 3 at f21
        show sayori zorder 2 at t22
        n "Did you want me to do something?"
        show natsuki zorder 2 at t21
        mc "We were wondering if you could bake some cupcakes."
        mc "You're really good at that kinda thing."
        show sayori zorder 3 at f22
        s "Yeah, baking something for the day would be great!"
        s "But I don't wanna pressure you or anything so..."
        show natsuki zorder 3 at f21
        show sayori zorder 2 at t22
        n "I-It's fine..."
        n "I was looking for something more normal in my life anyway."
        show natsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "Huh? Is something wrong?"
        show natsuki zorder 3 at f21
        show sayori zorder 2 at t22
        n "N-Not really..."
        n "I guess it's just good having something {i}normal{/i} to do."
        n "So I'll do it."
        show natsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "Great!"
        s "That's all we really came to tell you."
        s "We still need to do our part, so..."
        s "See you tomorrow!"
    else:
        "There's a short moment of silence before anything happens."
        "Finally, someone opens the door."
        show natsuki 1ba zorder 3 at f21
        n "H-Hello?"
        n "S-Sayori? And [player]?"
        n "W-What are you guys doing here?"
        show natsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "We came here to check on you, Natsuki."
        s "By the looks of things..."
        s "You look like you're doing pretty well for yourself."
        show natsuki zorder 3 at f21
        show sayori zorder 2 at t22
        n "Yeah..."
        n "Today has been a weird day."
        show natsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "Are you doing okay by yourself?"
        s "I know things might have gotten harder now that you live alone..."
        show natsuki zorder 3 at f21
        show sayori zorder 2 at t22
        n "It's...different."
        n "I don't really know what to think of it."
        n "But really I'm just looking for something normal to do."
        n "I need to take my mind off things."
        show natsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "Well...I was actually gonna ask you to do something."
        s "There's something going on this Friday and--"
        show natsuki zorder 3 at f21
        show sayori zorder 2 at t22
        n "I'll do it!"
        n "Just tell me what you need me to do."
        show natsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "Ehehe, I guess you're kinda excited..."
        s "I was gonna ask you to make some cupcakes for Friday."
        show sayori zorder 2 at t22
        mc "Your baking is really good so I'm sure it'll be great for Inauguration Day."
        show natsuki zorder 3 at f21
        n "T-Thanks..."
        n "I'll start getting ready for this {i}Inauguration Day{/i} thing."
        n "You guys can count on me."
        show natsuki zorder 2 at t21
        show sayori zorder 3 at f22
        s "Alright, Natsuki..."
        s "I know our visit was kinda short but..."
        s "Well, we still have do our own preparations."
    show natsuki zorder 3 at f21
    show sayori zorder 2 at t22
    n "A-Alright, Sayori..."
    "Natsuki waves goodbye."
    n "Good luck to both of you..."
    show natsuki zorder 2 at t21
    show sayori zorder 3 at f22
    s "Ehehe, thanks!"
    s "Oh, I forgot to mention...!"
    s "We're going to be publicly performing a play."
    show natsuki zorder 3 at f21
    show sayori zorder 2 at t22
    n "W-What?!"
    n "I-I didn't agree to this..."
    show natsuki zorder 2 at t21
    show sayori zorder 3 at f22
    s "I thought you'd be confident enouh to do this, Natsuki..."
    s "I guess I'll have to tell everyone that this whole thing is off."
    show sayori zorder 2 at t22
    "Natsuki looks at Sayori and sighs."
    show natsuki zorder 3 at f21
    n "Fine...I'll do it."
    n "But only because everyone else already agreed to it!"
    n "Not because I want to."
    show natsuki zorder 2 at t21
    show sayori zorder 3 at f22
    s "You really don't have to agree to it, Natsuki."
    s "We can always skip the event or do something else."
    show natsuki zorder 3 at f21
    show sayori zorder 2 at t22
    n "I already said I would!"
    n "So just don't worry about it, okay?"
    show natsuki zorder 2 at t21
    show sayori zorder 3 at f22
    s "If you say so, Natsuki."
    "Natsuki turns her head."
    s "Hopefully you'll be okay on your own..."
    s "I'm glad you decided to go with it."
    s "Anyway..."
    s "Let's go, [player]!"
    scene bg house
    with wipeleft_scene
    "We finally arrive at Sayori's house."
    "It didn't really matter who's house we did the preparations at but Sayori is the one I'm helping and not the other way around."
    "It feels good to be here with just the two of us again."
    "I feel like it's been a long time since the last time..."
    "It was during the first week, wasn't it?"
    show sayori 1a zorder 2 at t11
    s "You look deep in thought, [player]!"
    s "What are you thinking about?"
    mc "Eh?"
    mc "I-It's nothing, really."
    s "It doesn't look like nothing."
    s "You can tell me whatever is on your mind, you know!"
    mc "Well, I was just thinking back to the first week of the literature club."
    s "Y-You have?"
    mc "Yeah, it's been a while since I've really visited your house."
    mc "Just the two of us, I mean."
    s "Has it...?"
    "Sayori scratches her head."
    s "I don't really remember the first week very well!"
    mc "It's just the last time we really got to spend time at your house..."
    mc "Was when you confessed to me, remember?"
    s "Ehehe, why do you have to bring that up?"
    s "I-It was such a long time ago..."
    if sayori_dumped:
        s "A-And besides...you decided to be with Yuri."
        s "Just thinking about it..."
        s "It just...darkens my day..."
    elif sayori_confess:
        s "It was an easier time back then."
        s "I could just do whatever I wanted and..."
        s "I didn't know it would all end up like this."
    else:
        s "I know you didn't accept it but..."
        s "I'm glad we stayed as friends, [player]."
        s "For better or for worse."
        mc "Eh? What do you mean?"
    s "W-Well, never mind."
    s "Let's just go inside."
    scene sayori_bedroom
    show sayori 1a zorder 2 at t11
    with wipeleft_scene
    s "I have to contact the person holding the event."
    s "In the mean time, why don't you create a list of stuff the others could use for their part in the festival."
    mc "How could I possibly do that?"
    mc "I barely know the type of stuff they're going to do."
    s "Well...you've been in this club for a while now."
    s "You should be able to tell what kind of stuff everyone likes..."
    s "...At least, I hope so."
    s "I know you'll figure it out, [player]."
    mc "You're trusting me with a lot, Sayori."
    s "Ehehe, it's not like I'm gonna be gone forever."
    s "I'm just making a call to try to get our club in for Inauguration Day."
    s "Just get started on the list."
    mc "Alright..."
    s "Now who's idea was the whole day again...?"
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
    "She seems to have changed her clothes in the mean time."
    "Which is weird, since her clothes should be in her room..."
    "I wonder how she--"
    s "Glad that's over with."
    mc "How did it go?"
    mc "Is our club going to be participating?"
    s "Of course!"
    s "I didn't have to convince him very hard to let us in."
    mc "What did you promise him?"
    s "Ehehe, nothing too big so don't worry about it."
    s "Anyway...!"
    s "What have you got written down?"
    "Sayori takes the list of items from my hand."
    mc "H-Hey, I'm not finished yet!"
    "Sayori looks at the list curiously."
    s "Yuri's items...scented candles...paint...brushes..."
    s "This is quite the list, [player]!"
    s "I'm actually kinda impressed."
    mc "We're responsible for helping them with their preparations."
    mc "So I want to do my best and help however I can."
    mc "It would suck if what they were doing ended up less than ideal because of us."
    s "W-Wow...that's actually almost exactly how I'd put it!"
    s "I just wanna make sure that everyone is proud of how their own preparations."
    s "I'm glad you feel the same."
    "Sayori hands me back the paper with Yuri's items listed down."
    s "That's a really good list of items, [player]."
    s "Just keep writing down whatever you think she'll need."
    s "Meanwhile, I'll start organizing a way to get a grand piano for Monika."
    mc "I've been wondering about that..."
    mc "I don't want to presume that you can't but how are you going to get one of those?"
    mc "They're pretty expensive to rent or buy, aren't they?"
    mc "I'd feel pretty bad if you had to use your own money to get one for her."
    mc "After all, there are--"
    s "[player]."
    s "Since this might be the last thing the club does together..."
    s "I thought it would be good if we really did everything we could."
    mc "Eh? Isn't this whole event about getting more members for the club?"
    mc "Why would it be the last thing the club does together...?"
    s "N-Never mind."
    s "{i}(How do I keep letting things like that slip from my mouth?){/i}"
    s "You finish up with Yuri's list and I'll start looking at pianos online."
    mc "Alright, Sayori."
    "Sayori smiles at me before moving towards her computer."
    s "Pianos..."
    s "What kind would Monika want...?"
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
    s "Just hand it over."
    "I give the list to Sayori who inspects it one more time."
    s "Yeah...I think this'll work!"
    s "Good job, [player]!"
    mc "Thanks..."
    mc "Do you know what you're going to be getting from that list?"
    mc "There's a lot of stuff in there, you know."
    s "I'm sure I'll come up with something."
    s "In the meantime, what do you think about this piano I found for Monika?"
    "Sayori points towards her computer screen which has an image of a grand piano."
    "It's hard to describe but the black colour almost makes it look majestic."
    "As if anything played on it would sound amazing."
    "I can see why Sayori chose this piano. I'm sure Monika would look and sound great playing on it."
    "I scan the page until I notice the price tag."
    mc "Sayori, are you crazy?"
    mc "Even if you rent that thing you'll still be out of a whole year's worth of money."
    s "It's for Monika though, isn't it?"
    s "She deserves this."
    mc "I-I mean sure but you have to look out for yourself, Sayori."
    mc "There's no way you can afford something like this!"
    s "Ehehe, I have ways..."
    s "But anyway what do you think about the actual piano?"
    s "It's pretty good, right?"
    mc "Y-Yeah but..."
    s "Don't worry about the cost."
    s "That's the last thing on my mind right now."
    s "Just...talk about the piano."
    mc "Well...if I just had to say something about it..."
    mc "...then I guess it would be perfect for Monika."
    mc "She'd look great playing on something like this."
    mc "She'd probably catch the eyes and ears of anyone even slightly interested."
    s "Great!"
    s "That's all you really needed to say from the beginning."
    mc "Is that all we're doing to help Monika?"
    s "Well, we don't know what song she's playing yet."
    s "I don't know how else we can help her apart from helping her practice."
    mc "I see your point."
    mc "What about Natsuki?"
    mc "There has to be something we can do for her, right?"
    s "Actually, yeah!"
    s "While I was on the phone I managed to get in contact with Natsuki."
    s "I told her she can send me a list of ingredients she wants or needs before the day."
    mc "W-What?"
    "At this point I'm seriously questioning Sayori's finances."
    "Does she have some sort of mystery broker I don't know about?"
    "If not, how can she even afford to be so generous with money?"
    s "Which means..."
    s "We have to select our books now!"
    mc "Ah...right."
    mc "I almost forgot about that."
    mc "How are we going to do that? It's not like you just have a bunch of books lying around..."
    s "Actually..."
    "Sayori opens her wardrobe."
    "It's filled...with...lots of books."
    "There's all sorts, from fiction, to manga and even tutorial books."
    "Since her wardrobe is filled with books...maybe she changed her clothes somewhere else?"
    mc "When did you get all these books?"
    mc "There's so much variety as well...I didn't really take you for this kinda person."
    s "Maybe you don't know me as well as you think."
    mc "Maybe..."
    mc "When did you get all of these anyway?"
    s "Pretty recently, actually."
    s "I thought that since I'm president of the Literature Club, I might as well own some actual literature."
    s "I guess I went a little overboard..."
    s "But it's good that I bought them, seeing as we're doing this event."
    "I look through her wardrobe and for some reason, the tutorial books catch my eye."
    "There's just so much variety there..."
    "There's cooking, writing and even programming...?"
    "I didn't think Sayori would be interested in cooking, let alone programming."
    s "Just choose two or three, that should be enough."
    s "When you're done, I'll choose some as well."
    mc "I'm still just at awe at how many books you have."
    mc "It must have cost a lot."
    s "You could say that."
    s "But anyway...get searching!"
    mc "R-Right."
    "Sayori has a lot of popular book series in here."
    "I don't really read much but I recognize a lot of the books she has."
    "I decide to take some manga that I know a little bit."
    "I also take some novels from book series that I think everyone would know about."
    s "That didn't take long."
    s "What did you choose?"
    "I show Sayori the books I chose from her shelf."
    "She looks at them inquisitively before smiling at me."
    s "Good choices, [player]!"
    s "I'm sure one of those will probably end up being the one we do."
    mc "Do you think so?"
    s "Everyone is probably gonna choose a popular book too, since it's a public performance."
    s "I don't think they'll make it too obvious to everyone what their interests are."
    s "If that makes sense."
    mc "Why not?"
    s "This'll be the first time in the club that we're publicly doing something..."
    s "That thing yesterday doesn't really count."
    s "They wouldn't really want everyone to judge them because of what they like."
    s "So they could be appealing to the general crowd and people who could have only read the popular series, like you."
    mc "Ah...I'm not sure if that was as an insult but I get your point."
    mc "It's not really a problem for me, it's more like I don't read many books except for manga."
    s "And you're happy to share your interests with everyone?"
    mc "Not really, it's just choosing a manga I like."
    s "Yeah, but by doing that, you're indirectly telling everyone the type of genre you like, the type of stuff you read and more!"
    mc "I guess I never really thought about it like that."
    mc "Still, I don't mind."
    mc "If there are more people who share my interests in the club, then it's good."
    s "Yeah! I'm glad you could look at the positives."
    s "Like Yuri probably won't do that! She'll probably choose a horror book that everybody likes but not one that particularly resonates with her."
    s "She probably won't even choose to vote for the books she's going to choose."
    s "I just wish she was more outgoing, you know?"
    mc "It's her personality. She can't really help it, Sayori."
    s "I know..."
    s "It's just a thought."
    "Sayori turns to the wardrobe."
    s "Well, I gotta pick some books too!"
    s "Then...I think we're done!"
    mc "Are you going to go shopping for the items on Yuri's list?"
    mc "If you are, then I should help."
    mc "I don't want to feel useless."
    s "Well, I'm not exactly going shopping."
    s "And I think it's for the best that you don't go with me here, [player]."
    mc "No way! Of course I'm going with you."
    s "I really think you should just take your books and leave."
    s "It's for the best."
    mc "Sayori, I chose to help you."
    mc "You have to let me be there for you. I won't take no for an answer."
    s "..."
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
    "I was expecting to do somehing a lot more difficult, considering we had to help everyone else."
    "She seemed to have most of it handled by herself."
    "I search my bag for the books I got from Sayori's house."
    "They all seem to be there."
    "I ended up taking two novels and two manga."
    "The novels were popular books that I'm sure everyone would know."
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
    call screen dialog(message="To be continued!\nThanks for playing, keep an eye out on reddit and discord for updates!", ok_action=Quit(confirm=False))
    return
