define persistent.demo = False
define persistent.steam = ("steamapps" in config.basedir.lower())
define config.developer = False

python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    renpy.music.register_channel("music_play", mixer="music", tight=True)
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def delete_character(name):
        import os
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass
    def restore_all_characters():
        try: renpy.file("../characters/monika.chr")
        except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
        try: renpy.file("../characters/natsuki.chr")
        except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
        try: renpy.file("../characters/yuri.chr")
        except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
        try: renpy.file("../characters/sayori.chr")
        except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())
    def restore_relevant_characters():
        restore_all_characters()
        if persistent.playthrough == 1 or persistent.playthrough == 2:
            delete_character("sayori")
        elif persistent.playthrough == 3:
            delete_character("sayori")
            delete_character("natsuki")
            delete_character("yuri")
        elif persistent.playthrough == 4:
            delete_character("monika")
    def put_small_characters():
        delete_character("natsuki")
        delete_character("yuri")
        try: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsukismall.chr").read())
        except: pass
        try: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yurismall.chr").read())
        except: pass
    def restore_normal_characters():
        delete_character("natsuki")
        delete_character("yuri")
        try: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
        except: pass
        try: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
        except: pass
    def insert_dadsuki_character():
        delete_character("yasuhiro")
        try: open(config.basedir + "/characters/yasuhiro.chr", "wb").write(renpy.file("yasuhiro.chr").read())
        except: pass
    def insert_momsuki_character_normal():
        delete_character("haruki")
        try: open(config.basedir + "/characters/haruki.chr", "wb").write(renpy.file("harukinormal.chr").read())
        except: pass
    def insert_momsuki_character_broken():
        delete_character("haruki")
        try: open(config.basedir + "/characters/haruki.chr", "wb").write(renpy.file("harukibroken.chr").read())
        except: pass
    def pause(time=None):
        global _windows_hidden
        if not time:
            _windows_hidden = True
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            _windows_hidden = False
            return
        if time <= 0: return
        _windows_hidden = True
        renpy.pause(time)
        _windows_hidden = False





define audio.t1 = "<loop 22.073>bgm/1.ogg"
# Piano Only Version of DDLC Intro for True Route
define audio.t1m = "<loop 22.073>mod_assets/bgm/1monika.ogg"
# Mod Tracks - 17: Too Late
define audio.t1c = "<loop 0.535>mod_assets/bgm/1cast.ogg"
define audio.t2 = "<loop 4.499>bgm/2.ogg"
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define autio.t2r = "<to 38.23 loop 0>mod_assets/bgm/2r.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg"
define audio.t3f = "<loop 4.618>mod_assets/bgm/3f.ogg"
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define autio.t3r = "<to 48.0 loop 0>mod_assets/bgm/3r.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg"
define audio.t4g = "<loop 1.000>bgm/4g.ogg"
define audio.t5 = "<loop 4.444>bgm/5.ogg"
define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg"
define audio.t6b = "<loop 10.893>bgm/6.ogg"
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg"
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg"
define audio.t8b = "<loop 9.938>bgm/8.ogg"
define audio.t9 = "<loop 3.172>bgm/9.ogg"
define audio.t9g = "<loop 1.532>bgm/9g.ogg"
define audio.t10 = "<loop 5.861>bgm/10.ogg"
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"
# Mod Tracks - 11: Play Time!
define audio.t11 = "<loop 5.000>mod_assets/bgm/11.ogg"
# Mod Tracks - 12: A Date With You
define audio.t12y = "<loop 1.300>mod_assets/bgm/12_yuri.ogg"
define audio.t12n = "<loop 1.300>mod_assets/bgm/12_natsuki.ogg"
define audio.t12s = "<loop 1.300>mod_assets/bgm/12_sayori.ogg"
define audio.t12m = "<loop 1.300>mod_assets/bgm/12_monika.ogg"
# Mod Tracks - 13: Choices of Hope and Suffering
define audio.t13 = "<loop 1.700>mod_assets/bgm/13.ogg"
# Mod Tracks - 15: Hear Me, My Love
define audio.t15 = "mod_assets/bgm/15.ogg"
# Mod Tracks - 16: I'm Coming For You
define audio.t16 = "mod_assets/bgm/16.ogg"

define audio.m1 = "<loop 0>bgm/m1.ogg"
define audio.mend = "<loop 6.424>bgm/monika-end.ogg"
define audio.mendglitch = "<loop 6.424>mod_assets/bgm/monika-end-pitch.ogg"
# Mod Tracks - 14: Markovika
define audio.mkov = "<loop 1.500>mod_assets/bgm/monika-markov.ogg"
define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"


image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"
image bg residential_day = "bg/residential.png"
image bg class_day = "bg/class.png"
image bg corridor = "bg/corridor.png"
image bg club_day = "bg/club.png"
image bg club_day2:
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"
image bg closet = "bg/closet.png"
image bg bedroom = "bg/bedroom.png"
image bg sayori_bedroom = "bg/sayori_bedroom.png"
image bg house = "bg/house.png"
image bg kitchen = "bg/kitchen.png"

image bg notebook = "bg/notebook.png"
image bg notebook-glitch = "bg/notebook-glitch.png"

image bg glitch = LiveTile("bg/glitch.jpg")

image markovred = "#f21237"
image monikared = "#e03638"
image bg new_house = "bg/house.jpg"
image bg gym = "mod_assets/images/bg/gym.png"
image bg rooftop = "mod_assets/images/bg/rooftop.png"
image bg library = "mod_assets/images/bg/library.png"
image bg library_shelf = "mod_assets/images/bg/library_shelf.png"
image bg y_house = "mod_assets/images/bg/y_house.png"
image bg y_bedroom = "mod_assets/images/bg/y_bedroom.png"
image bg y_bedroom_kill = ConditionSwitch(
    "persistent.yuri_killing >= 400", "mod_assets/images/bg/y_bedroom.png",
    "persistent.yuri_killing >= 300","mod_assets/images/bg/y_bedroom_d.png",
    "persistent.yuri_killing >= 200","mod_assets/images/bg/y_bedroom_c.png",
    "persistent.yuri_killing >= 100","mod_assets/images/bg/y_bedroom_b.png",
    "True", "mod_assets/images/bg/y_bedroom.png",
    )
image bg y_corridor = "mod_assets/images/bg/y_corridor.png"
image bg hospital = "mod_assets/images/bg/hospital.png"
image bg hospital_room = "mod_assets/images/bg/hospital_room.png"
image bg cafe = "mod_assets/images/bg/cafe.png"
image bg n_house_day = "mod_assets/images/bg/n_house_day.png"
image bg n_house_sunset = "mod_assets/images/bg/n_house_sunset.png"
image bg n_bedroom = "mod_assets/images/bg/n_bedroom.png"
image bg n_oldlivingroom = "mod_assets/images/bg/n_oldlivingroom.png"
image bg n_livingroom = "mod_assets/images/bg/n_livingroom.png"
image bg n_hitroom = "mod_assets/images/bg/n_hitroom.png"
image bg n_dadroom = "mod_assets/images/bg/n_dadroom.png"
image bg n_corridor = "mod_assets/images/bg/n_corridor.png"
image bg shop_day = "mod_assets/images/bg/shop_day.png"
image bg shop_sunset = "mod_assets/images/bg/shop_sunset.png"
image bg mall_day = "mod_assets/images/bg/mall_day.png"
image bg mall_sunset = "mod_assets/images/bg/mall_sunset.png"
image bg city_day = "mod_assets/images/bg/city_day.png"
image bg city_sunset = "mod_assets/images/bg/city_sunset.png"
image bg portraitshop_day = "mod_assets/images/bg/portraitshop_day.png"
image bg portraitshop_sunset = "mod_assets/images/bg/portraitshop_sunset.png"
image bg marina = "mod_assets/images/bg/marina.png"
image bg train = "mod_assets/images/bg/train.png"
image bg school_front = "mod_assets/images/bg/school_front.png"
image bg school_hallway = "mod_assets/images/bg/school_hallway.png"
image bg school_insideroof = "mod_assets/images/bg/school_insideroof.png"
image bg school_stairway = "mod_assets/images/bg/school_stairway.png"
image bg m_livingroom = "mod_assets/images/bg/m_livingroom.png"
image bg m_bedroom = "mod_assets/images/bg/m_bedroom.png"

image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0



image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0




image sayori 1 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 1c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 1d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 1e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 1f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 1g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 1h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 1i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 1j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 1k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 1l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 1m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 1n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 1o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 1p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 1q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 1r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 1s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 1t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 1u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 1v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 1w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 1x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 1y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 2c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 2d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 2e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 2f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 2g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 2h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 2i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 2j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 2k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 2l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 2m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 2n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 2o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 2p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 2q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 2r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 2s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 2t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 2u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 2v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 2w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 2x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 2y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 3c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 3d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 3e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 3f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 3g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 3h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 3i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 3j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 3k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 3l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 3m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 3n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 3o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 3p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 3q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 3r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 3s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 3t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 3u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 3v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 3w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 3x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 3y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 4 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 4c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 4d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 4e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 4f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 4g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 4h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 4i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 4j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 4k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 4l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 4m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 4n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 4o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 4p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 4q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 4r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 4s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 4t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 4u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 4v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 4w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 4x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 4y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 5 = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5a = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5b = im.Composite((960, 960), (0, 0), "sayori/3b.png")
image sayori 5c = im.Composite((960, 960), (0, 0), "sayori/3c.png")
image sayori 5d = im.Composite((960, 960), (0, 0), "sayori/3d.png")

image sayori 1gk = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/images/sayori/gk.png")

# Normal Casual Sayori
image sayori 1casuala = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 1casualb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 1casualc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 1casuald = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 1casuale = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 1casualf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 1casualg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 1casualh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 1casuali = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 1casualj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 1casualk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 1casuall = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 1casualm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 1casualn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 1casualo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 1casualp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 1casualq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 1casualr = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 1casuals = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 1casualt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 1casualu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 1casualv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 1casualw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 1casualx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 1casualy = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 2casuala = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 2casualb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 2casualc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 2casuald = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 2casuale = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 2casualf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 2casualg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 2casualh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 2casuali = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 2casualj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 2casualk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 2casuall = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 2casualm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 2casualn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 2casualo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 2casualp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 2casualq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 2casualr = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 2casuals = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 2casualt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 2casualu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 2casualv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 2casualw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 2casualx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 2casualy = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori 3casuala = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 3casualb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 3casualc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 3casuald = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 3casuale = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 3casualf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 3casualg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 3casualh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 3casuali = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 3casualj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 3casualk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 3casuall = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 3casualm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 3casualn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 3casualo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 3casualp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 3casualq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 3casualr = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 3casuals = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 3casualt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 3casualu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 3casualv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 3casualw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 3casualx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 3casualy = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 4casuala = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 4casualb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 4casualc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 4casuald = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 4casuale = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 4casualf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 4casualg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 4casualh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 4casuali = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 4casualj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 4casualk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 4casuall = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 4casualm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 4casualn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 4casualo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 4casualp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 4casualq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 4casualr = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 4casuals = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 4casualt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 4casualu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 4casualv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 4casualw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 4casualx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 4casualy = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

# Date Clothes Sayori
image sayori 1datea = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/a.png")
image sayori 1dateb = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/b.png")
image sayori 1datec = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/c.png")
image sayori 1dated = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/d.png")
image sayori 1datee = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/e.png")
image sayori 1datef = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/f.png")
image sayori 1dateg = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/g.png")
image sayori 1dateh = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/h.png")
image sayori 1datei = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/i.png")
image sayori 1datej = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/j.png")
image sayori 1datek = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/k.png")
image sayori 1datel = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/l.png")
image sayori 1datem = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/m.png")
image sayori 1daten = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/n.png")
image sayori 1dateo = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/o.png")
image sayori 1datep = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/p.png")
image sayori 1dateq = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/q.png")
image sayori 1dater = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/r.png")
image sayori 1dates = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/s.png")
image sayori 1datet = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/t.png")
image sayori 1dateu = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/u.png")
image sayori 1datev = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/v.png")
image sayori 1datew = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/w.png")
image sayori 1datex = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/x.png")
image sayori 1datey = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/y.png")

image sayori 2datea = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/a.png")
image sayori 2dateb = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/b.png")
image sayori 2datec = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/c.png")
image sayori 2dated = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/d.png")
image sayori 2datee = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/e.png")
image sayori 2datef = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/f.png")
image sayori 2dateg = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/g.png")
image sayori 2dateh = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/h.png")
image sayori 2datei = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/i.png")
image sayori 2datej = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/j.png")
image sayori 2datek = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/k.png")
image sayori 2datel = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/l.png")
image sayori 2datem = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/m.png")
image sayori 2daten = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/n.png")
image sayori 2dateo = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/o.png")
image sayori 2datep = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/p.png")
image sayori 2dateq = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/q.png")
image sayori 2dater = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/r.png")
image sayori 2dates = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/s.png")
image sayori 2datet = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/t.png")
image sayori 2dateu = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/u.png")
image sayori 2datev = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/v.png")
image sayori 2datew = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/w.png")
image sayori 2datex = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/x.png")
image sayori 2datey = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/1cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/y.png")

image sayori 3datea = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/a.png")
image sayori 3dateb = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/b.png")
image sayori 3datec = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/c.png")
image sayori 3dated = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/d.png")
image sayori 3datee = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/e.png")
image sayori 3datef = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/f.png")
image sayori 3dateg = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/g.png")
image sayori 3dateh = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/h.png")
image sayori 3datei = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/i.png")
image sayori 3datej = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/j.png")
image sayori 3datek = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/k.png")
image sayori 3datel = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/l.png")
image sayori 3datem = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/m.png")
image sayori 3daten = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/n.png")
image sayori 3dateo = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/o.png")
image sayori 3datep = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/p.png")
image sayori 3dateq = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/q.png")
image sayori 3dater = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/r.png")
image sayori 3dates = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/s.png")
image sayori 3datet = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/t.png")
image sayori 3dateu = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/u.png")
image sayori 3datev = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/v.png")
image sayori 3datew = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/w.png")
image sayori 3datex = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/x.png")
image sayori 3datey = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/1cr.png", (0, 0), "sayori/y.png")

image sayori 4datea = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/a.png")
image sayori 4dateb = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/b.png")
image sayori 4datec = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/c.png")
image sayori 4dated = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/d.png")
image sayori 4datee = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/e.png")
image sayori 4datef = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/f.png")
image sayori 4dateg = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/g.png")
image sayori 4dateh = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/h.png")
image sayori 4datei = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/i.png")
image sayori 4datej = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/j.png")
image sayori 4datek = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/k.png")
image sayori 4datel = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/l.png")
image sayori 4datem = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/m.png")
image sayori 4daten = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/n.png")
image sayori 4dateo = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/o.png")
image sayori 4datep = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/p.png")
image sayori 4dateq = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/q.png")
image sayori 4dater = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/r.png")
image sayori 4dates = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/s.png")
image sayori 4datet = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/t.png")
image sayori 4dateu = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/u.png")
image sayori 4datev = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/v.png")
image sayori 4datew = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/w.png")
image sayori 4datex = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/x.png")
image sayori 4datey = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/2cl.png", (0, 0), "mod_assets/images/sayori/2cr.png", (0, 0), "sayori/y.png")

# Sayori Casual Sprites Definitions
image sayori 1ba = ConditionSwitch("sayori_outfit == 1", "sayori 1casuala", "True", "sayori 1datea")
image sayori 1bb = ConditionSwitch("sayori_outfit == 1", "sayori 1casualb", "True", "sayori 1dateb")
image sayori 1bc = ConditionSwitch("sayori_outfit == 1", "sayori 1casualc", "True", "sayori 1datec")
image sayori 1bd = ConditionSwitch("sayori_outfit == 1", "sayori 1casuald", "True", "sayori 1dated")
image sayori 1be = ConditionSwitch("sayori_outfit == 1", "sayori 1casuale", "True", "sayori 1datee")
image sayori 1bf = ConditionSwitch("sayori_outfit == 1", "sayori 1casualf", "True", "sayori 1datef")
image sayori 1bg = ConditionSwitch("sayori_outfit == 1", "sayori 1casualg", "True", "sayori 1dateg")
image sayori 1bh = ConditionSwitch("sayori_outfit == 1", "sayori 1casualh", "True", "sayori 1dateh")
image sayori 1bi = ConditionSwitch("sayori_outfit == 1", "sayori 1casuali", "True", "sayori 1datei")
image sayori 1bj = ConditionSwitch("sayori_outfit == 1", "sayori 1casualj", "True", "sayori 1datej")
image sayori 1bk = ConditionSwitch("sayori_outfit == 1", "sayori 1casualk", "True", "sayori 1datek")
image sayori 1bl = ConditionSwitch("sayori_outfit == 1", "sayori 1casuall", "True", "sayori 1datel")
image sayori 1bm = ConditionSwitch("sayori_outfit == 1", "sayori 1casualm", "True", "sayori 1datem")
image sayori 1bn = ConditionSwitch("sayori_outfit == 1", "sayori 1casualn", "True", "sayori 1daten")
image sayori 1bo = ConditionSwitch("sayori_outfit == 1", "sayori 1casualo", "True", "sayori 1dateo")
image sayori 1bp = ConditionSwitch("sayori_outfit == 1", "sayori 1casualp", "True", "sayori 1datep")
image sayori 1bq = ConditionSwitch("sayori_outfit == 1", "sayori 1casualq", "True", "sayori 1dateq")
image sayori 1br = ConditionSwitch("sayori_outfit == 1", "sayori 1casualr", "True", "sayori 1dater")
image sayori 1bs = ConditionSwitch("sayori_outfit == 1", "sayori 1casuals", "True", "sayori 1dates")
image sayori 1bt = ConditionSwitch("sayori_outfit == 1", "sayori 1casualt", "True", "sayori 1datet")
image sayori 1bu = ConditionSwitch("sayori_outfit == 1", "sayori 1casualu", "True", "sayori 1dateu")
image sayori 1bv = ConditionSwitch("sayori_outfit == 1", "sayori 1casualv", "True", "sayori 1datev")
image sayori 1bw = ConditionSwitch("sayori_outfit == 1", "sayori 1casualw", "True", "sayori 1datew")
image sayori 1bx = ConditionSwitch("sayori_outfit == 1", "sayori 1casualx", "True", "sayori 1datex")
image sayori 1by = ConditionSwitch("sayori_outfit == 1", "sayori 1casualy", "True", "sayori 1datey")

image sayori 2ba = ConditionSwitch("sayori_outfit == 1", "sayori 2casuala", "True", "sayori 2datea")
image sayori 2bb = ConditionSwitch("sayori_outfit == 1", "sayori 2casualb", "True", "sayori 2dateb")
image sayori 2bc = ConditionSwitch("sayori_outfit == 1", "sayori 2casualc", "True", "sayori 2datec")
image sayori 2bd = ConditionSwitch("sayori_outfit == 1", "sayori 2casuald", "True", "sayori 2dated")
image sayori 2be = ConditionSwitch("sayori_outfit == 1", "sayori 2casuale", "True", "sayori 2datee")
image sayori 2bf = ConditionSwitch("sayori_outfit == 1", "sayori 2casualf", "True", "sayori 2datef")
image sayori 2bg = ConditionSwitch("sayori_outfit == 1", "sayori 2casualg", "True", "sayori 2dateg")
image sayori 2bh = ConditionSwitch("sayori_outfit == 1", "sayori 2casualh", "True", "sayori 2dateh")
image sayori 2bi = ConditionSwitch("sayori_outfit == 1", "sayori 2casuali", "True", "sayori 2datei")
image sayori 2bj = ConditionSwitch("sayori_outfit == 1", "sayori 2casualj", "True", "sayori 2datej")
image sayori 2bk = ConditionSwitch("sayori_outfit == 1", "sayori 2casualk", "True", "sayori 2datek")
image sayori 2bl = ConditionSwitch("sayori_outfit == 1", "sayori 2casuall", "True", "sayori 2datel")
image sayori 2bm = ConditionSwitch("sayori_outfit == 1", "sayori 2casualm", "True", "sayori 2datem")
image sayori 2bn = ConditionSwitch("sayori_outfit == 1", "sayori 2casualn", "True", "sayori 2daten")
image sayori 2bo = ConditionSwitch("sayori_outfit == 1", "sayori 2casualo", "True", "sayori 2dateo")
image sayori 2bp = ConditionSwitch("sayori_outfit == 1", "sayori 2casualp", "True", "sayori 2datep")
image sayori 2bq = ConditionSwitch("sayori_outfit == 1", "sayori 2casualq", "True", "sayori 2dateq")
image sayori 2br = ConditionSwitch("sayori_outfit == 1", "sayori 2casualr", "True", "sayori 2dater")
image sayori 2bs = ConditionSwitch("sayori_outfit == 1", "sayori 2casuals", "True", "sayori 2dates")
image sayori 2bt = ConditionSwitch("sayori_outfit == 1", "sayori 2casualt", "True", "sayori 2datet")
image sayori 2bu = ConditionSwitch("sayori_outfit == 1", "sayori 2casualu", "True", "sayori 2dateu")
image sayori 2bv = ConditionSwitch("sayori_outfit == 1", "sayori 2casualv", "True", "sayori 2datev")
image sayori 2bw = ConditionSwitch("sayori_outfit == 1", "sayori 2casualw", "True", "sayori 2datew")
image sayori 2bx = ConditionSwitch("sayori_outfit == 1", "sayori 2casualx", "True", "sayori 2datex")
image sayori 2by = ConditionSwitch("sayori_outfit == 1", "sayori 2casualy", "True", "sayori 2datey")

image sayori 3ba = ConditionSwitch("sayori_outfit == 1", "sayori 3casuala", "True", "sayori 3datea")
image sayori 3bb = ConditionSwitch("sayori_outfit == 1", "sayori 3casualb", "True", "sayori 3dateb")
image sayori 3bc = ConditionSwitch("sayori_outfit == 1", "sayori 3casualc", "True", "sayori 3datec")
image sayori 3bd = ConditionSwitch("sayori_outfit == 1", "sayori 3casuald", "True", "sayori 3dated")
image sayori 3be = ConditionSwitch("sayori_outfit == 1", "sayori 3casuale", "True", "sayori 3datee")
image sayori 3bf = ConditionSwitch("sayori_outfit == 1", "sayori 3casualf", "True", "sayori 3datef")
image sayori 3bg = ConditionSwitch("sayori_outfit == 1", "sayori 3casualg", "True", "sayori 3dateg")
image sayori 3bh = ConditionSwitch("sayori_outfit == 1", "sayori 3casualh", "True", "sayori 3dateh")
image sayori 3bi = ConditionSwitch("sayori_outfit == 1", "sayori 3casuali", "True", "sayori 3datei")
image sayori 3bj = ConditionSwitch("sayori_outfit == 1", "sayori 3casualj", "True", "sayori 3datej")
image sayori 3bk = ConditionSwitch("sayori_outfit == 1", "sayori 3casualk", "True", "sayori 3datek")
image sayori 3bl = ConditionSwitch("sayori_outfit == 1", "sayori 3casuall", "True", "sayori 3datel")
image sayori 3bm = ConditionSwitch("sayori_outfit == 1", "sayori 3casualm", "True", "sayori 3datem")
image sayori 3bn = ConditionSwitch("sayori_outfit == 1", "sayori 3casualn", "True", "sayori 3daten")
image sayori 3bo = ConditionSwitch("sayori_outfit == 1", "sayori 3casualo", "True", "sayori 3dateo")
image sayori 3bp = ConditionSwitch("sayori_outfit == 1", "sayori 3casualp", "True", "sayori 3datep")
image sayori 3bq = ConditionSwitch("sayori_outfit == 1", "sayori 3casualq", "True", "sayori 3dateq")
image sayori 3br = ConditionSwitch("sayori_outfit == 1", "sayori 3casualr", "True", "sayori 3dater")
image sayori 3bs = ConditionSwitch("sayori_outfit == 1", "sayori 3casuals", "True", "sayori 3dates")
image sayori 3bt = ConditionSwitch("sayori_outfit == 1", "sayori 3casualt", "True", "sayori 3datet")
image sayori 3bu = ConditionSwitch("sayori_outfit == 1", "sayori 3casualu", "True", "sayori 3dateu")
image sayori 3bv = ConditionSwitch("sayori_outfit == 1", "sayori 3casualv", "True", "sayori 3datev")
image sayori 3bw = ConditionSwitch("sayori_outfit == 1", "sayori 3casualw", "True", "sayori 3datew")
image sayori 3bx = ConditionSwitch("sayori_outfit == 1", "sayori 3casualx", "True", "sayori 3datex")
image sayori 3by = ConditionSwitch("sayori_outfit == 1", "sayori 3casualy", "True", "sayori 3datey")

image sayori 4ba = ConditionSwitch("sayori_outfit == 1", "sayori 4casuala", "True", "sayori 4datea")
image sayori 4bb = ConditionSwitch("sayori_outfit == 1", "sayori 4casualb", "True", "sayori 4dateb")
image sayori 4bc = ConditionSwitch("sayori_outfit == 1", "sayori 4casualc", "True", "sayori 4datec")
image sayori 4bd = ConditionSwitch("sayori_outfit == 1", "sayori 4casuald", "True", "sayori 4dated")
image sayori 4be = ConditionSwitch("sayori_outfit == 1", "sayori 4casuale", "True", "sayori 4datee")
image sayori 4bf = ConditionSwitch("sayori_outfit == 1", "sayori 4casualf", "True", "sayori 4datef")
image sayori 4bg = ConditionSwitch("sayori_outfit == 1", "sayori 4casualg", "True", "sayori 4dateg")
image sayori 4bh = ConditionSwitch("sayori_outfit == 1", "sayori 4casualh", "True", "sayori 4dateh")
image sayori 4bi = ConditionSwitch("sayori_outfit == 1", "sayori 4casuali", "True", "sayori 4datei")
image sayori 4bj = ConditionSwitch("sayori_outfit == 1", "sayori 4casualj", "True", "sayori 4datej")
image sayori 4bk = ConditionSwitch("sayori_outfit == 1", "sayori 4casualk", "True", "sayori 4datek")
image sayori 4bl = ConditionSwitch("sayori_outfit == 1", "sayori 4casuall", "True", "sayori 4datel")
image sayori 4bm = ConditionSwitch("sayori_outfit == 1", "sayori 4casualm", "True", "sayori 4datem")
image sayori 4bn = ConditionSwitch("sayori_outfit == 1", "sayori 4casualn", "True", "sayori 4daten")
image sayori 4bo = ConditionSwitch("sayori_outfit == 1", "sayori 4casualo", "True", "sayori 4dateo")
image sayori 4bp = ConditionSwitch("sayori_outfit == 1", "sayori 4casualp", "True", "sayori 4datep")
image sayori 4bq = ConditionSwitch("sayori_outfit == 1", "sayori 4casualq", "True", "sayori 4dateq")
image sayori 4br = ConditionSwitch("sayori_outfit == 1", "sayori 4casualr", "True", "sayori 4dater")
image sayori 4bs = ConditionSwitch("sayori_outfit == 1", "sayori 4casuals", "True", "sayori 4dates")
image sayori 4bt = ConditionSwitch("sayori_outfit == 1", "sayori 4casualt", "True", "sayori 4datet")
image sayori 4bu = ConditionSwitch("sayori_outfit == 1", "sayori 4casualu", "True", "sayori 4dateu")
image sayori 4bv = ConditionSwitch("sayori_outfit == 1", "sayori 4casualv", "True", "sayori 4datev")
image sayori 4bw = ConditionSwitch("sayori_outfit == 1", "sayori 4casualw", "True", "sayori 4datew")
image sayori 4bx = ConditionSwitch("sayori_outfit == 1", "sayori 4casualx", "True", "sayori 4datex")
image sayori 4by = ConditionSwitch("sayori_outfit == 1", "sayori 4casualy", "True", "sayori 4datey")

# Only exists for the date sprite
image sayori 5ba = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/3ca.png")
image sayori 5bb = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/3cb.png")
image sayori 5bc = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/3cc.png")
image sayori 5bd = im.Composite((960, 960), (0, 0), "mod_assets/images/sayori/3cd.png")

image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat

image sayori g1:
    "sayori 1gk"
    pause 0.1
    "sayori 1k"

image natsuki 11 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 1a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 21 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 2a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 2b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 2c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 2d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 2e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 2f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 2g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 2h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 2i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 2j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 2k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 2l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 2m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 2n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 2o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 2p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 2q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 2r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 2s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 2t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 2u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 2v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 31 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 3a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 3b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 3c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 3d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 3e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 3f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 3g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 3h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 3i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 3j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 3k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 3l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 3m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 3n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 3o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 3p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 3q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 3r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 3s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 3t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 3u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 3v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 41 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 4a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 4b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 4c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 4d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 4e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 4f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 4g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 4h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 4i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 4j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 4k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 4l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 4m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 4n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 4o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 4p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 4q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 4r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 4s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 4t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 4u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 4v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 12 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2t.png")
image natsuki 12a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ta.png")
image natsuki 12b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tb.png")
image natsuki 12c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tc.png")
image natsuki 12d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2td.png")
image natsuki 12e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2te.png")
image natsuki 12f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tf.png")
image natsuki 12g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tg.png")
image natsuki 12h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2th.png")
image natsuki 12i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ti.png")

image natsuki 42 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2t.png")
image natsuki 42a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ta.png")
image natsuki 42b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tb.png")
image natsuki 42c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tc.png")
image natsuki 42d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2td.png")
image natsuki 42e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2te.png")
image natsuki 42f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tf.png")
image natsuki 42g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tg.png")
image natsuki 42h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2th.png")
image natsuki 42i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ti.png")

image natsuki 51 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")
image natsuki 5a = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3.png")
image natsuki 5b = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3.png")
image natsuki 5c = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3.png")
image natsuki 5d = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3.png")
image natsuki 5e = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3.png")
image natsuki 5f = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3.png")
image natsuki 5g = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3.png")
image natsuki 5h = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3.png")
image natsuki 5i = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3.png")
image natsuki 5j = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3.png")
image natsuki 5k = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3.png")
image natsuki 5l = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3.png")
image natsuki 5m = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3.png")
image natsuki 5n = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3.png")
image natsuki 5o = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3.png")
image natsuki 5p = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3.png")
image natsuki 5q = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3.png")
image natsuki 5r = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3.png")
image natsuki 5s = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3.png")
image natsuki 5t = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3.png")
image natsuki 5u = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3.png")
image natsuki 5v = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3.png")
image natsuki 5w = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3.png")
image natsuki 5x = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3.png")
image natsuki 5y = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3.png")
image natsuki 5z = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3.png")



image natsuki 1ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 1bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 1bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 1bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 1be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 1bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 1bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 1bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 1bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 1bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 1bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 1bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 1bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 1bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 1bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 1bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 1bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 1br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 1bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 1bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 1bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 1bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 1bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 1bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 1by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 1bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 2ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 2bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 2bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 2bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 2be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 2bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 2bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 2bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 2bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 2bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 2bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 2bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 2bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 2bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 2bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 2bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 2bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 2br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 2bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 2bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 2bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 2bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 2bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 2bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 2by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 2bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 3ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 3bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 3bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 3bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 3be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 3bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 3bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 3bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 3bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 3bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 3bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 3bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 3bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 3bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 3bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 3bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 3bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 3br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 3bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 3bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 3bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 3bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 3bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 3bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 3by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 3bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 4ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 4bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 4bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 4bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 4be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 4bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 4bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 4bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 4bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 4bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 4bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 4bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 4bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 4bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 4bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 4bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 4bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 4br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 4bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 4bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 4bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 4bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 4bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 4bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 4by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 4bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 12ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bta.png")
image natsuki 12bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btb.png")
image natsuki 12bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btc.png")
image natsuki 12bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btd.png")
image natsuki 12be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bte.png")
image natsuki 12bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btf.png")
image natsuki 12bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btg.png")
image natsuki 12bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bth.png")
image natsuki 12bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bti.png")

image natsuki 42ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bta.png")
image natsuki 42bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btb.png")
image natsuki 42bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btc.png")
image natsuki 42bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btd.png")
image natsuki 42be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bte.png")
image natsuki 42bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btf.png")
image natsuki 42bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btg.png")
image natsuki 42bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bth.png")
image natsuki 42bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bti.png")

image natsuki 5ba = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3b.png")
image natsuki 5bb = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3b.png")
image natsuki 5bc = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3b.png")
image natsuki 5bd = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3b.png")
image natsuki 5be = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3b.png")
image natsuki 5bf = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3b.png")
image natsuki 5bg = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3b.png")
image natsuki 5bh = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3b.png")
image natsuki 5bi = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3b.png")
image natsuki 5bj = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3b.png")
image natsuki 5bk = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3b.png")
image natsuki 5bl = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3b.png")
image natsuki 5bm = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3b.png")
image natsuki 5bn = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3b.png")
image natsuki 5bo = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3b.png")
image natsuki 5bp = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3b.png")
image natsuki 5bq = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3b.png")
image natsuki 5br = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3b.png")
image natsuki 5bs = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3b.png")
image natsuki 5bt = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3b.png")
image natsuki 5bu = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3b.png")
image natsuki 5bv = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3b.png")
image natsuki 5bw = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3b.png")
image natsuki 5bx = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3b.png")
image natsuki 5by = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3b.png")
image natsuki 5bz = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3b.png")


image natsuki 1 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 3 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 4 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 5 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")

image natsuki mouth = LiveComposite((960, 960), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.png"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.png")
image natsuki ghost3 = Image("natsuki/ghost3.png")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png")
image natsuki vomit = "natsuki/vomit.png"

image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"


image yuri 1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 4 = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")

image yuri 1a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 1b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/b.png")
image yuri 1c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/c.png")
image yuri 1d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/d.png")
image yuri 1e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/e.png")
image yuri 1f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/f.png")
image yuri 1g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/g.png")
image yuri 1h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/h.png")
image yuri 1i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/i.png")
image yuri 1j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/j.png")
image yuri 1k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/k.png")
image yuri 1l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/l.png")
image yuri 1m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/m.png")
image yuri 1n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/n.png")
image yuri 1o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/o.png")
image yuri 1p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/p.png")
image yuri 1q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/q.png")
image yuri 1r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/r.png")
image yuri 1s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/s.png")
image yuri 1t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/t.png")
image yuri 1u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/u.png")
image yuri 1v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/v.png")
image yuri 1w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/w.png")

image yuri 1y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y1.png")
image yuri 1y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y2.png")
image yuri 1y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y3.png")
image yuri 1y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y4.png")
image yuri 1y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y5.png")
image yuri 1y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y6.png")
image yuri 1y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y7.png")

image yuri 2a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 2b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 2c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 2d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 2e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 2f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 2g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 2h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 2i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 2j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 2k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 2l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 2m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 2n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 2o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 2p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 2q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 2r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 2s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 2t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 2u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 2v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 2w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 2y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 2y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 2y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 2y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 2y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 2y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 2y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 3a = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3b = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 3c = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 3d = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 3e = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 3f = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 3g = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 3h = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 3i = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 3j = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 3k = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 3l = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 3m = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 3n = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 3o = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 3p = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 3q = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 3r = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 3s = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 3t = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 3u = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 3v = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 3w = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 3y1 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 3y2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 3y3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 3y4 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 3y5 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 3y6 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 3y7 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 4a = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")
image yuri 4b = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/b2.png")
image yuri 4c = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/c2.png")
image yuri 4d = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/d2.png")
image yuri 4e = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/e2.png")

image yuri 1ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")

image yuri 1by1 = im.Composite((960, 960), (0, 0), "yuri/y1.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1by2 = im.Composite((960, 960), (0, 0), "yuri/y2.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1by3 = im.Composite((960, 960), (0, 0), "yuri/y3.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1by4 = im.Composite((960, 960), (0, 0), "yuri/y4.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1by5 = im.Composite((960, 960), (0, 0), "yuri/y5.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1by6 = im.Composite((960, 960), (0, 0), "yuri/y6.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1by7 = im.Composite((960, 960), (0, 0), "yuri/y7.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")

image yuri 2ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")

image yuri 2by1 = im.Composite((960, 960), (0, 0), "yuri/y1.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2by2 = im.Composite((960, 960), (0, 0), "yuri/y2.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2by3 = im.Composite((960, 960), (0, 0), "yuri/y3.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2by4 = im.Composite((960, 960), (0, 0), "yuri/y4.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2by5 = im.Composite((960, 960), (0, 0), "yuri/y5.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2by6 = im.Composite((960, 960), (0, 0), "yuri/y6.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2by7 = im.Composite((960, 960), (0, 0), "yuri/y7.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")

image yuri 3ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")

image yuri 3by1 = im.Composite((960, 960), (0, 0), "yuri/y1.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3by2 = im.Composite((960, 960), (0, 0), "yuri/y2.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3by3 = im.Composite((960, 960), (0, 0), "yuri/y3.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3by4 = im.Composite((960, 960), (0, 0), "yuri/y4.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3by5 = im.Composite((960, 960), (0, 0), "yuri/y5.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3by6 = im.Composite((960, 960), (0, 0), "yuri/y6.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3by7 = im.Composite((960, 960), (0, 0), "yuri/y7.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")

image yuri 4ba = im.Composite((960, 960), (0, 0), "yuri/a2.png", (0, 0), "yuri/3b.png")
image yuri 4bb = im.Composite((960, 960), (0, 0), "yuri/b2.png", (0, 0), "yuri/3b.png")
image yuri 4bc = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "yuri/3b.png")
image yuri 4bd = im.Composite((960, 960), (0, 0), "yuri/d2.png", (0, 0), "yuri/3b.png")
image yuri 4be = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "yuri/3b.png")

image yuri 1bfs = im.Composite((960, 960), (0, 0), "mod_assets/images/yuri/fs.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1brs = im.Composite((960, 960), (0, 0), "mod_assets/images/yuri/rs.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bts = im.Composite((960, 960), (0, 0), "mod_assets/images/yuri/ts.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bvs = im.Composite((960, 960), (0, 0), "mod_assets/images/yuri/vs.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")

# Patched Up Yuri
image yuri 2pa = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/a.png")
image yuri 2pb = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/b.png")
image yuri 2pc = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/c.png")
image yuri 2pd = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/d.png")
image yuri 2pe = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/e.png")
image yuri 2pf = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/f.png")
image yuri 2pg = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/g.png")
image yuri 2ph = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/h.png")
image yuri 2pi = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/i.png")
image yuri 2pj = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/j.png")
image yuri 2pk = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/k.png")
image yuri 2pl = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/l.png")
image yuri 2pm = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/m.png")
image yuri 2pn = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/n.png")
image yuri 2po = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/o.png")
image yuri 2pp = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/p.png")
image yuri 2pq = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/q.png")
image yuri 2pr = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/r.png")
image yuri 2ps = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/s.png")
image yuri 2pt = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/t.png")
image yuri 2pu = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/u.png")
image yuri 2pv = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/v.png")
image yuri 2pw = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/w.png")

image yuri 2py1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/y1.png")
image yuri 2py2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/y2.png")
image yuri 2py3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/y3.png")
image yuri 2py4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/y4.png")
image yuri 2py5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/y5.png")
image yuri 2py6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/y6.png")
image yuri 2py7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/y7.png")

image yuri 3pa = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/a.png")
image yuri 3pb = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/b.png")
image yuri 3pc = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/c.png")
image yuri 3pd = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/d.png")
image yuri 3pe = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/e.png")
image yuri 3pf = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/f.png")
image yuri 3pg = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/g.png")
image yuri 3ph = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/h.png")
image yuri 3pi = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/i.png")
image yuri 3pj = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/j.png")
image yuri 3pk = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/k.png")
image yuri 3pl = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/l.png")
image yuri 3pm = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/m.png")
image yuri 3pn = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/n.png")
image yuri 3po = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/o.png")
image yuri 3pp = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/p.png")
image yuri 3pq = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/q.png")
image yuri 3pr = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/r.png")
image yuri 3ps = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/s.png")
image yuri 3pt = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/t.png")
image yuri 3pu = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/u.png")
image yuri 3pv = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/v.png")
image yuri 3pw = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/w.png")

image yuri 3py1 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/y1.png")
image yuri 3py2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/y2.png")
image yuri 3py3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/y3.png")
image yuri 3py4 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/y4.png")
image yuri 3py5 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/y5.png")
image yuri 3py6 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/y6.png")
image yuri 3py7 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/images/yuri/2pr.png", (0, 0), "yuri/y7.png")

image yuri 4pa = im.Composite((960, 960), (0, 0), "mod_assets/images/yuri/3p.png", (0, 0), "yuri/a2.png")
image yuri 4pb = im.Composite((960, 960), (0, 0), "mod_assets/images/yuri/3p.png", (0, 0), "yuri/b2.png")
image yuri 4pc = im.Composite((960, 960), (0, 0), "mod_assets/images/yuri/3p.png", (0, 0), "yuri/c2.png")
image yuri 4pd = im.Composite((960, 960), (0, 0), "mod_assets/images/yuri/3p.png", (0, 0), "yuri/d2.png")
image yuri 4pe = im.Composite((960, 960), (0, 0), "mod_assets/images/yuri/3p.png", (0, 0), "yuri/e2.png")

image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat

image yuri stab_1 = "yuri/stab/1.png"
image yuri stab_2 = "yuri/stab/2.png"
image yuri stab_3 = "yuri/stab/3.png"
image yuri stab_4 = "yuri/stab/4.png"
image yuri stab_5 = "yuri/stab/5.png"
image yuri stab_6 = LiveComposite((960,960), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png")

image yuri stab_1n = "mod_assets/images/yuri/stab/1n.png"
image yuri stab_1o = "mod_assets/images/yuri/stab/1o.png"
image yuri stab_1p = "mod_assets/images/yuri/stab/1p.png"
image yuri stab_1w = "mod_assets/images/yuri/stab/1w.png"
image yuri stab_1y2 = "mod_assets/images/yuri/stab/1y2.png"
image yuri stab_1y3 = "mod_assets/images/yuri/stab/1y3.png"
image yuri stab_1y4 = "mod_assets/images/yuri/stab/1y4.png"
image yuri stab_1y7 = "mod_assets/images/yuri/stab/1y7.png"
image yuri stab_1ya = "mod_assets/images/yuri/stab/1ya.png"

image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15


image yuri oneeye = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/oneeye.png", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

image yuri glitch:
    "yuri/glitch1.png"
    pause 0.1
    "yuri/glitch2.png"
    pause 0.1
    "yuri/glitch3.png"
    pause 0.1
    "yuri/glitch4.png"
    pause 0.1
    "yuri/glitch5.png"
    pause 0.1
    repeat
image yuri glitch2:
    "yuri/0a.png"
    pause 0.1
    "yuri/0b.png"
    pause 0.5
    "yuri/0a.png"
    pause 0.3
    "yuri/0b.png"
    pause 0.3
    "yuri 1"
image yuri glitch_sayori:
    "mod_assets/images/yuri/0as.png"
    pause 0.1
    "mod_assets/images/yuri/0bs.png"
    pause 0.5
    "mod_assets/images/yuri/0as.png"
    pause 0.3
    "mod_assets/images/yuri/0bs.png"
    pause 0.3
    "yuri 1bts"

image yuri eyes = LiveComposite((1280, 720), (0, 0), "yuri/eyes1.png", (0, 0), "yuripupils")

image yuri eyes_base = "yuri/eyes1.png"

image yuripupils:
    "yuri/eyes2.png"
    yuripupils_move

image yuri cuts = "yuri/cuts.png"

image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"

# School Clothes Monika
image monika 1 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 3 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 4 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 5 = im.Composite((960, 960), (0, 0), "monika/3a.png")

image monika 1schoola = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 1schoolb = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 1schoolc = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 1schoold = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 1schoole = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 1schoolf = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 1schoolg = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 1schoolh = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 1schooli = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 1schoolj = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 1schoolk = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 1schooll = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 1schoolm = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 1schooln = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 1schoolo = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 1schoolp = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 1schoolq = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 1schoolr = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")
image monika 1schools = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/s.png")
image monika 1schoolt = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/t.png")
image monika 1schoolu = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/u.png")

image monika 2schoola = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 2schoolb = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 2schoolc = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 2schoold = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 2schoole = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 2schoolf = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 2schoolg = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 2schoolh = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 2schooli = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 2schoolj = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 2schoolk = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 2schooll = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 2schoolm = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 2schooln = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 2schoolo = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 2schoolp = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 2schoolq = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 2schoolr = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")
image monika 2schools = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/s.png")
image monika 2schoolt = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/t.png")
image monika 2schoolu = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/u.png")

image monika 3schoola = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 3schoolb = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 3schoolc = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 3schoold = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 3schoole = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 3schoolf = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 3schoolg = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 3schoolh = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 3schooli = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 3schoolj = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 3schoolk = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 3schooll = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 3schoolm = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 3schooln = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 3schoolo = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 3schoolp = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 3schoolq = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 3schoolr = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")
image monika 3schools = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/s.png")
image monika 3schoolt = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/t.png")
image monika 3schoolu = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/u.png")

image monika 4schoola = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 4schoolb = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 4schoolc = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 4schoold = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 4schoole = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 4schoolf = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 4schoolg = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 4schoolh = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 4schooli = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 4schoolj = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 4schoolk = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 4schooll = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 4schoolm = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 4schooln = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 4schoolo = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 4schoolp = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 4schoolq = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 4schoolr = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")
image monika 4schools = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/s.png")
image monika 4schoolt = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/t.png")
image monika 4schoolu = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/u.png")

image monika 5schoola = im.Composite((960, 960), (0, 0), "monika/3a.png")
image monika 5schoolb = im.Composite((960, 960), (0, 0), "monika/3b.png")

# Markov Monika
image monika 1schoolga = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/ga.png")
image monika 1schoolge = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/ge.png")
image monika 1schoolgf = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/gf.png")
image monika 1schoolgg = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/gg.png")
image monika 1schoolgh = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/gh.png")
image monika 1schoolgi = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/gi.png")
image monika 1schoolgy1 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/gy1.png")
image monika 1schoolgy2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/gy2.png")

image monika 2schoolga = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/ga.png")
image monika 2schoolge = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/ge.png")
image monika 2schoolgf = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/gf.png")
image monika 2schoolgg = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/gg.png")
image monika 2schoolgh = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/gh.png")
image monika 2schoolgi = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/gi.png")
image monika 2schoolgy1 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/gy1.png")
image monika 2schoolgy2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/gy2.png")

image monika 3schoolga = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/ga.png")
image monika 3schoolge = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/ge.png")
image monika 3schoolgf = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/gf.png")
image monika 3schoolgg = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/gg.png")
image monika 3schoolgh = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/gh.png")
image monika 3schoolgi = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/gi.png")
image monika 3schoolgy1 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/gy1.png")
image monika 3schoolgy2 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/gy2.png")

image monika 4schoolga = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/ga.png")
image monika 4schoolge = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/ge.png")
image monika 4schoolgf = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/gf.png")
image monika 4schoolgg = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/gg.png")
image monika 4schoolgh = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/gh.png")
image monika 4schoolgi = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/gi.png")
image monika 4schoolgy1 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/gy1.png")
image monika 4schoolgy2 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/gy2.png")

image monika 5schoolga = im.Composite((960, 960), (0, 0), "mod_assets/monika/3ga.png")
image monika 5schoolgb = im.Composite((960, 960), (0, 0), "mod_assets/monika/3gb.png")

# School Clothes Monika - Hair Down
image monika 1downschoola = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/ha.png")
image monika 1downschoolb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hb.png")
image monika 1downschoolc = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hc.png")
image monika 1downschoold = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hd.png")
image monika 1downschoole = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/he.png")
image monika 1downschoolf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hf.png")
image monika 1downschoolg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hg.png")
image monika 1downschoolh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hh.png")
image monika 1downschooli = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hi.png")
image monika 1downschoolj = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hj.png")
image monika 1downschoolk = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hk.png")
image monika 1downschooll = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hl.png")
image monika 1downschoolm = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hm.png")
image monika 1downschooln = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hn.png")
image monika 1downschoolo = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/ho.png")
image monika 1downschoolp = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hp.png")
image monika 1downschoolq = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hq.png")
image monika 1downschoolr = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hr.png")
image monika 1downschools = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hs.png")
image monika 1downschoolt = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/ht.png")
image monika 1downschoolu = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hu.png")

image monika 2downschoola = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/ha.png")
image monika 2downschoolb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hb.png")
image monika 2downschoolc = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hc.png")
image monika 2downschoold = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hd.png")
image monika 2downschoole = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/he.png")
image monika 2downschoolf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hf.png")
image monika 2downschoolg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hg.png")
image monika 2downschoolh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hh.png")
image monika 2downschooli = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hi.png")
image monika 2downschoolj = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hj.png")
image monika 2downschoolk = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hk.png")
image monika 2downschooll = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hl.png")
image monika 2downschoolm = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hm.png")
image monika 2downschooln = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hn.png")
image monika 2downschoolo = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/ho.png")
image monika 2downschoolp = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hp.png")
image monika 2downschoolq = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hq.png")
image monika 2downschoolr = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hr.png")
image monika 2downschools = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hs.png")
image monika 2downschoolt = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/ht.png")
image monika 2downschoolu = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hu.png")

image monika 3downschoola = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/ha.png")
image monika 3downschoolb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hb.png")
image monika 3downschoolc = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hc.png")
image monika 3downschoold = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hd.png")
image monika 3downschoole = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/he.png")
image monika 3downschoolf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hf.png")
image monika 3downschoolg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hg.png")
image monika 3downschoolh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hh.png")
image monika 3downschooli = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hi.png")
image monika 3downschoolj = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hj.png")
image monika 3downschoolk = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hk.png")
image monika 3downschooll = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hl.png")
image monika 3downschoolm = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hm.png")
image monika 3downschooln = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hn.png")
image monika 3downschoolo = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/ho.png")
image monika 3downschoolp = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hp.png")
image monika 3downschoolq = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hq.png")
image monika 3downschoolr = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hr.png")
image monika 3downschools = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hs.png")
image monika 3downschoolt = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/ht.png")
image monika 3downschoolu = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/1hr.png", (0, 0), "mod_assets/images/monika/hu.png")

image monika 4downschoola = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/ha.png")
image monika 4downschoolb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hb.png")
image monika 4downschoolc = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hc.png")
image monika 4downschoold = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hd.png")
image monika 4downschoole = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/he.png")
image monika 4downschoolf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hf.png")
image monika 4downschoolg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hg.png")
image monika 4downschoolh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hh.png")
image monika 4downschooli = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hi.png")
image monika 4downschoolj = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hj.png")
image monika 4downschoolk = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hk.png")
image monika 4downschooll = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hl.png")
image monika 4downschoolm = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hm.png")
image monika 4downschooln = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hn.png")
image monika 4downschoolo = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/ho.png")
image monika 4downschoolp = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hp.png")
image monika 4downschoolq = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hq.png")
image monika 4downschoolr = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hr.png")
image monika 4downschools = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hs.png")
image monika 4downschoolt = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/ht.png")
image monika 4downschoolu = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2hl.png", (0, 0), "mod_assets/images/monika/2hr.png", (0, 0), "mod_assets/images/monika/hu.png")

image monika 5downschoola = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/3ha.png")
image monika 5downschoolb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/3hb.png")

# Markov Monika - Hair Down
image monika 1downschoolga = im.Composite((960, 960), (0, 0), "monika/1hl.png", (0, 0), "monika/1hr.png", (0, 0), "mod_assets/images/monika/hga.png")
image monika 1downschoolge = im.Composite((960, 960), (0, 0), "monika/1hl.png", (0, 0), "monika/1hr.png", (0, 0), "mod_assets/images/monika/hge.png")
image monika 1downschoolgf = im.Composite((960, 960), (0, 0), "monika/1hl.png", (0, 0), "monika/1hr.png", (0, 0), "mod_assets/images/monika/hgf.png")
image monika 1downschoolgg = im.Composite((960, 960), (0, 0), "monika/1hl.png", (0, 0), "monika/1hr.png", (0, 0), "mod_assets/images/monika/hgg.png")
image monika 1downschoolgh = im.Composite((960, 960), (0, 0), "monika/1hl.png", (0, 0), "monika/1hr.png", (0, 0), "mod_assets/images/monika/hgh.png")
image monika 1downschoolgi = im.Composite((960, 960), (0, 0), "monika/1hl.png", (0, 0), "monika/1hr.png", (0, 0), "mod_assets/images/monika/hgi.png")
image monika 1downschoolgy1 = im.Composite((960, 960), (0, 0), "monika/1hl.png", (0, 0), "monika/1hr.png", (0, 0), "mod_assets/images/monika/hgy1.png")
image monika 1downschoolgy2 = im.Composite((960, 960), (0, 0), "monika/1hl.png", (0, 0), "monika/1hr.png", (0, 0), "mod_assets/images/monika/hgy2.png")

image monika 2downschoolga = im.Composite((960, 960), (0, 0), "monika/1hl.png", (0, 0), "monika/2hr.png", (0, 0), "mod_assets/images/monika/hga.png")
image monika 2downschoolge = im.Composite((960, 960), (0, 0), "monika/1hl.png", (0, 0), "monika/2hr.png", (0, 0), "mod_assets/images/monika/hge.png")
image monika 2downschoolgf = im.Composite((960, 960), (0, 0), "monika/1hl.png", (0, 0), "monika/2hr.png", (0, 0), "mod_assets/images/monika/hgf.png")
image monika 2downschoolgg = im.Composite((960, 960), (0, 0), "monika/1hl.png", (0, 0), "monika/2hr.png", (0, 0), "mod_assets/images/monika/hgg.png")
image monika 2downschoolgh = im.Composite((960, 960), (0, 0), "monika/1hl.png", (0, 0), "monika/2hr.png", (0, 0), "mod_assets/images/monika/hgh.png")
image monika 2downschoolgi = im.Composite((960, 960), (0, 0), "monika/1hl.png", (0, 0), "monika/2hr.png", (0, 0), "mod_assets/images/monika/hgi.png")
image monika 2downschoolgy1 = im.Composite((960, 960), (0, 0), "monika/1hl.png", (0, 0), "monika/2hr.png", (0, 0), "mod_assets/images/monika/hgy1.png")
image monika 2downschoolgy2 = im.Composite((960, 960), (0, 0), "monika/1hl.png", (0, 0), "monika/2hr.png", (0, 0), "mod_assets/images/monika/hgy2.png")

image monika 3downschoolga = im.Composite((960, 960), (0, 0), "monika/2hl.png", (0, 0), "monika/1hr.png", (0, 0), "mod_assets/images/monika/hga.png")
image monika 3downschoolge = im.Composite((960, 960), (0, 0), "monika/2hl.png", (0, 0), "monika/1hr.png", (0, 0), "mod_assets/images/monika/hge.png")
image monika 3downschoolgf = im.Composite((960, 960), (0, 0), "monika/2hl.png", (0, 0), "monika/1hr.png", (0, 0), "mod_assets/images/monika/hgf.png")
image monika 3downschoolgg = im.Composite((960, 960), (0, 0), "monika/2hl.png", (0, 0), "monika/1hr.png", (0, 0), "mod_assets/images/monika/hgg.png")
image monika 3downschoolgh = im.Composite((960, 960), (0, 0), "monika/2hl.png", (0, 0), "monika/1hr.png", (0, 0), "mod_assets/images/monika/hgh.png")
image monika 3downschoolgi = im.Composite((960, 960), (0, 0), "monika/2hl.png", (0, 0), "monika/1hr.png", (0, 0), "mod_assets/images/monika/hgi.png")
image monika 3downschoolgy1 = im.Composite((960, 960), (0, 0), "monika/2hl.png", (0, 0), "monika/1hr.png", (0, 0), "mod_assets/images/monika/hgy1.png")
image monika 3downschoolgy2 = im.Composite((960, 960), (0, 0), "monika/2hl.png", (0, 0), "monika/1hr.png", (0, 0), "mod_assets/images/monika/hgy2.png")

image monika 4downschoolga = im.Composite((960, 960), (0, 0), "monika/2hl.png", (0, 0), "monika/2hr.png", (0, 0), "mod_assets/images/monika/hga.png")
image monika 4downschoolge = im.Composite((960, 960), (0, 0), "monika/2hl.png", (0, 0), "monika/2hr.png", (0, 0), "mod_assets/images/monika/hge.png")
image monika 4downschoolgf = im.Composite((960, 960), (0, 0), "monika/2hl.png", (0, 0), "monika/2hr.png", (0, 0), "mod_assets/images/monika/hgf.png")
image monika 4downschoolgg = im.Composite((960, 960), (0, 0), "monika/2hl.png", (0, 0), "monika/2hr.png", (0, 0), "mod_assets/images/monika/hgg.png")
image monika 4downschoolgh = im.Composite((960, 960), (0, 0), "monika/2hl.png", (0, 0), "monika/2hr.png", (0, 0), "mod_assets/images/monika/hgh.png")
image monika 4downschoolgi = im.Composite((960, 960), (0, 0), "monika/2hl.png", (0, 0), "monika/2hr.png", (0, 0), "mod_assets/images/monika/hgi.png")
image monika 4downschoolgy1 = im.Composite((960, 960), (0, 0), "monika/2hl.png", (0, 0), "monika/2hr.png", (0, 0), "mod_assets/images/monika/hgy1.png")
image monika 4downschoolgy2 = im.Composite((960, 960), (0, 0), "monika/2hl.png", (0, 0), "monika/2hr.png", (0, 0), "mod_assets/images/monika/hgy2.png")

image monika 5downschoolga = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/3hga.png")
image monika 5downschoolgb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/3hgb.png")

# Casual Clothes Monika
image monika 1casuala = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/a.png")
image monika 1casualb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/b.png")
image monika 1casualc = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/c.png")
image monika 1casuald = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/d.png")
image monika 1casuale = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/e.png")
image monika 1casualf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/f.png")
image monika 1casualg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/g.png")
image monika 1casualh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/h.png")
image monika 1casuali = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/i.png")
image monika 1casualj = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/j.png")
image monika 1casualk = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/k.png")
image monika 1casuall = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/l.png")
image monika 1casualm = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/m.png")
image monika 1casualn = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/n.png")
image monika 1casualo = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/o.png")
image monika 1casualp = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/p.png")
image monika 1casualq = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/q.png")
image monika 1casualr = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/r.png")
image monika 1casuals = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/s.png")
image monika 1casualt = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/t.png")
image monika 1casualu = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/u.png")

image monika 2casuala = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/a.png")
image monika 2casualb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/b.png")
image monika 2casualc = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/c.png")
image monika 2casuald = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/d.png")
image monika 2casuale = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/e.png")
image monika 2casualf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/f.png")
image monika 2casualg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/g.png")
image monika 2casualh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/h.png")
image monika 2casuali = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/i.png")
image monika 2casualj = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/j.png")
image monika 2casualk = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/k.png")
image monika 2casuall = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/l.png")
image monika 2casualm = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/m.png")
image monika 2casualn = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/n.png")
image monika 2casualo = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/o.png")
image monika 2casualp = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/p.png")
image monika 2casualq = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/q.png")
image monika 2casualr = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/r.png")
image monika 2casuals = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/s.png")
image monika 2casualt = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/t.png")
image monika 2casualu = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/u.png")

image monika 3casuala = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/a.png")
image monika 3casualb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/b.png")
image monika 3casualc = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/c.png")
image monika 3casuald = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/d.png")
image monika 3casuale = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/e.png")
image monika 3casualf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/f.png")
image monika 3casualg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/g.png")
image monika 3casualh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/h.png")
image monika 3casuali = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/i.png")
image monika 3casualj = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/j.png")
image monika 3casualk = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/k.png")
image monika 3casuall = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/l.png")
image monika 3casualm = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/m.png")
image monika 3casualn = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/n.png")
image monika 3casualo = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/o.png")
image monika 3casualp = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/p.png")
image monika 3casualq = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/q.png")
image monika 3casualr = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/r.png")
image monika 3casuals = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/s.png")
image monika 3casualt = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/t.png")
image monika 3casualu = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/u.png")

image monika 4casuala = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/a.png")
image monika 4casualb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/b.png")
image monika 4casualc = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/c.png")
image monika 4casuald = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/d.png")
image monika 4casuale = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/e.png")
image monika 4casualf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/f.png")
image monika 4casualg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/g.png")
image monika 4casualh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/h.png")
image monika 4casuali = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/i.png")
image monika 4casualj = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/j.png")
image monika 4casualk = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/k.png")
image monika 4casuall = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/l.png")
image monika 4casualm = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/m.png")
image monika 4casualn = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/n.png")
image monika 4casualo = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/o.png")
image monika 4casualp = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/p.png")
image monika 4casualq = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/q.png")
image monika 4casualr = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/r.png")
image monika 4casuals = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/s.png")
image monika 4casualt = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/t.png")
image monika 4casualu = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/u.png")

image monika 5casuala = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/3ba.png")
image monika 5casualb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/3bb.png")

# Markov Monika Casual
image monika 1casualga = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/ga.png")
image monika 1casualge = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/ge.png")
image monika 1casualgf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/gf.png")
image monika 1casualgg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/gg.png")
image monika 1casualgh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/gh.png")
image monika 1casualgi = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/gi.png")
image monika 1casualgy1 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/gy1.png")
image monika 1casualgy2 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/gy2.png")

image monika 2casualga = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/ga.png")
image monika 2casualge = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/ge.png")
image monika 2casualgf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/gf.png")
image monika 2casualgg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/gg.png")
image monika 2casualgh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/gh.png")
image monika 2casualgi = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/gi.png")
image monika 2casualgy1 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/gy1.png")
image monika 2casualgy2 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/gy2.png")

image monika 3casualga = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/ga.png")
image monika 3casualge = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/ge.png")
image monika 3casualgf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/gf.png")
image monika 3casualgg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/gg.png")
image monika 3casualgh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/gh.png")
image monika 3casualgi = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/gi.png")
image monika 3casualgy1 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/gy1.png")
image monika 3casualgy2 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/gy2.png")

image monika 4casualga = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/ge.png")
image monika 4casualge = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/ge.png")
image monika 4casualgf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/gf.png")
image monika 4casualgg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/gg.png")
image monika 4casualgh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/gh.png")
image monika 4casualgi = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/gi.png")
image monika 4casualgy1 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/gy1.png")
image monika 4casualgy2 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/gy2.png")

image monika 5casualga = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/3bga.png")
image monika 5casualgb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/3bgb.png")

# Casual Clothes Monika - Hair Down
image monika 1downcasuala = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/ha.png")
image monika 1downcasualb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hb.png")
image monika 1downcasualc = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hc.png")
image monika 1downcasuald = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hd.png")
image monika 1downcasuale = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/he.png")
image monika 1downcasualf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hf.png")
image monika 1downcasualg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hg.png")
image monika 1downcasualh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hh.png")
image monika 1downcasuali = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hi.png")
image monika 1downcasualj = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hj.png")
image monika 1downcasualk = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hk.png")
image monika 1downcasuall = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hl.png")
image monika 1downcasualm = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hm.png")
image monika 1downcasualn = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hn.png")
image monika 1downcasualo = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/ho.png")
image monika 1downcasualp = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hp.png")
image monika 1downcasualq = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hq.png")
image monika 1downcasualr = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hr.png")
image monika 1downcasuals = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hs.png")
image monika 1downcasualt = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/ht.png")
image monika 1downcasualu = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hu.png")

image monika 2downcasuala = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/ha.png")
image monika 2downcasualb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hb.png")
image monika 2downcasualc = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hc.png")
image monika 2downcasuald = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hd.png")
image monika 2downcasuale = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/he.png")
image monika 2downcasualf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hf.png")
image monika 2downcasualg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hg.png")
image monika 2downcasualh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hh.png")
image monika 2downcasuali = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hi.png")
image monika 2downcasualj = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hj.png")
image monika 2downcasualk = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hk.png")
image monika 2downcasuall = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hl.png")
image monika 2downcasualm = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hm.png")
image monika 2downcasualn = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hn.png")
image monika 2downcasualo = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/ho.png")
image monika 2downcasualp = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hp.png")
image monika 2downcasualq = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hq.png")
image monika 2downcasualr = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hr.png")
image monika 2downcasuals = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hs.png")
image monika 2downcasualt = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/ht.png")
image monika 2downcasualu = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hu.png")

image monika 3downcasuala = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/ha.png")
image monika 3downcasualb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hb.png")
image monika 3downcasualc = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hc.png")
image monika 3downcasuald = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hd.png")
image monika 3downcasuale = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/he.png")
image monika 3downcasualf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hf.png")
image monika 3downcasualg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hg.png")
image monika 3downcasualh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hh.png")
image monika 3downcasuali = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hi.png")
image monika 3downcasualj = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hj.png")
image monika 3downcasualk = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hk.png")
image monika 3downcasuall = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hl.png")
image monika 3downcasualm = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hm.png")
image monika 3downcasualn = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hn.png")
image monika 3downcasualo = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/ho.png")
image monika 3downcasualp = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hp.png")
image monika 3downcasualq = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hq.png")
image monika 3downcasualr = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hr.png")
image monika 3downcasuals = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hs.png")
image monika 3downcasualt = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/ht.png")
image monika 3downcasualu = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hu.png")

image monika 4downcasuala = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/ha.png")
image monika 4downcasualb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hb.png")
image monika 4downcasualc = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hc.png")
image monika 4downcasuald = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hd.png")
image monika 4downcasuale = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/he.png")
image monika 4downcasualf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hf.png")
image monika 4downcasualg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hg.png")
image monika 4downcasualh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hh.png")
image monika 4downcasuali = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hi.png")
image monika 4downcasualj = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hj.png")
image monika 4downcasualk = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hk.png")
image monika 4downcasuall = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hl.png")
image monika 4downcasualm = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hm.png")
image monika 4downcasualn = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hn.png")
image monika 4downcasualo = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/ho.png")
image monika 4downcasualp = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hp.png")
image monika 4downcasualq = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hq.png")
image monika 4downcasualr = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hr.png")
image monika 4downcasuals = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hs.png")
image monika 4downcasualt = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/ht.png")
image monika 4downcasualu = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hu.png")

image monika 5downcasuala = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/3bha.png")
image monika 5downcasualb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/3bhb.png")

# Markov Monika Casual - Hair Down
image monika 1downcasualga = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hga.png")
image monika 1downcasualge = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hge.png")
image monika 1downcasualgf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hgf.png")
image monika 1downcasualgg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hgg.png")
image monika 1downcasualgh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hgh.png")
image monika 1downcasualgi = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hgi.png")
image monika 1downcasualgy1 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hgy1.png")
image monika 1downcasualgy2 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hgy2.png")

image monika 2downcasualga = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hga.png")
image monika 2downcasualge = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hge.png")
image monika 2downcasualgf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hgf.png")
image monika 2downcasualgg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hgg.png")
image monika 2downcasualgh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hgh.png")
image monika 2downcasualgi = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hgi.png")
image monika 2downcasualgy1 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hgy1.png")
image monika 2downcasualgy2 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hgy2.png")

image monika 3downcasualga = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hga.png")
image monika 3downcasualge = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hge.png")
image monika 3downcasualgf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hgf.png")
image monika 3downcasualgg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hgg.png")
image monika 3downcasualgh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hgh.png")
image monika 3downcasualgi = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hgi.png")
image monika 3downcasualgy1 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hgy1.png")
image monika 3downcasualgy2 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hgy2.png")

image monika 4downcasualga = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hge.png")
image monika 4downcasualge = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hge.png")
image monika 4downcasualgf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hgf.png")
image monika 4downcasualgg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hgg.png")
image monika 4downcasualgh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hgh.png")
image monika 4downcasualgi = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hgi.png")
image monika 4downcasualgy1 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hgy1.png")
image monika 4downcasualgy2 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hgy2.png")

image monika 5downcasualga = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/3bhga.png")
image monika 5downcasualgb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/3bhgb.png")

# Date Clothes Monika
image monika 1datea = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/a.png")
image monika 1dateb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/b.png")
image monika 1datec = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/c.png")
image monika 1dated = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/d.png")
image monika 1datee = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/e.png")
image monika 1datef = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/f.png")
image monika 1dateg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/g.png")
image monika 1dateh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/h.png")
image monika 1datei = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/i.png")
image monika 1datej = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/j.png")
image monika 1datek = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/k.png")
image monika 1datel = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/l.png")
image monika 1datem = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/m.png")
image monika 1daten = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/n.png")
image monika 1dateo = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/o.png")
image monika 1datep = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/p.png")
image monika 1dateq = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/q.png")
image monika 1dater = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/r.png")
image monika 1dates = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/s.png")
image monika 1datet = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/t.png")
image monika 1dateu = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/u.png")

image monika 2datea = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/a.png")
image monika 2dateb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/b.png")
image monika 2datec = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/c.png")
image monika 2dated = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/d.png")
image monika 2datee = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/e.png")
image monika 2datef = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/f.png")
image monika 2dateg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/g.png")
image monika 2dateh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/h.png")
image monika 2datei = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/i.png")
image monika 2datej = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/j.png")
image monika 2datek = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/k.png")
image monika 2datel = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/l.png")
image monika 2datem = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/m.png")
image monika 2daten = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/n.png")
image monika 2dateo = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/o.png")
image monika 2datep = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/p.png")
image monika 2dateq = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/q.png")
image monika 2dater = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/r.png")
image monika 2dates = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/s.png")
image monika 2datet = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/t.png")
image monika 2dateu = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/u.png")

image monika 3datea = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/a.png")
image monika 3dateb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/b.png")
image monika 3datec = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/c.png")
image monika 3dated = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/d.png")
image monika 3datee = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/e.png")
image monika 3datef = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/f.png")
image monika 3dateg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/g.png")
image monika 3dateh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/h.png")
image monika 3datei = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/i.png")
image monika 3datej = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/j.png")
image monika 3datek = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/k.png")
image monika 3datel = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/l.png")
image monika 3datem = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/m.png")
image monika 3daten = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/n.png")
image monika 3dateo = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/o.png")
image monika 3datep = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/p.png")
image monika 3dateq = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/q.png")
image monika 3dater = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "monika/r.png")
image monika 3dates = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "mod_assets/images/monika/s.png")
image monika 3datet = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "mod_assets/images/monika/t.png")
image monika 3dateu = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "mod_assets/images/monika/u.png")

image monika 4datea = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/a.png")
image monika 4dateb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/b.png")
image monika 4datec = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/c.png")
image monika 4dated = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/d.png")
image monika 4datee = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/e.png")
image monika 4datef = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/f.png")
image monika 4dateg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/g.png")
image monika 4dateh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/h.png")
image monika 4datei = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/i.png")
image monika 4datej = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/j.png")
image monika 4datek = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/k.png")
image monika 4datel = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/l.png")
image monika 4datem = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/m.png")
image monika 4daten = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/n.png")
image monika 4dateo = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/o.png")
image monika 4datep = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/p.png")
image monika 4dateq = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/q.png")
image monika 4dater = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "monika/r.png")
image monika 4dates = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/s.png")
image monika 4datet = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/t.png")
image monika 4dateu = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/u.png")

image monika 5datea = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/3ca.png")
image monika 5dateb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/3cb.png")

# Markov Monika Date
image monika 1datega = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "mod_assets/images/monika/ga.png")
image monika 1datege = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "mod_assets/images/monika/ge.png")
image monika 1dategf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "mod_assets/images/monika/gf.png")
image monika 1dategg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "mod_assets/images/monika/gg.png")
image monika 1dategi = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "mod_assets/images/monika/gi.png")
image monika 1dategy1 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "mod_assets/images/monika/gy1.png")
image monika 1dategy2 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "mod_assets/images/monika/gy2.png")

image monika 2datega = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/ga.png")
image monika 2datege = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/ge.png")
image monika 2dategf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/gf.png")
image monika 2dategg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/gg.png")
image monika 2dategi = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/gi.png")
image monika 2dategy1 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/gy1.png")
image monika 2dategy2 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/gy2.png")

image monika 3datega = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "mod_assets/images/monika/ga.png")
image monika 3datege = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "mod_assets/images/monika/ge.png")
image monika 3dategf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "mod_assets/images/monika/gf.png")
image monika 3dategg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "mod_assets/images/monika/gg.png")
image monika 3dategi = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "mod_assets/images/monika/gi.png")
image monika 3dategy1 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "mod_assets/images/monika/gy1.png")
image monika 3dategy2 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/1cr.png", (0, 0), "mod_assets/images/monika/gy2.png")

image monika 4datega = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/ge.png")
image monika 4datege = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/ge.png")
image monika 4dategf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/gf.png")
image monika 4dategg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/gg.png")
image monika 4dategi = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/gi.png")
image monika 4dategy1 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/gy1.png")
image monika 4dategy2 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2cl.png", (0, 0), "mod_assets/images/monika/2cr.png", (0, 0), "mod_assets/images/monika/gy2.png")

image monika 5datega = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/3cga.png")
image monika 5dategb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/3cgb.png")

# Date Clothes Monika - Hair Down
image monika 1downdatea = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/ha.png")
image monika 1downdateb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hb.png")
image monika 1downdatec = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hc.png")
image monika 1downdated = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hd.png")
image monika 1downdatee = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/he.png")
image monika 1downdatef = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hf.png")
image monika 1downdateg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hg.png")
image monika 1downdateh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hh.png")
image monika 1downdatei = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hi.png")
image monika 1downdatej = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hj.png")
image monika 1downdatek = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hk.png")
image monika 1downdatel = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hl.png")
image monika 1downdatem = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hm.png")
image monika 1downdaten = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hn.png")
image monika 1downdateo = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/ho.png")
image monika 1downdatep = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hp.png")
image monika 1downdateq = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hq.png")
image monika 1downdater = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hr.png")
image monika 1downdates = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hs.png")
image monika 1downdatet = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/ht.png")
image monika 1downdateu = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hu.png")

image monika 2downdatea = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/ha.png")
image monika 2downdateb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hb.png")
image monika 2downdatec = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hc.png")
image monika 2downdated = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hd.png")
image monika 2downdatee = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/he.png")
image monika 2downdatef = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hf.png")
image monika 2downdateg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hg.png")
image monika 2downdateh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hh.png")
image monika 2downdatei = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hi.png")
image monika 2downdatej = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hj.png")
image monika 2downdatek = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hk.png")
image monika 2downdatel = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hl.png")
image monika 2downdatem = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hm.png")
image monika 2downdaten = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hn.png")
image monika 2downdateo = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/ho.png")
image monika 2downdatep = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hp.png")
image monika 2downdateq = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hq.png")
image monika 2downdater = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hr.png")
image monika 2downdates = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hs.png")
image monika 2downdatet = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/ht.png")
image monika 2downdateu = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hu.png")

image monika 3downdatea = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/ha.png")
image monika 3downdateb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hb.png")
image monika 3downdatec = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hc.png")
image monika 3downdated = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hd.png")
image monika 3downdatee = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/he.png")
image monika 3downdatef = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hf.png")
image monika 3downdateg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hg.png")
image monika 3downdateh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hh.png")
image monika 3downdatei = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hi.png")
image monika 3downdatej = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hj.png")
image monika 3downdatek = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hk.png")
image monika 3downdatel = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hl.png")
image monika 3downdatem = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hm.png")
image monika 3downdaten = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hn.png")
image monika 3downdateo = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/ho.png")
image monika 3downdatep = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hp.png")
image monika 3downdateq = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hq.png")
image monika 3downdater = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hr.png")
image monika 3downdates = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hs.png")
image monika 3downdatet = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/ht.png")
image monika 3downdateu = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hu.png")

image monika 4downdatea = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/ha.png")
image monika 4downdateb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hb.png")
image monika 4downdatec = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hc.png")
image monika 4downdated = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hd.png")
image monika 4downdatee = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/he.png")
image monika 4downdatef = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hf.png")
image monika 4downdateg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hg.png")
image monika 4downdateh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hh.png")
image monika 4downdatei = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hi.png")
image monika 4downdatej = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hj.png")
image monika 4downdatek = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hk.png")
image monika 4downdatel = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hl.png")
image monika 4downdatem = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hm.png")
image monika 4downdaten = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hn.png")
image monika 4downdateo = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/ho.png")
image monika 4downdatep = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hp.png")
image monika 4downdateq = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hq.png")
image monika 4downdater = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hr.png")
image monika 4downdates = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hs.png")
image monika 4downdatet = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/ht.png")
image monika 4downdateu = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hu.png")

image monika 5downdatea = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/3cha.png")
image monika 5downdateb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/3chb.png")

# Markov Monika Date - Hair Down
image monika 1downdatega = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hga.png")
image monika 1downdatege = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hge.png")
image monika 1downdategf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hgf.png")
image monika 1downdategg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hgg.png")
image monika 1downdategh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hgh.png")
image monika 1downdategi = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hgi.png")
image monika 1downdategy1 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hgy1.png")
image monika 1downdategy2 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hgy2.png")

image monika 2downdatega = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hga.png")
image monika 2downdatege = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hge.png")
image monika 2downdategf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hgf.png")
image monika 2downdategg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hgg.png")
image monika 2downdategh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hgh.png")
image monika 2downdategi = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hgi.png")
image monika 2downdategy1 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hgy1.png")
image monika 2downdategy2 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hgy2.png")

image monika 3downdatega = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hga.png")
image monika 3downdatege = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hge.png")
image monika 3downdategf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hgf.png")
image monika 3downdategg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hgg.png")
image monika 3downdategh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hgh.png")
image monika 3downdategi = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hgi.png")
image monika 3downdategy1 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hgy1.png")
image monika 3downdategy2 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/1chr.png", (0, 0), "mod_assets/images/monika/hgy2.png")

image monika 4downdatega = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hge.png")
image monika 4downdatege = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hge.png")
image monika 4downdategf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hgf.png")
image monika 4downdategg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hgg.png")
image monika 4downdategh = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hgh.png")
image monika 4downdategi = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hgi.png")
image monika 4downdategy1 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hgy1.png")
image monika 4downdategy2 = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2chl.png", (0, 0), "mod_assets/images/monika/2chr.png", (0, 0), "mod_assets/images/monika/hgy2.png")

image monika 5downdatega = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/3chga.png")
image monika 5downdategb = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/3chgb.png")

# Monika School Generalised Definitions
image monika 1a = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoola", "True", "monika 1schoola")
image monika 1b = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoolb", "True", "monika 1schoolb")
image monika 1c = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoolc", "True", "monika 1schoolc")
image monika 1d = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoold", "True", "monika 1schoold")
image monika 1e = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoole", "True", "monika 1schoole")
image monika 1f = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoolf", "True", "monika 1schoolf")
image monika 1g = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoolg", "True", "monika 1schoolg")
image monika 1h = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoolh", "True", "monika 1schoolh")
image monika 1i = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschooli", "True", "monika 1schooli")
image monika 1j = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoolj", "True", "monika 1schoolj")
image monika 1k = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoolk", "True", "monika 1schoolk")
image monika 1l = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschooll", "True", "monika 1schooll")
image monika 1m = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoolm", "True", "monika 1schoolm")
image monika 1n = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschooln", "True", "monika 1schooln")
image monika 1o = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoolo", "True", "monika 1schoolo")
image monika 1p = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoolp", "True", "monika 1schoolp")
image monika 1q = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoolq", "True", "monika 1schoolq")
image monika 1r = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoolr", "True", "monika 1schoolr")
image monika 1s = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschools", "True", "monika 1schools")
image monika 1t = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoolt", "True", "monika 1schoolt")
image monika 1u = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoolu", "True", "monika 1schoolu")

image monika 2a = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoola", "True", "monika 2schoola")
image monika 2b = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoolb", "True", "monika 2schoolb")
image monika 2c = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoolc", "True", "monika 2schoolc")
image monika 2d = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoold", "True", "monika 2schoold")
image monika 2e = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoole", "True", "monika 2schoole")
image monika 2f = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoolf", "True", "monika 2schoolf")
image monika 2g = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoolg", "True", "monika 2schoolg")
image monika 2h = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoolh", "True", "monika 2schoolh")
image monika 2i = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschooli", "True", "monika 2schooli")
image monika 2j = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoolj", "True", "monika 2schoolj")
image monika 2k = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoolk", "True", "monika 2schoolk")
image monika 2l = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschooll", "True", "monika 2schooll")
image monika 2m = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoolm", "True", "monika 2schoolm")
image monika 2n = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschooln", "True", "monika 2schooln")
image monika 2o = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoolo", "True", "monika 2schoolo")
image monika 2p = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoolp", "True", "monika 2schoolp")
image monika 2q = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoolq", "True", "monika 2schoolq")
image monika 2r = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoolr", "True", "monika 2schoolr")
image monika 2s = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschools", "True", "monika 2schools")
image monika 2t = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoolt", "True", "monika 2schoolt")
image monika 2u = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoolu", "True", "monika 2schoolu")

image monika 3a = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoola", "True", "monika 3schoola")
image monika 3b = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoolb", "True", "monika 3schoolb")
image monika 3c = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoolc", "True", "monika 3schoolc")
image monika 3d = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoold", "True", "monika 3schoold")
image monika 3e = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoole", "True", "monika 3schoole")
image monika 3f = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoolf", "True", "monika 3schoolf")
image monika 3g = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoolg", "True", "monika 3schoolg")
image monika 3h = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoolh", "True", "monika 3schoolh")
image monika 3i = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschooli", "True", "monika 3schooli")
image monika 3j = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoolj", "True", "monika 3schoolj")
image monika 3k = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoolk", "True", "monika 3schoolk")
image monika 3l = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschooll", "True", "monika 3schooll")
image monika 3m = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoolm", "True", "monika 3schoolm")
image monika 3n = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschooln", "True", "monika 3schooln")
image monika 3o = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoolo", "True", "monika 3schoolo")
image monika 3p = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoolp", "True", "monika 3schoolp")
image monika 3q = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoolq", "True", "monika 3schoolq")
image monika 3r = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoolr", "True", "monika 3schoolr")
image monika 3s = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschools", "True", "monika 3schools")
image monika 3t = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoolt", "True", "monika 3schoolt")
image monika 3u = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoolu", "True", "monika 3schoolu")

image monika 4a = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoola", "True", "monika 4schoola")
image monika 4b = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoolb", "True", "monika 4schoolb")
image monika 4c = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoolc", "True", "monika 4schoolc")
image monika 4d = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoold", "True", "monika 4schoold")
image monika 4e = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoole", "True", "monika 4schoole")
image monika 4f = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoolf", "True", "monika 4schoolf")
image monika 4g = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoolg", "True", "monika 4schoolg")
image monika 4h = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoolh", "True", "monika 4schoolh")
image monika 4i = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschooli", "True", "monika 4schooli")
image monika 4j = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoolj", "True", "monika 4schoolj")
image monika 4k = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoolk", "True", "monika 4schoolk")
image monika 4l = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschooll", "True", "monika 4schooll")
image monika 4m = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoolm", "True", "monika 4schoolm")
image monika 4n = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschooln", "True", "monika 4schooln")
image monika 4o = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoolo", "True", "monika 4schoolo")
image monika 4p = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoolp", "True", "monika 4schoolp")
image monika 4q = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoolq", "True", "monika 4schoolq")
image monika 4r = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoolr", "True", "monika 4schoolr")
image monika 4s = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschools", "True", "monika 4schools")
image monika 4t = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoolt", "True", "monika 4schoolt")
image monika 4u = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoolu", "True", "monika 4schoolu")

image monika 5a = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 5downschoola", "True", "monika 5schoola")
image monika 5b = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 5downschoolb", "True", "monika 5schoolb")

# Monika Casual Generalised Definitions
image monika 1ba = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdatea", "monika_type == 1 and ch12_markov_agree", "monika 1downcasuala", "monika_outfit == 1", "monika 1datea", "True", "monika 1casuala")
image monika 1bb = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdateb", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualb", "monika_outfit == 1", "monika 1dateb", "True", "monika 1casualb")
image monika 1bc = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdatec", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualc", "monika_outfit == 1", "monika 1datec", "True", "monika 1casualc")
image monika 1bd = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdated", "monika_type == 1 and ch12_markov_agree", "monika 1downcasuald", "monika_outfit == 1", "monika 1dated", "True", "monika 1casuald")
image monika 1be = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdatee", "monika_type == 1 and ch12_markov_agree", "monika 1downcasuale", "monika_outfit == 1", "monika 1datee", "True", "monika 1casuale")
image monika 1bf = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdatef", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualf", "monika_outfit == 1", "monika 1datef", "True", "monika 1casualf")
image monika 1bg = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdateg", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualg", "monika_outfit == 1", "monika 1dateg", "True", "monika 1casualg")
image monika 1bh = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdateh", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualh", "monika_outfit == 1", "monika 1dateh", "True", "monika 1casualh")
image monika 1bi = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdatei", "monika_type == 1 and ch12_markov_agree", "monika 1downcasuali", "monika_outfit == 1", "monika 1datei", "True", "monika 1casuali")
image monika 1bj = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdatej", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualj", "monika_outfit == 1", "monika 1datej", "True", "monika 1casualj")
image monika 1bk = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdatek", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualk", "monika_outfit == 1", "monika 1datek", "True", "monika 1casualk")
image monika 1bl = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdatel", "monika_type == 1 and ch12_markov_agree", "monika 1downcasuall", "monika_outfit == 1", "monika 1datel", "True", "monika 1casuall")
image monika 1bm = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdatem", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualm", "monika_outfit == 1", "monika 1datem", "True", "monika 1casualm")
image monika 1bn = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdaten", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualn", "monika_outfit == 1", "monika 1daten", "True", "monika 1casualn")
image monika 1bo = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdateo", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualo", "monika_outfit == 1", "monika 1dateo", "True", "monika 1casualo")
image monika 1bp = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdatep", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualp", "monika_outfit == 1", "monika 1datep", "True", "monika 1casualp")
image monika 1bq = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdateq", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualq", "monika_outfit == 1", "monika 1dateq", "True", "monika 1casualq")
image monika 1br = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdater", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualr", "monika_outfit == 1", "monika 1dater", "True", "monika 1casualr")
image monika 1bs = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdates", "monika_type == 1 and ch12_markov_agree", "monika 1downcasuals", "monika_outfit == 1", "monika 1dates", "True", "monika 1casuals")
image monika 1bt = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdatet", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualt", "monika_outfit == 1", "monika 1datet", "True", "monika 1casualt")
image monika 1bu = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdateu", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualu", "monika_outfit == 1", "monika 1dateu", "True", "monika 1casualu")

image monika 2ba = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdatea", "monika_type == 1 and ch12_markov_agree", "monika 2downcasuala", "monika_outfit == 1", "monika 2datea", "True", "monika 2casuala")
image monika 2bb = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdateb", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualb", "monika_outfit == 1", "monika 2dateb", "True", "monika 2casualb")
image monika 2bc = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdatec", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualc", "monika_outfit == 1", "monika 2datec", "True", "monika 2casualc")
image monika 2bd = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdated", "monika_type == 1 and ch12_markov_agree", "monika 2downcasuald", "monika_outfit == 1", "monika 2dated", "True", "monika 2casuald")
image monika 2be = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdatee", "monika_type == 1 and ch12_markov_agree", "monika 2downcasuale", "monika_outfit == 1", "monika 2datee", "True", "monika 2casuale")
image monika 2bf = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdatef", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualf", "monika_outfit == 1", "monika 2datef", "True", "monika 2casualf")
image monika 2bg = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdateg", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualg", "monika_outfit == 1", "monika 2dateg", "True", "monika 2casualg")
image monika 2bh = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdateh", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualh", "monika_outfit == 1", "monika 2dateh", "True", "monika 2casualh")
image monika 2bi = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdatei", "monika_type == 1 and ch12_markov_agree", "monika 2downcasuali", "monika_outfit == 1", "monika 2datei", "True", "monika 2casuali")
image monika 2bj = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdatej", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualj", "monika_outfit == 1", "monika 2datej", "True", "monika 2casualj")
image monika 2bk = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdatek", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualk", "monika_outfit == 1", "monika 2datek", "True", "monika 2casualk")
image monika 2bl = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdatel", "monika_type == 1 and ch12_markov_agree", "monika 2downcasuall", "monika_outfit == 1", "monika 2datel", "True", "monika 2casuall")
image monika 2bm = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdatem", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualm", "monika_outfit == 1", "monika 2datem", "True", "monika 2casualm")
image monika 2bn = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdaten", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualn", "monika_outfit == 1", "monika 2daten", "True", "monika 2casualn")
image monika 2bo = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdateo", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualo", "monika_outfit == 1", "monika 2dateo", "True", "monika 2casualo")
image monika 2bp = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdatep", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualp", "monika_outfit == 1", "monika 2datep", "True", "monika 2casualp")
image monika 2bq = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdateq", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualq", "monika_outfit == 1", "monika 2dateq", "True", "monika 2casualq")
image monika 2br = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdater", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualr", "monika_outfit == 1", "monika 2dater", "True", "monika 2casualr")
image monika 2bs = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdates", "monika_type == 1 and ch12_markov_agree", "monika 2downcasuals", "monika_outfit == 1", "monika 2dates", "True", "monika 2casuals")
image monika 2bt = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdatet", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualt", "monika_outfit == 1", "monika 2datet", "True", "monika 2casualt")
image monika 2bu = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdateu", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualu", "monika_outfit == 1", "monika 2dateu", "True", "monika 2casualu")

image monika 3ba = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdatea", "monika_type == 1 and ch12_markov_agree", "monika 3downcasuala", "monika_outfit == 1", "monika 3datea", "True", "monika 3casuala")
image monika 3bb = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdateb", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualb", "monika_outfit == 1", "monika 3dateb", "True", "monika 3casualb")
image monika 3bc = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdatec", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualc", "monika_outfit == 1", "monika 3datec", "True", "monika 3casualc")
image monika 3bd = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdated", "monika_type == 1 and ch12_markov_agree", "monika 3downcasuald", "monika_outfit == 1", "monika 3dated", "True", "monika 3casuald")
image monika 3be = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdatee", "monika_type == 1 and ch12_markov_agree", "monika 3downcasuale", "monika_outfit == 1", "monika 3datee", "True", "monika 3casuale")
image monika 3bf = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdatef", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualf", "monika_outfit == 1", "monika 3datef", "True", "monika 3casualf")
image monika 3bg = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdateg", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualg", "monika_outfit == 1", "monika 3dateg", "True", "monika 3casualg")
image monika 3bh = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdateh", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualh", "monika_outfit == 1", "monika 3dateh", "True", "monika 3casualh")
image monika 3bi = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdatei", "monika_type == 1 and ch12_markov_agree", "monika 3downcasuali", "monika_outfit == 1", "monika 3datei", "True", "monika 3casuali")
image monika 3bj = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdatej", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualj", "monika_outfit == 1", "monika 3datej", "True", "monika 3casualj")
image monika 3bk = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdatek", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualk", "monika_outfit == 1", "monika 3datek", "True", "monika 3casualk")
image monika 3bl = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdatel", "monika_type == 1 and ch12_markov_agree", "monika 3downcasuall", "monika_outfit == 1", "monika 3datel", "True", "monika 3casuall")
image monika 3bm = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdatem", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualm", "monika_outfit == 1", "monika 3datem", "True", "monika 3casualm")
image monika 3bn = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdaten", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualn", "monika_outfit == 1", "monika 3daten", "True", "monika 3casualn")
image monika 3bo = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdateo", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualo", "monika_outfit == 1", "monika 3dateo", "True", "monika 3casualo")
image monika 3bp = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdatep", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualp", "monika_outfit == 1", "monika 3datep", "True", "monika 3casualp")
image monika 3bq = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdateq", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualq", "monika_outfit == 1", "monika 3dateq", "True", "monika 3casualq")
image monika 3br = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdater", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualr", "monika_outfit == 1", "monika 3dater", "True", "monika 3casualr")
image monika 3bs = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdates", "monika_type == 1 and ch12_markov_agree", "monika 3downcasuals", "monika_outfit == 1", "monika 3dates", "True", "monika 3casuals")
image monika 3bt = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdatet", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualt", "monika_outfit == 1", "monika 3datet", "True", "monika 3casualt")
image monika 3bu = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdateu", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualu", "monika_outfit == 1", "monika 3dateu", "True", "monika 3casualu")

image monika 4ba = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdatea", "monika_type == 1 and ch12_markov_agree", "monika 4downcasuala", "monika_outfit == 1", "monika 4datea", "True", "monika 4casuala")
image monika 4bb = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdateb", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualb", "monika_outfit == 1", "monika 4dateb", "True", "monika 4casualb")
image monika 4bc = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdatec", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualc", "monika_outfit == 1", "monika 4datec", "True", "monika 4casualc")
image monika 4bd = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdated", "monika_type == 1 and ch12_markov_agree", "monika 4downcasuald", "monika_outfit == 1", "monika 4dated", "True", "monika 4casuald")
image monika 4be = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdatee", "monika_type == 1 and ch12_markov_agree", "monika 4downcasuale", "monika_outfit == 1", "monika 4datee", "True", "monika 4casuale")
image monika 4bf = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdatef", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualf", "monika_outfit == 1", "monika 4datef", "True", "monika 4casualf")
image monika 4bg = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdateg", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualg", "monika_outfit == 1", "monika 4dateg", "True", "monika 4casualg")
image monika 4bh = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdateh", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualh", "monika_outfit == 1", "monika 4dateh", "True", "monika 4casualh")
image monika 4bi = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdatei", "monika_type == 1 and ch12_markov_agree", "monika 4downcasuali", "monika_outfit == 1", "monika 4datei", "True", "monika 4casuali")
image monika 4bj = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdatej", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualj", "monika_outfit == 1", "monika 4datej", "True", "monika 4casualj")
image monika 4bk = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdatek", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualk", "monika_outfit == 1", "monika 4datek", "True", "monika 4casualk")
image monika 4bl = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdatel", "monika_type == 1 and ch12_markov_agree", "monika 4downcasuall", "monika_outfit == 1", "monika 4datel", "True", "monika 4casuall")
image monika 4bm = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdatem", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualm", "monika_outfit == 1", "monika 4datem", "True", "monika 4casualm")
image monika 4bn = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdaten", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualn", "monika_outfit == 1", "monika 4daten", "True", "monika 4casualn")
image monika 4bo = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdateo", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualo", "monika_outfit == 1", "monika 4dateo", "True", "monika 4casualo")
image monika 4bp = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdatep", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualp", "monika_outfit == 1", "monika 4datep", "True", "monika 4casualp")
image monika 4bq = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdateq", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualq", "monika_outfit == 1", "monika 4dateq", "True", "monika 4casualq")
image monika 4br = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdater", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualr", "monika_outfit == 1", "monika 4dater", "True", "monika 4casualr")
image monika 4bs = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdates", "monika_type == 1 and ch12_markov_agree", "monika 4downcasuals", "monika_outfit == 1", "monika 4dates", "True", "monika 4casuals")
image monika 4bt = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdatet", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualt", "monika_outfit == 1", "monika 4datet", "True", "monika 4casualt")
image monika 4bu = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdateu", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualu", "monika_outfit == 1", "monika 4dateu", "True", "monika 4casualu")

image monika 5ba = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 5downdatea", "monika_type == 1 and ch12_markov_agree", "monika 5downcasuala", "monika_outfit == 1", "monika 5datea", "True", "monika 5casuala")
image monika 5bb = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 5downdateb", "monika_type == 1 and ch12_markov_agree", "monika 5downcasualb", "monika_outfit == 1", "monika 5dateb", "True", "monika 5casualb")

# Markov Monika Generalised Definitions
image monika 1ga = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoolga", "True", "monika 1schoolga")
image monika 1ge = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoolge", "True", "monika 1schoolge")
image monika 1gf = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoolgf", "True", "monika 1schoolgf")
image monika 1gg = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoolgg", "True", "monika 1schoolgg")
image monika 1gh = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoolgh", "True", "monika 1schoolgh")
image monika 1gi = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoolgi", "True", "monika 1schoolgi")
image monika 1gy1 = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoolgy1", "True", "monika 1schoolgy1")
image monika 1gy2 = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downschoolgy2", "True", "monika 1schoolgy2")

image monika 2ga = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoolga", "True", "monika 2schoolga")
image monika 2ge = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoolge", "True", "monika 2schoolge")
image monika 2gf = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoolgf", "True", "monika 2schoolgf")
image monika 2gg = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoolgg", "True", "monika 2schoolgg")
image monika 2gh = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoolgh", "True", "monika 2schoolgh")
image monika 2gi = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoolgi", "True", "monika 2schoolgi")
image monika 2gy1 = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoolgy1", "True", "monika 2schoolgy1")
image monika 2gy2 = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downschoolgy2", "True", "monika 2schoolgy2")

image monika 3ga = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoolga", "True", "monika 3schoolga")
image monika 3ge = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoolge", "True", "monika 3schoolge")
image monika 3gf = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoolgf", "True", "monika 3schoolgf")
image monika 3gg = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoolgg", "True", "monika 3schoolgg")
image monika 3gh = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoolgh", "True", "monika 3schoolgh")
image monika 3gi = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoolgi", "True", "monika 3schoolgi")
image monika 3gy1 = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoolgy1", "True", "monika 3schoolgy1")
image monika 3gy2 = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downschoolgy2", "True", "monika 3schoolgy2")

image monika 4ga = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoolga", "True", "monika 4schoolga")
image monika 4ge = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoolge", "True", "monika 4schoolge")
image monika 4gf = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoolgf", "True", "monika 4schoolgf")
image monika 4gg = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoolgg", "True", "monika 4schoolgg")
image monika 4gh = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoolgh", "True", "monika 4schoolgh")
image monika 4gi = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoolgi", "True", "monika 4schoolgi")
image monika 4gy1 = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoolgy1", "True", "monika 4schoolgy1")
image monika 4gy2 = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downschoolgy2", "True", "monika 4schoolgy2")

image monika 5ga = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 5downschoolga", "True", "monika 5schoolga")
image monika 5gb = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 5downschoolgb", "True", "monika 5schoolgb")

# Markov Monika Casual Generalised Definitions
image monika 1bga = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdatega", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualga", "monika_outfit == 1", "monika 1datega", "True", "monika 1casualga")
image monika 1bge = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdatege", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualge", "monika_outfit == 1", "monika 1datege", "True", "monika 1casualge")
image monika 1bgf = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdategf", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualgf", "monika_outfit == 1", "monika 1dategf", "True", "monika 1casualgf")
image monika 1bgg = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdategg", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualgg", "monika_outfit == 1", "monika 1dategg", "True", "monika 1casualgg")
image monika 1bgh = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdategh", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualgh", "monika_outfit == 1", "monika 1dategh", "True", "monika 1casualgh")
image monika 1bgi = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdategi", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualgi", "monika_outfit == 1", "monika 1dategi", "True", "monika 1casualgi")
image monika 1bgy1 = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdategy1", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualgy1", "monika_outfit == 1", "monika 1dategy1", "True", "monika 1casualgy1")
image monika 1bgy2 = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 1downdategy2", "monika_type == 1 and ch12_markov_agree", "monika 1downcasualgy2", "monika_outfit == 1", "monika 1dategy2", "True", "monika 1casualgy2")

image monika 2bga = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdatega", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualga", "monika_outfit == 1", "monika 2datega", "True", "monika 2casualga")
image monika 2bge = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdatege", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualge", "monika_outfit == 1", "monika 2datege", "True", "monika 2casualge")
image monika 2bgf = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdategf", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualgf", "monika_outfit == 1", "monika 2dategf", "True", "monika 2casualgf")
image monika 2bgg = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdategg", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualgg", "monika_outfit == 1", "monika 2dategg", "True", "monika 2casualgg")
image monika 2bgh = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdategh", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualgh", "monika_outfit == 1", "monika 2dategh", "True", "monika 2casualgh")
image monika 2bgi = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdategi", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualgi", "monika_outfit == 1", "monika 2dategi", "True", "monika 2casualgi")
image monika 2bgy1 = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdategy1", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualgy1", "monika_outfit == 1", "monika 2dategy1", "True", "monika 2casualgy1")
image monika 2bgy2 = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 2downdategy2", "monika_type == 1 and ch12_markov_agree", "monika 2downcasualgy2", "monika_outfit == 1", "monika 2dategy2", "True", "monika 2casualgy2")

image monika 3bga = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdatega", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualga", "monika_outfit == 1", "monika 3datega", "True", "monika 3casualga")
image monika 3bge = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdatege", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualge", "monika_outfit == 1", "monika 3datege", "True", "monika 3casualge")
image monika 3bgf = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdategf", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualgf", "monika_outfit == 1", "monika 3dategf", "True", "monika 3casualgf")
image monika 3bgg = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdategg", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualgg", "monika_outfit == 1", "monika 3dategg", "True", "monika 3casualgg")
image monika 3bgh = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdategh", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualgh", "monika_outfit == 1", "monika 3dategh", "True", "monika 3casualgh")
image monika 3bgi = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdategi", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualgi", "monika_outfit == 1", "monika 3dategi", "True", "monika 3casualgi")
image monika 3bgy1 = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdategy1", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualgy1", "monika_outfit == 1", "monika 3dategy1", "True", "monika 3casualgy1")
image monika 3bgy2 = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 3downdategy2", "monika_type == 1 and ch12_markov_agree", "monika 3downcasualgy2", "monika_outfit == 1", "monika 3dategy2", "True", "monika 3casualgy2")

image monika 4bga = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdatega", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualga", "monika_outfit == 1", "monika 4datega", "True", "monika 4casualga")
image monika 4bge = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdatege", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualge", "monika_outfit == 1", "monika 4datege", "True", "monika 4casualge")
image monika 4bgf = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdategf", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualgf", "monika_outfit == 1", "monika 4dategf", "True", "monika 4casualgf")
image monika 4bgg = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdategg", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualgg", "monika_outfit == 1", "monika 4dategg", "True", "monika 4casualgg")
image monika 4bgh = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdategh", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualgh", "monika_outfit == 1", "monika 4dategh", "True", "monika 4casualgh")
image monika 4bgi = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdategi", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualgi", "monika_outfit == 1", "monika 4dategi", "True", "monika 4casualgi")
image monika 4bgy = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdategy1", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualgy1", "monika_outfit == 1", "monika 4dategy1", "True", "monika 4casualgy1")
image monika 4bgy = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 4downdategy2", "monika_type == 1 and ch12_markov_agree", "monika 4downcasualgy2", "monika_outfit == 1", "monika 4dategy2", "True", "monika 4casualgy2")

image monika 5bga = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 5downdatega", "monika_type == 1 and ch12_markov_agree", "monika 5downcasualga", "monika_outfit == 1", "monika 5datega", "True", "monika 5casualga")
image monika 5bgb = ConditionSwitch("monika_outfit == 1 and monika_type == 1 and ch12_markov_agree", "monika 5downdategb", "monika_type == 1 and ch12_markov_agree", "monika 5downcasualgb", "monika_outfit == 1", "monika 5dategb", "True", "monika 5casualgb")

image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat

image monika g3:
    "monika 1bgg"
    pause 0.5
    "monika 1bg"

image monika g4:
    "monika 1gi"
    pause 0.5
    "monika 1i"

image monika g5:
    "monika 1ge"
    pause 0.5
    "monika 1e"

image monika g6:
    "monika 1ga"
    pause 0.5
    "monika 1a"

image monika g7:
    "monika 1ga"
    pause 0.5
    "monika 1a"

image monika g8:
    "monika 1gh"
    pause 0.5
    "monika 1h"

image monika g9:
    "monika 5ga"
    pause 0.5
    "monika 5a"

image monika 1bgy:
    "monika 2bgy1"
    pause 0.5
    "monika 2bgy2"

image monika 2bgy:
    "monika 2bgy1"
    pause 0.5
    "monika 2bgy2"

# Dadsuki
image dadsuki 1 = im.Composite((960, 960), (0, 0), "mod_assets/images/dadsuki/1a.png")
image dadsuki 1a = im.Composite((960, 960), (0, 0), "mod_assets/images/dadsuki/1a.png")
image dadsuki 1b = im.Composite((960, 960), (0, 0), "mod_assets/images/dadsuki/1b.png")
image dadsuki 1c = im.Composite((960, 960), (0, 0), "mod_assets/images/dadsuki/1c.png")
image dadsuki 1d = im.Composite((960, 960), (0, 0), "mod_assets/images/dadsuki/1d.png")
image dadsuki 1e = im.Composite((960, 960), (0, 0), "mod_assets/images/dadsuki/1e.png")
image dadsuki 1f = im.Composite((960, 960), (0, 0), "mod_assets/images/dadsuki/1f.png")
image dadsuki 1g = im.Composite((960, 960), (0, 0), "mod_assets/images/dadsuki/1g.png")
image dadsuki 1h = im.Composite((960, 960), (0, 0), "mod_assets/images/dadsuki/1h.png")
image dadsuki 1i = im.Composite((960, 960), (0, 0), "mod_assets/images/dadsuki/1i.png")
image dadsuki 1j = im.Composite((960, 960), (0, 0), "mod_assets/images/dadsuki/1j.png")
image dadsuki 1k = im.Composite((960, 960), (0, 0), "mod_assets/images/dadsuki/1k.png")
image dadsuki 1l = im.Composite((960, 960), (0, 0), "mod_assets/images/dadsuki/1l.png")
image dadsuki 1m = im.Composite((960, 960), (0, 0), "mod_assets/images/dadsuki/1m.png")
image dadsuki 1n = im.Composite((960, 960), (0, 0), "mod_assets/images/dadsuki/1n.png")
image dadsuki 1o = im.Composite((960, 960), (0, 0), "mod_assets/images/dadsuki/1o.png")
image dadsuki 1p = im.Composite((960, 960), (0, 0), "mod_assets/images/dadsuki/1p.png")

# Momsuki
image momsuki 1 = im.Composite((960, 960), (0, 0), "mod_assets/images/momsuki/1lr.png", (0, 0), "mod_assets/images/momsuki/a.png")
image momsuki 1a = im.Composite((960, 960), (0, 0), "mod_assets/images/momsuki/1lr.png", (0, 0), "mod_assets/images/momsuki/a.png")
image momsuki 1b = im.Composite((960, 960), (0, 0), "mod_assets/images/momsuki/1lr.png", (0, 0), "mod_assets/images/momsuki/b.png")
image momsuki 1c = im.Composite((960, 960), (0, 0), "mod_assets/images/momsuki/1lr.png", (0, 0), "mod_assets/images/momsuki/c.png")
image momsuki 1d = im.Composite((960, 960), (0, 0), "mod_assets/images/momsuki/1lr.png", (0, 0), "mod_assets/images/momsuki/d.png")
image momsuki 1e = im.Composite((960, 960), (0, 0), "mod_assets/images/momsuki/1lr.png", (0, 0), "mod_assets/images/momsuki/e.png")
image momsuki 1f = im.Composite((960, 960), (0, 0), "mod_assets/images/momsuki/1lr.png", (0, 0), "mod_assets/images/momsuki/f.png")
image momsuki 1g = im.Composite((960, 960), (0, 0), "mod_assets/images/momsuki/1lr.png", (0, 0), "mod_assets/images/momsuki/g.png")
image momsuki 1h = im.Composite((960, 960), (0, 0), "mod_assets/images/momsuki/1lr.png", (0, 0), "mod_assets/images/momsuki/h.png")
image momsuki 1i = im.Composite((960, 960), (0, 0), "mod_assets/images/momsuki/1lr.png", (0, 0), "mod_assets/images/momsuki/i.png")

# Mysterious Clerk
image mysteriousclerk 1a = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/a.png")
image mysteriousclerk 1b = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/b.png")
image mysteriousclerk 1c = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/c.png")
image mysteriousclerk 1d = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/d.png")
image mysteriousclerk 1e = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/e.png")
image mysteriousclerk 1f = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/f.png")
image mysteriousclerk 1g = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/g.png")
image mysteriousclerk 1h = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/h.png")
image mysteriousclerk 1i = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/i.png")
image mysteriousclerk 1j = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/j.png")
image mysteriousclerk 1k = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/k.png")
image mysteriousclerk 1l = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/l.png")
image mysteriousclerk 1m = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/m.png")
image mysteriousclerk 1n = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/n.png")
image mysteriousclerk 1o = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/o.png")
image mysteriousclerk 1p = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/p.png")
image mysteriousclerk 1q = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/q.png")
image mysteriousclerk 1r = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/r.png")
image mysteriousclerk 1s = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/s.png")
image mysteriousclerk 1t = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/t.png")
image mysteriousclerk 1u = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/u.png")
image mysteriousclerk 1v = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/v.png")
image mysteriousclerk 1w = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/a2.png")
image mysteriousclerk 1x = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/aB.png")

image mysteriousclerk 2a = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/a.png")
image mysteriousclerk 2b = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/b.png")
image mysteriousclerk 2c = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/c.png")
image mysteriousclerk 2d = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/d.png")
image mysteriousclerk 2e = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/e.png")
image mysteriousclerk 2f = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/f.png")
image mysteriousclerk 2g = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/g.png")
image mysteriousclerk 2h = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/h.png")
image mysteriousclerk 2i = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/i.png")
image mysteriousclerk 2j = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/j.png")
image mysteriousclerk 2k = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/k.png")
image mysteriousclerk 2l = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/l.png")
image mysteriousclerk 2m = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/m.png")
image mysteriousclerk 2n = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/n.png")
image mysteriousclerk 2o = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/o.png")
image mysteriousclerk 2p = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/p.png")
image mysteriousclerk 2q = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/q.png")
image mysteriousclerk 2r = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/r.png")
image mysteriousclerk 2s = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/s.png")
image mysteriousclerk 2t = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/t.png")
image mysteriousclerk 2u = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/u.png")
image mysteriousclerk 2v = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/v.png")
image mysteriousclerk 2w = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/a2.png")
image mysteriousclerk 2x = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/aB.png")

image mysteriousclerk 3a = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/a.png")
image mysteriousclerk 3b = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/b.png")
image mysteriousclerk 3c = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/c.png")
image mysteriousclerk 3d = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/d.png")
image mysteriousclerk 3e = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/e.png")
image mysteriousclerk 3f = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/f.png")
image mysteriousclerk 3g = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/g.png")
image mysteriousclerk 3h = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/h.png")
image mysteriousclerk 3i = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/i.png")
image mysteriousclerk 3j = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/j.png")
image mysteriousclerk 3k = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/k.png")
image mysteriousclerk 3l = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/l.png")
image mysteriousclerk 3m = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/m.png")
image mysteriousclerk 3n = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/n.png")
image mysteriousclerk 3o = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/o.png")
image mysteriousclerk 3p = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/p.png")
image mysteriousclerk 3q = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/q.png")
image mysteriousclerk 3r = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/r.png")
image mysteriousclerk 3s = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/s.png")
image mysteriousclerk 3t = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/t.png")
image mysteriousclerk 3u = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/u.png")
image mysteriousclerk 3v = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/v.png")
image mysteriousclerk 3w = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/a2.png")
image mysteriousclerk 3x = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/aB.png")

image mysteriousclerk 4a = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/a.png")
image mysteriousclerk 4b = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/b.png")
image mysteriousclerk 4c = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/c.png")
image mysteriousclerk 4d = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/d.png")
image mysteriousclerk 4e = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/e.png")
image mysteriousclerk 4f = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/f.png")
image mysteriousclerk 4g = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/g.png")
image mysteriousclerk 4h = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/h.png")
image mysteriousclerk 4i = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/i.png")
image mysteriousclerk 4j = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/j.png")
image mysteriousclerk 4k = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/k.png")
image mysteriousclerk 4l = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/l.png")
image mysteriousclerk 4m = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/m.png")
image mysteriousclerk 4n = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/n.png")
image mysteriousclerk 4o = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/o.png")
image mysteriousclerk 4p = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/p.png")
image mysteriousclerk 4q = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/q.png")
image mysteriousclerk 4r = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/r.png")
image mysteriousclerk 4s = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/s.png")
image mysteriousclerk 4t = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/t.png")
image mysteriousclerk 4u = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/u.png")
image mysteriousclerk 4v = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/v.png")
image mysteriousclerk 4w = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/a2.png")
image mysteriousclerk 4x = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/aB.png")

image mysteriousclerk 5a = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/a.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5b = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/b.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5c = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/c.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5d = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/d.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5e = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/e.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5f = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/f.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5g = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/g.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5h = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/h.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5i = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/i.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5j = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/j.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5k = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/k.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5l = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/l.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5m = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/m.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5n = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/n.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5o = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/o.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5p = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/p.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5q = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/q.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5r = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/r.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5s = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/s.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5t = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/t.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5u = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/u.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5v = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/v.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5w = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/a2.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")
image mysteriousclerk 5x = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/aB.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png")

image mysteriousclerk 1ad = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1bd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/b.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1cd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/c.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1dd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/d.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1ed = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/e.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1fd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/f.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1gd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/g.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1hd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/h.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1id = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/i.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1jd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/j.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1kd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/k.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1ld = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/l.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1md = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/m.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1nd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/n.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1od = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/o.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1pd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/p.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1qd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/q.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1rd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/r.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1sd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/s.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1td = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/t.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1ud = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/u.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1vd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/v.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1wd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/a2.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 1xd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/aB.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")

image mysteriousclerk 2ad = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2bd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/b.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2cd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/c.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2dd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/d.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2ed = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/e.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2fd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/f.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2gd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/g.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2hd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/h.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2id = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/i.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2jd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/j.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2kd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/k.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2ld = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/l.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2md = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/m.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2nd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/n.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2od = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/o.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2pd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/p.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2qd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/q.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2rd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/r.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2sd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/s.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2td = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/t.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2ud = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/u.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2vd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/v.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2wd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/a2.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 2xd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/aB.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")

image mysteriousclerk 3ad = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3bd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/b.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3cd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/c.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3dd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/d.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3ed = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/e.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3fd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/f.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3gd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/g.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3hd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/h.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3id = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/i.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3jd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/j.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3kd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/k.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3ld = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/l.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3md = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/m.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3nd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/n.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3od = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/o.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3pd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/p.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3qd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/q.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3rd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/r.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3sd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/s.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3td = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/t.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3ud = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/u.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3vd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/v.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3wd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/a2.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 3xd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/aB.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")

image mysteriousclerk 4ad = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4bd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/b.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4cd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/c.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4dd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/d.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4ed = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/e.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4fd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/f.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4gd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/g.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4hd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/h.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4id = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/i.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4jd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/j.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4kd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/k.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4ld = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/l.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4md = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/m.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4nd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/n.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4od = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/o.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4pd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/p.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4qd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/q.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4rd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/r.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4sd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/s.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4td = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/t.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4ud = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/u.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4vd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/v.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4wd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/a2.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 4xd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2l.png", (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/aB.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")

image mysteriousclerk 5ad = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/a.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5bd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/b.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5cd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/c.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5dd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/d.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5ed = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/e.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5fd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/f.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5gd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/g.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5hd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/h.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5id = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/i.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5jd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/j.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5kd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/k.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5ld = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/l.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5md = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/m.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5nd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/n.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5od = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/o.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5pd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/p.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5qd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/q.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5rd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/r.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5sd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/s.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5td = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/t.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5ud = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/u.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5vd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/v.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5wd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/a2.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 5xd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/aB.png", (0, 0), "mod_assets/images/mysteriousclerk/3a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")

image mysteriousclerk 6a = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/a.png")
image mysteriousclerk 6b = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/b.png")
image mysteriousclerk 6c = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/c.png")
image mysteriousclerk 6d = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/d.png")
image mysteriousclerk 6e = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/e.png")
image mysteriousclerk 6f = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/f.png")
image mysteriousclerk 6g = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/g.png")
image mysteriousclerk 6h = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/h.png")
image mysteriousclerk 6i = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/i.png")
image mysteriousclerk 6j = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/j.png")
image mysteriousclerk 6k = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/k.png")
image mysteriousclerk 6l = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/l.png")
image mysteriousclerk 6m = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/m.png")
image mysteriousclerk 6n = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/n.png")
image mysteriousclerk 6o = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/o.png")
image mysteriousclerk 6p = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/p.png")
image mysteriousclerk 6q = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/q.png")
image mysteriousclerk 6r = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/r.png")
image mysteriousclerk 6s = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/s.png")
image mysteriousclerk 6t = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/t.png")
image mysteriousclerk 6u = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/u.png")
image mysteriousclerk 6v = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/v.png")
image mysteriousclerk 6w = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/a2.png")
image mysteriousclerk 6x = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/aB.png")

image mysteriousclerk 7a = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/a.png")
image mysteriousclerk 7b = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/b.png")
image mysteriousclerk 7c = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/c.png")
image mysteriousclerk 7d = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/d.png")
image mysteriousclerk 7e = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/e.png")
image mysteriousclerk 7f = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/f.png")
image mysteriousclerk 7g = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/g.png")
image mysteriousclerk 7h = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/h.png")
image mysteriousclerk 7i = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/i.png")
image mysteriousclerk 7j = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/j.png")
image mysteriousclerk 7k = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/k.png")
image mysteriousclerk 7l = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/l.png")
image mysteriousclerk 7m = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/m.png")
image mysteriousclerk 7n = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/n.png")
image mysteriousclerk 7o = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/o.png")
image mysteriousclerk 7p = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/p.png")
image mysteriousclerk 7q = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/q.png")
image mysteriousclerk 7r = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/r.png")
image mysteriousclerk 7s = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/s.png")
image mysteriousclerk 7t = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/t.png")
image mysteriousclerk 7u = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/u.png")
image mysteriousclerk 7v = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/v.png")
image mysteriousclerk 7w = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/a2.png")
image mysteriousclerk 7x = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/aB.png")

image mysteriousclerk 6ad = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6bd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/b.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6cd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/c.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6dd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/d.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6ed = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/e.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6fd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/f.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6gd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/g.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6hd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/h.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6id = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/i.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6jd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/j.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6kd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/k.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6ld = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/l.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6md = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/m.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6nd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/n.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6od = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/o.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6pd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/p.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6qd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/q.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6rd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/r.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6sd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/s.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6td = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/t.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6ud = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/u.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6vd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/v.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6wd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/a2.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 6xd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/1r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/aB.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")

image mysteriousclerk 7ad = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/a.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7bd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/b.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7cd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/c.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7dd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/d.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7ed = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/e.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7fd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/f.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7gd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/g.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7hd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/h.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7id = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/i.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7jd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/j.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7kd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/k.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7ld = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/l.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7md = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/m.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7nd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/n.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7od = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/o.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7pd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/p.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7qd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/q.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7rd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/r.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7sd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/s.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7td = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/t.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7ud = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/u.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7vd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/v.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7wd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/a2.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")
image mysteriousclerk 7xd = im.Composite((960, 960), (0, 0), "mod_assets/images/mysteriousclerk/2r.png", (0, 0), "mod_assets/images/mysteriousclerk/4l.png", (0, 0), "mod_assets/images/mysteriousclerk/aB.png", (0, 0), "mod_assets/images/mysteriousclerk/db.png")

# Ayame School
image ayame 1 = im.Composite((960, 960), (0, 0), "mod_assets/images/ayame/1lr.png", (0, 0), "mod_assets/images/ayame/a.png")
image ayame 1a = im.Composite((960, 960), (0, 0), "mod_assets/images/ayame/1lr.png", (0, 0), "mod_assets/images/ayame/a.png")
image ayame 1b = im.Composite((960, 960), (0, 0), "mod_assets/images/ayame/1lr.png", (0, 0), "mod_assets/images/ayame/b.png")
image ayame 1c = im.Composite((960, 960), (0, 0), "mod_assets/images/ayame/1lr.png", (0, 0), "mod_assets/images/ayame/c.png")
image ayame 1d = im.Composite((960, 960), (0, 0), "mod_assets/images/ayame/1lr.png", (0, 0), "mod_assets/images/ayame/d.png")
image ayame 1e = im.Composite((960, 960), (0, 0), "mod_assets/images/ayame/1lr.png", (0, 0), "mod_assets/images/ayame/e.png")
image ayame 1f = im.Composite((960, 960), (0, 0), "mod_assets/images/ayame/1lr.png", (0, 0), "mod_assets/images/ayame/f.png")
image ayame 1g = im.Composite((960, 960), (0, 0), "mod_assets/images/ayame/1lr.png", (0, 0), "mod_assets/images/ayame/g.png")
image ayame 1h = im.Composite((960, 960), (0, 0), "mod_assets/images/ayame/1lr.png", (0, 0), "mod_assets/images/ayame/h.png")
image ayame 1i = im.Composite((960, 960), (0, 0), "mod_assets/images/ayame/1lr.png", (0, 0), "mod_assets/images/ayame/i.png")
image ayame 1j = im.Composite((960, 960), (0, 0), "mod_assets/images/ayame/1lr.png", (0, 0), "mod_assets/images/ayame/j.png")

# Gray Images
image bg residential_day_gray = im.Grayscale("bg/residential.png")
image bg club_day_gray = im.Grayscale("bg/club.png")
image bg house_gray = im.Grayscale("bg/house.png")
image bg sayori_bedroom_gray = im.Grayscale("bg/sayori_bedroom.png")
image bg bedroom_gray = im.Grayscale("bg/bedroom.png")
image bg m_livingroom_gray = im.Grayscale("mod_assets/images/bg/m_livingroom.png")
image sayori 1g_gray = im.Grayscale("mod_assets/images/sayori/preset/1g.png")
image sayori 1r_gray = im.Grayscale("mod_assets/images/sayori/preset/1r.png")
image sayori 1x_gray = im.Grayscale("mod_assets/images/sayori/preset/1x.png")
image sayori 2j_gray = im.Grayscale("mod_assets/images/sayori/preset/2j.png")
image sayori 4p_gray = im.Grayscale("mod_assets/images/sayori/preset/4p.png")
image sayori 4r_gray = im.Grayscale("mod_assets/images/sayori/preset/4r.png")
image sayori 1ba_gray = im.Grayscale("mod_assets/images/sayori/preset/1ba.png")
image sayori 1bu_gray = im.Grayscale("mod_assets/images/sayori/preset/1bu.png")
image sayori 4bl_gray = im.Grayscale("mod_assets/images/sayori/preset/4bl.png")
image sayori 4by_gray = im.Grayscale("mod_assets/images/sayori/preset/4by.png")
image natsuki 1q_gray = im.Grayscale("mod_assets/images/natsuki/preset/1q.png")
image natsuki 5g_gray = im.Grayscale("mod_assets/images/natsuki/preset/5g.png")
image natsuki 2bj_gray = im.Grayscale("mod_assets/images/natsuki/preset/2bj.png")
image yuri 3w_gray = im.Grayscale("mod_assets/images/yuri/preset/3w.png")
image yuri 4c_gray = im.Grayscale("mod_assets/images/yuri/preset/4c.png")
image yuri 2bq_gray = im.Grayscale("mod_assets/images/yuri/preset/2bq.png")
image monika 1b_gray = im.Grayscale("mod_assets/images/monika/preset/1b.png")
image monika 1d_gray = im.Grayscale("mod_assets/images/monika/preset/1d.png")
image monika 2p_gray = im.Grayscale("mod_assets/images/monika/preset/2p.png")
image monika 3a_gray = im.Grayscale("mod_assets/images/monika/preset/3a.png")
image monika 5a_gray = im.Grayscale("monika/3a.png")
image monika 1be_gray = im.Grayscale("mod_assets/images/monika/preset/1be.png")
image monika 1bj_gray = im.Grayscale("mod_assets/images/monika/preset/1bj.png")
image monika 1bm_gray = im.Grayscale("mod_assets/images/monika/preset/1bm.png")
image monika 1bo_gray = im.Grayscale("mod_assets/images/monika/preset/1bo.png")
image monika 1bp_gray = im.Grayscale("mod_assets/images/monika/preset/1bp.png")
image monika 2bl_gray = im.Grayscale("mod_assets/images/monika/preset/2bl.png")
image monika 2bm_gray = im.Grayscale("mod_assets/images/monika/preset/2bm.png")

define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define d = DynamicCharacter('d_name', image='dadsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define mo = DynamicCharacter('mo_name', image='momsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define e = Character('Everyone', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define cl = DynamicCharacter('cl_name', image='mysteriousclerk', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define a = DynamicCharacter('a_name', image='ayame', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define _dismiss_pause = config.developer

default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None
default persistent.first_poem = None
default persistent.seen_colors_poem = None
default persistent.monika_back = None
default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None

default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"
default d_name = "Yasuhiro"
default mo_name = "Haruki"
default cl_name = "Mysterious Clerk"
default a_name = "Ayame"



default n_poemappeal = [0, 0, 0, 0, 0, 0, 0, 0, 0]
default s_poemappeal = [0, 0, 0, 0, 0, 0, 0, 0, 0]
default y_poemappeal = [0, 0, 0, 0, 0, 0, 0, 0, 0]
default m_poemappeal = [0, 0, 0, 0, 0, 0, 0, 0, 0]


default poemwinner = ['sayori', 'sayori', 'sayori']


default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False


default n_read3 = False
default y_read3 = False


default n_poemearly = False


default poemsread = 0



default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0


default m_exclusivewatched = False
default n_exclusivewatched = False
default y_exclusivewatched = False

# Mod Variables
# Persistent
default persistent.name_saves = False
default persistent.monika_change = False
default persistent.monika_credits = False
default persistent.monika_gone = False
default persistent.monika_splash_message = False
default persistent.monika_ch3_skip = False
default persistent.sayori_love = False
default persistent.ch4_preparations = "Yuri"
default persistent.dialogue_change = [False,False,False]
default persistent.ch6_task = [False,False,False]
default persistent.ch11_task = [False,False,False]
default persistent.sayori_reload_yuri = False
default persistent.sayori_reload_yuri_message = True
default persistent.sayori_yuri_bad_ending = False
default persistent.sayori_natsuki_bad_ending = False
default persistent.yuri_killing = 0
default persistent.sayori_end_early = False
default persistent.y_playday = [False,False]
default persistent.n_playday = [False,False,False,False,False,False]
default persistent.natsuki_house = [False, False, False, False]
default persistent.arc_clear = [False,False,False,False,False]
default persistent.markov_agreed = False
default persistent.did_special_event = False
default persistent.ch13_nat_date = False
default persistent.ch15_sayori_chance = False
# Local Save
default visited_sayori_sat = False
default canload_ch5b = False
default monika_appeal = [False,False,False]
default act_one_dialogue = [False,False,False]
default sayori_save = 0
default monika_will_delete = True
default m_show = False
default sayori_personality = 0
default newpoemwinner = ['sayori', 'sayori', 'sayori']
default natarcpoemwinner = ['sayori', 'sayori', 'sayori']
default sayarcpoemwinner = ['sayori', 'sayori', 'sayori']
default monarcpoemwinner = ['sayori', 'sayori', 'sayori']
default ch5_scene = "monika"
default ch5_name = "Monika"
default ch7_scene = "monika"
default ch7_name = "Monika"
default bad_choice_first = False
default sayori_no_count = 0
default ch6_no_option = True
default read_book = True
default natsuki_approval = 4
default yuri_approval = 4
default did_all_tasks = False
default needs_to_read = False
default gave_book_to_monika = False
default sayori_dumped = False
default visited_yuri_hospital = False
default natsuki_outing = False
default yuri_date = False
default natsuki_date = False
default sayori_date = False
default monika_date = False
default bob_date = False
default s_ranaway = False
default n_ranaway = False
default m_ranaway = False
default n_poemappeal2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
default s_poemappeal2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
default y_poemappeal2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
default m_poemappeal2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
default go_nat_house = [False, False]
default talkabout_natsuki_house = [False, False, False, False]
default check_whole_house = False
default check_some_house = False
default ch11_yuri_choice = "birdseed"
default ch11_yuri_store = "pet store"
default ch11_monika_talked = False
default ch11_monika_dinner = False
default ch11_read_manga = True
default ch11_did_all_tasks = False
default ch11_badpoem = False
default monika_type = 2
default ch12_outcome = 0
default ch12_natsuki_help = True
default ch12_natsuki_reluctance = 1
default ch12_haruki_tried = False
default ch12_markov_agree = False
default haruki_personality = [False,False,False]
default normal_haruki = False
default n_appealS = 0
default s_appealS = 0
default y_appealS = 0
default m_appealS = 0
default m_hairdown_poemglitch = False
default ch13poemwinner = "Sayori"
default ch13_scene = "sayori"
default ch13_name = "Sayori"
default ch13_music_type = "harmonic"
default ch13_yuri_books = False
default ch13_natsuki_books = False
default ch13_cleaneye = False
default ch14poemwinner = "Sayori"
default ch14markovikatell = False
default ch14_player_choice = True
default ch14_player_manga = 3
default ch14_twonovels_tell = False
default ch14_book_choice = "Sayori"
default ch14_natyuri_choice = ["Natsuki", "Yuri"]
default ch14_votes = [0, 0, 0, 0, 0]
default ch14_overall_choice = "Sayori"
default ch14_sayori_date_choice = False
default ch14_m_ask = False
default ch14_m_tellsayori = False
default ch15poemwinner = "Sayori"
default ch15_m_together = False
default ch15_s_together = False
default chapter_names = ["An Ordinary Day","The Literature Club","The Meeting","You Three","Before The Festival","The Festival","A New Beginning","Portrait of Markov","The Play","Familiar Face","What's Wrong?","Before the Storm","A New Play","Preparations","Bring Your Book!","A Dilemma","How Did You Do That?","???","???","???","???","???"]
default special_chapter = False
default all_sayarc_poems_monika = False
default monika_outfit = 0
default sayori_outfit = 0
# Poem Game Fix
default sInList = False
default nInList = False
default yInList = False
default mInList = False

default y_gave = False
default y_ranaway = False


default ch1_choice = "sayori"


default help_sayori = None
default help_monika = None


default ch4_scene = "yuri"
default ch4_name = "Yuri"
default sayori_confess = True


default natsuki_23 = None
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
