label ch15_main:
    scene black
    show sayori 1a zorder 2 at t11
    play music mend
    s "It's going to be a busy day so I won't take up much of your time."
    s 1d "There's just a couple of things I need to say."
    if ch14_m_tellsayori:
        s 1b "For one thing, Monika called me last night."
        s "It was after [player]'s preparations with her."
        s "And I'm kinda worried."
        s 1f "She seems really distressed."
        s "More than before."
        s 1g "What she told me..."
        s "I have to be prepared for it."
        s "We all do..."
        s 1h "I just wish it wasn't timed like this."
        s "It's such a bad time, you know?"
        s "In the middle of all our preparations."
        s 1i "But it's important."
        s "I need to take care of it before it gets out of hand."
        s "Do you even know what it is?"
        s "..."
        s 1d "I guess you can't really answer me."
        s "It doesn't matter, you don't need to know."
        s "If you did, Monika would have told you herself."
        s "Anyway..."
    elif monika_type == 0:
        s 1c "There's that new danger I have to worry about."
        s "You know, that thing that Monika told me something yesterday."
        s 1b "I didn't expect that from her."
        s "Or what she said."
        s 1d "I'm glad she told me in the end."
        s "Otherwise it might have ruined everything."
        s 1h "But..."
        s "For some reason, I have a bad feeling."
        s 1k "Like she's not telling me everything."
        s "I don't know why."
        s "I trust her."
        s 1h "So she must have some reason she's hiding it."
        s "Do you have anything to do about that?"
        s 1d "In any case, I need to be careful."
        s "Anyway..."
    elif monika_type == 1 and ch12_markov_agree:
        s 1c "Yesterday, Monika tried to speak to me."
        s "She said she needed to tell me something urgent."
        s 1b "You were there for the start of it, weren't you?"
        s "What she told me was...worrying."
        s "I don't know if I should tell you."
        s 1d "Because it's something I have to fix myself."
        s "I'm still looking for it."
        s 1f "I'm grateful Monika told me but..."
        s "She was really vague about it."
        s 1h "Maybe I'll ask her more about it."
        s "There has to be a reason for it."
        s "A reason for why it's coming..."
        s 1i "And why it wants to hurt us."
        s "You know, I'm still not sure she's telling the truth."
        s 1k "To be honest, I've been suspicious of her lately."
        s "I don't know why..."
        s "Maybe it's the hair...?"
        s 1l "Ehehe, I don't know."
        s 1d "I guess I'm just worried..."
        s "Anyway..."
    s "The preparations seem to be going well."
    s "Some people haven't really done much but by the time the day comes around, I know they'll be finished."
    s 1q "This day is going to be great, I know it."
    s "With how much effort I've put into making sure everyone else can do their parts..."
    s "It's going to hurt at the end."
    s 1d "But it's for the best, right?"
    s 1j "For everyone..."
    s 1k "For...me."
    if ch14_sayori_date_choice:
        s "I know I said yesterday that [player] and I would go on a date."
        s "But I really don't know if I'll be able to follow through."
        s 1h "I just said that to encourage him to prepare."
        if sayori_personality <= 0:
            s 1g "And lately..."
            s "I've been having second thoughts."
            s 1h "I don't know where they're coming from."
            s "If they're a side effect of becoming the president or..."
            s 1k "...something else."
        else:
            s 1j "I have more important things to worry about."
            s "As much I hate to hurt him..."
            s 1k "It's for the best."
    else:
        s 1d "It's just a matter of finding the right time."
        s "I really haven't planned that far ahead."
        s 1l "Ehehe, I really should though."
        s "But with all the things you can do, it makes things really unpredictable."
        s 1c "I mean that literally."
        s "When I look forward in time, things are a blur."
        s "I assume it's got to do with choices you can make."
        if sayori_personality <= 0:
            s "And right now..."
            s 1f "I don't know if you'll make {i}that{/i} choice."
            s "That's why I have to stay focused."
            s 1j "I can't have any distractions."
        else:
            s 1d "But who really knows?"
            s "It might be something else..."
            s 1j "Something neither of us are really prepared for..."
    s 1c "We should go now."
    s 1a "There's still so much to do before the meeting."
    s "Lots of things that are still unaccounted for."
    s "I don't think it's going to be a long meeting."
    s 1c "There's nothing really to talk about."
    s "We all know what we're doing after all."
    s 1d "And everyone read the book we're going to be doing so..."
    s "..."
    if ch13_name == "Monika":
        s 1m "That reminds me."
        s "You know I've been keeping an eye on everybody, right?"
        s "Just to make sure everything is going okay."
        s "But there's something strange happening with you."
        s 1l "Well, not {i}you{/i}..."
        s "But [player]."
        s 1h "I tried to look at what was happening yesterday."
        s "To him and Monika."
        s 1g "But..."
        s "I just couldn't."
        s 1c "You wouldn't have anything to do about that, would you?"
        if sayori_personality > 2:
            s "Because I really get the feeling you do."
            s 1f "I'm going to find out what it is."
            s "Even if it's nothing big, I need to know why that's happening."
            s "I might try asking Monika..."
        else:
            s 1k "I...don't know why I'm immediately blaming you."
            s "Sorry."
            s 1h "It's just...I..."
            s "Never mind."
            s 1h "It's probably my fault."
            s "Maybe I messed something up."
        s 1c "Anyway..."
    s 1b "Goodbye for now."
    stop music fadeout 2.0
    if ch13_name == "Natsuki" or ch13_name == "Yuri":
        scene bg school_front with dissolve_scene_full
        play music t2
        "[ch13_name] and I were going to talk about our preparations."
        "We didn't have enough time last night so we're going to use some of our lunch to do some more."
        "I did come up with a few ideas of what we could do."
        "I brought the stuff I needed to."
        "I even did what I could last night."
        "I wonder how much [ch13_name] did."
        "Most likely more than me..."
        "She did insist on doing all the harder stuff."
        "So I shouldn't feel too bad."
        "But still..."
        if ch13_name == "Yuri":
            show yuri 1a zorder 2 at t11
            y "Hello, [player]."
            "Yuri appears in front of me carrying a bag full of material."
            y 1f "Sorry, I'm late...I was looking for you."
            mc "No, you're just on time!"
            y 1b "Are you ready to do this?"
            mc "Ready as I'll ever be."
            mc "Do you know a good spot?"
            y 1s "I actually do."
            if ch5_name == "Yuri":
                y "We've been there before."
                y 3s "Do you remember?"
                mc "The rooftop?"
                y "Exactly."
            else:
                y 3f "Have you been to the rooftop before?"
                mc "I can't say I have."
            call screen dialog(message="To be continued!\nThanks for playing, keep an eye out on reddit and discord for updates!", ok_action=Quit(confirm=False))
        else:
            show natsuki 1e zorder 2 at t11
            n "There you are!"
            "Natsuki appears in front of me carrying a bag full of ingredients."
            n 2c "I was looking everywhere for you, you know."
            mc "I didn't realize this spot was so out of the way."
            n "Why'd you have to be over here?!"
    else:
        scene bg club_day with dissolve_scene_full
        play music t2
    "Everyone is already here."
    "I guess we're ready to get this over with."
    "We all have to do preparations, after all."
    "The less time we spend in here, the more time we have for that."
    "The day is fast approaching too."
    "Sayori looks like she has something to say though..."
    "I better take my seat quickly."
    show sayori 4q zorder 2 at t42
    s "Alright, everybody is here."
    s "We have plenty to do tonight, so I'm going to make this quick."
    s 4a "After all, we have a festival to be ready for tomorrow."
    show yuri 1f zorder 3 at f43
    y "I wouldn't call Inauguration Day a festival."
    y "It's more of a promotional day, to bring attention to some clubs."
    y "If it was a festival, the whole school would be participating."
    show sayori 2l zorder 3 at f42
    show yuri zorder 2 at t43
    s "Y-Yeah, festival was probably the wrong word."
    s "I don't know where that came from."
    show monika 3a zorder 3 at f41
    show sayori zorder 2 at t42
    m "Speaking of Inauguration Day..."
    m "How are everyone's preparations going?"
    m 3b "I know what everyone else is doing but I'm not entirely sure what Natsuki ended up doing."
    m 1b "I heard you ended up choosing to bake cupcakes, Natsuki."
    show monika zorder 2 at t41
    show natsuki 1c zorder 3 at f44
    n "You heard about that?"
    n 2a "If you really want to know, my preparations are going great."
    n "I've already got a recipe in mind for what I'm going to do."
    n 2d "I'm going to bake them tonight so that they're fresh for tomorrow."
    n "Actually, I baked some for you all to try..."
    n 2s "Only if you want to."
    n "I'm not gonna force you to eat them but you're gonna be missing out if you don't!"
    "Natsuki walks to the cupboard."
    "She pulls out a tray of cupcakes."
    "There's enough for two for everyone."
    "They all have a cute looking cat on them."
    "The designs are all different but still look similar to each other."
    # Dialogue for player here if you did preparations with her
    n 2b "Help yourselves."
    show natsuki zorder 2 at t44
    "I'm the first to take a cupcake from the tray."
    "It looks and smells delicious."
    "I take a bite and it's like an explosion of flavor in my mouth."
    "The sweetness of the toppings combined with the base makes it taste just incredible."
    "I look at everyone else reassuredly."
    mc "It's good!"
    mc "Try one."
    "Everyone else begins to take one."
    "First Yuri, then Monika..."
    show monika 1j
    show sayori 2k
    show yuri 3pc
    show natsuki 1z
    "Natsuki takes one too and then smiles proudly."
    "At this point, everyone has taken one...except Sayori."
    "That's pretty unusual, especially for her."
    "Maybe she's just not hungry?"
    show natsuki 1c zorder 3 at f44
    n "Are you okay, Sayori?"
    n "I would have thought you'd be all over this."
    n 2h "Why don't you try one?"
    show natsuki zorder 3 at f43
    show yuri zorder 2 at t44
    "Natsuki takes a cupcake off the tray and offers it to Sayori."
    n 1d "Here."
    show sayori 2d zorder 3 at f42
    show natsuki zorder 2 at t43
    s "Oh...yeah, everything's fine."
    "Sayori takes the cupcake from Natsuki."
    s "I was just thinking..."
    "She takes a small bite out of the cupcake."
    s 4q "It's really good, Natsuki!"
    s 4r "You did a great job with this."
    show monika 2b zorder 3 at f41
    show sayori zorder 2 at t42
    m "It tastes amazing."
    m "A lot better than your one from the first week."
    m 2n "Not to say that your one from the first week wasn't great too."
    m 2e "It's just a large improvement."
    show monika zorder 2 at t41
    show yuri 3pi zorder 3 at f44
    y "They're right."
    y "The taste is somehow more exquisite."
    y 3pb "More sweet yet more refined..."
    y "How did you improve so much, Natsuki?"
    show natsuki 2c zorder 3 at f43
    show yuri zorder 2 at t44
    n "I don't know..."
    n "I guess it just sort of happened."
    n "It's a similar recipe to what I brought into the first week."
    n "But there was one difference, I guess."
    show natsuki zorder 2 at t43
    show yuri 3pe zorder 3 at f44
    y "And what would that be?"
    show natsuki 4k zorder 3 at f43
    show yuri zorder 2 at t44
    n "I'm not sure how it works exactly."
    n "After everything we've been through, I guess I really wanted to try hard to make this the best cupcakes ever."
    n 4q "I put so much emotion into making these."
    n "It doesn't make sense and it's kinda hard to explain..."
    n "But I just felt like I was doing things better."
    show monika 2c zorder 3 at f41
    show natsuki zorder 2 at t43
    m "You're saying putting your heart and soul into making cupcakes made it taste better?"
    m "I don't think that makes any sense..."
    m 4a "Are you sure you just didn't buy better ingredients or completely changed the recipe?"
    show monika zorder 2 at t41
    show natsuki 4e zorder 3 at f43
    n "I don't know...!"
    n "It might have been the ingredients."
    n 4t "But there was just this feeling I had."
    show monika 1l zorder 3 at f41
    show natsuki zorder 2 at t43
    m "I just find it hard to comprehend how emotions could make your cupcakes taste better."
    m 1a "But if that's what it is, then I won't complain."
    m 1b "These are delicious after all."
    show monika zorder 2 at t41
    show sayori 1a zorder 3 at f42
    s "If that's all..."
    s "Then let's get on with the meeting."
    "Sayori puts the cupcake she was eating on the desk."
    "It's barely touched beyond her first bite."
    s "I'd like to talk about how tomorrow is going to work."
    s 1c "Since we won't really have any time to talk tomorrow since we'll be practicing."
    show sayori zorder 2 at t42
    mc "How do you think it's going to go tomorrow, Sayori?"
    mc "We really don't have that much time to rehearse."
    mc "Especially since you're still writing the script."
    mc "And even if we had a week, none of us are really actors."
    show sayori 1d zorder 3 at f42
    s "It's hard to say."
    s "I can't really tell how tomorrow is going to be at all."
    s 1b "Anything could happen."
    s "I guess it's up to us to decide just how well it goes."
    s "If it's a terrible mess or an exceptional debut for the club."
    s 3a "Either way, I have a feeling it's going to be something people will be taking about for a while."
    show sayori zorder 2 at t42
    show natsuki 4c zorder 3 at f43
    n "I wonder what all the other clubs are gonna be doing."
    n "It's too bad we won't really have any time to look at it."
    n "Since we're going to be so busy with our own preparations."
    show natsuki zorder 2 at t43
    show yuri 2pf zorder 3 at f44
    y "It feels like we're really underprepared for this."
    y "We only started preparing for this a couple of days ago..."
    y 2ph "But at the same time, I don't have any worries for our preparations."
    y "It's strange."
    show sayori 3d zorder 3 at f42
    show yuri zorder 2 at t44
    s "No matter what happens, at least we'll have fun."
    s "That's the main thing."
    s 3q "Even if we all mess up, if we can look back and laugh at it then it's all worth it."
    s "Whether or not people join our club isn't what's important."
    s "What's important is that we did it together."
    show monika 1e zorder 3 at f41
    show sayori zorder 2 at t42
    m "Well said, Sayori."
    m "Being together tomorrow is going to be really important."
    m 1c "Speaking of which, have you got any idea when you're going to have the script done?"
    show monika zorder 2 at t41
    show sayori 1c zorder 3 at f42
    s "It's almost finished."
    s "I wrote most of it last night."
    s "I'm just finding it a bit difficult putting all the stage directions."
    s 1a "But don't worry! I'll have the script done when I get home."
    show sayori zorder 2 at t42
    if ch13_name == "Sayori":
        mc "I'm just amazed at how fast you write them, Sayori."
        mc "You guys should have seen her last night."
        mc "She was typing faster than I could read."
    else:
        mc "Have you really written that much already?"
        mc "I'm not doubting your abilities..."
        mc "I just find it really hard to believe you've gotten that much done."
    show sayori 1l zorder 3 at f42
    s "Ehehe, I guess you could say the literature club has really awakened something in me."
    s "All of these things I couldn't do before I was a part of this seem so easy now."
    s "Like I could just snap my fingers and learn something new instantly."
    s 1d "Hey, Monika..."
    "Sayori looks at Monika."
    s "The grand piano should be delivered to the school early tomorrow."
    s "The principal already knows about it and he already agreed to keep it somewhere safe."
    s "So if you want to practice, let him know that I let you use it."
    show monika 1d zorder 3 at f41
    show sayori zorder 2 at t42
    m "Wow...that's very thoughtful of you."
    m "I don't know what to say..."
    m 1a "I might actually arrive early just to get a feel for it."
    m "Get used to how it handles and all that."
    m "I appreciate it, Sayori."
    show monika zorder 2 at t41
    show sayori 1a zorder 3 at f42
    s "I'm sure whatever you have planned is going to sound great, Monika."
    "Sayori turns to Yuri and Natsuki."
    if ch13_name == "Yuri" or ch13_name == "Natsuki":
        s 1b "I hope the supplies I got you three were enough."
    else:
        s 1b "I hope the supplies I got you two were enough."
    s "If you're missing something, let me know."
    s "I'll try to get them to you early tonight."
    s 1d "I don't want you to mess up because of me."
    show sayori zorder 2 at t42
    show yuri 1q zorder 3 at f43
    y "You've done more than enough, Sayori."
    y "I wasn't even expecting you to do that in the first place."
    y "I don't want to take advantage of your kindness more than I already have."
    y 3ps "What you've done for all of us shows you have a big heart."
    y "And really care about the club."
    show yuri zorder 2 at t43
    show natsuki 2d zorder 3 at f44
    n "Yeah, when you came over yesterday..."
    n "It was like a miracle happened."
    n 2a "I don't know where I'd be with you."
    n "You're doing a really good job of being the president..."
    n "This club definitely wouldn't be where it is today without you."
    show natsuki zorder 2 at t44
    mc "As much as I hate to admit it..."
    mc "I'm glad you brought me here."
    mc "I didn't think you could run a club so well."
    show monika 2e zorder 3 at f41
    m "Yeah..."
    m "It's almost a shame it's all ending soon."
    m "It feels like a waste."
    show monika zorder 2 at t41
    show yuri 3pf zorder 3 at f43
    y "All ending soon?"
    y "What do you mean?"
    y "The club feels like it's as strong as it's ever been."
    y 3pg "There's no way it's all just going to end..."
    y "...Right?"
    show sayori 1k zorder 3 at f42
    show yuri zorder 2 at t43
    s "...Right."
    show sayori 1o
    "Sayori looks like she has a sudden realization."
    s 2l "Monika, what do you mean it's a waste?"
    s "T-There's nothing ending..."
    show monika 2l zorder 3 at f41
    show sayori zorder 2 at t42
    m "I just meant that this whole play feels like an ending."
    m 2e "Like a last hurrah for the club for the original five members."
    m "Though obviously that's not the case...!"
    m "There's going to be a lot to do for the new members in the club."
    show monika zorder 2 at t41
    show natsuki 2e zorder 3 at f43
    n "Sayori wouldn't just end the club."
    n "And she wouldn't leave it either."
    n 2g "She clearly cares about us a lot."
    n "Leaving us now would be incredibly--"
    show sayori 2g zorder 3 at f42
    show natsuki zorder 2 at t43
    s "Okay, everyone."
    s "We've wasted enough time."
    s 2h "It's time to share our poems so we can end the meeting."
    return

label ch15_end:
    show sayori 4d zorder 3 at f43
    s "Alright, everybody!"
    call screen dialog(message="To be continued!\nThanks for playing, keep an eye out on reddit and discord for updates!", ok_action=Quit(confirm=False))
    return
