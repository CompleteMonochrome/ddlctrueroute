# This happens after the main story
# Possibly will release as an individual option in custom start if I can't
# finish the story in a decent amount of time
label ch1x_monikadate:
    scene bg class_day
    play music t1
    show monika 1a zorder 2 at t11
    "I can feel my heart pounding against my chest."
    "I'm not sure I processed those words correctly."
    "She couldn't have possibly said what she just said, could she?"
    "It's a dumb question, but I have to ask her."
    mc "A date?"
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
            m "Thank you. Maybe at the end I'll have a nice surprise for you."
        "No.":
            m "Oh..."
            "A frown starts to form on Monika's face, but she quickly changes it to a smile."
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
