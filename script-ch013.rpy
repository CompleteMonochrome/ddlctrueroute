label ch13_main:
    scene black
    show sayori 1a zorder 2 at t11
    with dissolve_scene_full
    play music mend fadeout 2.0
    s "I want to say that I don't really know what's going to happen today."
    s "I know I made the day and everything but something is changing it..."
    s "I don't know if that makes any sense to you but it's making my ability to see into the future kinda useless."
    s "Maybe it's just the game glitching out from too many days or something."
    s "Or maybe I just can't see what's going to happen..."
    s "Who knows?"
    s "I could ask Monika about it but..."
    s "Never mind."
    s "Anyway, I should probably tell you that I changed the poem game a little."
    s "Your poem doensn't really matter anymore."
    s "After yesterday, I didn't really see the point."
    s "Seeing as everyone already knows the type of style you're writing."
    s "There was also this weird thing that was in the poem game script."
    s "I'm not really sure how to describe it but it had something to do with Monika..."
    s "Oh well, it's gone now so don't worry about it."
    s "I might just ask Monika if she knows what that is about."
    s "But yeah...you're poems don't really matter anymore!"
    if n_appeal >= 4 and (ch12_outcome == 3 or ch12_outcome == 1):
        s "Um...actually, that's not completely true."
        s "If you're still trying to make [player] go for Natsuki..."
        if sayori_confess:
            s "...even after what you made [player] say to me a long time ago..."
        s "...then your poem does matter a little bit."
        s "So if you really are going for her, then you should make sure that your poem is written for her...okay?"
        s "You'll see what I mean later today."
        s "Speaking of which..."
    else:
        s "Anyway..."
    s "I want to talk about what happened with Natsuki."
    if ch12_outcome == 3:
        s "She's got her mom back and her dad is back to normal."
        s "Whatever normal means..."
        s "I can't help but feel there's something wrong with what we did."
        s "Like...do you ever think that the ending we gave her feels..."
        s "...oh, I don't know, artificial maybe?"
        s "Is it really right to give Natsuki her mom back?"
        s "..."
        s "I guess what's done is done, isn't it?"
        s "It is the best outcome, it just feels wrong for some reason."
        s "Bringing someone back from the--"
        s "Never mind..."
        s "As long as Natsuki is happy..."
    elif ch12_outcome == 2:
        s "She's got her mom back and her dad is..."
        s "Well, not with Natsuki."
        s "When I asked Haruki what he was going to do with her yesterday, I think she said something about calling the police."
        s "I guess that's probably the best way to handle it, isn't it?"
        s "I don't really feel sorry for Yasuhiro or anything but I feel like we did something wrong."
        s "Like what Natsuki is feeling isn't real...does that make sense?"
        s "I mean we gave her back her mom but..."
        s "...I don't know what to think about this whole thing."
        s "I know I was the one who told you to bring her back..."
        s "..."
        s "Well, it doesn't matter. As long as Natsuki is happy."
    elif ch12_outcome == 1:
        s "So...what do you think about this whole thing?"
        s "Natsuki has her dad caring for her again, like a proper parent should."
        s "I don't know if things between them will ever be the same, especially since..."
        s "...{i}you know{/i}, is still missing."
        s "It's better this way, isn't it?"
        s "It's more natural than bringing back a dead person, right?"
        s "I mean, who are we to decide if someone should live or die?"
        s "Oh...sorry."
        s "I got a bit too philosphical there, didn't I?"
        s "I just hope Natsuki does end up happy, in the end."
    else:
        s "So...this is an interesting end for Natsuki."
        s "She lives by herself now."
        s "Yasuhiro is in jail while he's being investigated."
        s "Who knows how long he'll be in there for but with the evidence we have..."
        s "Well, he won't be getting out anytime soon."
        s "I have to wonder..."
        s "Can she really be happy like this?"
        s "I don't know the answer to that question."
        s "I guess the best thing we can do it support her through this time..."
        s "...and maybe she'll learn to be happy again."
    if s_appeal >= 4:
        s "I've been meaning to say..."
        s "There's this feeling in my body."
        s "We set out to solve Natsuki and Yuri's problems, right?"
        s "But..."
        s "I feel like there's something else."
        s "Like there's someone we haven't really helped yet."
        s "I have to think about this."
        s "See you, [player]."
    elif monika_type == 0:
        s "So everything is okay, right?"
        s "I mean..."
        s "We have solved everyone's problems, haven't we?"
        s "Yuri is feeling better, she isn't as shy anymore and she opens up to other people easier."
        s "It'll take time for her to really change for the better but..."
        s "...it's progress."
        s "Natsuki has her dad problem dealt with."
        s "Whatever way we dealt with it, we solved her problem in one way or another."
        s "And Monika...well, she was first."
        s "There's just..."
        s "No..."
        s "I can't think about that."
        s "There's nothing wrong, there's nothing left to fix."
        s "Um..."
        s "Sorry, I have to go."
    else:
        s "So I've been thinking..."
        s "There's nothing we really need to do today."
        s "Everyone is sorta happy, right?"
        s "I mean you {i}have{/i} helped everyone."
        s "You gave Monika a chance, you helped Yuri and Natsuki with their problems..."
        s "So why do I still feel like there's something missing...?"
        s "Maybe..."
        s "No, I can't think like that."
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
    "It's not really really a big issue, it's just that..."
    "It's always better walking to school with someone close to me."
    "There was more we could talk about and it made the journey less boring."
    "I wonder what final preparations Sayori is doing."
    "It must be something for the club."
    "Still, having this time for myself let's me think about what I've done."
    "All the decisions I made in the past and how I could have changed them."
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
    "I don't really have anywhere in particular I want to go but I make sure I'm relatively close to the Literature Club."
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
    "And it was all because of some cupcakes Sayori promised me."
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
    "It was really important and I knew I had the option to write the others, but I always chose Monika."
    "I must have forgotten it."
    "But why does it feel like Monika was more important..."
    "At least...during this time."
    "Well...there has must to be more to it."
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
    "It's not like she knew Sayori better than I do, did she?"
    "In any case..."
    "She told me to visit Sayori on Saturday, and I did."
    "Monika was there too and she assured me that Sayori was going to be feeling better."
    "I made sure that Sayori was okay, and I assured her that everything was going to be okay."
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
    "After Sayori's confession, I remember [ch4_name] came over to do some preparation."
    "I don't really remember what the preparation was for..."
    "Which, for some reason, is really bothering me."
    if ch4_name == "Yuri":
        "But I do remember making a banner with her."
        "We spent most of the day on it and I think it turned out pretty well."
        "The atmosphere we created was going to be great..."
    else:
        "But I do remember baking with Natsuki."
        "It was an experience that I would never forget."
        "Who knew baking was so much more fun with another person?"
    "Spending the day with [ch4_name] was probably one of my highlights of the first week."
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
        show yuri 1a zorder 2 at t11
        y "Ah, [player]."
        "Yuri appears in front of me."
        "She looks a little anxious."
        y "You're finally here."
        mc "Yuri?"
        mc "What are you doing out here?"
        y "I could be asking you the same question."
        mc "I had to think about a couple of things for a while."
        mc "I guess I just lost track of time."
        mc "What's your reason?"
        y "Well...I was out looking for you."
        y "I thought you'd be in the club but you weren't..."
        y "We waited a while and you didn't come..."
        y "...so I was going to try to find you."
        mc "Well, I'm here now."
        mc "Sorry if I worried you."
        y "N-No, that's okay."
        y "Besides...I don't think Natsuki is here yet either."
        mc "Oh...do you know where she is?"
        y "I have no idea."
        mc "I suppose Sayori will tell us, if she knows."
        y "A-Anyway, we should head inside before we waste anymore time."
    elif monika_type == 0:
        show monika 1a zorder 2 at t11
        m "Oh, you're late too?"
        "Monika appears in the corridor outside the club."
        mc "Monika? Why are you so late?"
        m "Ahaha, I could be asking you the same question!"
        mc "I guess I just lost track of time."
        mc "I had a lot I needed to think about."
        m "Oh, I see."
        mc "What about you?"
        mc "I didn't expect you to be late as well."
        m "Well...I had a piano lesson."
        m "I asked the tutor if he would teach me for a bit longer."
        m "Because I haven't really been practicing as much lately."
        mc "Is it for anything in particular?"
        m "Hmm...maybe."
        m "I'm not too sure on the details yet, but I've got something in mind."
        mc "I'd love to hear you play."
        mc "I mean you must have a decent amount of practice now, right?"
        "Monika smiles."
        m "I'm certainly getting better, I think."
        m "I'd be happy to let you and the others hear me play, when the time is right."
        mc "I can't wait."
        m "Anyway, we should get inside."
        m "We've kept the others waiting for long enough."
    elif ch12_markov_agree and monika_type == 1:
        show monika 1ha zorder 2 at t11
        m "Hi [player]~"
        "It's Monika, but..."
        "...she's not wearing her white ribbon and her hair is down."
        m "I suppose you're late too?"
        mc "A-Ah, I guess."
        m "What's the matter? You seem kinda shocked."
        mc "I'm a little surprised at your new look, that's all."
        "Monika looks at her herself."
        m "Oh, this?"
        m "Yeah...I thought I would change it up a little."
        m "We can talk about it later."
        mc "Alright..."
        m "So why aren't you in the club yet?"
        m "Ahaha, I thought I would be the late one~"
        mc "I had to think about a few things."
        mc "I guess I just lost track of time."
        m "I see..."
        mc "What's your reason?"
        m "Well, I was practicing piano and asked for a slightly extended lesson from the tutor."
        m "I just want to get better faster, you know?"
        mc "Any reason in particular?"
        m "Maybe~"
        mc "I'd love to hear you play."
        m "Maybe when the time is right, [player]."
        m "For now, we should get to the meeting. We've probably kept them waiting long enough."
    else:
        show monika 1a zorder 2 at t11
        m "[player]?"
        "Monika stands in front of me, just outside the clubroom."
        m "Why aren't you in the club already?"
        mc "Ah--"
        m "Actually, don't answer that."
        m "{i}Your{/i} business is not my concern."
        mc "Alright..."
        mc "Well, what are you doing out here?"
        m "I had a few matters I needed to attend to."
        m "I had a piano lesson for one."
        mc "Is that all...?"
        m "Well, I'd rather not tell you the rest."
        m "It's quite personal, if I'm honest."
        mc "I won't pry then."
        m "Good. Let's head inside before we waste anymore time."
    scene bg club_day
    show sayori zorder 2 at t32
    if visited_yuri_hospital:
        show monika 1a zorder 2 at t31
    else:
        show yuri 1a zorder 2 at t33
    with wipeleft_scene
    show sayori 1a zorder 2 at f32
    if visited_yuri_hospital:
        s "[player], where have you been?"
        s "Yuri even went out to look for you because you took so long..."
    else:
        s "What took the two of you so long?"
        s "We've been waiting here for ages."
    show sayori zorder 2 at t32
    if visited_yuri_hospital:
        show yuri 1a zorder 3 at f33
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
    else:
        show monika 1a zorder 2 at f31
        m "I had a few things I needed to deal with."
        m "Sorry, if I'm late but it was important."
        m "I don't know about [player] though..."
    show monika zorder 2 at t31
    mc "Sorry, Sayori."
    mc "I just had a lot on my mind and I guess I lost track of time."
    mc "It won't happen again."
    show sayori zorder 3 at f32
    s "Alright, if you say so..."
    "Sayori points to the second empty seat around the table."
    s "As you can probably tell, Natsuki isn't here today."
    s "She told me on the phone yesterday that she was going to take the day off."
    s "She didn't need to give me a reason..."
    s "It's pretty obvious, isn't it?"
    show sayori zorder 2 at t32
    mc "Yeah, I think I understand."
    show sayori zorder 3 at f32
    s "Anyway..."
    s "She isn't here but I was going to suggest not doing one of those book-reading things anymore."
    s "I don't really want to pressure Natsuki too much."
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y "So what do you suppose we do then?"
    show sayori zorder 3 at f32
    show yuri zorder 2 at t33
    s "Actually, I was gonna ask you guys!"
    s "We don't really {i}need{/i} to do anything."
    s "Especially since I've already done what I set out to do."
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y "Huh?"
    y "What did you set out to do, Sayori?"
    show sayori zorder 3 at f32
    show yuri zorder 2 at t33
    s "To make you all happy, of course!"
    s "Or at the very least, try to make you feel better."
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y "Feel better in terms of what..?"
    y "You're being a little bit cryptic."
    show sayori zorder 3 at f32
    show yuri zorder 2 at t33
    if (sayori_confess and not sayori_dumped) or s_appeal >= 4:
        s "Actually...maybe I'm not finished yet."
        s "There's still a couple of things I have to do."
        s "I hope I will be soon though."
    else:
        s "Never mind what I said Yuri."
        s "I'm really just thinking out loud."
    show sayori zorder 2 at t32
    if monika_type == 0:
        show monika 3b zorder 3 at f31
        m "There's nothing wrong with doing that."
        m "Sometimes you just have to say what's on your mind."
    elif ch12_markov_agree and monika_type == 1:
        show monika 2hb zorder 3 at f31
        m "Well, you are a pretty complicated person."
        m "There's so many special things about you, Sayori."
    else:
        m "I wonder if you're doing okay yourself, Sayori."
        m "You probably have a lot to think about, right?"
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s "Don't worry about me, Monika."
    s "I'll be fine."
    s "{i}(And so will everyone else...){/i}"
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y "Um...I have a suggestion for what we could do for a little bit."
    y "That is...if you all want to hear it."
    show sayori zorder 3 at f32
    show yuri zorder 2 at t33
    s "Of course! Say whatever is on your mind, Yuri."
    s "There are no bad suggestions, after all."
    show sayori zorder 2 at t32
    "Yuri looks at all of us then thinks for a moment."
    show yuri zorder 3 at f33
    y "Well..."
    y "There's an event coming up for school."
    y "I was hoping we could try to show what the Literature Club is about."
    show sayori zorder 3 at f32
    show yuri zorder 2 at t33
    s "Event? I haven't really been keeping up with school stuff."
    s "What event is it, Yuri? More importantly, when is it?"
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y "It's a thing the school is doing to promote the smaller clubs."
    y "I overheard someone talk about it."
    y "I think it was called \"Inauguration Day\" or something..."
    y "If I remember correctly it's on Friday this week."
    y "So we if we want to do something for it, we should start thinking about it today."
    y "It's strange though, I hadn't really heard of it before today."
    y "From the sounds of things, it was a pretty recent initiative by the school."
    y "I wonder who's idea that was..."
    show yuri zorder 2 at t33
    if monika_type == 0:
        show monika zorder 3 at f31
        m "Ahaha, I do have some idea as to who suggested it."
        show monika zorder 2 at t31
        show yuri zorder 3 at f33
        y "Who was it?"
        show monika zorder 3 at f31
        show yuri zorder 2 at t33
        m "You know how I'm friends with a lot of people around school?"
        m "Well, I asked what the presidents in smaller clubs thought of getting new members."
        m "They were all for it, so I got one of my friends whos a president of a larger club to try to help."
        m "He also happened to be a president of a smaller club so he was all for it."
        m "Then...I guess his influence made the school go for it."
        m "It might be a good idea for the Literature Club, if we ever wanted it to grow."
    elif monika_type == 1 and ch12_markov_agree:
        show monika zorder 3 at f31
        m "Oh, I might have an idea~"
        show monika zorder 2 at t31
        show yuri zorder 3 at f33
        y "Do you know something we don't, Monika?"
        show monika zorder 3 at f31
        show yuri zorder 2 at t33
        m "Well, all I can really say is what I heard about it during lunch."
        m "A couple of the smaller club's presidents wanted to try to get more members."
        m "I guess they actually managed to get the school to do it?"
        m "I think it's because one of the presidents was also a president of a larger club."
        m "So he probably had a pretty big influence on the whole thing..."
        m "I think it would be a great opportunity for the Literature Club to do something though!"
    else:
        show monika zorder 3 at f31
        m "It doesn't really matter, does it?"
        show monika zorder 2 at t31
        show yuri zorder 3 at f33
        y "I suppose it doesn't."
        y "I was just curious..."
        show monika zorder 3 at f31
        show yuri zorder 2 at t33
        m "It would be a good opportunity for the Literature Club, I think."
        m "You know, to get us to grow a little since there's only five of us."
    show monika zorder 2 at t31
    show sayori zorder 3 at f33
    s "Hmm..."
    s "I'm not sure if this is a good idea or not."
    show sayori zorder 2 at t33
    mc "Didn't you say there was no bad suggestions?"
    mc "Besides, it doesn't sound like a bad suggestion anyway."
    show sayori zorder 3 at f33
    s "Oh...it was definitely a good suggestion."
    s "I just meant that I have no idea what we could do to promote the club."
    s "{i}(Or if doing something like this again is a good idea...){/i}"
    show yuri zorder 3 at f31
    show sayori zorder 2 at t33
    y "Well..."
    y "I know you said that you don't want to do the 'play-read' thing anymore..."
    y "But I think we could do one of those, just in front of actual people this time."
    y "We've already done two practice ones so..."
    show yuri zorder 2 at t31
    show sayori zorder 3 at f33
    s "Do you expect me to write a script, like the last two?"
    s "It's hard work, you know."
    show sayori zorder 2 at t33
    if monika_type == 0:
        show monika zorder 3 at f31
        m "Maybe I could help you write it this time."
        m "Ah...that is, if we are really doing this."
    elif monika_type == 1 and ch12_markov_agree:
        show monika zorder 3 at f31
        m "Well, I can always lend you a hand."
        m "It would definitely be a good opportunity if we do this..."
    else:
        show monika zorder 3 at f31
        m "Don't worry about doing it by yourself, Sayori."
        m "I can help you with that."
    show monika zorder 2 at t31
    show sayori zorder 3 at f33
    s "Well..."
    s "We still can't do this without Natsuki."
    s "Either all of us have to agree to it, or we aren't doing it at all."
    show yuri zorder 3 at f32
    show sayori zorder 2 at t33
    y "It kinda sounds like you don't like my idea, Sayori."
    y "We don't have to do this, if you're {i}that{/i} opposed to it."
    y "You are the president after all..."
    show yuri zorder 2 at t32
    show sayori zorder 3 at f33
    s "No, Yuri!"
    s "It's not like that, really!"
    s "I really like the idea! It's just...."
    s "Well, there might be some complications..."
    show yuri zorder 3 at f32
    show sayori zorder 2 at t33
    y "Then we can work through them together, all five of us."
    y "I'm willing to do my part for the Literature Club."
    y "I'm sure the others are too."
    show yuri zorder 2 at t32
    "Seeing Yuri so confident..."
    "It almost feels a little unnatural compared to how she acted on my first day."
    "It's definitely not a bad thing and it probably isn't the first time she's done it."
    "I guess I've just started taking notice, for real, today."
    "I wonder when she changed though..."
    show sayori zorder 3 at f33
    s "I don't think you understand the scale of these complications, Yuri."
    s "But I appreciate the sediment."
    show sayori zorder 2 at t33
    if monika_type == 0:
        show monika zorder 3 at f31
        m "Ah...don't you mean 'sentiment'?"
        m "Sediments are something completely different, Sayori."
    elif monika_type == 1 and ch12_markov_agree:
        show monika zorder 3 at f31
        m "I think the word you're looking for is 'sentiment', Sayori."
    else:
        show monika zorder 3 at f31
        m "You meant 'sentiment'...right?"
    show monika zorder 2 at t31
    show sayori zorder 3 at f33
    s "Ehehe, yeah! Sentiment is what I meant~"
    s "Thanks, Monika!"
    s "Do you three have any more suggestions?"
    show sayori zorder 2 at t33
    "Sayori looks at the three of us."
    "It's as if she is scanning us for any other idea."
    if not monika_type == 0 and not ch12_markov_agree:
        show monika g7
        "I feel like I have a great suggestion for Sayori."
        "Maybe I should say something."
        menu:
            "Speak up.":
                $ sayori_personality += 1
                mc "Sayori, have you considered killing yourself?"
                show sayori zorder 3 at f33
                s "W-What?"
                s "[player], why would you even say that?!"
                s "That's..."
                show sayori zorder 2 at t33
                mc "H-Huh?"
                mc "I don't..."
                mc "Why did I...?"
                "Everyone just stares at me."
                "I don't even know why I said that..."
                "It felt like it just came out of my mouth, like I had no control over what I was saying."
                show monika zorder 3 at f31
                m "[player], are you feeling okay?"
                m "That was a pretty mean thing to say."
                show monika zorder 2 at t31
                show yuri zorder 3 at f32
                y "Sayori, he didn't mean it."
                y "I don't know what's come over him but..."
                "Yuri looks at me with a bewildered expression."
                y "You didn't mean it, right?"
                show yuri zorder 2 at t32
                mc "No! Of course I didn't mean it!"
                mc "I don't know what came over me!"
                mc "I'd never say anything like that...not to anyone."
                show sayori zorder 3 at f33
                s "..."
                s "So why did you say it to me..."
                $ _history_list = []
                show screen tear(20, 0.1, 0.1, 0, 40)
                window hide(None)
                play sound "sfx/s_kill_glitch1.ogg"
                show monika 1n zorder 2 at t31
                show yuri 1a zorder 2 at t32
                show sayori 1a zorder 3 at t33
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
    show sayori zorder 3 at f33
    s "I guess this is the best idea we're going to get, isn't it?"
    s "I wonder if Natsuki would have said anything different."
    s "Oh well..."
    s "Since we aren't really doing anything today, I thought we could skip to sharing poems."
    s "There's not really a point sitting here talking about what we could do for the fest--"
    s "I mean, for \"Inauguration Day\" without Natsuki here."
    s "The best we could do is come up with books to perform but that's not really fair without her."
    show yuri zorder 3 at f32
    show sayori zorder 2 at t33
    y "That's a fair reason, Sayori."
    y "We should be considerate of Natsuki's feelings as well."
    y "Maybe tonight we can all come up with a list of books that we like that would be a good idea to perform."
    y "And tomorrow we can choose which one we're performing from everyone's options."
    show yuri zorder 2 at t32
    show sayori zorder 3 at f33
    s "Yeah, that would probably be the best way to handle it."
    s "I guess that's everyone's task for tonight!"
    s "Everybody choose one or two books you'd like to perform in front of actual people."
    s "I don't know how long Natsuki is going to be away for so I'll go visit her tonight to make sure everything is okay."
    show sayori zorder 2 at t33
    if monika_type == 0:
        show monika zorder 3 at f31
        m "I think that's a great idea."
        m "She probably would appreciate you visiting."
        m "I wonder how she's dealing with everything..."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1hb zorder 3 at f31
        m "Knowing Natsuki, she'd probably appreciate the company."
        m "That's really kind of you, Sayori."
    else:
        show monika zorder 3 at f31
        m "Visiting Natsuki at a time like this...?"
        m "I guess something that resembles part of her normal life would be appreciated."
    show monika zorder 2 at t31
    "Sayori smiles sweetly at Monika."
    show sayori zorder 3 at f33
    s "Alright, everybody!"
    s "Is everyone ready to share their poems?"
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
    show yuri 2pa zorder 3 at f31
    y "Something is wrong with what you just said."
    y "And I can't help but feel we've done this before..."
    y "But this time, it feels different."
    show yuri zorder 2 at t31
    if monika_type == 0:
        show monika 1a zorder 3 at f33
        m "Ahaha, there's really nothing wrong."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1ha zorder 3 at f33
        m "I think you're overthinking it a little, Yuri."
    else:
        show monika 1c zorder 3 at f33
        m "Yuri, there's nothing wrong."
    m "You're probably just imagining it."
    show sayori zorder 3 at f32
    show monika zorder 2 at t33
    s "Um..."
    s "What did I say?"
    show yuri zorder 3 at f31
    show sayori zorder 2 at t32
    y "You deviated from your usual catchphrase when addressing the club."
    y "It's not important but I thought I'd point it out."
    show yuri zorder 2 at t31
    show sayori zorder 3 at f32
    s "Oh...I guess I did say it differently."
    s "Ehehe, I guess it's because Natsuki isn't here."
    s "Sorry!"
    show yuri zorder 3 at f31
    show sayori zorder 2 at t32
    y "You said it normally before we shared poems..."
    show yuri zorder 2 at t31
    show sayori zorder 3 at f32
    s "Is it really that important Yuri?"
    s "It was just a simple mistake."
    show yuri zorder 3 at f31
    show sayori zorder 2 at t32
    y "Uu..."
    y "It's just that stagnating air is common foreshadowing that something terrible is about to happen..."
    show yuri zorder 2 at t31
    mc "Okay...this is weird."
    mc "I feel like we've said all of this before."
    show yuri zorder 3 at f31
    y "So I'm not the only one..."
    show yuri zorder 2 at t31
    show sayori zorder 3 at f32
    s "Guys, come on."
    s "We have a meeting to finish."
    show yuri zorder 3 at f31
    show sayori zorder 2 at t32
    y "R-Right..."
    y "I apologize for interrupting you, Sayori.."
    y "Please go on."
    show yuri zorder 2 at t31
    show sayori zorder 3 at f32
    s "As I was saying..."
    s "Why don't we all head home and decide what books we want to perform?"
    s "I know it's pretty early end to the meeting but [player] was late and I still have a lot of preparations I need to make."
    s "We should come up with a variety of stuff because it might be hard to find a book that everyone likes..."
    s "...or that's actually reasonable to perform."
    show sayori zorder 2 at t32
    if monika_type == 0:
        show monika zorder 3 at f33
        m "We should probably assign some tasks to help you with your preparation, Sayori."
        m "After all, it wouldn't be fair if you did everything by yourself."
    elif monika_type == 1 and ch12_markov_agree:
        show monika zorder 3 at f33
        m "Maybe we should assign tasks to help with the preparation."
        m "It would make it easier for you, Sayori."
    else:
        show monika zorder 3 at f33
        m "It could be a good idea to split the workload."
        m "That way, everything will be done quicker."
    show sayori zorder 3 at f32
    show monika zorder 2 at t33
    s "T-That's not necessary, Monika."
    s "I can handle everything myself."
    show sayori zorder 2 at t32
    mc "I think Monika is right."
    mc "It wouldn't be fair if you had to organize everything for something the whole club is going to do."
    mc "I think splitting up the work is a great idea."
    show yuri zorder 3 at f31
    y "Me too."
    y "I want to help in any way that I can."
    y "After all, it was my idea so it would be wrong not to."
    show yuri zorder 2 at t31
    "Sayori thinks for a moment."
    show sayori zorder 3 at f32
    s "Alright, I guess you all have a good point."
    s "I wouldn't really mind doing all the work myself."
    s "I know I could do it but I appreciate you guys wanting to help me."
    show sayori zorder 2 at t32
    mc "Do you really think you can handle all of that?"
    mc "It would only be right to help you because of all the stuff we'd need to do."
    show sayori zorder 3 at f32
    s "Speaking of which..."
    s "What do we need to do?"
    s "Monika said it would be a good idea to split off the work so what does everyone want to do?"
    show yuri zorder 3 at f31
    show sayori zorder 2 at t32
    y "I thought you would be the one telling us what to do..."
    show yuri zorder 2 at t31
    show sayori zorder 3 at f32
    s "Huh?"
    s "You guys are my friends but I don't know you all {i}that{/i} well."
    s "Ehehe, I'd like to though!"
    show sayori zorder 2 at t32
    if monika_type == 0:
        show monika zorder 3 at f33
        m "I think I could help here."
        m "It's obvious that we should have some food for the occassion."
        m "Aside from small snacks, we could get Natsuki to bake something for us."
    elif monika_type == 1 and ch12_markov_agree:
        show monika zorder 3 at f33
        m "I know what everyone could do."
        m "We all have different types of talents, don't we?"
        m "Natsuki, for example, could bake us some cupcakes for the day."
    else:
        show monika zorder 3 at f33
        m "Well, I know a couple of things that we could do."
        m "I'm not really sure on the details but we all have different things we're most suited for."
        m "Natsuki could prepare some food for us as an example."
    show yuri zorder 3 at f31
    show monika zorder 2 at t33
    y "Well...what could I do then?"
    y "I..."
    y "I'm useless..."
    show yuri zorder 2 at t31
    if monika_type == 0:
        show monika zorder 3 at f33
        m "N-No!"
        m "That's not it at all!"
        m "You're the most talented person here--"
        "Monika prevents herself from finishing."
        "I feel like I've heard all of this before..."
        m "Ah..."
        m "Yuri, I was going to say you have beautiful handwriting."
        m "Maybe you could make some banners about the Literature Club to set the atmosphere."
        m "I know you'll do a great job!"
    elif monika_type == 1:
        show monika zorder 3 at f33
        m "Ahaha, it's not like that Yuri."
        m "You definitely have some talents that we could use to help the preparations."
        m "For example, your handwriting is really beautiful."
        m "Every time I read one of your poems I'm in awe at how good it is!"
        m "You could make some banners for the club to set the atmosphere."
        m "I'm sure they'll end up great!"
    else:
        show monika zorder 3 at f33
        m "Maybe not."
        m "I'm sure we can find {i}something{/i} for you to do."
        m "Hmm..."
        m "Your poems have really beatiful handwriting."
        m "Maybe you could use that to make something for the club."
        m "Maybe some banners or something to help set the atmosphere."
    show yuri zorder 3 at f31
    show monika zorder 2 at t33
    y "Atmosphere...?"
    y "Um, about that..."
    y "I..."
    y 2pr "I love atmosphere!"
    show yuri 2pl
    "Yuri's expression suddenly changes as she stares at her desk in focus and starts nodding to herself."
    show yuri zorder 2 at t33
    mc "Your mind is already racing, I see..."
    "Has this all happened before?"
    "I definitely remember Yuri saying that..."
    "And me saying that too."
    show sayori zorder 3 at f32
    s "Yeah, that's great!"
    s "I'm sure you'll do awesome, Yuri!"
    s "I'll handle all the background stuff."
    s "Like getting a decent space and signing up our club for the event."
    s "After all, I am the president."
    show sayori zorder 2 at t32
    if monika_type == 0:
        show monika zorder 3 at f33
        m "Hmm..."
        m "What should I do then?"
    elif monika_type == 1:
        show monika zorder 3 at f33
        m "Okay...then what should I do?"
    else:
        show monika zorder 3 at f33
        m "What does that leave me to do?"
    show monika zorder 2 at t33
    mc "I've got an idea for what you could do."
    mc "You don't have to do it but..."
    show monika zorder 3 at f33
    m "What is it?"
    show monika zorder 2 at t33
    mc "Well, since you've been practicing piano..."
    mc "Maybe you could play something for the festival."
    show sayori zorder 3 at f32
    s "F-Festival...?"
    s "What are you talking about, [player]?"
    show sayori zorder 2 at t32
    mc "Ah..."
    mc "I meant Inauguration Day."
    mc "I don't know where festival came from."
    mc "Still, maybe it would be good to get Monika to play some piano."
    mc "During the intermissions or something."
    mc "Maybe she could even record some pieces to play {i}during{/i} the play."
    show sayori zorder 3 at f32
    s "[player]..."
    s "I think that's a great idea!"
    s "I could even organize to get a grand piano for you or something!"
    s "What do you think, Monika?"
    show sayori zorder 2 at t32
    if monika_type == 0:
        show monika zorder 3 at f33
        m "I..."
        m "I don't really know if I'm good enough for that kinda thing."
        m "It's true I've been practicing for a while but..."
        m "I don't know if the play is the right time."
    elif monika_type == 1 and ch12_markov_agree:
        show monika zorder 3 at f33
        m "Ah..."
        m "Is it really a good idea for me to play?"
        m "If you all think I'm good enough to do that, then I'll consider it."
        m "I'm just not sure that it's the right time."
    else:
        show monika zorder 3 at f33
        m "Playing the piano for the day?"
        m "Hmm..."
        m "Not that I mind doing it because I could definitely do it."
        m "I'm just not sure it's the right time for me."
    m "I guess I have to do something though..."
    "Monika looks at all of us one by one."
    m "Okay, I'll do it."
    show sayori zorder 3 at f32
    show monika zorder 2 at t33
    s "Yaaaaaaaay!"
    s "Now we all have something to do."
    s "I'll be sure to let Natsuki know what she has to do."
    show yuri zorder 3 at f31
    show sayori zorder 2 at t32
    y "I think you're forgetting someone, Sayori."
    show yuri zorder 2 at t31
    mc "Yeah...I don't have any preparation I can do."
    mc "Maybe I could--"
    show sayori zorder 3 at f32
    s "Well, you could help one of us!"
    s "I'm sure any of us would appreciate your help!"
    show sayori zorder 2 at t32
    mc "Are you sure it wouldn't be better if I did something else?"
    mc "There might be some other preparations that we haven't covered yet."
    show sayori zorder 3 at f32
    s "If there is, I'll be handling it."
    s "So really, if you want to do that then you'll have have to help me."
    s "Ehehe, not like you have to though."
    s "You should choose whoever you think needs the most help."
    show sayori zorder 2 at t32
    if visited_yuri_hospital:
        "I would like to spend more time with Yuri..."
        "So it's only the right choice I'd choose her."
        mc "I already know who I'm going to help."
        mc "It's Yuri."
        mc "We're kind of dating so..."
        "There's a silence in the room as I say that."
        "No one says anything for a while, as if they're trying to comprehend what I just said."
        mc "After I visited her at the hospital, it became pretty obvious that she was important to me."
        show yuri zorder 3 at f31
        y "Ah...I wasn't expecting you to say it so suddenly."
        y "But he's right..."
        show yuri zorder 2 at t31
        show sayori zorder 3 at f32
        s "Well, you should think about what's right for the club."
        s "Dating or not, you should think about who you should help."
        s "If you think that Yuri needs your help the most, then feel free to help her."
        s "But if you think that someone else needs your help more..."
        s "Well, it's up to you."
        show yuri zorder 3 at f31
        show sayori zorder 2 at t32
        y "Sayori has a point, [player]."
        y "It would be unfair if you're helping me just because of that."
        y "The others might need your help too."
        y "So you should decide what's best for the club."
        show yuri zorder 2 at t31
        mc "Alright, I get it."
    else:
        show yuri zorder 3 at f31
        y "I could use some help..."
        y "I'm good at creating an atmosphere but another perspective might help too."
        y "There's definitely a lot of things you could help me with."
        "Sayori looks at Yuri quizzically."
        y "But...you should decide for yourself."
        y "A-After all, you probably think someone else needs more help."
        show yuri zorder 2 at t31
        show sayori zorder 3 at f32
        s "That's not true..."
        s "All of us need some help but we can also all do it by ourselves."
        s "It's just up to [player] to decide who he really thinks could use his help for Inauguration Day."
        show sayori zorder 2 at t32
        mc "Alright..."
    if monika_type == 0:
        show monika zorder 3 at f33
        m "I could use your help, too."
        m "I don't really know what kind of songs I could play on the day."
        m "Plus I could use a sort of audience to practice to."
        m "Maybe you could help me, if you want."
        m "But..."
        m "Like they said, the choice is yours."
        m "I'm not going to be upset or anything if you decide to help someone else."
        m "Even if I enjoy your company you have to think of the bigger picture..."
        m "...After all, this whole thing is for the club."
    elif monika_type == 1 and ch12_markov_agree:
        show monika zorder 3 at f33
        m "Hmm..."
        m "Maybe [player] could help me."
        m "If I'm going to play the piano on the day, I could use an audience to practice to."
        m "He could also help with choosing the songs I could play."
        m "Ahaha, it could be fun."
        m "However, I'm not going to force you."
        m "You should go because you think I need the help not because you want to hang out with me..."
        m "But I certainly wouldn't mind if that was the reason~"
    else:
        show monika zorder 3 at f33
        m "[player] could be useful helping me."
        m "There might be some songs he wants to hear on the day that I could play for him."
        m "It also helps if I practice in front of an audience so I can get some instant feedback after I play."
        m "But it's up to him, of course."
    show sayori zorder 3 at f32
    show monika zorder 2 at t33
    s "You know it kinda sounds like everyone is trying to convince you to help them."
    s "Ehehe, maybe I should tell you what I'm doing too."
    show sayori zorder 2 at t32
    mc "I'd like to know that before I make a decision."
    show sayori zorder 3 at f32
    s "Well, I was gonna handle all the background preparations."
    s "You know, getting our club registered for Inauguration Day and organising a space we could use."
    s "I was also gonna make us the script of the book we chose, like I've done before."
    s "And then I was gonna help out everyone else a little bit, to make their parts really good!"
    s "Not that I don't trust them to make it great already..."
    s "I just thought I could add some...flare."
    s "Like getting a grand piano arranged for Monika or getting an experienced baker to help Natsuki design awesome cupcakes!"
    show sayori zorder 2 at t32
    mc "That sounds like a lot of work..."
    mc "It would almost be wrong {i}not{/i} to hel you."
    show sayori zorder 3 at f32
    s "[player], you really don't have to."
    s "I can handle myself fine."
    if sayori_confess and not sayori_dumped:
        s "I was just offering in case you reaaaaaally wanted to spend time with your girlfriend..."
    else:
        s "I was just offering in case you reaaaaaally wanted to spend time with me or something..."
    show sayori zorder 2 at t32
    mc "S-Sayori...!"
    show sayori zorder 3 at f32
    s "Ehehe~"
    s "Like everyone else said though..."
    s "It's up to you."
    s "I'll still be able to do everything I said I would with or without your help."
    show sayori zorder 2 at t32
    if monika_type == 0:
        show monika zorder 3 at f33
        m "That really does sound like a lot of work, Sayori."
        m "Are you sure you can handle all of that if [player] doesn't choose to help you?"
    elif monika_type == 1 and ch12_markov_agree:
        show monika zorder 3 at f33
        m "Ahaha, wow..."
        m "That sure is a lot of work you've set for yourself."
    else:
        show monika zorder 3 at f33
        m "Are you sure you aren't overloading yourself, Sayori?"
        m "That seems like a lot to do."
    show sayori zorder 3 at f32
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
    show sayori zorder 3 at f32
    s "Alright, everybody!"
    s "That's definitely the end of our meeting today..."
    s "Unless any of you guys want to say something...?"
    if monika_type == 0:
        show monika zorder 3 at f33
        m "Actually, I would like to say something."
        m "It's kind of important."
    elif monika_type == 1 and ch12_markov_agree:
        show monika zorder 3 at f33
    else:
        show monika zorder 3 at f33
        m "There's nothing else to say."
        m "I think the meeting is as good as over."
    show sayori zorder 3 at f32
    s "If that's all..."
    s "...Then I'll see you all tomorrow!"
    return

label ch13_end_natsuki:
    $ ch13_scene = "natsuki"
    mc "I should probably help Natsuki."
    mc "With what she's been dealing with, I know she could probably use some help."
    mc "Or at least a visit from me."
    show sayori zorder 3 at f32
    s "I'm sure she wouldn't mind your company, [player]!"
    s "With what she has to deal with, I also think she'd appreciate your help."
    show yuri zorder 3 at f31
    show sayori zorder 2 at t32
    y "Ah, I see."
    y "I'll get the atmosphere done by myself then."
    show yuri zorder 2 at t31
    show sayori zorder 3 at f32
    s "Yuri, you sound kinda upset."
    s "Is something wrong?"
    show yuri zorder 3 at f31
    show sayori zorder 2 at t32
    y "Oh, it's nothing..."
    show yuri zorder 2 at t31
    show sayori zorder 3 at f32
    s "It doesn't look like nothing."
    show yuri zorder 3 at f31
    show sayori zorder 2 at t32
    if visited_yuri_hospital:
        y "Well, it's not a big deal."
        y "I just wanted to spend the preparation time with [player]."
        y "I understand he can make his own decisions..."
        y "So I'm not really that upset."
        y "I know he only wants what's best for the club after all."
        y "And..."
        "Yuri looks at me."
        y "I trust he knows what he's doing."
    else:
        y "I-It's really nothing..."
        y "Just forget I even said anything."
        y "Besides, he made his decision."
        y "It's not like I can change his mind anyway..."
        y "Um..."
        y "Did I say that out loud...?"
        y "D-Don't mind me."
    show yuri zorder 2 at t31
    show sayori zorder 3 at f32
    s "Alright, Yuri..."
    s "Whatever you say."
    show sayori zorder 2 at t32
    return

label ch13_end_yuri:
    $ ch13_scene = "yuri"
    mc "I think I should help Yuri with her preparations."
    mc "She won't be able to create the perfect atmosphere without some help."
    mc "So I think it's just the logical thing to do."
    show yuri zorder 3 at f31
    if visited_yuri_hospital:
        y "A-Are you sure about this, [player]?"
        y "Just because we're dating doesn't mean you have to--"
    else:
        y "M-Me?"
        y "N-Not that I don't want you to help me but are you sure?"
        y "You probably feel sorry for me and if that's the case then--"
    show yuri zorder 2 at t31
    show sayori zorder 3 at f32
    s "Ehehe, Yuri you need to calm down a little!"
    s "I really think he just knows you need the most help."
    s "Besides, it's everyone's responsibility to make sure that this event ends up amazing!"
    show sayori zorder 2 at t32
    mc "Sayori is right."
    mc "I think that if I help you make the atmosphere then we can really do something for the club."
    mc "Something that stands out and will make people want to join."
    show yuri zorder 3 at f31
    y "D-Do you really think we can do that?"
    show yuri zorder 2 at t31
    if ch4_name == "Yuri":
        mc "We've done it before, haven't we?"
        mc "I'm sure we can do it again."
    else:
        mc "I'm definitely sure we can do it."
        mc "I just hope that I can really help."
    show yuri zorder 3 at f31
    y "Thank you, [player]."
    y "I appreciate your kind words."
    show yuri zorder 2 at t31
    return

label ch13_end_monika:
    $ ch13_scene = "monika"
    mc "Well..."
    mc "I guess I should be helping Monika with her preparations."
    mc "Everyone else seems to have their own parts covered."
    mc "So I think helping Monika with whatever is the most appropriate thing for me to do."
    if monika_type == 0:
        show monika zorder 3 at f33
        m "Thanks [player]~"
        m "I'm sure I could really use your help."
        m "And maybe I can tell you more about that conversation we had earlier..."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1ha zorder 3 at f33
        m "Ah, thank you."
        m "I really appreciate you choosing to help me [player]~"
        m "Maybe I'll even tell you more about the poem I wrote..."
    else:
        show monika 1a zorder 3 at f33
        m "You're really going to help me?"
        m "Ahaha, I'm flattered."
        m "Thanks [player]."
    show sayori zorder 3 at f32
    show monika zorder 2 at t33
    s "I really hope you two are gonna do your best!"
    s "I can't wait to see hear Monika play."
    s "And with [player] helping her, then it's definitely gonna be great!"
    show yuri zorder 3 at f31
    show sayori zorder 2 at t32
    if visited_yuri_hospital:
        y "Ah, I thought Monika would need the most help out of all of us."
        y "But it is your decision after all, [player]."
        y "I trust you know what you're doing."
        y "We can always talk more later."
        y "Besides, I can handle the atmosphere myself."
    else:
        y "A-Are you kidding?"
        y "Monika needs the least--"
        "Yuri stops herself."
        y "I mean..."
        y "It is your decision..."
        y "I suppose I'll have to do the atmosphere myself."
    show yuri zorder 2 at t31
    mc "Yeah..."
    return

label ch13_end_sayori:
    $ ch13_scene = "sayori"
    mc "I guess I'd be most helpful helping Sayori."
    mc "It sounds like she's got a lot to do."
    mc "And I really want to make this event we're doing the best."
    show sayori zorder 3 at f32
    s "Really?"
    s "Thanks [player]~"
    s "I guess I can split off some of the workload to you."
    s "That way I can make my parts really good!"
    s "And you..."
    s "Ehehe, well..."
    show sayori zorder 2 at t32
    mc "Are you saying I can't do as well as you?"
    mc "That almost sounds like a challenge."
    show sayori zorder 3 at f32
    s "Take it however you want~"
    "Sayori smiles mischievously."
    s "I'm only kidding."
    s "I really do appreciate you helping me, [player]."
    if sayori_confess and not sayori_dumped:
        s "I just hope you're doing it not because we're a couple but because you actually think I could use the help."
    else:
        s "I just hope you thought about this carefully."
    show sayori zorder 2 at t32
    mc "I did and I want to help you."
    show yuri zorder 3 at f31
    if visited_yuri_hospital:
        y "I suppose it's only fair."
        y "I did assess that Sayori had the most work to do."
        y "Besides...[player] and I can always talk in our own time."
        y "It's not like this preparation is going to take all our spare time."
        y "I'm sure with your help, Sayori will actually be able to do what she's set out to."
    else:
        y "Y-You chose to help Sayori?!"
        "Yuri gives Sayori a look."
        y "I...suppose it makes the most sense."
        y "She does have the most do..."
        y "Maybe you {i}are{/i} just doing what's best for the club..."
        y "Despite what you said, it's not like you can actually handle all that work by yourself, Sayori."
    show yuri zorder 2 at t31
    show sayori zorder 3 at f32
    s "You'd be surprised, Yuri."
    s "I can do a lot of things you don't think I could."
    show yuri zorder 3 at f31
    show sayori zorder 2 at t32
    y "Ah...of course."
    y "I didn't mean that as an insult or anything."
    y "It's just your workload is...a lot."
    y "Even for two people."
    show yuri zorder 2 at t31
    show sayori zorder 3 at f32
    s "We'll be fine, I promise!"
    show sayori zorder 2 at t32
    if monika_type == 0:
        show monika zorder 3 at f33
        m "Just make sure you don't hurt yourself doing too much."
        m "Knowing you, you probably have a lot more stuff planned..."
    elif monika_type == 1 and ch12_markov_agree:
        show monika zorder 3 at f33
        m "Be careful not to waste all your energy, Sayori."
        m "That could be really bad for when the day comes."
    else:
        show monika zorder 3 at f33
        m "Whatever you say..."
        m "Just don't waste all your energy, Sayori."
    show sayori zorder 3 at f32
    show monika zorder 2 at t33
    s "Yeah, yeah..."
    return
