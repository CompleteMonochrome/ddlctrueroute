

transform tcommon(x=640, z=0.80):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:

        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03

transform tinstant(x=640, z=0.80):
    xcenter x yoffset 0 zoom z*1.00 alpha 1.00 yanchor 1.0 ypos 1.03

transform focus(x=640, z=0.80):
    yanchor 1.0 ypos 1.03 subpixel True
    on show:

        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.05 alpha 1.00
        yanchor 1.0 ypos 1.03
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.05
        parallel:
            easein .15 yoffset 0

transform sink(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .5 ypos 1.06

transform hop(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0

transform hopfocus(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.05 alpha 1.00 subpixel True
    easein .1 yoffset -21
    easeout .1 yoffset 0

transform dip(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 yoffset 25
    easeout .25 yoffset 0

transform panic(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    parallel:
        ease 1.2 yoffset 25
        ease 1.2 yoffset 0
        repeat
    parallel:
        easein .3 xoffset 20
        ease .6 xoffset -20
        easeout .3 xoffset 0
        repeat

transform leftin(x=640, z=0.80):
    xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x


transform thide(z=0.80):
    subpixel True
    transform_anchor True
    on hide:

        easein .25 zoom z*0.95 alpha 0.00 yoffset -20
transform lhide:
    subpixel True
    on hide:
        easeout .25 xcenter -300

transform t51:
    tcommon(176)
transform t52:
    tcommon(408)
transform t53:
    tcommon(640)
transform t54:
    tcommon(872)
transform t55:
    tcommon(1104)
transform t41:
    tcommon(200)
transform t42:
    tcommon(493)
transform t43:
    tcommon(786)
transform t44:
    tcommon(1080)
transform t31:
    tcommon(240)
transform t32:
    tcommon(640)
transform t33:
    tcommon(1040)
transform t21:
    tcommon(400)
transform t22:
    tcommon(880)
transform t11:
    tcommon(640)

transform i51:
    tinstant(176)
transform i52:
    tinstant(408)
transform i53:
    tinstant(640)
transform i54:
    tinstant(872)
transform i55:
    tinstant(1104)
transform i41:
    tinstant(200)
transform i42:
    tinstant(493)
transform i43:
    tinstant(786)
transform i44:
    tinstant(1080)
transform i31:
    tinstant(240)
transform i32:
    tinstant(640)
transform i33:
    tinstant(1040)
transform i21:
    tinstant(400)
transform i22:
    tinstant(880)
transform i11:
    tinstant(640)

transform f51:
    focus(176)
transform f52:
    focus(408)
transform f53:
    focus(640)
transform f54:
    focus(872)
transform f55:
    focus(1104)
transform f41:
    focus(200)
transform f42:
    focus(493)
transform f43:
    focus(786)
transform f44:
    focus(1080)
transform f31:
    focus(240)
transform f32:
    focus(640)
transform f33:
    focus(1040)
transform f21:
    focus(400)
transform f22:
    focus(880)
transform f11:
    focus(640)

transform s51:
    sink(176)
transform s52:
    sink(408)
transform s53:
    sink(640)
transform s54:
    sink(872)
transform s55:
    sink(1104)
transform s41:
    sink(200)
transform s42:
    sink(493)
transform s43:
    sink(786)
transform s44:
    sink(1080)
transform s31:
    sink(240)
transform s32:
    sink(640)
transform s33:
    sink(1040)
transform s21:
    sink(400)
transform s22:
    sink(880)
transform s11:
    sink(640)

transform h51:
    hop(176)
transform h52:
    hop(408)
transform h53:
    hop(640)
transform h54:
    hop(872)
transform h55:
    hop(1104)
transform h41:
    hop(200)
transform h42:
    hop(493)
transform h43:
    hop(786)
transform h44:
    hop(1080)
transform h31:
    hop(240)
transform h32:
    hop(640)
transform h33:
    hop(1040)
transform h21:
    hop(400)
transform h22:
    hop(880)
transform h11:
    hop(640)

transform hf51:
    hopfocus(176)
transform hf52:
    hopfocus(408)
transform hf53:
    hopfocus(640)
transform hf54:
    hopfocus(872)
transform hf55:
    hopfocus(1104)
transform hf41:
    hopfocus(200)
transform hf42:
    hopfocus(493)
transform hf43:
    hopfocus(786)
transform hf44:
    hopfocus(1080)
transform hf31:
    hopfocus(240)
transform hf32:
    hopfocus(640)
transform hf33:
    hopfocus(1040)
transform hf21:
    hopfocus(400)
transform hf22:
    hopfocus(880)
transform hf11:
    hopfocus(640)

transform d51:
    dip(176)
transform d52:
    dip(408)
transform d53:
    dip(640)
transform d54:
    dip(872)
transform d55:
    dip(1104)
transform d41:
    dip(200)
transform d42:
    dip(493)
transform d43:
    dip(786)
transform d44:
    dip(1080)
transform d31:
    dip(240)
transform d32:
    dip(640)
transform d33:
    dip(1040)
transform d21:
    dip(400)
transform d22:
    dip(880)
transform d11:
    dip(640)

transform l51:
    leftin(176)
transform l52:
    leftin(408)
transform l53:
    leftin(640)
transform l54:
    leftin(872)
transform l55:
    leftin(1104)
transform l41:
    leftin(200)
transform l42:
    leftin(493)
transform l43:
    leftin(786)
transform l44:
    leftin(1080)
transform l31:
    leftin(240)
transform l32:
    leftin(640)
transform l33:
    leftin(1040)
transform l21:
    leftin(400)
transform l22:
    leftin(880)
transform l11:
    leftin(640)


transform face(z=0.80, y=500):
    subpixel True
    xcenter 640
    yanchor 1.0 ypos 1.03
    yoffset y
    zoom z*2.00

transform cgfade:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0

transform n_cg2_wiggle:
    subpixel True
    xoffset 0
    easein 0.15 xoffset 20
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -15
    easeout 0.15 xoffset 0
    easein 0.15 xoffset 10
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -5
    ease 0.15 xoffset 0

transform n_cg2_wiggle_loop:
    n_cg2_wiggle
    1.0
    repeat

transform n_cg2_zoom:
    subpixel True
    truecenter
    xoffset 0
    easeout 0.20 zoom 2.5 xoffset 200


define dissolve = Dissolve(0.25)

define dissolve_cg = Dissolve(0.75)
define dissolve_scene = Dissolve(1.0)

define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

define dissolve_scene_half = MultipleTransition([
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

define close_eyes = MultipleTransition([
    False, Dissolve(0.5),
    Solid("#000"), Pause(0.25),
    True])

define open_eyes = MultipleTransition([
    False, Dissolve(0.5),
    True])

define trueblack = MultipleTransition([
    Solid("#000"), Pause(0.25),
    Solid("#000")
    ])


define wipeleft = ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64)


define wipeleft_scene = MultipleTransition([
    False, ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    True])


# Transitions from Kia - scaled to DDLC resolution
define w1 = ImageDissolve(im.Scale("mod_assets/images/menu/1.jpg", 1280, 720), 4.0, 8)
define w2 = ImageDissolve(im.Scale("mod_assets/images/menu/2.png", 1280, 720), 4.0, 8)
define w3 = ImageDissolve(im.Scale("mod_assets/images/menu/3.jpg", 1280, 720), 4.0, 8)
define w4 = ImageDissolve(im.Scale("mod_assets/images/menu/4.jpg", 1280, 720), 4.0, 8)
define w5 = ImageDissolve(im.Scale("mod_assets/images/menu/5.jpg", 1280, 720), 4.0, 8)
define w6 = ImageDissolve(im.Scale("mod_assets/images/menu/6.jpg", 1280, 720), 4.0, 8)
define w7 = ImageDissolve(im.Scale("mod_assets/images/menu/7.png", 1280, 720), 4.0, 8)
define w8 = ImageDissolve(im.Scale("mod_assets/images/menu/8.jpg", 1280, 720), 4.0, 8)
define w9 = ImageDissolve(im.Scale("mod_assets/images/menu/9.jpg", 1280, 720), 4.0, 8)
define w10 = ImageDissolve(im.Scale("mod_assets/images/menu/10.jpg", 1280, 720), 4.0, 8)
define w11 = ImageDissolve(im.Scale("mod_assets/images/menu/11.jpg", 1280, 720), 4.0, 8)
define w12 = ImageDissolve(im.Scale("mod_assets/images/menu/12.jpg", 1280, 720), 4.0, 8)
define w13 = ImageDissolve(im.Scale("mod_assets/images/menu/13.jpg", 1280, 720), 4.0, 8)
define w14 = ImageDissolve(im.Scale("mod_assets/images/menu/14.png", 1280, 720), 4.0, 8)
define w15 = ImageDissolve(im.Scale("mod_assets/images/menu/15.png", 1280, 720), 4.0, 8)
define w16 = ImageDissolve(im.Scale("mod_assets/images/menu/16.png", 1280, 720), 4.0, 8)
define w17 = ImageDissolve(im.Scale("mod_assets/images/menu/17.png", 1280, 720), 4.0, 8)
define w18 = ImageDissolve(im.Scale("mod_assets/images/menu/18.png", 1280, 720), 4.0, 8)
define w19 = ImageDissolve(im.Scale("mod_assets/images/menu/19.jpg", 1280, 720), 4.0, 8)
define w20 = ImageDissolve(im.Scale("mod_assets/images/menu/20.jpg", 1280, 720), 4.0, 8)
define w21 = ImageDissolve(im.Scale("mod_assets/images/menu/21.jpg", 1280, 720), 4.0, 8)
define w22 = ImageDissolve(im.Scale("mod_assets/images/menu/22.png", 1280, 720), 4.0, 8)
define w23 = ImageDissolve(im.Scale("mod_assets/images/menu/23.png", 1280, 720), 4.0, 8)
define w24 = ImageDissolve(im.Scale("mod_assets/images/menu/24.png", 1280, 720), 4.0, 8)
define w25 = ImageDissolve(im.Scale("mod_assets/images/menu/25.png", 1280, 720), 4.0, 8)
define w26 = ImageDissolve(im.Scale("mod_assets/images/menu/26.png", 1280, 720), 4.0, 8)
define w27 = ImageDissolve(im.Scale("mod_assets/images/menu/27.png", 1280, 720), 4.0, 8)
define w28 = ImageDissolve(im.Scale("mod_assets/images/menu/28.png", 1280, 720), 4.0, 8)
define circlewipe = ImageDissolve(im.Scale("mod_assets/images/menu/circlewipe-cw.jpg", 1280, 720), 4.0, 8)
define ccirclewipe = ImageDissolve(im.Scale("mod_assets/images/menu/circlewipe-ccw.jpg", 1280, 720), 4.0, 8)
define bites = ImageDissolve(im.Scale("mod_assets/images/menu/bites.jpg", 1280, 720), 4.0, 8)
define bowtie = ImageDissolve(im.Scale("mod_assets/images/menu/bowtie.png", 1280, 720), 4.0, 8)
define cmet = ImageDissolve(im.Scale("mod_assets/images/menu/cmet.jpg", 1280, 720), 4.0, 8)
define cwside = ImageDissolve(im.Scale("mod_assets/images/menu/cw-side.jpg", 1280, 720), 4.0, 8)
define cwtop = ImageDissolve(im.Scale("mod_assets/images/menu/cw-top.jpg", 1280, 720), 4.0, 8)
define dots = ImageDissolve(im.Scale("mod_assets/images/menu/dots.png", 1280, 720), 4.0, 8)
define edges = ImageDissolve(im.Scale("mod_assets/images/menu/edges.png", 1280, 720), 4.0, 8)
define flips = ImageDissolve(im.Scale("mod_assets/images/menu/flips.png", 1280, 720), 4.0, 8)
define fur = ImageDissolve(im.Scale("mod_assets/images/menu/fur.jpg", 1280, 720), 4.0, 8)
define goslow = ImageDissolve(im.Scale("mod_assets/images/menu/goslow.png", 1280, 720), 4.0, 8)
define letter = ImageDissolve(im.Scale("mod_assets/images/menu/letter.png", 1280, 720), 4.0, 8)
define maze = ImageDissolve(im.Scale("mod_assets/images/menu/maze.png", 1280, 720), 4.0, 8)
define radio = ImageDissolve(im.Scale("mod_assets/images/menu/radio.jpg", 1280, 720), 4.0, 8)
define snake = ImageDissolve(im.Scale("mod_assets/images/menu/snake.png", 1280, 720), 4.0, 8)
define snake2 = ImageDissolve(im.Scale("mod_assets/images/menu/snake2.png", 1280, 720), 4.0, 8)
define snakes = ImageDissolve(im.Scale("mod_assets/images/menu/snakes.png", 1280, 720), 4.0, 8)
define sunshine = ImageDissolve(im.Scale("mod_assets/images/menu/sunshine.jpg", 1280, 720), 4.0, 8)
define glasswool = ImageDissolve(im.Scale("mod_assets/images/menu/glasswool.jpg", 1280, 720), 4.0, 8)
define wet = ImageDissolve(im.Scale("mod_assets/images/menu/wet.jpg", 1280, 720), 4.0, 8)

define tpause = Pause(0.25)

image noise:
    truecenter
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    xzoom -1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    yzoom -1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    xzoom 1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    yzoom 1
    repeat

transform noise_alpha:
    alpha 0.25

transform noisefade(t=0):
    alpha 0.0
    t
    linear 5.0 alpha 0.40

image vignette:
    truecenter
    "images/bg/vignette.png"

transform vignettefade(t=0):
    alpha 0.0
    t
    linear 25.0 alpha 1.00

transform vignetteflicker(t=0):
    alpha 0.0
    t + 2.030
    parallel:
        alpha 1.00
        linear 0.2 alpha 0.8
        0.1
        alpha 0.7
        linear 0.1 alpha 1.00
        alpha 0.0
        1.19
        repeat
    parallel:
        easeout 20 zoom 3.0

transform layerflicker(t=0):
    truecenter
    t + 2.030
    parallel:
        zoom 1.05
        linear 0.2 zoom 1.04
        0.1
        zoom 1.035
        linear 0.1 zoom 1.05
        zoom 1.0
        1.19
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.6
        easeout_bounce 0.3 xalign 0.4
        repeat

transform rewind:
    truecenter
    zoom 1.20
    parallel:
        easeout_bounce 0.2 xalign 0.55
        easeout_bounce 0.2 xalign 0.45
        repeat
    parallel:
        easeout_bounce 0.33 yalign 0.55
        easeout_bounce 0.33 yalign 0.45
        repeat

transform heartbeat:
    heartbeat2(1)

transform heartbeat2(m):
    truecenter
    parallel:
        0.144
        zoom 1.00 + 0.07 * m
        easein 0.250 zoom 1.00 + 0.04 * m
        easeout 0.269 zoom 1.00 + 0.07 * m
        zoom 1.00
        1.479
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.5 + 0.02 * m
        easeout_bounce 0.3 xalign 0.5 - 0.02 * m
        repeat

transform yuripupils_move:
    function yuripupils_function

init python:
    def yuripupils_function(trans, st, at):
        trans.xoffset = -1 + random.random() * 9 - 4
        trans.yoffset = 3 + random.random() * 6 - 3
        return random.random() * 1.2 + 0.3

transform malpha(a=1.00):
    i11
    alpha a
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
