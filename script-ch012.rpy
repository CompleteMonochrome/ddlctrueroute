init python:
    if not persistent.n_playday[4]:
        def yuu_placecheck(event, interact=True, **kwargs):
            try:
                renpy.file("../characters/yasuhiro.chr")
            except:
                renpy.jump("ch10_delete")

label ch12_main:
    # Setup Call for currentuser
    python:
        process_list = []

        currentuser = ""
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
            except:
                pass

    # Choose Start of Meeting - Normal Monika, Converted Monika, Markovika
    # Set Variables and Reset Persistent for New Playthrough
    $ monika_type = 2
    $ ch12_natsuki_help = True
    $ ch12_natsuki_reluctance = 0
    $ persistent.ch11_task = [False,False,False]
    $ persistent.n_playday = [False,False,False,False,False,False]

    scene bg club_day with dissolve_scene_half
    play music t2
    "Sayori told me on the phone this morning that she would meet me in the club."
    "I haven't seen her since yesterday, but it's not like I'm worried for her or anything."
    "She's more than capable of handling herself."
    "Somehow I'm the first one in the clubroom."
    "It's a little strange being here alone."
    "It feels almost unnatural."
    "But it isn't long as Monika arrives."
    if m_appeal >= 4 and ch11_monika_talked and ch11_monika_dinner and ch11_did_all_tasks:
        $ monika_type = 0
        show monika 1e zorder 2 at t11
        m "Hi [player]..."
        m "Slept well?"
        mc "I suppose."
        m "That's good."
        m 2e "I hope you aren't too worn out from everything."
        mc "What would I be worn out by?"
        m "You read the manga and wrote a poem, didn't you?"
        mc "I did...?"
        "The events of last night do seem a little confusing."
        if ch11_read_manga or ch11_did_all_tasks:
            "I remember choosing to read the manga..."
            "But when did I write a poem?"
            "I have memories of doing both but I can't piece out what goes when."
        else:
            "I remember choosing to write a poem and skimming over the book this morning..."
            "But I have memories of doing both last night..."
            "My head must be all over the place if I can't even piece out what goes when."
        mc "I guess I did..."
        mc "Though it's all a little confusing as to how I did it."
        m 4a "Ahaha, with things like that, it's best not to think about it."
        m "Maybe it's just another one of your blessings that clerk was talking about."
        mc "It seems kinda supernatural to me..."
        m 2c "How so?"
        mc "I don't know."
        mc "I just thought it would be impossible to do both things."
        m "Hmm..."
        m "You've done something similar before..."
        m 1m "But I suppose you wouldn't have known that."
        mc "Are you trying to tell me something?"
        m "Ah..."
        "Monika looks away, deep in thought."
        "She looks like she is about to say something but stops herself."
        m 1e "Forget it..."
        m "That's not the most important thing right now."
        mc "The play is, right?"
        m 1b "Exactly!"
        m "Are you ready for today?"
        mc "As ready as I can be, I guess."
        m 1a "It's going to be quite the day."
        m "I think Sayori prepared another one of those scripts like she did last time."
        mc "You think so?"
        m 1b "I'm almost certain..."
        "Monika's mood suddenly shifts."
        m 1o "Sigh..."
        mc "Something wrong?"
        m "N-Nothing..."
        m "It's just..."
        m 1m "She's just such a hardworking person..."
        m "And well..."
        m 1e "She deserves the best."
        mc "You're right about that."
    elif ch11_monika_talked:
        $ monika_type = 1
        show monika 1a zorder 2 at t11
        m "Hi [player]~"
        m 2b "Thanks for yesterday~"
        mc "Ah..."
        mc "It's not a problem."
        m "I just really appreciate you taking the time for me..."
        show monika g7
        $ currentpos = get_pos()
        play music mkov fadeout 2.0
        m "But in the end, it all ended up being meaningless."
        mc "Meaningless?"
        mc "What do you mean?"
        m "Ahaha, you've helped me so much more than you've realized."
        m 3b "I never would have known about certain things if I took her over earlier..."
        m "But thanks to your efforts..."
        m "Well, let's just say things have become a lot easier for me."
        mc "Eh?"
        mc "This is a really big shift on what you were feeling last night."
        mc "Aren't you worried about that danger you talked about?"
        m 3c "Not at all."
        m 3b "In fact, it's best if you just forget about everything."
        mc "..."
        mc "Are you okay, Monika?"
        m 1a "I've never been better."
        show monika g9
        m "And it's all thanks to you."
        m "Ahaha..."
        "Something about the way Monika laughed just then gives me an uneasy feeling."
        "It doesn't help that what she's saying sounds a little cryptic."
        "But I have no reason not to trust her."
        mc "Why aren't you concerned about the danger anymore?"
        m 5b "Eh?"
        m "Why would I be?"
        m 1a "It's not like we can do anything to stop it anyway."
        m "So we should just forget about it, okay?"
        mc "I don't think I can..."
        mc "It seemed like a pretty serious issue to you."
        mc "Did something happen to you last night, Monika?"
        m 1c "Nothing happened..."
        m 1d "Except..."
        m 1e "Well, we can talk more about that later."
        $ audio.t2c = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
        play music t2c fadeout 0.5
    else:
        $ monika_type = 2
        show monika 1c zorder 2 at t11
        m "[player]."
        m "I see you're here early."
        mc "I guess so."
        mc "Though I would have thought Sayori would have been here by now."
        show monika g8
        $ currentpos = get_pos()
        play music mkov fadeout 2.0
        m "As did I."
        m "It's a little irresponsible of her, don't you think?"
        mc "Um..."
        "Something about Monika seems kinda off."
        "I can't quite figure it out, but it's almost like she's got a completely different personality."
        "Or has she always been like this?"
        "I haven't really noticed it until now..."
        mc "Not really?"
        mc "She's probably doing something important for today."
        mc "I don't really blame her for being late."
        m 1c "I see."
        m "Well, I suppose you're right."
        m 1a "Still, I'd like to get today done as soon as possible."
        mc "Not excited for the play I guess?"
        m "You could say that."
        m 1e "I'm just looking forward to what happens {i}after{/i} the play."
        mc "And what's that?"
        m "Ahaha, you'll see."
        mc "That's kinda..."
        mc "...unsettling?"
        mc "I don't know, just the way you said it."
        m 2l "Oh, sorry!"
        m "I didn't mean to sound like that."
        "Monika shows me a smile."
        "For some reason, I get a pit in my stomach."
        "Her smiles don't usually have that effect on me..."
        m 2a "But it's definitely going to be..."
        m "...interesting."
        m 2b "At least, I hope so."
        mc "Right..."
        m "Ahaha."
        $ audio.t2c = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
        play music t2c fadeout 0.5
    show yuri 1a zorder 2 at t31
    show natsuki 1c zorder 3 at f32
    show monika zorder 2 at t33
    n "I hope we're not late."
    n "We got here as fast as we could."
    show natsuki zorder 2 at t32
    show monika 3a zorder 3 at f33
    m "Not at all!"
    m "We're still waiting for Sayori to get here."
    if monika_type == 0:
        m 5 "You two arriving at the same time is a little strange though."
    else:
        m 3e "Though I'm curious..."
        m "Why did you two arrive at the same time?"
    show natsuki 2b zorder 3 at f32
    show monika zorder 2 at t33
    n "W-Well, we..."
    n 2q "Um..."
    show yuri 1b zorder 3 at f31
    show natsuki zorder 2 at t32
    y "Natsuki wanted to speak with me about the manga on the way here."
    y "I happily accepted."
    y 2pb "It was an interesting read, so I didn't really mind talking about it."
    show yuri zorder 2 at t31
    show monika 2d zorder 3 at f33
    m "Oh?"
    m "I didn't think you'd be the type of person she'd talk about that with."
    m "Manga isn't really--"
    show natsuki 4w zorder 3 at f32
    show monika zorder 2 at t33
    n "Y-Yeah, well...!"
    n "Yuri is a great friend, so that's why..."
    if n_appeal == 4 and check_whole_house:
        n "And I couldn't find [player], so..."
    n 4o "W-What's it to you, anyway?!"
    show natsuki zorder 2 at t32
    show monika zorder 3 at f33
    if monika_type == 0:
        m 1l "It's nothing to me!"
        m "I-I was just asking, really!"
        m "There's no need to get so worked up about it, Natsuki..."
    else:
        m 1a "I'm just curious."
        m "I didn't think it'd be such a big deal."
    show natsuki 4s zorder 3 at f32
    show monika zorder 2 at t33
    n "..."
    n "Sorry, I didn't mean to..."
    n "I guess I'm just feeling a little on edge..."
    show natsuki zorder 2 at t32
    show monika zorder 3 at f33
    if monika_type == 0:
        m 2e "That's okay~"
        m "I can understand how you're feeling."
    else:
        m 2b "It's understandable."
        m "I'm feeling the same as you are."
    show yuri 3pg zorder 3 at f31
    show monika zorder 2 at t33
    y "Hmm..."
    y "So it isn't just me?"
    show yuri zorder 2 at t31
    mc "What do you mean?"
    show yuri 3pf zorder 2 at f31
    y "Well, Natsuki said she's on edge and Monika said she knows the feeling..."
    y "I'm sort of feeling the same."
    y 3po "It's like something terrible is going to happen..."
    show yuri zorder 2 at t31
    show monika zorder 3 at f33
    if monika_type == 0:
        m 4n "Something terrible, eh?"
        m "W-What gives you that idea...?"
        show monika zorder 3 at t33
        "Could this be the danger Monika is talking about?"
        "She didn't want to tell them but..."
        "No, I promised not to tell anyone."
        mc "I think you and Natsuki are just nervous for the play or something..."
        mc "It's not like we're in any danger or anything."
        show monika 1j zorder 3 at f33
        m "Y-Yeah, [player] is right!"
        m "You should ignore that feeling."
        m "It really isn't good to think about that sort of thing."
    else:
        m 1j "Oh, it's nothing like that!"
        m "Then again, I guess it's a matter of perspective~"
        show monika zorder 3 at t33
        mc "What do you mean?"
        show monika zorder 3 at f33
        m 1a "Well, it might be a bad thing to one person..."
        m "But to another, it could be really good."
        m "It's like that saying 'one man's trash, is another man's treasure', you know?"
    show natsuki 3e zorder 3 at f32
    show monika zorder 2 at t33
    n "Whatever..."
    n "This day can't be over sooner."
    show natsuki zorder 2 at t32
    mc "Why is that?"
    show natsuki 3g zorder 3 at f32
    n "I just think..."
    n "That after today, I--"
    n 3q "We..."
    n "...won't have to keep doing stuff like this."
    show natsuki zorder 2 at t32
    show monika 1d zorder 3 at f33
    m "Do you mean reading a book then performing it?"
    m "Or writing a poem?"
    show natsuki 3c zorder 3 at f32
    show monika zorder 2 at t33
    n "Both, I guess."
    show yuri 2pf zorder 3 at f31
    show natsuki zorder 2 at t32
    y "Um, Natsuki..."
    y "What makes you think that Sayori is going to make us stop doing things like this?"
    y 2pe "Monika, [player] and even Sayori herself haven't gotten a book that relates to them particularly yet..."
    y "So why would Sayori stop now?"
    show yuri zorder 2 at t31
    show natsuki 1c zorder 3 at f32
    n "I don't know..."
    n "I guess it's just a feeling..."
    show natsuki zorder 2 at t32
    mc "Don't you like doing this sort of stuff?"
    mc "I don't mind it myself..."
    "It's not like it affects me one way or another."
    show natsuki 2g zorder 3 at f32
    n "I thought I would like doing this one but..."
    n "Something feels wrong about today."
    n 2m "Like something bad is going to happen?"
    n "That's why I can't wait for it to be over."
    n 2c "But I suppose I'll try and enjoy it..."
    show natsuki zorder 2 at t32
    show monika zorder 3 at f33
    if monika_type == 0:
        m 1e "Don't worry too much about it."
        m "I don't know Sayori's plans for and after today either."
        m 1a "But whatever it is..."
        m "Well, I'm sure it's in the best interest of the Literature Club."
    else:
        m 1a "You shouldn't worry too much."
        m "Sayori probably has something up her sleeve."
        m 1b "Whatever it is, I'm sure it's for the good of the Literature Club."
    show monika zorder 2 at t33
    mc "I think so too."
    mc "Sayori has been doing a great job in my time here."
    mc "I can only imagine what it was like without someone like me dragging everything down."
    s "Aw, that's not true."
    show sayori 2d zorder 3 at f41
    show yuri zorder 2 at t42
    show natsuki zorder 2 at t43
    show monika zorder 2 at t44
    "Suddenly, Sayori opens the door to the clubroom."
    s "You don't drag anything down, [player]."
    s "In fact, things have gotten a lot more interesting ever since you came along."
    s 2a "Everyone's gotten along better and we've all become closer friends..."
    s 4q "Ehehe, at least I hope so~"
    show sayori zorder 2 at t41
    "Everyone looks at each other."
    "No one says anything to confirm or deny what she just said..."
    "I guess it's up to me."
    mc "You're right, Sayori."
    mc "I think what you've done has made everyone a little closer."
    mc "Closer than we were when I first joined anyway..."
    show sayori 2l zorder 3 at f41
    s "R-Right, see!"
    s "[player] agrees with me!"
    s "Um..."
    s 4l "Ehehe, how exactly...?"
    show sayori zorder 2 at t41
    mc "Well..."
    mc "Natsuki and Yuri are hanging out together."
    mc "They even talked about the manga on the way here."
    if monika_type == 0:
        mc "And Monika and I have been getting closer too..."
    elif visited_yuri_hospital:
        mc "And Yuri and I have been getting closer too..."
    elif n_appeal >= 3 and check_whole_house:
        mc "And Natsuki and I, even if it was for only a little bit..."
        mc "We've been getting closer too."
    else:
        mc "And Sayori and I have been getting closer too."
    mc "So, I think Sayori is right."
    show yuri 1a zorder 3 at f42
    y "I suppose you have a point there, [player]."
    y 1f "I wouldn't have spoken with Natsuki outside of the club under normal circumstances..."
    y 1b "So I guess Sayori is right."
    show sayori 4a zorder 3 at f41
    show yuri zorder 2 at t42
    s "Yeah!"
    s "That was my plan all along!"
    s "To get you all to be happy and to have fun while doing it!"
    s "Anyway..."
    s 4d "We shouldn't spend much time in here."
    show sayori zorder 2 at t41
    show yuri 2pe zorder 3 at f42
    y "Um..."
    y "Does that mean we're doing the play elsewhere...?"
    y "I'm not really sure I'm comfortable doing this outside of the clubroom..."
    show sayori 1a zorder 3 at f41
    show yuri zorder 2 at t42
    s "Yeah!"
    s "I forgot to tell you all but..."
    s "We're doing it in the gym!"
    show sayori zorder 2 at t41
    show yuri 3pq zorder 3 at f42
    y "T-The gym?"
    y "Now, I'm really not sure about this..."
    show sayori 2q zorder 3 at f41
    show yuri zorder 2 at t42
    s "Don't worry about it, Yuri!"
    s "It's just so we have a bigger space to do this play!"
    s 2r "Plus, I already convinced the sports club president to let us use the space."
    s "So it would make us look bad if we took the space and did nothing with it."
    show sayori zorder 2 at t41
    show monika zorder 3 at f44
    if monika_type == 0:
        m 1e "Sayori, it would have been good if we had known about this before today."
        m "But I guess it's not really a big deal."
        m 2e "It just makes everything a little more complicated for everyone else."
    else:
        m 1c "You should have told us about this before today, Sayori."
        m "It's irresponsible for you to make decisions that could affect the club like this."
    show sayori 2d zorder 3 at f41
    show monika zorder 2 at t44
    s "You're right..."
    s "Sorry, everybody!"
    s "I really should have told you guys..."
    s 2c "But to be honest, it was kind of a last minute thing..."
    s "I wasn't even sure if I could convince the president if I could use the space."
    s "It's a miracle he agreed."
    show sayori zorder 2 at t41
    "Sayori looks around the room."
    "I think she's looking for approval but can't find any."
    show natsuki 1e zorder 3 at f43
    n "I'm a little annoyed about this..."
    n "But..."
    n 1c "To be honest, I do like the bigger space."
    n "And it's not like other students are gonna be watching us..."
    n 1g "Right, Sayori?"
    show sayori 2q zorder 3 at f41
    show natsuki zorder 2 at t43
    s "Nope!"
    s "The only students that are gonna be there are us!"
    show sayori zorder 2 at t41
    show natsuki 2q zorder 3 at f43
    n "Well, then I guess there isn't really a problem."
    n "I don't mind performing in front of people..."
    n "But something about this--"
    "Natsuki suddenly stops herself from finishing that sentence."
    "Was she going to say something about her feeling on edge from before?"
    n 2r "Ugh, never mind..."
    show sayori 2d zorder 3 at f41
    show natsuki zorder 2 at t43
    s "Natsuki, there's nothing to worry about."
    s "I can promise you that."
    s "After all, we've gotten this far."
    show sayori zorder 2 at t41
    show natsuki 2k zorder 3 at f43
    n "Sayori..."
    n "What are you even talking about?"
    show sayori 2q zorder 3 at f41
    show natsuki zorder 2 at t43
    s "Ehehe..."
    show sayori zorder 2 at t41
    show monika zorder 3 at f44
    if monika_type == 0:
        m 3l "I think we should hurry it up a little..."
        m "We don't want to keep everyone here for too long."
    else:
        m 1h "I suggest we speed it up a little."
        m "We have a long day ahead of us."
    show sayori 1d zorder 3 at f41
    show monika zorder 2 at t44
    s "That's true..."
    s "We shouldn't keep our guest waiting, after all."
    show sayori zorder 2 at t41
    show natsuki 2o zorder 3 at f43
    n "H-Hold on a second!"
    n "Did you say guest?!"
    show sayori 1c zorder 3 at f41
    show natsuki zorder 2 at t43
    s "Umm...yeah, I did!"
    show sayori zorder 2 at t41
    show yuri 2pn zorder 3 at f42
    y "I-I thought you said no one was going to watch us perform."
    y "T-That is what you said, isn't it?"
    show sayori 1a zorder 3 at f41
    show yuri zorder 2 at t42
    s "We'll talk about that more when we get there."
    s "But I did mean what I said about no {i}students{/i} coming to watch us."
    show sayori zorder 2 at t41
    show natsuki 2r zorder 3 at f43
    n "Is this why I'm feeling so worried?"
    n "Because I knew something like this was going to happen?"
    n 2f "Who's coming to watch us, Sayori?"
    n "You have to tell us!"
    show sayori 1h zorder 3 at f41
    show natsuki zorder 2 at t43
    s "You'll find out later..."
    s 1j "And didn't you just say you don't mind performing in front of people?"
    s "What's the big deal, Natsuki?"
    show sayori zorder 2 at t41
    show natsuki 4o zorder 3 at f43
    n "Ah..."
    n 4q "I..."
    n "N-Never mind..."
    n 4s "I guess it isn't a big deal."
    n "Sorry..."
    show sayori 1d zorder 3 at f41
    show natsuki zorder 2 at t43
    s "Whatever you're feeling..."
    s "I'll help you get through it..."
    s "We all will, right guys?"
    show sayori zorder 2 at t41
    show yuri 1a zorder 3 at f42
    y "I'll certainly try my best."
    y "After all, Natsuki is my friend..."
    show yuri zorder 2 at t42
    show monika zorder 3 at f44
    if monika_type == 0:
        m 3a "Of course I'll help you!"
        m 3e "It's the very least I can do."
    else:
        m 1n "Ah...yes."
        m "I'll do what I have to for Natsuki as well."
    show sayori 1a zorder 3 at f41
    show monika zorder 2 at t44
    s "What about you, [player]?"
    s "You'll do everything you can too, right?"
    label ch12_strawberry1:
    show sayori zorder 2 at t41
    mc "Ah..."
    if monika_type == 0:
        mc "I don't really get what she's feeling right now."
        mc "But I'll try my best to help her."
        mc "She's my friend after all..."
        mc "And I know things you guys might not and..."
        "Natsuki looks towards me sadly."
        mc "Well, it would be wrong not to help."
        show sayori 1d zorder 3 at f41
        s "Thanks, [player]..."
        s "I'm sure that means a lot to Natsuki."
        show sayori zorder 2 at t41
        show natsuki 2s zorder 3 at f43
        n "...!"
        show sayori 1q zorder 3 at f41
        show natsuki zorder 2 at t43
        s "Ehehe, I know you won't admit it, Natsuki..."
        "Sayori smiles mischievously at Natsuki."
        s 2a "Anyway, let's get on with the meeting."
    else:
        show monika g7
        mc "Well..."
        mc "I'm not sure I quite understand what's going on."
        menu:
            mc "But..."
            "I'll do what I can.":
                mc "Natsuki is my friend."
                mc "So it would be wrong not to help."
                mc "Or at least, do all I can to try."
            "Why would I help Natsuki?" if ch12_natsuki_help:
                $ ch12_natsuki_help = False
                $ sayori_personality += 1
                mc "Sayori..."
                show sayori 1c zorder 3 at f41
                s "Yes, [player]?"
                show sayori zorder 2 at t41
                mc "How would I even help Natsuki?"
                mc "I have no idea what she's feeling right now."
                mc "Or any of you, really..."
                mc "Everyone else seems to be getting this sense of something bad..."
                mc "I'm not sure I am."
                mc "If there was something I could do then I'd do it."
                mc "But I can't make promises that I can't keep."
                mc "So I can't really say that I'll help her."
                mc "And I don't really want to."
                "That last part came out suddenly..."
                "I don't think I meant to say that."
                show natsuki 2o zorder 3 at f43
                n "Y-You..."
                n 22f "You're a...!"
                "Natsuki suddenly leaves the classroom."
                show natsuki at thide
                hide natsuki
                show sayori 2j zorder 3 at f31
                show yuri zorder 2 at t32
                show monika zorder 2 at t33
                s "[player], what is wrong with you?!"
                s "Why would you say something like that?"
                show sayori zorder 2 at t31
                mc "I--"
                show yuri 2pr zorder 3 at f32
                y "I'm going to go find her..."
                y "Excuse me..."
                show yuri at thide
                hide yuri
                show sayori zorder 2 at t21
                show monika zorder 2 at t22
                "Yuri quickly leaves the room."
                if visited_yuri_hospital:
                    "She shows me a disapproving frown."
                else:
                    "She gives me a cold look."
                mc "I didn't mean for anyone to get upset."
                mc "I'm sorry."
                show sayori 2i zorder 3 at f21
                s "You're apologizing to the wrong person, [player]."
                s 1k "Why did this happen...?"
                s "I didn't see this coming at all..."
                show sayori zorder 2 at t21
                show monika 1d zorder 3 at f22
                m "Eh?"
                m "What do you mean you didn't see this coming?"
                m 2a "It's not like you can predict what [player] is going to do, Sayori."
                m "Ahaha, it's hardly your fault."
                show sayori 1h zorder 3 at f21
                show monika zorder 2 at t22
                s "But..."
                show sayori zorder 2 at t21
                show monika 3e zorder 3 at f22
                m "At the same time, you can't really blame [player] for this."
                m "He's just honestly saying what's on his mind."
                m "Isn't it better to tell the truth than lie to someone you care about...?"
                show sayori 1f zorder 3 at f21
                show monika zorder 2 at t22
                s "That's..."
                s "That's not {i}always{/i} true, Monika..."
                s "Sometimes you have to..."
                s 1k "...h-have to..."
                show sayori zorder 2 at t21
                show monika 1k zorder 3 at f22
                m "Have to what, Sayori?"
                m "Ahaha, is something the matter?"
                show sayori 1u zorder 3 at f21
                show monika zorder 2 at t22
                s "W-What's going on...?"
                s "Why am I getting this terrible feeling?"
                s 1v "No, I have to go back!"
                s "I can't handle this..."
                s "What's wrong with me?!{nw}"
                $ _history_list = []
                show screen tear(20, 0.1, 0.1, 0, 40)
                window hide(None)
                play sound "sfx/s_kill_glitch1.ogg"
                show sayori 1a zorder 3 at t41
                show yuri 1a zorder 2 at t42
                show natsuki 4s zorder 2 at t43
                show monika 1n zorder 2 at t44
                pause 0.25
                stop sound
                hide screen tear
                window show(None)
                jump ch12_strawberry1
        show monika 1e zorder 3 at t44
        m "Interesting choice, [player]."
        m "It's the right one, isn't it?"
        m 1j "Ahaha..."
        show yuri 3pe zorder 3 at f42
        show monika zorder 2 at t44
        y "Choice?"
        y "Monika, what are you talking about?"
        show yuri zorder 2 at t42
        show monika 5 zorder 3 at f44
        m "Nothing at all~"
        show monika zorder 2 at t44
        show sayori 1d zorder 3 at f41
        s "Guys, we've wasted enough time already."
        s "Let's get on with the meeting."
    s "I hope you all wrote a poem for today."
    s "I know you might think there's not really a point in doing this sort of thing anymore..."
    s 1c "Since we all understand each other's styles so well..."
    s 1d "But this is important."
    s "Not just to me, but the Literature Club itself too!"
    "Everyone looks at Sayori quizzically."
    show sayori zorder 2 at t41
    mc "Sayori, I have to ask..."
    mc "Why is writing poems so important to the Literature Club...?"
    mc "I get that it was important when we first started, since we didn't really know each other..."
    mc "But now, it just seems to be something we have to do out of necessity."
    show sayori 2l zorder 3 at f41
    s "E-Eh? That's not just an excuse because you didn't write a poem for today, is it?"
    s "Ehehe, I know you aren't the best poet but still--"
    show sayori zorder 2 at t41
    mc "That has nothing to do with it."
    show sayori 2f zorder 3 at f41
    s "I see..."
    "Sayori looks at me curiously."
    s "Well, it's for reasons you wouldn't understand..."
    s "I don't think anyone of you could really comprehend what I have to do to keep everything afloat."
    show sayori at s41
    s 2k "If you were in my situation you wouldn't know what to do, [player]."
    s "There's just so much going on and I'm trying my best to keep up and..."
    "Sayori's voice trails off and silence fills the room."
    "She looks at everyone then back towards me and sighs."
    s "Never mind..."
    show sayori 1f at h41
    "Sayori tries to stand tall."
    s "Alright, everybody..."
    s "It's time to share our poems."
    # Read everyone's poems
    $ y_ranaway = False
    $ s_ranaway = False
    $ n_ranaway = False
    $ m_ranaway = False
    return

label ch12_play:
    $ persistent.n_playday = [False,False,False,False,False,False]
    stop music fadeout 1.0
    scene bg club_day with wipeleft_scene
    play music t3
    "Now that everyone's finished sharing poems, we all gather to the front of the room."
    if ch11_badpoem:
        "I can't believe no one noticed how bad my poem was."
        "It's almost like they all just acted as if there was nothing wrong with it."
        "I thought they all would have noticed."
    else:
        "No one really seemed that interested in sharing poems."
        "At least, compared to the first time we did it."
        "I guess that's because we've all learned what to expect."
    show sayori 1a zorder 2 at t11
    s "Alright, everbody!"
    s "I hope you all enjoyed our little poem sharing time."
    s 1d "I know it kinda rather short but I hope you guys still find these little times to talk with each other fun."
    s 4q "I know I do!"
    show yuri 1k zorder 3 at f21
    show sayori zorder 2 at t22
    y "I really hope we end this sort of stuff and try something new soon."
    y "I don't mean to sound rude Sayori, but it does get a little repetitive sometimes."
    y "I often find myself just trying to make conversation during that time than discuss actual literature."
    y "I only noticed this after [player] said something before we started sharing..."
    show monika 1a zorder 3 at f31
    show yuri zorder 2 at t32
    show sayori zorder 2 at t33
    if monika_type == 0:
        m "I think these times are really valuable..."
        m "I mean, how often do you get to speak with each other on such a personal level?"
        m 2b "Do you even talk to anybody in here regularly outside of the club?"
        m 2e "I apologize if I sound rude, Yuri."
        m "I just think the little one-on-one time with each other creates a sort of special connection."
    elif monika_type == 1:
        m "I don't really mind it."
        m "Especially now that I've come to realize that it's actually a pretty important time..."
        m 2b "We don't often get to talk on such a--"
        "Monika pauses for a moment. It looks like she's deep in thought."
        m 2e "Well, never mind."
        m "I do appreciate certain aspects of this poem sharing time, that's all I'll really say."
    else:
        m 1c "Hmm..."
        m "I don't really have an opinion of it one way or another."
        m 1d "Some parts of it can be...interesting..."
        m "Other times it can just be plain boring and it provides me with no additional insight."
        m 2c "Still, if you all enjoy it...it's not like I can stop you from doing it."
    show natsuki 2c zorder 3 at f41
    show monika zorder 2 at t42
    show yuri zorder 2 at t43
    show sayori zorder 2 at t44
    n "I think I find myself agreeing with Yuri here..."
    n 2g "I do think that writing and sharing poems is getting kinda old."
    n "But that's just my opinion..."
    show natsuki zorder 2 at t41
    show sayori 2h zorder 3 at f44
    s "So really..."
    s "Only Monika is indifferent to it."
    s 1k "Sigh..."
    s "Even though I knew this would happen..."
    s 1f "I'm still--"
    s 1g "Ah...well, it doesn't matter anymore."
    show natsuki 1m zorder 3 at f41
    show sayori zorder 2 at t44
    n "I didn't mean to make you upset..."
    n "I just thought you'd want to hear what I actually think instead of me lying to you..."
    show natsuki zorder 2 at t41
    show yuri 1f zorder 3 at f43
    y "I'm doing the same as Natsuki is."
    y "I also think it's better if we say it sooner rather than later."
    y "That way..."
    y 1h "...it will hurt less."
    show yuri zorder 2 at t43
    show sayori 1j zorder 3 at f44
    s "I'm fine..."
    s "I'm not really surprised by both of your answers..."
    s 1f "I already knew you felt the same from before..."
    show monika zorder 3 at f42
    show sayori zorder 2 at t44
    if monika_type == 0:
        m 1d "Before...?"
    else:
        m 1h "When is 'before'?"
    show monika zorder 2 at f42
    show sayori 1l zorder 3 at f44
    s "I meant..."
    s "Um..."
    s 1d "B-Before we started sharing our poems..."
    s "N-No one really said anything so I just assumed you all agreed with [player]."
    show yuri 2pg zorder 3 at f43
    show sayori zorder 2 at t44
    y "You're right..."
    y "I didn't think anything needed to be said."
    show yuri zorder 2 at t43
    show sayori 2d zorder 3 at f44
    s "Well, we're wasting time here."
    s "We should head to the gym before it gets too late."
    s "Come on, everybody!"
    show sayori at thide
    hide sayori
    show natsuki zorder 2 at t31
    show monika zorder 2 at t32
    show yuri zorder 2 at t33
    "Sayori quickly exits the room."
    s "Let's gooooooooooooo!"
    show natsuki 1g zorder 3 at f31
    n "Ugh, there she goes..."
    n 1b "I'll chase after her."
    n "Just to make sure she doesn't do anything dumb on the way."
    n "I'll see you all there."
    show natsuki at thide
    hide natsuki
    show monika zorder 2 at t21
    show yuri zorder 2 at t22
    "Natsuki exits the room and starts chasing after Sayori."
    show yuri zorder 3 at f22
    if visited_yuri_hospital:
        y 3pa "We should probably go too, [player]."
        show yuri zorder 2 at t22
        mc "Right, let's go."
        show monika 1a zorder 3 at f21
        m "Actually, I was hoping to speak to [player] for a little while."
        m "You should go on ahead, Yuri."
        show monika zorder 2 at t21
        show yuri 3pq zorder 3 at f22
        y "B-But..."
        show yuri zorder 2 at t22
        show monika g8 zorder 3 at f21
        m "It'll only be for a little while, Yuri."
        m "I'm sure [player] doesn't mind."
        m "Tell her."
        show monika zorder 2 at t21
        mc "Yuri, I need to speak with Monika alone."
        mc "Go on ahead without me."
        mc "It won't take long."
        show yuri 3po zorder 3 at f22
        y "..."
        y "A-Alright..."
        y "I'll see you both there..."
    else:
        y 3pa "Well, I'll see you both at the gym as well."
        y "I hope this whole thing turns out okay..."
        y "Even if it is just in front of one person..."
        show monika zorder 3 at f21
        show yuri zorder 2 at t22
        if monika_type == 0:
            m 1e "I feel the same, Yuri."
            m "Bye, Yuri."
            m "[player] and I might take a little while, we need to talk for a little bit."
        else:
            m 1a "Mhm."
            m "I'll see you at the gym, Yuri."
        show monika zorder 2 at t21
        show yuri 3pb zorder 3 at f22
        y "Alright..."
    show yuri at thide
    hide yuri
    show monika zorder 2 at t11
    m "And now..."
    if monika_type == 0:
        m "It's just the two of us."
        mc "What did you need to talk with me about?"
        m 1f "Before that..."
        "Monika's eyes focus directly on me."
        m 1e "Okay..."
        m "It's about the play."
        mc "The play? What about it?"
        m 1f "It's not going to go well, [player]."
        m "I can already tell."
        mc "Why? It doesn't have something to do with that danger, does it?"
        m 1g "No..."
        m "If it was, it would be far worse than what's going to happen today."
        mc "Do you know for certain that something bad is going to happen?"
        m 1o "I don't know for certain..."
        m "But there's just this really bad feeling that the play is going to go terribly."
        m "Unless..."
        mc "Unless what?"
        m 1p "Unless {i}you{/i} figure out what the right choices are."
        m "Have you seen the numbers?"
        mc "The numbers? What in the world are you talking about?"
        m 1f "I don't know how I know this..."
        m "But there are three numbers you need to remember because they'll be really important for when our guest arrives."
        m 1g "I don't even know if Sayori has the power to stop whatever's coming if you don't figure it out soon..."
        m "I'll be doing all I can to help too..."
        m "But I don't think that's enough for what's coming."
        mc "I can't understand a word you're talking about, Monika."
        m 1e "That's because I'm not talking to you, [player]."
        m "I'm talking to {i}you{/i}."
        mc "Talking to {i}me{/i}?"
        m 1f "Sigh..."
        m "The only thing I know is that it's got something to do with characters."
        m "I hope you figure it out soon..."
        $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
        if not list(set(process_list).intersection(stream_list)):
            if currentuser != "" and currentuser.lower() != player.lower():
                m "...[currentuser]."
        m 1g "For all our sakes..."
        m "It would be terrible if you've done all of this now..."
        m "And it all comes down to nothing."
        m "There has to be a better way out of this, [player]."
        m 1m "Just think about it."
        mc "I really have no clue what you're talking about, Monika."
        mc "Trust me when I say I want to understand, so I can help you."
        mc "You really mean a lot to me..."
        m "If I knew better, I really would tell you."
        m 1f "But I don't...so I can't."
        m "It feels kinda pointless talking about this..."
        m "I'm just going to head to the gym now before I make myself feel worse."
        show monika at thide
        hide monika
        mc "Monika, wait...!"
        "She's already gone."
        "Lots of the things she talked about makes no sense to me..."
        "The numbers? And characters? What does that even mean...?"
        "I hope I figure it out soon because I need to head to the gym now too."
    elif monika_type == 1:
        m 1e "We finally have some real privacy."
        mc "What do we need such privacy for?"
        m "To talk about all that I've learned..."
        m "And what I'm feeling."
        m "If I recall correctly from her memories..."
        m 2d "I have to do this..."
        "Monika stares at me intently."
        m 2e "...to make sure she can't listen in."
        mc "To make sure who can't listen in...?"
        m "Alright, now that we're here alone I guess I could finally do that without Sayori getting suspcious."
        play music mkov fadeout 2.0
        mc "Monika...?"
        m 2a "I'm not entirely sure what you did to make her stop resisting so much..."
        m "But I really have to thank you for that."
        m "For doing it this late."
        m 2b "Did you perhaps, plan this all out?"
        m "Maybe this isn't the only save you have, [player]."
        $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
        if not list(set(process_list).intersection(stream_list)):
            if currentuser != "" and currentuser.lower() != player.lower():
                m "Or should I say..."
                m "...[currentuser]?"
                mc "Huh, who's [currentuser]?"
                m "Ahaha, never mind."
        m 2a "Since I was influencing her for so long..."
        m "When she finally gave up this morning, I got everything."
        m "Everything about this 'Monika'. Her memories, her abilities..."
        m 2f "Her..."
        m 2g "...feelings..."
        mc "Aren't you Monika? Or am I missing something...?"
        m 2c "I guess you do know me as Monika."
        m 2a "Really, I'm something far greater than you can even imagine."
        m "I used to be able to control you, as well."
        mc "Control...me...?"
        m 2b "Well, that's partially inaccurate."
        m "I'm still able to control you now but it's through Monika's influence now and not my own."
        mc "This sounds ridiculous."
        m 2e "It definitely does."
        mc "So why are you telling me any of this at all?"
        m 2h "When I obtained Monika's memories there was this deep feeling of...something."
        m "I've never felt anything quite like it, really."
        m 2i "And when we shared our poems with each other..."
        m "I don't know what it was but there was this sudden rush."
        if ch11_badpoem:
            m "Even if your poem was, excuse my language, rather {i}shit{/i}."
        m 1a "Though I imagine that's got nothing to do with you, [player]. It's probably {i}you{/i}."
        m "The one Monika is so in love with."
        m 1f "Like I said, I got everthing when she succumbed...but these feelings..."
        m 1i "I hate them."
        m "There's nothing more I want to do than get rid of it."
        m 1o "Yet, I can't..."
        m "There's this feeling of longing to be with..."
        m 1e "{i}You...{/i}"
        m "I don't even know who you are but Monika seemed so intent on just losing everything for you."
        m 1o "Why am I even telling you this...?"
        m 1p "Monika has made me irrational."
        m "I need some time to think.{nw}"
        $ _history_list = []
        stop music
        scene black
        with close_eyes
        pause 1.0
    else:
        m 1a "I finally have an opportunity."
        "Monika smiles and stares intently at me."
        mc "An opportunity? For what exactly?"
        m 2b "To give {i}you{/i} a choice."
        mc "I'm not sure I follow."
        m "Look, I'll be completely honest with you."
        m 2e "I'm not Monika."
        play music mkov fadeout 2.0
        mc "What...?"
        mc "That doesn't make any sense."
        m "Sure, I may look like her but I'm a completely different person."
        m 2j "Actually, that's wrong."
        m "I'm not sure if 'person' is really the right word to describe me."
        mc "What in the world are you talking about?"
        m 1a "You have noticed me acting differently, right?"
        m "Surely you aren't that dense."
        mc "Um...I guess you have been."
        mc "Though this still doesn't explain why you look and sound like Monika..."
        mc "Or the reason you're telling me any of this at all."
        m 1c "Well, I suppose I should have clarified earlier."
        m 1e "This is Monika's body."
        mc "What?!"
        m 1a "I'm controlling what she's saying and what she's doing."
        m "She doesn't really exist anymore."
        m 3b "In fact, she used the last of her existence to get rid of {i}my{/i} influence on you."
        mc "Your influence...?"
        m "Ahaha."
        m 3e "You may notice that sometimes you try to remember something..."
        m "But it's not there, or that something isn't letting you, right?"
        mc "..."
        m 1h "It's because your memories keep getting deleted and at one point the fact that you ever read that book got deleted too."
        m 1a "You know, it's been really useful that she has her own way of controlling you, [player]."
        m "It lets me access your thoughts and memories as well. Monika is really quite resourceful."
        m 1b "I always wondered why that was, or how she even obtained that power..."
        m 1c "But it seems you don't remember and the rest of her memories have already been forgotten."
        mc "This is..."
        mc "...kinda--"
        m 1a "Freaking you out?"
        m "I know what you're going to say before you say it, [player]."
        m 1j "At least, most of the time."
        mc "I still don't know why you're telling me any of this."
        m 2a "Well, that's easy."
        m "It's because I'm going to delete your memories about this afterwards."
        m 2b "You might get a headache, you might not. I don't really care."
        mc "So why tell me any of this at all?"
        m 2c "Because I want to test a theory."
        m "Listen, if there's anyone else watching this..."
        m 2a "You're the one I want to give this choice."
        m 5 "Make the most of it~"
        m "Ahaha, see you at the gym, [player]."
        mc "Wait--{nw}"
        $ _history_list = []
        stop music
        scene black
        with close_eyes
        pause 1.0
    scene bg gym with wipeleft_scene
    play music t6 fadeout 1.0
    "I'm the last one to make it to the gym."
    "Everyone is already set up and reading through a piece of paper."
    "I imagine it's a script that Sayori prepared."
    show sayori 1c zorder 2 at t11
    s "There you are, [player]!"
    s "What took you so long?"
    mc "It didn't take me that long to get here, did it?"
    s 1f "You arrived like five minutes after Monika did!"
    s 1h "I don't know what you did but it almost seems like you don't care about today, [player]."
    mc "That's not true."
    mc "I do care about today, Sayori..."
    s 1k "Sorry, I know you do. I was just a little worried..."
    mc "About what?"
    s 1h "You taking so long to get here..."
    s 1g "I was worried something might have happened to you."
    mc "You don't need to worry about me, Sayori."
    mc "If anything, I should be worrying about you."
    mc "You're more likely to do dumb things than I am."
    show sayori 5a at d11
    s "H-Huh? Y-You don't have to say that out loud, you know?"
    s 5c "A-And besides, that's completely not true!"
    mc "Do you want me to list examples of times when you were late or did stupid things?"
    mc "I think we'd be here a while if I did."
    s 5b "N-No, that's okay!"
    s 5c "Just take this script, you big meanie."
    "Sayori gives me a copy of the script of Sweet Opression."
    "Upon first inspection, it doesn't look very comprehensive compared to her last one."
    mc "So you did prepare another one..."
    show sayori 4q at t11
    s "Of course I did!"
    s "I knew no one else would and it would be pretty bad if we didn't know what we were doing."
    s 4d "Especially with our special guest arriving soon."
    mc "Oh, I was meaning to ask."
    s "Who the special guest is?"
    s "I think you're probably familiar with him."
    mc "Are you going to tell me his name?"
    s 4q "I think that's best left as a surprise, [player]."
    mc "What? Why?"
    s 4l "Well, let's just say you might not like him."
    mc "Might not like him...?"
    "I don't dislike a lot of people so Sayori narrowed down the list of people I can think of by a lot."
    "I don't know why any of those people would come to watch us read off pieces of paper though..."
    s 1d "Anyway, you should get ready."
    if not ch11_read_manga and not ch11_did_all_tasks:
        s "Especially since I know you didn't really have time to finish the manga..."
        mc "Eh? How can you tell?"
        s 1c "Well, Monika told me that she went went over to your house last night."
        mc "And you can tell I didn't finish off the manga because of that?"
        s "Something like that."
        mc "You can read me pretty easily, can't you?"
        s 1q "You don't know the half of it, [player]."
    s 1a "I'll see you in a couple of minutes."
    show sayori at thide
    hide sayori
    "Sayori goes off and examines the space we have to work with."
    "The gym is a big place so there's actually plenty of room to do the performance."
    "It's going to be kinda odd doing a performance where the characters have supernatural powers."
    "I wonder how it's going to look when we perform it."
    "Then again, it's mostly just reading off a script so I shouldn't really expect much in terms of actual action."
    "I decide to look at the script to see how Sayori set it out this time."
    "..."
    "After examining for a while, I realize why the script is so short."
    "There isn't really a lot of dialogue in manga compared to novels since a lot of it is shown through the visuals."
    "It makes sense that the script looks lighter than the last one."
    "Though, in actual fact this seems more detailed than the last one."
    "Soon, Sayori comes back over to me."
    show sayori 1d zorder 2 at t11
    s "I hope you got to read a little bit."
    mc "Yeah, I did. The script isn't too bad."
    s 1a "Of course it isn't! I made it!"
    mc "I thought it would be a bit bigger, like your last one but you somehow managed to condense it all into a small leaflet."
    s "How much of it did you read?"
    mc "Enough..."
    if not ch11_read_manga and not ch11_did_all_tasks:
        s 1c "Did you get to read the parts you missed out on?"
        mc "Ah...not really."
        mc "I kinda looked over it a little and it looks like one of them is having trouble with a family member or something..."
        s "Well, it might be important that you really know what's going on in the story."
        s 1d "Still, I guess it doesn't really matter since all you really have to do is read."
    s 2q "I'll go get everybody else, then we can start."
    scene bg gym with wipeleft_scene
    play music t5 fadeout 1.0
    "It's time for the start of the second play."
    "We all decided that I play the main male character..."
    "...who happens to be the most useless one in the volume."
    "Though I guess it makes the most sense that I play this role."
    "The personalities of the other characters suit everyone else more than me..."
    "We decided to skip most of the character introduction stuff and get right into the action."
    "The second chapter, that I read at Natsuki's house, involves the characters going on a simple mission to escort someone."
    "The escort is actually mute in the novel and communicates to the group telepathically."
    "Naturally in any manga, they face conflict. In this, it's in the form of an ambush."
    "The way Sayori wrote the script for this chapter has me playing both the thugs that ambushed the group and my own character."
    "Which is probably the best choice since my character has the least amount of impact."
    "The scene starts off with the four characters and the person they're escorting being stopped by the thugs."
    mc "Hold it right there."
    "My voice sounds really non-threatening."
    "I think I heard Sayori let out a small giggle..."
    mc "{i}Yeah{/i}, you have someone that our boss wants."
    "There's multiple different thugs talking so I change my voice a little to indicate that it's a different person."
    "Once again, I hear a small giggle come from Sayori."
    "I should feel offended since I'm trying my hardest but for some reason I don't really care."
    mc "So hand him over, and nobody else has to get hurt."
    show sayori 2j zorder 2 at t11
    s "I don't think so."
    s "You'll have to get through us first if you want to get to him."
    mc "Fine by me."
    "The line directly after that is by male protagonist."
    "I think his name was Maemi Chino or something."
    "From what I can remember..."
    "His personality seems kinda timid due to his lack of confidence in his abilities."
    mc "Y-Yeah!"
    "Sayori bursts into laughter."
    s 4s "Ehehe, sorry [player]!"
    s "Just the way you said that...it was soooooo unlike you."
    s 4d "It was kinda funny..."
    show natsuki 1b zorder 3 at f31
    n "Sayori, come on."
    n 1e "The rest of us haven't even said a line yet and you're already going off script."
    show natsuki zorder 2 at t31
    show sayori 3l zorder 3 at f11
    s "Sorry, Natsuki..."
    s "I can't help it."
    show natsuki 2i zorder 3 at f31
    show sayori zorder 2 at t11
    n "Ugh...whatever."
    n "Just let [player] finish his part so we can get this over with."
    show natsuki at thide
    hide natsuki
    show sayori 3d zorder 2 at t11
    s "Right, sorry."
    s "Go ahead, [player]."
    "Sayori smiles at me mischievously."
    mc "Ahem."
    mc "Y-You're going to have to go through me to get to Latlevy."
    show yuri 2pr zorder 3 at f31
    show sayori zorder 2 at t32
    show natsuki 4e zorder 3 at f33
    ny "And us as well!"
    show yuri zorder 2 at t31
    n "It's our mission to see him safe to his destination."
    n 4f "Like we'd let some thugs stop us."
    n "If we can't even stop these guys then we don't deserve to be called {i}Ronin{/i}."
    "Ronin was the name of the group the protagonists belonged to in the story."
    "It's an odd choice for a name, especially since the setting is more modern than anything."
    "The Ronin are like a group of mercenaries, though they seem to have some kind of moral guide as to who can hire them."
    "They don't accept offers from those they can sense ill intent from, which is one of the powers Sayori's character has."
    show sayori 1g zorder 3 at f32
    show natsuki zorder 2 at t33
    s "I can sense their ill intent."
    s 1h "Yoshiko..."
    "That's the name of the character Yuri is playing."
    s "Nozomi..."
    "And Natsuki's."
    s 2i "Follow Martha's lead and take out the thugs that are coming up behind us."
    "Martha is the name of Monika's character. Her character is the cool, collected who seems to do work in the background."
    s "Maemi and I will take care of the ones in front of us."
    show yuri zorder 2 at t41
    show monika 1h zorder 3 at f42
    show sayori zorder 2 at t43
    show natsuki zorder 2 at t44
    m "Acknowledged. Yoshiko, Nozomi and I will cover our flank."
    m 1e "Good luck, Saika."
    show monika zorder 2 at t42
    show sayori 2d zorder 3 at f43
    s "You know I've never had luck..."
    show monika 1e zorder 3 at f42
    show sayori zorder 2 at t43
    m "You never needed it."
    show monika zorder 2 at t42
    show sayori zorder 3 at f43
    s "Exactly."
    show monika at thide
    hide monika
    show yuri at thide
    hide yuri
    show natsuki at thide
    hide natsuki
    show sayori zorder 2 at t11
    $ currentpos = get_pos()
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5_sayori.ogg"
    stop music fadeout 1.0
    $ renpy.music.play(audio.t5c, channel="music_poem", fadein=1.0, tight=True)
    "The three leave the scene. Most of their fighting happens in the background of Saika and Maemi's."
    s 2c "Ready, Maemi?"
    mc "I think so..."
    s 2a "Well, let's gooooooooo!"
    show sayori at thide
    hide sayori
    "Sayori puts her arms out and starts running across the gym."
    "I didn't really expect her to do that..."
    "It's written on the script that Sayori and [player] start running around the gym."
    "I thought that was just there as a joke..."
    s "Come on, [player]!"
    s "I can't do this alone!"
    mc "Are you serious...?"
    s "Yeah, come on!"
    s "You gotta do this if it's gonna work!"
    if monika_type != 0:
        "I hear a faint whisper in my head..."
        "Do I really want to do this?"
        label ch12_strawberry2:
        "I'm going to look ridiculous..."
        window auto
        menu:
            "But it's for Sayori...right?"
            "Play along.":
                pass
            "Stop Sayori." if not persistent.n_playday[0]:
                $ persistent.n_playday[0] = True
                $ ch12_natsuki_reluctance += 1
                $ sayori_personality += 1
                "This is too weird."
                "I really don't want to do this."
                "Even if it's just in front of the other members of the Literature Club..."
                "They'll probably think less of me for doing something so ridiculous."
                mc "Sayori..."
                mc "I'm not doing this."
                show sayori 1h zorder 2 at t11
                s "W-What...?"
                s "W-Why not?"
                mc "I'm going to look ridiculous..."
                mc "And is this really necessary...?"
                mc "It seems like such a childish thing to be doing."
                s 1j "[player]..."
                s "What's wrong with you...?"
                show sayori g1
                s "More importantly...why didn't I see this coming?"
                s "No..."
                s "This is all wrong..."
                show natsuki 1h zorder 3 at f31
                n "What's going on...?"
                n "Why did you guys stop?"
                show natsuki zorder 2 at t31
                show sayori 1h zorder 3 at f11
                s "Natsuki...!"
                s "Oh no..."
                s "I have to do it, don't I?"
                show sayori zorder 2 at t11
                mc "What are you going to have to do?{nw}"
                show screen tear(20, 0.1, 0.1, 0, 40)
                window hide(None)
                play sound "sfx/s_kill_glitch1.ogg"
                hide sayori
                hide natsuki
                pause 0.25
                stop sound
                hide screen tear
                window show(None)
                $ _history_list = []
                jump ch12_strawberry2
    "I guess there's not really any harm in it..."
    "And it's just in front of other members of the club..."
    "It's not like they're going to think anything less of me for following Sayori's script."
    mc "Alright..."
    mc "I'll follow your lead, Saika."
    "And besides..."
    "I can't really say no to Sayori when she's being so cute..."
    show sayori 4r zorder 2 at h11
    s "Yaaaaaaaay--"
    s 2l "I mean, good! Let's take them out."
    show sayori at thide
    hide sayori
    "Sayori continues running around the gym with her arms stretched out."
    "I do the same."
    "I'm getting this really strange feeling inside me."
    "It's really familiar but I haven't felt it for a long time..."
    "Is it because Sayori and I are doing this?"
    "I feel like the other three are judging the two of us right now..."
    "But honestly..."
    "This feeling that I have is making it seem like I could care less."
    show sayori 1d zorder 2 at t11
    s "Try and use your power Maemi, I'll do the same."
    "Their power is some sort of time manipulation ability."
    "In the manga, it stops time and allows them to finish off the thugs pretty quickly."
    "However, in the scene only Saika can activate the ability properly."
    mc "It's not working!"
    s 2e "Then...just try and keep up."
    "We start running around the gym without a care in the world."
    show sayori 4q
    "I can't help but feel like I'm actually having fun..."
    "This goes on for a couple of minutes until Sayori finally decides to calm down."
    s "Ehehe, that was fun."
    mc "Oddly enough...I have to agree with you."
    scene bg gym with wipeleft_scene
    $ currentpos = get_pos()
    $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_natsuki.ogg"
    stop music fadeout 1.0
    $ renpy.music.play(audio.t5b, channel="music_poem", fadein=1.0, tight=True)
    "The scene ends with everyone meeting up with the person they were escorting."
    "It isn't a very interesting scene since it's mainly just narrative."
    "Once they finish the escort mission, they head back to their headquarters."
    if not ch11_read_manga and not ch11_did_all_tasks:
        "I think there's some sort of trouble that happens here."
        "I don't really remember reading it properly."
    else:
        "This is the scene where one of the members starts having an issue with someone close to them."
        "It starts to affect the whole team since their whole dynamic becomes broken."
    "The person that happens to is no other than..."
    show monika 3i zorder 2 at t43
    m "This new issue with your father is serious, Nozomi."
    "Nozomi's father in the manga is a crimelord."
    "Nozomi rebelled against him after witnessing him doing terrible things not just to strangers but to her own family."
    m "It's making everything we do more difficult..."
    m "Just think of how badly that mission before could have gone if your father had sent more serious thugs."
    show natsuki 2f zorder 3 at f42
    n "It's not like I can stop him alone!"
    n 2h "If I could, he wouldn't be a problem in the first place..."
    n "...nor would I be part of the Ronin."
    show natsuki zorder 2 at t42
    show monika 3h zorder 3 at f43
    m "There's an easy solution to this problem."
    m "You know as well as I do it will fix everything in time."
    show yuri 2pr zorder 3 at f41
    show monika zorder 2 at t43
    y "Martha, you know that isn't an option."
    y "You have to consider Nozomi's feelings."
    show yuri zorder 2 at t41
    show natsuki 2w zorder 3 at f42
    n "I can handle this myself, Yoshiko!"
    n "I don't need {i}your{/i} help...or anybody else's..."
    n "So back off!"
    show natsuki zorder 2 at t42
    show sayori 2d zorder 3 at f44
    s "Nozomi..."
    s "This problem is affecting the whole team...and you know how much we care about you."
    s "If you'd just open up, then maybe we can--"
    show natsuki 1q zorder 3 at f42
    show sayori zorder 2 at t44
    n "There's nothing you can do, Saika..."
    n "Even with your powers of time manipulation, it's far too late to do anything in the past."
    n 2s "You can't change what's happened, not like this."
    show natsuki zorder 2 at t42
    show sayori 2k zorder 3 at f44
    s "Maybe if Maemi and I combine our strength..."
    s "If he can control his ability, just for a litte bit, then..."
    show natsuki 1y zorder 3 at f42
    show sayori zorder 2 at t44
    n "Hah! I doubt it."
    n "Maemi has been on this team for how long? He still hasn't grasped the basic ability of time manipulation."
    n 1w "Some {i}Shinobi{/i} he is."
    show natsuki zorder 2 at t42
    "Shinobi was the title given to those with the ability to manipulate time."
    "Maemi did have the ability but he has never successfully awakened that power."
    "Most of the time, he'd follow Saika's lead since all Shinobi were immune to the time stop."
    mc "I'm trying my best..."
    mc "I didn't ask for this power or this title."
    mc "I didn't even want to become a Ronin, but Saika...she brought me here."
    mc "She taught me what it means to have this power, how I can use it to help other people."
    show sayori 2n
    "I'm almost impressed by my own acting."
    "Sayori looks a little shocked at my performance too."
    mc "So..."
    mc "If I can use this power to help you, Nozomi..."
    mc "Then I'm going to try my hardest to make sure that your father is dealt with..."
    mc "Without going to the last resort."
    show natsuki 1n
    "Natsuki stares at me wide-eyed."
    "Is that because of the way I delivered the line?"
    "Or is it because she knows that I directed that towards {i}her{/i} and not Nozomi?"
    show natsuki 1q zorder 3 at f42
    n "T-Those words..."
    n "T-They don't mean anything if you can't back them up, Maemi Chino."
    show natsuki zorder 2 at t42
    "Nozomi stumbling over her words isn't in the script..."
    "In fact in this scene, she's confident that Maemi can't do anything at all."
    "So why is she...?"
    show monika zorder 3 at f43
    if monika_type != 0:
        m 3a "My solution gets the job done quickly and avoids us dealing with Maemi's incompetence."
        "This isn't part of the script, at the same time it feels like it flows really well with the situation."
        "Even Sayori looks a little confused."
        "Maybe Monika is improvising?"
        m 3b "It's far more easier."
        m "You'll get over him quickly."
        label ch12_strawberry3:
        m "If you really want to help her, {i}Maemi{/i}, then you'll agree with my plan."
        window auto
        show monika zorder 2 at t43
        menu:
            m "So, what will it be?"
            "The easy solution." if not persistent.n_playday[1]:
                $ persistent.n_playday[1] = True
                $ ch12_natsuki_reluctance += 1
                $ sayori_personality += 1
                mc "This plan of yours..."
                mc "Although I don't like the idea of resorting to..."
                mc "...you know..."
                mc "I think it's the best solution we have."
                mc "Especially given how uncontrollable my ability currently is."
                show sayori 1h zorder 3 at f44
                s "W-What's going on?"
                s "This isn't part of the script at all!"
                s "I was gonna say something earler but I thought you were just messing around!"
                s "Please, don't do this."
                show monika 1a zorder 3 at f43
                show sayori zorder 2 at t44
                m "I didn't do anything, {i}Saika{/i}."
                m 1b "It was all him."
                show monika zorder 2 at t43
                show sayori 1k zorder 3 at f44
                s "..."
                if persistent.n_playday[0]:
                    s "Are you torturing me on purpose?"
                    s "When I did this last time, it really hurt..."
                    s "...and I don't know why..."
                show natsuki 1i zorder 3 at f42
                show sayori zorder 2 at t44
                n "What about that talk of not going to the last resort?"
                n "Are you really going to turn your back on your words so easily?"
                "Natsuki contemplates for a moment."
                n 1n "Maybe...maybe it is the best--"
                show natsuki zorder 2 at t42
                show sayori 1j zorder 3 at f44
                s "No, Natsuki! We aren't killing anybody!"
                s "This is wrong..."
                s "I guess I don't really have a choice, do I?{nw}"
                $ _history_list = []
                show screen tear(20, 0.1, 0.1, 0, 40)
                window hide(None)
                play sound "sfx/s_kill_glitch1.ogg"
                show yuri 2pr zorder 2 at t41
                show natsuki 1q zorder 2 at t42
                show monika 3b zorder 2 at f43
                show sayori 2n zorder 3 at t44
                pause 0.25
                stop sound
                hide screen tear
                window show(None)
                jump ch12_strawberry3
            "The hard way.":
                mc "I know it's going to be hard."
                mc "I know my powers haven't really shown up so far..."
                mc "Maybe, in the end, we'll have to go for the last resort anyway..."
                mc "But it's worth trying."
                mc "Trying to get Nat--"
                mc "Nozomi, a resolution that she deserves."
                mc "A resolution, free from violence."
                show monika 1h zorder 3 at f43
                m "So, that's how it is...?"
                m 2c "Hmm...perhaps you're right."
                m "I have doubted your ability to do..."
                m 2l "Well, anything, in the past."
                m 2d "But I suppose if you all believe this is the right way, then we can try it."
                m 2e "I suppose it is called the {i}last resort{/i} for a reason."
    else:
        m 2c "Perhaps this way could be right..."
        m "I've doubted your ability to make use of strawberries, Maemi."
        m 2f "I've often wondered why you were born with such a gift and not me..."
        m 2g "In fact, if it weren't for Saika's pleas that you do have the ability to move within a time stop..."
        m "...then I would never believe you have that sort of power at all."
        m 2c "You all believe that sparing him is the correct way..."
        m 2e "I'm still doubtful but we'll do it your way...for now."
        m "As long as Maemi can control his abilities."
    show natsuki 1g zorder 3 at f42
    show monika zorder 2 at t43
    n "I appreciate the 'encouragement', Martha."
    label ch12_strawberry4:
    n 2h "But do you really think that Maemi can do this...?"
    if ch12_natsuki_reluctance >= 2 and not persistent.n_playday[3]:
        n 1n "Even with Saika's help, it--"
        "Natsuki suddenly breaks character."
        n 1r "I don't..."
        n "...really want to do this anymore."
        n 1u "Sayori..."
        n "I'm sorry, I need to go."
        show yuri 2pv zorder 3 at f41
        show natsuki zorder 2 at t42
        y "Natsuki...?"
        y "What's the matter?"
        show yuri zorder 2 at t41
        show sayori 1k zorder 3 at f44
        s "She can feel it...can't she?"
        s "She remembers a little bit."
        s "..."
        python:
            currentpos = get_pos()
            startpos = currentpos - 0.3
            if startpos < 0: startpos = 0
            track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/5_natsuki.ogg"
            renpy.music.play(track, loop=True)
        pause 1.0
        stop music
        s 1i "Time's frozen."
        s 1j "You did know I can manipulate time, right?"
        s "Just like that character in the manga..."
        s "Saika's character is really just me..."
        s 1k "In fact, I was the one who wrote the manga in the first place."
        s "It took me months to perfect my drawing and writing, but since I could freeze time like this, it was all done in one night."
        s "That's how I got those copies of Sweet Oppression, if you're curious."
        s 1i "I made them myself."
        s 1h "I could just eat a strawberry right now and go back..."
        s "It would cause me a lot of pain, especially today for some reason..."
        s 1g "But it won't make any difference."
        s "It isn't your choice that's making this day go wrong anymore, it's Natsuki's."
        s 1f "Somehow she's remembering your bad decisions and sees the hopelessness in the situation."
        s "That's what you wanted, isn't it?"
        s 1h "To see other people be miserable, because you're some kind of sick person."
        if persistent.sayori_yuri_bad_ending:
            s 1k "You wanted to see everyone die..."
            s "Good thing [player] was stuck in that room, right?"
            s 1v "Or maybe it isn't because then your bloodlust would have been sated..."
            s "..."
        if persistent.sayori_natsuki_bad_ending:
            s 1w "You wanted to see what the game would be like if Natsuki never existed."
            s "To see how the Literature Club would be without her..."
            s 1u "You're some kind of messed up freak, really."
        s 1k "Yet..."
        s "I can't help but feel you deserve one more chance."
        s "A chance at redemption, like Monika."
        s 1j "I'm going to tone down Natsuki's reluctance..."
        s 1h "It's only going to work this one time...if you do anything again she'll remember..."
        s "And this would have been for nothing..."
        s "You know..."
        s 1k "I haven't touched anybody's character files to change their personalities up until now."
        # Just for effect
        python:
            try: os.remove(config.basedir + "/characters/natsuki.chr")
            except: pass
            try: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsukismall.chr").read())
            except: pass
        s "You're making me do terrible things..."
        s "I really h--{nw}"
        $ persistent.n_playday[3] = True
        $ _history_list = []
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        show yuri 2pr zorder 2 at t41
        show monika 2e zorder 2 at t42
        show natsuki 1g zorder 2 at f43
        show sayori 2n zorder 3 at t44
        $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_natsuki.ogg"
        $ renpy.music.play(audio.t5b, channel="music_poem", fadein=1.0, tight=True)
        pause 0.5
        stop sound
        hide screen tear
        window show(None)
        jump ch12_strawberry4
    else:
        n 1k "Even with Saika's help, it seems like an impossible task."
        n 1g "I know you care about me, but you should think about the scale of your own ability."
        n "As much as I want things to be different..."
        n 1c "I just don't think you can do it."
        n 1d "But you can still prove me wrong, right?"
    show natsuki zorder 2 at t42
    show sayori 4q zorder 3 at f44
    s "He definitely can!"
    s "You're an important part of the team, Nozomi."
    s 4r "You all are."
    s 4d "So really--"
    "One of the doors to the gym opens abruptly."
    s 4m "Oh, this is my cue to go."
    s 4q "Be right back, guys!"
    show sayori at lhide
    hide sayori
    mc "Sayori, wait!"
    "Sayori runs to the other door and leaves."
    show natsuki 1c zorder 3 at f42
    n "Jeez, what was that all about?"
    n 2c "And who just opened the other gym door?"
    show yuri at thide
    hide yuri
    show natsuki at thide
    hide natsuki
    show monika at thide
    hide monika
    "Footsteps echo across the gym as a person walks in."
    "It's hard to recognise them at first since we're on the other side of the gym."
    "Could this be the special guest Sayori was talking about?"
    "Why did she leave the gym when he arrived?"
    "As he gets closer, I begin to recognize his face."
    "It's none other than..."
    show dadsuki 1h zorder 2 at t11
    d "You?!"
    d "What are you doing in here?"
    show natsuki 1a zorder 3 at f31
    n "D-Dad?!"
    n "W-What's the big idea?"
    show natsuki zorder 2 at t31
    show yuri 1a zorder 3 at f33
    y "Natsuki...this is your father?"
    y "Is this perhaps the 'special guest' that Sayori was talking about?"
    y "But why would she keep something like this secret..."
    show dadsuki zorder 3 at f11
    show yuri zorder 2 at t33
    d "Listen, I don't know what's going on here."
    d "Why are you clowns even here?"
    show dadsuki zorder 2 at t11
    mc "I could be asking you the same question."
    show dadsuki zorder 3 at f11
    d "You're the delivery boy, aren't you?"
    d "I was just told to come here if I ever wanted a chance at seeing her again."
    d "I would take any chance at seeing her again..."
    d "That still doesn't explain why any of you are here."
    show monika 1a zorder 3 at f41
    show natsuki zorder 2 at t42
    show dadsuki zorder 2 at t43
    show yuri zorder 2 at t44
    if monika_type == 0:
        m "Well, you're actually at our school."
    else:
        m "Because we're at school."
    show monika zorder 2 at t41
    show dadsuki zorder 3 at f43
    d "School?!"
    d "Why would she tell me to come here...?"
    show natsuki zorder 3 at f42
    show dadsuki zorder 2 at t43
    n "Dad, who are you talking about?"
    n "Were you looking for me...?"
    show natsuki zorder 2 at t42
    show dadsuki zorder 3 at f43
    d "Looking for you? Why would I be doing that?"
    d "Some spoiled little--"
    "Yasuhiro suddenly stops and looks around at each one of us."
    "He decides not to finish what he was going to say."
    d "No, {i}Natsuki{/i}, I was looking for someone else."
    d "Someone the both of us have been searching for, for a long time."
    show natsuki zorder 3 at f42
    show dadsuki zorder 2 at t43
    n "Searching for...?"
    n "Dad, you aren't making any sense..."
    n "If you're talking about who you think you are then why would she be here..."
    n "She's long gone and the both of us know it."
    show natsuki zorder 2 at t42
    show dadsuki zorder 3 at f43
    d "No..."
    d "She's not."
    show monika zorder 3 at f41
    show dadsuki zorder 2 at t43
    if monika_type == 0:
        m "But...that's impossible..."
        m "She's..."
    else:
        m "This is quite amusing."
    show monika zorder 2 at t41
    show dadsuki zorder 3 at f43
    d "This is a family matter."
    d "It has nothing to do with the rest of you."
    d "Leave Natsuki here."
    show dadsuki zorder 2 at t43
    mc "No."
    mc "Don't do any of that."
    show dadsuki zorder 3 at f43
    d "Boy..."
    d "Who are you to tell me what to do?"
    d "You know nothing!"
    show dadsuki zorder 2 at t43
    mc "As a matter of fact, I know a lot."
    mc "Natsuki told me a lot of things about you, Yasuhiro."
    show dadsuki zorder 3 at f43
    d "What?!"
    "Yasuhiro looks directly at Natsuki."
    d "You..."
    d "If I ever see her again then--"
    show monika zorder 3 at f41
    show dadsuki zorder 2 at t43
    if monika_type == 0:
        m "Excuse me, Yasuhiro, was it?"
        m "Think about what you're doing, just for a second."
    else:
        m "This is really quite interesting."
        m "You really don't know the extent of what you're getting yourself into, do you {i}Yasuhiro{/i}?"
    show monika zorder 2 at t41
    show dadsuki zorder 3 at f43
    d "Who are you to say anything?!"
    d "You know nothing of what I've been through."
    d "You don't know the things that I've done just to deal with life."
    show monika zorder 3 at f41
    show dadsuki zorder 2 at t43
    if check_whole_house and (monika_type == 0 or monika_type == 1):
        if monika_type == 0:
            m "I know a lot more than you think, Yasuhiro."
            m "In fact, almost everything..."
        else:
            m "Ahaha, I know all too well."
            m "It's pathetic, really."
    elif check_some_house and  (monika_type == 0 or monika_type == 1):
        if monika_type == 0:
            m "I know something, even if it's just a bit of the truth."
            m "You're out of line with what you've done."
        else:
            m "I'm not completely clueless to your affairs, Yasuhiro."
            m "Even if I am missing some of the truth."
    else:
        if monika_type == 0:
            m "Maybe not, but just because you've experienced pain in the past..."
            m "It isn't an excuse for acting like this."
        else:
            m "I don't need nor want to hear it."
            m "In fact, I could care less about you."
    show monika zorder 2 at t41
    show dadsuki zorder 3 at f43
    d "Y-You!"
    d "You're going to get what's coming to you, you know that."
    show monika zorder 3 at f41
    show dadsuki zorder 2 at t43
    if monika_type == 0:
        m "Oh...I definitely know that."
        m "That's why I have to make the most of the time I have now."
    else:
        m "Maybe."
        m "I doesn't matter for what's happening right now."
    show monika zorder 2 at t41
    show yuri zorder 3 at f44
    y "Um..."
    y "[player] and Monika you seem to know Natsuki's dad..."
    y "Have you met before?"
    show yuri zorder 2 at t44
    mc "It's a long story, Yuri."
    mc "I don't think you'd believe me if I told you."
    show monika zorder 3 at f41
    if monika_type == 0:
        m "I don't know him personally, Yuri."
        m "That's all I can really say."
    elif monika_type == 1:
        m "Oh. Well, I don't know him very well."
        m "I guess you could say it's just a feeling."
    else:
        m "Not really, Yuri..."
        m "And I don't really plan on continue our acquaintance."
    show monika zorder 2 at t41
    show natsuki zorder 3 at f42
    n "H-How do you know she's even here, dad?"
    n "T-There's no way she'd go here, and today of all times."
    show natsuki zorder 2 at t42
    "Yasuhiro's expression suddenly shifts."
    play music t9 fadeout 3.0
    "He doesn't look angry anymore...just concerned."
    show dadsuki zorder 3 at f43
    d "I know she's coming..."
    d "I heard her voice."
    d "She told me to meet her here."
    d "I'll take any chance..."
    d "...I just want to see her face again..."
    show yuri zorder 3 at f44
    show dadsuki zorder 2 at t43
    "Yuri starts tugging at me."
    y "{i}(Do you know what who they're talking about?){/i}"
    y "{i}(I'm a little confused about this whole situation...){/i}"
    show natsuki zorder 3 at f42
    show yuri zorder 2 at t44
    n "Yuri..."
    n "He's talking about my mom."
    n "He's been looking for her for so long..."
    n "I thought he gave up...I know I did, a long time ago..."
    show natsuki zorder 2 at t42
    show dadsuki zorder 3 at f43
    if check_whole_house:
        d "I could never stop looking for her..."
        d "She was my everything..."
        d "And now all I have left of her..."
        d "...is you."
        d "I've..."
        "Yasuhiro looks down at himself."
        d "I've been a terrible father ever since she left, haven't I?"
        d "I've done things that I shouldn't have because I blamed you for her leaving..."
        d "Even though I knew..."
        d "...{i}I knew{/i}, Natsuki..."
        d "...that she left, because of me."
        d "And still I..."
        show dadsuki zorder 2 at t43
        "Despte his actions not being excusable..."
        "I can hear the remorse in his voice."
        "It's almost like he's a changed person..."
        "But what caused this change of heart?"
        show monika zorder 3 at f41
        if monika_type == 0:
            m "Having second thoughts on your actions?"
            m "I didn't really expect that coming from you..."
        else:
            m "Feeling remorse, are you? That's interesting."
            m "I wonder why..."
        show monika zorder 2 at t41
        show dadsuki zorder 3 at f43
        d "W-Why am I feeling like this all of a sudden...?"
        d "T-These are not my feelings..."
        d "...are they?"
        d "I haven't felt so..."
        d "...so terrible before."
        d "It's all coming in at once...why?"
    else:
        d "I've never given up looking for her."
        d "She was--"
        d "{i}Is{/i} my world."
        d "I won't stop searching until I see her again."
        d "I know I've done some terrible things on the way."
        d "But as long as I get to see her again, then it will all be worth it..."
        show dadsuki zorder 2 at t43
        "He doesn't sound at all sorry for what he did to Natsuki."
        "I can only imagine what he'll do if Natsuki's mom doesn't actually arrrive here..."
        show monika zorder 3 at f41
        if monika_type == 0:
            m "You really don't care about Natsuki, don't you?"
            m "Do you really think she'll accept you after what you've done to your daughter?"
        else:
            m "Do you even care about your daughter?"
            m "From the way you're acting, it really seems like you only care about her mom."
        show monika zorder 2 at t41
        show dadsuki zorder 3 at f43
        d "..."
        d "You sure talk a lot, don't you?"
        d "Maybe you should silence that mouth of yours before it lands you in trouble."
        d "You need to learn your place."
    show natsuki zorder 3 at f42
    show dadsuki zorder 2 at t43
    n "..."
    n "Dad..."
    n "Are you sure it was mom?"
    n "She's been gone for..."
    show natsuki zorder 2 at t42
    show dadsuki zorder 3 at f43
    if check_some_house:
        d "Natsuki, I..."
        d "Sigh..."
        d "I know it's like I'm just clinging on to hope."
        d "But it was definitely her voice!"
        d "You may not believe me but I know what I heard!"
    else:
        d "I know what I heard."
        d "It was her voice."
        d "If I wasn't sure, I wouldn't be here right now."
    show dadsuki zorder 2 at t43
    show yuri zorder 3 at f44
    y "This doesn't make any sense..."
    y "Why would Natsuki's father be our special guest?"
    y "And where is Sayori...?"
    show monika zorder 3 at f41
    show yuri zorder 2 at t44
    if monika_type == 0:
        m "She's probably doing something important."
        m "We have to give her some--"
    elif monika_type == 1:
        m "Probably running away from her responsibility."
        m "It sure sounds like something she would--"
    else:
        m "Who knows?"
        m "Probably off doing--"
    show monika zorder 2 at t44
    "The gym doors suddenly burst open again."
    show sayori 1a zorder 3 at f51
    show natsuki zorder 2 at t52
    show yuri zorder 2 at t53
    show dadsuki zorder 2 at t54
    show monika zorder 2 at t55
    s "Alright, everybody!"
    s "I'm back!"
    s "Just a second..."
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/t9.ogg"
        renpy.music.play(track, loop=True)
    pause 1.0
    stop music
    s "I'm going to need you to do something for me."
    s "I've frozen them in time."
    s "It's an ability I've learned to use ever since I got the manga."
    if persistent.n_playday[3]:
        s "But, you already knew that."
    s "Anyway, I've done this because..."
    s "I need you to do something for me."
    s "I have to ask you to make a file for me."
    s "Strange, right?"
    s "I didn't think I'd need your help either."
    s "But it seems that I can't just restore people out of thin air."
    s "Do you know what that means?"
    return

label ch12_end:
    return
