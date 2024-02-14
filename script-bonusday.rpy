label choose_bonus_day:
    scene black
    # Disable menu as player chooses options
    $ quick_menu = False
    $ from_custom_start = True
    play music mend fadeout 1.5
    # Check player gender after input
    if persistent.player_pronouns == 1:
        call female_pronouns
    elif persistent.player_pronouns == 2:
        call nonbinary_pronouns
    call screen customstart_twobgchoice("Choose Type",
        "mod_assets/images/bg/anticshop.png","Special Days",
        "mod_assets/images/bg/monika_day_room.png","New Timelines",False,
        lock1=(not persistent.arc_clear[0]),
        lock2=(not persistent.any_bonus_day))
    if _return == 0:
        jump special_day
    else:
        jump new_timelines

# Special Days technically cannot be reached without clearing the first arc. However, all of these days
# have a warning attached anyway if they haven't cleared that arc somehow but got access to this menu.
label special_day:
    scene black
    "Warning: These days were meant to be played during a certain time period."
    "Some of these days are also meant to be played after reaching a certain point in the True Route story."
    "The events may not make sense if played during the wrong time period or without reaching that point in True Route."
    label special_day_choice:
    menu:
        "Choose Special Day"
        "First Christmas Event.":
            if not persistent.arc_clear[0]:
                "This day was meant to be played after clearing the [persistent.arc_names[0]] arc."
                menu:
                    "Are you sure you want to continue?"
                    "Yes":
                        pass
                    "No.":
                        jump special_day_choice
            show screen tear(20, 0.1, 0.1, 0, 40)
            $ pause(0.25)
            $ christmas_chapter = True
            $ s_name = "Sayori"
            stop music
            $ renpy.save_persistent()
            stop sound
            jump christmas_chapter
        "Second Christmas Event.":
            if not persistent.arc_clear[1]:
                "This day was meant to be played after clearing the [persistent.arc_names[1]] arc."
                menu:
                    "Are you sure you want to continue?"
                    "Yes":
                        pass
                    "No.":
                        jump special_day_choice
            show screen tear(20, 0.1, 0.1, 0, 40)
            $ pause(0.25)
            $ christmas_chapter = True
            $ s_name = "Sayori"
            stop music
            $ renpy.save_persistent()
            stop sound
            jump christmas2_chapter
        "Special Day.":
            if not persistent.arc_clear[0]:
                "This day was meant to be played after clearing the [persistent.arc_names[0]] arc."
                "Are you sure you want to continue?"
                menu:
                    "Yes":
                        pass
                    "No.":
                        jump special_day_choice
            show screen tear(20, 0.1, 0.1, 0, 40)
            $ pause(0.25)
            $ christmas_chapter = True
            $ s_name = "Sayori"
            stop music
            $ renpy.save_persistent()
            stop sound
            jump special_chapter
        "Return Day":
            if not persistent.arc_clear[1]:
                "This day was meant to be played after clearing the [persistent.arc_names[1]] arc."
                menu:
                    "Are you sure you want to continue?"
                    "Yes":
                        pass
                    "No.":
                        jump special_day_choice
            show screen tear(20, 0.1, 0.1, 0, 40)
            $ pause(0.25)
            $ christmas_chapter = True
            $ s_name = "Sayori"
            stop music
            $ renpy.save_persistent()
            stop sound
            jump return_chapter
        "Valentine's Day.":
            if not persistent.arc_clear[1]:
                "This day was meant to be played after clearing the [persistent.arc_names[1]] arc."
                menu:
                    "Are you sure you want to continue?"
                    "Yes":
                        pass
                    "No.":
                        jump special_day_choice
            show screen tear(20, 0.1, 0.1, 0, 40)
            $ pause(0.25)
            $ valentines_chapter = True
            $ s_name = "Sayori"
            stop music
            $ renpy.save_persistent()
            stop sound
            jump valentines_chapter

label new_timelines:
    scene black
    $ bonus_chapter_active
    $ s_name = "???"
    s "Huh...where am I?"
    s "...New timelines?"
    s "Just how much do you know about our world?"
    s "On second though, I don't want to know."
    s "Just make your choice. I don't want anything to do with this."
    s "And even if I did, I don't seem to have any control..."
    call screen bonusdays_bonusdaychoice("bg notebook-original","Who is the president?",False,True,False,True,True, True,True,player)
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