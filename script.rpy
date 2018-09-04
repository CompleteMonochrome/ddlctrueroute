


label start:


    $ anticheat = persistent.anticheat


    $ chapter = 0


    $ _dismiss_pause = config.developer

    # Names before we meet them
    $ s_name = "???"
    $ m_name = "Girl 3"
    $ n_name = "Girl 2"
    $ y_name = "Girl 1"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True

    if persistent.playthrough == 0:
        $ chapter = 0
        call ch0_main


        call poem


        $ chapter = 1
        call ch1_main
        call poemresponse_start
        call ch1_end


        call poem


        $ chapter = 2
        call ch2_main
        call poemresponse_start
        call ch2_end


        call poem


        $ chapter = 3
        call ch3_main
        call poemresponse_start
        call ch3_end

        # Check if player cares a lot about Sayori
        if sayori_save == 3:
            call ch3_mainb
            if renpy.exists("script-saturday.txt.txt"):
                python:
                    try: os.remove(config.basedir + "/game/script-saturday.txt.txt")
                    except: pass
                    try: renpy.file(config.basedir + "/game/script-saturday.txt")
                    except: open(config.basedir + "/game/script-saturday.txt", "w").write("VGhhbmsgeW91IGZvciBnaXZpbmcgbWUgdGhpcyBjaGFuY2UuDQpJIGhhdmUgdG8gc2FjcmlmaWNlIG15c2VsZiwgZm9yIHlvdSBhbmQgU2F5b3JpLg0KVGhpcyBpcyBqdXN0IG15IHJldHJpYnV0aW9uLCBJJ2xsIGFsd2F5cyBsb3ZlIHlvdS4uLg==")
                call ch3_mainc_name
            elif renpy.exists("script-saturday.txt") or renpy.exists("script-saturday.rtf"):
                python:
                    try: os.remove(config.basedir + "/game/script-saturday.txt")
                    except: pass
                    try: os.remove(config.basedir + "/game/script-saturday.rtf")
                    except: pass
                    try: renpy.file(config.basedir + "/game/script-saturday.txt")
                    except: open(config.basedir + "/game/script-saturday.txt", "w").write("VGhhbmsgeW91IGZvciBnaXZpbmcgbWUgdGhpcyBjaGFuY2UuDQpJIGhhdmUgdG8gc2FjcmlmaWNlIG15c2VsZiwgZm9yIHlvdSBhbmQgU2F5b3JpLg0KVGhpcyBpcyBqdXN0IG15IHJldHJpYnV0aW9uLCBJJ2xsIGFsd2F5cyBsb3ZlIHlvdS4uLg==")
                call ch3_mainc
            else:
                jump ch3_skip_saturday
        # If player didn't care about Sayori enough but appealed to Monika
        elif monika_appeal[2]:
            call ch3_maind
            if renpy.exists("script-saturday.txt.txt"):
                python:
                    try: os.remove(config.basedir + "/game/script-saturday.txt.txt")
                    except: pass
                    try: renpy.file(config.basedir + "/game/script-saturday.txt")
                    except: open(config.basedir + "/game/script-saturday.txt", "w").write("SXQncyBqdXN0IHVzIHR3bywgZm9yZXZlciBhbmQgZXZlci4NCkZvcmV2ZXIuDQpJIGxvdmUgeW91Lg==")
                call ch3_maine_name
            elif renpy.exists("script-saturday.txt") or renpy.exists("script-saturday.rtf"):
                python:
                    try: os.remove(config.basedir + "/game/script-saturday.txt")
                    except: pass
                    try: os.remove(config.basedir + "/game/script-saturday.rtf")
                    except: pass
                    try: renpy.file(config.basedir + "/game/script-saturday.txt")
                    except: open(config.basedir + "/game/script-saturday.txt", "w").write("SXQncyBqdXN0IHVzIHR3bywgZm9yZXZlciBhbmQgZXZlci4NCkZvcmV2ZXIuDQpJIGxvdmUgeW91Lg==")
                call ch3_maine
            else:
                jump ch3_skip_saturday

        label ch3_skip_saturday:
        $ chapter = 4
        call ch4_main
        if not visited_sayori_sat:
            python:
                try: renpy.file(config.basedir + "/hxppy thxughts.png")
                except: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())

        $ chapter = 5
        # Actually Handled by Splash Screen if Saturday exists
        label ch5_skip:
        $ persistent.ch6_task = [False,False,False]
        $ quick_menu = True
        $ style.say_dialogue = style.normal
        $ allow_skipping = True
        $ config.allow_skipping = True
        if persistent.monika_change and not persistent.monika_gone:
            jump ch5_mainc
        elif persistent.monika_change and persistent.monika_gone:
            jump ch5_mainb
        else:
            call ch5_main

        # Super Messy Looking Code but I wanted everything to be under playthrough == 0
        call endgame
        jump endgame_skip

        # Redirect from Good Ending
        label ch5_good_redirect:
        call poem (False)

        label ch6_skip:
        $ chapter = 6
        call ch6_main
        call poemresponse_start_new
        call ch6_end

        # Here because of jump usage in ch6_end
        label ch6_after:
        if persistent.ch6_task[2]:
            call poem
        elif read_book and not persistent.ch6_task[2]:
            call poem(True,10)
        else:
            call poem


        label ch7_skip:
        $ chapter = 7
        call ch7_main
        call poemresponse_start_new
        call ch7_end


        label ch8_redirect:
        $ chapter = 8
        call ch8_main
        call ch8_end

        call poem


        label ch9_skip:
        $ chapter = 9
        call ch9_main
        if not yuri_date:
            call poemresponse_start_new
        call ch9_end

        label ch10_skip:
        $ chapter = 10
        call ch10_main
        call ch10_end

        label ch11_skip:
        $ chapter = 11
        call ch11_main
        call ch11_end

        if ch11_badpoem:
            call poem(True,10)
        else:
            call poem

        label ch12_skip:
        $ chapter = 12
        call ch12_main
        call poemresponse_start_new
        call ch12_play
        call ch12_end

        call poem


        label ch13_skip:
        $ chapter = 13
        call ch13_main
        call poemresponse_start_new
        call ch13_end

        call poem


        label ch14_skip:
        $ chapter = 14
        call ch14_main
        call poemresponse_start_new
        call ch14_end

        call poem


        label ch15_skip:
        $ chapter = 15
        call ch15_main
        call poemresponse_start_new
        call ch15_end

        label endgame_skip:
        $ renpy.full_restart(transition=None, label="splashscreen")
        return

    elif persistent.playthrough == 1:
        $ chapter = 0
        call ch100_main
        jump playthrough2


    elif persistent.playthrough == 2:

        $ chapter = 0
        call ch200_main

        label playthrough2:


            call poem
            if persistent.dialogue_change[0]:
                python:
                    try: renpy.file(config.basedir + "/I KNOW YOU CAN HEAR ME.txt")
                    except: open(config.basedir + "/I KNOW YOU CAN HEAR ME.txt", "wb").write(renpy.file("I KNOW YOU CAN HEAR ME.txt").read())
            else:
                python:
                    try: renpy.file(config.basedir + "/CAN YOU HEAR ME.txt")
                    except: open(config.basedir + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())


            $ chapter = 1
            call ch201_main
            call poemresponse_start
            call ch201_end


            call poem (False)
            python:
                try: renpy.file(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
                except: open(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())


            $ chapter = 2
            call ch202_main
            call poemresponse_start
            call ch202_end


            call poem (False)


            $ chapter = 3
            call ch203_main
            if y_appeal >= 3:
                call poemresponse_start2
            else:
                call poemresponse_start

            if persistent.demo:
                stop music fadeout 2.0
                scene black with dissolve_cg
                "End of demo"
                return

            call ch203_end

            return

    elif persistent.playthrough == 3:
        jump ch30_main

    elif persistent.playthrough == 4:

        $ chapter = 0
        call ch40_main
        jump credits

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
