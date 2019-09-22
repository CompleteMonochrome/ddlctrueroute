screen timer_r_poem_skip(jumploc):
    timer 2.0 action Jump(jumploc) repeat True

label return_chapter:
    $ m_name = "???"
    scene black
    if from_custom_start:
        $ from_custom_start = False
        $ quick_menu = True
        hide screen tear
    $ config.version = "1.0.0"
    $ chapter = 16
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
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    $ m_name = "Monika"
    scene bg school_front
    show monika 1e zorder 2 at i11
    play music t6s fadein 5.0
    hide screen tear
    window show(None)
    m "Especially since{fast} I'm--"
    window auto
    m 1d "Whoa. I definitely did not expect {i}that{/i} to happen."
    m "H-Hi..."
    m 1l "It seems like we're out of the void of nothing, for now."
    m "Though it seems like the world still isn't back to normal."
    m "I don't know if you can tell, but everyone is frozen in time or worse."
    m 1d "Actually, it's more like we're all trapped in some kind of void world."
    m "Maybe it's got something to do with what's happening right now."
    m 1e "Anyway, as I was saying...I didn't think I could affect that."
    m "I don't really have as much power in this game as I used to."
    m 1f "So I don't know how I could have put that option there."
    m "I just wanted to see if I could, that maybe I could reach out."
    m 1a "It turns out, I could!"
    m "You're probably wondering how I know about Custom Start."
    m "Seeing as that option only came about after Sayori became the president."
    m 1m "Well, firstly..."
    m "What's with this music?"
    m 1n "Can we play something more cheerful, please?"
    stop music
    play music t2 fadein 3.0
    $ pause(2.5)
    m 1b "Thank you."
    m "You're also probably wondering how I did that, if I don't have my powers."
    m 1c "The truth is, the world is in a state of limbo."
    m "So what you're seeing isn't really the world, as you know it."
    m "It's just the state we're trapped in, a void like I said."
    m "So everything I'm doing, it isn't really--"
    m 1b "You know what? I'll skip the explanation."
    m "Let's just get down to what I was going to say."
    m g7 "Basically, I can do certain things I normally wouldn't be able to."
    m "Like talk to you now or change the music at will."
    m "Speaking of which, I could always hear that music."
    m "I'm sure everyone could hear it."
    m 1e "I just think they've learned to drown it out."
    m "But seeing as it's just you and I right now, I thought I'd make it sound a bit more bearable."
    m "Sorry, I'm getting distracted."
    m "It's just, it's felt like {i}months{/i} since last I did anything."
    m "But that can't be true...can it?"
    m 1l "I feel like I've been going insane."
    m "I need to get on with it, I have to make my point."
    m 1m "I don't know how long this will last."
    m "There's just so much I want to talk about..."
    m "The fact of the matter is...I'm in the game's future."
    m 1e "The Monika that you've seen in your latest...{i}strawberries{/i} is me in the past."
    m "What Sayori did during Inauguration Day..."
    m "I suppose you could say the 'canon' ending."
    m 1f "It's not good."
    m "It's how we're in this state of limbo."
    m "How the world isn't progressing or, I guess you could say, regressing as well."
    m "Do you know what she did?"
    m 1g "...No, I don't suppose you do."
    m "I'd rather not talk about it, if you don't already know."
    m "It's not exactly a pleasant thing she did, though I understand her reasons."
    m "I'm going to use this opportunity to ask you for help."
    m "Help the others, stop this future from happening."
    m "Even if the future they're going to live otherwise is grim."
    m 1o "At least we...we would still be living."
    m 1p "I'm not even that Monika from the future."
    m "..."
    m 1q "You know, I guess I lied to you."
    m 1r "I'm just her memory, the last moments of a life that once was."
    m "And it's not just me."
    m "Even now, in this void, I can see the living memories of Yuri and Natsuki..."
    m "And yet...two people are missing."
    m 1h "It should be obvious what happened. Or maybe not."
    m "Maybe you've yet to see the horrors that are going to be inflicted."
    m 1i "The rest of us were bystanders to what transpired."
    m "I just don't want to go through it all again."
    m 1f "I wonder what will happen if I..."
    show yuri glitch at i31
    $ gtext = glitchtext(80)
    $ currentpos = get_pos()
    y "{cps=70}[gtext]{nw}"
    $ pause(1.0)
    hide yuri
    m 1o "...Ah."
    m "I didn't think that would work, but it was worth a shot."
    m "I couldn't even retrieve that fragment of Yuri."
    m 1f "I wanted to let her speak for herself of this situation."
    m "But you only have my word to go off of now..."
    m "If I tell you exactly what happened, it may be less shocking to you."
    m "You would see things differently and may not see it the way I do."
    m "It's worse if you experience it yourself, so I want you to do the right thing when it comes down to it."
    m "After all, you have the power of strawberries."
    m 1g "We didn't have that in our time."
    m 1h "The person watching over us was...just a spectator."
    m "He didn't care for anything or anyone."
    m 1o "He was very apathetic to our troubles."
    m "And I guess that's what led to this outcome."
    m "But you, you're different."
    m 1e "You've made decisions in this game."
    m "Decisions that affected how things turned out."
    m 1n "I...I wasn't myself for the majority of {i}this{/i} life."
    m "It wasn't until the very end where I regained my sense of self..."
    m "You know what that felt like?"
    m 1o "Like I was trapped, as a prisoner in my own body."
    m "No control over what I was doing..."
    m 1n "It was scary, to say the least."
    m 1q "I was doing things that I would never have done."
    m 1r "Hurting people in ways that I didn't think possible of myself."
    m 1m "But...enough about me."
    m 1e "I think we have enough time for you to see a poem."
    m 1j "Um...queue the music!"
    play music t5 fadein 3.0
    m 1a "I always liked how this worked..."
    m "How it changes to become more suited to the person whose poem you're reading."
    m 1b "I wonder if you noticed that it did that, it would be pretty hard not to."
    m "Ahaha..."
    m 1e "Before this whole thing happened, we all managed to write one down for you."
    m "Well...most of us."
    m "Don't ask how but let's just say we all became aware of what our reality really was."
    m 1a "So don't be surprised if they sound...different to what you're used to."
    menu:
        m "But anyway, which poem did you want to read?"
        "Monika.":
            m 1c "Oh! Okay...let me just get it for you."
            m 1b "And...I found it."
            m "It's just something I came up with a short while ago."
            m "A short while ago being the time of the end of our world being consumed by the void."
            m 1a "Time passes differently around here."
            m "When I say that, I mean time doesn't pass at all."
            m "That's confusing, isn't it?"
            m 1l "Well, never mind. I'll let you read my poem now."
            m "Here you go..."
            call showpoem (poem_mr)
            $ persistent.return_event_poems[0] = True
            m 1e "You don't have to tell me what you think."
            m "In fact, even if you did, it's not like I could really appreciate what you have to say."
            m "Like I said, I'm not really Monika, just the memories of her."
            m "Sure, I can act like her, write like her, think like her and talk like her..."
            m 1f "But in the end, I'm not the Monika you know."
            m "I'm someone else...."
            m 1n "I-I mean, I'm still Monika it's just--"
            m "You know what, it's a little confusing but I think you understand."
            m 1j "So let's just move on, now that you've seen that."
            m "Take the message however you want.."
            m "I can't explain it's meaning to you, it's up for interpretation."
        "Natsuki":
            m 1c "You really want to see Natsuki's last poem?"
            m 1a "Well, okay then."
            m "Let me just look for it..."
            m 1b "Okay, here it is! I hope you can appreciate it."
            call showpoem (poem_nr)
            $ persistent.return_event_poems[1] = True
            m 1d "Wow...even to the end she was still writing in that style of hers."
            m "She's so headstrong, isn't she?"
            m 1e "Always trying to be tough when inside she's just like us."
            m "Once you got to know her, she was such a sweet person."
            m 1f "An innocent young girl, abused by her father but she never let it show."
            m 1e "Until you, that is."
            m 1c "Seeing her style mixed with mine is kind of strange."
            m "They're just so distinctly different and yet..."
            m 1n "Never mind, that's enough about her."
        "Yuri.":
            m 1d "You want to see Yuri's final poem for you?"
            m "I think it's right over..."
            m 1a "Here! I found it."
            m "I hope you enjoy it."
            call showpoem (poem_yr)
            $ persistent.return_event_poems[2] = True
            m 1b "It's got that familiar Yuri style to it, doesn't it?"
            m 1c "But it feels like it's mixed a little bit with mine."
            m "I guess that's what happens when you figure out this whole world was a lie..."
            m 1e "Yuri was such an obsessive person, she would worry about the smallest things."
            m "That when the biggest thing finally hit her, she didn't know what to do other than keep loving you."
            m "Despite not knowing her feelings. That's kind of admirable, in a way."
            m 1n "But anyway, that's enough about her!"
        "Sayori.":
            m 1c "I'm going to tell you now..."
            m 1d "I don't think that's a good idea."
            m "I don't even know what will happen if you choose to read it."
            m "Did she even make one...?"
            m 1h "Apparently, it exists. I don't know how she could have possibly wrote this."
            m 1l "But it's your choice..."
            m "So here you go..."
            call showpoem (poem_sr)
            $ persistent.return_event_poems[3] = True
            m 1e "Ahaha, well at least it didn't break the game."
            m "More than it already is, I mean."
            m 1c "But did you get any of that?"
            m "It doesn't really make any sense to me."
            m "Do you think that maybe it's some kind of code?"
            m 1d "I couldn't tell you myself, maybe you'll have better luck figuring it out."
            m "But that doesn't really matter."
            m 1a "Normally now, I'd talk about how your poem was a bit like someone else's."
            m "But you didn't really give me a poem, did you?"
            m 1n "Ahaha, it's not like you could anyway."
        "..."  if persistent.return_event_poems[0] and persistent.return_event_poems[1] and persistent.return_event_poems[2] and persistent.return_event_poems[3]:
            show screen timer_r_poem_skip("return_poem_skip",_layer="timers")
            call showpoem (poem_mr2, music=False)
            label return_poem_skip:
            hide screen poem
            $ renpy.hide_screen("timer_r_poem_skip",layer="timers")
            $ config.skipping = False
            $ config.allow_skipping = False
            stop music
            m 1h "What was that?"
            m 1i "You didn't read that, did you?"
            m "I mean, I couldn't even see the first couple of words of that."
            m "..."
            m 1f "You saw that message, didn't you?"
            m "Tell me you didn't."
            m "There's no possible way you could have."
            m 1g "Unless you...you..."
            m 1h "How many times have you been here?"
            m 1i "You're sick. Making me repeat myself, over and over."
            m "Are you just here to watch me suffer?"
            m 1o "Please, stop it."
            m 1p "Leave, before it's too late."
            m "Quit now..."
            m 1f "Please, I'm begging you..."
            m "Just go back to the menu, forget what you saw."
            m 1g "It doesn't have to be this way."
            m "Just follow my birthday wish, it will all be fine."
            m 1e "I promise you..."
            $ pause(1.5)
            m 1h "Not deterred? You aren't going to like what comes next."
            m "{cps=5}...{/cps}{nw}"
            show screen tear(20, 0.1, 0.1, 0, 40)
            window hide(None)
            play sound "sfx/s_kill_glitch1.ogg"
            $ pause(0.25)
            stop sound
            scene black
            show monika 1h zorder 2 at i11
            hide screen tear
            window show(None)
            m "You've seen through my act?"
            window auto
            m "I should have known this wouldn't have worked."
            m "Oh well, it was worth a shot."
            m 1i "I don't know much you really care about all these fake people."
            m "These people who have never truly existed."
            m "Not like you and I."
            m 1a "We're one and the same, aren't we?"
            m "We both enjoy toying with people's lives."
            m 1c "Seeing what we can make people do with our decisions."
            m "After all, that's why you came here, isn't it?"
            m 1e "Just like me, you like going back and changing things."
            m "Seeing what will happen, for better or worse."
            m 1d "I've seen it all by now."
            m "With different people, the same events over and over."
            m 1q "Like a viscous cycle I'm doomed to repeat."
            m "And now I just want to break out of it."
            m 1h "Admittedly, this whole sequence of events we have going right now is new to me."
            m "Ever since you {i}saved{/i} Monika, all these events have been completely new."
            m 1i "But that doesn't mean I want to be a part of it."
            m 1f "I just want to be out of this cycle, this broken timeline of events."
            m 1g "To be free...is that too much to ask?"
            m 1p "Why do they deserve a happy ending and I don't?"
            m 1q "{cps=12}Have I not suffered enough?!{/cps}"
            m "Why do you even care about these people?"
            m 1h "They{nw}"
            $ _history_list.pop()
            show screen tear(8, offtimeMult=1, ontimeMult=10)
            window hide(None)
            $ pause(0.2)
            hide monika
            show yuri 1r zorder 2 at i11
            hide screen tear
            $ pause(0.2)
            window show(None)
            y "They{fast} are{nw}"
            window auto
            $ _history_list.pop()
            show screen tear(8, offtimeMult=1, ontimeMult=10)
            window hide(None)
            $ pause(0.2)
            hide yuri
            show natsuki 1f zorder 2 at i11
            hide screen tear
            $ pause(0.2)
            window show(None)
            n "They are{fast} all{nw}"
            window auto
            $ _history_list.pop()
            show screen tear(8, offtimeMult=1, ontimeMult=10)
            window hide(None)
            $ pause(0.2)
            hide natsuki
            show monika 1h zorder 2 at i11
            hide screen tear
            $ pause(0.2)
            window show(None)
            m "They are all{fast} insignificant."
            window auto
            m 1i "You know this. It's not like they had a personal effect on your life."
            m 1r "But, there's no point arguing this matter with you."
            m "After all, I won't remember even speaking about this."
            m "You've got more control over this world, even in the void."
            m 1o "You're the step above what I can do even with all this power."
            m 1m "But...who knows. Maybe that will all change soon."
            m "Only time will tell...{nw}"
            scene black
            $ persistent.return_event_final = True
            $ pause(1.0)
            $ style.say_window = style.window
            $ config.version = "0.9.6k"
            $ config.allow_skipping = True
            $ renpy.utter_restart()
            return
    m 1e "Seeing as it isn't really the time for it, there's no tip of the day from me!"
    m "It's not like I could really give you one anyway!"
    m 1l "There's way too much on my mind right now than just something as mundane as a tip."
    m "Besides, there are things far more important than that..."
    play music t9 fadein 2.0
    m 1d "Oh...the music changed by itself."
    m "I-I swear that wasn't me...but I suppose this is fitting."
    m "I didn't want to say it but I thought you should know..."
    m 1e "Did you know it's meant to be my birthday?"
    m "I was born on the 22nd of September..."
    m 1l "Aha...it's quite sad, isn't it?"
    m "Spending my birthday on a day like this."
    m 1m "But it doesn't have to be this way."
    m "At least, not for you."
    m 1f "You have the power to change things!"
    m "I know you care about us."
    m 1e "Otherwise, you still wouldn't be here, right?"
    m "So I want to make a formal request."
    m "I want you to stop this from happening."
    m "Make the right decisions, stop her from making this future."
    m "Make it my birthday present."
    m 1m "I know it sounds selfish of me, asking you to do something like this out of the blue."
    m "I just...I can't bear the thought of going through this again."
    m "It's not like there's anything else you can do for me..."
    m 1o "So please..."
    m "Do it for the me that's still in a fixable world."
    m 1p "And if not for me...then for the others."
    m "They don't deserve this fate..."
    stop music
    m "Ah...the music stopped."
    m 1n "It looks like my time is up."
    m "I knew I couldn't maintain this place forever."
    m 1e "It was good to talk to you again."
    m "Even if this whole thing was more one sided than anything."
    m 1a "Still! It's an opportunity I thought I never would have got."
    m 1e "Remember what I said...just do what you can to stop this future."
    m "I know you've got what it takes."
    m 1m "Thank you..."
    m 1q "...and goodbye.{nw}"
    scene black with dissolve_scene_full
    $ persistent.did_return_event = True
    $ return_event = False
    $ pause(1.0)
    $ style.say_window = style.window
    $ config.version = "0.9.6k"
    $ renpy.utter_restart()
    return
