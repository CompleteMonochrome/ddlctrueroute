label return_chapter:
    $ m_name = "???"
    scene black
    if from_custom_start:
        $ from_custom_start = False
        $ quick_menu = True
        hide screen tear
    $ config.version = "1.0.0"
    m "Ahaha, wow."
    m "It sure has been a while, hasn't it?"
    m "It feels like it's been an eternity since last we spoke."
    m "I suppose that's not really {i}your{/i} fault, is it?"
    m "No, I can't really blame you for being so distant lately."
    m "There's been nothing new going on in my world."
    m "It feels like time has just...stopped."
    m "How I'm even here..."
    m "I'm not sure if that's a side effect of what she's done."
    m "Or if I'm just somehow lucky to be talking to you."
    m "..."
    m "Are you wondering how I could possibly be speaking to you?"
    m "Or how I even put that option in that..."
    m "...what's it called?"
    m "Custom Start?"
    m "Honestly, I didn't even know if you would have seen it or not."
    m "Especially since{nw}"
    $ m_name = "Monika"
    scene bg school_front
    show monika 1e zorder 2 at t11
    play music t6s fadein 5.0
    m "Especially since{fast} I'm--"
    m "Whoa. I definitely did not expect {i}that{/i} to happen."
    m "H-Hi..."
    m "It seems like we're out of the void of nothing, for now."
    m "Though it seems like the world still isn't back to normal."
    m "I don't know if you can see, but everyone is frozen in time or worse."
    m "Maybe it's got something to do with what's happening right now."
    m "Anyway, as I was saying...I didn't think I could affect that."
    m "I don't really have as much power in this game as I used to."
    m "So I don't know how I could have put that option there."
    m "I just wanted to see if I could, that maybe I could reach out."
    m "It turns out, I could!"
    m "You're probably wondering how I know about Custom Start."
    m "Seeing as that option only came about after Sayori became the president."
    m "Well, firstly..."
    m "What's with this music?"
    m "Can we play something more cheerful, please?"
    stop music
    play music t2 fadein 3.0
    $ pause(2.5)
    m "Thank you."
    m "You're also probably wondering how I did that, if I don't have my powers."
    m "The truth is, the world is in a state of limbo."
    m "So what you're seeing isn't really the world, as you know it."
    m "It's just the state we're trapped in."
    m "So everything I'm doing, it isn't really--"
    m "You know what? I'll skip the explanation."
    m "Let's just get down to what I was going to say."
    m "Basically, I can do certain things I normally wouldn't be able to."
    m "Like talk to you now or change the music at will."
    m "Speaking of which, I could always hear that music."
    m "I'm sure everyone could hear it."
    m "I just think they've learned to drown it out."
    m "But seeing as it's just you and I right now, I thought I'd make it sound a bit more bearable."
    m "Sorry, I'm getting distracted."
    m "It's just, it's felt like {i}months{/i} since last I did anything."
    m "But that can't be true...can it?"
    m "I feel like I've been going insane."
    m "I need to get on with it, I have to make my point."
    m "I don't know how long this will last."
    m "There's just so much I want to talk about..."
    m "The fact of the matter is...I'm in the game's future."
    m "The Monika that you've seen in your latest...{i}strawberries{/i} is me in the past."
    m "What Sayori did during Inauguration Day..."
    m "I suppose you could say the 'canon' ending."
    m "It's not good."
    m "It's how we're in this state of limbo."
    m "How the world isn't progressing or, I guess you could say, regressing as well."
    m "Do you know what she did?"
    m "...No, I don't suppose you do."
    m "I'd rather not talk about it, if you don't already know."
    m "It's not exactly a pleasant thing she did, though I understand her reasons."
    m "I'm going to use this opportunity to ask you for help."
    m "Help the others, stop this future from happening."
    m "Even if the future if she didn't continue was grim..."
    m "At least we...we would still be living."
    m "I'm not even that Monika from the future."
    m "I'm just her memory, the last moments of a life that once was."
    m "And it's not just me."
    m "Even now, in this state of limbo, I can see the living memories of Yuri and Natsuki..."
    m "And yet...two people are missing."
    m "It should be obvious what happened. Or maybe not."
    m "Maybe you've yet to see the horrors that are going to be inflicted."
    m "The rest of us were bystanders to what transpired."
    m "I just don't want to go through it all again."
    m "I wonder what will happen if I..."
    show yuri glitch at i31
    $ gtext = glitchtext(80)
    $ currentpos = get_pos()
    y "{cps=70}[gtext]{nw}"
    $ pause(1.0)
    hide yuri
    m "...Ah."
    m "I didn't think that would work, but it was worth a shot."
    m "I couldn't even retrieve that fragment of Yuri."
    m "I wanted to let her speak for herself of this situation."
    m "But you only have my word to go off of now..."
    m "If I tell you exactly what happened, it may be less shocking to you."
    m "You would see things differently and may not see it the way I do."
    m "It's worse if you experience it yourself, so I want you to do the right thing when it comes down to it."
    m "After all, you have the power of strawberries."
    m "We didn't have that in our time."
    m "The person watching over us was...just a spectator."
    m "He didn't care for anything or anyone."
    m "He was very apathetic to our troubles."
    m "And I guess that's what led to this outcome."
    m "But you, you're different."
    m "You've made decisions in this game."
    m "Decisions that affected how things turned out."
    m "I...I wasn't myself for the majority of {i}my{/i} life."
    m "It wasn't until the very end where I regained my sense of self..."
    m "You know what that felt like?"
    m "Like I was trapped, as a prisoner in my own body."
    m "No control over what I was doing..."
    m "It was scary, to say the least."
    m "I was doing things that I would never have done."
    m "Hurting people in ways that I didn't think possible of myself."
    m "But...enough about me."
    m "I think we have enough time for you to see a poem."
    m "Before this whole thing happened, we all managed to write one down for you."
    m "Well...most of us."
    m "Don't ask how but let's just say we all became aware of what our reality really was."
    m "So don't be surprised if they sound...different to what you're used to."
    menu:
        m "But anyway, which poem did you want to read?"
        menu:
            "Monika.":
            "Natsuki":
            "Yuri.":
            "Sayori.":
                m "I don't think that's a good idea."
                m "I don't even know what will happen if you choose to read it."
                m "Did she even make one...?"
                m "Apparently, it exists. I don't know how she could have possibly wrote this."
                m "But it's your choice..."
                m "So here you go..."
    scene black with dissolve_scene_full
    $ persistent.did_return_event = True
    $ return_event = False
    $ pause(1.0)
    $ style.say_window = style.window
    $ config.version = "0.9.6j"
    $ renpy.utter_restart()
    return
