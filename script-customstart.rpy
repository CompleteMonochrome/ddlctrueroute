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

    python:
        import datetime
        currentdate = datetime.date.today()
        weekrange = datetime.timedelta(days = 7)

    if ((currentdate <= (datetime.date(2018, 9, 22) + weekrange)) or (currentdate <= (datetime.date(2019, 1, 1) + weekrange))) and persistent.arc_clear[0]:
        scene menu_bg_gray_insta with Dissolve(1.0)
    else:
        scene menu_bg_insta with Dissolve(1.0)

    # Disable menu as player chooses arc
    $ quick_menu = False
    call screen arc_choose_1
    $ custom_start_arc_choice = _return
    play music mend fadeout 1.5
    $ pause(1.5)
    $ s_name = "???"
    $ style.say_dialogue = style.normal
    $ allow_skipping = True
    $ config.allow_skipping = True
    $ sayori_personality = 0
    $ m_show = True
    $ from_custom_start = True
    $ get_achievement("*Custom Start*")
    if persistent.custom_starts_used > 50:
        s "How have you used this so many times?"
        s "You've definitely experienced doing bad things, haven't you?"
        s "There's just no possible way you couldn't have with this many uses."
        s "Whatever, I won't complain about it."
    elif persistent.custom_starts_used > 20:
        s "Look, I'll be honest."
        s "I don't know what effect these starts will have on the game."
        s "Maybe it could ruin things."
        s "Maybe it could--"
        s "Forget it, let's just carry on."
    elif persistent.custom_starts_used > 10:
        s "Do I even need to say anything?"
        s "You've been here a lot."
        s "Are you exploring what happens when you mess up...?"
        s "I hope not."
    elif persistent.custom_starts_used > 5:
        s "You're getting used to this, aren't you?"
        s "You've done this enough times to have gotten the hang of it."
        s "I hope you're doing this because you want to change your mistakes."
        s "You are doing that...right?"
    elif persistent.custom_starts_used > 0:
        s "You're planning to use this for good, right?"
        s "I mean...I don't really see any other reason."
        s "Being able to change what you've done in an instant..."
        s "That's incredible, isn't it?"
    else:
        s "Um..."
        s "What is this...?"
        s "Do you suddenly get to decide when and where you start?"
        s "Wow..."
        s "This mod has it all, doesn't it?"

    # Check Special or Christmas Days
    if (currentdate <= (datetime.date(2018, 9, 22) + weekrange)) and persistent.arc_clear[0]:
        s "Uhh...hey listen."
        if persistent.did_special_event:
            s "I know you've already done this."
            s "But I'll ask again anyway."
        else:
            s "I know you've already chosen where you want to start but..."
            s "A new part in the game opened up, but only for a while."
            s "There's something going on."
            s "Do you know what that is?"
        menu:
            s "...Do you want to try this Special Day?"
            "Start the Special Day.":
                s "What are we in for...?"
                show screen tear(20, 0.1, 0.1, 0, 40)
                $ pause(0.25)
                $ special_chapter = True
                $ s_name = "Sayori"
                stop music
                $ renpy.save_persistent()
                stop sound
                jump special_chapter
            "No.":
                s "Oh, okay."
                s "Then let's get to it."
    elif (currentdate <= (datetime.date(2019, 1, 1) + weekrange)) and persistent.arc_clear[0]:
        s "Uhh...hey listen."
        if persistent.did_christmas_event:
            s "I know you've already done this."
            s "But I'll say it again anyway."
            s "There's a special event that's opened up in the game."
        else:
            s "I know you've already chosen where you want to start but..."
            s "A new part in the game opened up, but only for a while."
            s "And it's the festive season, isn't it?"
            s "I think there's going to be some celebrations if we check it out..."
            s "...So do you want to see what it's all about?"
        menu:
            s "I think it's got to do with Christmas."
            "Celebrate Christmas.":
                s "Let's see what's in store for us..."
                show screen tear(20, 0.1, 0.1, 0, 40)
                $ pause(0.25)
                $ christmas_chapter = True
                $ s_name = "Sayori"
                stop music
                $ renpy.save_persistent()
                stop sound
                jump christmas_chapter
            "No.":
                s "Oh, okay."
                s "Then let's get to it."
    else:
        s "But we have to sort out a few things first."

    call screen customstart_girlchoice("bg house","Who did you spend the weekend with?",False,True,True,True,False,False)
    if _return == 2:
        $ persistent.ch4_preparations = "Natsuki"
        $ ch4_scene = "natsuki"
    elif _return == 3:
        $ persistent.ch4_preparations = "Yuri"
        $ ch4_scene = "yuri"
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
    s "Why don't we see what you're going to do..."
    if custom_start_arc_choice == 0:
        s "Oh."
        s "I hope you realized that your saves will be deleted."
        s "So you should close the game, if you didn't want that..."
        s "Last chance..."
        s "Okay..."
        show screen tear(20, 0.1, 0.1, 0, 40)
        $ pause(0.25)
        $ s_name = "Sayori"
        stop music
        $ persistent.custom_starts_used += 1
        $ renpy.save_persistent()
        stop sound
        jump ch5_skip
    elif custom_start_arc_choice == 1:
        s "Yuri's problem, eh?"
        s "Okay, we can do this."
        menu:
            s "So, where are you starting from?"
            "Starting the Book Day.":
                $ chapter = 6
                s "I see..."
            "Continuing the Book Day.":
                $ chapter = 7
                s "Alright..."
            "Play Day.":
                $ chapter = 8
                s "Getting right to it, I guess..."
                s "You can only start from the beginning of this day."
                s "I don't know what will happen so..."
                s "Anyway...!"
    elif custom_start_arc_choice == 2:
        s "Okay..."
        s "I hope that means you helped Yuri, right?"
        s "I guess I'll find out after you answer some more questions."
        menu:
            s "Which part are you starting from?"
            "Recovery Day.":
                $ chapter = 9
            "Visit Day.":
                $ chapter = 10
            "Second Visit.":
                $ chapter = 11
            "Play Day.":
                $ chapter = 12
    elif custom_start_arc_choice == 3:
        s "...Seriously?"
        s "You've gotten this far..."
        s "I have to know what happens!"
        s "Wait...I guess I'm going to find out, aren't I?"
        menu:
            s "Where are you up to?"
            "First day of preparations.":
                $ chapter = 13
            "Second day of preparations.":
                $ chapter = 14
            "Third day of preparations.":
                $ chapter = 15
            "Inauguration Day.":
                $ chapter = 16

    # Yuri Arc
    s "Let's get started with Yuri's problem."

    # Chapter 6
    call screen customstart_girlchoice("bg club_day","Who did you spend Festival Day with?",False)
    if _return == 0:
        $ ch5_scene = "sayori"
    elif _return == 1:
        $ ch5_scene = "monika"
    elif _return == 2:
        $ ch5_scene = "natsuki"
    elif _return == 3:
        $ ch5_scene = "yuri"
    $ ch5_name = ch5_scene.capitalize()

    s "Okay..."

    call screen customstart_girlchoice("bg notebook","Who did you write your first poem for?",True)
    if _return == 0:
        $ newpoemwinner[0] = "sayori"
        $ s_poemappeal[5] = 1
        $ s_appeal += 1
    elif _return == 1:
        $ newpoemwinner[0] = "monika"
        $ m_poemappeal[5] = 1
        $ m_appeal += 1
    elif _return == 2:
        $ newpoemwinner[0] = "natsuki"
        $ n_poemappeal[5] = 1
        $ n_appeal += 1
    elif _return == 3:
        $ newpoemwinner[0] = "yuri"
        $ y_poemappeal[5] = 1
        $ y_appeal += 1

    if chapter == 6:
        s "Well...alright."
        s "I guess I'll be seeing you."
        show screen tear(20, 0.1, 0.1, 0, 40)
        $ pause(0.25)
        $ s_name = "Sayori"
        stop music
        $ persistent.custom_starts_used += 1
        $ renpy.save_persistent()
        stop sound
        jump ch6_skip

    # Chapter 7
    $ bad_choice_first = False
    s "Let's keep going."

    call screen customstart_girlchoice("bg notebook","Who did you write your second poem for?",True)
    if _return == 0:
        $ newpoemwinner[1] = "sayori"
        $ s_poemappeal[6] = 1
        $ s_appeal += 1
    elif _return == 1:
        $ newpoemwinner[1] = "monika"
        $ m_poemappeal[6] = 1
        $ m_appeal += 1
    elif _return == 2:
        $ newpoemwinner[1] = "natsuki"
        $ n_poemappeal[6] = 1
        $ n_appeal += 1
    elif _return == 3:
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

    if chapter == 7:
        s "..."
        s "That's it."
        s "I'll see you when I see you..."
        show screen tear(20, 0.1, 0.1, 0, 40)
        $ pause(0.25)
        $ s_name = "Sayori"
        $ quick_menu = True
        stop music
        $ persistent.custom_starts_used += 1
        $ renpy.save_persistent()
        stop sound
        jump ch7_skip

    # Chapter 8
    s "Alright, sure."

    if read_book and persistent.ch6_task[2]:
        $ persistent.ch6_task[2] = False
        $ yuri_approval += 1
        $ read_book = True
        $ did_all_tasks = True
        if newpoemwinner[1] == "natsuki":
            $ natsuki_approval += 1
    elif read_book:
        $ yuri_approval += 1
        $ read_book = True
        $ did_all_tasks = False
    else:
        $ yuri_approval += 1
        $ read_book = False
        $ did_all_tasks = False
        if newpoemwinner[1] == "natsuki":
            $ natsuki_approval += 1

    call screen customstart_girlchoice("bg corridor","Who did you choose to read with?",False)
    if _return == 0:
        $ needs_to_read = True
        $ ch7_scene = "sayori"
        $ ch7_name = ch7_scene.capitalize()
        $ yuri_approval -= 1
    elif _return == 1:
        $ needs_to_read = False
        $ ch7_scene = "monika"
        $ ch7_name = ch7_scene.capitalize()
        $ yuri_approval -= 1
    elif _return == 2:
        $ needs_to_read = False
        $ ch7_scene = "natsuki"
        $ ch7_name = ch7_scene.capitalize()
        $ yuri_approval -= 1
        $ natsuki_approval += 1
    elif _return == 3:
        $ needs_to_read = True
        $ ch7_scene = "yuri"
        $ ch7_name = ch7_scene.capitalize()
        if did_all_tasks or read_book:
            $ yuri_approval = 4
        else:
            $ yuri_approval = 3

    if chapter == 8:
        s "..."
        s "So this is it."
        s "I guess I'll see you on the other side..."
        s "Good luck!"
        show screen tear(20, 0.1, 0.1, 0, 40)
        $ pause(0.25)
        $ s_name = "Sayori"
        $ quick_menu = True
        stop music
        $ persistent.custom_starts_used += 1
        $ renpy.save_persistent()
        stop sound
        jump ch8_redirect

    # Natsuki Arc
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

    # Chapter 9
    s "Now..."
    s "It seems we're in Natsuki's problem."
    s "So let's get this over with."

    call screen customstart_girlchoice("bg notebook","Who did you write your third poem for?",True)
    if _return == 0:
        $ newpoemwinner[2] = "sayori"
        $ s_poemappeal[8] = 1
        $ s_appeal += 1
    elif _return == 1:
        $ newpoemwinner[2] = "monika"
        $ m_poemappeal[8] = 1
        $ m_appeal += 1
    elif _return == 2:
        $ newpoemwinner[2] = "natsuki"
        $ n_poemappeal[8] = 1
        $ n_appeal += 1
    elif _return == 3:
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

    if chapter == 9:
        s "So this is where you're starting from?"
        s "..."
        s "Alright."
        s "I guess I will be seeing you."
        show screen tear(20, 0.1, 0.1, 0, 40)
        $ pause(0.25)
        $ s_name = "Sayori"
        $ quick_menu = True
        stop music
        $ persistent.custom_starts_used += 1
        $ renpy.save_persistent()
        stop sound
        jump ch9_skip

    # Chapter 10
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

    if chapter == 10:
        s "Well..."
        s "I hope you enjoy today."
        s "I don't know what's going to happen..."
        s "I guess I'll just be getting the memories of whatever you chose, right?"
        s "..."
        s "Goodbye."
        show screen tear(20, 0.1, 0.1, 0, 40)
        $ pause(0.25)
        $ s_name = "Sayori"
        $ quick_menu = True
        stop music
        $ persistent.custom_starts_used += 1
        $ renpy.save_persistent()
        stop sound
        jump ch10_skip

    # Chapter 11
    $ insert_dadsuki_character()
    s "Hmm..."
    s "Apparently you visited Natsuki's house twice!"
    s "What did you do the first time?"
    call screen customstart_twobgchoice("Did you check closed rooms?",
        "mod_assets/images/bg/n_house_day.png","Checked closed rooms",
        "mod_assets/images/bg/n_bedroom_day.png","Stayed in Natsuki's room",False)
    if _return == 0:
        $ natsuki_approval += 1
        s "I see."
        s "That seems like an invasion of privacy but..."
        s "I'm not judging! It's probably important."
        call screen customstart_fourbgchoice("Which rooms did you check?",
            "mod_assets/images/bg/n_dadroom.png","First room upstairs",
            "mod_assets/images/bg/n_hitroom.png","Second room upstairs",
            "mod_assets/images/bg/n_oldlivingroom.png","Closed room downstairs",
            "mod_assets/images/bg/n_livingroom.png","Living room",True)
        $ persistent.natsuki_house = _return
        $ renpy.save_persistent()
        $ talkabout_natsuki_house = persistent.natsuki_house
    elif _return == 1:
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
    $ renpy.save_persistent()

    # Yuri has a fresh bandage
    $ y_clean_bandages = True

    if chapter == 11:
        s "I'll be seeing you..."
        s "I hope..."
        show screen tear(20, 0.1, 0.1, 0, 40)
        $ pause(0.25)
        $ s_name = "Sayori"
        $ quick_menu = True
        stop music
        $ persistent.custom_starts_used += 1
        $ renpy.save_persistent()
        stop sound
        jump ch11_skip

    # Chapter 12
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

    s "So let's keep going."
    call screen customstart_girlchoice("bg notebook","Who did you write your fourth poem for?",True)
    if _return == 0:
        $ natarcpoemwinner[0] = "sayori"
        $ s_poemappeal2[0] = 1
        $ s_appeal += 1
    elif _return == 1:
        $ natarcpoemwinner[0] = "monika"
        $ m_poemappeal2[0] = 1
        $ m_appeal += 1
    elif _return == 2:
        $ natarcpoemwinner[0] = "natsuki"
        $ n_poemappeal2[0] = 1
        $ n_appeal += 1
    elif _return == 3:
        $ natarcpoemwinner[0] = "yuri"
        $ y_poemappeal2[0] = 1
        $ y_appeal += 1

    if chapter == 12:
        s "I guess this is it."
        s "I hope we can get Natsuki through this with the best outcome."
        show screen tear(20, 0.1, 0.1, 0, 40)
        $ pause(0.25)
        $ s_name = "Sayori"
        $ quick_menu = True
        stop music
        $ persistent.custom_starts_used += 1
        $ renpy.save_persistent()
        stop sound
        jump ch12_skip

    # Sayori Arc
    s "Haha...now we're at the start of {i}this{/i} problem."
    s "But we have to figure out how Natsuki's problem ended first."

    # Define Monika Type
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

    # Check if Haruki exists
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
    # Check Natsuki Arc Ending
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

    # Chapter 13
    # Check if Markov Agreed
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
                if not persistent.markov_agreed:
                    s "Are you positive?"
                    s "Once you make this decision, you can {i}never{/i} take it back."
                    menu:
                        s "You accepted the offer?"
                        "Yes.":
                            $ ch12_markov_agree = True
                            s "Great."
                        "No.":
                            $ ch12_markov_agree = False
                            s "Disappointing but not unexpected."
                else:
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

    call screen customstart_girlchoice("bg notebook","Who did you write your fifth poem for?",True)
    if _return == 0:
        $ sayarcpoemwinner[0] = "sayori"
        $ s_poemappeal2[1] = 1
        $ s_appealS += 1
    elif _return == 1:
        $ sayarcpoemwinner[0] = "monika"
        $ m_poemappeal2[1] = 1
        $ m_appealS += 1
    elif _return == 2:
        $ sayarcpoemwinner[0] = "natsuki"
        $ n_poemappeal2[1] = 1
        $ n_appealS += 1
    elif _return == 3:
        $ sayarcpoemwinner[0] = "yuri"
        $ y_poemappeal2[1] = 1
        $ y_appealS += 1

    if chapter == 13:
        s "And...that's it!"
        s "I'll be seeing you..."
        show screen tear(20, 0.1, 0.1, 0, 40)
        $ pause(0.25)
        $ s_name = "Sayori"
        $ quick_menu = True
        stop music
        $ persistent.custom_starts_used += 1
        $ renpy.save_persistent()
        stop sound
        jump ch13_skip

    # Chapter 14
    s "This almost feels like an interrogation, doesn't it?"
    s "But it isn't..."
    call screen customstart_girlchoice("bg corridor","Who are you with for Inauguration Day?",False)
    if _return == 0:
        $ ch13_scene = "sayori"
    elif _return == 1:
        $ ch13_scene = "monika"
    elif _return == 2:
        $ ch13_scene = "natsuki"
    elif _return == 3:
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

    # Choices for who you helped for Inauguration Day
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
    call screen customstart_girlchoice("bg notebook","Who did you write your sixth poem for?",True)
    if _return == 0:
        $ sayarcpoemwinner[1] = "sayori"
        $ s_poemappeal2[2] = 1
        $ s_appealS += 1
    elif _return == 1:
        $ sayarcpoemwinner[1] = "monika"
        $ m_poemappeal2[2] = 1
        $ m_appealS += 1
    elif _return == 2:
        $ sayarcpoemwinner[1] = "natsuki"
        $ n_poemappeal2[2] = 1
        $ n_appealS += 1
    elif _return == 3:
        $ sayarcpoemwinner[1] = "yuri"
        $ y_poemappeal2[2] = 1
        $ y_appealS += 1

    if chapter == 14:
        s "And...that's it!"
        s "I'll be seeing you..."
        show screen tear(20, 0.1, 0.1, 0, 40)
        $ pause(0.25)
        $ s_name = "Sayori"
        $ quick_menu = True
        stop music
        $ persistent.custom_starts_used += 1
        $ renpy.save_persistent()
        stop sound
        jump ch14_skip

    # Chapter 15
    s "Almost there, I promise."
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
    call screen customstart_girlchoice("bg club_day","Which person's book did you vote for?",False,not (not persistent.markov_agreed or monika_type == 0),not (not persistent.markov_agreed or monika_type == 0),False,not (not persistent.markov_agreed or monika_type == 0),not (not persistent.markov_agreed or monika_type == 0))
    if _return == 0:
        $ ch14_book_choice = "Sayori"
        $ ch14_overall_choice = "Sayori"
        if sayori_personality > 0:
            $ sayori_personality -= 1
        s "Well, that's your decision."
    elif _return == 1:
        $ ch14_book_choice = "Monika"
        $ ch14_overall_choice = "Monika"
        s "I see..."
    elif _return == 2:
        $ ch14_book_choice = "Natsuki"
        $ ch14_overall_choice = "Natsuki"
        $ natsuki_approval += 1
        s "Natsuki? Alright..."
    elif _return == 3:
        $ ch14_book_choice = "Yuri"
        $ ch14_overall_choice = "Yuri"
        $ yuri_approval += 1
        s "Yuri? Okay."
    elif _return == 4:
        $ ch14_book_choice = player
        s "Really?"
        if (natsuki_date and natsuki_approval > 2) or (yuri_date and yuri_approval > 2) or monika_type == 0 or (sayori_personality == 0 or (sayori_confess and not sayori_dumped)):
            $ ch14_overall_choice = player
            s "Well, alright..."
        else:
            s "I don't think anyone voted for your book..."
            s "You volunteered to remove it, right?"
            s "So you're going to have to choose something else."
            call screen customstart_girlchoice("bg club_day","Which person's book did you vote for?",False,False,not (not persistent.markov_agreed or monika_type == 0),False,not (not persistent.markov_agreed or monika_type == 0),not (not persistent.markov_agreed or monika_type == 0))
            if _return == 0:
                $ ch14_book_choice = "Sayori"
                $ ch14_overall_choice = "Sayori"
                if sayori_personality > 0:
                    $ sayori_personality -= 1
                s "Well, that's your decision."
            elif _return == 1:
                $ ch14_book_choice = "Monika"
                $ ch14_overall_choice = "Monika"
                s "I see..."
            elif _return == 2:
                $ ch14_book_choice = "Natsuki"
                $ ch14_overall_choice = "Natsuki"
                $ natsuki_approval += 1
                s "Natsuki? Alright..."
            elif _return == 3:
                $ ch14_book_choice = "Yuri"
                $ ch14_overall_choice = "Yuri"
                $ yuri_approval += 1
                s "Yuri? Okay."

    s "So after the meeting you were doing preparations, right?"
    s "Or at least you were going to."
    if ch14_book_choice != ch14_overall_choice:
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
    call screen customstart_girlchoice("bg notebook","Who did you write your seventh poem for?",True)
    if _return == 0:
        $ sayarcpoemwinner[2] = "sayori"
        $ s_poemappeal2[3] = 1
        $ s_appealS += 1
    elif _return == 1:
        $ sayarcpoemwinner[2] = "monika"
        $ m_poemappeal2[3] = 1
        $ m_appealS += 1
    elif _return == 2:
        $ sayarcpoemwinner[2] = "natsuki"
        $ n_poemappeal2[3] = 1
        $ n_appealS += 1
    elif _return == 3:
        $ sayarcpoemwinner[2] = "yuri"
        $ y_poemappeal2[3] = 1
        $ y_appealS += 1

    if chapter == 15:
        s "That's all there is, I think."
        s "I'll be seeing you..."
        show screen tear(20, 0.1, 0.1, 0, 40)
        $ pause(0.25)
        $ s_name = "Sayori"
        $ quick_menu = True
        stop music
        $ persistent.custom_starts_used += 1
        $ renpy.save_persistent()
        stop sound
        jump ch15_skip

    # Chapter 16
    $ ch15_ay_seen = True

    s "So this is it, huh?"
    s "After everything, we're finally here."
    s "We're at the beginning of the end..."
    s "But that's not a bad thing!"
    s "The end of something is the beginning of another."
    s "So don't be sad that you're approaching the end."
    s "It just means you get to experience something new."
    s "Anyway..."

    if ch13_name == "Natsuki":
        if monika_type == 0 or natsuki_date:
            $ natsuki_approval += 1
        else:
            if natsuki_approval > 0:
                $ natsuki_approval -= 1
    elif ch13_name == "Monika":
        if monika_type == 0 or (ch12_markov_agree and monika_type == 1):
            s "Seeing as you chose to be with Monika..."
            s "Did you go to the mall together?"
            s "Or by yourselves?"
            menu:
                "We went to the mall..."
                "Together.":
                    $ ch15_m_together = True
                "By ourselves.":
                    $ ch15_m_together = False
            s "Okay."
    elif ch13_name == "Sayori":
        $ ch15_s_together = False
        if ch14_sayori_date_choice and sayori_personality == 0:
            s "You were with Sayori, right?"
            s "Up until now, you've tried to please her."
            s "But..."
            s "If you really cared, you would experience it yourself."
            s "I don't know your true intentions."
            s "So if you really want to be together...then prove it."

    if chapter == 16:
        # Set to 15 to prevent error after poem game message
        $ chapter = 15
        s "That's it, isn't it?"
        s "Now all that's left is to see what consequences your actions have done..."
        show screen tear(20, 0.1, 0.1, 0, 40)
        $ pause(0.25)
        $ s_name = "Sayori"
        $ quick_menu = True
        stop music
        $ persistent.custom_starts_used += 1
        $ renpy.save_persistent()
        stop sound
        jump ch16_skip
