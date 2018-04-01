init python:
    import datetime

image credits_cg1:
    "images/cg/credits/1.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg2:
    "images/cg/credits/2.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg3:
    "images/cg/credits/3.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg4:
    "images/cg/credits/4.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg5:
    "images/cg/credits/5.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg6:
    "images/cg/credits/6.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg7:
    "images/cg/credits/7.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg8:
    "images/cg/credits/8.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg9:
    "images/cg/credits/9.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg10:
    "images/cg/credits/10.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg1_locked:
    "images/cg/credits/1b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg2_locked:
    "images/cg/credits/2b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg3_locked:
    "images/cg/credits/3b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg4_locked:
    "images/cg/credits/4b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg5_locked:
    "images/cg/credits/5b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg6_locked:
    "images/cg/credits/6b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg7_locked:
    "images/cg/credits/7b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg8_locked:
    "images/cg/credits/8b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg9_locked:
    "images/cg/credits/9b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg10_locked:
    "images/cg/credits/10b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg1_clearall:
    "images/cg/credits/1.png"
    size (640, 360)

image credits_cg2_clearall:
    "images/cg/credits/2.png"
    size (640, 360)

image credits_cg3_clearall:
    "images/cg/credits/3.png"
    size (640, 360)

image credits_cg4_clearall:
    "images/cg/credits/4.png"
    size (640, 360)

image credits_cg5_clearall:
    "images/cg/credits/5.png"
    size (640, 360)

image credits_cg6_clearall:
    "images/cg/credits/6.png"
    size (640, 360)

image credits_cg7_clearall:
    "images/cg/credits/7.png"
    size (640, 360)

image credits_cg8_clearall:
    "images/cg/credits/8.png"
    size (640, 360)

image credits_cg9_clearall:
    "images/cg/credits/9.png"
    size (640, 360)

image credits_cg10_clearall:
    "images/cg/credits/10.png"
    size (640, 360)

image credits_cg10alt_bad:
    "images/cg/credits/10.png"
    size (640, 360)
    9.4
    "images/menu/notfound.png"

image credits_cg10alt_bittersweet:
    "mod_assets/images/cg/credits/10alt.png"
    size (640, 360)
    9.4
    "images/menu/notfound.png"

image credits_cg10alt_good:
    "mod_assets/images/cg/credits/10alt.png"
    size (640, 360)

image credits_logo:
    "gui/logo.png"
    truecenter
    zoom 0.6 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

image credits_ts:
    "images/bg/splash-white.png"
    xalign 0.5 yalign 0.6
    zoom 0.65 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

style credits_header:
    font "gui/font/RifficFree-Bold.ttf"
    color "#ffaae6"
    size 36
    text_align 0.5
    outlines []

style credits_text:
    font "gui/font/Halogen.ttf"
    color "#fff"
    size 36
    text_align 0.5
    outlines []

style credits_text_small:
    font "gui/font/Halogen.ttf"
    color "#fff"
    size 30
    text_align 0.5
    outlines []

style monika_credits_text:
    font "gui/font/m1.ttf"
    color "#fff"
    size 40
    text_align 0.5
    outlines []

image credits_header = ParameterizedText(style="credits_header", ypos=-40)
image credits_text = ParameterizedText(style="credits_text", ypos=40)
image credits_text_small = ParameterizedText(style="credits_text_small", ypos=53)
image monika_credits_text = ParameterizedText(style="monika_credits_text", xalign=0.5)


transform credits_scroll:
    subpixel True
    yoffset 740
    linear 15 yoffset -380

transform credits_text_scroll:
    anchor (0.5, 0.5) subpixel True
    yoffset 920
    linear 15 yoffset -200

transform credits_sticker_scroll:
    subpixel True
    yoffset 940
    7.8
    linear 15 yoffset -180

transform credits_scroll_right:
    xalign 0.9
    credits_scroll

transform credits_scroll_left:
    xalign 0.1
    credits_scroll

transform credits_text_scroll_right:
    xpos 960
    credits_text_scroll

transform credits_text_scroll_right1:
    xpos 865
    credits_text_scroll

transform credits_text_scroll_right2:
    xpos 1055
    credits_text_scroll

transform credits_text_scroll_left:
    xpos 320
    credits_text_scroll

transform credits_sticker_1:
    yanchor 1.00
    xalign 0.32
    credits_sticker_scroll
transform credits_sticker_2:
    yanchor 1.00
    xalign 0.44
    credits_sticker_scroll
transform credits_sticker_3:
    yanchor 1.00
    xalign 0.56
    credits_sticker_scroll
transform credits_sticker_4:
    yanchor 1.00
    xalign 0.68
    credits_sticker_scroll

define credits_ypos = 250

#Normal Credits
image mcredits_1a:
    ypos credits_ypos
    xoffset -205
    "black"
    10.33
    Text("Every day,", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_1b:
    ypos credits_ypos
    xoffset -35
    "black"
    11.75
    Text("I imagine a future where", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 12.0, ramplen=4, alpha=False)
image mcredits_1c:
    ypos credits_ypos
    xoffset 170
    "black"
    13.76
    Text("I can be with you", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4, alpha=False)
image mcredits_2a:
    ypos credits_ypos + 50
    xoffset -226
    "black"
    19.45
    Text("In my hand", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_2b:
    ypos credits_ypos + 50
    xoffset -10
    "black"
    20.9
    Text(" is a pen that will write a poem", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)
image mcredits_2c:
    ypos credits_ypos + 50
    xoffset 225
    "black"
    23.27
    Text("of me and you", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4, alpha=False)

image mcredits_3:
    ypos credits_ypos + 100
    "black"
    28.35
    Text("The ink flows down into a dark puddle", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 16.0, ramplen=4, alpha=False)

image mcredits_4:
    ypos credits_ypos + 150
    xoffset -5
    "black"
    32.9
    Text(" Just move your hand -- write the way into his heart!", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)
image mcredits_5:
    ypos credits_ypos + 200
    "black"
    37.5
    Text("But in this world of infinite choices", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 16.0, ramplen=4, alpha=False)

image mcredits_6a:
    ypos credits_ypos + 250
    xoffset -145
    "black"
    42.0
    Text(" What will it take", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)
image mcredits_6b:
    ypos credits_ypos + 250
    xoffset 85
    "black"
    43.47
    Text(" just to find that special day?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)

#Mod Credits
image mcreditsm_1a:
    ypos credits_ypos
    xoffset -205
    "black"
    10.33
    Text(glitchtext(11), style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcreditsm_1b:
    ypos credits_ypos
    xoffset -35
    "black"
    11.75
    Text(glitchtext(24), style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 12.0, ramplen=4, alpha=False)
image mcreditsm_1c:
    ypos credits_ypos
    xoffset 170
    "black"
    13.76
    Text(glitchtext(17), style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4, alpha=False)
image mcreditsm_2a:
    ypos credits_ypos + 50
    xoffset -226
    "black"
    19.45
    Text(glitchtext(10), style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcreditsm_2b:
    ypos credits_ypos + 50
    xoffset -10
    "black"
    20.9
    Text(glitchtext(32), style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)
image mcreditsm_2c:
    ypos credits_ypos + 50
    xoffset 225
    "black"
    23.27
    Text(glitchtext(13), style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4, alpha=False)
image mcreditsm_3:
    ypos credits_ypos + 100
    "black"
    28.35
    Text(glitchtext(37), style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 16.0, ramplen=4, alpha=False)
image mcreditsm_4:
    ypos credits_ypos + 150
    xoffset -5
    "black"
    32.9
    Text(glitchtext(53), style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)
image mcreditsm_5:
    ypos credits_ypos + 200
    "black"
    37.5
    Text(glitchtext(37), style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 16.0, ramplen=4, alpha=False)
image mcreditsm_6a:
    ypos credits_ypos + 250
    xoffset -145
    "black"
    42.0
    Text(" What will it take", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)
image mcreditsm_6b:
    ypos credits_ypos + 250
    xoffset 85
    "black"
    43.47
    Text(" just to find that special day?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)

image mcredits_7:
    "black"
    alpha 0.0
    48.62
    linear 1.5 alpha 1.0

image mcredits_1_test:
    ypos credits_ypos + 300
    Text("What will it take just to find that special day?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4)

image end_glitch1:
    "bg/end-glitch1.jpg"
    alpha 0.0
    time 1.0
    alpha 1.0
    block:
        yoffset 1280 ytile 2
        linear 1 yoffset 0
        repeat
    time 9.45
    "end_glitch2"
    time 22.1
    "end_glitch3"
    time 28.65
    "end_glitch4"

image end_glitch2:
    "bg/end-glitch2.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch3:
    "bg/end-glitch3.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch4:
    parallel:
        "bg/end-glitch4.jpg"
        1.25
        "bg/end-glitch3.jpg"
        0.1
        repeat
    parallel:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

label credits_setup:
    $ persistent.autoload = "credits_setup"
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    scene black
    jump credits_start
    return

label credits:
    $ persistent.autoload = "credits"
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    scene black
    if persistent.monika_change and not persistent.monika_credits:
        play music "mod_assets/bgm/end-voicenew.ogg" noloop
    else:
        play music "bgm/end-voice.ogg" noloop

    show noise zorder 9:
        alpha 0.0
        linear 1.5 alpha 1.0
        time 2.0
        parallel:
            0.05
            choice:
                alpha 0.5
            choice:
                alpha 0.75
            choice:
                alpha 1.0
            repeat
        parallel:
            linear 0.375 alpha 0.7
            linear 0.375 alpha 1.0
        time 2.75
        alpha 0.95
        time 6.45
        alpha 0.3
        time 6.95
        alpha 0.9
        time 8.65
        linear 0.8 alpha 0
        alpha 0.5
        time 22.1
        alpha 0.85
        time 22.35
        alpha 0.5
        time 28.20
        alpha 0.3
        linear 0.45 alpha 0.9
        alpha 0.4
    show vignette zorder 10:
        alpha 0.75
        parallel:
            0.36
            alpha 0.75
            repeat
        parallel:
            0.49
            alpha 0.7
            repeat
    show end_glitch1 zorder 2
    show black as bar zorder 9:
        alpha 0.3
        size (1280,500)
        block:
            ypos 720
            linear 15 ypos -500
            repeat

    pause 39
    label credits_start:
    pause 2
    scene black
    pause 0.5
    $ consolehistory = []
    call updateconsole ("renpy.music.play(\"ddlc.ogg\")", "Playing audio \"ddlc.ogg\"...")
    pause 1.0
    call hideconsole
    if persistent.monika_change and not persistent.monika_credits:
        if persistent.dialogue_change[1]:
            play music "<to 50.0>mod_assets/bgm/creditsnewbad.ogg" noloop
        else:
            play music "<to 50.0>mod_assets/bgm/creditsnew.ogg" noloop
        show mcreditsm_1a zorder 50
        show mcreditsm_1b zorder 49
        show mcreditsm_1c zorder 48
        show mcreditsm_2a zorder 47
        show mcreditsm_2b zorder 46
        show mcreditsm_2c zorder 45
        show mcreditsm_3 zorder 44
        show mcreditsm_4 zorder 43
        show mcreditsm_5 zorder 42
        show mcreditsm_6a zorder 41
        show mcreditsm_6b zorder 40
    else:
        play music "<to 50.0>bgm/credits.ogg" noloop
        show mcredits_1a zorder 50
        show mcredits_1b zorder 49
        show mcredits_1c zorder 48
        show mcredits_2a zorder 47
        show mcredits_2b zorder 46
        show mcredits_2c zorder 45
        show mcredits_3 zorder 44
        show mcredits_4 zorder 43
        show mcredits_5 zorder 42
        show mcredits_6a zorder 41
        show mcredits_6b zorder 40
    show mcredits_7 zorder 51

    pause 50
    jump credits2

label credits2:
    python:
        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        monikaTime = renpy.random.random() * 4 + 4
        sayoriPos = 0
        natsukiPos = 0
        yuriPos = 0
        monikaPos = 0
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        monikaOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        monikaZoom = 1
        imagenum = 0
    scene black
    $ consolehistory = []
    if persistent.monika_change and not persistent.monika_credits:
        if persistent.dialogue_change[1]:
            play music "<from 50.0>mod_assets/bgm/creditsnewbad.ogg" noloop
        else:
            play music "<from 50.0>mod_assets/bgm/creditsnew.ogg" noloop
    else:
        play music "<from 50.0>bgm/credits.ogg" noloop
    $ starttime = datetime.datetime.now()
    pause 0.88
    show credits_logo
    pause 9.12
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ if persistent.monika_change: lockedtext = "_clearall"
    $ imagenum += 1
    show expression ("credits_cg1" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Concept & Game Design" as credits_header_1 at credits_text_scroll_left
    show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ if persistent.monika_change: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(16.95 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.monika_change:
        if not persistent.clearall:
            call updateconsole ("os.remove(\"images/cg/n_cg1.png\")", "n_cg1.png deleted successfully.")
        else:
            call updateconsole_clearall ("os.remove(\"images/cg/n_cg1.png\")", "n_cg1.png deleted successfully.")
    show expression ("credits_cg2" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Character Art" as credits_header_2 at credits_text_scroll_right
    show credits_text_small "Satchely\nRyuse\nTheAloofPotato\nDaydreamer" as credits_text_2 at credits_text_scroll_right1
    show credits_text_small "Danymations\nYuro Foxclaw\nTherationalpi\n" as credits_text_3 at credits_text_scroll_right2
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ if persistent.monika_change: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(26.05 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.monika_change:
        if not persistent.clearall:
            call updateconsole ("os.remove(\"images/cg/n_cg2.png\")", "n_cg2.png deleted successfully.")
        else:
            call updateconsole_clearall ("os.remove(\"images/cg/n_cg2.png\")", "n_cg2.png deleted successfully.")
    show expression ("credits_cg3" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Background Art" as credits_header_1 at credits_text_scroll_left
    show credits_text "Velinquent\nmugenjohncel\npetan" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ if persistent.monika_change: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.monika_change:
        if not persistent.clearall:
            call updateconsole ("os.remove(\"images/cg/y_cg1.png\")", "y_cg1.png deleted successfully.")
        else:
            call updateconsole_clearall ("os.remove(\"images/cg/y_cg1.png\")", "y_cg1.png deleted successfully.")
    show expression ("credits_cg4" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Writing" as credits_header_2 at credits_text_scroll_right
    show credits_text "Dan Salvato\nCompleteMonochrome" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ if persistent.monika_change: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(44.25 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.monika_change:
        if not persistent.clearall:
            call updateconsole ("os.remove(\"images/cg/y_cg2.png\")", "y_cg2.png deleted successfully.")
        else:
            call updateconsole_clearall ("os.remove(\"images/cg/y_cg2.png\")", "y_cg2.png deleted successfully.")
    show expression ("credits_cg5" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Music" as credits_header_1 at credits_text_scroll_left
    show credits_text "Dan Salvato\nG-RiNe Project" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ if persistent.monika_change: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(53.35 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.monika_change:
        if not persistent.clearall:
            call updateconsole ("os.remove(\"images/cg/n_cg3.png\")", "n_cg3.png deleted successfully.")
        else:
            call updateconsole_clearall ("os.remove(\"images/cg/n_cg3.png\")", "n_cg3.png deleted successfully.")
    show expression ("credits_cg6" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Vocals" as credits_header_2 at credits_text_scroll_right
    show credits_text "Jillian Ashcraft" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ if persistent.monika_change: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(62.45 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.monika_change:
        if not persistent.clearall:
            call updateconsole ("os.remove(\"images/cg/y_cg3.png\")", "y_cg3.png deleted successfully.")
        else:
            call updateconsole_clearall ("os.remove(\"images/cg/y_cg3.png\")", "y_cg3.png deleted successfully.")
    show expression ("credits_cg7" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Special Thanks" as credits_header_1 at credits_text_scroll_left
    show credits_text "Masha Gutin\nKagefumi" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ if persistent.monika_change: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(71.55 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.monika_change:
        if not persistent.clearall:
            call updateconsole ("os.remove(\"images/cg/s_cg1.png\")", "s_cg1.png deleted successfully.")
        else:
            call updateconsole_clearall ("os.remove(\"images/cg/s_cg1.png\")", "s_cg1.png deleted successfully.")
    show expression ("credits_cg8" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Special Thanks" as credits_header_2 at credits_text_scroll_right
    show credits_text "David Evelyn\nCorey Shin" as credits_text_2 at credits_text_scroll_right
    show s_sticker at credits_sticker_1
    show n_sticker at credits_sticker_2
    show y_sticker at credits_sticker_3
    if persistent.monika_change and not persistent.monika_credits:
        show m_sticker_bw at credits_sticker_4
    else:
        show m_sticker at credits_sticker_4
    $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ if persistent.monika_change: lockedtext = "_clearall"
    $ imagenum += 1
    if not persistent.monika_change:
        if not persistent.clearall:
            call updateconsole ("os.remove(\"images/cg/s_cg2.png\")", "s_cg2.png deleted successfully.")
        else:
            call updateconsole_clearall ("os.remove(\"images/cg/s_cg2.png\")", "s_cg2.png deleted successfully.")
    $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
    show expression ("credits_cg9" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Special Thanks" as credits_header_1 at credits_text_scroll_left
    show credits_text "Alecia Bardachino\nMatt Naples" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ if persistent.monika_change: lockedtext = "_clearall"
    $ pause(95.00 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.monika_change:
        if not persistent.clearall:
            call updateconsole ("os.remove(\"images/cg/s_cg3.png\")", "s_cg3.png deleted successfully.")
        else:
            call updateconsole_clearall ("os.remove(\"images/cg/s_cg3.png\")", "s_cg3.png deleted successfully.")
    elif not persistent.monika_credits:
        call updateconsole ("Goodbye", "NameError: name 'Goodbye' is not\ndefined")
    if persistent.monika_change:
        if persistent.monika_credits:
            show expression ("credits_cg10alt_good") as credits_image_2 at credits_scroll_left
        elif persistent.dialogue_change[1]:
            show expression ("credits_cg10alt_bad") as credits_image_2 at credits_scroll_left
        else:
            show expression ("credits_cg10alt_bittersweet") as credits_image_2 at credits_scroll_left
    else:
        show expression ("credits_cg10" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Special Thanks" as credits_header_2 at credits_text_scroll_right
    show credits_text "Monika\n[player]\nDDLCMods" as credits_text_2 at credits_text_scroll_right
    $ pause(104.10 - (datetime.datetime.now() - starttime).total_seconds())
    if persistent.monika_change and not persistent.monika_credits:
        call updateconsole ("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png deleted successfully.")
    else:
        if not persistent.monika_credits:
            if not persistent.clearall:
                call updateconsole ("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png deleted successfully.")
            else:
                call updateconsole_clearall ("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png deleted successfully.")
    if persistent.monika_credits:
        call updateconsole ("os.restore(\"game/screens.rpy\")", "screens.rpy restored successfully.")
        call updateconsole ("os.restore(\"game/gui.rpy\")", "gui.rpy restored successfully.")
        call updateconsole ("os.restore(\"game/menu.rpy\")", "menu.rpy restored successfully.")
        call updateconsole ("os.restore(\"game/script.rpy\")", "script.rpy restored successfully.")
    else:
        call updateconsole ("os.remove(\"game/screens.rpy\")", "screens.rpy deleted successfully.")
        call updateconsole ("os.remove(\"game/gui.rpy\")", "gui.rpy deleted successfully.")
        call updateconsole ("os.remove(\"game/menu.rpy\")", "menu.rpy deleted successfully.")
        call updateconsole ("os.remove(\"game/script.rpy\")", "script.rpy deleted successfully.")
    $ pause(115.72 - (datetime.datetime.now() - starttime).total_seconds())
    call hideconsole
    show credits_ts
    show credits_text "made with love by":
        zoom 0.75 xalign 0.5 yalign 0.25 alpha 0 subpixel True
        linear 2.0 alpha 1
        4.5
        linear 2.0 alpha 0
    pause 9.3
    play sound page_turn
    if persistent.monika_credits:
        show poem_newend with Dissolve(1)
    elif persistent.monika_change and not persistent.monika_credits:
        show poem_newendb with Dissolve(1)
    else:
        show poem_end with Dissolve(1)
    label postcredits_loop:
        $ persistent.autoload = "postcredits_loop"
        $ config.keymap['game_menu'] = []
        $ config.keymap['hide_windows'] = []
        $ renpy.display.behavior.clear_keymap_cache()
        $ quick_menu = False
        $ config.skipping = False
        $ config.allow_skipping = False
        scene black
        if persistent.monika_credits:
            show poem_newend
        elif persistent.monika_change and not persistent.monika_credits:
            show poem_newendb
        else:
            show poem_end
        $ pause()
        if persistent.monika_change and persistent.monika_credits:
            call screen dialog(message="Um...I think something has changed.\nLooks like you'll have to repeat today.\nBut it feels like it's going to be different...", ok_action=Function(renpy.full_restart, label="ch5_mainc"))
            # call screen dialog(message="Uh, oops I didn't think this would happen.\nLooks like we won't get to enjoy the festival.\nThanks for playing the mod!", ok_action=Quit(confirm=False))
        else:
            call screen dialog(message="Error: Script file is missing or corrupt.\nPlease reinstall the game.", ok_action=Quit(confirm=False))
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
