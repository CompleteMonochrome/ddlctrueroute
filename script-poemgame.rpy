init python:
    import random


    class PoemWord:
        def __init__(self, word, sPoint, nPoint, yPoint, mPoint='0', glitch=False):
            self.word = word
            self.sPoint = sPoint
            self.nPoint = nPoint
            self.yPoint = yPoint
            self.mPoint = mPoint
            self.glitch = glitch


    POEM_DISLIKE_THRESHOLD = 29
    POEM_LIKE_THRESHOLD = 45


    full_wordlist = []
    full_wordlist_old = []
    sayori_wordlist = []
    natsuki_wordlist = []
    yuri_wordlist = []
    monika_wordlist = []

    # New Wordlist
    with renpy.file('poemwords_mod.txt') as wordfile:
        for line in wordfile:

            line = line.strip()

            if line == '' or line[0] == '#': continue


            x = line.split(',')
            # currentword = PoemWord(x[0], float(x[1]), float(x[2]), float(x[3]), float(x[4]))
            full_wordlist.append(PoemWord(x[0], float(x[1]), float(x[2]), float(x[3]), float(x[4])))
            # if currentword.sPoint >= 3:
            #     sayori_wordlist.append(currentword)
            # elif currentword.nPoint >= 3:
            #     natsuki_wordlist.append(currentword)
            # elif currentword.yPoint >= 3:
            #     yuri_wordlist.append(currentword)
            # elif currentword.mPoint >= 3:
            #     monika_wordlist.append(currentword)
    # Original Wordlist
    with renpy.file('poemwords.txt') as wordfile:
        for line in wordfile:
            # Ignore lines beginning with '#' and empty lines
            line = line.strip()

            if line == '' or line[0] == '#': continue

            # File format: word,sPoint,nPoint,yPoint
            x = line.split(',')
            full_wordlist_old.append(PoemWord(x[0], float(x[1]), float(x[2]), float(x[3])))


    seen_eyes_this_chapter = False
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

    def randomPauseSayori(trans, st, at):
        if st > sayoriTime:
            global sayoriTime
            sayoriTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseNatsuki(trans, st, at):
        if st > natsukiTime:
            global natsukiTime
            natsukiTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseYuri(trans, st, at):
        if st > yuriTime:
            global yuriTime
            yuriTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseMonika(trans, st, at):
        if st > monikaTime:
            global monikaTime
            monikaTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomMoveSayori(trans, st, at):
        global sayoriPos
        global sayoriOffset
        global sayoriZoom
        if st > .16:
            if sayoriPos > 0:
                sayoriPos = renpy.random.randint(-1,0)
            elif sayoriPos < 0:
                sayoriPos = renpy.random.randint(0,1)
            else:
                sayoriPos = renpy.random.randint(-1,1)
            if trans.xoffset * sayoriPos > 5: sayoriPos *= -1
            return None
        if sayoriPos > 0:
            trans.xzoom = -1
        elif sayoriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * sayoriPos
        sayoriOffset = trans.xoffset
        sayoriZoom = trans.xzoom
        return 0

    def randomMoveNatsuki(trans, st, at):
        global natsukiPos
        global natsukiOffset
        global natsukiZoom
        if st > .16:
            if natsukiPos > 0:
                natsukiPos = renpy.random.randint(-1,0)
            elif natsukiPos < 0:
                natsukiPos = renpy.random.randint(0,1)
            else:
                natsukiPos = renpy.random.randint(-1,1)
            if trans.xoffset * natsukiPos > 5: natsukiPos *= -1
            return None
        if natsukiPos > 0:
            trans.xzoom = -1
        elif natsukiPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * natsukiPos
        natsukiOffset = trans.xoffset
        natsukiZoom = trans.xzoom
        return 0

    def randomMoveYuri(trans, st, at):
        global yuriPos
        global yuriOffset
        global yuriZoom
        if st > .16:
            if yuriPos > 0:
                yuriPos = renpy.random.randint(-1,0)
            elif yuriPos < 0:
                yuriPos = renpy.random.randint(0,1)
            else:
                yuriPos = renpy.random.randint(-1,1)
            if trans.xoffset * yuriPos > 5: yuriPos *= -1
            return None
        if yuriPos > 0:
            trans.xzoom = -1
        elif yuriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * yuriPos
        yuriOffset = trans.xoffset
        yuriZoom = trans.xzoom
        return 0

    def randomMoveMonika(trans, st, at):
        global monikaPos
        global monikaOffset
        global monikaZoom
        if st > .16:
            if monikaPos > 0:
                monikaPos = renpy.random.randint(-1,0)
            elif monikaPos < 0:
                monikaPos = renpy.random.randint(0,1)
            else:
                monikaPos = renpy.random.randint(-1,1)
            if trans.xoffset * monikaPos > 5: monikaPos *= -1
            return None
        if monikaPos > 0:
            trans.xzoom = -1
        elif monikaPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * monikaPos
        monikaOffset = trans.xoffset
        monikaZoom = trans.xzoom
        return 0



label poem(transition=True,totalWords=20):
    stop music fadeout 2.0
    if persistent.playthrough == 3:
        scene bg notebook-glitch
    else:
        scene bg notebook
    show screen quick_menu
    if persistent.playthrough == 3:
        show m_sticker at sticker_mid
    else:
        # Sayori, Natsuki and Monika Normal - Set Normal Positions before Glitch shows Monika
        if persistent.playthrough == 0:
            if m_show:
                show s_sticker at sticker_4left
                show n_sticker at sticker_4midleft
                # Check if hair down Monika playthrough
                if monika_type == 1 and ch12_markov_agree and chapter > 12:
                    if random.randint(0,50) == 0 and not m_hairdown_poemglitch:
                        $ m_hairdown_poemglitch = True
                        play sound "sfx/glitch3.ogg"
                        show mh_sticker g at sticker_4right
                    else:
                        show mh_sticker at sticker_4right
                else:
                    show m_sticker at sticker_4right
            else:
                show s_sticker at sticker_left
                show n_sticker at sticker_mid
        else:
            show n_sticker at sticker_mid
        # Yuri Cut
        if persistent.playthrough == 2 and chapter == 2:
            show y_sticker_cut at sticker_right
        # Yuri Normal - Set Normal Positions before Glitch shows Monika
        else:
            if m_show:
                show y_sticker at sticker_4midright
            else:
                show y_sticker at sticker_right
        # Monika Glitch
        if persistent.playthrough == 2 and chapter == 2:
            show m_sticker at sticker_m_glitch
    if transition:
        with dissolve_scene_full
    if persistent.playthrough == 3:
        play music ghostmenu
    else:
        play music t4
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    if persistent.playthrough == 0 and chapter == 0:
        call screen dialog("It's time to write a poem!\n\nPick words you think your favorite club member\nwill like. Something good might happen with\nwhoever likes your poem the most!", ok_action=Return())
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.5
        stop sound
        hide screen tear
        show s_sticker at sticker_4left
        show n_sticker at sticker_4midleft
        show y_sticker at sticker_4midright
        show m_sticker at sticker_4right
        $ m_show = True
    python:
        poemgame_glitch = False
        played_baa = False
        progress = 1
        numWords = totalWords
        sPointTotal = 0
        nPointTotal = 0
        yPointTotal = 0
        mPointTotal = 0
        if persistent.playthrough == 0:
            wordlist = list(full_wordlist)
            # swordlist = list(sayori_wordlist)
            # nwordlist = list(natsuki_wordlist)
            # ywordlist = list(yuri_wordlist)
            # mwordlist = list(monika_wordlist)
        else:
            wordlist = list(full_wordlist_old)

        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        monikaTime = renpy.random.random() * 4 + 4
        sayoriPos = renpy.random.randint(-1,1)
        natsukiPos = renpy.random.randint(-1,1)
        yuriPos = renpy.random.randint(-1,1)
        monikaPos = renpy.random.randint(-1,1)
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        monikaOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        monikaZoom = 1





        while True:
            ystart = 160
            if persistent.playthrough == 2 and chapter == 2:
                pstring = ""
                for i in range(progress):
                    pstring += "1"
            else:
                pstring = str(progress)
            ui.text(pstring + "/" + str(numWords), style="poemgame_text", xpos=810, ypos=80, color='#000')
            sInList = False
            nInList = False
            yInList = False
            mInList = False
            for j in range(2):
                if j == 0: x = 440
                else: x = 680
                ui.vbox()
                for i in range(5):
                    if persistent.playthrough == 3:
                        s = list("Monika")
                        for k in range(6):
                            if random.randint(0, 4) == 0:
                                s[k] = ' '
                            elif random.randint(0, 4) == 0:
                                s[k] = random.choice(nonunicode)
                        word = PoemWord("".join(s), 0, 0, 0, 0, False)
                    elif persistent.playthrough == 2 and not poemgame_glitch and chapter >= 1 and progress < numWords and random.randint(0, 400) == 0:
                        word = PoemWord(glitchtext(80), 0, 0, 0, 0, True)
                    else:
                        if not sInList and i >= 1 and j == 1 and persistent.playthrough == 0:
                            word = random.choice([a for a in wordlist if a.sPoint >= 3])
                            # wordlist.remove(word)
                            # swordlist.remove(newword)
                            # word.word = word.word+" tests"
                            sInList = True
                        elif not nInList and i >= 2 and j == 1 and persistent.playthrough == 0:
                            word = random.choice([a for a in wordlist if a.nPoint >= 3])
                            # wordlist.remove(word)
                            # nwordlist.remove(word)
                            # word.word = word.word+" testn"
                            nInList = True
                        elif not yInList and i >= 3 and j == 1 and persistent.playthrough == 0:
                            word = random.choice([a for a in wordlist if a.yPoint >= 3])
                            # wordlist.remove(word)
                            # ywordlist.remove(word)
                            # word.word = word.word+" testy"
                            yInList = True
                        elif not mInList and i >= 4 and j == 1 and persistent.playthrough == 0:
                            word = random.choice([a for a in wordlist if a.mPoint >= 3])
                            # wordlist.remove(word)
                            # mwordlist.remove(word)
                            # word.word = word.word+" testm"
                            mInList = True
                        else:
                            word = random.choice(wordlist)
                            if word.sPoint >= 3:
                                sInList = True
                            elif word.nPoint >= 3:
                                nInList = True
                            elif word.yPoint >= 3:
                                yInList = True
                            elif word.mPoint >= 3:
                                mInList = True
                        wordlist.remove(word)
                    ui.textbutton(word.word, clicked=ui.returns(word), text_style="poemgame_text", xpos=x, ypos=i * 56 + ystart)
                ui.close()

            t = ui.interact()
            if not poemgame_glitch:
                if t.glitch:
                    poemgame_glitch = True
                    renpy.music.play(audio.t4g)
                    renpy.scene()
                    renpy.show("white")
                    renpy.show("y_sticker glitch", at_list=[sticker_glitch])
                elif persistent.playthrough != 3:
                    renpy.play(gui.activate_sound)
                    if persistent.playthrough == 0:
                        if t.sPoint >= 3:
                            renpy.show("s_sticker hop")
                        if t.nPoint >= 3:
                            renpy.show("n_sticker hop")
                        if t.yPoint >= 3:
                            renpy.show("y_sticker hop")
                        if t.mPoint >= 3:
                            if ch12_markov_agree and monika_type == 1 and chapter > 12:
                                if random.randint(0,500) == 0 and not m_hairdown_poemglitch:
                                    m_hairdown_poemglitch = True
                                    renpy.sound.play([ "<silence .72>", "sfx/glitch3.ogg" ])
                                    renpy.show("mh_sticker hopg")
                                else:
                                    renpy.show("mh_sticker hop")
                            else:
                                renpy.show("m_sticker hop")
                    else:
                        if persistent.playthrough == 2 and chapter == 2 and random.randint(0,10) == 0: renpy.show("m_sticker hop")
                        elif t.nPoint > t.yPoint: renpy.show("n_sticker hop")
                        elif persistent.playthrough == 2 and not persistent.seen_sticker and random.randint(0,100) == 0:
                            renpy.show("y_sticker hopg")
                            persistent.seen_sticker = True
                        elif persistent.playthrough == 2 and chapter == 2: renpy.show("y_sticker_cut hop")
                        else: renpy.show("y_sticker hop")
            else:
                r = random.randint(0, 10)
                if r == 0 and not played_baa:
                    renpy.play("gui/sfx/baa.ogg")
                    played_baa = True
                elif r <= 5: renpy.play(gui.activate_sound_glitch)
            sPointTotal += t.sPoint
            nPointTotal += t.nPoint
            yPointTotal += t.yPoint
            if persistent.playthrough == 0:
                mPointTotal += t.mPoint
            progress += 1
            if progress > numWords:
                break

        if persistent.playthrough == 0:

            if chapter == 1:
                exec(ch1_choice[0] + "PointTotal += 5")

            unsorted_pointlist = {"sayori": sPointTotal, "natsuki": nPointTotal, "yuri": yPointTotal, "monika": mPointTotal}
            pointlist = sorted(unsorted_pointlist, key=unsorted_pointlist.get)

            if chapter < 5:
                poemwinner[chapter] = pointlist[3]
                if poemwinner[0] and poemwinner[1] and poemwinner[2] == "monika":
                    monika_appeal[2] = True
            elif chapter >= 12:
                sayarcpoemwinner[chapter-12] = pointlist[3]
            elif chapter == 11:
                natarcpoemwinner[chapter-11] = pointlist[3]
            elif chapter > 7 and chapter < 10:
                newpoemwinner[chapter-6] = pointlist[3]
            else:
                newpoemwinner[chapter-5] = pointlist[3]

        else:
            if nPointTotal > yPointTotal: poemwinner[chapter] = "natsuki"
            else: poemwinner[chapter] = "yuri"

        if chapter < 5:
            exec(poemwinner[chapter][0] + "_appeal += 1")
        elif chapter >= 12:
            exec(sayarcpoemwinner[chapter-12][0] + "_appealS += 1")
        elif chapter == 11:
            exec(natarcpoemwinner[chapter-11][0] + "_appeal += 1")
        elif chapter > 7:
            exec(newpoemwinner[chapter-6][0] + "_appeal += 1")
        else:
            exec(newpoemwinner[chapter-5][0] + "_appeal += 1")


        if chapter >= 11:
            if sPointTotal < POEM_DISLIKE_THRESHOLD: s_poemappeal2[chapter-11] = -1
            elif sPointTotal > POEM_LIKE_THRESHOLD: s_poemappeal2[chapter-11] = 1
            if nPointTotal < POEM_DISLIKE_THRESHOLD: n_poemappeal2[chapter-11] = -1
            elif nPointTotal > POEM_LIKE_THRESHOLD: n_poemappeal2[chapter-11] = 1
            if yPointTotal < POEM_DISLIKE_THRESHOLD: y_poemappeal2[chapter-11] = -1
            elif yPointTotal > POEM_LIKE_THRESHOLD: y_poemappeal2[chapter-11] = 1
            if mPointTotal < POEM_DISLIKE_THRESHOLD: m_poemappeal2[chapter-11] = -1
            elif mPointTotal > POEM_LIKE_THRESHOLD: m_poemappeal2[chapter-11] = 1
        else:
            if sPointTotal < POEM_DISLIKE_THRESHOLD: s_poemappeal[chapter] = -1
            elif sPointTotal > POEM_LIKE_THRESHOLD: s_poemappeal[chapter] = 1
            if nPointTotal < POEM_DISLIKE_THRESHOLD: n_poemappeal[chapter] = -1
            elif nPointTotal > POEM_LIKE_THRESHOLD: n_poemappeal[chapter] = 1
            if yPointTotal < POEM_DISLIKE_THRESHOLD: y_poemappeal[chapter] = -1
            elif yPointTotal > POEM_LIKE_THRESHOLD: y_poemappeal[chapter] = 1
            if mPointTotal < POEM_DISLIKE_THRESHOLD: m_poemappeal[chapter] = -1
            elif mPointTotal > POEM_LIKE_THRESHOLD: m_poemappeal[chapter] = 1

        if chapter < 5:
            exec(poemwinner[chapter][0] + "_poemappeal[chapter] = 1")
        elif chapter >= 12:
            exec(sayarcpoemwinner[chapter-12][0] + "_poemappeal2[chapter-12] = 1")
        elif chapter == 11:
            exec(natarcpoemwinner[chapter-11][0] + "_poemappeal2[chapter-11] = 1")
        elif chapter > 7:
            exec(newpoemwinner[chapter-6][0] + "_poemappeal[chapter] = 1")
        else:
            exec(newpoemwinner[chapter-5][0] + "_poemappeal[chapter] = 1")

    if persistent.playthrough == 2 and persistent.seen_eyes == None and renpy.random.randint(0,5) == 0:
        $ seen_eyes_this_chapter = True
        $ quick_menu = False
        play sound "sfx/eyes.ogg"
        $ persistent.seen_eyes = True
        $ renpy.save_persistent()
        stop music
        scene black with None
        show bg eyes_move
        $ pause(1.2)
        hide bg eyes_move
        show bg eyes
        $ pause(0.5)
        hide bg eyes
        show bg eyes_move
        $ pause(1.25)
        hide bg eyes with None
        $ quick_menu = True
    $ config.allow_skipping = True
    $ allow_skipping = True
    $ m_hairdown_poemglitch = False
    stop music fadeout 2.0
    hide screen quick_menu
    show black as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    $ pause(1.0)
    return

image bg eyes_move:
    "images/bg/eyes.png"
    parallel:
        yoffset 720 ytile 2
        linear 0.5 yoffset 0
        repeat
    parallel:
        0.1
        choice:
            xoffset 20
            0.05
            xoffset 0
        choice:
            xoffset 0
        repeat
image bg eyes:
    "images/bg/eyes.png"

image s_sticker:
    "gui/poemgame/s_sticker_1.png"
    xoffset sayoriOffset xzoom sayoriZoom
    block:
        function randomPauseSayori
        parallel:
            sticker_move_n
        parallel:
            function randomMoveSayori
        repeat

image n_sticker:
    "gui/poemgame/n_sticker_1.png"
    xoffset natsukiOffset xzoom natsukiZoom
    block:
        function randomPauseNatsuki
        parallel:
            sticker_move_n
        parallel:
            function randomMoveNatsuki
        repeat

image y_sticker:
    "gui/poemgame/y_sticker_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image y_sticker_cut:
    "gui/poemgame/y_sticker_cut_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image m_sticker:
    "gui/poemgame/m_sticker_1.png"
    xoffset monikaOffset xzoom monikaZoom
    block:
        function randomPauseMonika
        parallel:
            sticker_move_n
        parallel:
            function randomMoveMonika
        repeat

image m_sticker_bw:
    "mod_assets/gui/poemgame/m_sticker_1.png"
    xoffset monikaOffset xzoom monikaZoom
    block:
        function randomPauseMonika
        parallel:
            sticker_move_n
        parallel:
            function randomMoveMonika
        repeat

image mh_sticker:
    "mod_assets/gui/poemgame/mh_sticker_1.png"
    xoffset monikaOffset xzoom monikaZoom
    block:
        function randomPauseMonika
        parallel:
            sticker_move_n
        parallel:
            function randomMoveMonika
        repeat

image mh_sticker g:
    "mod_assets/gui/poemgame/mh_sticker_1g.png"
    xoffset monikaOffset xzoom monikaZoom
    block:
        function randomPauseMonika
        parallel:
            sticker_move_n
        parallel:
            function randomMoveMonika
        repeat

image s_sticker hop:
    "gui/poemgame/s_sticker_2.png"
    xoffset sayoriOffset xzoom sayoriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "s_sticker"

image n_sticker hop:
    "gui/poemgame/n_sticker_2.png"
    xoffset natsukiOffset xzoom natsukiZoom
    sticker_hop
    xoffset 0 xzoom 1
    "n_sticker"

image y_sticker hop:
    "gui/poemgame/y_sticker_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image y_sticker_cut hop:
    "gui/poemgame/y_sticker_cut_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker_cut"

image y_sticker hopg:
    "gui/poemgame/y_sticker_2g.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image m_sticker hop:
    "gui/poemgame/m_sticker_2.png"
    xoffset monikaOffset xzoom monikaZoom
    sticker_hop
    xoffset 0 xzoom 1
    "m_sticker"

image m_sticker_bw hop:
    "mod_assets/gui/poemgame/m_sticker_2.png"
    xoffset monikaOffset xzoom monikaZoom
    sticker_hop
    xoffset 0 xzoom 1
    "m_sticker"

image mh_sticker hop:
    "mod_assets/gui/poemgame/mh_sticker_2.png"
    xoffset monikaOffset xzoom monikaZoom
    sticker_hop
    xoffset 0 xzoom 1
    "mh_sticker"

image mh_sticker hopg:
    "mod_assets/gui/poemgame/mh_sticker_2.png"
    xoffset monikaOffset xzoom monikaZoom
    sticker_hop
    xoffset 0 xzoom 1
    "mh_sticker g"

image y_sticker glitch:
    "gui/poemgame/y_sticker_1_broken.png"
    xoffset yuriOffset xzoom yuriZoom zoom 3.0
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat


# sticker positions
# Four Stickers
transform sticker_4left:
    xcenter 60 yalign 0.9 subpixel True

transform sticker_4midleft:
    xcenter 160 yalign 0.9 subpixel True

transform sticker_4midright:
    xcenter 260 yalign 0.9 subpixel True

transform sticker_4right:
    xcenter 360 yalign 0.9 subpixel True

#Three Stickers
transform sticker_left:
    xcenter 100 yalign 0.9 subpixel True

transform sticker_mid:
    xcenter 220 yalign 0.9 subpixel True

transform sticker_right:
    xcenter 340 yalign 0.9 subpixel True

transform sticker_glitch:
    xcenter 50 yalign 1.8 subpixel True

transform sticker_m_glitch:
    xcenter 100 yalign 1.35 subpixel True

transform sticker_move_n:
    easein_quad .08 yoffset -15
    easeout_quad .08 yoffset 0

transform sticker_hop:
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
