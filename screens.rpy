










init -1 style default:
    font gui.default_font
    size gui.text_size
    color gui.text_color
    outlines [(2, "#000000aa", 0, 0)]
    line_overlap_split 1
    line_spacing 1

init -1 style default_monika is normal:
    slow_cps 30

init -1 style edited is default:
    font "gui/font/VerilySerifMono.otf"
    kerning 8
    outlines [(10, "#000", 0, 0)]
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos
    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

init -1 style normal is default:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

init -1 style input:
    color gui.accent_color

init -1 style hyperlink_text:
    color gui.accent_color
    hover_color gui.hover_color
    hover_underline True

init -1 style splash_text:
    size 24
    color "#000"
    font gui.default_font
    text_align 0.5
    outlines []

init -1 style poemgame_text:
    yalign 0.5
    font "gui/font/Halogen.ttf"
    size 30
    color "#000"
    outlines []

    hover_xoffset -3
    hover_outlines [(3, "#fef", 0, 0), (2, "#fcf", 0, 0), (1, "#faf", 0, 0)]

init -1 style gui_text:
    font gui.interface_font
    color gui.interface_text_color
    size gui.interface_text_size


init -1 style button:
    properties gui.button_properties("button")

init -1 style button_text is gui_text:
    properties gui.button_text_properties("button")
    yalign 0.5


init -1 style label_text is gui_text:
    color gui.accent_color
    size gui.label_text_size

init -1 style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size







init -1 style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style bar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)

init -1 style scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)
    unscrollable "hide"
    bar_invert True


init -1 style vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True






init -1 style slider:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb "gui/slider/horizontal_hover_thumb.png"

init -1 style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


init -1 style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)





















init -501 screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        text what id "what"

        if who is not None:

            window:
                style "namebox"
                text who id "who"



    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    use quick_menu


init -1 style window is default
init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue

init -1 style namebox is default
init -1 style namebox_label is say_label


init -1 style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

init -1 style window_monika is window:
    background Image("gui/textbox_monika.png", xalign=0.5, yalign=1.0)

init -1 style window_flashback is window:
    background Image("mod_assets/gui/textbox_flashback.png", xalign=0.5, yalign=1.0)

init -1 style window_christmas is window:
    background Image("mod_assets/gui/textbox_christmas.png", xalign=0.5, yalign=1.0)

init -1 style window_valentines is window:
    background Image("mod_assets/gui/textbox_valentines.png", xalign=0.5, yalign=1.0)

init -1 style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

init -1 style say_label:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]

init -1 style say_dialogue:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

init 499 image ctc:
    xalign 0.81 yalign 0.98 xoffset -5 alpha 0.0 subpixel True
    "gui/ctc.png"
    block:
        easeout 0.75 alpha 1.0 xoffset 0
        easein 0.75 alpha 0.5 xoffset -5
        repeat











init 499 image input_caret:
    Solid("#b59")
    size (2,25) subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat

init -501 screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xpos gui.text_xpos
            xanchor 0.5
            ypos gui.text_ypos

        text prompt style "input_prompt"
        input id "input"


init -1 style input_prompt is default

init -1 style input_prompt:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign

init -1 style input:
    caret "input_caret"
    xmaximum gui.text_width
    xalign 0.5
    text_align 0.5










init -501 screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action




define -1 config.narrator_menu = True


init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text

init -1 style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

init -1 style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

init -1 style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []


init -1 python:
    def RigMouse():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 345]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)

init -501 screen rigged_choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    timer 1.0/30.0 repeat True action Function(RigMouse)




define -1 config.narrator_menu = True


init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text

init -1 style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

init -1 style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

init -1 style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []







init -501 screen quick_menu():


    zorder 100

    if quick_menu:


        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.995


            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip()
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Load") action ShowMenu('load')


            textbutton _("Settings") action ShowMenu('preferences')







default -1 quick_menu = True




init -1 style quick_button:
    properties gui.button_properties("quick_button")
    activate_sound gui.activate_sound

init -1 style quick_button_text:
    properties gui.button_text_properties("quick_button")
    outlines []











init -1 python:
    def FinishEnterName(label="start"):
        if not player: return
        persistent.playername = player
        renpy.hide_screen("name_input")
        if persistent.prompt_info:
            renpy.show_screen("gender_input", message="What pronouns would you like to use?", male_action=Function(CheckPronouns, label=label, pronouns=0), female_action=Function(CheckPronouns, label=label, pronouns=1))
            # , nonbinary_action=Function(CheckPronouns, label=label, pronouns=2))
        else:
            renpy.jump_out_of_context(label)

    # Pronouns: 0 - Male, 1 - Female, 2 - Non-binary
    def CheckPronouns(label, pronouns):
        renpy.hide_screen("gender_input")
        persistent.player_pronouns = pronouns
        renpy.jump_out_of_context(label)

    def HideConfirmThenName(goto="choose_start"):
        renpy.hide_screen("confirm")
        renpy.show_screen("name_input", message="Please enter your name", ok_action=Function(FinishEnterName, label=goto))


init -501 screen navigation():
    python:
        import datetime
        currentdate = datetime.date.today()
        weekrange = datetime.timedelta(days = 7)

        customstartoutlines = [(4, "#b59", 0, 0), (2, "#b59", 2, 2)]
        customstarthover_outlines = [(4, "#fac", 0, 0), (2, "#fac", 2, 2)]
        customstartinsensitive_outlines = [(4, "#fce", 0, 0), (2, "#fce", 2, 2)]

        if ((currentdate <= (datetime.date(2018, 9, 22) + weekrange)) or (currentdate <= (datetime.date(2019, 1, 1) + weekrange)) or (currentdate <= (datetime.date(2019, 9, 22) + weekrange)) or (currentdate <= (datetime.date(2020, 1, 1) + weekrange)) or (currentdate <= (datetime.date(2024, 2, 29)))) and persistent.arc_clear[0]:
            customstartoutlines = [(4, "#228B22", 0, 0), (2, "#228B22", 2, 2)]
            customstarthover_outlines = [(4, "#32CD32", 0, 0), (2, "#32CD32", 2, 2)]
            customstartinsensitive_outlines = [(4, "#00FF00", 0, 0), (2, "#00FF00", 2, 2)]

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.8

        spacing gui.navigation_spacing

        if not persistent.autoload or not main_menu:

            if main_menu:

                if persistent.playthrough == 1:
                    textbutton _("ŔŗñĮ¼»ŧþŀÂŻŕěōì«") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=If(persistent.original_game_warning,
                        true=Function(FinishEnterName),
                        false=[SetVariable("persistent.original_game_warning",True), Show(screen="dialog", message="The game will play like the original from here.\nPlease delete firstrun and restart the game to play True Route.", ok_action=Function(FinishEnterName))]
                    )))
                elif persistent.playthrough == 0 and persistent.monika_gone:
                    textbutton _("ŔŗñĮ¼»ŧþŀÂŻŕěōì«") action If(persistent.playername, true=Show(screen="dialog", message="File error: \"characters/monika.chr\"\n\nThe file is missing or corrupt.",
                ok_action=Show(screen="dialog", message="The game is corrupt. Continuing from next chapter.", ok_action=Function(renpy.full_restart, label="ch5_premainb"))), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))
                else:
                    textbutton _("New Game") action If(persistent.playername,
                        true=If(persistent.prompt_info,
                            true=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)),
                            false=Start()),
                        false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))
                    if persistent.playthrough == 0 and persistent.monika_change and not persistent.monika_gone:
                        textbutton _("Custom Start") action If(persistent.playername,
                            true=Show(screen="confirm", message="Are you sure you want to use Custom Start?\nYou may find different outcomes if you\nchoose differently from your previous choices.",
                                yes_action=If(persistent.prompt_info,
                                    true=Function(HideConfirmThenName),
                                    false=Start("choose_start")),
                                no_action=Hide("confirm")),
                            false=Function(HideConfirmThenName))
                        if persistent.arc_clear[0] or persistent.any_bonus_day:
                            textbutton _("Bonus Days") action If(persistent.playername,
                            true=Show(screen="confirm", message="Are you sure you want to see a bonus day?",
                                yes_action=If(persistent.prompt_info,
                                    true=Function(HideConfirmThenName),
                                    false=Start("choose_bonus_day")),
                                no_action=Hide("confirm")),
                            false=Function(HideConfirmThenName)) text_outlines customstartoutlines text_hover_outlines customstarthover_outlines text_insensitive_outlines customstartinsensitive_outlines
                        textbutton _("Achievements") action [ShowMenu("achievements"), SensitiveIf(renpy.get_screen("achievements") == None)]

            else:

                textbutton _("History") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]

                textbutton _("Save Game") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]

            textbutton _("Load Game") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]

            if _in_replay:

                textbutton _("End Replay") action EndReplay(confirm=True)

            elif not main_menu:
                if persistent.playthrough != 3:
                    textbutton _("Main Menu") action MainMenu()
                else:
                    textbutton _("Main Menu") action NullAction()

            textbutton _("Settings") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]



            if renpy.variant("pc"):


                textbutton _("Help") action [Help("README.html"), Show(screen="dialog", message="The help file has been opened in your browser.", ok_action=Hide("dialog"))]


                textbutton _("Quit") action Quit(confirm=not main_menu)
        else:
            timer 1.75 action Start("autoload_yurikill")


init -1 style navigation_button is gui_button
init -1 style navigation_button_text is gui_button_text

init -1 style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

init -1 style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font "gui/font/RifficFree-Bold.ttf"
    color "#fff"
    outlines [(4, "#b59", 0, 0), (2, "#b59", 2, 2)]
    hover_outlines [(4, "#fac", 0, 0), (2, "#fac", 2, 2)]
    insensitive_outlines [(4, "#fce", 0, 0), (2, "#fce", 2, 2)]







init -501 screen main_menu() tag menu:
    python:
        import datetime
        currentdate = datetime.date.today()
        weekrange = datetime.timedelta(days = 7)


    style_prefix "main_menu"

    if persistent.ghost_menu:
        add "white"
        add "menu_art_y_ghost"
        add "menu_art_n_ghost"
    else:
        if ((currentdate <= (datetime.date(2018, 9, 22) + weekrange)) or (currentdate <= (datetime.date(2019, 1, 1) + weekrange)) or (currentdate <= (datetime.date(2019, 9, 22) + weekrange)) or (currentdate <= (datetime.date(2020, 1, 1) + weekrange)) or (currentdate <= (datetime.date(2024, 2, 29)))) and persistent.arc_clear[0]:
            add "menu_bg_gray"
        elif persistent.markov_agreed:
            add "menu_bg_evil"
        else:
            add "menu_bg"
        add "menu_art_y"
        add "menu_art_n"
        frame




        use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

    if not persistent.ghost_menu:
        add "menu_particles"
        add "menu_particles"
        add "menu_particles"
        if persistent.playthrough == 0 and persistent.monika_change and not persistent.monika_gone:
            add "menu_logo_mod"
        else:
            add "menu_logo"
    if persistent.ghost_menu:
        add "menu_art_s_ghost"
        add "menu_art_m_ghost"
    else:
        if persistent.playthrough == 1 or persistent.playthrough == 2:
            add "menu_art_s_glitch"
        else:
            add "menu_art_s"
        add "menu_particles"
        if persistent.playthrough != 4 and not persistent.monika_gone:
            if not persistent.arc_clear[0]:
                add "menu_art_m"
            else:
                if persistent.markov_agreed and not ((currentdate <= (datetime.date(2018, 9, 22) + weekrange)) or (currentdate <= (datetime.date(2019, 1, 1) + weekrange)) or (currentdate <= (datetime.date(2019, 9, 22) + weekrange)) or (currentdate <= (datetime.date(2020, 1, 1) + weekrange)) and persistent.arc_clear[0]):
                    add "menu_art_m_evil_early"
                else:
                    add "menu_art_m_evil"
        add "menu_fade"

    key "K_ESCAPE" action Quit(confirm=False)

init -1 style main_menu_frame is empty
init -1 style main_menu_vbox is vbox
init -1 style main_menu_text is gui_text
init -1 style main_menu_title is main_menu_text
init -1 style main_menu_version is main_menu_text:
    color "#000000"
    size 16
    outlines []

init -1 style main_menu_frame:
    xsize 310
    yfill True

    background "menu_nav"

init -1 style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

init -1 style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

init -1 style main_menu_title:
    size gui.title_text_size











init -501 screen game_menu_m():
    $ persistent.menu_bg_m = True
    add "gui/menu_bg_m.png"
    timer 0.3 action Hide("game_menu_m")

init -501 screen game_menu(title, scroll=None):


    if main_menu:
        add gui.main_menu_background
    else:
        key "mouseup_3" action Return()
        add gui.game_menu_background

    style_prefix "game_menu"

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    yinitial 1.0

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial 1.0

                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    if not main_menu and persistent.playthrough == 2 and not persistent.menu_bg_m and renpy.random.randint(0, 49) == 0:
        on "show" action Show("game_menu_m")

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


init -1 style game_menu_outer_frame is empty
init -1 style game_menu_navigation_frame is empty
init -1 style game_menu_content_frame is empty
init -1 style game_menu_viewport is gui_viewport
init -1 style game_menu_side is gui_side
init -1 style game_menu_scrollbar is gui_vscrollbar

init -1 style game_menu_label is gui_label
init -1 style game_menu_label_text is gui_label_text

init -1 style return_button is navigation_button
init -1 style return_button_text is navigation_button_text

init -1 style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

init -1 style game_menu_navigation_frame:
    xsize 280
    yfill True

init -1 style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

init -1 style game_menu_viewport:
    xsize 920

init -1 style game_menu_vscrollbar:
    unscrollable gui.unscrollable

init -1 style game_menu_side:
    spacing 10

init -1 style game_menu_label:
    xpos 50
    ysize 120

init -1 style game_menu_label_text:
    font "gui/font/RifficFree-Bold.ttf"
    size gui.title_text_size
    color "#fff"
    outlines [(6, "#b59", 0, 0), (3, "#b59", 2, 2)]
    yalign 0.5

init -1 style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30









init -501 screen about() tag menu:






    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")



define -1 gui.about = ""


init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text
init -1 style about_text is gui_text

init -1 style about_label_text:
    size gui.label_text_size











init -501 screen save() tag menu:



    use file_slots(_("Save"))


init -501 screen load() tag menu:


    if ch16_end_part and ch16_saving_monika:
        use fake_slots()
    else:
        use file_slots(_("Load"))

init -1 python:
    def FileMonikaName(name, page=None, **kwargs):
        if name == 1:
            return "Save Monika"
        elif name == 2:
            return "Save Monika"
        elif name == 3:
            return "Save Monika"

    def FileActionMonika(name, page=None, **kwargs):
        if name == 1 and not ch16_saved_monika[0]:
            renpy.jump_out_of_context("ch16_monika_save_1")
        elif name == 2 and not ch16_saved_monika[1]:
            renpy.jump_out_of_context("ch16_monika_save_2")
        elif name == 3 and not ch16_saved_monika[2]:
            renpy.jump_out_of_context("ch16_monika_save_3")
        else:
            return Show(screen="dialog", message="Now is not the time for that.", ok_action=Hide("dialog"))

    def FileActionMod(name, page=None, **kwargs):
        if persistent.playthrough == 1 and not persistent.deleted_saves and renpy.current_screen().screen_name[0] == "load" and FileLoadable(name):
            return Show(screen="dialog", message="File error: \"characters/sayori.chr\"\n\nThe file is missing or corrupt.",
                ok_action=Show(screen="dialog", message="The save file is corrupt. Starting a new game.", ok_action=Function(renpy.full_restart, label="start")))

        # Saving Monika Chapter 16
        elif persistent.playthrough == 0 and ch16_end_part and ch16_saving_monika and renpy.current_screen().screen_name[0] == "load":
            return Show(screen="dialog", message="Test test test", ok_action=Hide("dialog"))

        # Monika Missing Chapter 5b
        elif persistent.playthrough == 0 and not persistent.deleted_saves and renpy.current_screen().screen_name[0] == "load" and FileLoadable(name) and persistent.monika_gone and not canload_ch5b:
            return Show(screen="dialog", message="File error: \"characters/monika.chr\"\n\nThe file is missing or corrupt.",
                ok_action=Show(screen="dialog", message="The save file is corrupt. Continuing from next chapter.", ok_action=Function(renpy.full_restart, label="ch5_premainb")))

        elif persistent.playthrough == 3 and renpy.current_screen().screen_name[0] == "save":
            return Show(screen="dialog", message="There's no point in saving anymore.\nDon't worry, I'm not going anywhere.", ok_action=Hide("dialog"))

        elif persistent.playthrough == 0 and special_chapter:
            return Show(screen="dialog", message="This is an alternate reality. You can't save them.", ok_action=Hide("dialog"))

        elif persistent.playthrough == 0 and (christmas_chapter or valentines_chapter):
            return Show(screen="dialog", message="You have no influence on this timeline.", ok_action=Hide("dialog"))

        elif persistent.playthrough == 0 and ch16_end_part:
            return Show(screen="dialog", message="Actions that can affect the original sequence\nof events have been disabled.", ok_action=Hide("dialog"))

        # Monika Bad Ending Saturday
        elif persistent.playthrough == 0 and persistent.monika_ch3_skip and renpy.current_screen().screen_name[0] == "save":
            return Show(screen="dialog", message="There's no point in saving anymore.\nDon't worry, I'm not going anywhere.", ok_action=Hide("dialog"))

        #elif persistent.playthrough == 0 and persistent.monika_ch3_skip and renpy.current_screen().screen_name[0] == "load" and FileLoadable(name):
        #    return Show(screen="dialog", message="Aha, you're so cute!\nNo need for these if we're already happy.", ok_action=delete_all_saves())

        else:
            if renpy.current_screen().screen_name[0] == "save" and persistent.name_saves:
                # renpy.store.save_name = chapter_names[chapter]
                return Show(screen="save_input", message="Enter save name", ok_action=[Hide("save_input"), FileAction(name)])
            elif renpy.current_screen().screen_name[0] == "save":
                if christmas_chapter:
                    renpy.store.save_name = "Festive Season"
                elif special_chapter:
                    renpy.store.save_name = "Special Day"
                elif bonus_chapter_active:
                    renpy.store.save_name = bonus_chapter_names[bonus_chapter]
                else:
                    renpy.store.save_name = chapter_names[chapter]
            return FileAction(name)


init -501 screen file_slots(title):

    default page_name_value = FilePageNameInputValue()

    use game_menu(title):

        fixed:



            order_reverse True



            button:
                style "page_label"


                xalign 0.5


                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileActionMod(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        if persistent.name_saves:
                            text FileSaveName(slot):
                                style "slot_name_text"
                            text FileTime(slot, format=_("{#file_time}%m/%d/%Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"
                        else:
                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"
                            # text FileSaveName(slot):
                            #     style "slot_name_text"


                        key "save_delete" action FileDelete(slot)


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing








                for page in range(1, 20):
                    textbutton "[page]" action FilePage(page)

# Custom Mod Load Screen
init -501 screen fake_slots():

    default page_name_value = FilePageNameInputValue()

    use game_menu("Load"):

        fixed:



            order_reverse True



            button:
                style "page_label"


                xalign 0.5


                text "Save Her":
                    style "page_label_text"
                    


            grid 3 1:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(3 * 1):

                    $ slot = i + 1

                    button:
                        action FileActionMonika(slot)

                        has vbox

                        if slot == 1 or (slot == 2 and ch16_saved_monika[0]) or (slot == 3 and ch16_saved_monika[1]):
                            add Image("mod_assets/gui/monika_save_{0}.png".format(slot), xalign=0.5, yalign=1.0)
                        else:
                            add Image("mod_assets/gui/monika_save_locked.png", xalign=0.5, yalign=1.0)

                        if persistent.name_saves:
                            text FileMonikaName(slot):
                                style "slot_name_text"
                            text "??/??/????, ??:??":
                                style "slot_time_text"
                        else:
                            text "???, ??? ?? ????, ??:??":
                                style "slot_time_text"


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing








                for page in range(1, 1):
                    textbutton "[page]" action FilePage(page)




init -1 style page_label is gui_label
init -1 style page_label_text is gui_label_text
init -1 style page_button is gui_button
init -1 style page_button_text is gui_button_text

init -1 style slot_button is gui_button
init -1 style slot_button_text is gui_button_text
init -1 style slot_time_text is slot_button_text
init -1 style slot_name_text is slot_button_text

init -1 style page_label:
    xpadding 50
    ypadding 3

init -1 style page_label_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

init -1 style page_button:
    properties gui.button_properties("page_button")

init -1 style page_button_text:
    properties gui.button_text_properties("page_button")
    outlines []

init -1 style slot_button:
    properties gui.button_properties("slot_button")

init -1 style slot_button_text:
    properties gui.button_text_properties("slot_button")
    color "#666"
    outlines []









init -501 screen preferences() tag menu:



    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Settings"), scroll="viewport"):

        vbox:
            xoffset 50

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
                if config.developer:
                    vbox:
                        style_prefix "radio"
                        label _("Rollback Side")
                        textbutton _("Disable") action Preference("rollback side", "disable")
                        textbutton _("Left") action Preference("rollback side", "left")
                        textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")

                vbox:
                    style_prefix "radio"
                    label _("Save Names")
                    textbutton _("Enabled") action SetField(persistent, "name_saves", True)
                    textbutton _("Disabled") action SetField(persistent, "name_saves", False)

                vbox:
                    style_prefix "radio"
                    label _("Prompt Info")
                    textbutton _("Enabled") action SetField(persistent, "prompt_info", True)
                    textbutton _("Disabled") action SetField(persistent, "prompt_info", False)





            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")


                    bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, style="slider", offset=20)

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
    text "v[config.version]":
        xalign 1.0 yalign 1.0
        xoffset -10 yoffset -10
        style "main_menu_version"

init -1 style pref_label is gui_label
init -1 style pref_label_text is gui_label_text
init -1 style pref_vbox is vbox

init -1 style radio_label is pref_label
init -1 style radio_label_text is pref_label_text
init -1 style radio_button is gui_button
init -1 style radio_button_text is gui_button_text
init -1 style radio_vbox is pref_vbox

init -1 style check_label is pref_label
init -1 style check_label_text is pref_label_text
init -1 style check_button is gui_button
init -1 style check_button_text is gui_button_text
init -1 style check_vbox is pref_vbox

init -1 style slider_label is pref_label
init -1 style slider_label_text is pref_label_text
init -1 style slider_slider is gui_slider
init -1 style slider_button is gui_button
init -1 style slider_button_text is gui_button_text
init -1 style slider_pref_vbox is pref_vbox

init -1 style mute_all_button is check_button
init -1 style mute_all_button_text is check_button_text

init -1 style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

init -1 style pref_label_text:
    font "gui/font/RifficFree-Bold.ttf"
    size 24
    color "#fff"
    outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]
    yalign 1.0

init -1 style pref_vbox:
    xsize 225

init -1 style radio_vbox:
    spacing gui.pref_button_spacing

init -1 style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

init -1 style radio_button_text:
    properties gui.button_text_properties("radio_button")
    font "gui/font/Halogen.ttf"
    outlines []

init -1 style check_vbox:
    spacing gui.pref_button_spacing

init -1 style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

init -1 style check_button_text:
    properties gui.button_text_properties("check_button")
    font "gui/font/Halogen.ttf"
    outlines []

init -1 style slider_slider:
    xsize 350

init -1 style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

init -1 style slider_button_text:
    properties gui.button_text_properties("slider_button")

init -1 style slider_vbox:
    xsize 450










init -501 screen history() tag menu:




    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("The dialogue history is empty.")


init -1 style history_window is empty

init -1 style history_name is gui_label
init -1 style history_name_text is gui_label_text
init -1 style history_text is gui_text

init -1 style history_text is gui_text

init -1 style history_label is gui_label
init -1 style history_label_text is gui_label_text

init -1 style history_window:
    xfill True
    ysize gui.history_height

init -1 style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

init -1 style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

init -1 style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

init -1 style history_label:
    xfill True

init -1 style history_label_text:
    xalign 0.5










































































































































































init -501 screen save_input(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        input default chapter_names[chapter] value VariableInputValue("save_name") length 30 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890()-=!@#$%^&*()_+ "






        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action

init -501 screen name_input(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        input default "" value VariableInputValue("player") length 12 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"






        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action

init -501 screen dialog(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action

init 499 image confirm_glitch:
    "gui/overlay/confirm_glitch.png"
    pause 0.02
    "gui/overlay/confirm_glitch2.png"
    pause 0.02
    repeat

init -501 screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action



init -501 screen gender_input(message, male_action, female_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Male") action male_action
            textbutton _("Female") action female_action


init -501 screen arc_choose_1():
    python:
        import datetime
        currentdate = datetime.date.today()
        weekrange = datetime.timedelta(days = 7)

    default tt = Tooltip("")


    fixed at show_hide_fade:
        xalign 0.5
        yalign 0.5

        label _("Choose an arc to begin"):
            text_style "game_menu_label_text"
            xalign 0.5
            yalign 0.0

        grid 4 1:
            xalign 0.5
            yalign 0.7
            spacing 60

            imagebutton xsize 450 idle "gui/menu_art_m.png" hover "mod_assets/gui/menu_art_m_hover.png" hovered tt.Action("{color=#8ed73a}Festival Day{/color}\n{color=#ff0000}Warning: Your saves will be deleted upon proceeding.{/color}") hover_sound gui.hover_sound activate_sound gui.activate_sound focus_mask True at custom_start_zoom_1:
                action Show(screen="confirm", message="Are you sure you want to start on Festival Day?\nYour saves will be deleted.",
                            yes_action=[Hide("confirm"),Return(0)],
                            no_action=Hide("confirm"))
            imagebutton xsize 450 idle "gui/menu_art_y.png" hover "mod_assets/gui/menu_art_y_hover.png" hovered tt.Action("{color=#d88dee}Book of Despair{/color}") hover_sound gui.hover_sound activate_sound gui.activate_sound focus_mask True at custom_start_zoom_2:
                action Show(screen="confirm", message="Are you sure you want to start in Yuri's arc?",
                            yes_action=[Hide("confirm"),Return(1)],
                            no_action=Hide("confirm"))
            if persistent.arc_clear[0]:
                imagebutton xsize 450 idle "gui/menu_art_n.png" hover "mod_assets/gui/menu_art_n_hover.png" hovered tt.Action("{color=#cf0f88}Second Chance{/color}") hover_sound gui.hover_sound activate_sound gui.activate_sound focus_mask True at custom_start_zoom_3:
                    action Show(screen="confirm", message="Are you sure you want to start in Natsuki's arc?",
                            yes_action=[Hide("confirm"),Return(2)],
                            no_action=Hide("confirm"))
            else:
                imagebutton xsize 450 idle "mod_assets/gui/menu_art_n_locked.png" action NullAction() hovered tt.Action("This arc is locked") hover_sound gui.hover_sound at custom_start_zoom_3
            if persistent.arc_clear[1]:
                imagebutton xsize 450 idle "gui/menu_art_s.png" hover "mod_assets/gui/menu_art_s_hover.png" hovered tt.Action("{color=#6ecbfa}Inauguration Day{/color}") hover_sound gui.hover_sound activate_sound gui.activate_sound focus_mask True at custom_start_zoom_4:
                    action Show(screen="confirm", message="Are you sure you want to start in Sayori's arc?",
                            yes_action=[Hide("confirm"),Return(3)],
                            no_action=Hide("confirm"))
            else:
                imagebutton xsize 450 idle "mod_assets/gui/menu_art_s_locked.png" action NullAction() hovered tt.Action("This arc is locked") hover_sound gui.hover_sound at custom_start_zoom_4

    fixed at show_hide_fade_after:
        vbox:
            xalign 0.5
            yalign 0.99

            text tt.value:
                text_align 0.5

init -501 screen customstart_girlchoice(background,labeltext,chibis,excludemyself=True,locked1=False,locked2=False,locked3=False,locked4=False):

    default tt = Tooltip("")

    add background at show_hide_fade_bg_quick

    style_prefix "choice"

    fixed at show_hide_fade_quick:
        xalign 0.5
        yalign 0.5

        label _(labeltext):
            text_style "game_menu_label_text"
            xalign 0.5
            yalign 0.0

        grid 4 1:
            xalign 0.5
            if chibis:
                yalign 0.6
                spacing 30
            else:
                yalign 2.3
                spacing 60

            if chibis:
                if locked1:
                    imagebutton idle im.Grayscale("gui/poemgame/s_sticker_1.png") action NullAction() hovered tt.Action("{color=#6ecbfa}Sayori{/color} (Unavailable)") hover_sound gui.hover_sound focus_mask True xalign 0.5
                else:
                    imagebutton idle "gui/poemgame/s_sticker_1.png" hover "gui/poemgame/s_sticker_2.png" selected_idle "gui/poemgame/s_sticker_2.png" selected_hover "gui/poemgame/s_sticker_2.png" action Return(0) hovered tt.Action("{color=#6ecbfa}Sayori{/color}") hover_sound gui.hover_sound activate_sound gui.activate_sound focus_mask True xalign 0.5
                if locked2:
                    imagebutton idle im.Grayscale("gui/poemgame/m_sticker_1.png") action NullAction() hovered tt.Action("{color=#8ed73a}Monika{/color} (Unavailable)") hover_sound gui.hover_sound focus_mask True xalign 0.5
                else:
                    imagebutton idle "gui/poemgame/m_sticker_1.png" hover "gui/poemgame/m_sticker_2.png" selected_idle "gui/poemgame/m_sticker_2.png" selected_hover "gui/poemgame/m_sticker_2.png" action Return(1) hovered tt.Action("{color=#8ed73a}Monika{/color}") hover_sound gui.hover_sound activate_sound gui.activate_sound focus_mask True xalign 0.5
                if locked3:
                    imagebutton idle im.Grayscale("gui/poemgame/n_sticker_1.png") action NullAction() hovered tt.Action("{color=#cf0f88}Natsuki{/color} (Unavailable)") hover_sound gui.hover_sound focus_mask True xalign 0.5
                else:
                    imagebutton idle "gui/poemgame/n_sticker_1.png" hover "gui/poemgame/n_sticker_2.png" selected_idle "gui/poemgame/n_sticker_2.png" selected_hover "gui/poemgame/n_sticker_2.png" action Return(2) hovered tt.Action("{color=#cf0f88}Natsuki{/color}") hover_sound gui.hover_sound activate_sound gui.activate_sound focus_mask True xalign 0.5
                if locked4:
                    imagebutton idle im.Grayscale("gui/poemgame/y_sticker_1.png") action NullAction() hovered tt.Action("{color=#d88dee}Yuri{/color} (Unavailable)") hover_sound gui.hover_sound focus_mask True xalign 0.5
                else:
                    imagebutton idle "gui/poemgame/y_sticker_1.png" hover "gui/poemgame/y_sticker_2.png" selected_idle "gui/poemgame/y_sticker_2.png" selected_hover "gui/poemgame/y_sticker_2.png" action Return(3) hovered tt.Action("{color=#d88dee}Yuri{/color}") hover_sound gui.hover_sound activate_sound gui.activate_sound focus_mask True xalign 0.5
            else:
                if locked1:
                    imagebutton xsize 450 idle "mod_assets/gui/menu_art_s_locked.png" action NullAction() hovered tt.Action("{color=#6ecbfa}Sayori{/color} (Unavailable)") hover_sound gui.hover_sound at custom_start_zoom_insta
                else:
                    imagebutton xsize 450 idle "gui/menu_art_s.png" hover "mod_assets/gui/menu_art_s_hover.png" action Return(0) hovered tt.Action("{color=#6ecbfa}Sayori{/color}") hover_sound gui.hover_sound activate_sound gui.activate_sound focus_mask True at custom_start_zoom_insta
                if locked2:
                    imagebutton xsize 450 idle "mod_assets/gui/menu_art_m_locked.png" action NullAction() hovered tt.Action("{color=#8ed73a}Monika{/color} (Unavailable)") hover_sound gui.hover_sound at custom_start_zoom_insta
                else:
                    imagebutton xsize 450 idle "gui/menu_art_m.png" hover "mod_assets/gui/menu_art_m_hover.png" action Return(1) hovered tt.Action("{color=#8ed73a}Monika{/color}") hover_sound gui.hover_sound activate_sound gui.activate_sound focus_mask True at custom_start_zoom_insta
                if locked3:
                    imagebutton xsize 450 idle "mod_assets/gui/menu_art_n_locked.png" action NullAction() hovered tt.Action("{color=#cf0f88}Natsuki{/color} (Unavailable)") hover_sound gui.hover_sound at custom_start_zoom_insta
                else:
                    imagebutton xsize 450 idle "gui/menu_art_n.png" hover "mod_assets/gui/menu_art_n_hover.png" action Return(2) hovered tt.Action("{color=#cf0f88}Natsuki{/color}") hover_sound gui.hover_sound activate_sound gui.activate_sound focus_mask True at custom_start_zoom_insta
                if locked4:
                    imagebutton xsize 450 idle "mod_assets/gui/menu_art_y_locked.png" action NullAction() hovered tt.Action("{color=#d88dee}Yuri{/color} (Unavailable)") hover_sound gui.hover_sound at custom_start_zoom_insta
                else:
                    imagebutton xsize 450 idle "gui/menu_art_y.png" hover "mod_assets/gui/menu_art_y_hover.png" action Return(3) hovered tt.Action("{color=#d88dee}Yuri{/color}") hover_sound gui.hover_sound activate_sound gui.activate_sound focus_mask True at custom_start_zoom_insta

        if not excludemyself:
            hbox:
                xalign 0.5
                yalign 0.1

                textbutton _("Myself") action Return(4)

    fixed at show_hide_fade_quick:
        vbox:
            xalign 0.5
            if chibis:
                yalign 0.99
            else:
                if not excludemyself:
                    yalign 0.16
                else:
                    yalign 0.13

            text tt.value:
                if chibis:
                    size 40
                else:
                    if not excludemyself:
                        size 45
                    else:
                        size 50
                text_align 0.5

init -501 screen customstart_twobgchoice(labeltext,bg1,text1,bg2,text2,multi,highlight1=False,highlight2=False,lock1=False,lock2=False):

    default tt = Tooltip("")

    default choicea = highlight1
    default colora = "#f00"
    default choiceb = highlight2
    default colorb = "#f00"

    style_prefix "choice"

    fixed at show_hide_fade_quick:
        yalign 0.5

        grid 2 1:
            if multi:
                if lock1:
                    imagebutton:
                        action [NullAction(), Function(renpy.restart_interaction)]
                        idle im.Crop(im.Grayscale(bg1), (320, 0, 640, 720))
                        selected_idle im.Crop(bg1, (480, 0, 320, 720))
                        selected_hover im.Crop(im.MatrixColor(bg1, im.matrix.saturation(0.7)), (320, 0, 640, 720))
                        hovered tt.Action("{color="+colora+"}[text1] (Unavailable){/color}")
                        selected choicea
                        hover_sound gui.hover_sound
                else:
                    imagebutton:
                        action [ToggleScreenVariable("colora","#0f0","#f00"), ToggleScreenVariable("choicea",True,False), Function(renpy.restart_interaction)]
                        idle im.Crop(im.Grayscale(bg1), (320, 0, 640, 720))
                        hover im.Crop(im.MatrixColor(bg1, im.matrix.saturation(0.3)), (320, 0, 640, 720))
                        selected_idle im.Crop(bg1, (480, 0, 320, 720))
                        selected_hover im.Crop(im.MatrixColor(bg1, im.matrix.saturation(0.7)), (320, 0, 640, 720))
                        hovered tt.Action("{color="+colora+"}[text1]{/color}")
                        selected choicea
                        hover_sound gui.hover_sound
                        activate_sound gui.activate_sound
                if lock2:
                    imagebutton:
                        action [NullAction(), Function(renpy.restart_interaction)]
                        idle im.Crop(im.Grayscale(bg2), (320, 0, 640, 720))
                        selected_idle im.Crop(bg2, (320, 0, 640, 720))
                        selected_hover im.Crop(im.MatrixColor(bg2, im.matrix.saturation(0.7)), (320, 0, 640, 720))
                        hovered tt.Action("{color="+colorb+"}[text2] (Unavailable){/color}")
                        hover_sound gui.hover_sound
                else:
                    imagebutton:
                        action [ToggleScreenVariable("colorb","#0f0","#f00"), ToggleScreenVariable("choiceb",True,False), Function(renpy.restart_interaction)]
                        idle im.Crop(im.Grayscale(bg2), (320, 0, 640, 720))
                        hover im.Crop(im.MatrixColor(bg2, im.matrix.saturation(0.3)), (320, 0, 640, 720))
                        selected_idle im.Crop(bg2, (320, 0, 640, 720))
                        selected_hover im.Crop(im.MatrixColor(bg2, im.matrix.saturation(0.7)), (320, 0, 640, 720))
                        hovered tt.Action("{color="+colorb+"}[text2]{/color}")
                        selected choiceb
                        hover_sound gui.hover_sound
                        activate_sound gui.activate_sound
            else:
                if lock1:
                    imagebutton:
                        action [NullAction(), Function(renpy.restart_interaction)]
                        idle im.Crop(im.Grayscale(bg1), (320, 0, 640, 720))
                        hovered tt.Action(text1 + " (Unavailable)")
                        hover_sound gui.hover_sound
                else:
                    imagebutton:
                        action Return(0)
                        idle im.Crop(im.Grayscale(bg1), (320, 0, 640, 720))
                        hover im.Crop(bg1, (320, 0, 640, 720))
                        hovered tt.Action(text1)
                        hover_sound gui.hover_sound
                        activate_sound gui.activate_sound
                if lock2:
                    imagebutton:
                        action [NullAction(), Function(renpy.restart_interaction)]
                        idle im.Crop(im.Grayscale(bg2), (320, 0, 640, 720))
                        hovered tt.Action(text2 + " (Unavailable)")
                        hover_sound gui.hover_sound
                else:
                    imagebutton:
                        action Return(1)
                        idle im.Crop(im.Grayscale(bg2), (320, 0, 640, 720))
                        hover im.Crop(bg2, (320, 0, 640, 720))
                        hovered tt.Action(text2)
                        hover_sound gui.hover_sound
                        activate_sound gui.activate_sound

        label _(labeltext):
            text_style "game_menu_label_text"
            xalign 0.5
            yalign 0.0

        if multi:
            hbox:
                xalign 0.5
                yalign 0.9

                textbutton _("Done") action Return([choicea,choiceb])


    fixed at show_hide_fade_quick:
        vbox:
            xalign 0.5
            yalign 0.99

            text tt.value:
                size 40
                text_align 0.5

init -501 screen customstart_fourbgchoice(labeltext,bg1,text1,bg2,text2,bg3,text3,bg4,text4,multi,highlight1=False,highlight2=False,highlight3=False,highlight4=False):

    default tt = Tooltip("")

    default choicea = highlight1
    default colora = "#f00"
    default choiceb = highlight2
    default colorb = "#f00"
    default choicec = highlight3
    default colorc = "#f00"
    default choiced = highlight4
    default colord = "#f00"

    style_prefix "choice"

    fixed at show_hide_fade_quick:
        yalign 0.5

        grid 4 1:
            if multi:
                imagebutton:
                    action [ToggleScreenVariable("colora","#0f0","#f00"), ToggleScreenVariable("choicea",True,False), Function(renpy.restart_interaction)]
                    idle im.Crop(im.Grayscale(bg1), (480, 0, 320, 720))
                    hover im.Crop(im.MatrixColor(bg1, im.matrix.saturation(0.3)), (480, 0, 320, 720))
                    selected_idle im.Crop(bg1, (480, 0, 320, 720))
                    selected_hover im.Crop(im.MatrixColor(bg1, im.matrix.saturation(0.7)), (480, 0, 320, 720))
                    hovered tt.Action("{color="+colora+"}[text1]{/color}")
                    selected choicea
                    hover_sound gui.hover_sound
                    activate_sound gui.activate_sound
                imagebutton:
                    action [ToggleScreenVariable("colorb","#0f0","#f00"), ToggleScreenVariable("choiceb",True,False), Function(renpy.restart_interaction)]
                    idle im.Crop(im.Grayscale(bg2), (480, 0, 320, 720))
                    hover im.Crop(im.MatrixColor(bg2, im.matrix.saturation(0.3)), (480, 0, 320, 720))
                    selected_idle im.Crop(bg2, (480, 0, 320, 720))
                    selected_hover im.Crop(im.MatrixColor(bg2, im.matrix.saturation(0.7)), (480, 0, 320, 720))
                    hovered tt.Action("{color="+colorb+"}[text2]{/color}")
                    selected choiceb
                    hover_sound gui.hover_sound
                    activate_sound gui.activate_sound
                imagebutton:
                    action [ToggleScreenVariable("colorc","#0f0","#f00"), ToggleScreenVariable("choicec",True,False), Function(renpy.restart_interaction)]
                    idle im.Crop(im.Grayscale(bg3), (480, 0, 320, 720))
                    hover im.Crop(im.MatrixColor(bg3, im.matrix.saturation(0.3)), (480, 0, 320, 720))
                    selected_idle im.Crop(bg3, (480, 0, 320, 720))
                    selected_hover im.Crop(im.MatrixColor(bg3, im.matrix.saturation(0.7)), (480, 0, 320, 720))
                    hovered tt.Action("{color="+colorc+"}[text3]{/color}")
                    selected choicec
                    hover_sound gui.hover_sound
                    activate_sound gui.activate_sound
                imagebutton:
                    action [ToggleScreenVariable("colord","#0f0","#f00"), ToggleScreenVariable("choiced",True,False), Function(renpy.restart_interaction)]
                    idle im.Crop(im.Grayscale(bg4), (480, 0, 320, 720))
                    hover im.Crop(im.MatrixColor(bg4, im.matrix.saturation(0.3)), (480, 0, 320, 720))
                    selected_idle im.Crop(bg4, (480, 0, 320, 720))
                    selected_hover im.Crop(im.MatrixColor(bg4, im.matrix.saturation(0.7)), (480, 0, 320, 720))
                    hovered tt.Action("{color="+colord+"}[text4]{/color}")
                    selected choiced
                    hover_sound gui.hover_sound
                    activate_sound gui.activate_sound
            else:
                imagebutton:
                    action Return(0)
                    idle im.Crop(im.Grayscale(bg1), (480, 0, 320, 720))
                    hover im.Crop(bg1, (480, 0, 320, 720))
                    hovered tt.Action(text1)
                    hover_sound gui.hover_sound
                    activate_sound gui.activate_sound
                imagebutton:
                    action Return(1)
                    idle im.Crop(im.Grayscale(bg2), (480, 0, 320, 720))
                    hover im.Crop(bg2, (480, 0, 320, 720))
                    hovered tt.Action(text2)
                    hover_sound gui.hover_sound
                    activate_sound gui.activate_sound
                imagebutton:
                    action Return(2)
                    idle im.Crop(im.Grayscale(bg3), (480, 0, 320, 720))
                    hover im.Crop(bg3, (480, 0, 320, 720))
                    hovered tt.Action(text3)
                    hover_sound gui.hover_sound
                    activate_sound gui.activate_sound
                imagebutton:
                    action Return(3)
                    idle im.Crop(im.Grayscale(bg4), (480, 0, 320, 720))
                    hover im.Crop(bg4, (480, 0, 320, 720))
                    hovered tt.Action(text4)
                    hover_sound gui.hover_sound
                    activate_sound gui.activate_sound

        label _(labeltext):
            text_style "game_menu_label_text"
            xalign 0.5
            yalign 0.0

        if multi:
            hbox:
                xalign 0.5
                yalign 0.9

                textbutton _("Done") action Return([choicea,choiceb,choicec,choiced])


    fixed at show_hide_fade_quick:
        vbox:
            xalign 0.5
            yalign 0.99

            text tt.value:
                size 40
                text_align 0.5

init -501 screen customstart_twochoice(background,labeltext,image1,text1,image2,text2):

    default tt = Tooltip("")

    add background at show_hide_fade_bg_quick

    fixed at show_hide_fade_quick:
        xalign 0.5
        yalign 0.5

        label _(labeltext):
            text_style "game_menu_label_text"
            xalign 0.5
            yalign 0.0

        grid 2 1:
            xalign 0.5
            yalign 0.6
            spacing 200

            imagebutton idle image1+"_idle.png" hover image1+"_hover.png" action Return(0) hovered tt.Action(text1) hover_sound gui.hover_sound activate_sound gui.activate_sound xalign 0.5
            imagebutton idle image2+"_idle.png" hover image2+"_hover.png" action Return(1) hovered tt.Action(text2) hover_sound gui.hover_sound activate_sound gui.activate_sound xalign 0.5

    fixed at show_hide_fade_quick:
        vbox:
            xalign 0.5
            yalign 0.99

            text tt.value:
                size 40
                text_align 0.5

init -501 screen bonusdays_bonusdaychoice(background,labeltext,chibis,locked1=False,locked2=False,locked3=False,locked4=False,locked5=False,locked6=False,mc_name=""):

    default tt = Tooltip("")

    add background at show_hide_fade_bg_quick

    style_prefix "choice"

    fixed at show_hide_fade_quick:
        xalign 0.5
        yalign 0.5

        label _(labeltext):
            text_style "game_menu_label_text"
            xalign 0.5
            yalign 0.0

        grid 2 3:
            xalign 0.5
            yalign 0.6
            spacing 30

            if locked1:
                imagebutton idle im.Grayscale("gui/poemgame/s_sticker_1.png") action NullAction() hovered tt.Action("{color=#6ecbfa}Sayori{/color} (Unavailable)") hover_sound gui.hover_sound focus_mask True xalign 0.5
            else:
                imagebutton idle "gui/poemgame/s_sticker_1.png" hover "gui/poemgame/s_sticker_2.png" selected_idle "gui/poemgame/s_sticker_2.png" selected_hover "gui/poemgame/s_sticker_2.png" action Return(0) hovered tt.Action("{color=#6ecbfa}Sayori{/color}") hover_sound gui.hover_sound activate_sound gui.activate_sound focus_mask True xalign 0.5
            if locked2:
                imagebutton idle im.Grayscale("gui/poemgame/m_sticker_1.png") action NullAction() hovered tt.Action("{color=#8ed73a}Monika{/color} (Unavailable)") hover_sound gui.hover_sound focus_mask True xalign 0.5
            else:
                imagebutton idle "gui/poemgame/m_sticker_1.png" hover "gui/poemgame/m_sticker_2.png" selected_idle "gui/poemgame/m_sticker_2.png" selected_hover "gui/poemgame/m_sticker_2.png" action Return(1) hovered tt.Action("{color=#8ed73a}Monika{/color}") hover_sound gui.hover_sound activate_sound gui.activate_sound focus_mask True xalign 0.5
            if locked3:
                imagebutton idle im.Grayscale("mod_assets/gui/poemgame/mh_sticker_1.png") action NullAction() hovered tt.Action("{color=#8ed73a}Monika?{/color} (Unavailable)") hover_sound gui.hover_sound focus_mask True xalign 0.5
            else:
                imagebutton idle "mod_assets/gui/poemgame/mh_sticker_1.png" hover "mod_assets/gui/poemgame/mh_sticker_2.png" selected_idle "mod_assets/gui/poemgame/mh_sticker_2.png" selected_hover "mod_assets/gui/poemgame/mh_sticker_2.png" action Return(2) hovered tt.Action("{color=#f21237}Markov{/color}") hover_sound gui.hover_sound activate_sound gui.activate_sound focus_mask True xalign 0.5
            if locked4:
                imagebutton idle im.Grayscale("mod_assets/gui/poemgame/ay_sticker_1.png") action NullAction() hovered tt.Action("{color=#d28c5e}Ayame{/color} (Unavailable)") hover_sound gui.hover_sound focus_mask True xalign 0.5
            else:
                imagebutton idle "mod_assets/gui/poemgame/ay_sticker_1.png" hover "mod_assets/gui/poemgame/ay_sticker_2.png" selected_idle "mod_assets/gui/poemgame/ay_sticker_2.png" selected_hover "mod_assets/gui/poemgame/ay_sticker_2.png" action Return(3) hovered tt.Action("{color=#d28c5e}Ayame{/color}") hover_sound gui.hover_sound activate_sound gui.activate_sound focus_mask True xalign 0.5
            if locked5:
                imagebutton idle im.Grayscale("mod_assets/gui/poemgame/mc_sticker_1.png") action NullAction() hovered tt.Action("{color=#ffffff}[mc_name]{/color} (Unavailable)") hover_sound gui.hover_sound focus_mask True xalign 0.5
            else:
                imagebutton idle "mod_assets/gui/poemgame/mc_sticker_1.png" hover "mod_assets/gui/poemgame/mc_sticker_1.png" selected_idle "mod_assets/gui/poemgame/mc_sticker_1.png" selected_hover "mod_assets/gui/poemgame/mc_sticker_1.png" action Return(4) hovered tt.Action("{color=#ffffff}[mc_name]{/color}") hover_sound gui.hover_sound activate_sound gui.activate_sound focus_mask True xalign 0.5
            if locked6:
                imagebutton idle im.Grayscale("mod_assets/gui/poemgame/unknown_sticker_1.png") action NullAction() hovered tt.Action("{color=#ffffff}Unknown{/color} (Unavailable)") hover_sound gui.hover_sound focus_mask True xalign 0.5
            else:
                imagebutton idle "mod_assets/gui/poemgame/unknown_sticker_1.png" hover "mod_assets/gui/poemgame/unknown_sticker_1.png" selected_idle "mod_assets/gui/poemgame/unknown_sticker_1.png" selected_hover "mod_assets/gui/poemgame/unknown_sticker_1.png" action Return(5) hovered tt.Action("{color=#ffffff}Unknown{/color}") hover_sound gui.hover_sound activate_sound gui.activate_sound focus_mask True xalign 0.5

    fixed at show_hide_fade_quick:
        vbox:
            xalign 0.5
            yalign 0.99

            text tt.value:
                size 40
                text_align 0.5

init -501 screen item(item):
    frame:
        xalign 0.5
        yalign 0.3
        xsize 400
        ysize 400

        at show_hide_fade_bg_quick

        add item xalign 0.5 yalign 0.5 at show_hide_fade_bg_quick

init -501 screen achievements tag menu:

        default achname = Tooltip("")
        default achdesc = Tooltip("")
        default gridx = 6
        default gridy = 10
        default imageshow = None
        default colored = False

        use game_menu("{size=24}Achievements{/size}","viewport"):

            fixed:
                yalign 0.2
                yfit True
                order_reverse True

                button:
                    style "page_label"

                    xalign 0.5

                grid gridx gridy:

                    xalign 0.5
                    yalign 0
                    ypos 50

                    spacing 30

                    $ slot = 0

                    for ach in persistent.achievements_dict:

                        imagebutton:
                            xsize 100
                            ysize 100
                            xalign 0.5
                            yalign 0.5

                            action NullAction()
                            hovered [achname.Action(persistent.achievements_dict[ach]["title"]), achdesc.Action(persistent.achievements_dict[ach]["text"]), SetScreenVariable("imageshow",persistent.achievements_dict[ach]["icon"]), SetScreenVariable("colored",persistent.achievements_dict[ach]["achieved"]), Function(renpy.restart_interaction)]
                            unhovered [SetScreenVariable("imageshow",None), SetScreenVariable("colored",False), Function(renpy.restart_interaction)]
                            hover_sound gui.hover_sound

                            insensitive im.MatrixColor("mod_assets/gui/achievements/achhidden.png", im.matrix.saturation(0))
                            idle im.MatrixColor(im.Composite((96, 96), (0, 0), persistent.achievements_dict[ach]["icon"], (0, 0), im.MatrixColor("mod_assets/gui/achievements/achlockedoverlay.png", im.matrix.opacity(0.4))), im.matrix.saturation(0))
                            hover im.MatrixColor(im.Composite((96, 96), (0, 0), persistent.achievements_dict[ach]["icon"], (0, 0), im.MatrixColor("mod_assets/gui/achievements/achlockedoverlay.png", im.matrix.opacity(0.2))), im.matrix.saturation(0.2))
                            selected_idle im.MatrixColor(persistent.achievements_dict[ach]["icon"], im.matrix.saturation(0.7))
                            selected_hover persistent.achievements_dict[ach]["icon"]
                            selected persistent.achievements_dict[ach]["achieved"]
                            sensitive (persistent.achievements_dict[ach]["achieved"] or (persistent.achievements_dict[ach]["achieved"] and persistent.achievements_dict[ach]["hidden"]) or (not persistent.achievements_dict[ach]["achieved"] and not persistent.achievements_dict[ach]["hidden"]))

                    # Fill the rest with empty nulls
                    for i in range(0, (gridx*gridy)-len(persistent.achievements_dict)):
                        null

        fixed:
            add (None if imageshow == None else im.Scale(imageshow, 115, 115) if colored else im.Scale(im.MatrixColor(imageshow, im.matrix.saturation(0)), 115, 115)) xpos 490 yalign 0.01
            text achname.value:
                text_align 0.0
                size 30
                xpos 627
                yalign 0.04
            text achdesc.value:
                text_align 0.0
                size 24
                xpos 627
                yalign 0.10

init -1 style confirm_frame is gui_frame
init -1 style confirm_prompt is gui_prompt
init -1 style confirm_prompt_text is gui_prompt_text
init -1 style confirm_button is gui_medium_button
init -1 style confirm_button_text is gui_medium_button_text

init -1 style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

init -1 style confirm_prompt_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"

init -1 style confirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

init -1 style confirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")








init -501 screen fake_skip_indicator():
    use skip_indicator

init -501 screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 6

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform -1 delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


init -1 style skip_frame is empty
init -1 style skip_text is gui_text
init -1 style skip_triangle is skip_text

init -1 style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

init -1 style skip_text:
    size gui.notify_text_size

init -1 style skip_triangle:


    font "DejaVuSans.ttf"









init -501 screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform -1 notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

transform -1 custom_start_zoom_insta:
    zoom 0.6

transform -1 custom_start_zoom_1:
    zoom 0.6
    alpha 0
    linear 0.8 alpha 1.0

transform -1 custom_start_zoom_2:
    zoom 0.6
    alpha 0
    0.4
    linear 0.8 alpha 1.0

transform -1 custom_start_zoom_3:
    zoom 0.6
    alpha 0
    0.8
    linear 0.8 alpha 1.0

transform -1 custom_start_zoom_4:
    zoom 0.6
    alpha 0
    1.2
    linear 0.8 alpha 1.0

transform -1 show_hide_fade_bg:
    on show:
        alpha .0
        easein 1.0 alpha 1.0
    on hide:
        alpha 1.0
        easeout 2.0 alpha .0

transform -1 show_hide_fade_bg_quick:
    on show:
        alpha .0
        easein 1.0 alpha 1.0
    on hide:
        alpha 1.0
        easeout 0.75 alpha .0

transform -1 show_hide_fade:
    on show:
        alpha .0
        linear 2.0 alpha 1.0
    on hide:
        alpha 1.0
        linear 1.0 alpha .0

transform -1 show_hide_fade_quick:
    on show:
        alpha .0
        linear 0.75 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha .0

transform -1 show_hide_fade_after:
    alpha 0
    1.6
    linear 0.4 alpha 1.0
    on hide:
        alpha 1.0
        linear 1.4 alpha .0


init -1 style notify_frame is empty
init -1 style notify_text is gui_text

init -1 style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

init -1 style notify_text:
    size gui.notify_text_size
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
