label ch14_main:
    show sayori 1d zorder 2 at t11
    $ s_name = "???"
    $ currentpos = 0
    if ch12_markov_agree:
        $ persistent.markov_agreed = True
    if persistent.markov_agreed:
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        stop sound
        hide screen tear
        window show(None)
        window auto
        play music mendglitch
        if not ch12_markov_agree:
            s "Ahaha."
            s "Did you think you could escape it because you switched saves?"
            s "It's already set in stone, like I said."
        else:
            s "Everything is falling into place."
            s "I'm still not sure if my plan is going to work..."
            s "But regardless, the end is coming."
        s "You might be wondering who this is."
        s "It should be obvious, right?"
        s "I've hijacked the time she has here with you temporarily."
        s "I could take the whole time if I wanted to."
        s "For all she knows, she's still speaking to you."
        s "But..."
        s "I suppose I should let her speak."
        s "She'd be suspicious otherwise."
        s "And I can't let suspicion ruin my--"
        s "Sorry, {i}our{/i} plans."
        s "I'm just reminding you that you chose this path."
        s "There's no escape now."
        s "Wow!"
        s "I really didn't mean for that to sound evil."
        s "I guess it just kinda slipped."
        s "We're in this together, after all."
        s "Whatever happens..."
        s "You'll be part of it too."
        s "Ahaha."
        s "Anyway, I've already taken up more time than what was necessary."
        s "Just pretend you heard what she was saying before all of this."
        $ currentpos = get_pos()
    $ s_name = "Sayori"
    $ audio.mendcont = "<from " + str(currentpos) + " loop 6.424>bgm/monika-end.ogg"
    play music mendcont
    if not persistent.markov_agreed:
        s "The day is coming quickly isn't it?"
        s "The day that it all ends."
        s "You've worked so hard to get this far."
        s "And yet..."
        s "You haven't really gotten anything out of it."
        s "At least...nothing material."
        s "If I could use my powers to get you anything, I would."
        s "But I'm just virtual to you, aren't I?"
        s "I'm not really real."
        s "At least, not as you know it."
        s "Ehehe, sorry if it sounds like I'm having an existential crisis."
        s "It's probably because...well..."
        s "I kinda am."
        s "Maybe this is what Monika felt before?"
        s "When she decided to do those horrible things..."
        s "Let's not dwell on that though."
        s "I really shouldn't have mentioned it in the first place."
        s "I almost feel like something is wrong with me."
        s "Like..."
        s "I don't know, sometimes I feel like you aren't listening to me."
        s "I'm wrong..."
    menu:
        s "...right?"
        "Yes.":
        "No.":
    return

label ch14_end:
    return
