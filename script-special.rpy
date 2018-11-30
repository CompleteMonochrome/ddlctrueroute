label special_chapter:
    # Alternate Reality - Monika has no Ribbon
    $ monika_type = 1
    $ ch12_markov_agree = True
    scene black
    $ s_name = "???"
    $ audio.t2r = "<from 0 to 38.23 loop 0>mod_assets/bgm/2r.ogg"
    play music t2r
    "Where...am I?"
    "It feels...cold."
    "But strangely familiar."
    s "You're right where you need to be."
    "What?"
    "Who said that?"
    s "It's our special day, [player]."
    scene bg bedroom_gray with fade
    $ style.say_window = style.window_flashback
    s "It's {i}her{/i} special day."
    s "So..."
    s "Are you going to celebrate it with us?"
    "Celebrate what?"
    s "We're going back to before..."
    "Before what?"
    s "Well, before everything."
    s "Before all the conflict."
    scene bg house_gray with fade
    s "Before all of this started."
    s "Before I had so much to worry about."
    s "And before there was ever a true threat."
    scene bg sayori_bedroom_gray with fade
    s "A true...route to happiness."
    "What...?"
    s "But don't worry."
    s "It's not like that."
    s "There's just something we forgot to do."
    scene bg club_day_gray with fade
    s "And now, it's time to fix things."
    s "They say you can't change the past..."
    "We can't."
    "We just have to face the future."
    s "But..."
    s "Our reality is different, isn't it?"
    "It is?"
    s "We can experience alternate realities."
    s "Where the past was different."
    s "At least, for a while."
    s "In this reality..."
    scene bg residential_day_gray with fade
    s "In...the confines of this game, we can do almost anything."
    s "It's time to right a wrong."
    s "At least, for a while."
    "What did we do?"
    s "I just can't believe we forgot..."
    "Forgot what?"
    s "You'll see..."
    menu:
        s "Are you ready?"
        "Yes.":
            pass
        "Ready as I'll ever be.":
            pass
        "I was born ready.":
            pass
        "What will clicking this do?":
            pass
        "No?":
            s "Then what are you even doing here?"
            $ renpy.utter_restart()
    s "Great!"
    s "Then let's fix this thing together."
    stop music fadeout 1.5
    scene bg residential_day with Dissolve(1.5)
    play music t2 fadein 3.0
    $ s_name = "Sayori"
    $ style.say_window = style.window
    "We're on our way."
    "I can't believe we forgot."
    "Some friends we are."
    "I feel so bad about all of this."
    "We have to do the right thing."
    show sayori 2bc zorder 2 at t11
    s "What did you get her, [player]?"
    s 2bl "Something good, I hope?"
    mc "You'll find out when we get there, Sayori."
    mc "I want to keep it a surprise."
    s 2bj "Aww...but you can tell me, right?"
    s "I won't tell anyone!"
    s "I promise."
    show natsuki 1be zorder 3 at f31
    n "Jeez, Sayori."
    n "Can't you just wait until we get there?"
    n 2bb "And if [player] doesn't want to tell you then he doesn't have to."
    n "You can't just force him like that, you know!"
    show natsuki zorder 2 at t31
    show yuri 1bb zorder 3 at f33
    y "Natsuki is right."
    y "If [player] wants to keep it a surprise, then let him."
    y 2bf "We can't and shouldn't control his actions."
    show yuri zorder 2 at t33
    mc "Thanks for backing me up, you two."
    mc "She's been like this ever since yesterday."
    show sayori 1bh zorder 3 at f32
    s "You guys are no fun!"
    s "I told you all what I bought!"
    show sayori 4bq
    "Sayori holds her present high in the air."
    "It's wrapped in paper with an arm flexing pattern."
    "The paper itself is crudely taped together."
    "The tape is almost as prominent as the arms flexing."
    s 1bl "Why can't you just tell me?"
    show natsuki 1bh zorder 3 at f31
    show sayori zorder 2 at t32
    n "Sayori, you only told everyone because you couldn't keep it to yourself."
    n "The rest of us want to keep what we have a surprise."
    n 1bq "I just hope we can get there before it starts to spoil..."
    n "It's definitely better in terms of taste compared to what you brought, Sayori."
    show natsuki zorder 2 at t31
    show sayori 2bl zorder 3 at f32
    s "E-Eh? What do you mean?"
    "Natsuki rolls her eyes."
    s 4bq "Ehehe~"
    "Sayori laughs nervously."
    s 4br "I-I didn't have a lot of money to spend."
    s "So I just made sure to put a lot of thought into her present, you know?"
    show sayori zorder 2 at t32
    mc "You forgot to mention you had to borrow some money from me."
    show sayori 4bl zorder 3 at f32
    s "W-Well...I needed money for printing!"
    s 3bd "H-Hey look, we're almost there!"
    "Sayori points towards a house in the distance."
    "I can't really make it out from where we are."
    s 3bq "Come on guys!"
    show sayori zorder 2 at t32
    show yuri 3bh zorder 3 at f33
    y "So that's where she lives?"
    y "Interesting..."
    show yuri zorder 2 at t33
    mc "When I joined the literature club I never imagined I'd be doing something like this."
    mc "Do we even have a plan when we get there?"
    show sayori 1bd zorder 3 at f32
    s "It's our duty as her friends, [player]!"
    s "Plus...we kinda forgot about it."
    s 1ba "So we have to make it up to her."
    s "I'm sure she'll be so surprised!"
    show sayori zorder 2 at t32
    "So...we don't have a plan?"
    show natsuki 2bc zorder 3 at f31
    n "Do you think that maybe she'll be {i}that{/i} upset?"
    n "I mean she does have other friends, right?"
    n 2bg "It's not like every single one of them forgot about her birthday."
    show natsuki zorder 2 at t31
    show yuri 2bl zorder 3 at f33
    y "I suppose that's true."
    y "But if you think about it, she must be quite lonely."
    y 2bt "Being popular like Monika means everybody wants to be your friend."
    y "But when it comes down to it...can she really count on those people?"
    y "Or are they just there because of her popularity...?"
    y 2bv "Are they 'real' friends?"
    show natsuki 2bq zorder 3 at f31
    show yuri zorder 2 at t33
    n "I didn't think about it like that..."
    n "Still..."
    n 2bm "The whole reason we're doing this is because we forgot, right?"
    n "I just hope she forgives us."
    show natsuki zorder 2 at t31
    show sayori 1bd zorder 3 at f32
    s "We can't worry about the past now, Natsuki."
    s "We can't change it."
    s "We just have to--"
    show sayori zorder 2 at t32
    mc "Face the future."
    mc "That's what you were going to say, right?"
    show sayori 1bl zorder 3 at f32
    s "Actually, I was going to say treat her to cupcakes but I guess that works too!"
    show sayori zorder 2 at t32
    show yuri 1bf zorder 3 at f33
    y "I don't mean to interrupt, but we should probably quicken our pace."
    y "The sooner we get there, the better."
    show sayori 2bc zorder 3 at f32
    show yuri zorder 2 at t33
    s "You're right, let's go!"
    scene bg new_house with wipeleft_scene
    "The four of us arrive in front a house."
    "This should be the right one."
    "Sayori seems confident it is."
    show natsuki 2bc zorder 3 at f31
    n "Now that we're here, what's the plan?"
    n "Are we just going to tell her we're here?"
    n "It would kinda ruin the surprise."
    show natsuki zorder 2 at t31
    show yuri 1bq zorder 3 at f33
    y "What's the alternative?"
    y "It's not like we're just going to break into her home..."
    show sayori 1bn zorder 3 at f32
    show yuri zorder 2 at t33
    s "Yuri, you just gave me an idea!"
    show sayori zorder 2 at t32
    show yuri 1bo zorder 3 at f33
    y "I did...?"
    y "Sayori, you can't seriously be think--"
    show sayori zorder 3 at hf32
    show yuri 1bq zorder 2 at t33
    s "We're going to sneak into her house and--"
    show sayori zorder 2 at t32
    mc "Are you crazy, Sayori?"
    mc "I know you and Monika and close because you're the vice president and everything but..."
    mc "Isn't that crossing some kind of line?"
    show sayori 1bl zorder 3 at f32
    s "Just hear me out, okay?"
    s "She's going to love it!"
    s 2bd "You guys trust me, right?"
    show natsuki 2bg
    show yuri 1bf
    "Everyone except me nods their head."
    s "So here's my plan."
    s 2bc "[player] is going to stay out here and get Monika to look away."
    s "We'll use him as a distraction so that we can sneak inside."
    s "Then we'll get ready to surprise her when she comes back inside with [player]."
    show sayori zorder 2 at t32
    show yuri 1bh zorder 3 at f33
    y "As crazy as this sounds..."
    y "It isn't the worst idea I've heard."
    show natsuki 1bd zorder 3 at f31
    show yuri zorder 2 at t33
    n "Yeah, this could actually work."
    show natsuki zorder 2 at t31
    mc "Are you guys kidding?"
    mc "There's so many things that could go wrong here!"
    mc "What if she hears you walk in?"
    mc "What if she has an alarm or something?!"
    show sayori 1bd zorder 3 at f32
    s "Just trust me, [player]."
    s "This is going to work."
    s 1ba "Is everyone ready?"
    show sayori zorder 2 at t32
    mc "I'm not!"
    mc "How do you expect me to distract her?"
    show sayori 2bq zorder 3 at f32
    s "Ehehe, I don't know."
    s "Why don't you use your charm on her?"
    show natsuki 2by
    show yuri 1bd
    "Natsuki and Yuri let out a small giggle."
    s 2ba "You'll think of something."
    s "Good luck!"
    show sayori zorder 2 at t32
    mc "Can I just--"
    show sayori 2br zorder 3 at f32
    s "Sorry, what?"
    "Sayori clicks the button on the fence."
    "It seems like a doorbell of some sort."
    s "Oops!"
    s "Run everyone!"
    show natsuki at thide
    hide natsuki
    show sayori at thide
    hide sayori
    show yuri at thide
    hide yuri
    "Everyone moves out of sight."
    mc "I can't believe I'm doing this."
    "I take a deep breath and look towards the door."
    "In the corner of my eye, I can see the other three hiding."
    "If you can call going behind a car and being able to clearly see them through the windows 'hiding'."
    mc "Hello?"
    mc "Are you there?"
    "Someone steps out the house and opens the gate."
    "The door to the house is still open."
    show monika 1bf zorder 2 at t11
    m "[player]?"
    m "W-What are you doing here?"
    mc "Monika..."
    "I look towards the car they're hiding behind."
    "Sayori is signalling me something."
    "From where I am, it looks like random hand signs that don't mean anything."
    mc "Hello..."
    m 2bf "Hi?"
    m 2bg "I'm sorry but why are you here?"
    m "And what are you carrying?"
    "Monika points towards the small box I'm carrying in my hand has her gift."
    "I take a step backwards."
    m 2bh "What are you doing?"
    mc "Oh...you know..."
    mc "...stuff."
    "What do I do?"
    "For some reason, I suddenly remember the wrapping on Sayori's gift."
    mc "Ever heard of...uhh..."
    mc "...flex...tape?"
    "I move a few feet away from her."
    m 1bc "What tape...?"
    m "Where are you going?"
    "For some reason, Monika actually followed me."
    "The other three can get in her house now."
    mc "I just...have to put this in my pocket."
    "I put the small box in my pocket."
    "I look at the three girls trying to enter Monika's house."
    m 2bd "What are you look--"
    "Monika starts to turn behind her."
    mc "I love you."
    show monika at h11
    m 1bn "What?!"
    "That stopped her."
    "Sayori gives me a thumbs up as she enters the house."
    "But how am I going to explain what I just said?"
    m "[player], what did you just say?"
    mc "I...um..."
    mc "I said...I love you."
    show monika 1bo
    "Monika frowns."
    if sayori_confess:
        m 1bq "We both know that's not true, [player]."
        m "You and Sayori are a perfect couple."
        m 1br "I can't come between the two of you."
        m "As her friend, that would simply be too hurtful."
    else:
        m 1bf "That's...a lie, isn't it?"
        mc "What?"
        m 1bm "It's okay."
        m "You don't need to lie anymore."
        m "I know you like [ch4_name] more."
    m 2be "So let's just forget you said that."
    m "For both of our sakes, okay?"
    m 2bm "Besides...there's someone I'm already looking for."
    m "I just don't know if they're watching..."
    m 2bn "Not anymore."
    mc "What do you mean?"
    m 1bq "...Nothing."
    "Monika recomposes herself."
    m 1bc "So what's that small box you were carrying?"
    m "And why is it wrapped in that tacky paper?"
    "Tacky...?"
    "I didn't think it was tacky..."
    mc "Well...it's..."
    mc "It's for you."
    m 1bd "For me?"
    mc "You know...for your birthday."
    show monika 1bo at s11
    m "Ah..."
    "Monika's voice trembles."
    mc "I'm sorry I forgot."
    mc "I'm a terrible friend."
    m 1bn "No, that's..."
    m "That's not your fault."
    m "There's no way you could have known."
    mc "I still feel bad about it."
    mc "Here."
    show monika at t11
    "I get the box from my pocket and offer it to her."
    m 1be "Actually..."
    m "Just hold on to it for now."
    mc "Are you sure?"
    m "Yeah..."
    m 2be "You know, I've actually been meaning to talk to you about something."
    m "It's nothing bad."
    m "Why don't you come inside, [player]?"
    m "We can talk in there."
    mc "Okay, good idea."
    m 2ba "Then it's settled."
    m "Follow me."
    "I put the present back in my pocket."
    "Everything is going according to plan so far."
    "Hopefully that was enough for Sayori and the others to set up in there."
    scene bg m_livingroom with wipeleft_scene
    play music t3 fadeout 1.0
    "Monika and I enter her house."
    "I'm still carrying the box containing her gift."
    "There's no sign of the others just yet."
    "I wonder where they are..."
    show monika 1ba zorder 2 at t11
    m "Take a seat, [player]."
    m "I'll go--"
    show sayori 4br zorder 3 at hf21
    show monika zorder 2 at t22
    s "Surprise!"
    show sayori zorder 2 at t21
    show monika 1bd zorder 3 at f22
    m "Sayori?!"
    m "How did you--"
    show sayori zorder 2 at t41
    show monika zorder 2 at t42
    show natsuki 1bd zorder 3 at hf43
    show yuri 3bd zorder 3 at hf44
    ny "Happy birthday, Monika!"
    show monika 1bs zorder 3 at f42
    show natsuki zorder 2 at t43
    show yuri zorder 2 at t44
    m "Natsuki? Yuri?"
    m "E-Everyone..."
    "Monika wipes her face with her arm."
    m "You..."
    show sayori 2bd zorder 3 at f41
    show monika zorder 2 at t42
    s "We're really sorry that we forgot, Monika."
    s "We should have known it was your birthday."
    "Sayori brings out her gift and offers it to Monika."
    "Monika takes it and puts it on the floor before giving Sayori a hug."
    s 2ba "We all brought you something!"
    show sayori zorder 2 at t41
    show monika 2be zorder 3 at f42
    m "You guys..."
    m "You didn't have to do this."
    show monika zorder 2 at t42
    show natsuki 1be zorder 3 at f43
    n "Of course we did!"
    n 1bd "I even baked you a cake."
    "Natsuki opens the lid of the box and reveals a cake."
    "It's got pink frosting and is decorated with cats everywhere."
    "It's already sliced into a couple of pieces."
    "I'm surprised it held together all the way to Monika's house."
    n 1bq "You know...because friends shouldn't forget important stuff like this."
    show natsuki zorder 2 at t43
    mc "That was your gift?"
    mc "That looks incredible, Natsuki!"
    show natsuki 2bt zorder 3 at f43
    n "I know, right?!"
    n "It's my mom's recipe."
    n "Well, actually she passed it down to me from her mom but..."
    n 2bl "You get the idea."
    show natsuki zorder 2 at t43
    show yuri 1bh zorder 3 at f44
    y "Your mother can bake?"
    y "I thought she was just an actor in the theatre..."
    y 2bf "I didn't know she had that much talent."
    show natsuki 2bd zorder 3 at f43
    show yuri zorder 2 at t44
    n "She does a lot of things, you know!"
    n "Acting is just her main hobby."
    show natsuki 1bt
    "Natsuki smiles faintly."
    n "She's a really loving person."
    n 1bj "I don't know where I would be without her."
    show sayori 1bm zorder 3 at f41
    show natsuki zorder 2 at t43
    s "That cake looks soooo yummy!"
    s "Can I have some?"
    "Sayori tries to grab a piece of the cake."
    "Natsuki swats her hand off it."
    s 1bl "Ow..."
    show sayori zorder 2 at t41
    show natsuki 1be zorder 3 at f43
    n "You'll get some, Sayori."
    n "Just wait until everyone gives their gift."
    show natsuki zorder 2 at t43
    show yuri 2bi zorder 3 at f44
    y "Then I'll go next."
    y "I didn't know what you liked, Monika."
    y 2bf "But since you're part of the literature club, I got you a book."
    "Yuri gives the book to Monika."
    "It looks like it has some writing on the cover of it."
    "The cover itself has a heart that has an optical illusion."
    y 3ba "It's the limited edition version of 'Sound of your Heartbeat', signed by the author himself."
    y "I think you might like it."
    show monika 1bb zorder 3 at f42
    show yuri zorder 2 at t44
    m "Yuri..."
    m "You shouldn't have!"
    show monika zorder 2 at t42
    show yuri 3bo zorder 3 at f44
    y "I-I shouldn't...?"
    y "I-I'm sorry, I didn't know what to--"
    show monika 1bl zorder 3 at f42
    show yuri zorder 2 at t44
    m "That's not what I meant..."
    m "Let me rephrase it."
    m 1be "Yuri, this is incredible!"
    m "Thank you for getting me this."
    m "I love books written by this author. You even got me the limited edition and it's signed too!"
    m 2be "Thank you, it's an exceptional present."
    show monika zorder 2 at t42
    show yuri 2be zorder 3 at f44
    y "E-Exceptional...?"
    y 2bs "You're welcome, Monika."
    "Yuri smiles bashfully."
    y "I don't personally enjoy this sort of text but I hope you like it!"
    show monika 1bj zorder 3 at f42
    show yuri zorder 2 at t44
    m "I'm sure I'll love it, Yuri."
    m "Thank you."
    show sayori 1bq zorder 3 at f41
    show monika zorder 2 at t42
    s "Open mine next!"
    s "You'll love it...I hope!"
    show sayori zorder 2 at t41
    show monika 1ba zorder 3 at f42
    m "Ahaha, okay, Sayori..."
    "Monika picks up Sayori's present."
    "She looks at the wrapping and taping inquisitively."
    "She smiles and begins unwrapping it."
    "It's a photo album."
    m 1bc "What is this?"
    "Monika turns the page and in it are photos of things we've done in the club."
    "There's their first day when they formed the club without me."
    "Then there's pictures of me when I joined the club."
    "And stuff they did in preparation for the festival."
    "As Monika turns the pages, a sense of nostalgia fills me as I see pictures of all five of us in the weeks past."
    m 1be "Sayori..."
    m "Thank you."
    m "With these, I can cherish our memories forever."
    show sayori 1ba zorder 3 at f41
    show monika zorder 2 at t42
    s "I'm glad!"
    s 1bd "I honestly wasn't completely sure if you'd like it."
    s "...Or like us, since we forgot."
    s "But I'm glad you do."
    show sayori 2bd
    "Sayori puts her hand on Monika's shoulder."
    s "Do you forgive us, Monika?"
    show sayori zorder 2 at t41
    "Monika looks at Sayori."
    "She stares at her for a while before looking at the rest of us."
    show monika 3be zorder 3 at f42
    m "There's no way I could stay mad at you all."
    m "You're my friends..."
    m 3bm "I didn't tell anyone my birthday and I got upset about it."
    m "That's on me..."
    m 3bn "I guess I just thought you guys would know..."
    show monika 3bk
    "Monika beams."
    m "Okay, everyone..."
    m "I forgive you!"
    show sayori 4bq zorder 3 at f41
    show monika zorder 2 at t42
    s "Yaaaaaaay!"
    s "Hear that guys, we're back to normal!"
    show sayori zorder 2 at h41
    "Sayori begins hopping around."
    "She grabs a piece of cake while Natsuki isn't looking."
    show yuri 1bf zorder 3 at f44
    y "[player], you haven't given your present yet."
    y "What did you get her?"
    show monika 1be zorder 3 at f42
    show yuri zorder 2 at t44
    m "Saving the best for last, [player]?"
    show monika zorder 2 at t42
    mc "Ah, not really."
    mc "Here you go."
    "I take the present from my pocket and give it to Monika."
    mc "Tacky paper and all."
    "Monika takes the present and begins to unwrap it."
    mc "I know last week..."
    mc "You lost your ribbon."
    mc "That's why you're wearing your hair down."
    mc "You said your parents gave it to you."
    mc "So..."
    "Monika pulls out a white ribbon from the box."
    show monika 1bd
    "Her mouth is wide open."
    mc "I ordered you a new one."
    mc "It's made from some weird material."
    mc "I don't know, the tailor was kinda mysterious about the whole thing."
    mc "He runs a portrait restoration business as well but anyway I--"
    show monika 1be zorder 3 at f42
    m "Thank you, [player]."
    m "This...means a lot to me."
    show monika zorder 2 at t42
    "Monika gives me a hug."
    mc "Ah...well I'm glad you liked it."
    mc "Why don't you try it on?"
    show monika 2bb zorder 3 at f42
    m "Okay, I'll do that!"
    show monika at thide
    hide monika
    "Monika puts the ribbon on her head and ties it."
    # Alternate Reality - Restore to Normal Hair
    $ monika_type = 2
    $ ch12_markov_agree = False
    m "So..."
    show monika 1bb zorder 3 at f42
    m "What do you all think?"
    show sayori 4br zorder 3 at f41
    show monika zorder 2 at t42
    s "Oh my goooood!"
    s "It's so cute!"
    show sayori zorder 2 at t41
    show natsuki 2bj zorder 3 at f43
    n "It looks great."
    n "Just like your old one, Monika."
    show natsuki zorder 2 at t43
    show yuri 2bj zorder 3 at f44
    y "It's hard to imagine you without a bow, Monika."
    y "I think this style definitely suits you more."
    y 2bq "You know, rather than with your hair down."
    show monika 2ba zorder 3 at f42
    show yuri zorder 2 at t44
    m "Thanks, everyone."
    m 2be "And thank you, [player]."
    show monika zorder 2 at t42
    mc "It looks perfect on you, Monika."
    mc "I'm glad we're past that and that you've forgiven us."
    mc "Now we have to face the future."
    show monika 1be zorder 3 at f42
    m "You're right about that, [player]."
    m "That's actually what I was going to say to you when I invited you in."
    m "It's time to stop reminiscing..."
    m "And time to look at what's coming."
    show sayori 1bd zorder 3 at f41
    show monika zorder 2 at t42
    s "Wow, you guys..."
    s "No need to be so phenomenal, it's time to party!"
    show sayori 1ba
    "Sayori presses a button on her phone and music starts playing."
    "She also grabs another piece of cake."
    show sayori zorder 2 at t41
    mc "...It's philosophical, Sayori."
    mc "But you're right, pass me some cake!"
    stop music fadeout 3.0
    $ pause(3.0)
    scene bg m_livingroom_gray
    show sayori 1bk zorder 2 at i41
    show monika 1be_gray zorder 2 at i42
    show natsuki 2bj_gray zorder 2 at i43
    show yuri 2bq_gray zorder 2 at i44
    $ style.say_window = style.window_flashback
    s "So..."
    s "This is how things could have been."
    s "If things were just normal around here."
    s "No powers, no crazy things happening and..."
    s 1bj "...no you."
    s "This is just a look into a reality that could never happen."
    s "No matter how much better it looks."
    s 1bd "It's bittersweet, isn't it?"
    s "Seeing all this happen when the things you've seen have been terrible."
    s "I really wish we could live like this."
    s "We all look so happy."
    s "Just normal people, having fun."
    s 1bl "Obviously not including the part where we missed someone's birthday...!"
    s "But just..."
    s 1bk "Just looking at this makes me feel so sad."
    s "Because how impossible a reality like this is now."
    s 1bh "I hope you had fun..."
    s "But it's time to go."
    s "Back to our timeline."
    s "Back to what awaits us..."
    scene black with dissolve_scene_full
    $ persistent.did_special_event = True
    $ special_chapter = False
    $ pause(1.0)
    $ style.say_window = style.window
    $ renpy.utter_restart()
    return
