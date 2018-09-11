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

image sayori 1ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 1bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 1bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 1bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 1be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 1bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 1bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 1bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 1bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 1bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 1bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 1bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 1bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 1bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 1bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 1bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 1bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 1br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 1bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 1bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 1bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 1bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 1bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 1bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 1by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 2ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 2bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 2bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 2bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 2be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 2bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 2bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 2bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 2bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 2bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 2bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 2bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 2bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 2bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 2bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 2bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 2bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 2br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 2bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 2bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 2bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 2bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 2bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 2bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 2by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori 3ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 3bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 3bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 3bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 3be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 3bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 3bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 3bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 3bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 3bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 3bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 3bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 3bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 3bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 3bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 3bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 3bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 3br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 3bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 3bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 3bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 3bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 3bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 3bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 3by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 4ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 4bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 4bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 4bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 4be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 4bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 4bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 4bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 4bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 4bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 4bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 4bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 4bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 4bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 4bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 4bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 4bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 4br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 4bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 4bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 4bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 4bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 4bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 4bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 4by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

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
image monika 1schoolgy = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/gy.png")

image monika 2schoolga = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/ga.png")
image monika 2schoolge = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/ge.png")
image monika 2schoolgf = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/gf.png")
image monika 2schoolgg = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/gg.png")
image monika 2schoolgh = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/gh.png")
image monika 2schoolgi = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/gi.png")
image monika 2schoolgy = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/gy.png")

image monika 3schoolga = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/ga.png")
image monika 3schoolge = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/ge.png")
image monika 3schoolgf = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/gf.png")
image monika 3schoolgg = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/gg.png")
image monika 3schoolgh = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/gh.png")
image monika 3schoolgi = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/gi.png")
image monika 3schoolgy = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/images/monika/gy.png")

image monika 4schoolga = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/ga.png")
image monika 4schoolge = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/ge.png")
image monika 4schoolgf = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/gf.png")
image monika 4schoolgg = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/gg.png")
image monika 4schoolgh = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/gh.png")
image monika 4schoolgi = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/gi.png")
image monika 4schoolgy = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/images/monika/gy.png")

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

# Casual Clothes Monika
image monika 1casual1a = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/a.png")
image monika 1casual1b = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/b.png")
image monika 1casual1c = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/c.png")
image monika 1casual1d = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/d.png")
image monika 1casual1e = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/e.png")
image monika 1casual1f = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/f.png")
image monika 1casual1g = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/g.png")
image monika 1casual1h = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/h.png")
image monika 1casual1i = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/i.png")
image monika 1casual1j = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/j.png")
image monika 1casual1k = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/k.png")
image monika 1casual1l = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/l.png")
image monika 1casual1m = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/m.png")
image monika 1casual1n = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/n.png")
image monika 1casual1o = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/o.png")
image monika 1casual1p = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/p.png")
image monika 1casual1q = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/q.png")
image monika 1casual1r = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/r.png")
image monika 1casual1s = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/s.png")
image monika 1casual1t = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/t.png")
image monika 1casual1u = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/u.png")

image monika 2casual1a = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/a.png")
image monika 2casual1b = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/b.png")
image monika 2casual1c = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/c.png")
image monika 2casual1d = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/d.png")
image monika 2casual1e = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/e.png")
image monika 2casual1f = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/f.png")
image monika 2casual1g = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/g.png")
image monika 2casual1h = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/h.png")
image monika 2casual1i = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/i.png")
image monika 2casual1j = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/j.png")
image monika 2casual1k = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/k.png")
image monika 2casual1l = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/l.png")
image monika 2casual1m = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/m.png")
image monika 2casual1n = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/n.png")
image monika 2casual1o = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/o.png")
image monika 2casual1p = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/p.png")
image monika 2casual1q = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/q.png")
image monika 2casual1r = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/r.png")
image monika 2casual1s = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/s.png")
image monika 2casual1t = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/t.png")
image monika 2casual1u = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/u.png")

image monika 3casual1a = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/a.png")
image monika 3casual1b = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/b.png")
image monika 3casual1c = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/c.png")
image monika 3casual1d = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/d.png")
image monika 3casual1e = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/e.png")
image monika 3casual1f = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/f.png")
image monika 3casual1g = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/g.png")
image monika 3casual1h = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/h.png")
image monika 3casual1i = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/i.png")
image monika 3casual1j = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/j.png")
image monika 3casual1k = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/k.png")
image monika 3casual1l = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/l.png")
image monika 3casual1m = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/m.png")
image monika 3casual1n = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/n.png")
image monika 3casual1o = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/o.png")
image monika 3casual1p = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/p.png")
image monika 3casual1q = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/q.png")
image monika 3casual1r = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "monika/r.png")
image monika 3casual1s = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/s.png")
image monika 3casual1t = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/t.png")
image monika 3casual1u = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/u.png")

image monika 4casual1a = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/a.png")
image monika 4casual1b = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/b.png")
image monika 4casual1c = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/c.png")
image monika 4casual1d = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/d.png")
image monika 4casual1e = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/e.png")
image monika 4casual1f = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/f.png")
image monika 4casual1g = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/g.png")
image monika 4casual1h = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/h.png")
image monika 4casual1i = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/i.png")
image monika 4casual1j = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/j.png")
image monika 4casual1k = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/k.png")
image monika 4casual1l = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/l.png")
image monika 4casual1m = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/m.png")
image monika 4casual1n = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/n.png")
image monika 4casual1o = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/o.png")
image monika 4casual1p = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/p.png")
image monika 4casual1q = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/q.png")
image monika 4casual1r = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "monika/r.png")
image monika 4casual1s = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/s.png")
image monika 4casual1t = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/t.png")
image monika 4casual1u = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/u.png")

image monika 5casual1a = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/3ba.png")
image monika 5casual1b = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/3bb.png")

# Markov Monika Casual
image monika 1casual1ga = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/ga.png")
image monika 1casual1ge = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/ge.png")
image monika 1casual1gf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/gf.png")
image monika 1casual1gg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/gg.png")
image monika 1casual1gi = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/gi.png")
image monika 1casual1gy = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/gy.png")

image monika 2casual1ga = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/ga.png")
image monika 2casual1ge = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/ge.png")
image monika 2casual1gf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/gf.png")
image monika 2casual1gg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/gg.png")
image monika 2casual1gi = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/gi.png")
image monika 2casual1gy = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/gy.png")

image monika 3casual1ga = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/ga.png")
image monika 3casual1ge = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/ge.png")
image monika 3casual1gf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/gf.png")
image monika 3casual1gg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/gg.png")
image monika 3casual1gi = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/gi.png")
image monika 3casual1gy = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/1br.png", (0, 0), "mod_assets/images/monika/gy.png")

image monika 4casual1ga = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/ge.png")
image monika 4casual1ge = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/ge.png")
image monika 4casual1gf = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/gf.png")
image monika 4casual1gg = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/gg.png")
image monika 4casual1gi = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/gi.png")
image monika 4casual1gy = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bl.png", (0, 0), "mod_assets/images/monika/2br.png", (0, 0), "mod_assets/images/monika/gy.png")

# Casual Clothes Monika - Hair Down
image monika 1downcasual1a = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/ha.png")
image monika 1downcasual1b = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hb.png")
image monika 1downcasual1c = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hc.png")
image monika 1downcasual1d = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hd.png")
image monika 1downcasual1e = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/he.png")
image monika 1downcasual1f = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hf.png")
image monika 1downcasual1g = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hg.png")
image monika 1downcasual1h = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hh.png")
image monika 1downcasual1i = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hi.png")
image monika 1downcasual1j = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hj.png")
image monika 1downcasual1k = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hk.png")
image monika 1downcasual1l = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hl.png")
image monika 1downcasual1m = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hm.png")
image monika 1downcasual1n = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hn.png")
image monika 1downcasual1o = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/ho.png")
image monika 1downcasual1p = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hp.png")
image monika 1downcasual1q = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hq.png")
image monika 1downcasual1r = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hr.png")
image monika 1downcasual1s = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hs.png")
image monika 1downcasual1t = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/ht.png")
image monika 1downcasual1u = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hu.png")

image monika 2downcasual1a = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/ha.png")
image monika 2downcasual1b = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hb.png")
image monika 2downcasual1c = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hc.png")
image monika 2downcasual1d = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hd.png")
image monika 2downcasual1e = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/he.png")
image monika 2downcasual1f = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hf.png")
image monika 2downcasual1g = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hg.png")
image monika 2downcasual1h = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hh.png")
image monika 2downcasual1i = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hi.png")
image monika 2downcasual1j = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hj.png")
image monika 2downcasual1k = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hk.png")
image monika 2downcasual1l = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hl.png")
image monika 2downcasual1m = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hm.png")
image monika 2downcasual1n = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hn.png")
image monika 2downcasual1o = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/ho.png")
image monika 2downcasual1p = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hp.png")
image monika 2downcasual1q = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hq.png")
image monika 2downcasual1r = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hr.png")
image monika 2downcasual1s = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hs.png")
image monika 2downcasual1t = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/ht.png")
image monika 2downcasual1u = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/1bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hu.png")

image monika 3downcasual1a = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/ha.png")
image monika 3downcasual1b = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hb.png")
image monika 3downcasual1c = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hc.png")
image monika 3downcasual1d = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hd.png")
image monika 3downcasual1e = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/he.png")
image monika 3downcasual1f = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hf.png")
image monika 3downcasual1g = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hg.png")
image monika 3downcasual1h = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hh.png")
image monika 3downcasual1i = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hi.png")
image monika 3downcasual1j = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hj.png")
image monika 3downcasual1k = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hk.png")
image monika 3downcasual1l = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hl.png")
image monika 3downcasual1m = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hm.png")
image monika 3downcasual1n = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hn.png")
image monika 3downcasual1o = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/ho.png")
image monika 3downcasual1p = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hp.png")
image monika 3downcasual1q = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hq.png")
image monika 3downcasual1r = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hr.png")
image monika 3downcasual1s = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hs.png")
image monika 3downcasual1t = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/ht.png")
image monika 3downcasual1u = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/1bhr.png", (0, 0), "mod_assets/images/monika/hu.png")

image monika 4downcasual1a = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/ha.png")
image monika 4downcasual1b = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hb.png")
image monika 4downcasual1c = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hc.png")
image monika 4downcasual1d = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hd.png")
image monika 4downcasual1e = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/he.png")
image monika 4downcasual1f = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hf.png")
image monika 4downcasual1g = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hg.png")
image monika 4downcasual1h = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hh.png")
image monika 4downcasual1i = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hi.png")
image monika 4downcasual1j = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hj.png")
image monika 4downcasual1k = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hk.png")
image monika 4downcasual1l = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hl.png")
image monika 4downcasual1m = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hm.png")
image monika 4downcasual1n = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hn.png")
image monika 4downcasual1o = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/ho.png")
image monika 4downcasual1p = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hp.png")
image monika 4downcasual1q = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hq.png")
image monika 4downcasual1r = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hr.png")
image monika 4downcasual1s = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hs.png")
image monika 4downcasual1t = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/ht.png")
image monika 4downcasual1u = im.Composite((960, 960), (0, 0), "mod_assets/images/monika/2bhl.png", (0, 0), "mod_assets/images/monika/2bhr.png", (0, 0), "mod_assets/images/monika/hu.png")

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
image monika 1ba = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downcasual1a", "True", "monika 1casual1a")
image monika 1bb = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downcasual1b", "True", "monika 1casual1b")
image monika 1bc = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downcasual1c", "True", "monika 1casual1c")
image monika 1bd = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downcasual1d", "True", "monika 1casual1d")
image monika 1be = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downcasual1e", "True", "monika 1casual1e")
image monika 1bf = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downcasual1f", "True", "monika 1casual1f")
image monika 1bg = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downcasual1g", "True", "monika 1casual1g")
image monika 1bh = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downcasual1h", "True", "monika 1casual1h")
image monika 1bi = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downcasual1i", "True", "monika 1casual1i")
image monika 1bj = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downcasual1j", "True", "monika 1casual1j")
image monika 1bk = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downcasual1k", "True", "monika 1casual1k")
image monika 1bl = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downcasual1l", "True", "monika 1casual1l")
image monika 1bm = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downcasual1m", "True", "monika 1casual1m")
image monika 1bn = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downcasual1n", "True", "monika 1casual1n")
image monika 1bo = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downcasual1o", "True", "monika 1casual1o")
image monika 1bp = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downcasual1p", "True", "monika 1casual1p")
image monika 1bq = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downcasual1q", "True", "monika 1casual1q")
image monika 1br = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downcasual1r", "True", "monika 1casual1r")
image monika 1bs = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downcasual1s", "True", "monika 1casual1s")
image monika 1bt = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downcasual1t", "True", "monika 1casual1t")
image monika 1bu = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 1downcasual1u", "True", "monika 1casual1u")

image monika 2ba = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downcasual1a", "True", "monika 2casual1a")
image monika 2bb = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downcasual1b", "True", "monika 2casual1b")
image monika 2bc = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downcasual1c", "True", "monika 2casual1c")
image monika 2bd = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downcasual1d", "True", "monika 2casual1d")
image monika 2be = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downcasual1e", "True", "monika 2casual1e")
image monika 2bf = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downcasual1f", "True", "monika 2casual1f")
image monika 2bg = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downcasual1g", "True", "monika 2casual1g")
image monika 2bh = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downcasual1h", "True", "monika 2casual1h")
image monika 2bi = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downcasual1i", "True", "monika 2casual1i")
image monika 2bj = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downcasual1j", "True", "monika 2casual1j")
image monika 2bk = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downcasual1k", "True", "monika 2casual1k")
image monika 2bl = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downcasual1l", "True", "monika 2casual1l")
image monika 2bm = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downcasual1m", "True", "monika 2casual1m")
image monika 2bn = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downcasual1n", "True", "monika 2casual1n")
image monika 2bo = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downcasual1o", "True", "monika 2casual1o")
image monika 2bp = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downcasual1p", "True", "monika 2casual1p")
image monika 2bq = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downcasual1q", "True", "monika 2casual1q")
image monika 2br = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downcasual1r", "True", "monika 2casual1r")
image monika 2bs = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downcasual1s", "True", "monika 2casual1s")
image monika 2bt = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downcasual1t", "True", "monika 2casual1t")
image monika 2bu = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 2downcasual1u", "True", "monika 2casual1u")

image monika 3ba = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downcasual1a", "True", "monika 3casual1a")
image monika 3bb = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downcasual1b", "True", "monika 3casual1b")
image monika 3bc = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downcasual1c", "True", "monika 3casual1c")
image monika 3bd = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downcasual1d", "True", "monika 3casual1d")
image monika 3be = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downcasual1e", "True", "monika 3casual1e")
image monika 3bf = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downcasual1f", "True", "monika 3casual1f")
image monika 3bg = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downcasual1g", "True", "monika 3casual1g")
image monika 3bh = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downcasual1h", "True", "monika 3casual1h")
image monika 3bi = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downcasual1i", "True", "monika 3casual1i")
image monika 3bj = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downcasual1j", "True", "monika 3casual1j")
image monika 3bk = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downcasual1k", "True", "monika 3casual1k")
image monika 3bl = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downcasual1l", "True", "monika 3casual1l")
image monika 3bm = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downcasual1m", "True", "monika 3casual1m")
image monika 3bn = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downcasual1n", "True", "monika 3casual1n")
image monika 3bo = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downcasual1o", "True", "monika 3casual1o")
image monika 3bp = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downcasual1p", "True", "monika 3casual1p")
image monika 3bq = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downcasual1q", "True", "monika 3casual1q")
image monika 3br = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downcasual1r", "True", "monika 3casual1r")
image monika 3bs = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downcasual1s", "True", "monika 3casual1s")
image monika 3bt = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downcasual1t", "True", "monika 3casual1t")
image monika 3bu = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 3downcasual1u", "True", "monika 3casual1u")

image monika 4ba = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downcasual1a", "True", "monika 4casual1a")
image monika 4bb = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downcasual1b", "True", "monika 4casual1b")
image monika 4bc = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downcasual1c", "True", "monika 4casual1c")
image monika 4bd = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downcasual1d", "True", "monika 4casual1d")
image monika 4be = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downcasual1e", "True", "monika 4casual1e")
image monika 4bf = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downcasual1f", "True", "monika 4casual1f")
image monika 4bg = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downcasual1g", "True", "monika 4casual1g")
image monika 4bh = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downcasual1h", "True", "monika 4casual1h")
image monika 4bi = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downcasual1i", "True", "monika 4casual1i")
image monika 4bj = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downcasual1j", "True", "monika 4casual1j")
image monika 4bk = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downcasual1k", "True", "monika 4casual1k")
image monika 4bl = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downcasual1l", "True", "monika 4casual1l")
image monika 4bm = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downcasual1m", "True", "monika 4casual1m")
image monika 4bn = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downcasual1n", "True", "monika 4casual1n")
image monika 4bo = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downcasual1o", "True", "monika 4casual1o")
image monika 4bp = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downcasual1p", "True", "monika 4casual1p")
image monika 4bq = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downcasual1q", "True", "monika 4casual1q")
image monika 4br = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downcasual1r", "True", "monika 4casual1r")
image monika 4bs = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downcasual1s", "True", "monika 4casual1s")
image monika 4bt = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downcasual1t", "True", "monika 4casual1t")
image monika 4bu = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 4downcasual1u", "True", "monika 4casual1u")

image monika 5ba = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 5downcasual1a", "True", "monika 5casual1a")
image monika 5bb = ConditionSwitch("monika_type == 1 and ch12_markov_agree", "monika 5downcasual1b", "True", "monika 5casual1b")

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
    "monika 1casual1gg"
    pause 0.5
    "monika 1casual1g"

image monika g4:
    "monika 1schoolgi"
    pause 0.5
    "monika 1schooli"

image monika g5:
    "monika 1casual1ge"
    pause 0.5
    "monika 1casual1e"

image monika g6:
    "monika 1casual1ga"
    pause 0.5
    "monika 1casual1a"

image monika g7:
    "monika 1schoolga"
    pause 0.5
    "monika 1schoola"

image monika g8:
    "monika 1schoolgh"
    pause 0.5
    "monika 1schoolh"

image monika g9:
    "monika 5ga"
    pause 0.5
    "monika 5a"

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
image momsuki 1 = im.Composite((960, 960), (0, 0), "mod_assets/images/momsuki/1lr.png", (0, 0), "mod_assets/images/momsuki/1a.png")
image momsuki 1a = im.Composite((960, 960), (0, 0), "mod_assets/images/momsuki/1lr.png", (0, 0), "mod_assets/images/momsuki/1a.png")
image momsuki 1b = im.Composite((960, 960), (0, 0), "mod_assets/images/momsuki/1lr.png", (0, 0), "mod_assets/images/momsuki/1b.png")
image momsuki 1c = im.Composite((960, 960), (0, 0), "mod_assets/images/momsuki/1lr.png", (0, 0), "mod_assets/images/momsuki/1c.png")
image momsuki 1d = im.Composite((960, 960), (0, 0), "mod_assets/images/momsuki/1lr.png", (0, 0), "mod_assets/images/momsuki/1d.png")
image momsuki 1e = im.Composite((960, 960), (0, 0), "mod_assets/images/momsuki/1lr.png", (0, 0), "mod_assets/images/momsuki/1e.png")
image momsuki 1f = im.Composite((960, 960), (0, 0), "mod_assets/images/momsuki/1lr.png", (0, 0), "mod_assets/images/momsuki/1f.png")
image momsuki 1g = im.Composite((960, 960), (0, 0), "mod_assets/images/momsuki/1lr.png", (0, 0), "mod_assets/images/momsuki/1g.png")
image momsuki 1h = im.Composite((960, 960), (0, 0), "mod_assets/images/momsuki/1lr.png", (0, 0), "mod_assets/images/momsuki/1h.png")
image momsuki 1i = im.Composite((960, 960), (0, 0), "mod_assets/images/momsuki/1lr.png", (0, 0), "mod_assets/images/momsuki/1i.png")

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

# Gray Images
image bg residential_day_gray = im.Grayscale("bg/residential.png")
image bg club_day_gray = im.Grayscale("bg/club.png")
image bg house_gray = im.Grayscale("bg/house.png")
image bg sayori_bedroom_gray = im.Grayscale("bg/sayori_bedroom.png")
image sayori 1ba_gray = im.Grayscale("mod_assets/images/sayori/preset/1ba.png")
image sayori 1bu_gray = im.Grayscale("mod_assets/images/sayori/preset/1bu.png")
image sayori 4p_gray = im.Grayscale("mod_assets/images/sayori/preset/4p.png")
image sayori 4bl_gray = im.Grayscale("mod_assets/images/sayori/preset/4bl.png")
image sayori 4by_gray = im.Grayscale("mod_assets/images/sayori/preset/4by.png")
image natsuki 2bj_gray = im.Grayscale("mod_assets/images/natsuki/preset/2bj.png")
image yuri 2bq_gray = im.Grayscale("mod_assets/images/yuri/preset/2bq.png")
image monika 2p_gray = im.Grayscale("mod_assets/images/monika/preset/2p.png")
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
default chapter_names = ["An Ordinary Day","The Literature Club","The Meeting","You Three","Before The Festival","The Festival","A New Beginning","Portrait of Markov","The Play","Familiar Face","What's Wrong?","Before the Storm","A New Play","Preparations","Bring Your Book!","A Dilemma","???","???","???","???","???","???"]
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
