label christmas_chapter:
    $ monika_type = 1
    $ ch12_markov_agree = True
    scene black
    $ s_name = "???"
    play music t5christmas fadein 5.0

    scene black with dissolve_scene_full
    $ persistent.did_christmas_event = True
    $ special_chapter = False
    $ pause(1.0)
    $ style.say_window = style.window
    $ renpy.utter_restart()
    return