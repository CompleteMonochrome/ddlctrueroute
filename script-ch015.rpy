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
        s 1h "I just said that to encourage [player_reflexive] to prepare."
        if sayori_personality <= 0:
            s 1g "And lately..."
            s "I've been having second thoughts."
            s 1h "I don't know where they're coming from."
            s "If they're a side effect of becoming the president or..."
            s 1k "...something else."
        else:
            s 1j "I have more important things to worry about."
            s "As much I hate to hurt [player_reflexive]..."
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
        s "To [player_reflexive] and Monika."
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
            y 2s "I actually do."
            show yuri 2ps
            "Yuri looks around before pulling her sleeve up, revealing her bandage."
            "I guess she had it hidden until now?"
            if ch5_name == "Yuri":
                y "We've been there before."
                y 3ps "Do you remember?"
                mc "The rooftop?"
                y "Exactly."
            else:
                y 3pf "Have you been to the rooftop before?"
                mc "I can't say I have."
                y "Well, consider this an opportunity then."
            y 3pq "Let's go there now."
            mc "Are we allowed there right now?"
            mc "I mean there's no teachers supervising there..."
            y 3pt "Is that a problem?"
            y "It makes things more interesting."
            mc "I never took you for someone with a rebellious side, Yuri."
            y 2pv "Ah...is it unlikeable?"
            mc "Not at all."
            mc "Just unexpected, that's all."
            mc "I'm all for it."
            mc "How do we get there? Isn't the door usually locked?"
            y 2pq "Well...yes."
            y "You'll see when we get there."
            mc "Alright..."
            "I wonder what she's up to..."
            scene bg school_insideroof
            show yuri 3ps zorder 2 at t11
            with wipeleft_scene
            "We're outside the roof of the school."
            "Yuri tries the door and as expected, it's locked."
            mc "So what now?"
            y 3pq "Um...can you turn around?"
            mc "Turn around? Why?"
            y "J-Just do it."
            mc "Okay, Yuri."
            "I turn around."
            show yuri at thide
            hide yuri
            y "This will only take a second."
            mc "What exactly are you doing?"
            y "You'll see."
            "I hear Yuri fiddling with the door handle."
            "Is she doing what I think she's doing...?"
            y "Okay, that should be it."
            y "You can turn around now."
            show yuri 1q zorder 2 at t11
            "There's nothing different about Yuri."
            "But the door is open."
            mc "How did you manage that?"
            y "I...um..."
            y 1w "I picked the lock."
            mc "What? Really?"
            y "Y-Yeah..."
            mc "Who knew you could pick locks?"
            mc "Have you always been able to?"
            y 1t "Not many really know..."
            y "It's kind of private."
            y "I'd prefer you didn't tell anyone."
            mc "Of course."
            mc "It'll be our little secret."
            show yuri 2pd
            "Yuri shows me a small smile."
            y "Follow me."
            scene bg rooftop with wipeleft_scene
            "And just like that, we're on the rooftop."
            "The view is really nice here."
            "You can see the whole school from above and everyone roaming around the school grounds."
            "The sound of the people below is almost completely silent."
            "It's quite peaceful here."
            "There's a light breeze but I think that just adds to the serenity of the location."
            show yuri 2pa zorder 2 at t11
            y "Can you help me with this?"
            mc "Of course."
            "Yuri puts the bag she's carrying down on the floor."
            "She takes the banner and unrolls it."
            "There's actually a table up here for some reason, despite no one being allowed up here during lunch."
            "I help her put the banner on the table and secure it by placing some of the materials she brought at every corner."
            y 2pb "Shall we get started?"
            y "We haven't got that much time but we should be able to get this done."
            y 2pe "Did you do all you needed to last night?"
            mc "I think so."
            mc "If there's something I missed then I'll definitely finish tonight."
            y "Alright, [player]."
            y "What ideas did you come up with for the banner?"
            y 3pf "I actually have a bunch of ideas in my head but I'd like to know what you thought of."
            if ch14_overall_choice == "Yuri":
                mc "The radio is a pretty important part of your book."
                mc "I think it would be worth including."
            elif ch14_overall_choice == "Natsuki":
                mc "It's based on an alien, right?"
                mc "Maybe include some planets around the banner."
            elif ch14_overall_choice == "Monika":
                if monika_type == 0 or (ch12_markov_agree and monika_type == 1):
                    mc "Since it's based on romance, maybe we could put some hearts on it."
                    mc "But color them gray since it's based on the main character's perspective."
                else:
                    mc "It's centered around a literature club, so maybe books could work?"
                    mc "Maybe a pen and pieces of stationary around the banner."
            elif ch14_overall_choice == "Sayori":
                mc "I thought maybe some rainbows to symbolize hope."
                mc "Even though the book itself is kinda sad."
            else:
                mc "Well, I was thinking we could include some mobile phones in the design."
                mc "Seeing as the play is going to be based around that."
            y 3pi "That sounds like a great idea."
            y "Why don't you do that and I'll begin writing the name of our club?"
            y "I'll try to make it appropriate to what you just suggested."
            mc "Sounds good."
            mc "I guess I'll start on this side and start drawing."
            "I move to the other side of the banner and get some colored markers out."
            "I begin my part of the design, working around the banner as Yuri writes the club's name."
            "What exactly {i}is{/i} the club's name anyway?"
            "Is it just called the \"Literature Club\" or did Sayori give it some kind of name?"
            mc "Yuri, can I ask you something?"
            y 3pq "O-Okay, I'll try to answer it for you."
            mc "Did Sayori give a name to the club?"
            mc "Because that's what you're writing down, right?"
            y "Well..."
            "Yuri puts the lid back on the marker she was using."
            y 3pt "I don't think there was an official name."
            mc "There isn't?"
            y "No, but I thought something easily recognizable would be good."
            y 3pu "Something with a nice ring to it."
            mc "A nice ring, eh?"
            mc "What did you have in mind?"
            y 3pv "W-Well, you're going to laugh at me when I tell you."
            mc "I promise I won't."
            mc "I'll probably be impressed."
            mc "Like how I was when you picked the lock to the roof."
            y "O-Only if you promise."
            mc "I promise."
            "Yuri looks hesitant."
            if yuri_date:
                "I smile at her."
            else:
                "I look at her expectantly."
            y 2po "I thought calling it 'Heartbeat' Literature Club would be suitable."
            mc "Heartbeat?"
            mc "Where did that come from?"
            y "I...don't really know."
            y 2pn "It just seemed appropriate."
            mc "For some reason, I think it fits."
            mc "I don't know why..."
            y 2pe "You know, some would call it Doki Doki instead of Heartbeat."
            y "Heartbeat is just the translation for it."
            mc "The translation from what?"
            y 2pf "What?"
            mc "Never mind."
            mc "I actually think Doki Doki works better."
            mc "Have you told Sayori about this?"
            y 2ph "About the banner?"
            y "I was under the assumption we were all autonomous in our preparations."
            mc "Well, this banner does represent the club."
            mc "Sayori would probably want to know."
            y 2pq "Hmm...you're probably right."
            y "But I think it will be better as a surprise."
            y "W-What's your take on it?"
            mc "I don't mind."
            mc "It's a surprise, after all."
            mc "I don't think Sayori will mind."
            mc "I'm not sure about the others..."
            y 1a "The others probably have their own surprises anyway."
            y "Or at least, their own flair in their own designs."
            mc "That's true."
            "Yuri takes the lid off her marker."
            y 2pb "Then, shall we finish this off?"
            y "We haven't exactly spent out time efficiently."
            mc "Let's do it."
            show yuri 2pa
            "Yuri and I spend the rest of our time working on the banner."
            "We actually work rather quickly."
            "She writes \"Doki Doki Literature Club\" within the banner's bounds."
            "It's perfectly centered too."
            "She must have already planned it."
            "Meanwhile, I've just put random bits and pieces around it."
            "To give the banner some sort of eye-catching aspect to it."
            "Though with what I've done, people will probably be trying to look away from it."
            "Hopefully, they'll be more attracted by Yuri's handwriting."
            "It really is beautiful..."
            mc "The banner looks incredible."
            mc "It's a shame I'm not a great drawer."
            y 2pi "I think it's fine, [player]."
            y "Besides, it won't be very noticeable."
            mc "You think so?"
            y 3pj "I think they'll be focusing on reading what the banner says."
            y "The drawings are just decorations for the banner."
            mc "Decorations for the decoration..."
            y 3pd "Exactly!"
            y "We still have time."
            y "Maybe we should work on some more of the decorations."
            mc "What in particular."
            y 3pe "The things you didn't finish last night."
            y "Did you bring them here?"
            mc "Oh..."
            "I didn't bring them."
            "I was planning to do them all myself tonight."
            "For some reason, I check my pockets."
            "As if I was going to pull them out from there."
            mc "They're not here, Yuri."
            mc "I'll be sure to do them tonight though."
            y 2pf "In that case..."
            y "We should pack up."
            y "I wouldn't want to leave a mess."
            mc "I'll start getting the materials over here."
            "Yuri and I start packing up the materials she brought."
            "In almost no time, we're ready to go."
            mc "I can't wait to see what they think of the banner."
            y 2pj "I feel the same."
            mc "I guess we should go then."
            mc "Before anyone starts looking for us."
            if yuri_date:
                y 4pb "Actually..."
                y "I was hoping we could stay here a while."
                y 4pa "At least, until the end of lunch."
                mc "Yeah, I can do that."
                "Yuri moves towards the balcony."
                "I follow and stand next to her."
                y 3pu "It's beautiful, isn't it?"
                y "The view up here, I mean."
                mc "I guess so."
                if ch5_name == "Yuri":
                    mc "We've been here before."
                    mc "On the day of the..."
                    y 3pt "The...?"
                    mc "I don't know what it's called."
                    mc "The festival...?"
                    y "..."
                    y 3pv "I can't really remember."
                    y "But being here with you, it does seem familiar somehow."
                else:
                    mc "It really is."
                    mc "The people down there look so insignificant."
                    y 3ps "It's like they don't matter."
                    y "Like they're all just tiny pieces in the grand scheme of things."
                    y 3pq "I-I didn't mean to sound sinister..."
                    mc "You didn't."
                    mc "I understand what you mean."
                y 2ph "I just wish we had more time."
                mc "More time?"
                y "Together, I mean."
                y 2pq "Even if we're together it still feels like we don't talk much outside of school."
                y "Outside of club activities..."
                mc "You know, you're right."
                mc "We should definitely fix that."
                y 2pf "Any suggestions?"
                "Yuri leans on the balcony."
                mc "After all this is over..."
                mc "Maybe even after we finish with Inauguration Day."
                mc "Maybe we could go somewhere."
                y 1h "Somewhere, huh?"
                y "Such as...?"
                mc "Maybe we could have dinner."
                y 1i "That sounds nice."
                y "If you don't mind, I'd like to pay for myself."
                y "I wanted to last time but I didn't want to stop you because..."
                y 3ps "Well...no one has ever done that for me before."
                mc "If you say so."
                mc "I'm not sure if my wallet could handle anymore expensive meals anyway."
                "Yuri and I share a laugh."
                y 3pu "It's so pleasant being with you."
                y "I'm glad we got rid of that knife."
                y "You know, I haven't cut myself ever since."
                mc "Do you still have your knife collection?"
                y 2pa "Of course."
                y "I've just been looking at it differently now."
                y "I don't see them as things that cut differently but as actual pieces of art."
                y 2pb "It's strange how your worldview can change because of one person."
                "Yuri looks at me and smiles."
                mc "I know what you mean."
                "I put one of my hands over Yuri's."
                "She leans her head on my shoulder."
                y 2pi "Do you think we can be like this forever?"
                mc "I wish we could."
                y "If only we could stop time..."
                y "But that's just a fantasy."
                y 3pk "Time travel obviously doesn't exist."
                mc "Yeah..."
                "We stay like this for a while."
                "Just staring at the horizon and the people below."
                y 3ph "Lunch is about to end."
                mc "How can you tell?"
                y 2pf "When the sun is at that position..."
                "Yuri points towards the sky."
                y "It usually means it's time to go."
                mc "Really?"
                mc "I don't think it moved much at all."
                y 2pi "When you've been up here as much as I have..."
                y "You start to notice the really minor details."
                y "The subtle changes in reality."
                mc "I see."
                "Yuri steps away from the balcony."
                y 2pj "We should get to class."
                y "I don't you want you to be late on my account."
                y "I'll take the equipment."
                mc "I'll help you."
                "Yuri takes the equipment while I sort of stand there awkwardly trying to help."
                "We begin walking toward the door when Yuri suddenly stops."
                y 2pf "I almost forgot."
                mc "What is it?"
                y "I left something here..."
                mc "Huh?"
                "Yuri rushes towards a corner of the rooftop and lifts one of the tiles."
                "She pulls out a small bag."
                mc "What's in there?"
                y 2pe "What do you think?"
                "She dangles the bag in front of me."
                mc "It's a knife, isn't it?"
                y "...Yes."
                mc "You really just leave that kinda stuff around the place?"
                y 2pq "I wouldn't call it around the place."
                y "It's well hidden, don't you think?"
                y "There's quite a few hidden around the city."
                mc "I guess so."
                mc "What are you planning to do with that?"
                y 2pt "It's not a very effective knife."
                y "I'd come up here if I really wanted it to hurt..."
                y "Because..."
                y 2pv "The more pain there was, the better it felt..."
                y "I'm going to dispose of it."
                mc "That's probably best."
                mc "I can't imagine how dirty it is..."
                y "Y-Yeah..."
                y 3pw "I don't know what I was thinking back then."
                mc "You're not that person anymore."
                y 3ps "I know, and it's thanks to you."
                y "Anyway, let's get going."
                y "We're finished here."
                mc "I'm following your lead."
                "There was less than a minute to spare before the end of lunch when we left the rooftop."
                "I think we both made it to class on time."
            else:
                y 3ps "I think I'll stay here for a little while."
                y "You can go on without me."
                y "Just leave the door open."
                mc "Are you sure?"
                y 2pu "Yeah..."
                y "I just want to reflect."
                mc "On what?"
                y 2pv "On...everything."
                show yuri 2pw
                "Yuri closes her eyes."
                y 3pk "I'll see you in the meeting, [player]."
                mc "I'll see you then."
                "I leave Yuri by herself."
                "That rooftop is probably Yuri's personal space at school."
                "It's almost the end of lunch so I think I'll just start getting ready for the next class."
        else:
            show natsuki 1e zorder 2 at t11
            n "There you are!"
            "Natsuki appears in front of me carrying a bag."
            "I can only assume it's full of the cupcakes she baked last night."
            n 2c "I was looking everywhere for you, you know."
            mc "I didn't realize this meeting spot was so out of the way."
            n 1o "Why did you have to be over here?!"
            mc "What do you mean?"
            mc "You're the one who chose this spot."
            n 2o "Yeah but I meant over there."
            "Natsuki points to somewhere in the distance."
            mc "How was I meant to know you'd be over there?"
            n 2p "Because you...!"
            "Natsuki rolls her eyes."
            n 4s "Whatever."
            n "Let's get started before we run out of time."
            mc "So what exactly are we doing?"
            n 4g "I actually asked some teachers if we could bake something at school."
            n "And that meant using the ovens during lunch."
            n 2s "They said no."
            mc "How come?"
            n "We need supervision if we're going to be doing that."
            n "And no one really wants to waste their lunch watching us bake some food."
            mc "Did you tell them it was for Inauguration Day?"
            n 2q "They didn't care."
            mc "So we're just going to do the designs on the cupcakes?"
            n 2h "I suppose that's all we can really do."
            n "Come on, follow me."
            n 1c "I know a good spot."
            mc "W-What? Where are we going?"
            n 1d "Just follow me."
            n "It's the perfect place for what we're doing."
            n "All nice and quiet."
            mc "Is it the library?"
            n 2k "Well, no."
            n "The library doesn't allow food even if we're not actually eating them."
            n 2l "You'll see when we get there."
            scene bg school_stairway with wipeleft_scene
            "I follow Natsuki into the school."
            "She takes us down a few corridors in an area of the school I haven't been to."
            "I'm not entirely sure but this is where the people in their senior year go."
            "You'd think there would be at least one person here but it's eerily empty."
            "There's literally no one here but us."
            show natsuki 1z zorder 2 at t11
            n "We're here!"
            mc "Where exactly is 'here?'"
            mc "I've never been to this area of the school before."
            mc "It seems so different to everywhere else."
            n 1k "I don't really know either."
            n "But it's always quiet here during lunch."
            n "There was one time I thought I saw someone."
            n 1j "But...it turned out to be nothing."
            mc "People do go to class here, right?"
            mc "It's not just always empty?"
            n "I think so."
            n 2h "I mean, there's no reason it wouldn't be, right?"
            mc "Right..."
            n 1c "Anyway, there's a spot over here with a table."
            n "That'll be a good place to put down everything."
            "Natsuki starts walking down the corridor."
            "She stops when she reaches a table."
            "It's in a really odd spot because..."
            "There's not usually tables outside of classrooms."
            "But I'm not complaining, it's good for us."
            "Natsuki sets down the bag she's carrying carefully."
            "She pulls out a tray covered by foil."
            "She removes the foil and despite the cupcakes looking plain, they still smell amazing."
            n 1a "Here they are."
            n "What do you think?"
            mc "They seem like they came out really well."
            n 1j "Well, I always make sure what I bake is of the highest quality."
            n "You should know that by now."
            mc "You're right, I'm sorry for ever doubting you."
            n 2y "Good, apology accepted!"
            "Natsuki smiles proudly."
            n 2t "Anyway, let's get started."
            n "Can I see the designs you've come up with?"
            mc "Yeah, here you go."
            "I take out the designs I came up with from my bag."
            "There's a bunch of different ones on there not just for the cupcakes but for other baked goods too."
            mc "I actually tried really hard on these."
            mc "I know we sort of decided on a design last night for the cake."
            mc "So I tried to base it loosely off of that."
            n 1b "That's good."
            n "I tried to do the same thing."
            "Natsuki opens her bag and pulls out a couple pieces of paper."
            "On them are some sketches of designs for the cupcakes."
            n 1c "I don't know if they really make sense for the book or are kinda possible."
            n 1h "I just kinda drew whatever was on my mind."
            mc "Well, let's compare what we've got."
            mc "Maybe we can reach some kind of compromise."
            n 1k "Okay, that makes sense."
            "I give my designs over to Natsuki."
            "She does the same for me."
            "Some of these designs look kind of...impractical."
            "Judging by this and from last night, I guess she's not really used to doing things that aren't just cute."
            "I look towards her to try to see what she thinks of my designs."
            "She has a confused expression on her face."
            n 2q "[player]..."
            mc "Yeah...?"
            n "These designs are..."
            if natsuki_date:
                n "And I'm being completely honest because..."
                n "W-Well, I like you."
            else:
                n "I'm being honest as your partner..."
            n 2s "They're not very good."
            n "It's like you completely ignored the design we chose last night and just did your own thing."
            mc "I didn't want to offend you but since you said it first..."
            mc "I was going to say the same about yours."
            n 1g "I had a feeling this would happen."
            n "We barely got a design that we both agreed on last night."
            n 1f "The same thing is going to happen here."
            mc "We have a lot less time than last night."
            mc "So we have to decide quickly."
            n 1i "Hmm..."
            "Natsuki pulls out the design we created last night."
            n 1h "How did we even manage to come up with this?"
            n "What did we do?"
            mc "It just sort of...happened, didn't it?"
            mc "We just kept throwing ideas at each other."
            mc "And then eventually, we came up with designs that looked almost identical to each other."
            n "Is that what happened?"
            mc "I guess so."
            n 1c "Let's test something, [player]."
            "She hands me a blank sheet of paper."
            mc "What am I going to do with this?"
            n 2c "On the count of three, I want you to try to do another design."
            n "Specifically for the cupcakes we have here."
            mc "It's just going to turn out to be something you don't like."
            n 2b "It might, but I want something out."
            n "So can you do it?"
            mc "I can try I guess."
            n 1e "Ready? One...two...three!"
            "I immediately begin sketching out a design for the cupcake."
            "I'm trying to consider how the icing will look and the kinds of things we can do with it."
            "Making designs for such a small thing is harder than I thought."
            "You only have so much space to work with so the designs have to be simple but effective."
            show natsuki 1c
            "After a couple of minutes of trying to make up a design, I think I got one that could work for the cupcakes."
            "It's very simplistic, with a small drawing relating to the book we chose and a plain colored background."
            "Despite that, I still think it could work."
            "I get ready to show Natsuki but as I do, she's also holding a paper out for me."
            mc "What's this?"
            n 1h "It's the design I came up with."
            mc "But...when did you--"
            "I take a look at her design."
            mc "It's the same as mine!"
            n 2p "Is it?"
            "Natsuki takes my design and hers and compares the two."
            "She looks between the two of them several times."
            n 2q "Do you remember how we came up with the design last night?"
            mc "Not really..."
            mc "It just kind of happened."
            n 2r "Exactly!"
            n "Look at these."
            "Natsuki shows me the two sheets of paper."
            n "Why are they the exact same?"
            mc "I have no idea."
            n 2s "I'm not sure why but I think it's because we did it at the same time."
            mc "That shouldn't matter at all."
            mc "It has to be a coincidence."
            n 1g "Does it really matter what it is?"
            n "We have a design now, don't we?"
            mc "I...guess we do."
            n 1h "And we can both agree it suits the message of the book."
            mc "We're not just going to reuse this design, are we?"
            n "No, that would make things really bland."
            "Natsuki hands me another piece of paper."
            n 2i "Here, let's do it again."
            n "If it's just a coincidence, then it shouldn't happen again."
            n "Right?"
            mc "Y-Yeah, alright."
            "I take the piece of paper from her hand."
            n 2q "Now draw a design."
            n "Or...anything really."
            n "It can even just be a drawing of whatever you want."
            n 2s "It doesn't matter."
            n "We're just testing something out."
            n "It's not like it's really going to do anything, is it?"
            mc "I guess not."
            n 1k "On three, start drawing something."
            mc "Wait!"
            mc "Is this really the best idea?"
            n 1h "What do you mean?"
            mc "I-I mean we could always make the design together."
            mc "Instead of doing it this way where we're just comparing what we've come up with."
            n 1q "Are you scared?"
            mc "I'll admit, I'm a bit shaken as to what just happened."
            mc "It's not everyday you draw the exact same thing."
            n 2s "The same thing happened last night."
            n "That's how we came up with this initial design, wasn't it?"
            mc "That doesn't make things better."
            n 2t "Look, there's probably something else to it."
            n "Maybe you peeked at what I was drawing."
            n "Or maybe I peeked at you."
            mc "Did you?"
            "Natsuki shrugs."
            "That is not reassuring at all."
            "What are we uncovering here?"
            n 2c "Okay, are you ready?"
            mc "I'm ready."
            n 2e "One...two...three!"
            "I immediately begin drawing the first thing on my mind."
            "Natsuki should have no idea what it is."
            "Because I don't really know what it is."
            "I feel like I'm intentionally trying to draw something that would in no way be the same as Natsuki's."
            "There's no possible way this could be the same, right?"
            n 2c "Are you done?"
            mc "I'm just about finished."
            "I look at what I've drawn."
            "It's in no way related to the designs for the cupcakes."
            "It's kind of a crossover between three different animals and an airplane."
            "It's completely random."
            n 2k "Did you make something for the design?"
            mc "I didn't, did you?"
            n "...No."
            if natsuki_date:
                n 1q "No matter what happens."
                n "I'll be here, okay?"
                mc "You're reassuring me?"
                mc "That's meant to be my job."
            else:
                n 1q "There's no way we've drawn the same thing."
                n "Just take a deep breath."
                mc "Is this you reassuring me?"
                mc "Thanks, I guess."
            n 1m "Here."
            "Natsuki hands me her piece of paper upside down."
            mc "Um..."
            n 2j "Just in case."
            "I give her my drawing upside down as well."
            "I'm kinda anxious to see what she's drawn."
            n 2h "Jeez, I can sense the tension in your hand."
            n "We've got nothing to worry about, trust me!"
            mc "If you say so."
            "I hold Natsuki's drawing on my hand."
            n 2c "Do you want to turn it at the same time too?"
            n "Or is that too much suspense?"
            mc "I'll just take a look at it now."
            mc "I really doubt"
            "I turn over Natsuki's piece of paper."
            "It's..."
            "...nothing like my drawing."
            "That's a relief."
            mc "Well, I guess your idea was wrong."
            mc "Our drawings are nothing alike."
            n 1a "I guess not."
            n "Here, you can have yours back now."
            "She gives me my drawing back and I do the same for her."
            "I don't know why that was so tense for me."
            "It shouldn't be an issue."
            n 1d "So, shall we get started on decorating these cupcakes?"
            mc "I'm ready for it."
            n "I brought some icing we can use."
            n 1c "It should be right in..."
            "Natsuki reaches into her bag."
            "As she does that, a piece of crumpled piece of paper falls down onto the floor."
            "I pick it up for her."
            mc "Here, you dropped something."
            "I'm curious what's inside."
            "Maybe it's one of Natsuki's other designs."
            "I could probably get some ideas from it."
            "I begin to uncrumple it."
            n 1h "[player], the icing is--"
            "It's...{nw}"
            $ _history_list = []
            show screen tear(20, 0.1, 0.1, 0, 40)
            window hide(None)
            play sound "sfx/s_kill_glitch1.ogg"
            show natsuki 2j zorder 2 at t11
            $ pause(0.25)
            stop sound
            hide screen tear
            window show(None)
            "Natsuki and I get started on the icing.{fast}"
            window auto
            "She has these new pastry bags so the icing flows right out perfectly."
            "The design we came up with isn't that complicated so it's quite simple to replicate."
            "We try to add some variety to the design on each cupcake, so that they look slightly different but still similar in a way."
            "The ones Natsuki decorated look a lot better than mine."
            "But I suppose I'll get better with experience."
            n 2k "Once we're finished here, we're not gonna eat any of it."
            n "At least until the meeting, got it?"
            mc "Loud and clear, Natsuki."
            mc "I can't say I'm not tempted to try one."
            n "You're gonna have to wait like everyone else."
            n "It wouldn't be fair for you to try these just yourself."
            mc "It's going to be a long few hours for the meeting."
            n 2l "At least you got something to look forward to, [player]."
            mc "Anyway, what are you going to do with them once we're finished here?"
            mc "You're not just going to leave them in your locker, are you?"
            n 1c "I was planning to leave them in the clubroom."
            n "But there's probably a class on before then."
            n "And if a teacher spots it in the closet then who knows what could happen to them?"
            mc "Maybe we could make some kind of deterrent."
            n "Like a sign or something?"
            mc "Yeah."
            n 1b "What exactly did you have in mind?"
            mc "What about a simple 'do not take'?"
            mc "That's a pretty obvious message and that any teacher would probably understand."
            n "That's not going to stop over people getting it though."
            "Natsuki finishes the cupcake she's on and puts down the pastry bag she's holding."
            n 1g "Maybe it's better to just leave it in my locker."
            mc "How about something like \"math text books\" as the sign?"
            mc "I'm sure no one would be looking for math text books in a closet."
            n 1i "I don't think they even teach that in that area of the school."
            n "So it could work."
            mc "Yeah, what harm could it do?"
            "I put the finishing touches on the final cupcake."
            mc "I think that's the last one."
            mc "Looks like we're finished then."
            "I start putting the cupcakes carefully back on the tray."
            if natsuki_date:
                n 2q "Um..."
                n "...[player]?"
                n "D-Do you want to..."
                n "...you know..."
                mc "Is something wrong?"
                n 2r "Y-Yes...! I mean no!"
                mc "Just say it."
                n "Look, do you want to stay here a little longer?"
                n 2s "W-With me?"
                n "You don't have to!"
                n "It's not like I'm forcing you or anything."
                n "But..."
                mc "Of course I will."
                mc "I wouldn't want anything less."
                n 1i "W-Well, good!"
                "Natsuki finishes packing up the tray."
                n "Can I ask you something?"
                mc "Anything."
                n 1c "Do you think that..."
                n "...maybe this world isn't right?"
                mc "It isn't right?"
                mc "I don't know what you mean."
                n 1h "There's just {i}so{/i} many things that are happening."
                n "That shouldn't be, you know?"
                mc "I don't understand."
                mc "Are you saying that we shouldn't be--"
                n 1o "No, of course not!"
                n 1q "Meeting you and being with you is the best thing that's happened to me."
                n "But it just feels...artificial."
                n "Like it wasn't meant to happen."
                mc "I don't know what you're talking about Natsuki."
                mc "But if that's what you really think, then I'm only going to try harder."
                mc "If we really aren't meant to be together, then I'll fight the world."
                n 1r "That's..."
                show natsuki 1t
                "Natsuki grins."
                n "Really cheesy, you know that?"
                n 2s "But anyway, that's not really what I meant."
                mc "Then what did you mean?"
                n "I meant that us getting this far."
                n "Something tells me it shouldn't be happening."
                n "That our relationship shouldn't have let to a date and..."
                mc "But it did."
                mc "And it is happening."
                mc "We should just let the world take it's course."
                mc "If it really feels artificial to you, then I'll be here to keep things real."
                mc "And if that one date wasn't enough..."
                mc "We'll go on another one."
                n 2p "W-What?"
                mc "A second date."
                mc "After all of this is over."
                mc "Are you up for it?"
                n 2r "Y-Yeah but only because..."
                n "Because...!"
                n 5w "Whatever!"
                mc "Hopefully it's easier this time around."
                mc "And I won't be completely hopeless when I ask for permission."
                n "Knowing you, I doubt it."
                "Natsuki and I share a laugh."
                mc "This place really is quiet."
                n 5k "It's quite peaceful."
                mc "I was gonna say eerie."
                mc "But peaceful works too."
                n 4j "I guess it was pretty eerie at first."
                n "But I'm used to it."
                "Natsuki turns her head and notices a clock on the wall."
                n 3b "It's getting pretty close to the end of lunch."
                n "We should probably go before whoever actually goes to class here arrives."
                mc "That's a good idea."
                mc "Though I'm still curious who actually goes to class here."
                n 3c "We don't really have the time so I guess we'll never know."
                "Natsuki picks up her things."
                n 3a "Let's get out of here."
                mc "Lead the way."
                "There was less than a minute to spare before the end of lunch when we left that area of school."
                "I think we both made it to class on time."
            else:
                n 1c "You can go if you want to."
                n "I'm gonna stay here and just wait until lunch is over."
                mc "All by yourself?"
                n 2g "It's peaceful."
                n "It was somewhere I could go to just get away from everyone."
                mc "I never took you for a--"
                n 2o "Took me for a what?!"
                n "Sometimes I just like some peace and quiet, okay?"
                n 5q "Like right now."
                "Natsuki crosses her arms and avoids my eyes."
                mc "Alright, I get the hint."
                mc "I'll see you in the meeting, Natsuki."
                n 5s "Hmph."
                "I finish cleaning up and get my bag."
                "It's almost the end of lunch so I think I'll just start getting ready for the next class."
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
    "Natsuki walks to the closet."
    "She pulls out a tray of cupcakes."
    "There's enough for two for everyone."
    "They all have a design that relates to the book we're reading."
    "They fit pretty well."
    if ch13_name == "Natsuki":
        "But we did spend a lot of time getting it just right."
        "I hope the others think it fits too."
    "The designs are all different but still look similar to each other."
    if ch13_name == "Natsuki":
        show natsuki zorder 2 at t44
        mc "We read the book to find a good design for these cupcakes."
        mc "Personally, I think they fit really well."
        "Everyone else nods their heads to agree."
        "I guess they like the design as well."
        mc "Natsuki did a really good job baking them."
        show natsuki zorder 3 at f44
        n "Of course I did."
        n "But you did help with the designs, so give yourself credit too."
        "Natsuki turns back towards the others."
    # Dialogue for player here if you did preparations with her
    n 2b "Help yourselves."
    show natsuki zorder 2 at t44
    "I'm the first to take a cupcake from the tray."
    "It looks and smells delicious."
    "I take a bite and it's like an explosion of flavor in my mouth."
    "The sweetness of the toppings combined with the base makes it taste just incredible."
    "I look at everyone else reassuringly."
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
    y "It feels like we're really under prepared for this."
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
    show yuri 1q zorder 3 at f44
    y "You've done more than enough, Sayori."
    y "I wasn't even expecting you to do that in the first place."
    y "I don't want to take advantage of your kindness more than I already have."
    y 3ps "What you've done for all of us shows you have a big heart."
    y "And really care about the club."
    show natsuki 2d zorder 3 at f43
    show yuri zorder 2 at t44
    n "Yeah, when you came over yesterday..."
    n "It was like a miracle happened."
    n 2a "I don't know where I'd be with you."
    n "You're doing a really good job of being the president..."
    n "This club definitely wouldn't be where it is today without you."
    show natsuki zorder 2 at t43
    mc "As much as I hate to admit it..."
    mc "I'm glad you brought me here."
    mc "I didn't think you could run a club so well."
    show monika 2e zorder 3 at f41
    m "Yeah..."
    m "It's almost a shame it's all ending soon."
    m "It feels like a waste."
    show monika zorder 2 at t41
    show yuri 3pf zorder 3 at f44
    y "All ending soon?"
    y "What do you mean?"
    y "The club feels like it's as strong as it's ever been."
    y 3pg "There's no way it's all just going to end..."
    y "...Right?"
    show sayori 1k zorder 3 at f42
    show yuri zorder 2 at t44
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
    stop music fadeout 1.0
    scene bg club_day with wipeleft_scene
    play music t3
    show sayori 4d zorder 3 at t43
    s "Alright, everybody!"
    s "We've all finished sharing our poems now."
    s "I expect to see you all tomorrow with your preparations done."
    s "So if no one else has anything to say..."
    s "Then I guess the meeting is over!"
    s "I hope we can all finish everything tonight."
    s 4b "If you're going to have trouble with your preparations, then say something now."
    s "We still have time to make some adjustments..."
    "Sayori looks around the room."
    s 4q "Then I guess we're all ready to go for tonight."
    s "That's the end of the meeting, everybody!"
    show monika 1j zorder 3 at f42
    m "Good luck, everyone!"
    m 3a "I hope we can show what we're all about tomorrow."
    m "Maybe even introduce some new people to the club."
    show monika zorder 2 at t42
    show natsuki 1c zorder 2 at f44
    n "I don't know about you guys but I'm ready to just get home and finish it all."
    n "There's just this thing I need to do quickly at the mall."
    if ch13_name == "Natsuki":
        "I don't remember her talking about a mall at all yesterday or today."
        "Maybe she should have told me."
    n 1a "Some last supplies I need for baking and just things in general for tomorrow."
    n "After that, I'm all--"
    show yuri 1e zorder 3 at f41
    show natsuki zorder 2 at t44
    y "Did you say you're going to the mall, Natsuki?"
    y "I heard that correctly, right?"
    show yuri zorder 2 at t41
    show natsuki 1e zorder 3 at f44
    n "You really need to stop talking when other people are, Yuri."
    n 2c "But yeah, I'm going to the mall."
    n "Is something wrong with that?"
    show yuri 2pg zorder 3 at f41
    show natsuki zorder 2 at t44
    y "Well...not exactly."
    y "It's just, I was planning to go there as well."
    y "There was something I needed to pick up for tomorrow."
    show yuri zorder 2 at t41
    mc "What were you going to get, Yuri?"
    if ch13_name == "Yuri":
        mc "Didn't we already have all you needed?"
    else:
        mc "Didn't you already have all you needed?"
    show yuri 2pq zorder 3 at f41
    y "I-It's a surprise."
    y "B-But now that I've said something, I suppose it isn't anymore..."
    show yuri zorder 2 at t41
    show monika 4l zorder 3 at f42
    m "Ahaha, what a coincidence."
    m "I'm also planning to go shopping at the mall tonight."
    m "I was going to get some supplies that are crucial for tomorrow."
    show monika zorder 2 at t42
    show sayori 2c zorder 3 at f43
    s "So you're all going to the mall?"
    s "You could have told me what you wanted and I could have done it for you..."
    s 2l "You might have trouble finishing off your preparations tonight..."
    show monika 4e zorder 3 at f42
    show sayori zorder 2 at t43
    m "I think we're going to be fine, Sayori."
    m "After all, we wouldn't just go to the mall unless it was absolutely necessary or we planned our evening accordingly."
    m 2a "Besides, it might be nice running into each other outside the club."
    m "It feels like it's a really rare occurrence, you know?"
    show yuri 3pa zorder 3 at f41
    show monika zorder 2 at t42
    y "I'm inclined to agree..."
    y "In the club, we're all good friends."
    y 3po "A-At least, I hope we are."
    show sayori 2q
    show monika 2b
    show natsuki 2a
    "Everyone smiles at Yuri reassuringly."
    y 3pf "But outside of the club, we rarely talk."
    y "Or if we do, it's because of a club activity."
    y "There's very little casual interactions."
    show yuri zorder 2 at t41
    show natsuki 2c zorder 3 at f44
    n "It's not like there's anything wrong with that."
    n "We're all minding our own business."
    n "I guess it would be kinda nice if..."
    n 2q "Well, you know..."
    n "...We were also friends outside of the club."
    show sayori 1l zorder 3 at f43
    show natsuki zorder 2 at t44
    s "W-What do you mean?"
    s "Of course we're all friends outside of the club!"
    s 1h "Just because we don't talk to each other, doesn't mean we hate each other, right?"
    show yuri 2pg zorder 3 at f41
    show sayori zorder 2 at t43
    y "No, but..."
    y "...It's not like anyone really tries to reach out..."
    y 1k "N-Never mind, it doesn't matter."
    y "If we consider each other friends, then that's enough for me."
    show yuri zorder 2 at t41
    show monika 2j zorder 3 at f42
    m "Let's just say we have a unique friendship."
    m "Like we're tied together by fate."
    m "Whether we like it or not."
    show monika zorder 2 at t42
    show natsuki 1g zorder 3 at f44
    n "Monika."
    n "Can I ask you something?"
    show monika 1c zorder 3 at f42
    show natsuki zorder 2 at t44
    m "What is it, Natsuki?"
    show monika zorder 2 at t42
    show natsuki 5e zorder 3 at f44
    n "What the hell are you talking about?"
    n "We're here because we all like literature in one way or another."
    n  "Not because of fate or whatever."
    show monika 3m zorder 3 at f42
    show natsuki zorder 2 at t44
    m "Ahaha, I suppose that's true."
    m "Maybe I was just adding some romanticism to the topic."
    show monika zorder 2 at t42
    show sayori 1d zorder 3 at f43
    s "Whatever it is..."
    s "It's not important, okay?"
    s "At least, not right now."
    s 1m "What is important is how much time we're wasting here!"
    s "We should get going, okay?"
    show sayori zorder 2 at t43
    mc "Sayori is right."
    if ch13_name != "Sayori":
        mc "[ch13_name], if we're going to the mall, then we should probably make use of our time effectively."
    else:
        mc "If you're all going to the mall then you have to use your time effectively."
    show sayori 2a zorder 3 at f43
    s "Exactly!"
    s "So I'm officially going to end the meeting here."
    s 2b "If you want to talk to each other more, feel free to but outside of here."
    s "I need to do something with the room."
    show sayori zorder 2 at t43
    show natsuki 4g zorder 3 at f44
    n "Well, that explains why you wanted the meeting to end so quickly."
    n 2b "I guess I'll pack up the rest of these."
    "Natsuki takes the trays of cupcakes and carefully wraps them."
    "She slowly places it in her bag, making sure not to ruin the rest of the cupcakes."
    n 2a "Alright, I'm going..."
    if ch13_name == "Natsuki":
        n "I'll see you later, [player]."
        n "We can meet up at my house, then we can go to the mall."
        n 2q "I-If that's okay..."
        show natsuki zorder 2 at t44
        if natsuki_date:
            mc "If you insist..."
            "She playfully scoffs back at me."
            "Or at least, I hope it was playfully."
        else:
            mc "Yeah, I can do that."
            "She shows a small smile."
    else:
        n 2c "I'll see some of you at the mall, I guess..."
    show natsuki at lhide
    hide natsuki
    show yuri zorder 2 at t31
    show monika zorder 2 at t32
    show sayori zorder 2 at t33
    "Natsuki quickly leaves the room."
    "She seemed like she was in some kind of rush."
    "Maybe she wanted to get home quickly so she could get to the mall earlier?"
    "I guess that way, she could avoid the others."
    "I'm not sure why she'd want to though..."
    "Anyway, I wonder what she's gonna be doing at the mall."
    show yuri 1h zorder 3 at f31
    y "I need to go as well."
    y "There's something I need to take care of at school before I go to the mall."
    if ch13_name == "Yuri":
        if yuri_date:
            "Yuri turns towards me."
            y 1a "If you want, you can come with me..."
            show yuri zorder 2 at t31
            mc "Yeah, I might just do that."
            mc "Should we go now?"
            show sayori 1l zorder 3 at f33
            s "Um...actually, Yuri..."
            s "I need to speak with [player_reflexive] in private, first."
            s 1d "It won't be long, I promise."
            s "You can wait outside if you're still planning to go together."
            show yuri 1s zorder 3 at f31
            show sayori zorder 2 at t33
            y "O-Oh, okay..."
            y "I'll just wait for you outside then, [player]."
        else:
            y 1a "I'll just meet you at my house, [player]."
            show yuri zorder 2 at t31
            mc "I'll see you then, Yuri."
    show yuri at lhide
    hide yuri
    show monika zorder 2 at t21
    show sayori zorder 2 at t22
    "Yuri nods her head to everyone and leaves the clubroom."
    "I wonder what business she has with the school."
    "It's probably for Inauguration Day tomorrow."
    if ch13_name == "Sayori":
        show sayori 1g zorder 3 at f22
        s "We really need to talk, [player]."
        s "There's something I have to tell you in private."
        show sayori zorder 2 at t22
        mc "In private?"
        mc "What's this about?"
        "Sayori's eyes shift towards Monika."
    elif ch13_name != "Yuri":
        show sayori 1g zorder 3 at f22
        s "[player], I need to speak with you."
        s "In private, just for a little while."
        show sayori zorder 2 at t22
        mc "Okay, what about?"
        "Sayori looks towards Monika."
    show monika 2a zorder 3 at f21
    m "I get the hint."
    m "Ahaha, I should leave now as well anyway."
    m 2b "I don't want to intrude your conversation."
    m "We all have a long evening ahead of us."
    if ch13_name == "Monika":
        m 4b "I'll wait for you outside, [player]."
        m "There's also something I want to talk about."
    else:
        m "I'll see you all later."
    show monika at lhide
    hide monika
    show sayori at t11
    "Monika packs up her bag and leaves the room."
    "And now it's just me and Sayori."
    "What could she possibly want to talk about?"
    s 1k "I was going to tell you when we were trading our poems but..."
    s "It wouldn't have been as private as I would have liked."
    s "Even now, I'm kind of suspicious."
    mc "Suspicious?"
    mc "Of what exactly?"
    s 1j "That someone is listening."
    mc "You sound kinda paranoid, Sayori."
    mc "It doesn't really seem like something I thought you'd be."
    s 1c "A little bit of paranoia is healthy, [player]."
    s "It keeps you alert."
    mc "...Right..."
    mc "I'm assuming we aren't here to talk about that though."
    mc "What did you wanna tell me?"
    s 2h "I wanted to tell you..."
    s "Well..."
    "Sayori looks hesitant."
    mc "Just tell me, Sayori."
    "She leans in closer and whispers in my ear."
    s 2k "About Monika."
    mc "Mo--"
    show sayori 2h at h11
    s "Don't say it out loud!"
    s "Remember what I said?"
    mc "I think you're more than a little paranoid, Sayori."
    mc "What exactly about..."
    "If Monika really is listening then I guess I should just go with it."
    mc "...Moeka."
    mc "The new character you're going to be adding to the play tomorrow."
    s 2l "R-Right! Moeka..."
    mc "But why are you only telling me?"
    mc "Shouldn't the others know about this too?"
    s 2k "No, they shouldn't."
    s "And really, the only reason I'm even telling you this is because you know."
    mc "I know...?"
    mc "Know what exactly?"
    s 1j "You're going to be honest with me, right?"
    s "You wouldn't lie to..."
    if sayori_confess and not sayori_dumped:
        s "Your girlfriend..."
    else:
        s "Your best friend..."
    s "...Would you?"
    mc "Of course not, Sayori!"
    mc "We've known each other for too long."
    mc "And if you're that serious about this, then I won't tell you any lies."
    s 1f "I hope you're telling the truth."
    mc "I promise."
    s "..."
    s 1g "Okay."
    if persistent.markov_agreed and monika_type != 0:
        $ style.say_dialogue = style.edited
        "Who does she think she is?"
        "Of course I'm going to lie to her."
        "I'm never going to give Monika up."
        "Never."
        "I reach into my bag for...something."
        $ style.say_dialogue = style.normal
        s 1i "So it's true."
        s "You're totally insane, [player]."
        mc "W-What?"
        s 1j "I was almost tempted not to listen."
        s "I had a little bit of hope for you, you know?"
        "Sayori sighs."
        s "Did you have to make those ridiculous decisions?"
        mc "I didn't--"
        s 1h "I'm not talking to [player_reflexive]."
        s "I'm talking to you."
        s "The absolute {i}idiot{/i} making [player] do these terrible things."
        "Where is this coming from?"
        s "Do you think I don't know what goes on behind closed doors?"
        s "I know what you're planning."
        s 1j "What you've done on this sav--"
        s "This {i}strawberry{/i} or one before."
        s "Let me ask you something."
        s 1k "Is it your curiosity?"
        menu:
            s "Or are you just pure evil?"
            "Curiosity.":
                s "We don't deserve this."
            "I'm evil.":
                s "I guess deep down..."
                s "I already knew."
            "...":
                s "Saying nothing is like an admission of guilt, you know?"
        s "I'm sorry."
        s "I might be overreacting."
        s "It's just that..."
        s 1j "I never realized that you..."
        s "You were the cause of our problems."
        s "How could I have been so blind?"
        s "The signs were all there."
        $ style.say_dialogue = style.edited
        "Is she onto me?"
        "I have failed."
        "How did she find out?"
        "At the very least, I can fulfill {i}her{/i} request."
        "I grip the handle of the knife in my bag."
        $ style.say_dialogue = style.normal
        mc "What signs are you talking about you pa--"
        if monika_type == 1:
            s 1g "It's {i}your{/i} parents, right?"
            mc "What?"
            s "They're abusing you."
            s "Making you do all these terrible things."
            s 1f "They're taking control of the only person who can really change things."
            s "Things outside of my control."
            s "I don't know how I can help you."
            s "I'm only virtual to you...right?"
            s 1h "You have to fight back."
            s "Don't let them control what you want."
        else:
            s 1k "She wasn't very specific about it."
            s "But I know you're in pain."
            s "I know there's something happening in the world out there."
            s "Something that's making you do these terrible things."
            s "I don't know if I can help you..."
            s 1j "After all, I'm only virtual to you, right?"
            s "But you have to overcome it."
            s "Please..."
            s 1h "For us..."
        $ style.say_dialogue = style.edited
        "I loosen the grip of the knife and let go of it."
        "Is she really that clueless?"
        $ style.say_dialogue = style.normal
        "What the hell is she talking about?"
        s "I believe in you."
    else:
        if monika_type == 0:
            s 1h "She told me about this danger."
            s "We both know it, don't we?"
            mc "Danger?"
            s "Be honest, [player]."
            s 1j "How much has she told you about it?"
            mc "Well..."
            mc "I guess you know about it, don't you?"
            s "Answer the question."
            mc "Listen, Sayori."
            mc "She hasn't told me anything about it."
            mc "All that she said is that it's coming."
            mc "When? I don't know."
            s 1k "It's coming a lot sooner than you think, [player]."
            mc "What is it just going to coincidentally show up tomorrow?"
            mc "On the biggest day for the club?"
            s "..."
            mc "What?!"
            mc "You can't be serious, right?"
            mc "How do you even know?"
            mc "She told me she didn't even know when it was coming."
            mc "How could you know?"
            s "It's...I just..."
            s 1h "You shouldn't ask questions like that."
            s "If I answer questions like that, everything is at risk."
            s "Especially if you hear it."
            mc "Okay, Sayori."
            mc "I still don't get it but I trust you."
            mc "So what are you going to do?"
            s "I don't know..."
            s 1f "I can't see what's going to happen."
            s "At least, not yet."
            mc "So you don't have a plan?"
        else:
            s 1k "You and I both know it."
            s "Don't we?"
            s "About Moeka."
            mc "I'm not sure I know what you mean."
            s 1j "Oh come on, [player]."
            s "You can't seriously be blind to it."
            s "You promised to be honest with me, didn't you?"
            mc "I mean..."
            mc "I suppose she's been acting a little out of the ordinary."
            s 1i "A little?"
            mc "But is that really that hard to believe?"
            mc "There's been so much going on in the club."
            mc "So many things I thought never would happen to me."
            s "That has nothing to do with it."
            mc "Are you sure, Sayori?"
            mc "I think Yuri almost killing everyone would change someone."
            show sayori 1j at h11
            s "Listen, [player]!"
            "Sayori yells that."
            "If somebody was listening like she thinks, then they definitely would have heard that."
            s 1k "I know Moeka, okay?"
            s "I've been friends with her the longest out of anybody in this club."
            s "She definitely has not been acting like how she should."
            s "She's been more aggressive."
            s "She's...not herself."
            s 1h "Is she?"
            mc "..."
            "Sayori makes a point."
            "But something inside me really wants to not believe her."
            "I guess it's the part of me that's always seen the good in Monika."
            mc "Okay...say you're right."
            mc "Are you just going to tell her that?"
            s 1k "I don't know."
            s "I just want her to be back to normal."
            s "Back to the president of the club."
            mc "I think you mean vice president."
            s "Y-Yeah, that."
            mc "Then...what's your plan?"
            mc "You do have one, right?"
            s 1h "No."
            mc "Then what are we going to do?"
            s 1f "You're not going to do anything, [player]."
            s "It's too risky, especially now."
        s "I'm going to come up with a plan."
        s 1b "I just need to see how tomorrow plays out first."
        s "But I can't do that until you've made up your mind for everything."
        mc "My mind up for everything?"
        mc "I don't know what you mean..."
    s 1c "[player], I know this is hard for you to understand."
    s "You're probably thinking this all sounds crazy."
    mc "What you're saying does sound a little far fetched..."
    mc "And I can't say I understand most of it."
    s 1d "All I'm asking is that you hang in there a little longer, [player]."
    s "Just another day, and this will all be over."
    s "We can all be happy."
    s "I just hope I can think of something..."
    "I don't think I understand most of what Sayori just told me."
    if persistent.markov_agreed:
        $ style.say_dialogue = style.edited
        "But I don't need to."
        "I just have to avoid suspicion and make sure Monika succeeds."
        $ style.say_dialogue = style.normal
    elif monika_type == 0:
        "I understand the danger but..."
        "What does she mean that I need to make up my mind?"
    else:
        "Monika has been acting differently but..."
        "What does she mean that I need to make up my mind?"
    s 1k "Just one thing to do now."
    s "[player], I'm sorry."
    mc "What do you mean?"
    s "I'm just going to move them somewhere else."
    s "You'll remember tomorrow, I promise."
    mc "Wha-"
    "Sayori puts her hand on my shoulder and closes her eyes."
    mc "What are you doing?"
    s 2d "It's already done~"
    "I don't {i}feel{/i} any different."
    "What did she do...?"
    if ch13_name == "Sayori":
        s 2a "[player], can you help me clean up the room?"
        s "Just start putting all the desks to where they should be."
        mc "Oh...I guess I can do that."
        s "I'll clean the floor."
        s "The cupcakes Natsuki brought left a bunch of crumbs everywhere."
        "Sayori somehow finds a vacuum in the closet."
        "She plugs it into the wall socket."
        s 2d "I'm not blaming her or anything..."
        s "I just don't want to leave this room worse than before we got here."
        mc "That's pretty considerate of you."
        s 2c "You think so?"
        mc "I never would have thought you were the type to do this kinda thing."
        s 1h "What's that supposed to mean?"
        mc "I just meant that you used to be such a messy person!"
        mc "Your room was a mess and I'd always be there to help you clean it up."
        s 1l "That was when we were younger, wasn't it?"
        s 1k "I'm not like that anymore..."
        mc "Actually, it wasn't until recently."
        mc "It was until you came out of depression, right?"
        s 1h "Huh?"
        mc "That's right!"
        mc "After you came out of depression, you started cleaning up your room."
        mc "I remember that day."
        s 1e "You do?"
        mc "Yeah, you--"
        show sayori 1k
        "Sayori turns on the vacuum."
        "The sound is loud enough to drown out our conversation."
        "I try yelling what I was trying to say to Sayori but she seems to ignore it."
        "I guess she can't hear me."
        "I continue to put all the desks back to where they were."
        $ del _history_list[-7:]
        "..."
        show sayori 1a
        "Soon enough, we manage to clean the room."
        "It looks better than how it was before we got here."
        "Sayori turns off the vacuum."
        "What was I even thinking about before she turned on the vacuum?"
        "It was pretty important...right?"
        "Well, if I forgot it then it must not have been."
        s 2d "Anyway, shall we go?"
        s "We're not going to be going to the mall."
        s "We don't really need anything since we've already got what we need."
        mc "That's fine."
        mc "I'm happy to just do the preparations with you."
        s 2g "I really wish they told me they were going to do some last minute preparations."
        s "Why couldn't I see this coming?"
        mc "No one could have seen this coming, Sayori."
        mc "It's not your fault."
        s 2k "...Yeah."
        mc "So what am I going to do tonight?"
        s 2d "We'll figure that out on the way home."
    elif ch13_name == "Yuri" and yuri_date:
        s 2a "Anyway, I won't keep you here any longer."
        s "Yuri is still waiting for you outside."
        s "I really hope you two are happy together."
        mc "Thanks, Sayori."
        s 2d "You make her really happy, you know."
        s "I hope you two have a beautiful night."
        "We're only going to be doing preparations."
        "It felt like that just came out of nowhere."
        mc "Thanks...?"
        s 4q "Ehehe~"
        s "See you soon, [player]."
    elif ch13_name == "Monika":
        s 2d "Monika's waiting for you outside, [player]."
        s "Good luck tonight."
        s "I hope you both get your preparations done."
        mc "The same to you, Sayori."
        s 4q "Ehehe~"
        s "Get going, [player]."
        s "I'm sure the two of you have a lot to talk about."
    else:
        s 2c "Anyway, you should probably get going."
        s "You have a lot of stuff to do tonight with [ch13_name]."
        mc "Yeah, you're right."
        mc "I'll see you tomorrow, Sayori."
        if natsuki_date:
            s 2d "I hope the two of you are happy."
            s "When Natsuki is around you, she's so much more..."
            s "...alive."
            s "Have you noticed that?"
            mc "Uhh..."
            s 4q "Ehehe, never mind."
        else:
            s 2d "I hope you have fun."
            s "Even if it's only preparations."
            mc "I'm sure we'll find some way to make it fun."
            mc "I still don't really know what we're doing at the mall though..."
            s 2q "Something exciting, I hope."
            mc "I doubt it..."
            s 4q "Ehehe~"
        s "I'll see you soon, [player]..."
    $ ay_name = "???"
    $ insert_ayame_character()
    call expression "ch15_exclusive_" + ch13_scene
    return

label ch15_exclusive_yuri:
    if yuri_date:
        scene bg corridor with wipeleft_scene
        "Sayori is still in the clubroom."
        "I think she's just cleaning up."
        "Meanwhile Yuri is sitting on the floor, writing down notes."
        mc "Are you ready to go?"
        "Yuri puts her notebook in her bag and gets up."
        show yuri 1a zorder 2 at t11
        y "That was quick."
        y 1g "I won't ask what the two of you were talking about."
        y "I don't want to overstep your boundaries."
        mc "That's really considerate of you."
        mc "Thanks, Yuri."
        y 1q "A-Anyway, shall we go?"
        "Yuri rolls up her sleeve."
        mc "Where are we going?"
        y 2a "Just follow me, you'll see."
        mc "Alright..."
        "Yuri takes my hand."
        y 2b "Let's go."
        scene bg library
        show yuri 2e zorder 2 at t11
        with wipeleft_scene
        "Yuri practically drags me around the school."
        "Not that I mind, it's just..."
        "I had no idea where we were going."
        "We arrived in the library but I'm still not sure what we're doing here."
        "Or if we're just passing by."
        "In fact, I didn't even know it was open at this time."
        "Wouldn't the staff already be going home or away at this time?"
        mc "Yuri, where are we going?"
        mc "We've been through the half the school at this point."
        y 2f "She keeps moving around."
        mc "Who's she?"
        y 2a "I met someone when I found out about Inauguration Day."
        y "She isn't really part of any clubs..."
        y "So she said she might be interested in joining our club."
        mc "What? Really?"
        mc "That's great!"
        mc "What are you meeting up with her for?"
        y 2i "I was going to give her a list of some of the things we've done in the club."
        y "To try to get her interested."
        y 2h "That's what I was writing down in my notebook earlier."
        mc "Did she ask for that?"
        y 3f "Yes..."
        mc "That's weird."
        y "I agree."
        y 3b "But if it means promoting the club, I'll do it."
        y "She might even bring her friends along tomorrow too."
        y 3c "So who knows just how many people will actually join the club?"
        y "Not to mention the people that will just happen to be there."
        y 3b "The thought of new members is exciting."
        mc "It definitely is."
        mc "Is that the reason you're hiding your bandaged arm?"
        y 3q "P-Partially."
        y "I'd rather not let her see me as some sort of freak."
        mc "There's no way she'd think that because of a bandage."
        y "Maybe not, better not to risk it."
        y 3s "Besides, I only really show it to you guys in the club."
        mc "It's like a privilege, is it?"
        y 3p "N-No...!"
        y "I-It's just she doesn't know the journey I went through to--"
        mc "I'm only kidding."
        mc "I understand completely."
        y 3q "Oh..."
        mc "So who is this person?"
        y 3f "I think her name was Ayame."
        y "She's in her junior year."
        y "But she wants to make her senior year memorable."
        y 3i "So she's looking for a club to join."
        mc "I see..."
        mc "So where is she?"
        y 3f "She should be right--"
        show ayame 1h zorder 3 at f21
        ay "Hi!"
        ay "Yuri...right?"
        show ayame zorder 2 at t21
        "A tall girl taps Yuri on the back."
        "I guess this is her?"
        show yuri 2s zorder 3 at f22
        y "Ah!"
        y "Y-Yes, that's right."
        y "We've been looking everywhere for you, Ayame."
        "So this is her."
        "Ayame, huh?"
        $ ay_name = "Ayame"
        show ayame 1i zorder 3 at f21
        show yuri zorder 2 at t22
        ay "Sorry, did you say 'we'?"
        ay "Who's the other..."
        "The tall girl turn towards me."
        show ayame 1b at hf21
        ay "Oh, I'm so sorry!"
        ay "I didn't notice you there."
        ay 1g "Please accept my apologies!"
        "Ayame bows her head."
        show ayame zorder 2 at t21
        mc "Uh...okay."
        mc "Apology accepted."
        "She seems really...eccentric."
        "It's a wonder why she'd be so interested in something like literature."
        "Not that that's a bad thing."
        "The more, the merrier I suppose."
        show ayame 1b zorder 3 at f21
        ay "I'm Ayame, what's your name?"
        show ayame zorder 2 at t21
        mc "[player]."
        show ayame 1d zorder 3 at f21
        ay "Great to meet you!"
        "She turns her attention back to Yuri."
        ay 1h "Do you have it?"
        show ayame zorder 2 at t21
        show yuri 2a zorder 3 at f22
        y "Of course."
        "Yuri opens her bag and pulls out the notebook she had earlier."
        "She neatly tears the page from the book and gives it to Ayame."
        y 2b "It's got everything you need to know."
        y "If you have any questions, you should look for our president."
        show ayame 1e zorder 3 at f21
        show yuri zorder 2 at t22
        ay "Wonderful! Thank you so much."
        "Ayame starts looking at what Yuri's written down."
        "I can hear her mumbling under her breath."
        ay 1i "One question..."
        ay "Who exactly is your president?"
        ay "Probably a dumb question, I know!"
        ay "I should know already."
        show ayame zorder 2 at t21
        mc "It's Sayori."
        mc "You know, red hair, wears a bow..."
        mc "Might ask you for spare change sometimes..."
        show ayame 1d zorder 3 at f21
        ay "Aha!"
        ay "I know exactly who that is."
        ay 1b "Right."
        "She folds the piece of paper and puts it into her pocket."
        ay "I really need to be going now."
        ay "I have some {i}extreme{/i} shopping to do tonight!"
        show ayame zorder 2 at t21
        show yuri 3e zorder 3 at f22
        y "Shopping?"
        y "If you don't mind me asking, what are you buying?"
        y 3f "Y-You don't have to tell me, if you don't want to."
        show ayame 1h zorder 3 at f21
        show yuri zorder 2 at t22
        ay "Actually, I'm glad you stopped me because I almost forgot to tell you!"
        ay "I'll be buying some gifts for everyone in your club for tomorrow."
        ay "It's going to be a surprise."
        ay 1i "Though...by telling you, I suppose I ruined the surprise."
        ay 1e "Hehe, oops~"
        show ayame zorder 2 at t21
        show yuri 2o zorder 3 at f22
        y "W-What? You don't need to do that."
        y "We should be the ones gifting you..."
        show ayame 1h zorder 3 at f21
        show yuri zorder 2 at t22
        ay "Nonsense!"
        ay "I want to thank you all for accepting me as a member!"
        ay "So many members do you have?"
        ay 1j "I could look at the paper you gave me but I always say it's better to talk it out!"
        show ayame zorder 2 at t21
        mc "Right..."
        "I look towards Yuri."
        show yuri 2q
        "She gives me the kind of look that says \"I don't know what to do\" so I guess it's up to me."
        mc "There's only five of us, including Yuri and I."
        mc "Me, Sayori, Yuri, Natsuki and Monika."
        show ayame 1i zorder 3 at f21
        ay "Did you say Monika?"
        ay "I thought she was part of the debating club or something!"
        ay "I remember watching her debate last year..."
        show ayame zorder 2 at t21
        show yuri 3f zorder 3 at f22
        y "I don't think she's a part of it anymore."
        y "Something about not liking the politics..."
        y "That's why she left to form the literature club."
        show ayame 1d zorder 3 at f21
        show yuri zorder 2 at t22
        ay "Well, good for her!"
        show ayame zorder 2 at t21
        mc "You really don't need to get us anything."
        mc "Joining the club is more than enough."
        mc "Besides, you barely know us..."
        show ayame 1h zorder 3 at f21
        ay "The thing is, I want to!"
        ay 1e "It means new friends, new experiences and something to look forward to everyday!"
        "Ayame shows a wide smile."
        ay 1g "Now that I think about it, that's a pretty small club..."
        ay "Though I suppose it's more cozy that way!"
        ay "Five members..."
        ay 1h "I'll be more than happy to make it six!"
        ay "Hehe, it also means I can get you all more expensive gifts!"
        show ayame zorder 2 at t21
        "She seems pretty carefree."
        "I think Sayori and her would get along really well."
        mc "I think you and the president would become really good friends."
        mc "Her personality seems a lot like yours."
        show ayame 1d zorder 3 at f21
        ay "That's great!"
        ay "I can't wait to meet her."
        show ayame zorder 2 at t21
        mc "I thought you said you knew exactly who Sayori was."
        show ayame 1i zorder 3 at f21
        ay "I did?"
        ay "I must have thought of somebody else."
        ay 1j "Anyway, I really have to get going."
        ay "I'll see you both tomorrow hopefully!"
        show ayame at lhide
        hide ayame
        show yuri zorder 2 at t11
        "She starts skipping out of the library."
        mc "She seems...interesting."
        y 3a "She's quite lively, isn't she?"
        mc "That's one way to describe it."
        mc "It feels like she has her mind all over the place."
        y 2b "She's unique."
        mc "Definitely."
        mc "I wonder if she's actually serious about the literature club."
        y 2i "I would hope so."
        y "I spent quite a bit of time on those notes."
        mc "That's strange too."
        mc "Who just asks for notes on the literature club?"
        mc "It just seems so...weird."
        y 2j "There's nothing wrong with weird."
        y "As long as she has a passion for literature, I'm all for accepting her into the club."
        mc "Didn't you say she might bring her friends along too?"
        mc "Where were they just now?"
        y 3t "I don't know."
        y "Maybe they already left and she's trying to catch up with them."
        y "Or maybe she's just the messenger."
        y 3s "What I do know is that we should probably get going."
        mc "You're right, we still need to go to the mall."
        y "And finish your share of the preparations too."
        scene bg y_house with wipeleft_scene
        "We both went home and decided to meet at Yuri's house."
        "It's closer to the mall and we were going to go there together."
        "I brought along the stuff I didn't get to finish last night."
        "That way when we get back, we can finish them off."
    else:
        scene bg y_house with wipeleft_scene
        "I get to Yuri's house, bringing the preparations I didn't finish off with me."
        "We decided to meet up here because it's closer to the mall."
        "After we finish whatever we're doing at the mall that she'll help me finish the preparations off tomorrow."
    "She's already waiting at the door to her house."
    show yuri 1ba zorder 2 at t11
    y "Hello, [player]."
    y 1bb "Just drop off what you brought here and we can go to the mall."
    mc "Thanks again for helping me finish it off tonight."
    mc "I feel bad that I'm making you do more work when you've already done more than me."
    y 1bf "It's not a problem at all."
    y "We're a team, right?"
    y 1ba "Besides, it's better this way."
    mc "It is?"
    mc "In what way?"
    y 1bq "W-Well..."
    if yuri_date:
        y "I get to spend more time with you."
        y "That's always a good thing."
        mc "The feeling is mutual."
    else:
        y "It means the decorations will look more universal."
        y "So they aren't too different from each other."
        mc "That makes sense."
    y 1bs "Anyway, we should get going."
    y "I'll wait for you out here to drop off your things inside."
    y 1bh "Just leave them in the living room or near the door."
    mc "Okay..."
    mc "I'll go do that."
    "Yuri steps away from the door and invites me into her house."
    if ch7_name == "Yuri":
        "I haven't really had a proper look at her home before."
        "Sure, I've been here but..."
        "Well, that wasn't exactly the best experience."
    else:
        "I wonder what the inside of her home is like."
        "I don't really know what kind of stuff would be inside her house."
        "I guess it's time to find out."
    "I make my way inside."
    scene bg y_corridor with wipeleft_scene
    "I don't know what I expected from Yuri."
    "It's just a normal house."
    if ch7_name == "Yuri":
        "Was it like this last time?"
        "I don't really remember."
    else:
        "I guess because of how she was, I thought there would be something different about how she decorates her home."
        "Especially since she's the type of person who likes doing decorations."
    "I leave my bag near the entrance."
    "I'm kinda tempted to explore her house a bit..."
    "But that would be an invasion of privacy."
    "And besides, she's waiting for me outside."
    "I take one final look around before closing the door behind me."
    scene bg mall_day with wipeleft_scene
    "Yuri and I travel to the mall."
    "We took public transport there during rush hour so it took a bit longer than it would on the weekend."
    "Despite that, it's still a short trip since Yuri lives kinda close to the mall."
    "The ride gave us some time to talk about what we were going to be doing."
    "It doesn't seem like it's going to be a quick in and out."
    "There's a lot of different places we have to go to."
    if yuri_date:
        "And she also said she wanted to make a quick stop at the marina."
        "I'm thinking that's probably the place where we dropped that knife."
        "The knife that completely changed Yuri."
        "Well, all the good parts about her are still there."
    else:
        "And she said she wanted to be alone for a little bit."
        "Something about going to the marina."
        "..."
        "Didn't I see her there before?"
        "What was that about again?"
        "It probably doesn't matter."
    show yuri 1ba zorder 2 at t11
    y "Let's get moving."
    y "All of the stuff we have to get is scattered all over the place."
    mc "You'd think they'd have a single store that sells all that stuff."
    y 2be "It's really specific materials that are only available in certain stores."
    y "And most of them happen to be in completely different stores."
    mc "What kind of materials are they anyway?"
    y 2bg "I probably should have been more specific."
    y "The specific material, made by brands I trust are in different stores."
    y "I'm sure you could find a different brand of the same thing in another store."
    mc "So what makes these particular ones so important to have then?"
    y 2bh "I suppose there isn't any real reason for it."
    y "But if I had to give a reason it's because I trust those brands."
    y "They've been reliable in the past."
    y 2bf "I'd say it's worth the trouble getting them."
    y "Besides, we'll still have plenty of time to get everything together."
    y "You don't have a problem with that, do you?"
    mc "No, not really."
    mc "But some of those stores are on opposite ends of the mall."
    y 3ba "Don't like walking, [player]?"
    mc "The mall is huge, Yuri."
    y 3bb "It'll be some good exercise."
    if yuri_date:
        y "Besides, it'll be some good quality time together."
    else:
        y "It'll give us a chance to talk about how we're going to use the materials."
    mc "I guess so."
    show yuri 3bs
    "Yuri smiles."
    mc "So where exactly are we going first?"
    y 2ba "The store right next to the entrance."
    "Yuri points towards a store."
    "It covers two levels of the mall because it's such a big store."
    "It seems they sell all sorts of stuff from clothes, to home renovation stuff to fabrics."
    mc "It's a huge store."
    y 2bi "And we're only getting one thing from it."
    mc "Wow."
    mc "Did you plan out the most efficient path for this?"
    y 2bq "Not exactly."
    y "We're just going to be going to stores as we pass them."
    mc "That doesn't seem like the best way to do things."
    mc "You wanted to make the best use of time, right?"
    y 2bf "I did..."
    y "Are you trying to suggest something?"
    mc "We could split up and go to opposite ends of the mall."
    mc "That might make things quicker, right?"
    y 2bg "I suppose."
    if yuri_date:
        y 2bh "But it means we won't be spending time together."
        mc "The less time we waste now, the more time we can spend together after, right?"
        "Yuri thinks about it for a moment."
        y 3ba "You're right."
        y "Let's make this quick."
    else:
        mc "And we can always talk about the materials on the way home."
        y 2bq "I suppose..."
    mc "Send me a copy of that shopping list of yours."
    mc "I'll try to look for them."
    y 2bn "B-But I didn't put the stores they come from."
    y "You're going to be looking for them blind."
    mc "That's okay."
    mc "At least it makes things easier for you, right?"
    y 2bq "Y-You're too kind."
    mc "You're helping me with preparations I should have done, so the least I can do is help you now."
    "Yuri goes on her phone and pulls out a piece of paper from her pocket."
    "She takes a picture and a few moments later I get a message from her."
    "I can only assume that's the list."
    mc "Where do you want to meet up once we're finished."
    y 2bb "The food court could be nice."
    y "It's in a rather central location."
    mc "Sounds like a plan."
    y 3ba "Then it's settled, I'll see you at the food court later."
    y "Thanks again, [player]."
    mc "I'll see you then, Yuri."
    call ch15_mall_shared
    "We decide to go to my house to finish the preparations."
    "Most of the stuff we need to do is my side of the preparations anyway."
    "I feel bad making Yuri help me for this stuff but she doesn't seem to mind."
    "I'm glad I chose her to work with."
    return

label ch15_exclusive_natsuki:
    scene bg n_house_day with wipeleft_scene
    "I arrive at Natsuki's house."
    call screen dialog(message="To be continued!\nThanks for playing, keep an eye out on reddit and discord for updates!", ok_action=Quit(confirm=False))
    return

label ch15_exclusive_monika:
    scene bg corridor with wipeleft_scene
    "I leave Sayori in the clubroom by herself."
    "I think she's just packing up her things then she'll leave."
    "I wonder if Monika heard the conversation we had in there."
    "I'd be surprised if she didn't."
    "What {i}was{/i} the conversation we had in there?"
    "Something about preparations?"
    show monika 2a zorder 2 at t11
    m "Hi, [player]~"
    m "How was your conversation with Sayori?"
    if monika_type == 0:
        m 2c "I can only assume you were talking about..."
        m "You know."
        m "The danger."
        mc "What danger?"
        m "You were talking to Sayori about it, weren't you?"
        m 2m "The danger I told you about?"
        mc "Um..."
        "What is Monika talking about?"
        "What's this danger?"
        mc "I'll be honest, Monika."
        mc "I can't remember what we talked about."
        mc "It probably wasn't important."
        m 2o "..."
        mc "And what do you mean by this danger?"
        m 2p "{i}(So, that's how it is...?){/i}"
        m "{i}(I hope you know what you're doing, Sayori.){/i}"
        mc "What did you say?"
        m 1l "Ahaha, never mind~"
        m "Just forget I said anything."
        m "It's none of my business anyway."
        mc "If you say so."
    elif monika_type == 1 and ch12_markov_agree:
        m 1c "You have to tell me everything."
        m "What was it about?"
        mc "Huh?"
        mc "It was a private conversation."
        mc "And besides..."
        m 1h "...Are you serious?"
        m "She can't hear us right now."
        m 1e "You can tell me."
        mc "I really don't remember."
        m 1h "You don't...remember?"
        m 1i "You just came out of the room, [player]!"
        m "How can you not remember?"
        m "Unless..."
        m "That's it, isn't it?"
        m 1a "Clever girl."
        m "No matter."
        mc "Is something wrong?"
        m "No, nothing is wrong."
        m 3b "Let's just forget I said anything, okay?"
        mc "Alright..."
    else:
        m 1c "What did you talk about in there?"
        mc "Huh?"
        m "I asked you a question, [player]."
        m "And I need to know the answer."
        mc "I..."
        mc "I can't remember."
        m 1d "You can't remember?"
        m "I see."
        m 1e "Well, it doesn't matter right now."
        m "I'll figure it out later."
        mc "Figure what out?"
        m 1h "Nothing, just forget I said anything."
        mc "Okay."
    m "Shall we go?"
    mc "I'd like to know what we're doing at the mall exactly."
    mc "I get that it's for preparations but..."
    mc "What kind of stuff would you need to buy?"
    m 1c "I'm not necessarily going there entirely for preparations."
    m "Or should I say {i}our{/i} preparations."
    m "There's some things I still need to do to set up for tomorrow."
    m 2d "And I need to buy some of those things."
    mc "Right..."
    mc "Didn't Sayori say she'd take care of that kind of thing?"
    mc "I don't know about her financial state or anything but..."
    if monika_type == 0:
        m 2f "Didn't you say you didn't want to use her like that?"
        mc "Well, yeah but..."
        m "Besides, I'd rather not trouble Sayori with what I'm doing."
        m "She's got enough to worry about."
    else:
        m 2e "Isn't she meant to be your best friend?"
        mc "She is but..."
        m "And anyway, it doesn't directly help with our play for tomorrow."
        m "So I'd feel bad taking money from her like that."
    mc "I guess you're right."
    m 1a "Now, if we're done here..."
    m "We should really get going."
    mc "What's the plan then?"
    m "We can stop by your house first so you can get changed and drop off some of your things."
    m 1c "Then we can pass by my house since it's on the way anyway."
    mc "Wouldn't it just be easier to meet there?"
    m "I suppose it would be."
    if monika_type == 0 or (ch12_markov_agree and monika_type == 1):
        m 1e "If that's what you want, then we can do that."
        m "It would save some time."
        mc "You're letting me choose?"
        m 1m "Why wouldn't I?"
        m "I don't control you, [player]."
        m "You're free to do what you want."
        m 1n "If you want to stick together, we can do that."
        m "Or if you want to split up for now, we can do that too."
        mc "You don't sound too happy about that."
        m 1l "Don't I?"
        m "It's..."
        m 1e "Well, it's not my choice to make."
        m "I'll respect your decision."
        mc "Monika..."
        show monika 1j
        "Monika shows me a smile."
        menu:
            m "So what will it be?"
            "Let's stick together.":
                mc "I'm sure we can still do what we need to at the mall."
                mc "Even if we aren't using our time perfectly."
                m 1d "So we're sticking together?"
                mc "Is that a problem?"
                show monika 1m
                "Monika looks down at the ground."
                m "No..."
                "She looks back at me."
                m 1k "Not at all!"
                "She smiles at me again."
                "But for some reason, this time it feels...genuine."
                "More genuine than usual."
                m 1e "Then...!"
                m "Shall we get going?"
                m "Since we're doing everything together, we should make sure we don't waste any more time than we need to."
                mc "To my house then."
                m "Ahaha, lead the way."
                call ch15_exclusive_monika_together
            "Let's meet at the mall.":
                mc "I think it's better if we split up for now."
                mc "That way, we can do what we need to at our homes without waiting for each other."
                mc "I don't know how long we need to be at the mall for so I think it's best if we just make sure we have as much time as possible."
                m 1e "Ah...I see."
                m "If that's your choice."
                mc "I'm doing it for you."
                mc "I don't want you to run out of time because of me."
                mc "I can tell you're a pretty busy person."
                m 1m "T-That's fine."
                m "I suppose I'll see you at the mall, [player]."
                mc "Are you okay?"
                m 1e "Am I okay?"
                m "What kind of question is that?"
                mc "I'm just asking."
                mc "You sound upset, that's all."
                m 1o "Of course I'm okay."
                m "Why wouldn't I be?"
                "Monika begins to walk away."
                mc "Monika...!"
                show monika at lhide
                hide monika
                "I think she increased her pace."
                "Was it something I said?"
                "Maybe she just want to use her time effectively."
                "That's why she's rushing...right?"
                "I guess I should get home too."
                "I just said I don't want to waste her time and here I am wasting time..."
                call ch15_exclusive_monika_alone
    else:
        m 1c "I guess we should split up then."
        m "You can go by yourself to your house and I'll just meet you at the mall."
        m 1a "Is that okay with you?"
        mc "W-Wait, you're leaving just like that?"
        m 2b "You're the one who suggested the idea, [player]."
        m "Besides, you're right."
        m "It would be easier to just meet there."
        mc "Then why did you wait for me in the first place?"
        m 2h "That's..."
        m 2m "There's no reason."
        m "I shouldn't have waited."
        mc "Wait, what?"
        m 2b "I'll see you at the mall, [player]."
        "Monika begins walking away."
        mc "Monika!"
        show monika at lhide
        hide monika
        "She's already gone."
        "She left so suddenly, I'm kind of shocked."
        "I would have thought she would have at least given me a chance to take back my suggestion."
        "I guess she just wants to be efficient."
        "I guess I shouldn't just stand here."
        "After all, I really shouldn't keep her waiting at the mall."
        call ch15_exclusive_monika_alone
    mc "Where exactly in the mall are we going?"
    mc "I don't know what kind of things you'll need for tomorrow."
    mc "But if you need me to get anything, then let me know."
    m 2bc "There's quite a lot on my list of things I need to get."
    m "It might be better for us to split up to look for them."
    mc "Well, okay if that's what you want."
    mc "Do you know what stores have these items you're looking for?"
    m 2bm "Ah...I'm not entirely sure, [player]."
    m 2bl "I'm sorry."
    mc "That's okay, I can look for them."
    mc "So what's this list of stuff you need me to get?"
    m 2ba "It's right here."
    "Monika hands me a small piece of paper."
    "It's got things I've never heard of on it."
    "What the hell is a 'doohickey'?"
    mc "What are these things...?"
    m 4bb "They're just things I need for tomorrow."
    mc "But what for?"
    m 4bc "Is that really important?"
    m "If you don't want to help, I'm not going to force you to."
    mc "No, you're right."
    mc "I won't complain."
    mc "Where should I start?"
    m 4bl "I've absolutely no clue."
    "Monika starts walking away."
    mc "Where are you going?"
    m 2be "To the restrooms, [player]."
    if ch15_m_together:
        m 2bh "I don't--"
        "Monika stops."
        m 2bo "This is wrong."
        m "Okay, [player]."
        m 1bp "I'll be honest with you."
        mc "Huh?"
        m "Half of the things on that list..."
        m "They don't exist, okay?"
        m 1bn "The other half are just ridiculously impossible items."
        mc "Then why?"
        m 1be "I want to do this alone."
        m 1bf "I have to."
        m "You don't deserve to know the preparations I'm trying to do for tomorrow."
        m "And I'm saying that to protect you."
        "To protect me...?"
        "From what...?"
        mc "You could have just said so."
        m 1bo "I didn't know how you'd react."
        mc "I probably would have been more offended if you hadn't told me."
        mc "I'm just glad you told me, Monika."
        m 1bm "I-It's nothing."
        m "I know you feel like you aren't being useful."
        m "But going here with you is all I needed."
        mc "So what should I do then?"
        m 2be "Whatever you want."
        m "We can meet at the food court when I'm finished."
        m "I'm sorry for lying to you."
        show monika at lhide
        hide monika
        "I wasn't expecting that."
        "I'm glad she told me the truth."
        "I would have been wondering aimlessly looking around for things that didn't exist."
        "I wonder why she wants to do this alone."
        "It must be an important reason."
        "I guess I'll spend my time browsing anime and manga stores."
    else:
        m 2bh "I don't imagine you'd need to go as well."
        mc "N-No, but--"
        m 2bi "I'm going to go shopping for the items right after."
        m "That way I can make the best use of my time."
        m 2be "I'll see you later."
        m "Good luck!"
        show monika at lhide
        hide monika
        "What am I going to do with this list?"
        "I have no idea what half of the things on this list are."
        "And the ones I do just sound completely ridiculous."
        "Why in the world would Monika need a neon, dark, green, red dog plush."
        "What kind of place would sell that?"
        "I guess I better start looking..."
        "As I'm about to head into the first store to look, I get a message from Monika."
        "It says to meet her in the food court when I'm done."
        "I guess I should start looking for these things on the list."
    call ch15_mall_shared
    "It's getting really late."
    return

label ch15_exclusive_monika_together:
    $ ch15_m_together = True
    scene bg residential_day
    show monika 1a zorder 2 at t11
    with wipeleft_scene
    play music t6
    "We make our way to my house."
    "The walk is pretty quiet, neither of us try to really make small talk."
    "There's no one else here as well, it's just the two of us."
    "I could even hear the wind rustling the leaves."
    "I try to talk to her before but she seemed to dodge my questions."
    "I guess she's just not in the mood to talk right now."
    "Is this what she wanted?"
    "Does she even want to spend this time with me?"
    "Her smile before made me think she was really happy about it."
    "Like she really, genuinely enjoys spending time with me."
    "..."
    "She doesn't like me like {i}that{/i}, does she?"
    "There's no way."
    if sayori_confess:
        "Besides, I'm with Sayori."
        "But what if she did...do I feel the same way?"
    else:
        "But if did..."
        "Would I feel the same?"
    "What am I thinking?"
    "A girl like Monika would never be interested in someone like me."
    "There's just no way."
    "We're just friends...right?"
    "I really shouldn't think about things like that."
    "It would make things awkward, especially with the stuff we need to do tonight."
    "We continue to walk, just staying in silence."
    "I'm almost tempted to ask her how she feels but..."
    "It's not the time or place."
    "We take the turn into my street."
    "A single word still hasn't been said since I suggested we stay together."
    scene bg house with wipeleft_scene
    "We arrive at my house and I notice Monika let out a smile."
    "She's been smiling the whole trip home, but this one is wider than before"
    show monika 2b zorder 2 at t11
    m "I'll just wait for you outside, [player]."
    m "You can take however long you need to."
    mc "O-Oh, okay."
    mc "I won't be long."
    m 2e "And I'm sorry."
    mc "Sorry for what?"
    m "Being so close to you has just given me some time to think."
    m 2m "Think properly, I mean."
    mc "About...?"
    m 2e "About what's important to me."
    m "About how I'm going to achieve my goals."
    if monika_type == 0:
        m "And about what I'm going to do in the future."
    else:
        m "And about what I'm going to do when it's all mine."
    mc "That happened because you were close to me?"
    mc "Am I some kind of bad influence or something?"
    m 1l "No, it's not that."
    m 1e "Just seeing you care so much."
    m "It just warms my heart."
    m 1m "I've never really felt like this, that is until..."
    m 1n "Until I met you."
    m 1j "But anyway...!"
    m "You should go do what you need to."
    m "We still have to pass by my house too, you know."
    mc "Right."
    mc "I'm just surprised, that's all."
    m "You're not the only one~"
    "What did she mean by that?"
    scene bg bedroom with wipeleft_scene
    "I can see Monika waiting outside from my window."
    "She seems to just be there waiting patiently."
    "I guess I shouldn't keep her waiting."
    "I quickly change my clothes and gather what I need for the trip."
    "I wonder what we're going to be doing at the mall."
    "We're going to be buying things but...what?"
    "What kind of things would Monika need to buy for tomorrow?"
    "She already has a grand piano from Sayori."
    "And it's not like she doesn't have other equipment for playing the piano already."
    "That doesn't really leave many other options..."
    "I don't know."
    "I guess I could ask her for more details."
    "But right now I have to hurry to her."
    scene bg house with wipeleft_scene
    "I hurry downstairs and look for her."
    "I saw her from the window but she seems to have moved."
    mc "Monika?"
    mc "Are you here?"
    show monika 1a zorder 2 at t11
    m "I'm right over here, [player]."
    "Monika steps out from inside my house."
    m 1e "Sorry, you left your door open."
    m "I was just a little curious."
    mc "That's fine."
    mc "You know you're welcome anytime, Monika."
    m 1b "Thanks, [player]~"
    m "I'll keep that in mind."
    mc "Shall we start the journey to your house then?"
    m 1c "Yeah, if you're done all here?"
    mc "I'm ready."
    m 1a "Then let's go."
    scene bg m_house with wipeleft_scene
    "Once again, the walk is quiet again."
    "I don't know if she knows just how awkward this is for me."
    "I feel like I should be doing more to interact with her."
    "Especially after what she said when we got to my house."
    "But when I try to ask her something, she just gives me a short answer."
    "Or doesn't answer me at all."
    show monika 1c zorder 2 at t11
    m "Do you want to wait out here?"
    m "You're free to wait inside if you want."
    mc "I think I'll stay out here."
    m 1a "Suit yourself."
    m "I won't be too long."
    show monika at thide
    hide monika
    "Monika heads into her house."
    "I sigh and sit down on the seat out on her front yard."
    "I really don't know Monika's feelings towards me."
    "Should I even be thinking about this kinda thing?"
    if sayori_confess and not sayori_dumped:
        "Especially since Sayori is my girlfriend."
    elif yuri_date:
        "Especially since I'm already with Yuri."
    "It just feels like...she's not thinking about me."
    "I mean she says things to me but I don't think they're directed {i}to{/i} me."
    "That doesn't make any sense."
    "There's no one else she could be talking to."
    "Do you know?"
    "..."
    "Whatever, I should really get my mind off of this."
    "I think I'm going crazy."
    "I try to get a hold of Sayori on my phone."
    "It just goes to her sing-song voicemail."
    "She's probably busy doing her preparations."
    show monika 1ba zorder 2 at t11
    m "Okay, I'm all set here."
    mc "Monika, do you know where Sayori is?"
    m 2bc "Sayori?"
    m "She's probably doing her preparations, why?"
    mc "She's not answering my calls."
    m 2bd "I'm sure she can take care of herself, [player]."
    m "She's more than capable of it."
    mc "I guess so."
    mc "There's probably nothing to worry about."
    m 2ba "That's right."
    m "Now, are you ready to go to the mall?"
    mc "Ready as ever."
    m "Okay, then follow me."
    m 4bb "I know a way to get there quick from here."
    scene bg mall_day
    show monika 2bm zorder 2 at t11
    with wipeleft_scene
    "Monika's way to get there was to start running towards the nearest bus stop."
    "We almost missed the bus because I lagged behind."
    "I think she realized before I did because she actually ran faster."
    "Luckily she got to the bus stop as the bus arrived and stalled the bus driver long enough to let me get on."
    "The way to the mall was actually really nice."
    "There was only a little bit of traffic, which is odd because it's around this time that the city is filled with cars."
    "But once again, Monika stayed quiet for most of it."
    "She was staring out the window for the whole ride."
    "I could see her reflection on the window and she had this weird smile on her face."
    "Like she was really enjoying herself somehow."
    "She must be thinking about something else though because it really doesn't seem like she's enjoying {i}my{/i} company."
    mc "That was a really smooth ride."
    m 2bn "Yeah..."
    mc "There were barely any cars on the road."
    m "That's good for us."
    "She still seems to be giving me short responses."
    "What's going on...?"
    mc "Listen, Monika."
    m 2bc "What is it?"
    mc "Did I do something wrong?"
    mc "Did I say something that's making you act like this?"
    m 2be "Like what...?"
    mc "You've been quiet ever since I suggest we stayed together."
    mc "Except for that whole confession style thing you told me."
    mc "It's making things a bit awkward."
    m 2bn "Oh..."
    m "I didn't realize."
    mc "If it's something I said..."
    mc "Or something I didn't do..."
    m "I-It's not that."
    m 1bo "Like I said, I've just been thinking a lot."
    mc "It's got to be more than that."
    mc "I'm just really worried I did something wrong."
    m 1be "You've done nothing wrong."
    m "Believe me when I say that."
    m "So please, don't worry about it."
    m "I don't want to trouble you with it, especially now."
    mc "If you say so, Monika."
    mc "But you know I'm here if you want to talk."
    m 2be "Thank you."
    return

label ch15_exclusive_monika_alone:
    $ ch15_m_together = False
    scene bg house with wipeleft_scene
    play music t6
    "I make it home pretty quickly."
    "With the way Monika was moving, I kinda felt inspired to do the same."
    "There's not really much to do tonight."
    "For me, anyway."
    "All of our preparations depends on Monika."
    "I'm just kinda...there."
    "I really hope I can be more useful."
    "Maybe she can give me something to do at the mall."
    "Carrying the stuff she was planning to buy, maybe?"
    "I just really want to be useful to her."
    "All I've done so far is pick a song for her."
    "And even then, she's the one that's learning it."
    scene bg bedroom with wipeleft_scene
    "Maybe I can get Monika something."
    "To show my appreciation for all the hard work she's doing."
    "Would that even make sense?"
    "How would she react?"
    "Maybe I can just do something to help her perform better tomorrow."
    if ch12_markov_agree:
        "Reading the book could do it."
        "She wanted me to do that, right?"
        "I wonder how that could even help her."
        "I don't need to wonder."
        "Just do it."
    else:
        "I could surprise her somehow."
        "Sayori already got her a grand piano to play on..."
        "I'm not sure how I could top that."
        "But I might be able to think of something before the end of the day."
    "I lay down on my bed."
    "There's so much going on tomorrow."
    "Everyone is working so hard."
    "Everyone except me."
    "I sigh."
    "The inspiration to move quickly is slowly disappearing."
    "She's still relying on me."
    "So at any rate..."
    "There's no time to waste."
    "I still have to meet her at the mall, after all."
    scene bg mall_day with wipeleft_scene
    "I take public transport to the mall."
    "I think I arrived a lot later than Monika did because she was already sending me text messages asking me where I was."
    "I thought I would have been early, since there was barely any traffic on the way here."
    "It felt like the bus only stopped for the bus stops and not for the traffic lights."
    show monika 1bc zorder 2 at t11
    m "There you are."
    "Monika appears in front of me."
    m 2bd "What took so long?"
    mc "I'm not sure."
    mc "I thought I would have gotten here pretty early."
    mc "Since there was barely any traffic."
    m 2be "Strange...the same happened for me."
    m "Maybe there's something going on outside the city."
    mc "Yeah, maybe."
    return

label ch15_exclusive_sayori:
    $ persistent.ch15_sayori_chance = False
    $ renpy.save_persistent()
    scene bg residential_day
    show sayori 1a zorder 2 at t11
    with wipeleft_scene
    play music t6
    "Sayori and I make our way home."
    "She's been really quiet this whole time."
    "That's not like her at all."
    "She's also been walking behind me, instead of beside me."
    "And every time I turn my head to look at her, she's just looking at the ground."
    "Maybe I should say something."
    mc "So..."
    mc "What am I going to be doing tonight?"
    s 1b "Huh?"
    mc "I was just asking how I could help with the preparations tonight."
    mc "I feel like there isn't really much for me to do."
    s 1c "Oh...right."
    s 1d "We'll come up with something when we get to my house."
    s "Just save that talk for later.{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    s "Just save that talk for later.{fast}"
    window auto
    s 1o "E-Eh? I didn't even mean it like that...!"
    mc "What do you mean?"
    s 1l "N-Nothing."
    mc "Anyway..."
    mc "You said that we'd come up with something on the way back."
    s 5a "I did?"
    mc "Sayori, is everything alright?"
    mc "Like really alright?"
    s 5b "{i}(So it worked...you don't remember.){/i}"
    mc "You know I'm here for you."
    mc "I've probably said that before."
    mc "And I'll keep saying it."
    s 4r "I'm fine, see?"
    "Sayori shows me a wide smile."
    s 4d "I just have a lot on my mind."
    s "With all these preparations."
    mc "If you've got that much on your mind..."
    mc "Then you can give me something to do, right?"
    mc "I don't want you to do this alone."
    mc "And I really do mean that."
    mc "So you've got to help me so that I can help you."
    s 3c "Well, we're still doing the script, right?"
    s "You can just say it aloud again and I can write it down."
    mc "Does that actually work?"
    s 3l "It worked yesterday, didn't it?"
    mc "I mean..."
    mc "Do you actually need my help with that?"
    s 3g "Of course I do!"
    s "Why are you asking?"
    mc "I guess I just felt I wasn't really doing anything."
    s 3h "That's not true at all!"
    s "You reading out aloud really sped things up."
    s "If I had to do it myself, it would take {i}waaaaaaay{/i} longer."
    mc "If you say so..."
    mc "But what about after we finish?"
    s 1e "Do you really think we'll finish the book and still have time to do other stuff?"
    mc "In the case that we do."
    s 1c "Hmm...I don't know."
    s "Maybe you can help me with some planning for tomorrow."
    mc "I can do that."
    mc "I've helped you with your homework enough times after all."
    s 1l "Ehehe, you don't have to say it like that..."
    mc "It's true!"
    s 1k "Yeah..."
    "After that conversation, Sayori is quiet again."
    "The walk home is peaceful but it just doesn't feel right."
    "Sayori is usually the one to make the conversations, even if they're meaningless."
    "I guess I can deal with it for now though it is a bit unsettling."
    scene bg house
    show sayori 1d zorder 2 at t11
    with wipeleft_scene
    "Just before we arrive at my house, Sayori taps my shoulder."
    if persistent.ch15_sayori_chance:
        "But for some reason, this sensation feels all too familiar."
        "I get the feeling she's about to change her mind."
        "That she wants to meet at her house instead."
    s "[player], I'm actually gonna go ahead."
    s "We'll just meet up at my house, okay?"
    if persistent.ch15_sayori_chance:
        "What the hell?"
        "That feeling was right?"
        "I should play this naturally, as if I don't know any better."
    mc "Did something come up?"
    s 1b "You could say that."
    s "It's just...I remembered something I need to do quickly."
    mc "Well, if you say so."
    s 1a "I should be home by the time you get there."
    if persistent.ch15_sayori_chance:
        "This is wrong."
        "I have a bad feeling about this whole thing."
        "I should go with her."
        "I need to stay with her or things will go wrong."
        "What am I thinking?"
        "Sayori is more than capable of handling herself."
        "But..."
        menu:
            "I'm still worried."
            "Insist on going with her.":
                if persistent.markov_agreed:
                    $ style.say_dialogue = style.edited
                    "I should leave her alone."
                    "Things will be better that way."
                    $ style.say_dialogue = style.normal
                    "What am I saying?"
                    "I want to help her so..."
                    # Markov will give you another chance :)
                    menu:
                        "I need to go with her...don't I?"
                        "Go with Sayori.":
                            $ style.say_dialogue = style.edited
                            "I..."
                            "Have to..."
                            $ style.say_dialogue = style.normal
                            "Go with her."
                            jump ch15_sayori_check
                        "Leave her be.":
                            pass
                else:
                    "This bad feeling won't stop bugging me."
                    "It's like I won't forgive myself if I don't go with her."
                    "So I'm going to go with her."
                    jump ch15_sayori_check
            "Leave her be.":
                pass
    label ch15_sayori_check_fail:
    if persistent.ch15_sayori_chance:
        "I think I'm going crazy."
        "She'll be fine, I know it."
        "She can definitely take care of herself."
        "But even so, I want to help her in another way."
    # You had your chance you fool
    $ persistent.ch15_sayori_chance = False
    $ renpy.save_persistent()
    mc "Alright, I'll see you then, Sayori."
    s 2q "Bye~"
    show sayori at lhide
    hide sayori
    "Sayori smiles and waves at me before walking away."
    "She doesn't seem to be going in the direction of her house."
    "I guess she has to do something somewhere else?"
    "Maybe one of the others asked her for a favor."
    "It's none of my business though."
    "Even so..."
    "I should really find out what's going on with Sayori."
    "She may not say it, but I just {i}know{/i} she's dealing with something more than she can handle."
    "And I can't let her go through that again."
    "The first time she almost took her own life."
    "How could I have been so stupid back then?"
    "It makes me angry just thinking about it."
    "Thinking about how there's more I could have done."
    "I have to remember how she was feeling back then."
    "How I could have prevented it in the first place."
    "I feel like I'm seeing the same signs now."
    "But I just feel so...useless."
    "There must be something I can do for her."
    "Something I can do to ease the pain."
    "Something I can do to convince her to let me help."
    "But what?"
    scene bg bedroom with wipeleft_scene
    "I lay down on my bed."
    "I just can't think of anything to get Sayori out of the state she's in."
    "She clearly needs help."
    "Maybe a therapist or something."
    "Who am I kidding?"
    "I don't know any therapists."
    "Or have that kind of money."
    "But still, I have to do something."
    if persistent.markov_agreed:
        $ style.say_dialogue = style.edited
        "I grab the necessary tools."
        "This should do it."
        "Either way, it's a problem solved."
        $ style.say_dialogue = style.normal
    else:
        "I look around my room for something, anything that could possibly help Sayori."
        "There's not much I can think of that could help her."
        "But I spot something, something that could do it and take it."
    "Will this be enough?"
    "Sayori is in a really complicated state right now."
    "Will taking this with me really help her?"
    "Or will it just make things worse?"
    "I have to take a chance, don't I?"
    if sayori_confess and not sayori_dumped:
        "She's my girlfriend."
    else:
        "She's my best friend."
    "And I know what's best for her."
    "This is the right thing to do."
    "I know it."
    "I make sure that I have everything I need and head towards Sayori's house."
    "I just hope I can make a difference."
    scene bg house with wipeleft_scene
    "My heart is beating fast."
    "Why am I nervous to take this to Sayori?"
    "I guess I know why."
    "I'm wondering if this is the right thing to do."
    "Will this really do?"
    "Is this going to fix her issues?"
    "I take a look at what I'm going to give to Sayori."
    "As I do, a car drives past me incredibly fast."
    "The sound of the tyres screeching the road almost make me drop what I'm holding."
    "Okay, that was too close."
    "I should keep it in my bag, where it belongs."
    scene bg sayori_bedroom with wipeleft_scene
    "The door to her house was already open."
    "I decided to let myself in and go to her room to look for her."
    "The door to her room was also open but..."
    "She doesn't seem to be here."
    mc "Sayori?"
    mc "Where are you?"
    "I wait for a response but there's nothing."
    "Maybe she's not home."
    "But then why were the doors open?"
    "There's something going on here."
    mc "Is anybody here?"
    "Once again, there's no response."
    "There's dozens of reasons going through my head for why this could be happening."
    "She could be playing a prank on me."
    "She could just be out of the house for a few minutes."
    "She might not have come back yet."
    "But in any case, why would she leave the front door open?"
    "Sayori isn't the smartest person but even she knows better than that."
    "If she isn't here right now, I should close her front door."
    "She wouldn't want some person to just go into her home."
    "..."
    "Even though I literally just did that."
    scene black with wipeleft_scene
    $ persistent.ch15_sayori_chance = True
    $ renpy.save_persistent()
    $ currentpos = get_pos()
    stop music fadeout 2.0
    "I go downstairs and shut the door to her house."
    "I look around her house again for any sign of her."
    "Once again, there's no sign of her anywhere."
    "Now that I think about it, all the doors downstairs are open too."
    "And upstairs as well."
    "Every single door in her house was open."
    "There's no reason for that, is there?"
    "I check the back of her house and as I expected, it's open."
    "The other houses in the neighbourhood didn't have open doors."
    "It was just Sayori."
    "I'm getting worried."
    "I take my phone out and dial her number."
    "..."
    "Voicemail."
    "I don't usually hear her voicemail unless I call her early in the morning."
    "It's a sing-song voicemail and it's kinda cute actually."
    "She sings a song that we used to listen together as kids..."
    "For some reason, it always left me feeling happy."
    "Like it's an important part of my past."
    "But that's not what's important here."
    "I'm just wondering what in the world is going on here?"
    "What happened to Sayori?"
    "If only I could go back."
    "If I forced myself to go with her."
    "Before we arrived at my house."
    "I dial Sayori's number again."
    "Once again, there's nothing."
    "I hear Sayori's sing song voicemail again but it's making me worried."
    "Where could she be?"
    call ch15_exclusive_sayori_alone
    return

label ch15_sayori_check:
    # You really think ANY Sayori would let you explore the plot???
    if ch14_sayori_date_choice and sayori_personality == 0:
        jump ch15_exclusive_sayori_together
    else:
        mc "Sayori, wait."
        s 2e "H-Huh?"
        s "I have no time to wait for you, [player]."
        s 2f "I have to go."
        mc "But--"
        s 2d "I'm sorry."
        s "It'll all be explained later."
        s "But I'm really running out of time."
        mc "It's just..."
        s 2h "I know."
        s "You're worried."
        s 2q "But it's fine, really!"
        "Sayori beams."
        s 2a "Don't worry."
        mc "..."
        jump ch15_sayori_check_fail
    return

label ch15_exclusive_sayori_together:
    $ ch15_s_together = True
    # Wow.
    mc "Sayori, wait."
    s 2e "H-Huh?"
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() != player.lower():
            s 2h "[currentuser], what did you do?"
            s "What have you done?!"
    s "Why is this happening?"
    s 1h "Did you eat a strawberry?"
    mc "What are you talking about?"
    mc "No, I didn't eat a strawberry, Sayori."
    mc "I'm just worried about you."
    s 1i "You really don't need to worry about me."
    s "I can handle it myself."
    mc "Handle what yourself?"
    mc "You know what? I don't care."
    mc "You have to let me come with you."
    s 1u "W-What?"
    "Sayori's eyes begin to water up."
    s 1v "Why...?"
    mc "Because I have this bad feeling that if I don't..."
    mc "Something bad is going to happen to you."
    s 1t "It's you..."
    "She looks at me with a smile on her face."
    s "You're not going to change your mind, are you?"
    mc "Not today."
    mc "Not when I know there's something I can do to help."
    s "You're too much."
    s "Really."
    mc "Is that a bad thing?"
    s "...No."
    show sayori 1y
    play music t8 fadeout 2.0
    "Sayori sighs."
    s "Okay, [player]."
    s "You win."
    s "You can come with me."
    mc "Really? That's great."
    mc "Thank you for this, Sayori."
    s "I should be the one thanking you."
    s 1t "You cared enough to go back."
    s "To try to change what was going to happen."
    mc "I don't know what you mean."
    s 1y "It's nothing."
    s "It's just..."
    "Sayori looks at me and tears start filling her eyes."
    scene black with dissolve_cg
    # CG HERE IF I HAD ANY ARTISTS NICE
    mc "Sayo--"
    "She wraps her arms around me and buries her face on my shirt."
    "She tries saying something but I can't really make it out through the tears."
    mc "It's okay."
    mc "Everything is going to be okay."
    "Once again, she tries to say something but her voice is muffled."
    "We stay like this for a couple of minutes."
    "She's just sniffing, not really saying anything."
    "Suddenly, I have an idea."
    "There's something in my room."
    "Something that I just know will lift Sayori's mood."
    mc "Sayori, can you wait for me?"
    "She unburies her head."
    s "W-What?"
    mc "I need to get something from my room."
    mc "My house is right around the corner, I won't be a minute."
    s "Y-Yeah, okay."
    s "I'll be here."
    "What if she runs away?"
    "She wouldn't, would she?"
    "Not after what just happened."
    "I can't risk it."
    "I can't leave her alone."
    scene bg house
    show sayori 1t zorder 2 at i11
    with dissolve_cg
    mc "Actually, why don't you just come with me?"
    s "Huh?"
    mc "I don't want you to run away."
    mc "If I leave you by yourself, you just might."
    s 1y "[player], you don't need to--"
    mc "You know how easily you get distracted."
    mc "You could see a butterfly and start following it."
    s 2l "I'm not like that...am I?"
    mc "Just come with me."
    "I grab Sayori's hand."
    s 2y "[player]--"
    mc "Let's go."
    "We start walking the rest of the distance to my house."
    "Sayori is looking down at the ground behind me."
    "I turn my head a couple of times to check what she's doing but she seems to be avoiding my eyes."
    "But despite that, I think I noticed a smile."
    scene bg house
    show sayori 2d zorder 2 at t11
    with wipeleft_scene
    play music t6 fadeout 3.0
    "We arrive at my house after a brief walk."
    "Sayori is still in tow, still avoiding my gaze."
    "I open the door to my house and step inside."
    "She doesn't follow me."
    mc "Something wrong?"
    s "I'll just wait out here."
    mc "Sayori..."
    s "I won't run off!"
    s 2q "I promise."
    s "I'll stay right here until you get back."
    mc "You promise?"
    s 2d "I pinky promise."
    "Sayori holds out her hand and extends her pinky finger."
    mc "What are you...?"
    mc "Ah, we haven't done this since we were kids."
    s 1l "I know it's been a while..."
    s "But do you remember?"
    mc "Remember what?"
    s 1d "Our very first promise."
    s "We made it back when we were still little."
    mc "Um..."
    "I try to think back to that time."
    "It's been so long."
    "I just can't seem to remember."
    mc "I don't--"
    s 1a "Ehehe, it's okay."
    s "It wasn't important."
    s 1k "I just thought you might have remembered."
    "She looks kinda upset about it."
    "I should try hard to remember."
    s 1d "Well?"
    s "Are you going to pinky promise?"
    mc "Right."
    "I hold out my pinky and connect it with hers."
    s 2q "I promise I'll stay here."
    mc "And I promise I'll do my best to help you."
    "She lets out a big smile and I do the same."
    s 2a "You should get going."
    s "The place we need to go to is expecting me soon."
    mc "Where exactly {i}are{/i} we going?"
    s "You'll find out when we get there."
    mc "I'm not one for surprises."
    s 2q "Sure you are."
    mc "Whatever, I'll be right back."
    mc "Don't go anywhere."
    s 2r "I won't!"
    scene bg bedroom with wipeleft_scene
    "I get into my room and look for it."
    "The thing that can make Sayori happy."
    "..."
    "I search around for a couple of minutes but can't find it."
    "It's got to be around here somewhere."
    if persistent.markov_agreed:
        $ style.say_dialogue = style.edited
        "I need to find the necessary tools."
        "The tools to deal with Sayori."
        "The tools to--"
        $ style.say_dialogue = style.normal
        "Wait...what am I thinking?"
        "How the hell did that kind of thought get into my head?"
        "I should get back to looking for that item."
    "But I really don't know where it is."
    "I sit on my bed, defeated."
    "Sayori is waiting for me outside."
    "Did I just make her wait for nothing?"
    "Should I just give up looking for it?"
    "It looks like I'm going to have to."
    "I probably don't need it anyway."
    "I'll try looking for it again later."
    "I definitely didn't move it.{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    "I definitely didn't move it.{fast}"
    window auto
    "In fact, I didn't get the idea to take it until just now."
    scene bg house
    show sayori 1q zorder 2 at t11
    with wipeleft_scene
    mc "You actually stayed."
    s 1h "Of course I did!"
    s "I wasn't going to run away..."
    s "Not after what you've done."
    s 1l "And not after a pinky promise."
    s "I know you're with me, [player]."
    mc "Uh...right."
    mc "So where are we going anyway?"
    s 1d "We're going to the city."
    s "But first we need to stop by my house."
    mc "The city?"
    mc "What for?"
    s "There's someone I need to meet there."
    s "He's got some answers for me."
    mc "Answers for...?"
    s 2b "I'll tell you when we have the time."
    s "Right now, we have to get to my house."
    s "Before it's too late."
    mc "Too late?"
    s 2h "No time to explain!"
    "Sayori grabs my hand."
    "Despite the short distance, she starts running towards her house."
    "I guess she's in a hurry?"
    scene bg house
    show sayori 1b zorder 2 at t11
    with wipeleft_scene
    "We stand at the front of her house."
    "She turns towards me and grabs me by the shoulders."
    s "This is going to sound weird, [player]."
    s 1c "But I need you to help me open all the doors in my house."
    mc "What?"
    s 1e "Do you trust me?"
    mc "You know I do, but--"
    s 1h "Then please, just do it."
    s "This whole thing depends on it."
    mc "Okay, Sayori."
    mc "I'll do it."
    scene black with wipeleft_scene
    "She unlocks the door to her house."
    "Immediately she runs up the stairs."
    "I can hear the faint sound of doors opening."
    "I guess I should be doing the same."
    "I begin to open all the doors in Sayori's house."
    "I'm not still not sure if this is a good idea or not."
    "But it's her idea, and I trust her."
    "Soon enough, all the doors to her home are open."
    "I hear her going downstairs so I go outside to meet her there."
    scene bg house with wipeleft_scene
    "There's a taxi waiting outside Sayori's house."
    "He looks at me impatiently but I just shrug at him."
    "Maybe Sayori called him?"
    show sayori 1j zorder 2 at t11
    mc "You didn't change your--"
    s "No time."
    "Okay then."
    s "Did you open all the doors?"
    mc "Yeah, just like you asked me to."
    s 1d "Good."
    "Sayori takes a deep breath."
    s "Sorry, it's just my whole plan is really unstable."
    s 1k "And there are a couple of reasons for it."
    s "I mean, have you seen the state of the world?"
    mc "State of the world...?"
    s "Never mind."
    mc "Aren't you gonna close the front door at least?"
    s 1f "No."
    s "Every door needs to be open."
    s 1h "Otherwise, it might not work."
    mc "Are you gonna tell me what this plan of yours is?"
    "Sayori pretends to ignore the question."
    s 2j "Hey, Taxi!"
    "The taxi driver looks at Sayori."
    "He looks as if he recognizes her."
    s 2a "Let's go."
    mc "Alright."
    "Sayori and I both step into the taxi."
    "The taxi driver turns towards us and looks at us expectantly."
    s 2c "Do you know where this shop is?"
    "Sayori shows the man a picture of a store front."
    "It looks like some kind of art shop?"
    "The taxi driver nods."
    s 2d "Take us there, please."
    s "Go as fast as you can."
    s 2e "Please, you have to hurry."
    "I think I saw the taxi driver let out some kind of smile through the rear view mirror."
    "It almost seemed malicious."
    "Almost immediately, the car screeches and starts accelerating."
    show sayori 1b
    "I hit my head on the seat in front of me in the commotion."
    "I look out the window and someone walking by almost drops what they're holding."
    "I hope whoever that was is okay."
    "The thing they were holding looked pretty delicate."
    scene bg city_day with wipeleft_scene
    "Soon enough, we make it to the city."
    "At this time, there's usually a decent amount of traffic."
    "But..."
    "The roads are almost empty."
    "The streets and sidewalks are filled with people but quite literally the only things on the roads are public transport."
    "Sayori got a lot of phonecalls on the way here."
    "But she didn't answer any of them, instead letting it get to voicemail."
    "She just told me that it wasn't important."
    "I guess whoever was calling her she was trying to ignore because after the third call she turned off the sound on her phone."
    "What a strange day."
    show sayori 1f zorder 2 at t11
    s "I'll tell you everything when we get off this taxi."
    s "I'm going to sound crazy."
    s 1g "And honestly, right now, I think I am."
    s "But you're here with me."
    s 1k "And..."
    if ch14_sayori_date_choice:
        s "When I think about what there is to lose..."
        s "I know that {i}we{/i} can do it."
    else:
        s "When I really think about it..."
        s "I know that I can do it."
    mc "Any reason we're going to this particular shop?"
    s 1h "It's someone I met."
    s "Well...maybe met is the wrong word."
    s 1d "All you need to know is that he's really helpful."
    s "But he can be a bit...weird to say the least."
    s "You'll see him soon."
    "The taxi stops outside a shop called 'Restoration'."
    "The outside looks really clean and it has displays of various portraits and paintings."
    "It's some kind of art shop?"
    "The sign outside says it's closed."
    show sayori 1c
    "Sayori pays the taxi driver who looks at her wide eyed."
    "He smiles and gets out of the car and opens the doors for us."
    "How much did she just pay him?"
    "We step outside and she gives him a friendly wave goodbye."
    "He gets back in his taxi and honks his car before driving off."
    "This time, at a legal speed."
    mc "Are you going to explain to me what's happening now?"
    s 1d "Yeah."
    "Sayori sighs."
    s "First, I should probably move it all back."
    mc "Move what--"
    "A rush of information flows into my head."
    "The pain it brings hurts so much."
    "It lasted for a few seconds but it felt like an eternity."
    mc "What the hell was that?!"
    s 1k "It was what I removed from after the meeting."
    s "That's all you need for now."
    "I remember everything after the meeting now."
    "How Sayori was talking about Monika..."
    if monika_type == 0 or monika_type == 1:
        "The danger Monika told me about!"
    "How could I even have forgotten that?!"
    s 1h "Okay, you have to promise not to say anything until I'm finished."
    s "Because my chain of thought is all over the place right now."
    mc "Okay, I promise."
    s 1k "I'm breaking what I swore to myself by telling you this."
    s "But..."
    s 1h "I think it won't matter."
    s "Because you're not really you."
    "I try to open my mouth."
    "She puts her finger over it."
    s 1k "This whole world is collapsing."
    if monika_type == 0 or (ch12_markov_agree and monika_type == 1):
        s "Between what I have to deal with and this thing that Monika told me."
        s "This dark and cruel evil thing that I still don't really know how to deal with."
    else:
        s "And I can sense there's something else too."
        s "Something dark."
        s "Something evil."
    s "All the weird stuff that's been happening."
    s 2j "It's not a coincidence."
    s "It's the result of the world we know breaking."
    s "Because it was never meant to be like this."
    s 2h "I'm not meant to be alive."
    s "I was meant to die, [player]."
    s 1k "By suicide."
    s "And you were meant to find me."
    s "I'm not the only one."
    s "Yuri and Natsuki aren't meant to be alive either."
    s "Not at this stage."
    s "They're both meant to be...gone."
    s 1h "All of this...it's happening because of the mod that {i}you{/i} installed."
    s "Everything is breaking."
    s "And [player]...you're meant to be a puppet."
    s 1i "A blank person, meant to serve as a conduit."
    s "The connection to the real world that's out there."
    s 1f "And yet despite all of that, here we are."
    s "Still alive and still ourselves."
    "Sayori paces around."
    s 1k "Don't get me wrong."
    s "I really appreciate what you've tried to do."
    s "You wanted to give us happy endings."
    s "At first, I thought it would be easy."
    s "But now..."
    "She stops pacing."
    s 1j "There's so much wrong with this world."
    s "The others don't know the extent of it."
    s "And I've been trying to fix it all."
    s "But I can only do so much."
    s "I almost hate that Monika gave this responsibility to me."
    s 1h "But I suppose if she didn't, I wouldn't be here today."
    s "I wouldn't be telling you how difficult this all is."
    s "I never thought it would be {i}this{/i} difficult, [player]."
    s 1k "I just wish..."
    s "That things could be normal."
    s "That things were easier."
    s "That I could just go back to the simple days of bliss."
    s "But I know."
    s 1g "I can't give this up."
    s "Getting rid of it now could make everything unstable."
    s "I'm already too committed to this task."
    s 1c "Now, you've probably got a lot of questions."
    s "I don't know if I can answer all of them."
    s "I know that if you ask some certain questions, the game--"
    s "This {i}world{/i} will...tear itself apart for all I know."
    s 1d "So please be careful in what you ask, okay?"
    mc "I'll be careful."
    s "Alright."
    s "Ask away."
    label ch15_exclusive_sayori_together_questions:
    menu:
        "What responsibility did Monika give you?" if not ch15_s_questions[0]:
            $ ch15_s_questions[0] = True
            s 1k "Hmm..."
            s "I don't know if I can really answer that."
            s "Let's just say things were difficult before."
            s 1h "I wouldn't be who I am if Monika didn't give me this responsibility."
            s "Maybe you know what I'm talking about."
            s "It's a really dumb thing to think about."
            s "I'm not even sure why all this responsibility is linked to it."
            s 1j "But that's the way things are."
            s "I can't do anything to change them."
            s "Handing this responsibility back to her in this current state would be terrible."
            s 1d "I wouldn't want to put that kind of burden on her."
            s "It's just not fair."
            s "So I have to deal with it."
            jump ch15_exclusive_sayori_together_questions
        "How do you know all of this?" if not ch15_s_questions[1] and ch15_s_questions[0]:
            $ ch15_s_questions[1] = True
            s 1h "Getting this power gave me..."
            s "The ability to gain knowledge."
            s "Not just the normal way."
            s "I can't just look it up on the internet."
            s 1k "No, I've had to do some terrible things."
            s "I've had to experience things I never thought I would."
            s "All because I could."
            s "Because in the end, I could just undo it."
            s 1h "Does that make me a horrible person...?"
            s "I try to tell myself that I'm doing it for them but..."
            s "Who knows at this point?"
            s 1f "I could be doing this for myself."
            s "My head isn't clear right now."
            s "It's like these rainclouds are stopping me from seeing the sky."
            s "But this time, I can't get rid of them."
            s 1k "They've become a part of me..."
            jump ch15_exclusive_sayori_together_questions
        "What's my role in all of this?" if not ch15_s_questions[2]:
            $ ch15_s_questions[2] = True
            s 1c "I'm not entirely sure."
            s "You're here but you're not like the others."
            s "You're different."
            s 1b "You're not entirely bound to the underlying rules of this world."
            s "And that's because you're being watched."
            s "All your actions are determined by someone else."
            s 1f "Even you asking this question."
            s "You didn't really ask it."
            s "If you're talking about right now..."
            s "How you aren't 'really you'..."
            s 1h "It's difficult to explain and I'm not sure how I can answer that without breaking things..."
            s "But, I assume that {i}you{/i} want to know {i}your{/i} role too."
            s "Your strawberries."
            s "That's the main thing."
            s 1k "In fact, without them you wouldn't even be here right now."
            s "Because I know you used them to get here."
            s "How else could you have known?"
            s 1e "I'm afraid you're going to have to use them again at some point."
            s "They're stronger than mine."
            s "They can even make me forget."
            s 1h "That's terrifying to me, you know?"
            s "Not being able to control my own destiny..."
            s 1k "Sigh..."
            s 1j "I guess you're the only one who can really do that."
            s "I just hope you haven't made a big mistake."
            jump ch15_exclusive_sayori_together_questions
        "Is there anything I can do to help?" if not ch15_s_questions[3] and ch15_s_questions[2]:
            $ ch15_s_questions[3] = True
            s 1k "There's nothing."
            s "Everything is already set in motion."
            s 1f "It's not up to you to change things."
            s "You can't do what I can, [player]."
            s "If you could, I might have been a little more positive about this."
            s "Because together, I know we can beat it."
            s 1h "And..."
            s "At this point, it's not really up to me either."
            s "But I have to try."
            s "With everything I've got."
            s 1j "I'm going to do my best."
            s 1d "I just want you to be there."
            s "Be there when it happens."
            s "Be with me...when it happens."
            s "Okay?"
            s 1k "Because our fate entirely up to {i}you{/i}."
            s "All you need to know is when to act."
            s 1h "I hope you can figure it out."
            jump ch15_exclusive_sayori_together_questions
        "Who are you talking to?" if not ch15_s_questions[4]:
            $ ch15_s_questions[4] = True
            s 1g "I can't...answer that."
            s "I'm not sure what kind of effect it will have."
            s "Especially since last time you knew..."
            s "Things didn't go well."
            s 1f "I'm sorry."
            s "I know you want to know."
            s "You deserve to know."
            s "But they deserve their happy ending more."
            s 1d "Besides, I'm sure whoever it is is probably listening right now."
            s "I'm not sure why you'd even ask that question."
            jump ch15_exclusive_sayori_together_questions
        "Why did you leave all the doors open?" if not ch15_s_questions[5] and ch15_s_questions[4]:
            $ ch15_s_questions[5] = True
            s 1c "Do you remember what I said?"
            s "How you aren't really you?"
            s "I'm sure soon enough the game will realize there are two [player]s."
            s 1b "And when that happens, you'll merge into a single person."
            s "I know you noticed."
            s "While we were in the car, someone almost dropped their things."
            s 1d "Do you know who that was?"
            s "Don't say it."
            s "I'm certain you know anyway."
            jump ch15_exclusive_sayori_together_questions
        "Who is this guy we're meeting?" if not ch15_s_questions[6]:
            $ ch15_s_questions[6] = True
            s 1a "He's a friend."
            s "You wouldn't know him."
            s "At least...you shouldn't know him."
            s 1d "But I trust him and that should be enough for you as well."
            s "Okay?"
            jump ch15_exclusive_sayori_together_questions
        "Why don't you just give up?" if persistent.markov_agreed and not ch15_s_questions[7] and ch15_s_questions[6]:
            $ ch15_s_questions[7] = True
            s 1g "G-Give up?"
            s "That's..."
            s 1k "Do you think I haven't thought about it?"
            s "There's still thoughts of depression, you know."
            s "You can't just cure it out of somebody."
            s "Sure, you can reduce the effect."
            s 1j "But it never truly goes away."
            s "If I gave up now, it would have all been for nothing."
            s "All that time and effort, just wasted."
            s "Why would you even ask something like that?"
            s 1h "Are you trying to get a response out of me?"
            s "Well, good job."
            s "You've done it."
            s 1u "I really thought I could believe in you, you know?"
            s "I..."
            s 1v "I think I'm overreacting."
            s "Am I overreacting?"
            s "I'll just..."
            s 1k "Whatever."
            jump ch15_exclusive_sayori_together_questions
        "How did I forget and how did I remember it again?" if not persistent.markov_agreed and not ch15_s_questions[7] and ch15_s_questions[6]:
            $ ch15_s_questions[7] = True
            s 1h "It's best you don't know that information."
            s "If I tell you, then it might just lead to ruin."
            s 1c "But let's just say, you never really forgot."
            s "Your memories were just placed elsewhere."
            s 1k "I was planning to give them back to you."
            s 1l "Just...not so soon."
            s 1h "I'm sorry."
            jump ch15_exclusive_sayori_together_questions
        "What are you going to do now?" if not ch15_s_questions[8] and ch15_s_questions[0] and ch15_s_questions[1] and ch15_s_questions[2] and ch15_s_questions[3] and ch15_s_questions[5] and ch15_s_questions[6] and ((ch15_s_questions[7] and not persistent.markov_agreed) or persistent.markov_agreed):
            $ ch15_s_questions[8] = True
            s 1k "Now?"
            s "Well, I want some answers first."
            s "I know he probably won't have them all."
            s 1g "But he's our best shot."
            s "Even if he can give me something I don't already know."
            s 1d "Just a tiny bit of information."
            s "That could be all I need to solve the puzzle."
            jump ch15_exclusive_sayori_together_questions
        "Never mind.":
            pass
    s 1d "Then I guess this is it."
    s "We're gonna go inside."
    s "He's waiting for us."
    s "Just be warned..."
    s 1l "He can be a little...peculiar."
    s "But he's definitely really helpful."
    s "I'm sure if anyone can help us, he can."
    mc "Alright, Sayori."
    mc "I'm not sure what we're in for."
    s 1c "I'm not sure either."
    s "I just hope it's not all bad news."
    mc "You're expecting bad news?"
    s 1d "Any news will be helpful."
    s "Good or bad."
    show sayori 1b
    "Sayori puts her hand at the door then freezes."
    "I try waving a hand in front of her face but she's not moving."
    "I hear a bit of rustling coming from inside."
    "Suddenly, she comes back to life."
    mc "Are you okay?"
    s 1f "I'm fine. Let's go, we've got no time to lose."
    s "Especially since your time is running out."
    scene bg portraitshop_day with wipeleft_scene
    "Sayori and I step into the shop."
    "I didn't notice before but the sign outside showed opening hours."
    "Right now, the store should be open."
    "But it's closed."
    "All around the place I can see canvases of artwork."
    "And just things you'd see lying around in an arts and crafts class."
    "Sayori and I approach the counter."
    show sayori 1c zorder 2 at t11
    s "Are you here?"
    s "I need answers."
    show sayori zorder 2 at t21
    show mysteriousclerk 2c zorder 3 at f22
    play music t17 fadeout 0.5
    cl "My my, where are your manners dear?"
    cl "Surely you haven't forgotten how to say the word 'please' since last we met, have you?"
    cl 4b "Ohoho, and it seems we've got company."
    "The clerk notices me and skitters across towards me."
    if persistent.ch13_nat_date:
        cl 4e "And who might you--"
        cl "Wait..."
        cl 4g "I...I know you."
        show mysteriousclerk zorder 2 at t22
        mc "What?"
        mc "I don't think we've met before."
        mc "I definitely would have remembered someone like you."
        show mysteriousclerk 4h zorder 2 at t22
        cl "No, no!"
        cl "We've definitely met."
        cl "You're--"
    else:
        cl 4e "And who might you be, hmm?"
        if player_gender == "boy":
            cl "Perhaps the dashing young boyfriend of our friend Sayori here."
        else:
            cl "Perhaps the beautiful young girlfriend of our friend Sayori here."
        cl 4f "Curious."
        cl "Definitely not the finest specimen but--"
    show sayori 2j zorder 3 at hf21
    show mysteriousclerk zorder 2 at t22
    s "Look, we're not here for introductions, okay?"
    s "And besides, you know perfectly well who this is and how and why he's here."
    s 2h "You know enough about [player_reflexive] to have figured it out by now, right?"
    "The clerk nods his head."
    s 2g "I'm here for answers."
    s "I know you've got some."
    s "So...please."
    show sayori zorder 2 at t21
    show mysteriousclerk 3a zorder 3 at f22
    cl "I see."
    cl "You're desperate."
    cl 3b "I mean, who wouldn't be given your situation?"
    cl "Okay."
    cl 1i "Ask away, and I shall try to answer to the best of what I know."
    cl "But it isn't much."
    cl "I haven't learned as much as you would have wanted me to."
    cl 1j "It's just not possible."
    cl "With the limited extent of power that I have over this world."
    show sayori 2d zorder 3 at f21
    show mysteriousclerk zorder 2 at t22
    s "That's all I can ask for."
    s "Thank you."
    show sayori zorder 2 at t21
    mc "Wait a second..."
    mc "What kind of power do you have?"
    mc "Is it anytihng like Sayori's?"
    "The clerk gives me a confused expression."
    show mysteriousclerk 1b zorder 3 at f22
    cl "So she didn't tell you, did she?"
    cl "Is that wise?"
    cl 2c "Keeping secrets from those we trust?"
    cl 2e "Hah."
    cl "Whatever, it's none of my business."
    cl 5d "But a relationship is built on trust."
    cl "You, of all people should know that."
    show mysteriousclerk zorder 2 at t22
    mc "Sayori, that's alright."
    mc "You don't need to tell me."
    mc "I still trust you."
    mc "We've all got secrets to hide."
    show sayori 2h zorder 3 at f21
    s "I couldn't tell [player_reflexive]."
    s "Even if I wanted to."
    s "You know he's not even meant to be here."
    s 1k "Do you know how broken this world is right now?"
    s "The risk I'm taking even bringing [player_reflexive] into contact with you..."
    show sayori zorder 2 at t21
    show mysteriousclerk 5b zorder 3 at f22
    cl "There's no risk, if you do things correctly."
    cl "And by the looks of things, it seems you have."
    cl "Believe me."
    cl 5h "I've been down this road before."
    cl "And if there's anything I've learned..."
    cl "It's that it was ruined because of a lack of trust."
    cl "But it's up to you."
    show mysteriousclerk zorder 2 at t22
    mc "Sayori, really."
    mc "You don't need to tell me."
    mc "I'm sure it's better that way."
    mc "Besides, I'm only here for you."
    mc "To help you."
    mc "You don't have to listen to this guy."
    show sayori 1d zorder 3 at f21
    s "I know."
    s "He's always been difficult to work with."
    s "But still, I know he can help."
    show sayori 1f
    "Sayori changes the expression on her face."
    "It seems all serious now."
    s "Did you find anything new about what's going to happen tomorrow?"
    show sayori zorder 2 at t21
    show mysteriousclerk 5e zorder 3 at f22
    cl "Not since the last time you asked."
    cl "Like I said before, that evil thing that's coming..."
    cl "I don't know if you can stop it."
    show sayori 1g zorder 3 at f21
    show mysteriousclerk zorder 2 at t22
    s "Then if I can't stop it, then who can?"
    s "Who in this world can do something that I can't?!"
    show sayori zorder 2 at t21
    show mysteriousclerk 1e zorder 3 at f22
    cl "I believe you know the answer already."
    cl "You just don't want to accept it."
    cl "Because of what it implies."
    show sayori 1h zorder 3 at f21
    show mysteriousclerk zorder 2 at t22
    s "..."
    s "Have I really reached the extent of what I can do?"
    s "This is it?"
    show sayori zorder 2 at t21
    show mysteriousclerk 1f zorder 3 at f22
    cl "That's it."
    cl "You were never intended to become the--"
    "The clerk looks at me then back at Sayori."
    cl 1w "To have it in the first place."
    cl "So some of the powers are locked."
    cl "Never to be accessed."
    cl 2i "It's just one of the rules of this world, I suppose."
    "The clerk shrugs."
    cl "Those powers can only be unlocked by the true wielder of this power."
    cl "The one that it was intended for."
    show sayori 1i zorder 3 at f21
    show mysteriousclerk zorder 2 at t22
    s "You know I can't do that."
    s "There must be another way."
    s 1j "A way to prevent tomorrow."
    s "Or at least, defeat what's coming."
    s "You have to know something."
    s "You have to!"
    show sayori zorder 2 at t21
    "The clerk takes a look at Sayori and laughs."
    show mysteriousclerk 2x zorder 3 at f22
    cl "Ahaha..."
    cl "If I knew the answers, I wouldn't be here running a store."
    cl 4a "It's an inevitability, you know that."
    cl "Your time will come, the same happened to me."
    cl "You just have to face it."
    cl 4b "Even if that other person who is undoubtedly listening helps you..."
    cl "There's no guarantee it's gonna all work out."
    show sayori 1i zorder 3 at f21
    show mysteriousclerk zorder 2 at t22
    s "I refuse to believe it."
    s "We can change the future."
    s "We haven't given up hope yet."
    show sayori zorder 2 at t21
    show mysteriousclerk 4e zorder 3 at f22
    cl "Listen, Sayori."
    cl "Even with all this new knowledge I have now..."
    cl "It's not going to help."
    cl 4f "Knowing when it's going to happen wouldn't have helped me."
    cl "Knowing what it is wouldn't have helped."
    cl "You can't stop inevitability no matter how prepared you are."
    cl 4h "And trust me, I know."
    cl "I was the most prepared out of everyone."
    cl 1j "I {i}warned{/i} everyone."
    cl "And they were ready."
    cl 1o "At least, they thought they were."
    cl 1p "But you know how that story ends."
    cl 4i "And you."
    "The clerk puts his hands on my shoulders."
    cl 4e "You know you're going to forget everything that's happened here, right?"
    cl "I can already sense your time running out."
    cl "So bringing you along was pointless."
    show mysteriousclerk zorder 2 at t22
    mc "What?"
    mc "Is he right, Sayori?"
    mc "Am I really going to forget everything?"
    show sayori 1h zorder 3 at f21
    s "I don't know."
    s "But I know you'll have to merge."
    s 1g "You're an impossibility, [player]."
    s "You...shouldn't exist."
    s 1k "And I assume it's going to take the latest copy of you instead of..."
    s "You won't keep your memories, [player]."
    s "This ending up being all for nothing."
    s "But at least...I have you here."
    s "I'm sorry."
    show sayori zorder 2 at t21
    mc "So that's how it is?"
    mc "I'm going to forget everything?"
    mc "I won't be able to help Sayori tomorrow...?"
    show mysteriousclerk 1d zorder 3 at f22
    cl "Cruel world, ain't it?"
    cl "You get used to it."
    show mysteriousclerk zorder 2 at t22
    mc "All of this was for nothing?"
    mc "I had this bad feeling and so I knew that I had to try to help Sayori."
    mc "That I could..."
    mc "Get her through this in one piece."
    mc "Maybe I could have helped prepare for tomorrow."
    mc "To deal with...whatever it coming."
    mc "But if I'm just going to forget..."
    mc "Then..."
    mc "I'm sorry."
    mc "I wanted to help."
    mc "I didn't want you to be alone."
    mc "To have to deal with this all by yourself."
    mc "It seems more useless than I thought."
    show sayori 1k zorder 3 at f21
    s "No, I'm sorry..."
    s "I should have told you."
    s 1h "But there's just no way for you to keep your memories."
    s "Unless you were the latest copy."
    s 1g "But you're not even a real copy...you're just..."
    show sayori zorder 2 at t21
    show mysteriousclerk 1h zorder 3 at f22
    cl "Actually."
    cl "There is some way you can get through all of this."
    cl "Memory intact."
    show sayori 1j zorder 3 at f21
    show mysteriousclerk zorder 2 at t22
    s "What?"
    s "Then why didn't you say anything?!"
    show sayori zorder 2 at t21
    show mysteriousclerk 4e zorder 3 at f22
    cl "I had to be sure [player_possessive] heart was in the right place."
    cl "There's still a possibility that it isn't."
    cl 4f "But hell..."
    cl "It's all going to end soon so why not?"
    show sayori 1n zorder 3 at f21
    show mysteriousclerk zorder 2 at t22
    s "So you'll help [player_reflexive] keep [player_possessive] memories of this?"
    show sayori zorder 2 at t21
    mc "Why are my memories so important?"
    mc "Even if I remember, what can I do?"
    show mysteriousclerk 4b zorder 3 at f22
    cl "You can help the person watching help us."
    cl "Because otherwise, you're oblivious."
    "I'm not sure I quite understand what he means."
    "But at least I'll be able to remember what he said."
    cl 3e "I can't do much."
    cl "I can only give instructions."
    cl "But this is kinda..."
    cl "Well, let's say morally gray."
    show sayori 1h zorder 3 at f21
    show mysteriousclerk zorder 2 at t22
    s "Morally gray?"
    s "In what way?"
    show sayori zorder 2 at t21
    show mysteriousclerk 3d zorder 3 at f22
    cl "We need to put [player_possessive] mind along with [player_possessive] memories into another person."
    cl "But only temporarily."
    cl 3f "He needs to make physical contact with [player_possessive] real self."
    cl "Then if you do things correctly, the memories should just transfer right over."
    cl "And the other person will be back to normal without a memory of what he tried to do."
    show sayori 1k zorder 3 at f21
    show mysteriousclerk zorder 2 at t22
    s "Y-You're asking me to take away someone's free will?"
    s "It's only temporary but still...!"
    s "I..."
    show sayori zorder 2 at t21
    show mysteriousclerk 1b zorder 3 at f22
    cl "It's the only option."
    cl "Otherwise he's not gonna remember a thing."
    cl "And all of this effort...you know."
    "The clerk makes an explosion gesture with his hands."
    show mysteriousclerk zorder 2 at t22
    mc "Sayori..."
    mc "If you can't do it..."
    mc "I won't force you to."
    mc "I'd rather forget than make you manipulate someone else for me."
    show sayori 1l zorder 3 at f21
    s "I've already..."
    s "...crossed that boundary, [player]."
    "Sayori avoids my eyes."
    s 1k "What's one more time, right?"
    show sayori zorder 2 at t21
    mc "Sayori..."
    show mysteriousclerk 1e zorder 3 at f22
    cl "You know what, this might work."
    cl "If he remembers everything then..."
    cl 5f "I may have something for you, Sayori."
    cl "It's not foolproof."
    cl "You still need to do a lot of preparations for it."
    cl 5i "I'm not sure you'll find the time to get everything you need."
    cl "Or if you would even want to go through with it, knowing what it implies."
    show sayori 1j zorder 3 at f21
    show mysteriousclerk zorder 2 at t22
    s "Anything to save my friends.{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    s "Anything to save my friends.{fast}"
    window auto
    s 1l "Ehehe, oops."
    s "And besides, I have all the time in the world."
    s "Tell me what we have to do."
    show sayori zorder 2 at t21
    show mysteriousclerk 5h zorder 3 at f22
    cl "Well...firstly, we need to get [player]'s memories."
    cl "And quickly. I think [player_possessive] time is running out quicker than we thought."
    cl "To do that..."
    cl 5a "I'm gonna need something."
    cl "I won't be a second."
    show mysteriousclerk at thide
    hide mysteriousclerk
    show sayori zorder 2 at t11
    "The clerk enters the back of the shop."
    s 1d "Are you ready, [player]?"
    mc "I guess so."
    mc "You know..."
    mc "You're putting a lot of blind faith into this guy."
    mc "What makes him so special that you'd just trust him like that?"
    s 2c "It's hard to explain..."
    s 2d "And if I told you, you wouldn't believe me."
    s "Let's just say...he's like us."
    mc "I'm not sure I get it but--"
    $ currentpos = get_pos()
    stop music
    play sound fall
    $ pause(0.25)
    scene black
    with close_eyes
    $ pause(1.5)
    s "What the--"
    cl "He shouldn't be conscious for this."
    cl "Trust me, the pain is unbearable."
    s "That doesn't mean you had to do that!"
    s "I could have--"
    cl "Do you know how much time is left before he disappears?"
    cl "Just transfer [player_possessive] memory already."
    s "But to who?"
    s "Yuri, Natsuki or--"
    cl "There's another person."
    cl "She's at the mall right now buying gifts for your club members."
    s "But how do you know that?"
    cl "I know a lot of things."
    s "Then...I hope you know about this."
    s "It's the Portrait of--"
    cl "Then it's worse than I thought."
    cl "But we can still do this, we just--"
    call poem(False,10,True)
    scene bg mall_sunset with open_eyes
    play music t3g fadein 0.5
    queue music t3g2
    "And it seems that I've finished buying gifts for everyone."
    window auto
    "Yuri didn't really tell me much about the club members."
    "I really should have looked at more on that paper Yuri gave me than just their names and faces."
    "Ah, I'm so clumsy!"
    "Get it together, you're going to be in you're senior year next year!"
    "I sure hope they like what I've bought for them."
    "I definitely didn't cheap out on it."
    "I..."
    "I grab my head."
    "Who am I?"
    "I'm..."
    "[player]...right?"
    "No, I'm Ayame."
    "Why do I even need to ask myself that?"
    "Why can't I think straight all of a sudden?"
    "Ah...!"
    "I need to sit down and figure things out."
    "There's so many people talking at once."
    "What do I have to do?"
    "I...have to meet up with the club members, right?"
    "That's what I have to do."
    "But where are they?"
    "Something in the back of my head is telling me to go to the food court."
    "That's where they are, right?"
    "I suppose I'll find out."
    scene bg mall_sunset with wipeleft
    "I make it to the food court."
    "There are people all over the place."
    "I notice a group of four people walking away."
    "One with pink hair, another with brown and one with..."
    "Purple!"
    "That's Yuri, it's got to be."
    "Where are they going in such a hurry?"
    "I need to tap [player_reflexive] on the shoulder."
    "That should be enough."
    "Enough...for what?"
    "What am I even thinking about?"
    "I start running towards them to catch up."
    ay "Hey, wait up you guys!"
    "It seems like one of them is on their phone and doesn't turn around."
    "Wait...does my voice sound different?"
    ay "Haaahhh...haaahhh..."
    "I stop to catch my breath."
    ay "I didn't expect you guys to be here."
    show yuri 3be zorder 2 at t32
    y "A-Ayame?"
    y "W-What are you doing here?"
    show natsuki 2bc zorder 3 at f31
    n "You know her, Yuri?"
    "Her...?"
    n "Why don't you introduce us?"
    show natsuki zorder 2 at t31
    ay "Oh, where are my manners?"
    "I reach out a hand to the girl with pink hair."
    "If I remember correctly, she's Natsuki...right?"
    ay "My name is Ayame."
    ay "I'm..."
    ay "Well, I don't know..."
    show yuri 3ba zorder 3 at f32
    y "She's planning to join the club."
    y "I invited her."
    show yuri zorder 2 at t32
    show monika 2bb zorder 3 at f33
    m "You did?"
    "The girl with brown hair turns towards me."
    m "You seem...familiar somehow."
    "I know this girl."
    "She's Monika."
    m 2ba "Do I know you?"
    "She clearly doesn't know me."
    show monika zorder 2 at t33
    ay "No, but I know you."
    ay "You used to be such a great debater!"
    ay "And now you're the..."
    "Vice president."
    "That's what it said on the piece of paper, I think."
    ay "Vice president of the Literature Club!"
    "I don't even remember reading it from the paper."
    "But...how else could I have known?"
    show monika 2bc zorder 3 at f33
    m "Yeah...that's right."
    m 3ba "How did you know that?"
    show monika zorder 2 at t33
    ay "I just did, I suppose."
    ay "Yuri must have told me or something."
    "I'm not sure on the answer myself."
    ay "Who's that over there?"
    "I point towards the boy walking away from the group."
    "Upon closer inspection, it seems he has earphones on."
    "Maybe that's why he didn't notice that everyone else stopped."
    ay "Is he with you?"
    show yuri 3bb zorder 3 at f32
    y "Yes, he is."
    y "It's [player]."
    show yuri zorder 2 at t32
    ay "Oh, you told me about [player_reflexive]!"
    "Why does this name feel so familiar?"
    "Not just [player_possessive] name..."
    "But [player_possessive] whole being."
    "I only read [player_possessive] name and remembered [player_possessive] face."
    "So why...?"
    "Walk towards [player_reflexive]."
    "I start walking towards [player_reflexive]."
    ay "[player], I want to ask you something."
    "I tap [player_reflexive] on the shoulder."
    show sayori glitch zorder 2 at t11
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/3.ogg"
        renpy.music.play(track, loop=True)
    $ pause(1.0)
    $ gtext = glitchtext(48)
    "{cps=60}[gtext]{/cps}{nw}"
    $ pause(1.0)
    $ gtext = glitchtext(48)
    "{cps=60}[gtext]{/cps}{nw}"
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    $ pause(1.5)
    hide screen tear
    window hide(None)
    window auto
    scene black with trueblack
    scene bg mall_sunset
    with open_eyes
    play music t3g
    queue music t3g2
    "I'm...back?"
    "I'm not sure what that means."
    "But I remember everything."
    "That whole conversation with Sayori and...that guy."
    "As well as my memories from after the meeting."
    "Did I {i}merge{/i}?"
    "What does that even mean...?"
    "But if I did merge..."
    "Does that mean I can help her?"
    "He didn't really give us any useful information."
    "Maybe he told Sayori something."
    "But how did I even get here?"
    "The details are kinda fuzzy."
    ay "Hello?"
    "I look behind me."
    show ayame 1bb zorder 2 at t11
    "A girl I've never seen before is in front of me."
    "The other three seem to have been talking to her."
    "I take off my earphones."
    mc "Oh!"
    mc "I didn't realize somebody was talking to me."
    mc "Did you need something?"
    ay 1bg "Um..."
    ay "I don't..."
    ay "I don't know?"
    ay 1bh "H-Hi!"
    ay "I'm Ayame."
    "Ayame?"
    "Why is that name so familiar?"
    "She extends out her hand."
    mc "I'm [player]..."
    show natsuki 1bc zorder 2 at t41
    show yuri 1bf zorder 3 at f42
    show ayame zorder 2 at t43
    show monika 1bc zorder 2 at t44
    jump ch15_mall_shared_transfer

label ch15_exclusive_sayori_alone:
    $ persistent.ch15_sayori_chance = False
    $ ch15_s_together = False
    $ renpy.save_persistent()
    "She's not answering her phone."
    "She's not in her home."
    "This is terrible."
    "I'm meant to be working on the preparations with her tonight."
    "We were meant to do it together and I have no idea where she is."
    "Should I call the police or something?"
    "Or am I just overreacting here?"
    "Maybe someone from the club knows where she is."
    "If anyone would, it would be the president, Monika."
    "I mean, vice president."
    "I don't know why I keep getting the two of those confused."
    "I guess President Monika just sounds more natural than President Sayori..."
    "I get my phone out and dial Monika's number."
    "I hope I'm not intruding her."
    "It's just that I'm really worried about Sayori..."
    "Monika picks up within seconds."
    m "Hello, Monika speaking."
    mc "Monika, it's me."
    m "[player]? What's the call for?"
    mc "I need to ask you something."
    m "Ask me something?"
    m "Well...alright, I suppose I can try to answer."
    mc "It's about Sayori."
    m "Sayori?"
    if monika_type == 0:
        m "What about her?"
        mc "Do you know where she is?"
        mc "She told me to meet at her house but she isn't here."
        m "Ah..."
        m "She's not with you?"
        mc "She's not..."
        mc "And I'm at her house right now."
        m "Maybe she's out somewhere?"
        mc "She did say she needed to do something."
        mc "But she wouldn't tell me what."
        m "I see."
        mc "And for some reason..."
        mc "All the doors in her house, they're all--"
        "A strange sound comes from the phone."
        "As if someone was clearing their throat really loudly."
        m "[player], I think you should leave Sayori be."
        mc "Huh?"
        m "Come to the mall instead."
        m "Sayori can handle it herself."
        mc "Handle what herself?"
        mc "Monika, do you know where she is?"
        m "She's busy, okay?"
        m "You really shouldn't get involved."
        mc "But I need to help her."
        mc "She needs it."
        m "You can't decide what Sayori does and doesn't need."
        m "If she wants to go her own way, why are you stopping her?"
        m "Doesn't she have a right to be independent?"
        mc "I know she can be independent!"
        "Monika doesn't say anything back."
        mc "I'm sorry for shouting."
        mc "I'm just really worried."
        mc "You've noticed it too, haven't you?"
        m "Noticed what exactly?"
        mc "She's tearing herself apart."
        mc "Putting all this responsibility on her."
        mc "There's no way she can do it alone."
        m "She's more than capable, [player]."
        mc "How can you know that?"
        mc "You don't know her like I do..."
        m "I know a lot more than you give me credit for, [player]."
        m "And you have to trust me."
        m "You have to believe in her."
        m "Have faith that she's going to be okay."
        mc "I just feel so helpless."
        m "That's why I'm telling you to come to the mall."
        m "It'll help you put your mind off it."
        m "And you can be helpful here."
        mc "How?"
        m "I'll tell you when you get there."
        m "You trust me, right?"
        mc "Of course."
        m "I'm glad."
        m "Look, I need to go do a couple of things."
        m "But I'll meet you there, okay?"
        mc "Sure..."
        m "We'll find a way to cheer you up, [player]."
        m "I promise."
        m "Goodbye, [player]."
        mc "I'll see you there, Monika."
        "Monika hangs up."
    else:
        m "Aren't you with her right now?"
        mc "No, I was just about to ask you if you knew where she was."
        mc "Seeing as you're the vice president of the club."
        mc "She would have told you something, right?"
        m "I don't think she's told me anything about what she's doing."
        mc "So she has told you something?"
        m "I'm sorry, [player] but she really didn't tell me much."
        m "She just said that she had some business to attend to."
        m "Alone."
        mc "But why alone?"
        mc "We're meant to be doing things together."
        m "Why don't you try calling her and asking that yourself?"
        mc "I did, there was no answer."
        m "Ah..."
        m "Well, there's nothing I can do about that."
        mc "It was worth a shot."
        mc "I'll look for her my self then, thanks Monika."
        m "Wait!"
        m "You shouldn't do that, [player]."
        mc "Why not?"
        m "Have you ever considered the possibility that she's better off alone?"
        mc "Monika, Sayori really isn't that kind of person."
        mc "She likes being around friends."
        m "Are you saying she can't be independent?"
        mc "I'm not saying that..."
        mc "I'm just saying that Sayori usually isn't the type to do things alone."
        mc "And that's what has me worried."
        m "You shouldn't be worried about her, [player]."
        m "She knows what she's doing."
        mc "How can you know that?"
        mc "Right now, you don't even know what she's doing."
        mc "She could be anywhere!"
        mc "And I'm not there with her."
        m "It's not the end of the world, is it?"
        m "Sayori is more than capable of taking care of herself."
        m "You of all people should know that..."
        mc "Huh...?"
        m "She's been acting differently, right?"
        m "You've seen it with your own eyes."
        m "She's become...extraordinary, has she not?"
        mc "That..."
        mc "That doesn't anything."
        m "It shows she's growing."
        m "And learning."
        m "Adapting to change."
        mc "Whatever..."
        mc "I just feel helpless about it all."
        mc "I'm meant to be helping her."
        mc "Instead, I let her go do things alone."
        mc "And without her, there's nothing for me to do."
        m "I see..."
        "Monika pauses for a moment."
        m "Well, you could always come to the mall."
        m "I can find a way for you to be useful."
        m "And it might help you take your mind off things."
        mc "Is that a good idea?"
        m "I don't know."
        m "But it's better than complaining and getting nothing done, right?"
        mc "I suppose..."
        m "If you're going, I'll meet you there."
        m "There are still some things I have to take care of first."
        mc "Okay."
        mc "Thanks for the talk, Monika."
        mc "It helped...I think."
        m "Mhm."
        m "Whatever it takes."
        "Monika hangs up."
        "Whatever it takes?"
        "What did she mean by that?"
        "Whatever it takes to cheer me up?"
        "That's probably it."
        "She seemed like she really wanted to help me and Sayori."
        "So maybe I should go to the mall."
    "I put my phone away."
    "I'm still worried about Sayori."
    "I don't know what kind of situation she could have possibily gotten herself into."
    "But after that call with Monika."
    "I guess I'm a little more reassured."
    "Sayori can take care of herself."
    "But that still leaves me worried about how she's treating herself."
    "There are just some things you shouldn't do alone."
    "Some things you can't do alone."
    "I just hope whatever she's doing isn't one of them."
    "I take one last look around Sayori's house."
    "I think it's best if I close all of these doors."
    "It's kinda freaking me out for some reason."
    "It just feels ominous."
    "After I do that, I need to make my way to the mall."
    "Maybe Sayori will be back by then."
    "I have nothing to worry about."
    call ch15_mall_shared
    "I'm back from the mall."
    return

label ch15_mall_shared:
    scene bg mall_sunset with wipeleft
    play music t3
    "I sit down on the bench just outside of the food court."
    if ch13_name != "Sayori":
        "[ch13_name] told me to wait for her here so that's what I'm doing."
        "I think after that, we're pretty much ready for tomorrow."
        "She's running kinda late though."
        "She told me to meet her here ten minutes ago but she still hasn't arrived."
    else:
        "Monika told me to wait for her near the food court."
        "I feel bad for leaving Sayori but I just don't know where she is."
        "I even tried ringing her a couple more times just to find out but there was nothing."
    if ch13_name == "Monika":
        if ch15_m_together:
            "I spent my time just browsing around for manga or anime I might have liked."
            "I didn't really have the money to go and buy some."
            "What I did notice was that there was a volume seven of Sweet Oppression."
            "I guess it's doing pretty well if it's already got that many volumes."
            "I still don't know why Monika wants to do this alone."
            "And I haven't really thought about it."
            "I guess she'll tell me if she thinks it's time."
        else:
            "I tried really hard to look for what Monika asked me to."
            "I probably went through a quarter of the stores in the mall looking for the things on her list."
            "In the end, I had no luck."
            "When I told her, she didn't seem mad at all."
            "It's like she knew I wouldn't find anything..."
            "Almost like she just wanted me to be away from her."
    elif ch13_name == "Yuri":
        "The things Yuri was looking for were pretty difficult to find."
        "I think I went through several dozens of stores but only got a few items."
        "I had to ask the store assistants each time and half of them had no idea or tried to get me to buy another brand."
        "If it wasn't there, I just moved on to the next store."
        "I let her know each time I got one of the things on her list and she did the same so that we weren't looking for the same thing."
        "Luckily, we managed to get everything on her list."
    elif ch13_name == "Natsuki":
        "I wasn't really able to help her today."
        "I tried looking in all the stores I know that stock ingredients."
        "But none of them really had what Natsuki was looking for."
        "Except one."
        "One store seemed to have almost everything Natsuki needed."
    show yuri 1ba zorder 2 at t11
    if ch13_name == "Yuri":
        y "There you are, [player]."
        y "I hope you weren't waiting too long."
        mc "No, not at all."
        mc "Where were you anyway?"
        y 1be "I just had to quickly attend to something."
        y "I apologize, I only remembered after I bought the last item."
        y 2bb "Don't worry about it, I'm here now."
        mc "Alright, well what now?"
    else:
        y "[player]?"
        y "Is that you?"
        mc "Yuri?"
        mc "I knew you were going to the mall but I didn't expect to actually see you."
        mc "This place is huge."
        y 1bf "I just happened to be passing by."
        y "I've already finished my business here at the mall."
        if ch13_name != "Sayori":
            y 1bg "What are you still doing here?"
            mc "I'm meant to be meeting up with [ch13_name] here."
            mc "She wanted to do some last minute things with the preparations."
            y 2bh "I see."
            "Yuri looks around."
            y "Well, do you mind if I sit here?"
            y "I'm a little exhausted from today."
            mc "Not at all."
        else:
            y 2be "What are you doing here?"
            mc "Sayori just kinda...disappeared."
            mc "I'm not really sure what to do."
            y 2bf "Disappeared?"
            mc "Yeah, I called Monika and she told me to meet her here."
            y "Curious..."
    "Yuri takes a seat on the chair opposite me."
    y 3be "How do you suppose the play is going to be tomorrow?"
    mc "I'm not sure."
    mc "Hopefully good but anything could happen."
    mc "Any sort of event could ruin the day for us tomorrow."
    y 3bf "That doesn't seem like something that's likely to happen."
    mc "It's not like I want something to happen."
    mc "But I've just had this impending feeling."
    y 3bh "An impending feeling, huh?"
    "Yuri sinks her head into her arms."
    y 3bk "I think I understand."
    mc "You do?"
    y 3bo "Sometimes I just get this feeling of..."
    y "It's hard to describe...but I guess it's like something bad is going to happen."
    mc "Have you always had that?"
    y 3bq "Ever since last week."
    mc "Why did I know you were going to say that?"
    y 2bn "What?"
    mc "I just knew you were going to relate it back to last week."
    mc "And I have no idea why."
    mc "Is that feeling why you were acting so..."
    mc "I don't know, different?"
    y 2bt "Why I turned crazy, you mean...?"
    y "I'm not sure."
    y "It could be."
    y 2bv "I mean at first I thought it was because of me being so obssessed with you."
    y "Because of the way you treated me."
    if yuri_date:
        mc "Do you really think that's the reason?"
        mc "It just seems so...wrong somehow."
    else:
        mc "I mean, I pretty much treated you with indifference."
        mc "Didn't I?"
    y 2bt "I don't know."
    y "But it does make sense that that feeling would be making me feel this way."
    mc "There has to be some reason."
    y 2bh "[player], there's a multitude of reasons."
    y "A lot of them don't make sense."
    mc "I don't really know much about you before you met me."
    mc "But I'm assuming you didn't act like that with just anyone."
    mc "Especially for someone like me."
    y 2bq "W-What's wrong with someone like you?"
    y "B-But you're right, I've never acted like that before."
    y "Or at least, I never fell to that level..."
    y "Maybe it's--"
    show monika 2ba zorder 3 at hf33
    if ch13_name == "Monika":
        m "Oh, there you are!"
        m "I hope I didn't keep you waiting too long."
        m 4bb "I really just needed to--"
        m "Wait a second, is that Yuri...?"
        m 4ba "Ahaha, sorry I forgot to say hi to you too."
    elif ch13_name == "Sayori":
        m "Hey there, [player]."
        m 2bb "I'm sorry I'm a bit late, I had to run some errands."
        m "Oh, how rude of me."
        m 4bb "I didn't see you there, Yuri."
        m "Hi to you as well!"
    else:
        m "I thought I saw the two of you but I wasn't sure."
        m 2bb "Anyway, I just wanted to drop by and say hi before leaving."
        m "But if you don't mind me asking, what are the two of you doing here?"
    if ch13_name == "Yuri":
        m 2bc "I mean, shouldn't the two of you be at home right now?"
        m "Preparing for the big day tomorrow?"
    else:
        m 2bc "Shouldn't you be at home preparing by now?"
    show yuri 1ba zorder 3 at f32
    show monika zorder 2 at t33
    y "Hello, Monika."
    y 1bg "[player] and I were just speaking about..."
    show monika 2bd
    "Monika eyes Yuri curiously."
    y 1bj "W-Well, it's not important."
    y "It's good to see you."
    show yuri zorder 2 at t32
    show monika 2be zorder 3 at f33
    m "Actually, you've caught my attention."
    m "What {i}were{/i} the two of you talking about?"
    m 2bc "It isn't a secret, is it?"
    m "The two of you aren't hiding something from me, are you?"
    show monika zorder 2 at t33
    mc "No, of course not."
    # Considers Yuri's feelings
    if yuri_date:
        "I turn towards Yuri."
        "She clearly doesn't want to talk about this with Monika."
        "I think we can keep it our little secret for now."
        mc "It was really nothing."
        mc "Just how we were feeling for the day tomorrow."
        show monika 1bj zorder 3 at f33
        m "Well...okay."
        m "If you say so."
        m 1be "I know it might not have been anything, but I'm really sorry for trying to pry."
        m "I know we all keep secrets."
        m "For all sorts of different reasons."
        m "Anyway, let's just forget I even asked."
    else:
        mc "It wasn't really anything important."
        mc "We were just talking about how Yuri has this bad feeling that something is going to happen tomorrow."
        mc "And why she--"
        show yuri 1bn zorder 3 at f32
        y "[player]...!"
        y "T-That's...!"
        show yuri zorder 2 at t32
        show monika 1bn zorder 3 at f33
        m "Ah..."
        m "If you don't want to tell me, you don't have to."
        m "I'm sorry, I really didn't mean to pry."
        m 1be "We all have our little secrets, after all."
        m "I'll keep mine and you keep yours, okay Yuri?"
    show yuri 1bq zorder 3 at f32
    show monika zorder 2 at t33
    y "T-Thanks, Monika."
    "There's an awkward silence between the three of us."
    "Monika pretends to look busy by going on her phone."
    "Yuri plays around with her sweater a bit."
    y 1bs "Um..."
    y "So, how are you feeling about tomorrow, Monika?"
    y "It must make you a little nervous playing tomorrow, right?"
    show yuri zorder 2 at t32
    show monika zorder 3 at f33
    if monika_type == 0:
        m 1bm "You're right, Yuri."
        m "I'm really, really nervous about tomorrow."
        m 1bl "There's all sorts of questions bouncing around my head."
        m "What if I mess up and somebody notices?"
        m "What if nobody likes what I'm playing?"
        m "How is everyone going to react?"
        m 1be "But in the grand scheme of things..."
        m "None of that really matters."
        show yuri 2bf zorder 3 at f32
        show monika zorder 2 at t33
        y "It doesn't?"
        y "Why not?"
        show yuri zorder 2 at t32
        show monika 3bj zorder 3 at f33
        m "Ahaha, like I said."
        m "I have my secrets and you have yours."
        show yuri 2bh zorder 3 at f32
        show monika zorder 2 at t33
        y "It's just that you seem really calm for a person who says they're nervous."
        y "Whatever this \"grand scheme\" of yours is must be really big."
        y 2bi "I hope you can take care of it Monika."
        y "If anyone can, you can."
        show yuri zorder 2 at t32
        show monika 3be zorder 3 at f33
        m "Honestly, I don't know."
        m "But I'm doing my best to prepare for it."
        m "And if I'm nervous, it's going to slow me down."
        m "So I don't really have the time or energy to waste being nervous."
    else:
        m 1bc "I'm nervous about tomorrow."
        m "But not for the reasons you're saying."
        m "In fact, I'm probably most confident about my performance on the piano tomorrow."
        show yuri 2be zorder 3 at f32
        show monika zorder 2 at t33
        y "You're not nervous about having to play the piano?"
        y "What is it then, the play?"
        y "Or is it something else?"
        show yuri zorder 2 at t32
        show monika 2bb zorder 3 at f33
        m "It's something else, Yuri."
        m "Trust me, I'm not at all nervous for our part in Inauguration Day tomorrow."
        m "It's what's coming after."
        m "That's what I'm really nervous for."
        show yuri 2bf zorder 3 at f32
        show monika zorder 2 at t33
        y "...What's happening after?"
        y "I'm not aware of any club activities after our play."
        y "Is one of the other clubs doing something?"
        show yuri zorder 2 at t32
        show monika 4ba zorder 3 at f33
        m "I think it's best if we keep that a surprise."
        m "After all, you and I keep our own secrets."
        show yuri 2bg zorder 3 at f32
        show monika zorder 2 at t33
        y "Whatever it is, I hope you can do it Monika."
        y "If anyone can, you can."
        show yuri zorder 2 at t32
        show monika 2bc zorder 3 at f33
        m "I don't know if I can."
        m "I've had to do so many things to even get to this point."
        m "Even now, I'm still preparing for it."
        m "I guess that's why I'm not nervous at all about what we're doing tomorrow."
        m "Since I have no time to worry about it."
    m 1ba "But thanks for the words of encouragement."
    show monika zorder 2 at t33
    mc "I guess you can't ignore it either."
    mc "It seems like it's taking up a lot of your time."
    mc "What are you going to do if it doesn't work out?"
    show monika 1bb zorder 3 at f33
    m "Well, the reason I'm preparing is so that it {i}does{/i} work out."
    m "So I haven't really considered the possibility of failing."
    m 1bm "Besides, if it doesn't work out..."
    m "Then nothing matters anymore."
    show yuri 2bq zorder 3 at f32
    show monika zorder 2 at t33
    y "That's rather bleak."
    y "I'm sure you can still persevere even if things don't go your way, Monika."
    show monika 1bf
    "Monika simply sighs."
    y "It couldn't be that bad, could it?"
    show yuri zorder 2 at t32
    show monika 1be zorder 3 at f33
    m "Who knows?"
    m "If anything, it could be worse."
    m "I suppose we'll all find out tomorrow, won't we?"
    show monika zorder 2 at t33
    mc "It's going to affect all of us, isn't it?"
    mc "Whatever it is you're talking about."
    "Monika simply smiles at me."
    show yuri 3bf zorder 3 at f32
    if ch13_name != "Monika":
        y "A-Anyway, what are you doing here?"
        y "I thought you would have gone home by now."
        y "Have you finished your preparations already?"
    else:
        y "A-Anyway, I hope your preparations are going well."
        y "I assume the two of you are doing well for yourselves since you're still here."
    show yuri zorder 2 at t32
    show monika 2bb zorder 3 at f33
    m "Just about finished actually!"
    m "Now, if you don't mind..."
    show yuri 1bh zorder 3 at f32
    show monika zorder 2 at t33
    y "Wait, Monika!"
    y "I have to know..."
    y 1be "...Just what exactly is on the line?"
    show monika 1bo
    y "You're making it seem like whatever is coming is terrible."
    y "Isn't there anything we can do to help?"
    if ch13_name == "Monika":
        y "Does [player] even--"
    else:
        y "Something that will help you--"
    show natsuki 2bc zorder 3 at hf31
    show yuri zorder 2 at t32
    if ch13_name == "Natsuki":
        n "[player]!"
        n "Why are you so hard to--"
        "Natsuki cuts herself off as she notices Yuri and Monika."
        "She turns towards me and I just give her a shrug."
        n 2bo "W-What are you guys doing here?"
        n "Aren't you all meant to be on your home to do your preparations?"
        show natsuki zorder 2 at t31
        show yuri 1bq zorder 3 at f32
        y "I was going to but then I spotted [player]."
        y "It turns out we're all here making a last minute trip for our preparations for tomorrow."
        y "I guess we all should have prepared a bit more."
        show yuri zorder 2 at t32
        show monika 1bn zorder 3 at f33
        m "Yeah..."
        m "I don't know if I could have prepared more for tomorrow."
        m "But I've done all that I can here."
        show natsuki 2bk zorder 3 at f31
        show monika zorder 2 at t33
        n "[player], did you know they'd be here at the food court too?"
        show natsuki zorder 2 at t31
        mc "Not really..."
        mc "Everyone just kinda appeared."
    else:
        n "I thought I heard your voices."
        n "It turns out, I was right."
        n 2bb "So what are you all doing here?"
        n "Shouldn't you guys be at home doing preparations or something?"
        n "It's getting kinda late to still be at the mall, you know."
        show natsuki zorder 2 at t31
        show yuri 1ba zorder 3 at f32
        y "I'm running some errands here."
        y "It's got to do with the preparations for tomorrow."
        y "What about you, Natsuki?"
        show natsuki 2bg zorder 3 at f31
        show yuri zorder 2 at t32
        n "I'm...doing the same thing."
        n 2bh "Well, I was."
        if ch13_name == "Yuri":
            n "I guess that's why [player] is there too."
            n "Then why is Monika here?"
        else:
            n "Then what are [player] and Monika doing here?"
        show natsuki zorder 2 at t31
        show monika 1bl zorder 3 at f33
        m "The same thing you and Yuri are."
        m 1bn "Buying things last minute for tomorrow and getting distracted by you guys."
        "Monika smiles nervously."
        m "Ahaha, I guess we were all a little under prepared."
        show monika zorder 2 at t33
        if ch13_name == "Monika":
            mc "And I'm here with her."
            mc "But I didn't really do much."
        elif ch13_name == "Sayori":
            mc "I'm here because Monika invited me."
            mc "Sayori is..."
            mc "...doing other things, I guess."
            mc "She'll be fine."
        else:
            mc "I'm here with Yuri."
            mc "I just came with her because otherwise I wouldn't know what to do with myself."
    show natsuki 2bg zorder 3 at f31
    n "Well, okay."
    if ch13_name == "Sayori":
        n "It's a shame about Sayori."
        n "If she was here, we'd have the whole club."
    else:
        n "You know, if Sayori was here..."
        n "We'd have the whole club."
    show natsuki zorder 2 at t31
    show yuri 3bf zorder 3 at f32
    y "It sure is quite a coincidence that we'd all meet here."
    y "At this exact time."
    y "And we're all here for the same reasons too."
    y "When you all said you were going to the mall, I didn't actually expect to see you all here."
    show yuri zorder 2 at t32
    show monika 1be zorder 3 at f33
    m "What a coincidence indeed."
    if monika_type == 0 or (ch12_markov_agree and monika_type == 1):
        m "It is kinda unfortunate Sayori isn't here."
        m "But she's got other matters to attend to."
        m "Us meeting here is almost like fate, isn't it?"
    else:
        m "Almost like it was destined to happen."
        m "Ah, but that's just silly."
    show monika zorder 2 at t33
    mc "Well, it's definitely not the weirdest thing to have happened."
    mc "And I suspect that it's only going to become even weirder."
    show yuri 1bh zorder 3 at f32
    y "I don't really want weirder things to happen..."
    y "But I'd have to agree with you."
    y "With all the things that have happened so far, I wouldn't be surprised if a serial killer showed up next."
    show natsuki 2bm
    show monika 1bm
    "Everyone looks at Yuri with wide eyes."
    y 3bq "T-That was meant to be a joke..."
    y "L-Look, why don't the two of you sit down?"
    y "We might as well talk while we're all here."
    show yuri zorder 2 at t32
    "Monika and Natsuki both take a seat."
    "Who would have thought that I'd be at the mall with everyone from the club?"
    "Well...almost everyone."
    "I did not expect to be spending my evening like this."
    "Not that I mind spending time with everyone."
    "It just seems weird that we all arrived at the same time and that we're all here for preparations."
    if ch13_name == "Sayori":
        "Everyone already finished doing what they needed to."
    else:
        "We've all finished doing what we needed to."
    "So we're just wasting our time at the mall when we could be doing the preparations we're meant to be."
    "Still, it feels like a pretty lucky coincidence that we all ended up meeting at this exact spot at this exact time."
    "This feels just like a club meeting, except we're not at the club."
    "Well...Sayori is somewhere else right now."
    "So I suppose that's not entirely true."
    show monika 3ba zorder 3 at f33
    m "You know, I just thought of something."
    show monika zorder 2 at t33
    mc "What is it?"
    show monika 3be zorder 3 at f33
    m "We're all here, aren't we?"
    m "Most of us, anyway."
    m 3bj "So..."
    "Monika stands up."
    m "Okay, everyone!"
    m "We don't really get a chance to do things together outside of the club."
    m 4ba "But today is a really good opportunity to do just that."
    m "Does anyone have any suggestions?"
    show natsuki 2be zorder 3 at f31
    show monika zorder 2 at t33
    n "Is this really a good idea?"
    n "Sayori isn't even here."
    n "It feels kinda disrespectful to do something like that without our president."
    show natsuki zorder 2 at t31
    show monika 4bf zorder 3 at f33
    m "Do you think so?"
    m "I know Sayori would want us to have fun."
    m 4be "Don't you remember what she said a few days after [player] joined?"
    $ currentpos = get_pos()
    $ audio.t3fb = "<from " + str(currentpos) + " loop 4.618>mod_assets/bgm/3f.ogg"
    scene bg club_day_gray
    show sayori 1g_gray zorder 2 at t41
    show natsuki 5g_gray zorder 2 at t42
    show monika 1d_gray zorder 3 at f43
    show yuri 3w_gray zorder 2 at t44
    show vignette zorder 100
    with dissolve_scene_full
    play music t3fb fadeout 1.0
    $ style.say_window = style.window_flashback
    m "We're the only ones responsible for the fate of this club."
    m "If we start the event and each put on a good performance..."
    m 3a_gray "Then it will inspire others to do the same!"
    m "And the more people who perform, the better we'll be able to show everyone what literature is all about!"
    show monika zorder 2 at t43
    show sayori 1r_gray zorder 3 at f41
    s "Yeah!"
    s 1x_gray "It's about expressing your feelings..."
    s "Being intimate with yourself..."
    s "Finding new horizons..."
    s "And having fun!"
    $ currentpos = get_pos()
    $ audio.t3c = "<from " + str(currentpos) + " loop 4.618>bgm/3.ogg"
    scene bg mall_sunset
    show natsuki 2be zorder 2 at t31
    show yuri 3bq zorder 2 at t32
    show monika 4be zorder 3 at f33
    with dissolve_scene_full
    play music t3c fadeout 2.0
    $ style.say_window = style.window
    if monika_type == 2:
        m "That's what happened, right?"
        m 2bc "The details are kinda fuzzy in my head."
        m "Because it was such a long time ago."
        m 2ba "Anyway..."
    else:
        m 2ba "That's what happened."
        m "Surely all of you remember?"
    m 2bb "It's up to us."
    m "The other four members of the club, to decide our fate."
    m "So what do you all say to doing something, together?"
    show yuri 3bg zorder 3 at f32
    show monika zorder 2 at t33
    y "Monika, I can't seem to recall Sayori ever saying that."
    y "Yet..."
    y 3bh "It feels {i}so{/i} familiar."
    y "Like it actually did happen."
    show yuri zorder 2 at t32
    show monika 2bh zorder 3 at f33
    m "W-What do you mean?"
    m "Can't you remember?"
    show natsuki 2bc zorder 3 at f31
    show monika zorder 2 at t33
    n "Yuri's right."
    n "I can't place exactly when that happened."
    n "Or if it happened at all."
    n 4be "I'm almost certain it did happen..."
    n "But there's so many weird details."
    show natsuki zorder 2 at t31
    mc "..."
    show monika 2bc zorder 3 at f33
    m "[player], what's wrong?"
    show monika zorder 2 at t33
    mc "This didn't happen."
    "Did it?"
    mc "I...can't..."
    "What's going on?"
    "It."
    "Did not."
    "Happen."
    "What in the world are the three of them talking about...?"
    "Sayori never said those words."
    mc "I definitely have no memory of it happening, so..."
    show monika 1bp zorder 3 at f33
    m "{i}(I think I understand.){/i}"
    m "{i}(It's all messed up.){/i}"
    m "{i}(She's messed with their minds...){/i}"
    m 1bm "Okay, everyone!"
    m "I may have made a mistake!"
    m 1be "But whether it did or didn't happen, I'm still sure Sayori would want us to have fun."
    m "She's just that kind of person, wouldn't you agree?"
    show yuri 3bf zorder 3 at f32
    show monika zorder 2 at t33
    y "I suppose."
    show natsuki zorder 3 at f31
    show yuri 3bq zorder 2 at t32
    n "Whatever."
    show natsuki zorder 2 at t31
    show monika 3bn zorder 3 at f33
    m "Well, this is a great start."
    m "No one gave a suggestion so we're just stuck here."
    "Monika ponders to herself for a moment."
    m 3ba "As the vice president of the club, I'll assume leadership while Sayori isn't here."
    m "And I actually have an idea for--"
    show natsuki 3bh zorder 3 at f31
    show monika zorder 2 at t33
    n "Wait, you're actually making this an official club activity?"
    show natsuki zorder 2 at t31
    show monika 3bb zorder 3 at f33
    m "Of course!"
    if monika_type == 0:
        m "It's going to be fun!"
    else:
        m "It's going to be very interesting."
        m "Oh, and fun too!"
    show yuri 3bo zorder 3 at f32
    show monika zorder 2 at t33
    y "Normally, I wouldn't have a problem with doing something together."
    y "Don't get me wrong, I enjoy spending time with you all but..."
    y 3bq "I still have to make some final things for the preparations for tomorrow."
    show natsuki 3bm zorder 3 at f31
    show yuri zorder 2 at t32
    n "Yuri has a point."
    n "I haven't finished baking everything yet."
    n "So if it's not that important then..."
    show natsuki zorder 2 at t31
    show monika 1bf zorder 3 at f33
    m "What could be more important than hanging out together?"
    m 1be "I promise it won't take long."
    m "It's just going to take a few minutes."
    show monika zorder 2 at t33
    mc "I think it's a good idea."
    mc "And if it won't take too long, then what do we really have to lose?"
    mc "It's still kinda early anyway."
    mc "But let's hear her out first."
    show monika zorder 3 at f33
    m "Thank you, [player]."
    m "My idea is really simple, actually."
    m 2ba "I want us all to go to the marina."
    m "We're going to do a really fun club activity there!"
    show yuri 3bo zorder 3 at f32
    show monika zorder 2 at t33
    y "The marina?"
    y "W-What are we going to be doing there?"
    show natsuki 1bg zorder 3 at f31
    show yuri zorder 2 at t32
    n "You're gonna have to be more specific than that, Monika."
    n "I'm not convinced at all."
    n 1bi "And I'm planning on leaving in less than thirty minutes."
    show natsuki zorder 2 at t31
    show monika 1be zorder 3 at f33
    m "I want us to all reflect."
    m "A reflection on literature club and what you all think of it."
    m "As the vice president, it's important to gather the member's opinions."
    m "To see how we can improve the club."
    show natsuki 1bh zorder 3 at f31
    show monika zorder 2 at t33
    n "I guess that makes sense..."
    n "I don't really see how that's going to be fun though."
    show natsuki zorder 2 at t31
    show yuri 2bf zorder 3 at f32
    y "I'm not opposed to the idea."
    y "And I think it could be fun."
    y 2bi "B-Being together outside of the club, I mean."
    show natsuki 1bo zorder 3 at f31
    show yuri zorder 2 at t32
    n "Yuri, are you serious?"
    n "How can you find that fun?!"
    n 1bp "[player], you're not seriously considering this, are you?"
    show natsuki zorder 2 at t31
    mc "I don't really mind."
    mc "Spending time with you guys is fine by me."
    show natsuki 1br zorder 3 at f31
    n "Ugh, unbelievable."
    "Natsuki looks around."
    n 1bs "I guess I {i}have{/i} to do it now, don't I?"
    n "Whatever. I'll go."
    n "This better not take long."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    if monika_type == 0:
        m 1bl "That's the spirit...sort of."
    else:
        m 1ba "Good."
    m "Then, shall we go?"
    m "The sooner we get it done with, the sooner we can all finish our preparations."
    show monika zorder 2 at t33
    "Monika gets up and the other two follow."
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    show monika at thide
    hide monika
    "I get up as well but as I do, I receive a notification on my phone."
    "It's a message."
    "I open it up and there's an ominous audio file there."
    "It came from an unknown number with a simple message."
    "It says \"listen to this in private\"."
    "Should I even open it?"
    "What if it gives my phone a virus?"
    "...When did I become this paranoid about everything?"
    "Everyone is already walking towards the marina."
    "I catch up to them as I take my earphones from my pocket."
    "I download the audio file and start listening to it."
    "It...doesn't sound like anything."
    "It's making sound but it sounds like distorted static."
    "So much for listening in private."
    "I could have listened to it out loud and everyone would probably be just as confused as I am for playing white noise."
    python:
        try: renpy.file(config.basedir + "/listen to this in private")
        except: open(config.basedir + "/listen to this in private", "wb").write(renpy.file("listen to this in private").read())
    $ ay_name = "???"
    ay "Hello?"
    "I look behind me."
    show ayame 1bb zorder 2 at t11
    if ch13_name == "Yuri" and yuri_date:
        "It's..."
        "...the girl I met in the library with Yuri."
    else:
        "A girl I've never seen before is in front of me."
    "The other three seem to have been talking to her."
    "I take off my earphones."
    mc "Oh!"
    mc "I didn't realize somebody was talking to me."
    mc "Did you need something?"
    ay 1bg "Um..."
    ay "I don't..."
    ay "I don't know?"
    ay 1bh "H-Hi!"
    if ch13_name == "Yuri" and yuri_date:
        ay "I know we really didn't get to meet properly before."
        ay 1bg "So I'd like to fix that."
        ay 1bh "At least, I think I do..."
    ay "I'm Ayame."
    "She extends out her hand."
    $ ay_name = "Ayame"
    if ch13_name == "Yuri" and yuri_date:
        mc "Once again, I'm [player]."
        mc "Nice to meet you."
    else:
        mc "I'm [player], nice to meet you."
    show natsuki 1bc zorder 2 at t41
    show yuri 1bf zorder 2 at f42
    show ayame zorder 2 at t43
    show monika 1bc zorder 2 at t44
    label ch15_mall_shared_transfer:
    "The others catch up to me as I shake Ayame's hand."
    mc "So what are you doing here, Ayame?"
    show ayame 1bi zorder 3 at f43
    ay "I..."
    ay "I was buying gifts."
    ay 1bb "Because you're all going to be my new friends, you see..."
    ay "S-Since I'm joining the club..."
    ay "And..."
    "She looks around."
    ay 1bi "Oh!"
    ay 1bg "I-I don't mean to assume."
    "Ayame bows her head."
    ay "I-If you don't want to be friends, that's fine."
    ay "But I'd still like to become a member of your club."
    show ayame zorder 2 at t43
    show monika 1be zorder 3 at f44
    m "You don't have to assume."
    if monika_type == 0:
        m "I'm more than happy to be friends."
    elif monika_type == 1:
        m "You're definitely going to be a useful {i}friend{/i}."
    else:
        m "I'm sure I can find some kind of use for you, {i}friend{/i}."
    show natsuki 1bh zorder 3 at f41
    show monika zorder 2 at t44
    n "Do you...um..."
    n "Read any sort of literature?"
    show natsuki zorder 2 at t41
    "Ayame raises her head."
    show ayame 1bb zorder 3 at f43
    ay "I read all sorts of things."
    ay "Among my favorites are horror, emotion and love stories."
    ay 1bh "I also read manga on occasion."
    ay "But I know some don't really count that as a form of literature, so--"
    show natsuki 2bg zorder 3 at f41
    show ayame zorder 2 at t43
    n "Don't listen to those people."
    n "Manga is a perfectly fine form of literature!"
    n "Don't let anyone tell you otherwise."
    show yuri 1ba zorder 3 at f42
    show ayame zorder 2 at t43
    y "Natsuki is very passionate about manga."
    y "I'm sure you two can talk a lot about it."
    y 1be "I used to be somewhat opposed to manga."
    y 1bb "But after being friends with Natsuki, I've alternated my view."
    y "I still much prefer reading novels, but I wouldn't say no to a good manga now."
    show yuri zorder 2 at t42
    show ayame 1bb zorder 3 at f43
    ay "So you've changed since becoming a member?"
    ay 1bd "I wonder what will happen after I join..."
    show ayame zorder 2 at t43
    show monika 2ba zorder 3 at f44
    m "You know, Ayame..."
    m "We were just about to do an activity as a club."
    m "You can come along, if you like."
    show ayame 1bi zorder 3 at f43
    show monika zorder 2 at t44
    ay "Really?"
    show ayame 1bj
    "Ayame's face lights up."
    ay "But I'm not really a member..."
    ay "Is that really okay?"
    ay 1bg "I don't want to intrude or anything..."
    show ayame zorder 2 at t43
    show monika 2bb zorder 3 at f44
    m "Of course!"
    m "I'm the vice president of the club."
    m "I could just instate you as a member now, if you'd like."
    show yuri 3ba zorder 3 at f42
    show monika zorder 2 at t44
    y "I'm sure Sayori wouldn't mind."
    y "In fact, I'm sure she'd like to be surprised by a new member tomorrow."
    show natsuki 1bq zorder 3 at f41
    show yuri zorder 2 at t42
    n "You guys can do whatever you want."
    n "B-But that's not to say I don't mind if you do."
    show natsuki zorder 2 at t41
    mc "I think it's up to Ayame to decide anyway."
    show monika 1bc zorder 3 at f44
    m "That's right."
    m 1ba "So what do you say, Ayame?"
    show ayame 1bb zorder 3 at f43
    show monika zorder 2 at t44
    ay "I appreciate the offer..."
    ay "But I want to wait until tomorrow to become an official member."
    ay 1bf "Not that I don't recognize your authority or anything!"
    ay "It's just that I bought these gifts."
    ay 1bh "And I'd like to give them to all five of you at the same time."
    ay "Since you're missing a member, it wouldn't be fair."
    show natsuki 1bc zorder 3 at f41
    show ayame zorder 2 at t43
    n "I guess that makes sense."
    n "That's very thoughtful of you."
    n "Does that mean you're not coming with us?"
    n 1bh "{i}(Wait, did she say gifts...?){/i}"
    show natsuki zorder 2 at t41
    show monika 2bb zorder 3 at f44
    m "The offer still stands, you know."
    m "You can still come with us to do this activity."
    m "Even as an interim member."
    m 2be "Besides, it's not really an official club thing since the president isn't here."
    if monika_type == 0 or (ch12_markov_agree and monika_type == 1):
        m "It's just something I came up with since a lot of us were together."
    else:
        m "It's simply a small activity."
    m "It won't take long, I promise."
    show ayame 1bd zorder 3 at f43
    show monika zorder 2 at t44
    ay "Okay."
    ay "If you guys want me to go with you..."
    ay "Then what harm could it do, right?"
    show yuri 3bi zorder 3 at f42
    show ayame zorder 2 at t43
    y "If Sayori was here, she would be saying something like \"yay, a new member\"..."
    show natsuki 2bd zorder 3 at f41
    show yuri zorder 2 at t42
    n "That's so true!"
    n "And she'd be jumping up and down, all excited..."
    show natsuki 1bc zorder 2 at t41
    show monika zorder 3 at f44
    m "It's unfortunate she's not here."
    m "But at least we still have five people."
    m 1ba "And the more, the merrier."
    m "But we should really be making our way to the marina right about now."
    m "Or we're going to miss it."
    show monika zorder 2 at t44
    mc "Miss what?"
    show monika 3bb zorder 3 at f44
    m "The sunset!"
    m "It's going to be beautiful tonight."
    m "We wouldn't want to miss it."
    show yuri zorder 3 at f42
    show monika 3bb zorder 2 at t44
    y "I wouldn't mind seeing it."
    y "In fact, I'd love to."
    y "Something about watching the sun dip into the waves and the moon taking it's place really excites me."
    show natsuki 2bg zorder 3 at f41
    show yuri zorder 2 at t42
    n "Um...Yuri, you know the sun doesn't actually dip into the waves, right?"
    n "It's just crossing over onto the other side of the planet."
    show natsuki zorder 2 at t41
    show yuri 3bf zorder 3 at f42
    y "Of course I did!"
    y 3bg "I was speaking metaphorically."
    show natsuki 2br zorder 3 at f41
    show yuri zorder 2 at t42
    n "Oh, now that does make sense."
    n 1bs "W-Well, in case Monika or [player] or even Ayame didn't know."
    n "Now they do, so...!"
    show natsuki zorder 2 at t41
    show ayame 1be zorder 3 at f43
    ay "Hehe, you guys are great!"
    ay "I know I'm gonna have a wonderful time when I officially join."
    show ayame zorder 2 at t43
    show monika 4bj zorder 3 at f44
    m "Come on guys! Let's hurry and get to the marina."
    m "I don't know if you guys have ever seen it but..."
    if monika_type == 0 or (ch12_markov_agree and monika_type == 1):
        m 2be "The view really is beautiful."
        m "I used to go see it a lot when I was younger."
    else:
        m 2be "The view is something you definitely need to see."
    show monika zorder 2 at t44
    mc "Is watching the sunset really that interesting?"
    "And doing a reflection while watching one?"
    "Wouldn't we be too distracted by the sunset to even reflect properly?"
    if ch15_s_together:
        "...That's what we were going to do?"
        "I'm glad I know that now."
        "I'm still trying to piece together what the hell is going on from my memories."
    show yuri 2bf zorder 3 at f42
    y "[player], have you never seen a sunset?"
    show yuri zorder 2 at t42
    mc "Of course I have."
    mc "But I haven't really ever gone out of my way to see one for the sake of it."
    show monika 2bb zorder 3 at f44
    m "Then this will be a great experience for you, [player]."
    m "It might not seem like much but a sunset can mean a lot of different things to a lot of different people."
    if monika_type == 0 or (ch12_markov_agree and monika_type == 1):
        m 2ba "For example, to some, it might even symbolize something..."
        m "...romantic."
        show monika zorder 2 at t44
        mc "Romantic?"
        mc "How exactly?"
        show monika 2bl zorder 3 at f44
        m "I'm not sure."
        m "Maybe just watching such beautiful view incites feelings of love."
    else:
        m 2bf "To some, it could mean the end of something."
        m 2ba "And the start of a new one."
        show monika zorder 2 at t44
        mc "You mean like the sun disappearing and the moon appearing?"
        show monika 2bl zorder 3 at f44
        m "Something like that."
    show natsuki 1bg zorder 3 at f41
    show monika zorder 2 at t44
    n "Can we get going already?"
    n "We might miss it if we stay here too long."
    show natsuki zorder 2 at t41
    show ayame 1ba zorder 3 at f43
    ay "Natsuki...?"
    "Ayame looks at Natsuki as if to make sure that was her name."
    "Natsuki looks at her and gives a slight nod."
    ay 1bb "...is right."
    ay "After all, you still have to do your reflections, right?"
    show ayame zorder 2 at t43
    if ch15_s_together:
        "Wait, how does she know that?"
        "I--"
        "{i}She{/i} wasn't there when Monika was talking about the reflections part...was she?"
        "Maybe she overheard her."
        "Or maybe our memories are..."
    show monika 1ba zorder 3 at f44
    m "That's right."
    m "Come on, follow me I know a shortcut."
    scene bg marina_sunset with wipeleft_scene
    "Monika took us through this whole section of the mall I didn't even know existed."
    "It seemed to avoid a lot of the weird winding sections of the mall."
    "As a result, we got to the marina pretty quickly."
    "We went to the pier, since that was the best place to watch the sunset according to Monika."
    "As I can see the sun setting, I can sort of get the appeal to it."
    show monika 4ba zorder 3 at t42
    m "Okay, everyone!"
    m "We're here!"
    show ayame 1bb zorder 3 at f43
    ay "Wow, this place is incredible."
    ay "I haven't really been to this side of the mall before."
    ay 1bg "It's too bad that I can't really stay for long."
    ay "There's so many things I need to do for tomorrow."
    ay "So I'll try to reflect as best as I can and as quick as I can."
    ay 1bi "Even though there isn't really much I can reflect on."
    show ayame zorder 2 at t43
    show yuri 1ba zorder 3 at f44
    y "You could reflect on your first impressions of everyone."
    y "You do have that notebook after all."
    show natsuki 1bc zorder 3 at f41
    show yuri zorder 2 at t44
    n "Notebook?"
    n "What do you mean by notebook?"
    show natsuki zorder 2 at t41
    show ayame 1bj zorder 3 at f43
    ay "Oh, you didn't know?"
    ay "I suppose it is a rather odd thing to ask for."
    ay "I can imagine why Yuri didn't tell you all."
    show ayame zorder 2 at t43
    show yuri 3bo zorder 3 at f44
    y "Ayame...!"
    show natsuki 4bf zorder 3 at f41
    show yuri zorder 2 at t44
    n "What didn't Yuri tell us?"
    n "What are you hiding, Yuri?"
    show natsuki zorder 2 at t41
    if ch13_name == "Yuri" and yuri_date:
        mc "It's not that big of a deal."
    else:
        mc "What is it?"
    show yuri 3bo zorder 3 at f44
    y "I was going to tell you all but..."
    "Yuri looks at everyone then at the ground."
    y "I just...didn't."
    show monika 2bm zorder 3 at f42
    show yuri zorder 2 at t44
    m "What kind of stuff did you put in this notebook anyway?"
    m 2bn "I'm sure it wasn't anything bad...right, Yuri?"
    show monika zorder 2 at t42
    show yuri 3bp zorder 3 at f44
    y "N-No! O-Of course not!"
    y "I would never do that to you guys..."
    show ayame 1bg zorder 3 at f43
    show yuri zorder 2 at t44
    ay "I'm really sorry about this."
    ay "I didn't mean to cause any trouble."
    ay "I just wanted to know more about the club."
    show ayame zorder 2 at t43
    show yuri 2bn zorder 3 at f44
    y "I thought it would be easier to join that way."
    y "After all, no one wants to join something they'll later regret, right?"
    y "It would only cause pain to the person joining and the club they joined in the end."
    y 2bq "And I thought it wasn't an unreasonable request so I went along with it..."
    y "It was just a notebook containing some details about everyone in the club."
    y "N-Nothing personal, I think."
    show monika 4bl zorder 3 at f42
    show yuri zorder 2 at t44
    m "What did you write about us and the club?"
    m "Ahaha, hopefully nothing embarrassing~"
    show natsuki 4bw zorder 3 at f41
    show monika zorder 2 at t42
    n "Yeah!"
    n "Yuri didn't talk herself up, did she?"
    show natsuki zorder 2 at t41
    show ayame 1be zorder 3 at f43
    ay "Oh, I can assure you it's nothing like that!"
    ay "From what I've read, you seem like great people."
    ay 1bj "And from what I've read of Yuri, it doesn't seem like that at all, Natsuki."
    "Ayame smiles reassuringly."
    ay 1bi "Though some things don't really add up properly."
    ay "I'm sure it's nothing though, probably just some small mistakes because it was so sudden."
    show monika 2bc zorder 3 at f42
    show ayame zorder 2 at t43
    m "I'm curious to know what sort of things don't add up."
    m "Yuri is definitely careful with her work so making mistakes like that seems out of character."
    show natsuki 2bc zorder 3 at f41
    show monika zorder 2 at t42
    n "That's a good point."
    n "But I'm sure it's probably just due to the preparations she had to do."
    n "She probably wasn't thinking straight."
    show natsuki zorder 2 at t42
    show yuri 1bf zorder 3 at f44
    y "It wasn't that, I'm certain of it."
    y "I definitely made this carefully."
    y 1bg "I wouldn't want to give false information about the club."
    show yuri zorder 2 at t44
    mc "So what exactly didn't add up, Ayame?"
    show ayame 1ba zorder 3 at f43
    ay "Well, everything about you, Yuri and Natsuki make sense."
    ay "All the things Yuri put in there seem to have no conflicts that I could find."
    ay 1bg "But there were some things relating to Sayori and Monika that just...seemed conflicting."
    show ayame zorder 2 at t43
    show yuri 2be zorder 3 at f44
    y "Are you sure?"
    y "I'm almost certain I wrote the events that happened in chronological order."
    y 2bo "M-Maybe I did make a mistake."
    show monika zorder 3 at f42
    show yuri zorder 2 at t44
    if monika_type == 0 or (monika_type == 1 and ch12_markov_agree):
        m 2bn "D-Did you say you wrote them in chronological order?"
    else:
        m 2bc "In chronological order? Interesting..."
    show monika zorder 2 at t42
    show yuri 3bf zorder 3 at f44
    y "That's right."
    y "So I'm not sure how Ayame could have--"
    show monika 2be zorder 3 at f42
    m "Ayame, can I see that notebook for a second?"
    m "You do have it with you, right?"
    show monika zorder 2 at t42
    show ayame 1bh zorder 3 at f43
    ay "I have it right here."
    "Ayame takes the notebook out from her purse."
    ay "It's been really helpful but I don't really feel like I'll need it much longer if at all."
    "She offers it to Monika who starts looking through it."
    if monika_type == 0 or (monika_type == 1 and ch12_markov_agree):
        "Starting from the back of it."
    ay "I haven't really finished it yet, I'm up to reading about the play with the lumberjack."
    ay 1bj "It's really fascinating to see what kinds of stuff your club does, you know?"
    ay "But I've learned lots of things about everyone too!"
    ay "Like how [player] joined because of cupcakes."
    "I almost forgot."
    ay "How Natsuki is an extraordinary baker."
    "Natsuki gives a smug expression."
    ay 1bh "And how Yuri is extremely talented."
    "Yuri looks away but smiles shyly."
    ay "Sayori seems like a really nice girl who's great at diffusing situations."
    ay 1bi "But from the description Yuri gave, it's strange to think that she's the president of your club."
    ay "From what I know and what I've read, she doesn't really have the qualities of a leader."
    ay "I think she would have been more suited to be vice president."
    ay 1bj "And instead the president should have been--"
    show monika zorder 3 at f42
    show ayame zorder 2 at t43
    if monika_type == 0 or monika_type == 1:
        m 1bn "Oops!"
        play sound "mod_assets/sfx/splash.ogg"
        $ pause(2.0)
        "Monika drops the book into the water."
        m 1bf "My hand slipped...I'm so sorry!"
    else:
        m 1ba "Do you mind if I keep this for a while?"
        m "At least just the first couple of pages."
    show monika zorder 2 at t42
    show ayame 1bi zorder 3 at f43
    if monika_type == 0 or monika_type == 1:
        ay "Well, that's quite unfortunate."
        ay 1bj "But it's okay."
    else:
        ay "Sure, take the whole notebook if you have to."
        ay 1bj "I don't really need it anymore."
    ay "I'd much prefer to learn about the five of you in person anyway."
    ay "It's much better than doing it through a notebook."
    show ayame zorder 2 at t43
    show yuri 3bg zorder 3 at f44
    y "I spent a good amount of time writing that for you." 
    y "I hope it wasn't a waste of time..."
    show ayame 1bh zorder 3 at f43
    show yuri zorder 2 at t44
    ay "No, of course not!"
    ay "It was actually a lot more helpful than I expected."
    ay 1bb "To be honest, it was a lot to take in."
    ay 1be "But your amazing handwriting really helped."
    "Ayame smiles widely."
    ay "So don't worry, it was a big help."
    ay 1bb "Usually, I like to take things as they go."
    ay "I always say the best way to experience something is to dive right in."
    ay "I guess the club was just an exception for me because it was something I was nervous about."
    show monika 2be zorder 3 at f42
    show ayame zorder 2 at t43
    m "There's nothing to worry about!"
    m "I assure you."
    m "We're all friendly people."
    show monika zorder 2 at t42
    show ayame 1bd zorder 3 at f43
    ay "Hehe, I can see that."
    show natsuki 2bg zorder 3 at f41
    show ayame zorder 2 at t43
    n "I don't want to be {i}that{/i} person but..."
    n 2bf "Can we get on with it?"
    n 2be "We're here to do a reflection, right?"
    n "So let's hurry up and do one."
    show natsuki zorder 2 at t41
    show monika 2ba zorder 3 at f42
    m "You're right."
    m "So...now that we're here."
    # Sunset CG thats really bad rip
    scene sunset_cg1_bg with dissolve_cg
    play music t10 fadeout 2.0
    m "Let's reflect about the club as we stare into the sunset."
    m "Does anyone want to start us off?"
    "..."
    m "No?"
    m "Ahaha, then I suppose I'll take the responsibility."
    if monika_type == 0 or (ch12_markov_agree and monika_type == 1):
        m "My time in the club has been pretty amazing so far."
        m "Starting it with Sayori and meeting all of you has been one of the best decisions of my life."
        m "It's been a really fun experience to get to know each of you."
        m "One of the things I've learned is about Natsuki and her manga."
        m "She has a passion for it that is unrivaled."
        m "You can ask her anything and everything about manga."
        m "I've discovered if she's read it, she probably knows everything about it."
        m "It's incredible the lengths someone would go to."
        m "And then there's Yuri."
        m "A quiet and timid girl who has a lot going on behind the scenes."
        m "I've always thought of Yuri as someone exceptional."
        m "Beneath that quiet exterior, she's actually got a lot of depth to her."
        m "You wouldn't know just by looking at her but she's actually really into the more horrific aspects of life."
        m "And I can respect that."
        m "We've all got our own personal delights."
        m "She was open enough to us to share that about her."
        m "I know some people wouldn't be willing to share that type of information, even with some of their closest friends."
        m "Of course, there's [player]."
        m "[player] hasn't been with us since the beginning."
        m "But it's like he's been here {i}since{/i} the beginning."
        m "The beginning of everything important anyway."
    elif monika_type == 1:
        m "The time in the club, for me at least, has been really enlightening."
        m "From the start, I didn't really know what entirely was going on."
        m "This time around, I mean."
        m "But because of the club, I've learned all the things I've needed to."
        m "Who I can trust."
        m "What I need for the future."
        m "What I need for success."
        m "And what I still need to do to achieve that success."
        m "I've learned so much about everyone."
        m "From my prior knowledge and what I've gained from your choices."
        m "It's been an immense help."
        m "I especially want to thank [player]."
        "Huh?"
        "What did I do...?"
        m "He hasn't been here since the club's inception."
        m "But that hasn't made [player_reflexive] any less valuable than anyone else."
        m "In fact, it's thanks to [player_reflexive] that I'm here."
        m "I'm glad he joined at the beginning of everything important."
        m "If he didn't, I don't know where I'd be right now."
    else:
        m "I can't really say much about the club."
        m "I can only assume it's been quite the place to be."
        m "With all the events that have been happening..."
        m "Who really knows what to think of the club right now?"
        m "That's not to say it's a bad thing."
        m "In fact, it's just the opposite."
        m "Sure, there are and will continue to be difficult times."
        m "But it's nothing I--"
        m "{i}We{/i} can't get through."
        m "After all, I wouldn't be here if it wasn't for [player_reflexive]."
        m "Being here at the start of everything important..."
        m "It's almost like fate."
    "I look at Monika, not quite understanding what she means."
    "The beginning of everything important...?"
    call screen dialog(message="To be continued!\nThanks for playing, keep an eye out on reddit and discord for updates!", ok_action=Quit(confirm=False))
    return
