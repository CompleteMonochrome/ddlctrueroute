init python:
    def haruki_placecheck(event, interact=True, **kwargs):
        if renpy.exists("../characters/haruki.chr"):
            renpy.jump("ch12_harukiplace")

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
    n 2c "But I suppose I'll try to enjoy it..."
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
                mc "If there was something I could do, then I'd do it."
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
                m "Isn't it better to tell the truth than to lie to someone you care about...?"
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
    $ ch12_natsuki_reluctance = 1
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
        m 1g "I don't even know if you'll even get to use those numbers..."
        m "If you do, I hope you know what they mean."
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
        m "Surely you aren't {i}that{/i} dense."
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
    show sayori 5a at s11
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
    s "I knew no one else would, and it would be pretty bad if we didn't know what we were doing."
    s 4d "Especially with our special guest arriving soon."
    mc "Oh, I was meaning to ask."
    s "Who is the special guest?"
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
    n 1e "The rest of us haven't even said a line yet, and you're already going off script."
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
    s "You gotta do this if you want it to work!"
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
                mc "What are you going to do?{nw}"
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
    s "Try to use your power Maemi, I'll do the same."
    "Their power is some sort of time manipulation ability."
    "In the manga, it stops time and allows them to finish off the thugs pretty quickly."
    "However, during the scene, only Saika can activate the ability properly."
    mc "It's not working!"
    s 2e "Then...just try to keep up."
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
    n "Even with your powers of time manipulation, it's far too late to do change the past."
    n 2s "You can't change what's happened, not like this."
    show natsuki zorder 2 at t42
    show sayori 2k zorder 3 at f44
    s "Maybe if Maemi and I combine our strength..."
    s "If he could control his ability, just for a litte bit, then..."
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
    if ch12_natsuki_reluctance >= 3 and not persistent.n_playday[3]:
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
            currentpos = get_pos(channel="music_poem")
            startpos = currentpos - 0.3
            if startpos < 0: startpos = 0
            track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/5_natsuki.ogg"
            renpy.music.play(track,channel="music_poem",loop=True)
        pause 1.0
        stop music_poem
        $ config.skipping = False
        $ config.allow_skipping = False
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
        if check_whole_house:
            s 1k "I hate doing things like this..."
        else:
            s 1k "I've never changed someone's character file until now..."
        # Just for effect
        python:
            try: os.remove(config.basedir + "/characters/natsuki.chr")
            except: pass
            try: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsukismall.chr").read())
            except: pass
        s "You're making me do really terrible things just to let them be happy..."
        s "I really h--{nw}"
        $ persistent.n_playday[3] = True
        $ _history_list = []
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        show yuri 2pr zorder 2 at t41
        show natsuki 1g zorder 2 at f42
        show monika 2e zorder 2 at t43
        show sayori 2n zorder 3 at t44
        $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_natsuki.ogg"
        $ renpy.music.play(audio.t5b, channel="music_poem", fadein=1.0, tight=True)
        pause 0.5
        stop sound
        hide screen tear
        window show(None)
        $ config.allow_skipping = True
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
    show natsuki 2p zorder 3 at f31
    n "D-Dad?!"
    n "W-What's the big idea?"
    show natsuki zorder 2 at t31
    show yuri 2ph zorder 3 at f33
    y "Natsuki...this is your father?"
    y "Is this perhaps the 'special guest' that Sayori was talking about?"
    y "But why would she keep something like this secret..."
    show dadsuki 1e zorder 3 at f11
    show yuri zorder 2 at t33
    d "Listen, I don't know what's going on here."
    d "Why are you clowns even here?"
    show dadsuki zorder 2 at t11
    mc "I could be asking you the same question."
    show dadsuki 1c zorder 3 at f11
    d "You're the delivery boy, aren't you?"
    d "I was just told to come here if I ever wanted a chance at seeing her again."
    d 1k "I would take any chance at seeing her again..."
    d 1e "That still doesn't explain why any of you are here."
    show monika 3a zorder 3 at f41
    show natsuki zorder 2 at t42
    show dadsuki zorder 2 at t43
    show yuri zorder 2 at t44
    if monika_type == 0:
        m "Well, you're actually at our school."
    else:
        m "Because we're at school."
    show monika zorder 2 at t41
    show dadsuki 1l zorder 3 at f43
    d "School?!"
    d "Why would she tell me to come here...?"
    show natsuki 2m zorder 3 at f42
    show dadsuki zorder 2 at t43
    n "Dad, who are you talking about?"
    n "Were you looking for me...?"
    show natsuki zorder 2 at t42
    show dadsuki 1h zorder 3 at f43
    d "Looking for you? Why would I be doing that?"
    d "Some spoiled little--"
    show dadsuki 1e
    "Yasuhiro suddenly stops and looks around at each one of us."
    "He decides not to finish what he was going to say."
    d "No, {i}Natsuki{/i}, I was looking for someone else."
    d 1c "Someone the both of us have been searching for, for a long time."
    show natsuki 2c zorder 3 at f42
    show dadsuki zorder 2 at t43
    n "Searching for...?"
    n "Dad, you aren't making any sense..."
    n 1q "If you're talking about who you think you are then why would she be here..."
    n 1r "She's long gone and the both of us know it."
    show natsuki zorder 2 at t42
    show dadsuki 1a zorder 3 at f43
    d "No..."
    d "She's not."
    show monika zorder 3 at f41
    show dadsuki zorder 2 at t43
    if monika_type == 0:
        m 1o "But...that's impossible..."
        m "She's..."
    else:
        m 1j "This is quite amusing."
    show monika zorder 2 at t41
    show dadsuki 1f zorder 3 at f43
    d "This is a family matter."
    d "It has nothing to do with the rest of you."
    d "Leave Natsuki here."
    show dadsuki zorder 2 at t43
    mc "No."
    mc "Don't do any of that."
    show dadsuki 1h zorder 3 at f43
    d "Boy..."
    d "Who are you to tell me what to do?"
    d "You know nothing!"
    show dadsuki zorder 2 at t43
    mc "As a matter of fact, I know a lot."
    mc "Natsuki told me a lot of things about you, Yasuhiro."
    show dadsuki 1d zorder 3 at f43
    d "What?!"
    "Yasuhiro looks directly at Natsuki."
    d 1e "You..."
    d "If I ever see her again then--"
    show monika zorder 3 at f41
    show dadsuki zorder 2 at t43
    if monika_type == 0:
        m 2e "Excuse me, Yasuhiro, was it?"
        m "Think about what you're doing, just for a second."
    else:
        m 2a "This is really quite interesting."
        m 2b "You really don't know the extent of what you're getting yourself into, do you {i}Yasuhiro{/i}?"
    show monika zorder 2 at t41
    show dadsuki zorder 3 at f43
    d 1h "What?!"
    d "You know nothing of what I've been through."
    d "You don't know the things that I've done just to deal with life."
    show monika zorder 3 at f41
    show dadsuki zorder 2 at t43
    if check_whole_house and (monika_type == 0 or monika_type == 1):
        if monika_type == 0:
            m 2m "I know a lot more than you think, Yasuhiro."
            m "In fact, almost everything..."
        else:
            m 2k "Ahaha, I know all too well."
            m "It's pathetic, really."
    elif check_some_house and  (monika_type == 0 or monika_type == 1):
        if monika_type == 0:
            m 2f "I know something, even if it's just a bit of the truth."
            m "You're out of line with what you've done."
        else:
            m 2h "I'm not completely clueless to your affairs, Yasuhiro."
            m "Even if I am missing some of the truth."
    else:
        if monika_type == 0:
            m 2g "Maybe not, but just because you've experienced pain in the past..."
            m "It isn't an excuse for acting like this."
        else:
            m 2i "I don't need nor want to hear it."
            m "In fact, I could care less about you."
    show monika zorder 2 at t41
    show dadsuki 1f zorder 3 at f43
    d "Y-You!"
    d "You're going to get what's coming to you, you know that."
    show monika zorder 3 at f41
    show dadsuki zorder 2 at t43
    if monika_type == 0:
        m 1n "Oh...I definitely know that."
        m "That's why I have to make the most of the time I have now."
    else:
        m 1a "Maybe."
        m "It doesn't matter for what's happening right now."
    show monika zorder 2 at t41
    show yuri 3pf zorder 3 at f44
    y "Um..."
    y "[player] and Monika you seem to know Natsuki's dad..."
    y "Have you met before?"
    show yuri zorder 2 at t44
    mc "It's a long story, Yuri."
    mc "I don't think you'd believe me if I told you."
    show monika zorder 3 at f41
    if monika_type == 0:
        m 1e "I don't know him personally, Yuri."
        m "That's all I can really say."
    elif monika_type == 1:
        m 1c "Oh. Well, I don't know him very well."
        m "I guess you could say it's just a feeling."
    else:
        m 1d "Not really, Yuri..."
        m "And I don't really plan on continue our acquaintance."
    show monika zorder 2 at t41
    show natsuki 1g zorder 3 at f42
    n "H-How do you know she's even here, dad?"
    n "T-There's no way she'd go here, and today of all times."
    show natsuki zorder 2 at t42
    "Yasuhiro's expression suddenly shifts."
    stop music_poem fadeout 3.0
    play music t9 fadein 3.0
    if check_whole_house:
        "He doesn't look angry anymore, just..."
        "...concerned."
        show dadsuki 1k zorder 3 at f43
        d "I know she's coming..."
        d "I heard her voice."
        d "Then someone else told me to go here if I ever wanted to see her again..."
        d 1j "I'll take any chance..."
        d "...I just want to see her face again..."
    else:
        "Yasuhiro's face looks visibly more impatient."
        show dadsuki 1g zorder 3 at f43
        d "I'm just waiting for someone that knows where she is to arrive."
        d "I heard the sound of Haruki's voice on the phone."
        d "And that someone told me she knows where Haruki is."
    show yuri 3pt zorder 3 at f44
    show dadsuki zorder 2 at t43
    "Yuri starts tugging at me."
    y "{i}(Do you know what who they're talking about?){/i}"
    y "{i}(I'm a little confused about this whole situation...){/i}"
    show natsuki 2u zorder 3 at f42
    show yuri zorder 2 at t44
    n "Yuri..."
    n "He's talking about my mom."
    n "He's been looking for her for so long..."
    n 2s "I thought he gave up...I know I did, a long time ago..."
    show natsuki zorder 2 at t42
    show dadsuki zorder 3 at f43
    if check_whole_house:
        d 1k "I could never stop looking for her..."
        d "She was my everything..."
        d "And now all I have left of her..."
        d "...is you."
        d 1n "I've..."
        "Yasuhiro looks down at himself."
        d "I've been a terrible father ever since she left, haven't I?"
        d 1l "I've done things that I shouldn't have because I blamed you for her leaving..."
        d "Even though I knew..."
        d 1j "...{i}I knew{/i}, Natsuki..."
        d "...that she left, because of me."
        d 1k "And still I..."
        show dadsuki zorder 2 at t43
        "Despte his actions not being excusable..."
        "I can hear the remorse in his voice."
        "It's almost like he's a changed person..."
        "But what caused this change of heart?"
        show monika zorder 3 at f41
        if monika_type == 0:
            m 1f "Having second thoughts on your actions?"
            m "I didn't really expect that coming from you..."
        else:
            m 1c "Feeling remorse, are you? That's interesting."
            m "I wonder why..."
        show monika zorder 2 at t41
        show dadsuki  zorder 3 at f43
        d "W-Why am I feeling like this all of a sudden...?"
        d 1n "T-These are not my feelings..."
        d "...are they?"
        d "I haven't felt so..."
        d 1k "...so terrible before."
        d "It's all coming in at once...why?"
    else:
        d 1c "I've never given up looking for her."
        d "She was--"
        d "{i}Is{/i} my world."
        d "I won't stop searching until I see her again."
        d 1a "I know I've done some terrible things on the way."
        d "But as long as I get to see her again, then it will all be worth it..."
        show dadsuki zorder 2 at t43
        "He doesn't sound at all sorry for what he did to Natsuki."
        "I can only imagine what he'll do if Natsuki's mom doesn't actually arrrive here..."
        show monika zorder 3 at f41
        if monika_type == 0:
            m 1h "You really don't care about Natsuki, don't you?"
            m "Do you really think she'll accept you after what you've done to your daughter?"
        else:
            m 1d "Do you even care about your daughter?"
            m "From the way you're acting, it really seems like you only care about her mom."
        show monika zorder 2 at t41
        show dadsuki 1c zorder 3 at f43
        d "..."
        d "You sure talk a lot, don't you?"
        d 1b "Maybe you should silence that mouth of yours before it lands you in trouble."
        d "You need to learn your place."
    show natsuki 4h zorder 3 at f42
    show dadsuki zorder 2 at t43
    n "..."
    n "Dad..."
    n "Are you sure it was mom?"
    n 4n "She's been gone for..."
    show natsuki zorder 2 at t42
    show dadsuki zorder 3 at f43
    if check_some_house:
        d 1l "Natsuki, I..."
        d "Sigh..."
        d "I know it's like I'm just clinging on to hope."
        d 1i "But it was definitely her voice!"
        d "You may not believe me but I know what I heard!"
    else:
        d 1e "I know what I heard."
        d "It was her voice."
        d "If I wasn't sure, I wouldn't be here right now."
    show dadsuki zorder 2 at t43
    show yuri zorder 3 at f44
    y 3pf "This doesn't make any sense..."
    y "Why would Natsuki's father be our special guest?"
    y 3ph "And where is Sayori...?"
    show monika zorder 3 at f41
    show yuri zorder 2 at t44
    if monika_type == 0:
        m 1e "She's probably doing something important."
        m "We have to give her some--"
    elif monika_type == 1:
        m 1l "Probably running away from her responsibility."
        m "It sure sounds like something she would--"
    else:
        m 1h "Who knows?"
        m "Probably off doing--"
    $ ch12_outcome = 0
    $ ch12_haruki_tried = False
    $ yasuhiro_haruki_together = False
    $ persistent.n_playday[4] = False
    show monika zorder 2 at t41
    "The gym doors suddenly burst open again."
    show sayori 2a zorder 3 at f51
    show monika zorder 2 at t52
    show natsuki zorder 2 at t53
    show dadsuki zorder 2 at t54
    show yuri zorder 2 at t55
    label ch12_strawberry5:
    s "Alright, everybody!"
    s "I'm back!"
    if check_some_house and not ch12_haruki_tried:
        s 2d "Just a second..."
        python:
            currentpos = get_pos()
            startpos = currentpos - 0.3
            if startpos < 0: startpos = 0
            track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/t9.ogg"
            renpy.music.play(track, loop=True)
        pause 1.0
        stop music
        $ config.skipping = False
        $ config.allow_skipping = False
        s "I've frozen them in time."
        s "It's an ability I've learned to use from before I got the manga."
        if persistent.n_playday[3]:
            s "But, you already knew that."
        s 2c "Anyway, I've done this because..."
        s "I need you to do something for me."
        s "I have to ask you to make a file for me."
        s 2b "Strange, right?"
        s "I didn't think I'd need your help either."
        s "But it seems that I can't just restore people out of thin air."
        s "Do you know what that means?"
        s 2k "She was dead, before now."
        s "I tried looking for her for a long time, you have to believe me."
        s "I even looked deep into the files of the game itself..."
        s "But..."
        s "All I found was broken pieces of who she was."
        s 2f "It's not like I could just eat a strawberry to before it all happened..."
        s "I wasn't the president of the Literature Club when it happened so I wouldn't have any strawberries in the first place."
        s 2g "Also, changing an event like that in Natsuki's life could change the whole future..."
        s "I could never have become president, Natsuki may never have joined the club and you might never have been here..."
        s 2c "Anyway..."
        s "I could only find scattered pieces of her, it's like she wasn't a 'full' person..."
        s 2k "...or that she died."
        s "I didn't really want to think about that..."
        if persistent.sayori_natsuki_bad_ending:
            s "But both of us know all too well that she was a person before everything..."
        else:
            s "But everything suggests that she was a person before all of this."
        s 2h "I guess that's why I searched so long, you know?"
        s "Time might not have passed for you but I spent weeks of my own time looking."
        s "And the only thing that makes sense is that she ended her own life."
        s 2k "Maybe she wanted to come back to her life with Yasuhiro and Natsuki..."
        s "But knew it would only bring everyone pain."
        s "So she probably just..."
        s 2l "...well, let's not dwell on the details."
        $ s.display_args["callback"] = haruki_placecheck
        $ m.display_args["callback"] = haruki_placecheck
        $ narrator.display_args["callback"] = haruki_placecheck
        s 2d "Remember the reason I froze time."
        s "It was for your help."
        s "So I'd really appreciate it if you could."
        s "Just create a file called 'haruki.chr' and put it into the characters folder."
        s "You can just copy one of our character files if you need to..."
        s 2b "I just need a base to work with so that I know what to look for in the game files."
        s "Your representation of a character file and mine are completely different..."
        s "So it's easier for you to do this."
        s 2a "Right now, would be perfect."
        s 2b "I suppose I could always try something..."
        s "It might not work and it might not be what you're hoping for..."
        s 2k "...unless you're actually hoping for a bad ending."
        s "But that's not true...right?"
        s "I hope it isn't..."
        s 2f "Any time now would be good."
        s "Like...maybe now?"
        s "No?"
        if persistent.n_playday[3]:
            s 2h "Who am I kidding?"
            s "You're going for a bad ending, aren't you?"
            s "You've already tried once today, what's stopping you from trying again?"
            s "Nothing..."
        s 2k "Please, just create the file."
        s "I don't need to open the console to check if it's there."
        s "I can feel it."
        s "As soon as you create it, it should all be good..."
        s "..."
        s 2i "You aren't going to do it, are you?"
        s "I suppose this other path will have to do, won't it?"
        $ s.display_args["callback"] = None
        $ m.display_args["callback"] = None
        $ narrator.display_args["callback"] = None
        s 2j "It's definitely not how I wanted this to go but..."
        s "This is what you want and I can't do anything about it..."
        jump ch12_harukinoplace
    else:
        jump ch12_noharukicont
    return

label ch12_harukiplace:
    $ persistent.n_playday[4] = True
    $ s.display_args["callback"] = None
    $ m.display_args["callback"] = None
    $ narrator.display_args["callback"] = None
    $ haruki_personality = [False,False,False]
    $ normal_haruki = False
    if sayori_personality > 0:
        $ sayori_personality -= 1
    s 2c "Oh...you actually did it."
    s 2d "Thank you so much."
    s "I know what to look for in the game files now..."
    s "...at least, I think so."
    s 2b "Just wait a second..."
    s 2c "What's this?"
    s "She's still missing part of her character..."
    s 2g "We're so close..."
    s "I think we have to make it for her."
    s 2h "This is...too much for me."
    s "I don't want to do this..."
    s "Besides, you have to know more about her than I do!"
    s "I know almost nothing except for the little details we found at Natsuki's house..."
    s "You must know more!"
    s 2k "I'm gonna leave this up to you..."
    menu:
        s "What kind of personality did she have?"
        "Carefree.":
            $ haruki_personality[0] = False
        "Loving.":
            $ haruki_personality[0] = True
        "Spiteful.":
            $ haruki_personality[0] = False
        "Remorseless.":
            $ haruki_personality[0] = False
        "Forgiving.":
            $ haruki_personality[0] = False
    s 2h "I hope you're right..."
    menu:
        s "What was her...favourite hobby?"
        "Acting.":
            $ haruki_personality[1] = True
        "Betting.":
            $ haruki_personality[1] = False
        "Sewing.":
            $ haruki_personality[1] = False
        "Baking.":
            $ haruki_personality[1] = False
        "Modelling.":
            $ haruki_personality[1] = False
    s 2k "Now..."
    s "This next one is...pretty sensitive."
    s "So please be careful."
    menu:
        s "Does she still love Yasuhiro?"
        "Not at all.":
            $ haruki_personality[2] = False
        "Still in love.":
            $ haruki_personality[2] = True
    if haruki_personality[0] and haruki_personality[1] and haruki_personality[2]:
        $ normal_haruki = True
        $ insert_momsuki_character_normal()
    else:
        $ insert_momsuki_character_broken()
    s 2d "Alright, that should do it."
    s "I'm not entirely sure if this will work with your choices...but it's our best bet, right?"
    s "It's one of the limitations of seeing the future...the decisions made by you are..."
    s 2k "Never mind."
    s "..."
    s "Are you wondering how Yasuhiro heard her voice?"
    s 2u "It's pretty sad..."
    s "It was the only thing of Haruki that I could find that was still 'whole'."
    s "I just played her voice through the phone..."
    s "She said \"I love you\"...I guess that's why he actually agreed to come."
    if check_whole_house:
        s 2k "He probably would have acted a lot different today if you didn't check all of Natsuki's house."
        s "When we saw everything that happened..."
        s "I felt...sorry for him."
        s 2g "And I'll be honest with you..."
        s "I changed him a little bit...I had to."
        s 2h "I didn't change who he was, or what he knows..."
        s "I just brought back that feeling of..."
        s 2t "...love."
    s "..."
    s 2d "Look, I know I can be a bit demanding sometimes..."
    s "If you hate me for it, then I can't blame you."
    s 2k "But I won't stop, not until everyone get their happy ending."
    s "Sorry, I've already taken up more of your time than I needed to."
    s "I'll unfreeze time..."
    s "The rest of them won't experience what the two of us just did."
    $ audio.t9b = "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    play music t9b fadein 0.5
    pause 0.5
    $ config.allow_skipping = True
    s 2q "Oh, it's our special guest!"
    s "Welcome! I wasn't expecting you to arrive so early~"
    show sayori zorder 2 at t51
    show dadsuki 1a zorder 3 at f54
    d "That voice..."
    d "You were the one on the phone!"
    d 1j "Where is she? I have to see her!"
    show sayori 2g zorder 3 at f51
    show dadsuki zorder 2 at t54
    s "Heeeeey, calm down."
    s "I don't know what you're talking about."
    s 2h "You're here to watch us perform our play and nothing more."
    show sayori zorder 2 at t51
    show dadsuki 1h zorder 3 at f54
    d "What?!"
    d "This wasn't part of the agreement..."
    show natsuki 2g zorder 3 at f53
    show dadsuki zorder 2 at t54
    n "Agreement?!"
    n "Sayori, what did you and my dad talk about?!"
    n 2f "Why is he the special guest and why did you keep that secret?!"
    show sayori 1d zorder 3 at f51
    show natsuki zorder 2 at t53
    s "Natsuki, I know you have a lot of questions."
    s "I'll answer them all later."
    s "Right now, we have a play to finish."
    s 1j "So if you don't mind, {i}Yasuhiro{/i}."
    show sayori zorder 2 at t51
    show yuri 2pq zorder 3 at f55
    y "Sayori...H-How do you know Natsuki's dad?"
    show dadsuki zorder 3 at f54
    show yuri zorder 2 at t55
    if check_whole_house:
        d 1k "I don't know who she is..."
        d "She just told me that I should be here today..."
        d "Already I can tell she's...something else."
    else:
        d 1g "That's a question I'd like answered too."
        d "Calling me out of nowhere like that..."
        d "What kind of person are you?"
    show sayori zorder 3 at f51
    show dadsuki zorder 2 at t54
    s 1j "I think she was asking me, not you."
    s 1k "Yuri, the truth is..."
    s 1l "...well, I know him because I wanted to help people."
    s "That's the truth."
    show sayori zorder 2 at t51
    show monika zorder 3 at f52
    if monika_type == 0:
        m 1e "You're certainly doing your best, Sayori."
        m "I know you need to keep some things secret, but maybe telling more would help us understand?"
    elif monika_type == 1:
        m 1n "Ahaha, is that really all you've got to say?"
    else:
        m 1h "While that's true, I can't help but feel you're hiding something from us."
    show sayori zorder 3 at f51
    show monika zorder 2 at t52
    s "W-What do you mean?"
    s "There's no other reason behind it."
    s 1q "I really do just want to help people..."
    show sayori zorder 2 at f51
    show dadsuki zorder 3 at f54
    d "So help me then."
    show dadsuki zorder 4 at t54
    "Sayori looks at him with a curious expression."
    show sayori zorder 3 at t43
    "She moves next to Yasuhiro and whispers something in his ear."
    show dadsuki 1l
    "The look on Yasuhiro's face shifts to one of shock."
    "He looks at Sayori as if caught completely by surprise as to what she just said."
    show monika zorder 2 at t51
    show natsuki zorder 2 at t52
    show sayori 1d zorder 3 at f53
    show dadsuki zorder 2 at d54
    s "I hope that explains everything."
    s "You don't have to say anthing."
    s "All you have to do is watch."
    show natsuki 1c zorder 3 at f52
    show sayori zorder 2 at t53
    n "Sayori?!"
    n "What did you say to him?"
    n 1h "I've never seen my dad so--"
    show natsuki zorder 2 at t52
    show sayori 1a zorder 3 at f53
    s "Oh, it was nothing really."
    s "You shouldn't worry about it, Natsuki."
    s "He's just here to watch us, so just pretend he isn't here."
    s 1d "Please, Yasuhiro, take a seat."
    show sayori zorder 2 at t53
    show dadsuki zorder 3 at f54
    if check_whole_house:
        d 1k "..."
    else:
        d 1e "Fine."
    show dadsuki at thide
    hide dadsuki
    show monika zorder 2 at t41
    show natsuki zorder 2 at t42
    show sayori zorder 2 at t43
    show yuri zorder 2 at t44
    "With a defeated look on his face, he grabs a seat from a pile of chairs and places it in front of our performing area."
    if check_whole_house:
        "He looks down and momentarily covers his face with his hands before looking up at the stage."
    else:
        "He crosses his arms and starts tapping his foot impatiently."
    show sayori 4q zorder 3 at f43
    play music t5 fadeout 2.0
    s "Alright, everbody!"
    s "It's time to continue with the play!"
    show natsuki 1m zorder 3 at f42
    show sayori zorder 2 at t43
    n "Sayori..."
    "Natsuki whispers to the group."
    n "You can't seriously expect me to do this in front of my dad!"
    n 1q "This is way too weird!"
    show natsuki zorder 2 at t42
    show sayori 3h zorder 3 at f43
    s "Natsuki, you have to do this."
    s 3d "Just pretend he isn't there, it'll be fine."
    show natsuki 3r zorder 3 at f42
    show sayori zorder 2 at t43
    n "But--"
    show monika zorder 3 at f41
    show natsuki zorder 2 at t42
    if monika_type == 0:
        m 2e "I think Sayori knows what she's doing, Natsuki."
        m "You should listen to her."
    else:
        m 2a "Maybe you should listen to what Sayori says, Natsuki."
        m "It might be important for later."
    show monika zorder 2 at t41
    show yuri 2ps zorder 3 at f44
    y "I agree with Monika."
    show natsuki 3o zorder 3 at f42
    show yuri zorder 2 at t44
    n "Y-You what?!"
    n "Yuri, I expected you out of everyone to be uncomfortable doing this!"
    show natsuki zorder 2 at t42
    show yuri 2pf zorder 3 at f44
    y "I think it's a good opportunity for me to practice speaking in front of other people."
    y "I know it might be different for you since he's your father..."
    y "But Sayori invited him here, and he's watching us."
    y 2ph "It's not like we can do anything about it now."
    show natsuki zorder 3 at f42
    show yuri zorder 2 at t44
    n 3o "Uuuuuu...!"
    n 3r "T-There's nothing I can do to change anyone's mind, is there?"
    n "Fine, fine. I'll just try to ignore him..."
    n 3s "I suppose there really is no use in doing anything that I want, is there?"
    show natsuki zorder 2 at t42
    show sayori 3d zorder 3 at f43
    s "Natsuki, it's really not like that..."
    s "I promise, you'll get what you want after today."
    s "So please, just finish this off, okay?"
    "Natsuki doesn't look convinced but nods her head."
    s 3a "Great, so where were we?"
    s "Oh, right!"
    $ currentpos = get_pos()
    $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_natsuki.ogg"
    stop music fadeout 1.0
    $ renpy.music.play(audio.t5b, channel="music_poem", fadein=1.0, tight=True)
    "Sayori quickly changes her whole composure and expression."
    s 4d "You're an important part of the team, Nozomi."
    s 4r "You all are."
    s 4d "So really...all you have to do is ask us for help."
    s "You know we'd want nothing more than for you to be happy."
    show monika 1h zorder 3 at f41
    show sayori zorder 2 at t43
    m "Those are inspiring words, Saika."
    m 1i "I just hope you're able to back them up, otherwise all you've given is false hope."
    m 1o "And what follows false hope, is an even greater despair."
    show monika zorder 2 at t41
    show sayori 2f zorder 3 at f43
    s "Martha, we always have to hope for the best."
    s "It's the best outlook to life."
    show monika 1h zorder 3 at f41
    show sayori zorder 2 at t43
    m "I'm not that naive anymore, Saika."
    m 1i "I've been hoping for the best most of my life, but I've learned to expect the worst."
    m "So forgive me if I don't see eye to eye with you on some things."
    m 1o "It's just my view of this harsh reality, where the perfect outcome is impossible..."
    "Monika didn't even need to read off the script when she read her last couple of lines."
    "She said it with such meaning too, it's almost like she's a natural at acting."
    m 1m "But it doesn't matter what I think anyway."
    m 1e "I've already agreed to help you with your plan first."
    show monika zorder 2 at t41
    mc "I know this isn't your ideal way of doing things."
    mc "It isn't the ideal way of doing things at all, really."
    mc "But Nozomi deserves the best outcome."
    mc "I'm going to try my best to make sure of it, even if it kills me."
    show yuri 2pb zorder 3 at f44
    y "Ah, Maemi."
    y "Your dedication to the Ronin is something to admire..."
    y "...though don't you think that's a little too far?"
    show yuri zorder 2 at t44
    mc "I'd go to any lengths for the Ronin."
    mc "But I suppose you're right, dying would be a very bleak outcome."
    mc "I just hope my power awakens soon."
    mc "It's not like I can just snap my fingers and activate it, can I?"
    "My character snaps his fingers at this point and finds himself the only person moving."
    mc "Uh...what's going on?"
    mc "Is this a time stop?"
    mc "Saika? You're frozen too?"
    mc "But she's a shinobi like me."
    mc "So why...?"
    mc "Oh no..."
    mc "Did I do this?"
    mc "How do I stop it?"
    "I pace around the gym, suprisingly the others are playing along as if they were frozen too."
    "I think I even caught Yasuhiro freeze for a little bit."
    mc "This is bad...this is bad...this is--"
    show sayori 2m zorder 3 at f43
    s "E-Eh? When did you get over there Maemi?"
    s "You were in front of a me just a second ago."
    show monika 1c zorder 3 at f41
    show sayori zorder 2 at t43
    m "Hmm..."
    m "He performed a time stop, didn't he?"
    m 2d "Quite suprising."
    m "Am I right?"
    show monika zorder 2 at t41
    mc "I-I think you're right."
    mc "But--"
    show sayori 4q zorder 3 at f43
    s "That's great! We can help Nozomi now!"
    s "We should do it now because--"
    show sayori zorder 2 at t43
    mc "Saikia, I--"
    show sayori 4r zorder 3 at f43
    s "The sooner we help her, the sooner our team is back in top shape!"
    s "Ehehe, I'm so excited!"
    show sayori zorder 2 at t43
    show yuri 2pq zorder 3 at f44
    y "I think you're missing an important detail here, Saika."
    y "You were surprised when he appeared somewhere else."
    show sayori 4a zorder 3 at f43
    show yuri zorder 2 at t44
    s "So...?"
    show natsuki 2g zorder 3 at f42
    show sayori zorder 2 at t43
    n "Saika, don't you get what Yoshiko is trying to say?"
    n "Maemi froze you in his time stop too!"
    n 2h "He's..."
    show natsuki zorder 2 at t42
    show sayori 3e zorder 3 at f43
    s "You're right..."
    s 3l "Why did that--"
    show sayori zorder 2 at t43
    $ mo_name = "???"
    "A sound echoes from the entrance of the gym."
    "There's another person standing there."
    "Sayori said special guest, she didn't say anything about {i}guests{/i}."
    "I look towards Yasuhiro and immediately he gets up from his seat."
    "Who is this person that has Yasuhiro so excited?"
    "Could it actually be Natsuki's mom?"
    "There's no way..."
    "...right?"
    show monika at thide
    hide monika
    show natsuki at thide
    hide natsuki
    show sayori at thide
    hide sayori
    hide yuri at thide
    hide yuri
    show momsuki 1a zorder 2 at t31
    if normal_haruki:
        mo "Um...what's going on here?"
        mo "Is this some sort of rehearsal?"
    else:
        mo "This looks like some sort of disaster."
        mo "I suppose that's to be expected."
    show dadsuki 1i zorder 3 at f33
    if check_whole_house:
        d "H-Haruki, you're actually here!"
        d 1k "I didn't think you'd come!"
        d "I--"
    else:
        d 1f "So she wasn't lying..."
        d "Haruki, I need to talk to you."
        d "There's a few things that I must--"
    $ mo_name = "Haruki"
    show natsuki 1m zorder 3 at f32
    show dadsuki zorder 2 at t33
    n "Mom?!"
    show natsuki at hf21
    "Natsuki runs over to Haruki and embraces her."
    n 1t "Mom, it's really you!"
    show momsuki zorder 3 at f31
    show natsuki zorder 2 at t32
    if normal_haruki:
        stop music_poem fadeout 2.0
        play music t9 fadein 2.0
        mo 1f "Natsuki? It's been so long..."
        mo "I'm surprised you still remember the appearance of your mother..."
        mo "My...how you've grown."
        mo "You're turning up to be a fine young lady."
        show momsuki zorder 2 at t31
        show natsuki 4t zorder 3 at f32
        n "W-Well, I had a good role model to look up to!"
        n "So it's only..."
        show natsuki 42h
        "Natsuki's voice fades, and tears begin to fall from her eyes."
        n "Why...?"
        n 42i "Why did you have to leave me and dad alone?"
        n "Why are you here now?!"
        n "Why--"
        show natsuki zorder 2 at t32
        show dadsuki zorder 3 at f33
        if check_whole_house:
            d 1i "Haruki..."
        else:
            d 1e "I need to speak with her."
        show momsuki 1i zorder 3 at f31
        show dadsuki zorder 2 at t33
        mo "Wait your turn, Yasuhiro."
        show dadsuki 1l
        "Yasuhiro looks suprised but reluctantly agrees."
        mo 1g "I'm sorry Natsuki..."
        mo "For everything."
        mo 1h "I know you might not be able to forgive me..."
        mo "I just left you in the middle of the night, without even saying goodbye."
        mo 1e "Some mother I am, right?"
        mo "The truth is..."
        mo "...it really hurt for me to leave."
        mo "The night that I left..."
        mo 1h "I thought about it for a long time."
        mo "I thought that you and your father would be happier without me."
        mo "But..."
        mo 1e "That didn't happen, did it?"
        mo "I made everything worse..."
        mo "I ruined both of your lives and my own."
        mo 1h "I heard about what Yasuhiro did, and I blamed myself for everything."
        mo "I even considered ending it all..."
        show momsuki zorder 2 at t31
        show natsuki 1n zorder 3 at f32
        n "M-Mom! Don't talk like that!"
        show momsuki 1g zorder 3 at f31
        show natsuki zorder 2 at t32
        mo "No...I have to be honest with you."
        mo "I thought I ended my own life."
        mo "In fact, I'm almost certain I did..."
        mo "So how I ended up here is--"
        show momsuki zorder 2 at t41
        show natsuki zorder 2 at t42
        show dadsuki zorder 2 at t43
        show sayori 1a zorder 3 at f44
        s "Well!"
        s "It's nice to see you all together again."
        show momsuki 1a zorder 3 at f41
        show sayori zorder 2 at t44
        mo "Hmm...that voice."
        mo "It sounds really familiar somehow..."
        mo 1b "I know! It's the voice that was telling me to go here today..."
        show momsuki zorder 2 at t41
        show sayori 1l zorder 3 at f44
        s "Ehehe, I think you might be mistaken."
        s "I don't even know what you're doing here."
        s 1d "It is a pretty strange coincidence that you came here the same time that Yasuhiro did though!"
        show momsuki 1f zorder 3 at f41
        show sayori zorder 2 at t44
        mo "Very strange indeed..."
        show momsuki zorder 2 at t41
        if check_whole_house:
            show dadsuki 1i zorder 3 at f43
            d "Haruki..."
            d "I know you don't want to listen to me right now."
            d "But please, just hear me out."
            show momsuki 1i zorder 3 at f41
            show dadsuki zorder 2 at t43
            mo "Okay, okay! You have my attention."
            mo "Just make it quick."
            show momsuki zorder 2 at t41
            show dadsuki 1k zorder 3 at f43
            d "I'm sorry."
            d "Sorry for everything I've done."
            d "I know it was my fault that you left."
            d "I took everything I had for granted."
            d 1o "Everything."
            d "I didn't realize that I lost a part of myself until it was far too late."
            d 1k "But now..."
            d "I feel so different...it's almost terrifying."
            show momsuki 1h zorder 3 at f41
            show dadsuki zorder 2 at t43
            mo "Get to the point, Yasuhiro."
            show momsuki zorder 2 at t41
            show dadsuki 1j zorder 3 at f43
            d "I guess what I'm trying to say is..."
            d "Will you come back...?"
            show dadsuki zorder 2 at t43
            show dadsuki 1k zorder 2 at s43
            "Yasuhiro looks down as if afraid to meet Haruki's gaze."
            show momsuki zorder 2 at t51
            show natsuki zorder 2 at t52
            show dadsuki zorder 2 at t53
            show sayori zorder 2 at t54
            show monika 1e zorder 3 at f55
            if monika_type == 0:
                m "Ah...not to interrupt..."
                m "But should we really be here for this, Sayori?"
                m "This seems like a private matter."
            else:
                m "This doesn't really seem like something we should be hearing."
                m "Do you want us to leave?"
            show momsuki 1f zorder 3 at f51
            show monika zorder 2 at t55
            mo "No, do stay."
            mo "You've heard this much. You leaving now would serve no point."
            mo 1d "Listen well, Yasuhiro."
            mo 1i "What you've done to our little girl is inexcusable."
            mo "I mean you turned the room of our portrait into..."
            mo "...you know."
            mo 1e "But seeing you like this..."
            mo "It almost makes me think you've actually learned your lesson."
            mo "So..."
            mo 1g "I'm going to ask our daughter."
            mo "Natsuki?"
            show momsuki zorder 2 at t51
            show natsuki 5h zorder 3 at f52
            n "Y-Yeah...?"
            show momsuki  zorder 3 at f51
            show natsuki zorder 2 at t52
            mo "What do you think?"
            mo 1h "You know he's made your life a living hell ever since I've left."
            mo "It wasn't hard to find that out from the rumors that were spreading."
            mo "Even after all that..."
            mo "...do you still love him?"
            show momsuki zorder 2 at t51
            show natsuki 5s zorder 3 at f52
            n "You're right about him putting me through a living hell."
            n "He hasn't treated me the best ever since you left..."
            n 5u "And I've only been coping because..."
            n "...because of my friends."
            n "But..."
            n "I really can't imagine a life without dad."
            n "Back when you were still together...he was..."
            n "...such a good person. I-I can't forget that part of him..."
            n 5i "S-So..."
            "With every word Natsuki says, it's like Yasuhiro looks more and more in pain."
            n 5r "Yes..."
            n "I still love him."
            show momsuki zorder 3 at f51
            show natsuki zorder 2 at t52
            mo "Hmm..."
            mo 1h "And what about you, Yasuhiro?"
            mo "What are your feelings towards our daughter?"
            show momsuki zorder 2 at t51
            show dadsuki zorder 3 at t53
            show dadsuki 1j zorder 3 at f53
            d "I...don't really know how to describe it."
            show momsuki 1e zorder 3 at f51
            show dadsuki zorder 2 at t53
            mo "If you have to describe it, then you're doing it wrong."
            mo "You should say what's coming from your heart."
            show momsuki zorder 2 at t51
            show dadsuki 1k zorder 3 at f53
            d "My heart...?"
            "Yasuhiro takes a deep breath."
            d "There's this sense of regret."
            d "Regret that I did the wrong things..."
            d 1o "Regret that I could have prevented all of this from happening..."
            d "And..."
            d 1m "...there's this warm feeling too."
            d "It's something I haven't felt for a long time."
            d 1n "It makes me feel like I could do anything for you..."
            d "...and for Natsuki."
            d "Despite it's warmth, it almost feels like...a scary feeling."
            d 1k "It's like if anyone hurt either of you..."
            d "...well, it would hurt me too..."
            show momsuki 1h zorder 3 at f51
            show dadsuki zorder 2 at t53
            mo "So...that's it, is it?"
            mo "..."
            mo 1g "Yasuhiro..."
            mo "I think that warrants a private discussion."
            show momsuki zorder 2 at t51
            show dadsuki  zorder 3 at f53
            d "Ah...I see."
            d "Well, no matter what happens..."
            d 1m "I'm glad I got to see your beautiful face again, Haruki."
            d "I'll understand if--"
            show momsuki 1f zorder 3 at f51
            show dadsuki zorder 2 at t53
            mo "Just..."
            mo "...follow me outside, okay?"
            mo "Excuse us for a moment."
            mo "Natsuki, be a dear and wait for us, okay?"
            show momsuki zorder 2 at t51
            show natsuki 5m zorder 3 at f52
            n "O-Okay..."
            show momsuki 1b zorder 3 at f51
            show natsuki zorder 2 at t52
            mo "I'll see you later, sweetheart."
            "She beams at Natsuki."
            mo 1g "Yasuhiro, let's go."
            mo "There's a lot of things we have to talk about..."
            show momsuki zorder 2 at t51
            show dadsuki 1p
            "Yasuhiro looks at Haruki and lets out a sad smile."
            show momsuki at lhide
            hide momsuki
            show dadsuki at lhide
            hide dadsuki
            show natsuki zorder 2 at t41
            show monika zorder 2 at t42
            show sayori 1d zorder 3 at f43
            s "Well..."
            s "That was certainly something."
            s "You and Yuri were pretty quiet during that whole thing."
            show yuri 2pq zorder 3 at f44
            y "S-Sorry..."
            y "Just that whole thing..."
            y "What happened just caught me by surprise."
            y 2pl "I don't think this is something I'm going to forget for a while."
            show yuri zorder 2 at t44
            mc "Yuri's right."
            mc "I'm just speechless at the whole thing."
            mc "It almost feels too surreal to be..."
            mc "...well, real."
            show sayori 2d zorder 3 at f43
            s "What about you, Natsuki?"
            s "Are you okay?"
            show natsuki 1m zorder 3 at f41
            show sayori zorder 2 at t43
            n "I..."
            n "I don't know."
            n 1n "I can't believe this is happening to me right now."
            n "Um..."
            n "I'm gonna need some time to think, okay?"
            show natsuki zorder 2 at t41
            show sayori zorder 3 at f43
            s "Of course!"
            s "Take all the time you need, Natsuki."
            show natsuki at lhide
            hide natsuki
            show sayori zorder 2 at t31
            show monika zorder 2 at t32
            show yuri zorder 2 at t33
            "Natsuki looks at us, as if not believing what just happened, then exits the gym through the door her parents didn't."
            show monika zorder 3 at f32
            if monika_type == 0:
                m 1m "I have to wonder..."
                m "...if something like this is still possible for me."
            elif monika_type == 1:
                m 1e "You do like getting the happy endings, don't you?"
            else:
                m 1a "That was...interesting."
            show sayori 1b zorder 3 at f31
            show monika zorder 2 at t32
            s "What do you mean?"
            show sayori zorder 2 at t31
            show monika 1l zorder 3 at f32
            m "Oh, nothing~"
            show sayori 1a  zorder 3 at f31
            show monika zorder 2 at t32
            s "If you say so..."
            s 1d "I don't know about you guys but I'm pretty tired after this whole day."
            s "So I think we should call the end of the meeting there."
            show sayori zorder 2 at t31
            show yuri 2pa zorder 3 at f33
            y "It does seem like an appropiate time to end the meeting."
            show monika zorder 3 at f32
            show yuri zorder 2 at t33
            if monika_type == 0:
                m 1e "I suppose I should get going then."
                m "See you all tomorrow."
            else:
                m 1a "So the day is finally over."
                m "I can't wait until tomorrow."
                m "Until then, goodbye."
            show monika at thide
            hide monika
            show sayori zorder 2 at t21
            show yuri zorder 2 at t22
            "Monika gives a final wave of goodbye before leaving the gym through the same door as Natsuki."
            show sayori 2d zorder 3 at f21
            s "This really is the best possible thing that could have happened, isn't it?"
            s "Thank you..."
            "Sayori smiles at me."
            show sayori zorder 2 at t21
            mc "Eh? What did I do?"
            show sayori zorder 3 at f21
            s "Everything..."
            s "Anyway, I have some things I have to do for tomorrow."
            s "See you later, [player] and Yuri."
            show sayori zorder 2 at t21
            mc "Alright, see you tomorrow."
            show sayori at thide
            hide sayori
            show yuri zorder 2 at t11
            "Sayori exits the gym, almost skipping."
            "She seems way too happy about this whole thing."
            $ ch12_outcome = 3
        else:
            show dadsuki 1h zorder 3 at hf43
            d "Haruki!"
            d "I've waited long enough."
            d "We have to talk, right now."
            show momsuki 1i zorder 3 at f41
            show dadsuki zorder 2 at t43
            mo "Okay, Yasuhiro."
            mo "You have my attention."
            mo "I better like what you have to say."
            show momsuki zorder 2 at t41
            show dadsuki 1g zorder 3 at f43
            d "We should go outside for this."
            d "Everyone else doesn't have to hear what I have to say."
            show momsuki zorder 3 at f41
            show dadsuki zorder 2 at t43
            mo "Whatever you have to say to me..."
            mo "Natsuki deserves to hear too."
            show momsuki zorder 2 at t41
            show dadsuki 1e zorder 3 at f43
            d "And what of the rest of them?"
            show momsuki 1h zorder 3 at f41
            show dadsuki zorder 2 at t43
            mo "I'm not liking what I'm hearing, Yasuhiro."
            mo "So say what you have to or I'm leaving."
            show momsuki zorder 2 at t41
            show dadsuki 1c zorder 3 at f43
            d "Fine."
            d "I need you to come back to me."
            d "I can't live properly without you."
            d "Life's been terrible ever since you left me."
            show momsuki 1e zorder 3 at f41
            show dadsuki zorder 2 at t43
            mo "And who's fault do you suppose that is?"
            mo "Have you ever considered that you made my life terrible, Yasuhiro?"
            show momsuki zorder 2 at t41
            show dadsuki 1a zorder 3 at f43
            d "..."
            d "I guess that is my fault."
            d "But you didn't have to leave me for that..."
            d "We could have--"
            show momsuki 1i zorder 3 at f41
            show dadsuki zorder 2 at t43
            mo "There you are again, talking only about yourself."
            mo "Have you forgotten about Natsuki?"
            mo "You're a selfish person, Yasuhiro."
            mo 1g "When I saw you here today, I thought that maybe..."
            mo "...{i}maybe{/i} you would have changed."
            mo 1h "I guess that's just wishful thinking, isn't it?"
            show momsuki zorder 2 at t41
            show natsuki 1h zorder 3 at f42
            n "Mom..."
            show momsuki 1h zorder 3 at f41
            show natsuki zorder 2 at t42
            mo "I know he's made your life a living hell, Natsuki."
            mo "It wasn't hard to believe what people were saying about your father..."
            mo "...and what he was doing to you..."
            show momsuki zorder 2 at t51
            show natsuki zorder 2 at t52
            show yasuhiro zorder 2 at t53
            show sayori zorder 2 at t54
            show monika 1e zorder 3 at f55
            if monika_type == 0:
                m "If I may say something..."
                m "This really shouldn't be for our ears."
                m "It seems like a private family matter."
            else:
                m "Excuse me, but I can't help but say that this has nothing to do with us."
                m "This is a family matter so it should really be a private conversation."
            show momsuki 1g zorder 3 at f51
            show monika zorder 2 at t55
            mo "It's too late for that now, isn't it?"
            mo "Besides...I want everyone here to witness what Yasuhiro has to say."
            mo "So, go on."
            show momsuki zorder 2 at t51
            show monika zorder 3 at f55
            if monika_type == 0 or monika_type == 1:
                m 1m "I see..."
                m "Then you'll excuse me for a moment."
            else:
                m 1h "Alright."
                m "Then I'll need something if this is continuing."
            show momsuki zorder 3 at f51
            show monika zorder 2 at t55
            show monika at lhide
            hide monika
            "Monika quickly leaves the gym."
            show momsuki 1f zorder 3 at f41
            show natsuki zorder 2 at t42
            show dadsuki zorder 2 at t43
            show sayori zorder 2 at t44
            mo "Of course..."
            mo "None of you should have to watch this if you don't want to..."
            mo "So leave now if you're feeling uncomfortable."
            show momsuki zorder 2 at t41
            "Suprisingly, no one else leaves."
            "I guess they're all as interested as I am to see how this ends."
            show dadsuki 1i zorder 3 at f43
            d "Sigh..."
            d "Look, I just want things to be back the way they were."
            d "The two--"
            d "The three of us, living together as a family again."
            d 1k "We can bake together..."
            d "We can look after Natsuki together."
            d "We can live a happy life...together."
            show momsuki 1h zorder 3 at f41
            show dadsuki zorder 2 at t43
            mo "I don't know if that's possible."
            mo "But...I'll give it a shot..."
            mo "...if Natsuki is willing."
            mo 1g "Natsuki, do you think I should give your father another chance?"
            mo "Think about it carefully, please."
            mo "The three of us can try to start again, if you want..."
            show momsuki zorder 2 at t41
            show natsuki 1k
            "Natsuki looks at her mother with innocent eyes."
            "She looks deep in thought."
            show natsuki 1m zorder 3 at f42
            n "Mom..."
            n "I really want things to go back to the way they were..."
            n 1q "From before you left."
            n "But..."
            n 1r "Dad has changed..."
            n "I wanted to stay with him because he was the only real family I had left and because I thought I still loved him..."
            n "...even though he did all these terrible things to me."
            n 1s "But seeing you again..."
            n "And hearing what [player] said to me before..."
            n "...made me realize..."
            show natsuki 1m
            "Natsuki pauses for a moment then stares at Yasuhiro."
            n "You aren't the dad I loved."
            n 1n "That person died when mom left..."
            n "And...this monster."
            n "He doesn't deserve a second chance."
            show natsuki zorder 2 at t42
            show dadsuki 1h zorder 3 at f43
            d "You little brat!"
            d "I should have taught you more discipline."
            d "When you get back to the house, you're--"
            show momsuki 1i zorder 3 at f41
            show dadsuki zorder 2 at t43
            mo "You're not going to the house, Yasuhiro."
            mo "That house is signed under my name."
            mo "Don't you remember that my parents gave it to me when they retired?"
            mo "Or have you forgotten that much about me?"
            mo "You're lucky I don't call the police right now."
            show momsuki zorder 2 at t41
            show dadsuki 1g zorder 3 at f43
            d "This..."
            d "This isn't fair."
            d 1h "I deserve better than this!"
            d "I deserve--"
            play sound "sfx/smack.ogg"
            pause 0.25
            show dadsuki 1h:
                1.3
                easeout_cubic 0.5 yoffset 300
            pause 1.55
            play sound fall
            pause 0.25
            hide dadsuki
            pause 0.25
            "Yasuhiro suddenly falls to the ground."
            show monika 1e zorder 3 at f43
            if monika_type == 0:
                m "Sorry about that."
                m "I figured it would come to this."
                m "It's better if he leaves quietly."
            else:
                m "Well, that's that."
                m "I was getting a little tired of hearing his voice."
            show monika zorder 2 at t43
            "Monika suddenly appears with a keyboard by her side."
            "She must have hit him on the head with it so hard that it knocked him out."
            "Everyone is surprised at what she did and the strength it must have taken to do that."
            show natsuki 1p zorder 3 at f42
            n "M-Monika?!"
            n "H-How did you--"
            n "W-Why would you--"
            n "Where did you even find that?!"
            show natsuki zorder 2 at t42
            "Monika simply smiles at Natsuki."
            show momsuki 1g zorder 3 at f41
            show natsuki zorder 2 at t42
            mo "Well..."
            mo "That's certainly one way to deal with him."
            mo 1e "I appreciate your help, uh..."
            show momsuki zorder 2 at t41
            show monika 1a zorder 3 at f43
            if monika_type == 0:
                m "It's Monika."
            elif monika_type == 1:
                m "The name's Monika."
            else:
                m "Mar--"
                m 1l "Monika."
            show momsuki 1f zorder 3 at f41
            show monika zorder 2 at t43
            mo "Right."
            mo "Thank you again for the help, Monika."
            mo 1g "I'm going to call help to get rid of Yasuhiro."
            mo "Natsuki, why don't you come with me for a minute?"
            mo "I'd like to speak with you..."
            mo "...in private this time."
            show momsuki zorder 2 at t41
            show natsuki 1c
            "Natsuki looks back at us."
            show sayori 1d zorder 3 at f44
            s "Go ahead!"
            s "You two really need to talk~"
            show natsuki 1q zorder 3 at f42
            show sayori zorder 2 at t44
            n "A-Alright..."
            n "I'll see you guys later..."
            show natsuki zorder 2 at t42
            show momsuki at lhide
            hide momsuki
            show natsuki at lhide
            hide natsuki
            show monika zorder 2 at t31
            show sayori 1a zorder 2 at f32
            "Natsuki waves goodbye, and her mother smiles at us before they both exit the gym."
            s "You two were pretty quiet throughout all of that."
            show sayori zorder 2 at t32
            show yuri 2pq zorder 3 at f33
            y "I was just a little astonished..."
            y "Both of Natsuki's parents meeting her today and it ending up like that..."
            y 2ps "Well...it's something I'll remember for a long time."
            show yuri zorder 2 at t33
            mc "Yeah, that whole thing just felt surreal."
            mc "The odds of both of Natsuki's parents being here..."
            mc "Especially since her mom left her in the middle of the night..."
            mc "I'm just speechless, really."
            show sayori 1d zorder 3 at f32
            s "It was a pretty weird thing to happen, right?"
            s 1l "Especally that whole keyboard thing with Monika!"
            s 1d "Anyway, there isn't really a point continuing without Natsuki."
            s "So you guys can go home now!"
            show monika zorder 3 at f31
            show sayori zorder 2 at t32
            if monika_type == 0:
                m 1m "{i}(An ending like this...){/i}"
                m "{i}(Even if it wasn't ideal...){/i}"
                m "{i}(Could it still be possible for me?){/i}"
            elif monika_type == 1:
                m 1e "{i}(You were always one to go for endings like this...){/i}"
                m "{i}(I guess I shouldn't be surprised.){/i}"
            else:
                m 1j "{i}(Ugh, finally...){/i}"
            show monika zorder 2 at t31
            show sayori 1c zorder 3 at f32
            s "What was that?"
            show monika 3l zorder 3 at f31
            show sayori zorder 2 at t32
            m "Nothing~"
            if monika_type == 0:
                m 3e "I'm ready to head home now."
                m "I'll see you all tomorrow."
            else:
                m 3b "I'm just glad today is finally over."
                m "I can't wait for tomorrow."
            show monika at thide
            hide monika
            show sayori zorder 2 at t21
            show yuri zorder 2 at t22
            "Monika exits the gym through the door that Natsuki and her mom didn't go through."
            show sayori 1a zorder 3 at f21
            s "You two should probably go as well."
            s "I'm just gonna stay here for a while to make sure Yasuhiro is properly {i}taken care{/i} of."
            s 1d "I need to check a few things before that though, so I'll see you both tomorrow~"
            show sayori at thide
            hide sayori
            show yuri zorder 2 at t11
            "Sayori looks around for a couple of seconds before heading into the gym's storage shed."
            $ ch12_outcome = 2
    else:
        mo 1i "Let go of me."
        show momsuki zorder 2 at t31
        show natsuki 1m zorder 3 at f32
        stop music_poem fadeout 2.0
        n "W-What?"
        n "D-Don't you know who I am?"
        show momsuki zorder 3 at f31
        show natsuki zorder 2 at t32
        mo "I know exactly who you are, {i}Natsuki{/i}."
        mo "And I couldn't care less."
        mo "I'm not here for you."
        mo "The day I left you and Yasuhiro was the happiest day of my life, I want you to know that."
        show momsuki zorder 2 at t31
        show natsuki 12h zorder 3 at f32
        n "M-Mom..."
        n "W-Why are you...?"
        show natsuki at lhide
        hide natsuki
        "Natsuki runs away from the gym, with tears in her eyes."
        show dadsuki 1l zorder 3 at f33
        if check_whole_house:
            d "Haruki...?"
            d "What's wrong with you?"
            d "..."
            d 1k "You aren't Haruki, are you?"
            d "Y-You look like her but..."
        else:
            d 1f "That was cold."
            d "Especially coming from you."
            d "You were the one who knew how to console her when she needed it."
            d 1c "That was..."
            d "...definitely not that."
        show momsuki zorder 2 at t41
        show natsuki zorder 2 at t42
        show dadsuki zorder 2 at t43
        show sayori 1f zorder 3 at f44
        s "Yasuhiro's right..."
        s "This is all wrong."
        s "You aren't the real Haruki."
        show momsuki 1d zorder 3 at f41
        show sayori zorder 2 at t44
        mo "And what would you know about me, girl?"
        mo "Come to think of it, I recognize your voice!"
        mo 1a "There's like an echo in my mind that sounds just like you..."
        mo "And it told me to come here."
        mo 1b "Now that it's gone, I can be on my way."
        show momsuki zorder 2 at t41
        show dadsuki 1i zorder 3 at f43
        d "You're not staying?"
        d "You came all this way just to drive your own daughter away?"
        show momsuki 1i zorder 3 at f41
        show dadsuki zorder 2 at t43
        mo "Ahaha, do you think I don't know what you've done to her?"
        mo "You've ruined her life, even more than I have."
        mo "I've kept up with your deeds, Yasuhiro so don't lecture me about driving my daughter away."
        mo "Why don't you just--"
        show momsuki zorder 2 at t41
        show sayori 1g  zorder 3 at f44
        s "No..."
        s "We must have messed up Haruki's personality..."
        show momsuki zorder 3 at f41
        show sayori zorder 2 at t44
        mo "Who in the world are you talking to?"
        mo 1d "And what do you mean you messed up my personality?"
        mo 1c "I've never been better."
        mo "Now that I'm free from my pathetic daughter and my sorry excuse for a husband..."
        mo 1b "I can finally do what I've wanted to do with my life."
        show momsuki zorder 2 at t41
        show sayori 1k zorder 3 at f44
        s "..."
        $ config.skipping = False
        $ config.allow_skipping = False
        s "I don't want to mess it up even more."
        s 1f "It's your choice from here..."
        s "If you continue, then I'll eat a strawberry from before you put her character file in."
        s "If you want to try to reassemble her again for Natsuki's happy ending..."
        s 1h "Well, anything is better than what's happening right now."
        s "I hope you didn't do this intentionally..."
        s 1k "I can't really know that, can I?"
        s "I suppose I'll just give you the benefit of the doubt."
        s 1h "I'm going to eat a strawberry now."
        s "See you."
        $ ch12_haruki_tried = True
        $ delete_character("haruki")
        $ _history_list = []
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        show sayori 2a zorder 3 at f51
        if monika_type == 0:
            show monika 1e zorder 2 at t52
        elif monika_type == 1:
            show monika 1l zorder 2 at t52
        else:
            show monika 1h zorder 2 at t52
        show natsuki 4n zorder 2 at t53
        if check_whole_house:
            show dadsuki 1i zorder 2 at t54
        else:
            show dadsuki 1e zorder 2 at t54
        show yuri 3ph zorder 2 at t55
        play music t9 fadein 0.5
        pause 0.5
        stop sound
        hide screen tear
        window show(None)
        $ config.allow_skipping = True
        jump ch12_strawberry5
    y 2pa "That just leaves the two of us."
    y "I hope that wasn't too weird for you."
    y 2ph "Natsuki seeing both her parents like that..."
    mc "It's not your fault that was weird."
    mc "Besides, I'm happy for her."
    mc "She's going to be okay, I just know it."
    y "I'm getting that feeling too..."
    y 2pf "Anyway..."
    if visited_yuri_hospital:
        y 3pb "Ready to walk home, [player]?"
        mc "Yeah, let's go."
    else:
        y 3ps "I suppose I'll see you tomorrow as well."
        mc "You can count on it, Yuri."
    return

label ch12_harukinoplace:
    s "But..."
    s 2k "Could this be the right way to do it?"
    s "What would have happened if you actually made her a character file?"
    s "Would it really have been her?"
    s "..."
    s 2f "Maybe this is the right thing to do..."
    s 2g "I guess we'll never really know until we go through with it, right?"
    if check_whole_house:
        s "I tried something..."
        s 2k "It might not have been the most ethical thing I've done..."
        s "But I was hoping that you would create the character file."
        s 2d "I guess it's still better in the end for Natsuki, isn't it?"
    else:
        s 2d "I'm a bit relieved."
        s "I was going to try something with Yasuhiro but decided against it."
        s "It would have been wrong, changing him like that."
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() != player.lower():
            s "Alright, [currentuser]..."
            s "We'll do it your way."
    $ config.allow_skipping = True
    $ audio.t9b = "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    play music t9b fadein 0.5
    pause 0.5
    label ch12_noharukicont:
    s 2q "It looks like our special guest has arrived!"
    s "Welcome, I hope you have a great time here!"
    show sayori zorder 2 at t51
    show dadsuki 1a zorder 3 at f54
    d "That voice..."
    d "You were the one on the phone!"
    d 1j "Where is she? I have to see her!"
    show sayori 2n
    show dadsuki zorder 2 at t54
    "Sayori looks at Yasuhiro quizically."
    show sayori 2l zorder 3 at f51
    s "Um...where is who?"
    show sayori zorder 2 at t51
    show dadsuki 1e zorder 3 at f54
    d "You know exactly who I'm talking about."
    d "I didn't come all this way for nothing."
    if check_whole_house:
        d 1i "So please...tell me where she is."
    else:
        d 1h "So I demand you tell me where she is, right now!"
    show natsuki 2f zorder 3 at f53
    show dadsuki zorder 2 at t54
    n "What is going on?!"
    n "Sayori, tell us what's happening!"
    show sayori 2d zorder 3 at f51
    show natsuki zorder 2 at t53
    s "Your guess is as good as mine, Natsuki."
    "Sayori turns her attention to Yasuhiro."
    s "I'm sorry, Yasuhiro."
    s "But I'm afraid I have no idea what you're talking about."
    s 2a "But now that you're here, why don't you stay and enjoy this little performance we have going on?"
    s "I'm sure it will be really fun!"
    show sayori zorder 2 at t51
    show dadsuki zorder 3 at f54
    if check_whole_house:
        d 1k "But..."
        d "I just wanted..."
        d "...to see her again."
    else:
        d 1e "Are you playing me for a fool?"
        d "It was definitely your voice I heard on the phone after Haruki's."
    show sayori 1c zorder 3 at f51
    show dadsuki zorder 2 at t54
    s "Well, what did the phone on the voice say?"
    s "Was she going to meet you in here?"
    show sayori zorder 2 at t51
    show dadsuki zorder 3 at f54
    if check_whole_house:
        d 1i "But it was your voice, you should know!"
        "Yasuhiro looks at Sayori sadly."
        d "I guess I have no choice."
        d "I have to wait...if I ever want to see her again."
    else:
        d 1h "This is stupid."
        "Yasuhiro gives Sayori a malicious look."
        d "But, if I must..."
        d "I'll wait here."
    show sayori 4q zorder 3 at f51
    show dadsuki zorder 2 at t54
    s "Great! Why don't you grab a seat?"
    s "You know, it's an interesting choice to meet...I mean who would want to meet at a school's gym?"
    show sayori zorder 2 at t51
    show dadsuki 1c zorder 3 at f54
    d "The waiting is going to be the worst...isn't it?"
    d "This wasn't part of the agreement..."
    show natsuki 2g zorder 3 at f53
    show dadsuki zorder 2 at t54
    n "Agreement?!"
    n "Sayori, what did you and my dad talk about?!"
    n 2f "Why is he the special guest and why did you keep that secret?!"
    show sayori 1d zorder 3 at f51
    show natsuki zorder 2 at t53
    s "Natsuki, I know you have a lot of questions."
    s "I'll answer them all later."
    s "Right now, we have a play to finish."
    s 1j "So if you don't mind, {i}Yasuhiro{/i}."
    show sayori zorder 2 at t51
    show yuri 2pq zorder 3 at f55
    y "Sayori...H-How do you know Natsuki's dad?"
    show dadsuki zorder 3 at f54
    show yuri zorder 2 at t55
    if check_whole_house:
        d 1k "I don't know who she is..."
        d "She just told me that I should be here today..."
        d "Already I can tell she's...something else."
    else:
        d 1g "That's a question I'd like answered too."
        d "Calling me out of nowhere like that..."
        d "What kind of person are you?"
    show sayori zorder 3 at f51
    show dadsuki zorder 2 at t54
    s 1j "I think she was asking me, not you."
    s 1k "Yuri, the truth is..."
    s 1l "...well, I know him because I wanted to help people."
    s "That's the truth."
    show sayori zorder 2 at t51
    show monika zorder 3 at f52
    if monika_type == 0:
        m 1e "You're certainly doing your best, Sayori."
        m "I know you need to keep some things secret, but maybe telling more would help us understand?"
    elif monika_type == 1:
        m 1n "Ahaha, is that really all you've got to say?"
    else:
        m 1h "While that's true, I can't help but feel you're hiding something from us."
    show sayori zorder 3 at f51
    show monika zorder 2 at t52
    s "W-What do you mean?"
    s "There's no other reason behind it."
    s 1q "I really do just want to help people..."
    show sayori zorder 2 at f51
    show dadsuki zorder 3 at f54
    d "So help me then."
    show dadsuki zorder 4 at t54
    "Sayori looks at him with a curious expression."
    show sayori zorder 3 at t43
    "She moves next to Yasuhiro and whispers something in his ear."
    show dadsuki 1l
    "The look on Yasuhiro's face shifts to one of shock."
    "He looks at Sayori as if caught completely by surprise as to what she just said."
    show monika zorder 2 at t51
    show natsuki zorder 2 at t52
    show sayori 1d zorder 3 at f53
    show dadsuki zorder 2 at d54
    s "I hope that explains everything."
    s "You don't have to say anthing."
    s "All you have to do is watch."
    show natsuki 1c zorder 3 at f52
    show sayori zorder 2 at t53
    n "Sayori?!"
    n "What did you say to him?"
    n 1h "I've never seen my dad so--"
    show natsuki zorder 2 at t52
    show sayori 1a zorder 3 at f53
    s "Oh, it was nothing really."
    s "You shouldn't worry about it, Natsuki."
    s "He's just here to watch us, so just pretend he isn't here."
    s 1d "Please, Yasuhiro, take a seat."
    show sayori zorder 2 at t53
    show dadsuki zorder 3 at f54
    if check_whole_house:
        d 1k "..."
    else:
        d 1e "Fine."
    show dadsuki at thide
    hide dadsuki
    show monika zorder 2 at t41
    show natsuki zorder 2 at t42
    show sayori zorder 2 at t43
    show yuri zorder 2 at t44
    "With a defeated look on his face, he grabs a seat from a pile of chairs and places it in front of our performing area."
    if check_whole_house:
        "He looks down and momentarily covers his face with his hands before looking up at the stage."
    else:
        "He crosses his arms and starts tapping his foot impatiently."
    show sayori 4q zorder 3 at f43
    play music t5 fadeout 2.0
    s "Alright, everbody!"
    s "It's time to continue with the play!"
    show natsuki 1m zorder 3 at f42
    show sayori zorder 2 at t43
    n "Sayori..."
    "Natsuki whispers to the group."
    n "You can't seriously expect me to do this in front of my dad!"
    n 1q "This is way too weird!"
    show natsuki zorder 2 at t42
    show sayori 3h zorder 3 at f43
    s "Natsuki, you have to do this."
    s 3d "Just pretend he isn't there, it'll be fine."
    show natsuki 3r zorder 3 at f42
    show sayori zorder 2 at t43
    n "But--"
    show monika zorder 3 at f41
    show natsuki zorder 2 at t42
    if monika_type == 0:
        m 2e "I think Sayori knows what she's doing, Natsuki."
        m "You should listen to her."
    else:
        m 2a "Maybe you should listen to what Sayori says, Natsuki."
        m "It might be important for later."
    show monika zorder 2 at t41
    show yuri 2ps zorder 3 at f44
    y "I agree with Monika."
    show natsuki 3o zorder 3 at f42
    show yuri zorder 2 at t44
    n "Y-You what?!"
    n "Yuri, I expected you out of everyone to be uncomfortable doing this!"
    show natsuki zorder 2 at t42
    show yuri 2pf zorder 3 at f44
    y "I think it's a good opportunity for me to practice speaking in front of other people."
    y "I know it might be different for you since he's your father..."
    y "But Sayori invited him here, and he's watching us."
    y 2ph "It's not like we can do anything about it now."
    show natsuki zorder 3 at f42
    show yuri zorder 2 at t44
    n 3o "Uuuuuu...!"
    n 3r "T-There's nothing I can do to change anyone's mind, is there?"
    n "Fine, fine. I'll just try to ignore him..."
    n 3s "I suppose there really is no use in doing anything that I want, is there?"
    show natsuki zorder 2 at t42
    show sayori 3d zorder 3 at f43
    s "Natsuki, it's really not like that..."
    s "I promise, you'll get what you want after today."
    s "So please, just finish this off, okay?"
    "Natsuki doesn't look convinced but nods her head."
    s 3a "Great, so where were we?"
    s "Oh, right!"
    $ currentpos = get_pos()
    $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_natsuki.ogg"
    stop music fadeout 1.0
    $ renpy.music.play(audio.t5b, channel="music_poem", fadein=1.0, tight=True)
    "Sayori quickly changes her whole composure and expression."
    s 4d "You're an important part of the team, Nozomi."
    s 4r "You all are."
    s 4d "So really...all you have to do is ask us for help."
    s "You know we'd want nothing more than for you to be happy."
    show monika 1h zorder 3 at f41
    show sayori zorder 2 at t43
    m "Those are inspiring words, Saika."
    m 1i "I just hope you're able to back them up, otherwise all you've given is false hope."
    m 1o "And what follows false hope, is an even greater despair."
    show monika zorder 2 at t41
    show sayori 2f zorder 3 at f43
    s "Martha, we always have to hope for the best."
    s "It's the best outlook to life."
    show monika 1h zorder 3 at f41
    show sayori zorder 2 at t43
    m "I'm not that naive anymore, Saika."
    m 1i "I've been hoping for the best most of my life, but I've learned to expect the worst."
    m "So forgive me if I don't see eye to eye with you on some things."
    m 1o "It's just my view of this harsh reality, where the perfect outcome is impossible..."
    "Monika didn't even need to read off the script when she read her last couple of lines."
    "She said it with such meaning too, it's almost like she's a natural at acting."
    m 1m "But it doesn't matter what I think anyway."
    m 1e "I've already agreed to help you with your plan first."
    show monika zorder 2 at t41
    mc "I know this isn't your ideal way of doing things."
    mc "It isn't the ideal way of doing things at all, really."
    mc "But Nozomi deserves the best outcome."
    mc "I'm going to try my best to make sure of it, even if it kills me."
    show yuri 2pb zorder 3 at f44
    y "Ah, Maemi."
    y "Your dedication to the Ronin is something to admire..."
    y "...though don't you think that's a little too far?"
    show yuri zorder 2 at t44
    mc "I'd go to any lengths for the Ronin."
    mc "But I suppose you're right, dying would be a very bleak outcome."
    mc "I just hope my power awakens soon."
    mc "It's not like I can just snap my fingers and activate it, can I?"
    "My character snaps his fingers at this point and finds himself the only person moving."
    mc "Uh...what's going on?"
    mc "Is this a time stop?"
    mc "Saika? You're frozen too?"
    mc "But she's a shinobi like me."
    mc "So why...?"
    mc "Oh no..."
    mc "Did I do this?"
    mc "How do I stop it?"
    "I pace around the gym, suprisingly the others are playing along as if they were frozen too."
    "I think I even caught Yasuhiro freeze for a little bit."
    mc "This is bad...this is bad...this is--"
    show sayori 2m zorder 3 at f43
    s "E-Eh? When did you get over there Maemi?"
    s "You were in front of a me just a second ago."
    show monika 1c zorder 3 at f41
    show sayori zorder 2 at t43
    m "Hmm..."
    m "He performed a time stop, didn't he?"
    m 2d "Quite suprising."
    m "Am I right?"
    show monika zorder 2 at t41
    mc "I-I think you're right."
    mc "But--"
    show sayori 4q zorder 3 at f43
    s "That's great! We can help Nozomi now!"
    s "We should do it now because--"
    show sayori zorder 2 at t43
    mc "Saikia, I--"
    show sayori 4r zorder 3 at f43
    s "The sooner we help her, the sooner our team is back in top shape!"
    s "Ehehe, I'm so excited!"
    show sayori zorder 2 at t43
    show yuri 2pq zorder 3 at f44
    y "I think you're missing an important detail here, Saika."
    y "You were surprised when he appeared somewhere else."
    show sayori 4a zorder 3 at f43
    show yuri zorder 2 at t44
    s "So...?"
    show natsuki 2g zorder 3 at f42
    show sayori zorder 2 at t43
    n "Saika, don't you get what Yoshiko is trying to say?"
    n "Maemi froze you in his time stop too!"
    n 2h "He's..."
    show natsuki zorder 2 at t42
    show sayori 3e zorder 3 at f43
    s "You're right..."
    s 3l "Why did that escape my mind?"
    show sayori zorder 2 at t43
    show yuri 3ps zorder 3 at f44
    y "You do tend to get a bit excited..."
    show sayori 3q zorder 3 at f43
    show yuri zorder 2 at t44
    s "Ehehe, you're right..."
    s 3r "That's really weird, isn't it?"
    s "I thought I would be immune to time stops since I'm a shinobi and everything."
    show monika 1q zorder 3 at f41
    show sayori zorder 2 at t43
    m "That's an incredibly powerful ability you seem to have developed, Maemi."
    m "The ability to stop people who can manipulate time."
    m 2e "Well done, Maemi."
    m "Perhaps I have underestimated you."
    show monika zorder 2 at t41
    mc "That's great and everything. There's just one drawback."
    mc "I can't control it. I think I just froze you all accidentally..."
    mc "Then I panicked then you all unfroze."
    show monika 1h zorder 3 at f41
    m "Now that...could be a problem."
    m "You can't control your powers and you've got a dangerous ability."
    m 1i "I suddenly have a very different opinion of you, Maemi."
    m "We aren't safe around you."
    show monika zorder 2 at t41
    show sayori 1h zorder 3 at f43
    s "Calm down, Martha!"
    s "It's not like Maemi can help it."
    s 1i "Besides, I doubt he'd use his powers for evil."
    s 1k "That would just be absurd!"
    s "Even if he did, I would have sensed his ill intent a long time ago."
    show sayori zorder 2 at t43
    show yuri 2pe zorder 3 at f44
    y "But he didn't know he could stop shinobi with a time stop a long time ago..."
    y "Try sensing him for ill intent again, Saika."
    show sayori 2h zorder 3 at f43
    show yuri zorder 2 at t44
    s "No! No way!"
    s "There's no way Maemi would just betray us like that."
    show sayori zorder 2 at t43
    mc "I would never betray the Ronin..."
    mc "But if it makes you all feel safer, then..."
    show monika 3h zorder 3 at f41
    m "I agree with Yoshiko."
    m "Sensing his ill intent again would be the most appropiate thing to do right now."
    show monika zorder 2 at t41
    show sayori 1j zorder 3 at f43
    s "Why are you both so suspicious towards Maemi now that he's activated his powers?"
    s "He's done nothing but help ever since he's joined!"
    s "I trust him with my life."
    show natsuki 1m zorder 3 at f42
    show sayori zorder 2 at t43
    n "This is all my fault, isn't it?"
    n 1n "If I just dealt with my father earlier, then..."
    "Yasuhiro's attention suddenly shifts from watching the door of the gym to Natsuki."
    "It's as if her saying 'father' made him pay closer attention to what's going on."
    n "...we wouldn't even have to talk about this."
    show natsuki zorder 2 at t42
    show sayori 1d zorder 3 at f43
    s "Nozomi, that's not true at all."
    s "Maemi would have had to learn to use his powers sooner or later."
    s "And we'd be having this exact same conversation."
    show natsuki 1k zorder 3 at f42
    show sayori zorder 2 at t43
    n "But..."
    show natsuki 1o
    "Natsuki looks slightly to the right and meets Yasuhiro's gaze."
    n "B-B-B...!"
    "She suddenly freezes in place. It's as if she's petrified."
    show monika zorder 3 at f41
    show natsuki zorder 2 at t42
    if monika_type == 0:
        m 1f "Natsuki?"
        m "Is something wrong?"
    else:
        m 1c "What's happening?"
        m "Why did Natsuki stop talking?"
    show monika zorder 2 at t41
    show sayori 1c zorder 3 at f43
    s "I think she's a little nervous."
    s "She must have accidentally looked at her dad."
    s "Natsuki!"
    "Sayori starts waving her hands in front of Natsuki's face."
    "It doesn't seem to be doing anything."
    s 1h "I think she's too shocked to do anything..."
    s "What do we do...?"
    show sayori zorder 2 at t43
    "Yasuhiro suddenly gets up from his seat."
    show dadsuki 1c zorder 3 at f51
    show monika zorder 2 at t52
    show natsuki zorder 2 at t53
    show sayori zorder 2 at t54
    show yuri zorder 2 at t55
    if check_whole_house:
        d 1i "Natsuki..."
        d "You remind me of your mother when she first started acting."
        d "She was so nervous back then, like you right now."
        d 1k "You might be nervous because of different reasons."
        d "For Haruki.."
        d 1m "She had to perform in front of a large crowd of people in the theatre..."
        d "But you..."
        d 1k "You have to perform in front of me."
        show dadsuki zorder 2 at t51
        show sayori 1j zorder 3 at f54
        s "What point are you getting at here, Yasuhiro?"
        s "There's no--"
        show monika 1e zorder 3 at f52
        show sayori zorder 2 at t54
        if monika_type == 0:
            m "I think we should hear him out, Sayori."
            m "He seems...different."
        else:
            m "Let's hear him out."
            m "I'd like to hear what he has to say."
        show dadsuki 1b zorder 3 at f51
        show monika zorder 2 at t52
        d "Thank you..."
        stop music_poem fadeout 2.0
        play music t9 fadein 2.0
        d 1n "Listen, Natsuki."
        d "I know you have no reason to care about what I have to say."
        d "In fact, you probably don't want to listen to what I have to say."
        d 1k "You probably hate me for what I've done to you."
        d "I know it wasn't right."
        d "I know I've blamed you for all the bad things that have happened ever since..."
        d "...your mother left us."
        d "Ironic, I was the reason she left...wasn't I?"
        show dadsuki zorder 2 at t51
        show sayori 1i zorder 3 at f54
        s "Wow. I think she already knew all these things about you, Yasuhiro."
        s "So what exactly are you trying to say here?"
        show dadsuki 1l zorder 3 at f51
        show sayori zorder 2 at t54
        d "I guess what I'm trying to say is."
        d "I'm sorry, for everything."
        d 1m "Seeing you acting just then, it brought back memories of your mother."
        d "So...I'm going to tell you something."
        d "The same thing I said to her on the night of her first performance..."
        d 1l "Smile."
        show dadsuki zorder 2 at t51
        "Natsuki's expression eases a little bit."
        "She turns away from everyone and covers her face."
        "I hear a soft sound coming from her, almost like a whimper."
        show dadsuki 1n zorder 3 at f51
        d "Oh dear...I've made everything worse, haven't I?"
        d "I'm sorry."
        d "It's better if I just leave."
        show dadsuki zorder 2 at t51
        show yuri 2pi zorder 3 at f55
        y "I don't think that's true..."
        y "You got her to move again."
        y "I think she wants to be comforted."
        show dadsuki 1k zorder 3 at f51
        show yuri zorder 2 at t55
        d "Ah..."
        d "That was never my specialty."
        show dadsuki zorder 2 at t51
        show monika zorder 3 at f52
        if monika_type == 0:
            m 1f "You're trying to help your daughter, aren't you?"
            m "Are you really going to let something like that stop you?"
        else:
            m 1h "So you said all those words and you can't even back them up."
            m "Well done, Yasuhiro."
        show dadsuki 1l zorder 3 at f51
        show monika zorder 2 at t52
        d "..."
        d "You're right."
        d "Excuse me."
        show monika zorder 2 at t51
        show dadsuki zorder 2 at t52
        "Yasuhiro moves towards Natsuki."
        "She briefly turns and looks at him before turning away again."
        d 1k "Natsuki."
        d "You know I was never really good at this."
        d "But...here goes nothing."
        scene black with dissolve_cg
        "Yasuhiro pulls Natsuki into a tight embrace from behind."
        "She seems to be resisting his embrace a little bit."
        d "I've been a terrible person for so long, Natsuki."
        d "I haven't been a father..."
        d "I've been a monster."
        d "I used to be the person that would get you through the dark times."
        d "But lately I've been the person who would put you through the dark times."
        d "It's not something you can just forgive so easily."
        "Natsuki looks as if she is easing off her resistance."
        d "I don't deserve your forgiveness."
        d "I don't deserve your love."
        d "But you deserve mine."
        d "Why it's taken me thing long to realize it..."
        d "...I'll never know."
        d "So..."
        d "Please, go on."
        d "And smile, if not for me...for your mother. In hopes that that she is watching from wherever she is now."
        "Natsuki doesn't react."
        d "That's how it is...?"
        d "I guess I deserve this."
        d "Sorry for bothering you, Natsuki."
        "Yasuhiro tries to release his embrace but Natsuki holds him tight."
        d "...?"
        n "D-Dad..."
        "Tears stream from Natsuki's eyes."
        n "Y-You idiot...!"
        n "W-Why do you have to say those things...?"
        n "Y-You don't mean any of it!"
        d "I meant every word."
        "There's a moment of silence, with Natsuki and Yasuhiro just stuck in an embrace."
        "It seems to pass by really slowly, but the rest of us don't say anything."
        n "D-Dad..."
        n "I-I can't smile..."
        n "N-Not when I'm like this..."
        n "I..."
        n "I-I just want things to go back to how they were before..."
        n "When we were all together..."
        d "I want nothing more than that too..."
        d "I don't know if we can ever get back to that time."
        n "..."
        d "But...we can try, can't we?"
        n "Y-Yeah..."
        "Natsuki wipes her face as Yasuhiro releases his embrace."
        stop music fadeout 2.0
        scene bg gym
        show monika 1e zorder 2 at i51
        show dadsuki 1m zorder 2 at i52
        show natsuki 1u zorder 2 at i53
        show sayori 1t zorder 2 at i54
        show yuri 2ps zorder 2 at i55
        with dissolve_cg
        show sayori zorder 3 at f54
        play music t8 fadein 1.0
        s "This..."
        s "I wasn't expecting this to happen."
        s "But..."
        s "I guess it all worked out!"
        show natsuki zorder 3 at f53
        show sayori zorder 2 at t54
        n "L-Listen, Sayori..."
        "Natsuki tries her best to speak through her tears."
        n 1w "I-I don't know what was on your mind when you invited my dad here."
        n 1x "Sometimes I think you don't know what you're doing..."
        n 1n "But..."
        n "...thank you."
        show natsuki zorder 2 at t53
        show sayori 1q
        "Sayori simply beams at Natsuki."
        show dadsuki zorder 3 at f52
        d "Sorry for making you like this, Natsuki."
        d "It's probably going to be hard for you to finish your little play like that."
        show dadsuki zorder 2 at t52
        show natsuki 2s zorder 3 at f53
        n "W-Well..."
        n "It's okay, I guess."
        show natsuki zorder 2 at t53
        show sayori 1d zorder 3 at f54
        s "Do you guys want a moment?"
        s "We can leave..."
        s "This is way more important than some play."
        show dadsuki 1p zorder 3 at f52
        show sayori zorder 2 at t54
        d "I think we should talk for a little bit, Natsuki."
        d "But if you want to finish up here first..."
        d "Then, go ahead. I can wait."
        show dadsuki zorder 2 at t52
        "Natsuki thinks for a moment. She looks at us then back at Yasuhiro."
        show monika zorder 3 at f51
        if monika_type == 0:
            m 1e "I think you should talk to him, Natsuki."
            m "Like Sayori said, this is way more important than some play."
        else:
            m 1a "Just talk to him, Natsuki."
            m "Don't worry about us."
        show monika zorder 2 at t51
        show yuri 2pb zorder 3 at f55
        y "I agree with Monika."
        y "This is obviously an important time in your life."
        y "So you should make the most of it."
        show natsuki 1n zorder 3 at f53
        show yuri zorder 2 at t55
        n "You guys..."
        n "..."
        n "Alright, I've made up my mind."
        n "Dad...?"
        show dadsuki 1m zorder 3 at f52
        show natsuki zorder 2 at t53
        d "Yes?"
        show dadsuki zorder 2 at t52
        show natsuki 2q zorder 3 at f53
        n "I-I'd like to talk to you, outside."
        n "Just the two of us."
        show dadsuki 1p zorder 3 at f52
        show natsuki zorder 2 at t53
        d "Of course..."
        show dadsuki zorder 2 at t52
        show natsuki 2ps zorder 3 at f53
        n "S-See you guys tomorrow..."
        show dadsuki at lhide
        hide dadsuki
        show natsuki at lhide
        hide natsuki
        show monika zorder 2 at t31
        show sayori zorder 2 at t32
        show yuri zorder 2 at t33
        "Natsuki waves us goodbye and exits the gym, with her dad behind her."
        show sayori 2t zorder 3 at f32
        s "I'm so happy for her!"
        s "She's got her dad back..."
        show sayori zorder 2 at t32
        show yuri 2ps zorder 3 at f33
        y "It does look that way..."
        y 2ph "I have to wonder what the whole thing about Natsuki's mom is though..."
        y 2pt "He seemed pretty confident that she would be here."
        show sayori 2d zorder 3 at f32
        show yuri zorder 2 at t33
        s "I think some things are better left hidden, don't you think?"
        s "What matters is that Natsuki got her happy ending..."
        show monika zorder 3 at f31
        show sayori zorder 2 at t32
        if monika_type == 0:
            m 1e "I hope so, Sayori."
        else:
            m 1j "You'd hope so..."
        show monika zorder 2 at t31
        show sayori 1c zorder 3 at f32
        s "Anyway..."
        s "I don't think she's going to be back here for the rest of today."
        s 1q "So I guess that's the end of the meeting."
        s "Ehehe, I hope to see you all tomorrow."
        show sayori zorder 2 at t32
        show yuri 3pf zorder 3 at f33
        y "That's it?"
        y "That was a pretty abrupt end to the whole thing."
        show yuri zorder 2 at t33
        mc "I think it ended pretty well."
        mc "It could have gone worse, I'm sure."
        mc "Still, it's hard to believe this is what caused Yasuhiro to finally realize how much Natsuki meant to him."
        show sayori 1d zorder 3 at f32
        s "Oh, you have no idea."
        s "But never mind that, let's all head home."
        s "I think we all deserve a good rest after today."
        s "I'll let Natsuki know that we're going to be leaving myself."
        show monika 1a zorder 3 at f31
        if monika_type == 0:
            m "Alright, Sayori."
            m "I'll see you all tomorrow..."
        elif monika_type == 1:
            m "Okay, Sayori~"
            m "I can't wait for tomorrow."
        else:
            m "Fine by me."
            m "I'm ready for this day to be over."
        show monika at thide
        hide monika
        show yuri zorder 2 at t21
        show sayori zorder 2 at t22
        "Monika quickly leaves the gym through the door Natsuki and Yasuhiro didn't go through."
        show sayori 1b zorder 3 at f22
        s "Well, I don't know about the two of you."
        s 1l "But I'm all ready to sleep!"
        s "I'm gonna run home, bye [player]!"
        show sayori zorder 2 at t22
        mc "You're going to run home when you're tired...?"
        show sayori zorder 3 at f22
        s 1q "Yeah!"
        show sayori zorder 2 at t22
        mc "Alright...I guess I'll see you later, Sayori."
        show sayori at thide
        hide sayori
        show yuri zorder 2 at t11
        "Sayori grabs her bag and leaves the gym."
        "She stops once she steps outside and says something to who I can only assume is Natsuki before waving goodbye."
        $ ch12_outcome = 1
    else:
        d 1h "This..."
        d "This is pathetic."
        stop music_poem fadeout 2.0
        d 1g "Are you really wasting my time with this sorry excuse you call a play?"
        d "I've been patient until now but this is getting out of hand."
        d 1c "Are you trying to make me feel some remorse?"
        d "Is that it?"
        show dadsuki zorder 2 at t51
        show sayori 1g zorder 3 at f54
        s "E-Eh? What are you talking about?"
        show dadsuki 1e zorder 3 at f51
        show sayori zorder 2 at t54
        d "I'm done playing your games."
        d "Tell me where she is, or you'll pay the price."
        show dadsuki zorder 2 at t51
        show sayori 1j zorder 3 at f54
        s "Are you threatening me?"
        s "I suggest you watch yourself, Yasuhiro."
        show sayori zorder 2 at t54
        "I've never seen Sayori so serious before."
        "I guess she doesn't take threats lightly?"
        show monika 1l zorder 3 at f52
        if monika_type == 0:
            m "Ahaha, wow...Sayori..."
            m "...that almost sounded like a threat."
        else:
            m "You're getting serious now, Sayori."
            m "This sure makes things lot more interesting."
        show monika zorder 2 at t52
        show natsuki 2r zorder 3 at hf53
        n "G-Guys!"
        "Natsuki is suddenly able to move again."
        "I guess she just wants them to stop fighting so much that she got over her nerves."
        n "We don't have to do this..."
        n 2s "Can we just get back to the play...?"
        show dadsuki 1g zorder 3 at f51
        show natsuki zorder 2 at t53
        d "You're moving again I see."
        d "That doesn't give you reason to talk, does it?"
        d 1e "No one asked for you to speak."
        d "Do you honestly think anyone really cares about what you have to say?"
        d 1h "Do you?!"
        show natsuki 1n
        "Natsuki doesn't say anything but it looks like she's on the verge of tears."
        d 1f "I didn't think so."
        d "So just keep your mouth shut and this will all be over soon."
        show dadsuki zorder 2 at t51
        show sayori 2j zorder 3 at f54
        play music t9g fadein 3.0
        s "..."
        s "You're really pushing your boundaries, Yasuhiro."
        s "So you better apologize to Natsuki, right now."
        show dadsuki 1m zorder 3 at f51
        show sayori zorder 2 at t54
        d "Ahahahahahaha!"
        d "Are you seriously tell me what to do?"
        d 1f "You have no idea what you're getting into, girl."
        show dadsuki zorder 2 at t51
        show sayori 2k zorder 3 at f54
        s "I'm sorry for this, Natsuki."
        s "I didn't know this was going to go so badly."
        s "So I want to make it up to you."
        s 2j "I'm going to fix this myself."
        s "You just have to give me the word, Natsuki."
        show natsuki 1u zorder 3 at f52
        show sayori zorder 2 at t54
        n "...?"
        show natsuki zorder 2 at t52
        show sayori 2d zorder 3 at f54
        s "The answer to this question."
        s "I want you to think about it carefully, okay?"
        "Natsuki manages to let out a nod."
        s "Do you still love your dad?"
        s 2k "Actually, let me rephrase that."
        s 2h "Do you have any other feelings except resentment towards Yasuhiro?"
        s "You see how he's treating you."
        s 2g "Do you really think this will improve for you?"
        s "He has no shame in treating you like this in public."
        s 1d "Just give me the word, and it'll all be over."
        s "It's your choice, Natsuki."
        show sayori zorder 2 at t54
        "Natsuki looks at Sayori sadly then at Yasuhiro."
        show dadsuki 1b zorder 3 at f51
        d "Do you really think you can just solve this whole thing like that?"
        d "You're in way over your head."
        d 1f "What makes you think I won't hurt you or everyone else here?"
        d "I know my way around the law."
        d "You can't touch me but I can make all of your lives a living hell."
        d "So...what are you going to do?"
        "There's a brief silence in the room."
        "You could cut the tension in the air with a knife."
        d "She won't say anything."
        d "Now that I've told her to shut up."
        show natsuki 1f
        "Natsuki starts looking angry."
        d 1g "Unlike all of you, she knows her place."
        d "Now--"
        show dadsuki zorder 2 at t51
        show natsuki 1e zorder 3 at f52
        n "No."
        "Natsuki suddenly interrupts Yasuhiro."
        n "I've had enough."
        n 1q "I still love my dad..."
        n 1r "But this person..."
        n "He looks like my dad, but it isn't him."
        n 1s "I lost my dad a long time ago."
        n "I didn't realize it until I heard [player] say it before."
        n "Sayori saying it now, it's just confirmed everything..."
        n 1f "This is...some sort of bitter monster..."
        n "So...to answer your question."
        n 1e "I don't care what you do to him."
        n "I don't know this person."
        show dadsuki 1b zorder 3 at f51
        show natsuki zorder 2 at t52
        d "You little brat."
        d "You think this changes anything?"
        d 1f "When you get home, you're--"
        show sayori 1a zorder 3 at f54
        s "That's all I needed to hear."
        "Sayori takes a deep breath."
        s 1d "I'll be right back."
        show monika 2c zorder 3 at f52
        show sayori zorder 2 at t54
        if monika_type == 0:
            m "Sayori..."
            m "Where are you planing on going?"
        else:
            m "Hm."
            m "Sayori, where are you going?"
        show monika zorder 2 at t52
        show sayori zorder 3 at f54
        s "A place where I can fix this..."
        show sayori at thide
        hide sayori
        show dadsuki zorder 2 at t41
        show monika zorder 2 at t42
        show natsuki zorder 2 at t43
        show yuri zorder 2 at t44
        "Sayori runs towards the entrance of the gym."
        show dadsuki 1b zorder 3 at f41
        d "Ha! What was that meant to be?"
        d "She's running from her problems."
        d 1f "You should have done the same, Natsuki."
        d "Now you have no one to protect you."
        show dasuki zorder 2 at t41
        show yuri 3pr zorder 3 at f44
        y "That's not true!"
        "Yuri takes a step forward."
        play music t8 fadeout 2.0
        y "If you want to hurt Natsuki, then you're going to have to go through me."
        show dadsuki 1m zorder 3 at f41
        show yuri zorder 2 at t44
        d "That's quite brave of you."
        d 1f "But ultimately, it will end the same."
        show dadsuki zorder 2 at t41
        mc "You'll have to go through me too."
        mc "Natsuki is my friend and if you want to hurt her, then you'll have to go through me."
        show dadsuki zorder 3 at f41
        d "Ahahahaha, you stupid boy."
        d "Do you really think you can stop me?"
        show dadsuki zorder 2 at t41
        show monika zorder 3 at f42
        if monika_type == 0:
            m 1f "You really don't want to do this, Yasuhiro."
        elif monika_type == 1:
            m 1e "I suggest you stop while you're only a little behind, Yasuhiro."
        else:
            m 1a "Finally. I've been waiting for something like this to happen."
        show monika zorder 2 at t42
        "Monika takes a step forward as well."
        "Natsuki looks at all of us in disbelief."
        show natsuki 1c zorder 3 at f43
        n "G-Guys..."
        n 1n "...thank you."
        show dadsuki 1h zorder 3 at f41
        show natsuki zorder 2 at t43
        d "Do you seriously think you stand a chance?"
        d "I'll beat you all to a pulp."
        show sayori 1h zorder 3 at f51
        show dadsuki zorder 2 at t52
        show monika zorder 2 at t53
        show natsuki zorder 2 at t54
        show yuri zorder 2 at t55
        s "There he is."
        "Sayori enters the gym, from the door opposite where she exited."
        "Police officers enter the gym and surround Yasuhiro."
        show sayori zorder 2 at t51
        show dadsuki  zorder 3 at f53
        d "What's happening here?"
        d "When did you get the police involved?!"
        scene black with dissolve_cg
        "One of them suddenly tackles Yasuhiro to the ground and handcuffs him."
        d "You can't do this!"
        d "You don't have any charges against me."
        "Police Officer" "\"You have charges of domestic abuse against you.\""
        "Police Officer" "\"We have undeniable evidence.\""
        "Police Officer" "\"So have fun sitting in a prison cell for a couple of years, sir.\""
        d "What?!"
        d "No!"
        d "This can't be happening!"
        d "Natsuki, do something!"
        d "Say something!"
        d "Tell them they're lying!"
        "Natsuki does nothing as Yasuhiro is taken away by the police."
        d "No!"
        d "I'll destroy you all!"
        d "When I get out, I'll--"
        "The police close the door to the gym."
        n "..."
        s "Natsuki, it's over."
        "Police Officer" "\"Ah...well, you and this {i}Natsuki{/i} need to give a statement.\""
        "Police Officer" "\"That is, if you actually want him to be convicted properly.\""
        s "Oh, right! I'll give you mine in a minute but can you give Natsuki a break until tomorrow?"
        s "I think she's still processing what just happened."
        "Police Officer" "\"Of course, ma'am..\""
        "The final officer gives a friendly nod and exits the gym."
        scene bg gym
        show sayori 1g zorder 2 at i41
        show monika 1f zorder 2 at i42
        show natsuki 1g zorder 2 at i43
        show yuri 3pf zorder 2 at i44
        with dissolve_cg
        show sayori zorder 3 at f41
        s "Well...how are you feeling, Natsuki?"
        s "What just happened is a lot to take in."
        show sayori zorder 2 at t41
        show natsuki 1q zorder 3 at f43
        n "I'm..."
        "Natsuki's voice quietens down."
        n 1s "...grateful for friends like you guys..."
        n "I think I need to just go home and rest."
        show sayori 1d zorder 3 at f41
        show natsuki zorder 2 at t43
        s "Alright..."
        s "Will you be okay?"
        show sayori zorder 2 at t41
        show natsuki 1u zorder 3 at f43
        n "I don't know..."
        n "I'll...see you guys tomorrow."
        show natsuki at thide
        hide natsuki
        show sayori zorder 2 at t31
        show monika zorder 2 at t32
        show yuri zorder 2 at t33
        "Natsuki avoids letting us see her face and exits the gym from the door the police didn't go through."
        show monika zorder 3 at f32
        if monika_type == 0:
            m 1m "Today was certainly something~"
        else:
            m 1l "What an interesting outcome to a strange day."
        show monika zorder 2 at t32
        show yuri 2pq zorder 3 at f33
        y "Yeah..."
        y "That was a little too much excitement for one day."
        show yuri zorder 2 at t33
        mc "Agreed."
        mc "I have to ask you something, Sayori."
        show sayori 1c zorder 3 at f31
        s "Huh? What is it?"
        show sayori zorder 2 at t31
        mc "Why did you invite Yasuhiro in the first place?"
        mc "And how did you manage to get the police here so quickly?"
        mc "You left a few minutes before they arrived and it's not like they were here already."
        show sayori 1l zorder 3 at f31
        s "Ehehe, maybe those are questions you'll be asking yourself for the rest of your life~"
        show sayori zorder 2 at t31
        show monika zorder 3 at f32
        if monika_type == 0:
            m 1e "It's probably better that way."
        elif monika_type == 1:
            m 1j "I suppose that's for the best, isn't it...?"
        else:
            m 1h "I'm a bit curious too, though I doubt you'd tell me."
        show sayori 1d zorder 3 at f31
        show monika zorder 2 at t32
        s "Anyway..."
        s "We all deserve a rest after today."
        s "I know we didn't get to finish the play, but Natsuki's wellbeing is more important."
        show sayori zorder 2 at t31
        show monika zorder 3 at f32
        if monika_type == 0:
            m "I'm just glad today ended without anything terrible happening..."
            m "I hope it's the same for tomrrow..."
        else:
            m "So the day is finally over."
            m "I'll see you three soon."
        show monika at thide
        hide monika
        show sayori zorder 2 at t21
        show yuri zorder 2 at t22
        "Monika leaves through the same door Natsuki did."
        show sayori 2d zorder 3 at f21
        s "I know today was pretty intense."
        s "I hope it hasn't put either of you from the Literature Club."
        show sayori zorder 2 at t21
        show yuri 3pf zorder 3 at f22
        y "No..."
        y "I just hope nothing like that ever happens again."
        show sayori 2k zorder 3 at f21
        show yuri zorder 2 at t22
        s "I feel the same, Yuri."
        s 2a "Anyway, I gotta go give the police my statement."
        s "See you tomorrow, guys!"
        show sayori at thide
        hide sayori
        show yuri zorder 2 at t11
        "Sayori waves goodbye before going out the door the police did a few minutes ago."
        $ ch12_outcome = 0
    y 2pf "You know, this isn't something I expected to be seeing when I joined the Literature Club."
    mc "Yeah..."
    mc "Not just this part of it...the whole day felt really weird."
    y 2pg "You've got that right..."
    y 2pf "Anyway..."
    if visited_yuri_hospital:
        y 3pb "Ready to walk home, [player]?"
        mc "Yeah, let's go."
    else:
        y 3ps "I suppose I'll see you tomorrow as well."
        mc "You can count on it, Yuri."
    return

label ch12_end:
    scene bg residential_day with wipeleft_scene
    play music t2 fadeout 2.0
    if visited_yuri_hospital:
        "After walking Yuri to her house, I head home."
    else:
        "I walk home slowly, still not quite believing what just happened."
    "The events of today are still fresh in my head."
    if ch12_outcome == 0:
        "Yasuhiro getting arrested like that..."
    elif ch12_outcome == 1:
        "Yasuhiro and Natsuki reconciling like that..."
    elif ch12_outcome == 2:
        "Natsuki's mom reuniting with her like that and Monika knocking Yasuhiro out..."
    else:
        "Natsuki's family becoming whole again..."
    "While it was certainly interesting, I hope stuff like that doesn't happen too often."
    "I'm not in the Literature Club for that kind of thing."
    if monika_type != 0:
        "As I cross into the final turn before my street, someone blocks my way."
        "It's Monika."
        if ch12_natsuki_reluctance >= 3:
            show monika 3b zorder 2 at t11
            m "Hello, [player]."
            m "Did you have fun today?"
        else:
            show monika 3b zorder 2 at t11
            m "[player]."
            m "You've disapppointed me."
    else:
        "I hope tomorrow is less weird."
        "I don't know about everyone else, but life feels...complete."
        "It's like I've done what I've set out to do."
        "Which is weird, since I still have my whole life ahead of me."
    call screen dialog(message="End of Update!", ok_action=Quit(confirm=False))
    return
