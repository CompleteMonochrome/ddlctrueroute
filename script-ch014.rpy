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
        show monika 1he zorder 2 at i22
        show monika zorder 3 at f22
        m "Sayori, may I have a word with you?"
        show sayori 1m zorder 3 at f21
        show monika zorder 2 at t22
        s "Monika?"
        s "What are you doing here?"
        s "Did you hear any of that conversation?"
        show sayori zorder 2 at t21
        show monika 1hm zorder 3 at f22
        m "Sayori, there's no time to explain."
        m "I have to tell you this, it's urgent."
        show sayori 1h zorder 3 at f21
        show monika zorder 2 at t22
        s "Urgent?"
        s "W-What are you talking about?"
        s "Monika, we're going to run out of time any second now!"
        show sayori zorder 2 at t21
        show monika 1hg zorder 3 at f22
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
        show monika 1ha zorder 3 at f31
        show yuri zorder 2 at t32
        show sayori zorder 2 at t33
        m "I wouldn't call it supernatural, Yuri."
        m "Maybe it's just the club being such an amazing place."
        m 2hb "Not to mention our friends are here."
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
        show monika 1hc zorder 3 at f31
        m "You certainly sound sure of yourself."
        m "It's almost as if you know exactly what she's thinking."
        m 1he "But if you say she's going to come, then I trust you."
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
        show monika 1hj zorder 3 at f31
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
        show monika 1hc
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
        show monika 1he zorder 3 at f31
        m "It's because of me, right?"
        m "If I was just better from the beginning..."
        m "Then you wouldn't need to deal with any of this."
        m 1hf "The responsibility you're dealing with is too much, Sayori."
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
        show monika 1ha
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
        show monika 1he zorder 3 at f42
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
        show monika 1hc zorder 3 at f42
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
        show monika 1hm zorder 3 at f42
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
    show sayori 1d zorder 2 at t42
    s "Alright, everybody!"
    s "As you all know, we have to select a book to perform for the play."
    s "So if you can all take the books you brought out, then..."
    s "We can get started on voting!"
    "Sayori beams."
    show yuri 1a zorder 3 at f43
    y "W-Well, I hope you all don't make fun of me for my choices..."
    show sayori zorder 3 at f42
    show yuri zorder 2 at t43
    s "Of course not, Yuri!"
    s "We've all got books that might be embarassing to share."
    s "But that's nothing compared to what's going to happen on Friday!"
    s "It's gonna be--"
    show natsuki 1a zorder 3 at f41
    show sayori zorder 2 at t42
    n "I dont't think you're helping, Sayori!"
    n "Look at her!"
    show natsuki zorder 2 at t41
    "Yuri looks a bit shaken from what Sayori said."
    "I guess I am a little bit too."
    "Doing something like a play in front of so many people seems like it would be really embarassing."
    "For some reason though, I don't feel so tense about it."
    show sayori zorder 3 at f42
    s "Sorry! I didn't mean it like that."
    s "I just meant that if we can't even decide on a book to choose..."
    s "Then how are we going to be able to do this play?"
    s "Besides, I don't think anyone here is going to be judging you."
    s "Isn't that right?"
    show sayori zorder 2 at t42
    if monika_type == 0:
        show monika 1a zorder 3 at f44
        m "Sayori is right."
        m "We've all got our own tastes and laughing at your choices would only dissuade us from doing something like this again."
        m "And that goes for everyone."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1ha zorder 3 at f44
        m "Sayori is right."
        m "We've all got our own tastes and laughing at your choices would only dissuade us from doing something like this again."
        m "And that goes for everyone."
    else:
        show monika 1a zorder 3 at f44
        m "Sayori has a point here."
        m "Laughing at such a minor thing would just dissuade us from doing something like this again."
    show sayori zorder 3 at f42
    show monika zorder 2 at t44
    s "I think we're all just waiting to see what everyone else chose."
    s "So please don't worry, Yuri!"
    show sayori zorder 2 at t42
    show yuri zorder 3 at f43
    y "O-Okay..."
    y "Then I suppose I can start by showing you the books that I have chosen."
    "Yuri reaches for her bag and pulls out four different books."
    if ch13_name == "Yuri":
        "I recognize those books from the ones Yuri brought yesterday."
    else:
        "Just from the look of the cover, I can tell they're all some sort of horror."
    y "These books are..."
    y "More of a dark theme, but less so than the ones I previously thought of bringing."
    y "I believe any of these choices would be suitable to do a play on."
    show sayori zorder 3 at f42
    show yuri zorder 2 at t43
    s "As long as there isn't too many characters in those books then they're perfectly fine!"
    s "Do you know how many characters are in them, Yuri?"
    show sayori zorder 2 at t42
    show yuri zorder 3 at f43
    y "There's only..."
    "Yuri thinks for a moment."
    y "If I remember, there's five characters in every single book."
    y "Or at least, five that are important enough to consider a character."
    y "But I don't think there's more than five characters in a scene at once, at least from what I can remember."
    y "I'll give you all a summary based on what I remember."
    y "I think that's the best way to find out about the book and also convince you all to choose one of them."
    "Everyone nods in agreeance."
    "Yuri picks up the first book she placed."
    y "This book here probably has the most mild themes out of the four I chose."
    # Oxenfree Reference
    y "It's about a group of friends who go to an island with some kinda mystery behind it."
    y "Basically some weird activity happens with a radio and then paranormal activity happens around the island."
    y "There's this...entity, I guess you could say."
    y "It starts controlling people but one person is immune for some unknown reason."
    y "I won't spoil it beyond that but it's definitely a good read and doable as a play."
    show yuri zorder 2 at t43
    mc "You know...I think I've heard of a plot like that before."
    mc "It involved a radio...or something."
    mc "It might have been a game or anime."
    show yuri zorder 3 at f43
    y "A game? No, I've never heard of anything like that."
    y "But it did involve a radio so..."
    y "Um...anyway."
    "Yuri puts the book down and takes the second book."
    y "This book is a little more..."
    y "...involved than the others."
    # Five Nights at Freddys Reference
    y "It's about someone who got hired as a security guard at a local restaurant."
    y "But it's during the night when things get weird."
    y "The mascots of the restaurant come to life and start roaming around the restuarant."
    y "The security guard kinda has to deal with it and as he gets throught the nights, some ulterior story is told."
    y "When I say involved, I mean there's some parts that might need to be changed."
    show natsuki zorder 3 at f41
    show yuri zorder 2 at t43
    n "Why? Does someone die or something?"
    "Natsuki says that jokingly."
    show natsuki zorder 2 at t41
    show yuri zorder 3 at f43
    y "..."
    show natsuki zorder 3 at f41
    show yuri zorder 2 at t43
    n "Forget I asked..."
    show natsuki zorder 2 at t41
    show yuri zorder 3 at f43
    y "I think it could still be something we could do!"
    y "Just made more suitable for everyone, I suppose."
    y "We can probably just exclude some parts if we have to, it's the story that's important."
    y "But anyway...this third book."
    # Slender Reference
    y "It's about this one stalker-type character."
    y "No one believes it exists so this group of friends decides to investigate."
    y "But then horrible things start to happen and they become the victims of the stalker."
    y "They soon find out the stalker isn't ordinary and have to figure out a way to defeat it."
    y "I don't want to mention too much about the story beyond that because it takes away the mystery."
    show yuri zorder 2 at t43
    if monika_type == 0:
        show monika 1a zorder 3 at f44
        m "A stalker-type character?"
        m "Sort of like a person that follows you endlessly?"
        m "And it's got supernatural abilities too..."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1ha zorder 3 at f44
        m "A stalker-type character?"
        m "I'm kinda interested to see where this goes..."
        m "A supernatural stalker..."
    else:
        show monika 1a zorder 3 at f44
        m "Hmm..."
        m "I admit I am kinda interested by this."
        m "How exactly are they going to beat this supernatural stalker?"
    show yuri zorder 3 at f43
    show monika zorder 2 at t44
    y "I almost didn't choose this book..."
    y "Because of how dark it can get...but I think it would be really good if we did a play on it."
    y "I still have to show you my fourth book."
    # Doki Doki Literature Club Act 2-3 Reference
    y "It's about this person who joins some kind of club at school."
    y "Everything seems normal at first but as time goes on, weird thing start to happen."
    y "People start dying and memories are changed."
    y "The person becomes traumatised because they can't escape or do anything to stop the madness that's happening."
    y "Eventually, there's only--"
    "Yuri pauses and smiles."
    y "Actually, I think saying that would be too much of a spoiler."
    y "But those are my four choices."
    show sayori zorder 3 at f42
    show yuri zorder 2 at t44
    s "Those books definitely sound...um, interesting..."
    s "They all seem like something I think you'd read, Yuri."
    s "I'm sure there isn't anything too crazy."
    s "From the summaries you gave, the costumes don't have to be too detailed."
    s "And they're perfect too since there's only a few characters!"
    s "I mean, some of those books have an evil thing you mentioned but we could always do a stage effect depending on what it is, right?"
    show sayori zorder 2 at t42
    show yuri zorder 3 at f43
    y "R-Right..."
    show natsuki zorder 3 at f41
    show yuri zorder 2 at t43
    n "Now that I think about it, the books I chose also only have five characters."
    n "I didn't even intend to do that."
    n "But I guess it all works out, doesn't it?"
    n "I mean there are only five of us..."
    show natsuki zorder 2 at t41
    show sayori zorder 3 at f42
    s "I actually chose my books based on the number of characters as well as the stuff I like to read."
    s "So I made sure that there was only five characters in each book."
    show natsuki zorder 3 at f41
    show sayori zorder 2 at t42
    n "Only five characters?"
    n "So you made sure that what you chose would be suitable for the play..."
    show natsuki zorder 2 at t41
    show sayori zorder 3 at f42
    s "Exactly!"
    s "I could always get some people to volunteer for us during the play if there's more than five characters in your book."
    s "I'm sure they'd be happy to help."
    show sayori zorder 2 at t42
    show yuri zorder 3 at f43
    y "Not that I don't believe you, Sayori..."
    y "But where are you going to find people that aren't busy and actually want to help out on Friday?"
    y "And isn't the point of this to showcase what the literature club is about?"
    y "If we enlist the help of others, it shows that the literature club--"
    y "Ah, I'm sorry if you all disagree with me."
    y "I'm just saying what's on my mind and I know it isn't really a big thing."
    y "But I'd personally like to make our part of this event independent of people outside the club."
    y "It's like...a stepping stone."
    show yuri zorder 2 at t43
    if monika_type == 0:
        show monika 1e zorder 3 at f44
        m "I don't really understand what you're getting at, Yuri..."
        m "...But I know it's important to you."
        m "Still, there shoudn't be a problem getting help from people outside the club."
        m "Even if they're part of the play, it's still {i}our{/i} show, Yuri."
        m "And besides, we might not even need their help if we decide to vote on a book with five or less characters."
        m "The people who do end up helping might be ones interested in the club and end up joining..."
        m "So maybe it counts as being independent of people outside the club...?"
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1he zorder 3 at f44
        m "I have to say, I don't really understand the significance and why it's a stepping stone to you."
        m "But still, I don't think there's anything wrong with getting the help of other people."
        m "And it's not like we're definitely going to choose a book with more than five characters."
        m "If we vote on the books that focus on five or less characters then it won't be a problem."
        m "Besides, the people who volunteer might be people who are interested in joining the club."
        m "So I don't really see any downside to it."
    else:
        show monika 1c zorder 3 at f44
        m "Is there really a point to this argument?"
        m "It kinda sounds like you're just trying to stir trouble for Sayori, Yuri."
        m "There's nothing wrong with getting the help of other people."
        m "In fact, those very people might even join the literature club with how much..."
        m "...{i}fun{/i} they'll have."
        m "So technically, it could end up being independent of others if they join."
        m "If it's a stepping stone to you, then there should be more in the future...right?"
    show yuri zorder 3 at f43
    show monika zorder 2 at t44
    y "I-I suppose..."
    "Yuri doesn't seem satisfied with the answer."
    y "It's not a big deal, as I said previously."
    y "I just wanted to say what my mind was telling me to."
    y "I-It almost felt like a compulsion, actually."
    show sayori zorder 3 at f42
    show yuri zorder 2 at t43
    s "Eh? A compulsion?"
    s "I don't think it's anything like that, Yuri."
    s "It's probably just you finally being more open, at least around us."
    show sayori zorder 2 at t42
    show yuri zorder 3 at f43
    y "D-Do you think so?"
    show natsuki zorder 3 at f41
    show yuri zorder 2 at t43
    n "I'd certainly say so!"
    n "The Yuri from a few weeks ago wouldn't have spoken her mind about the situation."
    n "At least, not before being asked for her opinion!"
    n "I think it's great!"
    n "But..."
    show natsuki zorder 2 at t41
    show yuri zorder 3 at f43
    y "B-But...?"
    show natsuki zorder 3 at f41
    show yuri zorder 2 at t43
    n "Well..."
    n "I think there are times when it's better not to say anything."
    n "If I said everything that was on my mind, then I don't think any of you would still be friends with me..."
    show natsuki zorder 2 at t41
    show sayori zorder 3 at f42
    s "Don't say that, Natsuki!"
    s "Of course we'd still be friends with you!"
    show natsuki zorder 3 at f41
    show sayori zorder 2 at t42
    n "That's not really the point I'm trying to get across."
    n "I guess what I'm trying to say is..."
    n "Don't always speak your mind, especially if it's going to hurt people."
    n "Some things are better left unsaid."
    n "And I know that's kinda hypocritical coming from me but--"
    show natsuki zorder 2 at t41
    show yuri zorder 3 at f43
    y "I think I get the point, Natsuki."
    y "I apologize to anyone if I caused a disturbance or offended you."
    y "Especially you, Sayori."
    show sayori zorder 3 at f42
    show yuri zorder 2 at t43
    s "Um...no harm done, I guess?"
    "Sayori looks a little bit confused at Yuri's apology."
    s "It's not like I can blame you for having an opinion."
    s "Though Natsuki does have a point."
    s "Some things are better left unsaid..."
    show sayori 1f
    "Sayori's face changes expression briefly before changing back into her happy self."
    "I don't think anyone else noticed."
    s "But anyway...!"
    s "You guys still haven't shown your books!"
    s "Only Yuri has shown her books...so why don't you go next, Natsuki?"
    show natsuki zorder 3 at f41
    show sayori zorder 2 at t42
    n "M-Me? W-Well, okay..."
    "Natsuki puts a hand into her bag to search for the books."
    n "Three of my four choices were manga."
    n "That shouldn't come as a surprise."
    n "But I did choose a novel as well."
    n "It's one I really liked as a kid and..."
    n "Well, it's kinda special to me but it's not like you guys should vote on it because of that."
    n "A-Anyway, here they are."
    "Natsuki places four books in front of us."
    "She picked the first volume of three different manga and a novel that I haven't really heard of before."
    if ch13_name == "Natsuki":
        "Or at least, I wouldn't have if she didn't tell me about it yesterday."
    n "These three manga are from three of my favorite series."
    n "I think they could be interesting choices for the play."
    n "The novel I chose is what my parents used to read to me when I was younger."
    show natsuki zorder 2 at t41
    if monika_type == 0:
        show monika 1a zorder 3 at f44
        m "I don't want to sound rude or anything..."
        m "But wouldn't that be too childish to do a play on?"
        m "We have to think about our target audience here, Natsuki."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1ha zorder 3 at f44
        m "Not to be {i}that{/i} person..."
        m "But wouldn't a book like that seem kinda..."
        m "...I don't know, childish?"
        m "I don't want to be mean but we should be thinking of the people who are actually going to be watching us."
    else:
        show monika 1a zorder 3 at f44
        m "A book from when you were younger?"
        m "Wouldn't something like that be a little childish?"
        m "Think of the people that are actually going to come along."
    show natsuki zorder 3 at f41
    show monika zorder 2 at t44
    n "It's not like that, Monika."
    n "You haven't even let me explain it yet, jeez."
    n "It's actually a pretty mature novel!"
    n "When my parents read it to me, they removed parts that might have been too hard to understand when I was young."
    n "I only found out about it when I reread it yesterday."
    n "I think it might be a really good option!"
    show natsuki zorder 2 at t41
    if ch13_name == "Natsuki":
        mc "You should tell them what you told me yesterday."
    else:
        mc "Well, what's it about?"
    show natsuki zorder 3 at f41
    n "I'll talk about it last."
    n "I want to convince you guys to choose the manga anyway."
    n "It's kind of more of a backup anyway..."
    n "Anyway..."
    "Natsuki picks up the first book."
    "To no one's surprise, it's a manga."
    n "I know we didn't really get to do a proper play of a manga."
    n "So I thought we could try again."
    n "I don't have enough copies for everybody but you can always read a copy online!"
    show natsuki zorder 2 at t41
    show yuri zorder 3 at f43
    y "Um...is that legal?"
    y "I don't think we can just read something we don't own online..."
    show natsuki zorder 3 at f41
    show yuri zorder 2 at t43
    n "Well...!"
    n "Everyone else does it so it's no big deal!"
    n "And it's not like it's gonna be a regular thing."
    n "It's just for the day."
    show natsuki zorder 2 at t41
    show yuri zorder 3 at f43
    y "But if we start there then where do we draw the line?"
    y "Maybe we--"
    show sayori zorder 3 at f42
    show yuri zorder 2 at t43
    s "Guys, it's okay!"
    s "We'll figure something out if it ever comes to it."
    s "No one is gonna have to do anything illegal, okay?"
    "Natsuki and Yuri stop and seem satisfied with what Sayori said."
    s "Now. Natsuki, what was the manga about?"
    show natsuki zorder 3 at f41
    show sayori zorder 2 at t42
    n "This is among my personal favorite series of manga."
    n "The first volume is pretty action packed itself but it's pretty short..."
    n "If we want, we could probably do the first two or three volumes."
    n "It's actually a comedy manga about cooking."
    n "These five people are put into a team and have to cook against other teams."
    n "It's a really fun and non-serious book and I think you'd all enjoy it."
    "Natsuki picks up the second manga."
    n "This one is about a society where everyone is born with a power, unique to everyone."
    n "They're all training to become heroes and it focuses around this one girl who has no power to begin with."
    n "But she gets a power through a different way and one of her rivals becomes annoyed because of it."
    n "It's really interesting seeing her beginnings and I'd recommend it to anyone!"
    "She looks around and doesn't see many interested faces."
    "That type of story isn't really for everyone, so I can understand why."
    n "Well...okay."
    "Natsuki picks up the third manga she brought."
    n "This is probably the most wholesome out of all of the ones I brought."
    n "Because of that, it's become one of my favorite manga."
    n "It's about the life of an alien in school. No one knows where he came from, not even himself."
    n "He's taken in by a family and for the most part he's the same."
    n "He looks just like anyone else and no one suspects he's an alien."
    n "What makes this manga good is that he has the ability to predict the future."
    n "He uses it to become an everyday hero and it's just an overall happy story."
    n "There are obviously some problems because he's an alien but that's not until later."
    n "If we want to do a happy themed play, then I'd really suggest this manga."
    show natsuki zorder 2 at t41
    show sayori zorder 3 at f42
    s "I think you chose some great books, Natsuki!"
    s "I'm curious what your fourth book is about though..."
    s "Were you keeping the best for last?"
    show natsuki zorder 3 at f41
    show sayori zorder 2 at t42
    n "I guess you guys can be the judge of that."
    "Natsuki slowly picks up the fourth and final book she brought."
    n "Like I said earlier, this book used to be read to me by my parents."
    n "They never finished it because I'd always fall asleep before it ended."
    n "Yesterday, I finished reading it for the first time and..."
    "Natsuki's grip on the book tightens."
    n "I know this probably won't be chosen."
    n "The story isn't that good either, I just found it really interesting when I was young."
    n "It's set in medieval times and it's about a young girl who's parents are defenders of the realm."
    n "At least, that's what they were called in the book."
    n "They served a queen and one day decided to send them on a mission to slay the dragon in the realm."
    n "But they never came back and the dragon was still alive."
    n "So the young girl makes it her goal to slay the dragon."
    n "Along the way, she meets people who try to help her get over it and...yeah."
    n "Like I said, it's not really a great story."
    n "It was just something I brought because...I don't know."
    n "Maybe you guys would have judged me for bringing four different manga."
    n "I know you guys wouldn't really."
    n "It was just on my mind that you would...like it was a possibility."
    n "So I brought--"
    n "I'm just going around in circles, so I'm gonna stop talking."
    show natsuki zorder 2 at t41
    show sayori zorder 3 at f42
    s "That book sounds great, Natsuki."
    s "I haven't heard of it before but it sounds like a really nice journey."
    s "And it's kinda like you, isn't it?"
    s "Your parents were..."
    s "They were good people."
    show natsuki zorder 3 at f41
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
        show monika 1b zorder 3 at f44
        m "It got really quiet all of a sudden."
        m "I guess that's an opportunity to start sharing my books."
        "Monika places four books on the table."
        m "Ah...this just suddenly got a lot more difficult."
        m "It's strange sharing the books I read with you all."
        m "I know most of you have already seen me read these types of books but..."
        m "The ones I chose are all romantic adventure type books."
        m "The story about a person going through some sort of journey to get the love of their life."
        m "Or maybe finding love in a whole new place."
        m "Basically, the focus is around...love."
        show sayori zorder 3 at f42
        show monika zorder 2 at t44
        s "Ehehe, this is exactly the type of stuff I thought you'd bring, Monika."
        s "It's so like you!"
        show sayori zorder 2 at t42
        show monika zorder 3 at f44
        m "Really?"
        m "I didn't mean to be predictable or anything!"
        m "These four books are just what I thought would be appropriate given the audience."
        m "There's nothing too weird going on, maybe just a kissing scene or two in all of them."
        m "I think the story is excellent as well, which make them pretty good candidates."
        show natsuki zorder 3 at f41
        show yuri zorder 3 at f43
        show monika zorder 2 at t44
        ny "A kissing scene...?"
        "Natsuki and Yuri both say that with equal parts shock and surprise."
        show natsuki zorder 2 at t41
        show yuri zorder 2 at t43
        show monika zorder 3 at f44
        m "It's not a big deal!"
        m "Most of the time, it's towards the end of the novel."
        m "Where the characters share a forbidden love or when they finally realize their love for each other."
        m "I promise it won't be too weird!"
        m "But you guys can decide that when we vote on which one we're going to be doing."
        show natsuki zorder 3 at f41
        show monika zorder 2 at t44
        n "Look, Monika."
        n "Have you thought about how [player] feels about all of this?"
        n "I mean, he's the only guy here so how do you think he feels about having to..."
        n "Y-You know..."
        show natsuki zorder 2 at t41
        show yuri zorder 3 at f43
        y "I agree with Natsuki here."
        y "We should consider how [player] feels about all of this."
        y "He's going to have to play the role of the person who has to do...that thing."
        y "N-Not that I'm entirely opposed to him doing that, of course."
        y "I-It's just..."
        show yuri zorder 2 at t43
        "Are they actually arguing because I'm going to have to kiss one of them if we choose Monika's books?"
        "I'm not sure whether they want or don't want to do that."
        "That said, it's not like it's going to be a real kiss."
        "It's just for the play after all..."
        mc "If it's for the play...then I'll do it."
        show monika zorder 3 at f44
        m "Now hold on a second..."
        m "The two people who have to kiss don't have to be a guy and a girl, you know!"
        m "One of the novels even has two female lead characters that play the role."
        "Everyone looks at Monika in disbelief."
        m "I'm not saying that we {i}should{/i} be doing that!"
        m "I'm just saying that there's equal opportunity and [player] doesn't have to be the one to do everything."
        show sayori zorder 3 at f42
        show monika zorder 2 at t44
        s "I think everyone is more scared there's gonna be a scene like that at all."
        s "It's not like any of us really want to do something like that in public."
        show sayori zorder 2 at t42
        show monika zorder 3 at f44
        m "That's...a fair point I suppose."
        m "If we do decide to vote for my books, then we can decide if there's a kissing scene in the play or not."
        m "But at least let me talk about them first."
        "Monika slowly picks up the first book and looks at it carefully."
        m "This one is kind of like an adventure turned into a love story."
        m "The main character enlists the help of mercenaries to get some sort of relic."
        m "Along the way, he meets the guardians of the relic and their leader."
        m "The two make an instant connection but once she realizes what he's there for, she has to call it off."
        show natsuki zorder 3 at f41
        show monika zorder 2 at t44
        n "That sounds like a pretty dumb plot."
        n "But I can only guess how it ends because of the type of book it is."
        n "He chooses her over the relic, right?"
        show natsuki zorder 2 at t41
        show monika zorder 3 at f44
        m "You'll have to find that out yourself!"
        m "I don't want to spoil a good story after all."
        m "I will say that it's pretty sad and I know the little summary I gave you is kinda vague but I promise it's a good read!"
        "She replaces the book in here hands with the second one she brought."
        m "This is the book with the two female leads."
        m "Basically, a rich, privilleged girl falls in love with a more common girl."
        m "She becomes disillusioned with her life after seeing how the common girl's life works."
        m "Their love isn't really allowed because of the customs set into society."
        m "I think it's a really sweet story of how people can overcome society's expectations and reach for what they want."
        m "There's no direct violence or anything, it's just a really good story."
        m "And the two main characters don't even have to be female!"
        m "We could have [player] play one of them, it would essentially still be the same."
        "Monika looks at me and smiles sweetly."
        m "Anyway, moving on to the third book..."
        m "This one is pretty cliché but I guess that's what made me like it so much."
        m "It uses a lot of the stuff found in love books and movies and puts it into one book."
        m "I don't know just how bad it might look during a play, but I think it could be interesting to find out!"
        m "Anyway, this one has a love triangle."
        m "The main character has to choose between two people who he loves equally but can't find himself able to choose."
        m "Eventually, there's this old, wise character introduced that he goes to."
        m "That character helps him make a decision but its a bit unorthodox the way it's done."
        m "It will make for a hilarious play and you'll know at the end he made the right choice."
    elif monika_type == 1 and ch12_markov_agree:
        show monika 1hb zorder 3 at f44
        m "I suppose I'll be the one to break the silence."
        m "After all, I still have to share my books."
        "Monika places four books on the table."
    else:
        show monika 1b zorder 3 at f44
        m "Ahaha, why the silence?"
        m "I guess I'll use this chance to share the books I chose."
        "Monika places four books on the table."
        m "These books are all from the mystery and horror genre."
        m "Some of the stuff that happens in them is kinda gruesome, so we might want to cut or replace it."
        m "I think they're all really good books though."
        m "I'd read them over and over and over and--"
        m "Well, you get the idea."
        m "I'd spend eternity just reading these books if I could."
        m "And do you know why?"
        m "Because I have."
        show yuri zorder 3 at f43
        show monika zorder 2 at t44
        y "Monika, I didn't think you'd be into this type of genre."
        y "It really doesn't seem like the type of stuff I'd imagine you reading."
        y "But here you are talking about it like it's the greatest form of literature."
        show yuri zorder 2 at t43
        show monika zorder 3 at f44
        m "These books are timeless, Yuri."
        m "You might have heard of them before."
        m "They're really old pieces of literature but I still find myself fascinated by them."
        show natsuki zorder 3 at f43
        show monika zorder 2 at t44
        n "Since when were you into horror?"
        n "The last book I saw you reading before [player] joined the club was some cheesy romance book!"
        n "Don't tell me he got you into horror books?"
        show natsuki zorder 2 at t43
        show monika zorder 3 at f44
        m "There's nothing wrong with that, is there?"
        m "But no, he didn't get me into horror books."
        m "I was into this long before everything else."
        m "I'm just sharing it now, because it's appropriate for what we're doing."
        show sayori zorder 3 at f42
        show monika zorder 2 at t44
        s "Even I didn't know that about you, Monika."
        s "But I guess it's good you're being honest with your taste in books now!"
        s "What are your books about anyway?"
        s "They all look like they have some kinda scary monster in them!"
        show sayori zorder 2 at t42
        show monika zorder 3 at f44
        m "Don't worry, Sayori."
        m "There's nothing to be afraid of."
        m "Monsters aren't real, after all."
        "Monika smiles meaningfully."
    # After Choosing Book
    s "There's actually one thing I forgot to mention."
    s "It's pretty important so I'm not sure how I forgot it..."
    show natsuki zorder 3 at f41
    show sayori zorder 2 at t42
    n "What's so important?"
    s "Even though the play we're doing might only have a few cha"
    call screen dialog(message="To be continued!\nThanks for playing, keep an eye out on reddit and discord for updates!", ok_action=Quit(confirm=False))
    return
