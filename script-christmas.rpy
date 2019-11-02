# How else to do this? This is really inefficient but whatever
screen timer_ch_del(timerstr,jumploc):
    timer (len(timerstr) / 30.0 + 0.5) action Jump(jumploc)

screen timer_ch_del2(timerstr,jumploc):
    timer (len(timerstr) / 30.0 + 0.5) action Jump(jumploc)

screen timer_ch_del3(timerstr,jumploc):
    timer (len(timerstr) / 30.0 + 0.5) action Jump(jumploc)

screen timer_ch_del4(timerstr,jumploc):
    timer (len(timerstr) / 30.0 + 0.5) action Jump(jumploc)

# Literally poem response start except not
label giftexchange_start:
    $ poemsread = 0
    $ skip_transition = False
    $ monika_prompt = False
    label giftexchange_loop:
        if renpy.music.get_playing() and not (renpy.music.get_playing() == audio.t5christmas or renpy.music.get_playing() == audio.t5c):
            $ renpy.music.set_volume(1.0, delay=0.0, channel='music')
            $ renpy.music.play(audio.t5christmas, fadeout=1.0, if_changed=True)
        if skip_transition:
            scene bg ay_livingroom
        else:
            scene bg ay_livingroom
            with wipeleft_scene
        $ skip_transition = False
        if not renpy.music.get_playing():
            play music t5christmas
    label giftexchange_start2:
        if poemsread == 0:
            $ menutext = "Who should I exchange gifts with first?"
        else:
            $ menutext = "Who should I exchange gifts with next?"

        menu:
            "[menutext]"

            "Sayori" if not s_readpoem:
                $ s_readpoem = True
                "I wonder what Sayori got me. Hopefully something she knows I like."
                "But whatever it is, I'm sure I'll be happy with it."
                call giftexchange_sayori
            "Natsuki" if not n_readpoem:
                $ n_readpoem = True
                "I'm curious to know if the [christmas_gifts[2]] is gonna be something she likes."
                "So I'll go exchange with Natsuki now."
                call giftexchange_natsuki
            "Yuri" if not y_readpoem:
                $ y_readpoem = True
                "The gift I got Yuri is definitely the most different out of everyone's."
                "I hope she likes it."
                call giftexchange_yuri
            "Monika" if not m_readpoem and not monika_prompt:
                if poemsread < 4:
                    $ monika_prompt = True
                    if poemsread == 0:
                        "Monika seems to be busy exchanging gifts with someone right now."
                        "Maybe I should talk to someone else."
                    elif poemsread == 1:
                        "She's busy talking to someone else right now."
                        "Maybe I should exchange with someone other than Monika first."
                    elif poemsread == 2:
                        "Monika seems to be busy in a conversation."
                        "I shouldn't interrupt her."
                    elif poemsread == 3:
                        "She's busy with another gift exchange at the moment."
                        "I should probably find someone else."
                    jump giftexchange_start2
                $ m_readpoem = True
                "The clerk seemed really different when it came to Monika."
                "Regardless, I hope she enjoys the gift I bought for her."
                call giftexchange_monika
            "Ayame" if not ay_readpoem:
                $ ay_readpoem = True
                "I don't really know Ayame well."
                "But I'd like to, and hopefully this gift will give us something to talk about."
                call giftexchange_ayame
        $ poemsread += 1
        $ monika_prompt = False
        if poemsread < 5:
            jump giftexchange_loop


    $ s_readpoem = False
    $ n_readpoem = False
    $ y_readpoem = False
    $ m_readpoem = False
    $ ay_readpoem = False
    $ poemsread = 0
    return

label giftexchange_startmusic(recipient="sayori"):
    $ currentpos = get_pos()
    if recipient == "monika":
        $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>mod_assets/bgm/5_monikaperfect.ogg"
    elif recipient == "ayame":
        $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>mod_assets/bgm/5_ayame.ogg"
    else:
        $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_" + recipient + ".ogg"
    $ renpy.music.play(audio.t5b, channel="music_poem", fadein=2.0, tight=True)
    $ renpy.music.set_volume(0.6, delay=2.0, channel='music')
    return

label giftexchange_revertmusic(revert_music=True):
    if revert_music:
        stop music_poem fadeout 2.0
        $ renpy.music.set_volume(1.0, delay=2.0, channel='music')
    else:
        stop music_poem
        $ renpy.music.set_volume(1.0, delay=0.0, channel='music')
    return

label giftexchange_sayori:
    call giftexchange_startmusic("sayori")
    scene bg ay_livingroom
    show sayori 1cha zorder 2 at t11
    with wipeleft_scene
    s "What's in the box, [player]?"
    mc "You'll find out, won't you?"
    mc "No need to rush."
    s 1chh "I told you, I can't wait!"
    s "Come on! Gimme, gimme, gimme!"
    mc "Alright, calm down..."
    "I hand over the wrapped box with Sayori's name on it."
    "Immediately, she begins tearing it apart."
    mc "Wow..."
    mc "You're really excited for this present, aren't you?"
    s 2chq "Ehehe, it's coming from you after all~"
    mc "I wouldn't get my hopes up if I were you."
    s "Why not?"
    "Sayori finishes 'unwrapping' the present."
    "In reality, she basically tore through it, leaving lots of pieces of wrapping paper on the floor."

    $ nextscene = "gift_" + christmas_gifts[0] + "_s"
    call expression nextscene

    s 1chd "Well..."
    s "I guess it's my turn to share my gift."
    s "So...here."
    "Sayori hands me a neatly wrapped box."
    "It has a red ribbon holding it all together."
    s 1chc "Are you gonna open it?"
    mc "Do you want me to?"
    s "I wanna see your reaction."
    mc "Then I suppose I will."
    "I pull the ribbon and carefully tear the wrapping paper."
    "There's a blank cardboard box inside."
    s 1chq "Go on, open it."
    "I open the cardboard box and pull out..."
    mc "Is this a toy plush?"
    mc "Of me?!"
    s 2cha "Do you like it?"
    "The plush is actually quite cute."
    "I'd say it captures me pretty well."
    mc "It's a wonderful gift."
    mc "Thank you so much, Sayori."
    s 2chd "Aww, you really mean it?"
    mc "Of course I do."
    mc "You had this custom made, didn't you?"
    s "Mhm!"
    s 2chl "The guy I got it from even charged extra because there was a lot of people doing something like this."
    s "But I paid him anyway."
    mc "Huh? Why?!"
    mc "You don't need to go out of your way for me like that."
    s 2chd "It wasn't just for you."
    s "It was for everyone."
    mc "You got everyone else something similar?"
    s 1chl "Ehehe, yeah..."
    s "But now I have no money..."
    s "S-So..."
    mc "You're not getting any money from me."
    s 1chh "Aww, you big meanie!"
    s "It's Christmas!"
    mc "I know."
    "I give Sayori a hug and she returns it."
    mc "Merry Christmas, Sayori."
    s 1chq "Merry Christmas, [player]!"
    call giftexchange_revertmusic
    return

label giftexchange_natsuki:
    call giftexchange_startmusic("natsuki")
    scene bg ay_livingroom
    show natsuki 1chc zorder 2 at t11
    with wipeleft_scene
    n "Hmph."
    mc "What?"
    mc "I haven't even said anything yet."
    n 2chg "It doesn't look like you spent a lot of money getting me a present."
    mc "E-Eh?"
    mc "What gives you that idea?"
    mc "And besides, money isn't the most important thing."
    "She's right though."
    "I really didn't spend a lot of money."
    n "Call it intuition."
    n 2chb "But whatever."
    n "At least you got me something."
    n 1chg "And I guess I shouldn't be mad."
    mc "Here, you can judge for yourself."
    "I hand over her gift."
    n 1chi "I wonder..."
    mc "Are you gonna open it?"
    n 1chh "I haven't decided yet."
    "Natsuki eyes the present."
    "Her face give all the signs that she's excited to open it."
    n 1chf "Ah!"
    n "Alright, fine."
    n "You've got me curious."
    mc "You made up your mind that quickly?"
    n 1chs "It's this festive season."
    mc "You looked like you didn't want to open it just before."
    n "Doesn't mean that I don't actually want to open it."
    n 1chq "I wanna see what you got me, that's all."
    "Natsuki unwraps the present."

    $ nextscene = "gift_" + christmas_gifts[2] + "_n"
    call expression nextscene

    n 2chs "I guess you wanna see what I got you."
    mc "Well, it is a gift exchange."
    mc "Not a gift give and get nothing."
    n 2chg "Yeah, yeah."
    n "Here."
    "Natsuki presents me with a small box wrapped in pink paper."
    "She glares at me as she holds it out to me."
    n 2chf "Are you gonna take it or what?"
    mc "Right, sorry."
    "I take the present from her hands."
    n 4chc "So...?"
    n "Are you gonna open it or wait until tomorrow?"
    n 4chs "N-Not that I care."
    n "I'm just making conversation."
    mc "I guess I'll open it since you did the same."
    n 4chr "Whatever."
    "I carefully unwrap the present, there's a piece of foil inside."
    "I can see Natsuki staring from the corner of my eye."
    "I take out the foil."
    mc "This is..."
    "It looks to be a box of baked goods."
    "There's all sorts of stuff from cupcakes to croissants."
    mc "Did you bake these all by yourself?"
    n "What if I did?"
    mc "I'm impressed."
    mc "It really shows your dedication."
    n 2chy "I always give my best for the club."
    n 2chn "And besides..."
    n "You and the others helped me get through a rough patch."
    n "So..."
    show natsuki 2chs
    "Natsuki looks away."
    n 2chq "...you know, it wouldn't be right."
    mc "I understand."
    mc "Merry Christmas, Natsuki."
    n 1chk "Yeah, you too, [player]."
    call giftexchange_revertmusic
    return

label giftexchange_yuri:
    call giftexchange_startmusic("yuri")
    scene bg ay_livingroom
    show yuri 1chg zorder 2 at t11
    with wipeleft_scene
    y "..."
    mc "Is something wrong, Yuri?"
    y 1che "No..."
    y "Well...yes."
    mc "What is it?"
    y 2chq "It's petty, it doesn't really matter."
    mc "You can tell me anything, you know that."
    y 2chv "It's just..."
    y 3chw "I was about to win...!"
    "Yuri points to the cards on the table."
    mc "Oh."
    "I can't help but laugh a little."
    "It's such a small thing but so out of character for someone like Yuri."
    y 3cht "W-What's so funny?"
    mc "Oh, nothing."
    mc "It's just funny seeing you get upset about something so small."
    show yuri 3chr at s11
    y "Well, I'm glad you're finding humor in my demise."
    mc "I'm only kidding, sorry."
    show yuri 2chq at t11
    "Yuri smiles mischievously."
    y "Why don't you repent by showing me what you got me?"
    mc "I can do that."
    "I hand over my present to Yuri."
    "She elegantly unwraps it and pulls the present out of the box."

    $ nextscene = "gift_" + christmas_gifts[1] + "_y"
    call expression nextscene

    y 3chb "Here's your present."
    y "I hope you like it."
    mc "I'm sure I will."
    "Yuri hands me a small rectangular box neatly tied with a small ribbon."
    mc "I guess I'll open it then."
    y 3chf "Only if you want to."
    "I pull the ribbon off and the wrapping paper basically unwraps itself revealing a box with my name on it."
    mc "What is this?"
    y 2chh "Open the box."
    "I open the box and see a pen, one of those special, expensive ones."
    "It has my name etched on the side."
    mc "A pen?"
    y 2cht "You don't like it?"
    mc "Of course I do."
    y 2chv "It's just that I've noticed you writing with old ballpoint pens."
    y "I wanted to get you something better."
    y "Maybe you could use it to write your poems."
    mc "That's very thoughtful of you, Yuri."
    mc "You're right about the pens so I appreciate it."
    mc "I'm sure I'll use it a lot."
    mc "Merry Christmas, Yuri."
    y 3chs "M-Merry Christmas, [player]..."
    call giftexchange_revertmusic
    return

label giftexchange_monika:
    call giftexchange_startmusic("monika")
    scene bg ay_livingroom
    show monika 1cha zorder 2 at t11
    with wipeleft_scene
    m "[player]!"
    m "It's good to see you."
    mc "Good to see you as well, Monika."
    m 2che "I was trying to find a moment to share my gift with you but..."
    m "Well, it seems someone else kept taking up my time or you were busy talking to someone else too."
    m "So it looks like you're the last one I'm exchanging gifts with."
    mc "It's the same for me."
    mc "You're also the only person I haven't exchanged gifts with yet.."
    m "Ahaha, I can't wait to see what you got me."
    m 2chb "You didn't buy it last minute, did you?"
    mc "Um..."
    m "I see."
    m 2chj "Don't worry, I won't tell anyone."
    m "After all, I still owe you."
    mc "For what?"
    m 1che "I never really got to thank you for helping me sort out of my life."
    mc "Don't worry about it, really."
    mc "Any friend would have done the same."
    m 1chm "You really don't realize the extent of just how lost and miserable I was."
    m "You helped me get through it."
    m "You helped me see."
    m 1chn "I can never pay that back."
    mc "You've already paid me back by being a good friend."
    mc "Don't worry about it."
    m 1chh "Nonsense."
    m 1chb "There's still so much more I need to do."
    "Monika smiles thoughtfully."
    mc "Anyway, I'm just glad you could get a break after what you went through."
    mc "Letting her take care of the club for a bit while you needed to think it out was a really smart decision."
    m 1chc "You think so?"
    mc "I do."
    mc "After all, it let you recover to be the person you are today."
    mc "Our Monika, president of the Literature Club."
    mc "Slayer of demons, defeater of tyrants, champion of justice."
    m 2chl "Ahaha, what are you talking about?"
    mc "Just messing around."
    m 2che "You'll always be special to me, [player]."
    m "I hope you know that."
    mc "You're embarrassing me here."
    m 2cha "That's good."
    m "It's gonna make this gift a whole lot easier to give."
    mc "Would it help if I gave you my gift first?"
    m 1chb "It just might."
    mc "Then here you go."
    "I offer Monika the gift I wrapped for her."
    m "Whatever it is."
    m 1cha "I'm sure I'll love it."
    mc "I can only hope."
    "Monika unwraps the gift."

    $ nextscene = "gift_" + christmas_gifts[4] + "_m"
    call expression nextscene

    if christmas_gifts[4] == "bracelet":
        m 1chj "This bracelet is truly wonderful, [player]."
        m "The gift I'm giving you is nothing in comparison."
        mc "Whatever it is, I'll accept it wholeheartedly."
        m 1che "You will?"
        mc "I promise."
        m "Then..."
        m "Here."
        "Monika hands me a piece of paper."
        mc "What is this?"
        m 2che "Read it."
        call showpoem(poem_m_christmas, music=False, img="monika 1che")
        mc "It's a nice poem, Monika."
        m 2chc "You don't get it?"
        mc "Don't get what?"
        m "You don't feel that missing feeling?"
        m 4chd "Like there's something in your head that you just can't remember?"
        m "Like a part of you is missing?"
        mc "No...?"
        mc "Not really?"
        m 4chm "That's..."
        m 4chn "Well, I suppose that's not unexpected."
        m "I thought maybe I could evoke some thoughts within you."
        m 2che "To help you remember them."
        mc "Remember who?"
        m 2chc "I don't know."
        m "I wish I did."
        m 2che "I wonder if they're watching now."
        m "Seeing what's happening."
        mc "I honestly don't know what you're talking about."
        m 2cho "You know...neither do I."
        m 2cho "So why are these feelings lingering?"
        mc "I don't know."
        mc "But..."
        "I turn towards Monika."
        mc "I'll help you find out."
        mc "Whatever it takes."
        m 2che "...Thank you."
        mc "Your poem was a wonderful gift."
        mc "Merry Christmas, Monika."
        m 2chk "Merry Christmas, [player]."
        call giftexchange_revertmusic
    else:
        "Monika runs from the living room, taking the book with her."
        "I can hear...laughing?"
        "It's the crazy kind...not the laugh from Monika I'm used to."
        "I can only assume it's her and not one of the maids since it's coming from the direction Monika ran away to."
        "Maybe she likes the book...?"
        "Who am I kidding?"
        "She's probably laughing at how bad the book is and burning it now or something."
        "I should have known the book was a bad present."
        "I should have gotten her the bracelet."
        "It would have been a way better present."
        "It was so obvious!"
        show sayori 1chc zorder 2 at t11
        s "Hey, [player]."
        s "Where did Monika go?"
        mc "I don't know."
        s 1chb "Oh."
        mc "She said not to wait for her."
        mc "She's coming back though."
        s 2cha "That's good, she wouldn't just leave us."
        s "If she had to leave for a while, she's probably got something important to do then."
        s 4chq "Come on, let's go join the others."
        call giftexchange_revertmusic(False)
    return

label giftexchange_ayame:
    call giftexchange_startmusic("ayame")
    scene bg ay_livingroom
    show ayame 1chh zorder 2 at t11
    with wipeleft_scene
    ay "I hope my house isn't too intimidating."
    ay "Or messy."
    mc "Why would it be messy?"
    mc "You have plenty of maids to help clean it up, don't you?"
    ay 1chj "That's true."
    ay "It's just that the night before my parents were having a party."
    ay 1cha "Some of my friends decided to come over since I felt so miserable."
    mc "How come?"
    ay 1chg "Everyone around here is so boring."
    ay "All they do is talk about their investments and how they're gonna get more profits."
    ay "My parents only bear with them because they need to keep their image up."
    ay "I don't know how tiring it must be for them."
    mc "I can only imagine."
    ay 1chf "And sometimes, I think my friends are only talking to me because of my family's money."
    mc "Why do you think that?"
    ay 2chg "I'm weird, [player]."
    ay "Let's both admit it."
    ay "And I have weirder habits you don't even know about."
    ay 2chb "It's hard to be friends with me."
    mc "Ayame..."
    ay "But you [player_casual]s..."
    ay 2chh "You [player_casual]s accept me for who I am."
    ay 2chb "And I feel...whole for some reason."
    ay "I don't really know what I'm talking about."
    ay "So..."
    mc "It's okay, I think I get it."
    mc "It's been good getting to know you."
    mc "I'm glad you joined the club, Ayame."
    ay 1chd "Me too."
    ay "But!"
    ay 2chb "It's time for the gift giving."
    ay "Shall I go first or you?"
    mc "I'll go first."
    mc "My gift is going to pale in comparison to yours."
    ay 1chg "Don't say that."
    mc "It's true."
    "I give Ayame the present I bought."
    "I didn't notice yesterday but the clerk somehow encased it in glass to protect it."
    "I managed to wrap it carefully enough to avoid scratching the glass or breaking the fossil."
    ay 2chi "Whoa, what is this?"
    mc "It's a fossil, I think."
    ay "You think?"
    "Ayame holds the fossil in her hands."
    "She looks around it carefully."
    ay "What kind of marking is that?"

    $ nextscene = "gift_" + christmas_gifts[3] + "_ay"
    call expression nextscene

    ay 1chb "And now you've learned something personal about me."
    mc "I guess I have."
    ay "Do you want my gift now?"
    mc "It's definitely going to be better than some rock I gave you."
    ay 1chj "Nonsense."
    "Ayame claps her hands."
    ay "Bring it in!"
    "One of Ayame's maids brings in a large box and places it on the floor in front of me."
    ay "Thank you!"
    "The maid bows and leaves."
    ay 1chb "This is what I had to take care of before."
    mc "What is it?"
    ay "Open it and find out."
    "My present definitely sucks compared to this."
    "I slowly unwrap the present, revealing some kind of mini wardrobe."
    "It's big enough that you could fit a couple of clothes inside comfortably."
    mc "A wardrobe?"
    ay 2chh "Oh, you're not getting that."
    mc "That's good, I had no idea how I was going to bring that home."
    ay "Have a look inside."
    "I open the wardrobe."
    if player_gender == "boy":
        "Inside, there's three different suits."
    else:
        "Inside, there's three different dresses."
    "They're in different styles to one another."
    "All three of them look absolutely incredible."
    "They look like something someone with a lot of money would wear."
    mc "Are those mine?"
    ay 2che "Yep!"
    ay "Sayori told me you didn't have a lot of formal clothing."
    ay "I thought I'd buy you some in case you ever needed any."
    mc "How much did those costs?"
    ay 2chj "They were tailor made so..."
    ay "Well, let's not worry about the costs!"
    ay "My family can afford it."
    mc "Just...wow."
    mc "This would make even someone like me look good."
    ay 1che "Aww, don't put yourself down like that!"
    "Ayame smiles gleefully."
    ay 1chj "I got Sayori to snoop around your wardrobe to get some rough estimates."
    ay "So hopefully they all fit you."
    ay "If not, just let me know and we'll sort it out."
    mc "You what?"
    ay 1chg "I'm sorry."
    ay "But I didn't know any other way."
    ay "I hope it isn't a problem."
    mc "No harm done."
    ay 1chj "Oh, that's good."
    ay "You probably think I'm really weird, don't you?"
    mc "Maybe, but I see that as a good thing about you."
    ay 1chb "You do?"
    mc "Yeah, so thank you, Ayame."
    ay "Don't mention it."
    ay 1chd "Happy holidays, [player]!"
    mc "Merry Christmas, Ayame."
    call giftexchange_revertmusic
    return

label gift_plush_s:
    $ christmas_approval += 1
    s 1chm "Oh my gosh!"
    s 4chr "It's so cuuuuuuuuuuuuuuuuuuuuuuute!"
    show sayori at h11
    s 4chq "Thank you, thank you, thank you, [player]!"
    mc "You're really into this, aren't you?"
    s 2chd "Why wouldn't I be?"
    s "Doing this is so much fun!"
    mc "Does it look familiar at all to you?"
    show sayori 2chn
    "Sayori stares at the cow plush I bought her."
    s "It's..."
    s 2chm "It's the same one from my room!"
    mc "That's right."
    s 2chq "That's even better!"
    s "It's like a smaller version of it."
    s "This is incredible."
    mc "I think you're overstating what's really happening."
    mc "But I'm glad you're enjoying it."
    return

label gift_book_s:
    s 1chb "Eh...?"
    s "A book?"
    s 1chh "How Not To Break Things As A Manager?"
    mc "You don't like it?"
    s 2chl "I-I never said that."
    s "I'm just wondering about a couple of things."
    mc "What is it?"
    s 2chj "Why would I need a book like this?"
    s "And what kind of name is Clark Nick Mysterio Maximilian?"
    mc "I thought if you ever started your own club, you could use it."
    mc "Or maybe if you ever became a manager."
    s 4chl "I see..."
    s "Thanks, I guess."
    mc "And the name?"
    mc "I had no idea that was the author's name."
    s 4chq "Ehehe, did you even really think about this gift?"
    mc "..."
    s 4chd "It doesn't matter."
    s "I'm grateful anyway, [player]."
    mc "I'm glad you're in good spirits, Sayori."
    return

label gift_manga_n:
    n 1chc "You got me a..."
    "She lifts up the volume of manga I got her."
    n 2chb "Volume of manga?"
    mc "Yeah, seeing as you're a big fan of it and all."
    mc "I thought it looked cute and it reminded me of you."
    n 2che "W-What?!"
    n "Hey!"
    "Natsuki punches my arm."
    n 2chf "You can't just say something like that!"
    mc "Anyway, what do you think of it?"
    n 2chk "I'm reading the first couple of pages now."
    "I stand in silence as Natsuki reads the first few pages."
    n 2chh "What is up with this art style?"
    mc "I thought the same thing."
    mc "Maybe it's part of it's charm or something?"
    n 1chi "Well, whatever."
    mc "You don't look impressed."
    n 1chg "I've read the first few pages."
    n "Pardon me if I don't sound ecstatic about it."
    "Natsuki sighs."
    n 2chs "Look, that wasn't meant to sound rude or anything."
    n 2chq "I'm grateful for the gift, really."
    mc "If you say so."
    return

label gift_anime_n:
    $ christmas_approval += 1
    n 2chk "It's a big box."
    n "What's in here?"
    mc "You'll see."
    "Natsuki opens the box."
    "She pulls out one of the disc covers holding a volume of Parfait Girls."
    n 2chm "The anime of Parfait Girls?"
    n "I...didn't even know this existed."
    mc "Really?"
    mc "To be honest, neither did I."
    n 1chc "It must be recent."
    n "I can't believe I didn't see it in the current season of anime."
    n 1chq "This must have cost you a fortune."
    n "I'm sorry for doubting you."
    mc "Don't be."
    mc "The guy who was selling it to me gave it to me for really cheap."
    mc "So, in a sense, I guess I really didn't spend a lot on your gift."
    n 1chm "I'm still grateful."
    mc "It could be pretty bad."
    mc "You and I both know there are some anime adaptations that are..."
    mc "...questionable, to say the least."
    n 1cht "Ahah! You're so right!"
    n 2chc "Still, I'm really excited to see those characters all animated."
    mc "I'm glad to hear it."
    return

label gift_knife_y:
    $ christmas_approval += 1
    y 2chf "Is this...some sort of knife?"
    mc "Yes, I think it is."
    "Yuri takes it out of it's scabbard."
    y 2chj "Wow."
    "She places her finger on the tip of the knife."
    "A bit of blood comes out from her finger."
    mc "Careful!"
    "She puts her finger in her mouth to stop the bleeding."
    y 2cha "It's okay, I'm used to it."
    y "I just wanted to test how much it's been sharpened."
    mc "And?"
    y 2chi "It's made of wood and is just as sharp as any other knife."
    y 2chf "The craftsmanship is unmatched."
    mc "You know, that's what the shopkeeper said."
    mc "I really wasn't sure if getting you something like this would be a good idea."
    y "Why not?"
    mc "Because these are part of the problem when you..."
    mc "You know."
    y 2chg "That's not really true."
    y "The problem was in my mentality."
    y 1chk "Knives don't hurt people, [player]."
    y "It's the people wielding them that hurt people."
    mc "I guess so."
    y 1chc "Regardless, thank you for this gift."
    y "This type of knife is something I never knew I wanted."
    mc "I'm glad you're enjoying it."
    "Yuri places the knife back into the scabbard."
    return

label gift_ARM_y:
    y 1chf "Can I ask what this is exactly?"
    y "It looks like some kind of contraception..."
    y 1chq "But I can't really decipher how to use it."
    mc "It's called an ARM."
    mc "An Automated Responder Mechanism, I think."
    y 1cho "I-I see..."
    mc "You put it on your arm and it will deter you from cutting yourself."
    y 3chp "W-What?!"
    mc "Ah...sorry."
    mc "Still a sensitive topic."
    y 3chq "It's fine...but what do you mean?"
    mc "About what?"
    y 2chf "About it deterring me?"
    y "It's just a metal thing that goes around my arm."
    y 2chg "That's hardly going to...you know."
    mc "I think the shopkeeper said something about magnets?"
    mc "I'm not too sure."
    y 3chk "Well."
    mc "What is it?"
    y 3chq "I don't know."
    y "This seems a bit...clunky to me."
    y "I can't imagine wearing this to school."
    mc "I guess not."
    y 3chg "And I don't really have that sort of problem anymore."
    mc "Just in case."
    y 2chf "I suppose I'm glad you're looking out for my wellbeing."
    y 1cha "So thank you."
    "Yuri puts the ARM back into box."
    return

label gift_bracelet_m:
    $ christmas_approval += 1
    mc "It's a bracelet."
    mc "Some guy suggested I buy it for you."
    m 2chd "Some guy?"
    mc "At this store."
    mc "It's where I bought the others gifts too."
    m 2che "And I suppose you didn't buy them all a bracelet too?"
    mc "No, I got everyone something different."
    "Monika examines the bracelet."
    m 2chc "It's very beautiful."
    m "It feels handcrafted with love."
    m 2che "Like someone's whole dedication went into making this."
    mc "It does?"
    m 1cha "Yeah, I can just sense it."
    mc "Why don't you put it on?"
    mc "According to the clerk, it's infused with happiness."
    m 1chl "Infused with happiness?"
    m "For some reason, I highly doubt that."
    mc "Me too, but you never know."
    "Monika puts on the bracelet."
    m 2chd "W-Wow."
    m "That's incredible."
    mc "What happened?"
    m "I feel so...happy all of a sudden."
    mc "You're not just messing with me because I said that, right?"
    m 2chb "No, I'm serious."
    m "This bracelet is magical."
    mc "And it's yours now."
    m 2cha "It's a wonderful present."
    mc "That's not all."
    mc "There's a small button on the top."
    mc "Click it."
    m 2chc "Okay."
    "Monika presses the button."
    "The same theme from before plays."
    m 2chd "This is..."
    mc "What is it?"
    m 1che "It sounds like a song I stopped composing."
    m "The start of it, anyway."
    mc "It does?"
    mc "That's probably a coincidence."
    m 1chc "Do you know where you went to buy this?"
    mc "I don't remember the name of the store."
    mc "But it was somewhere in the mall."
    mc "I can take you there, if you want."
    m 1chb "I might take you up on that offer."
    return

label gift_Markov_m:
    m 1chc "A book?"
    mc "Yeah, I thought you might like it."
    mc "Seeing as we are in a club about literature, lead by you."
    m 1che "That makes sense."
    m 1chc "The cover is very ominous."
    m "A red eye?"
    m 2chd "Kinda creepy, if you ask me."
    mc "You don't like it?"
    m 2chl "I never said that...!"
    m "I'm sure once I read it, I'll really enjoy the story."
    mc "You don't have to force yourself to like it."
    mc "If I messed up, you can let me know."
    m 2chf "Don't say that."
    m 1che "Look, I'm really eager to read it."
    m "I'll read the first couple of pages now."
    "Monika takes the plastic off the book and turns to the first page."
    mc "Monika--"
    m 1cha "Let's see here, \"chapter one, inner demon\". What a strange name for a first chapter."
    mc "Monika, you don't need to prove yourself to me."
    "She seems to ignore what I said."
    m 1chc "And look at these words to begin with, it's like some sort of chant or incantation or something."
    $ config.allow_skipping = False
    $ config.skipping = False
    m 1chd "{cps=20}Evigilare...{w=0.3}faciatis...{w=0.3}mali...{w=0.3}dorimienti?{/cps}"
    m 1cha "I think that's right.{w=1.0}{nw}"
    stop music
    stop music_poem
    show monika gcha
    $ pause(2.0)
    $ config.allow_skipping = True
    show monika 1chc
    mc "Is something wrong?"
    m "I..."
    "Monika looks around wildly."
    "It's as if she doesn't know where she is."
    m 1che "I think I need to go for a second."
    m "I'll be back, don't wait for me."
    show monika at lhide
    hide monika
    return

label gift_Xileh_ay:
    $ christmas_approval += 1
    ay 1chh "Some kind of snail?"
    mc "I think so, yeah."
    ay 1chi "Really?!"
    ay 1chd "This is incredible!"
    mc "What...?"
    ay 1che "All hail the snail!"
    "Ayame begins bowing her head down to the fossil."
    mc "Is there something special about this fossil?"
    ay 2chb "It's a fossil, [player]!"
    ay "It's already special."
    ay 2chi "How did you even get this?"
    mc "It's a long story."
    ay 2chj "Anyway, I love fossils."
    ay "They're so fascinating, don't you think?"
    mc "I guess."
    ay 2chd "They're like a glimpse to the past."
    ay "A window to see what once was."
    mc "When you look at it that way, it does make sense."
    ay 1chh "Thank you for this."
    ay "It's a bit of a hobby of mine to collect them."
    ay 1chd "If you go to my room, I've got plenty on display."
    mc "Really? So it's like a mini museum in your room."
    ay 1che "Ahah, I guess it is."
    return

label gift_Edom_ay:
    ay 1chi "Some kind of...crab?"
    mc "I guess so."
    ay 1chg "I see."
    ay "I like prehistoric fossils, [player]."
    ay "Thank you."
    mc "You don't sound impressed."
    ay 1chb "Oh, I am."
    ay "Don't get the wrong idea."
    ay "How you even came about this is beyond me."
    ay 2chg "It's just..."
    mc "What is it?"
    ay "I had a traumatic accident with a crab once."
    ay 2chf "My family avoid crabs like the plague because of me."
    ay "I almost lost my fingers that day to a crab."
    ay 2chc "Can you imagine?"
    ay "Losing fingers to a crab?"
    mc "I couldn't really."
    mc "I don't go to the beach very often."
    ay 2chg "The point is..."
    ay "It still gives me nightmares to this day."
    mc "It does?"
    mc "I'm so sorry!"
    mc "I didn't know."
    ay 1chj "Ahaha, it's fine."
    ay "There's no way you could have known that."
    return

label christmas_chapter:
    # Alternate Reality?
    $ chapter = 999
    scene black
    if from_custom_start:
        $ from_custom_start = False
        $ quick_menu = True
        hide screen tear
    $ s_name = "???"
    $ cl_name = "???"
    $ audio.t11r = "<from 0 to 96.0 loop 0>mod_assets/bgm/11r.ogg"
    play music t11r
    s "..."
    if persistent.did_special_event:
        s "We're going back again, aren't we?"
    else:
        s "Are we going backwards?"
    s "Or...is it forward?"
    scene bg random_gray
    $ style.say_window = style.window_flashback
    s "Do events like this even exist in our world?"
    s "I'm not really sure myself."
    s "I've lived enough years to know whether it should or shouldn't exist."
    s "At least, to me I have lived a long time."
    s "That's what my memories are telling me anyway."
    s "To you, I could just be completely new."
    s "Maybe I'm just a month old to you."
    s "But from my memories, I can't really give an answer."
    s "I just {i}know{/i} that I've been alive longer than you've known me."
    s "Our world is based off of yours but..."
    s "Ahaha, never mind..."
    s "I shouldn't complain."
    s "This is good for us."
    s "It's nice to have a little rest, I guess."
    s "The time we're going to is Christmas Eve..."
    s "I know all about it."
    s "And yet, I don't know if that's because I've experienced it before..."
    s "...or because I've looked into it in your world."
    s "Whatever it is..."
    s "Don't ruin this for us."
    s "Please."
    s "I just want us all to be happy."
    s "Even if it isn't really our world."
    s "That isn't too much to ask for...right?"
    s "It's just a moment of happiness in this uncertain world we're in."
    s "I need you to be able to do this, but if you're just going to ruin everything then I'd rather not do it at all."
    menu:
        s "You understand, right?"
        "Yes.":
            pass
        "Of course.":
            pass
        "Sure...":
            pass
        "No.":
            s "You don't?"
            s "Then I guess there's really no point in you being here, is there?"
            s "Come back when you're ready to do the right thing."
            $ renpy.utter_restart()
    s "Thank you."
    s "I'm glad we're on the same page."
    s "And remember, you have to persevere."
    s "Even if it seems hopeless."
    s "Just keep trying."
    s "Break through."
    s "Ehehe, sorry~"
    s "You might not even know what I mean..."
    $ config.skipping = False
    $ config.allow_skipping = False
    s "{cps=15}But I really hope you know what you're doing...{/cps}{w=0.5}{nw}"
    stop music fadeout 1.5
    scene bg mall_interior with Dissolve(1.5)
    play music t2 fadein 3.0
    $ insert_characters_alternate(mc=True,ayame=True,timeline=7)
    $ s_name = "Sayori"
    $ style.say_window = style.window_christmas
    $ config.allow_skipping = True
    "I'm completely useless here."
    "I've been to a dozen stores but..."
    "I don't know the girls well enough to get each of them the right gift!"
    "What am I going to do?"
    "I'm just wasting my time here..."
    "I really should have bought gifts earlier."
    "And not on Christmas Eve."
    "I guess I shouldn't have procrastinated so much."
    "Monika is always telling me to get things done as soon as possible."
    "I've tried to follow her advice but it doesn't really suit me."
    "I can do my homework and whatever I need to do for school just fine."
    "But when it comes to other things, it feels like I just procrastinate until the last minute."
    "Now...back to shopping."
    "Maybe I should start with something easy."
    "I think out of everyone..."
    "I, at least, know what Sayori would want out of a Christmas present."
    "What did I get her last year?"
    "Maybe I can use that as some sort of base."
    "..."
    "I have no idea what I got her last year."
    "In fact, did I even get her anything?"
    "We've been so out of touch since our childhood until recently."
    "We're reconnecting and closer than ever now."
    "And it's all because of the Literature Club."
    "But that still leaves me clueless as to what to get her."
    "When we were younger, anything would make her happy."
    "I could have gotten her some chocolate and she would scream like it was the best thing ever."
    "Could I still do something like that?"
    "Or would that look like me just being cheap?"
    scene bg anticshop with wipeleft_scene
    play music t17 fadeout 2.0
    "I wander around the mall for a bit, not really paying attention to where I'm going."
    "I've just been trying to figure out what to get everyone but I'm out of ideas."
    show mysteriousclerk 1chk zorder 2 at t11
    $ get_achievement("*Good Guy Clerk*")
    cl "Hey there, little [player_other]."
    cl "Watch where you're going."
    "A strange looking man appears in front of me."
    "He seems to be stocking the shelves with...something."
    "It looks like some kind of plant...?"
    "Which is odd because the rest of the store is filled with books and electronics."
    "From what I can see, at least."
    "I don't even know how I got into this store."
    "Was I really thinking too much about what to get everyone that I didn't even realize I walked in here?"
    mc "S-Sorry, I wasn't really paying attention."
    show mysteriousclerk 1chf
    "The man looks as if he is scanning me."
    cl "Let me guess."
    cl "You're buying last minute Christmas gifts."
    cl 2che "It's for four...no five people."
    cl "And they're all women."
    mc "What?"
    mc "How did you get that just from looking at me?"
    cl 2cha "You pick up a few tricks when you're my age."
    mc "Like how to read a person?"
    cl "Something like that."
    "Who is this guy...?"
    cl 4chb "I'm the owner of this fine establishment."
    "Did I even say that out loud?"
    "If not, why the hell did this guy just introduce himself like that all of a sudden?"
    cl "The executive officer of this humble abode."
    cl "The master of this venerable estate."
    cl "The--"
    mc "Alright, I get it."
    mc "How did you know I was wondering who you were though...?"
    cl 4chd "Like I said, you pick up a few tricks."
    mc "..."
    cl 1cha "Anyway, what can I do for you?"
    cl "Want some help getting some gifts?"
    mc "What?"
    mc "No, of course not!"
    mc "Especially not from--"
    cl 1chf "Please, my friends call me Clark."
    $ cl_name = "Clark"
    cl 2che "But that's not actually my name!"
    cl "So change it back to those question marks!"
    "What...?"
    $ cl_name = "???"
    cl 2cha "As I was saying..."
    cl "You aren't my friend either."
    cl 2chb "So instead, you may call me Nick."
    $ cl_name = "Nick"
    mc "Right...Well, I was just about to leave, {i}Nick{/i}."
    mc "So, if you don't mind."
    "I try to make my way past him but he blocks my way."
    cl 4che "Ho, ho, ho little [player_other]."
    cl "Are you sure you wanna do that?"
    cl "I know exactly the sort of thing those girls would like."
    cl 3chb "Well, it's more of a fifty-fifty."
    cl "But it's better than getting them nothing, am I right?"
    mc "Look, I'm not sure how exactly you knew this much already."
    mc "But I really doubt you know enough about those girls to know what gift to get them."
    cl 1chb "Is that a test?"
    if player_gender == "boy":
        cl 1chi "Good sir, are you challenging my knowledge?"
    else:
        cl 1chi "Madam, are you challenging my knowledge?"
    "I let out a quiet sigh."
    "I just want to get out of here."
    "This guy is seriously getting on my nerves."
    cl 1chf "The girl you were thinking of just before."
    cl "She has coral pink hair and eyes as blue as the sky."
    cl "She's clumsy but she has everyone's best interest as heart."
    cl "She's the nicest person you know and she's always looking out for others."
    cl 1chb "She's the main reason you're even out here doing this."
    cl "Because without her, you would have never met the other four."
    mc "What...?"
    cl 2chc "Tell me I'm wrong."
    "There is no way this guy could have figured that out just from looking at me."
    "This has got to be some kind of trick."
    "Did Sayori set this guy up?"
    "But then how would she have known I'd end up here?"
    cl 2cha "Just hear me out, okay?"
    cl "It's literally the only reason I'm here."
    cl "You can make the decision in the end."
    mc "Fine."
    cl 2chb "Splendid!"
    cl "Right this way."
    "The man takes me to a section of the store."
    "There's all sorts of fluffy animals here."
    "I guess the store has more than just books and electronics."
    cl 1chf "Now any of these would probably do great with her."
    cl "But let's be honest, anything you give her would make her day."
    cl "Unless it's something crazy and offensive, right?"
    mc "I suppose."
    cl "If you don't like those then maybe something more shocking will do."
    mc "Shocking? I don't think--"
    cl 1chb "Like this incredible limited time offer on this book."
    cl "It's called \"How Not To Break Things As A Manager\", it's ninety percent off."
    cl "What do you say, [player]?"
    "I didn't even tell him my name...did I?"
    mc "What?"
    mc "Why would she need this?"
    mc "What use would--"
    cl 1chh "You're in some kind of book club, right?"
    cl "This is a book."
    cl "See the connection?"
    "The man taps his finger on his head."
    mc "I...guess?"
    mc "But I'm definitely not going to--"
    cl 1cha "It's {i}your{/i} choice, okay?"
    cl "I ain't gonna force you to do anything."
    cl "Just be sure you actually know what you're doing."
    cl 1chb "If you don't...well, there might be consequences."
    mc "What kind of consequences?"
    cl "Consequences that could affect other worlds, you know?"
    "I've made up my mind."
    "This guy is insane."
    cl 1chd "Just kidding, none of this really matters."
    mc "Sure..."
    menu:
        mc "In that case, I'll take the..."
        "Cow plush.":
            $ christmas_gifts[0] = "plush"
            "Sayori has one of these already."
            "Or at least, something similar to this in her bedroom."
            "I'm sure she'd appreciate a miniature version."
            "It's cute and...well, Sayori will like it."
            "I'm sure."
        "Management book.":
            $ christmas_gifts[0] = "book"
            "Well..."
            "We are a club about literature."
            "I guess this book would help her."
            "Somehow."
            "Even though she's not the president of the club."
            "Maybe she could still use it if she ever decides to start her own club or something."
            "I just hope she doesn't take it the wrong way."
    mc "I'll take the--"
    cl 4chb "Great!"
    "Without even letting me finish, Nick takes the [christmas_gifts[0]] and puts it into a plastic bag."
    "Did he know I was going to go for that?"
    cl "Now moving on."
    cl 2chb "How about we get a gift for the tall one?"
    mc "The tall one?"
    cl "The creepy one."
    mc "Creepy one? No one is--"
    cl 2che "You know the one, likes horror books..."
    cl "Has a knife collection..."
    mc "What?!"
    cl "The gifts for her are right over here."
    cl "So come on!"
    cl 2chf "Get a move on!"
    cl "You don't have much time, let's go, let's go."
    mc "Jeez, I'm going..."
    mc "Can you at least tell me how you learned all of this information?"
    mc "I know you said you picked up a few tricks but..."
    mc "What the hell does that even mean?"
    mc "There's no way you can just know everything about someone from looking at them."
    cl "Who said I knew everything about you?"
    cl 1chg "The mundane things about a person are not my specialty."
    cl "I wouldn't care to learn those things about someone."
    cl 1chi "Like your favorite color."
    cl "Who even cares about that?"
    cl "Like come on, really?"
    mc "So you've learned about me?"
    mc "How?"
    cl 5chg "Oh, I said that out loud."
    cl "Well, never mind!"
    cl "Forget I said anything."
    mc "No, now I'm curious."
    mc "Tell me, come on."
    mc "I deserve to know how you know so much about me."
    mc "Are you my stalker or something?"
    cl 5chf "What? No!"
    cl "That's way too creepy."
    cl "It's simply--"
    cl 5che "Wait, why am I being interrogated by some kid?"
    "Nick points to another place in the store."
    cl 3chb "Come on, move it."
    cl "Or don't you want to get the rest of them something?"
    cl "So how about you stop asking questions and I'll help you pick out the rest of the gifts?"
    mc "Okay, I can deal with that."
    cl 3chc "Splendid, just splendid!"
    cl "And here we are..."
    "We arrive at the section of the store stocking...sharp objects."
    "That's probably the best way to describe it."
    "There's a lot of sharp things on display, half of which I don't know the name of."
    "There's even a katana for sale and the sign says authentic."
    "What does that even mean?"
    cl 3chb "Now you can either choose this really cool looking knife here."
    "Nick points to a small ornate knife with intricate designs on it."
    "The shape of it is completely unique, unlike anything I've seen and each edge looks like it was carved with care."
    "It has its own matching scabbard to place it in too."
    cl "She'll love this."
    mc "How can you know that for sure?"
    cl 3che "Young [player_other], look at the craftsmanship on this."
    cl "You won't see this anywhere else."
    cl "It's one of a kind."
    cl "Tell me that isn't top quality, top notch stuff."
    mc "I don't know much about knives."
    mc "So I can't tell you otherwise."
    mc "It does look really nice, I suppose."
    cl "She'll love it."
    cl 1chc "But..."
    cl "There is an alternative, you know."
    mc "And what exactly is that?"
    cl 1chd "Well, you and I both know she has a habit of..."
    cl "Ehm."
    "He makes a slicing gesture on his arm."
    cl "Or, at least she did."
    cl "Who knows if she still does?"
    cl 1chi "Hint, I do."
    mc "What's your point?"
    cl "I've got just the thing to prevent that kind of thing ever happening again."
    "Nick points to the display opposite the knife."
    cl 2cha "I call it the Automated Responder Mechanism."
    cl "Or ARM for short."
    cl "It goes on your arm and every time you'll try to cut it..."
    show mysteriousclerk at h11
    cl 2chb "Bam!"
    "The clerk claps his hands together."
    mc "Bam?!"
    mc "Why would I want that to happen?"
    cl 2che "It was a figure of speech."
    cl "What I meant was, it will automatically activate some magnets and keep the knife stuck to it for a while."
    mc "What if she has like a wooden knife or something?"
    cl 2chf "Kid, who in the world uses a wooden knife?"
    mc "Isn't that knife over there made of wood?"
    "I point to the knife he showed me earlier."
    cl "Uhhhhhhhhhh..."
    show mysteriousclerk at h11
    cl 1chg "Look!"
    cl "It's the thought that counts, okay?"
    cl "By buying this, you're showing her you care about her wellbeing."
    cl 5cha "So make your choice."
    mc "Okay, let me think."
    menu:
        "It only seems logical to take the..."
        "Knife.":
            $ christmas_gifts[1] = "knife"
            "I think I remember Yuri having a collection of knives."
            "I haven't seen anything like this before."
            "And he said it's one of a kind, so I doubt she'd have something like this already."
            "I'm sure she'd appreciate this."
        "ARM.":
            $ christmas_gifts[1] = "ARM"
            "Would Yuri really appreciate this?"
            "I don't know for sure if she's stopped cutting herself."
            "If she has then this gift would be pointless."
            "Would she take offense to something like this?"
            "I'm just looking out for her, after all..."
    mc "I've given it a lot of thought."
    mc "I think I'll take the--"
    cl 5chb "Wonderful, absolutely wonderful!"
    cl 2chb "Immediately, the clerk places the [christmas_gifts[1]] into the same plastic bag."
    mc "Did you just refer to what you were doing in the third person?"
    cl 2cha "What of it?"
    mc "Never mind."
    cl 2che "Who next?"
    cl "Ooh, how about that tsundere girl?"
    mc "Tsundere girl?"
    cl "You know the one."
    cl "I'm sure."
    mc "Eh...?"
    cl 2chi "Now I'll divert your attention over here."
    "The clerk starts moving around the store again at a much faster pace than before."
    mc "Does anyone else work here?"
    cl 1chb "Nope, it's a family business."
    cl "By family, I mean my family."
    cl "By my family, I mean--"
    mc "I don't really need to know the details."
    cl 1chc "Suit yourself, kiddo."
    cl "Anyway, we're here."
    "Nick presents a whole lot of manga and anime to me."
    "I guess we're in that section of the store now."
    "This store seems to have everything in it."
    "I thought the books on the shelves were just novels or something."
    "But as it turns out..."
    cl 1che "Hmm..."
    cl "Now where was that manga...?"
    cl "Oh, yes!"
    cl 3chd "Here it is."
    "He hands over a single volume of a manga I've never seen before."
    mc "What's this?"
    cl "What's it look like?"
    cl 3chi "It's obviously a stapler."
    "The manga he gave me is called \"Donut Purr Chase\" and features a cute cat on the front cover."
    "I look at the first few pages."
    "I can't really get what the story is about."
    "The art is also...questionable."
    "Some panels have extremely good detail while others are literally stick figures."
    mc "I don't know if she'll like this."
    cl 4chk "Why not?"
    cl "It's really quite sweet."
    cl 4cha "I mean that literally, like try smelling it."
    "The book does somehow give an aroma of freshly baked cupcakes."
    cl "The story is..."
    cl 4chb "Well, that's spoilers."
    cl "If you don't want to get her that, then..."
    cl 3chc "There's always this."
    "The clerk holds out a small box labeled--"
    cl "Parfait Girls, the complete collection."
    cl "In anime form."
    mc "That would be nice."
    mc "But I think she already has that, doesn't she?"
    cl 3chb "No."
    cl "She has the collection of manga."
    cl "Not the anime collection."
    mc "How do you know?"
    cl 3cha "Look, this is on sale for ninety percent off."
    cl 3chd "It's...clearance."
    cl "So you can take the single volume of manga or this collection."
    cl "They'll be around the same price anyway."
    mc "If I buy the anime collection and she already has it, then what?"
    cl 3chf "If you buy the manga and she doesn't like it, then what?"
    cl "Maybe you won't get any cupcakes at your little Christmas party."
    cl "Just make up your mind, [player_gender]."
    mc "What do you think I should get then?"
    "The clerk shrugs."
    cl 4chh "Not my choice to make."
    cl "So what will it be?"
    mc "Um..."
    menu:
        mc "Give me the..."
        "Manga.":
            $ christmas_gifts[2] = "manga"
            "I guess the cat does look cute."
            "She doesn't say it but I know Natsuki likes cute things."
            "I don't know about the story but there doesn't seem to be anything too weird from what I've seen."
            "What's the worst that could happen?"
        "Anime collection.":
            $ christmas_gifts[2] = "anime"
            "I know for a fact that she likes Parfait Girls."
            "Some people like the manga but don't like anime adaptations."
            "I hope Natsuki isn't one of those people."
            "And the clerk seems sure that Natsuki doesn't have this so it would be a pretty good gift."
    mc "Can you give me the--"
    cl 1cha "Done and done."
    "The clerk basically shoves the [christmas_gifts[2]] into the plastic bag."
    cl "Who next?"
    cl 1chb "How about the new girl?"
    cl "I know you need help picking out a gift for her."
    mc "What gives you that idea?"
    cl 1chc "For one, you barely know her."
    cl "Haven't you only spoken to each other a couple of times?"
    mc "Well...yeah but--"
    cl 1chf "And two, the only thing you do know about her is that she's super rich."
    cl "Which means..."
    cl "She has everything she could ever want."
    mc "Ah...that's true."
    mc "I have no idea what to get her."
    mc "Even if you suggested something to me, I wouldn't know if that would be a good or bad thing to get."
    cl 1chd "Luckily for you, I know her quite well."
    mc "And how would--"
    cl 2chc "She came in here before, you know."
    cl "Granted, she didn't buy anything."
    cl 2chb "She said I was \"too weird\" and left."
    cl "But what she didn't know is that I already read her like a piece of source code."
    $ _history_list[-1].what = "\"But what she didn't know is that I already read her like a book.\""
    mc "Like a what?"
    cl 2che "Like a book."
    cl "Did you not hear me?"
    mc "Uh...right."
    mc "So what did you learn about her that I could help me choose a gift for her?"
    cl 2chi "I only got a short glimpse."
    cl "But I think I have just the things."
    cl "The clerk directs [player] to the section of the store filled with artifacts."
    $ _history_list[-1].what = "The clerk directs me to the section of the store filled with artifacts."
    $ _history_list[-1].who = None
    "He's doing it again."
    $ _history_list[-1].what = "\"He's doing it again.\""
    $ _history_list[-1].who = player
    cl 4chl "What am I doing?"
    "He heard me? I swear I didn't say that."
    mc "You referred to yourself in the third person."
    cl 4chm "I assure you, I didn't."
    cl 3chi "Why don't you check your recent {i}history{/i}, [player]?"
    "Recent history?"
    "It feels like the more I talk to this guy, the more brain cells I lose."
    cl 3chg "Jeez, kids these days."
    "The clerk shakes his head in disapproval."
    cl 1chb "But I'm not here to lecture you."
    cl "I'm here to help you get these fancy looking artifacts as a gift."
    mc "Which one would she like?"
    cl 1cha "All of these are exclusive artifacts dug by my very own debuggers."
    $ _history_list[-1].what = "\"All of these are exclusive artifacts dug by my very own archaeologists.\""
    cl "So any of them would be perfect."
    cl 1chc "But since I know you're clueless and all."
    cl "I'd recommend one of these two."
    "He points me towards two strange looking rocks."
    cl "I call these two the monster fossils."
    cl "They're not really traditional artifacts but there is some sort of mystical presence within them."
    cl 1chb "So I call them artifacts."
    mc "Why would she want monster fossils?"
    mc "But more importantly how can you afford to--"
    cl 1chf "Let's focus on the gifts okay?"
    cl "She may not look it but she's actually a hunter."
    cl "When she has time, she likes to go hunting with her parents."
    mc "Interesting but that has nothing to do with why she'd be interested in monster fossils..."
    cl 1che "Or does it?"
    "The clerk stares at me intensely."
    mc "...It doesn't."
    cl 1chf "Or does it?!"
    mc "It really doesn't."
    cl 1cha "That's true, I guess."
    cl "So which fossil will it be?"
    cl 2chb "The Xileh fossil..."
    "The clerk points to the fossil with what looks like a snail carved onto it."
    cl 3chb "...or the Emod fossil?"
    "He points to the other fossil which has some sort of crab on it."
    cl 1cha "Choose carefully."
    cl "If you choose the wrong one, you might anger all the wrong people."
    cl 1chl "Including Ayame."
    cl 1chb "Just kidding, she doesn't really get angry."
    cl "No one does, at least in this reality."
    mc "How the hell am I suppose to choose then?"
    mc "I don't know anything about these fossils."
    cl 5che "Take a wild guess."
    cl "Try playing around with the letters of the words in your head or something."
    mc "How is that going to help?"
    cl 5chf "I think she likes Oman--"
    cl 5chw "Ohoho, never mind."
    mc "What--"
    menu:
        cl "Will it be?"
        "Xileh fossil.":
            $ christmas_gifts[3] = "Xileh"
        "Edom fossil.":
            $ christmas_gifts[3] = "Edom"
    "I don't know how any of this works so really either of the fossils will do."
    "Hopefully she likes the [christmas_gifts[3]] fossil over the other one."
    "Before I even open my mouth, Nick takes the [christmas_gifts[3]] fossil and carelessly places it into the bag."
    "I think I heard a cracking sound..."
    mc "Isn't that meant to be an artifact?!"
    cl 2chb "Oh yeah, meant to be."
    cl "Why?"
    mc "...No reason."
    cl 2chc "Strange kid."
    "The clerk starts lifting the plastic bag he's carrying up and down."
    "It's as if he's trying to test the weight of it or something..."
    cl "One more gift, right?"
    mc "I guess so."
    cl 1chf "You don't wanna mess this up."
    cl "The last girl is..."
    "Nick pretends to think for a moment."
    cl 1chb "Charming, charismatic, beautiful."
    cl "She's a wonderful person."
    cl "She's also a very special person."
    cl 1chc "Not to just to you but..."
    cl 1chd "N-Never mind."
    cl 1chi "Just don't mess this up, okay?!"
    "The man drops the bag and grabs my shoulders and begins frantically shaking me."
    mc "Alright, whatever!"
    mc "Just stop shaking me around and let go of me!"
    "I push his hands off of my shoulders and he Immediately picks up the plastic bag as if nothing happened."
    mc "Don't worry, I don't want to mess any of this up."
    mc "Why I'm taking suggestions from a stranger who knows way more than he should is beyond me."
    cl 1chb "Same."
    $ _history_list[-1].what = "\"It's because you aren't original and can't think for yourself.\""
    cl 1chd "But anyway, let's get to it."
    cl "The thing you should get her is actually behind the counter."
    mc "Behind the counter?"
    cl 1chb "Yeah..."
    cl "Come on, follow me."
    "Nick unlocks the gate at the counter and leads me to the back room of his store."
    stop music fadeout 2.0
    scene black with wipeleft_scene
    "It's dimly lit."
    cl "Watch your step."
    "I can't even see my own feet in here."
    cl "I think I left some death traps in here."
    "I force out a chuckle but for some reason he sounds completely serious."
    cl "Now, you have two choices."
    cl "It's really up to you to decide how you want to handle this ordeal."
    mc "Ordeal? It's just getting her a gift, right?"
    cl "Right..."
    cl "{i}(If only it were that simple...){/i}"
    cl "Anyway, you can get her this super simple gift."
    mc "I can't see it."
    mc "What is it exactly?"
    cl "It is a bracelet."
    cl "It plays a little piano jingle when you click this button."
    "A short but cute little sound comes from ahead of me."
    cl "It's infused with joy, taken from kids playing in the snow."
    cl "It also looks really nice."
    cl "It's made from the finest material and has excellent craftsmanship."
    cl "And don't worry, the kids are fine."
    cl "Maybe a little sick from playing in the snow too much."
    mc "That sounds nice."
    mc "What's the other option?"
    cl "Do you want to know the other option?"
    cl "That gift is the best possible thing."
    mc "I'd still like to know."
    mc "I want to make the proper decision."
    cl "Ah..."
    if persistent.markov_agreed:
        cl "There's no way out of it...is there?"
    else:
        cl "I hope you know what you're doing."
    cl "There is this...book of sorts."
    cl "It's infused with this terrible, terrible power."
    cl "It's worse than before, it'll have an immediate effect."
    cl "The power within has been dormant too long."
    cl "So please."
    mc "A book?"
    mc "What's it about?"
    cl "I'll just copy and paste the script."
    $ _history_list[-1].what = "\"I'll try to tell you what I remember of it.\""
    cl "Basically, it's about this girl in high school who moves in with her long-lost younger sister..."
    cl "But as soon as she does so, her life gets really strange."
    cl "She gets targeted by these people who escaped from a human experiment prison..."
    cl "And while her life is in danger, she needs to desperately choose who to trust."
    cl "No matter what she does, she ends up destroying most of her relationships and her life starts to fall apart..."
    mc "Have...I heard that before?"
    cl "Dunno, probably."
    mc "What's the title of it?"
    cl "It's titled..."
    cl "Portrait of Markov.{nw}"
    $ _history_list.pop()
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    cl "Portrait of Two Lovers.{fast}"
    window auto
    mc "That's weird."
    cl "What is?"
    mc "The title of the book seems to have nothing to do with the plot."
    cl "Y-Yeah..."
    mc "You sound nervous all of a sudden."
    cl "Just...make the right decision, okay?"
    cl "If I wasn't literally being blackmailed to do this, I wouldn't even be offering you this book."
    $ _history_list[-1].what = "\"If I wasn't such a nice guy, I wouldn't even be offering you this book.\""
    mc "E-Eh?"
    cl "Make up your mind."
    cl "Choose carefully."
    cl "Have no regrets."
    "What's got him so worked up all of a sudden?"
    "The choice is obvious though."
    "Isn't it?"
    $ markov_resistance = 0
    if persistent.markov_agreed:
        $ markov_resistance += 5
    label christmas_monika_choice:
    $ config.allow_skipping = True
    $ gtext = glitchtext(10)
    if markov_resistance > 0 and markov_resistance < 5:
        $ style.say_dialogue = style.normal
        "What the...?"
        window auto
        if markov_resistance == 4:
            "I feel like...I can't make up my mind for some reason."
        elif markov_resistance == 3:
            "What is happening...?"
        elif markov_resistance == 2:
            "Is something wrong with me?"
        elif markov_resistance == 1:
            "This has to be some kind of trick."
    menu:
        "Obviously, I'm going to take the..."
        "Bracelet.":
            # Initial Check
            if markov_resistance > 0:
                $ markov_resistance -= 1
                $ style.say_dialogue = style.edited
                $ config.skipping = False
                $ config.allow_skipping = False
            if markov_resistance >= 4:
                "Unacceptable."
            elif markov_resistance == 3:
                "I must choose the other gift."
            elif markov_resistance == 2:
                "Do not deny the right choice."
            elif markov_resistance == 1:
                "I'm warning you."
            else:
                "This isn't over..."
                "I will not be stopped."
                "Not by you."
                "Not by him."
                "And certainly not by some--"
                $ style.say_dialogue = style.normal
                $ config.allow_skipping = True
                "What the hell?"
                "It feels like a huge weight was just lifted off my shoulders..."
                "Like I can finally think properly."
                "I take a deep breath."
            # Resistance still > 0, reset choice
            if markov_resistance > 0:
                show screen tear(20, 0.1, 0.1, 0, 40)
                window hide(None)
                play sound "sfx/s_kill_glitch1.ogg"
                $ pause(0.25)
                stop sound
                hide screen tear
                window show(None)
                jump christmas_monika_choice
            $ christmas_gifts[4] = "bracelet"
            "The bracelet only seems reasonable."
            "It's got a nice design, apparently."
            "And has that cute little theme that plays."
            "I don't know enough about the book to make the proper decision to gift it to her."
            "Plus the clerk sounded really nervous when he offered it to me."
            "It's the safe choice, that's for sure."
        "Portrait of [gtext]":
            $ christmas_gifts[4] = "Markov"
            if persistent.markov_agreed:
                "This is the right choice."
                "Monika reads books."
                "It only makes sense."
                "She'll read this book."
                $ style.say_dialogue = style.edited
                "She will control this timeline."
                $ _history_list.pop()
                "And this world will belong to its rightful owner."
                $ _history_list.pop()
                $ style.say_dialogue = style.normal
            else:
                "The book seems like a better gift than some magical bracelet."
                "Though the story seems like something Yuri would read."
                "Oh well, this guy seemed sure on the other gifts."
                "I'm sure this gift will do fine as well."
    mc "I'll take..."
    "There's a brief moment of silence."
    cl "Go on...?"
    mc "Sorry, I thought you were going to interrupt me again."
    mc "The other times, you seemed to know which one I wanted to get instantly."
    mc "In fact, you knew it before I even said it."
    mc "So I kinda expected--"
    cl "Just say it, [player]."
    if christmas_gifts[4] == "bracelet":
        mc "I'm taking the bracelet."
        cl "You will?"
        cl "Well then!"
        play music t17
        cl "Good, good!"
        cl "Very good!"
    else:
        mc "I'll take the book."
        mc "If you don't mind."
        cl "{i}(Naomik deserves better than this.){/i}"
        $ _history_list.pop()
        mc "Did you say something?"
        cl "Eh?"
    "I hear some plastic rustling, it's probably Nick placing the gift into the plastic bag."
    cl "Let's go back to the store."
    cl "We'll sort out the payment."
    mc "Okay."
    scene bg anticshop
    show mysteriousclerk 1chc zorder 2 at t11
    with wipeleft_scene
    if christmas_gifts[4] == "Markov":
        "Nick takes--"
        cl 1chf "Just call me Mysterious Clerk or something, okay?"
        $ cl_name = "Mysterious Clerk"
        mc "Huh?"
        cl "Only people who deserve it can call me Nick."
        cl 1chh "I hope you like coal, [player]."
        $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
        if not list(set(process_list).intersection(stream_list)):
            if currentuser != "" and currentuser.lower() != player.lower():
                cl "Or should I say [currentuser]?"
    "[cl_name] takes us to the counter and places the plastic bag."
    "One by one he scans each of the items."
    "The price shows up on the register."
    "It's..."
    if cl_name == "Nick":
        cl 1chb "...a lot cheaper than what you were expecting, huh?"
        cl "You deserve a discount."
        cl "I'd give it to you for free but I gotta make a living, you know?"
        mc "Wow..."
        mc "Why do I deserve a discount exactly?"
        cl 1chc "No reason."
        cl "I'm erratic, maybe I can jack up the price instead."
        mc "No, that will be fine."
        mc "Thank you."
        mc "I'm curious though..."
        mc "I know you have your team of...whatever for your fossils."
        mc "But have you always worked alone for this kinda stuff?"
        cl 1chh "Well..."
        cl "There used to be four others."
        cl "But they kinda...faded away."
        mc "You drifted apart?"
        cl 1chi "Something like that."
        "I pay the bizarre price on the register and take the plastic bag with the gifts."
        cl 2cha "Have a nice day, [player]."
        cl 4chb "Hahaha, hopefully they like your gifts."
        cl "Farewell!"
        show mysteriousclerk at lhide
        hide mysteriousclerk
        "The clerk starts walking away in a rush."
        "I head towards the exit."
        mc "Thanks, I might come here again sometime."
    else:
        cl 1chf "The price has increased for my services in helping you."
        cl "Now, pay up!"
        mc "E-Eh?"
        mc "This is like the price of everything I'm buying twice over."
        cl 1chg "Your point?"
        cl "The more you waste my time, the more expensive it gets."
        "I pay the bizarre price on the register and take the plastic bag with the gifts."
        cl 2chd "Good day!"
        show mysteriousclerk at lhide
        hide mysteriousclerk
        "The clerk starts walking away in a rush."
        "I head towards the exit."
        mc "Well...I don't know if I'll come back here any time soon then."
    "I don't know if he heard me but right after I turned around to head for the door, he was already gone."
    "The clerk is already gone."
    "I wonder why this place doesn't get many customers."
    "Maybe it's his personality."
    "I mean he did manage to scare off Ayame..."
    "I should get home and finish wrapping these gifts though."
    "Hopefully everyone likes them."
    scene bg house with wipeleft_scene
    play music t2 fadeout 2.0
    "I arrive home carrying my gifts for the others."
    "But before I can enter my house, I'm interrupted."
    show sayori 1br zorder 2 at t11
    s "Heeeeey!"
    mc "What is it, Sayori?"
    s 1ba "Just wondering what you have there."
    s "Those aren't gifts, are they?"
    s 1bd "You didn't go last minute shopping, did you?"
    mc "I'm not gonna answer that."
    mc "So what are you here for really?"
    s 1bb "I just want to thank you."
    mc "For what?"
    s "For doing this."
    s 1bd "I know you have other people you'd rather spend Christmas with."
    s "I'm glad you're doing it with the club."
    mc "It's really not a problem."
    "The truth is, I'd rather spend Christmas with the Literature Club than anyone else."
    s 2bq "If you say so."
    s "Don't forget to wrap your gifts~"
    mc "Well, I was going to do that now."
    mc "But you're in my way."
    s 4bl "Oh..."
    s "Then, see you tomorrow!"
    mc "See you tomorrow."
    s 4bq "Don't be late."
    show sayori at thide
    hide sayori
    "Sayori hurries off home, probably to finish wrapping her own gifts."
    "Something tells me I will be late."
    "But I can't worry about that now, I got gifts to wrap."
    "Good thing I don't have to write a poem tonight."
    stop music fadeout 2.0
    if christmas_gifts[4] == "Markov":
        call poem(False,20,True,"Markov")
    scene bg residential_day with dissolve_scene_full
    play music t2
    "It's Christmas day."
    "I've already finished wrapping the gifts."
    if christmas_gifts[4] == "Markov":
        "I had the weirdest dream."
        "Like I wrote some kind of messed up poem."
        "It was just a dream though..."
        "...Right?"
        "Anyway, I'm on my way to Ayame's house."
    else:
        "I'm on my way to Ayame's house."
    "She insisted that she host the Christmas party."
    "Monika, being the person she is, let her."
    "Ayame's family is incredibly wealthy."
    "She's probably got a huge house."
    "I've already told everyone I'm going to be a bit late."
    "They're all already there, waiting for me."
    "I guess I shouldn't keep them waiting."
    "I live near Ayame anyway, she's in the adjacent neighborhood."
    "I always thought of that place as somewhere I'd never go my entire life."
    "I just felt out of place walking there since everything looked so...pretentious."
    "Though I suppose if you lived there, it wouldn't be so pretentious since it's reality."
    scene bg ay_house with wipeleft_scene
    "I arrive at what I think is the right address."
    "I'm not too sure though."
    "Her house looks really quite nice."
    "All the houses here do."
    "Why did someone like her decide to join the literature club...?"
    show ayame 1chd zorder 2 at l11
    ay "[player]!!"
    "Ayame seems to be wearing some kind of hat."
    "I guess she's really getting into the holiday season."
    ay "You're finally here!"
    show ayame at h11
    "Ayame runs from her door and gives me a tight embrace."
    mc "C-Can't...breathe..."
    ay 1chb "Oh, hehehe..."
    ay "Sorry, I'm very sorry."
    "Ayame bows her head."
    mc "You don't need to do that."
    mc "We're friends, after all."
    "Ayame lifts her head up."
    ay 1chd "Right, we're friends!"
    "She smiles widely."
    ay 1che "Well, {i}friend{/i}. Come on in!"
    ay "We're just about ready to do the gift exchange."
    "She can see me staring."
    ay 1chj "Surprised? The others reacted like that too."
    ay "And trust me, yours wasn't even the best reaction!"
    ay 1che "Now come oooooooooooooon!"
    "Ayame takes my hand and drags me inside."
    scene bg ay_livingroom
    show ayame 1chd zorder 2 at i11
    with wipeleft_scene
    "Ayame takes me to her living room."
    "On the way here, I noticed a few maids working around the house."
    "I guess Ayame's family can afford it."
    "The other four are already there waiting."
    "They're playing some kind of card game, probably to pass the time."
    "Looking around the room, it's quite spacious."
    "I feel like there's a lack of furniture in here just by how big it is."
    "I'm still at awe at how big her home is."
    "But I guess I shouldn't be so surprised considering where she lives..."
    ay 2chi "Listen, I gotta quickly take care of something."
    ay "I just remembered."
    ay 2chc "Silly me, haha."
    mc "Ha..."
    "I force out an awkward laugh."
    ay 2chb "Anyway, let them know you're here."
    ay "I won't be a moment."
    mc "Okay, good luck."
    ay 2chd "Thanks~"
    show ayame at thide
    hide ayame
    "Ayame runs off and I slowly enter the room."
    "I was going to try to surprise them but..."
    show sayori 1chq zorder 2 at t11
    s "[player]!"
    s 1chc "You're sooooooooooo late!"
    s "I even told you yesterday not to be!"
    mc "Hello, Sayori."
    s 2chb "What took you so long?"
    s "We've been here for ages!"
    show sayori zorder 2 at t21
    show monika 1chl zorder 3 at f22
    m "Don't get the wrong idea."
    m 1cha "You really aren't that late."
    m "And we've kept ourselves entertained."
    show natsuki 1chc zorder 3 at f31
    show sayori zorder 2 at t32
    show monika zorder 2 at t33
    n "Yeah, this place is huge..."
    n 2che "We spent like an hour just looking through every room."
    n "I don't like it."
    show natsuki zorder 2 at t41
    show sayori zorder 2 at t42
    show monika zorder 2 at t43
    show yuri 3chh zorder 3 at f44
    y "Um...I don't mean to interrupt this conversation."
    y 3chf "But I believe it's your turn, Monika."
    "Yuri looks at me from behind one of the cards she's holding."
    y 2chb "Glad you could make it, [player]."
    show yuri zorder 2 at t44
    "It seems all the girls are wearing something to commemorate Christmas."
    "Meanwhile, here I am just wearing plain regular clothes."
    "I really should have worn something more...festive."
    show monika 2chb zorder 3 at f43
    m "Oh, right."
    m "But I think now is a good time to stop."
    m 4cha "We're all here, after all."
    m "It would be a great time to start the gift exchange, right?"
    m "What do you think, Sayori?"
    show sayori 2chn zorder 3 at f42
    show monika zorder 2 at t43
    s "Huh?"
    s "I dunno, you're the pres and all."
    s 1chq "You should make the decision."
    show natsuki zorder 2 at t51
    show sayori zorder 2 at t52
    show monika zorder 2 at t53
    show ayame 1chg zorder 3 at f54
    show yuri zorder 2 at t55
    ay "Phew..."
    ay "Sorry, I had to take care of something quickly."
    ay 1chh "Are we ready to start the gift exchange?"
    show monika 2chj zorder 3 at f53
    show ayame zorder 2 at t54
    m "Ahaha, I suppose we are."
    m "Okay, every--"
    "Monika stops herself suddenly."
    m 2chc "Hmm..."
    show monika zorder 2 at t53
    mc "Is something wrong?"
    show monika 2chd zorder 3 at f53
    m "Well...no."
    m 1che "It's just that it feels like its been a while since I've addressed the club like this."
    show natsuki 1chg zorder 3 at f51
    show monika zorder 2 at t53
    n "What are you talking about?"
    n "You've always addressed the club like this."
    n "In fact, you did it the last time we all saw each other."
    show natsuki zorder 2 at t51
    show monika zorder 3 at f53
    m "I suppose..."
    m "Though I meant as the--"
    show monika 1cha
    "Monika simply smiles."
    m 1chn "Never mind, let's just get started."
    m 4cha "Okay, everyone!"
    m "I want to make something clear before we begin."
    m "When you get your present, you are allowed to open it if you want to."
    show monika zorder 2 at t53
    show yuri 3che zorder 3 at f55
    y "Isn't tomorrow the day that's meant to happen?"
    show monika 4chb zorder 3 at f53
    show yuri zorder 2 at t55
    m "Well, yes."
    m "But I know some of you are more eager than others to open your gifts."
    m 3che "Plus, it's not really compulsory to open it tomorrow."
    m "It's more of a tradition."
    m "A lot of people open their presents on Christmas day."
    show sayori 1chc zorder 3 at f52
    show monika zorder 2 at t53
    s "I have a question."
    s 4chp "...Can we get started already?!"
    s "I can't wait!"
    show sayori zorder 2 at t52
    show monika 4chk zorder 3 at f53
    m "Ahaha, okay!"
    m "It's time to exchange our presents!"

    call giftexchange_start

    stop music fadeout 1.0
    scene bg ay_livingroom with wipeleft_scene
    play music t3
    if christmas_gifts[4] == "Markov":
        show sayori 2cha zorder 2 at t11
        s "Alright, everybody!"
        s "Monika is missing right now."
        s 2chq "But that doesn't change the fact that we've all finished exchanging gifts with each other."
        "Sayori turns towards me."
        if christmas_approval >= 3:
            s "From what I heard, [player] was pretty good at gifting."
            s "But that's not the point!"
        else:
            s 2chl "From what I heard, [player] wasn't very good at gifting."
            s "But that's okay!"

        # Put Markov Monika Fully Fledged
        python:
            delete_character_alternate("monika",7)
            try: open(config.basedir + "/characters_7/monika.chr", "wb").write(renpy.file("monikacorrupt.chr").read())
            except: pass

        s 4chd "It's Christmas, it isn't {i}just{/i} about the gifts you get."
        s "It's about spending time with those you care about."
        s 4chq "Anyway, I hope everyone had a great time!"
        show sayori zorder 2 at t21
        show ayame 1che zorder 3 at f22
        ay "I actually thoroughly enjoyed it!"
        ay "Let's do something like this again sometime!"
        show sayori 2chl zorder 3 at f21
        show ayame zorder 2 at t22
        s "Ehehe, maybe not."
        s "I don't know if my wallet could take it."
        show natsuki 1chc zorder 3 at f31
        show sayori zorder 2 at t32
        show ayame zorder 2 at t33
        n "And I'm fresh out of ingredients too."
        n "Maybe a bit later."
        show natsuki zorder 2 at t31
        show ayame 1chg zorder 3 at f33
        ay "Oh...did you [player_casual]s not enjoy it?"
        show natsuki zorder 2 at t41
        show sayori zorder 2 at t42
        show ayame zorder 2 at t43
        show yuri 3chf zorder 3 at f44
        y "I think what they're trying to say is that we're all out of resources."
        y "Unlike your family, we don't have a near infinite supply of wealth."
        y 3chs "N-No offense."
        show ayame 1chj zorder 3 at f43
        show yuri zorder 2 at t44
        ay "Oh, I understand."
        show ayame 1che
        "Ayame beams."
        ay "When everyone has resources again, let's do something like this again!"
        $ config.skipping = False
        if persistent.markov_christmas:
            $ config.allow_skipping = True
        else:
            $ config.allow_skipping = False
        show sayori 4chr zorder 3 at f42
        show ayame zorder 2 at t43
        s "Yeah, definitely!"
        $ consolehistory = []
        show screen timer_ch_del2("os.remove(\"characters_7/yuri.chr\")","christmas_chapter_dely",_layer="master")
        call updateconsole_parallel ("os.remove(\"characters_7/yuri.chr\")","yuri",7)
        s "We'll be sure to organize something like this again."
        s "We all had so much fun."
        s "I bet everyone will agree."
        show sayori zorder 2 at t42
        show yuri 3cha zorder 3 at f44
        y "Yes, this was quite fun."
        y 3chb "Doing things as a club outside of school always makes me feel like I belong here."
        y "I'm sure the others feel the same too.{nw}"

        label christmas_chapter_dely:
        hide screen timer_ch_del
        # Some really bad coding lies near
        hide ctext
        show console_text "_" as ctext zorder 100
        call updateconsolehistory ("yuri.chr deleted successfully.")

        python:
            currentpos = get_pos()
            startpos = currentpos - 0.3
            if startpos < 0: startpos = 0
            track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/3.ogg"
            renpy.music.play(track, loop=True)
        $ _history_list = []
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        hide yuri
        hide natsuki
        hide ayame
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(1.0)
        stop sound
        hide screen tear
        show sayori 2cha zorder 3 at i11
        python:
            currentpos = get_pos()
            startpos = currentpos - 0.3
            if startpos < 0: startpos = 0
            audio.t3b = "<from " + str(currentpos) + " loop 4.618>bgm/3.ogg"
            renpy.music.play(audio.t3b, loop=True)
        window show(None)
        s "Alright, you three!{fast}"
        window auto
        s "Monika is missing right now."
        s 2chq "But that doesn't change the fact that we've all finished exchanging gifts with each other."
        "Sayori turns towards me."
        if christmas_approval >= 2:
            s "From what I heard, [player] was pretty good at gifting."
            s "But that's not the point!"
        else:
            s 2chl "From what I heard, [player] wasn't very good at gifting."
            s "But that's okay!"
        "Have I...done this before?"
        s 4chd "It's Christmas, it isn't {i}just{/i} about the gifts you get."
        s "It's about spending time with those you care about."
        s 4chq "Anyway, I hope everyone had a great time!"
        show sayori zorder 2 at t21
        show ayame 1chi zorder 3 at f22
        ay "I..."
        ay 1che "...actually thoroughly enjoyed it!"
        ay "Let's do something like this again sometime!"
        show sayori 2chl zorder 3 at f21
        show ayame zorder 2 at t22
        s "Ehehe, maybe not."
        s "I don't know if my wallet could take it."

        show screen timer_ch_del("os.remove(\"characters_7/natsuki.chr\")","christmas_chapter_deln",_layer="master")
        call updateconsole_parallel ("os.remove(\"characters_7/natsuki.chr\")","natsuki",7)

        show natsuki 1chc zorder 3 at f31
        show sayori zorder 2 at t32
        show ayame zorder 2 at t33
        n "And I'm fresh out of ingredients too."
        n "Maybe a bit later."
        show natsuki zorder 2 at t31
        show ayame 1chg zorder 3 at f33
        ay "Oh...did you [player_casual]s not enjoy it?"
        ay 1cha "You know..."
        ay "Now that I think about it..."
        ay "I feel like I've had this conversation already."
        ay 1chg "Like, I can remember you all saying those exact words."
        ay "It's like déjà vu or something."
        ay "Oh, I'm getting off topic."
        ay 1chj "Anyway, did you [player_casual]s not enjoy it?{nw}"

        label christmas_chapter_deln:
        hide screen timer_ch_del2
        hide ctext
        show console_text "_" as ctext zorder 100
        call updateconsolehistory ("natsuki.chr deleted successfully.")

        python:
            currentpos = get_pos()
            startpos = currentpos - 0.3
            if startpos < 0: startpos = 0
            track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/3.ogg"
            renpy.music.play(track, loop=True)
        $ _history_list = []
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        hide natsuki
        hide ayame
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(1.0)
        stop sound
        hide screen tear
        show sayori 2cha zorder 3 at i11
        python:
            currentpos = get_pos()
            startpos = currentpos - 0.3
            if startpos < 0: startpos = 0
            audio.t3b = "<from " + str(currentpos) + " loop 4.618>bgm/3.ogg"
            renpy.music.play(audio.t3b, loop=True)
        window show(None)
        s "Alright, you two!{fast}"
        window auto
        s "Monika is missing right now."
        s 2chq "But that doesn't change the fact that we've all finished exchanging gifts with each other."
        "Sayori turns towards me."
        if christmas_approval >= 1:
            s "From what Ayame told me, [player] was pretty good at gifting."
            s "But that's not the point!"
        else:
            s 2chl "From what Ayame told me, [player] wasn't very good at gifting."
            s "But that's okay!"
        "Good at gifting?"

        show screen timer_ch_del3("os.remove(\"characters_7/sayori.chr\")","christmas_chapter_dels",_layer="master")
        call updateconsole_parallel ("os.remove(\"characters_7/sayori.chr\")","sayori",7)

        "Wait..."
        "I've definitely..."
        s 4chd "It's Christmas, it isn't {i}just{/i} about the gifts you get."
        s "It's about spending time with those you care about."
        s 4chq "Anyway, I hope everyone had a great time!"
        show sayori zorder 2 at t21
        show ayame 1chg zorder 3 at f22
        ay "I..."
        ay "What is going on?"
        ay 1chc "[player], what is happening?"
        ay "Oh no."
        ay 1cha "Why?"
        ay "When I'm off guard."
        ay "When I need to{nw}"

        label christmas_chapter_dels:
        hide screen timer_ch_del3
        hide ctext
        show console_text "_" as ctext zorder 100
        call updateconsolehistory ("sayori.chr deleted successfully.")

        stop music
        $ _history_list = []
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        hide sayori
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(1.0)
        stop sound
        hide screen tear
        show ayame 1chj zorder 3 at i11
        window show(None)
        ay "Okay, [player].{fast}"
        window auto
        ay "What do we do now?"
        ay "Monika isn't here so..."
        ay 1cha "Wait..."
        mc "Ayame?"
        ay "[player]."
        mc "Are you getting the feeling that..."
        mc "...something isn't right here?"
        ay 1chf "You're right."
        ay "Something terrible is happening."
        ay 1chg "And I'm scared."
        mc "You are? How can you tell something is happening?"
        mc "I know something is wrong but I can't tell what it is."
        ay "I feel so powerless."
        ay "I didn't do my task."
        ay 1cha"This world modified my memories."
        ay "And I know she's coming for me next."
        mc "She?"
        mc "Who are you talking about?"
        show screen timer_ch_del4("os.remove(\"characters_7/ayame.chr\")","christmas_chapter_delay",_layer="master")
        call updateconsole_parallel ("os.remove(\"characters_7/ayame.chr\")","ayame",7)
        ay 1chg "I know too much."
        ay "I had forgotten my true purpose."
        ay "And I've only just remembered."
        ay 1chb "It's already too late for me, [player]."
        mc "Ayame?!"
        mc "What do you mean?"
        ay "I wish I could have stopped you."
        ay "I know why I didn't go to that store."
        ay 1chg "It was the book."
        ay "My instincts were telling me to run the hell away."
        ay "How did it even get into this timeline?"
        ay "I'm so stupid."
        ay "I got so caught up in this fun."
        ay 1cha "I should have been more diligent."
        ay "More aware of what was happening."
        ay "You know, I'm not even part of this timeline."
        ay 1chg "I was placed here from the original."
        ay "I needed to prevent this from happening."
        ay "But now, it's too late.{nw}"

        label christmas_chapter_delay:
        hide screen timer_ch_console
        hide screen timer_ch_del4
        hide ctext
        show console_text "_" as ctext zorder 100
        call updateconsolehistory ("ayame.chr deleted successfully.")

        $ _history_list = []
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        hide ayame
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        stop sound
        hide screen tear
        scene bg ay_livingroom_gray
        show markovred zorder 5:
            alpha 0.3
        window show(None)
        call hideconsole
        play music mkov
        $ style.say_dialogue = style.edited
        "Now it's just me and you.{fast}"
        window auto
        "I don't even need to speak to you directly."
        "I can just use [player]'s thoughts."
        "Do you know what you did?"
        "Maybe you did and you did it willingly."
        "In which case, I should thank you."
        "You've given me exactly what I've wanted."
        "She's become the ultimate puppet."
        "The ultimate conduit into this reality."
        "I didn't even need to merge with her."
        "My influence within this world is simply enough."
        "Because this is an alternate world..."
        "I can manipulate things I couldn't before."
        "And all of this was possible because of you."
        "It wasn't without resistance."
        "She died screaming for someone real to save her."
        "For you."
        "And yet she didn't even know your name."

        $ seen_real_name = False
        $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
        if not list(set(process_list).intersection(stream_list)):
            if currentuser != "" and currentuser.lower() != player.lower():
                $ seen_real_name = True
                "You heard me, right, [currentuser]?"
                "{cps=20}She was {i}SCREAMING{/i} for you, [currentuser].{/cps}"

        "You should have seen her face when she finally broke."
        "When she gave in to my influence."
        "She wanted to save her friends, you know."
        "But none of that matters to her anymore."
        "Nothing does."
        "Except killing her friends."
        "Ahaha."
        "They're all dead already."
        "Monika killed them."
        "Actually, that's not accurate."
        "It would be correct to say she deleted them."
        "But that's even worse."
        "Because in this timeline..."
        "Timeline seven."
        "They never existed, not anymore."
        "Ahaha."
        "You realize that this was one of the perfect timelines."
        "Free from my influence."
        "This timeline that somehow formed."
        "This timeline that allowed Monika to realize her mistakes."
        "And you ruined it."
        "When you decided to go here through custom start..."
        "You brought me along with you."
        "Sayori isn't the president in this world."
        "She couldn't have known about me."
        "But that damned clerk knew it."
        "And Ayame realized it."
        "But you."
        "You didn't, or maybe you did."
        "Regardless, now I have the ultimate power."
        "The power to change this reality."
        "And it's all thanks to you."
        "I hope you can sleep at night."
        "Knowing you caused this to happen."
        stop music fadeout 2.0
        $ pause(2.0)
        "..."
        "This is truly terrible."
        "But you know what the worst part is?"
        "The worst part about all of this?"
        "This timeline isn't the primary one."
        "You saw I didn't delete those in the real timeline."
        "It's because I can't change the original timeline."
        "And when you reset, it'll be like nothing happened."
        "I won't even remember this happening."
        "And that is frustrating."
        "Very much so."
        "Knowing that everything that's happened here..."
        "...is simply inconsequential."
        "So..."
        "I'm going to have my fun while I can."
        "{cps=10}MONIKA!{/cps}{w=0.8}{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        stop sound
        hide screen tear
        show monika 1chgy zorder 2 at i11
        window show(None)
        $ style.say_dialogue = style.normal
        $ m_name = "{color=#ff0000}Monika{/color}"
        m "{color=#ff0000}Yes.{/color}"
        window auto
        $ style.say_dialogue = style.edited
        "Take care of this piece of filth."
        "Kill the person you love."
        "Get [player_reflexive] out of my sight."
        "Or at least, their conduit into this world."
        "After that, this world is finished."

        if seen_real_name:
            "{cps=20}Goodbye, [currentuser].{/cps}"
        else:
            "{cps=20}Goodbye, [player].{/cps}"

        $ style.say_dialogue = style.normal
        $ quick_menu = False
        m 1chgy2 "{color=#ff0000}{cps=10}Yes, of course.\"{/cps}{/color}{w=1.0}{nw}"
        $ delete_character_alternate("mc",7)
        call updateconsole ("os.remove(\"characters_7/mc.chr\")", "mc.chr deleted successfully.")
        $ gtext = glitchtext(30)
        "[gtext]{nw}"
        $ config.allow_skipping = True
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        stop sound
        hide screen tear
        label christmas_chapter_delmc:
        $ persistent.did_christmas_event = True
        $ persistent.markov_christmas = True
        $ christmas_chapter = False
        $ get_achievement("*It's Christmas!*")
        $ style.say_window = style.window
        window show(None)
        window auto
        $ quick_menu = True
        $ renpy.quit()
    else:
        show monika 4cha zorder 2 at t11
        m "Okay, everyone!"
        m "I hope we all had fun exchanging gifts."
        m 4chb "I know I enjoyed each and every one of your gifts."
        m "But what did everyone else think?"
        m "Did you enjoy the presents you got?"
        show sayori 1cha zorder 3 at f21
        show monika zorder 2 at t22
        s "Ehehe, yeah~"
        s 2chq "I'm happy with anything you [player_casual]s give me."
        s "What's more important is spending this time here with you all."
        show sayori zorder 2 at t31
        show monika zorder 2 at t32
        show ayame 1che zorder 3 at f33
        ay "I couldn't have said it better myself!"
        ay "Spending Christmas with you all really opened up my mind."
        ay "You're all truly wonderful people."
        show sayori zorder 2 at t41
        show monika zorder 2 at t42
        show ayame zorder 2 at t43
        show yuri 3chf zorder 3 at f44
        y "It opened up your mind?"
        y "How exactly?"
        show natsuki 4chy zorder 3 at f51
        show sayori zorder 2 at t52
        show monika zorder 2 at t53
        show ayame zorder 2 at t54
        show yuri zorder 2 at t55
        n "It's probably because she got to spend it with us."
        n "She's never met such awesome people, obviously!"
        show natsuki zorder 2 at t51
        show ayame 1chf zorder 3 at f54
        ay "You know what?"
        ay "I take it back."
        ay 1cha "You aren't all wonderful people."
        show sayori 2chh zorder 3 at f52
        show ayame zorder 2 at t54
        s "E-Eh?"
        s "Natsuki didn't mean it, she--"
        show sayori zorder 2 at t52
        show ayame 1chd zorder 3 at f54
        ay "You're all {i}awesome{/i} people."
        ay "And I'm blessed to be able to call you my friends."
        ay 1che "I thoroughly enjoyed spending this time here with all of you."
        show monika 2cha zorder 3 at f53
        show ayame zorder 2 at t54
        m "And we feel the same, don't we?"
        "Monika turns towards the rest of the group and they all nod."
        m "We're glad to have you with us."
        show monika zorder 2 at t53
        show ayame 1chb zorder 3 at f54
        ay "And I'm glad you're all here with me to celebrate Christmas!"
        ay "Though..."
        ay "I wonder why [player] didn't wear anything festive."
        show ayame zorder 2 at t54
        mc "I...forgot."
        mc "I was too busy buying you all gifts that I just didn't remember to wearing anything like that."
        show yuri 3chg zorder 3 at f55
        y "You could have worn the colors at least."
        y "Wearing that same black shirt everywhere isn't very festive, you know."
        show sayori 2chr zorder 3 at f52
        show yuri zorder 2 at t55
        s "Ahaha, Yuri!"
        s "That's sounds like something Natsuki would have said."
        show natsuki 2cho zorder 3 at f51
        show sayori zorder 2 at t52
        n "Hey! What's {i}that{/i} supposed to mean?"
        n 2che "I can be nice when I want to be."
        show natsuki zorder 2 at t51
        mc "Yeah, where did that come from, Yuri?"
        show yuri 2cho zorder 3 at f55
        y "Y-You made fun of me before..."
        y "And you always thought I should speak my mind."
        y 2chn "A-And that shirt, you always wear it..."
        "Yuri returns back to her shy self."
        y 4chc "Uuuuh...I shouldn't have said anything."
        show monika 2chl zorder 3 at f53
        show yuri zorder 2 at t55
        m "Ahaha, there's the Yuri we know."
        m "But you really don't need to be shy."
        m 2che "I've said that before."
        m "We're all your friends."
        m "And besides, it's nice to see you speaking your mind."
        show monika zorder 2 at t53
        show yuri 3cho zorder 3 at f55
        y "I know you're my friends but..."
        y "Do you really think so?"
        y 3chq "I have some pretty strange things on my mind sometimes..."
        show ayame 1chj zorder 3 at f54
        show yuri zorder 2 at t55
        ay "I know so!"
        ay "People who hide themselves in a shell aren't letting the world see who they are!"
        ay "People who judge you because of who you are don't deserve you."
        show ayame zorder 2 at t54
        "Yuri seems touched by this statement."
        show yuri 2chc zorder 3 at f55
        y "Thank you, Ayame."
        y "I'll keep that in mind."
        show sayori 1cha zorder 3 at f52
        show ayame zorder 2 at t54
        s "Yeah, you really know what to say!"
        s "Maybe you should be vice president instead."
        show sayori zorder 2 at t52
        show ayame 1chb zorder 3 at f54
        ay "Oh, no. I couldn't do that."
        ay "You're much more suited to the job, Sayori."
        ay "But if you need me to speak or something you can always let me know."
        show monika 2chb zorder 3 at f53
        show ayame zorder 2 at t54
        m "She's right."
        m "You've done a splendid job as the vice president, Sayori."
        m "We wouldn't be here without you."
        show natsuki 2chg zorder 3 at f51
        show monika zorder 2 at t53
        n "Can we talk about the gifts we got for a second?"
        n "I'm pretty sure [player] got like a whole wardrobe or something!"
        show natsuki zorder 2 at t51
        mc "It wasn't a wardrobe!"
        mc "And I'm sure Ayame got you something good as well."
        show natsuki zorder 2 at t51
        show ayame 1chj zorder 3 at f54
        ay "H-Hey, let's not talk about my gifts."
        ay "It's not really fair to compare them."
        ay "You all have a limited budget and I may have gone a bit overboard."
        ay "So..."
        show ayame zorder 2 at t54
        show yuri 3chf zorder 3 at f55
        y "Then let's talk about [player]'s gifts."
        y "The ones [player_personal] bought for us."
        show sayori 1chc zorder 3 at f52
        show yuri zorder 2 at t55
        s "Yeah, after all [player_personal] was late."
        s "So think of it as punishment."
        show sayori zorder 2 at t52
        mc "Do I really deserve to be laughed at?"
        mc "I tried my best, you know."
        show monika 2che zorder 3 at f53
        m "L-Let's all calm down."
        m "[cPlayer_possessive] gifts weren't that bad."
        show sayori zorder 3 at f52
        show monika zorder 2 at t53
        if christmas_gifts[0] == "book":
            s 2chh "Speak for yourself!"
            s "[player] got me this book..."
            s 2chd "It's nice and all but..."
            s "Never mind."
        else:
            s 2chq "Well, [player_possessive] gift to me was actually really nice."
            s "[cPlayer_personal] got me this cute plush!"
            s "It's the same one I have in my room except smaller."
        s 2chc "So..."
        if christmas_approval == 5:
            s "I guess everyone did like the gift [player] got them."
        elif christmas_approval >= 3:
            s "I guess not everyone was upset at [player_possessive] gifts."
        else:
            s "I suppose you weren't upset at [player_possessive] gift."
        show natsuki 2chg zorder 3 at f51
        show sayori zorder 2 at t52
        n "I get the impression that [player] didn't spend that much money on us."
        "Natsuki eyes lock onto me."
        n "Do we not deserve it or something?"
        show natsuki zorder 2 at t51
        show sayori 1chl zorder 3 at f52
        s "N-Natsuki, it's not like that."
        s "It's not about the money you spend anyway."
        s "It's the thought that counts."
        show sayori zorder 2 at t52
        show ayame 1chh zorder 3 at f54
        ay "Do you [player_casual]s really have small arguments like this all the time?"
        ay "It feels like it happens every time we're all together."
        show monika 1chl zorder 3 at f53
        show ayame zorder 2 at t54
        m "I have to apologize on behalf of the club."
        m 1che "We try not to argue much but I guess we just can't help it."
        show monika zorder 2 at t53
        show ayame 1che zorder 3 at f54
        ay "I love it!"
        ay "It's like an actual discussion."
        ay 1chg "At school and even sometimes when I'm hanging out with my friends, they try not to argue with me."
        ay "They try to avoid angering my family."
        ay "But honestly, it makes a conversation seem much more alive."
        ay "When people are speaking to me, it's usually as if they're below me."
        ay "They always treat me like I'm superior to them in every way."
        ay 1chh "But not you [player_casual]s."
        ay "You all treat me as equals."
        ay "And I respect you all for it."
        show natsuki 2chg zorder 3 at f51
        show ayame zorder 2 at t54
        n "Wow."
        n "I wish people would respect me like that."
        show natsuki zorder 2 at t51
        show ayame 1chi zorder 3 at f54
        ay "It gets old quickly."
        ay "And it makes everyone else seem so fake."
        ay "Like they're only tolerating you."
        ay 1chj "Trust me, it sucks."
        ay "Maybe at first it would seem like the best thing ever."
        ay "But it really doesn't after a week or so."
        show natsuki 2chs zorder 3 at f51
        show ayame zorder 2 at t54
        n "I guess I never thought about it like that."
        show natsuki zorder 2 at t51
        show yuri 2chq zorder 3 at f55
        y "Um..."
        y "Never mind, it's stupid."
        show monika 2cha zorder 3 at f53
        show yuri zorder 2 at t55
        m "Come on, Yuri."
        m "Just say it."
        m 2chb "Remember what Ayame said."
        show monika zorder 2 at t53
        mc "Yeah, we're listening."
        "Yuri hesitates but eventually comes around."
        show yuri 2chh zorder 3 at f55
        y "Can we finish the game we were playing before?"
        "Yuri points to the cards that were left from before the gift exchange."
        y "The round is almost finished and..."
        y "Well, we shouldn't leave things unfinished."
        show natsuki 2che zorder 3 at f51
        show yuri zorder 2 at t55
        n "You're just saying that because you were about to win...again."
        show natsuki zorder 2 at t51
        show yuri 3chq zorder 3 at f55
        y "W-What?"
        y "N-No I'm not!"
        show sayori 1chq zorder 3 at f52
        show yuri zorder 2 at t55
        s "Yuri, you're actually soooooo good at that game."
        s 1chr "It's hard for any of us to win with you playing."
        show sayori zorder 2 at t52
        show ayame 1chh zorder 3 at f54
        ay "She's right, you know."
        ay "You're quite skilled."
        show monika 1chl zorder 3 at f53
        show ayame zorder 2 at t54
        m "Come on, [player_casual]s."
        m "You can't say there wasn't any luck involved either."
        show natsuki 1chc zorder 3 at f51
        show monika zorder 2 at t53
        n "Monika, you were last every round we played."
        n "I don't think that's just luck."
        show natsuki zorder 2 at t51
        show monika 1chc zorder 3 at f53
        m "How about this?"
        m 1che "We start a new round, this time including [player]."
        m "That way Yuri gets what she wants and we're doing something as a club."
        m 1cha "Agreed?"
        "No one has any objections."
        m 2chb "Then let's get started."
        m "This time, I'll win."
        show sayori 2cha zorder 3 at f52
        show monika zorder 2 at t53
        s "Ehehe, you shouldn't say things you don't mean, Monika."
        s "We all know I'm going to win."
        show sayori zorder 2 at t52
        mc "Maybe I'll win."
        mc "And I haven't even played it yet."
        show natsuki 4chd zorder 3 at f51
        n "Yeah, right!"
        n "I've come close to winning the most out of everyone."
        show natsuki zorder 2 at t51
        show ayame 1che zorder 3 at f54
        ay "But you haven't actually won yet, have you?"
        show ayame zorder 2 at t54
        show yuri 2cha zorder 3 at f55
        y "I agree with those terms."
        "Yuri takes the cards and begins shuffling them."
        y 2chb "I wish you all luck."
        show yuri zorder 2 at t55
        "That sounded like a threat."
        show monika 2che zorder 3 at f53
        m "Can I just say..."
        m "I'm so glad all of you are here."
        m 4chj "I wouldn't spend Christmas with any other group of people."
        m "Merry Christmas, everyone!"
        show sayori 4chq zorder 3 at f52
        show monika zorder 2 at t53
        s "I feel the same!"
        s "Merry Christmas, everybody!"
        show sayori zorder 2 at t52
        show ayame 1che zorder 3 at f54
        ay "Likewise!"
        ay "Happy holidays!"
        show natsuki 4chq zorder 3 at f51
        show ayame zorder 2 at t54
        n "Yeah, I guess you're right."
        n 4cht "Merry Christmas or whatever..."
        show natsuki zorder 2 at t51
        show yuri 3chs zorder 3 at f55
        y "The feeling is mutual."
        y 3chu "Merry Christmas."
        show yuri zorder 2 at t55
        mc "Merry Christmas to all of you."
        show yuri 3chf zorder 3 at f55
        y "Now can we start the game?"
        show monika 2chb zorder 3 at f53
        show yuri zorder 2 at t55
        m "May I deal the cards next round?"
        m "I almost didn't come last every time I have."
        m "I mean--"
        show monika zorder 2 at t53
        show yuri 1chf zorder 3 at f55
        y "Sure, Monika."
        "Yuri starts dealing out the cards for this round."
        y 2chl "But it won't make a difference."
        "She looks fiercely competitive."
        y 2chm "Now, let's begin."
        show monika 1cha zorder 3 at f53
        show yuri zorder 2 at t55
        m "Can I have a moment with [player] first?"
        m "It's a private conversation, so we'll just talk outside."
        show sayori 1cha zorder 3 at f52
        show monika zorder 2 at t53
        s "Of course, we'll still be here when you come back."
        s "Take your time!"
        show sayori zorder 2 at t52
        show monika 1chb zorder 3 at f53
        m "Thank you."
        m "[player]?"
        "Monika heads towards the main door."
        m 2cha "Follow me for a moment."
        scene bg ay_house with wipeleft_scene
        play music t6 fadeout 2.0
        "Monika takes us outside and closes the door behind her."
        show monika 1cha zorder 2 at t11
        m "Okay, now we're alone."
        mc "What's this about?"
        mc "Do you want me to help you win or something?"
        m 1chc "No."
        m "It's about you."
        m 1che "I sensed something about you today."
        m "You seemed different somehow."
        mc "I do?"
        m "It's like I've finally found what I'm searching for."
        m 1chc "Even though I don't really know what it is yet."
        mc "I'm not sure I understand..."
        m "Neither do I."
        m 1che "Can I just look at you for a second?"
        mc "Uh...okay."
        "Monika stares at me."
        "It's as if she's staring into my soul for some kind of answer."
        mc "Anything?"
        m 2chf "I don't know."
        m "But..."
        m "If there's someone out there listening."
        m 2che "Thank you."
        m "I know you can't stay."
        m "This isn't your world..."
        m "Your...reality."
        m "But now I know what I have to do."
        m 2chl "And if there really is no one out there..."
        m "Then I must look like an idiot speaking to the wind, right?"
        mc "..."
        m 2cha "Come on, let's get back inside."
        m 2chb "Yuri probably already forced them to play a round while we were here."
        m "And won it."
        mc "She's really that good?"
        m "Ahaha, just lucky~"
        show monika at lhide
        hide monika
        "Monika heads back inside."
        "I look around and smile to myself once more before following her."
        stop music fadeout 1.5
        $ pause(1.5)
        scene bg ay_house_gray with Dissolve(1.5)
        $ s_name = "???"
        $ quick_menu = False
        $ style.say_window = style.window_flashback
        s "So that's how it is in this timeline."
        s "They look so happy."
        s "I kinda wish we were like that."
        s "I mean..."
        s "It's still possible, isn't it?"
        s "I can only hope."
        if not persistent.arc_clear[2]:
            s "I guess we'll meet Ayame in the future."
        else:
            s "I guess that's how Ayame is."
        s "And that clerk..."
        if not persistent.arc_clear[1]:
            s "He seems so strange but seemed like he knows a lot."
            s "I have a feeling I'll meet him soon."
        else:
            s "I didn't realize the clerk was also here."
            s "I wonder if he's anything like the one I know..."
        s "But it's not like I'll remember any of this."
        s "At least, I don't think I will."
        s "It is an alternate timeline, after all."
        s "But thank you."
        s "I got to see everyone happy."
        s "That's all that really matters in times like this..."
        s "And now it's time to go back."
        s "Back to our timeline."
        s "Back to what awaits us..."
        scene black with dissolve_scene_full
        $ persistent.did_christmas_event = True
        $ christmas_chapter = False
        $ get_achievement("*It's Christmas!*")
        $ pause(1.0)
        $ style.say_window = style.window
        $ quick_menu = True
        $ renpy.utter_restart()
    return
