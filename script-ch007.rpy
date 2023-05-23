label ch7_main:
    if (y_appeal >= 1 or y_appealS >= 1) and (m_appeal >= 1 or m_appealS >= 1) and (s_appeal >= 1 or s_appealS >= 1) and (n_appeal >= 1 or n_appealS >= 1) and not yuri_date and not natsuki_date and not ch15_s_together:
        $ get_achievement("*Playboy*")
    # Setup Variable for Replay
    if persistent.ch6_task[2]:
        $ did_all_tasks = True
    else:
        $ did_all_tasks = False
    scene black
    show monika 1e zorder 2 at i11
    if from_custom_start:
        hide screen tear
        $ from_custom_start = False
        $ quick_menu = True
    else:
        with dissolve_scene_full
    play music mend
    m "It's me again."
    m 1c "I can't control whether I end up here or not..."
    m "I wasn't sure if it was by chance that I was here before..."
    m "But I'm guessing it's probably Sayori who's responsible for it."
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    $ pause(1.0)
    hide screen tear
    show sayori 1f zorder 3 at i21
    show monika 1c zorder 2 at i22
    show sayori at f21
    s "I know you want to be here for this Monika..."
    s "After all, you want to help Yuri and Natsuki too..."
    s "...right?"
    show sayori zorder 2 at t21
    show monika zorder 3 at f22
    m 1f "Yeah..."
    m "How did you know that anyway?"
    show sayori zorder 3 at f21
    show monika zorder 2 at t22
    s "I heard you talking about wanting to help them overcome their issues."
    s "To be honest, I didn't even know they had those kind of issues."
    s "But after looking into it, it turns our you're right."
    s "They both have horrible things they are hiding from everyone."
    s "I can't believe I couldn't see it...some friend I am, right?"
    show sayori zorder 2 at t21
    show monika zorder 3 at f22
    m "There's no way you could have known that anyway, Sayori."
    m "Those issues are deeply rooted within the fabric of their being."
    m "They wouldn't have been obvious if you and I didn't already know about them."
    show sayori zorder 3 at f21
    show monika zorder 2 at t22
    s "I don't fully understand what you're saying, Monika."
    s "I want to help them, they're my friends and they don't deserve to be sad like that."
    show sayori zorder 2 at t21
    show monika zorder 3 at f22
    m "...What are you planning, Sayori?"
    m "I was going to take it slow with them and help them get over it naturally, but it seems like you have other ideas."
    show sayori zorder 3 at f21
    show monika zorder 2 at t22
    s "You'll find out soon enough. Anyway, there's no time for that."
    s 1g "This is going to be short because today is super important."
    s "We're gonna read more of the novel in the club."
    s 1h "Then we're gonna organize who plays what character for the play."
    show sayori zorder 2 at t21
    show monika zorder 3 at f22
    m 1g "Sayori..."
    m "That book you chose was deliberate, wasn't it?"
    m "I can clearly tell this wanderer is meant to be me."
    m 1p "I mean she has the power to manipulate people and control events..."
    m "I could do all of that..."
    show sayori zorder 3 at f21
    show monika zorder 2 at t22
    s 1g "If I'm honest..."
    s "All the novels I chose have similar stories..."
    s "Even that picture book that [player] told me no one read..."
    s 1k "The only thing that's different is the manga."
    s "I know this will only work if we're doing manga for Natsuki."
    s 1d "So it's got a completely different story, relating to her."
    show sayori zorder 2 at t21
    show monika zorder 3 at f22
    m 1a "I don't fully understand your plan here..."
    m 1e "I know you have good intentions but please be careful, Sayori."
    m "Some things just can't be solved the way you think they can be."
    m 1a "People are complicated, you know?"
    m 1e "That said, I know that making you president was a good idea."
    m "Whatever your plan is, I'll go along with it."
    m "I'm sure they'll be better off for it."
    show sayori zorder 3 at f21
    show monika zorder 2 at t22
    s "Thanks Monika..."
    s "That still leaves {i}you{/i}."
    # Not helping both times
    if sayori_personality == 2:
        s 1f "What are you doing?!"
        s "It's like you don't want to help us at all."
        s "I basically had to force you to agree to help..."
        s 1j "You...!"
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m 1p "Sayori..."
        m "Calm down."
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s "I'm..."
        s 1k "...sorry."
        s "But it was for my friends."
        s 1g "You know how much I care about them..."
        s "So when I see that you're not doing your best to help us..."
        s 1k "...it feels like a betrayal."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m 1g "What happened?"
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s "..."
        s 1g "It's better you don't know."
        s "I'd rather not have to do that again."
    # Not helping just then
    elif bad_choice_first:
        s 1g "Why would you do that?"
        s "You made me do something awful."
        s 1k "It took so much out of me..."
        s 1h "I know you care about them more than that..."
        s "Why would you even try to do something that's against who you are?"
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m 1g "What happened?"
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s 1k "A bad decision..."
        s "But..."
        s 1d "It's okay now."
        s 1k "It's better that you don't know Monika."
    # Not helping before
    elif sayori_personality == 1:
        s 1j "Even if you said you didn't care about them as much as I do..."
        s 1d "You've been so helpful."
        s "I'm glad I didn't have to do anything rash."
        s 1g "But if I had to, I would have..."
        s "You know how much I care about everyone..."
        s "There's nothing I wouldn't do for them."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m 1g "Sayori..."
        m "Are you feeling okay?"
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s 1k "I..."
        s "I'm fine."
        s 1d "It's just this new responsibility."
        s "It must be getting to me."
    else:
        s 1a "I want to thank you so much."
        s "You've been so helpful and I just know you care about them so much!"
        s 1d "I'm glad I didn't have to do anything rash."
        s 1g "But if I had to, I would have..."
        s "You know how much I care about everyone..."
        s "There's nothing I wouldn't do for them."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m 1g "Sayori..."
        m "Are you feeling okay?"
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s 1k "I..."
        s "I'm fine."
        s 1d "It's just this new responsibility."
        s "It must be getting to me."
    s 1d "In any case, [player] agreed to spend lunch with Yuri."
    show sayori zorder 2 at t21
    show monika zorder 3 at f22
    m 1d "Oh..."
    m "I was gonna suggest that to [player] today."
    show sayori zorder 3 at f21
    show monika zorder 2 at t22
    s "I..."
    s 1l "...may have listened to your conversation after the meeting."
    s "Sorry, I realize it was meant to be private..."
    show sayori zorder 2 at t21
    show monika zorder 3 at f22
    m 1f "Ah, so you know about the favor I asked [player_reflexive] to do?"
    m "I guess there's no hiding anything from you, is there?"
    show sayori zorder 3 at f21
    show monika zorder 2 at t22
    s "I-It's not like that. I was trying to figure out some things and it just happened like that..."
    s 1g "But that's right, I know about the favor."
    s "It's a good idea. I think it's already her second time going over the book."
    s "Who knows how badly she's been affected by whatevers written inside it now."
    show sayori zorder 2 at t21
    show monika zorder 3 at f22
    m "I didn't realize she went through it once already."
    m "We better act soon."
    m "There's something about that book that's bothering me but I can't quite figure out what."
    m "Or maybe I'm just thinking about it too much..."
    m 1e "In any case, I'm glad we're on the same page."
    show sayori zorder 3 at f21
    show monika zorder 2 at t22
    s 1d "[player]..."
    s "The real one."
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() != player.lower():
            s "Or should I say [currentuser]...?"
    s 1k "What you made [player] do..."
    if did_all_tasks:
        s 1d "You listened to me, didn't you?"
        s "I'm glad you did because I wasn't sure how to tell you right there."
        s "I felt like if I said the wrong words, [player] would have remembered..."
        s "And all of this would have been for nothing."
        s "But..."
        s "You wrote a good poem and managed to read a decent bit of the book."
        s 1h "We might need to do something like that again..."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m 1d "What did [player_personal] do?"
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s 1d "[cPlayer_personal] made it work."
        s "That's all I can really say without breaking the game."
        s 1t "Today is going to go great, I can feel it."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
    elif read_book:
        s 1b "From what I can tell, [player_personal] read quite a bit of the book."
        s "So we don't have much to worry about."
        s 1k "[cPlayer_possessive] poem on the other hand leaves something to be desired."
        s 1i "It isn't that important but it could affect the [player] in the game."
        s 1d "Regardless, I can tell today is going to be okay."
        s "It's not ideal but it's the second best possibility."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m 1d "What do you mean?"
        m "Was [player_personal] meant to do something?"
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s 1g "I told [player_reflexive]."
        s "[cPlayer_personal] didn't do it and I can't make [player_reflexive]."
        s "If I tell you directly, the game might break."
        s 1h "I don't want to risk it."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m 1e "I understand."
    else:
        s 1i "Why would you get [player] to write a poem?"
        s "We wanted you to read the book so you could talk to Yuri..."
        s 1k "Now [player_personal]'s going to be super weird when [player_personal] talks to her."
        s "[cPlayer_personal] won't have anything to discuss..."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m 1e "I could go with [player_reflexive]."
        m "I've read a decent amount of the book."
        m "We can--"
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s "I know you mean well Monika..."
        s 1g "But Yuri won't change anything if you're there."
        s "She'll act like she usually does in the club especially if someone from the club shows up."
        s "We have to go with it."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m 1f "..."
        m "Alright Sayori..."
    m 1q "I hope everything works out."
    m "There's so much at stake here."
    show sayori zorder 3 at f21
    show monika zorder 2 at t22
    s 1g "Well...it's time to wake up."
    s 1k "So we'll find out shortly..."
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    $ pause(1.0)
    hide screen tear
    hide sayori
    show monika 1f zorder 2 at i11
    m "Sayori really has changed, hasn't she?"
    m 1e "To everyone else, she's just the same cheerful old person."
    m "But between you and I..."
    m 1j "Well...we know better."
    m 1h "I know she's doing everything she can for her friends..."
    m "But do you think maybe she'll end up hurting everyone else in the process?"
    m "I'm still believe that change, especially the issues that Yuri and Natsuki are dealing with, should be natural."
    m "It can't be forced onto someone by changing who they are."
    m "Because at that point, are they really the same person anymore?"
    m "I don't know, I just think that's the path Sayori is going to follow."
    m 1l "Ah..."
    m "I've spoken for too long."
    m 1m "You're probably gonna end up late for school."
    m 1e "Keep your eyes peeled, [player]."

    stop music fadeout 2.0

    $ persistent.ch6_task = [False,False,False]
    $ renpy.save_persistent()
    scene bg bedroom
    with dissolve_scene_full
    play music t2

    if did_all_tasks and not read_book:
        "I had a look at the first chapter of the Portrait of Markov this morning..."
        "And it seemed exactly like something in my memory..."
        "Quickly looking through more of it, everything seemed familiar up to chapter seven."
        "I'm not sure if that's coincidence or what..."
        "But I'm glad I managed to write a good poem and hopefully have something to talk about with Yuri."
    elif did_all_tasks and read_book:
        "When I was writing my poem this morning..."
        "I felt like I knew exactly what I wanted my poem to be and just wrote it."
        "Looking at it right now, it doesn't seem that bad."
        "I somehow put effort into it while having to read that book Monika and Sayori wanted me to."
    elif not did_all_tasks and not read_book:
        "I had a look at the first chapter of the Portrait of Markov this morning..."
        "It wasn't long and I think I memorized a decent part of it."
        "It probably wasn't what Monika and Sayori wanted from me but I didn't have much time."
        "Besides, at least I wrote a good poem for the club."
    else:
        "Last night, I managed to read a decent amount of the book Monika and Sayori wanted me to."
        "That said, the poem I wrote this morning turned out really bad."
        "It's shorter than most of my other ones and everyone will be able to tell it's terrible."
        "But at least Monika and Sayori will be satisfied I can fulfill their favors."
    "I make my way downstairs where I hear some annoying knocking going on."
    scene bg house
    show sayori 1a zorder 2 at t11
    with wipeleft_scene
    s "Ah, you're finally awake!"
    s 1q "I told you that I'd be the one waiting outside this morning."
    s "And I was right~"
    mc "Well, you got me there."
    mc "I didn't exactly have the best night with everything I had to do."
    mc "Write a poem...read two different books..."
    mc "And I just couldn't get out of bed this morning."
    mc "It's like I was just physically stuck there for a while."
    s 1a "You sure you just weren't being lazy this morning?"
    mc "Yeah, whatever..."
    s 1g "You read some of that other book at least, right?"
    mc "Yeah...some."
    s 1d "Well, that's all I can ask for!"
    s "Thanks [player]!"
    s 1b "What do you think about the club book?"
    mc "Sayori..."
    mc "Can you at least get out of the way before I answer that question?"
    s 1l "W-What?"
    mc "You're standing right in the middle of the doorway."
    s 1r "Ehehe, sorry. Let's go."
    scene bg residential_day
    show sayori 1a zorder 2 at i11
    with wipeleft_scene
    mc "The book is pretty good I guess."
    s "You remember what I told you yesterday?"
    mc "About spending time with Yuri?"
    mc "How could I forget?"
    s 1d "I'm just making sure..."
    mc "How will I know where to find her, anyway?"
    s 2o "She's usually in the library..."
    s "...so try looking in there?"
    mc "The library?"
    s 2d "Yeah! She's usually just reading books in there."
    s "I'm sure you can find her."
    mc "Well...alright."
    mc "I'm still not feeling comfortable talking to her just to change her."
    mc "But you know what's best..."
    s 4a "It's not a bad change, I can promise you that."
    s "It might be difficult, but she will tell you something."
    s "I just hope you know what to say."
    mc "That's the most cryptic thing you've ever said."
    s 1q "Ehehe~"
    s "Just stay sharp, okay [player]?"
    mc "Yeah, yeah..."
    scene bg library
    with wipeleft_scene
    play music t6say fadeout 1
    "Soon enough it's lunch time."
    "Sayori said I'd find Yuri in the library."
    "I don't really go here much..."
    "So I'm a little lost."
    if ch5_name == "Monika":
        "Something about the place does feel familiar though."
    else:
        "This place is huge..."
    "That said, there's barely anyone in here but a librarian and a couple of bookworms."
    "I look around for Yuri."
    "I'm guessing she's probably in the horror section of the library seeing as that's what she likes to read."
    scene bg library_shelf
    with wipeleft_scene
    "Before long, I manage to find the horror section."
    "It's in a secluded corner of the library."
    show yuri 1a zorder 2 at t11
    mc "Hi Yuri."
    y 1e "[player]...?"
    y "I didn't expect to see you here..."
    mc "There's nothing wrong with me being here, is there?"
    y 1g "Um..."
    y "You're welcome to be here of course..."
    y "I can't stop you..."
    y "But, if I may ask..."
    y 3f "Why are you here?"
    mc "Well..."
    "I pull out the Portrait of Markov from my bag."
    mc "We never really got a chance to talk about this book, did we?"
    y "..."
    y 3g "I thought you forgot about that..."
    y "...I've already finished reading it."
    y "Actually, I suppose it's more accurate to say I've finished rereading it."
    mc "You've read this book before?"
    y "Ah...well, I just enjoy it a lot."
    y "I wanted to share it with you because the story was so captivating to me."
    y "S-Sorry I didn't say that sooner."
    mc "Well, that's okay. I'm just glad you shared it with me."
    mc "And besides, it just means we can talk about the book since you're basically an expert on it."
    y 3h "I don't know about being an expert but talking about it..."
    y 3i "That would be nice..."
    y 3f "But why are you spending time with me now...?"
    y "It's lunch...shouldn't you be out with your friends?"
    mc "Well, you're my friend."
    mc "So technically, I am."
    y 1n "Ah...!"
    y 1q "Well...I suppose you're right."
    y "How much have you read?"
    y "I don't want to spoil anything for you..."
    if read_book or did_all_tasks:
        $ yuri_approval += 1
        mc "I've read a decent amount."
        mc "I'm up to chapter seven."
        y 1i "Oh, so you're aware of her situation?"
        mc "Yeah, everything she does only makes things worse for her."
        mc "It's quite sad, but it really reeled me into the story."
        mc "So I'm grateful you bought me a copy."
        y 1a "That's okay."
        y 1h "I don't know why..."
        y "But I feel as if I chose that book for a reason."
        y "Out of all the books in the store..."
        y 1t "...it was the only one that I thought would be suitable for you..."
        y "It doesn't make sense because..."
        y 1v "I was only there to buy myself a book..."
        y "...then this thought just came into my head..."
        y "I..."
        y 1o "I'm rambling, aren't I?"
        y "Sorry..."
        mc "That's okay."
        mc "You don't need to apologize to me for those sorts of things."
        mc "I don't mind listening to you ramble on."
        mc "Besides, that's what makes you interesting."
        y 4b "I-Interesting?"
        y "I don't..."
        y "I don't think you're making sense..."
        mc "It's true..."
        y 4a "..."
        y "Y-You're too nice to me, [player]."
        y "You shouldn't..."
        mc "Why not? I can't help being a nice person, especially to a friend."
        y 4b "N-Never mind..."
        y "You came here to talk about the book, right?"
        y 1w "So...let's talk."
        mc "Right."
        y 1t "I know the story is..."
        y "Well, not for the faint of heart."
        y 1u "I'm happy you stuck through with it."
        mc "I should be thanking you for introducing me to it."
        mc "I kinda regret not starting it earlier."
        y 1t "What stopped you...?"
        y "Um..."
        y "I-I shouldn't be delving into your personal life..."
        y 1v "S-So you don't need to answer that."
        mc "Well..."
        mc "I guess I wasn't really interested in reading it until now."
        y 1h "I'm sorry if I'm prying..."
        y 2f "But what made you change your mind?"
        "I think back to what Sayori said."
        "I'm the only one that Yuri will open up to."
        "I decide it's best if I don't tell her anything about that."
        mc "I don't know."
        mc "It was just on my mind, so I started reading it."
        y 1g "Hmm..."
        y "I just find it weird that you're only starting now..."
        y "After we got the novel for the club."
        mc "Maybe that's it."
        mc "The novel got me into reading and I was just looking for something different."
        mc "I have to say, I'm enjoying Portrait of Markov more than A New Epiphany."
        y 2e "The club novel is pretty simple..."
        y "But what Sayori said yesterday..."
        y 2h "About it being what I needed my whole life...?"
        y 2o "Ah..."
        y "I'm getting off topic."
        y "S-Sorry."
        mc "Hey, Yuri..."
        mc "This might be a silly thought, but..."
        mc "The main character in the Portrait of Markov kind of reminds me of you a little bit."
        y 1f "How does she?"
        mc "Well, I guess she's more blunt in a lot of ways..."
        mc "But she also second-guesses all of the things that she says and does."
        mc "Like she's afraid she'll do something wrong."
        mc "It's not like I can see into your head or anything..."
        mc "But they're kind of reminiscent of some of your mannerisms."
        y 1v "I-I see..."
        "Yuri remains silent for a moment."
        y "But [player]..."
        y "That's probably..."
        y 1w "...a terrible thing to have in common with her!"
        y 4b "Uuuh, that's so embarrassing that you think that..."
        mc "W-Wait!"
        mc "I didn't mean it in a bad way or anything!"
        mc "I forgot that you were sensitive to that kind of thing..."
        mc "I just meant that it's cute."
        y 3q "A-Ah--"
        y "What are you saying all of a sudden...?"
        y "I...!"
        y "[player]..."
        y 3v "Sigh..."
        y 3s "You really don't know what it means..."
        y "...for you to be here..."
        y 3w "I really..."
        y "I want to tell you..."
        y "I..."
        mc "What do you want to tell me?"
        mc "I'll listen to anything you have to say."
        mc "I'm here for you, you know that."
        y 2k "The truth is..."
        y "I..."
        y "I have a habit..."
        mc "A habit?"
        y 2o "It's...like the book..."
        y "Not exactly for the faint of heart..."
        if ch4_name == "Yuri":
            y "Do you remember how I've got a..."
            y 2q "...passion for knives...?"
        else:
            y "You might not know this..."
            y "But I've got a passion..."
            y 2q "...for knives..."
        mc "Knives?"
        mc "There's nothing wrong with that."
        mc "We're all into our own things."
        mc "I'm sure if you knew what I was into, I'd feel what you're feeling now."
        "Yuri smiles shyly."
        y 1u "I-Is that so?"
        mc "Yeah, I can tell you all about it."
        mc "I mean...it's a bit embarrassing..."
        mc "But if we're sharing secrets."
        y 1t "Ah..."
        y "There's no need to do that."
        y "After all..."
        y 1u "Mine won't be a secret for much longer."
        y "I don't know why but today it just felt like my urges have become more uncontrollabe."
        y "Usually I would be able to restrain myself on acting on them."
        y "But..."
        "Yuri's voice trails off."
        play music t10 fadeout 1.0
        mc "What do you mean?"
        y 1t "I'm just going to say it..."
        y "Before it's too late."
        y "I can already feel it coming."
        y 1w "[player]..."
        y 1s "I'm in love with you."
        mc "Yuri...?"
        y 1v "P-Please, let me finish."
        y "Before you do what you have to."
        y 1t "Ever since you joined the club..."
        y "I've felt this urge within me."
        y 1w "An urge, I felt I needed to suppress because..."
        y "It could hurt..."
        y "The people I care about."
        y 1t "So I did."
        y "I stopped myself, for a while."
        y 1v "But over time...it became stronger."
        y "It was like an inevitability."
        y "I really thought I could keep this urge contained."
        y "But something happened so recently that's stopping me from doing that."
        y "I don't know what it is [player]...and I'm scared."
        y "It's like I can't control myself anymore."
        "I don't know why she's confessing all of these things to me."
        "And judging by what she's saying, she doesn't either."
        mc "Yuri...just calm down. Take a deep breath."
        mc "Y-You'll be okay."
        "She seems panicked. I have to try and calm her down."
        y 1t "Do you know..."
        y "...the things I've done to stop myself?"
        y 1v "I did everything I could think of."
        y 1r "But that feeling of dread..."
        y "That urge to hurt my friends..."
        y 1t "It's only gotten stronger."
        y "I isolate myself because I care about my friends..."
        y 1w "...because I care about you."
        y "The Literature Club..."
        y "I don't know why..."
        y 1v "But it's the only thing stopping me."
        y "And yet...it feels like it's the reason I'm becoming like this."
        y "If I wasn't in it, I don't know what I'd be doing right now."
        y "Would I be able to contain my urges?"
        menu:
            y "Or would I be some kind of psycopath?"
            "You're not a psycopath.":
                y "That's kind of you to say."
                y "I don't really know if that's true but..."
                y "It's nice to have someone believe in me."
            "You're a psychopath.":
                if yuri_approval > 0:
                    $ yuri_approval -= 1
                y "I see...that's what you really think of me?"
                y "I'm just a psycopath, am I?"
                y "...I suppose you're right."
        y "But in the end, it doesn't really matter."
        y "I can't stop myself, [player]. I have to act on these urges."
        y 1l "I need you to know this next part especially..."
        y "So, please."
        y "Listen carefully, it will be the first time I've told anybody."
        y "I don't know why I'm telling you..."
        y "But something tells me I have to..."
        y "That you're the right person."
        "Yuri exhales."
        y 1w "I cut myself..."
        y "At first, it was just to see what it would be like."
        y 1t "Then...it became something I did..."
        y "For fun..."
        y 1v "Then..."
        y "It became something I would do..."
        y "...for pleasure."
        y 1w "I couldn't stop myself."
        y "But I was always able to keep it to myself."
        y "I had no reason to reveal it to anyone."
        y "And yet every time you're near me..."
        y "I don't know why..."
        y "I have this compulsion to tell you everything."
        y "Like you can help me somehow..."
        "Yuri looks at me with a confused look on her face."
        y "It's all nonsense, isn't it?"
        mc "Did anything happen in the past few days to make you feel this way?"
        y "I don't know, it all happened so suddenly."
        y "I just think you're somehow connected to all of this."
        "I turn my gaze towards Yuri's arm."
        "Is that where she's cutting herself...?"
        "She notices me and quickly puts her hands behind her back."
        mc "If you want my opinion, I don't think cutting yourself is a good idea."
        y 1t "But I feel like if I don't cut myself, I'm going to die."
        y "An when I'm with you, that feeling only gets more intense."
        y "Why does someone I love bring feelings like this?"
        y 1v "Is that what love is?"
        y 1t "Is that what's making me feel like this?"
        y "[player]..."
        stop music
        $ config.skipping = False
        $ config.allow_skipping = False
        y 3y2 "I can't help it anymore."
        y "I have to do this."
        y 3y1 "Ahaha, I'll understand if you hate me for this."
        y 3y3 "But I just can't hold myself back anymore!"
        "She pulls out a knife from her pocket."
        show yuri stab_1
        mc "Yuri...!"
        if did_all_tasks:
            python:
                try: os.remove(config.basedir + "/It was easy.txt")
                except: pass
                try: os.remove(config.basedir + "/This is hard.txt")
                except: pass
                try: renpy.file(config.basedir + "/A message.txt")
                except: open(config.basedir + "/A message.txt", "wb").write(renpy.file("A message.txt").read())
        else:
            python:
                try: os.remove(config.basedir + "/A message.txt")
                except: pass
                try: os.remove(config.basedir + "/This is hard.txt")
                except: pass
                try: renpy.file(config.basedir + "/It was easy.txt")
                except: open(config.basedir + "/It was easy.txt", "wb").write(renpy.file("It was easy.txt").read())
        $ _history_list = []
        mc "Stop!{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.5)
        stop sound
        scene black
        show monika 1e zorder 2 at i11
        hide screen tear
        play music m1
        m "That was really close."
        m "I was listening in, just in case there any useful information that we could use to help her."
        m "I had some idea of what was with Yuri but I didn't realize the extent."
        m "I wonder why she's acting that way all of a sudden."
        m "She said her feelings for you are making her act that way."
        m "But I think there might be something else..."
        m "...or rather, {i}someone{/i} else."
        m "Ah, but that doesn't matter right now."
        m "Yuri was about to do something she was going to regret."
        m "It looks like Sayori stopped it from happening."
        m "She got 'you' out of there, just in time."
        m "In case you didn't realize..."
        m 1h "The game is frozen."
        m "As we're talking, Sayori is erasing the whole library thing."
        m 1f "Everyone is gonna forget what just happened."
        m 1e "But Sayori was right."
        m "Talking to Yuri alone was the only way to find out what was wrong with her."
        m "If I was there, I might have messed things up."
        m 1f "That's probably the best outcome we could have gotten."
        m 1e "I'm surprised she managed to control herself for that long."
        m "Hmm..."
        m "I should let you know..."
        m "It isn't entirely because of the game 'you' that she's feeling that way."
        m 1f "[cPlayer_personal] was just the catalyst."
        m "It's the book."
        m 1g "I read some of it and it's got the same effect on me."
        m "Once I realized, I stopped immediately."
        m "I'm still not sure if it's affected that 'you' in the game."
        m 1d "But we have to hope it doesn't, otherwise everything could go wrong."
        m 1e "It took me a while but..."
        m "I think I figured what Sayori has planned now."
        m "We have to save Yuri during the play."
        m "It's our best shot."
        m "I just hope it works."
        m 1d "Oh..."
        stop music fadeout 2.0
        m "It appears as if she's done."
        m 1a "See you!{nw}"
        $ config.allow_skipping = True
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        stop sound
        hide screen tear
    else:
        if yuri_approval > 0:
            $ yuri_approval -= 1
        mc "Well..."
        mc "Not much."
        mc "Do you mind filling me in on some lost details?"
        mc "I don't mind if you spoil it for me..."
        y 2h "You don't find it interesting...?"
        y 2i "Well, everyone does have their own tastes..."
        mc "That's not true."
        mc "I just couldn't find a lot of time to read it."
        mc "That's why I'm talking to you, because I'm actually really interested in it."
        "That's not really true, but Sayori wanted me to spend time with Yuri."
        "So I guess I'll say anything that makes Yuri spend more time with me."
        y 2q "Well..."
        y "Why don't we just read it together instead?"
        mc "But you've already finished it..."
        mc "I don't want to assume anything, but won't you get bored?"
        y 1u "Ah, [player]..."
        y "If only you knew..."
        y "Whenever I spend time with you..."
        y "Nothing is boring."
        mc "Do you mean that?"
        y 1n "W-What?"
        y "Did I say that out loud...oh no..."
        y 1o "You think I'm really weird now, don't you?"
        y "...oh gosh..."
        y "I shouldn't have said anything..."
        y "This is only going to get worse..."
        y 1p "[player]...please you..."
        y "I should g--"
        mc "Yuri, it's alright."
        mc "You don't have to leave because I went here."
        mc "In fact, I'd appreciate it if you stayed."
        y 1n "R-Really?"
        mc "Yeah, we don't have to talk about the book."
        mc "Why don't we just talk about ourselves?"
        y 1q "Um..."
        y 1s "Alright."
        y "..."
        "Yuri remains quiet, unable to come up with anything to say."
        mc "I guess I'll start it off..."
        mc "Why do you hang out over here, by yourself?"
        mc "Don't you want to spend some time with Monika, Natsuki, Sayori..."
        mc "...or even me?"
        y 1v "Hmm..."
        "Yuri thinks for a moment."
        y "Well...I don't want to go out of my way spending time with them..."
        y 1t "Unless it's for the club, I don't really talk to any of them..."
        mc "Oh..."
        mc "So I guess me being here probably isn't a good thing."
        y 1p "N-No!"
        y "I didn't mean it like that..."
        y 1q "I should have phrased it better..."
        y 1t "I don't want to go out of my way to spend time with the other three."
        y "You are..."
        y 1s "...an exception."
        mc "So you only like spending time with me?"
        mc "Is that what you're trying to say?"
        y 1v "I mean..."
        y "You don't have to feel the same way..."
        y "But..."
        "Yuri mumbles out that last part."
        "I can't believe that Yuri feels this way about me."
        "Is this what Sayori meant when she said she would only talk to me about it?"
        if sayori_confess:
            "Sayori and I are already a couple..."
        elif ch5_name == "Yuri" or ch4_name == "Yuri":
            "I've already spent time with her before..."
            "Do I feel the same way?"
        else:
            "I've barely spent any time with her..."
            "This is such a weird position to be in..."
        "What do I tell her?"
        "My goal was to change her, right?"
        "To get her to open up..."
        "I guess she is opening up, but this seems unhealthy."
        "She only likes spending time with me."
        "If I had read more of the book, then this conversation would have gone a lot better."
        mc "Yuri..."
        mc "I'm not really sure how to react to that."
        y 1w "Oh..."
        mc "That's not me saying I don't like your company as well..."
        mc "But isn't that a little odd?"
        mc "You were in the club before me..."
        mc "So you would have made friends with the other members."
        mc "I just don't get why I'm the center of your attention."
        y 1t "Isn't it obvious?"
        y "I..."
        play music t10y fadeout 1.0
        y 1u "I love you, [player]."
        mc "Yuri...?"
        y 1t "Every time you spend time with someone else..."
        y "I get this urge within me."
        y 1v "I tried to stop it at first..."
        y "I knew it was a bad thing..."
        y 1w "I barely knew you, \"why would I feel this way...?\""
        y "That's what I told myself."
        y "But..."
        y 2y2 "It's uncontrollable..."
        y "It feels like an inevitability."
        y "Like this was meant to happen..."
        y 2y1 "Do you know what I mean, [player]?"
        mc "Yuri..."
        mc "Before we go on, I need to tell you something."
        mc "Sayori told m--"
        stop music
        $ config.skipping = False
        $ config.allow_skipping = False
        y 2y4 "Who cares about Sayori?"
        y 2y7 "For all I care, she can go kill herself."
        y "All of them can."
        y 2y1 "Better yet, why don't I do it?"
        y "Ahaha, I have a knife right here."
        y "Did you know..."
        y "It's what I use to stimulate myself?"
        y 2y3 "I can make an exception and use it on someone else."
        y "Without her, we'll all be so much happier!"
        y "[player]..."
        python:
            try: os.remove(config.basedir + "/A message.txt")
            except: pass
            try: os.remove(config.basedir + "/It was easy.txt")
            except: pass
            try: renpy.file(config.basedir + "/This is hard.txt")
            except: open(config.basedir + "/This is hard.txt", "wb").write(renpy.file("This is hard.txt").read())
        y "You'll be mine and mine alone.{nw}"
        $ _history_list = []
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.5)
        stop sound
        scene black
        show monika 1e zorder 2 at i11
        hide screen tear
        play music m1
        m "Man, you really messed up."
        m "All you had to do was read the book."
        m 1f "So here we are."
        m "The game is frozen while Sayori tries to remove that whole fiasco..."
        m 1c "The events in the library are being redacted as we speak..."
        m "Which means Yuri won't remember anything that happened."
        m 1o "This is my fault too."
        m "I should have helped..."
        m 1e "Just goes to show how useless I am when I'm not the president, right?"
        m "The decision you made..."
        m 1f "It means helping Yuri just got a little harder."
        m "But..."
        m "I know you worked hard to make me happy..."
        m 1e "So I can't give up."
        m "Still, our only chance now is the play for the novel."
        m "I think I know what Sayori has planned now."
        m "It's a really good idea..."
        m 1g "I just hope it works."
        m 1d "Oh..."
        stop music fadeout 2.0
        m "It appears as if she's done."
        m 1a "See you!{nw}"
        $ config.allow_skipping = True
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        stop sound
        hide screen tear
    scene bg club_day
    with dissolve_scene_half
    play music t2
    "Another day passes, and it's time for the club meeting already."
    "The desks for the book reading are all setup already."
    "Everyone is already seated around the table."
    "Unlike yesterday, there seems to be only one spot free."
    "It's a spot next to Yuri."
    show yuri 1y5 zorder 2 at t44
    y "Hello [player]."
    mc "Hi Yuri..."
    mc "Why is the table layout different today?"
    y "Huh? What's wrong with it?"
    mc "It's just--"
    y "Is there something wrong, [player]?"
    mc "I don't mind it but it seems really..."
    mc "...specific."
    show sayori 1d zorder 3 at f43
    s "Well, Yuri got to the club early..."
    s "So I guess she took it upon herself to set the desks out this way."
    s "I wouldn't think about it too much."
    show monika 5 zorder 3 at f42
    show sayori zorder 2 at t43
    m "Ahaha, it does seem there is some...ulterior motive here, doesn't there?"
    m "Still, we should appreciate the work Yuri has done."
    m "She saved us the time doing it ourselves."
    show natsuki 3e zorder 3 at f41
    show monika 3a zorder 2 at t42
    n "Can we just get on with it?"
    n "The sooner we get this done, the better."
    show natsuki zorder 2 at t41
    show yuri 2y6 zorder 3 at f44
    y "Natsuki..."
    y 2y7 "Shut your mouth..."
    y "You beat up, malnourished, little--"
    y 3p "Um...!"
    y 3q "Please."
    show natsuki 3f zorder 3 at f41
    show yuri zorder 2 at t44
    n "Excuse me?"
    n "What is wrong with you Yuri?!"
    n "If I didn't know bette--"
    show natsuki zorder 2 at t41
    show sayori 1h zorder 3 at f43
    s "Guys!"
    s "I know everyone has been feeling a little different."
    s 1f "But let's just calm down..."
    s "Open our books..."
    s 1d "And start reading, okay~?"
    s "Why don't you start, [player]?"
    show sayori zorder 2 at t43
    mc "Um..."
    mc "Alright..."
    show natsuki 1g zorder 2 at t41
    show monika 1d zorder 2 at t42
    show yuri 1g zorder 2 at t44
    "I open up to the fifth chapter of the book."
    "It's called 'Obsession'."
    "I begin reading, keeping at a good pace."
    "I'm not enthusiastic like Monika was yesterday but it's bearable."
    "Besides, I can tell that everyone is actually reading in their heads."
    "They're just waiting for me to reach the end before they turn the page."
    "Soon enough, I finish the chapter."
    "That was definitely something."
    "We found out a little more about the wife and what she does."
    "It turns out that she's really obsessive of the lumberjack."
    "At the same time, she'd do anything for him."
    "It isn't an unhealthy relationship, it's more like a true love sort of thing."
    "But I wonder how the wanderer will play out into this..."
    show sayori 1b zorder 3 at f43
    s "Does anyone have anything to say about the chapter?"
    s "Yuri, maybe?"
    show sayori zorder 2 at t43
    show yuri 1h zorder 3 at f44
    y "No..."
    y "There's nothing to say."
    show monika 3b zorder 3 at f42
    show yuri zorder 2 at t44
    m "Well, I think the wife in this chapter reminded me a lot of Yuri."
    m "I mean she's intelligent, shy and has similar..."
    m 3e "...tendencies."
    m "I don't mean that in a bad way!"
    m 2a "I just find her to be super relatable."
    show monika zorder 2 at t42
    mc "Yeah, I agree."
    mc "I mean Yuri isn't exactly the same person."
    mc "But the wife really seems to fit the type of person Yuri is."
    mc "Plus, those tendencies are definitely something I could imagine Yuri being into."
    show yuri 1s zorder 3 at f44
    "Yuri whispers into my ear."
    y "Do you...really think so?"
    y "We can..."
    y "Be like them..."
    y "If you want...?"
    show sayori 1c zorder 3 at f43
    show yuri zorder 2 at t44
    s "Did you say something Yuri?"
    s "You should speak up, so the whole club can hear!"
    show sayori zorder 2 at t43
    show yuri 1o zorder 3 at f44
    y "U-Um..."
    y "I was just saying that if you all think I'm like the wife..."
    y "Then maybe for our play..."
    y "...I could..."
    y 1q "...take the role of the wife?"
    show natsuki 4e zorder 3 at f41
    show yuri zorder 2 at t44
    n "What?!"
    n "You can't be serious!"
    n "Just because you're similar to her doesn't mean you're the most suited."
    n "In fact, I'm pro--"
    show natsuki zorder 2 at t41
    show monika 2e zorder 3 at f42
    m "Ah, Natsuki..."
    m "I can already tell you're going to say something mean."
    show natsuki 4f zorder 3 at f41
    show monika zorder 2 at t42
    n "S-Shut up Monika!"
    n "I know for a fact..."
    n "That the only reason Yuri wants to be the wife..."
    n 4b "...is because [player] is going to be play the husband!"
    show natsuki zorder 2 at t41
    show yuri 1o zorder 3 at f44
    y "T-That's not true!"
    y "Everyone said that I'm similar to the wife..."
    y "So that's why..."
    show sayori 1k zorder 3 at f43
    show yuri zorder 2 at t44
    s "Natsuki..."
    s "I think it's better if we let Yuri have this."
    s 1d "Trust me, you'll get your chance."
    show natsuki 3n zorder 3 at f41
    show sayori zorder 2 at t43
    n "Fine!"
    n "Jeez, it's like no one cares what I have to say."
    show natsuki zorder 2 at t41
    show yuri 3y7 zorder 3 at f44
    y "{i}(That's because no one does, you little brat.){/i}"
    show yuri zorder 2 at t44
    mc "Did you say something Yuri?"
    show yuri 2p zorder 3 at f44
    y "N-No!"
    y "I didn't mean to shout..."
    y 2q "Please continue..."
    show yuri zorder 2 at t44
    show monika 2f zorder 3 at f42
    m "Natsuki, you know that's not true."
    m "We do care about you."
    m 2e "We just think that Yuri would be most suited to be a certain character."
    m "So please don't take this the wrong way..."
    show monika zorder 2 at t42
    show sayori 1q zorder 3 at f43
    s "Yeah! Let's just keep reading..."
    s "Maybe we'll find out which one of the other characters you can be."
    show natsuki 42b zorder 3 at f41
    show sayori zorder 2 at t43
    n "Hmph."
    n "Fine then."
    show natsuki zorder 2 at t41
    show sayori 1d zorder 3 at f43
    s "Great..."
    s "In that case, why don't you read for us?"
    show natsuki 42a zorder 3 at f41
    show sayori zorder 2 at t43
    n "Ugh...!"
    n "Only because I have to..."
    show natsuki zorder 2 at t41
    "Natsuki begrudgingly starts reading the next chapter."
    "She puts on a voice as if she is angry that she's reading."
    "That sour attitude disappears as she continues but she remains unenthused."
    show natsuki 1i zorder 2 at t41
    "The chapter is over shortly after."
    "That was basically just a huge dump of plot."
    "We found out more about the two daughters and a lot more about the wanderer."
    "The two daughters are pretty young, with the older one being more..."
    "...carefree, to put it nicely."
    "The other daughter seemed to have a mean attitude but was actually soft inside."
    "She used negative feelings to hide her soft interior from everyone else."
    "The wanderer decided to try manipulating the older daughter a little."
    "She did it in secret, slowly making her less and less happy."
    "The older daughter put on a facade for her family, appearing happy but desperately longing for...something."
    "The chapter ends with the older daughter missing and the lumberjack looking for her."
    show sayori 2i zorder 3 at f43
    s "So, do you still think it's boring?"
    s 2j "You have to admit, it's getting pretty tense!"
    show natsuki 4e zorder 3 at f41
    show sayori zorder 2 at t43
    n "Well..."
    n "Okay, I guess it's getting {i}slightly{/i} interesting."
    n "But only because of the weird stuff that's happening."
    n 4c "It's so unpredictable."
    show natsuki zorder 2 at t41
    show monika 3b zorder 3 at f42
    m "You have to appreciate the writing too."
    m "Without it, we probably wouldn't have bothered reading it for so long."
    m 1e "Still, I'm glad you're getting invested in it Natsuki."
    show monika zorder 2 at t42
    show sayori 4r zorder 3 at f43
    s "I think I know exactly who everyone should be!"
    s "[player] should be the lumberjack!"
    s "Monika can be the wanderer..."
    s "Natsuki, you should be the younger daughter."
    s 4l "Which...leaves me as the older daughter I guess!"
    show sayori zorder 2 at t43
    if player_gender == "girl":
        mc "Wait, why am I the lumberjack?"
        mc "Why can't I be someone else?"
        show sayori 4a zorder 3 at f43
        s "I think it fits you the most."
        s "Don't you agree?"
        show sayori zorder 2 at t43
        mc "I...suppose."
    show monika 1g zorder 3 at f42
    m "H-Hold on a second Sayori...!"
    m "I don't think putting me as the wanderer is a good idea..."
    m 1n "I mean, I have nothing in common with her!"
    show monika zorder 2 at t42
    show yuri 3r zorder 3 at f44
    y "T-That's not true!"
    y "You have a lot in common with her..."
    y "From her personality..."
    y "To the way you act."
    show monika 2f zorder 3 at f42
    show yuri zorder 2 at t44
    m "What?"
    m "I don't act like that..."
    m "Do I?"
    m "I mean..."
    m "...there's no way I would hurt someone like that..."
    show monika zorder 2 at t42
    show sayori 1d zorder 3 at f43
    s "Aw, I'm sure she didn't mean it like that Monika."
    s "She probably means the better part of your personality..."
    s 1a "You know..."
    s "Fun, smart, popular and beautiful."
    s 1d "The other parts are just the character in the book and nothing like you."
    show yuri zorder 3 at f44
    show sayori zorder 2 at t43
    y "You can take what I said however you want..."
    y "But I meant it..."
    show natsuki 4e zorder 3 at f41
    show yuri zorder 2 at t44
    n "What's gotten into you Yuri?"
    n "You've really changed, almost like--"
    show natsuki zorder 2 at t41
    show sayori 4l zorder 3 at f43
    s "Well...!"
    s "Would you look at the time?!"
    s "It's time to share our poems!"
    if not read_book and not did_all_tasks:
        show sayori zorder 2 at t43
        show yuri 1q zorder 3 at f44
        y "I-If you don't mind..."
        y "I need to be excused briefly."
        y "I have something I need to do..."
        show sayori 1b zorder 3 at f43
        show yuri zorder 2 at t44
        s "Oh..."
        s "Alright."
        s 1a "Just don't take too long!"
        show sayori zorder 2 at t43
        show sayori at thide
        show monika at thide
        show natsuki at thide
        hide sayori
        hide monika
        hide natsuki
        show yuri zorder 2 at t11
        "Yuri nods before getting up."
        "She pushes her chair in and puts the novel into her bag."
        "As she walks over to the door, she trips on my bag."
        show yuri 3n zorder 2 at t11
        play sound "sfx/smack.ogg"
        $ pause(0.25)
        play sound fall
        $ pause(0.25)
        mc "Sorry!"
        mc "I didn't mean for that to happen."
        mc "Here let me help you up."
        "I offer her my hand."
        y 1o "A-Ah..."
        y "T-That's okay..."
        y 1s "I can get up myself..."
        "Yuri holds on to my bag to support herself."
        "She gets up slowly, as if she's trying to hide something."
        mc "Take care Yuri."
        y 1u "Y-You too..."
        $ y_ranaway = True
    return

label ch7_end:
    stop music fadeout 1.0
    scene bg club_day
    show sayori 4a zorder 2 at t11
    with wipeleft_scene
    play music t3
    s "Okay--"
    s "Alright, everybody!"
    s 4d "I want to end the meeting quickly because we don't have much time..."
    s 1c "I'm just gonna say that we should all finish the novel tonight."
    s 1a "Then tomorrow we're gonna vote on which chapter we liked and reenact it real quick."
    s 3q "After that we'll start the next book!"
    s "If everything goes to plan, then I'm sure we'll have a great time!"
    show natsuki 1g zorder 3 at f21
    show sayori zorder 2 at t22
    n "Finally."
    n "I can't wait for this to be over with."
    n 1h "We're doing manga next, right?"
    show natsuki zorder 2 at t21
    show sayori 2d zorder 3 at f22
    s "Yep!"
    s "It's only fair since we made you read a novel."
    show monika 1a zorder 3 at f31
    show natsuki zorder 2 at t32
    show sayori zorder 2 at t33
    m "Have you already got a manga in mind?"
    m "It's better if we organize it now."
    show yuri 2k zorder 3 at f41
    show monika zorder 2 at t42
    show natsuki zorder 2 at t43
    show sayori zorder 2 at t44
    y "It better not be that joke you call a series in the cupboard."
    y "Besides, who even wants to read manga?"
    y 2y6 "We'd rather be dead."
    show yuri zorder 2 at t41
    show monika 3e zorder 3 at f42
    m "Um..."
    m "That's a bit harsh, don't you think?"
    show yuri 3r zorder 3 at f41
    show monika zorder 2 at t42
    y "I know you agree with me Monika."
    y "Manga is pitiful."
    show yuri zorder 2 at t41
    show natsuki 4e zorder 3 at f43
    n "Seriously?!"
    n "What is going on with Yuri?"
    n "And why is nobody doing anything about it?!"
    n 4f "You're all just standing there, pretending nothing is happening!"
    show natsuki zorder 2 at t43
    show sayori 1f zorder 3 at f44
    $ config.skipping = False
    $ config.allow_skipping = False
    s "Natsuki..."
    s "You're wrong."
    s "We're doing a lot to fix this..."
    s 1k "I'm sorry you have to put up with a lot before it's done."
    s "Watch out Monika..."
    s 1h "This may hurt a little."
    $ style.say_dialogue = style.edited
    $ currentpos = 50.309 - (get_pos() / 2.0)
    $ audio.t3r = "<from " + str(currentpos) + " to 48.0 loop 0>mod_assets/bgm/3r.ogg"
    play music t3r
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    s 1k "{cps=*5}Watch out Monika...{/cps}{nw}"
    s "{cps=*5}I'm sorry you have to put up with a lot before it's done.{/cps}{nw}"
    s 1f "{cps=*5}We're doing a lot to fix this...{/cps}{nw}"
    s "{cps=*5}You're wrong.{/cps}{nw}"
    s "{cps=*5}Natsuki...{/cps}{nw}"
    show sayori 2d zorder 2 at t44
    show natsuki 4f zorder 3 at f43
    n "{cps=*5}You're all just standing there, pretending nothing is happening!{/cps}{nw}"
    n 4e "{cps=*5}And why is nobody doing anything about it?!{/cps}{nw}"
    n "{cps=*5}What is going on with Yuri?{/cps}{nw}"
    n "{cps=*5}Seriously?!{/cps}{nw}"
    show natsuki 1h zorder 2 at t43
    show yuri 3r zorder 3 at f41
    y "{cps=*5}Manga is pitiful.{/cps}{nw}"
    y "{cps=*5}I know you agree with me Monika.{/cps}{nw}"
    show monika 3e zorder 3 at f42
    show yuri 2y6 zorder 2 at t41
    m "{cps=*5}That's a bit harsh, don't you think?{/cps}{nw}"
    m "{cps=*5}Um...{/cps}{nw}"
    show monika 1a zorder 2 at t42
    show yuri 2k zorder 3 at f41
    y "{cps=*5}We'd rather be dead.{/cps}{nw}"
    y "{cps=*5}It better not be that joke you call a series in the cupboard.{/cps}{nw}"
    show yuri at thide
    hide yuri
    show sayori zorder 2 at t33
    show natsuki zorder 3 at f32
    show monika zorder 2 at t31
    m "{cps=*5}It's better if we organize it now.{/cps}{nw}"
    m "{cps=*5}Have you already got a manga in mind?{/cps}{nw}"
    show monika at thide
    hide monika
    show sayori zorder 2 at f22
    show natsuki zorder 3 at t21
    s "{cps=*5}It's only fair since we made you read a novel.{/cps}{nw}"
    s "{cps=*5}Yep!{/cps}{nw}"
    show sayori zorder 2 at t22
    show natsuki zorder 3 at f21
    n "{cps=*5}We're doing manga next, right?{/cps}{nw}"
    n "{cps=*5}I can't wait for this to be over with.{/cps}{nw}"
    n "{cps=*5}Finally.{/cps}{nw}"
    show natsuki at thide
    hide natsuki
    show sayori 3q zorder 2 at t11
    s "{cps=*5}If everything goes to plan, then I'm sure we'll have a great time!{/cps}{nw}"
    s "{cps=*5}After that we'll start the next book!{/cps}{nw}"
    s 1a "{cps=*5}Then tomorrow we're gonna vote on which chapter we liked and reenact it real quick.{/cps}{nw}"
    s 1c "{cps=*5}So I'm just going to say that we should all finish the novel tonight.{/cps}{nw}"
    s 4d "{cps=*5}I want to end this quickly because we don't have much time...{/cps}{nw}"
    $ _history_list = []
    $ style.say_dialogue = style.normal
    $ currentpos = 100.618 - (get_pos() * 2.0)
    $ audio.t3r = "<from " + str(currentpos) + " loop 4.618>bgm/3.ogg"
    play music t3r
    hide noise
    hide vignette
    show layer master
    $ config.allow_skipping = True
    show sayori 4d zorder 3 at t11
    s "Alright, everybody!"
    s "I want everyone to read the last chapters with someone else."
    s 1a "It can be anybody you want..."
    s "A family member or a friend."
    s "I just want you to be with someone when you read it."
    show natsuki 1b zorder 3 at f21
    show sayori zorder 2 at t22
    n "Do we need to?"
    n "I don't really feel comfortable doing that..."
    n 2g "And I don't see the point either..."
    show natsuki zorder 2 at t21
    show sayori zorder 3 at f22
    s 3c "Well, I guess you don't have to do it."
    s 3q "But if you do, you'll spread the joy of literature to those you share it with."
    s "Unless, of course they're from the club."
    s 3r "Then I guess you'll share the joy of literature with each other!"
    "Is Sayori suggesting I spend the afternoon with one of my club members?"
    "How on Earth are they going to respond to a suggestion like that...?"
    show yuri 2b zorder 3 at f31
    show natsuki zorder 2 at t32
    show sayori zorder 2 at t33
    y "I-In that case, I'm going with [player]!"
    show yuri zorder 2 at t31
    show sayori 1b zorder 3 at f33
    s "Um...Yuri..."
    s 2l "I think [player] has to agree to it too."
    s "You can't just force [player_reflexive] to go with you."
    show yuri 2n zorder 3 at f31
    show sayori zorder 2 at t33
    y "But..."
    show monika 3e zorder 3 at f41
    show yuri zorder 2 at t42
    show natsuki zorder 2 at t43
    show sayori zorder 2 at t44
    m "Yuri, I'm sure if [player_personal] feels the same way about you..."
    m "[cPlayer_personal]'ll end up choosing you, right?"
    if sayori_confess:
        m 3l "Besides, [player] and Sayori are kinda a couple."
        m "So--"
    else:
        m 3l "Besides, [player] and Sayori are neighbors and best friends."
        m "So--"
    show monika zorder 2 at t41
    show natsuki 2h zorder 3 at f43
    n "[player], I know you're fed up with everybody here."
    n "You're probably the only person who's realized what's going on, right?"
    n "We can just--"
    show yuri 2r zorder 3 at f42
    show natsuki zorder 2 at t43
    y "Natsuki..."
    y 2y4 "Why don't you just shut your fucking mouth and let [player_reflexive] decide for [player_reflexive]self?"
    show monika 3i
    show natsuki 2q
    stop music fadeout 1.5
    $ pause(1.5)
    y 2y1 "Good."
    y "[player], I know you want to be with me."
    y "We can go to my house."
    y 2y3 "The whole afternoon, with just the two of us."
    y "Doesn't that sound wonderful?"
    y "We can just sit there and stare into each other's eyes."
    show yuri zorder 2 at t42
    show sayori 2l zorder 3 at f44
    s "Don't forget to read the book."
    s 2d "After all, that's the whole reason we're doing this!"
    s "Also, we shouldn't be putting pressure on [player]..."
    label ch7_redo:
    # Here in case they need to be
    $ persistent.autoload = ""
    $ renpy.save_persistent()
    $ quick_menu = True

    s "Because in the end, it's up to [player_reflexive] to decide who [player_personal] reads with."
    show sayori zorder 2 at t44
    menu:
        s "So, do you have a preference?"
        "Natsuki.":
            call ch7_end_natsuki
        "Yuri.":
            call ch7_end_yuri
        "Monika.":
            call ch7_end_monika
        "Sayori.":
            call ch7_end_sayori
    if ch7_scene == "yuri":
        scene bg y_house_day
    else:
        scene bg house
    #with wipeleft_scene
    play music t2g
    queue music t2g2
    hide screen tear
    window show(None)
    window auto
    $ _history_list = []
    $ ch7_name = ch7_scene.capitalize()
    if ch7_name == "Sayori":
        "So I guess Sayori is coming over to read with me tonight."
        "Sayori said she needed to do something before she came over."
        "So I'm just waiting until she arrives."
    elif ch7_name == "Yuri":
        $ persistent.sayori_reload_yuri = False
        $ persistent.sayori_reload_yuri_message = True
        $ renpy.save_persistent()
        "So I guess I'm finishing off the book with [ch7_name] tonight."
        "She sent me her address on my phone."
        "It took me a while to get to her house, seeing as she misspelled the street."
        "I think that's because she's a little excited."
    else:
        "So I guess I'm reading the last couple of chapters with [ch7_name] tonight."
        "I gave her my address, so I'm just waiting until she arrives."
    "I'm a little curious as to why Sayori wants us to read with someone."
    "I'm not really buying her whole \"sharing the joy of literature\" idea."
    "But I shouldn't be doubting her, she's my best friend."
    "She has no reason to lie to me."

    if ch7_name != "Yuri":
        "Soon enough, I hear the doorbell and [ch7_name] arrives at my house."
    else:
        "I finally decide to ring the doorbell to Yuri's home."


    $ nextscene = ch7_scene + "_exclusive_4"
    call expression nextscene

    if persistent.sayori_yuri_bad_ending:
        jump ch8_redirect
    else:
        return

label ch7_end_natsuki:
    $ ch7_scene = "natsuki"
    mc "I'll probably feel most comfortable reading with Natsuki."
    mc "So that's who I'll go with."
    show natsuki 3c zorder 3 at f43
    n "Thank you, [player]."
    n 3e "I was starting to think everyone here had gone insane."
    n 3g "I'm glad at least someone still has a brain."
    n "I-Is your house okay?"
    show natsuki zorder 2 at t43
    mc "Sure, I don't mind."
    if ch4_name == "Natsuki":
        mc "You have my number already, right?"
    else:
        mc "I'll tell you my number after the meeting."
    show yuri 2y3 zorder 3 at f42
    y "You have got to be {i}fucking{/i} kidding me."
    y "Why would you choose her?"
    y "You don't need her."
    y 2y1 "You need me."
    show yuri zorder 2 at t42
    show natsuki 3o zorder 3 at f43
    n "Yuri, what the hell?!"
    n "You need to see a therapist or something."
    n 3p "Because I'm seriously concerned for you!"
    show yuri 3y4 zorder 3 at f42
    show natsuki zorder 2 at t43
    y "Natsuki."
    y "You need to learn when to shut the fuck up."
    y 3y3 "Okay?"
    y "Now just leave [player] to me and we can all live a happy life.{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    return

label ch7_end_yuri:
    $ ch7_scene = "yuri"
    mc "Well...Yuri already chose me."
    mc "So I guess that's who I'll go with tonight."
    show yuri 2y3 zorder 3 at f42
    y "Y-Yes!"
    y "This is all I really wanted."
    if ch4_name == "Yuri":
        y 2b "You have my number still, right?!"
    else:
        y 2y5 "H-Here!"
        "Yuri hands me a piece of paper with crudely drawn numbers on it."
        y 2b "You can call me on that!"
    show yuri zorder 2 at t42
    show natsuki 3e zorder 3 at f43
    n "[player], what the hell is wrong with you?"
    n "Do you know what you've just done?"
    n 3f "I really ho--"
    show yuri 2y4 zorder 3 at f42
    show natsuki zorder 2 at t43
    y "That little brat is upset that you chose me."
    y "Don't mind her, she's not important."
    y 2y1 "All that matters is me!"
    y "I've been waiting for this moment for so long."
    y "You know..."
    y 2y4 "I just want to rip open your skin and crawl inside you."
    y 2y1 "Wouldn't that be just perfect?{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    return

label ch7_end_monika:
    $ ch7_scene = "monika"
    mc "Well...I would like to spend some time with Monika..."
    mc "If she doesn't mind..."
    show monika 2m zorder 3 at f41
    m "Um..."
    m 5 "Of course not!"
    m "We'll meet at your house, alright?"
    m "I'll be sure to br--"
    show monika zorder 2 at t41
    show yuri 2y3 zorder 3 at f42
    y "You have got to be {i}fucking{/i} kidding me."
    y "Why would you choose her?"
    show monika 1g zorder 3 at f41
    show yuri zorder 2 at t42
    m "Yuri, I'm sorry."
    m "But that's just the way it is."
    m 1f "Man..."
    m "I sure hope you feel better soon..."
    show monika zorder 2 at t41
    show yuri 2y4 zorder 3 at f42
    y "[player]."
    y 2y1 "Just come with me."
    y "You don't need her and her {i}Third Eye{/i}."
    y 2y3 "All we need is each other."
    show monika 3i zorder 3 at f41
    show yuri zorder 2 at t42
    m "Did you just say Third Eye?"
    m "Yuri, do you know what that is?"
    show monika zorder 2 at t41
    show yuri 2y4 zorder 3 at f42
    y "Ahaha, you have no idea and it's killing you isn't it?"
    show monika 1f zorder 3 at f41
    show yuri zorder 2 at t42
    m "Yuri, come on, I'm trying to help."
    m "So please stop being unreasonable."
    show monika zorder 2 at t41
    show yuri zorder 3 at f42
    y 2y4 "I'm being unreasonable?"
    y 2y3 "Ahahaha!"
    y "Monika, I can't believe how delusional and self-important you are!"
    y "Pulling [player] away from me every single time you're not included in something."
    y 1y1 "Are you jealous?"
    y "Crazy?"
    y 1y3 "Or maybe you just hate yourself so much that you take it out on others?"
    y 1y4 "Here's a suggestion. Have you considered killing yourself?{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    return

label ch7_end_sayori:
    $ ch7_scene = "sayori"
    if sayori_confess:
        mc "Well, Sayori and I are already a couple."
    else:
        mc "Well, Sayori and I are already neighbors."
    mc "So it would probably be best if I read with her."
    show sayori 4d zorder 3 at f44
    s "Aw, really?"
    s 4a "That's so nice of you [player]."
    s 1c "I might be a little late to get to your house."
    s "I have to take care of something but after that we--"
    show yuri 2y3 zorder 3 at f42
    show sayori zorder 2 at t44
    y "You have got to be {i}fucking{/i} kidding me."
    y "Why would you choose her?"
    y "You don't need her."
    y 2y1 "You need me."
    show yuri zorder 2 at t42
    show sayori 1h zorder 3 at f44
    s "Um...Yuri."
    s "I think you need to calm down a little."
    s 1g "You're being a little scary..."
    s "And I know you're not yourself..."
    s 1k "Trust me, I know all too well..."
    show yuri 2y6 zorder 3 at f42
    y "Sayori..."
    y 2y7 "You don't know anything."
    y "You are the most useless, stupid person I know."
    y 2y3 "The world would not care if you just killed yourself.{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    return
