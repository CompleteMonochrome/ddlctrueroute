# Literally poem response start except not
label giftexchange_start:
    $ poemsread = 0
    $ skip_transition = False
    label giftexchange_loop:
        $ skip_poem = False
        if renpy.music.get_playing() and not (renpy.music.get_playing() == audio.t5christmas or renpy.music.get_playing() == audio.t5c):
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
        $ skip_poem = False
        if poemsread == 0:
            $ menutext = "Who should I exchange gifts with first?"
        else:
            $ menutext = "Who should I exchange gifts with next?"

        menu:
            "[menutext]"

            "Sayori" if not s_readpoem:
                $ s_readpoem = True
                "I wonder what Sayori got me. Hopefully something she knows I like."
                "She's my good friend, after all."
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
            "Monika" if not m_readpoem:
                $ m_readpoem = True
                "The clerk seemed really different when it came to Monika."
                "Regardless, I hope she enjoys the gift I give her."
                call giftexchange_monika
            "Ayame" if not ay_readpoem:
                $ ay_readpoem = True
                "I don't really know Ayame well."
                "But I'd like to, and hopefully this gift will give us something to talk about."
                call giftexchange_ayame
        $ poemsread += 1
        if poemsread < 5:
            jump giftexchange_loop


    $ s_readpoem = False
    $ n_readpoem = False
    $ y_readpoem = False
    $ m_readpoem = False
    $ ay_readpoem = False
    $ poemsread = 0
    return

label giftexchange_sayori:
    call giftexchange_startmusic
    scene bg ay_livingroom
    show sayori 1cha zorder 2 at t11
    with wipeleft_scene
    s "What's in the box, [player]?"
    mc "You're gonna find out, aren't you?"
    s "I told you, I can't wait!"
    s "Come on! Gimme, gimme, gimme!"
    mc "Alright, calm down..."
    "I hand over the wrapped box with Sayori's name on it."
    "Immediately, she begins tearing it apart."
    mc "Wow..."
    mc "You're really excited for this present, aren't you?"
    s "Ehehe, it's coming from you after all~"
    mc "I wouldn't get my hopes up if I were you."
    s "Why not?"
    "Sayori finishes 'unwrapping' the present."
    "In reality, she basically tore through it, leaving lots of pieces of wrapping paper on the floor."

    $ nextscene = "gift_" + christmas_gifts[0] + "_s"
    call expression nextscene

    s "Well..."
    s "I guess it's my turn to share my gift."
    s "So...here."
    "Sayori hands me a neatly wrapped box."
    "It has a red ribbon holding it all together."
    s "Are you gonna open it?"
    mc "Do you want me to?"
    s "I wanna see your reaction."
    mc "Then I suppose I will."
    "I pull the ribbon and carefully tear the wrapping paper."
    "There's a blank cardboard box inside."
    s "Go on, open it."
    "I open the cardboard box and pull out..."
    mc "Is this a toy plush?"
    mc "Of me?!"
    s "Do you like it?"
    "The plush is actually quite cute."
    "I'd say it captures me pretty well."
    mc "It's a wonderful gift."
    mc "Thank you so much, Sayori."
    s "Aww, you really mean it?"
    mc "Of course I do."
    mc "You had this custom made, didn't you?"
    s "Mhm!"
    s "The guy even charged extra because there was a lot of people doing something like this."
    s "But I paid him anyway."
    mc "Huh? Why?!"
    mc "You don't need to go out of your way for me like that."
    s "It wasn't just for you."
    s "It was for everyone."
    mc "You got everyone else something similar?"
    s "Ehehe, yeah..."
    s "But now I have no money..."
    s "S-So..."
    mc "You're not getting any money from me."
    s "Aww, you big meanie!"
    s "It's Christmas!"
    mc "I know."
    "I give Sayori a hug and she returns it."
    mc "Merry Christmas, Sayori."
    s "Merry Christmas, [player]!"
    call giftexchange_revertmusic
    return

label giftexchange_natsuki:
    call giftexchange_startmusic
    scene bg ay_livingroom
    show natsuki 1chc zorder 2 at t11
    with wipeleft_scene

    $ nextscene = "gift_" + christmas_gifts[2] + "_n"
    call expression nextscene

    mc "Merry Christmas, Natsuki."
    n "Yeah, you too, [player]."
    call giftexchange_revertmusic
    return

label giftexchange_yuri:
    call giftexchange_startmusic
    scene bg ay_livingroom
    show yuri 1cha zorder 2 at t11
    with wipeleft_scene

    $ nextscene = "gift_" + christmas_gifts[1] + "_y"
    call expression nextscene
    mc "Merry Christmas, Yuri."
    y "M-Merry Christmas, [player]..."
    call giftexchange_revertmusic
    return

label giftexchange_monika:
    call giftexchange_startmusic
    scene bg ay_livingroom
    show monika 1cha zorder 2 at t11
    with wipeleft_scene

    $ nextscene = "gift_" + christmas_gifts[4] + "_m"
    call expression nextscene

    mc "Merry Christmas, Monika."
    m "Merry Christmas, [player]!"
    call giftexchange_revertmusic
    return

label giftexchange_ayame:
    # call giftexchange_startmusic
    scene bg ay_livingroom
    show ayame 1chh zorder 2 at t11
    with wipeleft_scene

    $ nextscene = "gift_" + christmas_gifts[3] + "_ay"
    call expression nextscene

    ay "Happy holidays, [player]!"
    mc "Merry Christmas, Ayame."
    # call giftexchange_revertmusic
    return

label gift_plush_s:
    $ christmas_approval += 1
    s "Oh my gosh!"
    s "It's so cuuuuuuuuuuuuuuuuuuuuuuute!"
    s "Thank you, thank you, thank you, [player]!"
    mc "You're really into this, aren't you?"
    s "Why wouldn't I be?"
    s "Doing this is so much fun!"
    mc "Does it look familiar at all to you?"
    "Sayori stares at the cow plush I bought her."
    s "It's..."
    s "It's the same one from my room!"
    mc "That's right."
    s "That's even better!"
    s "It's like a smaller version of it."
    s "This is incredible."
    mc "I think you're overstating what's really happening."
    mc "But I'm glad you're enjoying it."
    return

label gift_book_s:
    s "Eh...?"
    s "A book?"
    s "How Not To Break Things As A Manager?"
    mc "You don't like it?"
    s "I-I never said that."
    s "I'm just wondering about a couple of things."
    mc "What is it?"
    s "Why would I need a book like this?"
    s "And what kind of name is Clark Nick Mysterio Maximilian?"
    mc "I thought if you ever started your own club, you could use it."
    mc "Or maybe if you ever became a manager."
    s "I see..."
    s "Thanks, I guess."
    mc "And the name?"
    mc "I had no idea that was the author's name."
    s "Ehehe, did you even really think about this gift?"
    mc "..."
    s "It doesn't matter."
    s "I'm grateful anyway, [player]."
    mc "I'm glad you're in good spirits, Sayori."
    return

label gift_manga_n:
    return

label gift_anime_n:
    $ christmas_approval += 1
    return

label gift_knife_y:
    $ christmas_approval += 1
    return

label gift_ARM_y:
    return

label gift_bracelet_m:
    $ christmas_approval += 3
    return

label gift_Markov_m:
    return

label gift_Xileh_ay:
    $ christmas_approval += 1
    return

label gift_Edom_ay:
    return

label giftexchange_startmusic:
    $ currentpos = get_pos()
    if poem.author == "monika":
        $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>mod_assets/bgm/5_monikaperfect.ogg"
    elif poem.author == "ayame":
        $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>mod_assets/bgm/5_ayame.ogg"
    else:
        $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_" + poem.author + ".ogg"
    stop music fadeout 2.0
    $ renpy.music.play(audio.t5b, channel="music_poem", fadein=2.0, tight=True)
    return

label giftexchange_revertmusic:
    if music and revert_music:
        $ currentpos = get_pos(channel="music_poem")
        $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>mod_assets/bgm/5christmas.ogg"
        stop music_poem fadeout 2.0
        $ renpy.music.play(audio.t5c, fadein=2.0)
    return

label christmas_chapter:
    # Alternate Reality?
    $ chapter = 999
    scene black
    $ s_name = "???"
    $ cl_name = "???"
    $ audio.t11r = "<from 0 to 38.23 loop 0>mod_assets/bgm/11r.ogg"
    play music t11r
    s "..."
    if persistent.did_special_event:
        s "We're going back again, aren't we?"
    else:
        s "Are we going backwards?"
    s "Or...is it forward?"
    scene bg random_gray with Dissolve(0.5)
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
    s "That isn't too much to ask for...right?"
    s "It's just a moment of happiness in this uncertain world we're in."
    s "We need you to do this but if you're just going to ruin everything then I'd rather not do it at all."
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
    s "{cps=15}But I really hope you know what you're doing...{/cps}{nw}"
    stop music fadeout 1.5
    scene bg mall_interior with Dissolve(1.5)
    play music t2 fadein 3.0
    $ s_name = "Sayori"
    $ style.say_window = style.window_christmas
    "I'm completely useless here."
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
    "I wonder around the mall for a bit, not really paying attention to where I'm going."
    "I've just been trying to figure out what to get everyone but I'm out of ideas."
    show mysteriousclerk 1cha zorder 2 at t11
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
    "The man looks as if he is scanning me."
    cl "Let me guess."
    cl "You're buying last minute Christmas gifts."
    cl "It's for four...no five people."
    cl "And they're all women."
    mc "What?"
    mc "How did you get that just from looking at me?"
    cl "You pick up a few tricks when you're my age."
    mc "Like how to read a person?"
    cl "Something like that."
    "Who is this guy...?"
    cl "I'm the owner of this fine establishment."
    "Did I even say that out loud?"
    "If not, why the hell did this guy just introduce himself like that all of a sudden?"
    cl "The executive officer of this humble abode."
    cl "The master of this venerable estate."
    cl "The--"
    mc "Alright, I get it."
    mc "How did you know I was wondering who you were though...?"
    cl "Like I said, you pick up a few tricks."
    mc "..."
    cl "Anyway, what can I do for you?"
    cl "Want some help getting some gifts?"
    mc "What?"
    mc "No, of course not!"
    mc "Especially not from--"
    cl "Please, my friends call me Clark."
    $ cl_name = "Clark"
    cl 2che "But that's not actually my name!"
    cl "So change it back to those question marks!"
    "What...?"
    $ cl_name = "???"
    cl 2cha "As I was saying..."
    cl "You aren't my friend either."
    cl "So instead, you may call me Nick."
    $ cl_name = "Nick"
    mc "Right...Well, I was just about to leave, {i}Nick{/i}."
    mc "So, if you don't mind."
    "I try to make my way past him but he blocks my way."
    cl "Ho, ho, ho little [player_other]."
    cl "Are you sure you wanna do that?"
    cl "I know exactly the sort of thing those girls would like."
    cl "Well, it's more of a fifty-fifty."
    cl "But it's better than getting them nothing, am I right?"
    mc "Look, I'm not sure how exactly you knew this much already."
    mc "But I really doubt you know enough about those girls to know what gift to get them."
    cl "Is that a test?"
    if player_gender == "boy":
        cl "Good sir, are you challenging my knowledge?"
    else:
        cl "Madam, are you challenging my knowledge?"
    "I let out a quiet sigh."
    "I just want to get out of here."
    "This guy is seriously getting on my nerves."
    cl "The girl you were thinking of just before."
    cl "She has red hair and eyes as blue as a sapphire."
    cl "She's clumsy but she has everyone's best interest as heart."
    cl "She's the nicest person you know and she's always looking out for others."
    cl "She's the main reason you're even out here doing this."
    cl "Because without her, you would have never met the other four."
    mc "What...?"
    cl "Tell me I'm wrong."
    "There is no way this guy could have figured that out just from looking at me."
    "This has got to be some kind of trick."
    "Did Sayori set this guy up?"
    "But then how would she have known I'd end up here?"
    cl "Just hear me out, okay?"
    cl "You can make the decision in the end."
    mc "Fine."
    cl "Splendid!"
    cl "Right this way."
    "The man takes me to a section of the store."
    "There's all sorts of fluffy animals here."
    "I guess the store has more than just books and electronics."
    cl "Now any of these would probably do great with her."
    cl "But let's be honest, anything you give her would make her day."
    cl "Unless it's something crazy and offensive, right?"
    mc "I suppose."
    cl "If you don't like those then maybe something more shocking will do."
    mc "Shocking? I don't think--"
    cl "Like this incredible limited time offer on this book."
    cl "It's called \"How Not To Break Things As A Manager\", it's ninety percent off."
    cl "What do you say, [player]?"
    "I didn't even tell him my name...did I?"
    mc "What?"
    mc "Why would she need this?"
    mc "What use would--"
    cl "You're in some kind of book club, right?"
    cl "This is a book."
    cl "See the connection?"
    "The man taps his finger on his head."
    mc "I...guess?"
    mc "But I'm definitely not going to--"
    cl "It's {i}your{/i} choice, okay?"
    cl "I ain't gonna force you to do anything."
    cl "Just be sure you actually know what you're doing."
    cl "If you don't...well, there might be consequences."
    mc "What kind of consequences?"
    cl "Consequences that could affect other worlds, you know?"
    "I've made up my mind."
    "This guy is insane."
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
    cl "Great!"
    "Without even letting me finish, Nick takes the [christmas_gifts[0]] and puts it into a plastic bag."
    "Did he know I was going to go for that?"
    cl "Now moving on."
    cl "How about we get a gift for the tall one?"
    mc "The tall one?"
    cl "The creepy one."
    mc "Creepy one? No one is--"
    cl "You know the one, likes horror books..."
    cl "Has a knife collection..."
    mc "What?!"
    cl "The gifts for her are right over here."
    cl "So come on!"
    cl "Get a move on!"
    cl "You don't have much time, let's go, let's go."
    mc "Jeez, I'm going..."
    mc "Can you at least tell me how you learned all of this information?"
    mc "I know you said you picked up a few tricks but..."
    mc "What the hell does that even mean?"
    mc "There's no way you can just know everything about someone from looking at them."
    cl "Who said I knew everything about you?"
    cl "The mundane things about a person are not my specialty."
    cl "I wouldn't care to learn those things about someone."
    cl "Like your favorite color."
    cl "Who even cares about that?"
    cl "Like come on, really?"
    mc "So you've learned about me?"
    mc "How?"
    cl "Oh, I said that out loud."
    cl "Well, never mind!"
    cl "Forget I said anything."
    mc "No, now I'm curious."
    mc "Tell me, come on."
    mc "I deserve to know how you know so much about me."
    mc "Are you my stalker or something?"
    cl "What? No!"
    cl "That's way too creepy."
    cl "It's simply--"
    cl "Wait, why am I being interrogated by some kid?"
    "Nick points to another place in the store."
    cl "Come on, move it."
    cl "Or don't you want to get the rest of them something?"
    cl "So how about you stop asking questions and I'll help you pick out the rest of the gifts?"
    mc "Okay, I can deal with that."
    cl "Splendid, just splendid!"
    cl "And here we are..."
    "We arrive at the section of the store stocking...sharp objects."
    "That's probably the best way to describe it."
    "There's a lot of sharp things on display, half of which I don't know the name of."
    "There's even a katana for sale and the sign says authentic."
    "What does that even mean?"
    cl "Now you can either choose this really cool looking knife here."
    "Nick points to a small ornate knife with intricate designs on it."
    "The shape of it is completely unique, unlike anything I've seen and each edge looks like it was carved with care."
    "It has its own matching scabbard to place it in too."
    cl "She'll love this."
    mc "How can you know that for sure?"
    cl "Young [player_other], look at the craftsmanship on this."
    cl "You won't see this anywhere else."
    cl "It's one of a kind."
    cl "Tell me that isn't top quality, top notch stuff."
    mc "I don't know much about knives."
    mc "So I can't tell you otherwise."
    mc "It does look really nice, I suppose."
    cl "She'll love it."
    cl "But..."
    cl "There is an alternative, you know."
    mc "And what exactly is that?"
    cl "Well, you and I both know she has a habit of..."
    cl "Ehm."
    "He makes a slicing gesture on his arm."
    cl "Or, at least she did."
    cl "Who knows if she still does?"
    mc "What's your point?"
    cl "I've got just the thing to prevent that kind of thing ever happening again."
    "Nick points to the display opposite the knife."
    cl "I call it the Automated Responder Mechanism."
    cl "Or ARM for short."
    cl "It goes on your arm and every time you'll try to cut it..."
    show mysteriousclerk at h11
    cl "Bam!"
    "The clerk claps his hands together."
    mc "Bam?!"
    mc "Why would I want that to happen?"
    cl "It was a figure of speech."
    cl "What I meant was, it will automatically activate some magnets and keep the knife stuck to it for a while."
    mc "What if she has like a wooden knife or something?"
    cl "Kid, who in the world uses a wooden knife?"
    mc "Isn't that knife over there made of wood?"
    "I point to the knife he showed me earlier."
    cl "Uhhhhhhhhhh..."
    show mysteriousclerk zorder 2 at h11
    cl "Look!"
    cl "It's the thought that counts, okay?"
    cl "By buying this, you're showing her you care about her wellbeing."
    cl "So make your choice."
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
    cl "Wonderful, absolutely wonderful!"
    cl "Immediately, the clerk places the [christmas_gifts[1]] into the same plastic bag."
    mc "Did you just refer to what you were doing in the third person?"
    cl "What of it?"
    mc "Never mind."
    cl "Who next?"
    cl "Ooh, how about that tsundere girl?"
    mc "Tsundere girl?"
    cl "You know the one."
    cl "I'm sure."
    mc "Eh..."
    cl "Now I'll divert your attention over here."
    "The clerk starts moving around the store again at a much faster pace than before."
    mc "Does anyone else work here?"
    cl "Nope, it's a family business."
    cl "By family, I mean my family."
    cl "By my family, I mean--"
    mc "I don't really need to know the details."
    cl "Suit yourself, kiddo."
    cl "Anyway, we're here."
    "Nick presents a whole lot of manga and anime to me."
    "I guess we're in that section of the store now."
    "This store seems to have everything in it."
    "I thought the books on the shelves were just novels or something."
    "But as it turns out..."
    cl "Hmm..."
    cl "Now where was that manga...?"
    cl "Oh, yes!"
    cl "Here it is."
    "He hands over a single volume of a manga I've never seen before."
    mc "What's this?"
    cl "What's it look like?"
    cl "It's obviously a stapler."
    "The manga he gave me is called \"Donut Purr Chase\" and features a cute cat on the front cover."
    "I look at the first few pages."
    "I can't really get what the story is about."
    "The art is also...questionable."
    "Some panels have extremely good detail while others are literally stick figures."
    mc "I don't know if she'll like this."
    cl "Why not?"
    cl "It's really quite sweet."
    cl "I mean that literally, like trying smelling it."
    "The book does somehow give an aroma of freshly baked cupcakes."
    cl "The story is..."
    cl "Well, that's spoilers."
    cl "If you don't want to get her that, then..."
    cl "There's always this."
    "The clerk holds out a small box labeled--"
    cl "Parfait Girls, the complete collection."
    cl "In anime form."
    mc "That would be nice."
    mc "But I think she already has that, doesn't she?"
    cl "No."
    cl "She has the collection of manga."
    cl "Not the anime collection."
    mc "How do you know?"
    cl "Look, this is on sale for ninety percent off."
    cl "It's...clearance."
    cl "So you can take the single volume of manga or this collection."
    cl "They'll be around the same price anyway."
    mc "If I buy the anime collection and she already has it, then what?"
    cl "If you buy the manga and she doesn't like it, then what?"
    cl "Maybe you won't get any cupcakes at your little Christmas party."
    cl "Just make up your mind, [player_gender]."
    mc "What do you think I should get then?"
    "The clerk shrugs."
    cl "Not my choice to make."
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
    cl "Done and done."
    "The clerk basically shoves the [christmas_gifts[2]] into the plastic bag."
    cl "Who next?"
    cl "How about the new girl?"
    cl "I know you need help picking out a gift for her."
    mc "What gives you that idea?"
    cl "For one, you barely know her."
    cl "Didn't you only meet a couple days ago?"
    mc "Well...yeah but--"
    cl "And two, the only thing you do know about her is that she's super rich."
    cl "Which means..."
    cl "She has everything she could ever want."
    mc "Ah...that's true."
    mc "I have no idea what to get her."
    mc "Even if you suggested something to me, I wouldn't know if that would be a good or bad thing to get."
    cl "Luckily for you, I know her quite well."
    mc "And how would--"
    cl "She came in here before, you know."
    cl "Granted, she didn't buy anything."
    cl "She said I was \"too weird\" and left."
    cl "But what she didn't know is that I already read her like a piece of source code."
    $ _history_list[-1].what = "\"But what she didn't know is that I already read her like a book.\""
    mc "Like a what?"
    cl "Like a book."
    cl "Did you not hear me?"
    mc "Uh...right."
    mc "So what did you learn about her that I could me choose a gift for her?"
    cl "I only got a short glimpse."
    cl "But I think I have just the things."
    cl "The clerk directs [player] to the section of the store filled with artifacts."
    $ _history_list[-1].what = "The clerk directs me to the section of the store filled with artifacts."
    $ _history_list[-1].who = None
    "He's doing it again."
    $ _history_list[-1].what = "\"He's doing it again.\""
    $ _history_list[-1].who = player
    cl "What am I doing?"
    "He heard me? I swear I didn't say that."
    mc "You referred to yourself in the third person."
    cl "I assure you, I didn't."
    cl "Why don't you check your recent {i}history{/i}, [player]?"
    "Recent history?"
    "It feels like the more I talk to this guy, the more brain cells I lose."
    cl "Jeez, kids these days."
    "The clerk shakes his head in disapproval."
    cl "But I'm not here to lecture you."
    cl "I'm here to help you get these fancy looking artifacts as a gift."
    mc "Which one would she like?"
    cl "All of these are exclusive artifacts dug by my very own debuggers."
    $ _history_list[-1].what = "\"All of these are exclusive artifacts dug by my very own archaeologists.\""
    cl "So any of them would be perfect."
    cl "But since I know you're clueless and all."
    cl "I'd recommend one of these two."
    "He points me towards two strange looking rocks."
    cl "I call these two the monster fossils."
    cl "They're not really traditional artifacts but there is some sort of mystical presence within them."
    cl "So I call them artifacts."
    mc "Why would she want monster fossils?"
    mc "But more importantly how can you afford to--"
    cl "Let's focus on the gifts okay?"
    cl "She may not look it but she's actually a hunter."
    cl "When she has time, she likes to go hunting with her parents."
    mc "Interesting but that has nothing to do with why she'd be interested in monster fossils..."
    cl "Or does it?"
    "The clerk stares at me intensely."
    mc "...It doesn't."
    cl "Or does it?!"
    mc "It really doesn't."
    cl "That's true, I guess."
    cl "So which fossil will it be?"
    cl "The Xileh fossil..."
    "The clerk points to the fossil with what looks like a snail carved onto it."
    cl "...or the Emod fossil?"
    "He points to the other fossil which has some sort of crab on it."
    cl "Choose carefully."
    cl "If you choose the wrong one, you might anger all the wrong people."
    cl "Including Ayame."
    mc "How the hell am I suppose to choose then?"
    mc "I don't know anything about these fossils."
    cl "Take a wild guess."
    cl "Try playing around with the letters of the words in your head or something."
    mc "How is that going to help?"
    cl "I think she likes Oman--"
    cl "Ohoho, never mind."
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
    cl "Oh yeah, meant to be."
    cl "Why?"
    mc "...No reason."
    cl "Strange kid."
    "The clerk starts lifting the plastic bag he's carrying up and down."
    "It's as if he's trying to test the weight of it or something..."
    cl "One more gift, right?"
    mc "I guess so."
    cl "You don't wanna mess this up."
    cl "The last girl is..."
    "Nick pretends to think for a moment."
    cl "Charming, charismatic, beautiful."
    cl "She's a wonderful person."
    cl "She's also a very special person."
    cl "Not to just to you but..."
    cl "N-Never mind."
    cl "Just don't mess this up, okay?!"
    "The man drops the bag and grabs my shoulders and begins frantically shaking me."
    mc "Alright, whatever!"
    mc "Just stop shaking me around and let go of me!"
    "I push his hands off of my shoulders and he Immediately picks up the plastic bag as if nothing happened."
    mc "Don't worry, I don't want to mess any of this up."
    mc "Why I'm taking suggestions from a stranger who knows way more than he should is beyond me."
    cl "Same."
    $ _history_list[-1].what = "\"It's because you aren't original and can't think for yourself.\""
    cl "But anyway, let's get to it."
    cl "The thing you should get her is actually behind the counter."
    mc "Behind the counter?"
    cl "Yeah..."
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
    show mysteriousclerk 1cha zorder 2 at t11
    with wipeleft_scene
    if christmas_gifts[4] == "Markov":
        "Nick takes--"
        cl "Just call me Mysterious Clerk or something, okay?"
        $ cl_name = "Mysterious Clerk"
        mc "Huh?"
        cl "Only people who deserve it can call me Nick."
        cl "I hope you like coal, [player]."
        $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
        if not list(set(process_list).intersection(stream_list)):
            if currentuser != "" and currentuser.lower() != player.lower():
                cl "Or should I say [currentuser]?"
    "[cl_name] takes us to the counter and places the plastic bag."
    "One by one he scans each of the items."
    "The price shows up on the register."
    "It's..."
    if cl_name == "Nick":
        cl "...a lot cheaper than what you were expecting, huh?"
        cl "You deserve a discount."
        cl "I'd give it to you for free but I gotta make a living, you know?"
        mc "Wow..."
        mc "Why do I deserve a discount exactly?"
        cl "No reason."
        cl "I'm erratic, maybe I can jack up the price instead."
        mc "No, that will be fine."
        mc "Thank you."
        mc "I'm curious though..."
        mc "I know you have your team of...whatever."
        mc "But have you always worked alone for this kinda stuff?"
        cl "Well..."
        cl "There used to be four others."
        cl "But they kinda...faded away."
        mc "You drifted apart?"
        cl "Something like that."
        "I pay the bizarre price on the register and take the plastic bag with the gifts."
        cl "Have a nice day, [player]."
        cl "Hahaha, hopefully they like your gifts."
        cl "Farewell!"
        show mysteriousclerk at thide
        hide mysteriousclerk
        "I begin to walk away."
        mc "Thanks, I might come here again sometime."
    else:
        cl "The price has increased for my services in helping you."
        cl "Now, pay up!"
        mc "E-Eh?"
        mc "This is like the price of everything I'm buying twice over."
        cl "Your point?"
        cl "The more you waste my time, the more expensive it gets."
        "I pay the bizarre price on the register and take the plastic bag with the gifts."
        cl "Good day!"
        show mysteriousclerk at thide
        hide mysteriousclerk
        "I begin to walk away."
        mc "Well...I don't know if I'll come back here any time soon then."
    "I turn around to try to see his reaction but..."
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
    show sayori 1ba zorder 2 at t11
    s "Heeeeey!"
    mc "What is it, Sayori?"
    s "Just wondering what you have there."
    s "Those aren't gifts, are they?"
    s "You didn't go last minute shopping, did you?"
    mc "I'm not gonna answer that."
    mc "So what are you here for really?"
    s "I just want to thank you."
    mc "For what?"
    s "For doing this."
    s "I know you have other people you'd rather spend Christmas with."
    s "I'm glad you're doing it with the club."
    mc "It's really not a problem."
    s "If you say so."
    s "Don't forget to wrap your gifts~"
    mc "Well, I was going to do that now."
    mc "But you're in my way."
    s "Oh..."
    s "Then, see you tomorrow!"
    mc "See you tomorrow."
    s "Don't be late."
    show sayori at thide
    hide sayori
    "Sayori hurries off home, probably to finish wrapping her own gifts."
    "Something tells me I will be late."
    "But I can't worry about that now, I got gifts to wrap."
    "Good thing I don't have to write a poem tonight."
    stop music fadeout 2.0
    if christmas_gifts[4] == "Markov":
        call poem(False,20,True,"Monika")
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
    ay "Oh, hehehe..."
    ay "Sorry, I'm very sorry."
    "Ayame bows her head."
    mc "You don't need to do that."
    mc "We're friends, after all."
    "Ayame lifts her head up."
    ay "Right, we're friends!"
    "She smiles widely."
    ay "Well, {i}friend{/i}. Come on in!"
    ay "We're just about ready to do the gift exchange."
    "She can see me staring."
    ay "Surprised? The others reacted like that too."
    ay "And trust me, yours wasn't even the best reaction!"
    ay "Now come oooooooooooooon!"
    "Ayame takes my hand and drags me inside."
    scene bg ay_livingroom
    show ayame 1chd zorder 2 at t11
    with wipeleft_scene
    play music t3 fadeout 2.0
    "Ayame takes me to her living room."
    "The other four are already there waiting."
    "They're playing some kind of card game, probably to pass the time."
    "Looking around the room, it's quite spacious."
    "I feel like there's a lack of furniture in here just by how big it is."
    "I'm still at awe at how big her home is."
    "But I guess I shouldn't be so surprised considering where she lives..."
    ay "Listen, I gotta quickly take care of something."
    ay "I just remembered."
    ay "Silly me, haha."
    mc "Ha..."
    "I force out an awkward laugh."
    ay "Anyway, let them know you're here."
    ay "I won't be a moment."
    mc "Okay, good luck."
    ay "Thanks~"
    show ayame at thide
    hide ayame
    "Ayame runs off and I slowly enter the room."
    "I was going to try to surprise them but..."
    show sayori 1cha zorder 2 at t11
    s "[player]!"
    s "You're sooooooooooo late!"
    mc "Hello, Sayori."
    s "What took you so long?"
    s "We've been here for ages!"
    show sayori zorder 2 at t21
    show monika 1cha zorder 3 at f22
    m "Don't get the wrong idea."
    m "You really aren't that late."
    m "And we've kept ourselves entertained."
    show natsuki 1cha zorder 3 at f31
    show sayori zorder 2 at t32
    show monika zorder 2 at t33
    n "Yeah, this place is huge..."
    n "We spent like an hour just looking through every room."
    n "I don't like it."
    show natsuki zorder 2 at t41
    show sayori zorder 2 at t42
    show monika zorder 2 at t43
    show yuri 1cha zorder 3 at f44
    y "Um...I don't mean to interrupt this conversation."
    y "But I believe it's your turn, Monika."
    "Yuri looks at me from behind one of the cards she's holding."
    y "Glad you could make it, [player]."
    show yuri zorder 2 at t44
    "It seems all the girls are wearing something to commemorate Christmas."
    "Meanwhile, here I am just wearing plain regular clothes."
    "I really should have worn something more...festive."
    show monika zorder 3 at f43
    m "Oh, right."
    m "But I think now is a good time to stop."
    m "We're all here, after all."
    m "It would be a great time to start the gift exchange, right?"
    m "What do you think, Sayori?"
    show sayori zorder 3 at f42
    show monika zorder 2 at t43
    s "Huh?"
    s "I dunno, you're the pres and all."
    s "You should make the decision."
    show natsuki zorder 2 at t51
    show sayori zorder 2 at t52
    show monika zorder 2 at t53
    show ayame 1chd zorder 3 at f54
    show yuri zorder 2 at t55
    ay "Phew..."
    ay "Sorry I'm late!"
    ay "I had to take care of something quickly."
    ay "Are we ready to start the gift exchange?"
    show monika zorder 3 at f53
    show ayame zorder 2 at t54
    m "Ahaha, I suppose we are."
    m "Okay, every--"
    "Monika stops herself suddenly."
    m "Hmm..."
    show monika zorder 2 at t53
    mc "Is something wrong?"
    show monika zorder 3 at f53
    m "Well...no."
    m "It's just that it feels like its been a while since I've addressed the club like this."
    show natsuki zorder 3 at f51
    show monika zorder 2 at t53
    n "What are you talking about?"
    n "You've always addressed the club like this."
    n "In fact, you did it the last time we all saw each other."
    show natsuki zorder 2 at t51
    show monika zorder 3 at f53
    m "I suppose..."
    m "Though I meant as the--"
    "Monika simply smiles."
    m "Never mind, let's just get started."
    m "Okay, everyone!"
    m "I want to make something clear before we begin."
    m "When you get your present, you are allowed to open it if you want to."
    show monika zorder 2 at t53
    show yuri zorder 3 at f55
    y "Isn't tomorrow the day that's meant to happen?"
    show monika zorder 3 at f53
    show yuri zorder 2 at t55
    m "Well, yes."
    m "But I know some of you are more eager than others to open your gifts."
    m "Plus, it's not really compulsory to open it tomorrow."
    show sayori zorder 3 at f52
    show monika zorder 2 at t53
    s "I have a question."
    s "...Can we get started already?!"
    s "I can't wait!"
    show sayori zorder 2 at t52
    show monika zorder 3 at f53
    m "It's time to exchange our presents!"
    call giftexchange_start

    $ persistent.did_christmas_event = True
    $ christmas_chapter = False
    $ pause(1.0)
    $ style.say_window = style.window
    $ renpy.utter_restart()
    return