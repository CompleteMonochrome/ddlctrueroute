init python:
    process_list = []
    currentuser = ""
    if renpy.windows:
        try:
            process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
        except:
            pass
        try:
            for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                user = os.environ.get(name)
                if user:
                    currentuser = user
        except:
            pass

init python:
    menu_trans_time = 1
    splash_message_default = "This game is not suitable for children or those who are easily disturbed.\nThis mod is a fan work, not affiliated with Team Salvato."
    splash_messages = [
    "You are my sunshine,\nMy only sunshine",
    "I missed you.",
    "Play with me",
    "It's just a game, mostly.",
    "This game is not suitable for children\nor those who are easily disturbed?",
    "sdfasdklfgsdfgsgoinrfoenlvbd",
    "null",
    "I have granted kids to hell",
    "PM died for this.",
    "It was only partially your fault.",
    "This game is not suitable for children\nor those who are easily dismembered.",
    "Don't forget to backup Monika's character file."
    ]
    splash_monika_last = "Goodbye, I will love you forever."

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

image menu_art_y_locked:
    subpixel True
    "mod_assets/gui/menu_art_y_locked.png"
    xcenter 600
    ycenter 335
    zoom 0.60

image menu_art_n_locked:
    subpixel True
    "mod_assets/gui/menu_art_n_locked.png"
    xcenter 750
    ycenter 385
    zoom 0.58

image menu_art_s_locked:
    subpixel True
    "mod_assets/gui/menu_art_s_locked.png"
    xcenter 510
    ycenter 500
    zoom 0.68

image menu_art_m_locked:
    subpixel True
    "mod_assets/gui/menu_art_m_locked.png"
    xcenter 1000
    ycenter 640
    zoom 1.0

image menu_art_m_evil:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)
    30.0
    "mod_assets/gui/menu_art_m_evil.png"
    0.3
    "gui/menu_art_m.png"

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

image menu_logo:
    "gui/logo.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

image menu_logo_mod:
    "mod_assets/gui/mod_logo.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0


image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"


label splashscreen:

    python:
        process_list = []
        currentuser = ""
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
            except:
                pass


    python:
        firstrun = ""
        try:
            firstrun = renpy.file("firstrun").read(1)
        except:
            with open(config.basedir + "/game/firstrun", "wb") as f:
                pass
    if not firstrun:
        if persistent.first_run and (config.version == persistent.oldversion or persistent.autoload == "postcredits_loop"):
            $ quick_menu = False
            scene black
            menu:
                "A previous save file has been found. Would you like to delete your save data and start over?"
                "Yes, delete my existing data.":
                    "Deleting save data...{nw}"
                    python:
                        delete_character("ûüýþ")
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "No, continue where I left off.":
                    $ restore_relevant_characters()

        python:
            if not firstrun:
                try:
                    with open(config.basedir + "/game/firstrun", "w") as f:
                        f.write("1")
                except:
                    renpy.jump("readonly")

    if config.version != persistent.oldversion:
        $ restore_relevant_characters()
        $ persistent.oldversion = config.version
        $ renpy.save_persistent()

    if not persistent.first_run:
        python:
            restore_all_characters()
            restore_normal_characters()
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        "This is a Doki Doki Literature Club fan game that is not affiliated with Team Salvato."
        "It is designed to be played only after the official game has been completed."
        "You can download Doki Doki Literature Club at: http://ddlc.moe"
        "Individuals suffering from anxiety or depression may not have a safe experience playing this game. For content warnings, please visit: http://ddlc.moe/warning.html"
        menu:
            "By playing Doki Doki Literature Club, you agree that you are at least 13 years of age, and you consent to your exposure of highly disturbing content."
            "I agree.":
                pass
        $ persistent.first_run = True
        scene tos2
        with Dissolve(1.5)
        pause 1.0
        scene white


    python:
        s_kill_early = None
        if persistent.playthrough == 0:
            try: renpy.file("../characters/sayori.chr")
            except: s_kill_early = True
            if persistent.sayori_end_early:
                s_kill_early = True
        if not s_kill_early:
            if persistent.playthrough <= 2 and persistent.playthrough != 0:
                try: renpy.file("../characters/monika.chr")
                except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
            if persistent.playthrough <= 1 or persistent.playthrough == 4:
                try: renpy.file("../characters/natsuki.chr")
                except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
                try: renpy.file("../characters/yuri.chr")
                except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
            if persistent.playthrough == 4:
                try: renpy.file("../characters/sayori.chr")
                except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())

    if not persistent.special_poems:
        python hide:
            persistent.special_poems = [0,0,0]
            a = range(1,12)
            for i in range(3):
                b = renpy.random.choice(a)
                persistent.special_poems[i] = b
                a.remove(b)

    $ basedir = config.basedir.replace('\\', '/')



    if persistent.autoload:
        jump autoload



    $ config.allow_skipping = False

    if persistent.playthrough == 2 and not persistent.seen_ghost_menu and renpy.random.randint(0, 63) == 0:
        show black
        $ config.main_menu_music = audio.ghostmenu
        $ persistent.seen_ghost_menu = True
        $ persistent.ghost_menu = True
        $ renpy.music.play(config.main_menu_music)
        $ pause(1.0)
        show end with dissolve_cg
        $ pause(3.0)
        $ config.allow_skipping = True
        return


    if s_kill_early:
        show black
        play music "bgm/s_kill_early.ogg"
        $ pause(1.0)
        show end with dissolve_cg
        $ pause(3.0)
        scene white
        show expression "images/cg/s_kill_early.png":
            yalign -0.05
            xalign 0.25
            dizzy(1.0, 4.0, subpixel=False)
        show white as w2:
            choice:
                ease 0.25 alpha 0.1
            choice:
                ease 0.25 alpha 0.125
            choice:
                ease 0.25 alpha 0.15
            choice:
                ease 0.25 alpha 0.175
            choice:
                ease 0.25 alpha 0.2
            choice:
                ease 0.25 alpha 0.225
            choice:
                ease 0.25 alpha 0.25
            choice:
                ease 0.25 alpha 0.275
            choice:
                ease 0.25 alpha 0.3
            pass
            choice:
                pass
            choice:
                0.25
            choice:
                0.5
            choice:
                0.75
            repeat
        show noise:
            alpha 0.1
        with Dissolve(1.0)
        show expression Text("Now everyone can be happy.", style="sayori_text"):
            xalign 0.8
            yalign 0.5
            alpha 0.0
            600
            linear 60 alpha 0.5
        pause
        $ renpy.quit()


    show white
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    if persistent.playthrough == 0 and persistent.monika_change and not persistent.monika_gone:
        if persistent.markov_agreed:
            $ config.main_menu_music = audio.t1c
        else:
            $ config.main_menu_music = audio.t1m
    else:
        $ config.main_menu_music = audio.t1
    $ renpy.music.play(config.main_menu_music)
    $ starttime = datetime.datetime.now()
    show intro with Dissolve(0.5, alpha=True)
    $ pause(3.0 - (datetime.datetime.now() - starttime).total_seconds())
    hide intro with Dissolve(max(0, 3.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    if persistent.playthrough == 0 and persistent.monika_gone and persistent.monika_splash_message:
        $ splash_message = splash_monika_last
        $ persistent.monika_splash_message = False
    elif persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(max(0, 4.0 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    $ pause(6.0 - (datetime.datetime.now() - starttime).total_seconds())
    hide splash_warning with Dissolve(max(0, 6.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    $ pause(6.5 - (datetime.datetime.now() - starttime).total_seconds())
    $ config.allow_skipping = True
    return

label after_load:
    # For some reason we need to set these
    if not hasattr(store, 'ch11_badpoem'):
        $ ch11_badpoem = False
    if not hasattr(store,'monika_type'):
        $ monika_type = 2
    if not hasattr(store,'ch12_natsuki_help'):
        $ ch12_natsuki_help = True
    if not hasattr(store,'ch12_natsuki_reluctance'):
        $ ch12_natsuki_reluctance = 1
    if not hasattr(store,'ch12_haruki_tried'):
        $ ch12_haruki_tried = False
    if not hasattr(store,'ch12_markov_agree'):
        $ ch12_markov_agree = False
    if not hasattr(store,'normal_haruki'):
        $ normal_haruki = False
    if not hasattr(store,'ch12_outcome'):
        $ ch12_outcome = 0
    if not hasattr(store,'n_appealS'):
        $ n_appealS = 0
    if not hasattr(store,'s_appealS'):
        $ s_appealS = 0
    if not hasattr(store,'y_appealS'):
        $ y_appealS = 0
    if not hasattr(store,'m_appealS'):
        $ m_appealS = 0
    if not hasattr(store,'m_appealS'):
        $ m_appealS = 0
    if not hasattr(store,'m_hairdown_poemglitch'):
        $ m_hairdown_poemglitch = False
    if not hasattr(store,'sayarcpoemwinner'):
        $ sayarcpoemwinner = ['sayori', 'sayori', 'sayori']
    if not hasattr(store,'ch13poemwinner'):
        $ ch13poemwinner = "Sayori"
    if not hasattr(store,'ch13_scene'):
        $ ch13_scene = "sayori"
    if not hasattr(store,'ch13_name'):
        $ ch13_name = "Sayori"
    if not hasattr(store,'ch13_music_type'):
        $ ch13_music_type = "harmonic"
    if not hasattr(store,'ch13_yuri_books'):
        $ ch13_yuri_books = False
    if not hasattr(store,'ch13_natsuki_books'):
        $ ch13_natsuki_books = False
    if not hasattr(store,'ch13_cleaneye'):
        $ ch13_cleaneye = False
    if not hasattr(store,'natsuki_outing'):
        $ natsuki_outing = False
    if not hasattr(store,'ch14poemwinner'):
        $ ch14poemwinner = "Sayori"
    if not hasattr(store,'ch14markovikatell'):
        $ ch14markovikatell = False
    if not hasattr(store,'ch14_player_choice'):
        $ ch14_player_choice = True
    if not hasattr(store,'ch14_player_manga'):
        $ ch14_player_manga = 0
    if not hasattr(store,'ch14_twonovels_tell'):
        $ ch14_twonovels_tell = False
    if not hasattr(store,'ch14_book_choice'):
        $ ch14_book_choice = "Sayori"
    if not hasattr(store,'ch14_natyuri_choice'):
        $ ch14_natyuri_choice = ["Natsuki", "Yuri"]
    if not hasattr(store,'ch14_votes'):
        $ ch14_votes = [0, 0, 0, 0, 0]
    if not hasattr(store,'ch14_overall_choice'):
        $ ch14_overall_choice = "Sayori"
    if not hasattr(store,'cl_name'):
        $ cl_name = "Mysterious Clerk"
    if not hasattr(store, 'ch14_sayori_date_choice'):
        $ ch14_sayori_date_choice = False
    if not hasattr(store, 'chapter_names'):
        $ chapter_names = ["An Ordinary Day","The Literature Club","The Meeting","You Three","Before The Festival","The Festival","A New Beginning","Portrait of Markov","The Play","Familiar Face","What's Wrong?","Before the Storm","A New Play","Preparations","Bring Your Book!","A Dilemma","???","???","???","???","???","???"]
    if not hasattr(store, 'sInList'):
        $ sInList = False
    if not hasattr(store, 'nInList'):
        $ nInList = False
    if not hasattr(store, 'yInList'):
        $ yInList = False
    if not hasattr(store, 'mInList'):
        $ mInList = False

    # Because of a change in an update - remove with 0.9.4f
    if ch14_book_choice == "Player":
        $ ch14_book_choice = player
    if ch14_natyuri_choice[0] == "Player":
        $ ch14_natyuri_choice[0] = player
    if ch14_natyuri_choice[1] == "Player":
        $ ch14_natyuri_choice[1] = player

    # Normal Stuff
    if persistent.playthrough == 0:
        $ restore_all_characters()
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
        if persistent.yuri_kill >= 1380:
            $ persistent.yuri_kill = 1440
        elif persistent.yuri_kill >= 1180:
            $ persistent.yuri_kill = 1380
        elif persistent.yuri_kill >= 1120:
            $ persistent.yuri_kill = 1180
        elif persistent.yuri_kill >= 920:
            $ persistent.yuri_kill = 1120
        elif persistent.yuri_kill >= 720:
            $ persistent.yuri_kill = 920
        elif persistent.yuri_kill >= 660:
            $ persistent.yuri_kill = 720
        elif persistent.yuri_kill >= 460:
            $ persistent.yuri_kill = 660
        elif persistent.yuri_kill >= 260:
            $ persistent.yuri_kill = 460
        elif persistent.yuri_kill >= 200:
            $ persistent.yuri_kill = 260
        else:
            $ persistent.yuri_kill = 200
        jump expression persistent.autoload

    elif persistent.yuri_killing > 0 and persistent.autoload == "ch8_yuri_kill":
        if persistent.yuri_killing >= 400:
            $ persistent.yuri_killing = 500
        elif persistent.yuri_killing >= 300:
            $ persistent.yuri_killing = 400
        elif persistent.yuri_killing >= 200:
            $ persistent.yuri_killing = 300
        elif persistent.yuri_killing >= 100:
            $ persistent.yuri_killing = 200
        else:
            $ persistent.yuri_killing = 100
        jump expression persistent.autoload

    elif anticheat != persistent.anticheat:
        stop music
        scene black
        "The save file could not be loaded."
        "Are you trying to cheat?"
        $ m_name = "Monika"
        show monika 1 at t11
        if persistent.playername == "":
            m "You're so funny."
        else:
            m "You're so funny, [persistent.playername]."
        $ renpy.utter_restart()
    else:
        if persistent.playthrough == 0 and not persistent.first_load and not config.developer:
            $ persistent.first_load = True
            call screen dialog("Hint: You can use the \"Skip\" button to\nfast-forward through text you've already read.", ok_action=Return())
    return



label autoload:
    python:

        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()


        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
        $ persistent.yuri_kill += 200


    if renpy.get_return_stack():
        $ renpy.pop_call()
    jump expression persistent.autoload

label autoload_yurikill:
    if persistent.yuri_kill >= 1380:
        $ persistent.yuri_kill = 1440
    elif persistent.yuri_kill >= 1180:
        $ persistent.yuri_kill = 1380
    elif persistent.yuri_kill >= 1120:
        $ persistent.yuri_kill = 1180
    elif persistent.yuri_kill >= 920:
        $ persistent.yuri_kill = 1120
    elif persistent.yuri_kill >= 720:
        $ persistent.yuri_kill = 920
    elif persistent.yuri_kill >= 660:
        $ persistent.yuri_kill = 720
    elif persistent.yuri_kill >= 460:
        $ persistent.yuri_kill = 660
    elif persistent.yuri_kill >= 260:
        $ persistent.yuri_kill = 460
    elif persistent.yuri_kill >= 200:
        $ persistent.yuri_kill = 260
    else:
        $ persistent.yuri_kill = 200
    jump expression persistent.autoload

label before_main_menu:
    if persistent.playthrough == 0 and persistent.monika_change and not persistent.monika_gone:
        if persistent.markov_agreed:
            $ config.main_menu_music = audio.t1c
        else:
            $ config.main_menu_music = audio.t1m
    else:
        $ config.main_menu_music = audio.t1
    return

label quit:
    if persistent.ghost_menu:
        hide screen main_menu
        scene white
        show expression "gui/menu_art_m_ghost.png":
            xpos -100 ypos -100 zoom 3.5
        pause 0.01
    return

label readonly:
    scene black
    "The game cannot be run because you are trying to run it from a read-only location."
    "Please copy the DDLC application to your desktop or other accessible location and try again."
    $ renpy.quit()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
