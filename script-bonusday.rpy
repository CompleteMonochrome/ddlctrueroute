label choose_bonus_day:
    $ quick_menu = False
    play music mend fadeout 1.5
    # Check player gender after input
    if persistent.player_pronouns == 1:
        call female_pronouns
    elif persistent.player_pronouns == 2:
        call nonbinary_pronouns
    menu:
        "Choose Type."
        "Special Days":
            jump special_day
        "New Timelines" if persistent.any_bonus_day:
            jump new_timelines


label special_day:
    "Warning: These days were meant to be played during a certain time period."
    "Some of the events that happen may not make sense when played outside their time period."
    menu:
        "Choose Special Day"
        "First Christmas Event." if persistent.arc_clear[0] == True:
            show screen tear(20, 0.1, 0.1, 0, 40)
            $ pause(0.25)
            $ christmas_chapter = True
            $ s_name = "Sayori"
            stop music
            $ renpy.save_persistent()
            stop sound
            jump christmas_chapter
        "Second Christmas Event." if persistent.arc_clear[0] == True:
            show screen tear(20, 0.1, 0.1, 0, 40)
            $ pause(0.25)
            $ christmas_chapter = True
            $ s_name = "Sayori"
            stop music
            $ renpy.save_persistent()
            stop sound
            jump christmas2_chapter
        "Special Day." if persistent.arc_clear[0] == True:
            show screen tear(20, 0.1, 0.1, 0, 40)
            $ pause(0.25)
            $ christmas_chapter = True
            $ s_name = "Sayori"
            stop music
            $ renpy.save_persistent()
            stop sound
            jump special_chapter
        "Return Day" if persistent.arc_clear[1] == True:
            show screen tear(20, 0.1, 0.1, 0, 40)
            $ pause(0.25)
            $ christmas_chapter = True
            $ s_name = "Sayori"
            stop music
            $ renpy.save_persistent()
            stop sound
            jump return_chapter

label new_timelines:
    $ bonus_chapter_active
    $ s_name = "???"
    s "Huh...where am I?"
    s "...New timelines?"
    s "Just how much do you know about our world?"
    s "On second though, I don't want to know."
    s "Just make your choice. I don't want anything to do with this."
    s "And even if I did, I don't seem to have any control..."
    menu:
        "Who is the president?"
        "Sayori." if persistent.true_sayori_bonus:
            $ bonus_chapter = 0
            jump ch_sayori_bonus
        "Monika." if persistent.true_monika_bonus or persistent.love_markov_bonus:
            if persistent.true_monika_bonus and persistent.love_markov_bonus:
                menu:
                    "With the book's influence?"
                    "Yes.":
                        $ bonus_chapter = 1
                        jump ch_monika_bonus
                    "No.":
                        $ bonus_chapter = 2
                        jump ch_markov_bonus
            elif persistent.true_monika_bonus:
                $ bonus_chapter = 1
                $ s_name = "Sayori"
                jump ch_monika_bonus
            else:
                $ bonus_chapter = 2
                $ s_name = "Sayori"
                jump ch_markov_bonus
        "Ayame." if persistent.ayame_bonus:
            $ bonus_chapter = 3
            $ s_name = "???"
            jump ch_ayame_bonus
        "[player]" if persistent.ayame_bonus:
            $ bonus_chapter = 4
            $ s_name = "???"
            jump ch_mc_bonus
        "..." if persistent.bonus_days_completed[0] and persistent.bonus_days_completed[1] and persistent.bonus_days_completed[2] and persistent.bonus_days_completed[3] and persistent.bonus_days_completed[4]:
            $ bonus_chapter = 5
            jump ch_finale
    return