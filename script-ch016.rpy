label ch16_main:
    scene bg school_front
    if from_custom_start:
        hide screen tear
        $ from_custom_start = False
        $ quick_menu = True
    else:
        with dissolve_scene_full
    python:
        persistent.ayame_deleted = None
        # Set Callback to None after Yesterday
        n.display_args["callback"] = None
        mc.display_args["callback"] = None
        m.display_args["callback"] = None
        s.display_args["callback"] = None
        d.display_args["callback"] = None
        narrator.display_args["callback"] = None
        y.display_args["callback"] = None
        mo.display_args["callback"] = None
        cl.display_args["callback"] = None

    if ch15_s_together:
        "What the hell?"
        "I've got these...memories flooding into my head."
        "What...?"
        "These aren't my memories."
        "They can't be."
    return

label ch16_play_normal:
    return

label ch16_play_bad:
    return

label ch16_end:
    return

label ch16_sayoridate:
    return

label ch16_ending_good:
    return

label ch16_ending_neutral:
    return

label ch16_ending_bad:
    return

label ch16_badcatch:
    $ persistent.autoload = "ch16_badcatch"
    $ persistent.ch16_bad_ending_times += 1
    $ config.skipping = False
    $ config.allow_skipping = False
    $ renpy.save_persistent()
    $ cl.what_args["slow_abortable"] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    # Track where the player will load to
    show mask_2
    show mask_3
    show bg portraitshop_space
    show mysteriousclerk 4g zorder 2 at t11
    play music m1
    if persistent.ch16_bad_ending_times == 1:
        cl "Yeah, nice try."
        cl "You can't escape this now."
        cl "You need to listen."
    elif persistent.ch16_bad_ending_times == 2:
        cl "Look, kid."
        cl "You need to listen to all of this."
        cl "So just hear me out, okay?"
    elif persistent.ch16_bad_ending_times == 3:
        cl "For the third time."
        cl "It's not going to work."
        cl "Ugh, whatever."
    else:
        cl "Just listen."
        cl "Or you can keep quitting."
        cl "Up to you."
    cl "So let me start from where I left off."
    cl "Where was I?"
    cl "Oh, right."
    call expression "ch16_bad" + str(persistent.ch16_bad_part)
    return

label ch16_bad_1:
    $ persistent.autoload = "ch16_badcatch"
    $ persistent.ch16_bad_part = "_1"
    $ config.skipping = False
    $ config.allow_skipping = False
    $ renpy.save_persistent()
    $ cl.what_args["slow_abortable"] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    # Track where the player will load to
    show mask_2
    show mask_3
    show bg portraitshop_space
    show mysteriousclerk 4g zorder 2 at t11
    play music m1
    cl "You idiot."
    window auto
    cl "Are you kidding me?"
    cl "Do you know what you've just done?"
    cl 3e "I can't believe you freaking deleted her."
    cl "Why?"
    cl "Why would you do that?"
    cl "To what end?"
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() != player.lower():
                cl "Tell me your thought process, [currentuser]."
    cl 5b "Maybe you thought, oh she's just a new character."
    cl "She's not important, right?"
    cl "Wrong!"
    if persistent.ch15_sayori_saw_clerk or persistent.ch13_nat_date:
        cl 5b "Do you know who I am?"
        cl "You..."
        cl 5e "You should, shouldn't you?"
        if ch15_s_together:
            cl "I thought you wouldn't do anything stupid."
            cl "Especially since you had Sayori with you."
        elif natsuki_date:
            cl "You were with that Natsuki girl."
            cl "I'm sure we've met."
        else:
            cl "We didn't meet {i}here.{/i}"
            cl "But we've definitely met."
    elif persistent.did_christmas_event:
        cl 5b "You...don't know who I am, do you?"
        cl "Wait..."
        cl "...That look on your face says otherwise."
        cl "That's it."
        cl 5e "You saw me on another timeline."
        cl "Let me guess."
        cl "It was Christmas?"
    else:
        cl 5c "You have no idea who I am, do you?"
        cl "I suppose you wouldn't."
        cl "You haven't really explored this world."
    cl "Anyway, that's not really the point."
    cl "The point is you {i}freaking{/i} deleted her."
    cl "Let me repeat that."
    cl "You. Deleted. Ayame."
    cl "You're no better than what Monika originally was."
    cl "Actually, scratch that."
    cl "You're worse."
    cl "You did it for fun."
    cl "For curiousity."
    cl "And before you even try it."
    cl "No, I'm not in the characters folder."
    cl "So you can't delete me."
    label ch16_bad_2:
    $ persistent.ch16_bad_part = "_2"
    $ renpy.save_persistent()
    cl "I suppose I should explain a bit more about the person you deleted and why we're now here."
    cl "You might not have known it but..."
    cl "She was a pretty important part of Inauguration Day."
    cl "...What?"
    cl "Are you surprised?"
    cl "Did you seriously think that she was just gonna appear and not be relevant at all?"
    cl "That's a bit stupid, isn't it?"
    cl "No, she's meant to play a vital role in all of this."
    return
