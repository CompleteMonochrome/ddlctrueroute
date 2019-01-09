label ch6_main:
    scene black
    show monika 1f zorder 2 at i11
    if from_custom_start:
        hide screen tear
        $ from_custom_start = False
        $ quick_menu = True
    else:
        with dissolve_scene_full
    play music mend
    m "Um..."
    m "I'm not exactly sure what just happened."
    m "It's like all of yesterday just stopped happening all of a sudden."
    m 1g "Sayori, if you're listening..."
    m "Did you have anything to do with that?"
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    $ pause(2.0)
    hide screen tear
    show sayori 1d zorder 3 at i21
    show monika 1c zorder 2 at i22
    show sayori at f21
    s "Sorry!"
    s "I'm not used to doing this."
    s 1f "The next day isn't meant to exist..."
    s 1b "And I know {i}you{/i} helped Monika make Saturday a reality..."
    s "So I looked into figuring how you did it..."
    s "I thought I'd try to create it while Monika was performing."
    s 1k "It turns out that it broke the game..."
    s "I think I know how to prevent that from happening again..."
    s 1d "So there's no need worry about helping me make those files."
    s 1u "You know, when the game broke it was really scary..."
    s "I couldn't feel anything but at the same time all my senses were being violated..."
    s "It was just completely dark and it hurt so much..."
    s "There was this terrible noise that wouldn't stop."
    show sayori zorder 2 at t21
    show monika 1q zorder 3 at f22
    m "..."
    m "So, that's it?"
    m 1f "I didn't experience anything..."
    m "But when I was the president I'd have that same awful sensation."
    m "I used to hear that same deafening noise as well, every time the real [player] closed the game..."
    m "Instead, I just ended up here after yesterday ended."
    m "I'm still not sure why I'm able to be part of things like this if I don't have what you have Sayori."
    m "But the reason you're experiencing stuff like that is probably because you're the president now."
    m "Sayori..."
    m "I'm sorry."
    m "I don't want you to go through what I did."
    m "Everything will change..."
    m 1p "You'll start to become like the old me and..."
    show sayori 1d zorder 3 at f21
    show monika zorder 2 at t22
    s "Monika..."
    s "It's okay."
    s "I accept this responsibility, if it means my friends will end up happy."
    s 1k "And I know you're probably still blaming yourself for what the old you did."
    s 1g "But you aren't that person."
    s 1d "You're better than her."
    s "And if {i}you're{/i} listening, it can only mean you care about everyone else as much as I do."
    menu:
        s "Isn't that right?"
        "Yes.":
            s "You didn't really need to respond to that."
            s 1a "I can tell that you're a good person."
        "No.":
            $ sayori_personality += 1
            s 1h "E-Eh?"
            s "You don't mean that..."
            s "After all, you went this far already..."
    s 1d "Anyway..."
    s "I'm sorry about yesterday..."
    s "I guess it means we won't be getting any new members..."
    s 1f "I can't be completely sure but I think everyone's going to forget everything."
    s "I think it's probably the game's failsafe, but like I said I don't really know."
    show sayori zorder 2 at t21
    show monika 1f zorder 3 at f22
    m "Does that include me?"
    m "..."
    m 1p "It's so scary not knowing what's happening..."
    m "As the president, there was so many things I could do..."
    m 1o "But now, I feel so helpless."
    show sayori 1h zorder 3 at f21
    show monika zorder 2 at t22
    s "I don't know whether you'll keep your memories Monika."
    s "I'm still getting used to this..."
    s 1k "I can't do things the way you could..."
    s "But I'm trying my hardest, you have to believe me."
    s 1d "I want everyone to be as happy as you were..."
    s "...when [player_personal] told you that [player_personal] loved you."
    s "Ah, we don't have much time left..."
    s "...today is about to start..."
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() != player.lower():
            s "[currentuser]...?"
    s "I hope you'll do the right thing for everyone in the days to come."
    stop music fadeout 2.0

    scene bg residential_day
    with dissolve_scene_full
    $ put_small_characters()
    play music t2
    "It's an ordinary school day, like any other."
    "As usual, I'm surrounded by couples and friend groups walking to school together."
    "Normally, Sayori is the one waiting outside my house."
    "But today, it seems that I'm the one waiting for her."
    show sayori 1a at t11
    s "Hey, [player]..."
    s 1c "Sorry, I was a bit preoccupied this morning."
    s "I woke up really early today, I guess I just lost track of time..."
    mc "What were you doing that had you up so early?"
    s 1b "Well, I had to do some preparations for the club today."
    s 4a "We're gonna do something really fun!"
    mc "Are you going to tell me what that is?"
    s 4r "Nope!"
    s "It's gonna be a surprise~"
    mc "Speaking of which..."
    mc "Did we still have to write poems?"
    mc "I mean you weren't really clear whether we had to yesterday."
    mc "But I didn't want to be {i}that{/i} person and not have one to share."
    s 1n "Um...well I guess I didn't say anything about it, did I?"
    s "I just thought we'd all keep doing it, since it's become a habit."
    mc "Did you write one?"
    "Sayori suddenly avoids eye contact."
    s 1l "Y-Yeah! I'm the president of the club, of course I did."
    s "It might need a little work before I'm ready to share it though..."
    "By the way Sayori is acting, I can only guess she didn't write a poem for today."
    "It's a little irresponsible for her but I don't blame her if she was working on something for the club this morning."
    mc "Whatever you say Sayori..."
    s 1a "Ehehe, I hope you're ready to have a whole lot of fun today."

    scene bg corridor with wipeleft_scene
    "The day ends pretty quickly and soon it's time to go to the Literature Club."
    "Making my way to the club I see Monika struggling with some books."
    show monika 1e zorder 2 at t11
    m "Ah!"
    play sound "sfx/fall2.ogg"
    $ pause(1.5)
    "Monika drops some of the books she was carrying."
    mc "Did you need some help?"
    m "[player]? I thought you'd be inside by now."
    m 1a "But I'd definitely appreciate if you could pick those up."
    "I pick up the books she dropped on the floor."
    "A lot of them are copies of each other, some novels and some manga."
    "They seem pretty uninteresting but something catches my eye."
    "A single book titled \"Portrait of Markov\"."
    "There's an ominous-looking eye symbol on the front cover."
    "I can't quite put my finger on it but it seems oddly familiar."
    "I ignore the urge to think about it and put it back with the rest of the books."
    m 1b "Thanks, [player]."
    mc "What are you doing?"
    m 1a "I was just getting some books from the library for the club."
    m "Sayori has something planned with them, she wouldn't tell me what exactly."
    m 1c "She just told me to get these specific ones, like she had a list and everything."
    m 1l "Honestly, I was a little surprised she knew all of this was in there."
    mc "Ah...I guess this is what the big surprise was?"
    mc "She's getting us to read books?"
    m 1e "Ahaha, I guess we'll find out."

    scene bg club_day with wipeleft_scene
    "Monika and I enter the clubroom carrying the books."
    "Everyone is here already doing their own thing."
    show monika 1e zorder 2 at t21
    show sayori 4a zorder 3 at f22
    s "Hi Monika, did it go okay?"
    show monika 2c zorder 3 at f21
    show sayori zorder 2 at t22
    m "Ah, yeah..."
    m "I had a little trouble getting them all here."
    m 3a "It's okay though! [player] has the rest of them."
    show monika 1a zorder 2 at t21
    show sayori zorder 2 at t22
    "Monika puts the books down on a desk and I follow her lead."
    mc "So what's this big surprise you told me about?"
    mc "We're not just going to be reading books, are we?"
    mc "Surely you have something more fun planned."
    show sayori 1c zorder 3 at f22
    s "There's nothing wrong with reading books, is there?"
    s 4a "And anyway, I was thinking we should diversify a bit..."
    show monika 2d zorder 3 at f21
    show sayori zorder 2 at t22
    m "Diversify?"
    m "What do you mean?"
    show monika zorder 2 at t21
    show sayori 2b zorder 3 at f22
    s "Well, you know how Natsuki is usually reading manga?"
    s "And how Yuri is always reading novels?"
    s "I thought that maybe we could become closer if we all read the styles of literature other people read."
    s "So Yuri would be reading manga and Natsuki would be reading novels as well..."
    s "How does that sound?"
    show monika 2c zorder 3 at f21
    show sayori zorder 2 at t22
    m 4a "That..."
    m "...is actually a pretty good idea."
    m "Well done Sayori, I didn't expect something so intuitive coming from you."
    show monika zorder 2 at t21
    show sayori 3l zorder 3 at f22
    s "Hey...you're starting to sound a lot like [player]."
    s "I'm not sure if you meant that as an insult or anything..."
    s 3d "But I'll take that as a compliment."
    show monika 3n zorder 3 at f21
    show sayori zorder 2 at t22
    m "Ah, I didn't intend to offend you!"
    m "I guess I just had the wrong choice of words."
    m 3e "I definitely meant that as a compliment."
    show monika zorder 2 at t21
    mc "Well, diversifying is one thing but didn't you say this was going to be fun?"
    show sayori 4d zorder 3 at f22
    s "It's more than that."
    s "We're going to be doing it as a club!"
    s 4a "So we'll all be reading the same book."
    "That still sounds..."
    "Kind of dull?"
    s "Then we're going to be reenacting what happened in one of the chapters."
    show monika 2c zorder 3 at f21
    show sayori zorder 2 at t22
    m "Like in the form of a performance?"
    show monika zorder 2 at t21
    show sayori 4q zorder 3 at f22
    s "Yeah!"
    s "It'll be like a short play each time we get through a book!"
    show sayori zorder 2 at t22
    mc "That's certainly not what I expected."
    mc "But I guess it does sound kinda fun?"
    mc "One question though, if we're all reading the same book..."
    mc "Why is there only one copy of this one?"
    "I pick up the copy of \"Portrait of Markov\" from the pile of books and hold it out."
    show sayori 1b zorder 3 at f22
    s "Um...I don't know."
    s "That wasn't on the list of books, was it?"
    show monika 1m zorder 3 at f21
    show sayori zorder 2 at t22
    m "Oh, I didn't mean to keep that with the rest of the books."
    m "It was meant for my own personal time."
    show monika 2e zorder 2 at t21
    if ch5_name == "Monika":
        mc "Didn't you say you usually get your literature online?"
        show monika 2h zorder 3 at f21
        m "I did but I couldn't find this anywhere."
        m "Not even on the website of some bookstores I looked at."
        m 2e "Which is a little weird..."
        show monika zorder 2 at t21
    mc "Now that I've had a chance to get a better look at it..."
    mc "I think I have the same book, Yuri bought me a copy last week."
    "I pull out the book Yuri gave me last week from my bag."
    "It's a match, albeit the library's copy is a bit worse for wear."
    show monika zorder 3 at f21
    m "Well, what do you know?"
    m 1l "It must be a coincidence!"
    show monika zorder 2 at t21
    mc "Yeah, what are the odds?"
    mc "Now that we have three copies of it, it's like there's a {i}Third Eye{/i} here."
    show sayori 1a zorder 3 at f22
    s "Let's get back on track guys."
    s "I think we should start with something we can all read."
    s 4a "Like this!"
    "Sayori pulls out a picture book."
    "It looks like something a five year old would read."
    show sayori zorder 2 at t22
    mc "Sayori..."
    mc "You can't be serious."
    mc "That's hardly literature..."
    mc "And besides, how is that going to help us diversify?"
    mc "From what I know, no one here reads that sort of stuff."
    show sayori 1l zorder 3 at f22
    s "Um..."
    s 1d "Well...what about this one?"
    "Sayori pulls out another book, it looks like a short novel but definitely more appropriate."
    show monika zorder 3 at f21
    show sayori zorder 2 at t22
    m 3a "Ahaha, that would probably be more suitable for us."
    m 1a "I'll start handing them out."
    "Monika puts her copy of \"Portrait of Markov\" into her bag before picking up the other four copies of the novel Sayori suggested."
    "She gently hands one to me before going to Natsuki and Yuri and doing the same."
    "Surprisingly, Sayori pulls a copy from her bag."
    "It doesn't seem to be from the library as the book looks slightly different."
    show monika 2b zorder 3 at t21
    show sayori zorder 2 at t22
    m "There, now everyone has a copy."
    show natsuki 1g zorder 3 at f31
    show monika zorder 2 at t32
    show sayori zorder 2 at t33
    n "What is {i}this{/i} meant to be?"
    n 2b "You know I don't read stuff like this."
    show yuri 1f zorder 3 at f41
    show natsuki zorder 2 at t42
    show monika zorder 2 at t43
    show sayori zorder 2 at t44
    y "I'm of the same mind as Natsuki on this..."
    y "Why have you given us this book?"
    show yuri zorder 2 at t41
    show sayori 4a zorder 3 at f44
    s "Well, we're gonna be reading it together that's why!"
    s 4b "I saw that last week we were all doing our own thing, so this week we could do something as a whole club."
    s "And once we finish it, we'll do a little reenactment of a chapter we all liked."
    s 4d "Only in the club of course! I don't want you guys to be uncomfortable or anything..."
    show yuri 2h zorder 3 at f41
    show sayori zorder 2 at t44
    y "Um..."
    y "Do we have to do this?"
    y "I was okay doing my own thing and--"
    show yuri zorder 2 at t41
    show natsuki 2e zorder 3 at f42
    n "Yeah this seems kinda forced, doesn't it?"
    n "I'm not really sure this is a good idea..."
    show natsuki zorder 2 at t42
    show monika 1f zorder 3 at f43
    m "Aw, come on guys."
    m "Sayori took a lot of time to come up with this."
    m "At least give it a shot before saying it isn't a good idea."
    m 1e "Besides, you might change your mind afterwards."
    show natsuki 1q zorder 3 at f42
    show monika zorder 2 at t43
    n "Fine..."
    n "I guess it is nice getting the whole club involved in something."
    show yuri 1h zorder 3 at f41
    show natsuki zorder 2 at t42
    y "Well..."
    y "I suppose if everyone else is doing it..."
    y 1a "Then I'll join as well."
    show yuri zorder 2 at t41
    show sayori 4q zorder 3 at f44
    s "Yaay~"
    s "Thanks for doing this everyone!"
    s "I'm sure we'll all be better friends after this."
    s 4a "So let's get right into it!"
    show sayori zorder 2 at t44
    "Sayori already had a few desks arranged to form a table."
    "Everyone takes a spot on the table."
    if sayori_confess and ch5_name != "Sayori":
        "Despite Sayori and I being a couple, she didn't really want to force it."
        "The second person I feel closest to is probably [ch5_name], so I take a seat next to her."
    else:
        "Feeling closer to [ch5_name], I decide to sit next to her."
    "Everyone except Sayori inspects the book looking for some indication of what it could possibly be about."
    "Monika seems to be the most interested in it, even looking at the first couple of pages."
    show natsuki 1c zorder 3 at f42
    n "Um...what is this about?"
    n "I'm looking at the blurb but it's really vague."
    show natsuki zorder 2 at t42
    "I get a closer look at the book as well."
    "The name of the book is \"A New Epiphany\"."
    "The cover of the book has five people doing odd jobs around a tree of some sort."
    "Looking at the back, there's a short blurb and not much else."
    "Natsuki was right about the blurb though, it tells basically nothing about what to expect."
    show sayori 1q zorder 3 at f44
    s "I'm not entirely sure!"
    s "I just thought it would be a good book to read."
    s 1a "I guess we'll find out exactly what it has when we finish it, won't we?"
    show monika 3e zorder 3 at f43
    show sayori zorder 2 at t44
    m "If no one is against it..."
    m "I'd like to start it off."
    "She looks around the table and everyone gives her a shrug."
    m "Great!"
    show yuri 1s zorder 2 at t41
    show natsuki 1g zorder 2 at t42
    show monika 1c zorder 2 at t43
    show sayori 1a zorder 2 at t44
    "Monika opens the book to the first chapter and everyone does the same."
    "She starts reading it pretty slow and enthusiastically at first, as if keeping in mind everyone's own reading pace."
    "She speeds up a little bit and the enthusiasm dies as she reads on but soon enough we finish off the first chapter."
    "It was rather short but it introduced four characters who I can only assume are the protagonists."
    "One of them was a lumberjack, another his wife and the other two were their daughters."
    "It mainly introduced the setting of the place, which from the sounds of it sounds like a half century ago."
    "It sounded like it was foreshadowing some darker secret though..."
    show sayori 1c zorder 3 at f44
    s "So what'd everyone think of the first chapter?"
    "Sayori looks around towards everyone expectantly."
    "No one meets her eyes, instead Yuri is fiddling with the book, Natsuki is looking bored and Monika appears to be lost for words."
    s "Anyone?"
    s 1b "Well, how about you [player]?"
    s "Any thoughts?"
    show sayori zorder 2 at t44
    mc "Well, if I'm honest with you..."
    mc "It seemed kinda dull."
    mc "But..."
    mc "It is only the first chapter, I'm sure it gets really good."
    "I don't fully mean those last words."
    "I'm not into novels like this but if it helps gets some discussion going..."
    show yuri 1f zorder 3 at f41
    y "I-I agree with [player]."
    y "Many of the novels I read usually start off quite dull..."
    y "But once it starts getting into the story..."
    y 1a "It becomes hard to put down and it's like I'm in a trance."
    y 1h "I'm not sure if this novel can do that..."
    y "But I believe if Sayori picked it out, it could have that effect."
    y "Even if this doesn't seem like the genre of literature I usually read."
    show yuri zorder 2 at t41
    show sayori 1d zorder 3 at f44
    s "Well, you might be surprised Yuri."
    s "This book could be what you've needed your entire life."
    s "It could help solve everything!"
    "Sayori is getting really passionate about this book."
    "But she sounds like she's probably hiding something about it."
    "And seeing as just a few minutes ago she said she didn't know what it was about..."
    show yuri 1h zorder 3 at f41
    show sayori zorder 2 at t44
    y "..."
    y 1t "I'm not sure I understand what you mean by that..."
    y "H-How could this book..."
    y "...solve everything?"
    if ch5_name == "Yuri":
        y "{i}(What would you know about what's wrong with me Sayori...?){/i}"
        y "{i}(There's nothing wrong with me...is there?){/i}"
    show yuri zorder 2 at t41
    show sayori 1r zorder 3 at f44
    s "Ehehe, you'll see!"
    show natsuki 1e zorder 3 at f42
    show sayori zorder 2 at t44
    n "Honestly, I found it to be boring."
    n "Nothing grabbed my attention."
    n "The setting is super uninteresting."
    n 5g "I can't find myself enjoying this book at all."
    show natsuki zorder 2 at t42
    show monika 3f zorder 3 at f43
    m "There's no need to be so blunt about it Natsuki..."
    m "Sayori obviously picked out this book for a reason..."
    m 3e "It might not suit your tastes but others might end up enjoying it."
    m "And like what Yuri and [player] said, it's only just beginning."
    m "Maybe we'll all find something we enjoy in it."
    show natsuki 42b zorder 3 at f42
    show monika zorder 2 at t43
    n "Hmph."
    n "Whatever..."
    n "I'll keep participating, but only because I know we're going to have to read manga soon enough."
    n 1d "And when that time comes, I'm gonna show you all why it's a great form of literature!"
    if ch5_name == "Natsuki":
        n "You'll help me with that, won't you [player]?"
        n "You don't need to answer that, I already know you read manga so of course you will!"
    show natsuki zorder 2 at t42
    show monika 1n zorder 3 at f43
    m "Ah..."
    m "I'm not sure you're getting the idea that Sayori's trying to do for the club here."
    if ch5_name == "Monika":
        m "{i}(But if it means you're going to be participating in this as well Natsuki...){/i}"
        m "{i}(That's all we can hope for...){/i}"
    show monika zorder 2 at t43
    show sayori 1d zorder 3 at f44
    s "It's okay!"
    s 1c "I get where they're coming from."
    s "If you shoved something like this in my face when I had no interest then I'd probably feel the same."
    s "But this is going to be really important later on, so please try to have some fun."
    s 1r "For me? Pleeeeeease?"
    if ch5_name == "Sayori":
        s "{i}(This is just the beginning...){/i}"
        s "{i}(I know at the end of this, we'll all be happy...){/i}"
    show natsuki 1b zorder 3 at f42
    show sayori zorder 2 at t44
    n "Fine, fine."
    n "I'll try to enjoy it..."
    show yuri 1b zorder 3 at f41
    show natsuki zorder 2 at t42
    y "I'll do the same."
    y "Since you put a lot of thought into this..."
    show yuri zorder 2 at t41
    show sayori 4s zorder 3 at f44
    s "Thank you two so much!"
    s "I want everyone to have fun with this."
    s 4d "So I hope it's not too much to ask of you guys to read to the end of chapter four...?"
    show sayori zorder 2 at t44
    mc "Is this going to replace the poem writing?"
    mc "If it doesn't, it seems like a lot of my spare time is going to be taken up by the club."
    show sayori 1j zorder 3 at f44
    s "Come on, [player]!"
    s "It's only a short read, I'm sure even you can manage!"
    show sayori zorder 2 at t44
    mc "H-Hey! What do you mean by {i}even me{/i}?"
    show monika 1e zorder 3 at f43
    show sayori zorder 2 at t44
    m "Ahaha, it won't be that hard."
    m "I'm sure we can all manage, Sayori."
    "Yuri and Natsuki reluctantly nod their confirmation."
    show monika zorder 2 at t43
    show sayori 1m zorder 3 at f44
    s "Ah, that reminds me!"
    s "Before we run out of time, we should share our poems!"
    show sayori zorder 2 at t44
    mc "Did you actually bring one to share?"
    mc "From the sounds of things this morning--"
    show sayori 1j zorder 3 at f44
    s "I have it right here [player]!"
    "She pulls out a piece of paper from her bag and quickly shows it to me before taking it back."
    s 1l "See? I told you I'd have one..."
    show sayori zorder 2 at t44
    "From the looks of it, it seemed kinda rushed."
    "She probably wrote it during the day before the club meeting."
    "Despite that, it looked pretty long."
    return

label ch6_end:
    stop music fadeout 1.0
    scene bg club_day
    show sayori 4a zorder 2 at t42
    with wipeleft_scene
    play music t3
    s "Okay, everyone!"
    s "I hope everyone had--"
    show natsuki 1c zorder 3 at f41
    n "Wait!"
    n "Is it just me, or did Sayori say something really weird just now?"
    show natsuki zorder 2 at t41
    show yuri 1f zorder 3 at f43
    y "Natsuki's right..."
    y "You don't usually say that when you address the club."
    y 1h "In fact, that's usually Monika's catchphrase..."
    show yuri zorder 2 at t43
    show monika 3m zorder 3 at f44
    m "Catchphrase?"
    m "I-I don't have a catchphrase, do I?"
    m "And besides...when have I ever addressed the club like Sayori has?"
    show yuri 2f zorder 3 at f43
    show monika zorder 2 at t44
    y "You..."
    "Yuri pauses for a moment."
    y 2n "...never did...?"
    y 2o "Sorry...I don't know..."
    y "...what am I talking about?"
    show natsuki 2e zorder 3 at f41
    show yuri zorder 2 at t43
    n "Something is going on here."
    n "I can't figure out what it is..."
    n "And it's really bothering me!"
    show natsuki zorder 2 at t41
    show sayori 1j zorder 3 at f42
    s "T-There's nothing going on!"
    s "You're all acting really weird..."
    s 1g "Maybe it's because we're doing something different..."
    s "And we're not used to it yet."
    show sayori zorder 2 at t42
    show yuri 1h zorder 3 at f43
    y "That could be it..."
    y "But I can't feel there's some..."
    y "...underlying factor at play here."
    show yuri zorder 2 at t43
    show monika 3e zorder 3 at f44
    m "Yuri, I think you're overthinking this a little."
    m "Sayori is right."
    m "Since we are usually doing our own things..."
    m "It's only natural that we find it weird doing something as a whole club."
    m 3a "So, let's just calm down and hear what Sayori has to say."
    show natsuki 5g zorder 3 at f41
    show monika zorder 2 at t44
    n "Hmph."
    show natsuki zorder 2 at t41
    show sayori 1d zorder 3 at f42
    s "Thanks Monika..."
    s "Now that that's out of the way..."
    s 1a "I'd just like to say that I hope everyone had fun."
    s "And that we're going to continue this book until it's finished."
    s "There's only ten chapters, so I'm sure we'll get it done quick."
    s 1d "Um...if no one else has anything to say..."
    s 4r "Then I guess the meeting is over!"
    s "Don't forget to write a poem tonight as well."
    s "See you all tomorrow!"
    show sayori zorder 2 at t42
    show monika 1h zorder 3 at f44
    m "Actually, I'd like to speak to Yuri."
    m "In private..."
    show yuri 1f zorder 3 at f43
    show monika zorder 2 at t44
    y "Um...I suppose that's okay"
    y "But what for?"
    show yuri zorder 2 at t43
    show monika 3b zorder 3 at f44
    m "We're just gonna talk."
    m "It won't take long."
    m 3d "Is it okay if we stay here a little longer Sayori?"
    m "I'll be sure to pack everything up."
    show sayori 4a zorder 3 at f42
    show monika zorder 2 at t44
    s "Sure!"
    s "It saves me the trouble of doing it myself."
    s "Let's go, [player]."
    show sayori zorder 2 at t42
    show monika 2f zorder 3 at f44
    m "Um..."
    m "Could [player_personal] stay for a bit as well?"
    m 2e "Just outside, until I finish speaking with Yuri."
    m "Is that alright?"
    show monika zorder 2 at t44
    mc "Sure, I don't mind."
    show sayori 1b zorder 3 at f42
    s "Well, bye I guess..."
    mc "See you tomorrow Sayori."
    show sayori zorder 2 at t42
    show monika zorder 3 at f44
    m "Great, I'll just be a minute."
    scene corridor
    with wipeleft_scene
    "I wait outside the clubroom for what seems like a good ten minutes."
    "I can hear them talking faintly but not loud enough that I can make out what they're saying."
    "While I'm here I decide I might as well start reading the next chapter of that book we're reading."
    "Just as I was about to open the book, Yuri steps outside."
    show yuri 2n zorder 2 at t11
    y "Ah, [player]...!"
    y "Um..."
    y 1q "I-I'll see you tomorrow..."
    mc "Yeah, see you then."
    show yuri at thide
    hide yuri
    "Yuri gives me a nod before quickly heading off."
    show monika 1q zorder 2 at t11
    m "I hope she's going to be okay."
    m "I would hate to see anything happen to her."
    mc "What do you mean?"
    mc "What did you even talk about in there?"
    m 2h "Among other things which are between Yuri and me..."
    m 2e "We were just discussing a particular book..."
    mc "The one with the eye on the cover?"
    m "That very same one."
    m 4e "I was talking to Yuri about where she got it."
    m "It turns out it was just at the local bookstore..."
    m 4c "But when I checked their website earlier it wasn't there."
    mc "That's weird."
    m "I asked her how many copies of the book were there."
    m "She said she bought the last two in the store."
    m 2f "Now, I'm not sure if that means the last two copies or the {i}only{/i} two copies."
    mc "Okay..."
    mc "But why are you telling me this?"
    m 2g "What you said earlier, something about this {i}Third Eye{/i}..."
    m "It seems familiar."
    mc "That was just a joke, I didn't really mean anything by it."
    m 2h "Hmm..."
    m 2f "Maybe, but I really don't like the feeling I'm getting from this book."
    m "Can you do me a favor?"
    m 2e "I know you've got a lot to do tonight..."
    m "...with the poem writing and the book the club is reading..."
    m "But could you find some time to read Portrait of Markov as well?"
    m 3e "You don't have to read much of it, maybe just the first two chapters."
    mc "Well..."
    mc "I guess if I have time then I'll try to read it."
    mc "I wouldn't count on it though."
    m 1m "That's all I can hope for."
    m "Thanks [player]~"
    m 1j "I guess I'll see you tomorrow."
    show monika at thide
    hide monika
    "Monika waves goodbye before heading home."
    "I'm left wondering why she wants me to read that book."
    "It's just a normal book, isn't it?"
    "Yuri got it for me as a present for joining the club..."
    "In any case, Monika asked me for a favor so I'll try my best to find time."
    scene bg bedroom with wipeleft_scene
    play music t2 fadeout 1.0
    "I get home rather quick and decide to start reading the next three chapters of the club book."
    "A fifth character is introduced, she appears to have special abilities."
    "She has the ability to manipulate people and control events, but she doesn't seem good at it."
    "She was wandering between towns, seeking help and shelter and she stumbled into the family."
    "So the lumberjack and his family takes her in and starts to take care of her, unaware of her abilities."
    "I can't be certain but I have a feeling that she's falling in love with the lumberjack."
    "He already has a wife so I can tell there's going to be some sort of drama here..."
    "I wonder where all of this is leading..."
    "Just as it starts getting interesting, chapter four ends."
    "I'm a little tempted to keep reading but decide it's probably better if we do it as a club."
    "Besides, I still have to write a poem and read some of that other book."
    "Before I can start writing my poem, I hear a knock on my door."
    "Who could that be?"
    "I head downstairs and open the door."
    scene bg house with wipeleft_scene
    show sayori 1ba zorder 2 at t11
    $ persistent.ch6_task = [False,False,False]
    $ renpy.save_persistent()
    s "Hi [player]~"
    mc "Sayori? What are you doing here?"
    s 2bd "I'd like to ask you for a favor."
    mc "You as well, huh?"
    mc "Monika asked me to do something for her too..."
    mc "Well, let's hear it."
    s "I want you to spend some time with Yuri tomorrow."
    mc "Like, in the club?"
    mc "Weren't we going to be reading the book?"
    mc "I don't think we'll have much time to spend together, even if I wanted to."
    s 2bl "No..."
    s "I meant..."
    s 2bd "Like during lunch."
    mc "E-Eh?"
    mc "Why do you want me to spend lunch with Yuri?"
    if ch4_name == "Yuri" and ch5_name == "Yuri":
        mc "I mean, I don't particularly mind spending time with her..."
        mc "In fact, she's probably one of the people in the club I feel closer to."
        mc "Still this is kinda odd..."
    elif ch4_name == "Yuri" or ch5_name == "Yuri":
        mc "I mean, I don't mind spending more time with her..."
        mc "But she's not exactly who I'd prefer to spend my lunch time with."
    else:
        mc "I haven't really spent enough time with her before..."
        mc "So it would be difficult to approach her."
    s 1bi "Aw, come on."
    s "It won't be that bad..."
    mc "You still didn't answer why you want me to hang out with her."
    s 1bk "Well..."
    s "You know how she is..."
    s "She's usually secluded and doesn't really talk to anyone outside the club."
    s 1bj "I think that if you spoke with her about it..."
    s "She'll open up a bit more to everyone else."
    mc "Sayori..."
    mc "I don't think changing how she acts is a good idea."
    mc "Her personality is what makes her Yuri."
    s 1bh "Well...can you at least talk to her?"
    s "Maybe you don't have to spend all of your lunch with her."
    s 1bg "I just know that you'll be the one that gets through to her."
    s "Especially if you do the favor Monika asked from you."
    mc "Monika's favor?"
    s 1bc "Yeah, reading that other book."
    mc "How do you even know about that?"
    mc "She didn't tell you, did she?"
    s 1bk "Um..."
    s "I'm the president, of course she told me!"
    mc "I thought that the conversation between us was private..."
    mc "Well, I guess it doesn't really matter."
    s 1bj "So, are you gonna do it?"
    mc "Does it have to be me?"
    mc "You know her better than anyone..."
    mc "Do you really think that me talking to her will change her?"
    s 1bk "You're right..."
    s "I do know her better than anyone..."
    s "Which is how I know it has to be you."
    s 1bf "So please [player], I'm gonna ask you one more time..."
    label yuri_talk:
    show sayori 1bj
    menu:
        s "Will you spend your lunch with her tomorrow?"
        "Yes.":
            if not bad_choice_first:
                if sayori_personality > 0:
                    $ sayori_personality -= 1
            mc "Fine, I'll do it."
            mc "I can't believe you got me to agree to this."
            s 4br "Yaaaaay!"
            s "Thank you so much [player]!"
            "Sayori wraps her arms around me, jumping up and down."
            mc "C-Calm down Sayori."
            mc "I'm only going to talk to her..."
            mc "I'm not going to force her to change anything."
            mc "Besides..."
            if sayori_confess:
                mc "You're one of the most important people in my life..."
            else:
                mc "You're my best friend..."
            mc "So how could I say no?"
            s 4bd "You don't know how much this means, [player]..."
            s "You don't know how much closer we all are to the end."
            mc "The end...?"
            mc "Of what?"
            s 3bl "Um..."
            s "The story!"
            "I'm guessing she's talking about the club novel."
            "But the way she said how closer we are to the end..."
            "Well, it leaves a bad feeling."
            s 1ba "I'll see you tomorrow then."
            s "I promise I'll be the one waiting."
            s 1bd "Oh, I almost forgot..."
            s "I have to tell you one more thing."
            mc "What is it?"
            s "Please {i}save{/i}...like right now.{nw}"
            show screen tear(20, 0.1, 0.1, 0, 40)
            window hide(None)
            play sound "sfx/s_kill_glitch1.ogg"
            $ pause(0.25)
            stop sound
            hide screen tear
            window show(None)
            s "Please {i}save{/i}...like right now.{fast}"
            window auto
            mc "Save?"
            mc "What do you mean?"
            s 1bl "Um...I mean save yourself some time..."
            s "And stop talking to me!"
            mc "...What?"
            s 1bd "Just hurry up and read that book, okay?"
            mc "Whatever you say Sayori..."
            show sayori at thide
            hide sayori
            "Sayori gives me a one final embrace before running off back to her house."
            "I don't know what the big deal is, it's just lunch with Yuri."
            "It's not like she's gonna change from talking to me for a couple of minutes."
            "Sayori seemed hopeful though and she probably knows what's best for Yuri."
            "I just hope I don't accidentally make things worse."
            scene bg bedroom with wipeleft_scene
            "I'm really running out of time here."
            "Between reading the club novel and talking to Sayori..."
            "A couple of hours seems to have passed."
            "At this rate, I'll probably only have time to do one thing."
            "Either I read the book like Monika and Sayori wanted..."
            "Or write a really good poem."
            "I'll probably do the other one tomorrow but won't do as great of a job..."
            menu:
                "So, what should I do...?"
                "Write a good poem.":
                    $ read_book = False
                    $ persistent.ch6_task[0] = True
                    if persistent.ch6_task[1]:
                        $ persistent.ch6_task[2] = True
                    $ renpy.save_persistent()
                    "Well, I'm sure they won't mind so much if I only read one chapter of the book."
                    "Writing this poem will probably mean more than reading that weird book anyway."
                    "I can't spend too much time doing everybody favors, otherwise I'll have no time to myself."
                    "I still feel bad about it though..."
                    if not persistent.ch6_task[2]:
                        "If only life was like a game..."
                        "I could save the game, read the book then load it to before I did..."
                        "And still have the knowledge from reading the book while writing a pretty good poem."
                        "But this is reality and things like that don't exist."
                        "Anyway..."
                        "What's the worse that could happen if I don't read the book?"
                        "I'm still going to spend lunch with Yuri tomorrow."
                        "I'll probably end up reading the first chapter of the book as well, so it's not like I'm not doing what they asked."
                    else:
                        "Despite that feeling I kinda know what's inside the book."
                        "Like it's a familiar memory but I know I never did it myself."
                        "It's probably nothing and when I read the first chapter of the book tomorrow it's going be completely different."
                "Read Portrait of Markov.":
                    $ read_book = True
                    $ persistent.ch6_task[1] = True
                    if persistent.ch6_task[0]:
                        $ persistent.ch6_task[2] = True
                    $ renpy.save_persistent()
                    "Monika and Sayori really seemed intent on me reading this book."
                    "That's probably for a good reason."
                    "They seem more aware of what's going on than I do."
                    "If that's the case, I guess I'll start reading the book."
                    "..."
                    "Well, that was certainly interesting."
                    "The first two chapters pretty much got straight into it."
                    "It introduced a high school girl who decided to move in with her long-lost younger sister."
                    "But her life immediately became strange with weird stuff happening left and right."
                    "There is some huge foreshadowing going on here and despite not being a fan of this genre..."
                    "I'm actually pretty interested in the story."
                    "I decide to keep reading."
                    "..."
                    "Before long I'm up to chapter seven."
                    "People escaped from some sort of human experiment camp and are after the girl in the story."
                    "It seems like whatever she does, it ends up ruining her life even more."
                    "I realize it's actually almost midnight and decide to get some sleep so I can write a poem in the morning."
                    if not persistent.ch6_task[2]:
                        "If only this was a game, I could make a save..."
                        "Read this and find out whatever I needed to..."
                        "Then go back and write a good poem."
                        "But this is reality and things like that don't exist."
                        "I can already tell everyone is going to be so disappointed after reading my last one."
                        "But at least I can do Monika's and Sayori's favor to the best of my ability."
                    else:
                        "But I have this strange feeling within me."
                        "Like I know exactly what I'm going to write."
                        "For some reason I feel like this poem won't be as bad as I thought it would be."
                        "Maybe they'll even think it's better than my last one."
                        "That's unlikely..."
                        "But it feels like I'm putting some thought into it this time."
        "No." if ch6_no_option:
            $ sayori_no_count += 1
            $ config.skipping = False
            $ config.allow_skipping = False
            if bad_choice_first:
                if sayori_no_count == 4:
                    $ ch6_no_option = False
                    s 1bf "Are you going to keep trying?"
                    s "You really like making this difficult for us, don't you?"
                    s "There's only one option left..."
                    s 1bk "I know this may feel like I'm forcing it on you..."
                    s "But it's the only way."
                    s 1bu "So forgive me, okay?"
                    $ style.say_dialogue = style.edited
                    $ currentpos = 40.480 - (get_pos() / 2.0)
                    $ audio.t2r = "<from " + str(currentpos) + " to 38.23 loop 0>mod_assets/bgm/2r.ogg"
                    play music t2r
                    show noise zorder 100 at noise_alpha
                    show vignette zorder 100 at vignetteflicker(-2.030)
                    show layer master at rewind
                    show sayori 1bk
                    s "{cps=*3}But it's the only way.{/cps}{nw}"
                    s "{cps=*3}I know this may feel like I'm forcing it on you...{/cps}{nw}"
                    s 1bf "{cps=*3}There's only one option left...{/cps}{nw}"
                    s "{cps=*3}You really like making this difficult for us, don't you?{/cps}{nw}"
                    s "{cps=*3}Are you going to keep trying?{/cps}{nw}"
                    $ del _history_list[-12:]
                else:
                    s 1bf "No again?"
                    s "It's not going to work."
                    s "Stop trying..."
                    s 1bk "I can't make [player] do this, only you can."
                    s "So please, just help me..."
                    s "..."
                    s 1bu "I feel so awful for doing this."
                    $ style.say_dialogue = style.edited
                    $ currentpos = 40.480 - (get_pos() / 2.0)
                    $ audio.t2r = "<from " + str(currentpos) + " to 38.23 loop 0>mod_assets/bgm/2r.ogg"
                    play music t2r
                    show noise zorder 100 at noise_alpha
                    show vignette zorder 100 at vignetteflicker(-2.030)
                    show layer master at rewind
                    show sayori 1bk
                    s "{cps=*3}...{/cps}{nw}"
                    s "{cps=*3}So please, just help me...{/cps}{nw}"
                    s "{cps=*3}I can't make [player] do this, only you can.{/cps}{nw}"
                    s 1bf "{cps=*3}Stop trying...{/cps}{nw}"
                    s "{cps=*3}It's not going to work.{/cps}{nw}"
                    s "{cps=*3}No again?{/cps}{nw}"
                    $ del _history_list[-15:]
                $ style.say_dialogue = style.normal
                $ currentpos = 80.959 - (get_pos() * 2.0)
                $ audio.t2r = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
                play music t2r
                hide noise
                hide vignette
                show layer master
                $ config.allow_skipping = True
                jump yuri_talk
            else:
                $ bad_choice_first = True
                if sayori_personality < 2:
                    $ sayori_personality += 1
                mc "Sayori..."
                mc "I know you're my best friend and everything..."
                mc "But something tells me talking to her tomorrow is a bad idea."
                s "So that's the way it's going to be...?"
                if sayori_confess:
                    s 1bh "I thought you'd do anything for me..."
                else:
                    s 1bh "[player]..."
                mc "Sayori, I'm sorry."
                mc "Yuri is a friend but if you're trying to get me to change her..."
                mc "I can't really do that without feeling like a horrible person."
                s 1bi "I don't get it..."
                s "I thought you wanted to help..."
                s "You got us this far..."
                s "So why would you--"
                s 1bj "No."
                s "I'm not taking no for an answer here."
                mc "Sayori...?"
                s "You'd better change [player_possessive] mind..."
                s 1bk "I'm not going to like this..."
                s "But it's all for my friends..."
                s 1bf "So..."
                $ currentpos = 40.480 - (get_pos() / 2.0)
                $ audio.t2r = "<from " + str(currentpos) + " to 38.23 loop 0>mod_assets/bgm/2r.ogg"
                play music t2r
                show noise zorder 100 at noise_alpha
                show vignette zorder 100 at vignetteflicker(-2.030)
                show layer master at rewind
                show sayori 1bk
                $ style.say_dialogue = style.edited
                s "{cps=*3}But it's all for my friends...{/cps}{nw}"
                s 1bj "{cps=*3}I'm not going to like this...{/cps}{nw}"
                s "{cps=*3}You'd better change [player_possessive] mind...{/cps}{nw}"
                mc "{cps=*3}Sayori...?{/cps}{nw}"
                s "{cps=*3}I'm not taking no for an answer here.{/cps}{nw}"
                s "{cps=*3}No.{/cps}{nw}"
                s 1bi "{cps=*3}So why would you--{/cps}{nw}"
                s "{cps=*3}You got us this far...{/cps}{nw}"
                s "{cps=*3}I thought you wanted to help...{/cps}{nw}"
                s "{cps=*3}I don't get it...{/cps}{nw}"
                show sayori 1bh
                mc "{cps=*3}I can't really do that without feeling like a horrible person.{/cps}{nw}"
                mc "{cps=*3}Yuri is a friend but if you're trying to get me to change her...{/cps}{nw}"
                mc "{cps=*3}Sayori, I'm sorry.{/cps}{nw}"
                if sayori_confess:
                    s "{cps=*3}I thought you'd do anything for me...{/cps}{nw}"
                else:
                    s "{cps=*3}[player]...{/cps}{nw}"
                show sayori 1bj
                mc "{cps=*3}But something tells me talking to her tomorrow is a bad idea.{/cps}{nw}"
                mc "{cps=*3}I know you're my best friend and everything...{/cps}{nw}"
                mc "{cps=*3}Sayori...{/cps}{nw}"
                $ del _history_list[-37:]
                $ style.say_dialogue = style.normal
                $ currentpos = 80.959 - (get_pos() * 2.0)
                $ audio.t2r = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
                play music t2r
                hide noise
                hide vignette
                show layer master
                $ config.allow_skipping = True
                jump yuri_talk
    # Have to jump back because of all the jumps used here
    jump ch6_after
