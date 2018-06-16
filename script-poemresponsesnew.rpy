label poemresponse_start_new:
    $ poemsread = 0
    $ skip_transition = False
    label poemresponse_loop_new:
        $ skip_poem = False
        if renpy.music.get_playing() and not (renpy.music.get_playing() == audio.t5 or renpy.music.get_playing() == audio.t5c):
            $ renpy.music.play(audio.t5, fadeout=1.0, if_changed=True)
        if skip_transition:
            scene bg club_day
        else:
            scene bg club_day
            with wipeleft_scene
        $ skip_transition = False
        if not renpy.music.get_playing():
            play music t5
    label poemresponse_start2_new:
        $ skip_poem = False
        if poemsread == 0:
            $ menutext = "Who should I show my poem to first?"
        else:
            $ menutext = "Who should I show my poem to next?"

        menu:
            "[menutext]"

            "Sayori" if not s_readpoem and not s_ranaway:
                $ s_readpoem = True
                call poemresponse_sayori_new
            "Natsuki" if not n_readpoem and not n_ranaway:
                $ n_readpoem = True
                call poemresponse_natsuki_new
            "Yuri" if not y_readpoem and not y_ranaway:
                $ y_readpoem = True
                call poemresponse_yuri_new
            "Monika" if not m_readpoem and not m_ranaway:
                $ m_readpoem = True
                call poemresponse_monika_new
        $ poemsread += 1
        if poemsread < 3 or (persistent.playthrough == 0 and poemsread < 4 and not (y_ranaway or s_ranaway or n_ranaway or m_ranaway)):
            jump poemresponse_loop_new


    $ s_readpoem = False
    $ n_readpoem = False
    $ y_readpoem = False
    $ m_readpoem = False
    $ poemsread = 0
    return

label poemresponse_sayori_new:
    scene bg club_day
    show sayori 1a zorder 2 at t11
    with wipeleft_scene
    $ poemopinion = "med"
    if chapter > 11:
        if s_poemappeal2[chapter - 12] > 0:
            $ poemopinion = "good"
    else:
        if s_poemappeal[chapter - 1] < 0:
            $ poemopinion = "bad"
        elif s_poemappeal[chapter - 1] > 0:
            $ poemopinion = "good"
    $ nextscene = "ch" + str(chapter) + "_s_" + poemopinion
    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + str(chapter) + "_s_end"
        call expression nextscene
    return

label poemresponse_natsuki_new:
    scene bg club_day
    show natsuki 1c zorder 2 at t11
    with wipeleft_scene
    $ poemopinion = "med"
    if chapter > 11:
        if n_poemappeal2[chapter - 12] > 0:
            $ poemopinion = "good"
    else:
        if n_poemappeal[chapter - 1] < 0:
            $ poemopinion = "bad"
        elif n_poemappeal[chapter - 1] > 0:
            $ poemopinion = "good"
    $ nextscene = "ch" + str(chapter) + "_n_" + poemopinion
    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + str(chapter) + "_n_end"
        call expression nextscene
    return

label poemresponse_yuri_new:
    scene bg club_day
    show yuri 1a zorder 2 at t11
    with wipeleft_scene
    $ poemopinion = "med"
    if chapter > 11:
        if y_poemappeal2[chapter - 12] > 0:
            $ poemopinion = "good"
    else:
        if y_poemappeal[chapter - 1] < 0:
            $ poemopinion = "bad"
        elif y_poemappeal[chapter - 1] > 0:
            $ poemopinion = "good"
    $ nextscene = "ch" + str(chapter) + "_y_" + poemopinion
    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + str(chapter) + "_y_end"
        call expression nextscene
    return

label poemresponse_monika_new:
    scene bg club_day
    if chapter >= 12:
        if monika_type == 1 and ch12_markov_agree:
            show monika 1ha zorder 2 at t11
        else:
            show monika 1a zorder 2 at t11
    else:
        show monika 1a zorder 2 at t11
    with wipeleft_scene
    $ poemopinion = "med"
    if chapter > 11:
        if m_poemappeal2[chapter - 12] > 0:
            $ poemopinion = "good"
    else:
        if m_poemappeal[chapter - 1] < 0:
            $ poemopinion = "bad"
        elif m_poemappeal[chapter - 1] > 0:
            $ poemopinion = "good"
    $ nextscene = "ch" + str(chapter) + "_m_start"
    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + str(chapter) + "_m_end"
        call expression nextscene
    return

# NO ONES POEMS ARE BAD 9TH DAY (CHAPTER 6)
# YOUR POEMS ARE BAD ON 10TH DAY (CHAPTER 7) IF YOU READ BOOK AND DIDN'T RELOAD
label ch6_y_end:
    call showpoem (poem_y4)
    y 1h "I tried changing my style a little bit with this."
    y 1f "It still has a lot of metaphors but I thought I'd change some things..."
    y "...just to experiment."
    mc "It seems really intense, doesn't it?"
    mc "Or maybe that's just the feeling I'm getting from it."
    y 1v "Intense...?"
    y "I'm not sure that's the word I'd use..."
    y 1t "But...I think I understand what you mean."
    mc "Ah...yeah intense was probably the wrong word."
    mc "I'll try to rephrase it."
    mc "I can still recognize your style within the poem..."
    mc "It's just not something I thought you'd be writing about."
    mc "In a way, it's almost more metaphorical."
    y 3f "Hmm..."
    y "I actually intended for it to be less metaphorical."
    y "Seeing as we've become more comfortable--"
    y 3n "Ah, that is being in the club!"
    y 4c "Not between us personally or anything!"
    y "...I'm so sorry..."
    y "Did I just raise my voice?"
    mc "It's alright Yuri."
    if ch4_name == "Yuri":
        mc "I'm glad we've gotten closer too."
    else:
        mc "I know what you meant."
    y 3q "Okay..."
    y 3l "If you noticed..."
    y "It's actually less metaphorical and more severe than my first poems."
    mc "Ah..."
    mc "Well, I guess I must be bad at recognizing metaphors then."
    mc "Still, it's an impressive poem."
    y 3b "Thank you, [player]."
    return

label ch7_y_end:
    stop music fadeout 2.0
    call showpoem (poem_y22, music=False, paper="images/bg/poem_y1.jpg", img="yuri 2s")
    y 2q "Ahaha..."
    y "It doesn't really matter what it's about."
    y "My mind has been a bit all over the place lately."
    y 2d "It's like finishing that book has gotten me really excited."
    if did_all_tasks:
        y 2f "I-I had nothing to take it out on..."
        y "A-And I was going to..."
        y 2g "...do what I usually do."
        y "But..."
        y 2o "I-I don't know what it was..."
        y "Something...or someone..."
        y "Stopped me."
        y "It was like..."
        y 2p "An invisible force..."
    else:
        y 2q "I've had to take it out on your pen."
        y 2o "Ah--"
        y 2q "That is...y-your bag was open when I fell."
        y "And I, um..."
        y "Took it with me when I left the room..."
        y 2y6 "I really...like...the way..."
        y "It, um..."
        y "Feels."
        y 3p "It really..."
        y "...Um, calmed me down."
    y 2y5 "Ahaha."
    y 3p "I-I'm okay!!"
    y 3o "What did I just..."
    y "..."
    y 4c "...Can we pretend this conversation never happened?"
    y "You can keep the poem, though..."
    return

label ch9_y_end:
    call showpoem (poem_y3b)
    "Finishing the poem, I start to hand it back to Yuri."
    "But instead of taking it from me, she looks away."
    y "..."
    y 3pv "Do you...dislike it?"
    mc "Ah--no, of course not."
    mc "I just...don't really know how I should respond."
    "Despite Yuri's poems usually being cryptic, it wasn't hard to figure out what this one was about."
    y 2pv "I-I don't know if I'll be able to explain this one..."
    mc "That's fine."
    mc "I understand this one."
    y 2pi "..."
    "Yuri is having an even harder time speaking than usual."
    mc "Does this one...mean a lot to you?"
    "Yuri nods."
    mc "I'm not really good with words, but..."
    mc "I'm happy that you shared it with me."
    mc "So, thank you."
    mc "And I hope we keep spending time together."
    mc "I know today could have been different but..."
    y 2pq "I-It's okay..."
    y "There's always next time..."
    y 2ps "...right?"
    mc "Yeah."
    "I once again try to hand the poem back to her."
    "But instead, Yuri gently takes my hands and pushes them back toward me."
    "I hesitate in response to her warm touch."
    y 1v "You can..."
    y "Um..."
    y "The poem is..."
    "Once again, Yuri fails to form a complete sentence."
    mc "You mean I can keep it?"
    "Yuri nods."
    mc "I'd love to."
    "Yuri visibly smiles."
    y 2pu "You're so..."
    y "You're so nice, [player]..."
    y "I know I haven't always been the best person..."
    y 2pv "Or been very good with people in general but..."
    mc "Yuri, it's okay."
    mc "I know that wasn't really you."
    y 1s "I guess...we should move on before someone says something."
    y "But I'm sure we can talk again later..."
    mc "Yeah."
    mc "I'm sure we will."
    "With that, Yuri timidly smiles at me, and I return to my seat so I can put her poem away."
    "The extra time that Sayori gave us to share poems was actually pretty helpful here."
    "The conversation between Yuri and I went due to how she acts when she's around me."
    "Not that I mind how Yuri speaks, but it's nice to have enough time to actually talk."
    return

label ch12_y_end:
    if visited_yuri_hospital:
        call showpoem (poem_y5b, img="yuri 2pe")
        mc "That's the raccoon from one of your earlier poems, isn't it?"
        y 2pq "Ah..."
        y "I was hoping you wouldn't notice that."
        mc "Why not?"
        y "It's just not something I thought you would remember."
        y 2pu "But..."
        y "In a way..."
        y "I'm glad you did."
        mc "It sounds like the raccoon is going to die at the end..."
        mc "But that's just a metaphor for something else, isn't it?"
        y 3ps "Very observant of you, [player]."
        y "The rectification is sort of like a cure."
        y "I'm not sure you understand what I'm talking about but..."
        mc "Is the cure related at all to your cuts?"
        y 3pv "Ah..."
        y "Well, I was hoping it wouldn't be that obvious but..."
        y 3ps "...yes."
        mc "I think that's great."
        y 3pt "You do?"
        mc "Yeah, now that you're free from..."
        mc "The sickness, I guess is the best way to describe it."
        mc "Well, you can finally live life."
        y 2pq "Ahaha, I'm not sure life works like that..."
        y "But I appreciate you caring."
        y "When I first met you, I really thought that you wouldn't choose me of all people..."
        y 3pt "And when you wrote your poems for Monika in the first week, I..."
        y "...almost gave up hope that you would choose me."
        y 3pv "I had to try to learn to be content with being alone but it seemed impossible after I'd met you."
        y "So..."
        y 3ps "I really want to thank you."
        y "For helping me through my problem and making me stick with it..."
        y "Really, for everything, [player]..."
        y "I couldn't have done it without you."
        mc "I think you're giving me too much credit, Yuri."
        mc "You helped yourself too so you should feel proud of it..."
        y 3pt "D-Do you really think so?"
        mc "Yeah, I do."
        y 3pv "..."
        y 3ps "T-Thank you so much."
        "Yuri's eyes light up."
        y "I'll see you later, okay?"
        mc "I can't wait."
    else:
        call showpoem (poem_y5, img="yuri 2po")
        mc "That raccoon seems kinda familiar. Is it from one of your earlier poems?"
        y "Ah...you noticed that, did you?"
        y 2pq "I didn't want to make it too obvious, but it seems you figured it out pretty quickly."
        mc "Is there any particular reason for that?"
        y "Not particularly..."
        y "I was going to ask you afterwards what you thought about it and if you understood the metaphors."
        y 2ps "But you already know so..."
        mc "That doesn't mean we can't discuss it, does it?"
        y "I suppose you're right."
        y 3pv "There isn't really much to discuss though..."
        mc "Actually, I was getting this weird feeling from your poem while I was reading it."
        mc "I'm not sure if you intended that or not."
        y "What feeling would that be?"
        mc "I'm not really sure but it's almost like..."
        mc "Something is unfinished?"
        mc "Not about the poem itself but...something more?"
        mc "I don't think that makes sense, does it?"
        y 3pu "I think I understand."
        y "I also think I understand your reasons for thinking like that."
        y "You're talking about how the raccoon is affecting the person in the poem, right?"
        y 3pf "How they're 'unfinished' with feeding it?"
        mc "I guess...?"
        y 3ps "If you're worried in any way, then please don't be."
        y "It's all under control now, I think..."
        mc "What's under control?"
        y 2pq "Um..."
        y "Nothing."
        y "Thanks for sharing your poem, [player]."
        mc "You're welcome...?"
    return

label ch13_y_end:
    if visited_yuri_hospital:
        call showpoem (poem_y6b, img="yuri 3pa")
        y "I really should thank you again, [player]."
        y 3pb "You've brought a light into my world I never would have seen without you."
        mc "Ah...I wouldn't go that far."
        mc "But you're welcome, I guess."
        y 3pf "I'm serious..."
        y "I don't think I could be with anyone else."
        y "You're the only one that's gotten this close to me..."
        y 3pv "Even my parents would..."
        mc "It's okay."
        mc "I'm glad I got close to you as well, Yuri."
        y 2ps "You know..."
        y "That poem I made was talking about you."
        "I could sort of tell it was directed at someone."
        "I just wasn't sure if it was me."
        y 2pv "I really couldn't feel the point of writing anymore, [player]."
        y "I know I said it already but I have to emphasize it."
        y 2ps "But thinking about you when I wrote it..."
        y "And all the things we've done together."
        y "It brought back that feeling of writing."
        y 2pu "The longing to impress you."
        mc "That's..."
        mc "I don't really know what to say."
        y 2pv "..."
        y "D-Do you hate me for it?"
        mc "No, of course not!"
        mc "If I'm what's making you come to your senses then I'll happily take that role."
        show yuri 3pu
        "Yuri looks at me and smiles shyly."
        y "T-Thank you..."
        y 3ps "I know it's selfish to say but I'm glad you chose me instead of anyone else..."
        y "Natsuki is dealing with a hard time right now and I don't know what to do..."
        y 3pq "I would feel like a terrible person...if it wasn't for you."
        y "You just make it seem like all my troubles just aren't there."
        mc "What happened to Natsuki wasn't your fault or mine."
        y 3pt "I know...I just feel bad that I care more about you than her."
        y "Especially given her current situation."
        mc "Ah..."
        "I really don't know how to respond to {i}that{/i}."
        "I guess I'll try to change the topic a little bit."
        mc "We can't change what happened to her but the least we can do it help her out."
        mc "So both of us and the rest of the club can do that, together."
        y 3pu "Y-Yeah..."
        y "Thank you for sharing your poem and talking to me."
    else:
        call showpoem (poem_y6, img="yuri 3pe")
        mc "I don't know what you mean."
        y 3pf "W-What?"
        mc "This poem is just as good as any of your other poems."
        mc "If not, better."
        y 2pg "Ah...that's kind of you to say."
        y "I'd have to disagree on that."
        mc "How come?"
        y 1h "I already said I couldn't put all the feelings I wanted to in it."
        y "It's as if I just put those words there so they could form a sentence."
        y "Not so that I could properly convey what I was feeling."
        mc "Your poem makes it seem like you're conveying what you're saying right now."
        y "I guess..."
        mc "I think you're doing fine, Yuri."
        mc "Maybe it's just too much poem writing like I said."
        y 1w "I hope so..."
        mc "Maybe tonight you'll feel differently."
        mc "Things can still change, you know?"
        y 2q "Yeah..."
        "Yuri doesn't sound convinced."
        y "Thanks for sharing, [player]."
    return

label ch6_n_end:
    call showpoem (poem_n4)
    n 1c "So..."
    n "What do you think?"
    mc "Natsuki, does this poem reflect what you think of the club?"
    mc "It seems kinda sad..."
    n 2e "Jeez, where did you get that idea from?"
    n 2b "Sayori, Yuri and Monika are my friends."
    n "I just felt like writing a poem about the sea."
    n 5e "And it's easier to write about the sad things then it is about the happy things."
    mc "I'm your friend too, right?"
    if ch4_name == "Natsuki":
        n 1q "W-Well..."
        n 1s "I guess so..."
        mc "That's a relief."
    else:
        n 1o "H-Huh?"
        n "T-That's up to you, isn't it?"
        n 1s "Do you think that {i}I'm{/i} your friend?"
        mc "Yeah, I do."
    n 5g "Hmph."
    mc "So, {i}friend{/i}, care to tell me what inspired you to write this poem?"
    n 1e "If you're going to mock me then get out of here!"
    mc "Sorry!"
    mc "I'd still like to know your inspiration though."
    n 1c "Hmm..."
    n "Alright, I'll tell you."
    n "Last week, it felt like something happened."
    n "I'm not sure what but it felt like a good thing."
    n "Like all my friendships were looking up."
    n 1q "Whatever that means..."
    mc "I get it."
    "I felt that change as well."
    "I'm not sure if it's a good thing but I'm hoping it is."
    return

label ch7_n_end:
    call showpoem (poem_n5)
    n 2e "Do you get it?"
    mc "Sort of..."
    n 2c "You know what I said yesterday?"
    n "The feeling I was getting disappeared after we shared poems."
    n "But it came back again when I went into the club."
    n "It doesn't feel so good anymore..."
    n "And I have no idea what it is..."
    n 2g "But I've been feeling hopeless since the meeting today."
    n "I'm really starting to think no one cares about me anymore."
    if n_appeal > 0 and (not read_book or did_all_tasks):
        n "Well..."
        n 2i "Except you."
        n "..."
        n 3k "Why is everyone acting so different?"
        n "This isn't normal."
        n 3m "You have to have noticed it."
        n "Do you know why everyone's focusing on Yuri?"
        n "Is there something I'm missing?"
    else:
        n 2q "Everyone's been really cold lately..."
        n "And I don't know what's going on with Yuri."
        n 2m "But she's being really aggressive all of a sudden."
        n "She isn't normally like that."
        n 2r "And it really hurts when she starts acting that way towards me."
        n "I thought she and I were friends..."
        n "But during this week..."
    n 2s "Well...never mind."
    n "There's no point to this."
    return

label ch9_n_end:
    call showpoem (poem_n6)
    n 2k "I was kinda hoping to tell a story with this poem."
    n "I don't really know if it works with my writing style but..."
    mc "It seems like a sad story."
    mc "It's kinda metaphorical for one of your poems, isn't it?"
    n 2p "E-Eh?"
    n "What's wrong with that?"
    mc "Nothing..."
    mc "It's just a little strange seeing your style combined with metaphors."
    n 1q "..."
    n "This isn't the only poem that was like that, [player]."
    n 1s "Do you remember my second one?"
    mc "Vaguely..."
    n 1u "Ugh..."
    n "You're hopeless."
    n 1k "It was about a person called Amy that liked spiders."
    n "She was pretty much a normal person but the only difference was that she liked spiders."
    mc "Are you saying you're like Amy...?"
    n 4i "No..."
    n "I'm saying we're all like Amy."
    n "People will judge just because we like a certain thing..."
    n "Even if we're just like them in the end..."
    mc "I think I do remember you talking about this last week."
    mc "It's like the memories are flooding back."
    n 4h "..."
    n "Something isn't right with what you just said..."
    n 4g "Whatever, we haven't even talked about my poem for today yet."
    mc "Ah..."
    mc "Well, I think it's about someone important becoming a bad person...?"
    mc "It's like the person was sweet before and now they're bitter?"
    mc "I'm guessing that sweet and bitter are metaphors for something else."
    mc "That's what I'm getting from it..."
    if n_appeal >= 3:
        n "..."
        n "Well, you're sort of right..."
        n 4h "Actually..."
        n "Can I tell you something?"
        mc "Sure, I'm listening."
        n "The poem I wrote..."
        n 4q "It's got a lot to do about me..."
        n "I don't really know what why I'm telling you this."
        n "It's not something I'd just tell anyone."
        n 1s "But you seem to understand me the most..."
        mc "Your secret is safe with me."
        n "..."
        n 1r "Well, that's why I told you!"
    else:
        n "Hmph..."
        n "Whatever..."
        n 4o "It's not like you care at all."
        mc "What?"
        "Did I say something that caused her to lash out like that?"
        mc "Is something wrong?"
        n 4q "Nothing is wrong!"
        n "Just go already."
        n 4r "You've finished reading my poem, haven't you?"
        mc "But you're the one who wanted--"
        n "W-What?!"
    "Maybe Natsuki is dealing with problems too."
    "I hope it's not as intense as what Yuri was dealing with."
    return

label ch12_n_end:
    if n_appeal >= 4 and check_whole_house:
        call showpoem (poem_n7b,img="natsuki 2q")
        mc "I hope I haven't been inspiring your poems too much."
        mc "I really like your style and it wouldn't be right if you changed because of me."
        n 2p "H-Huh?!"
        n "W-What are you talking about?"
        n 2r "I-I didn't write this poem about you or anything..."
        mc "Are you sure?"
        n 4w "Y-Yeah!"
        "She sounds unconvincing."
        mc "Well, if you say so."
        n "And besides...!"
        n "This poem is written in my sort of like my style!"
        mc "Are you telling me or yourself?"
        n 1o "Uuuuuu...!"
        n "Why are you being like this?!"
        mc "I'm just concerned for you, that's all."
        mc "After what we talked about yesterday..."
        mc "Well, it's kinda hard not to be."
        n 1r "..."
        "Natsuki's expression suddenly changes."
        n 1q "I-It was nice having you around, [player]..."
        n "Even if it was only for a little bit..."
        n 1n "I'm glad you were there to talk to."
        mc "That's okay, everyone needs to let it all out at some point."
        mc "It's better than keeping it all bottled up inside, right?"
        n 1m "Yeah..."
        n "L-Look, I'm sorry for being rude just before..."
        n "But I really l--"
        n 1s "{i}(Wait, what am I saying...?){/i}"
        n "{i}(What if he doesn't feel the same...?){/i}"
        mc "You really what?"
        n 1u "Nothing..."
    else:
        call showpoem (poem_n7)
        mc "Are you hiding something else from me?"
        n 2c "Huh?"
        n "Where did that question come from?"
        mc "After reading your poem and what happened yesterday..."
        mc "It's pretty obvious that it's about hiding something."
        n 2f "Well, yeah!"
        n "We all hide things we don't want other people to know."
        n "Because otherwise, they'll judge us..."
        n "And it'll only make everything harder."
        mc "That doesn't really answer my question..."
        n 2r "What do you want me to say?"
        n "I'm allowed to have privacy, aren't I?"
        mc "I just wanted to talk about the message behind your poem."
        mc "If there's anything you want to tell me, I won't tell anyone."
        mc "I know we didn't really get to finish our conversation yesterday..."
        n 4n "No..."
        n "Well, maybe not now..."
        n 4s "It's not a good time, okay?!"
        mc "That was three different responses."
        n 4o "I-Is that a problem?!"
        n "Look, if you're just going to make fun of me, then go away."
        mc "That wasn't my intention."
        mc "I just want to know if anything else is wrong with you, that's all."
        mc "Something about your poems..."
        mc "Well, I guess they give a bad feeling?"
        mc "Especially after yesterday..."
        mc "Maybe you should just tell me instead of bottling it all up inside."
        "Natsuki looks at me for a moment."
        n 4m "There's nothing else you need to know, okay?"
        show natsuki 2l
        "Natsuki shows me an unconvincing smile."
        n "See, I'm fine."
        n 2i "Now you can go already."
    return

label ch6_s_end:
    call showpoem (poem_s4)
    s 1d "It's a little different from the poems you know me for..."
    s "But something happened yesterday that made me think..."
    mc "You also forgot to write one yesterday."
    mc "So you did it during the day, didn't you?"
    s 1l "I'm really that bad at hiding it?"
    s 1d "B-But I'm serious about what I said!"
    s "I didn't really expect it to affect how I'd write my poems so much."
    s "It's odd how your life can change in an instant, isn't it?"
    mc "I'm not really sure I get what you mean."
    if sayori_confess:
        mc "Even if we're a couple, it feels like not much has changed."
    else:
        mc "After I told you how I felt about you..."
    mc "I don't think I've really changed how I've written my poems."
    mc "I mean I might have, but that's because today I didn't expect us to be sharing poems."
    mc "You clearly didn't at least."
    s 1h "Aw, my poem wasn't that bad..."
    s 1k "I even used my lunch time to write it..."
    mc "I never said it was bad."
    mc "In fact, just the opposite, it's actually really well done."
    mc "It's got a mix of bunch of different styles that I think suit you."
    s 4d "Really?"
    mc "Yeah..."
    mc "To be honest, I thought you'd drop this whole poetry thing in a week."
    mc "But you stayed passionate for the club."
    s "Everyone in this club means so much to me."
    s "There's no way I wouldn't be passionate about it."
    "Seeing Sayori so determined is such a weird thing."
    "I've always known her for being..."
    "Well...Sayori."
    "This side of her is just different, in a good way."
    return

label ch7_s_end:
    call showpoem (poem_s5)
    s 2d "Feeling any better?"
    s "I tried to make it more happy than sad this time."
    mc "I can see that."
    mc "It almost seems excessive."
    s 2m "E-Excessive?"
    s "There's nothing wrong with being happy, is there?"
    mc "Not really."
    mc "It's just weird seeing you focus on the happy side of things."
    mc "You're usually known for your more..."
    mc "What's the word for it...?"
    s 1d "Bittersweet?"
    mc "Yeah, that."
    mc "You're usually more of a bittersweet writer."
    s "I was just thinking that if I write happy poems..."
    s "Then maybe everyone else will be happy too!"
    mc "If only that were the case."
    mc "But I don't think the world works like that Sayori."
    s 1k "Yeah...I know."
    s "But it's what I'm dreaming will happen one day."
    if y_ranaway:
        show sayori 1k
        show yuri 1s zorder 3 at f31
        y "I'm back..."
        y "Did I miss anything?"
        show yuri zorder 2 at t31
        show sayori zorder 3 at f32
        s 2d "Not really..."
        s "But you know we've already started sharing poems."
        show sayori zorder 2 at t32
        show yuri zorder 3 at f31
        y "Y-Yeah..."
        y "It was really urgent..."
        y 2v "I-I'm sorry for the sudden notice..."
        show yuri zorder 2 at t31
        show sayori zorder 3 at f32
        s 2j "That's okay Yuri!"
        s 2d "We still have lots of time, so you can take as long as you need!"
        show sayori zorder 2 at t32
        show yuri zorder 3 at f31
        y 1s "Alright..."
        y "Thanks, Sayori."
        y "I suppose I should go get my poem now."
        show yuri zorder 1 at thide
        hide yuri
        $ y_ranaway = False
    return

label ch9_s_end:
    call showpoem (poem_s6)
    mc "I don't think a fruit is going to make someone happy."
    mc "Unless that person is a strawberry fanatic."
    s 4r "Ehehe~"
    s "You didn't really get the message of the poem, did you?"
    mc "Well, I kinda get it..."
    mc "It's like someone was feeling sad but it was fixed by a fruit...?"
    s 4q "Not just any fruit..."
    s "A strawberry!"
    mc "I'm not really sure why that matters..."
    mc "What if the person didn't like strawberries?"
    mc "Wouldn't that ruin everything?"
    s 2n "Well...I suppose it would."
    s 2q "I guess it doesn't have to be a strawberry..."
    mc "I thought the strawberry was just a representation of something."
    s 1l "That's what it was meant to be..."
    s 1j "Why didn't you just say that at the beginning instead of going on about fruit?"
    s "You're such a meanie, [player]!"
    mc "Ahaha, sorry."
    s 1d "I went for a sad start but a happy ending this time."
    s "It feels good writing like this."
    mc "I guess giving people a happy ending would do that..."
    mc "But what's made you write like this?"
    mc "Your last poem was pure happiness whereas your other ones..."
    s 1a "I've just become more adequate."
    mc "Adequate?"
    s 1c "Being more determined, you know?"
    mc "Are you sure you're not thinking of adamant?"
    s 1a "Adamant! That's the word!"
    mc "Some things never change, do they?"
    s 1l "Heeey, what's that meant to mean?"
    mc "Even if you're the president of this club now..."
    mc "You're still a bit clumsy."
    s 1h "W-What...?"
    s "What did you just say?"
    mc "Ah..."
    mc "I didn't mean that as an insult or any--"
    s 1j "No, before that..."
    mc "That you're the president of the club now...?"
    s 1k "But..."
    s "Wasn't I always the president of this club?"
    mc "Um..."
    mc "Yeah, I guess you were."
    mc "Sorry, I guess that was poor word choice on my part."
    s "This is not good at all..."
    mc "What do you mean?"
    s 1l "Nothing!"
    s "It's not your fault..."
    s 1q "Anyway, we're done talking..."
    s "So..."
    "Is something wrong with her?"
    "Maybe it's something I said..."
    if sayori_confess and sayori_dumped:
        "I hope it's not because we broke up today..."
    return

label ch12_s_end:
    if sayori_confess and not sayori_dumped:
        call showpoem (poem_s7c)
        mc "This is a pretty interesting poem you wrote, Sayori."
        s 1c "You think so?"
        mc "Yeah, it feels like an emotional message or something."
        mc "What were you thinking when you wrote it?"
        s 1d "Well, it's kinda complicated..."
        mc "You can tell me."
        mc "Besides, it'll let me understand you better especially since you're my girlfriend."
        s "A-Ah--"
        mc "What's wrong?"
        s 1l "I-I didn't really expect you to say that all of a sudden, you know?"
        s "Ehehe, sorry. Don't worry about me, [player]."
        mc "It's hard not to sometimes."
        s "Yeah..."
        show sayori 1q
        "Sayori beams."
        s "Well, you want to know what I was thinking when I wrote it?"
        mc "Yeah, I do."
        s 1d "I was thinking of how terrible some people's life must be right now."
        s "Having your feelings and who you are as a person taken away like that..."
        mc "Eh? Like what...?"
        s 1f "And not being able to do something because you don't know what'll really happen..."
        mc "I'm not sure I understand..."
        s 1l "I told you it was complicated."
        mc "You're right about that..."
        mc "Those are some weird things to be thinking about though."
        s 2d "Mhm..."
        s "But it's been what's on my mind."
        s "Thanks for talking to me, [player]."
        mc "Ah, not a problem."
    elif s_appeal >= 4:
        call showpoem (poem_s7b)
        s 2d "There's lots of different feelings in that one, [player]."
        s "So I hope you sorta understand what I'm trying to say."
        mc "This is a pretty complicated poem, Sayori."
        mc "Is there some kinda message behind it?"
        s 1c "You can't tell?"
        s "You've been writing your poems like mine and you can't tell?"
        mc "It's a lot more complicated than your previous poems..."
        mc "Sorry if I can't really comprehend what you're trying to convey."
        mc "Though this talk of a past life is ringing some bells and I don't really know why."
        mc "It's almost like I was a part of this past life."
        s 1l "Ehehe, what are you talking about?"
        mc "Well, what if we had a life before this one?"
        mc "Where everything was simpler, like in your poem."
        s 1k "..."
        mc "I don't really know what I'm saying. I'm just trying to understand your poem."
        s 1d "Well, you definitely have an interesting way of understanding it."
        s "Though I guess I can't really blame you..."
        mc "Let me ask you something, Sayori."
        s 1c "What is it?"
        mc "Are you the person in the poem?"
        mc "The one that's feeling selfishness, happiness and sadness?"
        s 1d "Well..."
        s "I'll leave that up to you, [player]."
        s "You can take my poem however you like~"
        mc "It's just..."
        mc "Those last couple of lines..."
        s 1a "It could just be a coincidence..."
        mc "I suppose..."
        "I'm not really convinced that Sayori is telling me everything."
        "I wonder what she's hiding and why..."
    else:
        call showpoem (poem_s7)
        mc "Do you use a lot of effort when you're writing these poems, Sayori?"
        s 1c "Hmm...?"
        s "Why do you ask?"
        mc "It's the title of your poem."
        s 1a "Well, yeah!"
        s "Of course I use a lot of effort when I write."
        s 2b "I have to think really hard on what I want to say in my poem and the sort of meaning I want to put in it."
        mc "That's quite thoughtful of you."
        s 2d "Eh? Well, the president has to set a good example, you know!"
        s "And besides, it's not just in writing poems that I put effort in..."
        s "It's really everything I do for this club."
        mc "That's interesting."
        s 2c "What is?"
        mc "Well, you said that you put effort into everything you do for this club..."
        s "Yeah...?"
        mc "Do you do it for anything else?"
        s 2l "W-What do you mean? You should know the answer to that question since you know me better than anyone else!"
        mc "So no...?"
        s 1j "[player]..."
        mc "Sorry."
        mc "Still, I'd like to know if the person you're talking about in the poem is in the club."
        mc "It's a girl, so it would make sense if it was someone in the club."
        s 1l "W-What?"
        s "T-That's got nothing to do with it!"
        s "You're completely misunderstanding what I'm trying to say, [player]?"
        mc "Oh...really?"
        s 1q "Yeah!"
        s "It's just about being happy even though it's hard when you have other things to worry about."
        mc "Well, that's a lot more simple than what I was thinking..."
        s "Ehehe~"
        mc "Thanks for sharing, Sayori."
        mc "Just make sure you look out for your own happiness too, okay?"
        mc "I can't always look out for you, even with how hard I try."
        s 1d "Thanks, [player]. That means a lot..."
    return

label ch13_s_end:
    if sayori_confess or s_appeal >= 4:
        call showpoem (poem_s8b)
    else:
        call showpoem (poem_s8)
    s "So what do you think?"
    mc "I don't know what to say."
    s 2c "Huh?"
    mc "Are you trying to send me a message with this poem, Sayori?"
    mc "It seems pretty personal."
    s 2l "What makes you think that?"
    mc "I don't know..."
    mc "It feels like the poem is talking about putting up a fake personality."
    mc "Then putting up with it just because."
    s "I guess you could look at it that way."
    s 1a "It was just what was on my mind so you shouldn't take it so seriously."
    mc "Really? It almost seems like you're trying to hide something."
    if sayori_confess and not sayori_dumped:
        mc "I don't want to presume since you're my girlfriend but..."
    else:
        mc "I don't want to say anything since we're best friends but..."
    s 2h "[player], I didn't have to write about this topic."
    s "I didn't know it would make you feel so uncomfortable..."
    s 2k "Or maybe you just hate my poem."
    mc "I don't hate it, Sayori."
    mc "I'm just really concerned with what's going on."
    mc "I want to know if you're okay."
    s 2d "I'm fine, see?"
    show sayori 4q
    "Sayori gives a wide smile."
    s 4d "It is nice you're worried about me though."
    s "It makes me wonder if you worry about everyone else..."
    mc "Of course I do."
    mc "After what happened with Yuri and then with Natsuki yesterday..."
    mc "It's hard not to worry about everyone."
    s "Yeah..."
    s 4a "Yuri with her...personality was the first thing, wasn't it?"
    mc "First thing for what?"
    s "That made you realize this club isn't all just about literature."
    mc "I didn't join the club just for the literature, Sayori."
    mc "You should know that."
    s 2d "Ehehe, I did know that..."
    s "You joined because of the people in it..."
    s "And you're still here."
    show sayori 1g
    "Sayori shows a solemn look."
    s "Do you have what you want, [player]?"
    mc "What?"
    s 1h "From the club."
    s "You've made new friends, become a better writer..."
    if visited_yuri_hospital:
        s "...and even become closer to Yuri..."
    elif sayori_confess and not sayori_dumped:
        s "...and you have me as your girlfriend..."
    s 1f "So I'll ask again..."
    s "Do you have what you want?"
    "I can't really answer that question."
    menu:
        "But I have to say something."
        "Yes.":
            pass
        "No.":
            pass
    s 1k "I see..."
    s "Your answer doesn't really matter..."
    s "I was just curious, that's all."
    show sayori 1a
    "Sayori brings back her normal, carefree smile."
    s "In any case, thanks for talking to me [player]."
    mc "Any time, Sayori."
    return

label ch14_s_end:
    return

label ch6_m_end:
    call showpoem (poem_m6)
    m "What do you think, [player]?"
    m 1e "It might be a little difficult to comprehend."
    m "If it is, I'm sorry I tried something a little different today."
    m 1a "But I hope that you of all people can see what I'm trying to convey."
    mc "Well, abstract poems are all about having different meanings right?"
    mc "From my point of view, the poem is about some sort of fresh start."
    mc "Like the world was in some sort of apocalypse because of someone or something..."
    mc "Then it got reset, with a watcher taking care of everything...?"
    m 1l "Well, that's definitely one way to interpret it."
    m "If you noticed, I put lots of spaces into it which indicate the timing between words and lines."
    m 1c "But I already told you that last week, so I'm sure you know about it already."
    mc "Is there something that's caused you to change your writing a little?"
    mc "Maybe some new inspiration I don't know about?"
    m 3j "Ahaha, let's just say I've had {i}a new epiphany{/i}~"
    mc "..."
    m 1a "Anyway..."
    m 3b "Here's Monika's Writing Tip of the Day!"
    m "If you're having trouble increasing your writing skills, then try keeping a journal."
    m "You can put your own personal thoughts into it and whatever else comes into your mind."
    m "Who knows, you might even find some inspiration in the future from your past self."
    m "By doing this, you're not only improving your writing but also your personal development."
    m 3k "...That's my advice for today!"
    m "Thanks for listening~"
    return

label ch7_m_end:
    if m_appeal >= 2 and did_all_tasks:
        call showpoem (poem_m7b)
        "I'm getting a sinking feeling from reading that poem."
        "It wasn't because of the quality."
        "In fact, it was pretty good."
        "But it's like she's trying to send a message."
        "Or maybe I'm reading too far into it."
        m 2c "Nothing to say about it, [player]?"
        mc "Sorry, I was just deep in thought."
        m 2e "I hope you have a good interpretation of it this time."
        m "I've made sure to put in many ways you could interpret it..."
        m "But some are intentionally left clear to the reader."
        mc "Well..."
        mc "That explains why I thought you were trying to send a message."
        mc "I don't really get it though."
        mc "That said, it was a really good poem."
        m 2a "You think so?"
        m "I worked really, really hard on it."
        m "And I know it might be less abstract than what you know me for."
        m 2b "But I'm glad you liked it."
        mc "I'm not entirely sure how to interpret the message you're trying to send."
        mc "So I can guess that means your abstract tone is still showing through."
        m 2e "Ah...I see."
        m "Anyway..."
        m 3b "Here's Monika's Writing Tip of the Day!"
        m "Sometimes when you're looking over your work, you might...um..."
        m 3g "...what's happening to me?"
        $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
        if not list(set(process_list).intersection(stream_list)):
            if currentuser != "" and currentuser.lower() != player.lower():
                m "[currentuser]...I'm so scared..."
        m "Why am I getting this terrible feeling?"
        m 3f "Promise me you'll stay with me..."
        m "Promise me you'll get me through this..."
        m "Can you even hear me anymore?"
        $ renpy.call_screen("dialog", "Please help me.", ok_action=Return())
    else:
        call showpoem (poem_m7)
        mc "That was..."
        mc "The best abstract poem I've ever seen!"
        m 2a "Thanks, [player]."
        m "I worked really, really hard on it."
        m 2b "So I'm glad you enjoyed it so much."
        mc "It's really weird..."
        mc "I almost have no clue how to interpret your poem."
        mc "Like I have lots of different ideas but none of them really fit."
        m 3a "That's how you know that something abstract is good."
        m "You can interpret it in so many different ways, despite none of them really matching."
        m 3b "I intended on this one being like that so that it's really open to interpretation."
        m "There's not really a point in trying to explain it in that case."
        m "Seeing as you've written at least a few abstract poems by now..."
        m 3e "I hope you understand what I mean here."
        mc "Yeah, I think I do."
        m "Anyway..."
        m 3b "Here's Monika's Writing Tip of the Day!"
        m "Sometimes when you're looking over your work, you might miss out on some details."
        m "You might have been proofreading it for a good hour but there's a glaring mistake you can't spot."
        m "Try to find another person to have a look at it to ensure you didn't miss anything."
        m "If you can't do that, then leave it for a couple of hours and come back."
        m "You'll soon find something that you missed because you now have a clear mind."
    m 3k "...That's my advice for today!"
    m "Thanks for listening~"
    return

label ch9_m_end:
    if m_appeal == 3 and did_all_tasks:
        call showpoem (poem_m8b)
        m 2a "So, what do you think?"
        mc "It seems kinda...dark?"
        m 2e "Ah...I suppose it is in a way."
        mc "Any reason in particular for that?"
        m "If you want the truth..."
        m 2f "It's because of a certain piece of literature..."
        mc "The book again...?"
        "Monika nods."
        mc "I already got rid of it, so there's no need to worry about it."
        mc "Even if I don't fully understand what the big deal is."
        m 2g "I can't really comprehend it either..."
        m "But we should move away from that."
        m 2e "I'd rather not talk about it for any longer than we need to."
        mc "Yeah, I got off topic there..."
        mc "About your poem though..."
        mc "It seems like your writing it from a certain perspective."
        m "I guess you could say that."
        m "I'm trying to convey my thoughts a little more."
        m "To keep you up to date."
        "Monika smiles directly at me."
        mc "Keep me up to date with what?"
        mc "I'm not sure I understand what you're getting at."
        m 2a "Ahaha, perhaps I said too much."
        m "Hmm..."
        m 3b "Can I ask you something?"
        mc "Sure, go ahead."
        m 3c "Do you feel any changes in your behavior?"
        m "Maybe you've done something differently or acted different to how you would normally..."
        mc "Not that I know of..."
        m 3b "Well, that's a relief."
        m "You're still you, then?"
        mc "I guess..."
        mc "Why do you ask?"
        m 3f "Well..."
        m "You know what happened yesterday..."
        m "We don't want another thing like that to happen."
        mc "You're right about that..."
        mc "But I don't think that will be a problem for me though."
        m 3e "Just in case..."
        m "You let me know if you're feeling different, okay?"
        mc "Okay, you can count on it."
    else:
        call showpoem (poem_m8)
        m 2a "So, what do you think?"
        mc "It seems kinda..."
        mc "I don't know, sinister, maybe?"
        m 2e "Ah...I suppose it is in a way."
        mc "Any reason in particular for that?"
        m "Well..."
        m "I can't really tell you."
        mc "Alright..."
        m 3b "I can tell you more about the actual poem though..."
        m "It's written from a certain perspective..."
        m "Like it's telling you the thoughts of someone."
        mc "Do I know this someone?"
        mc "They seem...evil, maybe?"
        mc "Just the way it's written indicates they have plans for the world."
        mc "Or maybe that's just your abstraction doing that."
        m 3e "Ahaha, it does seem a bit like that..."
        m "It's probably just my abstraction doing that."
        show monika g4
        m "Hmm..."
        m "So you're still hanging on...?"
        mc "What do you mean?"
        m 2l "Ah, sorry!"
        m "I was talking to myself."
        mc "Are you feeling alright, Monika?"
        mc "I don't know if it's just me but you've been acting a little strange lately."
        m 2a "I'm fine, [player]."
        "Monika smiles sweetly."
        m 3c "There is something else I want to talk to you about..."
        if gave_book_to_monika:
            m 3e "I want to thank you for giving me the book."
            m "It's finally been dealt with."
            mc "What do you mean?"
            m "I've done what I need to with it."
            m "Now we only need to wait..."
            mc "What exactly are we waiting for?"
            m 2a "Ahaha, you'll see~"
            m "It might take a while for it take full effect..."
            "Something about how Monika's talking almost sounds..."
            "...malicious?"
            "But that's probably just my imagination."
            m "It probably is, [player]."
            mc "Huh?"
        else:
            m 3f "That book you threw in the bin yesterday..."
            mc "What about it?"
            m 3a "Ahaha, you might want to try harder to get rid of it."
            mc "I'm not sure I understand..."
            m "Never mind."
            m 3b "I should be thanking you, actually."
            mc "For what?"
            m 3e "For being so careless with the b--"
            m 3l "Um...!"
            m "I mean..."
            m 3e "For being a good friend, obviously."
            m "You're looking out for my wellbeing..."
            m "You remembered that I wanted you to get rid of the book and you did."
            mc "Well, it's what friends are for."
            mc "But I'm still not sure what the significance of it is..."
    m "Anyway...!"
    m 3b "Here's Monika's Writing Tip of the Day!"
    m "Sometimes when you see something interesting you might take inspiration from it."
    m "It's always good to keep reading and expanding your knowledge..."
    m "But you shouldn't fill your own writing with the ideas of others."
    m "If you do that, then you'll never learn to be properly creative."
    m "Your writing will end up being a copy of someone else's rather than your own."
    m "So try to be aware of what you're including from your subconsciousness."
    m 3k "...That's my advice for today!"
    m "Thanks for listening~"
    return

label ch12_m_end:
    if monika_type == 0:
        call showpoem (poem_m9c)
        m 1e "It's a really scary feeling, isn't it?"
        mc "What is?"
        m "Fighting to stay in control of yourself."
        m 1o "Relying on someone to make the right decisions for you."
        m "Like a 'savior'."
        mc "I guess..."
        mc "But I wouldn't really know."
        m 1p "I suppose you wouldn't."
        mc "I can't really imagine anyone feeling that they're fighting to stay in control."
        mc "But it seems like it would be pretty obvious to tell from a person watching."
        mc "They'd be acting differently at times."
        mc "At least, that's what I think."
        m 2f "I don't think so."
        m "That person probably wants to hide it from other people."
        m 2g "Just to keep others from worrying about them."
        m "I guess it sort of sounds like depression..."
        m "But I wouldn't really know the feeling either."
        mc "I'm sorry if this feels like it's coming out of nowhere..."
        mc "But Monika..."
        mc "Are you depressed or something?"
        m 2d "Me?"
        m "No..."
        m 2e "Nothing like that."
        m "Why do you ask?"
        mc "I just felt like I had to say that."
        mc "You've been acting a little different."
        m 2n "Ahaha, well it's definitely not depression I can assure you."
        m "{i}(I'm afraid it's much worse.){/i}"
        mc "Did you say something?"
        m 2l "No, nothing important."
        m 3f "I'm afraid I don't have any writing tips to give you today, [player]..."
        m "I've been a little busy thinking about other things..."
        mc "Ah, that's okay."
        mc "It's not like you're the best writer--."
        mc "Not to insult you or anything!"
        m 1l "That's okay, I don't take any offence to that."
        m "I know I'm not the best writer in the Literature Club."
        mc "I'd have to disagree on that."
        m 1e "Eh?"
        m "You're giving me too much credit, [player]."
        mc "I don't think so."
        mc "I think you're the best writer in the Literature Club and the fact that my poems are like yours confirms that."
        mc "Well, it's that or I just really like your style of writing."
        m 1m "Ahaha, maybe..."
        mc "Still, you don't need to give me any writing tips if you don't have any."
        mc "I can understand you probably have a lot on your mind."
        m 1n "Yeah..."
        m 1e "Well, thanks for reading my poem~"
        m "It means a lot to me."
        mc "Not a problem."
    elif monika_type == 1:
        call showpoem (poem_m9b)
        mc "This is certainly something."
        mc "It feels like there's a lot of conflict in this poem."
        mc "Is that how you felt when you were writing it?"
        m 1c "Hmm..."
        m "I actually had another poem that I had prepared but..."
        m 1e "Well, let's just say it didn't really suit what I was feeling."
        mc "How come?"
        m 2a "After our talk yesterday, I came to a realization."
        mc "Another epiphany?"
        m 2b "Not really..."
        m "It was more like a complete change of heart."
        m "Well, at least, I wish it was complete."
        mc "A change of heart? On what?"
        m 1a "On my perspective of this world."
        m "Ah..."
        m 1h "Why am I even telling you this? It's not like--"
        mc "I'm actually really interested in what you've got to say, Monika."
        mc "Especially after our talk yesterday."
        show monika 1o
        "Monika avoids my eyes."
        "It looks like she's questioning herself..."
        m 1p "[player], I don't know what it is..."
        m "But I think I should talk to you later."
        m "That is, if you're still interested in what I've got to say."
        mc "Yeah, definitely."
        m 1m "Great, maybe sometime later today then."
        "Monika smiles meaningfully."
        m 1e "You know, I can't help but feel I'm missing something."
        mc "Well, at around this time you'd usually give me a writing tip."
        m "Ah, that's right."
        m "Hmm..."
        "Monika thinks for a moment."
        m 2l "Ahaha, sorry!"
        m "I don't really have any tips for you today, [player]."
        mc "Ah, that's okay."
        mc "I understand you probably have a lot on your mind..."
        m 2m "That I do..."
        m "{i}(That I do, [player]){/i}..."
    else:
        call showpoem (poem_m9)
        mc "Hmm..."
        mc "Is that the same hole you talked about in your first poem?"
        m 2c "My first poem?"
        mc "Yeah, that hole in the wall."
        mc "Though you seemed to have described it differently this time around."
        m 2d "It very well could be."
        m "I've just been writing what's been on my mind, really."
        m "Then putting it in a format that's easy to understand."
        mc "I see..."
        mc "I'm not sure if it's just me..."
        mc "But I'm finding it hard to find a happy interpretation to your poems."
        m 3a "Not all poems have to be happy, some are just plain dark."
        m "Abstract poems may not obviously show the happy side straight away..."
        m "But if you look hard enough, I'm sure you'll find what you're looking for."
        mc "Right..."
        m 1h "Now, what do I need to do..."
        mc "What do you mean?"
        m 1i "Am I missing something?"
        mc "Well, by now you usually give out a writing tip for me."
        m 1l "I do, don't I?"
        m "Well, I was a little busy last night..."
        m "Doing my own sort of preparations for the play."
        m 1e "So I didn't really have time to come up with a writing tip for you today!"
        mc "You think about the tip you're going to give me the day before?"
        m "Of course!"
        m "It makes these times a lot easier for me."
        mc "I see..."
        mc "Thanks for sharing your poem, I guess..."
        m 1a "See you later, [player]~"
    return

label ch13_m_end:
    if monika_type == 0:
        call showpoem (poem_m10b)
        mc "What is it you're waiting for?"
        m 1d "Huh?"
        mc "Your message in your poem is about waiting, isn't it?"
        mc "Waiting for an inevitability."
        m 1l "Yeah, you saw that pretty quickly..."
        m "You can take a guess at what I'm waiting for."
        mc "It's got something to do with the danger, doesn't it?"
        "Monika doesn't respond."
        mc "Why can't we do anything about it?"
        mc "Why--"
        m 1f "[player], not here."
        m "If you really want, we can talk about it more later."
        m 1g "But right now isn't really the time or place, okay?."
        mc "Alright..."
        m 1e "Do you at least like the poem?"
        m "I thought it wouldn't have as much...flare as my other ones."
        mc "It seemed fine to me."
        mc "Why wouldn't it be as good as your other ones?"
        m "I don't know."
        if y_readpoem:
            m 2c "You've read Yuri's poem, right?"
            m "Maybe you would have felt the same as her."
        m 2e "Anyway, I'm glad you can see the message in the poem."
        m "And that it's not just empty words to you."
        mc "I've gotten pretty used to your style so it's getting easier for me to see what you're trying to convey."
        m 1j "Ahaha, I suppose that's true."
        m 1a "Anyway..."
        m "I have a writing tip for you, if you want to hear it."
        mc "Yeah, I would."
        mc "It's been a while since I've heard one."
        m "In that case..."
        m 3b "Here's Monika's Writing Tip of the Day!"
        m "Sometimes when you're writing, you'll feel like you're writing to get recognized."
        m "This will affect the way you write which makes what you write seem empty."
        m "In the end, it will make your writing unworthy to be read by you or the people you're writing for."
        m "Forget about the recognition and instead go for what's worth writing about."
        m "Delve into your mind and find topics that you want to write about and the words will just come through."
        m 3k "...That's my advice for today!"
        m "Thanks for listening~"
    elif monika_type == 1 and ch12_markov_agree:
        call showpoem (poem_m10b, img="monika 1hb")
        m "What do you think?"
        m "I tried to make it like my other abstract poems but..."
        m 1hc "It was a little difficult last night."
        mc "Difficult in what way?"
        m 2hd "I don't know."
        m "Everything just seemed harder to put into words, I guess."
        m 2ha "But I know this is still something I'm happy to show you."
        mc "I noticed there was some stuff you were trying to tell me."
        mc "It's about waiting, isn't it?"
        mc "For the right time?"
        m 4hb "I guess you could say that."
        mc "What about...?"
        m 4hj "Ahaha, you should know."
        m "If you don't already know what it is, then I suppose you'll have to figure it out."
        mc "I guess I'll have to."
        m 2ha "Not that I don't want to tell you."
        m "Right now just isn't the place for it."
        m 2hb "Maybe if we see each other later, [player]."
        mc "I'll try to talk to you later about it then."
        m "Ahaha, alright."
        m 1ha "Anyway..."
        m "I have a writing tip for you, if you want to hear it."
        mc "Yeah, I would."
        mc "It's been a while since I've heard one."
        m "In that case..."
        m 3hb "Here's Monika's Writing Tip of the Day!"
        m "Sometimes when you're writing, you'll feel like you're writing to get recognized."
        m "This will affect the way you write which makes what you write seem empty."
        m "In the end, it will make your writing unworthy to read by you or the people you're writing for."
        m "Forget about the recognition and instead go for what's worth writing about."
        m "Delve into your mind and find topics that you want to write about and the words will just come through."
        m 3hk "...That's my advice for today!"
        m "Thanks for listening~"
    else:
        call showpoem (poem_m10)
        m 1c "You don't have to like my poem, [player]."
        m "I can already tell by that look on your face that something is wrong."
        mc "There's nothing wrong..."
        mc "I'm just trying to figure out what the message behind your poem is."
        m 1a "It's rather straightforward, isn't it?"
        m "It's about feeling trapped, with nowhere to go."
        m 3b "That is...until it's the right time."
        mc "But when is the right time?"
        m 3a "Who knows?"
        m "Maybe you'll find that out and tell me."
        mc "So this poem isn't about you?"
        m 4e "That's up to your interpretation, [player]."
        m "Anyway..."
        m 1a "I have some advice, if you want to hear it."
        mc "Sure, what is it?"
        m "It's a writing tip. I know I didn't give you one last time so I'd like to give you one today."
        mc "Let's hear it."
        "Monika clears her throat."
        m 3b "Here's Monika's Writing Tip of the Day!"
        m "Sometimes when you're writing, you'll feel like you're writing to get recognized."
        m "This will affect the way you write which makes what you write seem empty."
        m "In the end, it will make your writing unworthy to read by you or the people you're writing for."
        m "Forget about the recognition and instead go for what's worth writing about."
        m "Delve into your mind and find topics that you want to write about and the words will just come through."
        m "That's all."
        m "Thanks for listening."
    return

label ch14_m_end:
    return

# Girls Rate Poems
label ch6_n_bad:
    jump ch6_n_med

label ch6_n_med:
    n "Well, I can admit this is your best one yet."
    n "Even if it isn't really suited towards me, I can tell that your writing has gotten alright."
    mc "Only alright?"
    n 5e "What do you want me to say?"
    n "It's not like it's anything special or something like that..."
    n 2c "Someone else might say something different."
    n "After all, we all have different opinions."
    n 2d "It doesn't mean their opinions are right, but you get what I mean."
    mc "Well, to be honest I didn't think this would be my best one."
    mc "I wrote the poem not really thinking much of it."
    mc "It was almost a last-minute thing."
    n 2e "Yeah, yeah..."
    n "Maybe if you put in more effort your writing could be more than alright."
    n "But I'm not going to give you any pointers any more."
    mc "Huh?"
    mc "Why not?"
    label ch6_n_shared:
    n 1h "You've been here a week, I'm sure you know everything you need to."
    n "Including what we all like, so there's no point."
    n "It's completely up to you how you write."
    n 1c "Oh..."
    n "I still have to show you my poem."
    n 1g "Here."
    return

label ch6_n_good:
    n "Well..."
    n 1g "..."
    n "It's not what I expected."
    mc "Oh...?"
    n "It's..."
    n 1h "Better than I expected."
    n 2q "It might just be your best poem yet."
    mc "That was certainly unexpected."
    n 2o "W-What? You don't think I can give out compliments?"
    mc "I--"
    n "Because I can list plenty of things wrong with this if I want to!"
    n 2r "Firstly...!"
    n "Um..."
    mc "I didn't mean it like that Natsuki."
    mc "I just meant that I didn't put that much effort into it."
    mc "I didn't think we'd have to share our poems today..."
    mc "So I personally thought it was a little rough on the edges."
    n 2n "..."
    n "Come on, give yourself more credit than that."
    n "This poem is really good!"
    n 2s "Okay...there I said it."
    mc "Thanks Natsuki."
    mc "I'm glad you feel that way about it."
    mc "If you really think it's that good, I might try to study it a bit."
    mc "To see what makes it so special..."
    n 1c "You..."
    n "...don't need to do that."
    jump ch6_n_shared

label ch7_n_bad:
    if not read_book or did_all_tasks:
        jump ch7_n_med
    if natsuki_approval > 0:
        $ natsuki_approval -= 1
    n 2e "Do I even need to say anything about this?"
    mc "What do you mean?"
    n "This is terrible."
    n "I thought after your last one you were actually getting good."
    n "Looks like you've proven me wrong."
    mc "Ah..."
    mc "I didn't have much time last night."
    n 2b "That's hardly an excuse."
    n "All you had to do was read a book and write a poem."
    mc "I had to read two--"
    n 2f "If you aren't going to take this seriously anymore then there's no point being here."
    n "I've had to put up with this whole club book idea."
    n 2g "At the very least you could keep writing {i}decent{/i} poems."
    mc "I'm sorry Natsuki."
    mc "I'll be more diligent next time..."
    n "You know I shouldn't even show you my poem after..."
    n "Whatever you call that."
    n 2h "But yesterday I said my friendships were looking up..."
    n "So I guess I need to."
    return

label ch7_n_med:
    if read_book and not did_all_tasks:
        jump ch7_n_bad
    n "It's alright..."
    if n_appeal > 0:
        mc "Only alright?"
        n "Well, I preferred yesterday's poem."
    n "The writing has gotten better, as expected."
    n "If I were to give an unbiased opinion..."
    n 2b "It's probably your best one, beating even yesterday's."
    mc "Thanks, I did try to put more thought into this one."
    mc "So I was hoping it would be better than the one from yesterday."
    n 2g "Whatever..."
    n "It feels like I'm the only one here who doesn't like this whole club book idea."
    n 2n "I've had to put up with so much..."
    mc "What do you mean?"
    label ch7_n_shared:
    n 2s "Everyone is acting so awful."
    n "And not just in the club, at h--"
    n 2f "Never mind..."
    n "Here, just look at my poem."
    return

label ch7_n_good:
    if read_book and not did_all_tasks:
        jump ch7_n_bad
    $ natsuki_approval += 1
    n 2f "Let's start with what I don't like..."
    n "Um..."
    n "..."
    mc "Is it that bad?"
    n "No!"
    n 2g "It's actually pretty good."
    if n_appeal > 0:
        n "In fact, it might even be better than your last one."
        n 2g "I have to ask..."
        n 3n "Are you writing your poems for me now?"
        mc "Um..."
        n 3h "You know what."
        n "Don't answer that."
        n 3q "It's better if I keep the answer in my head."
        n "Even if it isn't true."
    else:
        n "I liked it a lot more than your last one..."
        n 2c "Not only is the writing better..."
        n "But, um..."
        n "The style is more..."
        n 2q "More of what I like."
    mc "Well, I did write this to be more relatable to you."
    mc "So I'm glad you think it's good."
    n "..."
    n 3m "Do you like this whole club book idea?"
    n "I feel like it's bringing out the worst in a certain someone..."
    mc "What do you mean?"
    jump ch7_n_shared

label ch9_n_bad:
    jump ch9_n_med

label ch9_n_med:
    n 2i "Hmph."
    n "I don't really get the point of these poem sharing times anymore."
    mc "What do you mean?"
    n 2h "We're meant to be giving out advice, right?"
    n "Or at least learn something about each other from how we write..."
    mc "Yeah...?"
    n 2e "It's been over a week and I'm pretty sure we're all as close as we'll ever be."
    n "I don't know why Sayori is still making us write poems..."
    mc "Well, do you have any idea as to what to do instead?"
    mc "I'm sure Sayori is trying her hardest to keep us engaged..."
    mc "But if you have a better idea, I can let her know."
    n 2f "Why do you care?"
    mc "You're the one telling me all of this..."
    mc "So if that's the case, how can't I care?"
    n 4i "W-W-W...!!"
    "Natsuki finds herself unable to form a proper word."
    n "Well...!"
    n 4n "Maybe I thought you would understand..."
    mc "I'm trying my best but..."
    n 4q "It doesn't matter."
    n "Life really sucks right now..."
    n "Here, just read my poem and go about your day."
    return

label ch9_n_good:
    $ natsuki_approval += 1
    n 2q "Thanks..."
    mc "Huh?"
    if n_appeal >= 3:
        n "Your poems are..."
        n "They've been for me, haven't they?"
        mc "Well..."
        mc "I guess they have."
    else:
        n "This poem is..."
        n "It's written for me, isn't it?"
        n "At least, that's what I'm getting from reading it."
        mc "Um..."
        mc "I guess it is."
    n 2s "I don't really know what to say..."
    n 2u "It's really sweet, you know...?"
    mc "What do you mean?"
    n 2n "You're really keeping me going, [player]."
    n "Life is..."
    n "...not the best right now."
    "Natsuki turns away from me."
    n 2q "Look..."
    n "If I'm honest, I think this poem sharing thing is useless at this point..."
    mc "Why is that?"
    n 1r "This whole thing is about learning about each other from how we write..."
    n "It's been a week and by now..."
    n 1s "Well...I don't think it's doing anything."
    n "Listen..."
    n 1n "I know I might seem really cold..."
    n "But..."
    mc "It's okay, you don't have to say it."
    n "..."
    n 1r "R-Right..."
    n "Anyway, here's my poem..."
    return

label ch12_n_bad:
    jump ch12_n_med

label ch12_n_med:
    n 1e "Hmph."
    n "I have nothing to say about your poem."
    mc "Eh? Why not?"
    n "Is it really something we need to talk about, [player]?"
    n "I already get that you aren't writing for me."
    n 1g "So, what's the point?"
    mc "Maybe to get some feedback on what I can improve?"
    n "How can I tell you what to improve when I don't write like that?"
    n"There's no way for me to give you proper advice on something I'm not familiar with."
    mc "You make a good point, Natsuki."
    mc "I guess I shouldn't really be asking you to tell me what to improve when the style is so different."
    n 1c "You finally get it..."
    n "But, whatever..."
    n 1b "Here's my poem."
    return

label ch12_n_good:
    n 4h "Why?"
    mc "Why what?"
    n "Are you writing your poems like this intentionally?"
    mc "I'm writing them how I want to write them."
    n 4f "Ugh!"
    n "You know, it's really hard to get mad at you when you do this."
    mc "I'm not doing anything..."
    n 4p "Y-Yes you are!"
    n 4g "You clearly forgot to read the manga last night!"
    mc "Oh..."
    mc "Well, I couldn't really help that."
    mc "Something, that I can't remember, stopped me from reading it."
    n 2o "W-What kind of excuse is that?"
    mc "I don't really understand why you're so mad at me."
    mc "I haven't done anything wrong, have I?"
    mc "If I have, I'd like to apologize."
    n 2n "..."
    n "No, you haven't..."
    n 2q "Things have just been getting worse by the week."
    mc "How?"
    n "You wouldn't understand..."
    n 2r "I should be the one saying sorry."
    n "I'm just taking out my frustration on other people..."
    mc "There's no need."
    mc "We both made a mistake, so let's just forget both of them ever happened."
    n 2s "O-Okay..."
    n "H-Here, you can read it if you want..."
    "Natsuki hands me her poem."
    return

label ch14_n_bad:
    jump ch14_n_med

label ch14_n_med:
    if natsuki_outing:
        jump ch14_n_good
    return

label ch14_n_good:
    if not natsuki_outing:
        jump ch14_n_med
    n "..."
    n "I want to say thank you again."
    mc "For sharing my poem?"
    n "No, you idiot!"
    n "...For coming over yesterday..."
    n "And spending time with me."
    mc "Shouldn't you be thanking Sayori as well?"
    n "Are you really that dense, [player]?"
    n "It should be obvious, right?"
    mc "Are you talking about the date we went on?"
    n "Yes! It took you long enough."
    mc "Sorry, it's still kind of hard to believe."
    n "Hard to believe? In what way?"
    n "Am I really that hard to imagine a date with?"
    mc "I didn't mean it like that."
    mc "It's more like..."
    mc "I didn't expect to be on a date with you already..."
    mc "After what happened the day before."
    n "It's not {i}that{/i} hard to believe."
    n "You've been nice to me before all of that happened."
    return

label ch6_y_bad:
    jump ch6_y_med

label ch6_y_med:
    y "..."
    y "Well, it's probably your best one yet."
    y "Good job, [player]."
    mc "Thanks Yuri."
    mc "I honestly wasn't expecting you to think it was my best one."
    y 1f "Why is that?"
    mc "I didn't put much thought into it."
    mc "It was something I did last minute."
    y 1a "That's quite impressive, [player]."
    y "You can come up with a poem like this when you didn't even plan on it..."
    y "You really have applied yourself over the last week."
    y 1f "I can't say much more about it..."
    y "I don't particularly find any of it to be exceptional..."
    y "But there's nothing wrong with it."
    label ch6_y_shared:
    y 1a "You've..."
    y 1i "...clearly found your own writing style."
    y "It's up to you what you choose to do with it."
    y 1f "Whether you change it or not shouldn't be up to me."
    y "Um..."
    y "I almost forgot to show you my poem."
    y "Here, you might find it to be a little different."
    return

label ch6_y_good:
    y 1e "..."
    "As Yuri reads the poem, I notice her eyes lighten."
    y 2f "...Exceptional."
    mc "Really?"
    y "...?"
    y 2n "D-Did I say that out loud...?"
    y "What I meant to say was..."
    y 2p "It was your best one yet..."
    y "Uu...!"
    y 2o "That isn't to say your other poems are bad!"
    y "U-Um..."
    y "..."
    mc "Yuri, calm down."
    mc "You can take your time to say whatever it is you need to."
    "Yuri takes a breath."
    y 2n "Sorry..."
    y 2q "Over the last week, you have clearly gotten better at applying yourself."
    y "But..."
    y "I didn't think..."
    y "...you'd be capable of writing something as good as this."
    y 2p "I hope that didn't sound like an insult!"
    y 2q "It was...a compliment."
    mc "Thanks, that really means a lot coming from you."
    mc "Do you know how I could continue writing like this?"
    mc "This was mostly a fluke..."
    mc "I honestly didn't plan for it to end up like this."
    jump ch6_y_shared

label ch7_y_bad:
    if not read_book or did_all_tasks:
        jump ch7_y_med
    y 2q "Um..."
    y "This is..."
    "Yuri looks at the poem and back at me several times."
    y 2t "Did you...change something?"
    mc "About my writing?"
    mc "Yeah..."
    y "I thought so..."
    mc "I didn't have much time last night to do this."
    mc "I was doing favors for some people."
    mc "So I know it's terrible."
    y 2v "I-I see..."
    y 2p "But I never said it was terrible!"
    y 2y6 "Everything written by you is perfect!"
    mc "What?"
    mc "Yuri..."
    mc "I know for a fact that this is the worst poem I've written ever since I've joined the club."
    mc "There's no need to be so nice to me."
    mc "I can take it."
    y 2b "N-No!"
    y "I'm serious."
    y 2y5 "This poem is perfection and I love everything about you..."
    y "...it! I love everything about it!"
    y 3y5 "Will you read my poem now?"
    return

label ch7_y_med:
    if read_book and not did_all_tasks:
        jump ch7_y_bad
    else:
        jump ch7_y_good

label ch7_y_good:
    if read_book and not did_all_tasks:
        jump ch7_y_bad
    y 2b "I've been waiting for this..."
    y "Let's see what you've written for today."
    mc "Sure, here you go."
    "I hand her my poem but she practically rips it from my hands."
    "She brings my poem to her face and breathes in heavily."
    y "I love it."
    y "It's better than anything I've ever read."
    "From what I saw, she didn't really look at it."
    "I'm not sure if she's being nice to me or if there's some other reason..."
    y 2h "..."
    y "I feel so different around you."
    y "Have you noticed that?"
    y 2t "You're like a poison that I can't get enough of."
    y 2p "A-Ah..."
    y 2q "I mean..."
    y "This poem is a treasure."
    y 2b "Anything by you is."
    y 2y6 "Ahaha, can you hear my heart pounding?"
    y "It makes me want to cut myself..."
    y "I should carve this feeling into my skin."
    y 3y6 "Is that bad, [player]?"
    y "I'm not being weird, right?"
    y 3s "I-I'm having a harder time than usual at concealing my emotions..."
    y 3m "I'm kind of embarrassed."
    y 3y6 "But right now, I just want you to read my poem, too."
    y 3y5 "Okay?"
    return

label ch9_y_bad:
    jump ch9_y_good

label ch9_y_med:
    jump ch9_y_good

label ch9_y_good:
    y 2pa "[player]..."
    y "Before we continue, I'd just like to thank you..."
    y 2pg "You didn't have to visit me in the hospital today..."
    y "But if you didn't..."
    y 3pi "I probably wouldn't even be in the club today."
    mc "That's alright, Yuri."
    mc "You know I care a lot about you."
    mc "So it isn't a big issue for me..."
    y 3pq "T-Thank you..."
    y "A-Anyway..."
    y 3ps "About your poem..."
    y "It's..."
    y "It's perfect."
    y "At least, to me."
    y 3pt "And I'm not just saying that."
    y "Your writing has drastically improved over the course of the past two weeks."
    y 3pu "And I know that you were writing abstract poems before..."
    y "It's clear that you've been changing your style to be more metaphorical, right?"
    mc "Yeah..."
    y 3ps "So there's nothing to tell you to improve on."
    y "I'm really impressed by your work, [player]."
    mc "Thanks, Yuri."
    y 3pq "Would you like to read my poem now?"
    mc "Yeah, definitely."
    return

label ch12_y_bad:
    jump ch12_y_med

label ch12_y_med:
    if visited_yuri_hospital:
        jump ch12_y_good
    y 2pq "[player]..."
    y "I'm sorry I wasn't here last meeting."
    mc "Don't worry about it."
    mc "I'm sure it wasn't really your fault that you were away."
    mc "That's when you got those bandages for your arm, right?"
    y 2pf "That's right. The hospital gave me bandages for the cuts on my arm."
    y "I'm showing them because of two reasons..."
    y "One, it's uncomfortable to have my uniform rubbing against it..."
    y 2pi "And two, to remind me..."
    mc "Remind you of what...?"
    y 2pq "Um...never mind..."
    y "I don't really want to talk about that."
    y "I'd rather talk about something else with you..."
    mc "Anything in particular?"
    y 3po "N-Not really..."
    mc "How about what happened on Sunday?"
    y 2pj "Y-Yeah, okay..."
    y "I'm glad we had that chance to talk."
    y "It makes today a lot less confronting..."
    mc "Confronting?"
    mc "Yuri, am I scary to you?"
    y 2pq "N-No, not like that..."
    y "I guess it's just easier to talk to you now that I've told you about my feelings."
    y "Even if they are just one sided..."
    mc "Ah...I see."
    y 3ph "Don't worry, [player]."
    y "I'm okay, really."
    mc "Alright, Yuri. I believe you."
    show yuri 3ps
    "Yuri lets out a small smile."
    y "You can read my poem now, if you want."
    return

label ch12_y_good:
    if not visited_yuri_hospital:
        jump ch12_y_med
    y 2pb "I'm thankful we had that opportunity yesterday to talk, [player]."
    mc "The feeling is mutual, Yuri."
    mc "I really enjoyed...feeding ducks."
    y "I enjoyed your company."
    mc "Ah..."
    "Did she really just say that straight up?"
    "I enjoyed her company too but it caught me a little off-guard."
    mc "I-I really enjoy your company too."
    y 3pd "You're so funny when you're flustered, [player]."
    mc "I guess that's a good thing about me?"
    y 2pj "It definitely is."
    y "I can't think of one bad thing about you."
    mc "I can name a couple..."
    y 2ps "Well, don't spoil me..."
    y "I'd rather keep your qualities in my mind and not your misgivings."
    mc "That's probably for the best."
    mc "Yuri, I'm sorry I didn't get to express how I really felt in the first week."
    mc "I guess I just kinda had to act a certain way until I felt comfortable."
    y 2pu "That's okay...you're here now..."
    mc "I'll try to make up for it somehow."
    y 3pq "H-How are you planning to do that...?"
    mc "I'll think of something."
    "Yuri smiles bashfully."
    y 3pa "You're so kind, [player]."
    mc "I'd do the same for anyone else I care a lot about."
    y 3pu "Ah..."
    y "D-Does that mean you care about me?"
    y 3po "S-Sorry..."
    y "I already know the answer..."
    y "It just feels nice when you say it..."
    mc "I care about you a lot."
    mc "Don't ever forget it, Yuri."
    y 2ps "R-Right..."
    y "A-Anyway..."
    y "Do you want to read my poem now?"
    mc "Definitely."
    return

label ch13_y_bad:
    jump ch13_y_med

label ch13_y_med:
    if visited_yuri_hospital:
        jump ch13_y_good
    y "This poem..."
    mc "What about it?"
    y 2pf "I don't know."
    y "It just feels different somehow."
    "Did I accidentally do something differently last night?"
    "I don't think I did."
    mc "I'm sorry if it does."
    y 2pq "I don't think it's your fault."
    "Yuri ponders for a moment."
    y 2pt "Are you feeling the same as me?"
    mc "I don't know what you mean."
    y 2pv "You didn't feel it last night, did you?"
    y "I suppose it could just be me."
    mc "Yuri, I have no idea what you're talking about."
    y 3pt "It's a little difficult to explain."
    y "But it's almost like writing poems doesn't have the effect it once had."
    mc "What do you mean?"
    y 3pw "Well..."
    y "Usually when I write a poem I have to really think about it."
    y "So that I can put my emotions and an underlying message into it."
    y 3pg "When I wrote that one last night..."
    y "I just didn't feel anything."
    y 3ph "I couldn't invoke the metaphors and emotions that I wanted to."
    mc "That's weird."
    mc "Nothing changed for me."
    y 2pv "I see..."
    mc "Maybe this whole poem thing is just getting old."
    mc "We have been doing this for a while."
    y 2ph "I suppose you're right."
    y "I...guess you can read my poem then."
    return

label ch13_y_good:
    if not visited_yuri_hospital:
        jump ch13_y_med
    y "You know..."
    y "...after reading your poem, it confirms it."
    mc "Confirms what?"
    y 2pa "That it's not pointless to go on."
    mc "I'm not sure I understand, Yuri."
    y 2po "It's hard to describe, [player]."
    mc "Try your best."
    y 2pv "A-Alright..."
    y "When I was writing my poem last night, I felt...empty."
    y 3pt "Usually when I write my poems, I have to concentrate to make it how I want."
    y "The messages and metaphors behind the poem is just how I write."
    y 3ps "But you know that already."
    mc "Yeah..."
    y 3pv "But last night, when I was concentrating..."
    y "...or rather trying to..."
    y "It's like I felt that my poem wouldn't have any meaning."
    y 3pw "Like I was just writing down empty words on paper."
    y "But then..."
    y 2pq "I..."
    "Yuri hesitates."
    mc "What is it Yuri? You can tell me anything, you know that."
    show yuri 2pu
    "Yuri smiles shyly."
    y "I...thought of you."
    y "The words felt less empty somehow..."
    y 3ps "It was like the thought of you brought back meaning into my poem."
    y "S-Sorry, this is really embarassing to say."
    mc "No, it's fine."
    mc "I really appreciate you telling me this Yuri."
    mc "It means a lot to me, really."
    "I put a hand on Yuri's shoulder."
    y "Ah..."
    "Yuri grabs my hand and looks at me."
    show yuri 3ps
    "She smiles bashfully."
    y "Well...if you say so."
    y "A-Anyway, you can read it now."
    y 3pq "I hope you like it."
    mc "I know I will."
    return

label ch14_y_bad:
    jump ch14_y_med

label ch14_y_med:
    if visited_yuri_hospital:
        jump ch14_y_good

    return

label ch14_y_good:
    if not visited_yuri_hospital:
        jump ch14_y_med

    return

label ch6_s_bad:
    jump ch6_s_med

label ch6_s_med:
    s 1q "Ehehe~"
    s "Your writing has gotten really good, hasn't it [player]?"
    s "This poem might just be your best one yet!"
    s 4a "I'm so happy you're still doing this for the club!"
    mc "Ah..."
    mc "Thanks, but like I told you this morning..."
    mc "I didn't expect us to have to keep sharing poems..."
    mc "So this probably isn't as good as it could have been."
    s 1d "Aw, I know you don't mean that."
    s "How else could you write something like this, if you didn't try?"
    mc "I'm not lying to you Sayori."
    mc "I really didn't think it was that good."
    s "Well..."
    s 1a "That won't change my opinion."
    s "I'm sure everyone else probably thinks it's the best thing you've done all week as well."
    if poemsread == 0:
        mc "I wouldn't be too sure about that."
    else:
        mc "Well...you could be right."
    label ch6_s_shared:
    s "You should stick to your own style, [player]."
    s "It's what's gotten you this far."
    s 1d "I mean I'm not going to stop you from exploring different styles if you still plan on it..."
    s 1q "That's not my choice to make, it's yours!"
    "Sayori beams."
    s 1m "Ah..."
    s "I feel like I'm forgetting something."
    mc "Maybe showing me your poem?"
    s 1l "O-Oh yeah...!"
    s 1a "Here."
    return

label ch6_s_good:
    s 1m "Wow!"
    s "This is really good [player]!"
    s "Like sooooooooo good!"
    s 1q "It's probably your best one yet."
    s "Thanks for sharing it with me!"
    if sayori_confess:
        mc "You're not just saying that because we're a couple, are you?"
        s "Nope! I mean it!"
    else:
        mc "Really?"
        s "Yeah!"
    mc "You realize I didn't put in as much effort as I would have liked to on this..."
    mc "Right?"
    s 4a "So...you're going to have even better poems than this?"
    s "I'm so excited to read them!"
    "I don't think she's getting my point here."
    if poemsread == 0:
        "I may have unintentionally written a poem that's only really good to Sayori."
    s "I think the others will think it's great too."
    s "I can't help but think...that it's a little strange."
    mc "What is?"
    s 1b "Well, you."
    s "You changed your writing style from last week."
    s 1d "I wasn't really expecting you to."
    s "I thought you were gonna stick with those fully abstract poems."
    s "Instead you changed it up to have a little more emotion while still having those abstract vibes."
    s "Doing this isn't bad!"
    s "But..."
    jump ch6_s_shared

label ch7_s_bad:
    if not read_book or did_all_tasks:
        jump ch7_s_med
    s 4l "Ahaha..."
    s "Sorry..."
    mc "Sayori...?"
    s "This might have been okay..."
    s 2d "If it was your first poem."
    mc "It's that bad?"
    s 2b "Yeah...it's like you put no effort into this at all."
    mc "About that..."
    mc "I was a bit busy last night reading that other book."
    mc "So I couldn't spend as much time as I wanted on it."
    s 2d "It's not your fault."
    s "Not entirely I mean."
    mc "I know."
    mc "If I didn't have to read the club novel..."
    s 1h "T-That's not what I meant!"
    s "There's something else that could have happened."
    mc "I don't really get what you're talking about."
    s 1d "Well, it's okay [player]."
    s "Here, read my poem."
    s "Maybe it'll cheer you up a little."
    return

label ch7_s_med:
    if read_book and not did_all_tasks:
        jump ch7_s_bad
    s 4c "Your poems are only getting better [player]!"
    s 4q "I'm so proud of you."
    mc "Thanks..."
    mc "I did try to make this one better than my last."
    s "I didn't think you could get any better."
    if s_appeal > 0:
        s 1c "I still liked yesterday's poem better."
        s 1a "But your writing is getting super good!"
    else:
        s 1a "You just keep on surprising, don't you?"
    s "You stick with your writing style!"
    s "It's really working for you."
    mc "Yeah, no matter what I do I feel like I can only get better."
    mc "I can't help but feel weird about what's been happening though."
    s 1d "You shouldn't worry so much, [player]."
    s "It's not a good look on you."
    s "Here, why don't you read my poem?"
    s "It could cheer you up~"
    return

label ch7_s_good:
    if read_book and not did_all_tasks:
        jump ch7_s_bad
    s 4n "Hey, this is pretty good!"
    s "I really wasn't expecting you to keep getting better!"
    s 4m "Soon enough, you'll outshine all of us!"
    mc "Eh..."
    mc "I wouldn't count on it."
    mc "But I did try to make this my best one."
    s 1t "It's so full of emotion."
    s "It almost makes me wanna cry!"
    mc "S-Sayori..."
    s 2r "I'm only kidding!"
    s 2a "But it's really good, so don't let anyone tell you otherwise."
    mc "Thanks Sayori."
    s 1d "You sound a little down today, [player]."
    s "You feeling okay?"
    mc "Yeah...just feels like a weird day."
    mc "I'm just left thinking, you know?"
    s "Well, have a look at my poem."
    s "Maybe you'll find the answer you're looking for."
    s "It could also cheer you up~"
    return

label ch9_s_bad:
    jump ch9_s_med

label ch9_s_med:
    s 4q "Ehehe..."
    mc "What is it?"
    s 2d "That's one down, [player]."
    s "And now there's only one left..."
    mc "What are you talking about?"
    s "We're so close to the end."
    mc "You said that before..."
    mc "But you were talking about the book, right?"
    mc "And if you're talking about the new one..."
    s 2l "Um..."
    s "Well, never mind..."
    s "I guess I'm just a little excited from everything."
    mc "You mean Yuri freaking out yesterday...?"
    s 2g "No, that's not what I meant..."
    mc "Right..."
    mc "You still haven't said anything about my actual poem though."
    s 2n "Oh..."
    s "Well, it was amazing."
    mc "Did you even read it?"
    s 1l "Of course, I did!"
    s "It was..."
    "Sayori looks at the poem again."
    s "...about that thing."
    mc "Right..."
    s 1d "I can tell it's good, okay?"
    s "It flowed really well."
    mc "Whatever you say..."
    s 2a "Look, just read my poem..."
    s "And let's not talk about what just happened, okay?"
    mc "If you say so..."
    return

label ch9_s_good:
    s 4q "Ehehe~"
    s "It's really good, [player]."
    mc "You aren't just saying that, are you?"
    mc "It didn't even look like you read it..."
    s 2d "I did!"
    s "I just read through it quickly because..."
    s 2a "We're so close to the end."
    mc "The end...?"
    mc "You said that before."
    mc "But I thought you were talking about the book."
    mc "Seeing as we've barely even started the new one..."
    s 2l "Um..."
    s "Well, never mind..."
    s "I guess with the things happening lately, I'm just a little..."
    s "I don't know the word for it..."
    s 2d "But it's that feeling you get when you know a happy end is coming."
    mc "I don't think that's a feeling, Sayori."
    s 2c "Well, you gotta know what I mean..."
    mc "I'm really not sure I do..."
    s "I suppose you wouldn't..."
    s 2d "But you don't have to take that feeling away from me, [player]..."
    mc "Ah..."
    mc "Sorry, that wasn't my intention."
    s "It's fine..."
    s 2a "Anyway, you can look at my poem now."
    return

label ch12_s_bad:
    jump ch12_s_med

label ch12_s_med:
    s 1c "I've got a question."
    mc "What is it?"
    s 1f "You don't think I'm forceful..."
    s "...do you [player]?"
    mc "Forceful? Sayori, where did this come from all of a sudden?"
    s 1h "Just...answer the question, [player]."
    s 1k "It's for my own sake."
    mc "Your own sake?"
    mc "Well, in that case..."
    "I don't really want to hurt Sayori's feelings."
    "I care about her a lot but..."
    "These past couple of days have been a little strange with her telling me what to do all the time."
    "Is forceful really the right word to use here?"
    mc "Sayori, you're--"
    s 1g "No need, [player]."
    s "I already know what you're going to say..."
    mc "Eh? Didn't you want me to answer the question?"
    mc "How could you possibly know what I'm going to say?"
    s 1k "It's just a feeling."
    s "I just hoped that feeling wasn't right..."
    mc "Sayori..."
    s 2d "Forget I asked, [player]."
    s "Really, it's for the best."
    s "Just hand me your poem."
    mc "Alright..."
    mc "Here you go."
    "I give me poem to Sayori."
    s "It's a nice poem, [player]."
    s "Really gives me a sort of..."
    s 2q "I don't know, actually!"
    mc "Huh? I don't understand..."
    s "Well, how about read my poem now?"
    s "Maybe that will help you understand."
    mc "Okay..."
    "Sayori gives me her poem."
    return

label ch12_s_good:
    s 1d "Hi [player]~"
    s "I know I've been a bit...forceful lately..."
    mc "A bit is kind of an understatement..."
    s 1f "Hey! You don't need to be mean about it!"
    mc "Ah, sorry."
    mc "I'm sure you're doing it for our sakes though, right?"
    mc "You care about everyone here a lot."
    s 1l "H-Huh? Did I ever tell you that...?"
    mc "You didn't need to. I know you too well."
    s 2d "Ehehe, I suppose you do..."
    s "[player]..."
    s "I'll do all I can to make sure we all get through this."
    s "Or at least..."
    s "That you get through this."
    mc "What do you mean?"
    s 2q "I'm going to get you that happy ending you deserve."
    mc "Um..."
    mc "Sayori, what are you talking about?"
    mc "What's this talk of a happy ending?"
    s 2r "It is what it is."
    "I don't think she's making any sense."
    s 2c "Anyway..."
    s "You still haven't shown me your poem."
    mc "Oh, right."
    "I give Sayori my poem."
    s 2a "Wow..."
    s "I didn't expect this coming from you."
    mc "I can write poems like this if I want."
    s "I know! I'm just saying that...well..."
    s 2q "I liked your poem!"
    s "That's all there is to it."
    mc "I can't help but feel there's more to it."
    s "Ehehe, I think you're overthinking this a little."
    s 2r "Here, why don't you read my poem now?"
    return

label ch13_s_bad:
    jump ch13_s_med

label ch13_s_med:
    s "Hmm..."
    s "I suppose this is acceptable."
    mc "Eh? Is something wrong with my poem?"
    mc "I don't think I did anything different with it last night but..."
    s 2l "Nothing is wrong!"
    s "I'm just saying what's on my mind."
    mc "I guess you don't like this poem?"
    s 2q "Ehehe, I never said that~"
    mc "I can already tell by the tone of your voice you didn't like it."
    s 4m "What?"
    s "I did like it!"
    s 2j "There I said it, are you happy now you big meanie?"
    mc "Whatever you say..."
    s 2i "I can't win with you, can I?"
    mc "Well, I know you too well."
    mc "So it's not your fault."
    s 2g "I guess..."
    show sayori 1f
    "Sayori looks at me seriously."
    s "Everything okay, [player]?"
    mc "What do you mean?"
    s "You don't...um..."
    s 1g "...{i}feel{/i} any different do you?"
    s "You wrote your poem normally?"
    mc "Eh...?"
    if y_readpoem and not visited_yuri_hospital:
        mc "Yuri said the same thing..."
        mc "I wonder why that is."
    else:
        mc "What do you mean?"
    s 1c "It's probably nothing."
    s "But I'm just curious as to how you're feeling."
    mc "I'm feeling...normal, I guess?"
    s 1b "Well, that's good!"
    show sayori 1q
    "Sayori beams."
    s "Here, you can have a look at what I wrote."
    return

label ch13_s_good:
    s "Hey, this poem is pretty great!"
    mc "Thanks, Sayori."
    s 1b "It really makes me feel..."
    s 1d "Well...a whole range of stuff, really."
    mc "That's sort of what I was going for."
    mc "I'm just glad you liked it."
    s 2q "Of course I did, it's really good!"
    if y_readpoem:
        "I guess it's good she isn't feeling the same as Yuri was."
    s "[player], I just wanna say."
    s 4r "Hope you're having an awesome day!"
    mc "Eh...?"
    mc "Where did {i}that{/i} come from?"
    s 4n "Is there something wrong with wishing you an awesome day?"
    mc "No..."
    mc "It just seems kinda random."
    s 4a "Well, maybe I just want to thank you for this poem."
    mc "If you say so..."
    s 3d "And besides, I know how you felt about yesterday."
    s "It was a weird day, wasn't it?"
    s "I'm sure everyone is thinking about it."
    mc "Yeah..."
    s 1d "So I'm hoping you don't feel that way again."
    s 1q "That's why I'm wishing you an awesome day!"
    "Sayori beams."
    mc "Thanks..."
    "It's not like Sayori can decide if a day is weird or awesome..."
    "But I guess it's the thought that counts."
    s "Ehehe, you're welcome!"
    s 1a "Anyway, you can read what I wrote now."
    s "I hope you like it~"
    return

label ch14_s_bad:
    jump ch14_s_med

label ch14_s_med:
    return

label ch14_s_good:
    return

label ch6_m_start:
    m 2e "Hi [player]~"
    m "Is everything going okay with you?"
    mc "Yeah, everything seems to be going alright."
    if ch5_name == "Monika":
        m "How's your memories?"
        m "Are they clearing up a little?"
        mc "My memories...?"
        "I think back on the events that happened in the last week."
        "Me joining the club and meeting the four members..."
        "Writing poems and sharing them with each other..."
        "Everything appears to be in order."
        mc "Yeah, nothing's wrong with them or anything."
        mc "Why do you ask?"
        m 1m "Um...!"
        m "No reason!"
    else:
        m 2a "That's good!"
        m "I'm glad you've stuck with us for a whole week."
        m 1m "I wasn't really sure if you'd actually stay with the Literature Club."
        mc "Ah, well I joined because Sayori wanted me to."
        mc "I guess I'm just used to it now."
        mc "And I don't mind using some of my own time to spend it with the other people here."
        mc "Besides, I'd be lying if I said I wasn't enjoying myself a little bit."
    m 2a "Well, let's have a look at what you wrote for today."
    "I give my poem to Monika."
    $ nextscene = "mnew_" + newpoemwinner[0] + "_" + str(eval(newpoemwinner[0][0] + "_appeal"))
    call expression nextscene

    m "Anyway..."
    m "Would you like to read my poem now?"
    m "It's quite different from my other ones."
    m "But it's still abstract so I hope you like it~"
    mc "Sure, let's take a look."
    return

label ch7_m_start:
    m "Hmm..."
    if read_book and not did_all_tasks:
        m 2e "This is..."
        m "...certainly something."
        m "After yesterday's poem..."
        m 2l "Ahaha, well let's just say I had higher expectations."
        m 2e "I'm glad you managed to write one at least."
        mc "Yeah, I apologize for that."
        mc "I was reading the book you wanted me to."
        mc "I got too engaged in it I lost track of time..."
        mc "So this is the result."
        m 2c "I can't even tell what this poem is about..."
        m 2d "Or who it's meant to be for..."
        mc "Like I said, it was because I read that other book."
    elif read_book and did_all_tasks:
        m 3a "Wow, this is pretty unexpected."
        mc "What do you mean?"
        m 3b "Somehow, you've managed to write an even better poem than yesterday."
        mc "Well, I did try this time around."
        mc "I'm surprised I managed to write one so well though."
        m 2c "Why is that?"
        mc "Well, I was reading the book you wanted me to..."
        mc "Then for some reason, I knew exactly how I wanted my poem to turn out."
        mc "So I wrote it quick, but it turned out well."
        m 3b "That's unusual, but good for you I guess!"
        $ nextscene = "mnew_" + newpoemwinner[1] + "_" + str(eval(newpoemwinner[1][0] + "_appeal"))
        call expression nextscene
    elif not read_book and did_all_tasks:
        m 2d "Is it wrong to say I'm surprised?"
        mc "What do you mean?"
        m 3b "Somehow, you've managed to write an even better poem than yesterday."
        mc "Well, I did try this time around."
        mc "I focused mostly on the poem last night."
        m 2n "Ah, so you didn't read Portrait of Markov?"
        mc "I had a quick glance over it..."
        mc "But for some reason I could recall exactly what happens up to the seventh chapter."
        mc "I never read it before that but it seemed familiar."
        m 2e "Well, that's good for you!"
        $ nextscene = "mnew_" + newpoemwinner[1] + "_" + str(eval(newpoemwinner[1][0] + "_appeal"))
        call expression nextscene
    else:
        m 2d "I shouldn't be surprised, but I am."
        mc "What do you mean?"
        m 3b "Somehow, you've managed to write an even better poem than yesterday."
        mc "Well, I did try this time around."
        mc "I focused mostly on the poem last night."
        m 2n "Ah, so you didn't read Portrait of Markov?"
        mc "I had a quick glance over it..."
        mc "But I didn't get that far into it."
        mc "Sorry, I know I let you down."
        m 2e "That's okay, we still have a chance."
        mc "Huh?"
        $ nextscene = "mnew_" + newpoemwinner[1] + "_" + str(eval(newpoemwinner[1][0] + "_appeal"))
        call expression nextscene

    m 3h "Do yourself a favor and keep as far away from that book as possible."
    mc "What?"
    m 3i "Just throw it into the bin and never look at it ever again."
    mc "Is there a reason? I mean it was a present from Yuri."
    mc "I'd feel awful for doing that."
    m 2f "You have to trust me on this one [player]."
    mc "I don't understand..."
    m 2q "Okay..."
    m "Well, you don't have to throw it away."
    m 2o "Just promise me you'll never read a word of it again."
    mc "Um...I can try but I can't promise that."
    m 2e "That's good enough for me."
    m "Here, you can read my poem now."
    m 2p "Just...read it carefully."
    m "It's a deliberate form of abstraction."
    return

label ch9_m_start:
    m 3b "Hi, [player]~"
    m "Are you doing good with yourself?"
    mc "I guess..."
    mc "I've been doing everything I needed to if that's what you mean."
    m 2a "Ahaha, okay."
    m "How are you finding this whole book sharing thing so far?"
    mc "Well, it's okay..."
    mc "I just hope there isn't more of what happened yesterday."
    m 2e "We can only hope that it was only Yuri..."
    mc "Yeah..."
    m "Anyway...let's see what you've written for today."
    "I hand my poem over to Monika."
    m 2a "...Mhm!"

    $ nextscene = "mnew_" + newpoemwinner[2] + "_" + str(eval(newpoemwinner[2][0] + "_appeal"))
    call expression nextscene

    m 4e "I wonder what we're going to do with all this extra time."
    mc "Sayori could just dismiss us from the meeting."
    m "Well, I suppose that's true."
    m 2b "Today would be rather short then, don't you think?"
    m "But..."
    m 2e "It doesn't really matter, it just means we'll have more time to read the manga."
    m "Anyway, here's my poem."
    m "I think it might be more like my other poems..."
    return

label ch12_m_start:
    if monika_type == 0:
        m 2e "Ah, you've got another poem for me?"
        m "Did you write it for me again, [player]?"
        mc "Um..."
        m "You don't need to say anything."
        m "I can already tell you did."
        mc "What?"
        mc "You don't know that..."
        m 1e "It's okay."
        m "I really appreciate it..."
        "The truth is, I did write the poem for her."
        "But how does she know that if she hasn't even read it yet?"
        m 2f "Do you remember what I talked about yesterday?"
        m "About that danger that you shouldn't tell anyone about?"
        mc "Sort of..."
        mc "To be honest, it's a little hard to believe."
        m "I know."
        m 2g "It might happen when we least expect it so I've just been..."
        m 2o "Never mind."
        mc "What were you going to say?"
        m 2m "I don't want to ruin the mood with you here."
        m "The club is meant to be a place of happiness."
        m 2e "I shouldn't bring talk like that in here."
        mc "I really don't mind listening to what you have to say."
        m "It's okay..."
        m "Can I read your poem now?"
        mc "Yeah, of course."
    elif monika_type == 1:
        m 1a "Another poem from [player]?"
        m "It's like a dream come true~"
        mc "Um..."
        mc "What do you mean?"
        m 1c "Hmm..."
        m "Perhaps, that sounded too desperate."
        m 1d "Ehm."
        scene black
        $ pause(0.25)
        scene bg club_day
        show monika 2a zorder 2 at i11
        $ _history_list = []
        m "Ah, do you have another poem to share [player]?"
        mc "Yeah..."
        mc "Though it probably isn't my best work, so be warned."
        m "Ahaha, I'm sure anything by you is alright at the very least."
        m 2b "You're a natural poet, [player]."
        mc "Do you really think so?"
        mc "At times it kinda feels like I just write the first word on my mind."
        m 2c "Hmm..."
        m 2e "Well, that's certainly an interesting way to write poems."
        m "Though I don't think most of us really write like that!"
        m 4a "But we all have our own way of coming up with what to write."
        m "What matters is that we stick with that way of writing and don't change because of other people."
        mc "I suppose you're right."
        m 4b "Ahaha, well I usually am."
        mc "..."
        m 1a "Anyway, I'll take a look at your poem now."
        mc "Right, here you go."
    else:
        m 1h "Hm."
        m "Why is life so difficult, [player]?"
        mc "What do you mean?"
        m 1i "I've been doing my hardest to figure out what's going on..."
        m "But nothing makes sense..."
        mc "Monika, what are you talking about?"
        mc "What doesn't make sense to you? Maybe I can clarify it."
        m "I already know you don't know, [player]."
        m "There's nothing for you to clarify."
        mc "I can try at least?"
        mc "Just tell me what it is."
        m 1h "No, there's really no point."
        m "Right now, we're just wasting time."
        show monika g8
        m "{cps=15}So give me your poem already.{/cps}"
        $ style.say_dialogue = style.edited
        mc "Yes, of course."
        $ style.say_dialogue = style.normal

    "I hand my poem over to Monika."

    $ nextscene = "mnew_" + natarcpoemwinner[0] + "_" + str(eval(natarcpoemwinner[0][0] + "_appeal"))
    call expression nextscene

    if monika_type == 0:
        m 1e "Lately, I think your poems have become more important to me..."
        mc "Is that a good thing?"
        m "It depends on how you look at it."
        m 2e "You must feel flattered that I think your poems are so important, right?"
        mc "I guess..."
        m "There's really no need to hide it, [player]."
        m "I know you felt good when I told you your poems are important to me."
        mc "You see right through me, Monika."
        m 2m "I really do..."
        m 2n "Anyway, from another perspective it might be some sort of desperation..."
        m 2o "Like I'm only hanging on because of your poems..."
        mc "That's kinda dark..."
        m 4l "Well, it's not like I feel like that!"
        m "I'm just pointing out different perspectives, [player]."
        mc "I guess so."
        m 1j "Anyway, here's my poem."
        m "I really hope you like it~"
    elif monika_type == 1:
        m 1c "I'm a little curious..."
        mc "About what?"
        m 1d "Why this poem is so important to me..."
        mc "It is...?"
        m 2c "Well, not important enough that I'd do anything irrational for it..."
        m "But important in a way that..."
        m "Well..."
        m 2m "I'm not quite sure how to describe it, really!"
        mc "Maybe you just really like my style of writing?"
        mc "After all, it is pretty similar to yours."
        m 2n "That may be it..."
        m 2e "Anyway...you can take a look at my poem now."
        m "I hope you like it."
    else:
        m 2h "I have a question I want to ask you, [player]."
        m "There's not really a point but what do I have to lose?"
        mc "I'll try to answer to the best of my ability."
        m 2i "Oh, I know you will."
        "The way Monika said that gave me a weird feeling."
        m 2c "Do you remember the small details of your first week in the Literature Club?"
        mc "The small details...?"
        mc "Like what?"
        m 2e "Oh, I don't know..."
        m "What about some of the stuff you did in the first couple of days?"
        mc "Well..."
        mc "It was a while ago so those memories are a little hazy right now."
        m 2h "I see..."
        m "That's not really what I was after but I guess you tried to answer as best you could."
        m 2e "I'll let you read my poem now then."
    return

label ch13_m_start:
    if monika_type == 0:
        m "Doing well, [player]?"
        mc "As well as I could be, I guess."
        m 1n "Yesterday sure was strange, wasn't it?"
        m "Who knew all that stuff would happen?"
        mc "Yeah..."
        mc "I just hope nothing like that happens again."
        mc "It's a little too much excitement, especially coming from the Literature Club."
        m 1l "Ahaha, I don't think something like that will happen again."
        m 1m "At least, I hope so."
        "Monika looks worried."
        mc "Is there something wrong?"
        mc "I know you told me about...you know."
        mc "Is it still bothering you?"
        m 2e "Ah...don't mind me."
        m "I'll be fine."
        mc "Are you sure?"
        m "Yeah, just give me your poem."
        m "I'm sure I'll be feeling better after I read it."
        mc "Sure..."
    elif monika_type == 1 and ch12_markov_agree:
        m "I can't quite comprehend what I'm feeling right now."
        m "Just the sight of you, especially at these particular times..."
        m 2hl "Well...the sight of your--"
        mc "Who are you talking to?"
        m "Ah..."
        m 2hm "Sorry, I was just speaking to myself."
        "It didn't sound like she was talking to herself."
        "Though I suppose there would be no one else."
        "She clearly wasn't talking to me."
        m 1ha "Anyway...how do you feel about what happened yesterday?"
        mc "That whole thing with Natsuki?"
        mc "I'm mostly just glad it's over with."
        mc "I wasn't expecting anything like that coming from a Literature Club."
        m 3hb "Ahaha, it is quite a lot of excitement coming from a club like this."
        mc "Yeah, not something I'd like to do again anytime soon."
        m 3ha "Well...that might not be an option."
        mc "What?"
        m 3hj "Nothing~"
        mc "So I was wondering why you have your hair like that."
        m 1ha "I just thought I'd change up my look a little."
        m "It helps distinguish me from the others."
        mc "What do you mean by that?"
        mc "Yuri already has her hair down--"
        m 1hf "Are you saying you don't like it?"
        m 1hg "I can change it back...if you want."
        m "After all, I did do this for you..."
        "What?"
        "Did she just openly admit that...?"
        mc "N-No...I like it."
        mc "I-It's just..."
        "I really didn't mean to offend her."
        mc "Just forget I said anything."
        m 1hb "Ahaha, okay~"
        m "Anyway, I'll take a look at your poem now."
    else:
        m "[player]."
        mc "Monika."
        m 1b "Come to share your poem with me?"
        mc "I suppose I have."
        m "Well, let's get to it then."
        m "Hand it over."
        "I'm a bit surprised."
        "Usually she has a bit more to say than that."
        mc "Uh...right."
        mc "Here you go."
    "I hand my poem over to Monika."

    if sayarcpoemwinner[0] == "monika":
        $ nextscene = "msay_" + sayarcpoemwinner[0] + "_" + str(eval(sayarcpoemwinner[0][0] + "_appealS"))
    else:
        $ ch13poemwinner = sayarcpoemwinner[0].capitalize()
        $ nextscene = "msay_universal_" + str(eval(sayarcpoemwinner[0][0] + "_appealS"))
    call expression nextscene

    if monika_type == 0:
        m 1e "It hasn't affected you, I think."
        m "It's a little hard to tell."
        m "But it does make sense you're unaffected."
        mc "Unaffected?"
        mc "What am I unaffected by?"
        m "No matter what the actual style of the poem is..."
        m 1m "The way you wrote your poem still feels the same."
        m "At least to me."
        mc "Is that a good thing?"
        m 1c "I'm not sure..."
        m "I'll let you know if I ever figure out the answer."
        m 3a "But anyway, you haven't read my poem."
        m "Here, tell me what you think."
    elif monika_type == 1 and ch12_markov_agree:
        m 1hc "You know...I {i}feel{/i} like your poem should be different."
        m "Like there should be something missing..."
        m 1ha "But there isn't."
        mc "What do you mean?"
        m 2hb "Your poems are still written in the same way."
        m "Even if you're actually writing about and the style might be different..."
        mc "I'm still not quite sure what you mean, Monika."
        m "It doesn't really matter."
        m "It's just an observation from me."
        m 4ha "Speaking of which, you haven't observed my poem yet."
        mc "Ah...right."
        mc "Let's see it."
    else:
        m 1c "I hope you'll forgive me if I seem a little out of it today."
        m "I'm just in a rush for the meeting to be over, that's all."
        mc "Ah...I see."
        mc "I thought you just didn't like my poem or something."
        m 2d "You aren't the reason I'm acting like this."
        m "So don't blame yourself for it."
        mc "Alright, if you say so Monika."
        m 1e "Great."
        "Monika lets out a small smile."
        m "Would you like to read my poem now?"
        mc "Sure."
    "Monika hands me her poem."
    return

label ch14_m_start:
    return

label mnew_yuri_1:
    m 2a "Hmm..."
    m "Aha, if I couldn't tell from the handwriting..."
    m "I would have thought Yuri wrote this."
    m 3b "That's a good thing~"
    m "It's nice to see you changing up your style a bit."
    m "I wasn't sure if you were going to keep writing your poems like I do."
    mc "I guess I wanted to explore a little bit."
    mc "I might change it up a bit more depending on how I'm feeling."
    m 4a "Well, that's completely up to you!"
    m "You've gotten really good at writing poems over the last week."
    m "It's like you're a natural now."
    mc "Ah..."
    mc "Thanks, I didn't really expect to get so much into it."
    mc "In fact, I don't think this poem has as much of the feeling I was going for in it."
    mc "I kinda did it without thinking."
    mc "I wrote this hoping we wouldn't need to show our poems today."
    mc "So it's like a contingency poem, it isn't my best."
    m 1a "Ahaha, there's no need to be so modest."
    m "You can change your writing style from a more abstract based tone to more metaphorical."
    m 1b "That's really impressive!"
    mc "Yuri and you have pretty similar writing styles..."
    mc "So I guess I was just going for some abstract metaphors with this."
    mc "Then again, I did say I did it without thinking."
    mc "Meaning what's coming from my mouth could be complete rubbish."
    m 1e "Ah, I don't think so."
    m "I think you're definitely downplaying yourself a little."
    m "And besides, even if it was accidental..."
    m 1a "Being able to write in two different styles, no matter how similar they are, is good!"
    return

label mnew_natsuki_1:
    m 1a "I like this one!"
    m "It's a lot like Natsuki's style."
    m "Ahaha, in fact if it wasn't for the handwriting..."
    m "I would have thought she wrote this."
    m 1e "That isn't a bad thing~"
    m "In fact, it's good to see you changing up your writing style a bit."
    m "Even if I did enjoy your previous poems more."
    mc "Yeah, I guess I finally decided to explore some other styles."
    mc "I might change it up around a little depending on how I'm feeling."
    m 3b "Well, that's left up to you!"
    m "You really have gotten good at writing poems over the last week."
    m "You're basically a natural."
    mc "Ah..."
    mc "Thanks, I didn't expect that I'd be having fun writing poems."
    mc "In fact, this poem probably didn't have as much of the feeling I was going for in it."
    mc "I kinda wrote this one without thinking too much about it."
    mc "I wrote this hoping we wouldn't need to show our poems today."
    mc "So it's like a backup poem, not my best work."
    m 2e "You don't like bragging, do you?"
    m "The fact that you can change your style from abstract to cute is really quite impressive!"
    mc "Then again, I did say I did it without thinking."
    mc "Meaning what's coming from your mouth could be complete rubbish."
    m "Ah, I don't think so."
    m "I think you're definitely downplaying yourself a little."
    m "And besides, even if it was accidental..."
    m 3b "Being able to write in two different styles this well..."
    m "Especially when you consider just how different those styles are..."
    m 1a "Is an impressive feat!"
    return

label mnew_sayori_1:
    m 1k "Ahaha..."
    mc "Is something wrong?"
    m 2a "Not really..."
    m "But do you remember last week when I told you I thought your writing would become more like Sayori's?"
    mc "Um..."
    "I think back to Friday last week when I showed Monika my third poem."
    mc "Yeah actually, I do."
    m 3b "Well, this poem reminds me of something that she would write."
    m "It's got a lot of emotion in it and the way you phrased everything seems gentle."
    m "It isn't a bad thing that you can write like this!"
    m 2a "On the contrary, it's good to see you exploring your writing style a bit."
    m "You don't have to keep writing them for me just because I enjoyed them."
    mc "I suppose I did try something different this time."
    mc "I may change it up a little more depending on how I'm feeling."
    m 2e "That's your choice, of course~"
    m "You don't have to stick to any particular style."
    m 3b "In fact, I'd encourage you to explore other styles a bit more because your writing has gotten really good!"
    mc "Ah..."
    mc "Thanks, I guess I really didn't think I'd enjoy writing poems."
    mc "This one probably didn't have the feeling I was going for when I wrote it."
    mc "But I didn't really think about it much when I wrote it."
    mc "I was actually hoping we wouldn't need to share our poems today..."
    mc "So this is sort of like a backup poem."
    m "There's no need to be so humble, [player]."
    m "The fact that you can change your writing style from abstract to emotional is something to be proud of."
    mc "But then again, I did say I did it without thinking."
    mc "Meaning what's coming from your mouth could be complete rubbish."
    m 1e "Ah, I don't think so."
    m "I think you're definitely downplaying yourself a little."
    m "And even if you think it was accidental..."
    m 1a "Being able to write in different styles well is an impressive feat."
    return

label mnew_monika_1:
    m 1e "Ah..."
    m "So you decided to stick with my writing style?"
    mc "Yeah, I guess abstract poem writing is just my thing."
    m 3a "Well, I definitely enjoy reading your poems because of how you write."
    m "It's almost like looking in a mirror, isn't it?"
    mc "What do you mean?"
    m 2e "I meant that your poems have become so much like mine..."
    m "...that if it weren't for the handwriting you'd think I would have wrote them!"
    mc "Ah...is that a bad thing?"
    m 3a "It depends how you look at it."
    m 3b "If you're doing it because you like writing like that, then that's great!"
    m 3c "But if you're doing it simply to impress someone then..."
    m 3l "Well, they do say imitation is the sincerest form of flattery, right?"
    m 1a "Either way, I'm not going to judge you!"
    m "I'm just going to say that your poems have gotten really good over the last week."
    m 1e "You know, abstract poems like this have different meanings to different people."
    m "To me, it could mean one thing but to you it could mean something completely different."
    m 3a "That's what makes it so fun to write."
    mc "You're right there..."
    mc "But I wasn't really thinking when I wrote this poem."
    mc "I don't think it came out the best it could have."
    mc "In fact, it was more of a last minute contingency poem..."
    mc "Since I was hoping we wouldn't have to share our poems today."
    m 1e "You sure are a modest person, aren't you [player]?"
    m "You may not be able to go into different styles..."
    m 1a "But the fact you can write something like this to a high standard is really impressive."
    return

label mnew_yuri_2:
    m 3l "Anyway..."
    m 2h "I can tell you've been starting to write your poems for Yuri."
    mc "What's giving you that idea?"
    m 2f "[player], we've been here for over a week."
    m 2e "I can tell when a poem overlaps style with another."
    mc "Ah, so I suppose there's no point hiding it."
    m 5 "It's alright, I won't tell anyone~"
    m 3h "Just..."
    m "Be careful around her, alright?"
    m 3i "I don't want to see either of you get hurt."
    m 3p "That book sure is a piece of work..."
    return

label mnew_natsuki_2:
    m 3l "Anyway..."
    m 3j "Your poems have really gotten cute, haven't they?"
    m "Are you writing your poems for Natsuki now?"
    mc "Is something giving it away?"
    m 3a "We've been here over a week, so I've gotten used to everyone's poems."
    m "I can tell when a poem overlaps style with another."
    m 3b "And it's pretty clear you're writing for Natsuki, aren't you [player]?"
    mc "Ah..."
    m 5 "Ahaha, it's okay~"
    m 3d "Do you think Portrait of Markov has any cute themes in it?"
    mc "Not really, it's more of the opposite."
    m 3o "Yeah, you're right there."
    m 3p "There's nothing cute in that book at all."
    return

label mnew_sayori_2:
    m 3l "Anyway..."
    m 3a "This poem is really emotional, isn't it?"
    m "It's what you intended because you're writing for Sayori."
    m 3b "Am I right?"
    mc "Ah...how can you tell?"
    m 3e "[player], it's been over a week since you've joined."
    m "Which means we've had that long to get used to each other's writing..."
    m "So when you suddenly go from abstract to emotional, it's easy to tell the reason."
    mc "I guess you're right."
    if sayori_confess:
        mc "Since Sayori and I are a couple, I thought I'd start writing for her."
    else:
        mc "I thought maybe since she's my best friend, she'd appreciate me writing for her."
    m 5 "Ahaha, I won't tell her~"
    m 3p "You know, the book is quite emotional..."
    return

label mnew_monika_2:
    m 3l "Anyway..."
    m 3e "I noticed you were sticking with an abstract style."
    mc "It's what I've gotten used to."
    mc "I can't see myself changing my style now."
    m 3a "Well, I'm impressed by your dedication."
    mc "What do you mean?"
    m 3b "You've written abstract poems for a whole week."
    m "That either requires some serious motive..."
    m 3j "Or a whole lot of dedication, don't you think?"
    mc "Yeah, I guess you're right."
    m 3e "The abstract style is hard to master, isn't it?"
    m 3p "Though that book seemed to do an alright job..."
    return

label mnew_yuri_3:
    m 3e "Ah, I'm not surprised you wrote like this."
    mc "Why is that?"
    if play_firstpart and did_all_tasks:
        m 2a "Well, you're the reason Yuri is even here today."
        m "So it would only make sense that you'd continue to write for her."
    else:
        m 2a "Well, your last couple of poems have been similar."
        m "So it would only make sense that you'd continue to write like this."
    mc "I guess you're right..."
    mc "I mean it's a pretty enjoyable style to write in."
    m 3b "We all have our own idea of what's fun to write..."
    m "I do see how writing like Yuri could be fun though."
    m "But anyway..."
    return

label mnew_natsuki_3:
    m 3a "So you're still trying to get closer to Natsuki?"
    m "Good for you, [player]."
    mc "Eh...?"
    mc "Is it that obvious from the poem?"
    m 3b "It's not just this one."
    m "Your past couple of poems have been giving out a cute feeling more than anything."
    m 2e "There's nothing wrong with that, of course..."
    m "You should be the one to dictate how you write."
    mc "I mean, I already am..."
    mc "...aren't I?"
    m "Ahaha, I guess so."
    m "I'm just saying though."
    m "Hmm..."
    return

label mnew_sayori_3:
    m 3a "Sticking with an emotional style again?"
    m "Well, I can't blame you..."
    m 3c "They do invoke some sort of weird feeling within me."
    mc "Yeah, I've been trying to write like Sayori does..."
    mc "She's probably getting to me..."
    m 3b "Ahaha, there's nothing wrong with that."
    m 2e "In fact, I'm sure she appreciates it a lot."
    mc "What's that feeling you said it invokes?"
    m 2c "Hmm..."
    m "I don't know how to describe it."
    m "But I guess the closest thing is..."
    m 2d "...regret?"
    m 2e "I don't really know why."
    m "Anyway..."
    return

label mnew_monika_3:
    if did_all_tasks:
        m 2e "So you're still sticking with my style, I see."
        mc "I don't think I can change it at this point."
        mc "I'm just too used to it."
        m "Ah, well that's fine."
        m "In fact..."
        m "It really helps."
        m "So if you can..."
        m 3b "...you should keep writing like this."
        m 3n "I mean, of course you're welcome to change it..."
        m "It's just..."
        mc "I think I get the idea."
        m 2e "I hope you do..."
        m "But like I said before, I'm not going to make you change your style."
        m "It's up to you..."
        m 2f "...just remember that no matter what, I'll..."
        mc "Monika...?"
        m 2e "Ah...never mind."
    else:
        m 2c "It's another one of these?"
        m 2a "You should really explore more styles, [player]."
        m "It's not going to help anyone if you write like this."
        mc "What do you mean?"
        mc "I wasn't aware I was helping anyone by writing poems..."
        m 3b "Well, you're helping the wrong person."
        mc "I'm not quite sure I understand..."
        m 2f "Forget about it."
        m "I'll make sure you don't remember this whole conversation anyway."
        scene black
        $ pause(0.25)
        scene bg club_day
        show monika 3j zorder 2 at t11
        $ _history_list = []
        m "...so feel free to write however you want!"
        mc "What...?"
        m "Ahaha..."
    return

label mnew_yuri_4:
    m 3a "Continuing to write for Yuri, I see."
    mc "I guess I just enjoy writing in this style."
    m 3b "I guess that makes sense."
    if visited_yuri_hospital:
        m 3a "You visited Yuri at the hospital, right?"
        m "I think it's nice you're still writing your poems for her."
    else:
        m 3e "Though isn't it a bit too late?"
        m "That is..."
        m "If you are still going for Yuri~"
    mc "E-Eh?"
    m 1c "Well, I just don't see how continuing to write for Yuri is going to do anything."
    mc "I don't think I know what you're getting at."
    m 2e "She's already cured, isn't she?"
    if y_readpoem:
        mc "I guess..."
        mc "But that won't stop me from writing for her.."
    else:
        mc "Cured of what...?"
    m 2a "Ah, never mind."
    m "I don't think you'd understand anyway."
    mc "Alright..."
    return

label mnew_natsuki_4:
    m 3a "Another poem for Natsuki?"
    m "Ahaha, that's cute."
    mc "That was kinda my intention."
    mc "I don't think she's really appreciating it though."
    m 1c "What do you mean?"
    mc "I don't really know..."
    mc "But she doesn't really seem to want to talk to me."
    mc "Or anyone, really..."
    m 3b "It's probably because of--"
    m 3j "Ah, well I guess I shouldn't say."
    mc "What do you mean?"
    m 3a "Well, if she really wants to tell you."
    m "She'll do it herself."
    m 3d "I don't think she'll tell you today though..."
    mc "Right..."
    return

label mnew_sayori_4:
    m 1c "Oh."
    m "You wrote another one of your poems for Sayori, I see."
    mc "Yeah, I did."
    m 2b "You really care about her, don't you?"
    mc "Well, yeah..."
    mc "She's really important to me."
    m 2c "You know, usually this would get some sort of response from me."
    m "But..."
    mc "Yeah, it's not the greatest."
    m 2e "Hold on."
    "Monika rereads the poem"
    m 3b "Wow!"
    m "It really made me feel..."
    m 3k "Um..."
    m 3l "Happy...?"
    m "I guess."
    mc "Ah..."
    mc "You don't have to say anything about the poem."
    mc "I think it's worse that you're actually trying to making stuff up."
    m 3e "Well, that wasn't my intention but..."
    m "Sorry, [player]."
    mc "It's fine, no harm done anyway."
    return

label mnew_monika_4:
    if monika_type == 0:
        m 1e "Thank you."
        mc "Huh?"
        m "For this poem."
        mc "You're welcome...?"
        mc "Have you got anything to say about it?"
        mc "I know it's not exactly my best piece..."
        m 2e "I know..."
        m "But I think it's enough."
        mc "Enough for what?"
        m "Just enough..."
        mc "I hope you at least got the abstract feeling I was going for."
        m 2c "Oh..."
        m "Well, of course I did!"
        m 2e "My interpretation of it..."
        m "Well, I'd rather not tell you."
        m "It's a little personal to me."
        mc "Sure..."
    else:
        m 1c "Ah, another abstract poem?"
        m 1a "Well, it's too late."
        mc "Too late?"
        mc "For what?"
        m 1b "She's already gone, do you know that?"
        m 3j "Or is this still a desperate attempt to try to get her back?"
        mc "Monika, what are you talking about?"
        m 1h "Hmm..."
        m 3a "I'm talking about your poem, of course!"
        mc "Eh?"
        m 3b "That's just how I interpreted it."
        mc "That's not exactly what I had in mind when I wrote it but..."
        m "Well, abstract poems are meant to be interpreted differently."
        m "So it's not always interpreted how the author intended."
        mc "I guess you're right."
    return

# Sayori Arc Monika Poem Critiques
label msay_universal_1:
    if monika_type == 0:
        m 1f "Ah...you wrote this in the style of [ch13poemwinner]'s poems."
        mc "I did."
        m 1o "Does that mean..."
        "Monika stops for a moment."
        mc "What's wrong?"
        m 1p "N-Nothing..."
        m "I just thought that...well..."
        m 2o "Never mind."
        m "It's just strange seeing you write like this."
        m 2e "After all, all your poems until now have been like mine."
        m "I just thought that..."
        m "...you'd continue to write like that."
        mc "Well...you did tell me to explore different styles."
        m "That was a long time ago, [player]."
        m 2m "I guess it's fine..."
        m "It's not really your fault..."
        mc "What do you mean?"
        m 2n "Forget about it."
    elif monika_type == 1 and ch12_markov_agree:
        m 1hc "Hmm..."
        m "This isn't what I expected."
        mc "Eh...?"
        m 2hd "This poem, it's clearly not written in my style."
        mc "I didn't think it would be that obvious."
        m 2ha "It's in [ch13poemwinner]'s style, isn't it?"
        mc "Yeah, I thought I'd try something different."
        m 4hb "Well, I suppose I can't control how you write."
        m "You're your own person, after all."
        mc "Yeah...sorry if it offends you or anything."
        m 1hj "Not at all."
    else:
        m 1c "A poem for [ch13poemwinner]."
        mc "Yeah...was it that obvious?"
        m 1d "Not really, I just thought..."
        m 2a "Well, it's fine, I guess."
        m "I don't really have anything to say that I haven't said already."
        "Monika doesn't sound like she wants to talk."
        "I guess she didn't like the poem."
        m 2b "Not that I didn't like the poem."
        m "I don't really have an opinion on it one way or another."
        m 2e "Sorry if that isn't what you expected."
        mc "Ah, it's okay."
        mc "This whole thing is probably getting old for you anyway..."
        m "Maybe..."
    return

label msay_monika_1:
    if monika_type == 0:
        m 1e "You wrote this poem for me, didn't you?"
        m "I really appreciate that, [player]."
        mc "Yeah...I don't really see myself writing poems well any other way."
        mc "So I stuck with the abstract style that you tend to do."
        m 1m "I know I said before that you should look at different styles..."
        m "But it really warms my heart that you're still doing this."
        mc "Ah..."
        "It isn't that big of a deal, is it?"
        "I've just been writing poems for her."
        "Does it really mean that much...?"
        mc "I guess I'm glad you feel that way."
        m 2a "Ahaha, thank you again [player]."
        m "I know you probably think it's weird that I'm happy at the small things..."
        m "But you have to look at the positives in life, no matter how small they are."
        mc "Yeah, you're right."
    elif monika_type == 1 and ch12_markov_agree:
        m 1hb "Ah, [player]."
        m "It always brings me delight when you write a poem for me."
        m "It's like..."
        m 1hc "Hmm..."
        m 1hj "Well, it makes me feel grateful."
        m "So thank you."
        mc "I didn't think it was that big of a deal."
        m 1hl "It isn't, really."
        m "It's just appreciated."
        mc "I'm glad you liked it then."
        m 2he "It's hard not to."
        mc "What do you mean...?"
        m 2ha "Ahaha, don't worry about it."
    else:
        m 1h "Is there even a point to your poem?"
        mc "W-What do you mean?"
        m 1i "You're writing this for me, clearly."
        m "Do you think I'll change?"
        mc "I...don't know how to answer that question."
        m 1h "I'll never change."
        if ch12_natsuki_reluctance >= 3 and ch12_markov_agree:
            m "Even if you have agreed to help me."
        elif monika_type == 1:
            m "Maybe if you agreed to help me..."
        else:
            m "I've already set a plan in motion."
        m 1i "Anyway, there's no point talking about it any further."
        "Monika lets out a cold stare at me."
        m "That's done."
        mc "Eh?"
        m "Nothing."
    return
