label ch16_main:
    python:
        persistent.ayame_deleted = None
        # Set Callback to None after Yesterday
        mo_name = "???"
        n.display_args["callback"] = None
        mc.display_args["callback"] = None
        m.display_args["callback"] = None
        s.display_args["callback"] = None
        d.display_args["callback"] = None
        narrator.display_args["callback"] = None

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
