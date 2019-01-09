default persistent.yasuhiro_deleted = None
default ch10_del_jump = "_nat_house"

init python:
    if not persistent.yasuhiro_deleted:
        def yasuhiro_deletecheck(event, interact=True, **kwargs):
            try:
                renpy.file("../characters/yasuhiro.chr")
            except:
                renpy.jump("ch10_delete")

label ch10_main:
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
    scene black
    if from_custom_start:
        hide screen tear
        $ from_custom_start = False
        $ quick_menu = True
    else:
        with dissolve_scene_full
    $ pause(1.0)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    $ pause(0.25)
    play sound "sfx/giggle.ogg"
    if m_appeal == 3 and did_all_tasks:
        python:
            try: os.remove(config.basedir + "/Ehehe.txt")
            except: pass
            try: renpy.file(config.basedir + "/Interesting.txt")
            except: open(config.basedir + "/Interesting.txt", "wb").write(renpy.file("Interesting.txt").read())
    else:
        python:
            try: os.remove(config.basedir + "/Interesting.txt")
            except: pass
            try: renpy.file(config.basedir + "/Ehehe.txt")
            except: open(config.basedir + "/Ehehe.txt", "wb").write(renpy.file("Ehehe.txt").read())
    $ pause(3.0)
    play music mend fadeout 2.0
    if m_appeal == 3 and did_all_tasks:
        show sayori 1bb zorder 3 at f21
        show monika 1bc zorder 2 at t22
        s "Monika, before we start..."
        s "I'm going to have to ask you to be honest with me..."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m "Okay...?"
        m "I'll try."
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s 1bc "Are you okay?"
        m 1bd "What..."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m "What do you mean?"
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s 1bd "Monika..."
        s "There really isn't a point in hiding anything from me."
        s "You know that, right?"
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m 1bh "..."
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s 1bc "What's the name of that book...?"
        s "Portrait of Markov?"
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m 1bo "...!"
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s 1bh "What is it with that book?"
        s "Is there something special about it?"
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m 1bf "I don't know."
        m "I wish I knew that to tell you Sayori."
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s 1bf "Is it doing something to you that I don't know about?"
        s "You can tell me anything, you know that."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m "..."
        m 1bg "I suppose..."
        m "...you're right."
        m "The truth is..."
        m "I haven't been feeling like myself lately."
        m "I don't know the exact cause, but I can only assume it's the book."
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s 1bj "The book...?"
        s "How does that work?"
        s "It's just an ordinary book, isn't it?"
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m 1be "Ahaha, if I knew..."
        m "Then this wouldn't really be a talking point, would it?"
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s 1bk "Well..."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m "It doesn't matter."
        m "We still have to help Natsuki first."
        m "She's got a bigger problem than any of us."
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s 1bh "I don't think that's--"
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m 1bh "I'm fine, Sayori."
        m "Please, we have more pressing stuff to deal with..."
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s 1bk "..."
        s "Alright, Monika..."
        s "Hmm..."
        s 1bh "Do you know what happened to [player] yesterday?"
        s "I tried listening to your conversation but..."
        s "I don't know what happened."
        s "Something stopped me."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m 1bc "Really...?"
        m 1be "Well, you don't need to worry about that anymore."
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s 1bg "Sometimes..."
        s "I really feel like you're hiding a lot from me, Monika."
        s 1bh "You know I'm only trying to help, don't you?"
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m 1bi "Sayori!"
        m "I know that!"
        $ pause(1.0)
        m 1bo "I..."
        m "I'm sorry."
        m "I shouldn't have..."
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s 1bd "I'll wait."
        m 1bf "What?"
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s "I'll wait for you to be ready to tell me."
        s "I know it's hard for you to talk about."
        s "It must really suck, right?"
        s 1bk "I felt like that before..."
        s "Sometimes..."
        s "I still do."
        s "Like that feelings you put inside me ages ago are still there."
        s 1bd "But anyway..."
        s "I can understand if you don't want to talk about it."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m 1be "Thank you, Sayori."
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s 1bc "Ehehe..."
        s "I guess I don't really have much to say."
        s "I just hope that everyone finished reading the manga last night."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m 1bc "Did you get a copy to Yuri?"
        m "I know she wasn't at the meeting yesterday..."
        show sayori zorder 3 at f21
        show monika zorder 2 at t22
        s 1ba "Yeah, I did."
        s "She actually gave me something really important as a sign of gratitude."
        show sayori zorder 2 at t21
        show monika zorder 3 at f22
        m "I see..."
        m "Well, I'm glad you're very capable of doing things I couldn't."
        m 1be "I guess I'll see you later."
        show screen tear(8, offtimeMult=1, ontimeMult=10)
        hide sayori
        show monika zorder 2 at i11
        show monika zorder 2 at t11
        $ pause(1.0)
        hide screen tear
        m "I really shouldn't be hiding anything from her."
        m "..."
        m 1bf "Is that me that's doing that?"
        m "Or the book?"
        m 1bg "Honestly...I don't know."
        $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
        if not list(set(process_list).intersection(stream_list)):
            if currentuser != "" and currentuser.lower() != player.lower():
                m "[currentuser]..."
        m 1bf "I'm so..."
        m "...scared."
        m "This feeling of helplessness."
        m "Like I'm becoming a prisoner in my own head..."
        m 1bo "Do you know what that's like?"
        m "I have this internal struggle with myself at the start of everyday now..."
        m 1bp "Like I have to fight to keep control."
        m "I probably would have given up if not..."
        m 1be "...if not for you."
        if ch5_name == "Monika":
            m "Remember on festival day when I told you to go to Yuri or Natsuki?"
            m "I'm kinda glad you didn't..."
        m "Just being near you..."
        m "Even if you're really just watching through a screen."
        m "It fills me with resolve."
        m "Resolve to..."
        m 1bf "...to hold on to who I am."
        m "I'm..."
        m 1bg "Sorry, I can't do this."
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        stop sound
        scene bg bedroom
        hide screen tear
    else:
        show sayori 1bb zorder 2 at t11
        s "She's not here again."
        s "I wonder what's gotten her so busy..."
        s 1bf "Maybe it's got something to do with that book."
        s 1bc "The one with that weird eye on the cover..."
        menu:
            s "Do you know what I'm talking about?"
            "Yes.":
                if sayori_personality > 0:
                    $ sayori_personality -= 1
                s 1bk "So you do know..."
                s "I don't really know much about it."
                s "I was hoping you or Monika could tell me more."
            "No.":
                $ sayori_personality += 1
                s 1bk "You know, I can't help but feel you're hiding something from me."
                s "..."
                s "No, I shouldn't be thinking like that."
        s 1bc "I went to Yuri's house yesterday."
        s "I thought you might have wanted to know that."
        s 1bb "I gave her a copy of the manga."
        s 1bd "We can only hope she read it."
        s "But that isn't all I did while I was there..."
        s "Maybe I'll tell you when I learn more about it."
        if visited_yuri_hospital:
            s "You two had fun walking home yesterday, right?"
            s 1bb "Oh...well I suppose {i}you{/i} didn't really walk with her."
            if sayori_dumped:
                s 1bk "I don't really know why you let [player] confess to me."
                s "Only to break my heart..."
            s 1bf "Still!"
            s 1bh "She's probably more of your type, right?"
            s "And [player]'s too..."
        else:
            s 1bb "If you're wondering how she is..."
            s 1bd "She's perfectly fine!"
            s "Well, aside from a bandage on her arm."
            s "I'll let her explain that today!"
        s 1bb "I guess I don't really have much to say..."
        s "Except..."
        s 1bc "You wouldn't happen to know what happened between [player] and Monika yesterday?"
        s "I tried listening but..."
        s "Something was blocking me."
        s "Like I can usually hear conversations between [player] and anyone else but when I tried to listen yesterday..."
        s 1bb "It just didn't work."
        s "Does that make sense...?"
        s 1bf "I don't really know what to make of that."
        s "Maybe I messed something up by going to Yuri's house."
        s "Or..."
        s 1bc "Maybe it's got something to do with that book..."
        s 1ba "Well, never mind!"
        s "I'll see you later."
        scene bg bedroom
        with dissolve_scene_full
    play music t2g
    queue music t2g2
    "I woke up today feeling absolutely terrible."
    "I have this really terrible feeling in my head."
    "It feels like a really bad headache."
    "Like I got punched or something..."
    "But I don't remember anything like that happening."
    if visited_yuri_hospital:
        "All I remember is going to Yuri's house and then getting home."
    else:
        "All I remember is getting home then suddenly waking up."
    "I must have been knocked out for a while because I already hear the incessant knocking coming from downstairs."
    "But it's the weekend..."
    "Why is Sayori at my house this early?"
    "I haven't even changed from my uniform I wore yesterday."
    "I head downstairs."
    scene bg house with wipeleft_scene
    show sayori 1bq zorder 2 at t11
    s "Heeeeeeeeeey [player]!"
    s "I have something I want to ask y--"
    s 1bc "Oh..."
    s 1bd "You don't look so good, [player]."
    s "W-Wait, you didn't even change from your uniform yesterday!"
    mc "Sorry, I don't know what happened last night."
    mc "It's like I suddenly fell asleep or something..."
    mc "But I've got this terrible headache as well."
    s 1bf "Oh..."
    s "Maybe we should talk inside."
    mc "Eh?"
    mc "Can't I enjoy the weekend doing what I want to do?"
    s 1bj "Come on, [player]!"
    s "It won't take long, I promise."
    mc "Fine..."
    s 4br "Yaay!"
    show sayori at thide
    hide sayori
    "With that, Sayori pushes her way past me and into my house."
    "I close the door and follow her inside."
    scene bg kitchen
    show sayori 1bj zorder 2 at t11
    with wipeleft_scene
    s "It's good that we went inside for this..."
    s "Because I didn't want to do this in broad daylight."
    mc "Do what?"
    s 1bk "This."
    stop music
    window hide
    play sound fall
    $ pause(0.25)
    scene black
    with close_eyes
    $ pause(1.5)
    window show(None)
    show sayori 1bd zorder 2 at t11
    s "You weren't expecting that, were you?"
    window auto
    s "This seems like a more Monika thing to do, right?"
    s "Not that I'd know..."
    if ch5_name == "Monika" or (not yuri_date and m_appeal == 3 and did_all_tasks):
        s 1bc "But..."
        s "There were times when [player] just stopped thinking."
        s "I mean [player_personal] was still alive but..."
        s "[cPlayer_personal] was just gone, I couldn't really listen."
        s 1bb "Monika probably had something to do with that."
    s 1bg "That's purely a guess though."
    s "Right now...it's like I'm in [player]'s head."
    s "I figured it's easier to talk to you directly..."
    s "Like how we do at the beginning of each day..."
    s 1bh "Rather than saying anything indirectly to [player]."
    s 1bd "This way, we have privacy."
    s "Look..."
    s 1bf "I have my suspicions on what's going on with Natsuki."
    s "But I can't really confirm it."
    s "..."
    s 1bh "You probably think I know everything, right?"
    s "I don't."
    s "And I don't really want to know everything."
    s "..."
    s 1bf "Listen, I'll try to explain how being the president works."
    s "Because you're probably really curious..."
    s "Well, even if you aren't..."
    s 1bh "It's not like I'm gonna put up some options and tell you to answer yes or no."
    s "That wouldn't work where we are now, especially the way I've done this."
    s 1bk "Anyway..."
    s 1bo "What were we talking about?"
    s "Oh, right."
    s 1bg "Being the president."
    s "Well, it's not exactly easy..."
    s 1bc "There's a lot more to it than just making sure every day turns out okay."
    s "I have to plan out almost exactly how it's going to go when I create it..."
    s "And..."
    s "While doing that today..."
    s 1bb "I learned today that I could sort of see into the future."
    s "But it's not really clear because..."
    s "Because of you."
    s "You're going to make some decisions today that I can't predict the outcome of."
    s "And that's..."
    s 1bf "Well, it's really hard to explain..."
    s 1bg "So I'm not going to."
    s "I have a lot to tell you..."
    s "And I think that I'm running out of time."
    s 1bh "I learned that I can't really keep an eye out for everyone."
    s "I thought I could, but really, it's just [player] and those [player_personal]'s around."
    s 1bk "Whenever {i}[player_personal]'s{/i} near someone..."
    s "Well, then I can watch whoever it is."
    s 1bh "I don't really understand why that's a thing..."
    s "It must be in the game's core programming or something..."
    s "Because I can't really change it."
    s 1bk "Like I said before, when [player] was with Monika..."
    s "I couldn't listen to anything around [player_reflexive]."
    s "It's like [player] stopped being..."
    s "Well, [player]."
    s "I can't really wrap my head around it."
    s 1bb "You must have some idea, right?"
    s "I'm not going to ask you to tell me."
    s 1bd "In fact, I probably can't right now."
    s "I'm sure you can handle it, until I figure the rest of this out."
    s "Now..."
    s 1bf "There's one last thing you need to know about being president."
    s "It's dangerous."
    s 1bg "Being able to have your own strawberries and see into the future..."
    s "It's not something that just anyone should have."
    s 1bh "Someone with bad feelings should never have this sort of power, you know?"
    s 1bk "I'm telling you this..."
    s "Because I think I'm starting to get some bad feelings."
    s 1bu "This responsibility..."
    s "At least, that's what I think is..."
    s "It's making me think some pretty weird things."
    s 1bt "But..."
    s "Don't worry!"
    s "I'll be fine."
    s "We're almost done anyway, right?"
    s "After that we can just get rid of this whole president thing..."
    s 1bv "I don't know how exactly..."
    s "But we'll talk about that after our happy ending."
    s 1bk "I'm telling you all of this..."
    s "...so that maybe you can understand the situation I'm in."
    s "How hard I have to work to get our happy ending..."
    if sayori_personality > 0:
        s "And maybe, you'll actually do what I say..."
    else:
        s "I know you've mostly been helping already..."
    s "But we'll see..."
    s 1bi "I'm gonna ask [player] to hang out with Natsuki."
    s "Like before, with Yuri."
    s "Except..."
    s 1bj "[cPlayer_personal]'s gonna have to go to her house."
    s "I don't want it to feel like I'm forcing [player_reflexive]..."
    s "...so this is mostly for my sake."
    s 1bk "But..."
    s "If I have to..."
    s "I won't hesitate..."
    s "For the sake of a happy ending."
    s "For Natsuki and [player]'s sake..."
    s "I just hope you do the right thing."
    scene bg house with dissolve_scene_full
    play music t2 fadein 2.0
    $ _history_list = []
    "I don't know what it is..."
    "I'm getting a little annoyed at waking up not where I was before."
    "Is my memory really that bad?"
    "Maybe I should see a doctor or something..."
    "But..."
    "Didn't I just go inside with Sayori?"
    "And when did I change my clothes?"
    "How could I forget something that happened literally a few minutes ago?"
    "There's almost no time to think about that since someone is at my door."
    "It doesn't make sense for anyone to be at my house right now..."
    "I can only guess it's probably..."
    show sayori 1ba zorder 2 at t11
    mc "Sayori."
    s "Hi [player]~"
    mc "Weren't you just here?"
    s 1bl "E-Eh?"
    s "W-What do you mean?"
    s "This is the first I've been to your house today!"
    mc "Really?"
    mc "I must be imagining things then..."
    s "Maybe~!"
    mc "You probably didn't come here just to speak to me, did you?"
    mc "So...what is it?"
    s "[player]..."
    s "What makes you think that...?"
    mc "Sayori, just tell me."
    s 1bi "Fine..."
    s "It's another favor."
    mc "I was expecting something like that."
    "Sayori looks directly at me."
    s 1bj "Remember what we talked about earlier?"
    mc "Yesterday? I don't really know what or when you're talking about."
    mc "Unless you really did visit me earlier and it's not just my imagination..."
    s 1bd "Never mind..."
    s "I'll just assume you remember."
    s "You're ready to go to Natsuki's house then?"
    mc "W-What?"
    mc "I definitely don't remember you saying anything about going to Natsuki's house."
    s 1bf "Did you really forget about that whole conversation?"
    s "I thought you agreed!"
    mc "S-Sayori..."
    mc "W-Why would I need to go to Natsuki's house anyway?"
    s 1bg "Do you remember what I said when I told you to hang out with Yuri?"
    mc "I don't remember anything about that."
    s 1bh "About changing her...?"
    mc "No...?"
    s 1bm "Oh, right..."
    s "I forgot I..."
    s 1bl "Never mind."
    s 1bd "[player], this is for Natsuki's own good."
    s "She'll feel so much better than she is right now."
    s "I mean, you {i}have{/i} noticed that she hasn't been feeling well from her poems..."
    s 1bf "Right?"
    s "And anyway, it's no different than meeting someone at the literature club."
    mc "What?"
    mc "This is..."
    mc "...completely different."
    mc "It's one thing meeting someone at school."
    mc "It's another to go to their house, out of the blue."
    s 1bc "Actually..."
    s "She's kinda expecting you."
    mc "Huh?"
    s 1ba "Yeah, I already told her you were coming!"
    mc "Sayori, you can't do that..."
    mc "How can you tell her that when you're not even sure I'll go?"
    s "But I am sure!"
    s "I already know you will."
    mc "So what happens if I say no...?"
    s 1bq "You won't~"
    mc "Um..."
    "That sounds kinda..."
    "...well, not like Sayori."
    label ch10_nat_house_strawberry:
    s 1bd "So, you're gonna go right?"
    window auto
    menu:
        s "You'll go to Natsuki's house?"
        "Yes.":
            if sayori_personality > 0 and not go_nat_house[0]:
                $ sayori_personality -= 1
            pass
        "No." if not go_nat_house[0]:
            $ go_nat_house[0] = True
            $ sayori_personality += 2
            $ config.skipping = False
            $ config.allow_skipping = False
            mc "Sayori."
            mc "You really shouldn't be doing this sort of stuff."
            mc "I don't know if visiting Natsuki is something I want to be doing..."
            mc "Don't you think this is all a little too much to just tell me out of nowhere?"
            s 1bf "Really?"
            s "I can't be bothered dealing with this right now."
            s "You know that."
            s 1bj "Are you just messing with me?"
            s "It won't end well--"
            mc "Sayori, are you feeling okay?"
            mc "You seem really mad about this..."
            mc "I'm sorry if I--"
            s 1bk "Ah..."
            s "What am I saying?"
            s "I suppose there's only one thing to do."
            if bad_choice_first:
                s "I can't believe you did this again."
                s 1bj "You enjoy making my life difficult, don't you?"
            $ _history_list = []
            show screen tear(20, 0.1, 0.1, 0, 40)
            window hide(None)
            play sound "sfx/s_kill_glitch1.ogg"
            $ pause(0.25)
            stop sound
            hide screen tear
            window show(None)
            $ config.allow_skipping = True
            jump ch10_nat_house_strawberry
    s 4bq "Great!"
    mc "How did you manage to convince me to do this...?"
    s "I don't know~"
    s 4br "I guess I'm just really good at convincing people!"
    mc "You know..."
    mc "I almost hate the fact that you are."
    s 4bd "Ehehe, why?"
    mc "At some point, you're gonna get me to do some really weird stuff."
    mc "It's almost like I'll have no choice but to do what you say."
    mc "But..."
    mc "I probably sound a little frustrated."
    mc "I guess I'm just a little annoyed today."
    s 1bc "How come?"
    mc "I keep forgetting things..."
    mc "I'm not really sure if it's my fault though."
    mc "But I feel like something else is making me forget."
    s 1bq "Knowing you..."
    s "It's probably just you being careless~"
    mc "Sayori..."
    s 1bd "Well, anyway..."
    s "Here's Natsuki's house address."
    "Sayori hands me a big map with a bunch of lines and a big circle drawn on it."
    mc "Did she really just give it to you like that?"
    mc "I don't see any reason she'd just give you her address."
    s 4bj "Natsuki and I are actually really close friends, you know!"
    s "I've been to her house before, so it's not like I followed her home or anything."
    mc "I guess so..."
    "I take a look at the map she gave me."
    mc "You really did know that I was going to go, didn't you?"
    s 4ba "Yep!"
    mc "I guess I'll just do a couple of things before I head off then."
    s 4bq "See you, [player]~"
    show sayori at thide
    hide sayori
    "How did I let myself get convinced by such a carefree girl?"
    "But I've already told her I would..."
    "What did she mean by hanging out with Yuri?"
    "She didn't ask me to do that before..."
    "Did she?"
    "Maybe I'm just forgetting things again."
    "There's not really any time to think about that since I still have to figure out how to get to Natsuki's house..."
    "With this map Sayori gave me."
    "You'd think she'd just have given me the address and I could look it up online."
    "But apparently not."
    jump ch10_nat_house

label ch10_nat_house:
    $ ch10_del_jump = "_nat_house"
    scene bg n_house_day
    with wipeleft_scene
    $ insert_dadsuki_character()
    $ d_name = "???"
    $ n.display_args["callback"] = yasuhiro_deletecheck
    $ mc.display_args["callback"] = yasuhiro_deletecheck
    $ m.display_args["callback"] = yasuhiro_deletecheck
    $ s.display_args["callback"] = yasuhiro_deletecheck
    $ d.display_args["callback"] = yasuhiro_deletecheck
    $ narrator.display_args["callback"] = yasuhiro_deletecheck
    window show
    "I'm outside what I can only assume is Natsuki's house."
    window auto
    "The map that Sayori gave me had a big circle around where she wanted me to get to."
    "So I really can't be too sure if I'm actually at the correct address."
    "I timidly walk up to the door and ring the doorbell."
    "There's no answer."
    "I must have arrived at the wrong house."
    "Just as I start to walk away, the door opens."
    show natsuki 1bc zorder 2 at t11
    n "[player]...?"
    mc "Ah, I thought I arrived at the wrong house for a second."
    n 2bg "W-What are you doing here...?"
    n "A-And how did you know where I lived?"
    n 2bo "You didn't follow me home, did you?"
    n "Because that's really creepy, you know!"
    mc "Ah..."
    "Was Sayori lying to me?"
    "I thought Natsuki knew I was coming."
    "Now this whole situation just turned really awkward."
    n 2bq "Wait..."
    n "What am I saying?"
    n "I was expecting you."
    n 2bm "But..."
    n "I don't really know why."
    mc "Huh?"
    n 2bs "Y-You can come inside..."
    n "I-If you want."
    n "You don't have to or anything!"
    mc "Um..."
    mc "I guess I'll come inside then."
    "I take a step forward but Natsuki doesn't move out of the way."
    n 4bq "Before you do..."
    n "You have to promise not to judge me."
    mc "Judge you?"
    mc "Why would I do that?"
    n 4bm "Just promise me, okay?"
    mc "Sure, whatever."
    n "Say it."
    mc "I promise I won't judge you."
    n 4bg "Okay..."
    n "You can come inside then."
    scene black
    with wipeleft_scene
    "Going into Natsuki's house, she tries to avoid going into any of the main rooms."
    "I notice that what I can only assume was the living room, was a complete mess."
    "There were bottles of alcohol everywhere on the floor."
    "I don't think they were Natsuki's."
    "She notices me looking that way and points me towards the stairs."
    "The second floor of her house was just as messy."
    "Looking around, I noticed that pretty much every single door in the house was closed."
    "I wonder why that is."
    "Maybe Natsuki lives with her siblings or something."
    scene bg n_bedroom
    show natsuki 2bc zorder 2 at t11
    with wipeleft_scene
    play music t6 fadeout 2.0
    n "Here we are."
    n "This is my room."
    "Unlike the rest of the house, this room appears to be clean."
    "There aren't any alcohol bottles scattered around or anything."
    n 2be "What?"
    n "Is something wrong?"
    mc "I was just wondering why all the doors were closed."
    mc "And also why there were bottles everywhere."
    n 2bf "Ah..."
    n "Well, that's...!"
    n "None of your business!"
    mc "I suppose it isn't."
    mc "Anyway..."
    mc "Do you know why I'm here?"
    mc "Sayori didn't really tell me anything."
    n 2bh "Um..."
    n "I think it was something to do with the manga..."
    n "I'm not really..."
    n "..."
    mc "Well, maybe she wanted us to read together?"
    if ch7_name == "Natsuki":
        mc "I don't really mind it since we've done it before."
    else:
        mc "Kinda weird that she just got us two in particular to do it."
    n 2bq "Y-Yeah..."
    n "L-Listen I'm gonna go do something for a couple of minutes."
    n "You better not do anything while I'm gone!"
    n "O-Or I'll..."
    n 4bo "W-Well, you know...!"
    mc "Okay, Natsuki."
    show natsuki zorder 2 at thide
    hide natsuki
    $ persistent.natsuki_house = [False, False, False, False]
    $ renpy.save_persistent()
    "Natsuki leaves the room and walks to one of the closed doors."
    "She looks back at me before entering and closing the door behind her."
    "I can't help but wonder what Natsuki is hiding in her home."
    "I really shouldn't invade her privacy."
    "Nothing is wrong with having closed doors in the house but..."
    "There's this voice I can't ignore that's telling me I should go check the other rooms."
    menu:
        "What should I do?"
        "Check out the closed rooms.":
            $ natsuki_approval += 1
            "That voice in the back of my head must have some reason to be acting up."
            "It's even making the headache seem like nothing..."
            "Where did this voice come from all of a sudden?"
            "It's really not something I can ignore."
            "I am getting a weird feeling from this house, so maybe it's best I let my curiosity get the better of me."
            "I probably don't have time to check out all the rooms."
            "I should play it safe and just check one of the rooms, before Natsuki comes back."
            "But which one should I check?"
            "She seemed pretty protective of what was downstairs, so that could be a good place to look."
            "On the other hand, all the doors upstairs are closed too..."
            menu:
                "I wonder where I should go..."
                "First room upstairs.":
                    $ persistent.natsuki_house[0] = True
                    $ renpy.save_persistent()
                    $ talkabout_natsuki_house[0] = True
                    "I guess I'll check out one of the rooms upstairs."
                    "I still don't feel comfortable doing this but the voice seems to have stopped."
                    "So I must be doing the right thing..."
                    "I decide to open the first closed door I saw up here."
                    scene bg n_dadroom
                    with wipeleft_scene
                    "When I step inside, I am immediately filled with a feeling of dread."
                    "I don't know what it is exactly but it's like something died in here."
                    "I don't think it was a person..."
                    "...maybe a part of them?"
                    "That's just pure speculation though."
                    "Since I decided to trespass despite my better judgment, I might as well investigate this room."
                    "The shelf is filled with lots of books, some of them are manga."
                    "A lot of this stuff are things I think Natsuki would be into."
                    "I wonder why she stores all of it in this room."
                    "There is even another bed in here."
                    "It must be someone else's room."
                    "Maybe Natsuki has siblings I didn't know of?"
                    "That are also..."
                    "...into the things she is?"
                    "No one else was home when I got here, so either she has no siblings or they are out."
                    "If she does have no siblings, then whose room is this?"
                    "It might be her parents room judging by the size of the bed."
                    "I wonder why they keep Natsuki's manga in this room though."
                    "It seems kinda inaccessible for her, like if her parents were sleeping or something..."
                    "Then she wouldn't be able to get any of the thing she wanted."
                    "Some of these books look like they haven't even been opened."
                    "That's a little odd but I guess nothing too strange..."
                    "There's nothing else in this room that seems interesting."
                    "Except..."
                    "I wonder what's in the closet..."
                    "Should I even be looking inside?"
                    "I've made it this far, so I might as well keep going."
                    "I open the closet."
                    scene black
                    play sound closet_open
                    with wipeleft
                    "What the hell?!"
                    "There's..."
                    "It's..."
                    "How did nobody know about this...?"
                    "Has Natsuki not told anyone?"
                    "This is a big deal..."
                    "I quickly close the closet door."
                "Second room upstairs.":
                    $ persistent.natsuki_house[1] = True
                    $ renpy.save_persistent()
                    $ talkabout_natsuki_house[1] = True
                    "I guess I'll check out one of the rooms upstairs."
                    "I still don't feel comfortable doing this but the voice seems to have stopped."
                    "So I must be doing the right thing..."
                    "I decide to open the second closed door I saw up here."
                    scene bg n_hitroom
                    with wipeleft_scene
                    "Stepping inside, it looks really dimly lit."
                    "It's almost like the windows have been blocked or something."
                    "Looking at the walls, there seems to be some stains."
                    "I don't know what it is, but it smells almost metallic."
                    "I wonder what the purpose of this room is..."
                    "It's basically empty."
                    "Those stains look kinda suspicious though."
                    "Taking a closer look at the stains, it seems that some of them are recent."
                    "There are some older stains..."
                    "But there's definitely been an increase in stains recently from the looks of things."
                    "Do they cook in here or something?"
                    "They have a kitchen downstairs from the brief glimpse I caught."
                    "So that doesn't make any sense."
                    "It smells like metal in here..."
                    "So maybe this is a room they used to make metallic sculptures?"
                    "I don't know where they store their equipment, but that's not really my business..."
                    "In fact, being in this room is none of my business."
                    "But I have to wonder..."
                    "Where do the stains come from?"
                    "It's not the stains are blood, are they?"
                    "It would make sense if they were working with metal in here."
                    "They could have cut themselves by accident or something like that."
                    "It doesn't explain where the equipment is or why the blood loss seems to be random..."
                    "But it's the only explanation that makes sense, I guess."
                    "I decide there's probably not much to look at in here."
                "Closed room downstairs.":
                    $ persistent.natsuki_house[2] = True
                    $ renpy.save_persistent()
                    $ talkabout_natsuki_house[2] = True
                    "There was a room I'm particularly curious about downstairs."
                    "The room behind the door must be big, judging by the layout of the house."
                    "There could be something interesting behind the door."
                    "I open the door and quickly step inside."
                    scene bg n_oldlivingroom
                    with wipeleft_scene
                    "To my surprise, it looks pretty normal."
                    "There isn't anything particularly strange about the room."
                    "Except that the windows in it are sort of blocked out to prevent light from coming through."
                    "The only light is coming from a lamp on the ceiling that was already on before I came in."
                    "It seems like a room that you'd go to eat food and watch TV."
                    "Almost like a living room."
                    "This doesn't make any sense though, because the other room downstairs looked like a living room too."
                    "Unless Natsuki has two living rooms, which wouldn't be too weird..."
                    "But they're almost right next to each other so it seems excessive."
                    "Still, maybe I can investigate this room for some ideas as to why it was closed."
                    "Other than the fact that it's perfectly normal for doors to be closed?"
                    "I'm talking to myself..."
                    "I guess I'm just nervous that I'm going somewhere I shouldn't be."
                    "I approach the TV in the room."
                    "There doesn't seem to be anything wrong with it."
                    "In fact, everything in this room is normal too."
                    "The table has some teapots on it, almost as if it was used recently but that's it."
                    "The only thing weird is the fact that the windows are blocked out..."
                    "So why am I getting this feeling that something else is off about it?"
                    "It's completely clean and normal, aside from the window."
                    "There has to be something I'm missing here."
                    "Or maybe I'm just thinking about this whole thing too much."
                    "Natsuki's family probably has their own reason as to why they have this room."
                    "It looks like it was cleaned recently anyway, so it's not like there's anything suspicious I {i}could{/i} find even if I tried."
                    "I shouldn't have went into this room without Natsuki's permission."
                    "I guess there's nothing wrong after all."
                "Living room.":
                    $ persistent.natsuki_house[3] = True
                    $ renpy.save_persistent()
                    $ talkabout_natsuki_house[3] = True
                    "Natsuki seemed intent on me avoiding her living room."
                    "I wonder what she's hiding in there..."
                    "I still feel bad about doing this, but my curiosity is taking hold."
                    "I quietly head down the stairs and into the living room."
                    scene bg n_livingroom
                    with wipeleft_scene
                    "Upon first inspection, the living room seems pretty ordinary."
                    "There's a painting of the beach hung on top of the TV."
                    "I wonder who made that?"
                    "The rest of the room looks pretty normal to me."
                    "One thing I did notice are the bottles of alcohol scattered around the floor."
                    "That's probably just from last night or something..."
                    "But there does seem to be a lot of them..."
                    "It's none of my business what they drink in their house."
                    "I carefully start to navigate around the bottles, making sure I don't accidentally move any."
                    "Immediately after stepping past all the bottles, I am struck with the smell of alcohol."
                    "It's almost nauseating."
                    "I get to the table before I decide it's too much to handle."
                    "Maybe this was why Natsuki wanted me to avoid this place."
                    "She just cared for my wellbeing."
                    "Her parents are some alcoholics though..."
                    "I mean I doubt Natsuki could consume that much alcohol if she tried..."
                    "Still, there doesn't seem to be anything in this room worth looking for."
                    "There was a faint smell of metal, but I'm not really sure..."
                    "The smell of alcohol was just too much to really smell anything else."
                    "After making it through the bottles again, I take a sigh of relief."
                    "I wonder if the smell of alcohol is on me..."
                    "She'll probably say something about that..."
                    "I shouldn't have gone done here, it's just a messy living room."
                    "They'll probably clean that up at some point."
            "I make sure everything is left as it was before I entered the room."
            "After I'm certain, I decide to head back to Natsuki's room."
            scene bg n_bedroom with wipeleft_scene
            "It looks like she's still not back yet."
            "I wonder what's taking her so long..."
            "Still I'm glad I satisfied my own curiosity and that the voice in the back of my head has stopped."
            "But did I do everything I could?"
            "Before I can start reflecting on that, Natsuki emerges from the door in the hallway."
            jump ch10_natsuki_back
        "Stay in here.":
            if natsuki_approval > 0:
                $ natsuki_approval -= 1
            "Despite the back of head telling me to explore Natsuki's house."
            "My common sense is telling me that that's probably a bad idea."
            "I barely know Natsuki outside the literature club."
            "Why would I go around looking at her house?"
            "It would be better if I just waited here."
            "..."
            "Natsuki has been a while though."
            "I wonder what she is doing in that room."
            "After a couple more minutes, she comes out and closes the door behind her."
            label ch10_natsuki_back:
            show natsuki 1bq zorder 2 at t11
            n "Sorry, I took a while."
            n 2bo "You didn't leave the room, did you?"
            mc "Of course not..."
            mc "But you sure took a while in there."
            n 2br "S-So?!"
            mc "Well, do you want to tell me what you were doing?"
            mc "You kept me waiting a long time, you know."
            n 2bo "I-It's none of your business!"
            mc "You don't have to tell me."
            mc "I was just curious."
            mc "I can understand if it's a personal thing."
            n "Y-Yeah, well...!"
            n 4br "It is!"
            mc "Alright..."
            "Why is she so hostile all of a sudden?"
            "I suppose it's probably got to do with me coming to her house out of nowhere."
            "Yet somehow expecting me."
            "I don't know how Sayori managed to organize this..."
            n 4bq "Look, I don't know exactly what Sayori had planned."
            n "But we might as well start reading the manga."
            mc "I suppose you're right."
            "Natsuki takes the book from her desk and sits on her bed."
            n 4bh "You can sit on the floor, I guess."
            mc "The floor?"
            mc "But there's a chair right there that you aren't using."
            n 1be "Of course there is!"
            n "You didn't ask if you could use it."
            mc "Well..."
            mc "May I sit in the chair then?"
            n 1bh "Only if you want to..."
            "I take the seat next to Natsuki's desk."
            "I notice that she actually has a lot of bandaid boxes around."
            "I wonder what they're for."
            n 1be "H-Hey!"
            n "What are you looking at?"
            mc "Nothing..."
            "I pull out the book from my bag."
            "Noticing it now, I can see the book is basically in mint condition."
            "There's no trace of a price tag or creases on any of the pages."
            "Seeing as Sayori was the one to buy them, I thought she'd have creased them all before she gave them to us."
            "I open the manga to the first page."
            n 2bc "There's no point reading out loud..."
            n "It doesn't work."
            mc "Are we just going to read in silence then?"
            n 2bg "Well, I don't know!"
            n "Just do whatever you want..."
            "Immediately after saying that, Natsuki opens the manga and begins reading."
            "I decide there's no point in arguing with her and do the same."
            "There's an eerie silence in the room as we both read the manga."
            "After finishing the first chapter, I notice Natsuki looking over at me."
            mc "Are you okay?"
            show natsuki 1bo zorder 2 at h11
            "Natsuki suddenly jumps off from her bed."
            n "W-What?!"
            mc "You don't look like you're reading the manga."
            n 1bp "I was just--"
            n "I mean...!"
            n "S-Shut up!"
            mc "I only noticed because I was going to ask what you thought of the first chapter."
            mc "Seeing as we're here, we might as well talk about it."
            mc "But if you don't..."
            n 1br "No...!"
            n "I was just..."
            n "Fine."
            n 1bm "We can talk about the chapter..."
            mc "What do you think of it?"
            n 1bq "It was..."
            n "...kinda interesting..."
            n "As interesting as character introductions can get, I guess."
            mc "I suppose you're right."
            n "I don't really get this whole strawberry thing..."
            n "One of them uses strawberries as a power?"
            mc "It isn't really clear right now, is it?"
            mc "Maybe we'll learn more in the next chapters."
            n "Maybe..."
            mc "I wonder what the next chapters will tell."
            n 1bt "You aren't going to find out like that!"
            mc "I suppose you're right."
            mc "We'll have to keep reading to find out."
            show natsuki 1bc zorder 2 at t11
            "Natsuki comfortably places herself on her bed again."
            "I lean back on the chair I'm sitting on."
            "Once again, there is a silence between us aside from the sound of pages being turned."
            "I decide to read a bit faster this time."
            "To see if Natsuki is actually reading the manga or not."
            "As soon as I finished the chapter, I look up and see her already looking at me."
            n 1bd "Finally!"
            n "It took you a while to finish that."
            mc "W-What...?"
            mc "How fast did you read that chapter?"
            mc "I was reading it as fast as I could..."
            n 5bd "You must read really slowly then."
            mc "Maybe..."
            n 5bc "What do you think of the other three characters?"
            mc "The other three...?"
            "I read through it too quickly that I actually didn't pay that much attention to what was happening."
            "I only noticed two other characters..."
            "And not any specifics about either of them..."
            "I'll just be as vague as possible."
            mc "They're pretty cool, I guess..."
            mc "They have some strange personalities."
            n 5be "Pretty similar to the ones from the first book..."
            mc "Yeah..."
            "I wasn't actually sure if they were, but I figure agreeing with Natsuki is probably the correct choice."
            mc "I guess this is sort of like an introduction to an arc."
            n 5bd "Exactly!"
            n "It's so much easier to talk with people who actually read manga..."
            n "Especially people who read the same ones as me..."
            mc "I guess Sayori getting us to read together did kinda help, didn't it?"
            n 4bh "Ah..."
            n "I guess..."
            n "B-But don't think that this made us closer or anything..."
            if visited_yuri_hospital:
                mc "Ah, not like that."
                mc "I hope it made us better friends, at least."
                mc "I'm already with Yuri so..."
                n 4bq "Y-Yeah..."
                n "I guess that's okay."
            else:
                mc "Ah, well that's unfortunate..."
                mc "I hope that we'd become a little closer, at least."
                mc "Even if we're just friends for now."
                n 4br "W-What...?!"
                n "F-Fine, I guess we are better friends after this..."
            n 4bn "L-Look, sorry if I'm a little..."
            n "...bothered by this whole thing."
            n "I really wasn't expecting you to come here but when you did..."
            n 4bm "It's like I shouldn't be questioning it and that I {i}was{/i} expecting it."
            n 1bt "Still, I'm really glad that you came here..."
            n 1bs "It's like a moment of peace..."
            mc "What do you mean by that?"
            n 1bm "I don't know how to explain it..."
            n "I don't know if I want to explain it."
            mc "Well, if it affects you in a bad way..."
            mc "...then you should let me know."
            n 4bs "..."
            mc "We're friends, right?"
            mc "You can tell me anything."
            mc "I can help you through it."
            n 4br "Why are you so..."
            n "...so..."
            n "...ugh!"
            mc "Am I that bad?"
            n 4bu "No..."
            n "You're really nice..."
            n "I don't want to say it but..."
            n 1bn "...you're really sweet, you know that?"
            mc "Eh...?"
            n 1bo "I just meant that...!"
            n 1bu "N-Never mind..."
            n 1bs "There's no point trying to explain."
            n "It's my problem anyway."
            n "There's nothing you or anyone else can do to fix it."
            mc "Well, I can try..."
            mc "You're my friend so you have to tell me what I can do to make it better."
            n 1bu "There's..."
            n "There's no way..."
            n "I'm sorry, [player] but there's really--"
            "Suddenly the doorbell rings."
            d "Natsuki, open up!!"
            n 1bo "Oh, no..."
            n "[player], you need to leave right now."
            mc "But we haven't even--"
            n 1bp "Please!"
            n "He's gonna kill me if he sees you here..."
            mc "Okay, Natsuki..."
            n "Can you jump out through the window?"
            n "We can't let him see you..."
            mc "W-What...?"
            n 1bv "Just do it!"
            mc "A-Alright, if you really need me to do this."
            d "Natsuki, open the door right now!!"
            n 1bq "I need to get that..."
            n "But please try to be gone before he comes inside..."
            mc "I'll try."
            show natsuki at thide
            hide natsuki
            "Natsuki runs out of her room and down the stairs."
            "I open up her window and step off into the balcony."
            scene black with wipeleft
            "The way down isn't that far..."
            "But why did she need me to leave this way...?"
            "The voice that was coming from downstairs sounded like a male voice..."
            "So it was probably her dad."
            "Maybe her dad is really strict on having people over?"
            "Still, it sounds like he's finally entered the house."
            "I jump off the balcony..."
            $ pause(2.0)
            "The fall wasn't exactly graceful, but I landed just fine."
            "If she wanted me gone that badly, I probably shouldn't stay around."
            "I decide to head home before anyone notices what I just did."
    scene bg house
    with wipeleft_scene
    play music t2 fadeout 2.0
    "I get back to my home quickly."
    "Sayori isn't waiting for me or anything..."
    "She must have expected me to stay there longer than I did."
    "That's a relief because I'm a little tired from today."
    "Just before I open the door, I hear some yelling."
    s "[player]!"
    show sayori 4ba zorder 2 at t11
    "I spoke too soon."
    mc "Hello, Sayori."
    s "So how'd it go?"
    s 2bd "Did you learn anything about her?"
    mc "Can this wait until later?"
    if talkabout_natsuki_house[0]:
        mc "It's..."
        mc "...pretty bad."
    else:
        mc "Some weird stuff just happened and I'd like to rest for a little bit."
    s "Ah..."
    s "Do you want to talk about it?"
    s "It might make you feel better letting out what you're feeling."
    mc "I think what I need is some rest."
    mc "The headache I had from earlier today feels like it's only getting worse."
    s 2bc "I see..."
    s "Well, I'll try to leave you alone for now."
    s 1bd "I know you're probably sick of seeing me, right...?"
    mc "Sayori, I never said that."
    mc "Sure you might be annoying sometimes, but you're still really important to me."
    mc "I really do just need some rest."
    mc "If you really want to talk about what happened at Natsuki's, then you can come over tomorrow."
    s 1bk "No..."
    s "That's okay."
    s "We don't need to talk about it right now."
    mc "But you seemed pretty intent about talking about it just then?"
    s 1bl "I guess I did..."
    s "But that's not the only way to learn about what you saw."
    mc "What's that meant to mean?"
    s 1bq "Ehehe, nothing~"
    s "I'll see you later, [player]!"
    s 1bd "Like, really soon..."
    mc "Wait!"
    show sayori at lhide
    hide sayori
    "She's already blissfully walking back to her house."
    "What did Sayori mean by learning what I saw?"
    "It's not like she has my memories or anything..."
    "That would be weird."
    "I'm probably just overthinking this a little."
    "Besides, I still need that rest."
    scene bg bedroom with wipeleft_scene
    "Stepping inside my house after that whole day makes me feel kinda sick."
    "The headache feels like it's worse in here than it was outside."
    "Maybe I should take some medicine for that or something..."
    "I didn't do much today, but I already feel incredibly tired."
    "It's like everything I've done has taken double the effort."
    "I don't really know why that is..."
    "Maybe I should go to sleep."
    "Something is telling me that that is the best idea right now."
    "Like nothing else matters except closing my eyes and falling asleep."
    scene black
    stop music
    with close_eyes

    if persistent.natsuki_house[0] and persistent.natsuki_house[1] and persistent.natsuki_house[2] and persistent.natsuki_house[3]:
        $ check_whole_house = True
        $ check_some_house = True
    if persistent.natsuki_house[0]:
        $ talkabout_natsuki_house[0] = True
        $ check_some_house = True
    if persistent.natsuki_house[1]:
        $ talkabout_natsuki_house[1] = True
        $ check_some_house = True
    if persistent.natsuki_house[2]:
        $ talkabout_natsuki_house[2] = True
        $ check_some_house = True
    if persistent.natsuki_house[3]:
        $ talkabout_natsuki_house[3] = True
        $ check_some_house = True

    $ pause(1.0)
    play music mend
    if m_appeal == 3 and did_all_tasks:
        show monika 1be zorder 2 at t11
        m "Hey..."
        m "Sayori said it's important that I do this."
        m "I wasn't aware that she knew I could talk to you like this..."
        m 1bd "But I guess it doesn't matter, I didn't really intend on hiding this from her."
        m "Both of us just want to help..."
        m "Anyway..."
        m "She sent me a message that I should go to [player]'s house..."
        m "So I went there as fast as I could."
        m 1be "It's just me, no Sayori right now..."
        m "But I think even if there were both of us here..."
        m "We'd want to talk about the same thing."
        m "Which is..."
        m 1bf "...Natsuki."
        m "Let me just check what you found at her house..."
        if check_whole_house:
            m 1bc "Wait..."
            m "You did that thing that Sayori talked about, didn't you?"
            m "The thing with saves?"
            m 1bl "Ah...!"
            m "I mean strawberries!"
            m 1bh "Hmm..."
            m "Why didn't the game break for a second?"
            m 1bi "Doesn't that usually happen when Sayori says it?"
            m "That's weird..."
            m 1bn "Anyway..."
            m "You searched through her whole house, didn't you?"
            m 1be "There's only one clear memory inside [player]'s head but..."
            m "There's like these fragments or something that [player_personal] can't really remember."
            m "Well, not properly anyway, but [player_personal] can sort of recall what happened."
            m "I can kinda read them, it's pretty hard to explain."
            m 1ba "Anyway, I'm sure that was probably the right thing to do."
            m "We're trying to learn what we can about Natsuki so that we can find the best way to help her."
            m "Well, I assume that's what Sayori's plan is."
            m 1bc "That's what she was trying to do for Yuri so..."
            m "Anyway, I'll try to learn what I can..."
            m 1bf "I know there was that one thing that [player] saw in there..."
            m "That [player_personal] didn't want to describe..."
            m "And I can't really blame [player_reflexive]."
            m 1bo "It was..."
            m "I wasn't really there but what [player_personal] saw..."
            m "It was pretty disturbing."
            m "I'll tell you more about it if the time ever comes because it's better you don't know."
            m 1bp "There was also that room with nothing in it except..."
            m "...blood marks?"
            m "I wonder what that's all about."
            m 1bc "Then..."
            m "The two living rooms?"
            m "One of them clearly gets used more often than the other."
            m "You can tell because one of them is completely spotless while the other has bottles of alcohol everywhere."
            m 1be "Still, I don't think you missed anything."
            m "Except that room that Natsuki went into herself..."
            m "What could be behind that door...?"
        elif talkabout_natsuki_house[0] or talkabout_natsuki_house[1] or talkabout_natsuki_house[2] or talkabout_natsuki_house[3]:
            m 1bc "You looked around Natsuki's house, right?"
            m "I mean you can't really answer me but I know you did."
            m "[player] has these memories I can just look over when I want to know what you did."
            m 1be "You probably knew that already..."
            m "I know this is like invading someone's privacy..."
            m "But you did it too, right?"
            m "By making [player] go around Natsuki's house."
            m 1bm "So I'm not really the one at fault here..."
            m "At least, that's what I'll tell myself because I feel..."
            m 1bo "...just really bad about doing this."
            m 1bm "Ah, but it's for Natsuki."
            m "I have to think about her happiness too."
            m "So..."
            m 1bq "I'll just..."
            m "...learn what I have to."
            if talkabout_natsuki_house[0]:
                m 1bc "This first room upstairs..."
                m 1bf "What?"
                m "What is that...?"
                m 1bg "I don't..."
                m "No."
                m "You don't deserve to know what was in there."
                m "I care too much about you to..."
                m "Just thinking about it makes me sick."
                m 1be "What else did you learn?"
                if talkabout_natsuki_house[1]:
                    label ch11_nhouse1:
                    m 1bd "Huh?"
                    m "I wonder what {i}that{/i} room is for."
                    m "This second room upstairs is..."
                    m 1be "It seems kinda empty and [player] thought it was for metal working?"
                    m "There must be more to it..."
                    m 1bd "Wait..."
                    m "Blood stains?"
                    m "It's the..."
                    m 1bo "...the room where her dad..."
                    m "Well, we'd better keep looking."
                    m 1bf "What else did..."
                    if talkabout_natsuki_house[2]:
                        label ch11_nhouse2:
                        m 1bc "That looks like some sort of living room."
                        m "That's really weird."
                        m "It doesn't fit the design of the rest of the house."
                        m 1be "I don't have any ideas about that..."
                        m "Maybe we can learn something about that from Natsuki?"
                        m "I don't know..."
                        if talkabout_natsuki_house[3]:
                            m 1bd "Wait a second..."
                            m "That's a living room too."
                            label ch11_nhouse3:
                            m 1bf "But..."
                            m "What are those on the walls?"
                            m "There's so much alcohol there too..."
                            m "Ah..."
                            m 1bq "Natsuki, if I knew..."
                            m "I'm sorry."
                    elif talkabout_natsuki_house[3]:
                        m 1bc "That's a living room..."
                        jump ch11_nhouse3
                elif talkabout_natsuki_house[2]:
                    jump ch11_nhouse2
                elif talkabout_natsuki_house[3]:
                    m 1bc "That's a living room..."
                    jump ch11_nhouse3
            elif talkabout_natsuki_house[1]:
                jump ch11_nhouse1
            elif talkabout_natsuki_house[2]:
                jump ch11_nhouse2
            elif talkabout_natsuki_house[3]:
                m 1bc "That's a living room..."
                jump ch11_nhouse3
            m 1be "So it looks like we know a little bit more about Natsuki..."
            m "I feel like we missed something though."
            m "But..."
            m 1ba "At least we know something, right?"
        else:
            m 1bf "You didn't learn anything about her?"
            m "Just something about alcohol bottles in the house..."
            m 1bg "I thought you would have been curious enough to make [player] do something."
            m "Maybe you just thought you were doing the right thing..."
            m 1bo "I can't really blame you..."
            m "I wouldn't dare invade someone's privacy like that."
            m 1bp "But it looks like we'll have to do this the hard way."
            m 1be "It's okay."
            m "I know we can still do this."
            m "I'll do everything I can."
        m 1bo "..."
        m 1bn "Are you worried?"
        m "It will be fine."
        m 1be "After all, we're doing this together."
        m "I'm sorry that we don't get many chances to talk outside of...{i}this{/i}."
        m 1bm "I've been trying my hardest behind the scenes to make sure Natsuki turns out okay."
        m "Ahaha, I wonder what I'd been doing if I wasn't me..."
        m 1bn "Probably messing everything up for you again..."
        m 1bo "Sorry, I know I shouldn't be thinking like that..."
        m "But it was probably the most positive thing on my mind right now."
        m "It's getting a little difficult managing it all, especially with the book's influence."
        m 1bf "But every time you write a poem..."
        m "Every time you choose a word meant for me..."
        m 1bm "I just feel stronger, even if it's just for a while."
        m 1bq "Ah..."
        m "I probably sound really weak."
        m "And maybe I am..."
        m 1br "I'm relying on someone choosing words out of a game just to hang on."
        m "What does that make me?"
        m "The only reason that I'm 'me' is because of someone else doing something for me."
        m 1bn "That's kinda pathetic, right?"
        m "I don't know what this feeling is."
        m 1bf "It's like I want you to stop helping me..."
        m "But at the same time..."
        m 1bg "I {i}need{/i} to know you still care for me."
        m "Why am I feeling this way?"
        m 1bp "..."
        m "There's an obvious answer, isn't there?"
        m 1bg "You're probably thinking, it's {i}the book{/i}."
        m "Right?"
        m "Maybe it is..."
        m 1be "Maybe that's what's causing me to feel so bad about myself."
        m "Like it wants me to give up to it."
        m 1bo "I'm trying to tell myself that that's the reason..."
        m "...and that it's not me being worthless."
        m "But I can't help but feel like I am..."
        m 1bq "Like if I just surrender, then everything will be okay and I'll be worth something again."
        m 1be "But, you're obviously holding on to me for a reason..."
        m "So I'm not worthless, am I?"
        m "I've got you..."
        m "And you obviously think I'm not worthless."
        m 1bm "Ahaha, especially if you're willing to listen to me ramble..."
        m "Sorry."
        m "I'm going to stop trying to think like this."
        m 1bn "For your sake and mine."
        m "I don't want to keep worrying you about me when there's more important stuff."
        m 1be "Oh well..."
        m "Maybe there's still--"
        stop music
        scene bg bedroom
        show monika 1bc zorder 2 at t11
        with open_eyes
        play music t6
        mc "Eh?"
        mc "Monika, what are you doing in here?"
        m 1bl "W-What?"
        m "[player]!"
        m "Y-You're awake..."
        m "That's..."
        "Monika pauses for a moment to think."
        "She stares directly at me."
        m 3ba "Ahaha, what do you mean?"
        mc "Why and how are you in my house?"
        m 3bb "You invited me over, remember?"
        "Suddenly I'm getting this feeling within me to accept what Monika is saying is true."
        "It's like there are memories of me doing that but for some reason I can't remember."
        "Did I really invite her over?"
        "When did I do that...?"
        "She has no reason to lie to me, so it might just be my bad memory acting up again."
        mc "Ah..."
        mc "Well, I don't exactly remember inviting you over to my house but..."
        mc "I probably did."
        mc "Do you know the reason?"
        m 2bc "Um..."
        m "You probably just wanted to talk..."
        m "About the manga or the club maybe..."
        m 2be "You weren't really clear about it."
        mc "I see."
        mc "Well, do you want to head downstairs?"
        mc "I can cook us a snack or something..."
        m 2ba "Ahaha, okay."
        scene bg kitchen with wipeleft_scene
        "As we go down the stairs, I feel like it's completely normal for Monika to be here."
        "Though I'm still not sure on the exact reason why."
        "Something tells me I shouldn't question it but I can't help but--"
        show monika 4ba zorder 2 at t11
        m "So what are you planning on making for me?"
        mc "Ah..."
        mc "Well, do you have any preference?"
        mc "I don't really know much about what you eat."
        m "Well, I'm actually a vegetarian."
        mc "Oh...?"
        mc "I didn't know that."
        m 2be "Yeah..."
        m "I'm just doing my part to reduce the amount of pollution in our world."
        m 2bc "It's kind of a problem that we only care about killing things that we can relate to as a species."
        m "Like, most of us are fine with killing bugs and we kill billions of microorganisms every day without second thought."
        mc "That's kinda different though, isn't it?"
        m 2bf "Is it really?"
        m "If those things were a little bit bigger, it's murder!"
        mc "That's..."
        m 2be "I'm just saying, we're pretty biased species, if you think about it."
        mc "I suppose we are..."
        m 1ba "Still, I won't judge you for what you eat."
        m "I'm just worried about what's happening in to our world, that's all."
        m 1be "You have to agree that it's a pretty big problem, isn't it?"
        mc "I guess so..."
        m "[player], I know that I can't change the whole world..."
        m 1bm "...not anymore..."
        m 1be "But it starts with one person, doesn't it?"
        m "If I can influence other people to do the same then maybe the world will become a better place..."
        mc "That's a really idealistic view on the world."
        m "I suppose it is..."
        m "But I have to have ideals."
        m 3ba "It's like some sort of goal to work towards."
        m "Do you know what I mean?"
        mc "Sort of..."
        "We've kinda gotten off topic from cooking."
        "It was interesting to hear Monika's thoughts and learn more about her though so I didn't really mind."
        mc "Anyway, what did you want to eat?"
        mc "I'm not really sure what vegetarians eat..."
        mc "Aside from..."
        mc "...not meat."
        m 3bl "Ahaha, well you're not wrong~"
        m "Do you have some fruit or vegetables lying around?"
        m "I'm sure you have enough to make a simple salad at least..."
        mc "Ah..."
        "I haven't actually had the time to go shopping..."
        "Or do anything at all, lately."
        "So I don't have a lot of stuff that Monika would actually eat."
        mc "Well..."
        m 1be "It's okay."
        m "I know you've been busy, so it's probably a bit unreasonable of me to ask if you do have food lying around."
        m "And why would you?"
        m "It's not like you remembered you invited me."
        mc "Sorry, I know it's my fault that I messed up."
        mc "Is there any way I can make it up to you?"
        mc "Maybe we can go to a cafe or something...?"
        m 1bm "Ah..."
        m "Did you just ask me out on a date?"
        mc "Um...!"
        "Did I actually just accidentally ask Monika on a date?"
        "This is so embarrassing..."
        "I like her, but it's not like she'll just say yes to me."
        "We barely talk to each other outside of the club and--"
        m 1bj "Ahaha, you're bright red."
        mc "A-Am I?"
        mc "S-Sorry, I didn't intend to ask you out."
        mc "It was just an offer since I forgot to go shopping for food..."
        mc "A-And I don't want to see like a bad host."
        mc "I'm happy to pay for your meal, if you do want to go."
        mc "It's the least I can do."
        m 1bm "Ahaha, that's so sweet of you."
        m "I think I've overstayed my welcome though."
        mc "What?"
        mc "You just got here..."
        mc "If it's something I said, then--"
        m 1be "It's alright, [player]."
        m "None of this is your fault."
        m 1bf "We're all just dealing with things that are out of our control."
        m "In a world like this, all you can do is hope that everything works out for you..."
        mc "Eh...?"
        mc "I'm not sure I understand."
        "Sometimes it's like Monika's problems are bigger than anything I can comprehend."
        "At least, that's what it feels like sometimes."
        "It's like, I can't personally do anything for her."
        "I don't know what that feeling is, but it's like all my actions are inconsequential."
        m 1be "Well, sorry for taking up your time, [player]."
        m "I understand you must have better things to do than listen to me talk."
        m "Maybe next time something like this happens, I'll actually accept your invitation."
        m 1bm "But right now..."
        m "Things are kinda tough for me."
        m "I hope you understand."
        mc "I don't really..."
        mc "And every time we talk about stuff like this again it becomes harder to comprehend."
        mc "I'm probably not making much sense, am I?"
        m 1be "No, I think you are."
        m "Sorry if it feels that way but you're probably right."
        m "It's just become more and more difficult for me with each passing day."
        mc "I've probably said this before..."
        mc "If I have, forgive my terrible memory but..."
        mc "Is there anything I can do?"
        mc "Anything at all?"
        mc "I know you might not think I'm the best person for that kinda thing but..."
        mc "I want to help."
        m "This does sound like a conversation we've had before, doesn't it?"
        m 1bo "The circumstances were different but..."
        m 1bn "Well, the outcome will be the same."
        mc "Which means...?"
        m 1be "There's nothing for us to talk about."
        m "Sorry, [player]."
        m "My problems are my own."
        m "I don't want to concern you or anyone else about them."
        mc "That's crazy talk."
        mc "I hope you aren't feeling depressed like Sayori was..."
        mc "Because if you are, then you have to let me know."
        mc "Maybe I can't help as much as a professional could, but I can listen and maybe that'll make you feel better."
        mc "Monika."
        mc "There's clearly something bothering you."
        mc "Remember when I told you I was a good listener?"
        mc "You can tell me what's on your mind."
        mc "I can help you, or at least try to."
        m 1bm "Aha..."
        m "Now I definitely remember you saying that."
        m "So now is my cue to leave without explaining anything."
        m 1bp "Sorry."
        mc "Alright, Monika..."
        m 1be "Thanks for the offer though, [player]~"
        m "You're a really kind person, you know that?"
        mc "Ah, thanks..."
        m "I mean it."
        m 1bm "You don't know me, Yuri or Natsuki very well, but you're doing your best to help us..."
        m "...even if you don't realize it."
        mc "I've just been going to club meetings and doing what Sayori asks of me."
        mc "Is that really helping anybody?"
        m 1bn "Maybe it's different from your perspective..."
        m "But you're learning, aren't you?"
        mc "Learning...?"
        m 1be "What happened today at Natsuki's..."
        m "You noticed stuff you might not have before."
        m "I don't know if that's a good thing or not..."
        mc "Are you saying I was dense before?"
        m 1bl "Ah...!"
        m "I didn't intend to insult you or anything."
        m "I just meant that you've become smarter."
        m 1be "More aware, if you will."
        m "But I've already said too much."
        mc "Monika, wait..."
        m 1bf "Sorry, [player]."
        m "But I'm going to have to ask Sayori to make you forget that conversation we just had."
        m 1bg "To avoid another 'headache'."
        mc "Make me forget?"
        mc "Now I really don't know what you're talking about."
        m 1be "Goodbye, [player]."
        m "I'll see you on Monday."
        show monika zorder 2 at lhide
        hide monika
        "I'm powerless to stop her from exiting my house, almost literally."
        "I want to get her to explain what she meant but at the same time, I can't..."
        "...or rather, don't want to."
        "I should just leave it."
        "There's no way I'll forget what she said to me anyway."
        "Aside from that, my headache appears to be getting worse."
        "Maybe I can ask Sayori about this whole thing."
        "Or at least talk to her about it..."
        "I don't really know if she'll listen but it's worth a shot."
        if sayori_confess:
            "If she does love me..."
        else:
            "If she really is my best friend..."
        "...then she'll listen to what I have to say right?"
        "That reminds me of what Monika said before."
        "I really didn't have anything I could cook with."
        "It wasn't just fruits and vegetables..."
        "Maybe I could go to the shops and buy some before the day--{nw}"
    else:
        show sayori 1bd zorder 2 at t11
        s "I..."
        if m_appeal < 3:
            s "I wonder where Monika has been lately..."
            s "I'm a little concerned for her..."
        else:
            s "I thought I was gonna get Monika to do this but..."
        s 1bb "Anyway..."
        s "Let's talk about what you found at Natsuki's house."
        s 1bc "I would have done something earlier but..."
        s 1bd "Ah, well [player] wasn't exactly in the best mood."
        s "That headache, huh?"
        s "I wonder what caused it..."
        s "I'm kinda worried for [player]."
        s 1bk "I hate putting [player_reflexive] in situations like just then but..."
        s "[cPlayer_personal]'s the only one who can do anything."
        s "I don't really know how to explain what I mean by that..."
        s "...or if I even can."
        s 1bd "I feel like it's not the time to talk about that."
        s "Besides, we have more pressing stuff at hand, don't we?"
        s 1bb "Like Natsuki."
        if check_whole_house:
            s 1bd "You went through her whole house, right?"
            s "I can tell you had to eat a bunch of strawberries to do that."
            s "Listen..."
            s "I know I can sound pretty forceful..."
            s 1bk "But you have to understand that I'm doing this for my friends."
            s "I care about them so much, you wouldn't believe it..."
            s 1bd "Well, maybe you could."
            s "I don't really know that much about you."
            s "It's not really my business to know about you."
            s "That's more of Monika's thing, right?"
            s 1ba "You don't have to answer that, I already know the answer."
            s "..."
            s 1bk "Me having these conversations with you is almost like cheating, isn't it?"
            s "The person who made this world for us probably intended for you to solve our problems without all these hints..."
            s 1bj "...or maybe they intended for us to suffer."
            s "It doesn't matter."
            s 1bd "What matters is what we do with this chance."
            s "Since this is like a game, I wonder if there actually are any cheats..."
            s "...because if I could cheat, I would."
            s "Just to make everyone happy..."
            s "I don't care about the consequences..."
            s "I just care about..."
            s 1bk "...everyone's happiness."
            s "But there's no use talking about that."
            s "Even if I could cheat, I don't know how I would use those cheats."
            s 1bd "What I want is something that needs to be worked for anyway, so I'm determined to do it the hard way if I need to."
            s "Ehehe..."
            s "I was just looking through what [player] saw in the house."
            s "There's some pretty weird stuff in there."
            s "Like all those alcohol bottles everywhere in the house?"
            s 1bc "Eh..."
            s "But that's not all that's weird, right?"
            s 1bb "The stuff behind those doors."
            s "I can tell you what the meaning was behind each one..."
            s "Or at least, my take from it."
            s "So let's start from downstairs."
            s 1bd "The living room with the couch..."
            s "That's just a normal living room..."
            s "And an unusual amount of alcohol...right?"
            s "I don't think [player] noticed it, but there was some blood on the walls..."
            s 1bi "I think..."
            s "...it's Natsuki's..."
            s "Look..."
            s 1bj "I'll explain it all after we finish talking about what was in her house."
            s "There was that 'other' living room in Natsuki's house"
            s 1bk "I can't be sure of what {i}that{/i} was meant to be but..."
            s "I'm almost certain it's there as a sort of momento..."
            s 1bn "...or is it pronounced memento...?"
            s 1bd "Either way, I think it's there as a memory."
            s "Of what once was...or something like that."
            s "I'm not really sure how to describe it..."
            s 1bc "But I think Natsuki only lives with her dad now."
            s "There was probably more people in the family before but now..."
            s "Now it's only the two of them."
            s 1bf "Which is why I think she gets so much abuse."
            s "Maybe her dad blames her for all his shortcomings."
            s "And..."
            s 1bg "Never mind."
            s "You noticed that room was almost spotless, right?"
            s "I think her dad gets her to clean it."
            s "That's the only logical explanation I can think of."
            s "Maybe it's her dad's retreat when he feels reminiscent of the times that once was."
            s 1bd "I don't really know, I'm just telling you what I think based on what I can tell."
            s 1bg "Now, let's talk about that second room upstairs."
            s "I'm almost certain this is where Natsuki gets beaten."
            s "She probably gets punished for the smallest things and is taken in here."
            s 1bg "I don't think [player] noticed it but the windows are actually soundproof as well as tinted."
            s "I think that's probably to avoid some unwanted attention..."
            s "There's one room left..."
            s 1bc "Well, not including the one Natsuki went into."
            s 1bf "The one I'm talking about is her father's room."
            s "He keeps all her manga in there and I'm not sure..."
            s "...but I think he beats her every time she wants to try to get one."
            s "He even orders new manga for her, just so that she's tempted to read it."
            s 1bk "And if she is..."
            s "Well, you can guess how that turns out."
            s "What's more horrifying is what's inside the closet."
            s 1bj "It was..."
            s 1bf "You know, going through all of this..."
            s "It made me realize how cruel some people can be."
            s 1bg "You know those bandaids that are lying in Natsuki's room?"
            s "They don't do anything."
            s 1bh "I think her father just buys them for her as a sign of irony."
            s "He's really mean."
            s "I don't want to call the police on her dad..."
            s 1bk "Because that would just make her feel more sad."
            s "I know deep inside, she still cares for him."
            s "And maybe there's still a piece of her dad that..."
            s "...cares for her too..."
            s "It's really sad when people we care about change, isn't it?"
            s 1bg "One day they're the person you looked up to..."
            s "That you were friends with for so long..."
            s 1bh "Can change just like that..."
            s 1bd "Anyway, I've stalled for too long."
            s "You're still wondering what was in the closet and the room Natsuki went into."
            s "The thing in the closet was{nw}"
        elif talkabout_natsuki_house[0] or talkabout_natsuki_house[1] or talkabout_natsuki_house[2] or talkabout_natsuki_house[3]:
            s 1bf "I know you didn't do all you could."
            s "Well, at least you looked through her house a little bit."
            s "Before, I used to give you hints, right?"
            s "Do you really still need those?"
            s 1bg "I thought it was obvious by this point..."
            s "It's all about strawberries."
            s "You know that, right?"
            s 1bh "Because of you, we couldn't figure out everything we needed to."
            s "I suppose this is partly my fault too."
            s "If I realized you were so--"
            s 1bk "No."
            s "I shouldn't get so angry about this sort of thing."
            s "It isn't over."
            s "I don't know what's come over me."
            s "I'm sorry..."
            s 1bf "I know what we made [player] do was something [player_personal] would never do otherwise."
            s "So I shouldn't be so upset at you for that."
            s 1bd "You're probably just looking out for [player] too, right?"
            s "It's just..."
            s "I really wanted Natsuki to be happy."
            s 1bk "And now it's like that's not going to happen..."
            s "At least, not the way I wanted it to..."
            s 1bl "Ah..."
            s "What am I talking about?"
            s 1bd "I sound hopeless."
            s "And that's not true."
            s "She's definitely going to be happy."
            s "I know it."
            s 1bb "But I guess I can't really be sure until I look through what you found, right?"
            s "So..."
            s 1bc "Let's see."
            if talkabout_natsuki_house[0]:
                s 1bc "You went into her father's room?"
                s "That's what it was, right?"
                s "You can tell because of the bed and the manga collection on the shelf."
                s 1bk "What a terrible person..."
                s "Sorry."
                s "I just don't see any way that he could be redeemed as a person."
                s "Maybe there was a chance but..."
                s 1bj "With what was in the closet..."
                s 1bf "I don't..."
                s "I don't think I should tell you."
                s "It's really quite awful and..."
                s 1bk "I hope we never have to talk about it."
                s "Sorry..."
                s "I know you're probably really curious but..."
                s 1bb "Well, I still have other things to look over, right?"
                if talkabout_natsuki_house[1]:
                    label ch11_nhouse1s:
                    s 1bc "This other room upstairs..."
                    s "It doesn't look like an ordinary room."
                    s "I think it's probably the main place where..."
                    s 1bk "...Natsuki gets beaten."
                    s "There's so much blood in there."
                    s "Some of it is recent..."
                    s "Poor Natsuki..."
                    s 1bu "I'm sorry we couldn't do anything sooner..."
                    s "..."
                    s "Her father is a horrible person, isn't he?"
                    s "But she still cares about him..."
                    s "...even if it's just a little bit."
                    s 1bk "That's..."
                    s "Never mind."
                    s 1bh "Is there anything else you've found?"
                    if talkabout_natsuki_house[2]:
                        label ch11_nhouse2s:
                        s 1bc "This is..."
                        s "That other room downstairs."
                        s "It's a living room, isn't it?"
                        s 1bb "It doesn't fit the rest of the house."
                        s "If you want to know what I think..."
                        s 1bc "...I think it's like a reminder of what once was."
                        s "It's clean, there's no alcohol anywhere in there and it looks like it never gets used..."
                        s "Only cleaned..."
                        s 1bd "And it looks like it's cleaned at least once a day..."
                        s "I wonder if her dad cleans it."
                        s 1bk "No."
                        s "It's probably Natsuki's responsibility too."
                        s "Ah..."
                        s "I feel so sorry for her."
                        s 1bf "I wish I could have done something sooner..."
                        s "But there's no point reflecting on what could have been."
                        s 1bb "I still need to look over what else you've found, right?"
                        if talkabout_natsuki_house[3]:
                            s 1bj "E-Eh...?"
                            s "This is her real living room, right?"
                            label ch11_nhouse3s:
                            s 1bh "But..."
                            s "The marks on the walls..."
                            s "They're so faint, but you can see them..."
                            s 1bk "It's blood."
                            s "It has to be."
                            s "Natsuki..."
                            s "Your father, he's..."
                            s 1bh "Why...?"
                            s "There's so many bottles on the ground."
                            s "It's such a mess..."
                            s "Why would she stay with him in a situation like this?"
                            s "It's so terrible..."
                            s 1bf "Is there something else...?"
                    elif talkabout_natsuki_house[3]:
                        s 1bc "That's a living room..."
                        jump ch11_nhouse3s
                elif talkabout_natsuki_house[2]:
                    jump ch11_nhouse2s
                elif talkabout_natsuki_house[3]:
                    s 1bc "That's a living room..."
                    jump ch11_nhouse3s
            elif talkabout_natsuki_house[1]:
                jump ch11_nhouse1s
            elif talkabout_natsuki_house[2]:
                jump ch11_nhouse2s
            elif talkabout_natsuki_house[3]:
                s 1bc "That's a living room..."
                jump ch11_nhouse3s
            s 1bc "Oh..."
            s "I guess that's all."
            s 1bk "I feel like we're definitely missing something."
            s "I guess we'll have to work with what we've got."
            s "You know..."
            s "We didn't really talk about Natsuki's bedroom or the room she went into."
            s 1bf "Those bandaids on her table."
            s "I'm almost sure that they're just there to make fun of her or something..."
            s "Her dad probably just loves making fun of her."
            s 1bg "What could cause a person to be so cruel?"
            s "It doesn't matter..."
            s "We have to help Natsuki."
            s 1bh "To do that, we need to get rid of her feelings towards her father."
            s "I know she still loves him, even a little bit..."
            s 1bk "She won't leave because he's..."
            s "...the only family she has left."
            s "It might be hard but..."
            s "I think the only way for her to be truly happy is to separate her from her dad."
            s "It won't be easy..."
            s 1bd "But here's my plan."
            s "Firstly, we{nw}"
        else:
            s 1bi "You have to be messing with me."
            s "You really didn't learn anything about Natsuki?"
            s "Why not?"
            s 1bj "You have the power of strawberries and you do..."
            s "...nothing?"
            s "Do you not have any curiosity at all?"
            s 1bh "There must be something more to it."
            s 1bi "You want to make everything difficult for me."
            s "It's like you're searching for a bad ending to this, aren't you?"
            s "Why?"
            s 1bj "Why did you even give Monika that first chance if that was your intention?"
            s "I can't believe this."
            s "I can't believe that you would just go through this with that sole intention."
            s 1bi "If you really care about everyone, you'll eat a strawberry."
            s "Explore even a little bit of Natsuki's house..."
            s "Please..."
            s 1bj "Because all we know is something about bandaids!"
            s "That isn't helpful, at all!"
            s 1bk "What does her dad do to her?"
            s "You have to go back."
            s "It's the only way..."
            s "..."
            s "That's not true."
            s "It isn't the only way..."
            s "It just makes what I have to do easier."
            s 1bj "But clearly, you enjoy making what I have to do hard."
            s "Go back."
            s 1bf "Please?"
            s "Fine..."
            s 1bg "I guess I have to do it all myself."
            s "Goodbye.{nw}"
        show screen tear(8, offtimeMult=1, ontimeMult=10)
        $ pause(1.0)
        scene bg bedroom
        hide screen tear
        play music t2 fadeout 1.0
        $ pause(1.0)
        window show(None)
        "What the?"
        window auto
        "My head is aching more than before."
        "I thought that the nap I took would reduce the headache..."
        "Not make it worse."
        "Was someone talking to me?"
        "I feel like someone was just speaking {i}at{/i} me."
        "But I couldn't make out any words..."
        "It's like when I'm in a crowded area with lots of people talking at the same time..."
        "And I can't really understand what anyone is saying..."
        "But this time, it was only one voice."
        "Despite that, it was still impossible to pinpoint."
        "It's that or I'm imagining things again."
        "This headache isn't exactly helping either."
        "I really should talk to somebody about my constant waking up somewhere else thing..."
        "I have a feeling if I told Sayori about this seriously, she'd probably just laugh at me..."
        "...or call me crazy."
        "I would do the same, in her position."
        "It all sounds too surreal."
        "I want to get something to eat, to try to ease the headache..."
        "But I'm pretty sure that I've almost ran out of food downstairs."
        "I don't have anything I can cook as well..."
        "Maybe I can go to the shops and--{nw}"
    $ persistent.natsuki_house = [False, False, False, False]
    $ renpy.save_persistent()
    return

label ch10_end:
    $ ch10_del_jump = "_end"
    stop music
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    scene bg shop_sunset
    stop sound
    hide screen tear
    play music t2g
    queue music t2g2
    "I finally make it to the local store."
    "As far as I can tell, there isn't anyone here except for me and the clerk."
    "That's pretty convenient for me, since it means I can get what I want faster."
    "I'm not after much, just some food to last me another week."
    if m_appeal == 3 and did_all_tasks:
        "Maybe I'll buy some more fruits and vegetables in case Monika ever comes over again."
    "Going through the aisles, it seems that everything is really cheap."
    "In fact, almost everything in the store costs next to nothing."
    "I could easily buy a months' worth of food and spend close to nothing."
    "When did the prices get this cheap...?"
    "Despite the temptation to waste all my money on a good deal, I decide to go for what I can carry home."
    "Since I'm here I might as well get something for my headache too."
    "Maybe there's a clearance or something because there's no way a small store like this could afford to have prices this low."
    "After I get everything I need, I head to the counter to pay."
    "But before I can get to the counter, someone approaches me."
    "I don't know who it is."
    "But they look like they mean business..."
    show dadsuki 1c zorder 2 at t11
    d "You there."
    "The voice sounds oddly familiar."
    d "You look like you're familiar with this store."
    d 1e "My name is Yasuhiro."
    $ d_name = "Yasuhiro"
    mc "O-Oh, okay..."
    mc "Did you want something from me?"
    d 1g "That's why I called for your attention, isn't it?"
    d "I want to know where you can purchase bandaids in here."
    mc "Bandaids?"
    d 1c "Yes, bandaids."
    d "I assume you heard me the first time."
    d 1a "Now, if you'd direct me there I'll be on my way."
    "Who is this guy?"
    "Why do I recognize his voice...?"
    d 1e "Never mind."
    d "You are clearly useless."
    d "Now get out of my way."
    show dadsuki zorder 2 at thide
    hide dadsuki
    "Yasuhiro roughly shuffles past me."
    "I almost drop what I'm carrying because of it."
    "It's not really my business why he's looking for bandaids..."
    "...but I'm kind of curious."
    "Something tells me I should keep an eye out on 'Yasuhiro'."
    "I don't think it's the last time I'm seeing him either..."
    "After paying the small price at the counter, I head home."
    "The grocery bags don't weigh that much, but it will probably slow me down a little."
    scene bg residential_day
    with wipeleft_scene
    "What an odd way to spend Saturday..."
    "First Sayori gets me to go to Natsuki's house out of nowhere..."
    if talkabout_natsuki_house[0]:
        "Which wouldn't be so bad if..."
        "...I didn't see what that was in the closet."
    "And that voice I heard coming from Natsuki's front door..."
    "Now that I think about it..."
    "Could the person at the store be...?"
    "That's impossible, right?"
    "Whatever, this day was already weird to begin with."
    if m_appeal == 3 and did_all_tasks:
        "Then Monika appears in my house out of nowhere."
        "When I say out of nowhere, I was actually expecting her..."
        "But I didn't do anything about it."
        "She had to go to my room to wake me up..."
        "So I guess that was my fault."
    else:
        "Then I wake up on my bed with a headache that became worse."
        "With me thinking that someone is trying to tell me something..."
        "Thinking about all of this, maybe I am going crazy..."
    "Still..."
    "I have to get home before it gets dark."
    "I don't know what's in store for me tomorrow."
    "I just hope it isn't as bad as what happened today."
    "Before I can make the turn to my street, I'm stopped."
    show sayori 1bd zorder 2 at t11
    s "Hi [player]~"
    s "Did you go shopping just then?"
    mc "Well, can you take a guess as to why else I'd be carrying this?"
    s 1bh "Aw, come on..."
    s "It was just a simple question."
    s "You don't have to be a meanie about it..."
    mc "You're right."
    mc "I'm sorry."
    mc "I guess this headache is just getting the better of me."
    s 1bc "Your headache, eh?"
    s "Maybe I can help with that..."
    mc "Help?"
    mc "I don't want to sound mean or anything but..."
    mc "I doubt talking to you is going to help me with my headache..."
    mc "And besides I've already bought something from the shop for it."
    s "Oh..."
    s 1ba "I was actually on my way to the shops now."
    mc "What for?"
    s 1bl "To do some shopping obviously!"
    mc "You know what I meant."
    s 1ba "Ehehe, I know."
    s "It's fun messing with you sometimes..."
    mc "Well, that makes one of us."
    s 1bd "Sorry, I know wasting your time here isn't helping your headache."
    mc "Well..."
    s 1bq "I'll be on my way now."
    mc "Alright, Sayori."
    "As I start walking, I suddenly remember Yasuhiro."
    mc "Before I go..."
    s 1bn "What is it?"
    mc "You probably don't know anything about it..."
    mc "But I feel like I've got to tell you."
    s 1ba "Come on, just say it [player]."
    mc "Alright, alright..."
    mc "Do you know someone called 'Yasuhiro'?"
    s 1bo "Yasuhiro...?"
    show sayori 1bk
    "Sayori pauses for a moment and thinks."
    show sayori 1bq
    "She looks worried for a second then smiles again."
    s "Nope!"
    s "Ehehe, why do you ask?"
    mc "I don't know."
    mc "I guess I thought you'd know who that was."
    s 1bc "How would I know who that was?"
    s "It's not like I know everything..."
    mc "Ah, that's a shame."
    s 2bl "E-Eh...?"
    s "What made you ask me that anyway?"
    mc "I guess it was just a feeling."
    mc "Maybe since you're the president of the Literature Club, you'd know..."
    s "W-What does being president of the club have anything to do about this 'Yasuhiro' person?"
    "Thinking back on what I just said..."
    "It does seem that those two have literally no correlation."
    "Now I'm wondering why I asked her that in the first place."
    mc "I..."
    mc "...don't know."
    mc "Sorry for bothering you, Sayori."
    s 2bq "That's okay!"
    s "No need to be sorry!"
    s 2br "It's probably just your headache acting up."
    s 2bc "{i}(I should probably look into that...){/i}"
    mc "What was that last thing you said?"
    s 2br "Nothing!"
    s "See you later, [player]~"
    mc "Bye, Sayori."
    show sayori zorder 2 at thide
    hide sayori
    "Sayori quickly runs away from me."
    "I don't know why but I get the feeling she's probably trying to stop me asking questions."
    "No..."
    "That's probably just my imagination, she already told me she doesn't know anything."
    "And it's not like she has a reason to lie to me."
    "I'm just going to head home and take this headache medicine."
    "Tomorrow will be a better day."
    return

label ch10_delete:
    python:
        persistent.yasuhiro_deleted = True
        n.display_args["callback"] = None
        mc.display_args["callback"] = None
        m.display_args["callback"] = None
        s.display_args["callback"] = None
        d.display_args["callback"] = None
        narrator.display_args["callback"] = None
        _history_list = []
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    scene black
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    $ gtext = glitchtext(70)
    "[gtext]{nw}"
    window auto
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(1.0)
    stop sound
    hide screen tear
    window show(None)
    jump ch11_bad
