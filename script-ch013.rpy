label ch13_main:
    scene black
    show sayori 1a zorder 2 at t11
    with dissolve_scene_full
    play music mend fadeout 2.0
    s "So..."
    s "About Natsuki..."
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
    if ch12_markov_agree and monika_type == 1:
        show monika 1ha zorder 2 at t11
        m "Hi [player]~"
        "It's Monika."
        "Something seems different about her appearance."
        m "What took you so long to get here?"
        mc "Ah...I guess I just lost track of time."
        m 3hb "Well, it's not really a problem."
        m "Sayori just thought it would be better if we start with four members instead of three."
        mc "Four members? What do you mean?"
        m 1hc "Oh, you didn't know?"
        m "Natsuki stayed at home today because of what happened yesterday."
        m 1he "I think she needs some time for herself."
        mc "I see."
    return

label ch13_end:
    return
