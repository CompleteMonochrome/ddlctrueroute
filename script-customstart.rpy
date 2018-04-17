label choose_start:
    scene black
    with dissolve_scene_full
    play music mend
    $ s_name = "???"
    $ quick_menu = False
    $ style.say_dialogue = style.normal
    $ allow_skipping = True
    $ config.allow_skipping = True
    $ sayori_personality = 0
    $ m_show = True
    s "Um..."
    s "What is this...?"
    s "Do you suddenly get to decide when and where you start?"
    s "Wow..."
    s "This mod has it all, doesn't it?"
    s "I just want you to know..."
    s "...that if you decide to start from the festival then your saves will be deleted."
    s "We have to sort out a few things first."
    menu:
        s "Who did you spend the weekend with?"
        "Yuri.":
            $ persistent.ch4_preparations = "Yuri"
            $ ch4_scene = "yuri"
            $ ch4_name = ch4_scene.capitalize()
        "Natsuki.":
            $ persistent.ch4_preparations = "Natsuki"
            $ ch4_scene = "natsuki"
            $ ch4_name = ch4_scene.capitalize()
    s "And..."
    menu:
        s "Did you accept a confession?"
        "Yes.":
            $ persistent.sayori_love = True
            $ sayori_confess = True
        "No.":
            $ persistent.sayori_love = False
            $ sayori_confess = False
    s "Oh..."
    s "Well, it doesn't matter."
    s "Let's keep going."

    menu:
        s "Which part are you starting from? The options that show up are in the right order of events...I think..."
        "Festival Day.":
            s "I hope you realize that your saves will be deleted if you choose this."
            s "So you should close the game, if you didn't want that..."
            s "Last chance..."
            s "Okay..."
            $ quick_menu = True
            $ s_name = "Sayori"
            stop music fadeout 1.0
            $ renpy.save_persistent()
            jump ch5_skip
        "Yuri's problem.":
            jump custom_yuristart
        "Natsuki's problem." if persistent.arc_clear[0]:
            jump custom_natstart
        "Sayori's problem." if persistent.arc_clear[1]:
            jump custom_saystart

    label custom_yuristart:
    s "Yuri's problem, eh?"
    menu:
        s "So, where are you starting from?"

        "Starting the Book Day.":
            s "I see..."
            menu:
                s "Who did you spend the festival day with?"
                "Sayori":
                    $ ch5_scene = "sayori"
                    $ ch5_name = ch5_scene.capitalize()
                "Monika.":
                    $ ch5_scene = "monika"
                    $ ch5_name = ch5_scene.capitalize()
                "Natsuki.":
                    $ ch5_scene = "natsuki"
                    $ ch5_name = ch5_scene.capitalize()
                "Yuri.":
                    $ ch5_scene = "yuri"
                    $ ch5_name = ch5_scene.capitalize()
            s "Okay..."
            menu:
                s "And who did you write your poem for?"
                "Sayori.":
                    $ newpoemwinner[0] = "sayori"
                    $ s_appeal += 1
                "Monika.":
                    $ newpoemwinner[0] = "monika"
                    $ m_appeal += 1
                "Natsuki.":
                    $ newpoemwinner[0] = "natsuki"
                    $ n_appeal += 1
                "Yuri.":
                    $ newpoemwinner[0] = "yuri"
                    $ y_appeal += 1
            s "Well...alright."
            s "I guess I'll be seeing you."
            $ quick_menu = True
            $ s_name = "Sayori"
            stop music fadeout 1.0
            $ renpy.save_persistent()
            jump ch6_skip

        "Continuing the Book Day.":
            $ bad_choice_first = False
            s "Okay..."
            menu:
                s "Who did you spend the festival day with?"
                "Sayori":
                    $ ch5_scene = "sayori"
                    $ ch5_name = ch5_scene.capitalize()
                "Monika.":
                    $ ch5_scene = "monika"
                    $ ch5_name = ch5_scene.capitalize()
                "Natsuki.":
                    $ ch5_scene = "natsuki"
                    $ ch5_name = ch5_scene.capitalize()
                "Yuri.":
                    $ ch5_scene = "yuri"
                    $ ch5_name = ch5_scene.capitalize()
            s "Hmm..."
            menu:
                s "So who did you write your first poem for?"
                "Sayori.":
                    $ newpoemwinner[0] = "sayori"
                    $ s_appeal += 1
                "Monika.":
                    $ newpoemwinner[0] = "monika"
                    $ m_appeal += 1
                "Natsuki.":
                    $ newpoemwinner[0] = "natsuki"
                    $ n_appeal += 1
                "Yuri.":
                    $ newpoemwinner[0] = "yuri"
                    $ y_appeal += 1
            s "Alright..."
            menu:
                s "And your second one?"
                "Sayori.":
                    $ newpoemwinner[1] = "sayori"
                    $ s_appeal += 1
                "Monika.":
                    $ newpoemwinner[1] = "monika"
                    $ m_appeal += 1
                "Natsuki.":
                    $ newpoemwinner[1] = "natsuki"
                    $ n_appeal += 1
                "Yuri.":
                    $ newpoemwinner[1] = "yuri"
                    $ y_appeal += 1
            s "Now..."
            menu:
                s "Did you read the book, write a poem or do the impossible?"
                "Read the book.":
                    $ read_book = True
                "Wrote a poem.":
                    $ read_book = False
                "Did the impossible.":
                    $ read_book = True
                    $ persistent.ch6_task[2] = True
            s "..."
            s "That's it."
            s "I'll see you when I see you..."
            $ s_name = "Sayori"
            $ quick_menu = True
            stop music fadeout 1.0
            $ renpy.save_persistent()
            jump ch7_skip

        "Play Day.":
            $ bad_choice_first = False
            s "Getting right to it, I guess..."
            s "You can only start from the beginning of this day."
            s "I don't know what will happen so..."
            s "Anyway...!"
            menu:
                s "Who did you spend the festival day with?"
                "Sayori":
                    $ ch5_scene = "sayori"
                    $ ch5_name = ch5_scene.capitalize()
                "Monika.":
                    $ ch5_scene = "monika"
                    $ ch5_name = ch5_scene.capitalize()
                "Natsuki.":
                    $ ch5_scene = "natsuki"
                    $ ch5_name = ch5_scene.capitalize()
                "Yuri.":
                    $ ch5_scene = "yuri"
                    $ ch5_name = ch5_scene.capitalize()
            s "And..."
            menu:
                s "Who did you write your first poem for?"
                "Sayori.":
                    $ newpoemwinner[0] = "sayori"
                    $ s_appeal += 1
                "Monika.":
                    $ newpoemwinner[0] = "monika"
                    $ m_appeal += 1
                "Natsuki.":
                    $ newpoemwinner[0] = "natsuki"
                    $ n_appeal += 1
                "Yuri.":
                    $ newpoemwinner[0] = "yuri"
                    $ y_appeal += 1
            s "Alright..."
            menu:
                s "And your second one?"
                "Sayori.":
                    $ newpoemwinner[1] = "sayori"
                    $ s_appeal += 1
                "Monika.":
                    $ newpoemwinner[1] = "monika"
                    $ m_appeal += 1
                "Natsuki.":
                    $ newpoemwinner[1] = "natsuki"
                    $ n_appeal += 1
                "Yuri.":
                    $ newpoemwinner[1] = "yuri"
                    $ y_appeal += 1
            s "Now..."
            menu:
                s "Did you read the book, write a poem or do the impossible?"
                "Read the book.":
                    $ yuri_approval += 1
                    $ read_book = True
                    $ did_all_tasks = False
                "Wrote a poem.":
                    $ yuri_approval += 1
                    $ read_book = False
                    $ did_all_tasks = False
                    if newpoemwinner[1] == "natsuki":
                        $ natsuki_approval += 1
                "Did the impossible.":
                    $ yuri_approval -= 1
                    $ read_book = True
                    $ did_all_tasks = True
                    if newpoemwinner[1] == "natsuki":
                        $ natsuki_approval += 1
            menu:
                s "Who did you choose to read with the day before?"
                "Sayori.":
                    $ needs_to_read = True
                    $ ch7_scene = "sayori"
                    $ ch7_name = ch7_scene.capitalize()
                    $ yuri_approval -= 1
                "Monika.":
                    $ needs_to_read = False
                    $ ch7_scene = "monika"
                    $ ch7_name = ch7_scene.capitalize()
                    $ yuri_approval -= 1
                "Natsuki.":
                    $ needs_to_read = False
                    $ ch7_scene = "natsuki"
                    $ ch7_name = ch7_scene.capitalize()
                    $ yuri_approval -= 1
                    $ natsuki_approval += 1
                "Yuri.":
                    $ needs_to_read = True
                    $ ch7_scene = "yuri"
                    $ ch7_name = ch7_scene.capitalize()
                    if did_all_tasks or read_book:
                        $ yuri_approval = 4
                    else:
                        $ yuri_approval = 3
            s "..."
            s "So this is it."
            s "I guess I'll see you on the other side..."
            s "Good luck!"
            $ s_name = "Sayori"
            $ quick_menu = True
            stop music fadeout 1.0
            $ renpy.save_persistent()
            jump ch8_redirect

    label custom_natstart:
    s "Okay..."
    s "I hope that means you helped Yuri, right?"
    s "I guess I'll find out after you answer some more questions."

    menu:
        s "Who did you spend the festival day with?"
        "Sayori":
            $ ch5_scene = "sayori"
            $ ch5_name = ch5_scene.capitalize()
        "Monika.":
            $ ch5_scene = "monika"
            $ ch5_name = ch5_scene.capitalize()
        "Natsuki.":
            $ ch5_scene = "natsuki"
            $ ch5_name = ch5_scene.capitalize()
        "Yuri.":
            $ ch5_scene = "yuri"
            $ ch5_name = ch5_scene.capitalize()
    s "And..."

    menu:
        s "Who did you write your first poem for?"
        "Sayori.":
            $ newpoemwinner[0] = "sayori"
            $ s_appeal += 1
        "Monika.":
            $ newpoemwinner[0] = "monika"
            $ m_appeal += 1
        "Natsuki.":
            $ newpoemwinner[0] = "natsuki"
            $ n_appeal += 1
        "Yuri.":
            $ newpoemwinner[0] = "yuri"
            $ y_appeal += 1
    s "Alright..."

    menu:
        s "And your second one?"
        "Sayori.":
            $ newpoemwinner[1] = "sayori"
            $ s_appeal += 1
        "Monika.":
            $ newpoemwinner[1] = "monika"
            $ m_appeal += 1
        "Natsuki.":
            $ newpoemwinner[1] = "natsuki"
            $ n_appeal += 1
        "Yuri.":
            $ newpoemwinner[1] = "yuri"
            $ y_appeal += 1
    s "Now..."

    menu:
        s "Did you read the book, write a poem or do the impossible?"
        "Read the book.":
            $ yuri_approval += 1
            $ read_book = True
            $ did_all_tasks = False
        "Wrote a poem.":
            $ yuri_approval += 1
            $ read_book = False
            $ did_all_tasks = False
            if newpoemwinner[1] == "natsuki":
                $ natsuki_approval += 1
        "Did the impossible.":
            $ yuri_approval -= 1
            $ read_book = True
            $ did_all_tasks = True
            if newpoemwinner[1] == "natsuki":
                $ natsuki_approval += 1

    menu:
        s "Who did you choose to read with the day before the play?"
        "Sayori.":
            $ needs_to_read = True
            $ ch7_scene = "sayori"
            $ ch7_name = ch7_scene.capitalize()
            $ yuri_approval -= 1
        "Monika.":
            $ needs_to_read = False
            $ ch7_scene = "monika"
            $ ch7_name = ch7_scene.capitalize()
            $ yuri_approval -= 1
        "Natsuki.":
            $ needs_to_read = False
            $ ch7_scene = "natsuki"
            $ ch7_name = ch7_scene.capitalize()
            $ yuri_approval -= 1
            $ natsuki_approval += 1
        "Yuri.":
            $ needs_to_read = True
            $ ch7_scene = "yuri"
            $ ch7_name = ch7_scene.capitalize()
            if did_all_tasks or read_book:
                $ yuri_approval = 4
            else:
                $ yuri_approval = 3
    # Play Day - Assumes you go with Sayori's decision
    $ yuri_approval += 1
    s "I see..."

    menu:
        s "Did you use strawberries on the day of the play?"
        "Yes.":
            $ yuri_approval += 2
            $ play_firstpart = True
            s "Thank goodness..."
        "No.":
            $ yuri_approval += 1
            $ play_firstpart = False
            s "At least..."
    s "...she's okay."
    s "Now..."
    menu:
        s "Who did you write your third poem for?"
        "Sayori.":
            $ newpoemwinner[2] = "sayori"
            $ s_appeal += 1
        "Monika.":
            $ newpoemwinner[2] = "monika"
            $ m_appeal += 1
        "Natsuki.":
            $ newpoemwinner[2] = "natsuki"
            $ n_appeal += 1
        "Yuri.":
            $ newpoemwinner[2] = "yuri"
            $ y_appeal += 1
    s "Moving on..."

    if m_appeal < 3 or not did_all_tasks:
        s "Monika asked you for a book, right?"
        menu:
            s "What did you do with it?"
            "Gave it to her.":
                $ gave_book_to_monika = True
            "Threw it away.":
                $ gave_book_to_monika = False
        s "I see."

    menu:
        s "Which day are you starting from?"
        "Recovery Day.":
            s "So this is where you're starting from?"
            s "..."
            s "Alright."
            s "I guess I will be seeing you."
            $ s_name = "Sayori"
            $ quick_menu = True
            stop music fadeout 1.0
            $ renpy.save_persistent()
            jump ch9_skip
        "Visit Day.":
            if y_appeal == 3 and play_firstpart and did_all_tasks:
                s "You were given a chance to go see Yuri at the hospital, right?"
                s "So..."
                menu:
                    s "Did you?"
                    "Yes.":
                        $ visited_yuri_hospital = True
                        if sayori_confess:
                            $ sayori_dumped = True
                            $ sayori_personality += 1
                            s "I..."
                            s "I see."
                            s "Sorry, just..."
                            s "I just need a little time to think."
                        else:
                            s "I see."
                        s "..."
                        s "Did you..."
                        menu:
                            s "...go on a date?"
                            "Yes.":
                                $ yuri_date = True
                            "No.":
                                $ yuri_date = False
                    "No.":
                        $ visited_yuri_hospital = False
                        $ yuri_date = False
                        s "Oh, okay."
            else:
                $ visited_yuri_hospital = False
                $ yuri_date = False
            s "Well..."
            s "I hope you enjoy today."
            s "I don't know what's going to happen..."
            s "I guess I'll just be getting the memories of whatever you chose, right?"
            s "..."
            s "Goodbye."
            $ s_name = "Sayori"
            $ quick_menu = True
            stop music fadeout 1.0
            $ renpy.save_persistent()
            jump ch10_skip
        "Second Visit.":
            $ insert_dadsuki_character()
            if y_appeal == 3 and play_firstpart and did_all_tasks:
                s "You were given a chance to go see Yuri at the hospital, right?"
                s "So..."
                menu:
                    s "Did you?"
                    "Yes.":
                        $ visited_yuri_hospital = True
                        if sayori_confess:
                            $ sayori_dumped = True
                            $ sayori_personality += 1
                            s "I..."
                            s "I see."
                            s "Sorry, just..."
                            s "I just need a little time to think."
                        else:
                            s "I see."
                        s "..."
                        s "Did you..."
                        menu:
                            s "...go on a date?"
                            "Yes.":
                                $ yuri_date = True
                            "No.":
                                $ yuri_date = False
                    "No.":
                        $ visited_yuri_hospital = False
                        $ yuri_date = False
                        s "Oh, okay."
            else:
                $ visited_yuri_hospital = False
                $ yuri_date = False
            s "Hmm..."
            s "Apparently you visited Natsuki's house the day before."
            menu:
                s "Did you do anything aside from reading the manga?"
                "Checked closed rooms.":
                    $ natsuki_approval += 1
                    s "I see."
                    s "That seems like an invasion of privacy but..."
                    s "I'm not judging! It's probably important."
                    label custom_ch11_roomcheck:
                    menu:
                        s "Which rooms did you check?"
                        "First room upstairs." if not persistent.natsuki_house[0]:
                            $ persistent.natsuki_house[0] = True
                            $ talkabout_natsuki_house[0] = True
                            jump custom_ch11_roomcheck
                        "Second room upstairs." if not persistent.natsuki_house[1]:
                            $ persistent.natsuki_house[1] = True
                            $ talkabout_natsuki_house[1] = True
                            jump custom_ch11_roomcheck
                        "Closed room downstairs." if not persistent.natsuki_house[2]:
                            $ persistent.natsuki_house[2] = True
                            $ talkabout_natsuki_house[2] = True
                            jump custom_ch11_roomcheck
                        "Living room." if not persistent.natsuki_house[3]:
                            $ persistent.natsuki_house[3] = True
                            $ talkabout_natsuki_house[3] = True
                            jump custom_ch11_roomcheck
                        "Done.":
                            pass
                "Stayed in her room.":
                    $ natsuki_approval -= 1
                    s "Really?"
                    s "The other option sounded more appropriate..."
                    s "Oh well..."
            # Check if player checked rooms
            if persistent.natsuki_house[0] and persistent.natsuki_house[1] and persistent.natsuki_house[2] and persistent.natsuki_house[3]:
                $ check_whole_house = True
            if persistent.natsuki_house[0] or persistent.natsuki_house[1] or persistent.natsuki_house[2] or persistent.natsuki_house[3]:
                $ check_some_house = True
            # Set varables to false later to prevent errors in upcoming custom starts
            $ persistent.natsuki_house = [False, False, False, False]
            s "I'll be seeing you..."
            s "I hope..."
            $ s_name = "Sayori"
            $ quick_menu = True
            stop music fadeout 1.0
            $ renpy.save_persistent()
            jump ch11_skip
        "Play Day.":
            $ insert_dadsuki_character()
            if y_appeal == 3 and play_firstpart and did_all_tasks:
                s "You were given a chance to go see Yuri at the hospital, right?"
                s "So..."
                menu:
                    s "Did you?"
                    "Yes.":
                        $ visited_yuri_hospital = True
                        if sayori_confess:
                            $ sayori_dumped = True
                            $ sayori_personality += 1
                            s "I..."
                            s "I see."
                            s "Sorry, just..."
                            s "I just need a little time to think."
                        else:
                            s "I see."
                        s "..."
                        s "Did you..."
                        menu:
                            s "...go on a date?"
                            "Yes.":
                                $ yuri_date = True
                            "No.":
                                $ yuri_date = False
                    "No.":
                        $ visited_yuri_hospital = False
                        $ yuri_date = False
                        s "Oh, okay."
            else:
                $ visited_yuri_hospital = False
                $ yuri_date = False
            s "Hmm..."
            s "Apparently you visited Natsuki's house twice!"
            s "What did you do the first time?"
            menu:
                s "Did you do anything aside from reading the manga?"
                "Checked closed rooms.":
                    $ natsuki_approval += 1
                    s "I see."
                    s "That seems like an invasion of privacy but..."
                    s "I'm not judging! It's probably important."
                    label custom_ch11_roomcheck_2:
                    menu:
                        s "Which rooms did you check?"
                        "First room upstairs." if not persistent.natsuki_house[0]:
                            $ persistent.natsuki_house[0] = True
                            $ talkabout_natsuki_house[0] = True
                            jump custom_ch11_roomcheck_2
                        "Second room upstairs." if not persistent.natsuki_house[1]:
                            $ persistent.natsuki_house[1] = True
                            $ talkabout_natsuki_house[1] = True
                            jump custom_ch11_roomcheck_2
                        "Closed room downstairs." if not persistent.natsuki_house[2]:
                            $ persistent.natsuki_house[2] = True
                            $ talkabout_natsuki_house[2] = True
                            jump custom_ch11_roomcheck_2
                        "Living room." if not persistent.natsuki_house[3]:
                            $ persistent.natsuki_house[3] = True
                            $ talkabout_natsuki_house[3] = True
                            jump custom_ch11_roomcheck_2
                        "Done.":
                            pass
                "Stayed in her room.":
                    $ natsuki_approval -= 1
                    s "Really?"
                    s "The other option sounded more appropriate..."
                    s "Oh well..."
            # Check if player checked rooms
            if persistent.natsuki_house[0] and persistent.natsuki_house[1] and persistent.natsuki_house[2] and persistent.natsuki_house[3]:
                $ check_whole_house = True
            if persistent.natsuki_house[0] or persistent.natsuki_house[1] or persistent.natsuki_house[2] or persistent.natsuki_house[3]:
                $ check_some_house = True
            # Set varables to false later to prevent errors in upcoming custom starts
            $ persistent.natsuki_house = [False, False, False, False]

            $ ch11_did_all_tasks = True
            $ ch11_read_manga = True
            $ ch11_badpoem = False
            s "I can just feel how close we are..."
            if m_appeal == 3 and did_all_tasks:
                $ ch11_monika_talked = True
                s "Monika went over to your house to warn you about something, right?"
                menu:
                    s "What did you do after that?"
                    "Had dinner with her.":
                        $ ch11_monika_dinner = True
                        s "You did?"
                        s "That's..."
                        s "Um...none of my business."
                        s "What happened after dinner?"
                        menu:
                            s "Did you read the manga, write a poem or do the impossible?"
                            "Read the manga.":
                                $ ch11_read_manga = True
                                $ ch11_badpoem = True
                                $ ch11_did_all_tasks = False
                            "Wrote a poem.":
                                $ ch11_read_manga = False
                                $ ch11_badpoem = False
                                $ ch11_did_all_tasks = False
                            "Did the impossible.":
                                $ ch11_read_manga = True
                                $ ch11_badpoem = False
                                $ ch11_did_all_tasks = True
                    "Turned her down.":
                        $ ch11_monika_dinner = False
                s "Oh."

            s "Last question."
            menu:
                s "Who did you write your fourth poem for?"
                "Sayori.":
                    $ natarcpoemwinner[0] = "sayori"
                    $ s_appeal += 1
                "Monika.":
                    $ natarcpoemwinner[0] = "monika"
                    $ m_appeal += 1
                "Natsuki.":
                    $ natarcpoemwinner[0] = "natsuki"
                    $ n_appeal += 1
                "Yuri.":
                    $ natarcpoemwinner[0] = "yuri"
                    $ y_appeal += 1

            s "I guess this is it."
            s "I hope we can get Natsuki through this with the best outcome."
            $ s_name = "Sayori"
            $ quick_menu = True
            stop music fadeout 1.0
            $ renpy.save_persistent()
            jump ch12_skip

    label custom_saystart:
    "What."
    menu:
        "Yes":
            jump ch13_skip
        "No":
            jump ch13_skip
