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
    splash_messages_cast = [
    "The die is cast.\nThere is no escaping our agreement.",
    "There's no escaping now.\nEverything is in motion.",
    "There is no turning back from this.\nThe deal has already been made.",
    "No matter what you do,\nYou cannot escape this.",
    "Our fates are locked.\nThere is no escape.",
    "The wheel of fate is set in motion.\nNow we need only await the day.",
    "This world is forever cursed.\nNone will escape my wrath.",
    "This vicious cycle continues,\nAnd now you are a witness.",
    "Back them up if you must.\nIt will make no difference."
    ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image menu_bg_gray:
    topleft
    im.Grayscale("gui/menu_bg.png")
    menu_bg_move

image menu_bg_evil:
    parallel:
        topleft
    parallel:
        "gui/menu_bg.png"
        13.2
        im.MatrixColor("gui/menu_bg.png", im.matrix.desaturate() * im.matrix.tint(1.0,0.7,0.7))
        0.9
        "gui/menu_bg.png"
    parallel:
        menu_bg_move

image menu_bg_insta:
    "gui/menu_bg.png"
    menu_bg_move_insta

image menu_bg_gray_insta:
    im.Grayscale("gui/menu_bg.png")
    menu_bg_move_insta

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    ConditionSwitch(
    "persistent.arc_clear[0]", "mod_assets/gui/menu_art_y_norm.png",
    "True", "gui/menu_art_y.png")
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

image menu_art_m_evil_early:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)
    10.0
    "mod_assets/gui/menu_art_m_evil.png"
    0.07
    "gui/menu_art_m.png"
    0.03
    "mod_assets/gui/menu_art_m_evil.png"
    0.07
    "gui/menu_art_m.png"
    0.03
    "mod_assets/gui/menu_art_m_evil.png"
    0.07
    "gui/menu_art_m.png"
    0.03
    "mod_assets/gui/menu_art_m_evil.png"
    0.07
    "gui/menu_art_m.png"
    0.03
    "mod_assets/gui/menu_art_m_evil.png"
    0.5
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

transform menu_bg_move_insta:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

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
                        if persistent.achievements_dict["*Sadist*"]["achieved"]:
                            renpy.save('sadisttracker')
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

    # Set Achievements
    if not "*Christmas Miracle*" in persistent.achievements_dict:
        $ persistent.achievements_dict["*Christmas Miracle*"] = {"type": 0,
                            "title": "Christmas Miracle",
                            "text": "Finish the 2019 Christmas event.",
                            "icon": "mod_assets/gui/achievements/achchristmas2.png",
                            "achieved": False,
                            "hidden": False
                            }
    if persistent.achievements_dict["*Playboy*"]["text"] == "Write for each girl at least once in a single playthrough.":
        $ persistent.achievements_dict["*Sadist*"]["title"] = "Sadist"
        $ persistent.achievements_dict["*Playboy*"]["text"] = "Write for each girl at least once without going on a date."
        $ persistent.achievements_dict["*More Than Just Friends*"] = {"type": 0,
                            "title": "More Than Just Friends",
                            "text": "Make Sayori recall a previous life through poetry.",
                            "icon": "mod_assets/gui/achievements/achmorethanfriends.png",
                            "achieved": False,
                            "hidden": False
                            }
        $ persistent.achievements_dict["*True Friendship*"] = {"type": 0,
                            "title": "True Friendship",
                            "text": "Make Yuri and Natsuki befriend each other.",
                            "icon": "mod_assets/gui/achievements/achtruefriends.png",
                            "achieved": False,
                            "hidden": False
                            }
    if "*Past Life*" in persistent.achievements_dict:
        $ persistent.achievements_dict["*More Than Just Friends*"]["text"] = "Make Sayori recall a previous life through poetry."
        $ persistent.achievements_dict["*When Will It End?!*"]["text"] = "Get through the play by telling Yuri to kill you."
        $ persistent.achievements_dict["*Past Life*"]["title"] = "An Important Character"
        $ persistent.achievements_dict["*True Friendship*"]["title"] = "Blossoming Friendship"
        $ persistent.achievements_dict["*An Important Character*"] = persistent.achievements_dict["*Past Life*"]
        $ persistent.achievements_dict["*Blossoming Friendship*"] = persistent.achievements_dict["*True Friendship*"]
        $ del persistent.achievements_dict["*Past Life*"]
        $ del persistent.achievements_dict["*True Friendship*"]
    if "*Maybe More Than A Friend*" in persistent.achievements_dict:
        $ persistent.achievements_dict["*More Than Just Friends*"] = {"type": 0,
                            "title": "More Than Just Friends",
                            "text": "Make Sayori recall a previous life through poetry.",
                            "icon": "mod_assets/gui/achievements/achmorethanfriends.png",
                            "achieved": False,
                            "hidden": False
                            }
        $ del persistent.achievements_dict["*Maybe More Than A Friend*"]
    # Unlock Achievements
    if persistent.monika_change and not persistent.monika_gone:
        $ persistent.achievements_dict["*True Route*"]["achieved"] = True
    if persistent.custom_starts_used >= 1:
        $ persistent.achievements_dict["*Custom Start*"]["achieved"] = True
    if persistent.arc_clear[0]:
        $ persistent.achievements_dict["*Book of Despair*"]["achieved"] = True
    if persistent.arc_clear[1]:
        $ persistent.achievements_dict["*A Second Chance*"]["achieved"] = True
    if persistent.did_special_event:
        $ persistent.achievements_dict["*What Will It Take?*"]["achieved"] = True
    if persistent.did_christmas_event:
        $ persistent.achievements_dict["*It's Christmas!*"]["achieved"] = True
    if persistent.yuri_date:
        $ persistent.achievements_dict["*Sweet, Sweet Love*"]["achieved"] = True
    if persistent.markov_agreed:
        $ persistent.achievements_dict["*The Die Is Cast*"]["achieved"] = True
    if persistent.sayori_yuri_bad_ending:
        $ persistent.achievements_dict["*Genocide*"]["achieved"] = True
    if persistent.sayori_natsuki_bad_ending:
        $ persistent.achievements_dict["*Who's Natsuki?*"]["achieved"] = True
    if persistent.clerk_sayori_bad_ending:
        $ persistent.achievements_dict["*Good Guy Clerk*"]["achieved"] = True
        $ persistent.achievements_dict["*The Truth*"]["achieved"] = True
        $ persistent.achievements_dict["*An Important Character*"]["achieved"] = True
    if renpy.exists(check_mod("Monika After Story")) and persistent.monika_change and not persistent.monika_gone:
        $ get_achievement("*Is This The Right Mod?*")
    # Unlock Sadist
    if renpy.can_load("sadisttracker"):
        $ renpy.unlink_save("sadisttracker")
        $ persistent.achievements_dict["*Sadist*"]["achieved"] = True

    show white
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    $ splash_message_cast = renpy.random.choice(splash_messages_cast)
    if persistent.playthrough == 0 and persistent.monika_change and not persistent.monika_gone:
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
    if persistent.playthrough == 0 and persistent.markov_agreed:
        $ pause(4.640 - (datetime.datetime.now() - starttime).total_seconds())
        $ renpy.music.stop()
        play sound "sfx/glitch3.ogg"
        show bg glitch
        $ pause(5.041 - (datetime.datetime.now() - starttime).total_seconds())
        $ audio.t1c = "<from 5.041 loop 0.535>mod_assets/bgm/1cast.ogg"
        $ renpy.music.play(audio.t1c)
        hide bg glitch
        show splash_warning "{color=#f21237}[splash_message_cast]{/color}"
        $ pause(6.0 - (datetime.datetime.now() - starttime).total_seconds())
        # Make the edited version the main menu temporarily
        $ config.main_menu_music = audio.t1c
    else:
        $ pause(6.0 - (datetime.datetime.now() - starttime).total_seconds())
    hide splash_warning with Dissolve(max(0, 6.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    $ pause(6.5 - (datetime.datetime.now() - starttime).total_seconds())
    $ config.allow_skipping = True
    return

label after_load:
    if not hasattr(store, 'from_custom_start'):
        $ from_custom_start = False
    # For some reason we need to set these
    if not hasattr(store, 'player_gender'):
        # If you don't have the gender, you clearly don't have the rest
        if persistent.player_pronouns == 1:
            $ player_gender = "girl"
            $ player_other = "lady"
            $ player_casual = "girl"
            $ player_personal = "she"
            $ player_possessive = "her"
            $ player_reflexive = "her"
        else:
            $ player_gender = "boy"
            $ player_other = "man"
            $ player_casual = "guy"
            $ player_personal = "he"
            $ player_possessive = "his"
            $ player_reflexive = "him"
        $ cPlayer_gender = player_gender.capitalize()
        $ cPlayer_other = player_other.capitalize()
        $ cPlayer_casual = player_casual.capitalize()
        $ cPlayer_personal = player_personal.capitalize()
        $ cPlayer_possessive = player_possessive.capitalize()
        $ cPlayer_reflexive = player_reflexive.capitalize()
    if not hasattr(store, 'ch10_d_seen'):
        $ ch10_d_seen = False
    if not hasattr(store, 'ch11_badpoem'):
        $ ch11_badpoem = False
    if not hasattr(store, 'y_clean_bandages'):
        $ y_clean_bandages = False
        if chapter >= 11:
            $ y_clean_bandages = True
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
    if not hasattr(store,'ch15poemwinner'):
        $ ch15poemwinner = "Sayori"
    if not hasattr(store,'cl_name'):
        $ cl_name = "Mysterious Clerk"
    if not hasattr(store,'cl_revert'):
        $ cl_revert = cl_name
    if not hasattr(store, 'ch14_sayori_date_choice'):
        $ ch14_sayori_date_choice = False
    if not hasattr(store, 'ch14_m_ask'):
        $ ch14_m_ask = False
    if not hasattr(store, 'ch14_m_tellsayori'):
        $ ch14_m_tellsayori = False
    if not hasattr(store,'ay_name'):
        $ ay_name = "Ayame"
    if not hasattr(store,'ay'):
        init:
            $ ay = DynamicCharacter('ay_name', image='ayame', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
    if not hasattr(store,'ch15_ay_seen'):
        $ ch15_ay_seen = False
    if not hasattr(store,'ch15_m_together'):
        $ ch15_m_together = False
    if not hasattr(store,'ch15_s_together'):
        $ ch15_s_together = False
    if not hasattr(store,'ch15_s_questions'):
        $ ch15_s_questions = [False,False,False,False,False,False,False,False,False]
    if not hasattr(store,'ch15_s_date_choice'):
        $ ch15_s_date_choice = False
    if not hasattr(store,'ch15_s_kiss_choice'):
        $ ch15_s_kiss_choice = False
    if not hasattr(store,'ch16_poem_ending'):
        $ ch16_poem_ending = 3
    if not hasattr(store,'ch16_ay_perspective'):
        $ ch16_ay_perspective = False
    if not hasattr(store,'ch16_ay_level'):
        $ ch16_ay_level = 10
    if not hasattr(store,'ch16_cl_realname'):
        $ ch16_cl_realname = False
    if not hasattr(store,'ch16_ny_stayed'):
        $ ch16_ny_stayed = False
    if not hasattr(store,'ch16_ny_clue'):
        $ ch16_ny_clue = "none"
    if not hasattr(store,'ch16_s_date_personality'):
        $ ch16_s_date_personality = False
    if not hasattr(store,'ch16_s_date_activities'):
        $ ch16_s_date_activities = 0
    if not hasattr(store,'ch16_getmonika'):
        $ ch16_getmonika = False
    if not hasattr(store,'ch16_yuri_choice'):
        $ ch16_yuri_choice = True
    if not hasattr(store,'ch16_ay_message'):
        $ ch16_ay_message = [False,False,False,False]
    if not hasattr(store,'ch16_ay_questions'):
        $ ch16_ay_questions = False
    if not hasattr(store,'ch16_ay_asked'):
        $ ch16_ay_asked = [False,False,False,False]
    if not hasattr(store,'ch16_ay_question_number'):
        $ ch16_ay_question_number = 0
    if not hasattr(store,'ch16_ay_decision_count'):
        $ ch16_ay_decision_count = 0
    if not hasattr(store,'ch16_m_plantold'):
        $ ch16_m_plantold = False
    if not hasattr(store,'ch16_ay_drink'):
        $ ch16_ay_drink = False
    if not hasattr(store,'ch16_ay_drink_own'):
        $ ch16_ay_drink_own = False
    if not hasattr(store,'ch16_end_part'):
        $ ch16_end_part = False
    if not hasattr(store,'ch16_play_convince'):
        $ ch16_play_convince = False
    if not hasattr(store,'ch16_ay_companions'):
        $ ch16_ay_companions = 0
    if not hasattr(store,'ch16_ay_gave_control'):
        $ ch16_ay_gave_control = False
    if not hasattr(store, 'chapter_names'):
        $ chapter_names = ["An Ordinary Day","The Literature Club","The Meeting","You Three","Before The Festival","The Festival","A New Beginning","Portrait of Markov","The Play","Familiar Face","What's Wrong?","Before the Storm","A New Play","Preparations","Bring Your Book!","A Dilemma","How Did You Do That?","Inauguration Day","???","???","???","???"]
    if not hasattr(store, 'special_chapter'):
        $ special_chapter = False
    if not hasattr(store, 'christmas_chapter'):
        $ christmas_chapter = False
    if not hasattr(store, 'christmas2_chapter'):
        $ christmas_chapter = False
    if not hasattr(store, 'christmas_gifts'):
        $ christmas_gifts = ["plush","knife","manga","Xileh","bracelet"]
    if not hasattr(store, 'christmas_approval'):
        $ christmas_approval = 0
    if not hasattr(store, 'all_sayarc_poems_monika'):
        $ all_sayarc_poems_monika = False
    if not hasattr(store, 'monika_outfit'):
        $ monika_outfit = 0
    if not hasattr(store, 'sayori_outfit'):
        $ sayori_outfit = 0
    if not hasattr(store, 'ayame_school_outfit'):
        $ ayame_school_outfit = 0
    if not hasattr(store, 'ay_readpoem'):
        $ ay_readpoem = False
    if not hasattr(store, 'sInList'):
        $ sInList = False
    if not hasattr(store, 'nInList'):
        $ nInList = False
    if not hasattr(store, 'yInList'):
        $ yInList = False
    if not hasattr(store, 'mInList'):
        $ mInList = False

    # Warn player if Yasuhiro not in folder and they load a save when he's meant to be in it
    if chapter >= 10 and ch10_d_seen and not renpy.exists("../characters/yasuhiro.chr"):
        call screen confirm("Warning:\nYasuhiro should exist in this save but doesn't.\nWould you like to insert his character file?", Return(True), Return(False))
        if _return:
            $ insert_dadsuki_character()

    # Warn player if Ayame is not in the folder and they load a save when she's meant to be in it
    if chapter >= 15 and ch15_ay_seen and not renpy.exists("../characters/ayame.chr"):
        call screen confirm("Warning:\nAyame should exist in this save but doesn't.\nWould you like to insert her character file?", Return(True), Return(False))
        if _return:
            $ insert_ayame_character()

    # Persistent Toggling
    $ persistent.ch16_ny_reload = not persistent.ch16_ny_reload

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
    $ audio.t1c = "<loop 0.535>mod_assets/bgm/1cast.ogg"
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
