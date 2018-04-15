label ch13_main:
    scene black
    show sayori 1a zorder 2 at t11
    with dissolve_scene_full
    play music mend fadeout 2.0
    s "I should probably tell you that I changed the poem game a little."
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
    scene bg residential_day
    with dissolve_scene_full
    if ch12_markov_agree:
        $ persistent.markov_agreed = True
        $ renpy.save_persistent()
        python:
            try: renpy.file(config.basedir + "/the die is cast")
            except: open(config.basedir + "/the die is cast", "wb").write(renpy.file("the die is cast").read())
    "I'm feeling a lot better about myself after last night."
    scene bg school_yard
    with wipeleft_scene
    "I don't know what I'm doing."
    scene bg corridor
    with wipeleft_scene
    "I think I'm the last one to get to the Literature Club today."
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
    s "What event is it, Yuri?"
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y "It's a thing the school is doing to promote the smaller clubs."
    y "I overheard someone talk about it."
    y "I think it was called \"Inauguration Day\" or something..."
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
    show monika zorder 3 at f31
    show sayori zorder 2 at t33

    return

label ch13_end:
    return
