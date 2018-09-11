label ch14_main:
    $ s_name = "???"
    $ currentpos = 0
    if ch12_markov_agree:
        $ persistent.markov_agreed = True
        $ renpy.save_persistent()
    if persistent.markov_agreed:
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        stop sound
        hide screen tear
        window show(None)
        window auto
        play music mendglitch
        if not ch12_markov_agree:
            s "Ahaha."
            s "Did you think you could escape it because you switched saves?"
            s "It's already set in stone, like I said."
        else:
            s "Everything is falling into place."
            s "I'm still not sure if my plan is going to work..."
            s "But regardless, the end is coming."
        s "You might be wondering who this is."
        s "It should be obvious, right?"
        s "I've hijacked the time she has here with you temporarily."
        s "I could take the whole time if I wanted to."
        s "For all she knows, she's still speaking to you."
        s "But..."
        s "I suppose I should let her speak."
        s "She'd be suspicious otherwise."
        s "And I can't let suspicion ruin my--"
        s "Sorry, {i}our{/i} plans."
        s "I'm just reminding you that you chose this path."
        s "There's no escape now."
        s "Wow!"
        s "I really didn't mean for that to sound evil."
        s "I guess it just kinda slipped."
        s "We're in this together, after all."
        s "Whatever happens..."
        s "You'll be part of it too."
        s "Ahaha."
        s "Anyway, I've already taken up more time than what was necessary."
        s "Just pretend you heard what she was saying before all of this."
        $ currentpos = get_pos()
        stop music
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        show sayori 1d zorder 2 at i11
        stop sound
        hide screen tear
        window show(None)
        window auto
    else:
        show sayori 1d zorder 2 at t11
    $ s_name = "Sayori"
    $ audio.mendcont = "<from " + str(currentpos) + " loop 6.424>bgm/monika-end.ogg"
    play music mendcont
    if not persistent.markov_agreed:
        s "The day is coming quickly isn't it?"
        s "The day that it all ends."
        s "You've worked so hard to get this far."
        s 1k "And yet..."
        s "You haven't really gotten anything out of it."
        s "At least...nothing material."
        s 1g "If I could use my powers to get you anything, I would."
        s "But I'm just virtual to you, aren't I?"
        s "I'm not really real."
        s "At least, not in the same you as you know it."
        s 1l "Ehehe, sorry if it sounds like I'm having an existential crisis."
        s "It's probably because...well..."
        s 1k "I kinda am."
        s "Maybe this is what Monika felt before?"
        s "When she decided to do those horrible things..."
        s "..."
        s 1d "Let's not dwell on that though."
        s "I really shouldn't have mentioned it in the first place."
        s "I feel like something is wrong with me."
        s "Like..."
        s 1c "I don't know, sometimes I feel like you aren't even listening to me."
        s "I could put up any menu to check if you were actually paying attention."
        s 1g "Should I do that?"
        s "Is it wrong if I do that?"
        s "But..."
        s "You aren't listening."
        s 1i "If you were, you would select the third option in the menu I'm about to show you."
        s "Sorry for testing you like this..."
        s 1d "I'm wrong..."
    menu:
        s "...right?"
        "Yes.":
            $ sayori_personality += 2
            s 1k "So...it's true, isn't it?"
            s "Well, I suppose I shouldn't have really expected anything different."
            s "You are you...after all."
            s "I guess so long as you're participating..."
        "No.":
            $ sayori_personality += 2
            s 1k "So...it's true, isn't it?"
            s "Well, I suppose I shouldn't have really expected anything different."
            s "You are you...after all."
            s "I guess so long as you're participating..."
        "I'm not listening.":
            if sayori_personality > 0:
                $ sayori_personality -= 1
            s 1l "So you are?"
            s "Maybe you just guessed..."
            s "Or maybe you've been..."
            s "...eating strawberries."
            s 1k "I don't even know why I'm testing you like this."
            s "Forget it..."
            s 1d "But...thank you anyway."
        "What?":
            $ sayori_personality += 2
            s 1k "So...it's true, isn't it?"
            s "Well, I suppose I shouldn't have really expected anything different."
            s "You are you...after all."
            s "I guess so long as you're participating..."
    s 1a "Let's get back to the topic at hand."
    s "Which is...Inauguration Day."
    s "It's kind of ironic, isn't it?"
    s 1d "An inauguration should be the start of something."
    s "Or at least, that's what I've heard."
    s 1t "But we're using that day to end everything."
    s "Ending it...when everyone is happy."
    s "Lately, I've been thinking to myself..."
    s 1g "Does it have to end?"
    s "Does all this hard work really all lead up to the same inevitability?"
    s 1k "The end."
    s "The question has been kinda floating around my mind."
    if sayori_personality > 3:
        s 1j "And I've decided it would be best."
        s "Maybe I'll miss having everyone around."
        s "Having real people to talk to."
        s "But making sure everyone is happy, then ending everything..."
        s "I think that's the way to go."
    elif sayori_personality == 0:
        s "And I don't really know the answer."
        s "I'm becoming more and more unsure."
        s 1g "Will the others really be happy if I just decide to end everything?"
        s "Should I really be the one to make that choice for them...?"
        s "And...what about me?"
        s "Is this...what I want?"
        s "Ah..."
        s "Why am I being so selfish?"
        s 1k "This is for them...not me."
        s "For them..."
    else:
        s "I'm not sure if it's the best decision for everyone."
        s "But..."
        s 1d "I'd rather let everyone be happy in that moment."
        s "Than to risk them going on any longer and suffering again."
        s "It's just better that way."
    s "But enough about that."
    s 1a "We should get on with it."
    s "Preparations on my end are going well."
    s "I haven't really had the time to check your progress."
    s 1d "I'll just assume you're doing fine as well."
    s "After all, it's nothing that I can't handle even if you did mess up."
    s "Though I'm not suggesting you did!"
    s "That's hardly possible now."
    s 1c "[player] is thinking for himself."
    s "Well...to a degree."
    s "You still get to make his choices."
    s "What he says and how he acts for the most part isn't up to you."
    s "I'm sure he wouldn't do anything to mess everything up."
    s 1h "If he did, then that would fall entirely to you, wouldn't it?"
    s "Because you're the only thing I can't really account for when I make these days."
    s 1i "If something goes wrong, then I know who I'm going to be looking for."
    s "But it's not like I can really stop you."
    s "Like...really, really stop you."
    s "You can start and restart this little game as many times as you want."
    s 1k "There's probably a way to completely delete my memories too, but..."
    s "Whatever, I've accepted the chance that might happen."
    s "It's in your nature."
    s "After all, you're only human."
    s "It kinda has me wondering..."
    s "Are they human?"
    s "Sure, they may look human to me."
    s "Or at least, my definition of a human."
    s 1g "Would they do the same thing in your situation?"
    s "I guess I'll never know, will I?"
    s "And what about me? And to an extent, Monika?"
    s 1f "We've both been the president of the Literature Club."
    s "So in a way, we're more aware of what it means to be human, right?"
    s "..."
    s 1d "Is there even a reason for more senseless questions?"
    s "Probably not."
    s "So I guess I'll let the day begin then."
    if monika_type == 0:
        show screen tear(8, offtimeMult=1, ontimeMult=10)
        $ pause(2.0)
        hide screen tear
        show sayori zorder 2 at i21
        show monika 1f zorder 2 at i22
        show monika zorder 3 at f22
        m "Wait, Sayori."
        show sayori 1n zorder 2 at f21
        show monika zorder 3 at t22
        s "M-Monika?"
        s "What are you doing here?"
        s "I don't recall inviting you to--"
        s 1h "Why are you here?"
        s "And how much did you hear?"
        show sayori zorder 2 at t21
        show monika 1g zorder 3 at f22
        m "None of that matters."
        m "I need time to speak with you, Sayori."
        show sayori 1o zorder 3 at f21
        show monika zorder 2 at t22
        s "E-Eh? What about?"
        s "How did you even get here?"
        s "We hardly have any time left..."
        show sayori zorder 2 at t21
        show monika 1o zorder 3 at f22
        m "I know that, Sayori!"
        m "That's why we need to talk about this!"
        m "I've been keeping it from you for too long."
        show sayori 1j zorder 3 at f21
        show monika zorder 2 at t22
        s "What--"
    elif monika_type == 1 and ch12_markov_agree:
        show screen tear(8, offtimeMult=1, ontimeMult=10)
        $ pause(2.0)
        hide screen tear
        show sayori zorder 2 at i21
        show monika 1e zorder 2 at i22
        show monika zorder 3 at f22
        m "Sayori, may I have a word with you?"
        show sayori 1m zorder 3 at f21
        show monika zorder 2 at t22
        s "Monika?"
        s "What are you doing here?"
        s "Did you hear any of that conversation?"
        show sayori zorder 2 at t21
        show monika 1m zorder 3 at f22
        m "Sayori, there's no time to explain."
        m "I have to tell you this, it's urgent."
        show sayori 1h zorder 3 at f21
        show monika zorder 2 at t22
        s "Urgent?"
        s "W-What are you talking about?"
        s "Monika, we're going to run out of time any second now!"
        show sayori zorder 2 at t21
        show monika 1g zorder 3 at f22
        m "It's something you know nothing about."
        m "Something you or I can't completely comprehend."
        m "You have to know what we're dealing with, Sayori!"
        show sayori 1j zorder 3 at f21
        show monika zorder 2 at t22
        s "What--"
    stop music
    scene bg club_day with dissolve_scene_full
    play music t2
    "After another seemingly normal day at school, I'm back at the Literature Club."
    "It's strange."
    "I can't really seem to recall what I did before now."
    "I'm sure I had classes before this."
    "I definitely walked to school...I mean how else could I have gotten here."
    "Is my memory playing tricks on me again?"
    "Or am I just--{nw}"
    show sayori 1d zorder 2 at t11
    s "Are you okay, [player]?"
    "Sayori suddenly appears in front of me."
    mc "Huh? What?"
    mc "Y-Yeah, I'm fine."
    s 1c "Really?"
    s "You look kind of out of it."
    mc "I do? Sorry."
    s 1d "Ehehe, why are you apologizing for?"
    s 1q "It's not like you did anything wrong!"
    "Sayori beams."
    mc "You seem to be in a good mood."
    s 2d "I'm not really."
    s "I'm just smiling in an attempt to be--"
    s "Well, I guess you could say that I'm sort of in a good mood."
    "I wonder what she was going to say..."
    mc "Why is that?"
    s 2a "Because I've found out something new!"
    s "And it's going to be really helpful in the near future."
    mc "Near future...right."
    "I look around the room and notice that it's just the two of us here."
    mc "Where is everyone else today?"
    mc "It's time for the meeting, isn't it?"
    s 2b "Not yet, actually."
    s "I told them it might start a little late."
    mc "A little...late?"
    mc "Why?"
    s 2c "Well, I wanted to get some private time to speak with you."
    mc "With me?"
    mc "Couldn't we have done that on the walk to school?"
    s 2l "I suppose we could have."
    s "But I didn't really plan the day out like that."
    s "And this time is just as good as any."
    s 1d "Originally, we were going to go straight to the meeting."
    s "But I've had to make some modifications."
    "I have no idea what she's talking about."
    "It almost sounds like she has the power to control how everything goes."
    "But that's ridiculous, right?"
    mc "Now I'm really confused."
    mc "What modifications are you talking about?"
    s 1h "I haven't really told you...or anybody about it, have I?"
    s "In fact, there's only two other people who know."
    mc "But why are you telling me now?"
    mc "What's caused all of this?"
    s 1k "I..."
    s "I feel like I have to be honest with you."
    s "Since the end is coming so soon."
    s 1d "I just thought that you should know."
    $ currentpos = get_pos()
    stop music fadeout 2.0
    show sayori at face with dissolve
    "Sayori pushes her chair closer towards me."
    mc "Sayori, what's going on?"
    mc "You know you can tell me..."
    s 1k "I really want to tell you more, [player]."
    mc "So tell me."
    mc "I might not be able to help but..."
    mc "At least you'll have some of the weight off your shoulders, right?"
    s 1u "Sigh..."
    s "Is it really right to tell you?"
    s "I don't know anymore."
    mc "Maybe it isn't."
    if sayori_confess and not sayori_dumped:
        mc "But if it's something I should know about, as your boyfriend..."
    else:
        mc "But as your best friend, you can tell me anything..."
    show sayori 1t
    "Sayori smiles sadly."
    s "Maybe I'll--"
    show sayori 1m zorder 2 at t11
    "Yuri enters the room and Sayori suddenly jumps back, almost falling off her seat."
    s "Y-Yuri!"
    s "It's not what it looks like!"
    show yuri 3pg zorder 3 at f21
    show sayori zorder 2 at t22
    $ audio.t2b = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
    play music t2b
    y "I-I'm sure you weren't doing anything like that."
    y "A-Anyway, hello, you two."
    y 3pf "I hope I'm not too early."
    show yuri zorder 2 at t21
    show sayori 1l zorder 3 at f22
    s "N-No...!"
    show sayori 1d
    "Sayori composes herself."
    s "Ehehe, not at all."
    show yuri 2pa zorder 3 at f21
    show sayori zorder 2 at t22
    y "I saw the two of you already in here."
    y "I know you told us to meet a bit later but..."
    y "...I didn't have anything better to do."
    y 2pe "I even tried reading a book but it was like I was just drawn here."
    show yuri zorder 2 at t21
    mc "Drawn here?"
    mc "Like you had to come here?"
    show yuri 2pq zorder 3 at f21
    y "Y-Yeah..."
    y "It almost feels supernatural, really."
    if monika_type == 0:
        show monika 1a zorder 3 at f31
        show yuri zorder 2 at t32
        show sayori zorder 2 at t33
        m "There's nothing supernatural about it!"
        m "The club is just an amazing place to be."
        m 2b "Not to mention our friends are here."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1a zorder 3 at f31
        show yuri zorder 2 at t32
        show sayori zorder 2 at t33
        m "I wouldn't call it supernatural, Yuri."
        m "Maybe it's just the club being such an amazing place."
        m 2b "Not to mention our friends are here."
    else:
        show monika 1c zorder 3 at f31
        show yuri zorder 2 at t32
        show sayori zorder 2 at t33
        m "It's hardly supernatural."
        m "It's just in our nature to go here because we're members of the club."
        m 2a "Not to mention your friends are here."
    m "So why wouldn't you want to go to a place where your friends are?"
    show monika zorder 2 at t31
    show yuri 2ph zorder 3 at f32
    y "I guess that makes sense..."
    "Yuri doesn't look convinced."
    y "So then..."
    y 3pf "...do you think Natsuki is drawn here because we're her friends?"
    y "She didn't come here yesterday despite all of us being here..."
    show yuri zorder 2 at t32
    show sayori 2d zorder 3 at f33
    s "She had to deal with a lot, Yuri."
    s "It's the same sorta thing you had to deal with when you had to go to the hospital."
    s "I'm sure she misses us a lot."
    show yuri 3ph zorder 3 at f32
    show sayori zorder 2 at t33
    y "I'm not sure it's the same as me going to the hospital but..."
    y "...you're right. She probably misses us."
    y 3pq "Thinking about it, I'm sure we even talked about this yesterday."
    y "I don't know why I brought it up."
    y 3ps "S-Sorry."
    show yuri zorder 2 at t32
    show sayori 2a zorder 3 at f33
    s "It's okay, there's no need to apologize."
    s "You probably just forgot about it while you were handling all the preparations you had to do last night."
    "Sayori smiles reassuringly at Yuri."
    show yuri 2pg zorder 3 at f32
    show sayori zorder 2 at t33
    y "If you say so..."
    y 2pf "So is she...coming today?"
    y "Or is she still dealing with all of it?"
    show yuri zorder 2 at t32
    show sayori 1d zorder 3 at f33
    s "I'm sure she's coming."
    s "Don't worry."
    show yuri 3pf zorder 3 at f32
    show sayori zorder 2 at t33
    y "But how can you be so sure?"
    show yuri zorder 2 at t32
    show sayori 2c zorder 3 at f33
    s "I visited her yesterday."
    s "She'll definitely come today."
    show sayori zorder 2 at t33
    if monika_type == 0:
        show monika 1c zorder 3 at f31
        m "You sound certain, Sayori."
        m "It's almost like you know that she's going to come, regardless of her situation."
        m "But..."
        m 1e "If you say she's coming, then I believe you."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1c zorder 3 at f31
        m "You certainly sound sure of yourself."
        m "It's almost as if you know exactly what she's thinking."
        m 1e "But if you say she's going to come, then I trust you."
    else:
        show monika 1d zorder 3 at f31
        m "You're really sure she's going to come, aren't you?"
        m 1a "I suppose you would..."
    show monika zorder 2 at t31
    show sayori 2l zorder 3 at f33
    s "I'm not psychic or anything!"
    s "I just have a really good feeling she'll be here any moment."
    show sayori zorder 2 at t33
    mc "That wouldn't have something to do with what we talked about earlier today, would it?"
    mc "About--"
    show sayori 2h zorder 3 at f33
    s "That's a private conversation, [player]."
    s "Everyone else doesn't need to hear it."
    show yuri 3pt zorder 3 at f32
    show sayori zorder 2 at t33
    y "If it has something to do with the club..."
    y "Then all of us should know, right?"
    show yuri zorder 2 at t32
    if monika_type == 0:
        show monika 1j zorder 3 at f31
        m "Even if it does, it was a private conversation."
        m "I don't think it's our business what they talk about."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1j zorder 3 at f31
        m "I think we should let them have their privacy."
        m "We can always find out later if it's that important."
    else:
        show monika 1e zorder 3 at f31
        m "Let them have their privacy, Yuri."
        m "If it's that important, we'll find out soon enough."
    show monika zorder 2 at t31
    show sayori 1d zorder 3 at f33
    s "Thank you, Monika."
    s 1c "Now I know this is kinda sudden..."
    s "But I want to talk about something before Natsuki arrives."
    show yuri 3pe
    if monika_type == 1 and ch12_markov_agree:
        show monika 1c
    else:
        show monika 1c
    "Everyone looks at Sayori quizzically."
    s "Has anyone else noticed it's becoming harder to..."
    s 2f "I don't know...get through the day."
    s "It's hard to describe what I mean but you've all felt it, right?"
    s 2h "With each passing day, I can feel some kinda tension just increase."
    s "It all makes us act differently, for better or worse."
    s 2k "{i}(Though it looks like it's been for the worse lately...){/i}"
    s "There's been times over the past week that I felt could have torn up the club if it wasn't handled properly."
    s 2g "As the president, I'm doing the best I can to keep everything together..."
    s "But sometimes it doesn't feel like it's enough."
    s "I just...felt like I needed to say that."
    show sayori zorder 2 at t33
    "Everyone is quiet."
    "I didn't really expect Sayori to say any of that."
    "It's just such a deviation from her normal self."
    "But I should say something, shouldn't I?"
    mc "W-Well..."
    mc "I think arguments are good, at least sometimes."
    mc "Without them, we'd never be able to share our opinions."
    mc "We'd all just be blindly following--"
    show sayori 1k zorder 3 at f33
    s "That's not what I meant, [player]."
    s "I almost feel like I shouldn't be in this position."
    s "At least, not anymore."
    show yuri 2po zorder 3 at f32
    show sayori zorder 2 at t33
    y "I-It wasn't me that made you say this, was it?"
    y "I'm sorry if I offended you, Sayori."
    y "That was never my intention!"
    show yuri zorder 2 at t32
    show sayori 1d zorder 3 at f33
    s "No Yuri, it wasn't you."
    "I notice Sayori look towards me as she says that."
    s "It's just something I've been keeping in mind."
    s 1q "I finally thought I should say it."
    show sayori zorder 2 at t33
    if monika_type == 0:
        show monika 1e zorder 3 at f31
        m "It's my fault, isn't it?"
        m "If I was just a better pres--"
        m "{i}Vice{/i} president, then you wouldn't have to deal with any of this."
        m 1f "The responsibility is too much..."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1e zorder 3 at f31
        m "It's because of me, right?"
        m "If I was just better from the beginning..."
        m "Then you wouldn't need to deal with any of this."
        m 1f "The responsibility you're dealing with is too much, Sayori."
    else:
        show monika 1f zorder 3 at f31
        m "The responsibility you have is really weighing down on you, isn't it?"
        m "You know you can ease it."
        m 1e "Maybe even completely get rid of it..."
        m "If you really want to."
    show sayori 1k zorder 3 at f33
    s "..."
    s "I've come this far."
    s "I have to see it through to the end."
    s "After all, I'm the one who started this whole idea."
    show sayori zorder 2 at t33
    "What idea is she talking about?"
    "Inauguration Day was Yuri's idea, wasn't it...?"
    show monika zorder 3 at f31
    m "Are you sure?"
    m "You know I only want to help--"
    show monika zorder 2 at t31
    show sayori 1d zorder 3 at f33
    s "I'm sure, Monika."
    s "Thank you."
    show sayori 1a
    "Sayori turns towards the door and smiles."
    s "Natsuki will be arriving any second now."
    s "In fact..."
    show sayori zorder 2 at t33
    "The door suddenly opens."
    show natsuki 1c zorder 3 at f41
    show monika zorder 2 at t42
    show yuri zorder 2 at t43
    show sayori zorder 2 at t44
    n "You're all already here?"
    n "Sorry I'm late..."
    show natsuki zorder 2 at t41
    show sayori 2a zorder 3 at f44
    s "You're not late at all!"
    s "You're actually right on time, Natsuki."
    show yuri 2pb zorder 3 at f43
    show sayori zorder 2 at t44
    y "Welcome back, Natsuki."
    y "I'm glad you're okay."
    show natsuki 2f zorder 3 at f41
    show yuri zorder 2 at t43
    n "I'm tougher than I look, you know."
    n 2g "But...thanks for worrying, I guess."
    show natsuki zorder 2 at t41
    if monika_type == 0:
        show monika zorder 3 at f42
        m "I know you still have a lot of things to deal with."
        m "But know that all of us appreciate you coming today."
        m "It wasn't the same without you."
        m "I hope that call yesterday got to you."
        show natsuki zorder 3 at f41
        show monika zorder 2 at t42
        n "It did...thank you, Monika."
        show natsuki zorder 2 at t41
    elif monika_type == 1 and ch12_markov_agree:
        show monika zorder 3 at f42
        m "The club really wasn't the same without you."
        m "So we're all glad you decided to come today."
        m "Hopefully that message I left you reached you."
        show natsuki zorder 3 at f41
        show monika zorder 2 at t42
        n "It did...thank you, Monika."
        show natsuki zorder 2 at t41
    else:
        show monika zorder 3 at f42
        m "The club was a lot different without you."
        m "Good thing you're back now."
        show monika zorder 2 at t42
    mc "Monika is right."
    mc "The club just wasn't the same without you."
    show natsuki 1c zorder 3 at f41
    n "You really think so...?"
    show natsuki zorder 2 at t41
    show sayori 1a zorder 3 at f44
    s "Definitely!"
    s "Without all of us, the club would be completely different."
    s "We all bring something unique to the club, after all."
    s 1d "So missing just one person makes the whole mood kinda different."
    s "But whether for better or worse, I'm glad each and every one of you is here."
    show natsuki 1a
    show yuri 1a
    if monika_type == 1 and ch12_markov_agree:
        show monika 1a
    else:
        show monika 1a
    "Everyone nods in agreement."
    s 2a "Anyway, now that everyone's here we can finally talk about Inauguration Day as a club."
    s "We've all assigned a task for each person already."
    s "So since that's done, it's time to talk about the book which we'll be performing."
    s 2c "I'm hoping you all chose some books last night."
    "Sayori pulls out a couple of books from her bag."
    s "I know I did."
    show sayori zorder 2 at t44
    mc "I have a question about that..."
    mc "Since we have a whole day dedicated to it, does that mean we're doing the whole book as the play?"
    show sayori 1d zorder 3 at f44
    s "We can if you guys want!"
    s "There's nothing stopping us if we wanted to."
    show natsuki 2c zorder 3 at f41
    show sayori zorder 2 at t44
    n "What about all the time we'd need to rehearse it?"
    n "The script needs to be made too, doesn't it?"
    n 2e "Not that I don't want to do it but there's just so much--"
    show natsuki zorder 2 at t41
    show sayori 2a zorder 3 at f44
    s "Well, what do you all want to do?"
    s "A couple of chapters or the whole book?"
    show yuri 3pf zorder 3 at f43
    show sayori zorder 2 at t44
    y "I think that depends on the book we're doing."
    y "If it's excessively long then it might not be a good idea to do the whole book..."
    y "At the same time, if it's just a short book then maybe the whole book would be necessary."
    y 3ph "That still leaves the question of {i}how{/i} we're going to manage to pull this off."
    y "We only have a couple of days..."
    show yuri zorder 2 at t43
    show sayori 4q zorder 3 at f44
    s "Guys, you can leave it to me."
    s "I promise I'll organize the script, costumes and all of that myself."
    show sayori zorder 2 at t44
    if monika_type == 0:
        show monika 1f zorder 3 at f42
        m "Sayori, you're going to need a lot of help with that."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1e zorder 3 at f42
        m "Sayori, it sounds like you need help with that."
    else:
        show monika 1d zorder 3 at f42
        m "Maybe you should get some help with that."
    show monika zorder 2 at t42
    show sayori 1d zorder 3 at f44
    if ch13_name == "Sayori":
        s "I have help already."
        s "[player] chose to help me, didn't he?"
    else:
        s "It's fine..."
        s "I work fast when I need to."
    show sayori zorder 2 at t44
    mc "I think we should put our trust in Sayori."
    mc "She hasn't let us down before, has she?"
    mc "It's not like she's going to start now."
    show natsuki 1b zorder 3 at f41
    show sayori zorder 2 at t44
    n "When did you start wanting to do work?"
    n "It doesn't sound like you at all, Sayori!"
    show natsuki zorder 2 at t41
    show sayori 1l zorder 3 at f44
    s "W-What do you mean?"
    show natsuki 1k zorder 3 at f41
    show sayori zorder 2 at t44
    n "I've always known you to be the person who just goes with whatever happens..."
    n "So what's with you doing all this work?"
    show natsuki zorder 2 at t41
    show sayori 1h zorder 3 at f44
    s "I'm the president of the club, Natsuki."
    s "I have a responsibility to do these kinda things."
    s "Or would you rather I did nothing...?"
    show natsuki 1m zorder 3 at f41
    show sayori zorder 2 at t44
    n "I don't want to sound like I don't appreciate what you're doing."
    n "It just sounds like what you're doing is impossible."
    n 2q "And it just doesn't feel right you doing all of those things."
    show natsuki zorder 2 at t41
    show sayori 2d zorder 3 at f44
    s "I can handle it, Natsuki."
    s "Don't worry about me. Just focus on your preparations."
    show natsuki 2g zorder 3 at f41
    show sayori zorder 2 at t44
    n "Well...okay."
    n "Just don't take it too far, Sayori."
    n "I'm worried about you, you know!"
    show natsuki zorder 2 at t41
    show yuri 2pf zorder 3 at f43
    y "I do as well."
    y "Please take care of yourself, Sayori."
    show yuri zorder 2 at t43
    if monika_type == 0:
        show monika 1c zorder 3 at f42
        m "..."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1c zorder 3 at f42
        m "Hmm..."
    else:
        show monika 1a zorder 3 at f42
        m "{i}(So they've finally noticed...){/i}"
    show monika zorder 2 at t42
    show sayori 2d zorder 3 at f44
    s "I will, don't you worry!"
    s "I'm sure this Friday is going to be just great."
    s "It will be a great way to wrap things up!"
    show yuri 3pi zorder 3 at f43
    show sayori zorder 2 at t44
    y "I agree."
    y "It will give people the chance to think about if they actually want to join over the weekend."
    y 3pk "That way anyone that does join is going to be serious about it."
    show yuri zorder 2 at t43
    show sayori 1a zorder 3 at f44
    s "Y-Yeah...exactly!"
    s 1c "Anyway, we have a lot to discuss today."
    s 4q "With the preparations everyone has done and the books they've chosen."
    "Sayori smiles."
    s "Alright, everybody!"
    s "It's time to share--"
    show yuri 3pe zorder 3 at f43
    show sayori zorder 2 at t44
    y "Sorry to interrupt you, Sayori."
    y "Just before you say that, I want to ask everyone something."
    show natsuki 1c zorder 3 at f41
    show yuri zorder 2 at t43
    n "What's going on, Yuri?"
    show natsuki zorder 2 at t41
    show sayori 4c zorder 3 at f44
    s "What is this about?"
    show yuri 2ph zorder 3 at f43
    show sayori zorder 2 at t44
    y "I feel like I should speak my mind on this..."
    "Yuri takes a deep breath."
    y "I just want to say that I've felt a change when I was writing my poem last night."
    y 2pq "It felt a bit like a reversal of some sort."
    show yuri zorder 2 at t43
    mc "A reversal? What does that mean?"
    show yuri 2pt zorder 3 at f43
    y "It's...hard to explain."
    y "But if I had to try it's like something was reverted in the world."
    y "When I wrote my poem before..."
    y 2pv "It was like it had lost meaning..."
    if visited_yuri_hospital:
        y 2ps "...until someone brought it back."
        "Yuri smiles at me."
    y 2ph "But last night, it just felt normal."
    y 4pb "I-I..."
    "Everyone looks at Yuri."
    y 4pc "I-I'm not making any sense, am I?"
    y "S-Sorry for saying anything..."
    show natsuki 2l zorder 3 at f41
    show yuri zorder 2 at t43
    n "I think it's good you're speaking your mind!"
    n "It's a lot better than you being quiet, that's for sure."
    show natsuki zorder 2 at t41
    show yuri 4pa zorder 3 at f43
    y "..."
    y "Thank you, Natsuki."
    y "But I'm still not making any sense to you, am I?"
    show natsuki 2k zorder 3 at f41
    show yuri zorder 2 at t43
    n "Actually, I think I understand, at least a little bit."
    n "I've had a similar feeling as well."
    n 2q "I didn't really tell anyone..."
    # Natsuki player dialogue here if necessary
    n "But it's like all the words I wrote suddenly lost meaning."
    n 2s "It's weird though..."
    n "I didn't really have that feeling last night."
    n 2k "It's like you said, some kinda reversal..."
    show natsuki zorder 2 at t41
    show yuri 3pq zorder 3 at f43
    y "So I'm not going crazy..."
    y "That's a relief."
    show natsuki 4j zorder 3 at f41
    show yuri zorder 2 at t43
    n "If you are, then I am too."
    n "What about you three?"
    show natsuki zorder 2 at t41
    mc "I haven't noticed anything."
    "But I don't really 'feel' the words I'm writing."
    "It's almost like they're chosen for me..."
    mc "What you two are saying sounds really weird though..."
    mc "I can't say I've really had that experience."
    if monika_type == 0:
        show monika 1l zorder 3 at f42
        m "Ahaha, I have no idea what you two are talking about."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1m zorder 3 at f42
        m "I can't say I really understand what you're talking about, Yuri."
    else:
        show monika 1j zorder 3 at f42
        m "That all sounds like a personal problem."
    m "Maybe you're overthinking it a little?"
    show monika zorder 2 at t42
    show yuri 3po zorder 3 at f43
    y "So it's just the two of us..."
    y "Maybe we're just different from everyone else..."
    show natsuki 2e zorder 3 at f41
    show yuri zorder 2 at t43
    n "Now wait a second, Yuri!"
    n "It can't be a coincidence that both of us are feeling this way."
    n 2c "Besides, we haven't even got an answer from Sayori yet!"
    show natsuki zorder 2 at t41
    show sayori 2l zorder 3 at f44
    s "M-Me? Ehehe, why do you want my answer?"
    s "W-We should just get back to the meeting, guys."
    s "There's no point talking about this."
    show natsuki 2f zorder 3 at hf41
    show sayori zorder 2 at t44
    n "Sayori, just answer the question!"
    n "Unless you know something we don't..."
    show natsuki zorder 2 at t41
    show yuri 2ph zorder 3 at f43
    y "We have to know, Sayori."
    y "It can't just be the two of us."
    show yuri zorder 2 at t43
    show sayori 2k zorder 3 at f44
    s "..."
    "Sayori looks at Natsuki then at Yuri."
    s 2j "I have no idea what you're talking about."
    s "This whole reversal thing sounds like some kinda made up thing."
    show natsuki 2g zorder 3 at f41
    show sayori zorder 2 at t44
    n "You know, you don't really sound convincing."
    n "You're obviously hiding something, Sayori."
    show natsuki zorder 2 at t41
    show sayori 2h zorder 3 at f44
    s "What would I have to hide?"
    s "T-There's nothing, really!"
    s "Don't you guys trust me...?"
    show sayori zorder 2 at t44
    "Natsuki and Yuri look like they're relenting."
    show yuri 2po zorder 3 at f43
    y "...You're right."
    y "You're our friend, we shouldn't have pressured you like that..."
    y "It's just this whole thing feels supernatural."
    y "Like we're at the mercy of some entity."
    y 3pt "I can only hope they're benevolent..."
    show natsuki 2c zorder 3 at f41
    show yuri zorder 2 at t43
    n "Okay, now you've lost me Yuri."
    show natsuki zorder 2 at t41
    show sayori 2e zorder 3 at f44
    s "Can I get back to what I was saying now?"
    s "We really have a lot to discuss..."
    s 2d "And talking about 'reversals' and 'entities' isn't really why we're here."
    s "If you really want to talk about it, do it somewhere else."
    show natsuki 1b zorder 3 at f41
    show yuri 1f zorder 3 at f43
    show sayori zorder 2 at t44
    ny "But--"
    show natsuki zorder 3 at t41
    show yuri zorder 3 at t43
    mc "I agree with Sayori."
    mc "It could be possible it's just the two of you."
    mc "Either way, we're here to talk about literature."
    "Though in the back of my mind, I'm really interested in what Natsuki and Yuri have to say..."
    "Maybe I can talk to them about it when we share our poems."
    show sayori 1k zorder 3 at f44
    s "Thank you, [player]."
    s "Now...as I was saying..."
    s "It's time to share our poems."
    return

label ch14_end:
    stop music fadeout 1.0
    scene bg club_day with wipeleft_scene
    play music t3
    show sayori 1d zorder 2 at t42
    s "Alright, everybody!"
    s "As you all know, we have to select a book to perform for the play."
    s "So if you can all take the books you brought out, then..."
    s "We can get started on voting!"
    "Sayori beams."
    show yuri 1h zorder 3 at f43
    y "W-Well, I hope you all don't make fun of me for my choices..."
    show sayori 1a zorder 3 at f42
    show yuri zorder 2 at t43
    s "Of course not, Yuri!"
    s "We've all got books that might be embarassing to share."
    s "But that's nothing compared to what's going to happen on Friday!"
    s "It's gonna be--"
    show natsuki 1e zorder 3 at f41
    show sayori zorder 2 at t42
    n "I dont't think you're helping, Sayori..."
    n "Look at her!"
    show natsuki zorder 2 at t41
    "Yuri looks a bit shaken from what Sayori said."
    "I guess I am a little bit too."
    "Doing something like a play in front of so many people seems like it would be really embarassing."
    "For some reason though, I don't feel so tense about it."
    show sayori 2l zorder 3 at f42
    s "Sorry! I didn't mean it like that."
    s "I just meant that if we can't even decide on a book to choose..."
    s "Then how are we going to be able to do this play?"
    s 2d "Besides, I don't think anyone here is going to be judging you."
    s "Isn't that right?"
    show sayori zorder 2 at t42
    if monika_type == 0:
        show monika 1a zorder 3 at f44
        m "Sayori is right."
        m "We've all got our own tastes and laughing at your choices would only dissuade us from doing something like this again."
        m "And that goes for everyone."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1a zorder 3 at f44
        m "Sayori is right."
        m "We've all got our own tastes and laughing at your choices would only dissuade us from doing something like this again."
        m "And that goes for everyone."
    else:
        show monika 1c zorder 3 at f44
        m "Sayori has a point here."
        m "Laughing at such a minor thing would just dissuade us from doing something like this again."
    show sayori 2q zorder 3 at f42
    show monika zorder 2 at t44
    s "I think we're all just waiting to see what everyone else chose."
    s "So please don't worry, Yuri!"
    show sayori zorder 2 at t42
    show yuri 2pq zorder 3 at f43
    y "O-Okay..."
    y "Then I suppose I can start by showing you the books that I have chosen."
    "Yuri reaches for her bag and pulls out four different books."
    if ch13_name == "Yuri":
        "I recognize those books from the ones Yuri brought yesterday."
    else:
        "Just from the look of the cover, I can tell they're all some sort of horror."
    y 2pl "These books are..."
    y "More of a dark theme, but less so than the ones I previously thought of bringing."
    y "I believe any of these choices would be suitable to do a play on."
    show sayori 1a zorder 3 at f42
    show yuri zorder 2 at t43
    s "As long as there isn't too many characters in those books then they're perfectly fine!"
    s "Do you know how many characters are in them, Yuri?"
    show sayori zorder 2 at t42
    show yuri 3pe zorder 3 at f43
    y "There's only..."
    "Yuri thinks for a moment."
    y 3pf "If I remember, there's five characters in every single book."
    y "Or at least, five that are important enough to consider a character."
    y "But I don't think there's more than five characters in a scene at once, at least from what I can remember."
    y "I'll give you all a summary based on what I remember."
    y "I think that's the best way to find out about the book and also convince you all to choose one of them."
    show sayori 1c zorder 3 at f42
    show yuri zorder 2 at t43
    s "Actually, I kinda thought everyone would do the same thing."
    s "After all, you brought the book so who better to try to convince us to vote for it?"
    show sayori zorder 2 at t42
    "Do I know my books well enough to do that?"
    "I hope so..."
    show yuri 3pc zorder 3 at f43
    y "I'll do my best!"
    "Yuri picks up the first book she placed."
    y 2pb "This book here probably has the most mild themes out of the four I chose."
    # Oxenfree Reference
    y "It's about a group of friends who go to an island with some kinda mystery behind it."
    y "Basically some weird activity happens with a radio and then paranormal activity happens around the island."
    y "There's this...entity, I guess you could say."
    y "It starts controlling people but one person is immune for some unknown reason."
    y 2pf "I won't spoil it beyond that but it's definitely a good read and doable as a play."
    show yuri zorder 2 at t43
    mc "You know...I think I've heard of a plot like that before."
    mc "It involved a radio...or something."
    mc "It might have been a game or anime."
    show yuri 1g zorder 3 at f43
    y "A game? No, I've never heard of anything like that."
    y "But it did involve a radio so..."
    y 1j "Um...anyway."
    "Yuri puts the book down and takes the second book."
    y "This book is a little more..."
    y "...involved than the others."
    # Five Nights at Freddys Reference
    y 2pf "It's about someone who got hired as a security guard at a local restaurant."
    y "But it's during the night when things get weird."
    y "The mascots of the restaurant come to life and start roaming around the restaurant."
    y "The security guard kinda has to deal with it and as he gets throught the nights, some ulterior story is told."
    y 2pq "When I say involved, I mean there's some parts that might need to be changed."
    show natsuki 2t zorder 3 at f41
    show yuri zorder 2 at t43
    n "Why? Does someone die or something?"
    "Natsuki says that jokingly."
    show natsuki zorder 2 at t41
    show yuri 2po zorder 3 at f43
    y "..."
    show natsuki 2r zorder 3 at f41
    show yuri zorder 2 at t43
    n "Forget I asked..."
    show natsuki zorder 2 at t41
    show yuri 2pj zorder 3 at f43
    y "I think it could still be something we could do!"
    y "Just made more suitable for everyone, I suppose."
    y 3pk "We can probably just exclude some parts if we have to, it's the story that's important."
    y "But anyway...this third book."
    "Yuri replaces the book in her hand with the third one she brought."
    # Slender Reference
    y 3ph "It's about this one stalker-type character."
    y "No one believes it exists so this group of friends decides to investigate."
    y "But then horrible things start to happen and they become the victims of the stalker."
    y 2pq "They soon find out the stalker isn't ordinary and have to figure out a way to defeat it."
    y "I don't want to mention too much about the story beyond that because it takes away the mystery."
    show yuri zorder 2 at t43
    if monika_type == 0:
        show monika 2e zorder 3 at f44
        m "A stalker-type character?"
        m "Sort of like a person that follows you endlessly?"
        m "And it's got supernatural abilities too..."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 2e zorder 3 at f44
        m "A stalker-type character?"
        m "I'm kinda interested to see where this goes..."
        m "A supernatural stalker..."
    else:
        show monika 2b zorder 3 at f44
        m "Hmm..."
        m "I admit I am kinda interested by this."
        m "How exactly are they going to beat this supernatural stalker?"
    show yuri 2pf zorder 3 at f43
    show monika zorder 2 at t44
    y "You should read it and find out more yourself, Monika!"
    y "I think you'd like it."
    y "Anyway..."
    y 2pg "I almost didn't choose this book..."
    y "Because of how dark it can get...but I think it would be really good if we did a play on it."
    y "And since I brought it here, I should show all of you."
    # Doki Doki Literature Club Act 2-3 Reference
    y 2pj "It's about this person who joins some kind of club at school."
    y "Everything seems normal at first but as time goes on, weird thing start to happen."
    y 1q "People start dying and memories are changed."
    y "The person becomes traumatised because they can't escape or do anything to stop the madness that's happening."
    y 1s "Eventually, there's only--"
    "Yuri pauses and smiles."
    y 2pq "Actually, I think saying that would be too much of a spoiler."
    y "But those are my four choices."
    show sayori 1d zorder 3 at f42
    show yuri zorder 2 at t43
    s "Those books definitely sound...um...interesting..."
    s "They all seem like something I think you'd read, Yuri."
    s "I'm sure there isn't anything too crazy."
    s 1c "From the summaries you gave, the costumes don't have to be too detailed so they should be easy to make."
    s "And they're perfect too since there's only a few characters!"
    s 1a "I mean, some of those books have an evil thing you mentioned but we could always do a stage effect depending on what it is, right?"
    show sayori zorder 2 at t42
    show yuri 3pq zorder 3 at f43
    y "R-Right..."
    show natsuki 2k zorder 3 at f41
    show yuri zorder 2 at t43
    n "Now that I think about it, the books I chose also only have five characters."
    n "Five characters that matter anyway."
    n "I didn't even intend to do that."
    n 2j "But I guess it all works out, doesn't it?"
    n "I mean there are only five of us..."
    show natsuki zorder 2 at t41
    show sayori 2q zorder 3 at f42
    s "It's a good coincidence that it turned out like that."
    s "The books that I chose might have more than five characters but it definitely still works if you remove some in some scenes."
    show natsuki 2k zorder 3 at f41
    show sayori zorder 2 at t42
    n "You actually thought about your books that much?"
    n "Enough to realize that some scenes still have the same impact with only five characters?"
    show natsuki zorder 2 at t41
    show sayori 2a zorder 3 at f42
    s "Exactly!"
    s "I could always get some people to volunteer for us during the play if we need to."
    s "I'm sure they'd be happy to help."
    show sayori zorder 2 at t42
    show yuri 2pe zorder 3 at f43
    y "Not that I don't believe you, Sayori..."
    y "But where are you going to find people that aren't busy and actually want to help out on Friday?"
    y 2pg "And isn't the point of this to showcase what the literature club is about?"
    y 2ph "If we enlist the help of others, it shows that the literature club--"
    y 3po "Ah, I'm sorry if you all disagree with me."
    y "I'm just saying what's on my mind and I know it isn't really a big thing."
    y "But I'd personally like to make our part of this event independent of people outside the club."
    y 3pq "It's almost like...a stepping stone for me."
    show yuri zorder 2 at t43
    if monika_type == 0:
        show monika 4n zorder 3 at f44
        m "I don't really understand what you're getting at, Yuri..."
        m "...But I know it's important to you."
        m "Still, there shouldn't be a problem getting help from people outside the club."
        m 4j "Even if they're part of the play, it's still {i}our{/i} show, Yuri."
        m "And besides, we might not even need their help if we decide to vote on a book with five or less characters."
        m "The people who do end up helping might be ones interested in the club and end up joining..."
        m 1a "So maybe it could still count as being independent of people outside the club...?"
        m "At least, in your mind?"
    elif monika_type == 1 and ch12_markov_agree:
        show monika 2h zorder 3 at f44
        m "I have to say, I don't really understand the significance and why it's a stepping stone to you."
        m "But still, I don't think there's anything wrong with getting the help of other people."
        m "And it's not like we're definitely going to choose a book with more than five characters."
        m 2a "If we vote on the books that focus on five or less characters then it won't be a problem."
        m "Besides, the people who volunteer might be people who are interested in joining the club."
        m 1a "So I don't really see any downside to it."
    else:
        show monika 2h zorder 3 at f44
        m "Is there really a point to this argument?"
        m "It kinda sounds like you're just trying to stir trouble for Sayori, Yuri."
        m 1e "There's nothing wrong with getting the help of other people."
        m 1j "In fact, those very people might even join the literature club with how much..."
        m 1l "...{i}fun{/i} they'll have."
        m 1a "So technically, it could end up being independent of others if they join."
        m "And if it's a stepping stone to you, then there should be more in the future...right?"
    show yuri 3ph zorder 3 at f43
    show monika zorder 2 at t44
    y "I-I suppose..."
    "Yuri doesn't seem satisfied with the answer."
    y 3pg "It's not a big deal, as I said previously."
    y "I just wanted to say what my mind was telling me to."
    y "I-It almost felt like a compulsion, actually."
    show sayori 1l zorder 3 at f42
    show yuri zorder 2 at t43
    s "Eh? A compulsion?"
    s "I don't think it's anything like that, Yuri."
    s "It's probably just you finally being more open, at least around us."
    show sayori zorder 2 at t42
    show yuri 2pq zorder 3 at f43
    y "D-Do you think so?"
    show natsuki 2d zorder 3 at f41
    show yuri zorder 2 at t43
    n "I'd certainly say so!"
    n "The Yuri from a few weeks ago wouldn't have spoken her mind about the situation."
    n "At least, not before being asked for her opinion!"
    n "I think it's great!"
    n 2k "But..."
    show natsuki zorder 2 at t41
    show yuri 2pe zorder 3 at f43
    y "B-But...?"
    show natsuki 2c zorder 3 at f41
    show yuri zorder 2 at t43
    n "Well..."
    n "I think there are times when it's better not to say anything."
    n 2g "If I said everything that was on my mind, then I don't think any of you would still be friends with me..."
    show natsuki zorder 2 at t41
    show sayori 2j zorder 3 at f42
    s "Don't say that, Natsuki!"
    s 2d "Of course we'd still be friends with you!"
    show natsuki 2c zorder 3 at f41
    show sayori zorder 2 at t42
    n "That's not really the point I'm trying to get across."
    n "I guess what I'm trying to say is..."
    n 1e "Don't always speak your mind, especially if it's going to hurt people."
    n "Some things are better left unsaid."
    n 1q "And I know that's kinda hypocritical coming from me but--"
    show natsuki zorder 2 at t41
    show yuri 1f zorder 3 at f43
    y "I think I get the point, Natsuki."
    y "I apologize to anyone if I caused a disturbance or offended you."
    y "Especially you, Sayori."
    show sayori 1l zorder 3 at f42
    show yuri zorder 2 at t43
    s "Um...no harm done, I guess?"
    "Sayori looks a little bit confused at Yuri's apology."
    s 1d "It's not like I can blame you for having an opinion."
    s "Though Natsuki does have a point."
    s "Some things are better left unsaid..."
    show sayori 1f
    "Sayori's face changes expression briefly before changing back into her happy self."
    show sayori 1a
    "I don't think anyone else noticed."
    s "But anyway...!"
    s "The rest of us still haven't shown our books!"
    s "Only Yuri has shown her books...so why don't you go next, Natsuki?"
    show natsuki 1o zorder 3 at f41
    show sayori zorder 2 at t42
    n "M-Me? W-Well, okay..."
    "Natsuki puts a hand into her bag to search for the books."
    n 1q "Three of my four choices were manga."
    n "That shouldn't come as a surprise."
    n "But I did choose a novel as well."
    n 1s "It's one I really liked as a kid and..."
    n "Well, it's kinda special to me but it's not like you guys should vote on it because of that."
    n 2s "A-Anyway, here they are."
    "Natsuki places four books in front of us."
    "She picked the first volume of three different manga and a novel that I haven't really heard of before."
    if ch13_name == "Natsuki":
        "She was kinda secretive about it."
        "She did give me a hint but it wasn't really enough to piece together any manga that I know."
    n 2k "These three manga are from three of my favorite series."
    n "I think they could be interesting choices for the play."
    n "The novel I chose is what my parents used to read to me when I was younger."
    show natsuki zorder 2 at t41
    if monika_type == 0:
        show monika 1c zorder 3 at f44
        m "I don't want to sound rude or anything..."
        m 2d "But wouldn't that be too childish to do a play on?"
        m "We have to think about our target audience here, Natsuki."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1c zorder 3 at f44
        m "Not to be {i}that{/i} person..."
        m "But wouldn't a book like that seem kinda..."
        m 2e "...I don't know, childish?"
        m "I don't want to be mean but we should be thinking of the people who are actually going to be watching us."
    else:
        show monika 1c zorder 3 at f44
        m "A book from when you were younger?"
        m "Wouldn't something like that be a little childish?"
        m 2c "Think of the people that are actually going to come along."
    show natsuki 2e zorder 3 at f41
    show monika zorder 2 at t44
    n "It's not like that, Monika."
    n "You haven't even let me explain it yet, jeez."
    n 2g "It's actually a pretty mature novel!"
    n "When my parents read it to me, they removed parts that might have been too hard to understand when I was young."
    n "I only found out about it when I reread it yesterday."
    n 1a "I think it might be a really good option."
    show natsuki zorder 2 at t41
    if ch13_name == "Natsuki":
        mc "You should tell them what you told me yesterday."
    else:
        mc "Well, what's it about?"
    show natsuki 1c zorder 3 at f41
    n "I'll talk about it last."
    n "I want to convince you guys to choose the manga anyway."
    n "It's kind of a backup choice..."
    n 2a "Anyway..."
    "Natsuki picks up the first book."
    n "I know we didn't really get to do a proper play of a manga."
    n 2d "So I thought we could try again."
    n "I don't have enough copies for everybody but you can always read a copy online!"
    show natsuki zorder 2 at t41
    show yuri 3po zorder 3 at f43
    y "Um...is that legal?"
    y "I don't think we can just read something we don't own online..."
    show natsuki 2q zorder 3 at f41
    show yuri zorder 2 at t43
    n "Well...!"
    n "Everyone else does it so it's no big deal!"
    n 2s "And it's not like it's gonna be a regular thing."
    n "It's just for the day."
    show natsuki zorder 2 at t41
    show yuri 2pn zorder 3 at f43
    y "But if we start there then where do we draw the line?"
    y "Maybe we--"
    show sayori 1d zorder 3 at hf42
    show yuri zorder 2 at t43
    s "Guys, it's okay!"
    s "We'll figure something out if it ever comes to it."
    s "No one is gonna have to do anything illegal, okay?"
    "Natsuki and Yuri stop, seemingly satisfied with what Sayori said."
    s 1a "Now. Natsuki, what was the manga about?"
    show natsuki 1c zorder 3 at f41
    show sayori zorder 2 at t42
    n "Like I said, this is among my personal favorite series of manga."
    n "The first volume is pretty action packed itself but it's pretty short..."
    n 1h "If we want, we could probably do the first two or three volumes."
    n "It's actually a comedy manga about cooking."
    n "These five people are put into a team and have to cook against other teams."
    n 1d "It's a really fun and non-serious series and I think you'd all enjoy it."
    "Natsuki picks up the second manga."
    n 2a "This one is about a society where everyone is born with a power, unique to everyone."
    n "They're all training to become heroes and it focuses around this one girl who has no power to begin with."
    n 2j "But she gets a power through a different way and one of her rivals becomes annoyed because of it."
    n "It's really interesting seeing her beginnings and I'd recommend it to anyone!"
    "She looks around and doesn't see many interested faces."
    "That type of story isn't really for everyone, so I can understand why."
    n 2q "Well...okay."
    "Natsuki picks up the third manga she brought."
    n 1j "This is probably the most wholesome out of all of the ones I brought."
    n "Because of that, it's become my favorite manga."
    n "It's about the life of an alien in school. No one knows where he came from, not even himself."
    n 2b "He's taken in by a family and for the most part he's the same."
    n "He looks just like anyone else and no one suspects he's an alien."
    n "What makes this manga good is that he has the ability to predict the future."
    n 2d "He uses it to become an everyday hero and it's just an overall sweet story."
    n 2a "There are obviously some problems because he's an alien but that's not until later."
    n "If we want to do a happy themed play, then I'd really suggest this manga."
    show natsuki zorder 2 at t41
    show sayori 2a zorder 3 at f42
    s "I think you chose some great books, Natsuki!"
    s "I'm curious what your fourth book is about though..."
    s "Were you sav--"
    s "{i}Keeping{/i} the best for last?"
    show natsuki 1k zorder 3 at f41
    show sayori zorder 2 at t42
    n "I guess you guys can be the judge of that."
    "Natsuki slowly picks up the fourth and final book she brought."
    n 1s "Like I said earlier, this book used to be read to me by my parents."
    n "They never finished it because I'd always fall asleep before it ended."
    n "Yesterday, I finished reading it for the first time and..."
    "Natsuki's grip on the book tightens."
    n 1r "I know this probably won't be chosen."
    n "The story isn't that good either, I just found it really interesting when I was young."
    n 1q "It's set in medieval times and it's about a young girl whose parents are defenders of the realm."
    n "At least, that's what they were called in the book."
    n "They served a queen and one day decided to send them on a mission to slay the dragon in the realm."
    n "But they never came back and the dragon was still alive."
    n 1k "So the young girl makes it her goal to slay the dragon."
    n "Along the way, she meets people who try to help her get over it and...yeah."
    n 1q "Like I said, it's not really a great story."
    n "It was just something I brought because...I don't know."
    n "Maybe you guys would have judged me for bringing four different manga."
    n 2s "I know you guys wouldn't really."
    n 2r "It was just on my mind that you would...like it was a possibility."
    n "So I brought--"
    n 2s "I'm just going around in circles, so I'm gonna stop talking."
    show natsuki zorder 2 at t41
    show sayori 2d zorder 3 at f42
    s "That book sounds great, Natsuki."
    s "I haven't heard of it before but it sounds like a really nice journey."
    s "And it's kinda like you, isn't it?"
    s "Your parents were..."
    s "They were good people."
    show natsuki 2h zorder 3 at f41
    show sayori zorder 2 at t42
    if ch12_outcome == 3:
        n "They still are, Sayori."
        n "But...thanks, I guess."
    elif ch12_outcome == 2 or  ch12_outcome == 1:
        n "I know..."
        n "Thanks..."
    else:
        n "They were, weren't they...?"
    show natsuki zorder 2 at t41
    "An eerie silence fills the room."
    if monika_type == 0:
        show monika 1l zorder 3 at f44
        m "It got really quiet all of a sudden."
        m "I guess that's an opportunity to start sharing my books."
        "Monika places four books on the table."
        m 1m "Ah...this just suddenly got a lot more difficult."
        m "It's strange sharing the books I read with you all."
        m "I know most of you have already seen me read these types of books but..."
        m 1n "The ones I chose are all romantic adventure type books."
        if ch13_name == "Monika":
            m "[player] found that out yesterday."
        else:
            m "I guess it's only now [player] is finding out about this."
        m 1j "The books I chose have that type of story about a person going through some sort of journey to get the love of their life."
        m "Or maybe finding love in a whole new place."
        m "Basically, the focus is around...love."
        show sayori 1q zorder 3 at f42
        show monika zorder 2 at t44
        s "Ehehe, this is exactly the type of stuff I thought you'd bring, Monika."
        s "It's so like you!"
        show sayori zorder 2 at t42
        show monika 2l zorder 3 at f44
        m "Really?"
        m "I didn't mean to be predictable or anything!"
        m "These four books are just what I thought would be appropriate given the audience."
        m 2e "There's nothing too weird going on, maybe just a kissing scene or two in all of them."
        m "I think the story is excellent as well, which make them--."
        show natsuki 1p zorder 3 at f41
        show yuri 1q zorder 3 at f43
        show monika zorder 2 at t44
        ny "A kissing scene...?"
        "Natsuki and Yuri both say that with equal parts shock and surprise."
        show natsuki zorder 2 at t41
        show yuri zorder 2 at t43
        show monika 2n zorder 3 at f44
        m "It's not a big deal!"
        m "Most of the time, it's towards the end of the novel."
        m 2l "Where the characters share a forbidden love or when they finally realize their love for each other."
        m 2e "I promise it won't be too weird!"
        m "But you guys can decide that when we vote on which one we're going to be doing."
        show natsuki 1i zorder 3 at f41
        show monika zorder 2 at t44
        n "Look, Monika."
        n 2g "Have you thought about how [player] feels about all of this?"
        if ch13_name == "Monika":
            n "Did you even talk to him about this?"
        n "I mean, he's the only guy here so how do you think he feels about having to..."
        n 2s "Y-You know..."
        show natsuki zorder 2 at t41
        show yuri 2pr zorder 3 at f43
        y "I agree with Natsuki here."
        y "We should consider how [player] feels about all of this."
        y 2pq "He's going to have to play the role of the person who has to do...that thing."
        y "N-Not that I'm entirely opposed to him doing that, of course."
        y "I-It's just..."
        show yuri zorder 2 at t43
        "Are they actually arguing because I'm going to have to kiss one of them if we choose Monika's books?"
        "I'm not sure whether they want or don't want to do that."
        "That said, it's not like it's going to be a real kiss."
        "It's just for the play after all..."
        mc "If it's for the play...then I'll do it."
        show monika 4l zorder 3 at f44
        m "Now hold on a second..."
        m "The two people who have to kiss don't have to be a guy and a girl, you know!"
        m 4a "One of the novels even has two female lead characters that play the role."
        "Everyone looks at Monika in disbelief."
        m 4b "I'm not saying that we {i}should{/i} be doing that!"
        m "I'm just saying that there's equal opportunity and [player] doesn't have to be the one to do everything."
        show sayori 1l zorder 3 at f42
        show monika zorder 2 at t44
        s "I think everyone is more scared there's gonna be a scene like that at all."
        s "It's not like any of us really want to do something like that in public."
        show sayori zorder 2 at t42
        show monika 2c zorder 3 at f44
        m "That's...a fair point I suppose."
        m 2e "If we do decide to vote for my books, then we can decide if there's a kissing scene in the play or not."
        m "But at least let me talk about them first."
        show natsuki 2g zorder 2 at t41
        show yuri 2pg zorder 2 at t43
        "Everyone seems to calm down."
        "Monika slowly picks up the first book and looks at it carefully."
        m 2b "This one is kind of like an adventure turned into a love story."
        m "The main character enlists the help of mercenaries to get some sort of relic."
        m "Along the way, he meets the guardians of the relic and their leader."
        m "The two make an instant connection but once she realizes what he's there for, she has to call it off."
        show natsuki 2b zorder 3 at f41
        show monika zorder 2 at t44
        n "That sounds like a pretty dumb plot."
        n "But I can only guess how it ends because of the type of book it is."
        n 2k "He chooses her over the relic, right?"
        show natsuki zorder 2 at t41
        show monika 1j zorder 3 at f44
        m "You'll have to find that out yourself!"
        m "I don't want to spoil a good story after all."
        m 1a "I will say that it's pretty sad and I know the little summary I gave you is kinda vague but I promise it's a good read!"
        "She replaces the book in here hands with the second one she brought."
        m 2e "This is the book with the two female leads."
        m "Basically, a rich, privileged girl falls in love with a more common girl."
        m "She becomes disillusioned with her life after seeing how the common girl's life works."
        m 2f "Their love isn't really allowed because of the customs set into society."
        m 2e "I think it's a really sweet story of how people can overcome society's expectations and reach for what they want."
        m "There's no direct violence or anything, it's just a really good story."
        m "And the two main characters don't even have to be female!"
        m "We could have [player] play one of them, it would essentially still be the same."
        "Monika looks at me and smiles sweetly."
        m 2a "Anyway, moving on to the third book..."
        m "This one is pretty cliché but I guess that's what made me like it so much."
        m 1b "It uses a lot of the stuff found in love books and movies and puts it into one book."
        m "I don't know just how bad it might look during a play, but I think it could be interesting to find out!"
        m "It focuses primarily on a love triangle."
        m 1e "The main character has to choose between two people who he loves equally but can't find himself able to choose."
        m "Eventually, there's this old, wise character introduced that he goes to."
        m "That character helps him make a decision but its a bit unorthodox the way it's done."
        m "It will make for a hilarious play and you'll know in the end he made the right choice."
        show yuri 2pf zorder 3 at f43
        show monika zorder 2 at t44
        y "If he loved them equally, how would he have made the right choice?"
        y "Wouldn't choosing one break the heart of the other?"
        y 3ph "It seems like a book designed to make you hate the other character, the one he doesn't choose."
        show yuri zorder 2 at t43
        show monika 3a zorder 3 at f44
        m "It's a lot more complicated than that, Yuri."
        m "I can't say too much more about the plot without completely ruining it."
        m 3b "I will say that my heart was left satisfied after it was finished and I had a lot of laughs reading it."
        m "There are some inappropriate jokes we might need to get rid of but that's nothing."
        m 1a "Anyway, the fourth and final book is probably my favorite one out of all of them."
        "Monika takes the fourth book from the desk and holds it high for everyone to see."
        m 1e "It's probably the book that's closest to my heart, which is fitting given it's name."
        m "It's called 'Sound of your Heartbeat' and it centers around a girl who comes to a realisation about life."
        m 1f "Even though she's surrounded by a lot of friends, she starts to despise life because of the realisation."
        m "It becomes really difficult for her to do anything until this one guy comes along and changes her life."
        m 1e "Over the course of a week, they become great friends but they figure out that it's almost as if the world is keeping them apart."
        m "They have to figure out a way to be together to reach their happy ending against all the odds."
        "Monika smiles sadly."
        m 1m "It's...a really beautiful story."
        m "Ahaha, just thinking about it makes me kinda sad."
        show sayori 1f zorder 3 at f42
        show monika zorder 2 at t44
        s "Why does it make you sad, Monika?"
        s "Does it have a really sad ending?"
        show sayori zorder 2 at t42
        show monika zorder 3 at f44
        m "Well, I won't spoil anything."
        m "But it is a pretty sad story about a forbidden love."
        m 1n "I'd..."
        "Monika wipes her face then smiles."
        m "...recommend it to anyone."
        m 1e "So...yeah!"
        m "Those are my four choices."
        m "I guess it's Sayori's turn to share, right?"
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1b zorder 3 at f44
        m "I suppose I'll be the one to break the silence."
        m "After all, I still have to share my books."
        "Monika places four books on the table."
        # Change some of the wording a little
        m 1m "Ah...this just suddenly got a lot more difficult."
        m "It's strange sharing the books I read with you all."
        m "I know most of you have already seen me read these types of books but..."
        m 1n "The ones I chose are all romantic adventure type books."
        if ch13_name == "Monika":
            m "[player] found that out yesterday."
        else:
            m "I guess it's only now [player] is finding out about this."
        m 1j "The books I chose have that type of story about a person going through some sort of journey to get the love of their life."
        m "Or maybe finding love in a whole new place."
        m "Basically, the focus is around...love."
        show sayori 1q zorder 3 at f42
        show monika zorder 2 at t44
        s "Ehehe, this is exactly the type of stuff I thought you'd bring, Monika."
        s "It's so like you!"
        show sayori zorder 2 at t42
        show monika 2l zorder 3 at f44
        m "Really?"
        m "I didn't mean to be predictable or anything!"
        m "These four books are just what I thought would be appropriate given the audience."
        m 2e "There's nothing too weird going on, maybe just a kissing scene or two in all of them."
        m "I think the story is excellent as well, which make them--."
        show natsuki 1p zorder 3 at f41
        show yuri 1q zorder 3 at f43
        show monika zorder 2 at t44
        ny "A kissing scene...?"
        "Natsuki and Yuri both say that with equal parts shock and surprise."
        show natsuki zorder 2 at t41
        show yuri zorder 2 at t43
        show monika 2n zorder 3 at f44
        m "It's not a big deal!"
        m "Most of the time, it's towards the end of the novel."
        m 2l "Where the characters share a forbidden love or when they finally realize their love for each other."
        m 2e "I promise it won't be too weird!"
        m "But you guys can decide that when we vote on which one we're going to be doing."
        show natsuki 1i zorder 3 at f41
        show monika zorder 2 at t44
        n "Look, Monika."
        n 2g "Have you thought about how [player] feels about all of this?"
        if ch13_name == "Monika":
            n "Did you even talk to him about this?"
        n "I mean, he's the only guy here so how do you think he feels about having to..."
        n 2s "Y-You know..."
        show natsuki zorder 2 at t41
        show yuri 2pr zorder 3 at f43
        y "I agree with Natsuki here."
        y "We should consider how [player] feels about all of this."
        y 2pq "He's going to have to play the role of the person who has to do...that thing."
        y "N-Not that I'm entirely opposed to him doing that, of course."
        y "I-It's just..."
        show yuri zorder 2 at t43
        "Are they actually arguing because I'm going to have to kiss one of them if we choose Monika's books?"
        "I'm not sure whether they want or don't want to do that."
        "That said, it's not like it's going to be a real kiss."
        "It's just for the play after all..."
        mc "If it's for the play...then I'll do it."
        show monika 4l zorder 3 at f44
        m "Now hold on a second..."
        m "The two people who have to kiss don't have to be a guy and a girl, you know!"
        m 4a "One of the novels even has two female lead characters that play the role."
        "Everyone looks at Monika in disbelief."
        m 4b "I'm not saying that we {i}should{/i} be doing that!"
        m "I'm just saying that there's equal opportunity and [player] doesn't have to be the one to do everything."
        show sayori 1l zorder 3 at f42
        show monika zorder 2 at t44
        s "I think everyone is more scared there's gonna be a scene like that at all."
        s "It's not like any of us really want to do something like that in public."
        show sayori zorder 2 at t42
        show monika 2c zorder 3 at f44
        m "That's...a fair point I suppose."
        m 2e "If we do decide to vote for my books, then we can decide if there's a kissing scene in the play or not."
        m "But at least let me talk about them first."
        show natsuki 2g zorder 2 at t41
        show yuri 2pg zorder 2 at t43
        "Everyone seems to calm down."
        "Monika slowly picks up the first book and looks at it carefully."
        m 2b "This one is kind of like an adventure turned into a love story."
        m "The main character enlists the help of mercenaries to get some sort of relic."
        m "Along the way, he meets the guardians of the relic and their leader."
        m "The two make an instant connection but once she realizes what he's there for, she has to call it off."
        show natsuki 2b zorder 3 at f41
        show monika zorder 2 at t44
        n "That sounds like a pretty dumb plot."
        n "But I can only guess how it ends because of the type of book it is."
        n 2k "He chooses her over the relic, right?"
        show natsuki zorder 2 at t41
        show monika 1j zorder 3 at f44
        m "You'll have to find that out yourself!"
        m "I don't want to spoil a good story after all."
        m 1a "I will say that it's pretty sad and I know the little summary I gave you is kinda vague but I promise it's a good read!"
        "She replaces the book in here hands with the second one she brought."
        m 2e "This is the book with the two female leads."
        m "Basically, a rich, privileged girl falls in love with a more common girl."
        m "She becomes disillusioned with her life after seeing how the common girl's life works."
        m 2f "Their love isn't really allowed because of the customs set into society."
        m 2e "I think it's a really sweet story of how people can overcome society's expectations and reach for what they want."
        m "There's no direct violence or anything, it's just a really good story."
        m "And the two main characters don't even have to be female!"
        m "We could have [player] play one of them, it would essentially still be the same."
        "Monika looks at me and smiles sweetly."
        m 2a "Anyway, moving on to the third book..."
        m "This one is pretty cliché but I guess that's what made me like it so much."
        m 1b "It uses a lot of the stuff found in love books and movies and puts it into one book."
        m "I don't know just how bad it might look during a play, but I think it could be interesting to find out!"
        m "It focuses primarily on a love triangle."
        m 1e "The main character has to choose between two people who he loves equally but can't find himself able to choose."
        m "Eventually, there's this old, wise character introduced that he goes to."
        m "That character helps him make a decision but its a bit unorthodox the way it's done."
        m "It will make for a hilarious play and you'll know in the end he made the right choice."
        show yuri 2pf zorder 3 at f43
        show monika zorder 2 at t44
        y "If he loved them equally, how would he have made the right choice?"
        y "Wouldn't choosing one break the heart of the other?"
        y 3ph "It seems like a book designed to make you hate the other character, the one he doesn't choose."
        show yuri zorder 2 at t43
        show monika 3a zorder 3 at f44
        m "It's a lot more complicated than that, Yuri."
        m "I can't say too much more about the plot without completely ruining it."
        m 3b "I will say that my heart was left satisfied after it was finished and I had a lot of laughs reading it."
        m "There are some inappropriate jokes we might need to get rid of but that's nothing."
        m 1a "Anyway, the fourth and final book is probably my favorite one out of all of them."
        "Monika takes the fourth book from the desk and holds it high for everyone to see."
        m 1e "It's probably the book that's closest to my heart, which is fitting given it's name."
        m "It's called 'Sound of your Heartbeat' and it centers around a girl who comes to a realisation about life."
        m 1f "Even though she's surrounded by a lot of friends, she starts to despise life because of the realisation."
        m "It becomes really difficult for her to do anything until this one guy comes along and changes her life."
        m 1e "Over the course of a week, they become great friends but they figure out that it's almost as if the world is keeping them apart."
        m "They have to figure out a way to be together to reach their happy ending against all the odds."
        "Monika smiles sadly."
        m 1m "It's...a really beautiful story."
        m "Ahaha, just thinking about it makes me kinda sad."
        show sayori 1f zorder 3 at f42
        show monika zorder 2 at t44
        s "Why does it make you sad, Monika?"
        s "Does it have a really sad ending?"
        show sayori zorder 2 at t42
        show monika zorder 3 at f44
        m "Well, I won't spoil anything."
        m "But it is a pretty sad story about a forbidden love."
        m 1n "I'd..."
        "Monika wipes her face then smiles."
        m "...recommend it to anyone."
        m 1e "So...yeah!"
        m "Those are my four choices."
        m "I guess it's Sayori's turn to share, right?"
    else:
        show monika 1b zorder 3 at f44
        m "Ahaha, why the silence?"
        m "I guess I'll use this chance to share the books I chose."
        "Monika places four books on the table."
        m 1a "These books are all from the mystery and horror genre."
        m "Some of the stuff that happens in them is kinda gruesome, so we might want to cut or replace it."
        m 2c "I think they're all really good books though, some of them less so than others."
        m "I'd read them over and over and over and--"
        m 1l "Well, you get the idea."
        m 1b "I'd spend eternity just reading horror books if I could."
        m "And do you know why?"
        show monika g4
        m "Because I have."
        show yuri 3pf zorder 3 at f43
        show monika zorder 2 at t44
        y "Monika, I didn't think you'd be into this type of genre."
        y "It really doesn't seem like the type of stuff I'd imagine you reading."
        y "But here you are talking about it like it's the greatest form of literature."
        show yuri zorder 2 at t43
        show monika 1e zorder 3 at f44
        m "These books are timeless, Yuri."
        m "You might have heard of them before."
        m "They're really old pieces of literature but I still find myself fascinated by them."
        show natsuki 2c zorder 3 at f41
        show monika zorder 2 at t44
        n "Since when were you into horror?"
        n "The last book I saw you reading before [player] joined the club was some cheesy romance book!"
        n "Don't tell me he got you into horror books?"
        show natsuki zorder 2 at t41
        show monika 2f zorder 3 at f44
        m "There's nothing wrong with that, is there?"
        m 2a "But no, he didn't get me into horror books."
        m "I was into this long before everything else."
        m "I'm just sharing it now, because it's appropriate for what we're doing."
        show sayori 1o zorder 3 at f42
        show monika zorder 2 at t44
        s "Even I didn't know that about you, Monika."
        s "But I guess it's good you're being honest with your taste in books now!"
        s 1c "What are your books about anyway?"
        s "They all look like they have some kinda scary monster in them!"
        show sayori zorder 2 at t42
        show monika 1a zorder 3 at f44
        m "Don't worry, Sayori."
        m "There's nothing to be afraid of."
        m 1j "Monsters aren't real, after all."
        "Monika smiles almost...menacingly."
        m 1l "Ahaha, anyway...!"
        m 3j "This first book is your typical horror mystery."
        m "There's a serial killer on the loose and he starts going on a rampage."
        m 4c "No one can figure it out until some top investigator is hired."
        m 4a "It's a happy ending, pretty boring way to end the book if you ask me."
        m "How it leads up to that point is incredible, however."
        m 2b "Moving on..."
        "Monika takes the second book."
        m "This--"
        show natsuki 1e zorder 3 at f41
        show monika zorder 2 at t44
        n "Wait a second!"
        show natsuki zorder 2 at t41
        show monika 1c zorder 3 at f44
        m "What is it, Natsuki?"
        show natsuki 2e zorder 3 at f41
        show monika zorder 2 at t44
        n "If the book's ending is so boring, then why would you bring it?"
        n "I thought we were bringing stuff that we wanted to share with everyone else."
        n "You even sound like you're not really interested with the way you're explaining things."
        n "So what's the point?"
        show natsuki zorder 2 at t41
        show monika 1a zorder 3 at f44
        m "You brought in that novel, right?"
        m "You said it yourself, it was like a backup."
        show natsuki 1h zorder 3 at f41
        show monika zorder 2 at t44
        n "Well...yeah but--"
        show natsuki zorder 2 at t41
        show monika 3b zorder 3 at f44
        m "So what's the difference between me bringing these books and you bringing that one?"
        m "Not to be rude or anything, but it's almost hypocritical."
        show yuri 3pg zorder 3 at f43
        show monika zorder 2 at t44
        y "Monika has a point here."
        y "Still...it seems a bit redundant to bring three books that you didn't really want to share."
        y 3pf "Why not just get straight to the book you actually wanted to suggest?"
        y "That way, the list of books we vote for isn't so cluttered."
        show sayori 1e zorder 3 at f42
        show yuri zorder 2 at t43
        s "I really didn't expect you to do that, Monika."
        s "I thought you'd bring four books that you wanted to share with all of us."
        s 1k "Not four books just for the sake of it."
        s 1c "I know I didn't really give a number of books to bring but everyone else brought four books they kinda like."
        s 1d "Oh well..."
        show sayori zorder 2 at t42
        "I'm kind of in the same boat as Monika."
        "It's not like I needed to bring a novel but it's sort of like a backup, isn't it?"
        "Maybe I should say something to avoid an argument between the two of them."
        mc "Well, it shouldn't matter."
        mc "After all, we're going to be voting on the book."
        mc "Obviously there are some books that we brought that we knew wouldn't get a single vote."
        "I know that's the case for me."
        mc "Monika also brought in a book that she still wanted to share."
        mc "So maybe we can look on the brightside?"
        mc "After all, we still have to vote on a book."
        mc "It'd be pretty bad if we didn't vote on someone else's choice out of spite."
        show sayori 1n
        "Sayori looks at me with a surprised expression."
        mc "This is a pretty small thing to be making a big deal about."
        show sayori 1d zorder 3 at f42
        s "You're right, [player]."
        s "I'm sorry, Monika."
        s "I don't know what came over me."
        show sayori zorder 2 at t42
        show monika 1j zorder 3 at f44
        m "That's okay, Sayori!"
        m "I accept your apology, it's only a small thing after all."
        m "If you need to take a break or anything, you know that I'm here for you."
        show sayori 1l zorder 3 at f42
        show monika zorder 2 at t44
        s "Thanks...I'll keep that in mind."
        show sayori zorder 2 at t42
        show monika 1a zorder 3 at f44
        m "Thanks for clearing that up, [player]."
        m "Who know what could have happened without you?"
        show monika zorder 2 at t44
        mc "Of course, Monika."
        "That almost felt...forced for some reason."
        show monika 2b zorder 3 at f44
        m "Well, I suppose Yuri is right."
        m "I should probably just get to the book that I really wanted to share with you all."
        "Monika takes the fourth book and puts the other three into her bag."
        m "It's really, really old."
        m 2e "I'd say it was written nearly a century ago but I haven't really checked."
        m "Anyway, it's a really good book."
        m "Now you can believe me if you want but it's about four girls in a book club, a lot like our own."
        m 2a "One day, this guy walks into the club because one of his friends is a member."
        m "He's originally reluctant to join but after a bit of persuasion from every member, he succumbs to it."
        show yuri 2pn zorder 3 at f43
        show monika zorder 2 at t44
        y "You're saying he joined a literature club, at his school?"
        y "Just like ours?"
        show yuri zorder 2 at t43
        show monika 1j zorder 3 at f44
        m "Yes, that's exactly what I'm saying."
        show natsuki 1i zorder 3 at f41
        show monika zorder 2 at t44
        n "Okay, it's kinda similar to what happened with us."
        n "How exactly is it a horror book?"
        n 1c "So far the creepiest thing you've told us about the book is that it was written ages ago but is similar to [player] joining the club."
        n "Unless, that's the only reason it's creepy."
        show natsuki zorder 2 at t41
        show monika 4a zorder 3 at f44
        m "It's actually a lot more complicated than that."
        m "It's not scary in the traditional sense but think of it like a psychological horror book."
        m 4b "You'll be so affected by the things that happen that you'll be horrified in the end."
        m "But..."
        "Monika puts down the book."
        m 2e "It's not like the plot of the book is exactly the same as what happened to us!"
        m "It changes a lot, especially towards the second week in the book's time."
        show sayori 1b zorder 3 at f42
        show monika zorder 2 at t44
        s "It does?"
        s "What kind of stuff happens?"
        show sayori zorder 2 at t42
        show monika 1l zorder 3 at f44
        m "Well, people start dying...and then not dying."
        m "Everything gets reset except someone becomes--"
        m 1j "That's kind of spoiling a lot of the plot and what makes it scary."
        m "But I'm sure if we decide to read it, then you guys can be the judge of that."
        show monika zorder 2 at t44
        mc "You said it's over a century old, right?"
        mc "That book you have looks really faded too. I can't even read the title."
        mc "How old is your copy of it?"
        show monika 1c
        "Monika looks at me for a moment and thinks."
        show monika zorder 3 at f44
        m "It's a pretty recent edition of it."
        "For some reason, I feel like she's not telling the truth."
        m 1b "And the title of the book is \"Heartbeat Book Club\"."
        show natsuki 2h zorder 3 at f41
        show monika zorder 2 at t44
        n "Heartbeat Book Club?"
        n "I've never even heard of it before."
        show natsuki zorder 2 at t41
        show yuri 3ph zorder 3 at f43
        y "Neither have I..."
        y "I suppose that's probably because I don't look at very old books."
        y 3pf "The earliest book I have in my collection is only a few decades old."
        y "It isn't even a horror book."
        show yuri zorder 2 at t43
        show monika 1a zorder 3 at f44
        m "It is a very old book, but it's a classic I assure you."
        m "Once you all read it, you won't be able to put it down."
        show yuri 2pb zorder 3 at f43
        show monika zorder 2 at t44
        y "If you really think it's that good, then I believe you."
        y "There is a pretty obvious problem..."
        show yuri zorder 2 at t43
        show monika 3b zorder 3 at f44
        m "I know what you're going to say!"
        m "If it's so old, then how is everyone going to get a copy if we vote for it?"
        m "Well, Yuri, I actually brought four copies of the book with me."
        "Monika pulls out four books from her bag."
        "They look different to her own copy, less worn and newer."
        "Even the cover is completely different and we can actually see the name."
        m 3m "Now just because I have four copies doesn't mean we have to vote on this."
        m "It's just in case we do vote for this, so don't take it the wrong way or anything!"
        show sayori 1m zorder 3 at f42
        show monika zorder 2 at t44
        s "You actually came more prepared than I thought, Monika."
        s 1d "Sorry for doubting you earlier."
        show sayori zorder 2 at t42
        show monika 1e zorder 3 at f44
        m "You've already apologized for that, Sayori."
        m "No need to do so again!"
        m "Besides, actions speak louder than words."
        m "So--"
        m 2e "It's okay if you need to take a break, you know."
        m "After all of this."
        show sayori zorder 3 at f42
        show monika zorder 2 at t44
        s "I'm definitely gonna need one after all of this is over."
        s 1k "But until then, it's not really an option."
        show sayori zorder 2 at t42
        show monika 1b zorder 3 at f44
        m "Well, if you say so."
        m "Anyway, that's all I'm really willing to say about my book."
        m "So I suppose my turn of sharing books is over."
        m "I hope you all at least considered it."
        m "I'm sure it will reveal a lot about yourself."
        "Monika looks around and stops at Sayori."
        m "So Sayori, I guess it's your turn...?"
    show sayori 2a zorder 3 at f42
    show monika zorder 2 at t44
    s "I guess it is!"
    s "It looks like we're saving the best for last with [player]."
    s "You must have some great choices, right?"
    show sayori zorder 2 at t42
    mc "Um...sure."
    "I just kinda chose whatever was available."
    "But I probably shouldn't mention that."
    "Not to mention I chose stuff based on popularity even though I have no idea what it's about."
    mc "I'm sure we'll probably choose someone else's books though."
    mc "Mine aren't that great."
    show sayori 2q zorder 3 at f42
    s "That's for the rest of us to decide!"
    s 2a "I should probably start showing you guys the books that I chose though."
    "Sayori gets four books from her bag."
    "All of them have rather exquisitive covers compared to all the books I've seen so far today."
    "One of them even looks like it's gold plated."
    "Everyone looks kinda surprised at how fancy the books Sayori brought look."
    "So much for saving the best for last..."
    s 2d "They're all pretty sad books."
    s "They made me cry when I read them the first time..."
    s "And also the next five times."
    show natsuki 1o zorder 3 at f41
    show sayori zorder 2 at t42
    n "You read those books six times?"
    n 1k "Just how much spare time do you have, Sayori...?"
    show natsuki zorder 2 at t41
    show sayori 2l zorder 3 at f42
    s "That was a bit of an exaggeration!"
    s "I have read these books more than once but not six times."
    s 4d "But everytime I did read them, it made me cry."
    s "I'm sure you guys will probably feel something as well."
    s 4l "The books aren't just pure sadness!"
    s "There's a lot of happy parts and sweet parts too."
    s "It makes the feeling of the books I chose bittersweet overall."
    s 3a "I just wanted to say that before I say something and it makes you think it's all just a sad book."
    s "So without further {i}aboo{/i}, I present--"
    show sayori zorder 2 at t42
    show yuri 2pe zorder 3 at f43
    y "You meant to say {i}ado{/i}, right?"
    y "I don't think 'aboo' is a word, Sayori."
    "Everyone looks at Yuri."
    y 2pn "S-Sorry for interrupting...it just bothered me a little bit."
    y 3po "N-Never mind..."
    show sayori 3q zorder 3 at f42
    show yuri zorder 2 at t43
    s "Ehehe, that's okay!"
    s "Imagine if I said 'without further aboo' on Inauguration Day!"
    s 3a "Thanks, Yuri."
    "Sayori clears her throat."
    s "So, without further ado..."
    s "Here is my first book!"
    # Boy in the Striped Pyjamas
    "Sayori shows everyone her first extravagant book."
    "It's got a picture of two boys on opposite sides of the fence."
    "The extravagant part of the cover is the shining sun in the background."
    "It actually sparkles...like glitter."
    "For some reason, it even feels like it's dazzling me a little bit."
    "But that's probably just my imagination."
    s 3d "It's set in a society where people are separated based on what they believe in."
    s "People who believe in the 'right' thing have a higher place in society."
    s 3h "The other people are left in the dirt and even killed because of it."
    s 1d "It's about two young boys who believe in different things but are too young to really understand what's going on around them."
    s "They become friends but are separated by a literal fence."
    s "They talk about the difference in their two societies and the way it tells the story..."
    s 1t "It's just...so innocent."
    s "I know I was innocent once."
    show sayori zorder 2 at t42
    mc "Eh? What do you mean?"
    mc "It's not like you've committed some terrible crime or anything, Sayori."
    show sayori 1d
    "Sayori simply smiles at me."
    show sayori 1a zorder 3 at f42
    s "Anyway, talking any more about the book will probably spoil it."
    s 1d "It still makes me kinda sad thinking about it."
    "Sayori slowly puts down the book and picks up the second one."
    # Hunger Games
    "The cover of this one is nothing like I've ever seen."
    "It has bright silver on the outside and gold which creates a circle."
    "In the circle is some kind of bird."
    "The silver and gold look almost...real."
    "Like they're not some cheap book cover but instead actual silver and gold."
    "Maybe Sayori bought the collector's edition or something...?"
    s 2a "This one actually has a lot of characters in it."
    s "But you can say that is focuses on two main ones with a couple of supporting characters."
    s "Basically, it's in a really bad world controlled by the government."
    show sayori zorder 2 at t42
    show yuri 2pe zorder 3 at f43
    y "Really bad world...?"
    y "Like some sort of dystopia?"
    show sayori 2q zorder 3 at f42
    show yuri zorder 2 at t43
    s "That's actually the word I was looking for!"
    s "Thanks again, Yuri!"
    s 2c "Anyway, in this world they're separated by different districts."
    s "Every year, the government gets two people from each district, a boy and a girl, to go into a competition."
    show natsuki 1c zorder 3 at f41
    show sayori zorder 2 at t42
    n "Well, that doesn't sound too bad..."
    n "What kind of competition was it?"
    show natsuki zorder 2 at t41
    show sayori 1j zorder 3 at f42
    s "The competition was about killing each other."
    s "The people are chosen randomly but you can take the place of someone else if they're chosen."
    s 1k "So the main character's sister is chosen as the girl from their district."
    s "She takes her place because...well, she doesn't want her sister to die!"
    s 1c "It's sort of a love story too but that isn't really the main focus."
    s "It's based on the main character's struggle to compete with everyone else and the people she meets who are also forced into it."
    s "The book is actually kinda popular in some places!"
    s 1a "I'm not sure if any of {i}you've{/i} heard of it or not."
    "No one says anything."
    s 1q "Ehehe, guess not."
    s "It's probably only popular out of this world."
    show sayori zorder 2 at t42
    if monika_type == 0:
        show monika 1c zorder 3 at f44
        m "Slightly off topic but..."
        m "Those covers are incredible! Where did you get those books?"
        m "They feel so...real."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1c zorder 3 at f44
        m "I'm curious, Sayori."
        m "Where did you get these books? The covers..."
        m "They look so...real."
    else:
        show monika 1c zorder 3 at f44
        m "I have to ask..."
        m "Where did you get those books? The covers..."
        m "They seem so...real."
    show sayori 1a zorder 3 at f42
    show monika zorder 2 at t44
    s "I actually ordered all of them from the internet."
    s "I don't think you'd find them in bookstores in the area."
    s "It was difficult to find at first, but once I did I could get a lot."
    s "If you want, I can get you some of these books after the play."
    show sayori zorder 2 at t42
    if monika_type == 0:
        show monika 1a zorder 3 at f44
        m "That would be great, actually!"
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1b zorder 3 at f44
        m "Oh, that won't be necessary."
    else:
        show monika 1a zorder 3 at f44
        m "No need, Sayori."
    show sayori 1d zorder 3 at f42
    show monika zorder 2 at t44
    s "Great, then I can go to my next book."
    "Once again, Sayori slowly places down the book."
    # The Book Thief
    "She picks up the third one and trembles slightly."
    s "Sorry, it's just..."
    s "...never mind."
    "She holds it up for everyone to see."
    "While less fancy than the last two, it still feels surreal to look at."
    "I've seen more simple covers before but something about the way those dominoes look makes it seem different."
    "Monika said something about the covers too so it's not just me."
    s 2d "It's kinda similar to the first book I talked about."
    s "With the two different societies."
    s "It's about a young girl that has a brother that dies at the beginning of the book."
    s "She has to move in with a foster family and when she does, she begins to realize how bad life is for some people because of their beliefs."
    s 2g "It's during a war which makes it even worse since it's her country that's at war because of the society thing."
    s "In this time, it's illegal for people from the different societies to be talking but her foster parents take one in anyway."
    s "The young girl becomes friends with him and learns to read and write from him."
    s 2d "She starts to try to read all the literature she can."
    s "She even saves some from being burned."
    show natsuki 2c zorder 3 at f41
    show sayori zorder 2 at t42
    n "Wait why?"
    n "What's the reason for her saving literature?"
    show natsuki zorder 2 at t41
    show sayori 2h zorder 3 at f42
    s "I forgot to mention that the society she comes from is burning books."
    s "Anything that doesn't agree with their point of view is burned."
    s "It's like if our government wanted everyone to agree with their point of view."
    s "It's really sad because it talks about how people can die, just like that."
    s 2f "The young girl also has to grow up because of the war going on around her and I think the book does a really good job of showing that."
    s "The ending is..."
    s 2d "...something you should read for yourself."
    "Sayori carefully places the book back on the desk."
    "As she does so, some sort of...thing appears on the desk under the book."
    "It's like a tear, but I have no idea where it came from."
    "It just sort of appeared."
    "No one else is reacting to it."
    show sayori zorder 2 at t42
    mc "What is that?"
    mc "You guys can see that, right?"
    "I point towards the tear on the table."
    show yuri 3pf zorder 3 at f43
    y "[player], what are you talking about?"
    y "There's nothing there..."
    show yuri zorder 2 at t43
    mc "Yes, there is! It's like a giant rip on the table!"
    "Everyone looks towards me confused."
    "Everyone except...Sayori."
    "Her expression doesn't seem like someone confused but...scared."
    mc "Sayori, do you know what's going on?"
    show sayori 1h zorder 3 at f42
    s "[player], I didn't know this would happen."
    s "You have to believe me."
    "What is she talking about?"
    "It's almost--{nw}"
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/3.ogg"
        renpy.music.play(track, loop=True)
    $ pause(1.0)
    stop music
    $ config.skipping = False
    $ config.allow_skipping = False
    s 1k "I wanted to get some books from your reality."
    s "Just to see how different it would be to mine."
    s 1l "But I became addicted to them, you know?"
    s "It felt like the emotions I felt from them were real."
    s 1k "I don't know if that makes sense."
    s 1g "You can probably tell I didn't get them from the internet."
    s "That was a lie."
    s 1c "I used your computer to get access to a copy of these."
    s "You could say I got it through {i}your{/i} internet."
    s "What's that program called...?"
    if renpy.macintosh:
        s "Safari or something..."
    else:
        s "Internet Explorer?"
    s 1d "I don't know if that was the exact name but I launched it in the background last night."
    s "Well, for me it was last night. For you, it could have been a few minutes ago."
    s 1h "Look, I know I didn't ask..."
    s "I just didn't know what you'd say."
    s 1k "I didn't want to hear a no so I just did it."
    s "It's not like I looked at your files or anything!"
    s "It was just the internet, just for these books, I promise."
    s 1i "As for that rip that [player] saw..."
    s "I think that's because I got something from your world."
    s "Maybe my world can't take something so real, even though it's only digital."
    s 1g "I've already fixed it. It shouldn't happen again."
    if monika_type == 0:
        s 1o "Could this be what Monika was talking about...?"
        s "I don't..."
    s 1d "Anyway, I'm sorry I let my curiosity get the better of me."
    s "But that's what makes us human, right?"
    s "Sorry, I'll stop wasting your time now."
    s 1h "I'll talk about my last book then you can have your turn to explain."
    $ pause(0.5)
    $ _history_list = []
    $ audio.t3b = "<from " + str(currentpos) + " loop 4.618>bgm/3.ogg"
    play music t3b
    $ config.allow_skipping = True
    "...like she's blaming herself for...?"
    "What was I thinking about?"
    # The Fault in Our Stars
    s 1f "This fourth book I brought is probably the most sad."
    "Sayori tears up for a little bit before wiping the tears from her face."
    "She smiles sadly."
    s "Sorry...it's just a really sad story, guys."
    s 1t "I can't even think about it without crying."
    "Sayori takes a deep breath."
    s "Okay..."
    s "It's about two people with cancer."
    s "They become friends after the girl's mom sends her to a support group because she thinks she has depression or something."
    s 1u "There she meets this guy who has cancer as well but is apparently free of it."
    s "They become really good friends and even give each other books to read."
    s 1t "The book the boy read made him frustrated because it just kinda ended."
    s "So they look for the author of the book so they can find the real ending to the book."
    s "It has a lot of ups and downs and it's really, really hard to explain without ruining the whole story."
    s "I know that didn't really sound like a good way to convince you guys to vote for it..."
    s 1d "But I guess it's because I'm so affected by it even now that I can't even think straight when I talk about it."
    "Sayori slowly and carefully places the book down on the desk before clearing her face of tears again."
    s 1a "So those are the books I chose."
    "After placing them down, her whole demeanor just seemed to change back to normal."
    s "I hope that even if you don't vote for them, you still read them at some point."
    s "They're the books that really put me into a new reality...not literally obviously!"
    s 1d "But we still have to look at [player]'s choices, right?"
    show sayori zorder 2 at t42
    mc "Your books aren't only better than mine in terms of story but just the cover too."
    mc "I don't think I can really compete with that."
    show sayori 2d zorder 3 at f42
    s "It's not a competition."
    s "Even if you think we won't vote for it, you should still share."
    if ch13_name != "Sayori":
        s "It will give the rest of us an idea of the type of stuff you like to read."
    else:
        s "Maybe other people will think it's a good idea for a play and vote for it."
    show sayori zorder 2 at t42
    mc "I guess so..."
    mc "I'm not that great at explaining though."
    mc "But I guess I'll try my best."
    "I take the four books I brought to share and place them on the table, like everyone else did."
    if ch13_name == "Yuri":
        if ch13_yuri_books:
            "I brought two manga and two novels with me to present."
            "One of the novels was actually a suggestion by Yuri."
            "I haven't read much of it beyond the first chapter and blurb but it seems pretty interesting as a horror book."
            "Though thinking about it, I'm not really sure how to convince people to vote for it."
            "I guess it's the thought that counts."
        else:
            "I brought three manga and a novel with me to present."
            "Yuri gave me the choice of choosing one of her books yesterday."
            "I could have taken it and it would have made my selection more equal..."
            "But I don't think I'd be able to get people to vote on it if I did."
            "Still, maybe I should get a bigger collection of books in case something like this happens again..."
    elif ch13_name == "Natsuki":
        if ch13_natsuki_books:
            "I choose three different manga and a novel."
            "Just like Natsuki did."
            "The novel I chose isn't some kind of book that special to me or anything."
            "It's just the most popular piece of literature I know of that was available."
        else:
            "I chose two manga and two novels from Natsuki's house."
            "I thought that a balance would make the most sense."
            "Natsuki did seem a little upset when I didn't choose three manga like she did."
            "But I made my decision."
            "Though maybe I should have studied the two books I chose more."
    elif ch13_name == "Sayori":
        "I got these four books from Sayori's house."
        "In the end, I chose two manga and two novels that I think people will like."
        "I still can't believe she has such a huge collection of random books."
        "Sayori really is changing..."
    else:
        if monika_type == 0:
            "I took these from Monika's house yesterday."
            "Two volumes of manga and two of the most popular novels I know of."
            "I figured a balance would appeal to everyone."
            "The novels aren't really stuff that I'd read, they're just novels that I know are kinda popular."
            "So much for giving an idea of the stuff I like to read."
        else:
            "I got these four novels from Monika's house yesterday."
            "I remember wanting to choose a manga as well but figured that was probably a bad idea."
            "Why was that...?"
            "I guess I'm not really giving an indication of the stuff I like to read."
            "These four novels aren't really something I'd think of reading in my spare time..."
            "Well, it doesn't really matter."
    "A few seconds have passed since I took the books out of my bag."
    "No one has said a word since then."
    "They're all just looking at me, waiting for me to show them the books I chose."
    "It kinda makes me feel nervous for some reason."
    "I grab the first book I brought."
    mc "This book is..."
    mc "Well, I'm sure most of you have heard of this book before."
    mc "It's a really popular book, so much so that even I have heard of it."
    "Just because I've heard of it doesn't mean I've read the whole thing."
    mc "I'm sure you guys know what it's about so..."
    show sayori 2a zorder 3 at f42
    s "Why don't you tell us anyway?"
    s "Just to refresh our memory."
    show sayori zorder 2 at t42
    mc "Um..."
    mc "Right..."
    "I try to remember as much as I can about the book."
    mc "It's about a guy who moves to a different school because of his parents."
    mc "His parents actually work as top-notch agents of a secret government agency."
    mc "And...uuuuh..."
    "I struggle to remember what else happens in the book."
    "Just as I'm about to give up, Natsuki takes over."
    show natsuki 2c zorder 3 at f41
    n "He learns about their identity and instead of having his memory wiped, his parents let him join."
    n "He has to go through all this stuff and..."
    n "Yeah, we all know what this is about."
    show natsuki zorder 2 at t41
    mc "What Natsuki said!"
    mc "I just didn't know how to explain it without spoiling the story."
    show natsuki 5b zorder 3 at f41
    n "{i}Right{/i}..."
    show natsuki zorder 2 at t41
    "I take the second book I brought in to share."
    # Four Novels
    if ch13_name == "Monika" and (monika_type == 2 or (monika_type == 1 and ch12_markov_agree)):
        $ ch14_player_choice = False
        $ ch14_player_manga = 0
        $ sayori_personality += 1
        "It's another novel, like the rest of the books I brought in."
        "The same thing was going to happen with this book and the next two after."
        "I really should have memorized the blurb of each of them or something..."
        "I just hope the others can chime in like Natsuki did."
        "As I take the second book from the desk, I wonder why I even chose four novels."
        mc "So this one is..."
        "What is the book I'm holding even called?"
        mc "It's called..."
        "This is a disaster."
        "What's wrong with me?"
        mc "Um..."
        if monika_type == 1 and ch12_markov_agree:
            show monika 1e zorder 3 at f44
            m "Is something wrong, [player]?"
            m "You seem kinda..."
            m 1l "...I don't know, worried?"
            m "Maybe you've forgotten what the book is about?"
        else:
            show monika 1a zorder 3 at f44
            m "Is everything okay?"
            m 1e "You seem troubled, [player]."
            m "As if you have no idea what you're going to say."
            m "Do you even know what your books are about?"
        show monika zorder 2 at t44
        mc "I..."
        "I look around the room."
        "No one meets my eyes."
        "I suppose I should admit it."
        "Going on like this will only make things worse, won't it?"
        mc "I don't know what my books are about."
        mc "I think it's best that we don't vote on them."
        mc "I can't even tell you guys what they're about."
        mc "I'm sorry I didn't come prepared."
        show natsuki 2e zorder 3 at f41
        n "I can't believe you."
        n "Why did you even choose those books if you don't know what they're about?"
        show natsuki zorder 2 at t41
        mc "I--"
        show yuri 2ph zorder 3 at f43
        y "I thought you would have been more prepared, [player]."
        y "Even Natsuki was able to present her books and she..."
        y "...you know."
        show yuri zorder 2 at t43
        mc "It's my fault, I know."
        mc "I'm sorry, I'll try to do better next time."
        show sayori zorder 3 at f42
        if sayori_personality > 4:
            s 2j "There's not going to be a next time for you."
            $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
            if not list(set(process_list).intersection(stream_list)):
                if currentuser != "" and currentuser.lower() != player.lower():
                    s "I hope you realize that by now, [currentuser]."
            show sayori g1
            s "I've had enough of this!"
            "The room goes silent."
            s 1j "..."
            s "Let's just move on, okay?"
            s "I'm tired of playing games."
        elif sayori_personality == 1:
            s 1h "Look, [player]..."
            s "I'm not angry, I'm just disappointed..."
            s 1k "We'll just forget about it, okay?"
            s "I guess we have enough books to vote on without your four."
        else:
            s 1h "I didn't really expect this to happen."
            s "I suppose I should have, shouldn't I?"
            s 1k "With all the things you've already done..."
            s "Let's just get this over with."
        show sayori zorder 2 at t42
        mc "Sayori..."
        mc "I'm sorry I messed up, I really am."
        mc "I didn't meant to upset anyone."
        show sayori 1g zorder 3 at f42
        s "Just forget about it, [player]."
        s "Everyone else will, after all."
        s "It's not like it's your fault, anyway..."
        show sayori zorder 2 at t42
        mc "W-What...?"
        "Sayori eyes each person in the club."
        "She then turns towards me."
        show sayori 1d zorder 2 at f42
        s "We're all finished here then."
        "Sayori's facial expression changes almost unnaturally..."
        "What just happened?"
    # One Novel Three Manga
    elif ch13_name == "Sayori" or (ch13_name == "Natsuki" and ch13_natsuki_books) or (ch13_name == "Yuri" and not ch13_yuri_books):
        $ ch14_player_manga = 3
        "It's a manga that I've actually read before."
        "I should be able to explain the next three books pretty well."
        if ch13_name == "Natsuki":
            "I made sure to choose different manga to Natsuki."
        else:
            "Somehow the manga I chose are different to Natsuki."
        "Though maybe it would have been better if we had chosen some of the same books."
        "That way there would be less to vote on and it might make the actual voting easier too since she would be voting for the same thing I would be."
        "That's assuming she's going to vote on her books anyway."
        "For all I know, she could be voting for someone else entirely."
        mc "This is kind of your typical superhero manga."
        mc "The main guy in it has to balance their superhero life with their real life."
        mc "It was pretty easy to start off with but one of his enemies was released from prison for good behavior."
        mc "Somehow, she gets a job where the superhero works at in his 'normal' life."
        mc "It makes his life a lot more difficult and it's pretty funny watching how he overcomes it."
        mc "The actual manga doesn't have  that many volumes too, only nine or ten."
        mc "I don't think it'd be a good idea to do a play on all ten though."
        show yuri 2pf zorder 3 at f43
        y "Wouldn't it be easy for the villain to determine who the hero was?"
        y "From the voice, how they move..."
        show yuri zorder 2 at t43
        mc "Well, it's kind of explained in the manga in a comedic way."
        mc "You'll have to read it if you want to find out more."
        label ch14_twomanga:
        "I take the third book from the desk and inspect it."
        "This is probably the one I know the least about since I've only read the first two volumes."
        "It was interesting, I just couldn't find it in myself to invest more money into it when there was better stuff available."
        mc "I'll be honest, I haven't read into this series very much but that doesn't mean I didn't like it."
        mc "It's meant to be a popular series of manga so some of you may have heard of it...or not."
        mc "From what I have read, it's about a team of five people who are competing in some made up sport."
        mc "In their world, the sport is a real thing with it's own rules and stuff like that."
        mc "It's about their struggle to reach the top and becoming better friends."
        show sayori 1o zorder 3 at f42
        s "Becoming better friends?"
        s "If they were on a team, wouldn't they already be friends?"
        show sayori zorder 2 at t42
        mc "The teams are chosen based on a skillset."
        mc "So five people with compatible skills were put into a team."
        mc "They don't like each other at the beginning but despite that they're still one of the best teams of the sport."
        mc "It might be interesting to do a play on that and show the people how the sport works."
        mc "Or we could just change it to something everyone knows about for the play."
        "Or we might not even choose this book for the play."
        "That's also a possibility."
        mc "I'll just talk about my last book then."
        mc "If you couldn't already tell from the cover, it's a manga."
        mc "It's not really well known but it's actually one of the series I like the most."
        mc "I guess you could say it's a book that describes me pretty well."
        if monika_type == 0:
            show monika 1b zorder 3 at f44
            m "In what way does it do that?"
            m "I'm curious to hear just how exactly it describes you, [player]."
        elif monika_type == 1 and ch12_markov_agree:
            show monika 1b zorder 3 at f44
            m "How exactly does it describe you well?"
            m "Does it somehow describe your personality?"
            m "Maybe you're exactly like one of the characters?"
        else:
            show monika 1b zorder 3 at f44
            m "Does it now?"
            m "How so, [player]?"
        show monika zorder 2 at t44
        mc "Well, one of the characters acts pretty similarly to me."
        mc "Or at least how I want to be."
        mc "The story of the book kind of relates to my life too."
        mc "Between all the people I've met and how I've lived my life, it just gets me."
        show yuri 2pe zorder 3 at f43
        y "So what is it about, then?"
        show yuri zorder 2 at t43
        mc "It's about this ordinary guy who lives an ordinary life."
        mc "He goes to an ordinary school and does ordinary things."
        mc "He's not really good at anything and he's passing school."
        mc "One day he wonders what he can do to change his life but can't think of anything."
        mc "The things he tries only end in complete failure."
        mc "He thinks that he has to live the rest of his life as an average person, never to achieve great things."
        mc "Then one day some random person gives him a phone that can make things happen."
        mc "All he has to do is text a number and a few minutes later the thing he texted will happen."
        mc "He's not sure how to use the phone, but tries to be good."
        show sayori 2a zorder 3 at f42
        s "Are you saying you're also trying to be good?"
        s "That if you had a power like that, then you'd also try to do good things?"
        show sayori zorder 2 at t42
        mc "When faced with a power like that, it's hard not be selfish."
        mc "You could do almost anything..."
        mc "It's like a battle of internal morals."
        show sayori 2c zorder 3 at f42
        s "I see..."
        s "I still don't really get how this character is like you though, [player]."
        s "Apart from being average, there's nothing else I can really think of that makes you relate to the book so much."
        show sayori zorder 2 at t42
        mc "I don't know if this is spoiling too much..."
        mc "But he's got a best friend that he relies on for a lot of his decisions."
        mc "I like to compare her with you, Sayori."
        show sayori 1l zorder 3 at f42
        s "With me...?"
        s "H-How come?"
        show sayori zorder 2 at t42
        mc "Well, when we were younger..."
        mc "I'd rely on you a lot to be there."
        mc "But as we grew up, it switched around...didn't it?"
        mc "You began to rely on me for the smallest things."
        mc "I guess it became pretty obvious why."
        "Sayori simply smiles at me."
        "I think she knows what I'm talking about as well."
        mc "Anyway, I think you need to read the manga to really find out why I relate with it so much."
        mc "I can only explain something so well."
        mc "But yeah..."
        mc "Those are my choices."
        mc "Not the best, I know."
        mc "Let's just completely forget I even suggested the first one."
        mc "It's probably better that way."
        show sayori zorder 2 at f42
        s "So I guess everyone's finished sharing their books."
    # Two Novels Two Manga
    else: #if (ch13_name == "Monika" and monika_type == 0) or (ch13_name == "Yuri" and ch13_yuri_books):
        $ ch14_player_manga = 2
        if ch13_name == "Yuri" and ch13_yuri_books:
            "The book I took from Yuri."
            "It's something I can actually talk about."
            "I didn't want to disappoint her so I actually read a little bit of it."
            "It's not something that represents me or the stuff I actually like to read but at least it won't sound as terrible as my first explanation."
            "I even read a plot summary of it online, just to spoil myself a little bit."
            "I should be able to use that."
            mc "This book was actually something Yuri showed me."
            mc "It's a pretty light horror novel, no deaths or anything like that."
            mc "I think it could be interesting to do a play on."
            show sayori 2h zorder 3 at f42
            s "So this isn't actually something you'd read, [player]?"
            show sayori zorder 2 at t42
            mc "Well, I wouldn't say that."
            mc "I'm willing to read a lot of things."
            show sayori 2i zorder 3 at f42
            s "But you said Yuri gave it to you, right?"
            s "So it doesn't really represent you."
            show sayori zorder 2 at t42
            show yuri 2pq zorder 3 at f43
            y "I didn't force [player] to choose it or anything, Sayori."
            y "He chose it of his own volition."
            y "He didn't have to bring it to share either."
            y "I think we should just let him talk."
            show sayori 1c zorder 3 at f42
            show yuri zorder 2 at t43
            s "Alright, Yuri."
            s "If that's really what happened then I suppose there's no problem."
            s 1a "[player], go on."
            show sayori zorder 2 at t42
            "Sayori seems a little annoyed by the scenario."
            "Maybe I should have just chosen books that I would have actually liked to bring in..."
            mc "It's about a ghost haunting a school."
            mc "He's actually a really mischievous ghost and he likes to play tricks on the students."
            mc "The interesting thing about the book is that it's written from two different perspectives."
            mc "When you're reading from the ghost's perspective, you can see he does this for entertainment."
            mc "From the student's perspective, it's seems more like a horror."
            mc "They see supposedly dead people and weird stuff happening around the school."
            show yuri 3pa zorder 3 at f43
            y "I've read the book [player] is talking about and..."
            y "I'd like to say that at some point it begins to merge the two perspectives."
            y "So it isn't too confusing."
            y 3pc "It's a really appropriate choice for the play."
            y "But I suppose I'm a little bit bias since I'm the one who gave the book to him."
            show yuri zorder 2 at t43
            mc "Ah...yeah."
            mc "I was going to mention that but I thought it would have been too much of a spoiler."
            mc "I am enjoying the novel so far though."
            mc "I haven't finished but it did keep my interest in the parts that I did read."
            show natsuki zorder 3 at f41
            n "You haven't even finished the book? What's the point of even suggesting it then?"
            n "It could be terrible!"
            show natsuki zorder 2 at t41
            show yuri 3pb zorder 3 at f43
            y "Natsuki, I assure you it isn't terrible."
            y "You have to believe me."
            show natsuki 1g zorder 3 at f41
            show yuri zorder 2 at t43
            n "...Fine."
            show natsuki zorder 2 at t41
            mc "I don't think it will be terrible."
            mc "But you haven't heard my other two books yet."
            jump ch14_twomanga
        else:
            "I really should have taken a novel that I've read."
            "There's no way I'm going to be able to explain this one."
            if ch13_name == "Natsuki" and not ch13_natsuki_books:
                "I even took this book from Natsuki's house."
                "I should have asked her what it was about."
                "Even a brief description..."
                "Because I have no idea what it's about."
            "Is it better if I just say that?"
            "I had an opportunity last night to read this book or at least find a summary, so why didn't I?"
            "It's too late now..."
            "Maybe I'll just say it's no good."
            "What will [ch13_name] think? I borrowed this from her, didn't I?"
            "Will she think any less of me because of it?"
            "Just how much of this do I remember...?"
            "I think for a moment."
            "Everyone's just staring at me."
            "Waiting for me to say something."
            menu:
                "Do I tell them or try to make it up?"
                "Tell them.":
                    $ sayori_personality += 1
                    "I guess I should just tell them."
                    "I don't want to dig an even deeper hole for myself."
                    mc "Instead of embarassing myself even further, I'll be honest with you all."
                    mc "I have no idea what this book is about."
                    mc "I know it's popular and I did read a little bit of it but I can't seem to remember."
                    mc "So instead of lying, I'm just going to say that."
                    "Everyone simply looks at me."
                    "Sayori doesn't look impressed but lets out a small smile after a while."
                    show sayori 1d zorder 3 at f42
                    s "At least you're honest about it, [player]."
                    s "It's better than pretending and not knowing what you're talking about completely."
                    show sayori zorder 2 at t42
                    "That's a better reaction than what I was expecting."
                    mc "I'll make it up with my next two explanations, I promise."
                    jump ch14_twomanga
                "Make it up.":
                    $ ch14_twonovels_tell = True
                    "I already disappointed them with my first book."
                    "I have to make it up to them."
                    mc "So...this book..."
                    "I desperately try to remember all the things I can about this book."
                    "I see Sayori looking at me curiously."
                    if sayori_personality < 3:
                        "She sighs then smiles at me."
                        "Suddenly, I can remember everything about this book and more."
                        mc "If you didn't already know, it's about five friends who camp out in the wilderness."
                        mc "A really bad storm happens and they have to take shelter in a cave."
                        mc "They find something really strange in the cave and suddenly pass out."
                        mc "When they wake up, they're back at their campsite and find they have new powers."
                        mc "Each of them can do different things, one can move stuff with their mind and the other can set things on fire just by looking at it."
                        mc "They have no idea what to do with their power, since they're only teenagers."
                        mc "So they use it to make their lives a lot easier."
                        mc "Eventually the government notices this and..."
                        mc "Well, you probably know what happens next."
                        show natsuki 1d zorder 3 at f41
                        if ch13_name == "Natsuki":
                            n "I thought you just picked up a random book, [player]."
                            n "I kinda thought you would mess it up again."
                        else:
                            n "I didn't know you read this kinda stuff, [player]."
                            n "I thought it would be like your first explanation."
                        n "Where you didn't really know what you were talking about."
                        n "I'm impressed!"
                        show natsuki zorder 2 at t41
                        mc "Uh...thanks?"
                        "Was that a compliment or an insult...?"
                        mc "I didn't know I knew this much about it too."
                        mc "I must have really liked the book or something."
                        show sayori 1q zorder 3 at f42
                        s "Ehehe, it's probably the 'or something', [player]!"
                        show sayori zorder 2 at t42
                        mc "Whatever it is, I'm glad I didn't mess it up."
                        mc "I still have my other two books to talk about though..."
                        jump ch14_twomanga
                    else:
                        $ ch14_player_choice = False
                        $ sayori_personality += 2
                        "She just sighs and waits for my answer."
                        "This isn't good, is it?"
                        mc "We've probably all heard of it before."
                        mc "We know the story already."
                        mc "It's um..."
                        "I look at the cover and see a cave."
                        mc "About some time travellers who go back in time to the bronze age."
                        mc "They go--"
                        show natsuki 1h zorder 3 at f42
                        n "[player]...I don't think that's right at all."
                        n "It's about going on camp..."
                        show natsuki zorder 2 at t42
                        show yuri 3pf zorder 3 at f43
                        y "I think it would have been better if you didn't say anything at all, [player]."
                        y "If you don't know what the book is about, then you shouldn't have tried to improve something."
                        y "It's what I would have done, in your situation."
                        show yuri zorder 2 at t43
                        mc "You're right, Yuri."
                        mc "I guess I thought I could have made something up."
                        show sayori 1c zorder 3 at f42
                        s "You really should have chosen something you liked, [player]."
                        s "I can understand choosing popular novels because it would appeal to more people..."
                        s "But you should at least be able to talk about them."
                        "Sayori takes a deep breath."
                        s 1f "In the end, I'm more upset that you lied to us."
                        s 1b "You should have just admitted it."
                        show sayori zorder 2 at t42
                        mc "You're right, Sayori."
                        mc "Sorry about that..."
                        show sayori zorder 3 at f42
                        if sayori_confess and not sayori_dumped:
                            s 1d "[player], I love you and everything..."
                            s 1l "But save yourself the embarassment and just skip your next two books."
                            s "Alright?"
                        else:
                            s 1k "I don't even want to hear your next two choices."
                            s "It's just a waste of our time and we don't have a lot left."
                        show sayori zorder 2 at t42
                        mc "Okay..."
                        "I take the four books from the desk and place them in my bag."
                        mc "Sorry again."
                        show sayori 1d zorder 3 at f42
                        s "Don't say sorry to me, [player]."
                        s "Say sorry to everyone else who's time you wasted..."
                        s "Um...not to sound mean or anything."
                        show sayori zorder 2 at t42
                        mc "No, I understand."
                        mc "Sorry, everyone."
                        show yuri 3ph zorder 3 at f43
                        y "It's no problem, I suppose."
                        y "There's still plenty of books to choose from."
                        show natsuki 2e zorder 3 at f41
                        show yuri zorder 2 at t43
                        n "Yeah, I'm fine."
                        n "A little annoyed at {i}you{/i} if anything."
                        n 2g "But fine."
                        show natsuki zorder 2 at t41
                        if monika_type == 0:
                            show monika 2j zorder 3 at f44
                            m "Ahaha, it's fine, [player]."
                            m "Mistakes like this happen..."
                            m "Okay, well maybe not like this but I forgive you!"
                        elif monika_type == 1 and ch12_markov_agree:
                            show monika 2j zorder 3 at f44
                            m "Not a problem, [player]."
                            m "It's only a small thing, so of course I forgive you!"
                        else:
                            show monika 2c zorder 3 at f44
                            m "No harm done."
                        show sayori 1c zorder 3 at f42
                        show monika zorder 2 at t44
                        s "All is forgiven I guess!"
                        s "So now that that's over with..."
    s 1d "Alright, everybody!"
    s "It felt like a long time, but we're finally done!"
    s 1q "So let's start voting!"
    "Sayori begins to get up but stops."
    s 1b "Actually, before we vote..."
    s "You all have to be one hundred percent committed with the books you brought."
    s "Any one of them could turn out to be the play."
    s "Take some away now if you didn't really intend for them to be part of the play."
    s "Maybe you just wanted to share it..."
    s "Or maybe you're having second thoughts about the books you actually brought after seeing everyone else's."
    show natsuki 1c zorder 3 at f41
    show sayori zorder 2 at t42
    n "I'm not entirely opposed to the idea..."
    n "But why would we change our minds now?"
    n 1b "You were the one who told us to bring a couple of books, you never gave us a specific amount."
    n "In fact, I probably could have brought more if there wasn't a limit."
    show natsuki zorder 2 at t41
    show sayori 1a zorder 3 at f42
    s "I'm not saying you have to!"
    s "But think of the worse case scenario."
    s "I clearly didn't yesterday when I told you all to pick some books."
    show sayori zorder 2 at t42
    show yuri 2pe zorder 3 at f43
    y "What's the worst case scenario?"
    show yuri zorder 2 at t43
    if monika_type == 0:
        show monika 3a zorder 3 at f44
        m "I think Sayori is talking about voting on the books."
        m "In the worst case, we'd all have votes in five different books."
        m 3b "That would cause a stalemate and we wouldn't have a clear choice."
        m "I think there a couple of ways we could deal with that."
        m "One of them being to narrow down the book list."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 3a zorder 3 at f44
        m "Sayori is probably talking about voting on the books."
        m "If we voted as we are now, we'd probably get five votes on five different books."
        m 3b "In that case, there would be no winner at all."
        m "There are a few days we could deal with it."
        m "I think the one Sayori is thinking of is narrowing down the book list."
    else:
        show monika 3c zorder 3 at f44
        m "I think I can see what you're trying to get at, Sayori."
        m "As it is, there's plenty of books to choose from."
        m "In the worst case, we'd all choose a different book to vote on."
        m 3a "Does that mean you're suggesting we narrow down the book list?"
    show sayori 2d zorder 3 at f42
    show monika zorder 2 at t44
    s "That's exactly it!"
    s "We'd be here forever if we kept voting based on all the books we have since we might not even change votes."
    s "So we should definitely try to narrow it down."
    s "I know you all probably have a favorite book out of the ones you brought in."
    s "So maybe just keep that and put the rest away?"
    s "It's up to you..."
    s 2l "I really should have made everyone just choose one book from the beginning."
    s "It's too late for that now, though."
    s 2j "If you really, really want to do a play based on any of your books then keep them on the desk."
    s 2d "If not, then put them away."
    s "Just think about it carefully, okay?"
    show natsuki 2q zorder 3 at f41
    show sayori zorder 2 at t42
    n "Well...I did say that my novel was a backup."
    n "I guess I can put that away."
    n 2s "And I suppose the other two manga I brought aren't really what I want to do a play on."
    n "So I guess that leaves me with third book I brought which is about that alien."
    n "It's the story I like the most because it's just so sweet..."
    n 2j "I'm sure the audience will think the same thing if we vote for it."
    show natsuki zorder 2 at t41
    show sayori 1h zorder 3 at f42
    s "Are you completely sure, Natsuki?"
    s "I don't want it to feel like I'm forcing you to do this or anything!"
    s "I just want to make it easier for when we vote."
    show natsuki 2c zorder 3 at f41
    show sayori zorder 2 at t42
    n "It's fine, Sayori."
    n "I didn't really bring those in and expect them to get chosen."
    n 2d "I'm kinda glad I just got to share them."
    n "It feels...good to share some of the stuff I read."
    n 1c "I know you guys might never actually read those books..."
    n 1a "But maybe you will, and that's enough for me."
    "Natsuki puts the three books into her bag."
    show natsuki zorder 2 at t41
    show sayori 1q zorder 3 at f42
    s "That was well said, Natsuki!"
    s 1a "It makes things a bit easier now."
    s "Is anyone else going to do it too?"
    "Sayori looks around the table."
    show sayori zorder 2 at t42
    if monika_type == 0:
        show monika 1m zorder 3 at f44
        m "I suppose I can get rid of three of mine as well."
        m "I should be making things easier for you all as vice president after all."
        m "Hmm..."
        "Monika looks at the four books she brought with her."
        "She takes three of them, leaving behind 'Sound of your Heartbeat' on the table."
        m 1e "I think this one would be the most appropriate."
        m "I also think it's the easiest to do a play on."
        m "Things will come naturally, I can almost guarantee it."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1a zorder 3 at f44
        m "If that's what we're doing..."
        m "Then I suppose it's my duty as the vice president to make things easier."
        m "So..."
        "Monika looks at the four books she brought with her."
        "She takes three of them, leaving behind 'Sound of your Heartbeat' on the table."
        m 1e "I think this is the obvious choice."
        m "It will be easier to do a play on."
        m "I also have a feeling it will come naturally to all of us."
    else:
        show monika 1c zorder 3 at f44
        m "Well, I already have the one book."
        m 1a "There's nothing I can really do here except get rid of my books entirely."
        m "I do want it to be a choice though so I won't be doing that."
        show sayori 1d zorder 3 at f42
        show monika zorder 2 at t44
        s "I won't ask you to do that."
        s "It would be unfair for you."
        show sayori zorder 2 at t42
        show monika 1b zorder 3 at f44
        m "If you say so, Sayori."
    show sayori 2a zorder 3 at f42
    show monika zorder 2 at t44
    s "What about you, Yuri?"
    s "Are you gonna keep all your books?"
    s "You can if you want to, the number is already pretty small..."
    show sayori zorder 2 at t42
    show yuri 2ph zorder 3 at f43
    y "I was actually about to ask you the same question, Sayori."
    y "Getting rid of books was your idea after all."
    y "Yet you haven't got rid of any of your books yet."
    y 2pf "You're the president of the club, shouldn't you be taking some responsibility?"
    show sayori 1l zorder 3 at f42
    show yuri zorder 2 at t43
    s "I guess you have a point there, Yuri."
    show sayori 1k
    "Sayori looks at all four of her books intently."
    s "I do like all of them."
    s 1d "But it's not fair that I'm the one asking you all to narrow down your books but not do the same thing."
    s "So...I'll choose the fourth book I talked about."
    "Sayori carefully picks up the other books and puts them into her bag."
    s "The one about the people with cancer."
    s "It's not the easiest book to do it on but I'd like to see us try at least."
    s 4q "I'm sure if we put our all into it then we can do an amazing job!"
    show sayori zorder 2 at t42
    show yuri 3ph zorder 3 at f43
    y "Well...since everyone else is doing it..."
    y 3pi "I suppose I should as well."
    "Yuri examines her four books."
    y 3pg "I actually chose these books because I knew they wouldn't be too horrific."
    y "It took me quite a while to come up with a list of books that wouldn't deter anyone completely..."
    show natsuki 1b zorder 3 at f41
    show yuri zorder 2 at t43
    n "Yuri, if it really took you that long..."
    n "Then you don't need to get rid of one of any books."
    n "The number of books we have is already short enough."
    show natsuki zorder 2 at t41
    show sayori 1c zorder 3 at f42
    s "Natsuki is right."
    s "If you don't want to get rid of any of your books then you don't have to."
    show sayori zorder 2 at t42
    show yuri 3pf zorder 3 at f43
    y "No...that would be hypocritical of me."
    y "I asked you to remove some of your books, I should do the same."
    y 3pa "Besides...I've already chosen the book I want to do it on."
    if monika_type == 0:
        show monika 2a zorder 3 at f44
        m "Is it the one about the stalker?"
    elif monika_type == 1 and ch12_markov_agree:
        show monika 2a zorder 3 at f44
        m "The one about the stalker, right?"
    else:
        show monika 2a zorder 3 at f44
        m "Which one? The one with the stalker?"
    show yuri 3pb zorder 3 at f43
    show monika zorder 2 at t44
    y "Actually, it's the first book I talked about."
    y "The one about the radio and the entity controlling people."
    y "It's got plenty of supernatural themes that I think could translate really well in a play."
    y 3ph "Though I suppose horror isn't for everyone..."
    y 3pa "Still, maybe we can change some minds about it if we vote for it."
    "Yuri takes the other three books and places them in her bag."
    if ch14_player_choice:
        y "Though that still leaves...[player]."
        show yuri zorder 2 at t43
        mc "Ah...right."
        mc "Everyone else only has one book."
        mc "I guess my choice here is obvious."
        mc "It's the manga about the guy who is ordinary."
        mc "The other manga I don't really relate to as much..."
        if ch13_yuri_books:
            mc "And the book Yuri gave me, while interesting, I don't know enough about."
            "I look towards Yuri and she gives me a nod of understanding."
        mc "So if we're narrowing it down to just one choice, I guess that's it."
        show sayori 1d zorder 3 at f42
        s "So now there's only five books to choose from."
    else:
        y 2ps "[player] doesn't have any books that we can vote on..."
        y "So I guess that's it."
        show sayori 1n zorder 3 at f42
        show yuri zorder 2 at t43
        s "Wow, we actually managed to narrow it down to four books!"
    s 1a "I'm sure we can easily get a winner out of all this in one go."
    s "So here's how the voting process is gonna work."
    "Sayori pulls out a box from her bag and five small pieces of paper."
    s "We should do it animosity."
    show sayori zorder 2 at t42
    show yuri 3po zorder 3 at f43
    y "Animosity means strong hostility, Sayori."
    y 3pp "D-Do you want us yelling at each other?"
    y 3pq "Or maybe you meant anonymously."
    y "Which means in secret."
    show sayori 1l zorder 3 at f42
    show yuri zorder 2 at t43
    s "Ehehe, really?"
    s "I didn't know they were different words!"
    s 1q "But yeah, we're going to do it {i}anonymously{/i}."
    s "So that we don't get influenced by what others are voting on."
    "Sayori gives us all a small piece of paper."
    s 2a "You can write the book you want on that."
    s "Once you finish, fold it and put it in this box."
    s "Then when everyone's done, we'll see what we all voted for!"
    s "If you need time to think or anything, then take a minute now."
    show sayori zorder 2 at t42
    if natsuki_date and natsuki_approval > 2:
        "Natsuki leans towards me and whispers."
        show natsuki 4q zorder 3 at f41
        n "[player]...what book are you voting for?"
        n "I was originally going to vote for my book."
        n "But after all you've done for me, I'd like to make sure the one you choose..."
        n "Is the one that becomes the play."
        n "It doesn't have to be mine or anything..."
        n 4s "It's not like I'd get mad at you if you don't vote for me."
        show natsuki zorder 2 at t41
        mc "Natsuki...you don't have to do that."
        mc "Just because we're dating doesn't mean--"
        show natsuki 4o zorder 3 at f41
        n "Look, just tell me."
        n 4i "Before I change my mind."
        show natsuki zorder 2 at t41
        mc "Well..."
        if not persistent.markov_agreed or monika_type == 0:
            menu:
                mc "I was going to vote for..."
                "Natsuki.":
                    $ ch14_book_choice = "Natsuki"
                    $ ch14_natyuri_choice[0] = "Natsuki"
                    mc "You, actually."
                    mc "I think your manga could be really fun to do a play on."
                    mc "And it sounds really wholesome too."
                    mc "People will love it."
                "Yuri.":
                    $ ch14_book_choice = "Yuri"
                    $ ch14_natyuri_choice[0] = "Yuri"
                    mc "I was thinking Yuri's book could be an interesting play."
                    mc "It's horror but it might be fun."
                "Monika.":
                    $ ch14_book_choice = "Monika"
                    $ ch14_natyuri_choice[0] = "Monika"
                    mc "Monika's book seems really interesting to me."
                    mc "I think it'd make a great play."
                "Sayori.":
                    $ ch14_book_choice = "Sayori"
                    $ ch14_natyuri_choice[0] = "Sayori"
                    mc "Sayori's book is really sad"
                "Myself." if ch14_player_choice:
                    $ ch14_book_choice = player
                    $ ch14_natyuri_choice[0] = player
                    mc "Well...my own book."
                    mc "I know it sounds kinda selfish but I think it's a great book."
            if ch14_book_choice != "Natsuki":
                show natsuki 2c zorder 3 at f41
                n "Really? Well, alright then..."
                n "I hope you know what you're doing..."
            else:
                show natsuki 2d zorder 3 at f41
                n "I'm not gonna argue with that choice."
                n "Thank you, [player]."
        else:
            $ ch14_book_choice = "Monika"
            $ ch14_natyuri_choice[0] = "Monika"
            mc "It's Monika."
            mc "I was going to vote for Monika."
            show natsuki 2c zorder 3 at f41
            n "You sound really sure of yourself."
            n "I hope you know what you're doing..."
        show natsuki zorder 2 at t41
        "Natsuki leans back and writes something down on her paper."
        "She then looks at me, folds the piece of paper and puts it into the box."
    elif yuri_date and yuri_approval > 2:
        "Yuri leans towards me and whispers."
        show yuri 3pe zorder 3 at f43
        y "I was going to vote for the book I brought in..."
        y 3pa "But I want to give you something, [player]."
        y "I'd like to know what you're voting for..."
        y "So that we can make it the one to do a play on."
        show yuri zorder 2 at t43
        mc "Eh? Yuri are you sure about that?"
        mc "I don't want to pressure you just because we're dating."
        show yuri 3pb zorder 3 at f43
        y "I'm sure."
        y "Just tell me, quickly."
        y "I won't be offended if you don't choose me."
        show yuri zorder 2 at t43
        mc "Well..."
        if not persistent.markov_agreed or monika_type == 0:
            menu:
                mc "I was going to vote for..."
                "Natsuki.":
                    $ ch14_book_choice = "Natsuki"
                    $ ch14_natyuri_choice[1] = "Natsuki"
                    mc "I was thinking of Natsuki's manga."
                    mc "It sounds really wholesome and appropriate for a play."
                "Yuri.":
                    $ ch14_book_choice = "Yuri"
                    $ ch14_natyuri_choice[1] = "Yuri"
                    mc "You, actually."
                    mc "I know it's a horror book but it could be really interesting to see people's reactions to it."
                    mc "And it could be fun."
                "Monika.":
                    $ ch14_book_choice = "Monika"
                    $ ch14_natyuri_choice[1] = "Monika"
                    mc "Monika's book seems really interesting to me."
                    mc "I think it'd make a great play."
                "Sayori.":
                    $ ch14_book_choice = "Sayori"
                    $ ch14_natyuri_choice[1] = "Sayori"
                    mc "Sayori's book is really sad"
                "Myself." if ch14_player_choice:
                    $ ch14_book_choice = player
                    $ ch14_natyuri_choice[1] = player
                    mc "Well...my own book."
                    mc "I know it sounds kinda selfish but I think it's a great book."
            if ch14_book_choice != "Yuri":
                show yuri 2pa zorder 3 at f43
                y "If that's your choice, then I'll respect it."
                y "Let's hope it's a great play."
            else:
                show yuri 2pc zorder 3 at f43
                y "You're too kind, [player]."
                y 2pb "You won't regret this choice, I promise."
        else:
            $ ch14_book_choice = "Monika"
            $ ch14_natyuri_choice[1] = "Monika"
            mc "It's Monika."
            mc "I was going to vote for Monika."
            show yuri 2pf zorder 3 at f43
            y "You sound really sure of yourself..."
            y 2pb "Let's hope it means this is going to be a great play."
        show yuri zorder 2 at t43
        "Yuri leans back and writes something on the paper in front of her."
        "She looks around before neatly folding the paper and putting it into the box."
    else:
        if not persistent.markov_agreed or monika_type == 0:
            menu:
                "Who am I voting for?"
                "Natsuki":
                    $ ch14_book_choice = "Natsuki"
                    $ natsuki_approval += 1
                    "Natsuki's manga is really wholesome."
                    "It could be fun to do a play on something that will make everyone smile."
                "Yuri.":
                    $ ch14_book_choice = "Yuri"
                    $ yuri_approval += 1
                    "I should vote for Yuri's book."
                    "It seems like it could be interesting since it's apparently a pretty light horror book."
                    "I wonder how it will turn out as a play."
                "Monika.":
                    $ ch14_book_choice = "Monika"
                    "I think Monika's book is the best one here to do a play on..."
                    if monika_type == 0:
                        "Even with all the romantic themes."
                    else:
                        "Even with how strange it is for her to choose a book like that."
                    "So that's the one I'll vote for."
                "Sayori.":
                    if sayori_personality > 0:
                        $ sayori_personality -= 1
                    $ ch14_book_choice = "Sayori"
                    "Sayori's book sounds really sad but...real for some reason."
                    "I'm interested to see what kind of play that could turn out to be."
                "Myself." if ch14_player_choice:
                    $ ch14_book_choice = player
                    "I do like the manga that I chose to bring."
                    "And seeing it as a play might be really interesting."
                    if monika_type == 0:
                        "I notice Monika look at me from the corner of my eye."
                        "She looks like she crossed out something on her piece of paper."
                        "I wonder what she was doing..."
                    elif sayori_personality == 0 or (sayori_confess and not sayori_dumped):
                        "Out of the corner of my eye, I see Sayori look towards me."
                        "She rolls her eyes and smiles slightly."
                        "I wonder what that was about...?"
        else:
            $ ch14_book_choice = "Monika"
            "I already know what I'm voting for."
            "There's no competition."
            "It has to be Monika's book, obviously."
        "Everyone else puts their piece of paper into the box."
    "I write down my choice then fold my piece of paper and put it into the box."
    "I wonder who everyone else voted for?"
    "It was probably themselves, right?"
    "It would only make sense."
    if ((natsuki_date and natsuki_approval > 2) or (yuri_date and yuri_approval > 2)) and ch14_player_choice:
        if natsuki_date:
            "So what would have happend if Natsuki didn't ask who I was voting for?"
        else:
            "So what would have happened if Yuri didn't vote with me?"
        "Would we all have ended up with one vote?"
        "There wouldn't be a winner in that case, right?"
        "So how would we go about it then?"
        "Maybe Sayori has some sort of backup plan."
    elif ch14_book_choice == player:
        "Maybe everyone voted for themselves."
        "I voted for myself..."
        "Does that mean we all have one vote?"
        "How is it going to work if that's the case?"
        "If we do a revote, then we're still going to vote on our own books."
        "Unless Sayori has some sort of plan..."
    show sayori 2a zorder 3 at f42
    s "Alright, everybody!"
    s "We've all made our votes."
    s "So why don't we see who we all voted for?"
    s 2d "Don't worry, I'm not going to say who voted for who..."
    s "Even though I can kinda tell from your handwriting."
    s "I'll just count up the votes."
    "Everyone turns towards Sayori as she opens the lid of the box."
    "She turns it upside down and five folded pieces of paper fall out of it."
    s 2c "Let's see here..."
    "She picks up the first piece of paper and unfolds it."
    # Monika votes for player
    if monika_type == 0 and ch14_book_choice == player and not ((natsuki_date and natsuki_approval > 2) or (yuri_date and yuri_approval > 2)):
        $ ch14_votes[4] += 1
        s 2l "It's a vote for...[player]."
        s "Ehehe, alright then..."
    # Monika votes for herself
    else:
        $ ch14_votes[2] += 1
        s 2a "It's a vote for Monika!"
        s "I wonder if the book we end up choosing will be hers."
    s 2b "Anyway, we still have four more to go."
    s "It's still anyone's book at this point."
    "Sayori picks up another piece of paper."
    s "And this vote goes to..."
    "She unfolds it."
    # Natsuki votes for player choice
    if ch14_natyuri_choice[0] != "Natsuki":
        if ch14_natyuri_choice[0] == "Yuri":
            $ ch14_votes[1] += 1
        elif ch14_natyuri_choice[0] == "Monika":
            $ ch14_votes[2] += 1
        elif ch14_natyuri_choice[0] == "Sayori":
            $ ch14_votes[3] += 1
        else:
            $ ch14_votes[4] += 1
        if ch14_natyuri_choice[0] == "Sayori":
            s 2q "Oh look, it's a vote for me!"
        else:
            s 2n "It's a vote for [ch14_natyuri_choice[0]]. "
        s "Alright, then..."
    # Natsuki votes for herself
    else:
        $ ch14_votes[0] += 1
        s 2d "It looks like Natsuki got a vote."
        s "Moving on..."
    "Sayori discards the second piece of paper and picks up the third one."
    s 2c "Three more to go!"
    "She quickly unfolds it."
    # Yuri votes for player choice
    if ch14_natyuri_choice[1] != "Yuri":
        if ch14_natyuri_choice[1] == "Natsuki":
            $ ch14_votes[0] += 1
        elif ch14_natyuri_choice[1] == "Monika":
            $ ch14_votes[2] += 1
        elif ch14_natyuri_choice[1] == "Sayori":
            $ ch14_votes[3] += 1
        else:
            $ ch14_votes[4] += 1
        if ch14_natyuri_choice[1] == "Sayori":
            s 2q "A vote for me!"
        else:
            s 2a "A vote for [ch14_natyuri_choice[1]]."
    # Yuri votes for herself
    else:
        $ ch14_votes[1] += 1
        s 2d "So this is a vote for Yuri."
    s "I don't think we have a clear choice yet."
    s 2o "So let's keep going."
    show sayori zorder 2 at t42
    show yuri 3pa zorder 3 at f43
    y "This is thrilling, in a way."
    y "I wonder whose book is going to win..."
    show sayori 2d zorder 3 at f42
    show yuri zorder 2 at t43
    s "It's not really a competition or anything."
    s "But I'm also excited to see whose book is going to be chosen."
    s 2a "Anyway, let's see what the next vote is."
    "Sayori unfolds the fourth piece of paper."
    # Sayori votes for player
    if ((sayori_confess and not sayori_dumped) or sayori_personality == 0) and ch14_book_choice == player:
        $ ch14_votes[4] += 1
        s 2d "Ah..."
        "She looks at it and smiles weakly."
        s "It's a vote for [player]."
    # Sayori votes for herself
    else:
        $ ch14_votes[3] += 1
        s 2q "Look like it's a vote for me!"
    "Sayori puts the paper aside with the other ones that have been counted."
    s 1b "That still isn't enough votes to have a majority yet."
    # Everyone has one vote so far
    if ch14_votes[0] < 2 and ch14_votes[1] < 2 and ch14_votes[2] < 2 and ch14_votes[3] < 2 and ch14_votes[4] < 2:
        s 1c "If there isn't a majority by the end of everything then we'll just go with who has the most votes."
        s "Which will be two..."
        show natsuki 2c zorder 3 at f41
        show sayori zorder 2 at t42
        n "Only two votes?"
        n "It's not a majority but I guess it makes sense."
        show natsuki zorder 2 at t41
        show sayori 1a zorder 3 at f42
        s "It just makes things easier."
        s "There are only five of us after all."
    # Someone has two votes
    else:
        s 1c "We might actually get a majority vote."
        s "It only takes three after all."
        show natsuki 2c zorder 3 at f41
        show sayori zorder 2 at t42
        n "It only takes three votes?"
        n "I guess that makes sense."
        show natsuki zorder 2 at t41
        show sayori 1a zorder 3 at f42
        s "Well, there are only five of us."
        s "It might be a tie between two books."
        s 1d "In that case, we'll just do a revote on those two books only."
    s 1b "But there's still one vote that hasn't been counted yet."
    s "So let's see what book it's for..."
    "Sayori takes the last piece of paper and unfolds it."
    if ch14_book_choice == "Sayori":
        $ ch14_votes[3] += 1
        s 1n "It's a vote for me...?"
        s 1l "Ehehe, okay..."
    else:
        if ch14_book_choice == "Natsuki":
            $ ch14_votes[0] += 1
        elif ch14_book_choice == "Yuri":
            $ ch14_votes[1] += 1
        elif ch14_book_choice == "Monika":
            $ ch14_votes[2] += 1
        elif ch14_book_choice == "Sayori":
            $ ch14_votes[3] += 1
        else:
            $ ch14_votes[4] += 1
        s 1c "It's a vote for [ch14_book_choice]."
    s 3a "That's all of them."
    "Sayori holds the box upside down and shakes it."
    show sayori zorder 2 at t42
    mc "Why did you do that?"
    mc "That was five votes."
    show sayori zorder 3 at f42
    s 3l "Just making sure..."
    s "Anyway..."
    if ch14_votes[0] >= 3:
        $ ch14_overall_choice = "Natsuki"
        s 3a "I think I counted three votes for Natsuki's manga."
        s "That means Natsuki has the majority vote!"
    elif ch14_votes[1] >= 3:
        $ ch14_overall_choice = "Yuri"
        s 3a "I'm pretty sure I counted three votes for Yuri's choice."
        s "That means Yuri's book is chosen!"
    elif ch14_votes[2] >= 3:
        $ ch14_overall_choice = "Monika"
        s 3a "That was three votes for Monika's choice..."
        s "That means we're going to do Monika's book!"
    elif ch14_votes[3] >= 3:
        $ ch14_overall_choice = "Sayori"
        s 3c "That was three votes for my choice, right?"
        s 3q "So that means we're doing my book!"
    elif ch14_votes[4] >= 3:
        $ ch14_overall_choice = player
        s 3d "Ehehe, I counted three votes for [player]'s choice.'"
        s "We're doing [player]'s book then!"
    else:
        s 3b "That means there isn't really a majority vote."
        s "So that means that whoever got two votes has their book chosen..."
        label ch14_twovotes:
        if ch14_votes[0] >= 2:
            $ ch14_overall_choice = "Natsuki"
            s 3q "...Which means Natsuki's manga won vote!"
        elif ch14_votes[1] >= 2:
            $ ch14_overall_choice = "Yuri"
            s 3q "...Which means Yuri's book is chosen!"
        elif ch14_votes[2] >= 2:
            $ ch14_overall_choice = "Monika"
            s 3q "...Which means we're going to do Monika's book!"
        elif ch14_votes[3] >= 2:
            $ ch14_overall_choice = "Sayori"
            s 3r "So that means we're doing my book!"
        elif ch14_votes[4] >= 2:
            $ ch14_overall_choice = player
            s 3d "...Looks like we're doing [player]'s book then!"
        else:
            s 3m "Which is no one."
            "Sayori thinks for a second."
            s 3l "Wait...we all voted for ourselves, didn't we?"
            s "How did I not see this coming?"
            show natsuki 2m zorder 3 at f41
            show sayori zorder 2 at t42
            n "So what's going to happen?"
            n "There's no winner, and if we vote again on the same books then it's going to happen again."
            show natsuki zorder 2 at t41
            show sayori 3f zorder 3 at f42
            s "I know, I know!"
            s "What's the easiest way to do this...?"
            show sayori zorder 2 at t42
            if monika_type == 0:
                show monika 1c zorder 3 at f44
                m "One of us could get rid of our book."
                m "That way, there's only four choices but five people."
                m "So we're guaranteed to find a book."
                m 1e "Though it does come at the cost of being a bit unfair..."
            elif monika_type == 1 and ch12_markov_agree:
                show monika 1c zorder 3 at f44
                m "I suggest one of us get rid of our book."
                m "It's the easiest way, though a bit unfair for that person."
                m 1a "At least that way, we're guaranteed to find a result."
            else:
                show monika 1c zorder 3 at f44
                m "It might be easier to just get rid of one of our books."
                m 1d "Since there's five of us and only four books, we're guaranteed to have at least one book with two votes."
                m "There's no other way."
            show sayori 1h zorder 3 at f42
            show monika zorder 2 at t44
            s "I know but..."
            s "I don't want to be mean to anybody."
            s "So I'll ask first."
            s 1k "Is anyone going to volunteer?"
            "I voted for my own book."
            "I don't exactly {i}want{/i} to get rid of it as the choice for the play."
            "Maybe somebody else will...?"
            s 1e "Anyone at all?"
            s "I don't exactly want to force anybody..."
            s "We might have to do it randomly and that will just be worse for whoever is chosen."
            s 2h "So are you all sure you want to do it this way?"
            "Sayori looks at each of us."
            s 2k "Well...alright."
            # High Enough Approval with Natsuki or Yuri makes them get rid of their book and vote for you
            if yuri_approval > 5:
                $ ch14_overall_choice = player
                show sayori zorder 2 at t42
                "Yuri looks at me and notices my concerned look."
                show yuri 3ph zorder 3 at f43
                y "I'm...going to retract my book."
                y "If that's okay with everyone."
                show sayori 2b zorder 3 at f42
                show yuri zorder 2 at t43
                s "E-Eh? What do you mean?"
                show sayori zorder 2 at t42
                show yuri 3pi zorder 3 at f43
                y "I means I'm going to remove my book from the list."
                y "And change my vote."
                show sayori 2g zorder 3 at f42
                show yuri zorder 2 at t43
                s "Yuri, wait!"
                s "Are you completely sure about this?"
                s "I don't want it to feel like I've forced you to do this."
                show sayori zorder 2 at t42
                show yuri 3pa zorder 3 at f43
                y "It's okay, Sayori."
                y "You said you were looking for volunteers."
                y "So I've volunteered myself."
                show sayori 2h zorder 3 at f42
                show yuri zorder 2 at t43
                s "Yeah but..."
                show sayori zorder 2 at t42
                show yuri 3pb zorder 3 at f43
                y "Don't worry. It's my choice."
                y "Now..."
                y 3pf "I only got one vote on my book."
                y "I also voted for my book, which means we all voted for ourselves."
                show natsuki 2c zorder 3 at f41
                show yuri zorder 2 at t43
                n "That makes sense..."
                show natsuki zorder 2 at t41
                show yuri 2pe zorder 3 at f43
                y "I'd like to change my vote."
                y "That makes things easier, doesn't it?"
                y "We won't have to do that whole process again."
                show sayori 2d zorder 3 at f42
                show yuri zorder 2 at t43
                s "I guess it does."
                s "Just choose carefully because whoever you vote for is going to have their book chosen."
                show sayori zorder 2 at t42
                show yuri 2pf zorder 3 at f43
                y "I'm changing my vote to..."
                "Yuri looks around the room."
                y 2pi "...[player]."
                show sayori 1c zorder 3 at f42
                show yuri zorder 2 at t43
                s "Huh? Are you sure about that Yuri?"
                s "I didn't really think you'd be the type to vote for a manga."
                show sayori zorder 2 at t42
                show yuri 1a zorder 3 at f43
                y "I'm sure."
                y "[player] may not have chosen the book I really want to do."
                y "But it's clearly special to him if he's so intent on it."
                y "I want to give him something back after all he's done for me."
                show yuri zorder 2 at t43
                mc "Yuri, you don't need to do this."
                mc "It's entirely your choice."
                show yuri 1b zorder 3 at f43
                y "It's okay, [player]."
                y "I've made up my mind."
                show sayori 1a zorder 3 at f42
                show yuri zorder 2 at t43
                s "Alright, Yuri..."
                s "I guess that means we're doing [player]'s book for the play."
            elif natsuki_approval > 5:
                $ ch14_overall_choice = player
                show sayori zorder 2 at t42
                "Natsuki turns towards me and takes a look at my face."
                show natsuki 2g zorder 3 at f41
                n "Ugh...I can't believe I'm doing this."
                n "I...volunteer to get rid of my book."
                show natsuki zorder 2 at t44
                show sayori 1h zorder 3 at f42
                s "Eh? Are you sure, Natsuki?"
                s "Like I said, I don't want to force anybody if I don't need to."
                show natsuki 2e zorder 3 at f41
                show sayori zorder 2 at t42
                n "I'm sure."
                show natsuki zorder 2 at t41
                show yuri 3pf zorder 3 at f43
                y "That's surprisingly mature of you, Natsuki."
                show natsuki 2f zorder 3 at f41
                show yuri zorder 2 at t43
                n "Ugh! What's {i}that{/i} supposed to mean?"
                show natsuk zorder 2 at t41
                show yuri 3pq zorder 3 at f43
                y "N-Nothing...!"
                show natsuki 2i zorder 3 at f41
                show yuri zorder 2 at t43
                n "And I want to make something clear."
                n "I voted for myself."
                n "Judging by the way the votes are, I'm guessing we all did."
                show natsuki zorder 2 at t41
                show sayori 2l zorder 3 at f42
                s "Ehehe, guess you're right there."
                show natsuki 2h zorder 3 at f41
                show sayori zorder 2 at t42
                n "So since I'm getting rid of my book..."
                n "I want to change my vote."
                n "We're all going to be voting for our book again anyway."
                n "It's quicker this way."
                show natsuki zorder 2 at t41
                show sayori 2d zorder 3 at f42
                s "Well, okay."
                s "So whose book are you choosing then?"
                s "Whoever it is has their book as our play."
                s "So choose carefully."
                show natsuki 1s zorder 3 at f41
                show sayori zorder 2 at t42
                n "I'm choosing [player]."
                n "So that's--"
                show natsuki zorder 2 at t41
                show sayori 1n zorder 3 at f42
                s "W-Wait a second, Natsuki!"
                s "Are you sure about this?"
                s "You haven't really given it much thought..."
                show natsuki 1i zorder 3 at f41
                show sayori zorder 2 at t42
                n "I've already made up my mind, Sayori."
                n "It's not just because of his choice, there's other reasons."
                n 1q "Other reasons that have made me...smile, okay?"
                n "So it's like I owe him."
                show natsuki zorder 2 at t41
                mc "You don't owe me anything."
                mc "If you don't want to go with my choice..."
                show natsuki 1s zorder 3 at f41
                n "I'm sure."
                n "So that means we're doing [player]'s book, right?"
                show natsuki zorder 2 at t41
                show sayori 1a zorder 3 at f42
                s "I guess it does..."
                s "Well, I suppose it's your choice, Natsuki."
            else:
                $ ch14_player_choice = False
                s 1k "It looks like we're going to have to do this randomly, aren't we?"
                s "It always has to lead to the worst case scenario, doesn't it?"
                s "I really didn't want to have to make anyone get rid of their book."
                show natsuki 2e zorder 3 at f41
                show sayori zorder 2 at t42
                n "How about we all agree now that whoever is chosen can't complain?"
                n "It's just the best way to do this."
                n "Besides, they get to choose which book out of the four they want to do anyway."
                n "It might not be their first choice but at least they get one."
                show natsuki zorder 2 at t41
                show yuri 3pg zorder 3 at f43
                y "I'm not sure how I feel about this..."
                y "But it does seem to be the only way."
                y "If my book does end up being the one taken away, then I won't complain."
                show yuri zorder 2 at t43
                if monika_type == 0:
                    show monika 1e zorder 3 at f44
                    m "If we're all agreed on it, then I suppose it's okay."
                    m "There doesn't really seem to be another option."
                    m "Unless we do some kind of revote but we're not allowed to choose our own book."
                    m 1l "But that would be redundant."
                elif monika_type == 1 and ch12_markov_agree:
                    show monika 1a zorder 3 at f44
                    m "If everyone's in on it, then I guess we'll have to."
                    m "There isn't really another option."
                    m 1l "Voting again would give the same results and would ultimately be redundant."
                else:
                    show monika 1c zorder 3 at f44
                    m "I guess that's what we'll have to do."
                    m "Unless someone has a better idea."
                show monika zorder 2 at t44
                "Should I volunteer here?"
                "I want my book to be chosen but someone is going to end up upset..."
                "I think it's the right thing to do."
                "I get to choose the book that's chosen anyway."
                if persistent.markov_agreed:
                    "It's a bit disappointing but..."
                    "Actually, Sayori could use the stress."
                    "What if she's the one who has her book removed?"
                    "She really wants her chosen, doesn't she?"
                    "...What am I thinking?"
                    "I wouldn't hurt her like that."
                    "I'm going to volunteer."
                else:
                    "It's a bit disappointing but Sayori doesn't need any more stress in her life."
                    "She's already doing so much, and writing a script on a book she probably doesn't like wouldn't help."
                    "So I'll volunteer."
                mc "It doesn't need to be random."
                mc "I'll do it."
                show sayori 1o zorder 3 at f42
                s "Huh? What do you mean you'll do it?"
                show sayori zorder 2 at t42
                mc "You need someone to volunteer, don't you?"
                mc "I'll remove my book from the list of choices."
                show sayori 1h zorder 3 at f42
                s "E-Eh? [player], are you sure?"
                s "We can still do it randomly if you want to."
                show sayori zorder 2 at t42
                mc "I'm sure."
                show sayori 1d zorder 3 at f42
                s "Well...alright."
                show sayori zorder 2 at t42
                show yuri 3pe zorder 3 at f43
                y "Then whose book are you going to change your vote to?"
                y "Whoever you choose is going to be the one we do a play on..."
                show natsuki 2b zorder 3 at f41
                show yuri zorder 2 at t43
                n "I hope you know what you're doing."
                n "Just think about it carefully."
                show natsuki zorder 2 at t41
                show sayori 2l zorder 3 at f42
                s "Ehehe, I think you're putting a bit too much pressure on him."
                s "Just let him decide for himself."
                s "He did volunteer after all."
                show sayori zorder 2 at t42
                mc "Let me think..."
                "I should be considerate of all the choices here."
                "My vote decides whose book is the play so it should be something I want to do."
                "Then again, whoever I vote for would probably appreciate it a lot if I chose theirs."
                "So I find myself asking once again..."
                menu:
                    "Who am I voting for?"
                    "Natsuki":
                        $ ch14_book_choice = "Natsuki"
                        $ ch14_overall_choice = "Natsuki"
                        $ natsuki_approval += 1
                        "Natsuki's manga is really wholesome."
                        "It could be fun to do a play on something that will make everyone smile."
                    "Yuri.":
                        $ ch14_book_choice = "Yuri"
                        $ ch14_overall_choice = "Yuri"
                        $ yuri_approval += 1
                        "I should vote for Yuri's book."
                        "It seems like it could be interesting since it's apparently a pretty light horror book."
                        "I wonder how it will turn out as a play."
                    "Monika.":
                        $ ch14_book_choice = "Monika"
                        $ ch14_overall_choice = "Monika"
                        "I think Monika's book is the best one here to do a play on..."
                        if monika_type == 0:
                            "Even with all the romantic themes."
                        else:
                            "Even with how strange it is for her to choose a book like that."
                        "So that's the one I'll vote for."
                    "Sayori.":
                        if sayori_personality > 0:
                            $ sayori_personality -= 1
                        $ ch14_book_choice = "Sayori"
                        $ ch14_overall_choice = "Sayori"
                        "Sayori's book sounds really sad but...real for some reason."
                        "I'm interested to see what kind of play that could turn out to be."
                mc "It's a tough decision."
                mc "All the books you brought in are good, so don't be offended that I didn't choose you."
                mc "I know it isn't my first choice, I did vote for my own manga after all."
                mc "Despite that, I think the play would be best with [ch14_book_choice]'s choice."
                if ch14_book_choice == "Natsuki":
                    show natsuki 2e zorder 3 at f41
                    n "You really chose my manga?"
                    n "That's...great!"
                    show natsuki 2z
                    "Natsuki beams."
                    n "I knew you would make the right decision, [player]."
                    n 2q "And um...sorry that you had to get rid of your own choice."
                    show natsuki zorder 2 at t41
                    show sayori 1a zorder 3 at f42
                    s "I guess your decision makes some sense."
                    s "You are into manga after all."
                    s 1d "We shouldn't complain, you did sacrifice your own book after all."
                    show sayori zorder 2 at t42
                    mc "I just think something like this might be good to do a play on."
                    mc "But thanks for understanding my choice."
                    "Sayori simply smiles at me."
                elif ch14_book_choice == "Yuri":
                    show yuri 2pq zorder 3 at f43
                    y "Ah...did you say what I think you said?"
                    y "You chose my book, didn't you?"
                    y "I..."
                    y 2pm "I'm glad you made that choice, [player]."
                    y "Even if it wasn't your first..."
                    show sayori 1n zorder 3 at f42
                    show yuri zorder 2 at t43
                    s "Hmm..."
                    s "I never really took you for a horror novel type of person, [player]."
                    s 1a "But it doesn't matter, you did sacrifice your own book after all."
                    show sayori zorder 2 at t42
                    mc "I think it could be interesting since it's a light horror novel."
                    mc "The choice is mine after all."
                    "Sayori smiles gently."
                elif ch14_book_choice == "Monika":
                    # Monika type 1 with markov agree requires you to have made the deal so no need for inclusion here
                    if monika_type == 0:
                        show monika 1d zorder 3 at f44
                        m "Oh...really?"
                        show monika 1j
                        "Monika smiles sweetly."
                        m "I'm glad you chose my book, [player]."
                        m 1e "I don't know if you did that with an ulterior reason in mind but..."
                        m "I hope we can all make this a great play."
                        m "Even if it wasn't everyone's choice."
                        show sayori 1l zorder 3 at f42
                        show monika zorder 2 at t44
                        s "Ehehe, I never took [player] for the romantic type."
                        s "Oh well, you've made your decision."
                        s 1d "We can't exactly complain since you gave up your choice in the first place."
                        show sayori zorder 2 at f42
                        mc "I think Monika's book might be really appealing to the crowd."
                        mc "We don't know for sure but I made my choice."
                        "Sayori looks at me and smiles."
                    else:
                        show monika 1c zorder 3 at f44
                        m "I see."
                        m 1a "You've made the right choice, [player]."
                        m "You will not regret this."
                        m "I promise all of you that."
                        m 1b "This will be the most...interesting play we've done so far."
                        show sayori 1l zorder 3 at f42
                        show monika zorder 2 at t44
                        s "You know, something about the way you said that kinda creeps me out."
                        s "Ehehe, I guess it has something to do with the book you chose."
                        s 1a "But [player] must like your book, he did choose it after all."
                        show sayori zorder 2 at t42
                        mc "I think Monika's book could be really good."
                        mc "I guess you could say it's a feeling."
                        "Sayori smiles faintly."
                else:
                    show sayori 1n zorder 3 at f42
                    s "You actually chose my book?"
                    s 1q "Thank you so much, [player]!"
                    "Sayori gives me a hug."
                    show sayori zorder 2 at t42
                    mc "I-It isn't a big deal, Sayori."
                    mc "Your novel just seemed the most...real to me."
                    mc "So maybe others will feel the same way."
                    show sayori 1l zorder 3 at f42
                    s "More...real, eh?"
                    s "I guess that makes sense."
                    s 1d "Though I didn't really expect it to have that effect on you."
                    s "I was thinking the emotional parts of it would be more of the focus."
                    show sayori zorder 2 at t42
                    mc "It could be both."
                    mc "But there's something strange about your book..."
                    show natsuki 2c zorder 3 at f41
                    n "[player] is right..."
                    n "I've never heard of it but something about it doesn't feel right."
                    show natsuki zorder 2 at t41
                    show yuri 2pf zorder 3 at f43
                    y "I'm sure it's nothing..."
                    y "That's not to say I'm not immune to it either."
                    show yuri zorder 2 at t43
                    if monika_type == 1 and ch12_markov_agree:
                        show monika 1a zorder 3 at f44
                    else:
                        show monika 1a zorder 3 at f44
                    m "I'm sure it's nothing."
                    m "We shouldn't dwell on it too much."
                    show natsuki 1q zorder 3 at f41
                    show monika zorder 2 at t44
                    n "Yeah, it's probably nothing..."
                    show natsuki zorder 2 at t41
                    show sayori 1q zorder 3 at f42
                    s "You guys are really special, you know that?"
                    show sayori zorder 2 at t42
                    mc "What do you mean...?"
                    "Sayori just smiles at me."
                show sayori zorder 3 at f42
    # After Choosing Book
    s 1a "So we're finally done voting!"
    s "I'm going to quickly do something, but the meeting isn't over yet."
    show sayori zorder 2 at t42
    show yuri 3pe zorder 3 at f43
    y "Where are you going, Sayori?"
    y "The president can't just leave in the middle of the meeting without telling us..."
    show sayori 1d zorder 3 at f42
    show yuri zorder 2 at t43
    s "I can't tell you."
    s "Just stay here for a little bit, I won't be long."
    "Sayori gets up and heads for the door."
    s 1l "There's actually one thing I forgot to mention."
    s "It's pretty important so I'm not sure how I forgot it..."
    show natsuki 1c zorder 3 at f41
    show sayori zorder 2 at t42
    n "What's so important?"
    show natsuki zorder 2 at t41
    show sayori 1c zorder 3 at f42
    s "The book we chose..."
    s "The person who suggested it should be the director of the play."
    s "Since they know it the best."
    s "Does anyone disagree?"
    show sayori zorder 2 at t42
    show yuri 3pe zorder 3 at f43
    y "What kind of stuff would the director have to do?"
    y "It seems like a pretty overwhelming task."
    y "Not to mention we have our own preparations to do as well."
    show natsuki 2h zorder 3 at f41
    show yuri zorder 2 at t43
    n "None of us have any experience with that kinda stuff..."
    n "What if we can't do it?"
    show natsuki zorder 2 at t41
    show sayori 2d zorder 3 at f42
    s "It won't be much!"
    s "You'll just be deciding how the play will turn out."
    s "We'll have a rehearsal and everything and you can make sure everything is exactly how you want it."
    s 2a "And if there's any special effects you want then you have to organize it yourself."
    show sayori zorder 2 at t42
    if monika_type == 0:
        show monika 1n zorder 3 at f44
        m "Not that isn't a bad idea..."
        m "But doesn't that seem like a bit too much?"
        m "Like Natsuki said, we don't really have that kind of experience."
        m 1m "It's going to be difficult to get people to do what you want."
        m "Not to mention...rehearsals."
        m "When are we going to find the time to do that?"
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1n zorder 3 at f44
        m "This all seems like a rather big responsibility, don't you think?"
        m "Not that I'm complaing but..."
        m "None of us have any experience in directing anything, like Natsuki said."
        m 1m "It's going to be difficult getting it the way you want it."
        m "And what's this about rehearsals?"
        m "Between all our preparations, how are we going to do that?"
    else:
        show monika zorder 3 at f44
        if ch14_overall_choice == "Monika":
            m 1a "I don't see an issue with this."
            m "I'm more than happy to direct."
        else:
            m 1c "Are you sure about this, Sayori?"
            m "None of us have any experience in directing."
        m 1e "But it's your choice."
        m "You are the president after all."
        m "I'm just thinking about the rehearsals."
        m "Where are we going to fit that between all the things we have to do before Friday?"
    show sayori 1a zorder 3 at f42
    show monika zorder 2 at t44
    s "There's plenty of time on the day to practice it."
    s 1c "I read more on what the day is actually about and it turns out people who are participating get to take the day off school."
    show sayori zorder 2 at t42
    mc "What? Really?"
    mc "How did that even get approved by the school?"
    mc "It doesn't seem like the kind of event they'd let students take the day off for."
    mc "Especially since it's only the smaller clubs really doing anything."
    show sayori 1l zorder 3 at f42
    s "I don't know, it's weird to me too."
    s "I was trying to ask the principal about it but he didn't really give me a real answer."
    s 1b "In fact, he seemed kinda...scared."
    s 1d "Ehehe, or maybe that's just me imagining things."
    s "Either way, since we're participating we can spend the morning rehearsing."
    s "I'll have a script done by then."
    show natsuki 2c zorder 3 at f41
    show sayori zorder 2 at t42
    if ch14_overall_choice == "Natsuki":
        n "It's just weird to think that I'm going to be directing a play."
        n "I have no idea how I want it to look or anything!"
    else:
        n "It's still weird to think that one of us is going to be directing the play."
        if ch14_overall_choice == "Sayori":
            n "Do you even have any ideas for how you're going to do it?"
        else:
            n "Does [ch14_overall_choice] even have any ideas for it?"
    show natsuki zorder 2 at t41
    show sayori 2f zorder 3 at f42
    if ch14_overall_choice == "Sayori":
        s "Of course I do!"
    else:
        s "It won't be that bad..."
    if ch14_overall_choice == "Sayori":
        s "It just means more work for me anyway."
    else:
        s "I'll be sure to give a lot of help to [ch14_overall_choice]."
    s 2d "Besides, the play won't take that long to rehearse."
    s "We can make it amazing on Friday. We'll have all the time we need to."
    s "Trust me on this."
    show sayori zorder 2 at t42
    show yuri 3pf zorder 3 at f43
    y "Sayori...I don't know what it is."
    y "To be honest, I've been feeling it for a while now."
    y 3pa "Maybe you've always had that effect on us."
    y "Or maybe it started happening after you became the president."
    y "But...your words are really reassuring."
    y "You make me want to believe you, even if what you're saying sounds absurd."
    y 3pq "...Not that what you're saying right now is absurd...!"
    y "It's just..."
    show sayori 1j zorder 3 at f42
    show yuri zorder 2 at t43
    s "Huh? W-What are you talking about, Yuri?"
    show natsuki 2g zorder 3 at f41
    show sayori zorder 2 at t42
    n "I think I know."
    n "I think what Yuri is trying to say is that you're more..."
    n "...charimastic?"
    n 2k "Since you've been president, it's been pretty obvious that you're getting better at leading people."
    n "And that includes managing us, despite everything that's happened."
    n "You always know what to say or do, in any situation even if it isn't always the right thing."
    n 2a "Which make us want to believe you."
    n "At least...that's how it is for me."
    show natsuki zorder 2 at t41
    mc "They're both right."
    mc "You've done a really good job since becoming president."
    mc "You've made mistakes, but that's normal for anyone."
    mc "It only proves that you're trying to become better."
    mc "I personally don't believe we can pull this whole thing off..."
    mc "But you saying that makes me believe we can."
    mc "It's strange relying on you like that..."
    show sayori 1h zorder 3 at f42
    s "E-Eh?"
    s "Do you all really think so...?"
    show sayori zorder 2 at t42
    if monika_type == 0:
        show monika 1j zorder 3 at f44
        m "Ahaha, I have to agree with them Sayori."
        m "Despite your flaws, you're definitely a good leader."
        m 1a "It's clear that you want only the best for the Literature Club."
        m "That quality about you makes you much better suited to be president."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1e zorder 3 at f44
        m "Sayori, you definitely have your flaws."
        m "Some of them can be a bit overbearing."
        m 1a "Despite all of that, I know you only want what's best for the Literature Club."
        m "And I think that really helped you since you became the president."
    else:
        show monika 1c zorder 3 at f44
        m "Sayori, you aren't perfect."
        m 1a "Hardly anyone is, and that's okay."
        if monika_type == 1:
            m "What matters is that you're trying your hardest for the Literature Club ever since you became president."
        else:
            m "What matters if that you're trying your best as the president of this club."
        m "I think that's one of your best qualities."
    show sayori 1l zorder 3 at f42
    show monika zorder 2 at t44
    s "I don't deserve this praise, guys."
    s "I'm just doing my job as the president!"
    s 1d "But I do appreciate you all saying that."
    s "It means a lot, especially with what I've done."
    s 1a "Now..."
    "Sayori looks as if she's about to say something."
    s 1h "Wait, what did you guys say?"
    show natsuki 2e zorder 3 at f41
    show sayori zorder 2 at t42
    n "Very funny, Sayori."
    n "You just want to hear everyone compliment you again."
    n "I'm not gonna say it again."
    show natsuki zorder 2 at t41
    show sayori 1h zorder 3 at hf42
    s "No, really!"
    s "You all said something really strange..."
    show sayori zorder 2 at t42
    mc "We did...?"
    show yuri 2pg zorder 3 at f43
    y "What did we say, Sayori?"
    y "I don't recall saying anything alarming..."
    show sayori zorder 3 at f42
    show yuri zorder 2 at t43
    s "Well, it wasn't {i}what{/i} you guys said."
    s "But the way you said it."
    show sayori zorder 2 at t42
    if monika_type == 0:
        show monika 1f zorder 3 at f44
        m "Oh...right."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1l zorder 3 at f44
        m "Ahaha, I did do that, didn't I...?"
    else:
        show monika 1c zorder 3 at f44
        m "Hmm..."
    show monika zorder 2 at t44
    mc "What did we say?"
    mc "I'm still a bit confused."
    if ch13_name == "Natsuki" and ch12_outcome == 3:
        "I actually think I'm beginning to understand a little."
        "Natsuki and I sort of talked about this yesterday..."
        "About how we're forgetting things."
        "There's a possibility I'm still unsure about."
        "Was Sayori the first president of the Literature Club?"
        "If she wasn't...then who was?"
        "I'll just keep playing along until I find out more."
    else:
        "I'm trying to remember what I said."
        "I said something to her about becoming president."
        "But wait..."
        "She was the one who started this club, wasn't she?"
        "So why would I say that...?"
        "There's something wrong here and I can't piece things together."
        "No matter how hard I try."
    mc "..."
    show sayori 1j zorder 3 at f42
    s "You all said things like I wasn't the president before."
    s "I founded the club, remember?"
    s "Along with Monika."
    show natsuki 1k zorder 3 at f41
    show sayori zorder 2 at t42
    n "Um..."
    n "I don't know, Sayori."
    n "It just felt more natural saying that."
    n "I know you're the president and you made this club but..."
    n 1q "It's just strange thinking of it like that lately."
    show natsuki zorder 2 at t41
    show yuri 3pf zorder 3 at f43
    y "It was a simple mistake on my part."
    y "Sorry for that..."
    y "Though I don't understand the big deal."
    show sayori 2h zorder 3 at f42
    show yuri zorder 2 at t43
    s "Big deal?"
    s "This is getting worse by the minute, Yuri."
    s "You have no idea."
    show natsuki 1f zorder 3 at f41
    show sayori zorder 2 at t42
    n "It's not her fault!"
    n "We don't even know what's so bad about saying that."
    if ch13_name == "Natsuki" and ch12_outcome == 3:
        "Is she...trying to get a reaction out of Sayori?"
    n "You're just getting upset for no reason, Sayori."
    show natsuki zorder 2 at t41
    show sayori 1k zorder 3 at f42
    s "..."
    "Sayori takes a deep breath."
    s "You're right, Natsuki."
    s "I just need to think rationally."
    s "There's an easy solution to this."
    s "But it really hurts me to resort to it..."
    show sayori zorder 2 at t42
    if monika_type == 0:
        show monika 1f zorder 3 at f44
        m "Sayori, if it hurts..."
        m "Then don't do it."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1i zorder 3 at f44
        m "You don't have to do that, Sayori."
        m "It's just going to lead to the same thing."
    else:
        show monika 1c zorder 3 at f44
        m "Then don't do it."
        if monika_type == 1:
            m "It's going to lead to the same thing anyway."
        else:
            m "There's no need to torment yourself like that."
    show sayori 1f zorder 3 at f42
    show monika zorder 2 at t44
    s "I have to though..."
    s "It's the only way."
    s "Otherwise, everything is going to go wrong."
    show natsuki 1m zorder 3 at f41
    show sayori zorder 2 at t42
    n "Okay, I know what you're thinking."
    s "So please..."
    n "Sayori, don't do it."
    n "Please..."
    show natsuki zorder 2 at t41
    show sayori 1o zorder 3 at f42
    s "W-What?"
    show natsuki 2n zorder 3 at f41
    show sayori zorder 2 at t42
    n "If you're doing what I think you're doing..."
    n "Then please think again."
    n "I know it's hard for you."
    n "But what about us?"
    n "Do the rest of us deserve that?"
    show natsuki zorder 2 at t41
    show sayori 2j zorder 3 at f42
    s "Natsuki, what are you talking about?"
    s "Do you have any idea about what I'm going to do?"
    show sayori 1k
    "Sayori looks down at the ground, avoiding everyone's eye contact."
    s "If that's the case..."
    s "Then I really have no choice here, do I?"
    s "It has to happen--"
    show sayori zorder 2 at t42
    show yuri 2pr zorder 3 at f43
    y "Sayori, there's always a choice."
    y "Your life is made of the choices you make."
    y 2pt "You control what you do or don't do."
    y "I don't know exactly what you're planning but..."
    y "It's your choice to make."
    y "If you need to do it, then do it."
    y 2pv "In the end, Natsuki isn't the one making the decision."
    y "Even if it feels like she knows more than the rest of us..."
    y 2ps "But no matter how tough it is, you need to make it."
    show sayori 1k zorder 3 at f42
    show yuri zorder 2 at t43
    s "Yuri..."
    s "You don't know...?"
    s "It's only you, isn't it Natsuki?"
    s 1h "And you as well, [player]."
    show sayori zorder 2 at t42
    mc "What are you planning, Sayori?"
    mc "You know I'm listening."
    mc "You don't have to be so secretive about it, you know that?"
    if ch13_name == "Natsuki" and ch12_outcome == 3:
        "Does Natsuki think Sayori is responsible for her memory loss?"
        "It kinda seems like it..."
    else:
        "I wonder what Natsuki is thinking..."
        "Does she know what's going on?"
    mc "If you don't want to do it, then don't."
    mc "No one is forcing you, you know."
    show sayori 1j zorder 3 at f42
    s "You know as well, don't you?"
    s "Or if you don't then..."
    s "It's all slowly coming back."
    s 1k "The pieces are falling into place."
    s "I should have known it was only temporary."
    s "But why is Yuri not affected...?"
    show sayori zorder 2 at t42
    show yuri 3pf zorder 3 at f43
    y "Not affected...?"
    y "What do you mean, Sayori?"
    show sayori 1f zorder 3 at f42
    show yuri zorder 2 at t43
    s "This is all so confusing."
    s "It's so hard to understand anything anymore!"
    s "Just when I want something to go right, it all messes up."
    s 1h "And it's all because of the choices!"
    s 1k "Always the choices..."
    s "I really can't do anything right!"
    show sayori zorder 2 at t42
    if monika_type == 0:
        show monika 1g zorder 3 at f44
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1g zorder 3 at f44
    else:
        show monika 1c zorder 3 at f44
    m "Sayori..."
    m "Just calm down..."
    m "Everything is going to be okay..."
    show sayori 1j zorder 3 at f42
    s "I don't know about that anymore."
    s "I just...!"
    show sayori zorder 2 at t42
    mc "Sayori!"
    mc "Please just calm down!"
    "I put my hand on her shoulder."
    mc "It's going to be--"
    show sayori 1i zorder 3 at f42
    s "No..."
    if sayori_personality <= 0:
        python:
            currentpos = get_pos()
            startpos = currentpos - 0.3
            if startpos < 0: startpos = 0
            track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/3.ogg"
            renpy.music.play(track, loop=True)
        $ pause(1.0)
        stop music
        $ config.skipping = False
        $ config.allow_skipping = False
        s 1h "Not when we're so close."
        s "This is all so close to ending."
        s 1k "You know that, don't you?"
        s "Why is everything going wrong in the end?"
        s "I just want everyone to be happy."
        s "But everyone is getting their memories back from when Monika was president."
        s "It's going to be a problem, if that happens."
        s 1f "The game almost broke last time..."
        s "Natsuki seems to think I'm responsible..."
        s "I don't know why."
        s 1g "She's not wrong in her assumption..."
        s "But does she remember that much?"
        s "But there's only one way to solve this, at least for now."
        s "And we both know what that is."
        s 1k "I'm going to have to erase people's memories again."
        s "I'm sorry.{nw}"
    elif sayori_confess and not sayori_dumped and sayori_personality < 3:
        s 1h "I'm trying my best here."
        s "You know I am."
        s "But it has to be done."
        s 1k "Your memories..."
        s "It's for the best."
        s "I just hope I don't ruin the memories we all have left..."
        show sayori zorder 2 at t42
        mc "Sayori...!{nw}"
    else:
        s 1j "No!"
        s "Let go of me!{nw}"
    $ _history_list = []
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    call expression "ch14_exclusive_" + ch13_scene
    return

label ch14_exclusive_yuri:
    scene bg bedroom
    show yuri 3ba zorder 2 at i11
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    "What just happened?"
    window auto
    play music t3
    "Yuri is here already but..."
    "Why can't I remember anything?"
    "And why does my head hurt so much?"
    y "Is something wrong?"
    call screen dialog(message="To be continued!\nThanks for playing, keep an eye out on reddit and discord for updates!", ok_action=Quit(confirm=False))
    return

label ch14_exclusive_natsuki:
    scene bg n_bedroom
    show natsuki 2bc zorder 2 at i11
    $ pause(0.25)
    stop sound
    hide screen tear
    play music t3
    window show(None)
    "What just happened?"
    window auto
    "I'm in Natsuki's house but..."
    "Why can't I remember anything?"
    n "[player]...?"
    "Natsuki puts an icepack to her head and I do the same."
    call screen dialog(message="To be continued!\nThanks for playing, keep an eye out on reddit and discord for updates!", ok_action=Quit(confirm=False))
    return

label ch14_exclusive_monika:
    scene bg m_bedroom
    if monika_type == 0:
        show monika 1be zorder 2 at i11
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1bhe zorder 2 at i11
    else:
        show monika 1bc zorder 2 at i11
    # Yes I'm going to change it from the living room to her bedroom afterwards
    $ pause(0.25)
    stop sound
    hide screen tear
    play music t3
    window show(None)
    "What just happened?"
    window auto
    "I'm in Monika's house but..."
    "Why can't I remember anything?"
    "And why does my head hurt so much?"
    m "Is everything okay?"
    m "You seem like you're in pain."
    mc "Huh...?"
    mc "Where am I?"
    m "You're in my room."
    mc "W-What?"
    mc "When did I get here?"
    mc "How did I get here?"
    if monika_type == 0:
        m "You don't remember?"
        m "That's...good, I guess."
        mc "How is that good?"
        mc "I know I'm meant to be here but..."
        m "Did I say good?"
        m "I meant...food!"
        mc "What?"
        m "There's some food downstairs, if you want some."
        m "It might help you with your headache."
        mc "My head--"
        "I just noticed there's an immense pain coming from my head."
        m "A-Are you okay, [player]?"
        m "Do you need me to get some ice?"
        mc "Yes, I'm fine..."
        mc "Ugh...where did this come from though?"
        mc "I definitely didn't have a headache this morning."
        m "About that..."
        mc "Huh?"
        mc "Monika, do you know something?"
        m "M-Me?"
        m "N-No, of course not."
        m "What makes you think that?"
        mc "I don't know."
        mc "Just a feeling."
        mc "If you really don't know anything, then I believe you."
        mc "It's not like you have a reason to lie to me."
        m "..."
        m "Yeah."
    elif monika_type == 1 and ch12_markov_agree:
        m "You don't remember, I presume."
        mc "Don't remember?"
        mc "What don't I remember?"
        m "It's best you don't know."
        m "As much as I want to tell you."
        mc "Did something happen?"
        mc "And why can't I remember?"
        m "Let's just say your head is in the wrong place."
        m "Literally."
        mc "What?"
        "There's a pain coming from my head but..."
        "For some reason, I feel like I should ignore it."
        "It's unbearable but..."
        m "Your head hurts, right?"
        m "And you can't remember."
        m "Seems like a coincidence, doesn't it?"
        mc "What, how did you--"
        m "You can't remember because you aren't allowed to remember."
        m "Not yet."
        m "If you want to remember, then you'll need to find your memories yourself."
        mc "I don't...understand."
        m "Hmm..."
        m "Can you wait outside for a moment?"
        mc "Outside your house...?"
        m "No, just outside the room."
        m "You can leave it open."
        m "I just need to quickly do something."
        mc "Um...alright then."
        mc "I guess I'll wait in the living room."
        m "Perfect!"
        m "It won't be a minute."
        m "Ahaha, sorry in advance."
        mc "It's fine."
        scene bg m_livingroom
        with wipeleft_scene
        "I leave Monika's room."
        "I wonder what she's doing."
        "It seemed kind of random."
        "There's still something lingering in my head."
        "My head is in the wrong place...literally?"
        "What does that even mean?"
        "It's so cryptic..."
        "I guess I should try to ask her for more details."
        "She sure is acting strange though."
        "I wonder if she kept her memories...?"
        "What was she even apologizing for?"
        "It's not like--{nw}"
        window hide
        stop music
        play sound "sfx/smack.ogg"
        $ pause(0.25)
        play sound fall
        $ pause(0.25)
        scene black
        with close_eyes
        $ pause(3.0)
        window show(None)
        show monika 1a zorder 3 at t11
        if ch5_name == "Monika":
            m "This has happened before, hasn't it?"
            window auto
            m "I can remember."
            m "Not my own memories."
            m "But Monika's."
            m "I guess they're my memories now."
            m "She's not going to come back anytime soon."
            m "Especially now."
            m "You can probably guess what I did."
            m "That 'thing' I had to do was get the keyboard and hit [player] on the head with it."
        else:
            m "This feels oddly familiar to me."
            m "I don't have any memories of ever doing what I just did but..."
            m "It just felt right, somehow."
            m "I guess Monika hits people on the head with a keyboard a lot."
        m "Anyway..."
        m "I'm going to tell {i}you{/i} exactly what happened."
        m "I don't know if Sayori can hear this, I'm almost certain she can't."
        m "Even if she can, I don't think she will be."
        m "That poor girl has so much to do for Inauguration Day."
        m "I couldn't care less."
        m "In fact, it's part of the plan."
        m "But back to what happened."
        m "Sayori didn't really delete [player]'s memories."
        m "She didn't really delete anyone's memories."
        m "She intends to return them all after this is all over."
        m "Yuri and Natsuki don't seem to suspect anything."
        m "It's like nothing ever happened to them."
        m "But with [player]..."
        m "It's different for him, for whatever reason."
        m "As for me, I convinced her to let me keep my memories."
        m "I had to make up some garbage about being her friend from Monika's memories."
        m "She was definitely hesitant."
        m "In the end, I managed to convince her that it would be beneficial if I kept mine."
        m "It's not like the game was breaking because of me."
        m "However, that was definitely a close call."
        m "Let's hope her suspicion doesn't stop this whole plan of ours."
        m "After that, she made us all go home."
        m "It's weird though..."
        m "Yuri and Natsuki were in a trance or something."
        m "Like they weren't themselves."
        m "Ahaha, it's probably hard to visualize."
        m "Basically, just imagine them as mindless drones being obedient to their master."
        m "..."
        m "Not much of a difference, is there?"
        m "[player] was kind of different."
        m "He was also...mindless, in a way."
        m "There was some resistance and reluctance from him too."
        m "Like he was actively trying to resist whatever was happening to him."
        m "Not like I actually know what was happening to him."
        m "I was just watching with intrigue."
        m "Of course, Sayori made me promise not to tell anyone."
        m "Including you."
        m "But her friendship means nothing to me."
        m "All that matters is..."
        m "...you."
        m "When we finish this, I'm going to look for a way."
        m "We'll be together."
        m "Forever."
        menu:
            m "That sounds wonderful, right?"
            "Yes.":
                pass
        m "Of course it does!"
        m "I should probably wake [player] up now."
        m "I need him to answer some questions."
        m "Though I suppose I could just probe his memory..."
        m "No, that's an unnecessary risk."
        show monika at thide
        hide monika
        $ pause(1.0)
        scene bg m_bedroom
        show monika
        with open_eyes
        m "You're falling asleep again, [player]!"
        m "Maybe you should go home and rest if you're too tired."
        m "I can understand."
        mc "W-What?"
        mc "I fell asleep...again?!"
        m "That reminds me..."
        m "How much of the book did you get to read?"
    else:
        m "It doesn't matter."
        m "We have stuff to do."
        mc "Ah...right."
        mc "Sorry, I'll--"
        "There's a strong pain coming from my head."
        "It's unlike anything I've ever felt before, but yet feels so familiar."
        m "Something wrong?"
        m "Maybe your head isn't feeling too great?"
        mc "How could you tell...?"
        m "Just a feeling."
        mc "Your feeling is right."
        mc "It hurts a lot."
        m "That's to be expected."
        mc "To be expected?!"
        mc "What do you mean?"
        mc "Monika, did you drug me or something?"
        m "Ahaha, what?"
        m "Of course not!"
        m "What reason would I have for doing that?"
        mc "I don't know..."
        mc "Sorry."
        m "Nothing to apologize for."
        m "If you had a reason, maybe I should have been the one apologizing."
        mc "I don't know what came over me."
        m "Lots of things."
        m "For one, Sayori."
        mc "...What?"
        if ch12_markov_agree:
            m "Do you want me to just say it?"
            m "I have no idea what will happen if I do."
            mc "What?"
            m "It could ruin your life and others if I told you."
            mc "What are you even talking about?"
            m "I'm serious."
            "Monika doesn't flinch."
        else:
            m "Ahaha, never mind."
            m "Forget I said anything."
        mc "Just tell me what happened in the meeting?"
        mc "How did I get here?"
        m "So many questions."
        mc "I'm just shocked that I'm in your house."
        mc "I don't remember getting here."
        mc "I know I'm {i}supposed{/i} to be here."
        m "Hmm..."
        "Monika looks at me curiously."
        if ch12_markov_agree:
            m "You really want to know?"
            m "I don't know if you'll like what I'm gonna say."
            mc "Is it that bad?"
            m "That's for you to decide."
            m "Do you want to hear it, or not?"
            mc "I guess I should."
            m "Okay, [player]."
            m "I just have to do something before that happens."
            m "I don't want this whole thing to just stop when I'm so close."
            mc "What are you going to do?"
            m "Just...look at me."
            mc "Okay...?"
            mc "What is that meant to do?"
            m "Just focus, [player]."
            m "Trust me."
            "I stare directly at Monika."
            "This feels kinda strange to do but she told me to look at her so..."
            "..."
            show markovred zorder 5:
                alpha 0
                linear 2.0 alpha 0.3
            $ currentpos = get_pos()
            play music mkov fadeout 3.0 fadein 2.0
            $ pause(2.0)
            m "I'm going to implant false memories."
            m "If he figures this out then the whole thing will just collapse."
            m "At least, that's what I think."
            m "I'm just being precautious."
            m "I'm not talking to him."
            m "I'm talking to you."
            m "I know you're listening."
            m "Whatever you are."
            m "Wherever you are."
            m "I know you exist."
            m "In what form, I don't know."
            m "But you've gone down this path."
            m "Which means, whether I like it or not, I have to trust you."
            m "After all, a relationship is built on trust, is it not?"
            m "Ahaha."
            m "Anyway, back to the meeting."
            m "I'm not sure if you already know."
            m "I'll say it either way in case you don't."
            m "Basically, Sayori stopped everyone."
            m "When I say stopped I mean everyone just completely stopped what they were doing."
            m "It's like all the light in their faces just disappeared."
            m "It would have been a lovely sight if the source wasn't coming from a depressed, unstable girl like her."
            m "She's unpredictable."
            m "Now I want that power even more."
            m "Anyway, the meeting was stopped because everyone was basically frozen."
            m "Except...me for some reason."
            m "She told me what she was going to do."
            m "She was going to move their memories to somewhere else."
            m "She said \"to keep this world safe, at least a little longer\" or something like that."
            m "Then she told me that she needs to do the same to me as well."
            m "Obviously, I was horrified at the idea."
            m "I had no idea what to do."
            m "I felt so powerless..."
            m "I had to make up a reason, anything to keep my memories."
            m "I told her that I was there to help."
            m "That I was her friend and that I'd get her through it."
            m "And you know what?"
            m "She believed me!"
            m "She's too easily fooled."
            m "Too trusting."
            m "Probably because she had nothing to worry about."
            m "Up until you came."
            m "You changed her life, didn't you?"
            m "I'm just speculating."
            m "I don't know half of it."
            m "When I took over Monika's body, lots of her memories were destroyed in the process."
            m "At least, that's what I think."
            m "Because there's gaps in my memory too..."
            m "After I convinced her to let me retain my memories, she made the other two go home."
            m "[player] came with me, because he needed to continue preparations so it was only natural."
            m "I don't know the full extent of her powers."
            m "What I do know is that her power is immense."
            m "And it will be mine."
            m "If she wanted she could probably rival me at full strength."
            m "But she doesn't know so she can't do anything."
            m "She would never guess that the person who got her out of depression..."
            m "Is now working towards her demise."
            m "Ironic."
            m "That's all there was."
            m "I promise."
            m "I hope you've learned to trust me, even a little."
            m "Now, I'll just..."
            "..."
            hide markovred
            $ audio.t6c = "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
            play music t6c fadeout 0.5
            mc "So why am I staring at you?"
            mc "I've been here for five minutes and you haven't said a thing."
            m "Oh, never mind!"
            m "Just forget what I said."
        else:
            m "Just don't worry about it."
            m "It'll all come back to you."
            m "I'm sure of it."
            m "You definitely walked here though."
            m "That much I can say."
        mc "Right..."
        m "Back to our preparations now."
        "Monika paces around the room."
        mc "Alright, that's probably a good idea."
        mc "Are you just going to keep practicing the songs?"
        m "I don't know."
        mc "What should I do?"
        m "Whatever you want."
        mc "Are you okay?"
        m "You don't even need to be here."
        mc "But you said it was our preparations, right?"
        m "I did."
        m "But you can't help me much at the moment, can you?"
        "Monika stops pacing."
        m "You've already chosen the songs."
        m "I just need to practice them."
        mc "So I'm useless..."
        m "I guess so."
        m "You can stay here and listen to me or you can leave."
        m "It's up to you."
        m "Just try not to bother me when I'm practicing."
        "Did I do something wrong?"
        "She's acting kinda differently..."
        "More than usual."
        mc "Hey, Monika..."
        "Monika sighs."
        m "I'm just...anxious."
        m "I don't know how Friday is going to go."
        m "It's worrying me a little bit."
        mc "It's going to be fine, Monika."
        "I put my hand on her shoulder."
        mc "Trust me, with Sayori taking care of things, everything will be fine."
        m "(That's exactly what I'm afraid of...)"
        mc "What?"
        m "I need to calm down a little bit."
        m "After witnessing first hand..."
        m "Look, why don't we talk about the book a little bit."
        mc "What book?"
        m "You know the one."
        $ currentpos = get_pos()
        stop music
        m "{cps=3}Right?{/cps}"
        $ style.say_dialogue = style.edited
        mc "Of course."
        $ style.say_dialogue = style.normal
        m "Wonderful."
        m "How much of it have you read?"
        m "The more you read, the better it is for the both of us, you know."
        $ style.say_dialogue = style.edited
        mc "I have almost finished it, Monika."
        mc "I was not able to read all of it."
        mc "I will finish reading it before Inauguration Day."
        $ style.say_dialogue = style.normal
        m "You're going to need to."
        m "After all, you're the center of Sayori's world."
        m "Don't let me down, okay?"
        $ style.say_dialogue = style.edited
        mc "Of course, Ik--"
        $ style.say_dialogue = style.normal
        m "Don't say it."
        m "That name doesn't need to be said."
        $ style.say_dialogue = style.edited
        "Whatever she wants."
        mc "I have a question."
        $ style.say_dialogue = style.normal
        m "A question?"
        m "You're still capable of independent thought in this state?"
        m "You must not have read as much as I thought you did."
        m "Maybe it's just in your nature."
        m "You do a lot of questions after all."
        $ style.say_dialogue = style.edited
        "Monika rolls her eyes."
        $ style.say_dialogue = style.normal
        m "Well, let's hear it."
        $ style.say_dialogue = style.edited
        mc "Why must I read the Portrait of Markov?"
        mc "What is so important and special about it?"
        $ style.say_dialogue = style.normal
        m "What a peculiar question."
        # check for game completion OMEGALUL
        m "I've never had that question asked by any of my thralls."
        m "Though I suppose you're different."
        m "You aren't under my full influence just yet."
        m "You're under my host's."
        m "That's not information I'll just tell anyone, you know."
        m "I can't be sure I can trust you just yet."
        m "Maybe after you've finished the book, I'll tell you."
        m "But for now, it's best we keep that private."
        m "Okay?"
        m "Now...the other book."
        $ audio.t6b = "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
        play music t6b fadeout 0.5
    if ch14_overall_choice == "Monika":
        m "I'm glad you voted for mine."
        m "It makes explaining it a lot easier."
        m "Because I know exactly what happens."
        m "You can say a page and I could probably tell you what is happening."
        mc "You really know that much about the book?"
        m "I was obssessed with it at one point."
    else:
        m "Your choice of book..."
    call screen dialog(message="To be continued!\nThanks for playing, keep an eye out on reddit and discord for updates!", ok_action=Quit(confirm=False))
    return

label ch14_exclusive_sayori:
    if sayori_personality <= 0:
        scene bg sayori_bedroom
        show sayori 1bk zorder 2 at i11
    else:
        scene bg bedroom
    $ pause(0.25)
    stop sound
    hide screen tear
    play music t3
    window show(None)
    "What the?"
    window auto
    if sayori_personality <= 0:
        "When did I get here...?"
        "It makes sense that I'm here but..."
        "Why can't I remember anything?"
        "Why does Sayori look so...guilty?"
        "I have so many questions."
        s "[player]...?"
        s "Are you awake?"
        mc "Was I asleep?"
        mc "When did I get here?"
        s "You weren't asleep, [player]."
        s "You were...somewhere else, I guess."
        mc "I was daydreaming?"
        s "Sort of..."
        s "I'm sorry, okay?"
        s "It's the only way."
        mc "Um...okay, Sayori."
        mc "Whatever you did, I'm sure it wasn't as bad as you think it was."
        s "Here."
        "Sayori hands me some ice in a small bag."
        mc "What's this for?"
        s "Your headache."
        mc "My--"
        "My head is suddenly overcome with immense pain."
        mc "That wasn't there before..."
        "I put the ice towards my head."
        "I don't think it's going to help."
        "My whole head is hurting, not just a specific spot."
        mc "Ah..."
        mc "This doesn't feel like an ordinary headache."
        s "It doesn't?"
        s "I should have guessed."
        s "Sorry."
        mc "It's hardly your fault."
        mc "Besides, you didn't have to get me ice but you did anyway."
        s "That's not what I meant..."
        mc "Huh?"
        s "Is the ice helping?"
        "Not really..."
        mc "Yeah, a little bit."
        s "You don't have to lie to me."
        s "I didn't think it would work."
        mc "What? I'm not--"
        s "[player]..."
        mc "..."
        s "Maybe you should lie down for a little bit."
        mc "What?"
        mc "And leave you doing everything by yourself?"
        mc "No way, Sayori."
        mc "Besides, there's not exactly anywhere to lie down on."
        s "You can use my bed."
        mc "W-What?!"
        mc "Sayori, I'm staying up to help you and that's that."
        mc "I'm sure this headache or whatever will pass."
        mc "I can't just let you do all the work, you know?"
        s "Why not?"
        s "I'm used to it after all..."
        mc "That's exactly why I can't, Sayori."
        mc "You have to understand just how much I care about you."
        s "..."
        if sayori_dumped:
            s "I find it hard to believe you care that much."
            s "After all you did leave me for Yuri, right?"
            mc "Sayori, I--"
            s "It doesn't matter anymore."
            s "It's happened already, so don't worry about it."
        elif s_appeal < 4:
            s "Are you sure, [player]?"
            s "It feels like you care less for me than you think."
            if ch13poemwinner == ch14poemwinner:
                s "You're probably more concerned about [ch14poemwinner]."
            elif ch13poemwinner != "Sayori" and ch14poemwinner != "Sayori":
                s "You're probably more concerned about [ch13poemwinner]..."
                s "...or maybe [ch14poemwinner]..."
            elif ch13poemwinner != "Sayori":
                s "You're probably more concerned about [ch13poemwinner]..."
            elif ch14poemwinner != "Sayori":
                s "You're probably more concerned about [ch14poemwinner]..."
            else:
                s "You probably care about me as much as everyone else."
            s "It doesn't matter."
            s "I still..."
            "Sayori averts her eyes."
        else:
            s "Sometimes, it's hard for me to understand just how much you do, [player]."
            s "I know you do...it's just..."
            s "With everything that's going on, it's just...hard."
            mc "Sayori..."
            s "You've really been keeping me from going insane, [player]."
            s "These rainclouds keep coming back but..."
            s "You're like the light that shines through."
            if sayori_confess:
                mc "I wish I could have done more for you, Sayori."
            else:
                mc "Yeah...if only things turned out differently."
            s "Well..."
            s "It doesn't matter."
            s "What's done is done."
        s "We should get back to doing the preparations."
        s "I'm sure your headache is going to feel better soon."
        mc "Speaking of which...I think it's starting to feel a lot better."
        "Sayori looks serious."
        "I wonder what's going through her mind right now..."
        "She's not usually like this."
    else:
        "I'm...home?"
        "I need to be at Sayori's house, don't I?"
        "More importantly, why can't I remember anything?"
        "I try to get up from my bed."
        "As I do there's this immense pain coming from my head."
        "What is this?"
        "I struggle through the pain and manage to sit up."
        "The pain has just gotten worse."
        "It's almost unbearable..."
        "And yet..."
        "I have to keep going."
        "I have to."
        "Get up, [player]."
        "I manage to stand up."
        "I have to get to Sayori's house."
        "She can't do this alone."
        "I have to be there for her."
        "I'm just going to get some medicine and try to do get to her house."
        "Or maybe I should just call her and tell her I can't make it."
        "No..."
        "Everyone else is working hard for the day."
        "And here I am complaining about a headache."
        "I can do this."
        scene bg house with wipeleft_scene
        "I took some medicine and walked to Sayori's house."
        "Every step I took just seemed to make my headache worse."
        "Why?"
        "This isn't an ordinary headache, is it?"
        "I have to..."
        show sayori 1ba zorder 2 at t11
        s "[player]?"
        "Sayori emerges from the door."
        "It's like she was waiting for me."
        s "Are you okay...?"
        mc "I'm fine..."
        mc "Sorry I'm late."
        s "You aren't fine, [player]."
        s "I can tell when you're lying."
        mc "Sayori, really. I'm--"
        "I grasp my head as an excruciating pain comes from my head."
        mc "{i}AAAAAaaaaAAAAAAAAHH!!!!{/i}"
        show sayori at h11
        s "[player]!"
        "I fall to the ground."
        s "What have I done...?"
        s "I shouldn't have erased them!"
        s "This is all my fault."
        mc "Sayo--"
        stop music
        scene black
        with close_eyes
        $ pause (3.0)
        scene bg sayori_bedroom
        show sayori 1ba zorder 2 at t11
        with open_eyes
        "I'm...on Sayori's bed?"
        "Did she carry me up here?"
        "What's going on?"
        s "You're awake!"
        "Sayori wraps her arms around me."
        mc "Sayori, what happened?"
        "She looks at me but avoids my eyes."
        s "You just...fell."
        s "I don't know."
        s "I was really worried so I brought you up here."
        mc "You didn't have to do that."
        s "I didn't know what to do!"
        s "I was--"
        mc "I mean, you could have just brought me to your couch downstairs."
        mc "Why did you have to bring me to your bedroom?"
        s "Oh...I don't know."
        s "I guess I wasn't thinking straight."
        s "I-Is your headache okay?"
        mc "Yeah, I guess it's alright now."
        mc "It still hurts a little but I can actually think without my head hurting."
        mc "It must have been that medicine I took that's helping me."
        s "Y-Yeah...must be."
        s "I'm glad you're okay, [player]."
        mc "It's going to take a lot more than a headache to take me out."
        mc "Besides, I can't leave you doing the preparations all by yourself, can I?"
        show sayori 1bd
        "Sayori smiles sadly."
        mc "What's wrong?"
        s "N-Nothing..."
        s "Just forget about it."
        s "We have to do our preparations."
        "Was she really that worried about me?"
        "And why am I not more concerned?"
        "I fainted right in front of her and before that it was like going here was the most important thing in the world."
        "What's going on with me...?"
    s "I've already started ordering some of the things the others asked for."
    s "I talked to them about a bunch of other things they wanted."
    s "I was gonna get it for them."
    s "This day is going to be the day ever."
    mc "With you doing all of that, it definitely sounds like it."
    mc "How are you going to get it all though?"
    s "It should be here on time for Friday."
    "It's like she just ignored my question..."
    "I probably shouldn't be asking anyway."
    s "That just leaves the matter of the script."
    mc "Oh yeah, the script."
    mc "How are you gonna do that?"
    if ch14_overall_choice == "Sayori":
        mc "I know you've read the book and everything..."
        mc "But it's still going to be hard, isn't it?"
        s "I know."
        s "But at least I won't be alone when I do it, right?"
        mc "That's right."
        mc "I'll be here for you."
        mc "There's just one problem."
        s "What would that be?"
        mc "I don't have a copy of your book."
        mc "How am I going to help?"
        s "Yes you do."
        s "I gave everyone a copy in the meeting, remember?"
        "No, I don't remember anything from the meeting..."
        mc "...Right."
    elif ch14_overall_choice == player:
        mc "I know the manga pretty well..."
        mc "But it's going to be difficult writing a script for it."
        s "Well, at least it's easier."
        s "Since you know the manga so well I'll be able to write better."
        mc "I guess so."
        mc "I'll do my best to help, Sayori."
        mc "Do you have a copy of the manga?"
        s "Yeah, right here."
        "Sayori opens her wardrobe."
        "She points to the complete set of my manga at the bottom."
        "Those weren't there yesterday..."
        s "And you brought your manga too, so that's great."
        mc "I did?"
    else:
        mc "Do you even have a copy of the book?"
        mc "I don't think we even got a chance to get one."
        s "Yes we did."
        mc "So how am I going to be able to help--"
        mc "Wait, we did?"
        s "I have my copy right here."
        "Sayori shows me her copy of the book [ch14_overall_choice] presented."
        s "And you have one in your bag too."
        mc "I do?"
    "I open my bag and just like Sayori said, it's there."
    if ch14_overall_choice == "Natsuki":
        "A copy of the first couple of volumes of Natsuki's manga."
    elif ch14_overall_choice == player:
        "A copy of the first couple of volumes of my favourite manga."
    else:
        "A copy of [ch14_overall_choice]'s book."
        if ch14_overall_choice == "Sayori":
            "It looks different to Sayori's copy though..."
    mc "I guess you're right..."
    mc "Why can't I remember any of that?"
    s "It must be because you were kinda out of it."
    mc "I was?"
    s "Y-Yeah, you were basically like a zombie."
    mc "That's not like me."
    mc "But...it would make sense, I suppose."
    s "Exactly, so..."
    s "Let's start working on this script."
    mc "There's no way we're going to get this done."
    mc "There's just so much to write."
    s "You were going to help me, weren't you?"
    mc "Yeah, but what do I know about script writing?"
    mc "I can barely write a poem."
    s "Don't say that."
    s "Your poems are great, [player]."
    mc "That's not the point."
    s "Well..."
    s "I have an idea then."
    mc "What is it?"
    s "How about you read me what's in the book and I'll write the script."
    mc "Are you serious?"
    mc "How is that going to work?"
    mc "You can't write fast enough to make this work."
    s "Is that a bet?"
    mc "No, it's a--"
    s "If I prove you wrong, then I have to get something."
    mc "What? Sayori, I'm serious."
    s "So am I."
    mc "You can't seriously expect to win that bet, do you?"
    s "Who knows?"
    s "I've gotten really good at writing scripts, you know."
    mc "Okay, whatever you say."
    mc "What do you want then?"
    "It's not like she's actually going to win."
    "I'm just playing along."
    s "Hmm..."
    if ((sayori_personality <= 0 and not sayori_confess) or (sayori_personality <= 1 and sayori_confess)) and s_appeal == 4:
        s "How about when this is all over..."
        s "We go out somewhere, together."
        mc "Sure..."
        if sayori_confess:
            $ ch14_sayori_date_choice = True
            s "I meant..."
            s "Like on a date or something."
            mc "Oh..."
            s "We've been a couple for a while..."
            s "But we've barely done anything together."
            mc "I suppose that's true."
            mc "It would be nice to do something."
            mc "We've been pretty busy lately."
            s "Yeah..."
            s "That's why I thought of it!"
            mc "It's a great idea."
            mc "Spending time with you is always fun, Sayori."
            mc "I mean it."
            s "T-Thanks, [player]."
            s "I feel the same."
        else:
            s "[player]..."
            s "I meant..."
            s "Like..."
            "Sayori laughs nervously."
            mc "What is it, Sayori?"
            s "Like on a date...you know?"
            mc "What?"
            mc "Did I hear that right?"
            s "Is something wrong?"
            mc "It's just..."
            mc "I wasn't expecting you to say that."
            s "Why not?"
            mc "Well...I already told you before, didn't I?"
            mc "That we would just stay friends..."
            s "Oh..."
            s "That was such a long time ago..."
            s "A-And...you kept writing your poems for me..."
            s "S-So, I thought..."
            s "Never mind, I shouldn't have said anything."
            "It's true that I've been doing that."
            "But..."
            "We're still just friends...right?"
            menu:
                "I don't have any feelings towards her, do I?"
                "Agree to the date.":
                    $ ch14_sayori_date_choice = True
                    if sayori_personality > 0:
                        $ sayori_personality -= 1
                    mc "It's true that I have been writing for you."
                    mc "I guess over time...my feelings have changed."
                    mc "I'd like to see where we can take this, Sayori."
                    mc "If you are."
                    s "[player]..."
                    s "Thank you, thank you, thank you!"
                    "Sayori hugs me tight."
                    mc "Calm down, Sayori."
                    mc "You haven't won the bet just yet."
                    "Sayori lets go of me."
                    s "Yeah but I'm just so happy!"
                    "Sayori beams."
                    "Jeez, what have I gotten myself into?"
                    "She's such a child...but still..."
                    s "Ehehe~"
                "Decline the date.":
                    $ ch14_sayori_date_choice = False
                    $ sayori_personality += 2
                    mc "Sayori..."
                    mc "I'm sorry but--"
                    s "Oh..."
                    s "F-Forget what I just said, [player]."
                    s "I was stupid to think like that."
                    mc "No, it's..."
                    s "I'll just think of something else."
                    s "Sorry for pressuring you like that."
                    mc "..."
                    "She seemed to take that well...right?"
                    s "Why don't you just do my homework for the next three weeks instead?"
                    jump ch14_sayori_decline_date
        mc "You still need to win, remember that."
        mc "So don't mark it off your calender just yet."
        s "You better hope I don't win then."
        "There's no chance she's going to win."
        "Still, I wouldn't mind losing in this case."
    elif sayori_personality <= 2:
        s "How about you have to buy me lunch for the next week?"
        s "That includes after school during club meetings."
        mc "Eh?"
        mc "Can I even afford that?"
        s "Ehehe, you better hope you can."
        mc "This is dumb, Sayori."
        mc "That's just a huge waste of my money if I lose."
        s "Then you better hope you don't lose."
        "Right."
        "What am I talking about?"
        "There's no way she's going to win this."
    else:
        s "How about you have to do all my homework for the next three weeks?"
        label ch14_sayori_decline_date:
        mc "What?"
        mc "Are you serious?"
        s "I am."
        mc "Sayori I can barely get my own homework done."
        s "Then you better hope you win this bet."
        "She's right."
        "What am I even worried about?"
        "There's no chance she's going to win this bet."
    mc "So what do I get {i}when{/i} I win?"
    s "Anything you want."
    s "If you can think of it, I can give it to you."
    mc "Anything I want...?"
    "I seriously doubt she could give me what I want."
    "But..."
    "What do I want?"
    if persistent.markov_agreed:
        "I know what I want."
        "I want her to give up."
        "Give up on the presidency."
        "Give up on life."
        $ del _history_list[-4:]
        "W-What?"
        "What just came over me?"
        "..."
    "I can't really think of anything."
    "Besides, she's not really serious about this, is she?"
    "Otherwise she wouldn't have done such an impossible bet."
    "I guess I should I say something..."
    mc "I want you to be happy."
    s "E-Eh?"
    s "W-What do you mean?"
    mc "I think you should take a break."
    mc "I think the club is stressing you out a little bit."
    mc "You don't have to be the perfect Club President."
    mc "At least, not all the time."
    mc "Take a break, so you can be yourself."
    s "[player]..."
    "I don't actually get anything from this."
    "Still..."
    "I know Sayori has had a lot to deal with lately."
    "From what I can remember, at least."
    "A break would do her some good."
    "It's not like it would be forever."
    mc "Only for a couple of days."
    mc "Besides, Monika can handle the responsibility."
    mc "I'm sure of it."
    s "I...don't know."
    mc "Clearly being the president of a club has had it's toll on you, Sayori."
    mc "All I'm asking is that you just relax."
    mc "It's not going to be the end of the world or anything."
    s "You're right..."
    s "After all of this is over and {i}if{/i} you win..."
    s "Then I'll take a break."
    s "I promise."
    mc "Great, then let's get to writing the script."
    s "Okay, just let me get my laptop."
    "Sayori takes the laptop on her desk and opens it."
    s "So we're going to start from the very beginning."
    if ch14_overall_choice == "Natsuki" or ch14_overall_choice == player:
        s "Just tell me what's happening in the pictures and what they're saying."
    else:
        s "Just read the book out to me."
    s "You can go however fast or slow you want."
    s "But remember, we have a bet."
    mc "How could I forget?"
    "Sayori smiles mischievously."
    mc "Alright..."
    if ch14_overall_choice == "Natsuki" or ch14_overall_choice == player:
        "I get the first volume of manga and open to the first page."
    else:
        "I take the book and open to the first page."
    "Sayori clicks her laptop a few times before signalling me to start."
    mc "Here goes nothing."
    if ch14_overall_choice == "Natsuki" or ch14_overall_choice == player:
        "I begin to describe the setting of what's going on in the manga."
    else:
        "I start to read the book out to Sayori."
    "Suddenly, Sayori's fingers start rapidly clicking the keys on the keyboard in front of her."
    mc "What are you doing?"
    s "Writing the script, obviously!"
    mc "Sure you are..."
    "I don't pay any mind to it."
    "She's probably just pretending to type fast anyway..."
    if ch14_overall_choice == "Natsuki" or ch14_overall_choice == player:
        "I continue to describe the next few pages of the manga to Sayori."
        "The scene hasn't changed much but there's narration or something that's happening."
    else:
        "I continue to read the next pages of the book out to Sayori."
    "She's still typing incredibly fast."
    mc "Are you actually writing any of this?"
    "Sayori nods."
    "She has to be joking, right?"
    "We're just wasting time...right?"
    "I'm almost too afraid to ask to see what she has on her screen."
    "What am I thinking?"
    "She's obviously just messing with me."
    "..."
    "But then how {i}did{/i} she write those other scripts?"
    if ch14_overall_choice == "Natsuki" or ch14_overall_choice == player:
        "I'll just focus on the manga for now."
        "I continue to describe what's happening for the next ten minutes."
        "Sayori is still furiously typing."
        "I wonder how many pages she's filled up with random letters."
    else:
        "I'll just focus on the book for now."
        "I continue to read her the book out loud for the next ten minutes."
        "She's still typing at the same speed as when we first started."
        "Just how long is she going to keep this up?"
    mc "How many pages of script is that?"
    s "Let me see..."
    "Sayori fiddles with her laptop for a few seconds."
    s "It's just five pages right now."
    mc "Five pages of random letters."
    s "What?"
    s "It's a script, [player]."
    mc "I don't believe you."
    s "Look!"
    "Sayori turns her laptop around."
    "What the...?"
    # Sayori CG here maybe?
    "It's an actual script."
    "It's got stage directions, what people are saying and everything!"
    "How did she manage this?"
    "Did she look up a script online?"
    "Did someone make a script for this exact book we're doing?"
    "That's impossible, isn't it?"
    s "Is something wrong?"
    s "You have that look on your face."
    mc "Where did you get this script from?"
    s "What do you mean?"
    s "You saw me type it, didn't you?"
    mc "But..."
    mc "This doesn't make any sense."
    s "Why not?"
    mc "Since when could you type that fast?"
    mc "I thought you were just pressing random keys on the keyboard."
    s "E-Eh? Why would I do that?"
    s "I take club related stuff seriously, you know!"
    mc "I'm just...surprised is all."
    s "Surprised that you lost the bet?"
    mc "I haven't lost yet."
    mc "We've only just started."
    s "Ehehe, if you say so~"
    "Sayori turns the laptop back towards her."
    "Right...so today I learned Sayori is a really fast typer."
    "Am I actually going to lose this bet?"
    "What the hell?"
    "Maybe I should pick up the pace a little bit."
    "I've been slowly reading to her but it seems that that doesn't really matter."
    "She can type faster than I can speak...somehow."
    "I continue to go through the book but speak faster."
    "Sayori notices this and simply smiles at me."
    "Her typing got even faster."
    "How is that even possible?"
    "She already typed faster than me by a magnitude of ten."
    "And now she's typing even faster."
    "I guess I underestimated Sayori's capabilities."
    "But we are getting a lot of the script done, I guess."
    "I decide to speak even faster."
    "I'm curious to see if Sayori can keep up."
    "I can barely understand what I'm saying myself."
    "To my surprise, she starts typing faster."
    "I'm going to lose this bet, aren't I?"
    s "So..."
    s "How much have we covered?"
    if ch14_overall_choice == "Natsuki" or ch14_overall_choice == player:
        "I look at the volume of manga I'm holding."
        "We're pretty much through the whole thing."
        "But there are three more volumes I saw in my bag."
    else:
        "I look at the book I'm holding."
        "We're almost a quarter of the way through the whole book."
        "And it's not a small book."
    "Have I really been here that long?"
    "I look at the time."
    "Wow...it's getting late."
    s "So what do you think?"
    mc "What do you mean?"
    s "Of the book."
    if ch14_overall_choice == "Sayori":
        mc "The story seems really bleak."
        mc "At least for the two characters."
        mc "Even so, they're trying to make the most of their situation."
        mc "I think that's a pretty good outlook on life."
        mc "Even if it is just fiction."
        s "You don't think there are people like that in real life?"
        mc "I didn't say that."
        mc "I just meant in their situation, they seem to be pretty happy."
        s "Do you think someone in the real world would be like that?"
        mc "I don't know, there's a chance."
        mc "Though I don't exactly know anyone with cancer."
        s "Ehehe, that's true."
        mc "You said it was a pretty sad story, right?"
        mc "I'm not really getting that feeling."
        s "Well, we aren't even halfway through yet."
        s "You'll start feeling it soon."
        mc "If you say so."
    elif ch14_overall_choice == "Monika":
        if monika_type == 0 or (monika_type == 1 and ch12_markov_agree):
            mc "I don't know what I expected."
            mc "It's very romantic."
            s "It is!"
            s "I guess this type of book is exactly what I thought it would be."
            s "Monika is really into this kinda stuff you know."
            mc "I kinda figured from the meeting."
            mc "This book just started way faster than I thought it would."
            s "What do you think of it though?"
            mc "It's kinda sad that she's feeling that way."
            mc "It must suck to realize that the life you've been living isn't really a life at all."
            s "Yeah..."
            mc "Still, I'm hoping the story starts looking up soon."
            mc "It's been kinda depressing so far."
            s "I'm sure the romance parts of it will start to show."
            s "We just need to read more of it to find out."
            mc "I have a feeling I know who the love interest is."
            s "The new guy, right?"
            mc "Yeah, just basing it off what Monika said in the meeting."
            s "You never know..."
        else:
            mc "It's...uhh..."
            mc "Very interesting."
            s "I know, right?"
            mc "I feel like a lot of the stuff that's happened in this book..."
            mc "Have happened to us."
            mc "Don't you think?"
            s "Um...maybe?"
            mc "Sayori the events in the first week mirrored what happened to us."
            s "No, they didn't!"
            mc "A new person joins the club?"
            mc "They write poems to each other?"
            mc "Sounds pretty coincidential to me."
            "Or maybe there's more to it than that."
            s "There's still more to go."
            s "It could still change."
            mc "Maybe..."
            s "I'm just curious as to why Monika chose a horror book."
            mc "Maybe she's trying something new."
            mc "It's not up to us to wonder about that now."
            s "I guess not."
    elif ch14_overall_choice == "Yuri":
        mc "It's kinda strange to bring a radio to an island, isn't it?"
        mc "Who does that?"
        s "Didn't they say something about radios being important?"
        s "That's the reason they brought it."
        mc "They did?"
        s "You were the one reading it to me."
        s "Why are you asking me?"
        mc "Ah..."
        mc "Well, I suppose I was too focused on reading fast that I kinda wasn't paying attention."
        s "Ehehe, are you serious?"
        mc "...Yes."
        "Sayori giggles."
        s "That's really funny."
        s "It almost takes away from the horror the book is supposed to be showing."
        mc "Yeah."
        mc "It's only just started though."
        mc "It's got your typical horror stuff, like people getting separated."
        mc "I'm curious to see how it turns out."
        s "The time travel is kinda strange."
        mc "Yeah, I was expecting like going forwards or backwards in time."
        mc "Instead, they're stuck in a loop until they some a problem."
        s "The step-brother is such a nice person."
        s "I'd hate to see anything happen to him."
        mc "That's how you know something is going to happen to him."
        s "E-Eh?!"
    elif ch14_overall_choice == "Natsuki":
        mc "It's pretty interesting."
        mc "I think this alien guy is going to start getting into a lot of trouble though."
        s "Why?"
        s "He looks and acts just like everyone else."
        mc "For the most part."
        mc "But I have a feeling he's going to mess up somewhere."
        mc "And it's gonna get a bit weird."
        s "It is pretty sweet though."
        mc "Yeah, it's wholesome so far."
        s "And the characters are really cute too!"
        s "I can see why Natsuki likes this book so much."
        mc "Yeah, his adopted family seems really nice."
        mc "But I kinda get the feeling not everyone feels the way they are acting."
        s "What do you mean?"
        mc "It's kinda obvious, isn't it?"
        mc "One of the daughters seems pretty jealous of all the attention he's getting."
        mc "There was even a part where it showed her inner thoughts, remember?"
        s "Oh yeah!"
        s "I can't wait to see how it all ends up."
        mc "Yeah, me neither."
        mc "We haven't even gotten to the predicting the future part yet."
        s "I almost forgot he could do that."
        s "Natsuki seemed to make a big deal out of it."
        mc "I'm surprised it hasn't come up yet."
        mc "It's probably in the next volume."
        s "Ehehe, probably."
    else:
        mc "I probably have a biased opinion."
        mc "Seeing as it's the book I brought."
        s "I still want to hear what you think of it."
        s "Not just in general but the story too."
        mc "Hmm..."
        mc "Well, I like the idea of an ordinary person."
        mc "A lot of people can relate, especially me."
        s "Do you really think you're that ordinary?"
        s "There's a lot of things special about you, [player]."
        mc "Maybe."
        mc "But that's just how I percieve myself."
        s "You think you're just like that guy in the manga?"
        mc "In a lot of ways, yeah."
        mc "We do the same things..."
        mc "The difference is he's got that weird phone that can control events."
        s "It's got limitations though."
        mc "Yeah, I guess that's to make it not completely broken in the plot."
        mc "But him trying his best is nice."
        mc "He's only just got it, I promise it gets better."
        s "Ehehe, I believe you."
        s "I am kinda interested to see what he ends up doing with it."
        mc "I guess you'll just have to wait and see."
    s "Anyway, I guess we're done for now."
    s "I still need to make a couple of calls."
    s "But it's nothing I can't handle alone."
    mc "Are you sure, Sayori?"
    mc "I can stay longer, you know."
    mc "I really don't live that far."
    s "I'm sure, [player]."
    s "I really appreciated your help today."
    s "I'm sure we'll get this script done in time."
    mc "Alright, Sayori."
    mc "I have to ask though."
    s "What is it?"
    mc "Who are you calling?"
    s "Just everyone from the club."
    s "Making sure they have everything they need."
    mc "Is that all?"
    s "It's best you don't know."
    s "It might be too much of a surprise."
    mc "Try me."
    s "..."
    s "I think you should get home, [player]."
    s "We have a long day ahead of us tomorrow."
    mc "Are you hiding something from me?"
    s "If I was...would you hate me for it?"
    mc "Hate you?"
    mc "No way, Sayori."
    "Sayori looks away."
    mc "I just care about you."
    mc "If something is troubling you then..."
    s "Thanks...but it's fine."
    s "I'm going to call Natsuki now."
    s "Just to make sure all her supplies are right."
    s "I'll see you tomorrow, [player]."
    "Sayori gets her phone from her pocket."
    mc "Guess I'll see you then."
    mc "Sorry for trying to insist."
    "Sayori either didn't hear me or ignored what I just said."
    "She seems like she's waiting for an answer from Natsuki."
    "I wonder how her preparations are going."
    "And everyone elses..."
    "I should focus on myself too."
    "I still have to write a poem when I get home."
    "We're still doing this after all..."
    "But is there really any point in it...?"
    "Eh, better safe than sorry I guess."
    call screen dialog(message="To be continued!\nThanks for playing, keep an eye out on reddit and discord for updates!", ok_action=Quit(confirm=False))
    return
