label female_pronouns:
    $ player_gender = "girl"
    $ cPlayer_gender = player_gender.capitalize()
    $ player_other = "lady"
    $ cPlayer_other = player_other.capitalize()
    $ player_casual = "girl"
    $ cPlayer_casual = player_casual.capitalize()
    $ player_personal = "she"
    $ cPlayer_personal = player_personal.capitalize()
    $ player_possessive = "her"
    $ cPlayer_possessive = player_possessive.capitalize()
    $ player_reflexive = "her"
    $ cPlayer_reflexive = player_reflexive.capitalize()
    return

label choose_start:
    # Check player gender after input
    if persistent.player_female:
        call female_pronouns

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
            s "You did?!"
            s "I..."
        "No.":
            $ persistent.sayori_love = False
            $ sayori_confess = False
            s "Oh..."
    s "Well, it doesn't matter."
    s "Let's keep going."

    python:
        import datetime
        currentdate = datetime.date.today()
        weekrange = datetime.timedelta(days = 7)

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
            $ persistent.custom_starts_used += 1
            $ renpy.save_persistent()
            jump ch5_skip
        "Yuri's problem.":
            jump custom_yuristart
        "Natsuki's problem." if persistent.arc_clear[0]:
            jump custom_natstart
        "Sayori's problem." if persistent.arc_clear[1]:
            jump custom_saystart
        "Special Day." if (currentdate <= (datetime.date(2018, 9, 22) + weekrange)) and persistent.arc_clear[0]:
            s "What's this?"
            s "What have you done?"
            s "What are we in for...?"
            $ special_chapter = True
            $ quick_menu = True
            $ s_name = "Sayori"
            stop music fadeout 1.0
            $ renpy.save_persistent()
            jump special_chapter
        "Christmas Eve." if (currentdate <= (datetime.date(2018, 12, 23) + weekrange)) and persistent.arc_clear[0]:
            s "Christmas Eve?"
            s "Is it really that time already?"
            s "I guess it's time to get our festivities up!"
            $ christmas_chapter = True
            $ quick_menu = True
            $ s_name = "Sayori"
            stop music fadeout 1.0
            $ renpy.save_persistent()
            jump christmas_chapter

    label custom_yuristart:
    s "Yuri's problem, eh?"
    menu:
        s "So, where are you starting from?"
        # Chapter 6
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
                    $ s_poemappeal[5] = 1
                    $ s_appeal += 1
                "Monika.":
                    $ newpoemwinner[0] = "monika"
                    $ m_poemappeal[5] = 1
                    $ m_appeal += 1
                "Natsuki.":
                    $ newpoemwinner[0] = "natsuki"
                    $ n_poemappeal[5] = 1
                    $ n_appeal += 1
                "Yuri.":
                    $ newpoemwinner[0] = "yuri"
                    $ y_poemappeal[5] = 1
                    $ y_appeal += 1
            s "Well...alright."
            s "I guess I'll be seeing you."
            $ quick_menu = True
            $ s_name = "Sayori"
            stop music fadeout 1.0
            $ persistent.custom_starts_used += 1
            $ renpy.save_persistent()
            jump ch6_skip
        # Chapter 7
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
                    $ s_poemappeal[5] = 1
                    $ s_appeal += 1
                "Monika.":
                    $ newpoemwinner[0] = "monika"
                    $ m_poemappeal[5] = 1
                    $ m_appeal += 1
                "Natsuki.":
                    $ newpoemwinner[0] = "natsuki"
                    $ n_poemappeal[5] = 1
                    $ n_appeal += 1
                "Yuri.":
                    $ newpoemwinner[0] = "yuri"
                    $ y_poemappeal[5] = 1
                    $ y_appeal += 1
            s "Alright..."
            menu:
                s "And your second one?"
                "Sayori.":
                    $ newpoemwinner[1] = "sayori"
                    $ s_poemappeal[6] = 1
                    $ s_appeal += 1
                "Monika.":
                    $ newpoemwinner[1] = "monika"
                    $ m_poemappeal[6] = 1
                    $ m_appeal += 1
                "Natsuki.":
                    $ newpoemwinner[1] = "natsuki"
                    $ n_poemappeal[6] = 1
                    $ n_appeal += 1
                "Yuri.":
                    $ newpoemwinner[1] = "yuri"
                    $ y_poemappeal[6] = 1
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
            $ persistent.custom_starts_used += 1
            $ renpy.save_persistent()
            jump ch7_skip
        # Chapter 8
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
                    $ s_poemappeal[5] = 1
                    $ s_appeal += 1
                "Monika.":
                    $ newpoemwinner[0] = "monika"
                    $ m_poemappeal[5] = 1
                    $ m_appeal += 1
                "Natsuki.":
                    $ newpoemwinner[0] = "natsuki"
                    $ n_poemappeal[5] = 1
                    $ n_appeal += 1
                "Yuri.":
                    $ newpoemwinner[0] = "yuri"
                    $ y_poemappeal[5] = 1
                    $ y_appeal += 1
            s "Alright..."
            menu:
                s "And your second one?"
                "Sayori.":
                    $ newpoemwinner[1] = "sayori"
                    $ s_poemappeal[6] = 1
                    $ s_appeal += 1
                "Monika.":
                    $ newpoemwinner[1] = "monika"
                    $ m_poemappeal[6] = 1
                    $ m_appeal += 1
                "Natsuki.":
                    $ newpoemwinner[1] = "natsuki"
                    $ n_poemappeal[6] = 1
                    $ n_appeal += 1
                "Yuri.":
                    $ newpoemwinner[1] = "yuri"
                    $ y_poemappeal[6] = 1
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
                    $ yuri_approval += 1
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
            $ persistent.custom_starts_used += 1
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
            $ s_poemappeal[5] = 1
            $ s_appeal += 1
        "Monika.":
            $ newpoemwinner[0] = "monika"
            $ m_poemappeal[5] = 1
            $ m_appeal += 1
        "Natsuki.":
            $ newpoemwinner[0] = "natsuki"
            $ n_poemappeal[5] = 1
            $ n_appeal += 1
        "Yuri.":
            $ newpoemwinner[0] = "yuri"
            $ y_poemappeal[5] = 1
            $ y_appeal += 1
    s "Alright..."

    menu:
        s "And your second one?"
        "Sayori.":
            $ newpoemwinner[1] = "sayori"
            $ s_poemappeal[6] = 1
            $ s_appeal += 1
        "Monika.":
            $ newpoemwinner[1] = "monika"
            $ m_poemappeal[6] = 1
            $ m_appeal += 1
        "Natsuki.":
            $ newpoemwinner[1] = "natsuki"
            $ n_poemappeal[6] = 1
            $ n_appeal += 1
        "Yuri.":
            $ newpoemwinner[1] = "yuri"
            $ y_poemappeal[6] = 1
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
            $ yuri_approval += 1
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
            $ s_poemappeal[8] = 1
            $ s_appeal += 1
        "Monika.":
            $ newpoemwinner[2] = "monika"
            $ m_poemappeal[8] = 1
            $ m_appeal += 1
        "Natsuki.":
            $ newpoemwinner[2] = "natsuki"
            $ n_poemappeal[8] = 1
            $ n_appeal += 1
        "Yuri.":
            $ newpoemwinner[2] = "yuri"
            $ y_poemappeal[8] = 1
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
        # Chapter 9
        "Recovery Day.":
            s "So this is where you're starting from?"
            s "..."
            s "Alright."
            s "I guess I will be seeing you."
            $ s_name = "Sayori"
            $ quick_menu = True
            stop music fadeout 1.0
            $ persistent.custom_starts_used += 1
            $ renpy.save_persistent()
            jump ch9_skip
        # Chapter 10
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
            $ persistent.custom_starts_used += 1
            $ renpy.save_persistent()
            jump ch10_skip
        # Chapter 11
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
            $ persistent.custom_starts_used += 1
            $ renpy.save_persistent()
            jump ch11_skip
        # Chapter 12
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
                    $ s_poemappeal2[0] = 1
                    $ s_appeal += 1
                "Monika.":
                    $ natarcpoemwinner[0] = "monika"
                    $ m_poemappeal2[0] = 1
                    $ m_appeal += 1
                "Natsuki.":
                    $ natarcpoemwinner[0] = "natsuki"
                    $ n_poemappeal2[0] = 1
                    $ n_appeal += 1
                "Yuri.":
                    $ natarcpoemwinner[0] = "yuri"
                    $ y_poemappeal2[0] = 1
                    $ y_appeal += 1

            s "I guess this is it."
            s "I hope we can get Natsuki through this with the best outcome."
            $ s_name = "Sayori"
            $ quick_menu = True
            stop music fadeout 1.0
            $ persistent.custom_starts_used += 1
            $ renpy.save_persistent()
            jump ch12_skip

    label custom_saystart:
    s "Wait...seriously?"
    s "You've gotten this far..."
    s "I have to know what happens!"
    s "Wait...I guess I'm going to find out, aren't I?"

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
            $ s_poemappeal[5] = 1
            $ s_appeal += 1
        "Monika.":
            $ newpoemwinner[0] = "monika"
            $ m_poemappeal[5] = 1
            $ m_appeal += 1
        "Natsuki.":
            $ newpoemwinner[0] = "natsuki"
            $ n_poemappeal[5] = 1
            $ n_appeal += 1
        "Yuri.":
            $ newpoemwinner[0] = "yuri"
            $ y_poemappeal[5] = 1
            $ y_appeal += 1
    s "Alright..."

    menu:
        s "And your second one?"
        "Sayori.":
            $ newpoemwinner[1] = "sayori"
            $ s_poemappeal[6] = 1
            $ s_appeal += 1
        "Monika.":
            $ newpoemwinner[1] = "monika"
            $ m_poemappeal[6] = 1
            $ m_appeal += 1
        "Natsuki.":
            $ newpoemwinner[1] = "natsuki"
            $ n_poemappeal[6] = 1
            $ n_appeal += 1
        "Yuri.":
            $ newpoemwinner[1] = "yuri"
            $ y_poemappeal[6] = 1
            $ y_appeal += 1
    s "Now..."

    menu:
        s "Did you read the book, write a poem or do the impossible?"
        "Read the book.":
            $ yuri_approval += 1
            $ read_book = True
            $ did_all_tasks = False
        "Wrote a poem.":
            $ yuri_approval -= 1
            $ read_book = False
            $ did_all_tasks = False
            if newpoemwinner[1] == "natsuki":
                $ natsuki_approval += 1
        "Did the impossible.":
            $ yuri_approval += 1
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
            $ s_poemappeal[8] = 1
            $ s_appeal += 1
        "Monika.":
            $ newpoemwinner[2] = "monika"
            $ m_poemappeal[8] = 1
            $ m_appeal += 1
        "Natsuki.":
            $ newpoemwinner[2] = "natsuki"
            $ n_poemappeal[8] = 1
            $ n_appeal += 1
        "Yuri.":
            $ newpoemwinner[2] = "yuri"
            $ y_poemappeal[8] = 1
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
            label custom_ch11_roomcheck_3:
            menu:
                s "Which rooms did you check?"
                "First room upstairs." if not persistent.natsuki_house[0]:
                    $ persistent.natsuki_house[0] = True
                    $ talkabout_natsuki_house[0] = True
                    jump custom_ch11_roomcheck_3
                "Second room upstairs." if not persistent.natsuki_house[1]:
                    $ persistent.natsuki_house[1] = True
                    $ talkabout_natsuki_house[1] = True
                    jump custom_ch11_roomcheck_3
                "Closed room downstairs." if not persistent.natsuki_house[2]:
                    $ persistent.natsuki_house[2] = True
                    $ talkabout_natsuki_house[2] = True
                    jump custom_ch11_roomcheck_3
                "Living room." if not persistent.natsuki_house[3]:
                    $ persistent.natsuki_house[3] = True
                    $ talkabout_natsuki_house[3] = True
                    jump custom_ch11_roomcheck_3
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

    s "Just a few more questions."
    menu:
        s "Who did you write your fourth poem for?"
        "Sayori.":
            $ natarcpoemwinner[0] = "sayori"
            $ s_poemappeal2[0] = 1
            $ s_appeal += 1
        "Monika.":
            $ natarcpoemwinner[0] = "monika"
            $ m_poemappeal2[0] = 1
            $ m_appeal += 1
        "Natsuki.":
            $ natarcpoemwinner[0] = "natsuki"
            $ n_poemappeal2[0] = 1
            $ n_appeal += 1
        "Yuri.":
            $ natarcpoemwinner[0] = "yuri"
            $ y_poemappeal2[0] = 1
            $ y_appeal += 1


    s "Since you're starting from this day..."
    s "It means you've finished helping Natsuki, right?"
    s "Well, at least...the really important parts of helping Natsuki."
    s "So...what happened on the day of the play?"

    if m_appeal >= 4 and ch11_monika_talked and ch11_monika_dinner and ch11_did_all_tasks:
        $ monika_type = 0
    elif ch11_monika_talked:
        $ monika_type = 1
    else:
        $ monika_type = 2

    if monika_type != 0:
        s "..."
        s "Why do I feel like something bad is going to happen?"
        s "Did you listen to...it?"
        s "I don't know what that means but you had to choose some things..."
        menu:
            s "Did you listen to it at each occasion?"
            "Yes.":
                $ ch12_natsuki_reluctance += 2
                $ sayori_personality += 3
                s "Okay..."
                s "I don't know what that did but I feel really..."
                s "Never mind."
            "No.":
                s "Suddenly I feel a lot better."
                s "I don't really know why."

    if check_some_house:
        s "You were told about somebody coming, weren't you?"
        menu:
            s "You had to put in a file...so did you?"
            "Yes.":
                s "You did?"
                s "Alright..."
                s "Apparently it had something to do with a personality."
                menu:
                    s "Was it right...?"
                    "Yes.":
                        $ normal_haruki = True
                        $ insert_momsuki_character_normal()
                        s "Well...that's something."
                    "No.":
                        s "Then there was no point in even talking about this, was there?"
            "No.":
                s "I see."
                s "Well...I hope you knew what you're doing."

    s "So that means..."
    if normal_haruki:
        if check_whole_house:
            $ natsuki_approval += 2
            $ ch12_outcome = 3
            s "You brought back Natsuki's family..."
            s "She has to be happy, right?"
        else:
            $ natsuki_approval += 1
            $ ch12_outcome = 2
            s "Her dad is gone..."
            s "I don't really know how she's feeling about that."
    else:
        if check_whole_house:
            $ natsuki_approval += 1
            $ ch12_outcome = 1
            s "Natsuki and her dad are back together as a family..."
            s "That's so...unexpected."
            s "But I bet they're both feeling better."
        else:
            if natsuki_approval > 0:
                $ natsuki_approval -= 1
            $ ch12_outcome = 0
            s "Natsuki lives by herself now?"
            s "I...don't really know how to feel about that."
            s "Her problem is solved but..."

    s "Whatever..."
    if ch12_natsuki_reluctance >= 3:
        s "I think we're almost done--."
        $ currentpos = get_pos()
        stop music
        $ pause(0.5)
        s "..."
        s "An offer...was made."
        s "I'm sure you're aware of what this is."
        menu:
            s "Did you...accept it?"
            "Yes.":
                $ ch12_markov_agree = True
                s "Great."
            "No.":
                $ ch12_markov_agree = False
                s "Disappointing but not unexpected."
        s "Hold on a moment..."
        play music "<from " + str(currentpos) + " loop 6.424>bgm/monika-end.ogg"
        s "..."
        s "...done here...?"
        s "Did something just happen?"
        s "...Never mind."
        s "Where was I?"
        s "Let me just say what I wanted to say again..."

    s "I think we're almost done here."
    menu:
        s "You just need to say which day you're starting from."
        "First day of preparations.":
            s "Alright, last question then..."
            menu:
                s "Who did you write your fifth poem for?"
                "Sayori.":
                    $ sayarcpoemwinner[0] = "sayori"
                    $ s_poemappeal2[1] = 1
                    $ s_appealS += 1
                "Monika.":
                    $ sayarcpoemwinner[0] = "monika"
                    $ m_poemappeal2[1] = 1
                    $ m_appealS += 1
                "Natsuki.":
                    $ sayarcpoemwinner[0] = "natsuki"
                    $ n_poemappeal2[1] = 1
                    $ n_appealS += 1
                "Yuri.":
                    $ sayarcpoemwinner[0] = "yuri"
                    $ y_poemappeal2[1] = 1
                    $ y_appealS += 1

            s "And...that's it!"
            s "I'll be seeing you..."

            $ s_name = "Sayori"
            $ quick_menu = True
            stop music fadeout 1.0
            $ persistent.custom_starts_used += 1
            $ renpy.save_persistent()
            jump ch13_skip
        "Second day of preparations.":
            s "I see..."
            menu:
                s "You have to tell me who you wrote your fifth poem for."
                "Sayori.":
                    $ sayarcpoemwinner[0] = "sayori"
                    $ s_poemappeal2[1] = 1
                    $ s_appealS += 1
                "Monika.":
                    $ sayarcpoemwinner[0] = "monika"
                    $ m_poemappeal2[1] = 1
                    $ m_appealS += 1
                "Natsuki.":
                    $ sayarcpoemwinner[0] = "natsuki"
                    $ n_poemappeal2[1] = 1
                    $ n_appealS += 1
                "Yuri.":
                    $ sayarcpoemwinner[0] = "yuri"
                    $ y_poemappeal2[1] = 1
                    $ y_appealS += 1

            s "This almost feels like an interrogation, doesn't it?"
            s "But it isn't..."
            menu:
                s "...so who did you choose to help for Inauguration Day?"
                "Sayori.":
                    $ ch13_scene = "sayori"
                "Monika.":
                    $ ch13_scene = "monika"
                "Natsuki.":
                    $ ch13_scene = "natsuki"
                "Yuri.":
                    $ ch13_scene = "yuri"
            $ ch13_name = ch13_scene.capitalize()
            s "Alright..."

            # Dumping Sayori for Natsuki
            if ch13_name == "Natsuki" and (ch12_outcome == 3 or ch12_outcome == 1) and n_appeal >= 4 and n_appealS >= 1 and sayori_confess:
                s "It's clear by this point, you're trying to appeal to Natsuki."
                s "At least, it feels like you are with all your poem choices."
                s "But even so, you..."
                s "Are you going to leave the one you chose before?"
                s "Even if you aren't going to try to be with Natsuki."
                menu:
                    s "So...are you leaving Sayori?"
                    "Yes.":
                        $ sayori_dumped = True
                        $ sayori_personality += 2
                        s "I...see."
                        s "Then..."
                        s "Sorry, it's just..."
                        s "Never mind."
                        s "I hope you two have a good time together."
                    "No.":
                        $ sayori_dumped = False
                        if sayori_personality > 0:
                            $ sayori_personality -= 1
                        s "You aren't?"
                        s "I see..."
                        s "That's good!"
                        s "Not that it matters or anything...!"
                        s "It's just..."
                        s "...just good."
            # Going On Date
            if ch13_name == "Natsuki" and (ch12_outcome == 3 or ch12_outcome == 1) and n_appeal >= 4 and n_appealS >= 1 and ((sayori_dumped and sayori_confess) or (not sayori_confess)):
                s "You were given the opportunity to go with Natsuki..."
                s "...On a date."
                menu:
                    s "Did you take that opportunity?"
                    "Yes.":
                        $ natsuki_date = True
                        s "So they're together now..."
                        s "Okay."
                    "No.":
                        $ natsuki_date = False
                        s "You didn't?"
                        s "Then what was the point of it all..."
                        s "Whatever."

            if ch13_name == "Monika":
                s "Since you went with Monika, you chose some music, right?"
                menu:
                    s "What was it?"
                    "Harmonic.":
                        $ ch13_music_type = "harmonic"
                    "Upbeat.":
                        $ ch13_music_type = "upbeat"
                    "Melancholy.":
                        $ ch13_music_type = "melancholy"
                s "Oh, alright."
            elif ch13_name == "Yuri":
                s "When you were with Yuri..."
                menu:
                    s "Did you take one of her books?"
                    "Yes.":
                        $ ch13_yuri_books = True
                        $ yuri_approval += 1
                    "No.":
                        $ ch13_yuri_books = False
                s "I see..."
            elif ch13_name == "Natsuki":
                s "At the end of the day with Natsuki..."
                menu:
                    s "Did you take three manga or just two?"
                    "Three manga.":
                        $ ch13_natsuki_books = True
                        $ natsuki_approval += 1
                    "Two manga.":
                        $ ch13_natsuki_books = False
                s "Okay, sure."

            s "Okay...so then..."
            menu:
                s "Who was your sixth poem written for?"
                "Sayori.":
                    $ sayarcpoemwinner[1] = "sayori"
                    $ s_poemappeal2[2] = 1
                    $ s_appealS += 1
                "Monika.":
                    $ sayarcpoemwinner[1] = "monika"
                    $ m_poemappeal2[2] = 1
                    $ m_appealS += 1
                "Natsuki.":
                    $ sayarcpoemwinner[1] = "natsuki"
                    $ n_poemappeal2[2] = 1
                    $ n_appealS += 1
                "Yuri.":
                    $ sayarcpoemwinner[1] = "yuri"
                    $ y_poemappeal2[2] = 1
                    $ y_appealS += 1

            s "And...that's it!"
            s "I'll be seeing you..."

            $ s_name = "Sayori"
            $ quick_menu = True
            stop music fadeout 1.0
            $ persistent.custom_starts_used += 1
            $ renpy.save_persistent()
            jump ch14_skip
        "Third day of preparations.":
            s "I see..."
            menu:
                s "You have to tell me who you wrote your fifth poem for."
                "Sayori.":
                    $ sayarcpoemwinner[0] = "sayori"
                    $ s_poemappeal2[1] = 1
                    $ s_appealS += 1
                "Monika.":
                    $ sayarcpoemwinner[0] = "monika"
                    $ m_poemappeal2[1] = 1
                    $ m_appealS += 1
                "Natsuki.":
                    $ sayarcpoemwinner[0] = "natsuki"
                    $ n_poemappeal2[1] = 1
                    $ n_appealS += 1
                "Yuri.":
                    $ sayarcpoemwinner[0] = "yuri"
                    $ y_poemappeal2[1] = 1
                    $ y_appealS += 1

            s "This almost feels like an interrogation, doesn't it?"
            s "But it isn't..."
            menu:
                s "...so who did you choose to help for Inauguration Day?"
                "Sayori.":
                    $ ch13_scene = "sayori"
                "Monika.":
                    $ ch13_scene = "monika"
                "Natsuki.":
                    $ ch13_scene = "natsuki"
                "Yuri.":
                    $ ch13_scene = "yuri"
            $ ch13_name = ch13_scene.capitalize()
            s "Alright..."

            # Dumping Sayori for Natsuki
            if ch13_name == "Natsuki" and (ch12_outcome == 3 or ch12_outcome == 1) and n_appeal >= 4 and n_appealS >= 1 and sayori_confess:
                s "It's clear by this point, you're trying to appeal to Natsuki."
                s "At least, it feels like you are with all your poem choices."
                s "But even so, you..."
                s "Are you going to leave the one you chose before?"
                s "Even if you aren't going to try to be with Natsuki."
                menu:
                    s "So...are you leaving Sayori?"
                    "Yes.":
                        $ sayori_dumped = True
                        $ sayori_personality += 2
                        s "I...see."
                        s "Then..."
                        s "Sorry, it's just..."
                        s "Never mind."
                        s "I hope you two have a good time together."
                    "No.":
                        $ sayori_dumped = False
                        if sayori_personality > 0:
                            $ sayori_personality -= 1
                        s "You aren't?"
                        s "I see..."
                        s "That's good!"
                        s "Not that it matters or anything...!"
                        s "It's just..."
                        s "...just good."
            # Going On Date
            if ch13_name == "Natsuki" and (ch12_outcome == 3 or ch12_outcome == 1) and n_appeal >= 4 and n_appealS >= 1 and ((sayori_dumped and sayori_confess) or (not sayori_confess)):
                s "You were given the opportunity to go with Natsuki..."
                s "...On a date."
                menu:
                    s "Did you take that opportunity?"
                    "Yes.":
                        $ natsuki_date = True
                        s "So they're together now..."
                        s "Okay."
                    "No.":
                        $ natsuki_date = False
                        s "You didn't?"
                        s "Then what was the point of it all..."
                        s "Whatever."

            if ch13_name == "Monika":
                s "Since you went with Monika, you chose some music, right?"
                menu:
                    s "What was it?"
                    "Harmonic.":
                        $ ch13_music_type = "harmonic"
                    "Upbeat.":
                        $ ch13_music_type = "upbeat"
                    "Melancholy.":
                        $ ch13_music_type = "melancholy"
                s "Oh, alright."
            elif ch13_name == "Yuri":
                s "When you were with Yuri..."
                menu:
                    s "Did you take one of her books?"
                    "Yes.":
                        $ ch13_yuri_books = True
                        $ yuri_approval += 1
                    "No.":
                        $ ch13_yuri_books = False
                s "I see..."
            elif ch13_name == "Natsuki":
                s "At the end of the day with Natsuki..."
                menu:
                    s "Did you take three manga or just two?"
                    "Three manga.":
                        $ ch13_natsuki_books = True
                        $ natsuki_approval += 1
                    "Two manga.":
                        $ ch13_natsuki_books = False
                s "Okay, sure."

            s "Okay...so then..."
            menu:
                s "Who was your sixth poem written for?"
                "Sayori.":
                    $ sayarcpoemwinner[1] = "sayori"
                    $ s_poemappeal2[2] = 1
                    $ s_appealS += 1
                "Monika.":
                    $ sayarcpoemwinner[1] = "monika"
                    $ m_poemappeal2[2] = 1
                    $ m_appealS += 1
                "Natsuki.":
                    $ sayarcpoemwinner[1] = "natsuki"
                    $ n_poemappeal2[2] = 1
                    $ n_appealS += 1
                "Yuri.":
                    $ sayarcpoemwinner[1] = "yuri"
                    $ y_poemappeal2[2] = 1
                    $ y_appealS += 1

            s "There's just a little bit more I need to ask."
            s "Like...the book we chose in the meeting."
            s "I'm just thinking about the books everyone brought..."
            s "Just a second."
            if ch13_name == "Monika" and (monika_type == 2 or (monika_type == 1 and ch12_markov_agree)):
                $ ch14_player_choice = False
                $ ch14_player_manga = 0
                $ sayori_personality += 1
            elif ch13_name == "Sayori" or (ch13_name == "Natsuki" and ch13_natsuki_books) or (ch13_name == "Yuri" and not ch13_yuri_books):
                $ ch14_player_manga = 3
            else:
                $ ch14_player_manga = 2
                if not (ch13_name == "Yuri" and ch13_yuri_books):
                    if sayori_personality > 2:
                        $ sayori_personality += 1
            s "Okay, I think I've got it."
            menu:
                s "Do you have any idea who you voted for?"
                "Sayori." if not persistent.markov_agreed or monika_type == 0:
                    $ ch14_book_choice = "Sayori"
                    $ ch14_overall_choice = "Sayori"
                    if sayori_personality > 0:
                        $ sayori_personality -= 1
                    s "Well, that's your decision."
                "Monika.":
                    $ ch14_book_choice = "Monika"
                    $ ch14_overall_choice = "Monika"
                    s "I see..."
                "Natsuki." if not persistent.markov_agreed or monika_type == 0:
                    $ ch14_book_choice = "Natsuki"
                    $ ch14_overall_choice = "Natsuki"
                    $ natsuki_approval += 1
                    s "Natsuki? Alright..."
                "Yuri."  if not persistent.markov_agreed or monika_type == 0:
                    $ ch14_book_choice = "Yuri"
                    $ ch14_overall_choice = "Yuri"
                    $ yuri_approval += 1
                    s "Yuri? Okay."
                "Myself" if not persistent.markov_agreed or monika_type == 0:
                    $ ch14_book_choice = player
                    s "Really?"
                    if (natsuki_date and natsuki_approval > 2) or (yuri_date and yuri_approval > 2) or monika_type == 0 or (sayori_personality == 0 or (sayori_confess and not sayori_dumped)):
                        $ ch14_overall_choice = player
                        s "Well, alright..."
                    else:
                        s "I don't think anyone voted for your book..."
                        s "You volunteered to remove it, right?"
                        s "So you're going to have to choose something else."
                        menu:
                            s "Do you have any idea who you voted for after your book got removed?"
                            "Sayori." if not persistent.markov_agreed or monika_type == 0:
                                $ ch14_book_choice = "Sayori"
                                $ ch14_overall_choice = "Sayori"
                                if sayori_personality > 0:
                                    $ sayori_personality -= 1
                                s "Well, that's your decision."
                            "Monika.":
                                $ ch14_book_choice = "Monika"
                                $ ch14_overall_choice = "Monika"
                                s "I see..."
                            "Natsuki." if not persistent.markov_agreed or monika_type == 0:
                                $ ch14_book_choice = "Natsuki"
                                $ ch14_overall_choice = "Natsuki"
                                $ natsuki_approval += 1
                                s "Natsuki? Alright..."
                            "Yuri."  if not persistent.markov_agreed or monika_type == 0:
                                $ ch14_book_choice = "Yuri"
                                $ ch14_overall_choice = "Yuri"
                                $ natsuki_approval += 1
                                s "Yuri? Okay."

            s "So after the meeting you were doing preparations, right?"
            s "Or least you were going to."
            s "You read the book that was chosen instead."
            if ch13_name == "Monika" and monika_type == 0:
                s "Monika asked you a question, right?"
                s "About telling someone something."
                s "Whatever that means."
                menu:
                    s "What did you say?"
                    "Tell someone" if not persistent.markov_agreed:
                        $ ch14_m_tellsayori = True
                        s "That's good."
                        s "I wonder who she's talking about."
                    "Don't tell anyone.":
                        $ ch14_m_tellsayori = False
                        s "I see..."
                        s "Well, maybe you have your reasons."
            elif ch13_name == "Sayori" and ((sayori_personality <= 0 and not sayori_confess) or (sayori_personality <= 1 and sayori_confess)) and s_appeal == 4:
                if sayori_confess:
                    $ ch14_sayori_date_choice = True
                    s "You agreed to a date, didn't you?"
                    s "Seeing as...well, you know."
                    s "Thank you."
                else:
                    s "There was a question asked."
                    s "Do you remember?"
                    s "It was about a date."
                    menu:
                        s "Did you say yes?"
                        "Yes.":
                            $ ch14_sayori_date_choice = True
                            if sayori_personality > 0:
                                $ sayori_personality -= 1
                            s "You did?!"
                            s "I don't know what to say."
                            s "Wow..."
                        "No.":
                            $ ch14_sayori_date_choice = False
                            $ sayori_personality += 2
                            s "Oh? Really..."
                            s "I...suppose I can't control what you do."
                            s "It is your story as well."

            s "Okay...so then..."
            menu:
                s "Who was your seventh poem written for?"
                "Sayori.":
                    $ sayarcpoemwinner[2] = "sayori"
                    $ s_poemappeal2[3] = 1
                    $ s_appealS += 1
                "Monika.":
                    $ sayarcpoemwinner[2] = "monika"
                    $ m_poemappeal2[3] = 1
                    $ m_appealS += 1
                "Natsuki.":
                    $ sayarcpoemwinner[2] = "natsuki"
                    $ n_poemappeal2[3] = 1
                    $ n_appealS += 1
                "Yuri.":
                    $ sayarcpoemwinner[2] = "yuri"
                    $ y_poemappeal2[3] = 1
                    $ y_appealS += 1

            s "That's all there is, I think."
            s "I'll be seeing you..."

            $ s_name = "Sayori"
            $ quick_menu = True
            stop music fadeout 1.0
            $ persistent.custom_starts_used += 1
            $ renpy.save_persistent()
            jump ch15_skip
