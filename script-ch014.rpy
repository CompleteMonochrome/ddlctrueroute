label ch14_main:
    $ s_name = "???"
    $ currentpos = 0
    if persistent.markov_agreed and not ch12_markov_agree:
        play music mendglitch
        s "Ahaha."
        s "Did you think you could escape it because you switched saves?"
        s "It's already set in stone, like I said."
        s "But..."
        s "I suppose I should let her speak."
        s "She'd be suspicious otherwise."
        s "And I can't let suspicion ruin my--"
        s "{i}Our{/i} plans."
        
        $ currentpos = get_pos()
    elif ch12_markov_agree:
        play music mendglitch
        $ currentpos = get_pos()
    $ s_name = "Sayori"
    $ audio.mendcont = "<from " + str(currentpos) + " loop 6.424>bgm/monika-end.ogg"
    play music mendcont
    return

label ch14_end:
    return
