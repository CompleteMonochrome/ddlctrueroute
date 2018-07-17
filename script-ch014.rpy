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
        show monika 1ha zorder 3 at f44
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
    y "The mascots of the restaurant come to life and start roaming around the restuarant."
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
        show monika 2he zorder 3 at f44
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
        show monika 2hh zorder 3 at f44
        m "I have to say, I don't really understand the significance and why it's a stepping stone to you."
        m "But still, I don't think there's anything wrong with getting the help of other people."
        m "And it's not like we're definitely going to choose a book with more than five characters."
        m 2ha "If we vote on the books that focus on five or less characters then it won't be a problem."
        m "Besides, the people who volunteer might be people who are interested in joining the club."
        m 1ha "So I don't really see any downside to it."
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
        "Or at least, I wouldn't have if she didn't tell me about it yesterday."
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
        show monika 1hc zorder 3 at f44
        m "Not to be {i}that{/i} person..."
        m "But wouldn't a book like that seem kinda..."
        m 2he "...I don't know, childish?"
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
    n 1q "It's set in medieval times and it's about a young girl who's parents are defenders of the realm."
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
        show monika 1hb zorder 3 at f44
        m "I suppose I'll be the one to break the silence."
        m "After all, I still have to share my books."
        "Monika places four books on the table."
        # Change some of the wording a little
        m 1hm "Ah...this just suddenly got a lot more difficult."
        m "It's strange sharing the books I read with you all."
        m "I know most of you have already seen me read these types of books but..."
        m 1hn "The ones I chose are all romantic adventure type books."
        if ch13_name == "Monika":
            m "[player] found that out yesterday."
        else:
            m "I guess it's only now [player] is finding out about this."
        m 1hj "The books I chose have that type of story about a person going through some sort of journey to get the love of their life."
        m "Or maybe finding love in a whole new place."
        m "Basically, the focus is around...love."
        show sayori 1q zorder 3 at f42
        show monika zorder 2 at t44
        s "Ehehe, this is exactly the type of stuff I thought you'd bring, Monika."
        s "It's so like you!"
        show sayori zorder 2 at t42
        show monika 2hl zorder 3 at f44
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
        show monika 2hn zorder 3 at f44
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
        show monika 4hl zorder 3 at f44
        m "Now hold on a second..."
        m "The two people who have to kiss don't have to be a guy and a girl, you know!"
        m 4ha "One of the novels even has two female lead characters that play the role."
        "Everyone looks at Monika in disbelief."
        m 4hb "I'm not saying that we {i}should{/i} be doing that!"
        m "I'm just saying that there's equal opportunity and [player] doesn't have to be the one to do everything."
        show sayori 1l zorder 3 at f42
        show monika zorder 2 at t44
        s "I think everyone is more scared there's gonna be a scene like that at all."
        s "It's not like any of us really want to do something like that in public."
        show sayori zorder 2 at t42
        show monika 2hc zorder 3 at f44
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
        show monika 1hj zorder 3 at f44
        m "You'll have to find that out yourself!"
        m "I don't want to spoil a good story after all."
        m 1ha "I will say that it's pretty sad and I know the little summary I gave you is kinda vague but I promise it's a good read!"
        "She replaces the book in here hands with the second one she brought."
        m 2he "This is the book with the two female leads."
        m "Basically, a rich, privileged girl falls in love with a more common girl."
        m "She becomes disillusioned with her life after seeing how the common girl's life works."
        m 2hf "Their love isn't really allowed because of the customs set into society."
        m 2he "I think it's a really sweet story of how people can overcome society's expectations and reach for what they want."
        m "There's no direct violence or anything, it's just a really good story."
        m "And the two main characters don't even have to be female!"
        m "We could have [player] play one of them, it would essentially still be the same."
        "Monika looks at me and smiles sweetly."
        m 2ha "Anyway, moving on to the third book..."
        m "This one is pretty cliché but I guess that's what made me like it so much."
        m 1hb "It uses a lot of the stuff found in love books and movies and puts it into one book."
        m "I don't know just how bad it might look during a play, but I think it could be interesting to find out!"
        m "It focuses primarily on a love triangle."
        m 1he "The main character has to choose between two people who he loves equally but can't find himself able to choose."
        m "Eventually, there's this old, wise character introduced that he goes to."
        m "That character helps him make a decision but its a bit unorthodox the way it's done."
        m "It will make for a hilarious play and you'll know in the end he made the right choice."
        show yuri 2pf zorder 3 at f43
        show monika zorder 2 at t44
        y "If he loved them equally, how would he have made the right choice?"
        y "Wouldn't choosing one break the heart of the other?"
        y 3ph "It seems like a book designed to make you hate the other character, the one he doesn't choose."
        show yuri zorder 2 at t43
        show monika 3ha zorder 3 at f44
        m "It's a lot more complicated than that, Yuri."
        m "I can't say too much more about the plot without completely ruining it."
        m 3hb "I will say that my heart was left satisfied after it was finished and I had a lot of laughs reading it."
        m "There are some inappropriate jokes we might need to get rid of but that's nothing."
        m 1ha "Anyway, the fourth and final book is probably my favorite one out of all of them."
        "Monika takes the fourth book from the desk and holds it high for everyone to see."
        m 1he "It's probably the book that's closest to my heart, which is fitting given it's name."
        m "It's called 'Sound of your Heartbeat' and it centers around a girl who comes to a realisation about life."
        m 1hf "Even though she's surrounded by a lot of friends, she starts to despise life because of the realisation."
        m "It becomes really difficult for her to do anything until this one guy comes along and changes her life."
        m 1he "Over the course of a week, they become great friends but they figure out that it's almost as if the world is keeping them apart."
        m "They have to figure out a way to be together to reach their happy ending against all the odds."
        "Monika smiles sadly."
        m 1hm "It's...a really beautiful story."
        m "Ahaha, just thinking about it makes me kinda sad."
        show sayori 1f zorder 3 at f42
        show monika zorder 2 at t44
        s "Why does it make you sad, Monika?"
        s "Does it have a really sad ending?"
        show sayori zorder 2 at t42
        show monika zorder 3 at f44
        m "Well, I won't spoil anything."
        m "But it is a pretty sad story about a forbidden love."
        m 1hn "I'd..."
        "Monika wipes her face then smiles."
        m "...recommend it to anyone."
        m 1he "So...yeah!"
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
        show monika 1hc zorder 3 at f44
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
        show monika 1hb zorder 3 at f44
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
            show monika 1he zorder 3 at f44
            m "Is something wrong, [player]?"
            m "You seem kinda..."
            m 1hl "...I don't know, worried?"
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
        mc "The actual manga isn't that many volumes too, only nine or ten."
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
            show monika 1hb zorder 3 at f44
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
        mc "He goes to an ordinary school and does orindary things."
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
        if ch13_yuri_books:
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
            "Is it better if I just say that?"
            "I had an opportunity last night to read this book or at least find a summary, so why didn't I?"
            "It's too late now..."
            "Maybe I'll just say it's no good."
            "What will Monika think? I borrowed this from her, didn't I?"
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
                            show monika 2hj zorder 3 at f44
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
    call screen dialog(message="To be continued!\nThanks for playing, keep an eye out on reddit and discord for updates!", ok_action=Quit(confirm=False))
    s "You all have to be one hundred percent committed with the books you brought."
    s "Any one of them could turn out to be the play."
    s "Take some away now if you didn't really intend for them to be part of the play."
    s "Maybe you just wanted to share it..."
    s "Just think carefully, okay?"
    menu:
        "Who am I voting for?"
        "Yuri.":
            $ ch14_book_choice = "Yuri"
            $ yuri_approval += 1
            "I'm obviously going to vote for Yuri's book."
        "Natsuki":
            $ ch14_book_choice = "Natsuki"
            $ natsuki_approval += 1
        "Monika.":
            $ ch14_book_choice = "Monika"
        "Sayori.":
            if sayori_personality > 0:
                $ sayori_personality -= 1
            $ ch14_book_choice = "Sayori"
        "Myself." if ch14_player_choice:
            $ ch14_book_choice = "Player"
    # After Choosing Book
    s "There's actually one thing I forgot to mention."
    s "It's pretty important so I'm not sure how I forgot it..."
    show natsuki zorder 3 at f41
    show sayori zorder 2 at t42
    n "What's so important?"
    show natsuki zorder 2 at t41
    show sayori zorder 3 at f42
    s "The book we chose..."
    s "The person who suggested it should be the director of the play."
    s "Since they know it the best!"
    s "Does anyone disagree?"
    return

label ch14_exclusive_yuri:
    return

label ch14_exclusive_natsuki:
    return

label ch14_exclusive_monika:
    return

label ch14_exclusive_sayori:
    return
