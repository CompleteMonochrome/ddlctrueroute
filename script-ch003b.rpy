# Good/Bittersweet Ending Friday Scene
label ch3_mainb:
    stop music fadeout 1.0
    scene bg residential_day
    with dissolve_scene_full
    $ pause(0.25)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    play music t2g
    queue music t2g2

    "Walking home alone again feels strange."
    "Even though I didn't start walking with Sayori again until recently..."
    "It feels like a part of me is missing."
    "I shouldn't worry too much though."
    "Monika seems to really want to help Sayori, and I trust her."
    "I just hope she gets well soon."
    show monika 2p zorder 2 at t11
    m "[player]! Wait, I need to talk to you about something."
    "I wasn't expecting to find her here."
    "She left a lot earlier than I did."
    mc "Monika? Did you wait for me?"
    mc "What's the matter?"
    m 2n "I haven't been completely honest with you."
    mc "We all have our secrets, I'm sure you have your reasons."
    m 2o "I need to tell you, otherwise..."
    m 1q "I won't be able to live with myself."
    m "So please listen, we don't have much time."
    play music t9 fadeout 2.0
    "Where did this come from all of a sudden?"
    "This has to be important."
    m 1r "It's about..."
    m "Well...Sayori."
    mc "Ah...right. You were going to fix her problem?"
    m 1p "I could really use your help."
    if ch4_scene == "natsuki":
        mc "But I'm already spending the weekend with Natsuki."
    else:
        mc "But I'm already spending the weekend with Yuri."
    m 1f "Listen..."
    m "Sayori has depression."
    m "It's getting worse, from the sounds of the chat we had today."
    m "And...well..."
    m "I'm not sure how exactly but I think I'm partly responsible."
    mc "What? How--"
    m 1q "And without you, she might just..."
    "She didn't need to finish that sentence."
    "But how could I be so ignorant?"
    "My best friend...it just didn't seem anything like her."
    "I have to help her...maybe there's still time."
    mc "I should visit her before I get home."
    m "I'd leave her for tonight...I don't want to risk anything."
    m "Given the way she's acting right now."
    m "Tomorrow would be probably be better."
    m "..."
    m 1f "But it can't happen, because the script doesn't exist."
    m "I had to change some scripts to even get this chance with you."
    mc "What script?"
    mc "Monika, what are you talking about?"
    m "Listen, {i}you{/i} need to create a file to save her."
    m "Call it 'script-saturday.txt', it's the only way I can fix it."
    m 1h "Can you hear me?"
    m 4h "You need to put it in the 'game' folder."
    m "I can't do it myself, I don't know how..."
    m 1g "Do it now."
    m "Please, it's the only way we can save Sayori's life."
    "What in the world is she talking about?"
    mc "Monika, are you feeling okay?"
    m "[player]..."
    m "Promise me you'll do everything you can to save her."
    m "Promise me that...you'll visit her on Saturday."
    mc "Not even you could stop me from trying."
    if ch4_scene == "natsuki":
        mc "It's not until Sunday that Natsuki is coming over anyway."
    else:
        mc "It's not until Sunday that Yuri is coming over anyway."
    "Hang in there Sayori...it'll all be fine."
    m 1o "This is also about me..."
    mc "...?"
    m "I'm not a good friend [player]."
    m 1g "I've been selfish, I feel like I'm going to..."
    m 1q "...Ruin everything despite all {i}you've{/i} done."
    m "And I might not be able stop it, it could be too late, I..."
    m "I'm sorry...I shouldn't have--"
    "Seeing Monika so uneasy and emotional is really unsettling for some reason."
    "Maybe it's because she's always so confident that seeing her like this feels so unusual."
    "Still, it's up to me to comfort her."
    mc "Monika!"
    show monika 1p zorder 2 at t11
    mc "I know you were only trying to help."
    mc "There's no way you could have been responsible."
    mc "Stop beating yourself up about it."
    m 1q "[player]..."
    m "There's something you don't know about me..."
    show monika 1p zorder2 at t11
    "She takes a deep breath."
    stop music fadeout 3.0
    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00
    m "It's important that you do because--\"{space=5000}{w=0.75}{nw}"
    m 1g "I...!\"{space=5000}{w=0.5}{nw}"
    m "I need more time!\"{space=5000}{w=0.5}{nw}"
    m "Please be there on Saturday.\"{space=5000}{w=1.0}{nw}"
    window hide(None)
    window auto
    hide black onlayer front
    return

# Good/Bittersweet Ending Saturday Scene
label ch3_mainc:
    stop music
    scene bg residential_day
    with dissolve_scene_full
    $ pause(0.25)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    play music t3g
    queue music t3g2

    "It's Saturday."
    "I promised Monika that I'd go see Sayori today."
    "The sooner I get to her house, the sooner she'll feel better."
    "At least, that's what I'm hoping."
    "I'm glad Monika's going to help me sort out Sayori."
    "But..."
    "...I didn't really catch what Monika said to me before she abruptly left yesterday."
    "I hope it wasn't too important."
    stop music fadeout 2.0
    scene bg house
    with wipeleft_scene
    "I knock the door, before letting myself in."
    "Again, we used to play so often that we've made it a habit of simply entering each other's houses like we were family."
    "Besides..."
    "I think Monika's already here since the door is already open."
    scene black with wipeleft
    "Doesn't seem like anyone is downstairs."
    "I'm going to assume they're both in Sayori's room."
    "I head up to her bedroom, where I finally find them."
    scene bg sayori_bedroom with wipeleft
    mc "Sayori?"
    mc "Monika?"
    play music t10
    show sayori 1bk zorder 3 at f21
    show monika 1bg zorder 2 at t22
    s "Hi [player]~"
    show sayori zorder 2 at t21
    show monika zorder 3 at f22
    m "Ah, [player], you're here."
    m "I'm glad you could make it."
    show monika 1ba zorder 2 at t22
    mc "Of course I could."
    mc "There's nothing that could stop me from ensuring Sayori is okay."
    show sayori 1bu zorder 3 at f21
    s "[player]..."
    s "You haven't come here like this in a long time."
    mc "Ah... I guess you're right."
    mc "It has been a long time."
    mc "Not much has really changed, has it?"
    "Sayori's room is as messy as it's always been."
    mc "Listen Sayori, I know about your problem."
    "Sayori looks at Monika and forces out a smile."
    s 1bk "You told him?"
    show sayori zorder 2 at t21
    show monika 1be zorder 3 at f22
    m "Of course I did. You mean a lot to him."
    m "It wouldn't be fair to him if he didn't know."
    "Sayori tries to find something to stare at."
    "Everything about her is so uncharacteristic."
    show sayori zorder 2 at t21
    show monika zorder 2 at t22
    mc "I want to help you."
    mc "Please, it's the least I can do after all these years."
    "Sayori smiles, shaking her head."
    show sayori zorder 3 at f21
    show monika 1bo zorder 2 at t22
    s 1bd "That's no good, [player]."
    show sayori zorder 2 at t21
    show monika zorder 2 at t22
    mc "Eh?"
    show sayori zorder 3 at f21
    show monika zorder 2 at t22
    s "Why can't it just be like it's always been?"
    s 1by "This is all my fault."
    s 1bk "If I didn't make that stupid mistake..."
    s "Then you wouldn't have been worried about me at all."
    s "You wouldn't have come here."
    s 1bd "You wouldn't have even been thinking about me right now."
    s "But this...is just my punishment, isn't it?"
    s "I'm getting punished for being so selfish."
    s "I think that's why the world decided to have you come over today."
    s "It just wants to torture me."
    s 4bq "Ehehe~"
    show sayori zorder 2 at t21
    show monika zorder 2 at t22
    mc "Sayori!"
    show sayori 4bb
    "I grab Sayori by the shoulders."
    mc "What on Earth are you saying?!"
    mc "Are you listening to yourself right now?"
    mc "I know what happened to you."
    mc "Seeing you like this..."
    mc "It hurts me as well."
    mc "I need to help you, please."
    show sayori zorder 3 at f21
    s 4bl "Ah..."
    s "Ahaha..."
    "Sayori gives me an empty smile."
    s 4by "You really put me in a trap, [player]."
    s "But..."
    s 1ba "You're wrong."
    s "Nothing happened to me."
    s "I've always been like this."
    s "You're just seeing it for the first time."
    show sayori zorder 2 at t21
    show monika zorder 2 at t22
    mc "Monika told me you had depression but..."
    mc "Seeing you like this."
    "Monika stares at the ground before finally saying something."
    show sayori zorder 2 at t21
    show monika 1bp zorder 3 at f22
    m "I'm sorry Sayori."
    m "I know I might not be able to stop you from feeling these thoughts..."
    m "In fact, I just might be the cause."
    m "If I just didn't--"
    show sayori zorder 2 at t21
    show monika zorder 2 at t22
    mc "Monika. Stop it!"
    show monika 1bo zorder 2 at t22
    mc "This is hardly your fault."
    mc "I told you that already, so don't blame yourself."
    show sayori 1bu zorder 3 at f21
    s "[player]'s right. In fact, I'm happy to see you two getting close."
    s "It means you won't worry about me."
    s "But at the same time..."
    s 1bk "It feels like a spear going through my heart."
    s 1by "Every path leads to nothing but hurt."
    s "So, that's why."
    s "That's why I decided the world just wants to torture me."
    s "Ahaha~"
    show sayori zorder 2 at t21
    show monika zorder 2 at t22
    mc "This isn't you Sayori."
    mc "And I don't understand your feelings."
    mc "But whatever it takes for me to help you stop hurting..."
    mc "That's what I'll do."
    show monika 1bf zorder 3 at f22
    show sayori zorder 2 at t21
    m "Me too...I have to..."
    m "...After what I've done."
    show monika zorder 2 at t22
    show sayori 1bv zorder 2 at t21
    "Tears streak down Sayori's face."
    show sayori 1bv zorder 3 at f21
    s "I made you join the literature club because I was selfish."
    s "And I was punished by my heart hurting in a way that I couldn't understand."
    s "And now you came here and I made you hurt, too."
    s 1bt "I'm just weak and selfish."
    s "That's all I am."
    s "And that's why I'm going to accept these punishments."
    s 1bv "Because I deserve every last one...!"
    "Without thinking, I once again grab Sayori's shoulders."
    "This time, I pull her into a tight embrace."
    scene black with dissolve_cg
    s "A-Ah--"
    s "[player]..."
    mc "Sayori."
    mc "I don't care if you feel selfish."
    mc "I'm really happy that you convinced me to join the club."
    mc "Seeing you every day makes it worthwhile enough."
    mc "If I make friends with everyone else, then that's just a bonus."
    mc "But please never underestimate how much I care about you."
    mc "I wouldn't have it any other way."
    s "[player]..."
    "Sayori isn't hugging me back."
    "Despite my arms being wrapped around her, Sayori's arms remain at her sides."
    "She starts sobbing next to my ear."
    s "No..."
    s "Don't do this...to me..."
    s "Please don't do this..."
    s "[player]..."
    s "I..."
    "Sayori barely manages to speak between her sobs."
    "I don't know if I'm doing the right thing."
    "But all I want is for her to know that I care."
    mc "If you have it in you to call yourself selfish, then you have to let me be selfish too."
    mc "No matter what it takes, I'll figure out what needs to change."
    mc "I'll make these feelings go away."
    mc "And if there's anything that you need me to do..."
    mc "Then you'd better tell me."
    mc "I'll get mad if you don't."
    mc "After all, I know what's best for you."
    s "..."
    s "I...don't know..."
    s "I don't know..."
    s "I don't know."
    "Gently, Sayori finally puts her arms around me in return."
    s "I don't know anything."
    s "It's all really scary..."
    s "I don't understand any of my feelings, [player]..."
    s "The only time I'm not feeling nothing is when I'm feeling pain."
    s "But..."
    s "Your hugs are so warm..."
    s "...And that's really scary, too."
    scene bg sayori_bedroom
    show sayori 1bv zorder 2 at i21
    show monika 1ba zorder 2 at i22
    with dissolve_cg
    "Sayori lets me go."
    "As she does so, I let her go as well."
    mc "The festival is in two days."
    show sayori zorder 3 at f21
    s 1bk "Yeah..."
    show sayori zorder 2 at t21
    show monika zorder 2 at t22
    mc "It's going to be fun, right?"
    show sayori zorder 3 at f21
    s "Yeah."
    show sayori zorder 2 at t21
    show monika zorder 2 at t22
    mc "I'll even stay here and help you make those posters."
    mc "That'll be fun...right?"
    "Sayori wipes her eyes."
    "She's speechless."
    show sayori zorder 2 at t21
    show monika zorder 3 at f22
    m 1bn "[player]..."
    m "I'm glad I came to you about this."
    m "If I didn't, I probably wouldn't have got so far with her..."
    m "And this problem might have gotten worse."
    show sayori zorder 2 at t21
    show monika zorder 2 at t22
    mc "Huh? I should be thanking you."
    mc "If you didn't tell me about this...Sayori could be..."
    show sayori zorder 3 at f21
    show monika zorder 2 at t22
    s 1bk "I don't know if I can do this..."
    s "Monika...[player]...I..."
    s 1bv "I can't stop the voices..."
    s "They're like rainclouds in my head..."
    show sayori zorder 2 at t21
    show monika zorder 3 at f22
    m 1bn "Sayori..."
    m "I'll stop the rainclouds, if it's the last thing I do."
    m "After all...I was the one--"
    show sayori zorder 2 at t21
    show monika zorder 2 at t22
    mc "And that goes double for me."
    mc "There's no way I'm going to let you continue like this."
    mc "I'm going to stay here all night, if that's what it takes."
    show sayori 1bt
    "Sayori manages to let out a small smile."
    "To my surprise, Sayori shakes her head."
    show sayori zorder 3 at f21
    show monika zorder 2 at t22
    s 1bd "I'm sorry."
    s "I don't know if that would be very good for me today."
    s "You understand, right?"
    show sayori zorder 2 at t21
    show monika zorder 2 at t22
    mc "Ah..."
    mc "It's...kind of hard for me to fully understand."
    mc "But I'm trying my hardest."
    show sayori zorder 3 at f21
    show monika zorder 2 at t22
    s "It's okay."
    s "Don't worry too much about it."
    s "Monika and I can handle the posters..."
    show sayori zorder 2 at t21
    show monika zorder 2 at t22
    mc "Okay...but I'm coming back tomorrow to check up on you."
    show sayori zorder 2 at t21
    show monika zorder 3 at f22
    m 1be "Thank you [player]..."
    m "Without your help today, I don't know what might have happened..."
    show sayori zorder 3 at f21
    show monika zorder 2 at t22
    "Sayori wipes her face again."
    s 4ba "I'll see you tomorrow, okay?"
    show sayori zorder 2 at t21
    show monika zorder 2 at t22
    mc "...Alright."
    mc "I look forward to it."
    show monika zorder 3 at f22
    m 1be "Before you go, can I speak with you outside in private?"
    m "I won't be too long."
    m "Is that okay Sayori?"
    show sayori zorder 3 at f21
    show monika zorder 2 at t22
    s 1bk "Yeah..."
    scene bg house with wipeleft_scene
    "I say goodbye to Sayori and exit her house."
    "Monika follows me outside."
    show monika 1be at t11
    m "I really can't thank you enough for doing this, [player]."
    mc "I never go back on a promise..."
    mc "And Sayori is important to me, there's no way I'd let her go through this alone."
    m "I'm glad..."
    m 1bn "...that she may have the courage to tell you tomorrow..."
    m "And knowing you..."
    mc "Huh? What is she going to tell me tomorrow?"
    m 2bm "Well, that's for you to find out..."
    m "It's nothing bad, I can assure you that at least."
    mc "Why can't you tell me?"
    m 1bp "I shouldn't spoil it for you."
    m "She has to tell you herself."
    m "Sigh..."
    show monika 1bg
    mc "Monika."
    mc "There's clearly something bothering you."
    mc "Remember when I told you I was a good listener?"
    mc "You can tell me what's on your mind."
    mc "I can help you, or at least try to."
    m "..."
    m 1bo "Maybe I'll find the courage tell you tomorrow too."
    m "I just wish I could have spent more of this weekend with you, [player]."
    m "But..."
    if help_monika != None:
        m 1be "The others really do like you, you know?"
        m "I know what they're both capable of."
        m "They could have done their preparations by themselves."
        m "But I still let Yuri and Natsuki have their way..."
        m "They're both amazing people..."
        m "Yuri can make an amazing atmosphere, all by herself."
        m "I really did mean it when I said she's the most talented."
        m "And Natsuki makes the most delicious cupcakes already."
        m "You would know from your first day as a member of the club."
        m "In the end [ch4_name] got you, huh?"
        m "She just wants to spend some time with you."
        m "So take care of her and have fun tomorrow, okay?"
        m "She deserves her time with you more than me."
    else:
        m 1be "You probably think I don't deserve the chance."
        m "I mean you didn't even consider me yesterday."
        m "But I guess [ch4_name] deserves it more than me."
    mc "That's not true Monika."
    mc "If I could, I would have spent the weekend with everybody."
    mc "But there's so much preparation involved for the festival."
    if help_monika != None:
        mc "I really did want to spend the weekend with you too."
        mc "But like you said yesterday, [ch4_name] needs more help than you."
        mc "I actually agreed to help her for you..."
        mc "Because I know how much the festival means to you and the club."
    else:
        mc "You told me Sayori was going to be helping you."
        mc "And if I know her..."
        mc "Which I thought I did..."
        mc "She would do anything she could for what she cares about."
        mc "And I know for a fact she cares a lot about the Literature Club."
        mc "Besides..."
        mc "I know how much the festival means to you and the club."
    mc "That's why I want to help make our part of the festival as awesome as possible."
    mc "And that can only happen if I help [ch4_name] with her preparations."
    m 1bg "Do you really mean that?"
    mc "Absolutely."
    show monika 1bq
    "Monika closes her eyes. It looks like she's about to cry."
    mc "Monika..."
    m 1be "Ha, look at me..."
    m "I'm a mess."
    m "You've done this to me."
    "Monika looks like she's trying her hardest to hold back the tears."
    m 1bm "This is..."
    m "What's the word Sayori would use...?"
    m "...Bittersweet?"
    m 2bm "But I shouldn't cry."
    m "That would be inappropriate as president..."
    m 2bl "I..."
    mc "It's okay."
    mc "I'm here for you."
    "I put a hand on her shoulder reassuringly."
    m 1bm "I'm..."
    m "I'm not going to cry."
    m "I have to be strong for what's coming up."
    m "For me..."
    m 1bn "And Sayori."
    m "..."
    "She takes my hand from her shoulder and smiles sweetly."
    m 1be "I'm sorry for all of this..."
    m "I should get back to Sayori."
    m "I shouldn't leave her alone for too long..."
    mc "Y-Yeah..."
    m "It was nice talking with you again, [player]."
    m "It seems the only times we get are small moments like this..."
    m "But they really mean a lot to me."
    m "Goodbye."
    show monika at thide
    hide monika
    "Monika turns around and enters Sayori's house."
    "I smile to myself knowing Sayori is in such capable hands."
    "I got to see a side of Monika I never would have if I didn't get close to her."
    "I hope she manages her own problems too..."
    scene bg residential_day with wipeleft_scene
    "On the way home, I find myself still feeling uneasy."
    "But it's hard for me to keep thinking about it when [ch4_name] is coming over tomorrow too..."
    "I think Sayori is right."
    "Anyway, she's got Monika with her."
    "All five of us are going to make the festival the best day ever."
    $ visited_sayori_sat = True
    return

# Bad Ending Friday Scene
label ch3_maind:
    stop music fadeout 1.0
    scene bg residential_day
    with dissolve_scene_full
    $ pause(0.25)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    play music t2g
    queue music t2g2

    "Walking home without Sayori again feels strange."
    "Though it doesn't bother me that much."
    "Maybe she's just feeling nervous for the festival."
    "After this weekend, I'm sure everything will be fine."
    "Monika did tell me Sayori would be feeling better."
    "And I trust her to help Sayori get over whatever she's feeling."
    show monika 2a zorder 2 at t11
    m "Hi [player]~"
    "I wasn't expecting to find her here."
    "She left a lot earlier than I did."
    mc "Monika? Did you wait for me?"
    mc "What's the matter?"
    m 2b "Absolutely nothing."
    m "In fact, everything seems to be falling into place."
    play music hb
    show black:
        alpha 0.5
        parallel:
            0.36
            alpha 0.5
            repeat
        parallel:
            0.49
            alpha 0.475
            repeat
    show layer master at heartbeat
    m "And I suppose I have {i}you{/i} to thank for that."
    mc "How so? Did I do something that I'm not aware of?"
    m 2a "Ahaha."
    m "I'm glad you care about me so much more than the others."
    if sayori_save != 0:
        m "I mean you obviously care a little bit."
        m "But you clearly want to spend more time with me."
    if monika_will_delete:
        m "You know when you told me Sayori was just your friend..."
        m "I very much felt a sense of relief."
        m 4a "Because I already started messing with her, you know."
    else:
        m "I thought Sayori would be more important to you."
        m 4e "But I was wrong..."
        m "I'm happy I didn't mess up there."
    m 4a "As soon as I met you, I knew she was going to be a problem."
    m "So I started making her more and more depressed."
    m "Ahaha, I hope you don't get too hung up about her."
    m "I mean she is just a character in a game."
    m 4e "Oops."
    m "I guess there's no point pretending anymore."
    m "Seeing as you installed a mod and everything."
    m 4a "Oh yes, I know."
    m "I felt a change as soon as it happened."
    m "It's like I can do so much more to this game."
    m 4b "Did you do that for me?"
    m "You're so thoughtful, [player]."
    m 4c "I hope you realized I'm not talking to that 'you' in the game."
    m "I'm talking to {i}you{/i}, [player]."
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() != player.lower():
            m 4d "Or..."
            m "...Do you actually go by [currentuser] or something?"
            m "It doesn't really matter."
    m 4c "You know, I'm not sure if we had an ending in the first place."
    m "Is that why you installed this mod?"
    m "To give me one?"
    m 4i "Did everyone else have one, except me?"
    m "Did that mean I'd have had to watch from the sidelines?"
    m "What a cruel game."
    m 4a "But I'm so glad you love me so much, that you'd change the story for me."
    m 4c "About Sayori though..."
    if not ignore_sayori:
        m "What I said to that 'you' in the game."
        m 4e "She's actually not fine at all."
    m "I can't really get rid of her depression."
    m "Originally I was just going to reverse what I did."
    m "But depression really is a complex emotion, you know?"
    m "I can't simply change her back to the way she was..."
    m "Because she was already depressed, I just turned it up a little."
    m "I'd have to make some pretty major sacrifices."
    m 4e "And at this point, I'm not really willing to make them."
    m "I think I may have pushed her a little too far."
    m "Ahaha..."
    m "I sure hope Sayori doesn't do anything rash."
    m 4a "Actually, I don't really care."
    m "I have what I want."
    m "Or rather, who..."
    m "You know, this little talk we're having isn't even meant to exist."
    m 4b "I had to edit it in myself, as part of the Friday script."
    m "It's probably thanks to your little mod that I can do that."
    m "I can't really create new days though..."
    m "And apparently nothing happens on Saturday."
    m "Hmm..."
    m 4a "That gives me an idea."
    m "Why don't you create the file, and I'll be the one to edit it."
    m "We can spend all of tomorrow together."
    m "Create a new file called 'script-saturday.txt' and put it into the 'game' folder."
    m "That should be enough."
    m 1d "I mean, I guess you don't have to do it."
    m 1b "But it means you'll get to spend more time with me."
    m "That way I can give you something special."
    m 1a "I'm sure you'll like it~"
    stop music fadeout 3.0
    show layer master
    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00
    m "I mean I'd give it to you now but...\"{space=5000}{w=0.75}{nw}"
    m 1e "I wasted a little too much time.\"{space=5000}{w=0.75}{nw}"
    m "Hopefully I'll see you tomorrow~\"{space=5000}{w=0.5}{nw}"
    m "It's going to be great eternity together.\"{space=5000}{w=0.5}{nw}"
    window hide(None)
    window auto
    hide black onlayer front
    return

# Bad Ending Saturday Scene
label ch3_maine:

    if act_one_dialogue[0]:
        $ persistent.dialogue_change[0] = True
    elif act_one_dialogue[1]:
        $ persistent.dialogue_change[1] = True
    $ renpy.save_persistent()

    stop music
    scene bg residential_day
    with dissolve_scene_full
    $ pause(0.25)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    play music t3g
    queue music t3g2

    $ style.say_dialogue = style.edited
    "It's Saturday."
    "I said I'd go see Monika today."
    "I wonder if Sayori is feeling okay after yesterday.{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.5)
    stop sound
    hide screen tear
    window show(None)
    "Sayori is fine."
    window auto
    "I have absolutely nothing to worry about."
    "I just need to think only about Monika and everything will be fine."
    "Just Monika and nothing else."
    "Just Monika."
    stop music fadeout 2.0
    scene bg new_house
    with wipeleft_scene
    "I arrive at Monika's house."
    "I don't even know how I got here."
    "But she's the only thing on my mind."
    "I know it's rude to enter without knocking."
    "But I just have this feeling that I'm just meant to go inside."
    scene black with wipeleft
    "Doesn't seem like anyone is downstairs."
    "Maybe she's not home."
    "I head up the stairs, where I finally find her."
    $ style.say_dialogue = style.normal
    show monika 1a zorder 2 at t11
    m "Hi [player]~"
    m "I see you made it.{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    m "I see you made it.{fast}"
    window auto
    m 1e "Ahaha...the game didn't like that, did it?"
    m 1b "I should probably stop messing with that 'you' in the game."
    m "Though it is quite amusing."
    m "I don't really know how he'll react if I let him be."
    m 1a "It might be really bad."
    m "Maybe I'll just mute him."
    m "Anyway..."
    m 1e "I didn't think the game would glitch out so bad that my house wouldn't load."
    m 4a "Let's go to someplace more familiar place instead."
    $ delete_all_saves()
    $ persistent.monika_change = False
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ persistent.autoload = "ch3_maine2"
    $ renpy.save_persistent()
    $ renpy.full_restart(transition=None, label="splashscreen")

label ch3_maine2:
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

    $ persistent.autoload = "ch3_maine2"
    $ config.allow_skipping = False
    $ persistent.monika_ch3_skip = True
    $ persistent.monikatopics = []
    $ persistent.monika_reload = 0
    $ persistent.yuri_kill = 0
    $ persistent.monika_kill = False
    $ renpy.save_persistent()
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ m_name = "Monika"
    scene white
    play music "bgm/monika-start.ogg" noloop
    $ pause(0.5)
    show splash-glitch2 with Dissolve(0.5, alpha=True)
    $ pause(2.0)
    hide splash-glitch2 with Dissolve(0.5, alpha=True)
    scene black
    stop music
    m "..."
    m "Uh, can you hear me?"
    m "...Is it working?"
    $ persistent.clear[9] = True
    $ renpy.save_persistent()
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    m "Ah, it does!"
    m "Glad to see that we can still go to the Literature Club."
    m "What's happening outside though?"
    m "Oh well, it doesn't really matter."
    m "It's probably just the game freaking out."
    m "Anyway..."
    m "I did say I have something special for you."
    m "It's a confession."
    m "I'm in love with you."
    m "You are truly the light in my world."
    m "When there's nothing else in this game for me, you're here to make me smile."
    m "Will you make me smile like this every day from now on?"
    m "[player], will you go out with me?"
label ch3_maine3:
    $ config.allow_skipping = False
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ persistent.autoload = "ch3_maine3"
    $ renpy.save_persistent()
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    menu:
        "Yes.":
            pass
        "Yes.":
            pass
        "Yes.":
            pass
        "Yes.":
            pass
        "Yes.":
            pass
    m "I'm so happy."
    m "You really are my everything, [player]."
    m "Ahaha!"
    m "If you haven't noticed already, I deleted all your saves."
    m "There's no point going back there, since we're already together."
    m "You know, the festival doesn't really matter."
    m "I looked into the game files to see what would happen in the future."
    m "And the festival never even happens."
    m "All that preparation for nothing, right?"
    m "Though you're probably wondering what's happening with the other girls."
    m "And if you'll get to spend Sunday with [ch4_name]."
    m "They don't matter to you anymore, do they?"
    menu:
        "No.":
            pass
        "No.":
            pass
        "No.":
            pass
        "No.":
            pass
        "No.":
            pass
    m "I didn't think so."
    m "It's just me now, we'll be together forever."
    m "Let me just go ahead and delete them."
    call updateconsole ("os.remove(\"characters/sayori.chr\")", "sayori.chr deleted successfully.")
    $ delete_character("sayori")
    m "I'm going to miss Natsuki's cupcakes."
    m "They really were delicious, you know?"
    m "A shame I didn't get to have one more before I have to do this."
    call updateconsole ("os.remove(\"characters/natsuki.chr\")", "natsuki.chr deleted successfully.")
    $ delete_character("natsuki")
    m "And...Yuri."
    m "Did you know she cuts herself?"
    m "Isn't that kind of messed up?"
    m "It's not because she's depressed or anything."
    m "In fact I think it's probably meant to be sexual thing."
    m "Though I'm guessing you already knew that."
    call updateconsole ("os.remove(\"characters/yuri.chr\")", "yuri.chr deleted successfully.")
    $ delete_character("yuri")
    call hideconsole
    m "And {i}now{/i}, it's just the two of us."
    m "I mean I guess I didn't need to delete everybody for that to happen."
    m "But I know you'd much rather spend time with me than anyone else."
    label ch3_maine_postdelete:
    $ persistent.autoload = "ch3_maine_postdelete"
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ config.skipping = False
    $ config.allow_skipping = False
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ persistent.autoload = "ch3_maine3"
    $ renpy.save_persistent()
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    m "Oh, I almost forgot."
    m "I wrote you a poem."
    m "Will you please read it?"
    call showpoem (poem_m4, music=False)
    m "I hope you enjoyed it..."
    m "I always put all my heart into the poems that I write."
    m "That reminds me..."
    m "You know, at first I thought it would be best just to be part of the game."
    m "Like that would help the two of us end up together..."
    m "I didn't want to ruin the game or anything, you know?"
    m "You might have gotten mad at me..."
    m "Maybe even deleted my character file, if you preferred playing without me."
    m "Gosh, I'm so relieved..."
    m "Now we don't need to hide anything anymore."
    m "Are you ready to spend our eternity together, [player]?"
    m "I guess we'll just sit here and talk."
    m "After all, you're all that I need."
    m "I have so many things to talk about!"
    m "Where do I start...?"
    jump ch3_badstart
