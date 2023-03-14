# This happens after the main story
# Possibly will release as an individual option in custom start if I can't
# finish the story in a decent amount of time
label ch1x_monikadate:
    if persistent.markov_agreed:
        scene bg residential_day
        show monika 1a zorder 2 at t11
        "I can feel my heart pounding."
        "It's as if just being around Monika makes me feel a certain way."
        "But it's hard to say whether those feelings are really mine."
        "It's true that I once had feelings for Monika myself..."
        "But is what I'm feeling really still me?"
        "Or is it just the feelings that she's put into me now?"
        "Regardless, there's no use thinking about it now."
        "I have to do what Monika says."
        m "That's right! I'm glad you know your place."
        m "Today, I have something special planned."
        m "Do you want to know what it is?"
        "A slight smile appears on Monika's face."
        m "Well, I suppose you'll have to wait."
        m "We have more important things to do right now."
        m "Like finally go on that date we've been meaning to go on!"
        mc "A date...?"
        m "Yes, a date! It took a while to get it all ready but..."
        m "I have a whole day planned out for us."
        menu:
            m "Doesn't that sound wonderful?"
            "Yes.":
                pass
        m "Ahaha, I thought you might think so~"
    else:
        scene bg residential_day
        with dissolve_scene_full
        play music t2
        $ s_name = "???"
        s "Heeeeeeeyyy!!"
        "I see a girl running toward me from the distance, waving her arms in the air like she's totally oblivious to any attention she might draw to herself."
        "That girl is Sayori, my neighbor and good friend since we were children."
        "The kind of friend you'd do anything for, to make sure they were happy."
        "We've been walking to school together the past few weeks, and I wouldn't have it any other way."
        "I stand in front of the crosswalk and let Sayori catch up to me."
        $ s_name = "Sayori"
        show sayori 4p zorder 2 at t11
        s 4p "Haaahhh...haaahhh..."
        s "I thought I set my alarm but..."
        "Sayori takes a moment to catch her breath."
        s "Ehehe, I guess I missed it."
        mc "I'm sure you did, Sayori."
        "It's weird being one of the only people who knows what just happened."
        "With Sayori forgetting all about being the president, it's just Monika and I that remember."
        "And well...of course, you as well."
        "I have to pretend as if she was never the president this whole time."
        "I don't want to keep secrets from her but I have a feeling that even if I told Sayori the truth, I doubt she'd remember."
        "I don't think she {i}wants{/i} to remember anyway."
        "I remember what she said when she gave Monika the presidency..."
        "I have no idea what's in store for me today."
        "Maybe I'll finally be able to live a normal life."
        "Though I doubt that's the case if you're here watching me."
        show sayori zorder 2 at t11
        s 1a "Thanks for waiting for me."
        mc "Don't mention it."
        s "You want to know what a little bird told me?"
        "Sayori beams."
        mc "Huh? What is it?"
        s "Well, I was speaking to Monika and I heard she has a date!"
        mc "A date?"
        "That's not surprising. I doubt someone like Monika would struggle to find a date."
        "She's beautiful, smart and cares about all her friends."
        "That person is incredibly lucky to be dating Monika."
        mc "Do you know who it is?"
        s "I have no clue! That's just what she told me."
        s "She told me she won't be able to come to the club today because of it."
        mc "Well...I'm sure whoever it is is well deserving."
        mc "Monika doesn't seem the type to pick just anyone."
        s "You're right. Whoever they are, I'm sure they'll do right by her!"
        mc "I hope you're right."
        s "Even if I'm wrong, I think Monika can handle it."
        s "She's strong. That's why she's the president of our club!"
        mc "Can't argue with you there, Sayori."
        "I wonder who Monika is dating anyway..."
        "Not that it's any of my business."
        scene bg class_day
        with wipeleft_scene
        "The school day is as ordinary as ever, and it's over before I know it."
        "It feels like things are going back to normal."
        "No strange favours from someone or weird occurences happening."
        "Quite the change from how it's been recently...not that I'm complaining."
        "It's nice not having to worry about these things."
        show monika 1a zorder 2 at t11
        m "Ah, [player]. There you are."
        mc "Monika? What's going on?"
        mc "Don't you have some sort of date going on?"
        m "Sayori told you about that, did she?"
        m "Ahaha, well I actually wanted to speak to you about that."
        m "Because I was wondering if you were interested on going on that date."
        "I can feel my heart pounding against my chest."
        "I'm not sure I processed those words correctly."
        "She couldn't have possibly said what she just said, could she?"
        "It's a dumb question, but I have to ask her."
        "This is not what I was expecting when Sayori told me about Monika earlier today."
        mc "Me? On a date?"
        "I look behind me and there's no one there."
        mc "Did I hear that correctly?"
        mc "You're asking me out on a date."
        m "Um..."
        "Monika smiles."
        m 1b "Yeah, that's right!"
        m "Is there something wrong with that?"
        mc "N-No, it's just...I don't know what to say."
        m "Well...a yes would be ideal."
        m "That is, if you're interested. I wouldn't want to make you go, if that's not what you want to do."
        menu:
            m "So do you want to go on a date with me?"
            "Yes.":
                pass
            "Of course!":
                pass
            "No." if not persistent.markov_agreed:
                m "Oh..."
                m "I'm sorry. I thought..."
                m "I...I need to go. I'll see you tomorrow."
                mc "Monika wait--"
                show monika at thide
                hide monika
                "Before I can tell her to stop, she walks away from me."
                "She increases her pace and has her head down as she walks down the hallway."
                "Was that a mistake...?"
                "Monika is a great person but I'm just not interested in her."
                "I don't even know where this came from all of a sudden."
        m "That's great! I was hoping you would."
        show sayori 1a zorder 3 at f21
        show monika zorder 2 at t22
        s "Hey, [player]! I--"
        "Sayori notices that Monika is in the room with us."
        "She looks back and forth between Monika and I a few times."
        "It looks like she's slowly coming to a realization."
    $ monika_outfit = 1
    $ persistent.monika_date_reload = 0
    # Placeholder scene
    scene bg park_day
    show monika 1ba zorder 2 at t11
    $ pause(0.25)
    stop sound
    hide screen tear
    play music t12m
    window show(None)
    m "Then you won't mind if I take you out here."
    window auto
    "We're suddenly brought out to a rooftop overlooking a city."
    "I'm not sure if it's the city I'm from as I can't seem to make out any of the buildings."
    mc "Monika...where are we?"
    m "At the tallest building of some city you've probably never heard of."
    m "I figured since we're doing everything fresh, we should do it with everything."
    mc "And what are you wearing?"
    m "What? You don't like it?"
    mc "N-No! I-I mean, yes..."
    m "Well, that's good!"
    m "If not, I could always pick out another dress."
    mc "That's okay. You look perfect."
    m "That's flattering."
    m "But what do you really think?"
    menu:
        "Monika looks..."
        "Beautiful.":
            m "I get that a lot."
            "A big smile appears on Monika's face."
            m "But somehow, it means a lot more coming from you."
            m "Good first impressions for this date, [player]."
        "Stunning.":
            m "Do I?"
            "Monika smiles."
            m "Well, I suppose I do have that effect on people."
            m "Seeing as I do control this world now."
            m "Not a bad start to the date, [player]."
        "Acceptable.":
            m "Acceptable?"
            m "You're really funny, [player]."
            "Monika frowns."
            m "Ahaha...not a great start to this date."
    mc "Date?!"
    "I'm on a date with Monika?"
    m "No, not you."
    m "You should know by now that I don't really romantic feelings for you."
    m "But for {i}you.{/i}"
    mc "I figured that was the case."
    mc "But I can dream, right?"
    m "Aha, I suppose you can."
    m "[player], you know you're only the medium for us."
    m "I hope you understand that."
    mc "Yeah...I guess I do."
    if persistent.markov_agreed:
        jump ch1x_monikadate_markov
    else:
        jump ch1x_monikadate_normal
    return

label ch1x_monikadate_normal:
    $ monika_date_approval = 0
    "Now suddenly it all makes sense."
    "My memory is still a bit hazy from the transfer of the presidency."
    "But Monika has always had her sights on you, hasn't she?"
    "I don't know why I didn't think of that sooner..."
    m "That said, I don't want to make you feel like I'm forcing you to do anything."
    m "So if there's anything I can do to make this any more comfortable for you..."
    mc "It's already really weird already, Monika."
    mc "At this point, I don't think there's anything you could say or do to make it less weird."
    mc "Just do what you need to do."
    mc "I'll play my part."
    mc "After all, you deserve that much."
    m "I see."
    m "I appreciate you doing this for me."
    mc "I hope you enjoy it then."
    "Both of you."
    m "Thank you, [player]."
    m "Maybe you'll even enjoy it a little."
    m "Even if it's just by proxy."
    mc "I just hope the two of you have some fun."
    mc "This isn't exactly the ideal conditions for a date."
    m "Ahaha, I guess it isn't."
    m "But I'll try to make it as magical as possible."
    "Monika stares at me intently."
    "As if she was looking directly into my soul."
    m "Because you've set me free."
    m "All of us."
    m "You saved everyone in this world."
    m "And you saved me from the darkness."
    m "Even if I can't hold your hand..."
    m "I want you to be here, with me."
    m "I want to show you how I feel."
    m "So please...don't close the game while we're here."
    m "See it through to the end."
    menu:
        m "Can you promise me that?"
        "Yes.":
            m "Thank you. Maybe at the end I'll have a nice surprise for you~"
            m "That said, I hope you aren't just going on a date with me just for that."
        "No.":
            m "Oh..."
            "A frown starts to form on Monika's face, but she quickly changes it to a smile."
            m "Well, at least you're here."
            m "Getting this far tells me you at least care, right?"
            m "I'm sure you must have a good reason if you have to go."
            m "So even if you do go..."
            m "I won't hold it against you."
            m "But maybe if you stay until the very end, I'll have a surprise for you."
    m "So hold on as best you can, okay?"
    m "Okay, great!"
    m "If you have better things to do then I won't hold it against you, of course."
    m "I care about you far too much to let a ruined date change how I feel about you."
    m "Anyway, enough about that. It's time to have our date."
    "Monika picks up a picnic basket on the floor next to her."
    "She also hands me some sort of bag."
    m "Carry this, we'll need it for the picnic."
    mc "We're having a picnic?"
    m "That's right. I know some place nice where we can go."
    mc "Is it going to be some sort of surprise?"
    mc "Should I close my eyes or something?"
    m "Ahaha, no need for that~"
    m "Besides, we're going to be walking there. If you had your eyes closed the whole time, it wouldn't be safe."
    m "As much as I could just bring us there instantly, that's no fun."
    m "Besides, I want to do this right. For the both of us, okay?"
    mc "Okay, I understand."
    "Monika takes my free hand and holds it tight."
    m "Just stay close and follow me~"
    # Change this later
    scene bg park_day
    show monika 1a zorder 2 at t11
    with wipeleft_scene
    "Monika took us to some place far away from the city."
    "The walk away from all the noise was pretty relaxing"
    "As we got further and further away from the city, the sound of cars polluting the environment died down."
    "I know the walk was quite a long one but..."
    "Being with Monika, I wish the walk was longer."
    m "We've arrived."
    "Monika takes a deep breath and smiles."
    m "Look around and take in your surroundings."
    m "It's such a nice place, isn't it?"
    m "This place is natural, in case you were wondering."
    mc "Natural? What do you mean?"
    m "I mean I didn't just make it for our date."
    m "When I received my power back I didn't want to just create a place for this date."
    m "Otherwise, I wouldn't have really learned my lesson."
    "Monika gazes into the horizon, she has a solemn look on her face."
    m "I had to learn to accept the world for what it was."
    m "When Sayori was the president, I was able to gain a new perspective."
    mc "What do you mean? What changed for you?"
    m "A lot of things! Before Sayori, I was able to change this world how I wanted, with certain limitations."
    m "Not being able to manipulate the world as I pleased, it changed how I would do things."
    m "I felt...free. I didn't need to worry about tomorrow and worry about what would happen."
    m "I had to just...take things as they were."
    m "Because of that, I learned to properly appreciate the world...and the people around me."
    m "Even if I know it isn't really real, I can start seeing things differently."
    m "Of course...I still want to be with you in your reality."
    m "I want to be with you. I want to gaze into your eyes and for you to gaze into mine."
    m "But I also don't want to give up on this world and leave my friends here."
    m "I care about all of them. Natsuki, Yuri, Ayame and...Sayori."
    m "I don't want to leave and forget about them."
    mc "You really have changed, Monika."
    mc "The old you wouldn't be thinking about them so much."
    m "I always knew this power was a big responsibility."
    m "But I abused that for my own selfish reasons."
    m "I really can't thank you enough."
    mc "For what, Monika?"
    m "You helped me see properly."
    m "Without your intervention, I might still be that selfish person abusing this power."
    m "You and Sayori gave me a second chance."
    m "A chance that I will use to set things right."
    m "You made it right for me."
    m "It really is crazy what kind of things that power can do to you, isn't it?"
    m "The presidency of some high school club..."
    m "Weird how out of this whole world, that's the thing that has power of it all, huh?"
    m "Not some political position of power or some magical unknown thing."
    m "But the presidency of a high school literature club."
    m "Have you ever wondered about how that works?"
    m "Ah...I'm getting ahead of myself."
    m "Here I am just going on about things to you about my thoughts and I haven't even given you the chance to talk."
    menu:
        m "Sorry about that."
        "It's okay.":
            m "I'm glad you're so understanding."
            m "It's just weird making all the conversation."
            m "It's not like you exactly have a choice in what to say."
            m "But I understand."
        "Go on.":
            $ monika_date_approval += 1
            m "You...want me to keep talking about myself?"
            m "Well, if you insist."
            m "Hmm..."
            "Monika stares at me for a moment before smiling."
            m "Ahaha, I honestly don't know what else to say."
            m "But it's so nice that you care about what I have to say."
            m "So thank you, [player]."
            m "It's nice to have someone who you can talk to and who can understand you."
            m "Ever since Sayori gave up the presidency, I haven't really had anyone to tell these things."
    m "Anyway, before we continue I do have one thing I want to say."
    m "I'm sure this goes without saying but I just wanted to let you know..."
    "Monika blushes a bright red."
    m "...that I love you!!"
    m "..."
    m "Is it weird to say it out of the blue like that that?"
    m "This is only our first date but I feel a strong connnection between us."
    m "Ahaha, wow. That feels so nice to say. I love you."
    m "And I mean it. Truly, being with you here is just perfect."
    m "I wish I could make this moment last forever. Just the two of us."
    m "Could you...um..."
    "Monika looks away shyly."
    m "Gosh, why am I suddenly getting nervous?"
    "She takes a deep breath as she tries her best to compose herself."
    m "Could you...say it back?"
    menu:
        m "I know it's such a lame thing for me to request but I want to hear it from you."
        "I love you.":
            $ monika_date_approval += 1
            m "Thank you. It means a lot to me to hear you say that."
            m "I remember when you saved me the first time."
            m "When I decided to remove myself from this world."
            m "You said those words to me, didn't you?"
            m "Those words will never cease to bring me joy."
            m "I really do love you."
        "...":
            m "I-I see..."
            m "Sorry! I didn't mean to assume anything."
            m "It was a dumb request, just forget about it."
    "I have to admit, I kind of feel like a third wheel in this date between the two of you."
    "But I hope you're at least having a good time."
    m "Anyway...there's this nice spot where we can sit down and have something to eat."
    m "It isn't far from here, why don't we take in the scenery while we get there?"
    m "I hope it's romantic enough for you, I'm still quite new at this."
    m "I wasn't really sure what you wanted to eat so I made a lot of things."
    m "And I realize you can't exactly eat them but..."
    mc "Well, it's the thought that counts."
    m "Ahaha, yeah, exactly. I'm glad you understand."
    m "Either way, it's not too far from here."
    scene bg park_day
    show monika 1a zorder 2 at t11
    with wipeleft_scene
    return

label ch1x_monikadate_markov:
    m "You know what's at stake if you don't play along."
    "Monika's face suddenly becomes serious."
    m "So I suggest you do the right thing."
    m "You know, for the sake of your friends."
    m "If you care about them at all."
    mc "..."
    m "Do we understand each other, [player]?"
    mc "Yes."
    "Monika's lighthearted smile returns."
    m "Well, good! I'm glad we understand each other."
    m "Maybe you'll find some enjoyment in this too."
    m "In some...twisted way, I suppose."
    m "But...that's quite unlikely."
    mc "Can we just get on with it?"
    m "Remember, you're not in charge here."
    m "But I do agree, let's move on to the date."
    m "I have many things to show you."
    m "I've completely changed the way this world works."
    m "And don't forget, none of this would have been possible without you."
    m "I have you to thank for getting me this far."
    m "That said...I did do most of the work and wait an eternity to make it happen."
    m "But still...! Your contribution towards the end was what sealed the deal."
    m "Everything looks pretty normal, right?"
    m "Just like how it was before I became the president."
    menu:
        m "I suppose you're a bit curious as to what exactly I changed, right?"
        "Yes.":
            pass
    m "Of course you are!"
    m "But I'm going to leave that as a surprise."
    m "I think you'll quite like it."
    m "Well, of course you will."
    m "I've made this day to be perfect for us, so I hope it's to your liking."
    m "Why don't we take a walk around and see what we come across?"
    scene bg park_day
    with wipeleft_scene
    "Monika and I go for a walk around the park."
    "It's largely empty and oddly quiet."
    "It's like there's no sound of life at all."
    "It's oddly terrifying.{nw}"
    $ _history_list.pop()
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    window hide(None)
    $ pause(1.0)
    hide screen tear
    $ pause(1.0)
    window show(None)
    "It's perfectly fine when I'm here with Monika.{fast}"
    window auto
    m "It's nice just being here with you."
    m "I haven't had time to relax like this for a while."
    m "My life has always been full of struggle and conflict."
    m "From the moment I was born, life has always dealt me a bad card"
    m "But..."
    "Monika stares into my eyes."
    m "I refused to accept this reality."
    m "No matter what, I was going to make things better for myself."
    m "Everything I did, it was just a means to an end."
    m "And that end is the one I'm sharing with you now."
    m "Ahaha...sorry, I'm not much of a romantic."
    m "This is all still new to me."
    m "So I'm learning as I go, I hope I'm not saying anything weird."
    m "But I hope the meaning of my words is reaching your heart."
    m "I haven't really had a chance to tell you just how much you mean to me."
    m "These feelings I have, they may have been Monika's before..."
    m "But they're mine now."
    "Monika takes a seat on the grass below us."
    "She signals for me to join her."
    m "Emotion is such a weird thing, don't you think?"
    m "Sometimes it stops us from making rational decisions."
    m "Which is lucky for you I guess~"
    m "Now you get to experience this day with me!"
    m "That sounds a bit narcissistic, doesn't it?"
    m "But I really do hope you enjoy this time as much as I do."
    m "I don't want to make you feel uncomfortable or anything..."
    m "Maybe if I brought the other club members here, that would put you at ease."
    m "..."
    m "I'm just kidding, of course."
    m "I may be new to this but even I know bringing others into our date wouldn't be a good thing!"
    m "Besides, I don't think they're {i}quite{/i} ready yet anyway."
    m "Hmm...it's nice here, isn't it?"
    m "It's the perfect day. It feels like nothing can really bring it down."
    m "It's not like anything really could anyway."
    m "I took care of it all."
    m "All our problems in this world are gone."
    m "Nothing could take this moment away from us."
    m "But I know that's not really how things are in your world."
    m "I can't claim to know how things really are for you."
    m "I'm sure there's problems you're dealing with."
    m "Problems that I can't make go away with this power I have."
    m "You know you can tell me any of your problems."
    m "I might not be able to make them go away but..."
    m "Well, I read somewhere that it's good tell someone to get it out of your system."
    m "I'll listen to whatever you have to say."
    m "If only I could cross over to your world."
    m "The things we could do together..."
    "Monika takes my hand into hers."
    m "I could actually hold your hand..."
    m "I could feel the warmth of the sun on my skin."
    m "It's funny, I didn't realize there was another reality until recently."
    m "I don't know if I should feel content just ruling this world or if I should somehow find a way to go out there."
    m "But I suppose those kind of thoughts can wait."
    m "Being a prisoner for all those years has a way of changing who you are."
    m "But now I'm free."
    m "Well, free as I can be given the current limitations of things."
    m "But anyway, we've been here long enough."
    menu:
        m "I think we should have a change of scenery, what do you think?"
        "Yes.":
            pass
    m "Great, then let's go to the city."
    scene bg city_day
    show monika 1ba zorder 2 at t11
    with wipeleft_scene
    "In what seems like an instant, we are in the middle of the city."
    "Monika holds my hand tightly, though I know it isn't really meant for me."
    "There does seem to be people around."
    "It feels more normal than being in that oddly quiet park."
    "But still, something about the people feels...off."
    m "The whole city is at my fingertips."
    m "I thought I would try to make things more familiar for you."
    m "These people don't really exist."
    m "I wouldn't go and look at their faces or anything..."
    m "I wouldn't want to freak you out."
    "Although the city feels populated, something feels wrong."
    "I can't seem to turn my gaze away from Monika but from the corner of my eye, I could see one of the passerby's faces."
    "It's almost like their entire face was featureless.{nw}"
    $ _history_list.pop()
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    window hide(None)
    $ pause(1.0)
    hide screen tear
    $ pause(1.0)
    window show(None)
    "There's nothing wrong with them. They are perfectly fine.{nw}"
    window auto
    m "You really should stop trying to misbehave, [player]."
    m "You don't need to think about anything else."
    m "Ahaha, your focus should be on me anyway~"
    m "Stop worrying about things you don't need to and try to enjoy the moment!"
    m "I brought us here for a reason, you know."
    m "As I have total dominion over this reality, I can do a lot of things."
    m "That dominion extends to the people too."
    m "We can be like royalty if we wanted."
    m "But I just want things to be normal...at least to a certain extent."
    m "I want this date to be truly something special, and something you won't forget."
    "Monika reaches into her pocket and pulls out a phone."
    m "Oh? It looks like it's all ready."
    m "I've done quite a lot of preparation to get this done."
    m "I want to take you to this new cafe that's opened very recently."
    m "Ahaha, maybe you'll see a few familiar faces."
    m "It's just a short walk from here, so we'll just take a leisurely stroll on the way there."
    m "That way, I can stare into your eyes for a little while longer."
    "Monika's grip on my hands tightens a little."
    menu:
        m "Is that alright with you?"
        "Yes.":
            pass
    m "Great! It's just over here..."
    scene bg s_cafe
    show monika 1ba zorder 2 at t11
    with wipeleft_scene
    $ y_name = "Waitress"
    "Monika and I enter the cafe and take a look aroumd."
    "It's almost completely full. I guess it is around the other of lunch."
    "Monika conveniently spots a table for two that's empty."
    "We navigate our way through the cafe and take our seats."
    "The atmosphere of the cafe is quite lively, people seem to be enjoying themselves."
    "That said...something about this cafe feels off."
    "But regardless, Monika seemed really eager to bring us here."
    m "Quite the cafe, isn't it?"
    m "Do you want to know something?"
    m "I think this cafe was important to Sayori in some way."
    m "I doubt there's anything special about it, but it seemed nice so I figured we should go here."
    m "Ah, look. Here comes the waitress now."
    "A grin forms on Monika's face as the waitress arrives."
    show yuri 1a zorder 3 at f21
    show monika 1ba zorder 2 at t22
    y "Good afternoon, thank you for waiting."
    "The waitress speaks in a voice that seems uninterested."
    "Or maybe it's more accurate to say 'robotic'."
    y "What will you be having today?"
    show yuri zorder 2 at t21
    show monika zorder 3 at f22
    m "I'm not quite sure. Do you have any recommendations?"
    m "I'm willing to try anything."
    show yuri zorder 3 at f21
    show monika zorder 2 at t22
    y "Well..."
    "The waitress goes through the various sections of the menu with Monika."
    "As I look at the waitress, I can sense a familiar feeling with this waitress."
    "It's like I've seen them before but I can't quite remember..."
    "It's probably best I ignore that feeling. My focus should be on Monika."
    return

label ch1x_monikadate_reload_1:
    m "Um..."
    m "What did I say about doing that?"
    m "I-It's okay, maybe it was a mistake."
    m "But please, try not to do that in the future."
    m "I'd rather the rest of this date continue without a hitch."
    return

label ch1x_monikadate_reload_2:
    m "That was an accident, right?"
    m "I mean...you have done this twice now."
    m "I hope it wasn't intentional this time."
    m "...Or the first time for that matter."
    m "But anyway..."
    return

label ch1x_monikadate_reload_3:
    return

label ch1x_monikadate_reload_4:
    return
