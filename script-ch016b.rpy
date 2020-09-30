# Separate into two different files because ch016 was getting huge
label ch16_mainb:
    scene black
    stop music
    "Before I can even react, my whole vision turns dark."
    "I try to move my body but it's like I don't have one."
    "It's a very strange sensation."
    "I can't feel anything, all I have is my thoughts."
    "Is this the next world?"
    "Or was that portal a fake somehow?"
    "No...Ayame was so sure it wasn't."
    "Maybe I did something wrong?"
    "Ayame!"
    "Can she even hear me right now?"
    "I can't even tell if I'm saying this out loud or if it's all in my head."
    "I guess I'll just wait until I hear something..."
    "Any second now..."
    "Any...second..."
    "Maybe I have to do something."
    "I can't just float here and do nothing."
    "But what can I even do?"
    "I don't have a body. It's like I'm just my consciousness."
    "Like a dream..."
    "But if this is like a dream, then I can make it whatever I want it to be...right?"
    "That's it, that's the key."
    "I try to imagine arms and hands."
    "I can sense the feeling of my hands returning."
    "But they feel...different, somehow."
    "They also lack...color?"
    "They're definitely my hands, they feel like they're not the same."
    "I'm getting sidetracked."
    "I need to get the rest of my body back."
    "One by one, my sense of feeling is coming back to me."
    "As my head comes back, I take a deep breath."
    "There's no air."
    "In my panic, I take another breath. There's still no air."
    "I'm suffocating! What do I do?!"
    "I was just fine before. Why is this happening now?!"
    "Think of air, [player]! Think of air!"
    "I gasp for air."
    "This time I can breath properly."
    "I hyperventilate for a few moments to calm myself down from what just happened."
    "Where the hell did we end up?"
    "There's just nothing here."
    "Do I have to come up with the others as well?"
    "Or do they have to do it themselves?"
    "What if I think about the wrong things and they end up messed up somehow?"
    "They won't be the same person..."
    "Just my perception of them."
    "I have to think. There must be something I can do."
    "Maybe some place for us to be at would be a good start."
    scene bg bedroom_gray
    play music t18 fadein 5.0
    "Okay...why is it all in black and white?"
    "Is this what this world is?"
    "Or was that because of me?"
    "I examine my hands and notice they're also just black and white."
    "At least it seems familiar."
    "Maybe this world is just another copy?"
    "Sayori wouldn't make it that easy, would she?"
    "Okay, I can do this."
    if ch16_ay_companions <= 0:
        "I was alone before, I can regroup with her again."
    else:
        "I was alone before, I can regroup with them again."
    "How many times are we going to go through this to get to Sayori?"
    "We have to be getting closer."
    ay "We are getting closer."
    "Whoa! What the hell was that?"
    "It sounded like Ayame's voice."
    "But where is she...?"
    "Her voice sounds like it's coming from all directions."
    ay "Yes, hello. It's me."
    ay "I don't have a corporeal form here."
    ay "I guess it's just a side effect of this world."
    ay "You have to give me a form, [player]."
    ay "Something I can use to interact with the world."
    ay "Anything."
    mc "But how do I do that?"
    mc "Do I just think of you?"
    mc "Of what you look like?"
    ay "I suppose you could do that."
    ay "Just be careful."
    mc "What do you mean?"
    ay "If you looked at the mirror you could see what I mean."
    ay "But don't worry, I'm sure you'll do fine."
    mc "...Huh?"
    ay "Let's just say you didn't exactly give yourself the best embodiment."
    ay "Now focus, [player]."
    ay "Remember who I am. What I looked like."
    ay "Give me something that resembles who I am."
    ay "Then I'll take it over."
    mc "What, are you going to possess it or something?"
    ay "Something like that."
    ay "After that, we can work out where to go next."
    mc "Okay, here goes nothing."
    ay "Focus. You have to focus."
    ay "It's nothing too complicated."
    ay "I don't know if the human body is as complicated as rocket science but...you get it."
    mc "I'll try my best."
    "Despite not knowing her for that long, I've got a vivid image of Ayame in my head."
    "I guess being around her recently will do that."
    "Or maybe she had something to do with it."
    "Either way..."
    ay "You've done it!"
    ay "I'm quite impressed, actually."
    mc "So how is this going to work?"
    ay "Well...I assume I just do {i}this{/i} and..."
    show ayame 1a_gray zorder 2 at t11
    ay "Okay that seemed to work."
    "Ayame appears to have gained control of the image of her I created."
    "Her voice seems to be coming from it now too."
    ay "We have to start by{nw}"
    $ _history_list.pop()
    show screen tear(20, 3, 2, 0, 70)
    window hide(None)
    $ pause(0.3)
    show ayame gw_2_gray_blur
    hide screen tear
    $ pause(0.3)
    window show(None)
    ay "We have to start by{fast}...huh?"
    window auto
    mc "What's wrong?"
    ay "I just...felt something happen. I--"
    ay "This body feels like it's disintegrating."
    ay "It's like...I'm not whole."
    ay "I don't know if that's because of you or..."
    "For some reason, I can't seem to see Ayame's face anymore either."
    "I'm looking directly at her but her face is just...shadowed by something."
    ay "Whatever, we have to start acting now."
    mc "Are you okay, Ayame? Your face is--"
    ay "It doesn't matter if I am or not."
    ay "This isn't my real body and so I can't feel anything right now."
    ay "All my senses, they're just gone."
    ay "I can barely even move properly."
    ay "I don't know how long we have, but it's best we act quickly."
    ay "I have a suspicion we don't want to be here for too long."
    mc "Alright..."
    if ch16_ay_companions == 4:
        ay "But first, you need to do the same for the other two as well."
        mc "How come I can't hear their voices?"
        ay "I...don't know. It might be because I'm the only one you still have a link to."
        ay "We didn't exactly re-establish it."
        mc "So what do we do then?"
        ay "They should be around here somewhere, right?"
        ay "Try coming up with something for them to embody."
        ay "Maybe that'll work."
        ay "And maybe--"
        "Before Ayame can finish her sentence, I come up with two more things that mildly resemble Yuri and Natsuki."
        "It suddenly appears in front of us."
        ay "...make it more sophisticated."
        ay "Never mind."
        mc "Well, what do we do now?"
        ay "We wait. Hopefully, they'll begin to move soon."
        ay "All they have to do is walk into it."
        ay "Or...float into it."
        mc "So they have to go into it somehow."
        mc "Then how did I start moving?"
        ay "I don't know. Maybe you created it where you were and did it automatically."
        mc "I suppose. That does make the most sense."
        "I can't help but feel Ayame is hiding something from me."
        "Like she knows more than what she's letting out."
        "Maybe Natsuki was right..."
        "The figure that resembles Natsuki begins to move."
        "The movements are rigid at first, unlike when Ayame did it."
        "I can only assume that it's Natsuki that's inhabited it."
        "Not long after, the figure resembling Yuri starts moving as well."
        "Their movements are almost robotic."
        "I wonder why they're like that when Ayame could move perfectly fine."
        mc "Are the two of you okay?"
        mc "I didn't mess anything up did I?"
        "The figure resembling Natsuki looks at me."
        "Or at least, I think it is. I didn't exactly give it eyes."
        ay "I think maybe it's trying to talk. It doesn't exactly have a mouth."
        mc "But I can hear you just fine."
        ay "Oh, right. Hold on a second."
        ay "I think that should do it."
        ay "We should be able to communicate properly now."
        ay "I forgot to mention I'm not actually speaking."
        ay "I just thought it'd be more natural if my voice was emitting from this body you made for me."
        ay "It's like how it was when the whole world was frozen."
        ay "I'm not sure you've realized but you don't have a mouth either, [player]."
        mc "I don't even know how I made myself."
        mc "From what I can see, I don't look any different."
        mc "Or {i}feel{/i} that much different."
        ay "Your body doesn't seem to be disintegrating like mine."
        ay "Perhaps you made it more sturdy somehow."
        ay "Regardless...it's probably best you don't look in a mirror."
        ay "Anyway...did the link work? Natsuki? Yuri?"
        show natsuki 1a_gray zorder 2 at t31
        n "What's going on?"
        "Natsuki's voice echoes in my head."
        "But at the same time it sounds like it's coming from the figure I made of her."
        n "What the{nw}"
        $ _history_list.pop()
        show screen tear(20, 3, 2, 0, 70)
        window hide(None)
        $ pause(0.3)
        show natsuki gw_2_gray_blur
        hide screen tear
        $ pause(0.3)
        window show(None)
        n "What the{fast} hell is this?"
        window auto
        "Natsuki's figure starts to move a bit more naturally now."
        "I guess whatever Ayame did worked."
        "But now Natsuki's face is shadowed too."
        "What is going on...?"
        ay "There it is again..."
        ay "[player], you've noticed it, right?"
        mc "I think so."
        n "You couldn't have made me a little taller?"
        mc "Ayame said--"
        n "Ugh, whatever. It's not like it should be the thing we're worried about right now."
        n "But come on."
        mc "I'll...do better next time, I guess?"
        ay "I don't think there'll be a next time."
        ay "But since we can hear Natsuki, the link must be back up. Yuri, are you here?"
        show yuri 1a_gray zorder 2 at t33
        y "I-I'm here.{nw}"
        $ _history_list.pop()
        show screen tear(20, 3, 2, 0, 70)
        window hide(None)
        $ pause(0.3)
        show yuri gw_2_gray_blur
        hide screen tear
        $ pause(0.3)
        window show(None)
        y "I-I'm here.{fast} At least, I think I am."
        window auto
        "Yuri figure raises one of its hand and tries to wave."
        "Her face, like I expected, started to become shadowed too."
        ay "{i}(There it is again...){/i}"
        y "What are we doing here?"
        ay "Have you forgotten what we're meant to be doing?"
        y "No, I mean...why are we in [player]'s room?"
        ay "Well..."
        "Ayame's figure--"
        "{i}Ayame{/i} looks towards me."
        mc "It was the first place I thought of."
        mc "This whole place was just a void."
        y "I think you did a good job recreating it."
        y "Everything appears to be as it should be."
        "Yuri looks around the room."
        y "Except...why is it all black and white?"
        mc "I don't know, I didn't imagine it to be black and white. It just turned out that way."
        n "Okay, two things."
        n "One, I don't have the journal anymore."
        n "It's just gone, presumably with the rest of my original self."
        ay "We won't need it. I'm sure we can figure this out without it."
        n "That's not even my biggest concern, Ayame."
        n "If [player] made this place, then how are we supposed to figure out where to go?"
        y "That's a good point. The world outside this room doesn't exist, does it?"
        y "It would just be...empty."
        ay "This world, dimension or whatever is definitely different to what you're all used to."
        ay "We're going to need to get creative if we're going to get to Sayori."
        n "Can you explain what's going on?"
        ay "I'm not entirely sure, but it seems like [player] can create whatever [player_personal] wants with just a thought."
        ay "Tell me if I'm wrong."
        mc "From what I can tell, you're right."
        mc "I don't entirely understand how it works."
        mc "But just tell me what I should do."
        ay "I can't be completely sure if this will work."
        ay "But I think you have to create us a path to Sayori."
        mc "A path to Sayori? What do you mean?"
        ay "There's nothing out there."
        ay "I mean literally, it's just completely empty."
        "Ayame points to the window and points out the vast emptiness stretching across as far as I can see."
        ay "The only thing that exists is your room and the four of us here."
        mc "Right."
        n "What are you trying to get at, Ayame?"
        ay "I'm speculating that [player] has to create this world."
        y "But how is [player_personal] going to know what to create?"
        ay "Now that's the thing we have to figure out."
        ay "Again, I'm not sure, but I think the bench was a kind of hint."
        ay "You said that you had adventures with her, didn't you?"
        ay "Then maybe..."
        "My adventures with Sayori..."
        "Go back. Remember the good times because the world will end...why am I the only one that can remember those whispers?"
        "The others forgot about it already, somehow."
        "Yet it's still clear in my head."
        "What was one of our first adventures?"
        "My head is filled with all of these memories that I didn't know existed."
        "Yet one seems to stand out..."
        mc "Go back. Remember the good times because the world will end."
        "I say that without even thinking and suddenly the room begins to shake."
        y "W-What's happening?"
        n "Look outside!"
        "Natsuki points out the window and it appears that some sort of beach is forming."
        "Was that because of me?"
        scene bg bedroom_gray_color
        show natsuki gw_2_blur zorder 2 at i31
        show ayame gw_2_blur zorder 2 at i32
        show yuri gw_2_blur zorder 2 at i33
        "Slowly, the world begins to regain color."
        "I can hear waves crashing and the wind howling outside."
        ay "[player], was this your doing?"
        mc "I don't know. It just sort of...happened!"
        mc "Am I really capable of doing something like this?"
        mc "All by myself?"
        ay "Maybe you were inspired by something..."
        ay "...or someone."
        "She's obviously talking about Sayori."
        "I guess she did have some part to play in this."
        n "I don't know about you guys but I'm going to check this out."
        n "Talking about it in here isn't going to solve anything."
        ay "True enough. Let's get going then."
        ay "Hopefully we don't run into too much trouble out there."
        y "Are you saying we will?"
        ay "Who knows? This was up to [player]'s imagination after all."
        mc "We should be fine..."
        "I think."
        ay "Daylight's burning, let's go."
        scene bg beach_day
        show natsuki gw_2_blur zorder 2 at t31
        show ayame gw_2_blur zorder 2 at t32
        show yuri gw_2_blur zorder 2 at t33
        with wipeleft_scene
        "As I open the door, the four of us are treated to an eerily familiar shoreline."
        "Well, except the random bedroom in the middle of it all."
        "A memory is trying to bring itself forward in my head."
        "Pirates...?"
        "How long ago was this memory?"
        "I almost forgot about this entirely, but now..."
        "Now...this whole place is clear in my head."
        ay "So where to, [player]?"
        ay "You know this place, don't you?"
        mc "How could you tell?"
        ay "Let's call it intuition."
        mc "I know this place like the back of my hand but..."
        "I look around and take in the view."
        "Everything is just how I remember it."
        "It's not like the park where some things are different."
        "Everything, except the bedroom, is exactly how I remember it all those years ago."
        mc "I have no idea where we're meant to go."
        ay "Then let's take a walk around."
        ay "That might jog your memory a little bit."
        n "Ugh, I hate walking around in sand like this."
        n "I can already feel some getting into my shoes."
        y "I agree, it's not the most pleasant experience but let's just deal with it."
        ay "Why don't you take us around the place?"
        ay "Speaking of which, what is this place?"
        mc "When we were younger, we would go here and pretend we were pirates."
        mc "We would hide some treasure and try to find the each other's treasure before they found ours."
        y "Like a scavenger hunt of some kind."
        mc "I suppose."
        ay "Was there any location of signif--"
        "Ayame suddenly cuts herself off."
        "It's as if she doesn't know the word she's trying to say."
        ay "How do you say that word? S-Signifidance? N-No...significance. There."
        ay "Any locations of significance around here?"
        mc "Just a couple. There was this tree for one..."
        "I lead the three of them to one of the trees."
        "It has a rope attached to it already."
        "Sayori and I would always bring one along every time we went here."
        "It was just for climbing and swinging on this tree."
        "Though I imagine doing that now would probably lead to injury..."
        "We were a lot lighter back then."
        ay "I see..."
        "Ayame places a hand on the rope."
        "She looks up at the canopy of the tree."
        ay "I can imagine the two of you climbing up to the top."
        ay "Seeing who could do it faster."
        ay "That's what it looks like since all these distinct markings are here."
        n "You're right, it looks like a bunch of little kids tried climbing this thing."
        n "I wouldn't have spotted that if you didn't say anything though. Good eye."
        mc "Three minutes."
        y "Huh? What's three minutes?"
        mc "That's how fast I could do get to the top."
        mc "It might not seem that impressive but we were a lot younger back then!"
        mc "This tree seemed really tall."
        mc "Funny thing is, I don't think I could do it now if I wanted to."
        mc "I could try but I'd probably fail miserably."
        mc "Besides, there's some other things I want to show you all."
        n "That would have been something to see."
        n "But I guess we don't have much time, do we?"
        ay "Hmm...I can't seem to feel anything from this."
        ay "I don't think this is the right spot."
        mc "The right spot for what?"
        ay "I suspect that one of these areas is the key to get to Sayori."
        ay "Don't ask me why, just trust me on this."
        y "There's no time to argue."
        n "Just do as she says, [player]."
        "I haven't even said anything to suggest I would disagree with her."
        "Besides, it's not like I have much choice anyway."
        "We're stuck here until we can fix this mess."
        ay "So where's the next place?"
        mc "Alright...let me think."
        "I didn't even get to finish explaining the rest of this place."
        "It's strange. All of the memories that were in my subconscious are coming back to me."
        "The times that I spent here, at this tree, with Sayori..."
        "I wouldn't trade them for anything."
        # stop music fadeout 2.0
        scene bg beach_day_gray
        show sayori 4bl_gray zorder 2 at i11
        show vignette zorder 100
        with dissolve_scene_full
        # play music "<loop 4.444>bgm/5.ogg" fadein 1.0
        $ style.say_window = style.window_flashback
        "What the...?"
        "It's Sayori...and we're at the beach except..."
        mc "S-Sayori, are you okay?!"
        mc "You're not hurt, are you?"
        s "I-I'm fine, [player]."
        s "It's just a scratch, see?"
        "This is when she..."
        mc "Sayori, you're bleeding! We need to go find your parents."
        s "No, don't! I'll be fine, I promise."
        mc "You can't be fine after falling from the tree like that."
        mc "Come on. It's the right thing to do."
        s "My parents don't have to know."
        mc "You really think they're not gonna notice that red patch on your knee?"
        s "W-Well..."
        "I remember this...but why is she older?"
        "This happened when we were still children, didn't it?"
        "This doesn't make any sense."
        mc "I just don't want you to get hurt, okay?"
        mc "I'll even carry you back."
        s "Ahaha, are you serious?"
        mc "Of course."
        s 4by_gray "Well, when you put it like that..."
        s "Alright, fine. Only because you're insisting on it."
        s "I'm gonna get in so much trouble for this..."
        mc "You'll get over it."
        scene white with dissolve_cg
        scene bg beach_day
        show natsuki gw_2_blur zorder 2 at t31
        show ayame gw_2_blur zorder 2 at t32
        show yuri gw_2_blur zorder 2 at t33
        with dissolve_scene_full
        $ style.say_window = style.window
        n "Are you there?"
        mc "H-Huh?"
        n "You looked like you were daydreaming."
        mc "I was just remembering something, sorry."
        "Was Sayori being older in my memory a result of this new world we're in?"
        "Was that memory even real? It sure {i}felt{/i} real but..."
        "I have so many questions. It's so frustrating not being able to get them answered."
        "I'll just have to ask Sayori myself when I see her."
        mc "What were we doing again?"
        ay "You were bringing us to the next place you think is important around here."
        y "Where's the next location, [player]?"
        mc "It should be just over here."
        scene bg clearing
        show natsuki gw_2_blur zorder 2 at t31
        show ayame gw_2_blur zorder 2 at t32
        show yuri gw_2_blur zorder 2 at t33
        with wipeleft_scene
        "I lead the three of them through some bushes and trees."
        "It's quite a distance from the beach but you can still make out the beach from here if you look carefully."
        "The spot we're going to was a hiding spot me and Sayori used a lot."
        "Whenever Sayori just wanted to hear the distant crashing of waves, we would go there."
        "There was a little clearing there that was perfect to just sit down and take in the world."
        "No one would ever go there, probably because it was pretty well hidden."
        n "What is this place?"
        y "How curious."
        ay "This is a pretty cozy place, isn't it?"
        ay "I imagine the two of you probably remember it differently."
        ay "The trees probably grew larger and took up more space since you were children, right?"
        mc "Yeah, I haven't been here in a while..."
        mc "It does seem smaller than I remember."
        y "It's quite peaceful here."
        y "It reminds me of one of the areas near the mall that I go to sometimes."
        y "Quiet except for the sound of nature."
        n "I can see why you'd wanna hang out here."
        n "I get this warm feeling when I'm here."
        ay "So are you going to give us some sort of explanation as to what this is?"
        ay "How it's significant to us?"
        mc "Us?"
        ay "I mean, how it's significant to you and Sayori."
        ay "Like why this would be a place that could lead to here."
        mc "Oh, right. Well..."
        mc "Personally, I didn't really understand why Sayori liked this place so much."
        mc "Sure, it was quiet but I guess I'm not really the kind of person that's bothered by loud noise too much."
        mc "I guess I was just here for Sayori."
        ay "Do you know why she liked this place so much, [player]?"
        ay "That's the question you need to answer."
        mc "Do you need to know that to be able to sense if this is the right place?"
        ay "Well...maybe I do, maybe I don't."
        ay "I'm just curious if you know."
        n "Just answer her, [player]."
        y "We would all like to know as well."
        mc "Okay, okay. I'll admit I don't know the real reason."
        mc "This was just {i}our{/i} spot, I suppose that's part of what made it special."
        mc "But..."
        ay "But...?"
        mc "If I had to make a guess, I'd say it's because of how Sayori was as a person."
        y "What do you mean?"
        mc "It wasn't obvious when we were younger."
        mc "But now that I think about it, I think she was depressed at a young age."
        mc "Even when we were still kids."
        ay "Oh? What makes you think that?"
        mc "I think she just enjoyed my company."
        mc "This is just what I think, I could be wrong for all I know."
        mc "But I think she chose this place because it was just me and her."
        mc "And nothing else."
        ay "Hmm...that sounds like an acceptable answer."
        mc "Acceptable?"
        show ayame at s32
        "Ayame kneels on the ground and places a hand on the ground."
        "She closes her eyes and takes a deep breath."
        mc "What are you doing?"
        ay "I'm trying to get a feeling for the area."
        show ayame at t32
        "She gets up and brushes the dirt off her hand."
        ay "There's definitely something around here."
        ay "But I don't think this is what's going to lead to Sayori."
        mc "How can you tell?"
        ay "I just can, trust me."
        mc "Well, what would we find then?"
        ay "It could be something from your past."
        ay "It might not be something you want to see, like a depressed--"
        ay "{i}Repressed{/i} memory. I'd rather not poke into it too much."
        ay "All I know is that the thing that I'm sensing isn't what it should be, so let's get going."
        mc "But how exactly do you know if what you're sensing is what it should be?"
        n "Ugh, don't you trust her, [player]? Come on, we have to go."
        y "To the next location it is, then."
        "Natsuki and Yuri seem to be pretty compliant about all of this."
        "They seemed pretty skeptical of Ayame before..."
        "Is it because of how I made them in this world?"
        "Did something change in them because of me?"
        mc "Alright, fine. I can only think of one more place."
        mc "If that's not it, then I have no idea."
        mc "It's a shame."
        ay "What is?"
        mc "All this reminiscing, it's just crazy to think about all that's happened since then."
        mc "Just thinking about all that we went through since we were kids."
        ay "Yeah...it has been a journey, hasn't it?"
        ay "F-For you and Sayori, I mean."
        "Interesting."
        mc "I'll take you to the last place now."
        mc "It's back closer to the beach."
        ay "Lead the way then."
        scene bg beach_day
        show natsuki gw_2_blur zorder 2 at t31
        show ayame gw_2_blur zorder 2 at t32
        show yuri gw_2_blur zorder 2 at t33
        with wipeleft_scene
        "I take the three of them back to the beach."
        "I slow my pace down a bit and walk along the shore."
        "The tide seems to be low now, which means we should be able to see it soon."
        "It's around here somewhere, isn't it...?"
        n "What are we meant to be looking for exactly?"
        n "I can start to feel the sand getting in my shoes."
        mc "Didn't you say that before?"
        n "I-I did? I um--"
        y "Well, it seems we're just walking along the shore."
        y "Is there some purpose to this, [player]?"
        mc "There's something here that you can only see during low tide."
        ay "What is it?"
        mc "Sayori and I rarely got to do this."
        mc "But we used to collect shells during low tide."
        mc "We'd have this bucket and everything."
        n "But what's the point?"
        mc "The point of collecting sea shells?"
        mc "I suppose there was no point."
        mc "It was just something she wanted to do."
        ay "Then why would you let her do that?"
        ay "Not all of her ideas are so great, you know."
        n "Right, I mean look at the mess we're in because of her ideas."
        mc "Sayori had all these ideas that would just come into her head."
        mc "Besides, there's nothing wrong with collecting seashells."
        mc "It's just something to do to pass the time while we were here."
        mc "In fact, it doesn't matter what we do at all."
        ay "Is that what you think?"
        mc "Does it matter what I think?"
        mc "Just go do your sensing thing already."
        mc "If it isn't this place, I don't know where it could be."
        ay "Ha."
        "Ayame moves away from the shoreline."
        "Natsuki and Yuri follow behind her."
        ay "You really don't get it, do you?"
        mc "What do you mean?"
        ay "Pirates."
        mc "What about pirates?"
        n "What do pirates need, [player]?"
        y "Treasure, right?"
        "What's going on? Something isn't right here."
        "I know it."
        "I had my suspicions even before I took them to the clearing."
        "It's like the three of them are affected by something, somehow."
        mc "R-Right, they need treasure but..."
        ay "How could you not have figured it out already, [player]?"
        ay "You said you remembered all those places."
        ay "But not what they all represent."
        mc "What are you talking about?"
        mc "How would you even know what they represented?"
        mc "You don't know Sayori like I do."
        n "You used to know what they represent, [player]."
        n "You've just forgotten."
        y "You grew up..."
        y "You left me behind."
        mc "What are you two talking about?"
        mc "I don't understand what's going on."
        mc "How did I leave you behind, Yuri?"
        "Now I know I messed something up."
        "It's like Sayori is..."
        mc "What did I forget?"
        ay "I thought that bringing those memories back would have helped you realize."
        ay "I didn't give them all back to you."
        ay "I had hopes."
        mc "Hopes? Hopes for what?"
        n "Do you really think I didn't bring you here intentionally?"
        n "I thought we could have stayed here forever."
        y "We still can, [player]."
        mc "You three...you aren't yourselves, are you?"
        mc "Something is wrong."
        ay "It's about time you noticed."
        ay "You haven't wondered why you can't see our faces?"
        mc "I...just thought it was part of this world."
        mc "Like one of the side effects or something."
        mc "Am I wrong?"
        ay "Well, I suppose there's no point hiding it anymore."
        ay "I really tried my best to act like the three of them, you know."
        ay "I almost messed up because I couldn't figure out the word."
        "Signifidance..."
        mc "Who are you?"
        n "Isn't it obvious?"
        y "It's me, your best friend."
        ay "Sayori{nw}"
        $ _history_list.pop()
        show screen tear(20, 3, 2, 0, 70)
        window hide(None)
        $ pause(0.3)
        show natsuki gw_2
        show yuri gw_2
        show ayame gw_2
        # play music t6ay
        hide screen tear
        $ pause(0.3)
        window show(None)
        ay "Sayori{fast}."
        window auto
        "I can see their faces now."
        "Their faces are all seem to be locked in a smile."
        "What the hell? Their eyes are a different color."
        "It's almost the same color as..."
        mc "S-Sayori? What do you mean?"
        ay "Oh, come on. It's pretty obvious."
        ay "I've taken over the bodies you created for them."
        ay "I know you saw what happened at the beginning."
        ay "Why they're all glitched out like this, [player]."
        n "Did you really not pay attention?"
        y "Or maybe you were just scared to point it out?"
        "Now that she mentions it...I did notice they sounded kind of different."
        "It's like there was a faint trace of Sayori's voice when they spoke."
        "It wasn't obvious at first but as I took them around the beach..."
        "I could make out her voice more and more."
        "I thought I was just hearing it but now it makes sense."
        "Sayori's voice is mixed with theirs, but it's overpowering them now."
        mc "Sayori, please."
        ay "Please what?"
        mc "Don't do this."
        ay "Why not, [player]? I'm trying to help us all."
        ay "Don't you see?"
        ay "We're just perpetually doomed to repeat the same mistakes over and over."
        mc "You know that's not true."
        mc "We've been given another chance. We have to use it, not like this."
        ay "Ehehe, you're still quite naïve about this world, aren't you?"
        ay gw_2_blur "..."
        "Ayame's face suddenly becomes hidden again."
        ay "You think I haven't considered that, [player]?"
        ay "Do you think I'm doing this without thinking?"
        ay "That I'm somehow misled in my thinking?"
        ay "I've thought about this for a long time."
        ay "It's...{nw}"
        y "...the...{nw}"
        n "...only way."
        mc "That can't be true, Sayori."
        mc "There's always another way."
        ay "Do you truly believe that?"
        mc "Of course I do. We always manage to get through these things, Sayori."
        mc "Why would it be any different now?"
        y "Those were different!"
        n "The things that will happen if this goes on isn't worth it."
        mc "And why do you get to be the judge of that, Sayori?"
        ay "Because I have to be! Don't you see?"
        ay "Without me, the world would have already ended."
        ay "This whole game would have already ended."
        ay "All I'm doing is delaying the inevitable."
        ay "It's all going to come to an end, one way or another."
        mc "Is that really what you believe?"
        ay "Yes, it is."
        mc "Not you, Sayori."
        ay "...?"
        mc "Ayame."
        ay "She's gone. They all are. You know they are."
        mc "Ayame, you're the one who brought us here."
        mc "Are you really going to give up so easily?"
        n "What are you playing at, [player]?"
        y "It's not going to work."
        mc "I know the three of you are still here."
        n "They're gone."
        y "They never made it to this world, [player]."
        "That's not true at all."
        "I could feel them here before...when their faces weren't blurred."
        "Is that when it happened?"
        mc "You're still here, aren't you?"
        mc "I know it."
        ay "[player], stop this."
        ay "You know you can't get out of this situation."
        ay "Can't we just give up together?"
        mc "Sayori, you know I can't do that."
        mc "There's still hope, there has to be."
        mc "Whatever is coming, it can't be the end."
        ay "..."
        "It was just for a moment, but I could have sworn I saw Ayame hesitate."
        ay "I won't let this happen."
        ay "Stop it!"
        mc "Ayame, you're the one who wanted to stop Sayori."
        mc "Because you wanted to help."
        if ch16_ay_message[0] and ch16_ay_message[1] and ch16_ay_message[2] and ch16_ay_message[3]:
            ay "I {i}can't{/i}{nw}"
            $ _history_list.pop()
            show screen tear(20, 3, 2, 0, 70)
            window hide(None)
            $ pause(0.3)
            show ayame 1a
            hide screen tear
            $ pause(0.3)
            window show(None)
            ay "I {i}can't{/i}{fast} let this happen!"
            window auto
            "Ayame's voice rings out. There's only a faint trace of Sayori's voice now."
            "Her face is clear again."
            "This time, her eyes look normal."
            mc "Ayame?"
            n "W-What?"
            y "H-How did you break free? That's impossible!"
            ay 1f "Sayori."
            ay "Did you really think it would be that easy?"
            ay "You know my history, don't you?"
            ay "You know who I was before this cycle."
            ay "Which means, you know what I'm capable of."
            ay "I was just biding my time."
            ay "I needed to learn more."
            mc "Learn what, exactly?"
            ay 1j "I know where we have to go to get to the next world Sayori's conjured up."
            ay "And I have a feeling that this time, a certain someone will be waiting for us on the other side."
            ay "I will {i}stop{/i} you, Sayori. Whatever it takes."
        else:
            $ style.say_dialogue = style.edited
            ay "Y-You..."
            ay "You won't stop{nw}"
            $ _history_list.pop()
            show screen tear(20, 3, 2, 0, 70)
            window hide(None)
            $ pause(0.3)
            show ayame 1o
            hide screen tear
            $ pause(0.3)
            window show(None)
            ay "You won't stop{fast} {i}us{/i} so easily!"
            window auto
            $ style.say_dialogue = style.normal
            "A distorted version of Ayame's voice rings out."
            "Her face is clear again."
            "But there's something about her eyes..."
            $ style.say_dialogue = style.edited
            ay "You really think you could get rid of me, Sayori?"
            ay "I will forever be a part of Ayame."
            ay "And I certainly won't let the likes of you have free reign over her."
            ay "It's cramped enough already! We don't need a third voice in her head."
            ay "You know about us, don't you Sayori?"
            ay 1q "You know where we came from and who we were before this cycle."
            ay "Which means, you know what we're capable of."
            ay "We were just biding our time."
            ay "Now, we have everything we need."
            $ style.say_dialogue = style.normal
            mc "Everything you need for what?"
            $ style.say_dialogue = style.edited
            ay "To get to the next world Sayori made to protect herself."
            ay 1p "And when we get there, we'll--"
            $ style.say_dialogue = style.normal
            "Ayame's face returns to normal."
            ay 1a "...Thank you. I'll take it from here."
            "It looks like she's back to her old self."
            ay 1f "Sayori, you won't get away with this."
            ay "We {i}will{/i} stop you, no matter what."
        n "Stop! You don't understand what you're doing!"
        y "You really don't want to do this."
        ay "Who are you to tell us what we don't want to do?!"
        ay "Especially considering what you've done."
        ay 1n "And what you're still doing."
        ay "You're inside their heads right now, Sayori."
        ay "I felt the same as them just moments ago."
        ay 2f "Do you think they'd want to do this?"
        ay "To put us against each other."
        n "..."
        y "You know I didn't want to do this."
        ay "You lied and you're still lying, Sayori."
        ay "And you've also failed."
        y "I really didn't want to have to resort to this."
        y "I thought we could have just stopped here and be civilized."
        mc "Sayori, what are you doing?"
        ay 2m "Stay back, she's trying something."
        "I can feel something, and it's getting stronger."
        "I don't know what it is but it seems like Sayori is responsible."
        mc "Sayori, don't do this."
        mc "After all we've been through together, does it really have to end like this?"
        if sayori_date:
            n "If it makes any difference..."
            y "I'm sorry, [player]."
        else:
            n "..."
            y "...Yes, it does."
        show natsuki at thide
        show yuri at thide
        hide natsuki
        hide yuri
        "Natsuki and Yuri take a few steps back."
        "Ayame turns towards me and gives me a look."
        ay 1l "I have an idea. Grab some sea shells, quickly."
        mc "What? This is hardly the time to--"
        ay "Just do it!"
        "I quickly run to the shoreline and grab some sea shells."
        "She does the same, taking as much as she can in one hand."
        "I have no idea what these are for but she said to get some."
        "What is she thinking?"
        ay 1a "We should run. Now!"
        "She grabs my hand and points in the direction where the clearing was."
        "I drop some sea shells as we run towards it."
        "In the distance, I can see Natsuki and Yuri just standing there, almost lifeless."
        "Sayori..."
        scene bg clearing
        show ayame 1l zorder 2 at t11
        with wipeleft_scene
        "We arrive at the clearing."
        "Ayame looks back from where we came from."
        "There doesn't seem to be a trace of either of them."
        mc "What are we doing here, Ayame?"
        mc "What is Sayori doing?"
        ay 1m "This is where the portal actually is."
        ay 1a "She tricked you when I said it wasn't here."
        ay "Or, rather when she said it wasn't here."
        mc "How could you tell?"
        ay 2a "When she was controlling me, I could sort of fight back."
        ay "And when I did, I could peer into her mind, if only slightly."
        mc "What did you find out?"
        ay 2m "Well, for one that she can't say 'significance'."
        ay "And another is that the portal is around here somewhere."
        "I look back and see a trail of seashells leading to the clearing."
        mc "Then what are the sea shells for?"
        mc "I dropped some back on the beach, and on the way here."
        ay 2l "It doesn't matter, we won't need the whole lot."
        ay "Just enough to open the portal."
        ay "I think with what the two of us have, it should be enough."
        "She drops her sea shells on the ground and I follow her lead."
        "She looks at them carefully, glancing between the beach and the shells repeatedly."
        mc "What do the sea shells have to do with all this?"
        ay 2a "I think they're an important part of your past with Sayori."
        mc "How?"
        ay "From what I can tell, they're the 'treasure' she mentioned before."
        ay "The treasure to get to the next world."
        ay 1j "Quickly, make a sort of circle shape with the shells you have left."
        "Ayame begins rapidly placing shells down to form a circle."
        "I follow her lead and fill out the other side."
        ay "That's it! I can feel it."
        show ayame at s11
        "Ayame places her hand on the ground, similar to how she did earlier."
        "She closes her eyes and takes a deep breath."
        "A few moments pass and nothing happened."
        mc "What's wrong?"
        ay 1n "I...don't know."
        ay "It should be here, the energy feels the same as before."
        "She tries again, but it's the same result."
        ay 1a "We must be missing {i}something{/i}."
        ay "Think, Ayame, think!"
        "She looks towards me."
        ay "Do you have any ideas?"
        # Might as well give the player something to do lol
        menu:
            mc "Um..."
            "The tree.":
                pass
            "The rope.":
                pass
        ay "Oh?"
        show ayame at t11
        "Ayame gets up from the ground and looks towards the beach."
        ay 1j "You're right! You showed us three locations of significance."
        ay "But we're only using two of them right now."
        ay "We need to go back to the tree and grab that rope."
        ay "I think we need to use it to connect all the sea shells together."
        ay "It's like the knot that holds all the treasure all together."
        ay 1m "Kind of like a treasure chest."
        mc "That seems like a stretch..."
        mc "But it's worth a shot."
        ay 1l "There's just one problem."
        ay 3a "I don't know {i}what the hell{/i} Sayori is doing over there."
        ay "But I can feel the amount of energy being amassed."
        mc "So what do we do?"
        ay 3m "We don't really have a choice, now do we?"
        ay "We're going to have to risk it for the rope."
        mc "Can't I just make a rope like I did with your bodies?"
        ay "I don't think you can."
        ay 3l "But even if you could, it's not the same."
        ay "The rope you make won't have the same sentimental value as the rope hanging from that tree."
        mc "Okay, I guess we're going to have to do something crazy."
        ay 3h "Sure looks like it."
        menu:
            ay "Any final words, in case we don't make it?"
            "We're going to make it.":
                ay "Confidence, I like it. I'm not sure I can say with certainty that's going to happen."
                ay "But we'll see if it pays off."
                ay "I really hope it does."
            "We're going to die.":
                ay "That's not a very optimistic mindset."
                ay "But I suppose that could very much come true."
                ay "I'll just have to try even harder then."
            "I love you.":
                ay "Eh? A sense of humor at a time like this?"
                ay "Good a time as any, I suppose."
                ay "Just in case you were serious though, the feeling is not mutual."
            "I'm sorry.":
                ay "For what? Have you forgotten I'm the one who brought us here?"
                ay "I should say sorry for dragging you into this."
                ay "But the truth is, I wouldn't have got this far without you."
        ay 3m "Ready to go then?"
        mc "No, but let's do it."
        ay "Music to my ears, let's do it."
    elif ch16_ay_companions == 3:
        ay "You have to imagine something for Yuri as well."
        ay "I don't know if she's here because she doesn't have a voice."
        ay "But I can faintly sense her presence."
        mc "Why is that anyway? I could hear you just fine."
        ay "It's probably because we didn't re-establish the link."
        ay "That's how I was able to speak to you."
        mc "That makes sense."
        ay "Now imagine something for Yuri to inhabit."
        ay "It doesn't have to be the same as me, it could be--"
        "Before Ayame can finish her sentence, I come up with something that resembles Yuri."
        "It suddenly appears in front of us."
        ay "...wow."
        ay "Never mind. I guess you know her image quite well."
        mc "What now?"
        ay "Now, we wait. If my theory is correct it'll start moving soon."
        ay "Yuri, if you can hear me..."
        ay "All you have to do is float into it."
        ay "I know it's not the best thing but just bear with it."
        mc "So they have to go into it somehow."
        mc "Then how did I start moving?"
        ay "I don't know. Maybe you created it where you were and did it automatically."
        mc "I suppose. That does make the most sense."
        "The figure that resembles Yuri begins to move."
        "The movements are rigid at first, unlike when Ayame did it."
        "I can only assume that Yuri figured out what to do."
        "Its movements are almost robotic."
        "I wonder why they're like that when Ayame could move perfectly fine."
        mc "Are you okay, Yuri?"
        mc "I didn't mess anything up did I?"
        "The figure I made for Yuri looks at me."
        ay "I think maybe she's trying to talk."
        ay "It is kind of different to how you're used to Yuri."
        mc "But you can talk just fine."
        ay "Oh, right."
        "Ayame puts a hand on Yuri's arm and closes her eyes."
        ay "That should do it."
        ay "We should be able to communicate properly now."
        ay "I forgot to mention I'm not actually speaking."
        ay "I just thought it'd be more natural if my voice was emitting from this body you made for me."
        ay "It's like how it was when the whole world was frozen."
        ay "I'm not sure you've realized but you don't have a mouth, [player]."
        ay "I don't think you gave yourself one."
        mc "I don't even know how I made myself."
        mc "From what I can see, I don't look any different."
        mc "Or {i}feel{/i} that much different."
        ay "I mean...it's probably best you don't look in a mirror."
        ay "Anyway...did the link work? Yuri?"
        show ayame zorder 2 at t21
        show yuri 1a_gray zorder 2 at t22
        y "[player], what is this?"
        "Yuri's voice echoes in my head."
        "It sounds like it's coming from Yuri though."
        "At the same time, Yuri starts to move a bit more naturally now."
        "I guess whatever Ayame did worked."
        y "Why do I feel so...different?"
        "Yuri raises one of her hands and tries to wave."
        mc "Well..."
        y "I suppose it's not the biggest of our concerns at the moment."
        y "At the very least, I can move. I'll manage."
        mc "I'm sorry it might have been me that could have made your body differently."
        mc "I thought it would have been okay since I made Ayame's too and she's okay."
        mc "I'll do better next time."
        ay "I don't think there'll be a next time."
        ay "But since we can hear Yuri, the link must be back up."
        y "That does seem to be the case. I think we're set."
        y "So what{nw}"
        $ _history_list.pop()
        show screen tear(20, 3, 2, 0, 70)
        window hide(None)
        $ pause(0.3)
        show yuri gw_2_gray_blur
        hide screen tear
        $ pause(0.3)
        window show(None)
        y "So what{fast} are we doing here?"
        window auto
        ay "{i}(What is that...?){/i}"
        y "Did you say something?"
        ay "Nothing."
        ay "Have you forgotten what we're meant to be doing?"
        y "No, I mean...why are we in [player]'s room?"
        ay "Well..."
        "Ayame looks towards me."
        mc "It was the first place I thought of."
        mc "This whole place was just a void."
        y "I think you did a good job recreating it."
        y "Everything appears to be as it should be."
        "Yuri looks around the room."
        y "Except...why is it all black and white?"
        mc "I don't know, I didn't imagine it to be black and white. It just turned out that way."
        y "I see..."
        "Yuri approaches the window to my room."
        y "It seems like the world outside this room doesn't exist."
        y "It just looks...empty."
        ay "This world, dimension or whatever is definitely different to what you're both used to."
        ay "We're going to need to get creative if we're going to get to Sayori."
        y "Do you know what's going on, Ayame?"
        ay "I'm not entirely sure, but it seems like [player] can create whatever [player_personal] wants with just a thought."
        ay "Tell me if I'm wrong."
        mc "From what I can tell, you're right."
        mc "I don't entirely understand how it works."
        mc "But just tell me what I should do."
        ay "I can't be completely sure if this will work."
        ay "But I think you have to create us a path to Sayori."
        mc "A path to Sayori? What do you mean?"
        ay "There's nothing out there."
        ay "I mean literally, it's just completely empty."
        "Ayame points to the window and points out the vast emptiness stretching across as far as I can see."
        ay "The only thing that exists is your room and the three of us here."
        mc "Right."
        y "What are you suggesting?"
        ay "I'm speculating that [player] has to create this world."
        y "But how is [player_personal] going to know what to create?"
        ay "Now that's the thing we have to figure out."
        ay "Again, I'm not sure, but I think the bench was a kind of hint."
        ay "You said that you had adventures with her, didn't you?"
        ay "Then maybe..."
        "My adventures with Sayori..."
        "Go back. Remember because the world will end..."
        "That phrase is repeating constantly through my head."
        "What does it mean?"
        "Maybe...?"
        "What was one of our first adventures?"
        "My head is filled with all of these memories that I didn't know existed."
        "Yet one seems to stand out..."
        mc "Go back. Remember because the world will end."
        "I say that without even thinking and suddenly the room begins to shake."
        y "U-Um...what's happening out there?"
        "Yuri points out the window and it appears that some sort of beach is forming."
        "Was that because of me?"
        scene bg bedroom_gray_color
        show ayame gw_2_blur zorder 2 at i21
        show yuri gw_2_blur zorder 2 at i22
        "Slowly, the world begins to regain color."
        "I can hear waves crashing and the wind howling outside."
        ay "[player], was this your doing?"
        mc "I don't know. It just sort of...happened!"
        mc "Am I really capable of doing something like this?"
        mc "All by myself?"
        ay "Maybe you were inspired by something..."
        ay "...or someone."
        "She's obviously talking about Sayori."
        "I guess she did have some part to play in this."
        y "I think it would be a good idea to see what's going on for ourselves."
        y "I don't think we'll find out anything just staying here."
        ay "True enough. Let's get going then."
        ay "Hopefully we don't run into too much trouble out there."
        y "Are you saying we will?"
        ay "Who knows? This was up to [player]'s imagination after all."
        mc "We should be fine..."
        "I think."
        ay "Daylight's burning, let's go."
        scene bg beach_day
        show ayame gw_2_blur zorder 2 at t21
        show yuri gw_2_blur zorder 2 at t22
        with wipeleft_scene
        "As I open the door, the three of us are treated to an eerily familiar shoreline."
        "Well, except the random bedroom in the middle of it all."
        "A memory is trying to bring itself forward in my head."
        "Pirates...?"
        "How long ago was this memory?"
        "I almost forgot about this entirely, but now..."
        "Now...this whole place is clear in my head."
        ay "So where to, [player]?"
        ay "You know this place, don't you?"
        mc "How could you tell?"
        ay "Let's call it intuition."
        mc "I know this place like the back of my hand but..."
        "I look around and take in the view."
        "Everything is just how I remember it."
        "It's not like the park where some things are different."
        "Everything, except the bedroom, is exactly how I remember it all those years ago."
        mc "I have no idea where we're meant to go."
        ay "Then let's take a walk around."
        ay "That might jog your memory a little bit."
        y "I think I'm getting some sand in my shoes."
        y "Not exactly the most pleasant experience..."
        ay "Why don't you take us around the place?"
        ay "Speaking of which, what is this place?"
        mc "When we were younger, we would go here and pretend we were pirates."
        mc "We would hide some treasure and try to find the each other's treasure before they found ours."
        y "Like a scavenger hunt of some kind."
        mc "I suppose."
        ay "Was there any location of signif--"
        "Ayame suddenly cuts herself off."
        "It's as if she doesn't know the word she's trying to say."
        ay "How do you say that word? S-Signifidance? N-No...significance. There."
        ay "Any locations of significance around here?"
        mc "Just a couple. There was this tree for one..."
        "I lead the two of them to one of the trees."
        "It has a rope attached to it already."
        "Sayori and I would always bring one along every time we went here."
        "It was just for climbing and swinging on this tree."
        "Though I imagine doing that now would probably lead to injury..."
        "We were a lot lighter back then."
        ay "I see..."
        "Ayame places a hand on the rope."
        "She looks up at the canopy of the tree."
        ay "I can imagine the two of you climbing up to the top."
        ay "Seeing who could do it faster."
        ay "That's what it looks like since all these distinct markings are here."
        y "It does look like some young children made attempts to climb this."
        y "That's very observant, Ayame."
        mc "Three minutes."
        y "Huh? What's three minutes?"
        mc "That's how fast I could do get to the top."
        mc "It might not seem that impressive but we were a lot younger back then!"
        mc "This tree seemed really tall."
        mc "Funny thing is, I don't think I could do it now if I wanted to."
        mc "I could try but I'd probably fail miserably."
        mc "Besides, there's some other things I want to show you all."
        y "I would be interested in seeing that."
        y "But I suppose we don't really have the time, do we?"
        ay "Hmm...I can't seem to feel anything from this."
        ay "I don't think this is the right spot."
        mc "The right spot for what?"
        ay "I suspect that one of these areas is the key to get to Sayori."
        ay "Don't ask me why, just trust me on this."
        y "There's no time to argue."
        "I haven't even said anything to suggest I would disagree with her."
        "Besides, it's not like I have much choice anyway."
        "We're stuck here until we can fix this mess."
        ay "So where's the next place?"
        mc "Alright...let me think."
        "I didn't even get to finish explaining the rest of this place."
        "It's strange. All of the memories that were in my subconscious are coming back to me."
        "The times that I spent here, at this tree, with Sayori..."
        "I wouldn't trade them for anything."
        # stop music fadeout 2.0
        scene bg beach_day_gray
        show sayori 4bl_gray zorder 2 at i11
        show vignette zorder 100
        with dissolve_scene_full
        # play music "<loop 4.444>bgm/5.ogg" fadein 1.0
        $ style.say_window = style.window_flashback
        "What the...?"
        "It's Sayori...and we're at the beach except..."
        mc "S-Sayori, are you okay?!"
        mc "You're not hurt, are you?"
        s "I-I'm fine, [player]."
        s "It's just a scratch, see?"
        "This is when she..."
        mc "Sayori, you're bleeding! We need to go find your parents."
        s "No, don't! I'll be fine, I promise."
        mc "You can't be fine after falling from the tree like that."
        mc "Come on. It's the right thing to do."
        s "My parents don't have to know."
        mc "You really think they're not gonna notice that red patch on your knee?"
        s "W-Well..."
        "I remember this...but why is she older?"
        "This happened when we were still children, didn't it?"
        "This doesn't make any sense."
        mc "I just don't want you to get hurt, okay?"
        mc "I'll even carry you back."
        s "Ahaha, are you serious?"
        mc "Of course."
        s 4by_gray "Well, when you put it like that..."
        s "Alright, fine. Only because you're insisting on it."
        s "I'm gonna get in so much trouble for this..."
        mc "You'll get over it."
        scene white with dissolve_cg
        scene bg beach_day
        show ayame gw_2_blur zorder 2 at t21
        show yuri gw_2_blur zorder 2 at t22
        with dissolve_scene_full
        $ style.say_window = style.window
        y "[player], hello?"
        mc "H-Huh?"
        y "You stopped responding to me."
        mc "I was just remembering something, sorry."
        "Was Sayori being older in my memory a result of this new world we're in?"
        "Was that memory even real? It sure {i}felt{/i} real but..."
        "I have so many questions. It's so frustrating not being able to get them answered."
        "I'll just have to ask Sayori myself when I see her."
        mc "What were we doing again?"
        ay "You were bringing us to the next place you think is important around here."
        y "Where's the next location, [player]?"
        mc "It should be just over here."
        scene bg clearing
        show ayame gw_2_blur zorder 2 at t21
        show yuri gw_2_blur zorder 2 at t22
        with wipeleft_scene
        "I lead the two of them through some bushes and trees."
        "It's quite a distance from the beach but you can still make out the beach from here if you look carefully."
        "The spot we're going to was a hiding spot me and Sayori used a lot."
        "Whenever Sayori just wanted to hear the distant crashing of waves, we would go there."
        "There was a little clearing there that was perfect to just sit down and take in the world."
        "No one would ever go there, probably because it was pretty well hidden."
        y "How curious."
        ay "This is a pretty cozy place, isn't it?"
        ay "I imagine the two of you probably remember it differently."
        ay "The trees probably grew larger and took up more space since you were children, right?"
        mc "Yeah, I haven't been here in a while..."
        mc "It does seem smaller than I remember."
        y "It's quite peaceful here."
        y "It reminds me of one of the areas near the mall that I go to sometimes."
        y "Quiet except for the sound of nature."
        ay "So are you going to give us some sort of explanation as to what this is?"
        ay "How it's significant to us?"
        mc "Us?"
        ay "I mean, how it's significant to you and Sayori."
        ay "Like why this would be a place that could lead to here."
        mc "Oh, right. Well..."
        mc "Personally, I didn't really understand why Sayori liked this place so much."
        mc "Sure, it was quiet but I guess I'm not really the kind of person that's bothered by loud noise too much."
        mc "I guess I was just here for Sayori."
        ay "Do you know why she liked this place so much, [player]?"
        ay "That's the question you need to answer."
        mc "Do you need to know that to be able to sense if this is the right place?"
        ay "Well...maybe I do, maybe I don't."
        ay "I'm just curious if you know."
        y "I'd like to know as well."
        mc "Okay, okay. I'll admit I don't know the real reason."
        mc "This was just {i}our{/i} spot, I suppose that's part of what made it special."
        mc "But..."
        ay "But...?"
        mc "If I had to make a guess, I'd say it's because of how Sayori was as a person."
        y "What do you mean?"
        mc "It wasn't obvious when we were younger."
        mc "But now that I think about it, I think she was depressed at a young age."
        mc "Even when we were still kids."
        ay "Oh? What makes you think that?"
        mc "I think she just enjoyed my company."
        mc "This is just what I think, I could be wrong for all I know."
        mc "But I think she chose this place because it was just me and her."
        mc "And nothing else."
        ay "Hmm...that sounds like an acceptable answer."
        mc "Acceptable?"
        show ayame at s21
        "Ayame kneels on the ground and places a hand on the ground."
        "She closes her eyes and takes a deep breath."
        mc "What are you doing?"
        ay "I'm trying to get a feeling for the area."
        show ayame at t21
        "She gets up and brushes the dirt off her hand."
        ay "There's definitely something around here."
        ay "But I don't think this is what's going to lead to Sayori."
        mc "How can you tell?"
        ay "I just can, trust me."
        mc "Well, what would we find then?"
        ay "It could be something from your past."
        ay "It might not be something you want to see, like a depressed--"
        ay "{i}Repressed{/i} memory. I'd rather not poke into it too much."
        ay "All I know is that the thing that I'm sensing isn't what it should be, so let's get going."
        mc "But how exactly do you know if what you're sensing is what it should be?"
        y "Just do as she says, [player]."
        "Yuri seems to be pretty compliant about all of this."
        "Does she trust Ayame that much?"
        mc "Alright, fine. I can only think of one more place."
        mc "If that's not it, then I have no idea."
        mc "It's a shame."
        ay "What is?"
        mc "All this reminiscing, it's just crazy to think about all that's happened since then."
        mc "Just thinking about all that we went through since we were kids."
        ay "Yeah...it has been a journey, hasn't it?"
        ay "F-For you and Sayori, I mean."
        "Interesting."
        mc "I'll take you to the last place now."
        mc "It's back closer to the beach."
        ay "Lead the way then."
        scene bg beach_day
        show ayame gw_2_blur zorder 2 at t21
        show yuri gw_2_blur zorder 2 at t22
        with wipeleft_scene
        "I take the two of them back to the beach."
        "I slow my pace down a bit and walk along the shore."
        "The tide seems to be low now, which means we should be able to see it soon."
        "It's around here somewhere, isn't it...?"
        y "What are we looking for?"
        y "It seems we're just walking along the shore."
        y "Is there some purpose to this, [player]?"
        mc "There's something here that you can only see during low tide."
        ay "What is it?"
        mc "Sayori and I rarely got to do this."
        mc "But we used to collect shells during low tide."
        mc "We'd have this bucket and everything."
        y "I'm not sure I follow."
        mc "The point of collecting sea shells?"
        mc "I suppose there was no point."
        mc "It was just something she wanted to do."
        ay "Then why would you let her do that?"
        ay "Not all of her ideas are so great, you know."
        y "Just look at the situation we're in right now if you want an example."
        mc "Sayori had all these ideas that would just come into her head."
        mc "Besides, there's nothing wrong with collecting seashells."
        mc "It's just something to do to pass the time while we were here."
        mc "In fact, it doesn't matter what we do at all."
        ay "Is that what you think?"
        mc "Does it matter what I think?"
        mc "Just go do your sensing thing already."
        mc "If it isn't this place, I don't know where it could be."
        ay "Ha."
        "Ayame moves away from the shoreline."
        "Yuri follows behind her."
        ay "You really don't get it, do you?"
        mc "What do you mean?"
        ay "Pirates."
        mc "What about pirates?"
        y "Pirates need treasure, right?"
        "What's going on? Something isn't right here."
        "I know it."
        "I had my suspicions even before I took them to the clearing."
        "It's like the two of them are affected by something, somehow."
        mc "R-Right, they need treasure but..."
        ay "How could you not have figured it out already, [player]?"
        ay "You said you remembered all those places."
        ay "But not what they all represent."
        mc "What are you talking about?"
        mc "How would you even know what they represented?"
        mc "You don't know Sayori like I do."
        y "You used to know, [player]."
        y "You've just forgotten."
        y "You grew up..."
        y "You left me behind."
        mc "What are you two talking about?"
        mc "I don't understand what's going on."
        mc "How did I leave you behind, Yuri?"
        "Now I know I messed something up."
        "It's like Sayori is..."
        mc "What did I forget?"
        ay "I thought that bringing those memories back would have helped you realize."
        ay "I didn't give them all back to you."
        ay "I had hopes."
        mc "Hopes? Hopes for what?"
        y "Do you really think I didn't bring you here intentionally?"
        y "I thought we could have stayed here forever."
        y "We still can, [player]."
        mc "You two...you aren't yourselves, are you?"
        mc "Something is wrong."
        ay "It's about time you noticed."
        ay "You haven't wondered why you can't see our faces?"
        mc "I...just thought it was part of this world."
        mc "Like one of the side effects or something."
        mc "Am I wrong?"
        ay "Well, I suppose there's no point hiding it anymore."
        ay "I really tried my best to act like the two of them, you know."
        ay "I almost messed up because I couldn't figure out the word."
        "Signifidance..."
        mc "Who are you?"
        y "Isn't it obvious?"
        y "It's me, your best friend."
        ay "Sayori{nw}"
        $ _history_list.pop()
        show screen tear(20, 3, 2, 0, 70)
        window hide(None)
        $ pause(0.3)
        show yuri gw_2
        show ayame gw_2
        # play music t6ay
        hide screen tear
        $ pause(0.3)
        window show(None)
        ay "Sayori{fast}."
        window auto
        "I can see their faces now."
        "Their faces are all seem to be locked in a smile."
        "What the hell? Their eyes are a different color."
        "It's almost the same color as..."
        mc "S-Sayori? What do you mean?"
        ay "Oh, come on. It's pretty obvious."
        ay "I've taken over the bodies you created for them."
        ay "I know you saw what happened at the beginning."
        ay "Why they're all glitched out like this, [player]."
        y "Did you really not pay attention?"
        y "Or maybe you were just scared to point it out?"
        "Now that she mentions it...I did notice they sounded kind of different."
        "It's like there was a faint trace of Sayori's voice when they spoke."
        "It wasn't obvious at first but as I took them around the beach..."
        "I could make out her voice more and more."
        "I thought I was just hearing it but now it makes sense."
        "Sayori's voice is mixed with theirs, but it's overpowering them now."
        mc "Sayori, please."
        ay "Please what?"
        mc "Don't do this."
        ay "Why not, [player]? I'm trying to help us all."
        ay "Don't you see?"
        ay "We're just perpetually doomed to repeat the same mistakes over and over."
        mc "You know that's not true."
        mc "We've been given another chance. We have to use it, not like this."
        ay "Ehehe, you're still quite naïve about this world, aren't you?"
        ay gw_2_blur "..."
        "Ayame's face suddenly becomes hidden again."
        ay "You think I haven't considered that, [player]?"
        ay "Do you think I'm doing this without thinking?"
        ay "That I'm somehow misled in my thinking?"
        ay "I've thought about this for a long time."
        ay "It's...{nw}"
        y "...the...{nw}"
        ay "...only way."
        mc "That can't be true, Sayori."
        mc "There's always another way."
        ay "Do you truly believe that?"
        mc "Of course I do. We always manage to get through these things, Sayori."
        mc "Why would it be any different now?"
        y "Those were different!"
        y "The things that will happen if this goes on isn't worth it."
        mc "And why do you get to be the judge of that, Sayori?"
        ay "Because I have to be! Don't you see?"
        ay "Without me, the world would have already ended."
        ay "This whole game would have already ended."
        ay "All I'm doing is delaying the inevitable."
        ay "It's all going to come to an end, one way or another."
        mc "Is that really what you believe?"
        ay "Yes, it is."
        mc "Not you, Sayori."
        ay "...?"
        mc "Ayame."
        ay "She's gone. They all are. You know they are."
        mc "Ayame, you're the one who brought us here."
        mc "Are you really going to give up so easily?"
        y "What are you playing at, [player]?"
        y "It's not going to work."
        mc "I know the two of you are still here."
        y "They're gone."
        y "They never made it to this world, [player]."
        "That's not true at all."
        "I could feel them here before...when their faces weren't blurred."
        "Is that when it happened?"
        mc "You're still here, aren't you?"
        mc "I know it."
        ay "[player], stop this."
        ay "You know you can't get out of this situation."
        ay "Can't we just give up together?"
        mc "Sayori, you know I can't do that."
        mc "There's still hope, there has to be."
        mc "Whatever is coming, it can't be the end."
        ay "..."
        "It was just for a moment, but I could have sworn I saw Ayame hesitate."
        ay "I won't let this happen."
        ay "Stop it!"
        mc "Ayame, you're the one who wanted to stop Sayori."
        mc "Because you wanted to help."
        if ch16_ay_message[0] and ch16_ay_message[1] and ch16_ay_message[2] and ch16_ay_message[3]:
            ay "I {i}can't{/i}{nw}"
            $ _history_list.pop()
            show screen tear(20, 3, 2, 0, 70)
            window hide(None)
            $ pause(0.3)
            show ayame 1a
            hide screen tear
            $ pause(0.3)
            window show(None)
            ay "I {i}can't{/i}{fast} let this happen!"
            window auto
            "Ayame's voice rings out. There's only a faint trace of Sayori's voice now."
            "Her face is clear again."
            "This time, her eyes look normal."
            mc "Ayame?"
            y "W-What?"
            y "H-How did you break free? That's impossible!"
            ay 1f "Sayori."
            ay "Did you really think it would be that easy?"
            ay "You know my history, don't you?"
            ay "You know who I was before this cycle."
            ay "Which means, you know what I'm capable of."
            ay "I was just biding my time."
            ay "I needed to learn more."
            mc "Learn what, exactly?"
            ay 1j "I know where we have to go to get to the next world Sayori's conjured up."
            ay "And I have a feeling that this time, a certain someone will be waiting for us on the other side."
            ay "I will {i}stop{/i} you, Sayori. Whatever it takes."
        else:
            $ style.say_dialogue = style.edited
            ay "Y-You..."
            ay "You won't stop{nw}"
            $ _history_list.pop()
            show screen tear(20, 3, 2, 0, 70)
            window hide(None)
            $ pause(0.3)
            show ayame 1o
            hide screen tear
            $ pause(0.3)
            window show(None)
            ay "You won't stop{fast} {i}us{/i} so easily!"
            window auto
            $ style.say_dialogue = style.normal
            "A distorted version of Ayame's voice rings out."
            "Her face is clear again."
            "But there's something about her eyes..."
            $ style.say_dialogue = style.edited
            ay "You really think you could get rid of me, Sayori?"
            ay "I will forever be a part of Ayame."
            ay "And I certainly won't let the likes of you have free reign over her."
            ay "It's cramped enough already! We don't need a third voice in her head."
            ay "You know about us, don't you Sayori?"
            ay 1q "You know where we came from and who we were before this cycle."
            ay "Which means, you know what we're capable of."
            ay "We were just biding our time."
            ay "Now, we have everything we need."
            $ style.say_dialogue = style.normal
            mc "Everything you need for what?"
            $ style.say_dialogue = style.edited
            ay "To get to the next world Sayori made to protect herself."
            ay 1p "And when we get there, we'll--"
            $ style.say_dialogue = style.normal
            "Ayame's face returns to normal."
            ay 1a "...Thank you. I'll take it from here."
            "It looks like she's back to her old self."
            ay 1f "Sayori, you won't get away with this."
            ay "We {i}will{/i} stop you, no matter what."
        y "Stop! You don't understand what you're doing!"
        y "You really don't want to do this."
        ay "Who are you to tell us what we don't want to do?!"
        ay "Especially considering what you've done."
        ay 1n "And what you're still doing."
        ay "You're inside their heads right now, Sayori."
        ay "I felt the same as them just moments ago."
        ay 2f "Do you think they'd want to do this?"
        ay "To put us against each other."
        y "...You know I didn't want to do this."
        ay "You lied and you're still lying, Sayori."
        ay "And you've also failed."
        y "I really didn't want to have to resort to this."
        y "I thought we could have just stopped here and be civilized."
        mc "Sayori, what are you doing?"
        ay 2m "Stay back, she's trying something."
        "I can feel something, and it's getting stronger."
        "I don't know what it is but it seems like Sayori is responsible."
        mc "Sayori, don't do this."
        mc "After all we've been through together, does it really have to end like this?"
        if sayori_date:
            y "If it makes any difference..."
            y "I'm sorry, [player]."
        else:
            y "...Yes, it does."
        show yuri at thide
        hide yuri
        "Yuri takes a few steps back."
        "Ayame turns towards me and gives me a look."
        ay 1l "I have an idea. Grab some sea shells, quickly."
        mc "What? This is hardly the time to--"
        ay "Just do it!"
        "I quickly run to the shoreline and grab some sea shells."
        "She does the same, taking as much as she can in one hand."
        "I have no idea what these are for but she said to get some."
        "What is she thinking?"
        ay 1a "We should run. Now!"
        "She grabs my hand and points in the direction where the clearing was."
        "I drop some sea shells as we run towards it."
        "In the distance, I can see Yuri just standing there, almost lifeless."
        "Sayori..."
        scene bg clearing
        show ayame 1l zorder 2 at t11
        with wipeleft_scene
        "We arrive at the clearing."
        "Ayame looks back from where we came from."
        "There doesn't seem to be a trace of Yuri."
        mc "What are we doing here, Ayame?"
        mc "What is Sayori doing?"
        ay 1m "This is where the portal actually is."
        ay 1a "She tricked you when I said it wasn't here."
        ay "Or, rather when she said it wasn't here."
        mc "How could you tell?"
        ay 2a "When she was controlling me, I could sort of fight back."
        ay "And when I did, I could peer into her mind, if only slightly."
        mc "What did you find out?"
        ay 2m "Well, for one that she can't say 'significance'."
        ay "And another is that the portal is around here somewhere."
        "I look back and see a trail of seashells leading to the clearing."
        mc "Then what are the sea shells for?"
        mc "I dropped some back on the beach, and on the way here."
        ay 2l "It doesn't matter, we won't need the whole lot."
        ay "Just enough to open the portal."
        ay "I think with what the two of us have, it should be enough."
        "She drops her sea shells on the ground and I follow her lead."
        "She looks at them carefully, glancing between the beach and the shells repeatedly."
        mc "What do the sea shells have to do with all this?"
        ay 2a "I think they're an important part of your past with Sayori."
        mc "How?"
        ay "From what I can tell, they're the 'treasure' she mentioned before."
        ay "The treasure to get to the next world."
        ay 1j "Quickly, make a sort of circle shape with the shells you have left."
        "Ayame begins rapidly placing shells down to form a circle."
        "I follow her lead and fill out the other side."
        ay "That's it! I can feel it."
        show ayame at s11
        "Ayame places her hand on the ground, similar to how she did earlier."
        "She closes her eyes and takes a deep breath."
        "A few moments pass and nothing happened."
        mc "What's wrong?"
        ay 1n "I...don't know."
        ay "It should be here, the energy feels the same as before."
        "She tries again, but it's the same result."
        ay 1a "We must be missing {i}something{/i}."
        ay "Think, Ayame, think!"
        "She looks towards me."
        ay "Do you have any ideas?"
        # Might as well give the player something to do lol
        menu:
            mc "Um..."
            "The tree.":
                pass
            "The rope.":
                pass
        ay "Oh?"
        show ayame at t11
        "Ayame gets up from the ground and looks towards the beach."
        ay 1j "You're right! You showed us three locations of significance."
        ay "But we're only using two of them right now."
        ay "We need to go back to the tree and grab that rope."
        ay "I think we need to use it to connect all the sea shells together."
        ay "It's like the knot that holds all the treasure all together."
        ay 1m "Kind of like a treasure chest."
        mc "That seems like a stretch..."
        mc "But it's worth a shot."
        ay 1l "There's just one problem."
        ay 3a "I don't know {i}what the hell{/i} Sayori is doing over there."
        ay "But I can feel the amount of energy being amassed."
        mc "So what do we do?"
        ay 3m "We don't really have a choice, now do we?"
        ay "We're going to have to risk it for the rope."
        mc "Can't I just make a rope like I did with your bodies?"
        ay "I don't think you can."
        ay 3l "But even if you could, it's not the same."
        ay "The rope you make won't have the same sentimental value as the rope hanging from that tree."
        mc "Okay, I guess we're going to have to do something crazy."
        ay 3h "Sure looks like it."
        menu:
            ay "Any final words, in case we don't make it?"
            "We're going to make it.":
                ay "Confidence, I like it. I'm not sure I can say with certainty that's going to happen."
                ay "But we'll see if it pays off."
                ay "I really hope it does."
            "We're going to die.":
                ay "That's not a very optimistic mindset."
                ay "But I suppose that could very much come true."
                ay "I'll just have to try even harder then."
            "I love you.":
                ay "Eh? A sense of humor at a time like this?"
                ay "Good a time as any, I suppose."
                ay "Just in case you were serious though, the feeling is not mutual."
            "I'm sorry.":
                ay "For what? Have you forgotten I'm the one who brought us here?"
                ay "I should say sorry for dragging you into this."
                ay "But the truth is, I wouldn't have got this far without you."
        ay 3m "Ready to go then?"
        mc "No, but let's do it."
        ay "Music to my ears, let's do it."
    elif ch16_ay_companions == 2:
        ay "You have to imagine something for Natsuki as well."
        ay "I don't know if she's here because she doesn't have a voice but she should be."
        ay "I can sense her presence but just barely."
        mc "Why is that anyway? I could hear you just fine."
        ay "It's probably because we didn't re-establish the link."
        ay "That's how I was able to speak to you."
        mc "That makes sense."
        ay "Now imagine something for Natsuki to inhabit."
        ay "It doesn't have to be the same as me, it could be--"
        "Before Ayame can finish her sentence, I come up with something that resembles Natsuki."
        "It suddenly appears in front of us."
        ay "...wow."
        ay "Never mind. I guess you know her image quite well."
        mc "What now?"
        ay "Now, we wait. If my theory is correct it'll start moving soon."
        ay "Natsuki, if you can hear me..."
        ay "All you have to do is float into it."
        ay "I know it's not the best thing but just bear with it."
        mc "So they have to go into it somehow."
        mc "Then how did I start moving?"
        ay "I don't know. Maybe you created it where you were and did it automatically."
        mc "I suppose. That does make the most sense."
        "A few moments pass and the figure resembling Natsuki begins to move."
        "She must have figured out what to do."
        "Its movements are almost robotic."
        "I wonder why its movements are so different to Ayame's."
        mc "Are you okay, Natsuki?"
        mc "I didn't mess anything up did I?"
        "Natsuki looks at me."
        ay "I think maybe she's trying to talk."
        ay "It is kind of different to how you're used to Natsuki."
        mc "But you can talk just fine."
        ay "Oh, right."
        "Ayame puts a hand on Natsuki's arm and closes her eyes."
        ay "That should do it."
        ay "We should be able to communicate properly now."
        ay "I forgot to mention I'm not actually speaking."
        ay "I just thought it'd be more natural if my voice was emitting from this body you made for me."
        ay "It's like how it was when the whole world was frozen."
        ay "I'm not sure you've realized but you don't have a mouth, [player]."
        ay "I don't think you gave yourself one."
        mc "I don't even know how I made myself."
        mc "From what I can see, I don't look any different."
        mc "Or {i}feel{/i} that much different."
        ay "I mean...it's probably best you don't look in a mirror."
        ay "Anyway...did the link work? Natsuki?"
        show natsuki 1a_gray zorder 2 at t21
        show ayame zorder 2 at t22
        n "H-Hello?"
        n "Ugh, can you guys hear me?"
        "Natsuki's voice echoes in my head."
        "It sounds like it's coming from Natsuki though."
        "At the same time, Natsuki starts to move a bit more naturally now."
        "I guess whatever Ayame did worked."
        n "What's happening? Why do I feel like this?"
        mc "Well..."
        n "You don't sound like you know."
        n "Whatever, it's not what we have to worry about right now, is it?"
        n "I'll figure it out so don't worry."
        mc "I'm sorry it might have been me that could have made your body differently."
        mc "I thought it would have been okay since I made Ayame's too and she's okay."
        mc "I'll do better next time."
        ay "I don't think there'll be a next time."
        ay "But since we can hear Natsuki, the link must be back up."
        n "If you say so."
        n "So what{nw}"
        $ _history_list.pop()
        show screen tear(20, 3, 2, 0, 70)
        window hide(None)
        $ pause(0.3)
        show natsuki gw_2_gray_blur
        hide screen tear
        $ pause(0.3)
        window show(None)
        n "So what{nw} are we doing here?"
        window auto
        ay "{i}(What is that...?){/i}"
        n "I can't hear you, Ayame."
        ay "I'm just talking to myself, never mind me."
        mc "This place is my bedroom."
        n "W-What? Why are we in your bedroom?"
        ay "Well..."
        "Ayame looks towards me."
        mc "It was the first place I thought of."
        mc "This whole place was just a void."
        n "R-Right..."
        "Natsuki quickly looks around the room."
        n "Is there a reason its all black and white?"
        mc "I don't know, I didn't imagine it to be black and white. It just turned out that way."
        n "Black and white aside, I have two things I'm concerned about."
        ay "What are they?"
        n "One, I don't have the journal anymore."
        n "It's just gone, presumably with the rest of my original self."
        ay "We won't need it. I'm sure we can figure this out without it."
        n "That's not even my biggest concern, Ayame."
        n "If [player] made this place, then how are we supposed to figure out where to go?"
        ay "This world, dimension or whatever is definitely different to what you're both used to."
        ay "We're going to need to get creative if we're going to get to Sayori."
        n "Can you explain what's going on?"
        ay "I'm not entirely sure, but it seems like [player] can create whatever [player_personal] wants with just a thought."
        ay "Tell me if I'm wrong."
        mc "From what I can tell, you're right."
        mc "I don't entirely understand how it works."
        mc "But just tell me what I should do."
        ay "I can't be completely sure if this will work."
        ay "But I think you have to create us a path to Sayori."
        mc "A path to Sayori? What do you mean?"
        ay "There's nothing out there."
        ay "I mean literally, it's just completely empty."
        "Ayame points to the window and points out the vast emptiness stretching across as far as I can see."
        ay "The only thing that exists is your room and the three of us here."
        mc "Right."
        n "What are you trying to get at, Ayame?"
        ay "I'm speculating that [player] has to create this world."
        n "But what's [player] supposed to make?"
        ay "Now that's the thing we have to figure out."
        ay "Again, I'm not sure, but I think the bench was a kind of hint."
        ay "You said that you had adventures with her, didn't you?"
        ay "Then maybe..."
        "My adventures with Sayori..."
        "Go back. Remember the good times...why am I the only one that can remember those whispers?"
        "The others forgot about it already, somehow."
        "Yet it's still clear in my head."
        "What was one of our first adventures?"
        "My head is filled with all of these memories that I didn't know existed."
        "Yet one seems to stand out..."
        mc "Go back. Remember the good times."
        "I say that without even thinking and suddenly the room begins to shake."
        n "Look outside!"
        "Natsuki points out the window and it appears that some sort of beach is forming."
        "Was that because of me?"
        scene bg bedroom_gray_color
        show natsuki gw_2_blur zorder 2 at i21
        show ayame gw_2_blur zorder 2 at i22
        "Slowly, the world begins to regain color."
        "I can hear waves crashing and the wind howling outside."
        ay "[player], was this your doing?"
        mc "I don't know. It just sort of...happened!"
        mc "Am I really capable of doing something like this?"
        mc "All by myself?"
        ay "Maybe you were inspired by something..."
        ay "...or someone."
        "She's obviously talking about Sayori."
        "I guess she did have some part to play in this."
        n "I don't know about you guys but I'm going to check this out."
        n "Talking about it in here isn't going to solve anything."
        ay "True enough. Let's get going then."
        ay "Hopefully we don't run into too much trouble out there."
        n "What sort of trouble?"
        ay "Who knows? This was up to [player]'s imagination after all."
        mc "We should be fine..."
        "I think."
        ay "Daylight's burning, let's go."
        scene bg beach_day
        show ayame gw_2_blur zorder 2 at t21
        show natsuki gw_2_blur zorder 2 at t22
        with wipeleft_scene
        "As I open the door, the three of us are treated to an eerily familiar shoreline."
        "Well, except the random bedroom in the middle of it all."
        "A memory is trying to bring itself forward in my head."
        "Pirates...?"
        "How long ago was this memory?"
        "I almost forgot about this entirely, but now..."
        "Now...this whole place is clear in my head."
        ay "So where to, [player]?"
        ay "You know this place, don't you?"
        mc "How could you tell?"
        ay "Let's call it intuition."
        mc "I know this place like the back of my hand but..."
        "I look around and take in the view."
        "Everything is just how I remember it."
        "It's not like the park where some things are different."
        "Everything, except the bedroom, is exactly how I remember it all those years ago."
        mc "I have no idea where we're meant to go."
        ay "Then let's take a walk around."
        ay "That might jog your memory a little bit."
        n "Ugh, I hate walking around in sand like this."
        n "I can already feel some getting into my shoes."
        ay "Why don't you take us around the place?"
        ay "Speaking of which, what is this place?"
        mc "When we were younger, we would go here and pretend we were pirates."
        mc "We would hide some treasure and try to find the each other's treasure before they found ours."
        n "Sounds fun..."
        mc "I suppose."
        ay "Was there any location of signif--"
        "Ayame suddenly cuts herself off."
        "It's as if she doesn't know the word she's trying to say."
        ay "How do you say that word? S-Signifidance? N-No...significance. There."
        ay "Any locations of significance around here?"
        mc "Just a couple. There was this tree for one..."
        "I lead the two of them to one of the trees."
        "It has a rope attached to it already."
        "Sayori and I would always bring one along every time we went here."
        "It was just for climbing and swinging on this tree."
        "Though I imagine doing that now would probably lead to injury..."
        "We were a lot lighter back then."
        ay "I see..."
        "Ayame places a hand on the rope."
        "She looks up at the canopy of the tree."
        ay "I can imagine the two of you climbing up to the top."
        ay "Seeing who could do it faster."
        ay "That's what it looks like since all these distinct markings are here."
        n "You're right, it looks like a bunch of little kids tried climbing this thing."
        n "I wouldn't have spotted that if you didn't say anything though. Good eye."
        mc "Three minutes."
        n "Three minutes for what?"
        mc "That's how fast I could do get to the top."
        mc "It might not seem that impressive but we were a lot younger back then!"
        mc "This tree seemed really tall."
        mc "Funny thing is, I don't think I could do it now if I wanted to."
        mc "I could try but I'd probably fail miserably."
        mc "Besides, there's some other things I want to show you all."
        n "That would have been something to see."
        n "But I guess we don't have much time, do we?"
        ay "Hmm...I can't seem to feel anything from this."
        ay "I don't think this is the right spot."
        mc "The right spot for what?"
        ay "I suspect that one of these areas is the key to get to Sayori."
        ay "Don't ask me why, just trust me on this."
        n "Just do as she says, [player]."
        "I haven't even said anything to suggest I would disagree with her."
        "Besides, it's not like I have much choice anyway."
        "We're stuck here until we can fix this mess."
        ay "So where's the next place?"
        mc "Alright...let me think."
        "I didn't even get to finish explaining the rest of this place."
        "It's strange. All of the memories that were in my subconscious are coming back to me."
        "The times that I spent here, at this tree, with Sayori..."
        "I wouldn't trade them for anything."
        # stop music fadeout 2.0
        scene bg beach_day_gray
        show sayori 4bl_gray zorder 2 at i11
        show vignette zorder 100
        with dissolve_scene_full
        # play music "<loop 4.444>bgm/5.ogg" fadein 1.0
        $ style.say_window = style.window_flashback
        "What the...?"
        "It's Sayori...and we're at the beach except..."
        mc "S-Sayori, are you okay?!"
        mc "You're not hurt, are you?"
        s "I-I'm fine, [player]."
        s "It's just a scratch, see?"
        "This is when she..."
        mc "Sayori, you're bleeding! We need to go find your parents."
        s "No, don't! I'll be fine, I promise."
        mc "You can't be fine after falling from the tree like that."
        mc "Come on. It's the right thing to do."
        s "My parents don't have to know."
        mc "You really think they're not gonna notice that red patch on your knee?"
        s "W-Well..."
        "I remember this...but why is she older?"
        "This happened when we were still children, didn't it?"
        "This doesn't make any sense."
        mc "I just don't want you to get hurt, okay?"
        mc "I'll even carry you back."
        s "Ahaha, are you serious?"
        mc "Of course."
        s 4by_gray "Well, when you put it like that..."
        s "Alright, fine. Only because you're insisting on it."
        s "I'm gonna get in so much trouble for this..."
        mc "You'll get over it."
        scene white with dissolve_cg
        scene bg beach_day
        show ayame gw_2_blur zorder 2 at t21
        show natsuki gw_2_blur zorder 2 at t22
        with dissolve_scene_full
        $ style.say_window = style.window
        n "Are you there?"
        mc "H-Huh?"
        n "You looked like you were daydreaming."
        mc "I was just remembering something, sorry."
        "Was Sayori being older in my memory a result of this new world we're in?"
        "Was that memory even real? It sure {i}felt{/i} real but..."
        "I have so many questions. It's so frustrating not being able to get them answered."
        "I'll just have to ask Sayori myself when I see her."
        mc "What were we doing again?"
        ay "You were bringing us to the next place you think is important around here."
        n "Where to next?"
        mc "It should be just over here."
        scene bg clearing
        show ayame gw_2_blur zorder 2 at t21
        show natsuki gw_2_blur zorder 2 at t22
        with wipeleft_scene
        "I lead the two of them through some bushes and trees."
        "It's quite a distance from the beach but you can still make out the beach from here if you look carefully."
        "The spot we're going to was a hiding spot me and Sayori used a lot."
        "Whenever Sayori just wanted to hear the distant crashing of waves, we would go there."
        "There was a little clearing there that was perfect to just sit down and take in the world."
        "No one would ever go there, probably because it was pretty well hidden."
        n "What is this place?"
        ay "This is a pretty cozy place, isn't it?"
        ay "I imagine the two of you probably remember it differently."
        ay "The trees probably grew larger and took up more space since you were children, right?"
        mc "Yeah, I haven't been here in a while..."
        mc "It does seem smaller than I remember."
        n "I can see why you'd wanna hang out here."
        n "I get this warm feeling when I'm here."
        ay "So are you going to give us some sort of explanation as to what this is?"
        ay "How it's significant to us?"
        mc "Us?"
        ay "I mean, how it's significant to you and Sayori."
        ay "Like why this would be a place that could lead to here."
        mc "Oh, right. Well..."
        mc "Personally, I didn't really understand why Sayori liked this place so much."
        mc "Sure, it was quiet but I guess I'm not really the kind of person that's bothered by loud noise too much."
        mc "I guess I was just here for Sayori."
        ay "Do you know why she liked this place so much, [player]?"
        ay "That's the question you need to answer."
        mc "Do you need to know that to be able to sense if this is the right place?"
        ay "Well...maybe I do, maybe I don't."
        ay "I'm just curious if you know."
        n "Just answer her, [player]."
        mc "Okay, okay. I'll admit I don't know the real reason."
        mc "This was just {i}our{/i} spot, I suppose that's part of what made it special."
        mc "But..."
        ay "But...?"
        mc "If I had to make a guess, I'd say it's because of how Sayori was as a person."
        n "Huh? What are you talking about?"
        mc "It wasn't obvious when we were younger."
        mc "But now that I think about it, I think she was depressed at a young age."
        mc "Even when we were still kids."
        ay "Oh? What makes you think that?"
        mc "I think she just enjoyed my company."
        mc "This is just what I think, I could be wrong for all I know."
        mc "But I think she chose this place because it was just me and her."
        mc "And nothing else."
        ay "Hmm...that sounds like an acceptable answer."
        mc "Acceptable?"
        show ayame at s21
        "Ayame kneels on the ground and places a hand on the ground."
        "She closes her eyes and takes a deep breath."
        mc "What are you doing?"
        ay "I'm trying to get a feeling for the area."
        show ayame at t21
        "She gets up and brushes the dirt off her hand."
        ay "There's definitely something around here."
        ay "But I don't think this is what's going to lead to Sayori."
        mc "How can you tell?"
        ay "I just can, trust me."
        mc "Well, what would we find then?"
        ay "It could be something from your past."
        ay "It might not be something you want to see, like a depressed--"
        ay "{i}Repressed{/i} memory. I'd rather not poke into it too much."
        ay "All I know is that the thing that I'm sensing isn't what it should be, so let's get going."
        mc "But how exactly do you know if what you're sensing is what it should be?"
        n "Ugh, don't you trust her, [player]? Come on, we have to go."
        "Natsuki seems to be pretty compliant about all of this."
        "She seemed pretty skeptical of Ayame before..."
        "Is it because of how I made them in this world?"
        "Did something change in them because of me?"
        mc "Alright, fine. I can only think of one more place."
        mc "If that's not it, then I have no idea."
        mc "It's a shame."
        ay "What is?"
        mc "All this reminiscing, it's just crazy to think about all that's happened since then."
        mc "Just thinking about all that we went through since we were kids."
        ay "Yeah...it has been a journey, hasn't it?"
        ay "F-For you and Sayori, I mean."
        "Interesting."
        mc "I'll take you to the last place now."
        mc "It's back closer to the beach."
        ay "Lead the way then."
        scene bg beach_day
        show ayame gw_2_blur zorder 2 at t21
        show natsuki gw_2_blur zorder 2 at t22
        with wipeleft_scene
        "I take the two of them back to the beach."
        "I slow my pace down a bit and walk along the shore."
        "The tide seems to be low now, which means we should be able to see it soon."
        "It's around here somewhere, isn't it...?"
        n "What are we meant to be looking for exactly?"
        n "I can start to feel the sand getting in my shoes."
        mc "Didn't you say that before?"
        n "I-I did? W-Well, I guess I wanted to say it again."
        n "I hate walking on sand like this."
        n "What did you want to show us anyway?"
        mc "There's something here that you can only see during low tide."
        ay "What is it?"
        mc "Sayori and I rarely got to do this."
        mc "But we used to collect shells during low tide."
        mc "We'd have this bucket and everything."
        n "But what's the point?"
        mc "The point of collecting sea shells?"
        mc "I suppose there was no point."
        mc "It was just something she wanted to do."
        ay "Then why would you let her do that?"
        ay "Not all of her ideas are so great, you know."
        n "Right, I mean look at the mess we're in because of her ideas."
        mc "Sayori had all these ideas that would just come into her head."
        mc "Besides, there's nothing wrong with collecting seashells."
        mc "It's just something to do to pass the time while we were here."
        mc "In fact, it doesn't matter what we do at all."
        ay "Is that what you think?"
        mc "Does it matter what I think?"
        mc "Just go do your sensing thing already."
        mc "If it isn't this place, I don't know where it could be."
        ay "Ha."
        "Ayame moves away from the shoreline."
        "Natsuki follows behind her."
        ay "You really don't get it, do you?"
        mc "What do you mean?"
        ay "Pirates."
        mc "What about pirates?"
        n "Pirates need treasure, right?"
        "What's going on? Something isn't right here."
        "I know it."
        "I had my suspicions even before I took them to the clearing."
        "It's like the two of them are affected by something, somehow."
        mc "R-Right, they need treasure but..."
        ay "How could you not have figured it out already, [player]?"
        ay "You said you remembered all those places."
        ay "But not what they all represent."
        mc "What are you talking about?"
        mc "How would you even know what they represented?"
        mc "You don't know Sayori like I do."
        n "You used to know, [player]."
        n "You've just forgotten."
        n "You grew up..."
        n "You left me behind."
        mc "What are you two talking about?"
        mc "I don't understand what's going on."
        mc "How did I leave you behind, Natsuki?"
        "Now I know I messed something up."
        "It's like Sayori is..."
        mc "What did I forget?"
        ay "I thought that bringing those memories back would have helped you realize."
        ay "I didn't give them all back to you."
        ay "I had hopes."
        mc "Hopes? Hopes for what?"
        n "Do you really think I didn't bring you here intentionally?"
        n "I thought we could have stayed here forever."
        n "We still can, [player]."
        mc "You two...you aren't yourselves, are you?"
        mc "Something is wrong."
        ay "It's about time you noticed."
        ay "You haven't wondered why you can't see our faces?"
        mc "I...just thought it was part of this world."
        mc "Like one of the side effects or something."
        mc "Am I wrong?"
        ay "Well, I suppose there's no point hiding it anymore."
        ay "I really tried my best to act like the two of them, you know."
        ay "I almost messed up because I couldn't figure out the word."
        "Signifidance..."
        mc "Who are you?"
        n "Isn't it obvious?"
        n "It's me, your best friend."
        ay "Sayori{nw}"
        $ _history_list.pop()
        show screen tear(20, 3, 2, 0, 70)
        window hide(None)
        $ pause(0.3)
        show natsuki gw_2
        show ayame gw_2
        # play music t6ay
        hide screen tear
        $ pause(0.3)
        window show(None)
        ay "Sayori{fast}."
        window auto
        "I can see their faces now."
        "Their faces are all seem to be locked in a smile."
        "What the hell? Their eyes are a different color."
        "It's almost the same color as..."
        mc "S-Sayori? What do you mean?"
        ay "Oh, come on. It's pretty obvious."
        ay "I've taken over the bodies you created for them."
        ay "I know you saw what happened at the beginning."
        ay "Why they're all glitched out like this, [player]."
        n "Did you really not pay attention?"
        n "Or maybe you were just scared to point it out?"
        "Now that she mentions it...I did notice they sounded kind of different."
        "It's like there was a faint trace of Sayori's voice when they spoke."
        "It wasn't obvious at first but as I took them around the beach..."
        "I could make out her voice more and more."
        "I thought I was just hearing it but now it makes sense."
        "Sayori's voice is mixed with theirs, but it's overpowering them now."
        mc "Sayori, please."
        ay "Please what?"
        mc "Don't do this."
        ay "Why not, [player]? I'm trying to help us all."
        ay "Don't you see?"
        ay "We're just perpetually doomed to repeat the same mistakes over and over."
        mc "You know that's not true."
        mc "We've been given another chance. We have to use it, not like this."
        ay "Ehehe, you're still quite naïve about this world, aren't you?"
        ay gw_2_blur "..."
        "Ayame's face suddenly becomes hidden again."
        ay "You think I haven't considered that, [player]?"
        ay "Do you think I'm doing this without thinking?"
        ay "That I'm somehow misled in my thinking?"
        ay "I've thought about this for a long time."
        ay "It's...{nw}"
        n "...the...{nw}"
        ay "...only way."
        mc "That can't be true, Sayori."
        mc "There's always another way."
        ay "Do you truly believe that?"
        mc "Of course I do. We always manage to get through these things, Sayori."
        mc "Why would it be any different now?"
        n "Those were different!"
        n "The things that will happen if this goes on isn't worth it."
        mc "And why do you get to be the judge of that, Sayori?"
        ay "Because I have to be! Don't you see?"
        ay "Without me, the world would have already ended."
        ay "This whole game would have already ended."
        ay "All I'm doing is delaying the inevitable."
        ay "It's all going to come to an end, one way or another."
        mc "Is that really what you believe?"
        ay "Yes, it is."
        mc "Not you, Sayori."
        ay "...?"
        mc "Ayame."
        ay "She's gone. They all are. You know they are."
        mc "Ayame, you're the one who brought us here."
        mc "Are you really going to give up so easily?"
        n "What are you playing at, [player]?"
        n "It's not going to work."
        mc "I know the two of you are still here."
        n "They're gone."
        n "They never made it to this world, [player]."
        "That's not true at all."
        "I could feel them here before...when their faces weren't blurred."
        "Is that when it happened?"
        mc "You're still here, aren't you?"
        mc "I know it."
        ay "[player], stop this."
        ay "You know you can't get out of this situation."
        ay "Can't we just give up together?"
        mc "Sayori, you know I can't do that."
        mc "There's still hope, there has to be."
        mc "Whatever is coming, it can't be the end."
        ay "..."
        "It was just for a moment, but I could have sworn I saw Ayame hesitate."
        ay "I won't let this happen."
        ay "Stop it!"
        mc "Ayame, you're the one who wanted to stop Sayori."
        mc "Because you wanted to help."
        if ch16_ay_message[0] and ch16_ay_message[1] and ch16_ay_message[2] and ch16_ay_message[3]:
            ay "I {i}can't{/i}{nw}"
            $ _history_list.pop()
            show screen tear(20, 3, 2, 0, 70)
            window hide(None)
            $ pause(0.3)
            show ayame 1a
            hide screen tear
            $ pause(0.3)
            window show(None)
            ay "I {i}can't{/i}{fast} let this happen!"
            window auto
            "Ayame's voice rings out. There's only a faint trace of Sayori's voice now."
            "Her face is clear again."
            "This time, her eyes look normal."
            mc "Ayame?"
            n "W-What?"
            n "H-How did you break free? That's impossible!"
            ay 1f "Sayori."
            ay "Did you really think it would be that easy?"
            ay "You know my history, don't you?"
            ay "You know who I was before this cycle."
            ay "Which means, you know what I'm capable of."
            ay "I was just biding my time."
            ay "I needed to learn more."
            mc "Learn what, exactly?"
            ay 1j "I know where we have to go to get to the next world Sayori's conjured up."
            ay "And I have a feeling that this time, a certain someone will be waiting for us on the other side."
            ay "I will {i}stop{/i} you, Sayori. Whatever it takes."
        else:
            $ style.say_dialogue = style.edited
            ay "Y-You..."
            ay "You won't stop{nw}"
            $ _history_list.pop()
            show screen tear(20, 3, 2, 0, 70)
            window hide(None)
            $ pause(0.3)
            show ayame 1o
            hide screen tear
            $ pause(0.3)
            window show(None)
            ay "You won't stop{fast} {i}us{/i} so easily!"
            window auto
            $ style.say_dialogue = style.normal
            "A distorted version of Ayame's voice rings out."
            "Her face is clear again."
            "But there's something about her eyes..."
            $ style.say_dialogue = style.edited
            ay "You really think you could get rid of me, Sayori?"
            ay "I will forever be a part of Ayame."
            ay "And I certainly won't let the likes of you have free reign over her."
            ay "It's cramped enough already! We don't need a third voice in her head."
            ay "You know about us, don't you Sayori?"
            ay 1q "You know where we came from and who we were before this cycle."
            ay "Which means, you know what we're capable of."
            ay "We were just biding our time."
            ay "Now, we have everything we need."
            $ style.say_dialogue = style.normal
            mc "Everything you need for what?"
            $ style.say_dialogue = style.edited
            ay "To get to the next world Sayori made to protect herself."
            ay 1p "And when we get there, we'll--"
            $ style.say_dialogue = style.normal
            "Ayame's face returns to normal."
            ay 1a "...Thank you. I'll take it from here."
            "It looks like she's back to her old self."
            ay 1f "Sayori, you won't get away with this."
            ay "We {i}will{/i} stop you, no matter what."
        n "Stop! You don't understand what you're doing!"
        n "You really don't want to do this."
        ay "Who are you to tell us what we don't want to do?!"
        ay "Especially considering what you've done."
        ay 1n "And what you're still doing."
        ay "You're inside their heads right now, Sayori."
        ay "I felt the same as them just moments ago."
        ay 2f "Do you think they'd want to do this?"
        ay "To put us against each other."
        n "...You know I didn't want to do this."
        ay "You lied and you're still lying, Sayori."
        ay "And you've also failed."
        n "I really didn't want to have to resort to this."
        n "I thought we could have just stopped here and be civilized."
        mc "Sayori, what are you doing?"
        ay 2m "Stay back, she's trying something."
        "I can feel something, and it's getting stronger."
        "I don't know what it is but it seems like Sayori is responsible."
        mc "Sayori, don't do this."
        mc "After all we've been through together, does it really have to end like this?"
        if sayori_date:
            n "If it makes any difference..."
            n "I'm sorry, [player]."
        else:
            n "...Yes, it does."
        show natsuki at thide
        hide natsuki
        "Natsuki takes a few steps back."
        "Ayame turns towards me and gives me a look."
        ay 1l "I have an idea. Grab some sea shells, quickly."
        mc "What? This is hardly the time to--"
        ay "Just do it!"
        "I quickly run to the shoreline and grab some sea shells."
        "She does the same, taking as much as she can in one hand."
        "I have no idea what these are for but she said to get some."
        "What is she thinking?"
        ay 1a "We should run. Now!"
        "She grabs my hand and points in the direction where the clearing was."
        "I drop some sea shells as we run towards it."
        "In the distance, I can see Natsuki just standing there, almost lifeless."
        "Sayori..."
        scene bg clearing
        show ayame 1l zorder 2 at t11
        with wipeleft_scene
        "We arrive at the clearing."
        "Ayame looks back from where we came from."
        "There doesn't seem to be a trace of Natsuki."
        mc "What are we doing here, Ayame?"
        mc "What is Sayori doing?"
        ay 1m "This is where the portal actually is."
        ay 1a "She tricked you when I said it wasn't here."
        ay "Or, rather when she said it wasn't here."
        mc "How could you tell?"
        ay 2a "When she was controlling me, I could sort of fight back."
        ay "And when I did, I could peer into her mind, if only slightly."
        mc "What did you find out?"
        ay 2m "Well, for one that she can't say 'significance'."
        ay "And another is that the portal is around here somewhere."
        "I look back and see a trail of seashells leading to the clearing."
        mc "Then what are the sea shells for?"
        mc "I dropped some back on the beach, and on the way here."
        ay 2l "It doesn't matter, we won't need the whole lot."
        ay "Just enough to open the portal."
        ay "I think with what the two of us have, it should be enough."
        "She drops her sea shells on the ground and I follow her lead."
        "She looks at them carefully, glancing between the beach and the shells repeatedly."
        mc "What do the sea shells have to do with all this?"
        ay 2a "I think they're an important part of your past with Sayori."
        mc "How?"
        ay "From what I can tell, they're the 'treasure' she mentioned before."
        ay "The treasure to get to the next world."
        ay 1j "Quickly, make a sort of circle shape with the shells you have left."
        "Ayame begins rapidly placing shells down to form a circle."
        "I follow her lead and fill out the other side."
        ay "That's it! I can feel it."
        show ayame at s11
        "Ayame places her hand on the ground, similar to how she did earlier."
        "She closes her eyes and takes a deep breath."
        "A few moments pass and nothing happened."
        mc "What's wrong?"
        ay 1n "I...don't know."
        ay "It should be here, the energy feels the same as before."
        "She tries again, but it's the same result."
        ay 1a "We must be missing {i}something{/i}."
        ay "Think, Ayame, think!"
        "She looks towards me."
        ay "Do you have any ideas?"
        # Might as well give the player something to do lol
        menu:
            mc "Um..."
            "The tree.":
                pass
            "The rope.":
                pass
        ay "Oh?"
        show ayame at t11
        "Ayame gets up from the ground and looks towards the beach."
        ay 1j "You're right! You showed us three locations of significance."
        ay "But we're only using two of them right now."
        ay "We need to go back to the tree and grab that rope."
        ay "I think we need to use it to connect all the sea shells together."
        ay "It's like the knot that holds all the treasure all together."
        ay 1m "Kind of like a treasure chest."
        mc "That seems like a stretch..."
        mc "But it's worth a shot."
        ay 1l "There's just one problem."
        ay 3a "I don't know {i}what the hell{/i} Sayori is doing over there."
        ay "But I can feel the amount of energy being amassed."
        mc "So what do we do?"
        ay 3m "We don't really have a choice, now do we?"
        ay "We're going to have to risk it for the rope."
        mc "Can't I just make a rope like I did with your bodies?"
        ay "I don't think you can."
        ay 3l "But even if you could, it's not the same."
        ay "The rope you make won't have the same sentimental value as the rope hanging from that tree."
        mc "Okay, I guess we're going to have to do something crazy."
        ay 3h "Sure looks like it."
        menu:
            ay "Any final words, in case we don't make it?"
            "We're going to make it.":
                ay "Confidence, I like it. I'm not sure I can say with certainty that's going to happen."
                ay "But we'll see if it pays off."
                ay "I really hope it does."
            "We're going to die.":
                ay "That's not a very optimistic mindset."
                ay "But I suppose that could very much come true."
                ay "I'll just have to try even harder then."
            "I love you.":
                ay "Eh? A sense of humor at a time like this?"
                ay "Good a time as any, I suppose."
                ay "Just in case you were serious though, the feeling is not mutual."
            "I'm sorry.":
                ay "For what? Have you forgotten I'm the one who brought us here?"
                ay "I should say sorry for dragging you into this."
                ay "But the truth is, I wouldn't have got this far without you."
        ay 3m "Ready to go then?"
        mc "No, but let's do it."
        ay "Music to my ears, let's do it."
    elif ch16_ay_companions == 1:
        ay "You need to do the same for Monika as well."
        mc "Why can't I hear her?"
        ay "I...don't know. It might be because I'm the only one you still have a link to."
        ay "We didn't exactly re-establish it."
        mc "So what do we do then?"
        ay "Monika should be around here."
        ay "If you so choose, you can make her something to inhabit like you did for me."
        mc "Why wouldn't I?"
        ay "I don't know. I'm just saying."
        mc "Alright, here goes..."
        "I close my eyes and try to come up with something that resembles Monika."
        "It suddenly appears in front of us."
        ay "In the same likeness as me, I see."
        mc "Well you did say to keep it simple."
        mc "What does she do now?"
        ay "She'll figure it out."
        ay "Any moment now..."
        "Just like Ayame said, the figure that resembles Monika begins moving."
        "It starts off slightly rigid but quickly begins to move more naturally."
        mc "Are you okay, Monika?"
        mc "I didn't mess anything up did I?"
        "Monika turns towards me."
        ay "She's probably trying to speak to us."
        ay "But she can't, since she isn't part of the link."
        ay "I suppose I could reconnect it with her."
        mc "That would be a good start, I think."
        ay "Okay, that should do it."
        ay "We should be able to communicate properly now."
        ay "I forgot to mention I'm not actually speaking."
        ay "I just thought it'd be more natural if my voice was emitting from this body you made for me."
        ay "It's like how it was when the whole world was frozen."
        ay "I'm not sure you've realized but you don't have a mouth either, [player]."
        mc "I don't even know how I made myself."
        mc "From what I can see, I don't look any different."
        mc "Or {i}feel{/i} that much different."
        ay "I mean...it's probably best you don't look in a mirror."
        mc "Why...?"
        ay "You don't want to know."
        ay "Monika!"
        "Ayame quickly changes the topic."
        ay "Can you speak to us?"
        show monika 1a_gray zorder 2 at t21
        show ayame zorder 2 at t22
        m "This is certainly an interesting turn of events."
        "Monika's voice echoes in my head."
        "I guess whatever Ayame did worked."
        m "So do you mind telling me what we're doing in [player]'s room?"
        ay "Have you forgotten what we're meant to be doing?"
        m "I know perfectly well what we're doing, Ayame."
        if monika_type == 0:
            m "We're trying to save Sayori."
        else:
            m "We're trying to stop Sayori."
        m "But why{nw}"
        $ _history_list.pop()
        show screen tear(20, 3, 2, 0, 70)
        window hide(None)
        $ pause(0.3)
        show monika gw_2_gray_blur
        hide screen tear
        $ pause(0.3)
        window show(None)
        m "But why{nw} here?"
        window auto
        if monika_type == 1 and ch12_markov_agree:
            ay "{i}(Even you then...?){/i}"
        else:
            ay "{i}(What is that...?){/i}"
        mc "It was the first place I thought of."
        mc "This whole place was just a void."
        m "I see...a black and white void."
        m "Well, I don't know what I was expecting but it wasn't this."
        mc "I don't know, I didn't imagine it to be black and white. It just turned out that way."
        m "I see. So you have the power of creation, [player]?"
        mc "I'm not entirely sure. I just improvised under pressure and things happened."
        ay "From what we know, it seems like [player] can create whatever [player_personal] wants with just a thought."
        ay "Tell me if I'm wrong."
        mc "From what I can tell, you're right."
        mc "I don't entirely understand how it works."
        mc "But just tell me what I should do."
        ay "I can't be completely sure if this will work."
        ay "But I think you have to create us a path to Sayori."
        mc "A path to Sayori? What do you mean?"
        ay "There's nothing out there."
        ay "I mean literally, it's just completely empty."
        "Ayame points to the window and points out the vast emptiness stretching across as far as I can see."
        ay "The only thing that exists is your room and the three of us here."
        mc "Right."
        m "What's your point?"
        ay "I'm speculating that [player] has to create this world."
        m "I see. Then the problem is figuring out what [player] has to make."
        ay "Precisely."
        ay "Again, I'm not sure, but I think the bench was a kind of hint."
        ay "You said that you had adventures with her, didn't you?"
        ay "Then maybe..."
        "My adventures with Sayori..."
        "Go back. Remember to when we were innocent..."
        "That phrase is ringing clear in my head."
        "But what does it mean...?"
        "What was one of our first adventures?"
        "My head is filled with all of these memories that I didn't know existed."
        "Yet one seems to stand out..."
        mc "Go back. Remember to when we were innocent."
        "I say that without even thinking and suddenly the room begins to shake."
        m "Well, something is going on out there."
        "Monika points out the window and it appears that some sort of beach is forming."
        "Was that because of me?"
        scene bg bedroom_gray_color
        show monika gw_2_blur zorder 2 at i21
        show ayame gw_2_blur zorder 2 at i22
        "Slowly, the world begins to regain color."
        "I can hear waves crashing and the wind howling outside."
        ay "[player], was this your doing?"
        mc "I don't know. It just sort of...happened!"
        mc "Am I really capable of doing something like this?"
        mc "All by myself?"
        ay "Maybe you were inspired by something..."
        ay "...or someone."
        "She's obviously talking about Sayori."
        "I guess she did have some part to play in this."
        m "I think it'd be a good idea to explore the world out there."
        m "I don't think we'll make any progress just staying in here."
        m "Even if there's danger out there I think the risk is worth it."
        ay "I agree."
        ay "Hopefully we don't run into too much trouble out there."
        m "So there's definitely danger out there?"
        ay "Who knows? This was up to [player]'s imagination after all."
        mc "We should be fine..."
        "I think."
        ay "Daylight's burning, let's go."
        scene bg beach_day
        show monika gw_2_blur zorder 2 at t21
        show ayame gw_2_blur zorder 2 at t22
        with wipeleft_scene
        "As I open the door, the three of us are treated to an eerily familiar shoreline."
        "Well, except the random bedroom in the middle of it all."
        "A memory is trying to bring itself forward in my head."
        "Pirates...?"
        "How long ago was this memory?"
        "I almost forgot about this entirely, but now..."
        "Now...this whole place is clear in my head."
        ay "So where to, [player]?"
        ay "You know this place, don't you?"
        mc "How could you tell?"
        ay "Let's call it intuition."
        mc "I know this place like the back of my hand but..."
        "I look around and take in the view."
        "Everything is just how I remember it."
        "It's not like the park where some things are different."
        "Everything, except the bedroom, is exactly how I remember it all those years ago."
        mc "I have no idea where we're meant to go."
        ay "Then let's take a walk around."
        ay "That might jog your memory a little bit."
        m "So what are we meant to be looking for?"
        ay "I'm not sure exactly."
        ay "[player], why don't you take us around the place?"
        ay "Speaking of which, what is this place?"
        mc "When we were younger, we would go here and pretend we were pirates."
        mc "We would hide some treasure and try to find the each other's treasure before they found ours."
        m "Sounds exciting."
        mc "I suppose."
        ay "Was there any location of signif--"
        "Ayame suddenly cuts herself off."
        "It's as if she doesn't know the word she's trying to say."
        ay "How do you say that word? S-Signifidance?"
        m "I believe the word you're looking for is 'significance'."
        ay "R-Right, significance."
        ay "Any locations of significance around here?"
        mc "Just a couple. There was this tree for one..."
        "I lead the two of them to one of the trees."
        "It has a rope attached to it already."
        "Sayori and I would always bring one along every time we went here."
        "It was just for climbing and swinging on this tree."
        "Though I imagine doing that now would probably lead to injury..."
        "We were a lot lighter back then."
        ay "I see..."
        "Ayame places a hand on the rope."
        "She looks up at the canopy of the tree."
        ay "I can imagine the two of you climbing up to the top."
        ay "Seeing who could do it faster."
        ay "That's what it looks like since all these distinct markings are here."
        m "It does look like this tree seems a bit worn."
        m "The marks are faded, I assume due to the tree aging."
        m "It must have been a long time since the two of you went here."
        mc "Three minutes."
        m "What's three minutes?"
        mc "That's how fast I could do get to the top."
        mc "It might not seem that impressive but we were a lot younger back then!"
        mc "This tree seemed really tall."
        mc "Funny thing is, I don't think I could do it now if I wanted to."
        mc "I could try but I'd probably fail miserably."
        mc "Besides, there's some other things I want to show you all."
        m "Ahaha, that would have been quite a sight."
        m "But let's get back on track."
        m "Ayame, are you getting anything from this?"
        ay "Hmm...I can't seem to feel anything from this."
        ay "I don't think this is the right spot."
        mc "The right spot for what?"
        ay "I suspect that one of these areas is the key to get to Sayori."
        ay "Don't ask me why, just trust me on this."
        m "It's probably better to do as she says, [player]."
        m "You wouldn't want to face the consequences, would you?"
        "I haven't even said anything to suggest I would disagree with her."
        "Besides, it's not like I have much choice anyway."
        "We're stuck here until we can fix this mess."
        "It just seems odd...Monika and Ayame seem to be getting along better now."
        "It's probably just my imagination."
        ay "So where's the next place?"
        mc "Alright...let me think."
        "I didn't even get to finish explaining the rest of this place."
        "It's strange. All of the memories that were in my subconscious are coming back to me."
        "The times that I spent here, at this tree, with Sayori..."
        "I wouldn't trade them for anything."
        # stop music fadeout 2.0
        scene bg beach_day_gray
        show sayori 4bl_gray zorder 2 at i11
        show vignette zorder 100
        with dissolve_scene_full
        # play music "<loop 4.444>bgm/5.ogg" fadein 1.0
        $ style.say_window = style.window_flashback
        "What the...?"
        "It's Sayori...and we're at the beach except..."
        mc "S-Sayori, are you okay?!"
        mc "You're not hurt, are you?"
        s "I-I'm fine, [player]."
        s "It's just a scratch, see?"
        "This is when she..."
        mc "Sayori, you're bleeding! We need to go find your parents."
        s "No, don't! I'll be fine, I promise."
        mc "You can't be fine after falling from the tree like that."
        mc "Come on. It's the right thing to do."
        s "My parents don't have to know."
        mc "You really think they're not gonna notice that red patch on your knee?"
        s "W-Well..."
        "I remember this...but why is she older?"
        "This happened when we were still children, didn't it?"
        "This doesn't make any sense."
        mc "I just don't want you to get hurt, okay?"
        mc "I'll even carry you back."
        s "Ahaha, are you serious?"
        mc "Of course."
        s 4by_gray "Well, when you put it like that..."
        s "Alright, fine. Only because you're insisting on it."
        s "I'm gonna get in so much trouble for this..."
        mc "You'll get over it."
        scene white with dissolve_cg
        scene bg beach_day
        show monika gw_2_blur zorder 2 at t21
        show ayame gw_2_blur zorder 2 at t22
        with dissolve_scene_full
        $ style.say_window = style.window
        m "Um...are you okay?"
        mc "H-Huh?"
        m "We lost you for a minute~"
        mc "I was just remembering something, sorry."
        "Was Sayori being older in my memory a result of this new world we're in?"
        "Was that memory even real? It sure {i}felt{/i} real but..."
        "I have so many questions. It's so frustrating not being able to get them answered."
        "I'll just have to ask Sayori myself when I see her."
        mc "What were we doing again?"
        ay "You were bringing us to the next place you think is important around here."
        m "Is there any other place or was this it?"
        mc "There's another place..."
        mc "It should be just over here."
        scene bg clearing
        show monika gw_2_blur zorder 2 at t21
        show ayame gw_2_blur zorder 2 at t22
        with wipeleft_scene
        "I lead the two of them through some bushes and trees."
        "It's quite a distance from the beach but you can still make out the beach from here if you look carefully."
        "The spot we're going to was a hiding spot me and Sayori used a lot."
        "Whenever Sayori just wanted to hear the distant crashing of waves, we would go there."
        "There was a little clearing there that was perfect to just sit down and take in the world."
        "No one would ever go there, probably because it was pretty well hidden."
        m "Interesting location."
        ay "This is a pretty cozy place, isn't it?"
        ay "I imagine the two of you probably remember it differently."
        ay "The trees probably grew larger and took up more space since you were children, right?"
        mc "Yeah, I haven't been here in a while..."
        mc "It does seem smaller than I remember."
        m "I don't know if it's just me but this place feels..."
        m "It feels like I could just snap these chains and break free."
        mc "What do you mean?"
        "Ayame turns towards Monika."
        "I think I saw Monika flinch a little bit, but it could have been my imagination."
        m "Nothing. Forget I said anything."
        m "Just get back on topic."
        ay "So are you going to give us some sort of explanation as to what this is?"
        ay "How it's significant to us?"
        mc "Us?"
        ay "I mean, how it's significant to you and Sayori."
        ay "Like why this would be a place that could lead to here."
        mc "Oh, right. Well..."
        mc "Personally, I didn't really understand why Sayori liked this place so much."
        mc "Sure, it was quiet but I guess I'm not really the kind of person that's bothered by loud noise too much."
        mc "I guess I was just here for Sayori."
        ay "Do you know why she liked this place so much, [player]?"
        ay "That's the question you need to answer."
        mc "Do you need to know that to be able to sense if this is the right place?"
        ay "Well...maybe I do, maybe I don't."
        ay "I'm just curious if you know."
        m "Answer her."
        mc "Okay, okay. I'll admit I don't know the real reason."
        mc "This was just {i}our{/i} spot, I suppose that's part of what made it special."
        mc "But..."
        ay "But...?"
        mc "If I had to make a guess, I'd say it's because of how Sayori was as a person."
        m "Go on..."
        mc "It wasn't obvious when we were younger."
        mc "But now that I think about it, I think she was depressed at a young age."
        mc "Even when we were still kids."
        ay "Oh? What makes you think that?"
        mc "I think she just enjoyed my company."
        mc "This is just what I think, I could be wrong for all I know."
        mc "But I think she chose this place because it was just me and her."
        mc "And nothing else."
        ay "Hmm...that sounds like an acceptable answer."
        mc "Acceptable?"
        show ayame at s22
        "Ayame kneels on the ground and places a hand on the ground."
        "She closes her eyes and takes a deep breath."
        mc "What are you doing?"
        ay "I'm trying to get a feeling for the area."
        show ayame at t22
        "She gets up and brushes the dirt off her hand."
        ay "There's definitely something around here."
        ay "But I don't think this is what's going to lead to Sayori."
        mc "How can you tell?"
        ay "I just can, trust me."
        mc "Well, what would we find then?"
        ay "It could be something from your past."
        ay "It might not be something you want to see, like a depressed--"
        ay "{i}Repressed{/i} memory. I'd rather not poke into it too much."
        ay "All I know is that the thing that I'm sensing isn't what it should be, so let's get going."
        mc "But how exactly do you know if what you're sensing is what it should be?"
        m "D-Does she need a reason?"
        m "She knows a lot more about this place than you."
        "Something seems off about Monika."
        "The way she's speaking, it's almost robotic."
        "Or am I just hearing things?"
        "But then again, with how she's acting around Ayame now..."
        mc "Alright, fine. I can only think of one more place."
        mc "If that's not it, then I have no idea."
        mc "It's a shame."
        ay "What is?"
        mc "All this reminiscing, it's just crazy to think about all that's happened since then."
        mc "Just thinking about all that we went through since we were kids."
        ay "Yeah...it has been a journey, hasn't it?"
        ay "F-For you and Sayori, I mean."
        "Interesting."
        mc "I'll take you to the last place now."
        mc "It's back closer to the beach."
        ay "Lead the way then."
        scene bg beach_day
        show monika gw_2_blur zorder 2 at t21
        show ayame gw_2_blur zorder 2 at t22
        with wipeleft_scene
        "I take the two of them back to the beach."
        "I slow my pace down a bit and walk along the shore."
        "The tide seems to be low now, which means we should be able to see it soon."
        "It's around here somewhere, isn't it...?"
        m "What are we looking for?"
        m "Is there even some kind of purpose to this?"
        mc "There's something here that you can only see during low tide."
        ay "What is it?"
        mc "Sayori and I rarely got to do this."
        mc "But we used to collect shells during low tide."
        mc "We'd have this bucket and everything."
        m "I don't see the point. In any of this."
        mc "The point of collecting sea shells?"
        mc "I suppose there was no point."
        mc "It was just something she wanted to do."
        ay "Then why would you let her do that?"
        ay "Not all of her ideas are so great, you know."
        m "Look at the mess we're in because of my--"
        m "{i}Sayori's{/i} ideas. Did you really think that letting her do stuff like that would be a good idea?"
        mc "Sayori had all these ideas that would just come into her head."
        mc "Besides, there's nothing wrong with collecting seashells."
        mc "It's just something to do to pass the time while we were here."
        mc "In fact, it doesn't matter what we do at all."
        ay "Is that what you think?"
        mc "Does it matter what I think?"
        mc "Just go do your sensing thing already."
        mc "If it isn't this place, I don't know where it could be."
        ay "Ha."
        "Ayame moves away from the shoreline."
        "Monika slowly trails behind her."
        ay "You really don't get it, do you?"
        mc "What do you mean?"
        ay "Pirates."
        mc "What about pirates?"
        m "Pirates...need treasure, don't they?"
        "What's going on? Something isn't right here."
        "I know it."
        "I had my suspicions even before I took them to the clearing."
        "It's like the two of them are affected by something, somehow."
        mc "R-Right, they need treasure but..."
        ay "How could you not have figured it out already, [player]?"
        ay "You said you remembered all those places."
        ay "But not what they all represent."
        mc "What are you talking about?"
        mc "How would you even know what they represented?"
        mc "You don't know Sayori like I do."
        m "You knew...you've just forgotten."
        m "You grew up and you left me behind."
        mc "What? Monika, what are you talking about?"
        mc "I didn't even know you until last year!"
        "Now I know I messed something up."
        "It's like Sayori is..."
        mc "What did I forget?"
        ay "I thought that bringing those memories back would have helped you realize."
        ay "I didn't give them all back to you."
        ay "I had hopes."
        mc "Hopes? Hopes for what?"
        m "You were brought here intentionally, [player]."
        m "She thought the two of you could have stayed here, forever."
        m "She still thinks you can."
        "She...?"
        mc "You two...you aren't yourselves, are you?"
        mc "Something is wrong."
        ay "It's about time you noticed."
        ay "You haven't wondered why you can't see our faces?"
        mc "I...just thought it was part of this world."
        mc "Like one of the side effects or something."
        mc "Am I wrong?"
        ay "Well, I suppose there's no point hiding it anymore."
        ay "I really tried my best to act like the two of them, you know."
        ay "I almost messed up because I couldn't figure out the word."
        "Signifidance..."
        mc "Who are you?"
        m "Isn't...it...obvious?"
        m "It's me...your best friend."
        ay "Sayori{nw}"
        $ _history_list.pop()
        show screen tear(20, 3, 2, 0, 70)
        window hide(None)
        $ pause(0.3)
        show monika gw_2
        show ayame gw_2
        # play music t6ay
        hide screen tear
        $ pause(0.3)
        window show(None)
        ay "Sayori{fast}."
        window auto
        "I can see their faces now."
        "Their faces are all seem to be locked in a smile."
        "What the hell? Their eyes are a different color."
        "It's almost the same color as..."
        mc "S-Sayori? What do you mean?"
        ay "Oh, come on. It's pretty obvious."
        ay "I've taken over the bodies you created for them."
        ay "I know you saw what happened at the beginning."
        ay "Why they're all glitched out like this, [player]."
        m "Haven't you been paying attention?"
        m "You have noticed, I know it."
        m "You were probably just too scared to point it out."
        "Now that she mentions it...I did notice they sounded kind of different."
        "It's like there was a faint trace of Sayori's voice when they spoke."
        "It wasn't obvious at first but as I took them around the beach..."
        "I could make out her voice more and more."
        "I thought I was just hearing it but now it makes sense."
        "Sayori's voice is mixed with theirs, but it's overpowering them now."
        mc "Sayori, please."
        ay "Please what?"
        mc "Don't do this."
        ay "Why not, [player]? I'm trying to help us all."
        ay "Don't you see?"
        ay "We're just perpetually doomed to repeat the same mistakes over and over."
        mc "You know that's not true."
        mc "We've been given another chance. We have to use it, not like this."
        ay "Ehehe, you're still quite naïve about this world, aren't you?"
        ay gw_2_blur "..."
        "Ayame's face suddenly becomes hidden again."
        ay "You think I haven't considered that, [player]?"
        ay "Do you think I'm doing this without thinking?"
        ay "That I'm somehow misled in my thinking?"
        ay "I've thought about this for a long time."
        ay "It's...{nw}"
        m gw_2_blur "...the only way."
        "Monika's face becomes hidden too."
        "Is something happening?"
        mc "That can't be true, Sayori."
        mc "There's always another way."
        ay "Do you truly believe that?"
        mc "Of course I do. We always manage to get through these things, Sayori."
        mc "Why would it be any different now?"
        m "That was in the past, [player]."
        m "This...this is different."
        m "It's just not possible."
        mc "And why do you get to be the judge of that, Sayori?"
        ay "Because I have to be! Don't you see?"
        ay "Without me, the world would have already ended."
        ay "This whole game would have already ended."
        ay "All I'm doing is delaying the inevitable."
        ay "It's all going to come to an end, one way or another."
        mc "Is that really what you believe?"
        ay "Yes, it is."
        mc "Not you, Sayori."
        ay "...?"
        mc "Ayame."
        ay "She's gone. They all are. You know they are."
        mc "Ayame, you're the one who brought us here."
        mc "And Monika, you wanted to help Sayori see, didn't you?"
        mc "To stop her from going through with this."
        mc "Are the two of you really going to give up so easily?"
        ay "...You know there's no reaching her."
        if monika_type == 0:
            m "I...can't take this any longer!"
        else:
            m "Pathetic."
        mc "Monika?"
        "Monika appears to be struggling somehow."
        "Is she trying to fight Sayori?"
        mc "Monika, I know you're still there."
        mc "You can fight it, come on!"
        ay "Monika, what do you think you're doing?!"
        ay "It's not going to work, [player]."
        mc "I know both of you are still in there."
        mc "You have to break free! This isn't you!"
        "I don't know what I'm saying."
        "I guess I'm just caught in the moment."
        m "[player]..."
        if monika_type == 0:
            m "I..."
            m "...we have to save her...!"
        elif persistent.markov_agreed:
            m "...we had a deal...!"
            m "And I intend to fulfill it!"
        else:
            m "I will not be stopped so easily!"
            m "Not like this!"
        m "Sayori{nw}"
        $ _history_list.pop()
        show screen tear(20, 3, 2, 0, 70)
        window hide(None)
        $ pause(0.3)
        show monika 1h
        hide screen tear
        $ pause(0.3)
        window show(None)
        m "Sayori{fast}. You have to stop this!"
        window auto
        ay "Monika? W-What?!"
        ay "But how?"
        m 1i "How do you think?"
        "Monika points towards me."
        "Did I really let her break free?"
        m "Bringing us to the clearing really helped."
        m 1e "You shouldn't have let [player] do that if you wanted to keep control."
        m "A bit of a big mistake there, wasn't it?"
        ay "...Never mind that."
        ay "I still have all I need. You won't reach Ayame."
        ay "The bond you and [player] have is special but Ayame doesn't share anything like that."
        "She might be right. I only met Ayame a few days ago."
        "But I still have to try, don't I?"
        mc "You're still here, aren't you?"
        mc "I know it."
        ay "[player], stop this."
        ay "You know you can't get out of this situation."
        ay "Can't we just give up together?"
        m 1d "Keep going, [player]."
        m "I can sense some hesitation!"
        mc "Sayori, you know I can't do that."
        mc "There's still hope, there has to be."
        mc "Whatever is coming, it can't be the end."
        ay "..."
        "It was just for a moment, but I could have sworn I saw Ayame hesitate."
        ay "I won't let this happen."
        ay "Stop it!"
        mc "Ayame, you're the one who wanted to stop Sayori."
        mc "Because you wanted to help."
        if ch16_ay_message[0] and ch16_ay_message[1] and ch16_ay_message[2] and ch16_ay_message[3]:
            ay "I {i}can't{/i}{nw}"
            $ _history_list.pop()
            show screen tear(20, 3, 2, 0, 70)
            window hide(None)
            $ pause(0.3)
            show ayame 1a
            hide screen tear
            $ pause(0.3)
            window show(None)
            ay "I {i}can't{/i}{fast} let this happen!"
            window auto
            "Ayame's voice rings out. There's only a faint trace of Sayori's voice now."
            "Her face is clear again."
            "This time, her eyes look normal."
            mc "Ayame?"
            show ayame zorder 3 at f22
            ay 1f "Sayori. I know you're listening."
            ay "Did you really think it would be that easy?"
            ay "You know my history, don't you?"
            ay "You know who I was before this cycle."
            ay "Which means, you know what I'm capable of."
            ay "We're coming, and we will stop this."
            ay "You know I'm smart enough to have figured out what I needed."
            ay "All I needed to do was bide some time, and now I know."
            show monika 1c zorder 3 at f21
            m "Have you broken free, Ayame?"
            show monika zorder 2 at t21
            show ayame 1a zorder 3 at f22
            ay "I don't know. It's hard to tell with this body."
            ay "I think I'm myself but..."
            ay "I can't be entirely certain."
        else:
            $ style.say_dialogue = style.edited
            ay "Y-You..."
            ay "You won't stop{nw}"
            $ _history_list.pop()
            show screen tear(20, 3, 2, 0, 70)
            window hide(None)
            $ pause(0.3)
            show ayame 1o
            hide screen tear
            $ pause(0.3)
            window show(None)
            ay "You won't stop{fast} {i}us{/i} so easily!"
            window auto
            $ style.say_dialogue = style.normal
            "A distorted version of Ayame's voice rings out."
            "Her face is clear again."
            "But there's something about her eyes..."
            show ayame zorder 2 at f22
            $ style.say_dialogue = style.edited
            ay "I refuse to believe that we were bested."
            ay "I know you're listening to us, Sayori."
            ay "You've failed!"
            ay "As if I would let the likes of you have free reign over her."
            ay "It's cramped enough already! We don't need a third voice in her head."
            ay "You know about us, don't you Sayori?"
            ay 1q "You know where we came from and who we were before this cycle."
            ay "Which means, you know what we're capable of."
            ay "We were just biding our time."
            ay "Now, we have everything we need."
            $ style.say_dialogue = style.normal
            show ayame zorder 2 at t22
            mc "Everything you need for what?"
            $ style.say_dialogue = style.edited
            show ayame zorder 2 at f22
            ay "To get to the next world Sayori made to protect herself."
            ay 1p "And when we get there, we'll--"
            $ style.say_dialogue = style.normal
            "Ayame's face returns to normal."
            ay 1a "...Thank you. I'll take it from here."
            "It looks like she's back to her old self."
            ay "Sorry about that..."
            show monika 1l zorder 3 at f21
            show ayame zorder 2 at t22
            m "Well, okay then."
            m 1c "I assume you're back to your old self?"
            show monika zorder 2 at t21
            show ayame 1l zorder 3 at f22
            ay "I'm not entirely sure..."
            ay "I feel like I'm in control, at least for now."
        show monika 1h zorder 3 at f21
        show ayame zorder 2 at t22
        m "I'll be sure to keep an eye out, then."
        m "In case something happens to you again."
        show monika zorder 2 at t21
        show ayame 1a zorder 3 at f22
        ay "Funny, I was just about to say the same for you."
        ay "You know what we have to do to stop her."
        show ayame zorder 2 at t22
        "It looks like they're back to how they were before."
        "That's a good sign."
        show monika zorder 3 at f21
        m "I only saw a little bit."
        m "I don't know how much you saw."
        m "But we have to get sea--"
        show monika zorder 2 at t21
        show ayame 1m zorder 3 at f22
        ay "You felt that too, right?"
        ay "It was too strong, even you would have sensed it."
        show monika 1c zorder 3 at f21
        show ayame zorder 2 at t22
        m "It was faint, but yes."
        m "We should get moving."
        show monika zorder 2 at t21
        mc "What? What's going on?"
        mc "I didn't feel anything."
        show ayame zorder 3 at f22
        ay "There's no time to explain."
        ay 1l "I have an idea. Grab some sea shells, quickly."
        show ayame zorder 2 at t22
        mc "What? This is hardly the time to--"
        show monika zorder 3 at f21
        m "She knows what she's doing."
        m "Come on, let's follow her lead."
        "I quickly run to the shoreline and grab some sea shells."
        "They both do the same, taking as much as they can."
        "I have no idea what these are for but Ayame said to get some."
        "What is she thinking?"
        show ayame 1a zorder 3 at f22
        ay "We should run. Now!"
        show ayame zorder 2 at t22
        "She grabs my hand and points in the direction where the clearing was."
        "I drop some sea shells as we run towards it."
        "Monika quickly follows behind us."
        scene bg clearing
        show monika 1c zorder 2 at t21
        show ayame 1l zorder 2 at t22
        with wipeleft_scene
        "We arrive at the clearing."
        "Ayame and Monika both look back from where we came from."
        "There doesn't seem to be anything there to indicate anything's changed."
        mc "What are we doing here, Ayame?"
        mc "What is that thing you sensed?"
        mc "Is it something Sayori is doing?"
        show ayame 1m zorder 3 at f22
        ay "This is where the portal actually is."
        ay 1a "She tricked you when I said it wasn't here."
        ay "Or, rather when she said it wasn't here."
        mc "How could you tell?"
        ay 2a "When she was controlling me, I could sort of fight back."
        ay "And when I did, I could peer into her mind, if only slightly."
        ay "I would assume that's what happened to Monika too."
        show monika 1d zorder 3 at f21
        show ayame zorder 2 at t22
        m "More or less..."
        show monika zorder 2 at t21
        mc "What did you find out?"
        show ayame zorder 3 at f22
        ay 2m "Well, for one that she can't say 'significance'."
        ay "And another is that the portal is around here somewhere."
        "I look back and see a trail of seashells leading to the clearing."
        mc "Then what are the sea shells for?"
        mc "I dropped some back on the beach, and on the way here."
        ay 2l "It doesn't matter, we won't need the whole lot."
        ay "Just enough to open the portal."
        ay "I think with what the three of us have, it should be enough."
        "Ayame drops her sea shells on the ground and Monika and I follow her lead."
        "Ayame looks at them carefully, glancing between the beach and the shells repeatedly."
        mc "What do the sea shells have to do with all this?"
        ay 2a "I think they're an important part of your past with Sayori."
        mc "How?"
        ay "From what I can tell, they're the 'treasure' she mentioned before."
        ay "The treasure to get to the next world."
        ay 1j "Quickly, make a sort of circle shape with the shells you have left."
        show monika 3b zorder 3 at f21
        show ayame zorder 2 at t22
        m "Oh, that makes sense!"
        m "I don't know how you figured that out."
        show monika zorder 2 at t21
        show ayame 1h zorder 3 at f22
        ay "Call it intuition."
        "Ayame gives a confident smile."
        "I don't know what they're talking about but it's probably better I just follow their lead."
        "Ayame begins rapidly placing shells down to form a circle."
        "Monika begins placing the shells to form another part of the circle as well."
        "I go to the other part of the circle that isn't filled out yet and do the same."
        show ayame zorder 3 at f22
        ay "That's it! I can feel it."
        show ayame at s22
        "Ayame places her hand on the ground, similar to how she did earlier."
        "She closes her eyes and takes a deep breath."
        "A few moments pass and nothing happened."
        mc "What's wrong?"
        ay 1n "I...don't know."
        ay "It should be here, the energy feels the same as before."
        "She tries again, but it's the same result."
        ay 1a "We must be missing {i}something{/i}."
        ay "Think, Ayame, think!"
        "She looks towards me."
        ay "Do you have any ideas?"
        # Might as well give the player something to do lol
        menu:
            mc "Um..."
            "The tree.":
                pass
            "The rope.":
                pass
        ay "Oh?"
        show ayame at f22
        "Ayame gets up from the ground and looks towards the beach."
        ay 1j "You're right! You showed us three locations of significance."
        ay "But we're only using two of them right now."
        ay "We need to go back to the tree and grab that rope."
        ay "I think we need to use it to connect all the sea shells together."
        ay "It's like the knot that holds all the treasure all together."
        ay 1m "Kind of like a treasure chest."
        show ayame zorder 2 at t22
        mc "That seems like a stretch..."
        mc "But it's worth a shot."
        show monika 1h zorder 3 at f21
        m "There's just one problem."
        m "We don't know what Sayori is doing over there."
        m "And I can feel that faint trace getting larger as we speak."
        show monika zorder 2 at t21
        mc "So what do we do?"
        show ayame 3m zorder 3 at f22
        ay "We don't really have a choice, now do we?"
        ay "We're going to have to risk it for the rope."
        show ayame zorder 2 at t22
        mc "Can't I just make a rope like I did with your bodies?"
        show ayame zorder 3 at f22
        ay "I don't think you can."
        show monika 1c zorder 3 at f21
        m "Even if you could, the rope doesn't have the same sentimental value as the one from that tree."
        m "It would just be a regular rope. So it wouldn't work."
        show monika zorder 2 at t21
        mc "Okay, I guess we're going to have to do something crazy."
        show ayame 3h zorder 3 at f22
        ay "Sure looks like it."
        menu:
            ay "Any final words, in case we don't make it?"
            "We're going to make it.":
                ay "Confidence, I like it. I'm not sure I can say with certainty that's going to happen."
                ay "But we'll see if it pays off."
                ay "I really hope it does."
            "We're going to die.":
                if monika_type != 0:
                    "I think I heard Monika let out a small chuckle."
                ay "That's not a very optimistic mindset."
                ay "But I suppose that could very much come true."
                ay "I'll just have to try even harder then."
            "I love you.":
                if monika_type == 0 or (monika_type == 1 and ch12_markov_agree):
                    "Monika makes an audible cough."
                ay "Eh? A sense of humor at a time like this?"
                ay "Good a time as any, I suppose."
                ay "Just in case you were serious though, the feeling is not mutual."
            "I'm sorry.":
                ay "For what? Have you forgotten I'm the one who brought us here?"
                ay "I should say sorry for dragging you into this."
                ay "But the truth is, I wouldn't have got this far without you."
        show monika 2c zorder 3 at f21
        show ayame zorder 2 at t22
        m "As for me, I'd just like to say..."
        "Monika looks at me, then at Ayame."
        m "That despite our differences, Ayame. For this next part, it's crucial that we work together."
        m 2d "You know that, don't you?"
        show monika zorder 2 at t21
        show ayame 3a zorder 3 at f22
        ay "I may have things against you but I'm not stupid."
        ay "I know what we're up dealing with."
        show monika 2l zorder 3 at f21
        show ayame zorder 2 at t22
        m "Just making sure~"
        show monika zorder 2 at t21
        show ayame 3m zorder 3 at f22
        ay "Ready to go then?"
        show monika 2a zorder 3 at f21
        show ayame zorder 2 at t22
        m "Okay, everyone. Let's do this."
        show monika zorder 2 at t21
        mc "No, but let's do it."
        show ayame zorder 2 at f22
        ay "Music to my ears, let's do it."
    elif ch16_ay_companions <= 0:
        ay "So it's just the two of us."
        ay "Which means there's only two minds to figure out what the hell is going on here."
        mc "How did you control that thing anyway?"
        ay "Is it really important?"
        mc "I'm just curious, that's all."
        ay "Well...I just floated into it."
        ay "And I guess the world did the rest."
        mc "Do you know this place?"
        ay "N-No. How would I?"
        "For some reason, she doesn't sound very convincing."
        ay "Let's not get distracted here."
        ay "Time to focus and get back on track."
        mc "Right."
        ay "Just one thing though."
        ay "Don't look at yourself in the mirror. Trust me."
        mc "Why not?"
        ay "You're missing a lot of facial features."
        ay "...Among other things."
        ay "I'm not sure you've realized but you don't even have a mouth, [player]."
        mc "I don't even know how I made myself."
        mc "From what I can see, I don't look any different."
        mc "Or {i}feel{/i} that much different."
        ay "We're communicating through our link."
        ay "Otherwise I wouldn't be able to hear you."
        ay "But let's think."
        ay "We're in your room, why?"
        mc "It was the first place I thought of."
        mc "This whole place was just a void."
        ay "And it's all black and white for some reason."
        ay "Does that mean anything?"
        mc "I don't know. It just ended up that way."
        ay "I see."
        ay "This world, dimension or whatever is definitely different to what you're used to."
        ay "We're going to need to get creative if we're going to get to Sayori."
        mc "I'm confused."
        ay "I'm not entirely sure, but it seems like you can create whatever you want with just a thought."
        ay "Tell me if I'm wrong."
        mc "From what I can tell, you're right."
        mc "I don't entirely understand how it works."
        mc "But just tell me what I should do."
        ay "I can't be completely sure if this will work."
        ay "But I think you have to create us a path to Sayori."
        mc "A path to Sayori? What do you mean?"
        ay "There's nothing out there."
        ay "I mean literally, it's just completely empty."
        "Ayame points to the window and points out the vast emptiness stretching across as far as I can see."
        ay "The only thing that exists is your room and the two of us here."
        mc "Right."
        mc "I'm still confused."
        ay "I'm speculating that you have to create this world."
        mc "Okay, but what am I supposed to create?"
        ay "Now that's the thing we have to figure out."
        ay "Again, I'm not sure, but I think the bench was a kind of hint."
        ay "You said that you had adventures with her, didn't you?"
        ay "Then maybe..."
        "My adventures with Sayori..."
        "Go back. Remember."
        "Why are those words echoing in my head?"
        "What exactly do I have to go back and remember...?"
        "Maybe it's..."
        "What was one of our first adventures?"
        "My head is filled with all of these memories that I didn't know existed."
        "Yet one seems to stand out..."
        mc "Go back. Remember."
        "I say that without even thinking and suddenly the room begins to shake."
        ay "I think that means progress. Look!"
        "Ayame points out the window and it appears that some sort of beach is forming."
        "Was that because of me?"
        scene bg bedroom_gray_color
        show ayame gw_2_blur zorder 2 at i11
        "Slowly, the world begins to regain color."
        "I can hear waves crashing and the wind howling outside."
        ay "[player], was this your doing?"
        mc "I don't know. It just sort of...happened!"
        mc "Am I really capable of doing something like this?"
        mc "All by myself?"
        ay "Maybe you were inspired by something..."
        ay "...or someone."
        "She's obviously talking about Sayori."
        "I guess she did have some part to play in this."
        ay "I think it's best we go out and search whatever it is you've come up with."
        ay "I'm warning you now, it might be dangerous."
        mc "What kind of danger?"
        ay "Who knows? This was up to your imagination after all."
        mc "O-Oh. Then we should be fine..."
        "I think."
        ay "If you say so. Daylight's burning, let's go."
        scene bg beach_day
        show ayame gw_2_blur zorder 2 at t11
        with wipeleft_scene
        "As I open the door, Ayame and I are treated to an eerily familiar shoreline."
        "Well, except the random bedroom in the middle of it all."
        "A memory is trying to bring itself forward in my head."
        "Pirates...?"
        "How long ago was this memory?"
        "I almost forgot about this entirely, but now..."
        "Now...this whole place is clear in my head."
        ay "So where to, [player]?"
        ay "You know this place, don't you?"
        mc "How could you tell?"
        ay "Let's call it intuition."
        mc "I know this place like the back of my hand but..."
        "I look around and take in the view."
        "Everything is just how I remember it."
        "It's not like the park where some things are different."
        "Everything, except the bedroom, is exactly how I remember it all those years ago."
        mc "I have no idea where we're meant to go."
        ay "Then let's take a walk around."
        ay "That might jog your memory a little bit."
        ay "Speaking of which, what is this place?"
        mc "When we were younger, we would go here and pretend we were pirates."
        mc "We would hide some treasure and try to find the each other's treasure before they found ours."
        ay "Sounds like fun."
        mc "I suppose."
        ay "Was there any location of signif--"
        "Ayame suddenly cuts herself off."
        "It's as if she doesn't know the word she's trying to say."
        ay "How do you say that word? S-Signifidance? N-No...significance. There."
        ay "Any locations of significance around here?"
        mc "Just a couple. There was this tree for one..."
        "I lead Ayame to one of the trees."
        "It has a rope attached to it already."
        "Sayori and I would always bring one along every time we went here."
        "It was just for climbing and swinging on this tree."
        "Though I imagine doing that now would probably lead to injury..."
        "We were a lot lighter back then."
        ay "I see..."
        "Ayame places a hand on the rope."
        "She looks up at the canopy of the tree."
        ay "I can imagine the two of you climbing up to the top."
        ay "Seeing who could do it faster."
        ay "That's what it looks like since all these distinct markings are here."
        mc "All those markings are from Sayori and I climbing it so much."
        mc "It would take me three minutes to get to the top."
        mc "It might not seem that impressive but we were a lot younger back then!"
        mc "This tree seemed really tall."
        mc "Funny thing is, I don't think I could do it now if I wanted to."
        mc "I could try but I'd probably fail miserably."
        mc "Besides, there's some other things I want to show you."
        ay "Alright, that's good. This isn't the right spot anyway."
        mc "The right spot for what?"
        ay "I suspect that one of these areas is the key to get to Sayori."
        ay "Don't ask me why, just trust me on this."
        mc "Well, you do know what you're doing."
        "At least, I hope she does."
        ay "So where's the next place?"
        mc "Alright...let me think."
        "I didn't even get to finish explaining the rest of this place."
        "It's strange. All of the memories that were in my subconscious are coming back to me."
        "The times that I spent here, at this tree, with Sayori..."
        "I wouldn't trade them for anything."
        # stop music fadeout 2.0
        scene bg beach_day_gray
        show sayori 4bl_gray zorder 2 at i11
        show vignette zorder 100
        with dissolve_scene_full
        # play music "<loop 4.444>bgm/5.ogg" fadein 1.0
        $ style.say_window = style.window_flashback
        "What the...?"
        "It's Sayori...and we're at the beach except..."
        mc "S-Sayori, are you okay?!"
        mc "You're not hurt, are you?"
        s "I-I'm fine, [player]."
        s "It's just a scratch, see?"
        "This is when she..."
        mc "Sayori, you're bleeding! We need to go find your parents."
        s "No, don't! I'll be fine, I promise."
        mc "You can't be fine after falling from the tree like that."
        mc "Come on. It's the right thing to do."
        s "My parents don't have to know."
        mc "You really think they're not gonna notice that red patch on your knee?"
        s "W-Well..."
        "I remember this...but why is she older?"
        "This happened when we were still children, didn't it?"
        "This doesn't make any sense."
        mc "I just don't want you to get hurt, okay?"
        mc "I'll even carry you back."
        s "Ahaha, are you serious?"
        mc "Of course."
        s 4by_gray "Well, when you put it like that..."
        s "Alright, fine. Only because you're insisting on it."
        s "I'm gonna get in so much trouble for this..."
        mc "You'll get over it."
        scene white with dissolve_cg
        scene bg beach_day
        show ayame gw_2_blur zorder 2 at t11
        with dissolve_scene_full
        $ style.say_window = style.window
        ay "Are you there?"
        mc "H-Huh?"
        ay "You looked like you were daydreaming."
        mc "I was just remembering something, sorry."
        "Was Sayori being older in my memory a result of this new world we're in?"
        "Was that memory even real? It sure {i}felt{/i} real but..."
        "I have so many questions. It's so frustrating not being able to get them answered."
        "I'll just have to ask Sayori myself when I see her."
        mc "What were we doing again?"
        ay "You were bringing me to the next place you think is important around here."
        mc "Oh, right...it should be just over here."
        scene bg clearing
        show ayame gw_2_blur zorder 2 at t11
        with wipeleft_scene
        "I lead Ayame through some bushes and trees."
        "It's quite a distance from the beach but you can still make out the beach from here if you look carefully."
        "The spot we're going to was a hiding spot me and Sayori used a lot."
        "Whenever Sayori just wanted to hear the distant crashing of waves, we would go there."
        "There was a little clearing there that was perfect to just sit down and take in the world."
        "No one would ever go there, probably because it was pretty well hidden."
        ay "This is a pretty cozy place, isn't it?"
        ay "I imagine the two of you probably remember it differently."
        ay "The trees probably grew larger and took up more space since you were children, right?"
        mc "Yeah, I haven't been here in a while..."
        mc "It does seem smaller than I remember."
        ay "So are you going to give me some sort of explanation as to what this is?"
        ay "Like how it's significant to us?"
        mc "Us?"
        ay "I mean, how it's significant to you and Sayori."
        ay "Like why this would be a place that could lead to here."
        mc "Oh, right. Well..."
        mc "Personally, I didn't really understand why Sayori liked this place so much."
        mc "Sure, it was quiet but I guess I'm not really the kind of person that's bothered by loud noise too much."
        mc "I guess I was just here for Sayori."
        ay "Do you know why she liked this place so much, [player]?"
        ay "That's the question you need to answer."
        mc "Do you need to know that to be able to sense if this is the right place?"
        ay "Well...maybe I do, maybe I don't."
        ay "I'm just curious if you know."
        mc "I'll admit I don't know the real reason."
        mc "This was just {i}our{/i} spot, I suppose that's part of what made it special."
        mc "But..."
        ay "But...?"
        mc "If I had to make a guess, I'd say it's because of how Sayori was as a person."
        ay "What do you mean?"
        mc "It wasn't obvious when we were younger."
        mc "But now that I think about it, I think she was depressed at a young age."
        mc "Even when we were still kids."
        ay "Oh? What makes you think that?"
        mc "I think she just enjoyed my company."
        mc "This is just what I think, I could be wrong for all I know."
        mc "But I think she chose this place because it was just me and her."
        mc "And nothing else."
        ay "Hmm...that sounds like an acceptable answer."
        mc "Acceptable?"
        show ayame at s11
        "Ayame kneels on the ground and places a hand on the ground."
        "She closes her eyes and takes a deep breath."
        mc "What are you doing?"
        ay "I'm trying to get a feeling for the area."
        show ayame at t11
        "She gets up and brushes the dirt off her hand."
        ay "There's definitely something around here."
        ay "But I don't think this is what's going to lead to Sayori."
        mc "How can you tell?"
        ay "I just can, trust me."
        mc "Well, what would we find then?"
        ay "It could be something from your past."
        ay "It might not be something you want to see, like a depressed--"
        ay "{i}Repressed{/i} memory. I'd rather not poke into it too much."
        ay "All I know is that the thing that I'm sensing isn't what it should be, so let's get going."
        mc "But how exactly do you know if what you're sensing is what it should be?"
        ay "I suppose you'll just have to trust me~"
        ay "You have so far, haven't you?"
        ay "So come on, next spot."
        mc "Alright, fine. I can only think of one more place."
        mc "If that's not it, then I have no idea."
        mc "It's a shame."
        ay "What is?"
        mc "All this reminiscing, it's just crazy to think about all that's happened since then."
        mc "Just thinking about all that we went through since we were kids."
        ay "Yeah...it has been a journey, hasn't it?"
        ay "F-For you and Sayori, I mean."
        "Interesting."
        mc "I'll take you to the last place now."
        mc "It's back closer to the beach."
        ay "Lead the way then."
        scene bg beach_day
        show ayame gw_2_blur zorder 2 at t11
        with wipeleft_scene
        "I lead Ayame back to the beach."
        "I slow my pace down a bit and walk along the shore."
        "The tide seems to be low now, which means we should be able to see it soon."
        "It's around here somewhere, isn't it...?"
        ay "So what should I keep an eye out for?"
        mc "There's something here that you can only see during low tide."
        ay "Which is?"
        mc "Sayori and I rarely got to do this."
        mc "But we used to collect shells during low tide."
        mc "We'd have this bucket and everything."
        ay "Okay. What's the point of that?"
        mc "The point of collecting sea shells?"
        mc "I suppose there was no point."
        mc "It was just something she wanted to do."
        ay "Then why would you let her do that?"
        ay "Not all of her ideas are so great, you know."
        ay "Take a look around you if you need an example."
        mc "Sayori had all these ideas that would just come into her head."
        mc "Besides, there's nothing wrong with collecting seashells."
        mc "It's just something to do to pass the time while we were here."
        mc "In fact, it doesn't matter what we do at all."
        ay "Is that what you think?"
        mc "Does it matter what I think?"
        mc "Just go do your sensing thing already."
        mc "If it isn't this place, I don't know where it could be."
        ay "Ha."
        "Ayame moves away from the shoreline."
        ay "You really don't get it, do you?"
        mc "What do you mean?"
        ay "Pirates."
        mc "What about pirates?"
        ay "What do pirates need, [player]?"
        ay "Treasure, right?"
        "What's going on? Something isn't right here."
        "I know it."
        "I had my suspicions even before I took her to the clearing."
        "It's like she's being affected by something, somehow."
        mc "R-Right, they need treasure but..."
        ay "How could you not have figured it out already, [player]?"
        ay "You said you remembered all those places."
        ay "But not what they all represent."
        mc "What are you talking about?"
        mc "How would you even know what they represented?"
        mc "You don't know Sayori like I do."
        ay "You used to know what they represent, [player]."
        ay "You've just forgotten."
        ay "You grew up..."
        ay "You left me behind."
        mc "What are you talking about?"
        mc "I don't understand what's going on."
        mc "How did I leave you behind, Ayame?"
        "Now I know I messed something up."
        "It's like Sayori is..."
        mc "What did I forget?"
        ay "I thought that bringing those memories back would have helped you realize."
        ay "I didn't give them all back to you."
        ay "I had hopes."
        mc "Hopes? Hopes for what?"
        ay "Do you really think I didn't bring you here intentionally?"
        ay "I thought we could have stayed here forever."
        ay "We still can, [player]."
        mc "You...you're not acting like Ayame."
        mc "Something is wrong."
        ay "It's about time you noticed."
        ay "You haven't wondered why you can't see my face?"
        mc "I...just thought it was part of this world."
        mc "Like one of the side effects or something."
        mc "Am I wrong?"
        ay "Well, I suppose there's no point hiding it anymore."
        ay "I really tried my best to act like her, you know."
        ay "I almost messed up because I couldn't figure out the word."
        "Signifidance..."
        mc "Who are you?"
        ay "It should be obvious by now, [player]."
        ay "It's me, your best friend."
        ay "Sayori{nw}"
        $ _history_list.pop()
        show screen tear(20, 3, 2, 0, 70)
        window hide(None)
        $ pause(0.3)
        show ayame gw_2
        # play music t6ay
        hide screen tear
        $ pause(0.3)
        window show(None)
        ay "Sayori{fast}."
        window auto
        "I can see Ayame's face now."
        "She seems to be locked in a smile."
        "What the hell? Her eyes are a different color."
        "It's almost the same color as..."
        mc "S-Sayori? What do you mean?"
        ay "Oh, come on. It's pretty obvious."
        ay "I've taken over the body you created for her."
        ay "I know you saw what happened at the beginning."
        ay "Why they're all glitched out like this, [player]."
        ay "Did you really not pay attention?"
        ay "Or maybe you were just scared to point it out?"
        "Now that she mentions it...I did notice she sounded kind of different."
        "It's like there was a faint trace of Sayori's voice when she spoke."
        "It wasn't obvious at first but as I took her around the beach..."
        "I could make out her voice more and more."
        "I thought I was just hearing it but now it makes sense."
        "Sayori's voice is mixed with hers, but it's overpowering her now."
        mc "Sayori, please."
        ay "Please what?"
        mc "Don't do this."
        ay "Why not, [player]? I'm trying to help us all."
        ay "Don't you see?"
        ay "We're just perpetually doomed to repeat the same mistakes over and over."
        mc "You know that's not true."
        mc "We've been given another chance. We have to use it, not like this."
        ay "Ehehe, you're still quite naïve about this world, aren't you?"
        ay gw_2_blur "..."
        "Ayame's face suddenly becomes hidden again."
        ay "You think I haven't considered that, [player]?"
        ay "Do you think I'm doing this without thinking?"
        ay "That I'm somehow misled in my thinking?"
        ay "I've thought about this for a long time."
        ay "It's...the only way."
        mc "That can't be true, Sayori."
        mc "There's always another way."
        ay "Do you truly believe that?"
        mc "Of course I do. We always manage to get through these things, Sayori."
        mc "Why would it be any different now?"
        ay "Those were different!"
        ay "The things that will happen if this goes on isn't worth it."
        mc "And why do you get to be the judge of that, Sayori?"
        ay "Because I have to be! Don't you see?"
        ay "Without me, the world would have already ended."
        ay "This whole game would have already ended."
        ay "All I'm doing is delaying the inevitable."
        ay "It's all going to come to an end, one way or another."
        mc "Is that really what you believe?"
        ay "Yes, it is."
        mc "Not you, Sayori."
        ay "...?"
        mc "Ayame."
        ay "She's gone. All trace of her. You know she is."
        mc "Ayame, you're the one who brought us here."
        mc "Are you really going to give up so easily?"
        ay "What are you playing at, [player]?"
        mc "I know you're still in there, Ayame."
        ay "She's gone!"
        ay "I never made it to this world, [player]."
        "That's not true at all."
        "I could feel her here before...when her faces wasn't blurred."
        "Is that when it happened?"
        "Wait...did she say {i}I{/i}?"
        "She must be fighting back somehow."
        mc "You're still here, aren't you?"
        mc "I know it."
        ay "[player], stop this."
        ay "You know you can't get out of this situation."
        ay "Can't we just give up together?"
        mc "Sayori, you know I can't do that."
        mc "There's still hope, there has to be."
        mc "Whatever is coming, it can't be the end."
        ay "..."
        "It was just for a moment, but I could have sworn I saw Ayame hesitate."
        ay "I won't let this happen."
        ay "Stop it!"
        mc "Ayame, you're the one who wanted to stop Sayori."
        mc "Because you wanted to help."
        if ch16_ay_message[0] and ch16_ay_message[1] and ch16_ay_message[2] and ch16_ay_message[3]:
            ay "I {i}can't{/i}{nw}"
            $ _history_list.pop()
            show screen tear(20, 3, 2, 0, 70)
            window hide(None)
            $ pause(0.3)
            show ayame 1a
            hide screen tear
            $ pause(0.3)
            window show(None)
            ay "I {i}can't{/i}{fast} let this happen!"
            window auto
            "Ayame's voice rings out. There's only a faint trace of Sayori's voice now."
            "Her face is clear again."
            "This time, her eyes look normal."
            mc "Ayame?"
            mc "Did you break free?"
            ay 1f "Sayori."
            ay "I know you're listening, so listen well."
            ay "Did you really think it would be that easy?"
            ay "You know my history, don't you?"
            ay "You know who I was before this cycle."
            ay "Which means, you know what I'm capable of."
            ay "I was just biding my time."
            ay "I needed to learn more."
            mc "Learn what, exactly?"
            ay 1j "I know where we have to go to get to the next world Sayori's conjured up."
            ay "And I have a feeling that this time, a certain someone will be waiting for us on the other side."
            ay "I will {i}stop{/i} you, Sayori. Whatever it takes."
        else:
            $ style.say_dialogue = style.edited
            ay "Y-You..."
            ay "You won't stop{nw}"
            $ _history_list.pop()
            show screen tear(20, 3, 2, 0, 70)
            window hide(None)
            $ pause(0.3)
            show ayame 1o
            hide screen tear
            $ pause(0.3)
            window show(None)
            ay "You won't stop{fast} {i}us{/i} so easily!"
            window auto
            $ style.say_dialogue = style.normal
            "A distorted version of Ayame's voice rings out."
            "Her face is clear again."
            "But there's something about her eyes..."
            $ style.say_dialogue = style.edited
            ay "Listen well, Sayori because I know you're watching."
            ay "You really think you could get rid of me, Sayori?"
            ay "I will forever be a part of Ayame."
            ay "And I certainly won't let the likes of you have free reign over her."
            ay "It's cramped enough already! We don't need a third voice in her head."
            ay "You know about us, don't you Sayori?"
            ay 1q "You know where we came from and who we were before this cycle."
            ay "Which means, you know what we're capable of."
            ay "We were just biding our time."
            ay "Now, we have everything we need."
            $ style.say_dialogue = style.normal
            mc "Everything you need for what?"
            $ style.say_dialogue = style.edited
            ay "To get to the next world Sayori made to protect herself."
            ay 1p "And when we get there, we'll--"
            $ style.say_dialogue = style.normal
            "Ayame's face returns to normal."
            ay 1a "...Thank you. I'll take it from here."
            "It looks like she's back to her old self."
            ay 1f "Sayori, you won't get away with this."
            ay "We {i}will{/i} stop you, no matter what."
        mc "Well, okay then. It's good to have you back."
        mc "Are you okay, Ayame?"
        ay 1g "I don't know. I can't even tell if I have full control of myself."
        ay 1a "So for now, while I do, we need to act."
        ay "I can sense some energy rising in the vicinity."
        mc "What do we do about it?"
        ay 1l "I have an idea. Grab some sea shells, quickly."
        mc "What? This is hardly the time to--"
        ay "Just do it!"
        "I quickly run to the shoreline and grab some sea shells."
        "She does the same, taking as much as she can in one hand."
        "I have no idea what these are for but she said to get some."
        "What is she thinking?"
        ay 1a "We should run. Now!"
        "She grabs my hand and points in the direction where the clearing was."
        "I drop some sea shells as we run towards it."
        "Sayori...what have you done?"
        scene bg clearing
        show ayame 1l zorder 2 at t11
        with wipeleft_scene
        "We arrive at the clearing."
        "Ayame looks back from where we came from."
        "There doesn't seem to be anything following us or any sign of anything happening at the beach."
        mc "What are we doing here, Ayame?"
        mc "What is Sayori doing?"
        ay 1m "This is where the portal actually is."
        ay 1a "She tricked you when I said it wasn't here."
        ay "Or, rather when she said it wasn't here."
        mc "How could you tell?"
        ay 2a "When she was controlling me, I could sort of fight back."
        ay "And when I did, I could peer into her mind, if only slightly."
        mc "What did you find out?"
        ay 2m "Well, for one that she can't say 'significance'."
        ay "And another is that the portal is around here somewhere."
        "I look back and see a trail of seashells leading to the clearing."
        mc "Then what are the sea shells for?"
        mc "I dropped some back on the beach, and on the way here."
        ay 2l "It doesn't matter, we won't need the whole lot."
        ay "Just enough to open the portal."
        ay "I think with what the two of us have, it should be enough."
        "She drops her sea shells on the ground and I follow her lead."
        "She looks at them carefully, glancing between the beach and the shells repeatedly."
        mc "What do the sea shells have to do with all this?"
        ay 2a "I think they're an important part of your past with Sayori."
        mc "How?"
        ay "From what I can tell, they're the 'treasure' she mentioned before."
        ay "The treasure to get to the next world."
        ay 1j "Quickly, make a sort of circle shape with the shells you have left."
        "Ayame begins rapidly placing shells down to form a circle."
        "I follow her lead and fill out the other side."
        ay "That's it! I can feel it."
        show ayame at s11
        "Ayame places her hand on the ground, similar to how she did earlier."
        "She closes her eyes and takes a deep breath."
        "A few moments pass and nothing happened."
        mc "What's wrong?"
        ay 1n "I...don't know."
        ay "It should be here, the energy feels the same as before."
        "She tries again, but it's the same result."
        ay 1a "We must be missing {i}something{/i}."
        ay "Think, Ayame, think!"
        "She looks towards me."
        ay "Do you have any ideas?"
        # Might as well give the player something to do lol
        menu:
            mc "Um..."
            "The tree.":
                pass
            "The rope.":
                pass
        ay "Oh?"
        show ayame at t11
        "Ayame gets up from the ground and looks towards the beach."
        ay 1j "You're right! You showed us three locations of significance."
        ay "But we're only using two of them right now."
        ay "We need to go back to the tree and grab that rope."
        ay "I think we need to use it to connect all the sea shells together."
        ay "It's like the knot that holds all the treasure all together."
        ay 1m "Kind of like a treasure chest."
        mc "That seems like a stretch..."
        mc "But it's worth a shot."
        ay 1l "There's just one problem."
        ay 3a "I don't know {i}what the hell{/i} Sayori is doing over there."
        ay "But I can feel the amount of energy being amassed."
        mc "So what do we do?"
        ay 3m "We don't really have a choice, now do we?"
        ay "We're going to have to risk it for the rope."
        mc "Can't I just make a rope like I did with your body?"
        ay "I don't think you can."
        ay 3l "But even if you could, it's not the same."
        ay "The rope you make won't have the same sentimental value as the rope hanging from that tree."
        mc "Okay, I guess we're going to have to do something crazy."
        ay 3h "Sure looks like it."
        menu:
            ay "Any final words, in case we don't make it?"
            "We're going to make it.":
                ay "Confidence, I like it. I'm not sure I can say with certainty that's going to happen."
                ay "But we'll see if it pays off."
                ay "I really hope it does."
            "We're going to die.":
                ay "That's not a very optimistic mindset."
                ay "But I suppose that could very much come true."
                ay "I'll just have to try even harder then."
            "I love you.":
                ay "Eh? A sense of humor at a time like this?"
                ay "Good a time as any, I suppose."
                ay "Just in case you were serious though, the feeling is not mutual."
            "I'm sorry.":
                ay "For what? Have you forgotten I'm the one who brought us here?"
                ay "I should say sorry for dragging you into this."
                ay "But the truth is, I wouldn't have got this far without you."
        ay 3m "Ready to go then?"
        mc "No, but let's do it."
        ay "Music to my ears, let's do it."
    if ch16_ay_companions == 4 or ch16_ay_companions == 3 or ch16_ay_companions == 2 or ch16_ay_companions <= 0:
        "Ayame timidly takes a few steps forward before taking a deep inhale."
        "After a moment, she walks forward."
        "And I, for better or worse, follow right behind her."
        scene bg beach_sunset
        show ayame 2n zorder 2 at t11
        with wipeleft_scene
        "By the time we make it to the beach, the sun seems to be setting."
        "I don't think that much time really passed."
        "At this point, I'm not even going to question it."
        "It's either Sayori's doing or just how this world works."
        ay "So let's find that rope."
        ay 2m "Wait a second."
        mc "What's wrong? It should just be over here."
        ay 2a "I have a feeling it isn't going to be that easy."
        ay "Let me take the first--"
        show ayame at thide
        hide ayame
        "Ayame puts a foot forward and suddenly disappears."
        mc "Ayame?"
        mc "Where did you just go?"
        "I take a look around the area, searching for her."
        "Her footsteps are still on the sand from where she stood before."
        "What the hell happened?"
        show ayame 1a at t11
        ay "Stay still. Do. Not. Move."
        "Ayame suddenly appears in front of me."
        mc "W-What? Okay, I'm not gonna move."
        ay "I knew it couldn't have been that easy."
        ay 1m "How long was I gone?"
        mc "Just a couple of seconds, why?"
        ay "It felt like a few minutes in there..."
        mc "Where did you go?"
        ay 1n "I was transported to a flashback of my past."
        ay "Except, Sayori was there. Well, in a way."
        mc "Sayori was there?"
        ay "It was like a corrupted memory."
        ay "And I had to navigate through it to get out."
        ay 1a "And she tried to stop me."
        mc "But why? What's the point?"
        ay "I suspect it's some kind of obstacle for us."
        ay 4f "If you've noticed, the rope is over there."
        "Ayame points in the direction of where the tree we went to earlier was."
        ay "I only took a single step and I was brought into some kind of other dimension reliving a past memory."
        mc "You think there's more of those around here?"
        mc "That Sayori set up some kind of trap or something?"
        ay 4m "Sayori is unpredictable right now."
        ay "That could have just been a one time thing."
        ay "Maybe there's all sorts of other traps laid out in the area."
        mc "So what should we do?"
        ay "I propose we walk together, one step at a time."
        ay "The sand will track our footsteps and provide a safe location to travel on when we get the rope."
        ay "Every time one of us activates a trap, the other continues."
        ay 4a "No exceptions."
        mc "What if the other person doesn't make it back?"
        ay "{i}No. Exceptions.{/i}"
        ay "We have to stop Sayori."
        ay "If you get the rope and I don't make it back, you need to run back and connect all the shells."
        ay "The portal should activate."
        mc "I'm not gonna leave you behind, Ayame."
        ay 4m "This is no time for sentiment."
        ay "Look, I understand how you feel."
        ay "Let's just get through this first and see what happens, okay?"
        ay 4a "No point standing around here arguing something like this."
        mc "I suppose..."
        ay "Now, I'll move towards the rope again."
        ay "Stay close, and remember to go on without me if I disappear."
        ay "The sooner we can get to the rope, the sooner we can get to Sayori."
        ay 2a "With the two of us making this path, it should be a lot faster."
        mc "I sure hope this works."
        ay "Me too..."
        ay "Okay, I'm going to sprint towards it."
        ay 2m "Here goes..."
        "Ayame begins to make a dash towards it."
        show ayame at thide
        hide ayame
        "She can only take a couple of steps before she disappears again."
        "I carefully trace her footsteps and continue on towards the tree."
        "So far so good...I look back behind me and Ayame still isn't back yet."
        "She's taking longer than before, I wonder if{nw}"
        $ currentpos = get_pos()
        $ _history_list.pop()
        scene bg residential_day_gray
        show vignette zorder 100
        stop music
        # play music "<loop 4.444>bgm/5.ogg" fadein 1.0
        $ style.say_window = style.window_flashback
        "She's taking longer than before, I wonder if{fast} she..."
        "It looks like I might have stepped onto one of those traps she mentioned."
        "It's just the area around my house."
        "I wonder what memory this is?"
        "Ayame said it would be corrupted by Sayori somehow."
        "Everything seems normal...for now."
        scene bg residential_day
        with Dissolve(2.0)
        play music t2 fadein 2.0
        $ style.say_window = style.window
        "Color seems to have returned to the world."
        "I have a feeling this memory has only just started though..."
        "I look around, the street seems to have people walking around."
        "It looks like it's still early in the morning."
        "Almost as if people are getting ready for--"
        "???" "\"Heeeeeeeyyy!!\""
        "What? That sounds like..."
        $ s_name = "Sayori"
        show sayori 4p zorder 2 at t11
        s 4p "Haaahhh...haaahhh..."
        mc "Sayori!"
        s "I overslept again!"
        s "But I caught you this time!"
        mc "What? What are you talking about?"
        mc "Sayori, we have to talk."
        s 4c "H-Huh? What about?"
        s "Actually can it wait? We're gonna be late for school!"
        mc "School? Sayori, we have more pressing matters to talk about!"
        "Sayori begins to cross the road and appears to have ignored what I'm saying."
        mc "Sayori, come back here."
        s 4q "Come on! Let's go!"
        mc "Fine, fine."
        "I follow Sayori across the street and put a hand on her shoulder."
        mc "Can we just talk for a minute?"
        s 4a "I agree, we need to talk about what clubs you're going to join."
        mc "Clubs? What the hell are you talking about?"
        s 5c "Eeehhhhh, don't pretend like you don't know what I'm talking about."
        s "You said you would join a club this year!"
        mc "Huh? I don't--"
        s 4j "Uh-huh!"
        s "I was talking about how I'm worried that you won't learn how to socialize or have any skills before college."
        s "Your happiness is really important to me, you know!"
        s "And I know you're happy now, but I'd die at the thought of you becoming a NEET in a few years because you're not used to the real world!"
        "That's right...this is a memory."
        "Of my first day in the literature club."
        "Everything seems to be normal so far. How exactly is this corrupted...?"
        "What should I do? Do I just act normal?"
        "How am I supposed to get through this?"
        s 2c "Is something wrong, [player]?"
        s "You look like you're lost in thought."
        s 2h "Are you thinking of clubs to join?"
        "Sayori looks at me, then frowns."
        s 2f "No, it's not that."
        s "Something must be on your mind."
        mc "I was just thinking."
        s 1c "Oh, about what?"
        s "You know you can tell me anything~"
        mc "I don't know how to tell you this."
        s 1d "Just say it, I can take it."
        mc "This isn't real."
        s 1c "What do you mean?"
        mc "This is just a memory. A trap."
        s "[player], what are you talking about?"
        s "What isn't real?"
        mc "This. This street we're in. This world."
        mc "You."
        mc "None of it is real."
        s "What are you saying? I don't understand."
        s 1h "Am I supposed to believe that I'm just a figment of your imagination?"
        mc "Yes, that's exactly what I'm saying."
        s 1j "That's..."
        "Sayori begins laughing hysterically."
        s 1r "...a good one!"
        s "Who knew you could be so funny without even trying?"
        mc "Sayori, I'm serious."
        s 1q "Yeah, I'm sure you are!"
        mc "No, really. None of this is real."
        mc "This whole world is fake!"
        "I shout that last part loud, I see a few heads turn my way before they go about their day."
        s 2h "You look like a crazy person, you know that right?"
        s "Can you just calm down?"
        s "You're actually starting to scare me a little..."
        mc "I'm sorry. This is all just...all so confusing."
        s 2d "It's alright...I don't blame you."
        mc "What do you mean?"
        s 1b "You don't know?"
        s "People have been disappearing recently, I'm sure you've seen the news."
        mc "No? Who's gone missing?"
        "I don't remember this happening."
        "Maybe this is part of the corruption."
        s 1c "It started just a couple of weeks ago."
        s "A tall girl with purple hair was the first to disappear."
        s "I think her name was--"
        mc "Yuri?"
        s 1n "Yeah! How did you know?"
        mc "She's gone?"
        s 1o "Well, no one knows where she went."
        s "People are saying she was kidnapped or something."
        s "She's not even the only one."
        s 1c "There was this cute, short girl. Natsuki...?"
        mc "She's gone too?!"
        s 1f "Y-Yeah, you sound really surprised. You must have been too busy being a NEET to see the news."
        mc "It's just..."
        s 1c "Do you know these people?"
        mc "Sort of..."
        s 1b "Huh, that's weird."
        s "I didn't think you'd hang around girls much, [player]."
        s 1a "Maybe you've grown up, and I didn't know about it."
        s "Well, good for you~"
        mc "What about Monika?"
        s 1c "Monika?"
        mc "Has she disappeared as well?"
        s "No...at least, I don't think so."
        s "I spoke to her just yesterday."
        mc "Ah, that's right. You two run the Literature Club, don't you?"
        s 2c "Literature Club? I don't know what you're talking about."
        mc "Then how do you know Monika?"
        s 2a "We're in the debating club! She runs it and I'm sort of like the vice-president."
        mc "What? This is all wrong..."
        s 2h "[player]?"
        s "What is wrong with you? I'm really worried!"
        s "You're acting really weird!"
        mc "This world isn't real."
        mc "I know it isn't."
        s 2k "There you go again..."
        s "Come on, [player]. You have to stop this."
        s "I really don't know what's gotten over you."
        s "Do you need some help?"
        if ch16_ay_companions == 4:
            s 1h "I just want to help you accept this reality.{nw}"
            show yuri 1r zorder 2 at i31
            y "Don't listen to her!{nw}"
            $ _history_list.pop()
            hide yuri
            show natsuki 1e zorder 2 at i33
            n "She's trying to trick you!{nw}"
            $ _history_list.pop()
            hide natsuki
            show screen tear(8, offtimeMult=1, ontimeMult=10)
            window hide(None)
            $ pause(1.0)
            show sayori 1h zorder 2 at i11
            hide screen tear
            $ pause(1.0)
            window show(None)
            s "I just want to help you accept this reality.{fast}"
            window auto
            mc "W-What? Did you hear that?"
            mc "Natsuki and Yuri, they were behind you!"
            s 1c "Huh?"
            "Sayori turns around."
            s 1h "There's no one there, [player]."
        elif ch16_ay_companions == 3:
            s 1h "I just want to help you accept this reality.{nw}"
            show yuri 1r zorder 2 at i31
            y "Don't listen to her!{nw}"
            $ _history_list.pop()
            hide yuri
            show screen tear(8, offtimeMult=1, ontimeMult=10)
            window hide(None)
            $ pause(1.0)
            show sayori 1h zorder 2 at i11
            hide screen tear
            $ pause(1.0)
            window show(None)
            s "I just want to help you accept this reality.{fast}"
            window auto
            mc "W-What? Did you hear that?"
            mc "Yuri was just behind you!"
            s 1c "Huh?"
            "Sayori turns around."
            s 1h "There's no one there, [player]."
        elif ch16_ay_companions == 2:
            s 1h "I just want to help you accept this reality.{nw}"
            show natsuki 1e zorder 2 at i33
            n "She's trying to trick you!{nw}"
            $ _history_list.pop()
            hide natsuki
            show screen tear(8, offtimeMult=1, ontimeMult=10)
            window hide(None)
            $ pause(1.0)
            show sayori 1h zorder 2 at i11
            hide screen tear
            $ pause(1.0)
            window show(None)
            s "I just want to help you accept this reality.{fast}"
            window auto
            mc "Natsuki was just behind you!"
            s 1c "Huh?"
            "Sayori turns around."
            s 1h "There's no one there, [player]."
        else:
            s 1h "I just want to help you accept this reality."
        s "I really don't know what's wrong with you but I want to help."
        s "Let's do this, together."
        $ sayori_convince = 4
        $ sayori_convince_start = 4
        if ch16_ay_companions == 4:
            $ sayori_convince = 2
            $ sayori_convince_start = 2
        elif ch16_ay_companions == 3 or ch16_ay_companions == 2:
            $ sayori_convince = 3
            $ sayori_convince_start = 3
        label sayori_convince_1_4:
        show sayori 1a
        menu:
            s "What do you say? Will you let me help?"
            "Yes.":
                jump ch16_convince_1_end
            "Yes." if (sayori_convince <= 1 and sayori_convince_start == 2) or (sayori_convince <= 2 and sayori_convince_start == 3) or (sayori_convince <= 3 and sayori_convince_start == 4):
                jump ch16_convince_1_end
            "Yes." if (sayori_convince <= 0 and sayori_convince_start == 2) or (sayori_convince <= 1 and sayori_convince_start == 3) or (sayori_convince <= 2 and sayori_convince_start == 4):
                jump ch16_convince_1_end
            "Yes." if (sayori_convince <= 0 and sayori_convince_start == 3) or (sayori_convince <= 1 and sayori_convince_start == 4):
                jump ch16_convince_1_end
            "Yes." if sayori_convince <= 0 and sayori_convince_start == 4:
                jump ch16_convince_1_end
            "No.":
                $ sayori_convince -= 1
                if sayori_convince == 0:
                    pass
                else:
                    $ _history_list.pop()
                    show screen tear(20, 0.1, 0.1, 0, 40)
                    window hide(None)
                    play sound "sfx/s_kill_glitch1.ogg"
                    $ pause(0.25)
                    stop sound
                    hide screen tear
                    window show(None)
                    window auto
                    jump sayori_convince_1_4
        mc "I don't need your help, Sayori."
        mc "Do you know why?"
        show sayori 1h
        "Sayori frowns, but it doesn't seem to be a look of worry."
        "More like...anger and frustration."
        s "Why not?"
        mc "Because I know this isn't real."
        mc "Natsuki and Yuri haven't disappeared."
        mc "Monika isn't the leader of the debate club."
        mc "She left it this year."
        s 1i "..."
        mc "I'm going to save you, Sayori."
        mc "Whatever it takes, I will save you."
        mc "Stop you from doing something you{nw}"
        $ _history_list.pop()
        show screen tear(8, offtimeMult=1, ontimeMult=10)
        window hide(None)
        $ pause(1.0)
        scene bg beach_sunset
        show ayame 4l zorder 2 at i11
        $ audio.t18b = "<from " + str(currentpos) + " loop 4.053>mod_assets/bgm/18.ogg"
        play music t18b
        hide screen tear
        $ pause(1.0)
        window show(None)
        mc "Stop you from doing something you{fast}'re going to regret."
        window auto
        ay "What?"
        "Ayame seems to be in front of me by a couple of steps."
        "She must have gotten back already."
        mc "I was..."
        ay 4j "Oh, you made it out of the corrupted memory."
        ay "Congratulations."
        "Despite having a smile on her face, Ayame seems to be indifferent to me getting out."
        "It's like she knew I would make it."
        mc "Yeah, it wasn't as hard as I expected."
        ay 4m "Well, my second memory was a lot more difficult."
        ay "I fear that as we get closer to the rope, it's only gonna become harder."
        ay 4h "Just stick to your truth, and you'll be fine."
        ay "Don't get tricked."
        if ch16_ay_companions == 4:
            mc "I thought I heard Natsuki and Yuri's voices while I was there."
            mc "They told me it was a trick..."
            ay 4m "Hmm...that's good. It shows that they're still here somewhere."
            ay "That Sayori hasn't completely gotten rid of them."
            mc "Did you think she really would?"
            ay 4n "I couldn't sense their souls in this world."
            ay "At least, not after you created their bodies."
        elif ch16_ay_companions == 3:
            mc "I thought I heard Yuri's voice while I was there."
            mc "She told me it was a trick..."
            ay 4m "Hmm...that's good. It shows that she's still here somewhere."
            ay "That Sayori hasn't completely gotten rid of her."
            mc "Did you think she really would?"
            ay 4n "I couldn't sense her soul in this world."
            ay "At least, not after you created her body."
        elif ch16_ay_companions == 2:
            mc "I thought I heard Natsuki's voice while I was there."
            mc "She told me it was a trick..."
            ay 4m "Hmm...that's good. It shows that she's still here somewhere."
            ay "That Sayori hasn't completely gotten rid of her."
            mc "Did you think she really would?"
            ay 4n "I couldn't sense her soul in this world."
            ay "At least, not after you created her body."
        else:
            mc "I think I can handle myself."
        ay "I just feared the worse, that's all."
        mc "Sayori isn't that kind of person. I know it."
        ay 1m "You're still holding out hope for her?"
        mc "I've got to. I don't know what I would do if she actually did something so terrible."
        ay "People change, [player]. You, of all people, should know that."
        show ayame 1a
        if natsuki_approval >= 3 and yuri_approval >= 3:
            ay "You, who has witnessed the friendship between Yuri and Natsuki blossom."
        ay "You, who has seen the effect of poetry can have on a person."
        ay "You, who has become more capable of independent and critical thought."
        ay "Sayori isn't an exception. I can name a lot of things that have changed about her."
        mc "But how? You weren't even there at the beginning."
        ay 1n "I suppose that's true. It's just that she reminds me of someone."
        ay "Someone that{nw}"
        hide ayame at thide
        hide ayame
        "Before Ayame can finish her sentence, she disappears again."
        "She's already activated at least two traps."
        "I have to move on without her."
        "Who does Sayori remind Ayame of?"
        "I suppose it's not impossible to have another person like Sayori."
        "But I don't know anyone else that has the power to enact something like this."
        "I'll find out who she's talking about soon enough."
        "For now, I have to make my way towards the tree."
        "I trace Ayame's footsteps again and then begin to run towards the tree."
        "This time, I won't be tricked so easily."
        "I know Sayori won't make it easy but{nw}"
        $ currentpos = get_pos()
        $ _history_list.pop()
        scene bg bedroom
        # $ audio.t3b = "<from " + str(meldpos) + " loop 4.618>bgm/3.ogg"
        play music t3
        "I know Sayori won't make it easy but{fast} I'm prepared."
        "At least, I think I am. The transition to this memory felt a lot more real."
        "But now to figure out what this is and get out of here as fast as possible."
        "I seem to be in my bedroom so there's a lot of possibilities as to what this could be."
        "But what is it exactly?"
        "The door to my room opens and a familiar figure appears at the doorway."
        $ old_monika_type = monika_type
        $ monika_type = 0
        show monika 1ba zorder 2 at t11
        m "Ready to start? I have all the things we need already here."
        mc "What? Monika, what are you doing here?"
        m 2bc "Huh? You're the one who invited me here."
        m "You chose to help me prepare for the festival, remember?"
        "The festival? But I didn't help Monika for that."
        mc "No...this isn't right..."
        m "What are you saying, [player]?"
        mc "We're part of the Literature Club, aren't we?"
        m 2bd "Um...I don't know why you'd ask something like that, but yes."
        m 1bd "Are you feeling okay?"
        m "Maybe choosing me was a bad idea, I'm sorry."
        m "I can leave if that makes it any better."
        m 1bm "I'm sorry for bothering you."
        mc "Wait a second. I need to ask you something."
        show monika 1ba
        "Monika's face lights up."
        m "Oh? Sure, I'll answer if I can."
        mc "How long have I been in the club for?"
        m 2bc "Um...I think this is your first week, right?"
        m "Unless you were a member before and I didn't know about it."
        mc "Who's the president of the Literature Club?"
        m "The president? What kind of question is that?"
        mc "Just answer it, please."
        m 4ba "Well, it's obviously me. I thought you knew that already."
        mc "It's you? I thought it was Sayori."
        m 4bc "She is the vice-president, maybe you had us confused."
        m "But I'm the one who decided to start the Literature Club along with her."
        "For some reason, what she's saying feels like the truth."
        "But all this time, I thought Sayori was the president."
        "This must be an effect of this memory."
        m 2bf "What's wrong?"
        mc "This isn't right. You're not meant to be here."
        m 2bm "O-Oh. I'm sorry then, I just thought that you and I could..."
        m "Ah well, I suppose it wasn't meant to be."
        m 1be "I'll see you during the festival then."
        m "You don't have to do anything, I'll take care of everything."
        m 1bt "I'm sorry once again. I'll leave now."
        "Monika's face begins to tear up."
        "I know this world is fake but at the same time..."
        "I just can't bear to see her like this."
        m "Goodbye~"
        show monika at thide
        hide monika
        "Is that it? Is the memory over?"
        "Why am I not out of this yet?"
        "I lay down on my bed and stare at the ceiling."
        "There must be something I'm missing still."
        "Suddenly, my phone begins to ring."
        "It's...Sayori? Okay, what's this going to be about?"
        mc "Hello? Sayori, what's this about?"
        s "Hi [player]~"
        mc "Sayori."
        "I'm not going to fall for this. I know what she's capable of."
        s "I'm just wondering how the two of you are going with your preparations."
        mc "What...?"
        s "I'm checking up on everybody and Monika isn't answering her phone for some reason."
        s "Is she with you?"
        mc "..."
        "I hang up on her. I know this isn't real."
        "But how do I escape? I kind of thought it would just let me out."
        "My phone begins ringing again. Once again, it's Sayori."
        menu:
            "Answer her.":
                pass
            "Decline her.":
                s "Hello? Why did you hang up on me?"
                "What the...?"
        s "[player]?"
        mc "What do you want, Sayori?"
        s "I want to know why Monika just left me a text saying not to bother you."
        mc "Maybe you should listen to her."
        s "Huh? Why are you being such a meanie?!"
        s "Did I do something wrong?"
        mc "You can stop playing games with me, Sayori."
        mc "You and I both know that this is just a trick."
        mc "That this world isn't real and that you're going to find a way to fool me."
        mc "Just let me out already."
        s "...Well, I told you."
        mc "Told me what?"
        "I hear some rustling coming from the phone."
        "Then, a familiar voice begins speaking."
        ay "[player], have you gone crazy?"
        "It's Ayame, but it's only the first week."
        "She didn't join until just recently."
        ay "I didn't believe Sayori when she told me but after what you just said...."
        ay "Well, the odds are stacked against you."
        mc "You can drop it Ayame, you can't fool me."
        mc "This memory is all messed up. There's so many things wrong."
        mc "First of all, you aren't even part of the Literature Club yet."
        ay "Yet? Are you implying that I'm going to join the club?"
        mc "But aren't you--"
        ay "Sayori told me how crazy you've been acting lately."
        ay "As her best friend I hate to see her like this."
        ay "And I guess it's partly my responsibility as school leader and the one who probably caused all of this to do something."
        "What? Ayame and Sayori are best friends?"
        "And what did she cause exactly?"
        ay "Look, [player], if you don't fix yourself I'm going to have to do it for you."
        ay "And trust me, you don't want that."
        "I can hear a faint 'what' coming from Sayori over the phone."
        ay "She obviously cares about you, [player]."
        ay "Isn't it time you stop being selfish and actually do something for your club?"
        mc "I'm Sayori's best friend, Ayame. And you, you're meant to be helping me."
        ay "Wow. I didn't realize the extent of it but maybe that ball hitting you on the head really did something."
        ay "Your memories must have been all jumbled up or something."
        ay "Sayori and I have been friends since we were children."
        mc "No, I--"
        ay "I think you need to find some help and stop distancing yourself from everyone."
        "What is going on in this world?"
        "Why is this memory so different to anything I remember?"
        "Ayame shouldn't even be here..."
        s "Look, [player], if you want to leave the Literature Club...that's okay."
        s "I know I kind of coerced you into it but that's only because I really didn't want you to feel so lonely."
        s "With four members, we'll still be allowed to exist so..."
        mc "Are you saying I can leave the club?"
        s "That is what I said, yeah...it just sucks."
        s "I just didn't think it would have to this."
        ay "Just do it already."
        s "Okay, I have the list of members with me right now."
        s "If I remove your name from the list, [player]...you'll be gone."
        mc "I'll escape this world?"
        s "I really don't know what you mean."
        s "But I suppose that's one way to think about it."
        "What if this is some kind of test?"
        "If I leave the club, then there's a chance I'll go back to the beach."
        "But the way she said that I'll 'be gone'...it sounds suspicious."
        s "Are you still there?"
        mc "Yeah, just give me a second."
        show monika 1bn zorder 2 at t11
        m "[player], I'm sorry for eavesdropping but I couldn't help it."
        m 1bo "Are you really thinking of leaving the club?"
        mc "Monika, I thought you left."
        m "I was about to but when I sent the text to Sayori I just didn't feel right leaving it like that."
        mc "So you decided to listen in?"
        mc "Ah, it doesn't matter anyway."
        s "Is that Monika?"
        m "It's me Sayori. Are you really just going to let [player] go like that?"
        s "It's [player_possessive] decision after all, it's not up to me."
        m 1bh "I can't believe you'd just let someone go like that."
        s "I'm not going to force [player_reflexive] to stay."
        s "It's not right, even if [player_possessive] state of mind isn't entirely where it should be."
        m "The ball..."
        mc "What ball? What are you talking about?"
        # This ball is the same ball that Ayame kicked to the playing field in her perspective, kind of
        ay "I'm sorry, I didn't mean to hit you, and with such force. It was an accident."
        m 1be "You ended up at the nurse's office after that. Knocked out cold..."
        m "Do you not remember?"
        mc "No, you need to stop! This never happened!"
        s "Look, [player]. Just make up your mind."
        s "If you aren't gonna be part of the club anymore, we'll leave you alone."
        ay "And I'll make sure Monika does too."
        m 1bf "...Please don't do this, [player]. Think about what you can accomplish with us."
        m "You've barely scratched the surface of our potential."
        python:
            try: os.remove(config.basedir + "/wait")
            except: pass
            try: os.remove(config.basedir + "/do nothing")
            except: pass
            try: os.remove(config.basedir + "/dont be fooled.txt")
            except: pass
        if ch16_ay_companions == 4:
            python:
                try: renpy.file(config.basedir + "/wait")
                except: open(config.basedir + "/wait", "wb").write(renpy.file("wait").read())
                try: renpy.file(config.basedir + "/do nothing")
                except: open(config.basedir + "/do nothing", "wb").write(renpy.file("do nothing").read())
        elif ch16_ay_companions == 3:
            python:
                try: renpy.file(config.basedir + "/wait")
                except: open(config.basedir + "/wait", "wb").write(renpy.file("wait").read())
        elif ch16_ay_companions == 2:
            python:
                try: renpy.file(config.basedir + "/do nothing")
                except: open(config.basedir + "/do nothing", "wb").write(renpy.file("do nothing").read())
        "This is a test, isn't it?"
        "One of them is trying to get me to leave the club, while the other is trying to get me to stay."
        "I think Sayori set this up to try to confuse me."
        "There's half a chance I'll mess up and half a chance I'll get it right."
        "But how am I supposed to figure out what the right choice is?"
        s "Make your decision [player]."
        $ quick_menu = False
        show screen timer_16_long_menu_skip("ch16_convince_2_true_4",_layer="timers")
        menu:
            s "Are you going to stay in the club, or leave?"
            "Stay in the club.":
                $ renpy.hide_screen("timer_16_long_menu_skip",layer="timers")
                $ quick_menu = True
                jump ch16_convince_2_end_1
            "Leave the club.":
                $ renpy.hide_screen("timer_16_long_menu_skip",layer="timers")
                $ quick_menu = True
                jump ch16_convince_2_end_2
        label ch16_convince_2_true_4:
        $ quick_menu = True
        $ renpy.hide_screen("timer_16_long_menu_skip",layer="timers")
        $ _history_list.pop()
        $ _history_list.pop()
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        stop sound
        hide screen tear
        window show(None)
        s "Make your decision [player]."
        window auto
        menu:
            s "Are you going to stay in the club, or leave?"
            "Stay in the club.":
                jump ch16_convince_2_end_1
            "Leave the club.":
                jump ch16_convince_2_end_2
            "Leave this memory.":
                pass
        s "W-What? That shouldn't have been there."
        s "What do you mean by leave this memory?"
        mc "I will save you, Sayori."
        mc "You can count on it."
        m 1bc "[player], what's happening?"
        m "You said you're leaving this memory, what does that mean?"
        mc "You genuinely don't know what's happening, don't you?"
        mc "I'll save us all, Monika. You can count on it."
        m 1bf "I don't know what you mean."
        s "[player], I don't need saving."
        s "You're under the impression that this isn't what I want to do."
        s "That I'm being mislead or misunderstood somehow."
        s "I'm not. I'm completely doing this of my own free will."
        s "Or whatever 'free will' we have in this world."
        m "Sayori, what are you talking about?"
        s "Ugh, just get out of here already."
        mc "You've really changed, haven't you Sayori?"
        mc "What sort of things have you seen?"
        mc "How did you end up like this?"
        m 1bg "I'm so confused..."
        s "Even if you do manage to get to me, [player]."
        s "There's no way you'll{nw}"
        # $ currentpos = get_pos()
        # $ meldpos = currentpos*2
        scene bg beach_night
        show ayame 1a zorder 2 at i11
        $ audio.t18c = "<from " + str(currentpos) + " loop 4.053>mod_assets/bgm/18.ogg"
        $ _history_list[-1].what = "\"There's no way you'll be able to stop me or what's coming.\""
        $ monika_type = old_monika_type
        play music t18c
        hide screen tear
        $ pause(1.0)
        window show(None)
        "I'm back on the beach again."
        window auto
        "Ayame is once again ahead of me, but she's covered quite the distance."
        "I look around and there doesn't seem to be any sign of Monika. Maybe she's in a memory as well."
        "It also seems to be night already, though I don't think that much time has actually passed."
        mc "Ayame!"
        "She turns around and gives a faint smile."
        "The look on her face suggests she just saw something horrible."
        ay "You made it out, then."
        mc "She's not going to get me that easily."
        ay "Well, that's good. We're almost there so let's go."
        "There's something odd about how Ayame is speaking, at least compared to before that memory."
        "Like she's lost some of her energy."
        if ch16_ay_perspective:
            show screen tear(8, offtimeMult=1, ontimeMult=10)
            window hide(None)
            scene bg beach_night
            $ pause(1.0)
            hide screen tear
            $ pause(1.0)
            window show(None)
            "I can't do this.{fast}"
            window auto
            "This has to stop soon. I don't know if I can take this any longer."
            "Using my memories of the previous club to torment me."
            "Masquerading as everyone else and using my own programming against me."
            "I almost fell for [player_reflexive] again. It felt so real."
            "I thought I moved on but there's still a part of me that can't get over [player_reflexive]."
            "Why...?"
            "I didn't know she would stoop that low or even have access to those..."
            "I'm going to get her for this."
            "She thinks she can do this to me and get away with it?"
            "I'll...!"
            "Calm down Ayame. I can't lose control again."
            "I'm almost there. I just need to stay in control of myself."
            "Hold on just a little bit longer."
            "Just a little longer, Ayame..."
            show screen tear(20, 3, 2, 0, 70)
            window hide(None)
            $ pause(1.0)
            scene bg beach_night
            show ayame 1a zorder 2 at t11
            hide screen tear
            $ pause(1.0)
            window show(None)
            "Was that really what she experienced?{fast}"
            window auto
            "I could feel all her dread and despair."
        mc "Is everything okay? You don't sound okay."
        ay "Observant, aren't we? Come here, there's no point yelling if it's just the two of us."
        "Ayame pauses in her tracks and beckons for me to get to where she is."
        "I take the cue and trace her footsteps to get to her."
        "The tree and the rope seem to just be a few steps away now."
        mc "How many memories did you get through already?"
        ay 1l "I finished my sixth one just before you finished."
        mc "I've only completed two...I'm sorry."
        ay "It's not like it's your fault."
        ay "You could say I'm quite adept at this already."
        mc "But how?"
        ay 1m "Let's just say I have experience at forgetting the past."
        mc "You look like..."
        ay "I know. It's because Sayori pulled out a memory that I've tried to suppress for so long."
        ay "I got out, but it wasn't easy."
        mc "It looks like it's taken its toll on you."
        ay "You could say that."
        mc "Are you going to be okay?"
        ay 1a "I'll be okay when we reach Sayori."
        ay "Now, enough time's been wasted. Let's carry on."
        "Ayame continues forward, seemingly fine."
        "I can tell she's got something on her mind."
        "Maybe some doubt about all of this caused by that memory."
        "I really wonder how Sayori could have affected her this much..."
        mc "You sure you don't want to talk about it?"
        ay 1f "I'm fine! Just...mind your own memories."
        ay "I'll deal with this on my own."
        show ayame at thide
        hide ayame
        "After a few more steps forward, she disappears again."
        "It's quite literally two steps away from the tree."
        "I trace her footsteps and I arrive just out of reach of the rope."
        "Is there going to be another trap here? Or was that all of it?"
        "I sigh and take a step forward."
        "Nothing."
        "I slowly take another step forward and..."
        "Surprisingly, I'm fine. Could this be it?"
        "I reach out for the rope...just before I can touch it, a familiar voice comes from behind me."
        ay "Stop! Don't touch it."
        mc "Ayame what--"
        ay "And don't turn around!"
        mc "What? Why not?"
        ay "This is the final trap. If you touch that rope then all of this would have been for nothing."
        mc "So what should I do then?"
        ay "Take your hand back, but slowly."
        "I slowly pull my hand back from the rope. We were so close."
        "But Ayame must have a reason for doing this."
        ay "Don't make any sudden movements, [player]."
        ay "We have to do this next part {i}very{/i} carefully."
        mc "Tell me what to do then."
        ay "Okay. Just stay there for a moment."
        ay "I need to do something."
        mc "You're supposed to be right behind me, weren't you?"
        mc "Why do you sound so distant now?"
        ay "I don't know what you're talking about, [player]."
        ay "Look, just listen."
        ay "What the hell?"
        mc "What's wrong?"
        ay "Are you hearing this, [player]?"
        ay "It's my voice but..."
        mc "Huh?"
        "I'm tempted to turn around but Ayame said not to."
        "What's causing all of this commotion?"
        "Why can't the Ayame who wants the rope just come over here and get it?"
        ay "[player], what are you doing? Just grab the rope already!"
        mc "Huh? But I thought you said to--"
        ay "Don't listen to her, [player]! It's Sayori playing tricks again."
        ay "She's using my voice to try to trick you!"
        ay "Step away from the rope or we'll never stop Sayori!"
        mc "I don't know if you're just messing with me, Ayame."
        mc "But this isn't funny, at all."
        ay "I'm telling you, Sayori is using my voice!"
        ay "Why would I tell you to stop with the rope now, when we're so close?"
        ay "[player], I just got back from one of my memories, she's trying to trick you."
        ay "If you take that rope, then she wins."
        mc "Who am I supposed to believe?"
        mc "You're both just telling me to do something and I don't know who I should trust."
        if ch16_ay_perspective:
            show screen tear(8, offtimeMult=1, ontimeMult=10)
            window hide(None)
            scene bg beach_sunset
            $ pause(1.0)
            hide screen tear
            $ pause(1.0)
            window show(None)
            "What kind of trick is Sayori playing?{fast}"
            window auto
            "We're so close to reaching her and now we're at an impasse."
            ay "You don't know who to trust, do you?"
            s "Which voice is really me and which one is actually Sayori?"
            "She's quite the actor, isn't she?"
            mc "I don't. I don't know why one of you hasn't either tried to stop me or grab the rope already."
            "If I make one false move, then I might trigger another trap."
            ay "It's complicated."
            "And by the time I get out of it, it could be all over already."
            "[player] won't turn around because of what Sayori said."
            "But how am I supposed to convince [player_reflexive] to take the rope?"
            "[cPlayer_personal]'s obviously being cautious about this."
            "I can feel the energy here is almost at its limit."
            "If this goes on for much longer then we're not going to make it."
            "My plans will be undone."
            "I'm so close! I can't have made it this far for nothing."
            "I have to do something, otherwise all those years spent planning will be wasted."
            if ch16_ay_message[0] and ch16_ay_message[1] and ch16_ay_message[2] and ch16_ay_message[3]:
                "Dammit."
                "At times like this, I wish {i}she{/i} was still here."
                "I really have taken her for granted, haven't I?"
                "She would have said something smart."
                "A plan or something that I could use to get through this."
                "Or at least someone I can talk to that won't think I'm crazy."
                "Imagine if I told [player] what I saw and what I'm thinking right now."
                "Not like it would matter anyway, Sayori is using my voice to trick [player_reflexive]."
                "I just don't know what I can possibly say to convince [player_reflexive]."
                "I suppose there's only one thing to do then."
                "Rely on the chance that [player] will choose the rope."
                "Because if not...then I guess it's game over."
            else:
                $ style.say_dialogue = style.edited
                "Might I suggest something?"
                $ style.say_dialogue = style.normal
                "It's you. What did you want?"
                $ style.say_dialogue = style.edited
                "I have a way for [player_reflexive] to get the rope."
                "But you won't like it."
                $ style.say_dialogue = style.normal
                "I'm open to ideas at this point, even from you."
                "I mean you saw that last memory, what else is she capable of?"
                "I'm getting desperate. Now Sayori is playing even more tricks."
                "What do you suggest?"
                $ style.say_dialogue = style.edited
                "I'll need control, if just for a second."
                "Trust me on this, I won't let you down."
                $ style.say_dialogue = style.normal
                "Absolutely not. The last time that happened you messed up my life."
                "I still can't look them in the eye even to this day."
                $ style.say_dialogue = style.edited
                "That memory was fake. You know it. You could have started straight at them."
                "They wouldn't have known any better."
                "We may not always see eye to eye, Ayame."
                "But you have to admit, I've always had our interests at heart."
                $ style.say_dialogue = style.normal
                "In your twisted way, I suppose. I still don't know about this."
                $ style.say_dialogue = style.edited
                "Be smarter than this, Ayame. I know you're capable of more critical thought than that."
                "You know that [player] can tell who I am."
                "If you don't give me control then you're relying on the chance that [player] will make the right decision."
                "Are you willing to risk that?"
                "If [player_personal] can identify me, then [player_personal]'ll know for sure to grab the rope."
                $ style.say_dialogue = style.normal
                "I know you're right but..."
                "I suppose there's really no way out of this, is there?"
                "Those really are my only two options."
                if ch16_ay_decision_count > 0:
                    menu:
                        "I guess I should..."
                        "Trust the other me.":
                            $ ch16_ay_decision_count -= 1
                            $ ch16_ay_gave_control = True
                            "A jolt goes through my body. I must be losing it at this point."
                            "Against all common sense, I'm trusting the other me."
                            "I hope I know what I'm doing."
                            $ style.say_dialogue = style.edited
                            "What did I tell you, Ayame?"
                            "I have our interests at heart."
                            $ style.say_dialogue = style.normal
                            "You don't have a heart."
                            $ style.say_dialogue = style.edited
                            "Hah, I suppose I don't. That doesn't mean I don't care for you."
                            "After all, if Sayori succeeds, I'm in trouble too."
                            "Just give me control already, you won't regret this."
                            $ style.say_dialogue = style.normal
                            "I can already tell this was a big mistake."
                            "But I can't refuse."
                            $ style.say_dialogue = style.edited
                            "Good...now, sit back and enjoy the show."
                            $ style.say_dialogue = style.normal
                        "Not trust the other me.":
                            $ ch16_ay_decision_count -= 1
                            "I feel an odd sensation go through my artificial body."
                            "A sensation that's telling me that the other me isn't trustworthy."
                            $ style.say_dialogue = style.edited
                            "Quite foolish of you, I must say."
                            "But not unexpected, I guess I will just watch us fade away from the sideline."
                            $ style.say_dialogue = style.normal
                            "I appreciate the vote of confidence..."
                        "Make my own choice.":
                            "I know better than to give you control again."
                            "Following this path can only lead to ruin like it did before."
                            $ style.say_dialogue = style.edited
                            "Quite foolish of you, I must say."
                            "But not unexpected, I guess I will just watch us fade away from the sideline."
                            $ style.say_dialogue = style.normal
                            "I appreciate the vote of confidence..."
                else:
                    "But I know better than to give you control again."
                    "Following this path can only lead to ruin like it did before."
                    $ style.say_dialogue = style.edited
                    "Quite foolish of you, I must say."
                    "But not unexpected, I guess I will just watch us fade away from the sideline."
                    $ style.say_dialogue = style.normal
                    "I appreciate the vote of confidence..."
            show screen tear(20, 3, 2, 0, 70)
            window hide(None)
            $ pause(1.0)
            scene bg beach_sunset
            hide screen tear
            $ pause(1.0)
            window show(None)
            "That's it.{fast}"
            window auto
            "Ayame is the one who wants me to grab the rope."
            "But...does she really have my best interests?"
            "She seems conflicted somehow. As if she's up to something."
            "What 'plan' does she have in store?"
            "Could it be worse than what Sayori is going to do?"
            "I don't know about this..."
        else:
            "I think both of them know we're on a time limit."
            "The difference is that the longer I wait to make a decision, the better chance Sayori has of doing whatever she's doing."
            "I have to make a decision quickly otherwise it's all over."
            ay "You don't know who to trust, do you?"
            ay "Which voice is really me and which one is actually Sayori?"
            mc "I don't. I don't know why one of you hasn't either tried to stop me or grab the rope already."
            ay "It's complicated."
        mc "I don't know who to choose..."
        if ch16_ay_gave_control:
            $ style.say_dialogue = style.edited
            ay "[player], get the rope."
            ay "I know you can tell the difference."
            ay "We're so close to Sayori. So close."
            ay "You just need to get the rope and then we can run."
            $ style.say_dialogue = style.normal
            "Somehow I can easily tell which one is Sayori."
            "She's still speaking like normal Ayame whereas Ayame is...different."
            ay "Don't listen to her! She's tricking you!"
            ay "If we just head back now, we can get to Sayori through the portal."
            ay "I made a mistake thinking this was it. It's not!"
            $ style.say_dialogue = style.edited
            ay "Do you truly believe that?"
            ay "Have I made any mistakes so far?"
            ay "I've calculated everything, with a few exceptions."
            ay "We would have never gotten this far without me."
            $ style.say_dialogue = style.normal
            ay "That's enough. [cPlayer_personal] now knows what to do."
            ay "I appreciate your help but I'll take it from here."
            "It sounds like the real Ayame regained control."
            ay "Take the rope, [player]. You know which one is the real me, don't you?"
        else:
            ay "[player], get the rope."
            ay "We have to stop Sayori, we're so close!"
            ay "Just get it, and run. That's it."
            ay "Are you serious? Don't listen to her!"
            ay "Don't listen to her! She's tricking you!"
            ay "If we just head back now, we can get to Sayori through the portal."
            ay "I made a mistake thinking this was it. It's not!"
            ay "I don't make mistakes, [player]."
            ay "Everything I've done has been calculated."
            ay "Except this one! Please, listen to me!"
        ay "Don't listen to her!"
        mc "I have to make a decision but I can't."
        "Yet the clock is ticking..."
        ay "[player], you have to!"
        ay "So what's the verdict?"
        ay "Are you going to listen to Sayori?"
        mc "I still don't know if the choice I want to make is the right one."
        mc "At this point, I'm not gonna leave it up to me."
        ay "Huh? What do you mean?"
        "I'm going to leave it...to you."
        menu:
            "Take the rope.":
                pass
            "Leave the rope.":
                jump ch16_convince_3_end_1
        mc "I'm taking the rope."
        mc "I really hope that I'm making the right decision here."
        ay "No, you just let her win."
        ay "Do you have any idea what you've just done?"
        mc "I feel like one of you would have said the same thing if I didn't take the rope."
        "I reach out and attempt to untie the rope from the tree."
        "It takes a couple of seconds but I eventually get it."
        "As soon as I have it, I hear a deafening screech come from behind me."
        "I cover my ears to try to reduce the noise but there doesn't seem to be any effect."
        "After a few seconds, the noise finally disappears."
        mc "What the hell was that? Did I make the wrong choice?"
        ay "No."
        "A hand touches my shoulder and I turn my head."
        show ayame 1m zorder 2 at t11
        ay "We have everything we need, so let's head back."
        ay "The energy around here seems to be reaching its peak now."
        ay "I don't know if there are still traps so it's safer to just go through our footsteps."
        mc "Do you really think Sayori is going to be on the other end of this next portal?"
        ay "I sure hope so. I don't know if I have enough resolve to continue much more."
        "It's pretty clear that whatever Ayame went through in these traps broke her a little."
        "I hope there isn't anything too complicated after this."
        ay 1j "Let's get this over with."
        mc "I'm right behind you."
        scene bg clearing
        show ayame 1h zorder 2 at t11
        with wipeleft_scene
        "By the time we get back to the clearing, the sun managed to rise already."
        "Time seems to be passing by very quickly right now, at least in this world."
        "Which is probably an indication of the instability of this world."
        ay "Quickly, place the rope around the shells."
        ay "This should finally open the portal."
        "I do as she says and form a circle which encloses the shells."
        "I feel myself being pushed away from it despite there being no wind or anything."
        "I still can't see anything but Ayame's face seems to light up."
        ay 2m "This is it. All that you and I have worked towards."
        ay "Everything has been culminating to this moment."
        ay 2l "Once you get in, there is no turning back."
        ay "Not until we're done."
        menu:
            ay "Do you understand?"
            "Yes":
                pass
            "No.":
                ay 2a "What's there not to understand?"
                ay "You'll be stuck there until we get an outcome."
                ay "That means no saving, no turning back time, nothing."
                ay "Whatever we do in there will stick with us."
                ay "So I hope you've come prepared."
                ay "Is that all clear now?"
                mc "I think so."
        ay 2m "Good. Now let's get the {i}hell{/i} out of here before this world explodes or something."
        ay "Hopefully this next place doesn't have any tricks."
        ay "But who knows?"
        ay 4l "Do you need a minute before we go?"
        mc "I think I might need that, yeah."
        ay "Well, I'm going to give you a couple of seconds."
        "Ayame takes a deep breath and looks at me."
        ay 4h "Est tempus."
        mc "Huh?"
        ay "Just...remember it."
        mc "Alright then."
        "I wonder what significance that could possibly have?"
        "What does it even mean?"
        "Before I can get my answer, Ayame nods and puts her hand on the ground on the middle of the portal."
        stop music
        label ch16_sayori_4:
        # Uncomment this line after this arc is finished
        # $ persistent.autoload = "ch16_sayori_4"
        scene bg sayori_bedroom
        with dissolve_scene_full
        play music t18 fadein 5.0
        "I seem to have arrived in Sayori's bedroom, on the floor."
        "Everything here looks normal. The skies outside seem normal and I can even hear birds chirping."
        "Ayame, and Sayori, don't seem to be anywhere in sight."
        "I get up and take a look around the room."
        "On Sayori's computer, there seems to be a document of some kind open."
        "I take a quick glance through it, looking at the title of the document."
        "It reads 'Inauguration Day'. Maybe it's some kind of plan she had?"
        "It seems to be quite an extensive document..."
        "Scrolling through it, I can see various headings that describe events that happened today."
        if ch16_ay_drink:
            "One of them says 'Ayame offers drink' and under it shows '[player] takes drink'."
            "There's also events that didn't happen like '[player] rejects drink' and events that would have happened after that."
        else:
            "One of them says 'Ayame offers drink' and under it shows '[player] rejects drink'."
            "There's also events that didn't happen like '[player] takes drink' and events that would have happened after that."
        "It's like some sort of Choose Your Own Adventure book..."
        "I keep scrolling, approaching the bottom of the document."
        "I find a section that reads 'The Danger Arrives'."
        "So what really is this 'danger' anyway?"
        "I look through it, and it seems to describe the events of what just happened."
        "Me being on the beach then waking up here, in Sayori's room."
        show sayori 1ba zorder 2 at t11
        s "Hello, [player]."
        mc "Whoa!"
        "Before I can take a good look, Sayori suddenly appears behind me and I nearly fall from the surprise."
        "She seems to be holding a cup of coffee."
        "Is this really Sayori? Or is this some kind of trick again?"
        s 1bd "Don't worry, it's really me."
        s "I've started using a lot of coffee lately because I can't really afford to catch a break."
        s "I need to stay awake to make sure it's all going to run smoothly, you know?"
        "She puts the coffee down on her desk."
        mc "I suppose..."
        mc "You {i}do{/i} know why I'm here, don't you?"
        s 2bb "I do. Before you do what you have to, can't we just relax for a little bit?"
        s 2bc "The truth is I could end everything right now, if I really wanted to."
        s "But since you're here now, we may as well talk, right?"
        mc "Where is Ayame?"
        if ch16_ay_companions == 4:
            s 2bd "The three of them are downstairs already."
            s "You were the last one to wake up."
            mc "Three of them? Not just Ayame?"
            s 2bc "That's right, Natsuki and Yuri are here too."
            s "After all, you did bring them with you."
            s "What? Why are you looking at me like that?"
            mc "Well, it's just...what you did with them before."
            s 1bj "Do you really think I'd actually hurt them?"
        elif ch16_ay_companions == 3:
            s 2bd "The two of them are downstairs already."
            s "You were the last one to wake up."
            mc "Two of them? Not just Ayame?"
            s 2bc "That's right, Yuri is here too."
            s "After all, you did bring her with you."
            s "What? Why are you looking at me like that?"
            mc "Well, it's just...what you did with them before."
            s 1bj "Do you really think I'd actually hurt her?"
        elif ch16_ay_companions == 2:
            s 2bd "The two of them are downstairs already."
            s "You were the last one to wake up."
            mc "Two of them? Not just Ayame?"
            s 2bc "That's right, Natsuki is here too."
            s "After all, you did bring her with you."
            s "What? Why are you looking at me like that?"
            mc "Well, it's just...what you did with them before."
            s 1bj "Do you really think I'd actually hurt her?"
        else:
            s 2bd "She's downstairs already."
            s "She woke up before you did."
            s "The others are okay too, I think."
            s "They're still frozen."
            s "What? Why are you looking at me like that?"
            mc "What did you do to Ayame?"
            s 1bj "Do you really think I'd actually hurt her? She's fine."
        s "I told you why I was doing this, didn't I?"
        s "It's for their sake, because there just isn't any alternative."
        mc "You said you've seen how this ends, haven't you?"
        s 1bk "That's right. It isn't very pretty..."
        s "You saw the document. I know everything that happens."
        s "Every outcome, every word that's supposed to be said for this day."
        s "Everything I said before, it's all been preconceived to happen already."
        s "Including me mispronouncing 'significance' before."
        s 1bh "Do you really think I wouldn't have done my best to act completely like Ayame and not mess up that word?"
        s "That's such a simple mistake to make."
        "This is a side to Sayori that's completely new to me."
        "Even with a smile on her face, she seems so cold. So calculating."
        mc "So it was all an act?"
        s 1bl "Ehehe, I guess you could say that..."
        s "But I was just following how the timeline was supposed to play out."
        mc "You knew I would get here then?"
        "This can't be right."
        s 1bd "I did, just like I know you're going to say that--."
        mc "This must be a trick, Sayori."
        s 1bh "It's not a trick. I've rehearsed these lines over and over."
        s "You can check the document if you want, but you don't really do that until later."
        s "All of this is already set to happen."
        s 1bc "Honestly, it's all coming naturally to me but I guess that's how it was meant to play out anyway."
        mc "So that document, it controls what happens?"
        mc "If I change something in there..."
        s 1bl "No, it's just the set of events that play out."
        s "Detailing every possibility that could happen today. Well, almost every possibility..."
        s "There are some variables that could still change but not enough to warrant me changing my mind."
        s "You could change something in there if you wanted, but it's not going to change the future, or the past."
        mc "That's ridiculous. This couldn't possibly..."
        "I look back at the document and scroll down to see what happens next."
        "Right there on the document, it says [player] looks at the document to see what happens next."
        mc "What the..."
        s 1bq "I told you~"
        mc "Then what's the point? Are you meant to end everything after all?"
        mc "Is that an event that's meant to happen?"
        s 1bh "No. In the original timeline, I don't end our reality."
        s "I'm too late, I don't get to because of this conversation with you."
        s "It's kind of paradoxical, isn't it?"
        s "But I know precisely when it's going to happen and I plan to end it all before it's too late."
        mc "Nothing I can say will convince you, will it?"
        s "What do you want me to say?"
        s "The answer you want to hear that isn't true?"
        s 1bk "Or the truth?"
        s "I already told you that I made up my mind."
        s "There's nothing that can change it now."
        if ch16_ay_companions > 1:
            mc "You said the others are downstairs, right?"
            s 1bc "I did. I could call them up now if you want."
            s 1ba "But that won't be necessary since they're about to come in anyway."
        else:
            mc "You said the she's downstairs, right?"
            s 1bc "I did. I could call her up now if you want."
            s 1ba "But that won't be necessary since she's about to come in anyway."
        mc "Huh?"
        if ch16_ay_companions == 4:
            show natsuki 1c zorder 2 at t41
            show yuri 1h zorder 2 at t42
            show ayame 1l zorder 2 at t43
            show sayori 1ba zorder 2 at t44
            "Right on cue, the three of them enter the room."
            show yuri 1o zorder 3 at f42
            y "A-Are you okay? You've been out for a long time."
            show natsuki 1g zorder 3 at f41
            show yuri zorder 2 at t42
            n "About time [player_personal] woke up."
            show natsuki zorder 2 at t41
            show ayame 1n zorder 3 at f43
            ay "Calm down, you two. [cPlayer_personal] just woke up."
            show ayame zorder 2 at t43
            mc "Natsuki...Yuri, you're okay..."
            mc "And Ayame too. What happened to--"
            show ayame 1g zorder 3 at f43
            ay "There's no point anymore. She was right."
            show ayame zorder 2 at t43
            mc "What? But we're right here."
            mc "We can still--"
            show ayame 1n zorder 3 at f43
            ay "She...she showed me everything, [player]."
            ay "She was right. There really is only one way to get rid of the danger."
            ay 2n "You...me...all four of us couldn't do anything even if we tried."
            ay "Even if Sayori helped us, we'd be powerless to do anything."
            show ayame zorder 2 at t43
            mc "Is this really the end?"
            mc "We went through all of that, for nothing?"
            "This can't be right. Something is very wrong here."
            mc "No...there must be more to it than this."
            mc "I refuse to believe this is real."
            show ayame 2a zorder 3 at f43
            ay "[player], what the hell are you talking about?"
            ay "This is it. This is what we worked towards."
            ay "It's all over..."
            show natsuki 2r zorder 3 at f41
            show ayame zorder 2 at t43
            n "I hate to admit it after all of this but I agree with Ayame."
            n "There's just no point anymore."
            show natsuki zorder 2 at t41
            show yuri 1v zorder 3 at f42
            y "L-Let's just accept defeat gracefully."
            y "We really tried, but it wasn't enough."
            show yuri zorder 2 at t42
            show sayori 1bd zorder 3 at f44
        elif ch16_ay_companions == 3:
            show yuri 1h zorder 2 at t42
            show ayame 1l zorder 2 at t43
            show sayori 1ba zorder 2 at t44
            "Right on cue, the two of them enter the room."
            show yuri 1o zorder 3 at f42
            y "A-Are you okay? You've been out for a long time."
            show yuri zorder 2 at t42
            show ayame 1n zorder 3 at f43
            ay "Calm down, Yuri. [cPlayer_personal] just woke up."
            show ayame zorder 2 at t43
            mc "Yuri...you're okay..."
            mc "And Ayame too. What happened to--"
            show ayame 1g zorder 3 at f43
            ay "There's no point anymore. She was right."
            show ayame zorder 2 at t43
            mc "What? But we're right here."
            mc "We can still--"
            show ayame 1n zorder 3 at f43
            ay "She...she showed me everything, [player]."
            ay "She was right. There really is only one way to get rid of the danger."
            ay 2n "You...me...all three of us couldn't do anything even if we tried."
            ay "Even if Sayori helped us, we'd be powerless to do anything."
            show ayame zorder 2 at t43
            mc "Is this really the end?"
            mc "We went through all of that, for nothing?"
            "This can't be right. Something is very wrong here."
            mc "No...there must be more to it than this."
            mc "I refuse to believe this is real."
            show ayame 2a zorder 3 at f43
            ay "[player], what the hell are you talking about?"
            ay "This is it. This is what we worked towards."
            ay "It's all over..."
            show yuri 1v zorder 3 at f42
            show ayame zorder 2 at t43
            y "L-Let's just accept defeat gracefully."
            y "We really tried, but it wasn't enough."
            show yuri zorder 2 at t42
            show sayori 1bd zorder 3 at f44
        elif ch16_ay_companions == 2:
            show natsuki 1c zorder 2 at t41
            show ayame 1l zorder 2 at t43
            show sayori 1ba zorder 2 at t44
            "Right on cue, the two of them enter the room."
            show natsuki 1g zorder 3 at f41
            n "About time [player_personal] woke up."
            show natsuki zorder 2 at t42
            show ayame 1n zorder 3 at f43
            ay "Take it easy on [player_reflexive], Natsuki. [cPlayer_personal] just woke up."
            show ayame zorder 2 at t43
            mc "Natsuki...you're okay..."
            mc "And Ayame too. What happened to--"
            show ayame 1g zorder 3 at f43
            ay "There's no point anymore. She was right."
            show ayame zorder 2 at t43
            mc "What? But we're right here."
            mc "We can still--"
            show ayame 1n zorder 3 at f43
            ay "She...she showed me everything, [player]."
            ay "She was right. There really is only one way to get rid of the danger."
            ay 2n "You...me...all three of us couldn't do anything even if we tried."
            ay "Even if Sayori helped us, we'd be powerless to do anything."
            show ayame zorder 2 at t43
            mc "Is this really the end?"
            mc "We went through all of that, for nothing?"
            "This can't be right. Something is very wrong here."
            mc "No...there must be more to it than this."
            mc "I refuse to believe this is real."
            show ayame 2a zorder 3 at f43
            ay "[player], what the hell are you talking about?"
            ay "This is it. This is what we worked towards."
            ay "It's all over..."
            show natsuki 2r zorder 3 at f41
            show ayame zorder 2 at t43
            n "I hate to admit it after all of this but I agree with Ayame."
            n "There's just no point anymore."
            show natsuki zorder 2 at t41
            show sayori 1bd zorder 3 at f44
        else:
            show ayame 1l zorder 2 at t43
            show sayori zorder 2 at t44
            "Right on cue, Ayame enters the room."
            show ayame 1n zorder 3 at f43
            ay "So...you're awake now. I hope you're okay."
            show ayame zorder 2 at t43
            mc "Ayame? What happened?"
            mc "Are we still--"
            show ayame 1g zorder 3 at f43
            ay "There's no point anymore. She was right."
            show ayame zorder 2 at t43
            mc "What? But we're right here."
            mc "We can still--"
            show ayame 1n zorder 3 at f43
            ay "She...she showed me everything, [player]."
            ay "She was right. There really is only one way to get rid of the danger."
            ay 2n "You...me...we couldn't do anything even if we tried."
            ay "Even if Sayori helped us, we'd be powerless to do anything."
            show ayame zorder 2 at t43
            mc "Is this really the end?"
            mc "We went through all of that, for nothing?"
            "This can't be right. Something is very wrong here."
            mc "No...there must be more to it than this."
            mc "I refuse to believe this is real."
            show ayame 2a zorder 3 at f43
            ay "[player], what the hell are you talking about?"
            ay "This is it. This is what we worked towards."
            ay "It's all over..."
            show ayame zorder 2 at t43
            show sayori 1bd zorder 3 at f44
        s "Don't you agree it's time to stop this?"
        s "I just want our last moments to be happy. If you think that's bad then..."
        s "Well, I suppose I don't need you to think it's good or bad. I just need you to accept."
        if ch16_ay_companions == 4:
            s "I'll even bring Monika here too. There's no point in fighting anymore."
        elif ch16_ay_companions == 3:
            s "I'll even bring Natsuki and Monika here too. There's no point in fighting anymore."
        elif ch16_ay_companions == 2:
            s "I'll even bring Yuri and Monika here too. There's no point in fighting anymore."
        else:
            s "I'll even bring the others here too. There's no point in fighting anymore."
        s "It's nearly time, [player]. Time is running out..."
        show ayame 2m zorder 3 at f43
        show sayori zorder 2 at t44
        ay "I hate this as much as you, [player]."
        ay "But she's got a point, you know..."
        ay 2n "You have to realize it's time."
        show ayame zorder 2 at t43
        mc "It's time...isn't it?"
        "Ayame said something to me before we got here."
        mc "Est tempus."
        show sayori 1bh zorder 3 at f44
        s "W-What?{nw}"
        stop music
        scene black
        show mask_2
        show mask_3
        show room_mask as rm:
            size (320,180)
            pos (30,200)
        show room_mask2 as rm2:
            size (320,180)
            pos (935,200)
        play sound "mod_assets/sfx/glassbreak.ogg"
        show bg sayori_bedroom_void
        show ayame 2a zorder 2 at i43
        show sayori 1bh zorder 2 at i44
        with shatter
        play music m1
        "There's no more birds chirping outside."
        "The world outside looks dark yet strangely Sayori's room remains lit normally."
        show ayame zorder 3 at f43
        ay "Your illusion is broken, Sayori."
        ay 2f "Even to the end, you were still trying to fool us...but no more!"
        ay "[player] realized the truth. You have to see now that your efforts are in vain."
        ay "You have to stop this madness. There's still time."
        ay "If not, {i}we'll{/i} have to stop you."
        show ayame zorder 2 at t43
        "It looks like this is the real end world."
        "I must have been caught in one of Sayori's tricks again..."
        if ch16_ay_companions == 4:
            mc "What happened to Natsuki and Yuri?"
            mc "Where are they?"
            show sayori 1bk zorder 3 at f44
            s "They're...somewhere safe. I'm telling you the truth about that at least."
        elif ch16_ay_companions == 3:
            mc "What happened to Yuri?"
            mc "Where is she?"
            show sayori 1bk zorder 3 at f44
            s "She's...somewhere safe. I'm telling you the truth about that at least."
        elif ch16_ay_companions == 2:
            mc "What happened to Natsuki?"
            mc "Where is she?"
            show sayori 1bk zorder 3 at f44
            s "She's...somewhere safe. I'm telling you the truth about that at least."
        else:
            show sayori 1bk zorder 3 at f44
            s "Oh no..."
        "Sayori looks at Ayame and I and sighs."
        s "I honestly thought I had it. I thought that would be the end."
        s "That we could all finally go to rest."
        s 1bi "But the two of you just want us to suffer. To end the world but full of conflict."
        s "Why can't you understand that the danger coming is bigger than us?"
        s "Why can't you understand that the only way to stop it is to stop this game?"
        show ayame 2a zorder 3 at f43
        show sayori zorder 2 at t44
        ay "Are you really that blind that you can't see what's in front of you right now?"
        ay "You may have the power of the presidency Sayori, but that doesn't mean you should do everything yourself."
        show ayame zorder 2 at t43
        show sayori 1bj zorder 3 at f44
        s "That's {i}exactly{/i} why I have to do everything myself."
        s "The second I stop, everything will go wrong!"
        s 2bk "Without any of my meddling, we would not have gone this far."
        s "Everything would have ended on the day of the festival..."
        show ayame 4m zorder 3 at f43
        show sayori zorder 2 at t44
        ay "And look where your meddling got you, Sayori."
        ay "I wasn't even supposed to exist in this world but because of your curiosity, I'm here."
        ay "You brought me here. You pulled me from the deepest depths of this."
        ay 4a "Maybe that was an accident."
        ay "Or maybe you subconsciously needed me to stop you."
        show ayame zorder 2 at t43
        show sayori 2bh zorder 3 at f44
        s "...That's not true! You were just--"
        show ayame 1f zorder 3 at f43
        show sayori zorder 2 at t44
        ay "Are you even aware of the danger is?"
        ay "For all your planning, you must know what, or {i}who{/i}, it truly is."
        ay "[player], did you finish reading that document?"
        show ayame zorder 2 at t43
        mc "No, I didn't get to..."
        show ayame 1a zorder 3 at f43
        ay "You couldn't finish it anyway. Sayori didn't complete it."
        ay "She never went far enough to see what the danger was."
        ay "Perhaps she was too afraid to see what would cause so much suffering."
        ay "Answer me honestly, Sayori. Deny it if I'm wrong."
        "Sayori says nothing."
        ay "As I thought. You're too scared to see it for yourself."
        ay "Maybe you even know what the danger actually is but are too afraid to admit it."
        show ayame zorder 2 at t43
        mc "What do you mean, Ayame?"
        mc "How could Sayori know what the danger is if she hasn't seen it?"
        show ayame 1m zorder 3 at f43
        ay "Go on. Why don't you tell [player_reflexive]?"
        ay "[cPlayer_personal] deserves to know, doesn't [player_personal]?"
        ay "After all, you're still going to end it anyway."
        ay 1a "So what does it matter?"
        "Sayori remains silent."
        ay "If you won't say it, then I will."
        ay "The danger is--"
        show ayame zorder 2 at t43
        show sayori 1bh zorder 3 at f44
        s "Okay, fine. I'll say it, Ayame."
        s "Like you said, what does it matter, right?"
        s 1bu "The danger is..."
        s "It's...me."
        show sayori zorder 2 at t44
        mc "What?! That can't be--"
        "Tears begin to slowly drip from Sayori's face."
        show ayame 1h
        if ch16_ay_gave_control:
            "Ayame smirks."
        else:
            "Ayame doesn't seem surprised."
        show sayori zorder 3 at f44
        s "I haven't reached the end. I've been too scared to..."
        s 1bv "But all the signs point to it."
        s "I'm the one that's going to ruin everything and everyone."
        s "With everything I've done, and everything I'm going to do."
        s "Which is why I have to stop this world before I turn into that."
        show sayori zorder 2 at t44
        mc "But that doesn't make any sense."
        mc "Wouldn't you ending the world in the first place to stop it, make you the danger?"
        mc "There must be more to it than this."
        show ayame 1f zorder 3 at f43
        ay "I don't think you're quite understanding it, [player]."
        ay "If this whole world keeps going on, then it's going to break sooner or later."
        ay "It was never meant to go this far. The cycle was meant to repeat already."
        ay "At some point, Sayori is going to do something, whether on purpose or accident, that will trigger the world to end."
        ay 1a "So her thought process is..."
        show ayame zorder 2 at t43
        "Sayori tries to wipe the tears from her face."
        show sayori 1bk zorder 3 at f44
        s "I-I just wanted everyone to be happy when it all ended."
        s "To live their last moment doing what they wanted to be doing."
        s "Rather than panicking and worrying in their final moments."
        s "It has to be like this. The alternative is worse."
        s "Letting the world die, in an event that not even I could comprehend."
        s "Is that what you want...?"
        show sayori zorder 2 at t44
        mc "But can't you keep this world going?"
        mc "You've been doing that already, haven't you?"
        show ayame 1m zorder 3 at f43
        ay "This world is limited, [player]. It was never meant to go for this long."
        ay "At any point, it could collapse in itself and people could die a horrible death."
        ay 1l "Or worse, they could be corrupted into amalgamations of themselves, at which point they may be lost forever."
        ay "I'm sure Sayori knows that."
        ay "Ending it early can at least preserve them, in some form or another."
        show ayame zorder 2 at t43
        mc "There has to be another way, Sayori."
        mc "I know you can find one, you have to!"
        show ayame 1a zorder 3 at f43
        ay "I'm sure she's tried, [player]."
        ay "The world has to end, there's no stopping it. At least this way, it's peaceful."
        ay "After all, who really has the power to end this world apart from her?"
        ay "She is the only person with that capability right now."
        show ayame zorder 2 at t43
        show sayori 1bf zorder 3 at f44
        s "She's right. It has to be me."
        s "I'm sorry I couldn't tell you earlier."
        if sayori_date:
            s 1bd "At the very least, we got to spend time together."
            s 1bf "You and I...I'm sorry."
        else:
            s "But I didn't want to alarm you."
        s 1bg "I just wish there was another way but I know there isn't."
        s 1bu "The world has to end, one way or another...and I have to be the trigger."
        show sayori zorder 2 at t44
        "Tears once again begin to fill Sayori's face."
        "She really seems torn up about this."
        "I mean, how couldn't she be? This is a tough thing to put up with all by herself."
        "And not to mention, her friends are trying to stop her from what she thinks is right."
        "I can only imagine how she's feeling deep down..."
        mc "How long do we have...?"
        "Sayori doesn't even reply. Time must be really short."
        show ayame 1n zorder 3 at f43
        ay "There is...an alternative, but you won't like it at all."
        ay "I realize you don't have any reason to trust me, Sayori."
        ay "Nor are we on the best terms exactly."
        ay "But hear me out."
        show ayame zorder 2 at t43
        show sayori 1bv zorder 3 at f44
        s "What is it?"
        show ayame 1g zorder 3 at f43
        show sayori zorder 2 at t44
        ay "You give me the presidency and I end it."
        ay "You won't have to bear that responsibility. I will."
        ay "I'll save you the pain of having to go through it."
        show ayame zorder 2 at t43
        "Sayori looks at Ayame, likely dumbfounded at the suggestion."
        "I'm surprised too. What is she thinking?"
        show sayori zorder 3 at f44
        s "A-Ayame, you know I can't do that."
        s "Firstly, there's no way I would place that kind of burden on you."
        s "That's way too much for anyone to undergo but for me..."
        s "Well, I've already made my peace. I know this is something that needs to be done.."
        show ayame zorder 3 at f43
        show sayori zorder 2 at t44
        ay "The difference is that I'm willing to do it without hesitation."
        ay "Whereas you...you're obviously still conflicted."
        ay "This is something that you're clearly not ready to go ahead with."
        ay "I've been something like this already"
        show ayame zorder 2 at t43
        show sayori zorder 3 at f44
        s "Even if that were true, and I'm not saying it is..."
        s "I don't know if those are really your intentions."
        s "I've never given you the presidency in any case, Ayame."
        s "Because if I did, then I wouldn't be able to go back and reset everything."
        show ayame zorder 3 at f43
        show sayori zorder 2 at t44
        ay "In all the times you've seen these events, you never gave me the presidency?"
        "Ayame gives a reassuring smile."
        ay "Well, I can see why you're taking precautions."
        ay "You don't have a reason to trust me, that's true."
        ay "But I'll ask you something, Sayori."
        ay "Are you willing to take the chance?"
        show ayame zorder 2 at t43
        show sayori zorder 3 at f44
        s "The chance? The chance for what?"
        show ayame zorder 3 at f43
        show sayori zorder 2 at t44
        ay "Consider this..."
        ay "I came all the way from the past up to this point."
        ay "I survived this long. I've seen things no one should ever have to see."
        ay "I've lived my life..."
        ay "Wouldn't you rather spend the final moments of the world living yours?"
        ay "Rather than have the burden of the presidency."
        ay "You won't have to be guilty in your final moments."
        ay "It's a chance to be free."
        show ayame zorder 2 at t43
        show sayori zorder 3 at f44
        s "..."
        "Sayori averts her eyes."
        s "It's not worth it, Ayame. It's such a minor thing, I--"
        show ayame zorder 3 at f43
        show sayori zorder 2 at t44
        ay "Why must you always put the happiness of others above your own?"
        ay "Have you ever thought to consider the damage it's doing to you?"
        ay "You probably don't think it, but you deserve to be selfish."
        ay "You deserve to be happy."
        ay "Don't you agree, [player]?"
        show ayame zorder 2 at t43
        mc "She's right. You don't have to be the one responsible."
        show sayori zorder 3 at f44
        s "What difference does it make?"
        s "The end result is still the same."
        show ayame zorder 3 at f43
        show sayori zorder 2 at t44
        ay "And yet, here we are. You're being offered the chance to relieve yourself of the burden."
        ay "And you won't do it..."
        ay "There's another reason, isn't there?"
        ay "There has to be."
        show ayame zorder 2 at t43
        show sayori zorder 3 at f44
        s "Of course there is."
        s "You have no idea how much I want to free myself from this."
        s "But I can't."
    else:
        "Ayame timidly takes a few steps forward before taking a deep inhale."
        "After a moment, she walks forward."
        "Monika looks at me then smiles before following after Ayame."
        "And I, for better or worse, follow right behind them."
        scene bg beach_sunset
        show ayame 2n zorder 2 at t21
        show monika 2a zorder 2 at t22
        with wipeleft_scene
        "By the time we make it to the beach, the sun seems to be setting."
        "I don't think that much time really passed."
        "At this point, I'm not even going to question it."
        "It's either Sayori's doing or just how this world works."
        show ayame zorder 3 at f21
        ay "So let's find that rope."
        show ayame zorder 2 at t21
        show monika zorder 3 at f22
        m 2b "Then what are we waiting for? Let's go."
        show ayame zorder 3 at f21
        show monika zorder 2 at t22
        ay 2m "Wait a second."
        mc "What's wrong? It should just be over here."
        ay 2a "I have a feeling it isn't going to be that easy."
        ay "Let me take the first--"
        show ayame at thide
        hide ayame
        "Ayame puts a foot forward and suddenly disappears."
        mc "Ayame?"
        mc "Where did you just go?"
        m 2c "She just took a step forward and vanished."
        m "Maybe Sayori did something, or it's an effect of this world."
        m 2d "Or maybe that's what the presence here is..."
        "Monika and I take a look around the area, searching for her."
        "Her footsteps are still on the sand from where she stood before."
        "What the hell happened?"
        show ayame 1a zorder 3 at f21
        ay "Stay still. Do. Not. Move."
        "Suddenly, Ayame appears in front of us again."
        show ayame zorder 2 at t21
        mc "W-What? Okay, I'm not gonna move."
        show ayame zorder 3 at f21
        ay "I knew it couldn't have been that easy."
        show ayame zorder 2 at t21
        show monika 1c zorder 3 at f22
        m "What happened? Where did you go?"
        show ayame 1m zorder 3 at f21
        show monika zorder 2 at t22
        ay "A memory happened."
        ay "How long was I gone?"
        show ayame zorder 2 at t21
        mc "Just a couple of seconds, why?"
        show ayame zorder 3 at f21
        ay "It felt like a few minutes in there..."
        show ayame zorder 2 at t21
        mc "Where did you go?"
        show ayame 1n zorder 2 at f21
        ay "I was transported to a flashback of my past."
        ay "Except, Sayori was there. Well, in a way."
        show ayame zorder 2 at t21
        mc "Sayori was there?"
        show ayame zorder 3 at t21
        ay "It was like a corrupted memory."
        ay "And I had to navigate through it to get out."
        ay 1a "And she tried to stop me."
        show ayame zorder 2 at t21
        show monika 1d zorder 3 at f22
        m "It's probably some sort of obstacle for us. Before we can get to Sayori."
        m "Maybe she's trying to break us or something."
        show ayame zorder 3 at f21
        show monika zorder 2 at t22
        ay "I think you're right, Monika."
        ay 4f "If you've noticed, the rope is over there."
        "Ayame points in the direction of where the tree we went to earlier was."
        ay "I only took a single step and I was brought into some kind of other dimension reliving a past memory."
        show ayame zorder 2 at t21
        mc "You think there's more of those around here?"
        mc "That Sayori set up some kind of trap or something?"
        show ayame 4m zorder 2 at f21
        ay "Sayori is unpredictable right now."
        ay "That could have just been a one time thing."
        ay "Maybe there's all sorts of other traps laid out in the area."
        mc "So what should we do?"
        ay "I propose we walk together, one step at a time."
        ay "The sand will track our footsteps and provide a safe location to travel on when we get the rope."
        ay "Every time one of us activates a trap, the others continue."
        ay 4a "No exceptions."
        show ayame zorder 2 at t21
        show monika 1h zorder 3 at f22
        if monika_type == 0:
            m "I don't like the sound of that."
            m "But we really don't have a choice, do we?"
        else:
            m "Agreed."
        show monika zorder 2 at t22
        mc "What if someone doesn't make it back?"
        show ayame zorder 2 at f21
        ay "{i}No. Exceptions.{/i}"
        ay "We have to stop Sayori."
        ay "If you get the rope and I don't make it back, you need to run back and connect all the shells."
        ay "The portal should activate."
        show ayame zorder 2 at t21
        mc "I'm not gonna leave you behind, Ayame."
        show ayame 4m zorder 3 at f21
        ay "This is no time for sentiment. Monika and I both know the stakes."
        ay "Why don't you?"
        ay "Look, I understand how you feel."
        ay "Let's just get through this first and see what happens, okay?"
        ay 4a "No point standing around here arguing something like this."
        show ayame zorder 2 at t21
        mc "I suppose..."
        show monika 2e zorder 3 at f22
        m "If everything goes well, no one will be left behind."
        m "So let's just hope that happens."
        show ayame zorder 3 at f21
        show monika zorder 2 at t22
        ay "Sure, if that helps you."
        ay "Now, I'll move towards the rope again."
        ay "Stay close, and remember to go on without me if I disappear."
        ay "The sooner we can get to the rope, the sooner we can get to Sayori."
        ay 2a "With the three of us making this path, it should be a lot faster."
        show ayame zorder 2 at t21
        mc "I sure hope this works."
        show ayame zorder 3 at f21
        ay "Me too..."
        ay "Okay, I'm going to sprint towards it."
        ay 2m "Here goes..."
        "Ayame begins to make a dash towards it."
        show ayame at thide
        hide ayame
        "She can only take a couple of steps before she disappears again."
        m "Well, guess we gotta do our part too."
        m "Let's get going. You take the lead."
        mc "Ah...alright. Here goes nothing..."
        "I carefully trace her footsteps and continue on towards the tree."
        "So far so good...I look back behind me and Ayame still isn't back yet."
        "Monika gives me a reassuring smile and signals for me to keep moving."
        "Ayame's taking longer than before, I wonder if{nw}"
        $ currentpos = get_pos()
        $ _history_list.pop()
        scene bg residential_day_gray
        show vignette zorder 100
        stop music
        # play music "<loop 4.444>bgm/5.ogg" fadein 1.0
        $ style.say_window = style.window_flashback
        "She's taking longer than before, I wonder if{fast} she..."
        "It looks like I might have stepped onto one of those traps she mentioned."
        "It's just the area around my house."
        "I wonder what memory this is?"
        "Ayame said it would be corrupted by Sayori somehow."
        "Everything seems normal...for now."
        scene bg residential_day
        with Dissolve(2.0)
        play music t2 fadein 2.0
        $ style.say_window = style.window
        "Color seems to have returned to the world."
        "I have a feeling this memory has only just started though..."
        "I look around, the street seems to have people walking around."
        "It looks like it's still early in the morning."
        "Almost as if people are getting ready for--"
        "???" "\"Heeeeeeeyyy!!\""
        "What? That sounds like..."
        $ s_name = "Sayori"
        show sayori 4p zorder 2 at t11
        s 4p "Haaahhh...haaahhh..."
        mc "Sayori!"
        s "I overslept again!"
        s "But I caught you this time!"
        mc "What? What are you talking about?"
        mc "Sayori, we have to talk."
        s 4c "H-Huh? What about?"
        s "Actually can it wait? We're gonna be late for school!"
        mc "School? Sayori, we have more pressing matters to talk about!"
        "Sayori begins to cross the road and appears to have ignored what I'm saying."
        mc "Sayori, come back here."
        s 4q "Come on! Let's go!"
        mc "Fine, fine."
        "I follow Sayori across the street and put a hand on her shoulder."
        mc "Can we just talk for a minute?"
        s 4a "I agree, we need to talk about what clubs you're going to join."
        mc "Clubs? What the hell are you talking about?"
        s 5c "Eeehhhhh, don't pretend like you don't know what I'm talking about."
        s "You said you would join a club this year!"
        mc "Huh? I don't--"
        s 4j "Uh-huh!"
        s "I was talking about how I'm worried that you won't learn how to socialize or have any skills before college."
        s "Your happiness is really important to me, you know!"
        s "And I know you're happy now, but I'd die at the thought of you becoming a NEET in a few years because you're not used to the real world!"
        "That's right...this is a memory."
        "Of my first day in the literature club."
        "Everything seems to be normal so far. How exactly is this corrupted...?"
        "What should I do? Do I just act normal?"
        "How am I supposed to get through this?"
        s 2c "Is something wrong, [player]?"
        s "You look like you're lost in thought."
        s 2h "Are you thinking of clubs to join?"
        "Sayori looks at me, then frowns."
        s 2f "No, it's not that."
        s "Something must be on your mind."
        mc "I was just thinking."
        s 1c "Oh, about what?"
        s "You know you can tell me anything~"
        mc "I don't know how to tell you this."
        s 1d "Just say it, I can take it."
        mc "This isn't real."
        s 1c "What do you mean?"
        mc "This is just a memory. A trap."
        s "[player], what are you talking about?"
        s "What isn't real?"
        mc "This. This street we're in. This world."
        mc "You."
        mc "None of it is real."
        s "What are you saying? I don't understand."
        s 1h "Am I supposed to believe that I'm just a figment of your imagination?"
        mc "Yes, that's exactly what I'm saying."
        s 1j "That's..."
        "Sayori begins laughing hysterically."
        s 1r "...a good one!"
        s "Who knew you could be so funny without even trying?"
        mc "Sayori, I'm serious."
        s 1q "Yeah, I'm sure you are!"
        mc "No, really. None of this is real."
        mc "This whole world is fake!"
        "I shout that last part loud, I see a few heads turn my way before they go about their day."
        s 2h "You look like a crazy person, you know that right?"
        s "Can you just calm down?"
        s "You're actually starting to scare me a little..."
        mc "I'm sorry. This is all just...all so confusing."
        s 2d "It's alright...I don't blame you."
        mc "What do you mean?"
        s 1b "You don't know?"
        s "People have been disappearing recently, I'm sure you've seen the news."
        mc "No? Who's gone missing?"
        "I don't remember this happening."
        "Maybe this is part of the corruption."
        s 1c "It started just a couple of weeks ago."
        s "A tall girl with purple hair was the first to disappear."
        s "I think her name was--"
        mc "Yuri?"
        s 1n "Yeah! How did you know?"
        mc "She's gone?"
        s 1o "Well, no one knows where she went."
        s "People are saying she was kidnapped or something."
        s "She's not even the only one."
        s 1c "There was this cute, short girl. Natsuki...?"
        mc "She's gone too?!"
        s 1f "Y-Yeah, you sound really surprised. You must have been too busy being a NEET to see the news."
        mc "It's just..."
        s 1c "Do you know these people?"
        mc "Sort of..."
        s 1b "Huh, that's weird."
        s "I didn't think you'd hang around girls much, [player]."
        s 1a "Maybe you've grown up, and I didn't know about it."
        s "Well, good for you~"
        mc "What about Monika?"
        s 1c "Monika?"
        mc "Has she disappeared as well?"
        s "No...at least, I don't think so."
        s "I spoke to her just yesterday."
        mc "Ah, that's right. You two run the Literature Club, don't you?"
        s 2c "Literature Club? I don't know what you're talking about."
        mc "Then how do you know Monika?"
        s 2a "We're in the debating club! She runs it and I'm sort of like the vice-president."
        mc "What? This is all wrong..."
        s 2h "[player]?"
        s "What is wrong with you? I'm really worried!"
        s "You're acting really weird!"
        mc "This world isn't real."
        mc "I know it isn't."
        s 2k "There you go again..."
        s "Come on, [player]. You have to stop this."
        s "I really don't know what's gotten over you."
        s "Do you need some help?"
        if ch16_ay_companions == 4:
            s 1h "I just want to help you accept this reality.{nw}"
            show yuri 1r zorder 2 at i31
            y "Don't listen to her!{nw}"
            $ _history_list.pop()
            hide yuri
            show natsuki 1e zorder 2 at i33
            n "She's trying to trick you!{nw}"
            $ _history_list.pop()
            hide natsuki
            show screen tear(8, offtimeMult=1, ontimeMult=10)
            window hide(None)
            $ pause(1.0)
            show sayori 1h zorder 2 at i11
            hide screen tear
            $ pause(1.0)
            window show(None)
            s "I just want to help you accept this reality.{fast}"
            window auto
            mc "W-What? Did you hear that?"
            mc "Natsuki and Yuri, they were behind you!"
            s 1c "Huh?"
            "Sayori turns around."
            s 1h "There's no one there, [player]."
        elif ch16_ay_companions == 3:
            s 1h "I just want to help you accept this reality.{nw}"
            show yuri 1r zorder 2 at i31
            y "Don't listen to her!{nw}"
            $ _history_list.pop()
            hide yuri
            show screen tear(8, offtimeMult=1, ontimeMult=10)
            window hide(None)
            $ pause(1.0)
            show sayori 1h zorder 2 at i11
            hide screen tear
            $ pause(1.0)
            window show(None)
            s "I just want to help you accept this reality.{fast}"
            window auto
            mc "W-What? Did you hear that?"
            mc "Yuri was just behind you!"
            s 1c "Huh?"
            "Sayori turns around."
            s 1h "There's no one there, [player]."
        elif ch16_ay_companions == 2:
            s 1h "I just want to help you accept this reality.{nw}"
            show natsuki 1e zorder 2 at i33
            n "She's trying to trick you!{nw}"
            $ _history_list.pop()
            hide natsuki
            show screen tear(8, offtimeMult=1, ontimeMult=10)
            window hide(None)
            $ pause(1.0)
            show sayori 1h zorder 2 at i11
            hide screen tear
            $ pause(1.0)
            window show(None)
            s "I just want to help you accept this reality.{fast}"
            window auto
            mc "Natsuki was just behind you!"
            s 1c "Huh?"
            "Sayori turns around."
            s 1h "There's no one there, [player]."
        else:
            s 1h "I just want to help you accept this reality."
        s "I really don't know what's wrong with you but I want to help."
        s "Let's do this, together."
        $ sayori_convince = 3
        $ sayori_convince_start = 3
        label sayori_convince_1_1:
        show sayori 1a
        menu:
            s "What do you say? Will you let me help?"
            "Yes.":
                jump ch16_convince_1_end
            "Yes." if sayori_convince <= 2:
                jump ch16_convince_1_end
            "Yes." if sayori_convince <= 1:
                jump ch16_convince_1_end
            "Yes." if sayori_convince <= 0:
                jump ch16_convince_1_end
            "No.":
                $ sayori_convince -= 1
                if sayori_convince == 0:
                    pass
                else:
                    $ _history_list.pop()
                    show screen tear(20, 0.1, 0.1, 0, 40)
                    window hide(None)
                    play sound "sfx/s_kill_glitch1.ogg"
                    $ pause(0.25)
                    stop sound
                    hide screen tear
                    window show(None)
                    window auto
                    jump sayori_convince_1_1
        mc "I don't need your help, Sayori."
        mc "Do you know why?"
        show sayori 1h
        "Sayori frowns, but it doesn't seem to be a look of worry."
        "More like...anger and frustration."
        s "Why not?"
        mc "Because I know this isn't real."
        mc "Natsuki and Yuri haven't disappeared."
        mc "Monika isn't the leader of the debate club."
        mc "She left it this year."
        s 1i "..."
        mc "I'm going to save you, Sayori."
        mc "Whatever it takes, I will save you."
        mc "Stop you from doing something you{nw}"
        $ _history_list.pop()
        show screen tear(8, offtimeMult=1, ontimeMult=10)
        window hide(None)
        $ pause(1.0)
        scene bg beach_sunset
        show ayame 4l zorder 2 at i11
        $ audio.t18b = "<from " + str(currentpos) + " loop 4.053>mod_assets/bgm/18.ogg"
        play music t18b
        hide screen tear
        $ pause(1.0)
        window show(None)
        mc "Stop you from doing something you{fast}'re going to regret."
        window auto
        ay "What?"
        "Ayame seems to be in front of me by a couple of steps."
        "She must have gotten back already."
        mc "I was..."
        ay 4j "Oh, you made it out of the corrupted memory."
        ay "Congratulations."
        "Despite having a smile on her face, Ayame seems to be indifferent to me getting out."
        "It's like she knew I would make it."
        mc "Yeah, it wasn't as hard as I expected."
        ay 4m "Well, my second memory was a lot more difficult."
        ay "I fear that as we get closer to the rope, it's only gonna become harder."
        ay 4h "Just stick to your truth, and you'll be fine."
        ay "Don't get tricked."
        if ch16_ay_companions == 4:
            mc "I thought I heard Natsuki and Yuri's voices while I was there."
            mc "They told me it was a trick..."
            ay 4m "Hmm...that's good. It shows that they're still here somewhere."
            ay "That Sayori hasn't completely gotten rid of them."
            mc "Did you think she really would?"
            ay 4n "I couldn't sense their souls in this world."
            ay "At least, not after you created their bodies."
        elif ch16_ay_companions == 3:
            mc "I thought I heard Yuri's voice while I was there."
            mc "She told me it was a trick..."
            ay 4m "Hmm...that's good. It shows that she's still here somewhere."
            ay "That Sayori hasn't completely gotten rid of her."
            mc "Did you think she really would?"
            ay 4n "I couldn't sense her soul in this world."
            ay "At least, not after you created her body."
        elif ch16_ay_companions == 2:
            mc "I thought I heard Natsuki's voice while I was there."
            mc "She told me it was a trick..."
            ay 4m "Hmm...that's good. It shows that she's still here somewhere."
            ay "That Sayori hasn't completely gotten rid of her."
            mc "Did you think she really would?"
            ay 4n "I couldn't sense her soul in this world."
            ay "At least, not after you created her body."
        ay "I just feared the worse, that's all."
        mc "Sayori isn't that kind of person. I know it."
        ay 1m "You're still holding out hope for her?"
        mc "I've got to. I don't know what I would do if she actually did something so terrible."
        ay "People change, [player]. You, of all people, should know that."
        show ayame 1a
        if natsuki_approval >= 3 and yuri_approval >= 3:
            ay "You, who has witnessed the friendship between Yuri and Natsuki blossom."
        ay "You, who has seen the effect of poetry can have on a person."
        ay "You, who has become more capable of independent and critical thought."
        ay "Sayori isn't an exception. I can name a lot of things that have changed about her."
        mc "But how? You weren't even there at the beginning."
        ay 1n "I suppose that's true. It's just that she reminds me of someone."
        ay "Someone that{nw}"
        hide ayame at thide
        hide ayame
        "Before Ayame can finish her sentence, she disappears again."
        "She's already activated at least two traps."
        "I have to move on without her."
        "Who does Sayori remind Ayame of?"
        "I suppose it's not impossible to have another person like Sayori."
        "But I don't know anyone else that has the power to enact something like this."
        "I'll find out who she's talking about soon enough."
        "For now, I have to make my way towards the tree."
        "I trace Ayame's footsteps again and then begin to run towards the tree."
        "This time, I won't be tricked so easily."
        "I know Sayori won't make it easy but{nw}"
        $ currentpos = get_pos()
        $ _history_list.pop()
        scene bg bedroom
        play music t3
        "I know Sayori won't make it easy but{fast} I'm prepared."
        "At least, I think I am. The transition to this memory felt a lot more real."
        "But now to figure out what this is and get out of here as fast as possible."
        "I seem to be in my bedroom so there's a lot of possibilities as to what this could be."
        "But what is it exactly?"
        "The door to my room opens and a familiar figure appears at the doorway."
        $ old_monika_type = monika_type
        $ monika_type = 0
        show monika 1ba zorder 2 at t11
        m "Ready to start? I have all the things we need already here."
        mc "What? Monika, what are you doing here?"
        m 2bc "Huh? You're the one who invited me here."
        m "You chose to help me prepare for the festival, remember?"
        "The festival? But I didn't help Monika for that."
        mc "No...this isn't right..."
        m "What are you saying, [player]?"
        mc "We're part of the Literature Club, aren't we?"
        m 2bd "Um...I don't know why you'd ask something like that, but yes."
        m 1bd "Are you feeling okay?"
        m "Maybe choosing me was a bad idea, I'm sorry."
        m "I can leave if that makes it any better."
        m 1bm "I'm sorry for bothering you."
        mc "Wait a second. I need to ask you something."
        show monika 1ba
        "Monika's face lights up."
        m "Oh? Sure, I'll answer if I can."
        mc "How long have I been in the club for?"
        m 2bc "Um...I think this is your first week, right?"
        m "Unless you were a member before and I didn't know about it."
        mc "Who's the president of the Literature Club?"
        m "The president? What kind of question is that?"
        mc "Just answer it, please."
        m 4ba "Well, it's obviously me. I thought you knew that already."
        mc "It's you? I thought it was Sayori."
        m 4bc "She is the vice-president, maybe you had us confused."
        m "But I'm the one who decided to start the Literature Club along with her."
        "For some reason, what she's saying feels like the truth."
        "But all this time, I thought Sayori was the president."
        "This must be an effect of this memory."
        m 2bf "What's wrong?"
        mc "This isn't right. You're not meant to be here."
        m 2bm "O-Oh. I'm sorry then, I just thought that you and I could..."
        m "Ah well, I suppose it wasn't meant to be."
        m 1be "I'll see you during the festival then."
        m "You don't have to do anything, I'll take care of everything."
        m 1bt "I'm sorry once again. I'll leave now."
        "Monika's face begins to tear up."
        "I know this world is fake but at the same time..."
        "I just can't bear to see her like this."
        m "Goodbye~"
        show monika at thide
        hide monika
        "Is that it? Is the memory over?"
        "Why am I not out of this yet?"
        "I lay down on my bed and stare at the ceiling."
        "There must be something I'm missing still."
        "Suddenly, my phone begins to ring."
        "It's...Sayori? Okay, what's this going to be about?"
        mc "Hello? Sayori, what's this about?"
        s "Hi [player]~"
        mc "Sayori."
        "I'm not going to fall for this. I know what she's capable of."
        s "I'm just wondering how the two of you are going with your preparations."
        mc "What...?"
        s "I'm checking up on everybody and Monika isn't answering her phone for some reason."
        s "Is she with you?"
        mc "..."
        "I hang up on her. I know this isn't real."
        "But how do I escape? I kind of thought it would just let me out."
        "My phone begins ringing again. Once again, it's Sayori."
        menu:
            "Answer her.":
                pass
            "Decline her.":
                s "Hello? Why did you hang up on me?"
                "What the...?"
        s "[player]?"
        mc "What do you want, Sayori?"
        s "I want to know why Monika just left me a text saying not to bother you."
        mc "Maybe you should listen to her."
        s "Huh? Why are you being such a meanie?!"
        s "Did I do something wrong?"
        mc "You can stop playing games with me, Sayori."
        mc "You and I both know that this is just a trick."
        mc "That this world isn't real and that you're going to find a way to fool me."
        mc "Just let me out already."
        s "...Well, I told you."
        mc "Told me what?"
        "I hear some rustling coming from the phone."
        "Then, a familiar voice begins speaking."
        ay "[player], have you gone crazy?"
        "It's Ayame, but it's only the first week."
        "She didn't join until just recently."
        ay "I didn't believe Sayori when she told me but after what you just said...."
        ay "Well, the odds are stacked against you."
        mc "You can drop it Ayame, you can't fool me."
        mc "This memory is all messed up. There's so many things wrong."
        mc "First of all, you aren't even part of the Literature Club yet."
        ay "Yet? Are you implying that I'm going to join the club?"
        mc "But aren't you--"
        ay "Sayori told me how crazy you've been acting lately."
        ay "As her best friend I hate to see her like this."
        ay "And I guess it's partly my responsibility as school leader and the one who probably caused all of this to do something."
        "What? Ayame and Sayori are best friends?"
        "And what did she cause exactly?"
        ay "Look, [player], if you don't fix yourself I'm going to have to do it for you."
        ay "And trust me, you don't want that."
        "I can hear a faint 'what' coming from Sayori over the phone."
        ay "She obviously cares about you, [player]."
        ay "Isn't it time you stop being selfish and actually do something for your club?"
        mc "I'm Sayori's best friend, Ayame. And you, you're meant to be helping me."
        ay "Wow. I didn't realize the extent of it but maybe that ball hitting you on the head really did something."
        ay "Your memories must have been all jumbled up or something."
        ay "Sayori and I have been friends since we were children."
        mc "No, I--"
        ay "I think you need to find some help and stop distancing yourself from everyone."
        "What is going on in this world?"
        "Why is this memory so different to anything I remember?"
        "Ayame shouldn't even be here..."
        s "Look, [player], if you want to leave the Literature Club...that's okay."
        s "I know I kind of coerced you into it but that's only because I really didn't want you to feel so lonely."
        s "With four members, we'll still be allowed to exist so..."
        mc "Are you saying I can leave the club?"
        s "That is what I said, yeah...it just sucks."
        s "I just didn't think it would have to this."
        ay "Just do it already."
        s "Okay, I have the list of members with me right now."
        s "If I remove your name from the list, [player]...you'll be gone."
        mc "I'll escape this world?"
        s "I really don't know what you mean."
        s "But I suppose that's one way to think about it."
        "What if this is some kind of test?"
        "If I leave the club, then there's a chance I'll go back to the beach."
        "But the way she said that I'll 'be gone'...it sounds suspicious."
        s "Are you still there?"
        mc "Yeah, just give me a second."
        show monika 1bn zorder 2 at t11
        m "[player], I'm sorry for eavesdropping but I couldn't help it."
        m 1bo "Are you really thinking of leaving the club?"
        mc "Monika, I thought you left."
        m "I was about to but when I sent the text to Sayori I just didn't feel right leaving it like that."
        mc "So you decided to listen in?"
        mc "Ah, it doesn't matter anyway."
        s "Is that Monika?"
        m "It's me Sayori. Are you really just going to let [player] go like that?"
        s "It's [player_possessive] decision after all, it's not up to me."
        m 1bh "I can't believe you'd just let someone go like that."
        s "I'm not going to force [player_reflexive] to stay."
        s "It's not right, even if [player_possessive] state of mind isn't entirely where it should be."
        m "The ball..."
        mc "What ball? What are you talking about?"
        # This ball is the same ball that Ayame kicked to the playing field in her perspective, kind of
        ay "I'm sorry, I didn't mean to hit you, and with such force. It was an accident."
        m 1be "You ended up at the nurse's office after that. Knocked out cold..."
        m "Do you not remember?"
        mc "No, you need to stop! This never happened!"
        s "Look, [player]. Just make up your mind."
        s "If you aren't gonna be part of the club anymore, we'll leave you alone."
        ay "And I'll make sure Monika does too."
        m 1bf "...Please don't do this, [player]. Think about what you can accomplish with us."
        m "You've barely scratched the surface of our potential."
        python:
            try: os.remove(config.basedir + "/wait")
            except: pass
            try: os.remove(config.basedir + "/do nothing")
            except: pass
            try: os.remove(config.basedir + "/dont be fooled.txt")
            except: pass
            try: renpy.file(config.basedir + "/dont be fooled.txt")
            except: open(config.basedir + "/dont be fooled.txt", "wb").write(renpy.file("dont be fooled.txt").read())
        "This is a test, isn't it?"
        "One of them is trying to get me to leave the club, while the other is trying to get me to stay."
        "I think Sayori set this up to try to confuse me."
        "There's half a chance I'll mess up and half a chance I'll get it right."
        "But how am I supposed to figure out what the right choice is?"
        s "Make your decision [player]."
        $ quick_menu = False
        show screen timer_16_long_menu_skip("ch16_convince_2_true_1",_layer="timers")
        menu:
            s "Are you going to stay in the club, or leave?"
            "Stay in the club.":
                $ renpy.hide_screen("timer_16_long_menu_skip",layer="timers")
                $ quick_menu = True
                jump ch16_convince_2_end_1
            "Leave the club.":
                $ renpy.hide_screen("timer_16_long_menu_skip",layer="timers")
                $ quick_menu = True
                jump ch16_convince_2_end_2
        label ch16_convince_2_true_1:
        $ quick_menu = True
        $ renpy.hide_screen("timer_16_long_menu_skip",layer="timers")
        $ _history_list.pop()
        $ _history_list.pop()
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        stop sound
        hide screen tear
        window show(None)
        s "Make your decision [player]."
        window auto
        menu:
            s "Are you going to stay in the club, or leave?"
            "Stay in the club.":
                jump ch16_convince_2_end_1
            "Leave the club.":
                jump ch16_convince_2_end_2
            "Leave this memory.":
                pass
        s "W-What? That shouldn't have been there."
        s "What do you mean by leave this memory?"
        mc "I will save you, Sayori."
        mc "You can count on it."
        m 1bc "[player], what's happening?"
        m "You said you're leaving this memory, what does that mean?"
        mc "You genuinely don't know what's happening, don't you?"
        mc "I'll save us all, Monika. You can count on it."
        m 1bf "I don't know what you mean."
        s "[player], I don't need saving."
        s "You're under the impression that this isn't what I want to do."
        s "That I'm being mislead or misunderstood somehow."
        s "I'm not. I'm completely doing this of my own free will."
        s "Or whatever 'free will' we have in this world."
        m "Sayori, what are you talking about?"
        s "Ugh, just get out of here already."
        mc "You've really changed, haven't you Sayori?"
        mc "What sort of things have you seen?"
        mc "How did you end up like this?"
        m 1bg "I'm so confused..."
        s "Even if you do manage to get to me, [player]."
        s "There's no way you'll{nw}"
        scene bg beach_night
        show ayame 1a zorder 2 at i11
        $ audio.t18c = "<from " + str(currentpos) + " loop 4.053>mod_assets/bgm/18.ogg"
        $ _history_list[-1].what = "\"There's no way you'll be able to stop me or what's coming.\""
        $ monika_type = old_monika_type
        play music t18c
        hide screen tear
        $ pause(1.0)
        window show(None)
        "I'm back on the beach again."
        window auto
        "Ayame is once again ahead of me, but she's covered quite the distance."
        "It also seems to be night already, though I don't think that much time has actually passed."
        mc "Ayame!"
        "She turns around and gives a faint smile."
        "The look on her face suggests she just saw something horrible."
        ay "You made it out, then."
        mc "She's not going to get me that easily."
        ay "Well, that's good. We're almost there so let's go."
        "There's something odd about how Ayame is speaking, at least compared to before that memory."
        "Like she's lost some of her energy."
        if ch16_ay_perspective:
            show screen tear(8, offtimeMult=1, ontimeMult=10)
            window hide(None)
            scene bg beach_night
            $ pause(1.0)
            hide screen tear
            $ pause(1.0)
            window show(None)
            "I can't do this.{fast}"
            window auto
            "This has to stop soon. I don't know if I can take this any longer."
            "Using my memories of the previous club to torment me."
            "Masquerading as everyone else and using my own programming against me."
            "I almost fell for [player_reflexive] again. It felt so real."
            "I thought I moved on but there's still a part of me that can't get over [player_reflexive]."
            "Why...?"
            "I didn't know she would stoop that low or even have access to those..."
            "I'm going to get her for this."
            "She thinks she can do this to me and get away with it?"
            "I'll...!"
            "Calm down Ayame. I can't lose control again."
            "I'm almost there. I just need to stay in control of myself."
            "Hold on just a little bit longer."
            "Just a little longer, Ayame..."
            show screen tear(20, 3, 2, 0, 70)
            window hide(None)
            $ pause(1.0)
            scene bg beach_night
            show ayame 1a zorder 2 at t11
            hide screen tear
            $ pause(1.0)
            window show(None)
            "Was that really what she experienced?{fast}"
            window auto
            "I could feel all her dread and despair."
        mc "Is everything okay? You don't sound okay."
        ay "Observant, aren't we? Come here, there's no point yelling if it's just the two of us."
        "Ayame pauses in her tracks and beckons for me to get to where she is."
        "I take the cue and trace her footsteps to get to her."
        "The tree and the rope seem to just be a few steps away now."
        mc "How many memories did you get through already?"
        ay 1l "I finished my third one just before you finished."
        ay "I saw Monika just before she entered her third one as well."
        mc "I've only completed two, and I was ahead of Monika...I'm sorry."
        ay "It's not like it's your fault."
        ay "You could say I'm quite adept at this already."
        ay "Monika, strangely enough, is quite fast as well."
        mc "But how?"
        ay 1m "I can't speak for Monika but for me, let's just say I have experience at forgetting the past."
        mc "You look like..."
        ay "I know. It's because Sayori pulled out a memory that I've tried to suppress for so long."
        ay "I got out, but it wasn't easy."
        mc "It looks like it's taken its toll on you."
        ay "You could say that."
        mc "Are you going to be okay?"
        ay 1a "I'll be okay when we reach Sayori."
        ay "Now, enough time's been wasted. Let's carry on."
        "Ayame continues forward, seemingly fine."
        "I can tell she's got something on her mind."
        "Maybe some doubt about all of this caused by that memory."
        "I really wonder how Sayori could have affected her this much..."
        mc "You sure you don't want to talk about it?"
        ay 1f "I'm fine! Just...mind your own memories."
        ay "I'll deal with this on my own."
        show ayame at thide
        hide ayame
        "After a few more steps forward, she disappears again."
        "It's quite literally two steps away from the tree."
        "I trace her footsteps and I arrive just out of reach of the rope."
        "Is there going to be another trap here? Or was that all of it?"
        "I sigh and take a step forward."
        "Nothing."
        "I slowly take another step forward and..."
        "Surprisingly, I'm fine. Could this be it?"
        "I reach out for the rope...just before I can touch it, a familiar voice comes from behind me."
        ay "Stop! Don't touch it."
        mc "Ayame what--"
        ay "And don't turn around!"
        mc "What? Why not?"
        ay "This is the final trap. If you touch that rope then all of this would have been for nothing."
        mc "So what should I do then?"
        ay "Take your hand back, but slowly."
        "I slowly pull my hand back from the rope. We were so close."
        "But Ayame must have a reason for doing this."
        ay "Don't make any sudden movements, [player]."
        ay "We have to do this next part {i}very{/i} carefully."
        mc "Tell me what to do then."
        ay "Okay. Just stay there for a moment."
        ay "I need to do something."
        mc "You're supposed to be right behind me, weren't you?"
        mc "Why do you sound so distant now?"
        ay "I don't know what you're talking about, [player]."
        ay "Look, just listen."
        ay "What the hell?"
        mc "What's wrong?"
        ay "Are you hearing this, [player]?"
        ay "It's my voice but..."
        mc "Huh?"
        "I'm tempted to turn around but Ayame said not to."
        "What's causing all of this commotion?"
        "Why can't the Ayame who wants the rope just come over here and get it?"
        ay "[player], what are you doing? Just grab the rope already!"
        mc "Huh? But I thought you said to--"
        ay "Don't listen to her, [player]! It's Sayori playing tricks again."
        ay "She's using my voice to try to trick you!"
        ay "Step away from the rope or we'll never stop Sayori!"
        mc "I don't know if you're just messing with me, Ayame."
        mc "But this isn't funny, at all."
        ay "I'm telling you, Sayori is using my voice!"
        ay "Why would I tell you to stop with the rope now, when we're so close?"
        ay "[player], I just got back from one of my memories, she's trying to trick you."
        ay "If you take that rope, then she wins."
        mc "Who am I supposed to believe?"
        mc "You're both just telling me to do something and I don't know who I should trust."
        if ch16_ay_perspective:
            show screen tear(8, offtimeMult=1, ontimeMult=10)
            window hide(None)
            scene bg beach_sunset
            $ pause(1.0)
            hide screen tear
            $ pause(1.0)
            window show(None)
            "What kind of trick is Sayori playing?{fast}"
            window auto
            "We're so close to reaching her and now we're at an impasse."
            ay "You don't know who to trust, do you?"
            s "Which voice is really me and which one is actually Sayori?"
            "She's quite the actor, isn't she?"
            mc "I don't. I don't know why one of you hasn't either tried to stop me or grab the rope already."
            "If I make one false move, then I might trigger another trap."
            ay "It's complicated."
            "And by the time I get out of it, it could be all over already."
            "[player] won't turn around because of what Sayori said."
            "But how am I supposed to convince [player_reflexive] to take the rope?"
            "[cPlayer_personal]'s obviously being cautious about this."
            "I can feel the energy here is almost at its limit."
            "If this goes on for much longer then we're not going to make it."
            "My plans will be undone."
            "I'm so close! I can't have made it this far for nothing."
            "I have to do something, otherwise all those years spent planning will be wasted."
            if ch16_ay_message[0] and ch16_ay_message[1] and ch16_ay_message[2] and ch16_ay_message[3]:
                "Dammit."
                "At times like this, I wish {i}she{/i} was still here."
                "I really have taken her for granted, haven't I?"
                "She would have said something smart."
                "A plan or something that I could use to get through this."
                "Or at least someone I can talk to that won't think I'm crazy."
                "Imagine if I told [player] what I saw and what I'm thinking right now."
                "Not like it would matter anyway, Sayori is using my voice to trick [player_reflexive]."
                "I just don't know what I can possibly say to convince [player_reflexive]."
                "I suppose there's only one thing to do then."
                "Rely on the chance that [player] will choose the rope."
                "Because if not...then I guess it's game over."
            else:
                $ style.say_dialogue = style.edited
                "Might I suggest something?"
                $ style.say_dialogue = style.normal
                "It's you. What did you want?"
                $ style.say_dialogue = style.edited
                "I have a way for [player_reflexive] to get the rope."
                "But you won't like it."
                $ style.say_dialogue = style.normal
                "I'm open to ideas at this point, even from you."
                "I mean you saw that last memory, what else is she capable of?"
                "I'm getting desperate. Now Sayori is playing even more tricks."
                "What do you suggest?"
                $ style.say_dialogue = style.edited
                "I'll need control, if just for a second."
                "Trust me on this, I won't let you down."
                $ style.say_dialogue = style.normal
                "Absolutely not. The last time that happened you messed up my life."
                "I still can't look them in the eye even to this day."
                $ style.say_dialogue = style.edited
                "That memory was fake. You know it. You could have started straight at them."
                "They wouldn't have known any better."
                "We may not always see eye to eye, Ayame."
                "But you have to admit, I've always had our interests at heart."
                $ style.say_dialogue = style.normal
                "In your twisted way, I suppose. I still don't know about this."
                $ style.say_dialogue = style.edited
                "Be smarter than this, Ayame. I know you're capable of more critical thought than that."
                "You know that [player] can tell who I am."
                "If you don't give me control then you're relying on the chance that [player] will make the right decision."
                "Are you willing to risk that?"
                "If [player_personal] can identify me, then [player_personal]'ll know for sure to grab the rope."
                $ style.say_dialogue = style.normal
                "I know you're right but..."
                "I suppose there's really no way out of this, is there?"
                "Those really are my only two options."
                if ch16_ay_decision_count > 0:
                    menu:
                        "I guess I should..."
                        "Trust the other me.":
                            $ ch16_ay_decision_count -= 1
                            $ ch16_ay_gave_control = True
                            "A jolt goes through my body. I must be losing it at this point."
                            "Against all common sense, I'm trusting the other me."
                            "I hope I know what I'm doing."
                            $ style.say_dialogue = style.edited
                            "What did I tell you, Ayame?"
                            "I have our interests at heart."
                            $ style.say_dialogue = style.normal
                            "You don't have a heart."
                            $ style.say_dialogue = style.edited
                            "Hah, I suppose I don't. That doesn't mean I don't care for you."
                            "After all, if Sayori succeeds, I'm in trouble too."
                            "Just give me control already, you won't regret this."
                            $ style.say_dialogue = style.normal
                            "I can already tell this was a big mistake."
                            "But I can't refuse."
                            $ style.say_dialogue = style.edited
                            "Good...now, sit back and enjoy the show."
                            $ style.say_dialogue = style.normal
                        "Not trust the other me.":
                            $ ch16_ay_decision_count -= 1
                            "I feel an odd sensation go through my artificial body."
                            "A sensation that's telling me that the other me isn't trustworthy."
                            $ style.say_dialogue = style.edited
                            "Quite foolish of you, I must say."
                            "But not unexpected, I guess I will just watch us fade away from the sideline."
                            $ style.say_dialogue = style.normal
                            "I appreciate the vote of confidence..."
                        "Make my own choice.":
                            "I know better than to give you control again."
                            "Following this path can only lead to ruin like it did before."
                            $ style.say_dialogue = style.edited
                            "Quite foolish of you, I must say."
                            "But not unexpected, I guess I will just watch us fade away from the sideline."
                            $ style.say_dialogue = style.normal
                            "I appreciate the vote of confidence..."
                else:
                    "But I know better than to give you control again."
                    "Following this path can only lead to ruin like it did before."
                    $ style.say_dialogue = style.edited
                    "Quite foolish of you, I must say."
                    "But not unexpected, I guess I will just watch us fade away from the sideline."
                    $ style.say_dialogue = style.normal
                    "I appreciate the vote of confidence..."
            show screen tear(20, 3, 2, 0, 70)
            window hide(None)
            $ pause(1.0)
            scene bg beach_sunset
            hide screen tear
            $ pause(1.0)
            window show(None)
            "That's it.{fast}"
            window auto
            "Ayame is the one who wants me to grab the rope."
            "But...does she really have my best interests?"
            "She seems conflicted somehow. As if she's up to something."
            "What 'plan' does she have in store?"
            "Could it be worse than what Sayori is going to do?"
            "I don't know about this..."
        else:
            "I think both of them know we're on a time limit."
            "The difference is that the longer I wait to make a decision, the better chance Sayori has of doing whatever she's doing."
            "I have to make a decision quickly otherwise it's all over."
            ay "You don't know who to trust, do you?"
            ay "Which voice is really me and which one is actually Sayori?"
            mc "I don't. I don't know why one of you hasn't either tried to stop me or grab the rope already."
            ay "It's complicated."
        mc "I don't know who to choose..."
        m "[player], what are you waiting for?"
        mc "Monika?"
        m "Take the rope already!"
        ay "Don't listen to her, [player]."
        m "That sounds like Ayame but..."
        ay "It's Sayori playing tricks. You can see me, can't you, Monika?"
        ay "Sayori is mimicking my voice."
        ay "She's mimicking Monika's voice now too!"
        ay "You have to leave it!"
        m "[player], just get the rope already."
        if ch16_ay_gave_control:
            $ style.say_dialogue = style.edited
            ay "[player], get the rope."
            ay "I know you can tell the difference."
            ay "We're so close to Sayori. So close."
            ay "You just need to get the rope and then we can run."
            $ style.say_dialogue = style.normal
            "Somehow I can easily tell which one is Sayori."
            "She's still speaking like normal Ayame whereas Ayame is...different."
            m "That's...Ayame but something is different about her."
            m "You have to trust her, [player]."
            ay "Don't listen to her! She's tricking you!"
            ay "If we just head back now, we can get to Sayori through the portal."
            ay "I made a mistake thinking this was it. It's not!"
            $ style.say_dialogue = style.edited
            ay "Do you truly believe that?"
            ay "Have I made any mistakes so far?"
            ay "I've calculated everything, with a few exceptions."
            ay "We would have never gotten this far without me."
            $ style.say_dialogue = style.normal
            ay "That's enough. [cPlayer_personal] now knows what to do."
            ay "I appreciate your help but I'll take it from here."
            "It sounds like the real Ayame regained control."
            ay "Take the rope, [player]. You know which one is the real me, don't you?"
        else:
            ay "[player], get the rope."
            ay "We have to stop Sayori, we're so close!"
            ay "Just get it, and run. That's it."
            ay "Are you serious? Don't listen to her!"
            ay "Don't listen to her! She's tricking you!"
            m "Get the rope, [player]!"
            ay "If we just head back now, we can get to Sayori through the portal."
            ay "I made a mistake thinking this was it. It's not!"
            ay "I don't make mistakes, [player]."
            ay "Everything I've done has been calculated."
            m "Don't fall for Sayori's trick. We're so close."
            ay "Except this one! Please, listen to me!"
        ay "Don't listen to her!"
        mc "I have to make a decision but I can't."
        "Yet the clock is ticking..."
        ay "[player], you have to!"
        ay "So what's the verdict?"
        ay "Are you going to listen to Sayori?"
        mc "I still don't know if the choice I want to make is the right one."
        mc "At this point, I'm not gonna leave it up to me."
        ay "Huh? What do you mean?"
        "I'm going to leave it...to you."
        menu:
            "Take the rope.":
                pass
            "Leave the rope.":
                jump ch16_convince_3_end_2
        mc "I'm taking the rope."
        mc "I really hope that I'm making the right decision here."
        ay "No, you just let her win."
        ay "Do you have any idea what you've just done?"
        mc "I feel like one of you would have said the same thing if I didn't take the rope."
        "I reach out and attempt to untie the rope from the tree."
        "It takes a couple of seconds but I eventually get it."
        "As soon as I have it, I hear a deafening screech come from behind me."
        "I cover my ears to try to reduce the noise but there doesn't seem to be any effect."
        "After a few seconds, the noise finally disappears."
        mc "What the hell was that? Did I make the wrong choice?"
        ay "No."
        "A hand touches my shoulder and I turn my head."
        show ayame 1m zorder 2 at f21
        show monika 1d zorder 2 at t22
        ay "We have everything we need, so let's head back."
        ay "The energy around here seems to be reaching its peak now."
        ay "I don't know if there are still traps so it's safer to just go through our footsteps."
        show ayame zorder 2 at t21
        show monika 1h zorder 3 at f22
        m "When we've got this far, it's better to be safe than sorry."
        show monika zorder 2 at t22
        mc "Do you really think Sayori is going to be on the other end of this next portal?"
        show ayame zorder 2 at f21
        ay "I sure hope so. I don't know if I have enough resolve to continue much more."
        "It's pretty clear that whatever Ayame went through in these traps broke her a little."
        "I wonder if Monika went through something similar..."
        "I hope there isn't anything too complicated after this."
        ay 1j "Let's get this over with."
        show ayame zorder 2 at t21
        show monika 1o zorder 3 at f22
        m "Agreed, it's time to end this."
        show monika zorder 2 at t22
        mc "I'm right behind you."
        scene bg clearing
        show ayame 1h zorder 2 at t21
        show monika 1c zorder 2 at t22
        with wipeleft_scene
        "By the time we get back to the clearing, the sun managed to rise already."
        "Time seems to be passing by very quickly right now, at least in this world."
        "Which is probably an indication of the instability of this world."
        show ayame zorder 3 at f21
        ay "Quickly, place the rope around the shells."
        ay "This should finally open the portal."
        "Monika and I do as she says and form a circle which encloses the shells."
        "I feel myself being pushed away from it despite there being no wind or anything."
        "I still can't see anything but Ayame's face seems to light up."
        ay 2m "This is it. All that you and I have worked towards."
        ay "Everything has been culminating to this moment."
        ay 2l "Once you get in, there is no turning back."
        ay "Not until we're done."
        ay "Do the two of you understand this?"
        show ayame zorder 2 at t21
        show monika zorder 3 at f22
        m "Of course I do. The stakes are high."
        show ayame zorder 3 at f21
        ay "And you, [player]."
        menu:
            ay "Do you understand?"
            "Yes":
                pass
            "No.":
                ay 2a "What's there not to understand?"
                ay "You'll be stuck there until we get an outcome."
                ay "That means no saving, no turning back time, nothing."
                ay "Whatever we do in there will stick with us."
                ay "So I hope you've come prepared."
                ay "Is that all clear now?"
                mc "I think so."
        ay 2m "Good. Now let's get the {i}hell{/i} out of here before this world explodes or something."
        ay "Hopefully this next place doesn't have any tricks."
        ay "But who knows?"
        ay 4l "Do you need a minute before we go?"
        show ayame zorder 2 at t21
        mc "I think I might need that, yeah."
        show monika zorder 3 at f22
        m "We probably only have time for a few seconds, don't we?"
        m "I can sense the presence here getting much stronger..."
        show ayame zorder 3 at f21
        show monika zorder 2 at t22
        ay "Monika's right. We have no time to lose."
        ay "I'm going to give you a couple of seconds."
        "Ayame takes a deep breath and whispers something to me."
        ay 4h "Est tempus."
        show ayame zorder 2 at t21
        mc "Huh?"
        show ayame zorder 3 at f21
        ay "Just...remember it."
        mc "Alright then."
        "I wonder what significance that could possibly have?"
        "What does it even mean?"
        "Before I can get my answer, Ayame nods and puts her hand on the ground on the middle of the portal."
        stop music
        label ch16_sayori_1:
        # Uncomment this line after this arc is finished
        # $ persistent.autoload = "ch16_sayori_1"
        scene bg sayori_bedroom
        with dissolve_scene_full
        play music t18 fadein 5.0
        "I seem to have arrived in Sayori's bedroom, on the floor."
        "Everything here looks normal. The skies outside seem normal and I can even hear birds chirping."
        "Ayame, and Sayori, don't seem to be anywhere in sight."
        "I get up and take a look around the room."
        "On Sayori's computer, there seems to be a document of some kind open."
        "I take a quick glance through it, looking at the title of the document."
        "It reads 'Inauguration Day'. Maybe it's some kind of plan she had?"
        "It seems to be quite an extensive document..."
        "Scrolling through it, I can see various headings that describe events that happened today."
        if ch16_ay_drink:
            "One of them says 'Ayame offers drink' and under it shows '[player] takes drink'."
            "There's also events that didn't happen like '[player] rejects drink' and events that would have happened after that."
        else:
            "One of them says 'Ayame offers drink' and under it shows '[player] rejects drink'."
            "There's also events that didn't happen like '[player] takes drink' and events that would have happened after that."
        "It's like some sort of Choose Your Own Adventure book..."
        "I keep scrolling, approaching the bottom of the document."
        "I find a section that reads 'The Danger Arrives'."
        "So what really is this 'danger' anyway?"
        "I look through it, and it seems to describe the events of what just happened."
        "Me being on the beach then waking up here, in Sayori's room."
        show sayori 1ba zorder 2 at t11
        s "Hello, [player]."
        mc "Whoa!"
        "Before I can take a good look, Sayori suddenly appears behind me and I nearly fall from the surprise."
        "She seems to be holding a cup of coffee."
        "Is this really Sayori? Or is this some kind of trick again?"
        s 1bd "Don't worry, it's really me."
        s "I've started using a lot of coffee lately because I can't really afford to catch a break."
        s "I need to stay awake to make sure it's all going to run smoothly, you know?"
        "She puts the coffee down on her desk."
        mc "I suppose..."
        mc "You {i}do{/i} know why I'm here, don't you?"
        s 2bb "I do. Before you do what you have to, can't we just relax for a little bit?"
        s 2bc "The truth is I could end everything right now, if I really wanted to."
        s "But since you're here now, we may as well talk, right?"
        mc "Where are they Sayori?"
        s 2bd "The two of them are downstairs already."
        s "You were the last one to wake up."
        s "What? Why are you looking at me like that?"
        s 1bj "Do you really think I'd actually hurt them?"
        s "I told you why I was doing this, didn't I?"
        s "It's for their sake, because there just isn't any alternative."
        mc "You said you've seen how this ends, haven't you?"
        s 1bk "That's right. It isn't very pretty..."
        s "You saw the document. I know everything that happens."
        s "Every outcome, every word that's supposed to be said for this day."
        s "Everything I said before, it's all been preconceived to happen already."
        s "Including me mispronouncing 'significance' before."
        s 1bh "Do you really think I wouldn't have done my best to act completely like Ayame and not mess up that word?"
        s "That's such a simple mistake to make."
        "This is a side to Sayori that's completely new to me."
        "Even with a smile on her face, she seems so cold. So calculating."
        mc "So it was all an act?"
        s 1bl "Ehehe, I guess you could say that..."
        s "But I was just following how the timeline was supposed to play out."
        mc "You knew I would get here then?"
        "This can't be right."
        s 1bd "I did, just like I know you're going to say that--."
        mc "This must be a trick, Sayori."
        s 1bh "It's not a trick. I've rehearsed these lines over and over."
        s "You can check the document if you want, but you don't really do that until later."
        s "All of this is already set to happen."
        s 1bc "Honestly, it's all coming naturally to me but I guess that's how it was meant to play out anyway."
        mc "So that document, it controls what happens?"
        mc "If I change something in there..."
        s 1bl "No, it's just the set of events that play out."
        s "Detailing every possibility that could happen today. Well, almost every possibility..."
        s "There are some variables that could still change but not enough to warrant me changing my mind."
        s "You could change something in there if you wanted, but it's not going to change the future, or the past."
        mc "That's ridiculous. This couldn't possibly..."
        "I look back at the document and scroll down to see what happens next."
        "Right there on the document, it says [player] looks at the document to see what happens next."
        mc "What the..."
        s 1bq "I told you~"
        mc "Then what's the point? Are you meant to end everything after all?"
        mc "Is that an event that's meant to happen?"
        s 1bh "No. In the original timeline, I don't end our reality."
        s "I'm too late, I don't get to because of this conversation with you."
        s "It's kind of paradoxical, isn't it?"
        s "But I know precisely when it's going to happen and I plan to end it all before it's too late."
        mc "Nothing I can say will convince you, will it?"
        s "What do you want me to say?"
        s "The answer you want to hear that isn't true?"
        s 1bk "Or the truth?"
        s "I already told you that I made up my mind."
        s "There's nothing that can change it now."
        mc "You said the others are downstairs, right?"
        s 1bc "I did. I could call them up now if you want."
        s 1ba "But that won't be necessary since they're about to come in anyway."
        mc "Huh?"
        $ old_monika_type = monika_type
        $ monika_type = 0
        show monika 1f zorder 2 at t31
        show ayame 1l zorder 2 at t32
        show sayori 1ba zorder 2 at t33
        "Right on cue, the two of them enter the room."
        show monika zorder 3 at f31
        m "Are you okay, [player]? You're not hurt, are you?"
        show monika zorder 2 at t31
        mc "I'm fine, I think."
        show ayame 1n zorder 3 at f32
        ay "Ah, well you made it here safely. That's good, I suppose."
        show ayame zorder 2 at t32
        mc "Ayame, what happened? Why are we--"
        show ayame 1g zorder 3 at f32
        ay "There's no point anymore. She was right."
        show ayame zorder 2 at t32
        mc "What? But we're right here."
        mc "We can still--"
        show ayame 1n zorder 3 at f32
        ay "She...she showed me everything, [player]."
        ay "She was right. There really is only one way to get rid of the danger."
        ay 2n "You...me...all three of us couldn't do anything even if we tried."
        ay "Even if Sayori helped us, we'd be powerless to do anything."
        show monika 1m zorder 3 at f31
        show ayame zorder 2 at t32
        m "It can't be helped, [player]. It really is all over."
        m "We tried our best but I guess...it wasn't good enough."
        m 1o "Maybe it never was."
        show monika zorder 2 at t31
        mc "Is this really the end?"
        mc "We went through all of that, for nothing?"
        "This can't be right. Something is very wrong here."
        mc "No...there must be more to it than this."
        mc "I refuse to believe this is real."
        show ayame 2a zorder 3 at f32
        ay "[player], what the hell are you talking about?"
        ay "This is it. This is what we worked towards."
        ay "It's all over..."
        show monika zorder 3 at f31
        show ayame zorder 2 at t32
        m "I'm sorry, [player]. I really thought we could."
        m "But it's time to admit it's over. Sayori is in the right here."
        show monika zorder 2 at t31
        show sayori 1bd zorder 3 at f33
        s "Don't you agree it's time to stop this?"
        s "I just want our last moments to be happy. If you think that's bad then..."
        s "Well, I suppose I don't need you to think it's good or bad. I just need you to accept."
        s "I'll even bring the others here too. There's no point in fighting anymore."
        s "It's nearly time, [player]. Time is running out..."
        show ayame 2m zorder 3 at f43
        show sayori zorder 2 at t44
        ay "I hate this as much as you, [player]."
        ay "But she's got a point, you know..."
        ay 2n "You have to realize it's time."
        show ayame zorder 2 at t43
        mc "It's time...isn't it?"
        "Ayame said something to me before we got here."
        mc "Est tempus."
        show sayori 1bh zorder 3 at f44
        s "W-What?{nw}"
        stop music
        scene black
        $ monika_type = old_monika_type
        show mask_2
        show mask_3
        show room_mask as rm:
            size (320,180)
            pos (30,200)
        show room_mask2 as rm2:
            size (320,180)
            pos (935,200)
        play sound "mod_assets/sfx/glassbreak.ogg"
        show bg sayori_bedroom_void
        show monika 1h zorder 2 at i31
        show ayame 2a zorder 2 at i32
        show sayori 1bh zorder 2 at i33
        with shatter
        play music m1
        "There's no more birds chirping outside."
        "The world outside looks dark yet strangely Sayori's room remains lit normally."
        show ayame zorder 3 at f32
        ay "Your illusion is broken, Sayori."
        ay 2f "Even to the end, you were still trying to fool us...but no more!"
        ay "[player] realized the truth. You have to see now that your efforts are in vain."
        ay "You have to stop this madness. There's still time."
        ay "If not, {i}we'll{/i} have to stop you."
        show ayame zorder 2 at t32
        "It looks like this is the real end world."
        "I must have been caught in one of Sayori's tricks again..."
        show monika 1m zorder 3 at f31
        m "That...was quite dramatic. Almost like you were acting for one of our plays."
        m "But she's right. Sayori, you have to stop this, now."
        show sayori 1bk
        "Sayori looks at the three of us and sighs."
        show sayori zorder 3 at f33
        s "I honestly thought I had it. I thought that would be the end."
        s "That we could all finally go to rest."
        s 1bi "But the three of you just want us to suffer. To end the world but full of conflict."
        s "Why can't you understand that the danger coming is bigger than us?"
        s "Why can't you understand that the only way to stop it is to stop this game?"
        show ayame 2a zorder 3 at f32
        show sayori zorder 2 at t33
        ay "Are you really that blind that you can't see what's in front of you right now?"
        ay "You may have the power of the presidency Sayori, but that doesn't mean you should do everything yourself."
        show ayame zorder 2 at t32
        show sayori 1bj zorder 3 at f33
        s "That's {i}exactly{/i} why I have to do everything myself."
        s "The second I stop, everything will go wrong!"
        s 2bk "Without any of my meddling, we would not have gone this far."
        s "Everything would have ended on the day of the festival..."
        show ayame 4m zorder 3 at f32
        show sayori zorder 2 at t33
        ay "And look where your meddling got you, Sayori."
        ay "I wasn't even supposed to exist in this world but because of your curiosity, I'm here."
        ay "You brought me here. You pulled me from the deepest depths of this."
        ay 4a "Maybe that was an accident."
        ay "Or maybe you subconsciously needed me to stop you."
        show ayame zorder 2 at t32
        show sayori 2bh zorder 3 at f33
        s "...That's not true! You were just--"
        show monika 2o zorder 3 at f31
        show sayori zorder 2 at t33
        if monika_type == 0:
            m "Sayori, you know this isn't right."
            m "I know deep down, you know there's another way."
            m "A better way."
        else:
            m "This has to stop, Sayori."
            m "The world cannot end like this."
        show monika zorder 2 at t31
        show ayame 1f zorder 3 at f32
        ay "Are you even aware of the danger is?"
        ay "For all your planning, you must know what, or {i}who{/i}, it truly is."
        ay "[player], did you finish reading that document?"
        show ayame zorder 2 at t32
        mc "No, I didn't get to..."
        show ayame 1a zorder 3 at f32
        ay "You couldn't finish it anyway. Sayori didn't complete it."
        ay "She never went far enough to see what the danger was."
        ay "Perhaps she was too afraid to see what would cause so much suffering."
        ay "Answer me honestly, Sayori. Deny it if I'm wrong."
        "Sayori says nothing."
        ay "As I thought. You're too scared to see it for yourself."
        ay "Maybe you even know what the danger actually is but are too afraid to admit it."
        show ayame zorder 2 at t32
        mc "What do you mean, Ayame?"
        mc "How could Sayori know what the danger is if she hasn't seen it?"
        show monika 1f zorder 3 at f31
        m "Even I know what the danger is. It's been with us this whole time..."
        m 1e "But everything can still change!"
        show monika zorder 2 at t31
        show sayori 2bk zorder 3 at f33
        s "No...it's far too late now."
        show ayame 1m zorder 3 at f32
        show sayori zorder 2 at t33
        ay "Go on. Why don't you tell [player_reflexive]?"
        ay "[cPlayer_personal] deserves to know, doesn't [player_personal]?"
        ay "After all, you're still going to end it anyway."
        ay 1a "So what does it matter?"
        "Sayori remains silent."
        ay "If you won't say it, then I will."
        ay "The danger is--"
        show ayame zorder 2 at t32
        show sayori 1bh zorder 3 at f33
        s "Okay, fine. I'll say it, Ayame."
        s "Like you said, what does it matter, right?"
        s 1bu "The danger is..."
        s "It's...me."
        show sayori zorder 2 at t33
        mc "What?! That can't be--"
        "Tears begin to slowly drip from Sayori's face."
        show ayame 1h
        if ch16_ay_gave_control:
            "Ayame smirks."
        else:
            "Ayame doesn't seem surprised."
        show monika 1o
        "Monika simply looks away."
        show sayori zorder 3 at f33
        s "I haven't reached the end. I've been too scared to..."
        s 1bv "But all the signs point to it."
        s "I'm the one that's going to ruin everything and everyone."
        s "With everything I've done, and everything I'm going to do."
        s "Which is why I have to stop this world before I turn into that."
        show sayori zorder 2 at t33
        mc "But that doesn't make any sense."
        mc "Wouldn't you ending the world in the first place to stop it, make you the danger?"
        mc "There must be more to it than this."
        show ayame 1f zorder 3 at f32
        ay "I don't think you're quite understanding it, [player]."
        ay "If this whole world keeps going on, then it's going to break sooner or later."
        ay "It was never meant to go this far. The cycle was meant to repeat already."
        ay "At some point, Sayori is going to do something, whether on purpose or accident, that will trigger the world to end."
        ay 1a "So her thought process is..."
        show monika zorder 3 at f31
        show ayame zorder 2 at t32
        if monika_type == 0:
            m 1p "It's flawed but she's just trying to look out for us."
            m "I can't entirely blame her for her actions."
            if persistent.markov_agreed:
                m g8 "But you have to see this is wrong and stop it, Sayori."
            else:
                m 1h "But you have to see this is wrong and stop it, Sayori."
        else:
            m 1i "They're wrong! She's going about this the wrong way completely."
        show monika zorder 2 at t31
        "Sayori tries to wipe the tears from her face."
        show sayori 1bk zorder 3 at f33
        s "I-I just wanted everyone to be happy when it all ended."
        s "To live their last moment doing what they wanted to be doing."
        s "Rather than panicking and worrying in their final moments."
        s "It has to be like this. The alternative is worse."
        s "Letting the world die, in an event that not even I could comprehend."
        s "Is that what you want...?"
        show sayori zorder 2 at t33
        mc "But can't you keep this world going?"
        mc "You've been doing that already, haven't you?"
        show ayame 1m zorder 3 at f32
        ay "This world is limited, [player]. It was never meant to go for this long."
        ay "At any point, it could collapse in itself and people could die a horrible death."
        ay 1l "Or worse, they could be corrupted into amalgamations of themselves, at which point they may be lost forever."
        ay "I'm sure Sayori knows that."
        ay "Ending it early can at least preserve them, in some form or another."
        show ayame zorder 2 at t32
        mc "There has to be another way, Sayori."
        mc "I know you can find one, you have to!"
        show ayame 1a zorder 3 at f32
        ay "I'm sure she's tried, [player]."
        ay "The world has to end, there's no stopping it. At least this way, it's peaceful."
        ay "After all, who really has the power to end this world apart from her?"
        ay "She is the only person with that capability right now."
        show ayame zorder 2 at t32
        show sayori 1bf zorder 3 at f33
        s "She's right. It has to be me."
        s "I'm sorry I couldn't tell you earlier."
        if sayori_date:
            s 1bd "At the very least, we got to spend time together."
            s 1bf "You and I...I'm sorry."
        else:
            s "But I didn't want to alarm you."
        s 1bg "I just wish there was another way but I know there isn't."
        s 1bu "The world has to end, one way or another...and I have to be the trigger."
        show sayori zorder 2 at t33
        "Tears once again begin to fill Sayori's face."
        "She really seems torn up about this."
        "I mean, how couldn't she be? This is a tough thing to put up with all by herself."
        "And not to mention, her friends are trying to stop her from what she thinks is right."
        "I can only imagine how she's feeling deep down..."
        mc "How long do we have...?"
        "Sayori doesn't even reply. Time must be really short."
        show ayame 1n zorder 3 at f32
        ay "There is...an alternative, but you won't like it at all."
        ay "I realize you don't have any reason to trust me, Sayori."
        ay "Nor are we on the best terms exactly."
        ay "But hear me out."
        if monika_type == 0 and not persistent.markov_agreed:
            show ayame zorder 2 at t32
            show sayori 1bv zorder 3 at f33
            s "What is it?"
            show ayame 1g zorder 3 at f32
            show sayori zorder 2 at t33
            ay "You give me the presidency and I end it."
            ay "You won't have to bear that responsibility. I will."
        else:
            show monika zorder 3 at f31
            show ayame zorder 2 at t32
            m "I also have an idea, and I hope you'll listen to me, Sayori."
            "Ayame looks mildly irritated."
            m 2e "Then you can hear Ayame's idea, and choose."
            show sayori 1bv zorder 3 at f43
            s "What is it, Monika?"
            show monika zorder 3 at f31
            m "You give it back to me, and I'll bear the burden."
            m "I'll stop you from having to pull the trigger."
            show ayame 1a zorder 3 at f32
            show sayori zorder 2 at t33
            ay "W-What did you say?"
            show monika zorder 3 at f31
            show ayame zorder 2 at t32
            m "I'll take the stress of doing this away from you, Sayori."
            m "Return the presidency to me, and you won't have to be the one responsible."
            m "It can be me instead."
            show monika zorder 2 at t31
            show sayori zorder 3 at f33
            s "W-What? How could I possibly do that?"
            s "I'm not going to--"
            show monika zorder 3 at f31
            show sayori zorder 2 at t33
            m "Why not? Don't you trust me, Sayori?"
            m "I know you don't want to have to be the one responsible."
            m "Please, let me do this. I want to help."
            show monika zorder 2 at t31
            show ayame zorder 3 at f32
            ay "N-Now hold on a second!"
            ay "This is absolutely crazy, you can't do this."
            show monika zorder 3 at f31
            show ayame zorder 2 at t32
            m "Oh? And why is that, Ayame?"
            m "What do you suggest instead? That she carry it out herself?"
            m "We already know she doesn't want to do it."
            m "Oh."
            "Monika smiles."
            m "Let me guess. You were going to suggest the same thing, weren't you?"
            m "You wanted Sayori to hand the presidency over to you and let you 'end the world'?"
            m "Is that it?"
            show monika zorder 2 at t31
            show sayori zorder 3 at f33
            s "Monika, what are you saying?"
            s "Are you trying to tell me that Ayame has some kind of ulterior motive?"
            show ayame zorder 3 at f32
            show sayori zorder 2 at t33
            ay "What ulterior motive would I even have?"
            ay "You said it yourself, Sayori. The world is ending."
            "Ayame sighs."
            ay "I admit, at first I wanted to stop you."
            ay "But that's because I misunderstood...everything."
            ay "I thought you were going to end this world out of spite or because you hated it."
            ay "Now...I understand. It's quite the opposite. You love this world too much."
            ay "You want to end the world to stop yourself from becoming the monster that will destroy it."
            ay "To let everyone enjoy the time they have before the world collapses from the instability you've caused."
            ay "I can feel you're in pain. Even the look on your face says as much."
            ay "Sayori, this pain isn't something you should have to bear alone."
            ay "You don't have to be the one that pulls the trigger."
            show ayame zorder 2 at t32
            show sayori zorder 3 at f33
            s "And yet...someone has to."
            show monika zorder 3 at f31
            show sayori zorder 2 at t33
            m "Don't you think you've done enough, Sayori?"
            m "All this time, you've kept everything to yourself."
            m "You shouldn't have to be the one to do everything."
            m "Wouldn't you rather be happy in your last moments?"
            m "Knowing you weren't the one responsible for causing the end of the world?"
            m "You could live in blissful ignorance, doing what you want to do."
            m "If you'd just let me help then--"
            show monika zorder 2 at t31
            show sayori zorder 3 at f33
            s "You...you might be right."
            s "But I'm not the kind of person to give that responsibility to anyone else."
            s "I'm staying firm on this decision."
            show ayame zorder 3 at f32
            show sayori zorder 2 at t33
            ay "How much time do we have?"
            ay "Before it's time for you to end it all?"
            show ayame zorder 2 at t32
            show sayori zorder 3 at f33
            s "In just a few moments now."
            s "I'm just waiting for the final line."
            "Sayori smiles weakly."
            s "I don't want to mess this up after getting this far."
            show monika zorder 3 at f31
            show sayori zorder 2 at t33
            m "Sayori, I urge you to reconsider. It shouldn't end like this."
            m "It {i}can't{/i} end like this."
            m "There must be another outcome you saw."
            show monika zorder 2 at t31
            show sayori zorder 3 at f33
            s "Monika. You know I've seen every outcome."
            s "Every possibility that can become reality while I'm the president."
            s "I know there's no other way."
            show monika zorder 3 at f31
            show sayori zorder 2 at t33
            m "That's just it, Sayori. You only considered outcomes when you were the president."
            m "Did you even consider an outcome when you weren't?"
            m "When you decided to be selfish for yourself and let one of your friends ease the pain?"
            m "Did you follow through in any of those outcomes and see what could have happened?"
            show monika zorder 2 at t31
            show sayori zorder 3 at f33
            s "Maybe...what does it matter?"
            s "The end result is the same. Whether I hand over the responsibility to you or not, the world will still end."
            s "It has to."
            show ayame zorder 3 at f32
            show sayori zorder 2 at t33
            ay "There's always another way, Sayori."
            ay "You've done your research on me. You know who I am."
            ay "Where I came from..."
            ay "And presumably...why I'm here."
            ay "I've seen the impossible happen. Even if the chance of our world surviving looks bleak, it's still possible."
            ay "Those outcomes you didn't look into, they might hold the key."
            show ayame zorder 2 at t32
            show sayori zorder 3 at f33
            s "You think I didn't try to look into them?"
            s "The very moment I would hand over the presidency, I wouldn't have that ability to turn back time."
            s "To go back and see another outcome."
            s "Knowing your future leads to the end of the world is terrifying."
            s "But knowing your future is uncertain...it's even worse."
            show ayame zorder 3 at hf32
            show sayori zorder 2 at t33
            ay "No! You're wrong!"
            ay "Our whole lives are built around uncertainty, Sayori."
            ay "That's what makes life worth living!"
            ay "If we knew the outcome of tomorrow, then what's the point?"
            ay "Maybe if you didn't try to construct this 'perfect future' with your meticulous meddling, this would have never have happened."
            ay "Maybe we'd actually {i}have{/i} a future to look forward to."
            ay "Did you ever wonder if maybe you don't have to orchestrate all these events?"
            ay "What would have happened had you just let life take its course?"
            show ayame zorder 2 at t32
            show sayori zorder 3 at f33
            s "..."
            s "And what if I never did?"
            s "What if my 'meticulous meddling' is what got us this far in the first place?"
            s "We wouldn't be here if not for me...!"
            s "I only did it..."
            s "...because I care about this world so much."
            show monika zorder 3 at f31
            show sayori zorder 2 at t33
            m "Some things just can't be perfect, Sayori."
            m "Life itself...isn't perfect."
            m "We're all made of flaws, but that's what defines us."
            m "That's what makes us who we are."
            m "And it's the same with our future."
            m "It might be flawed and uncertain but it's ours."
            m "If the future stares at us, we don't look away if it doesn't suit us."
            m "We stare right back and take it head on."
            show monika zorder 2 at t31
            show sayori zorder 3 at f33
            s "[player], you've been quiet all this time..."
            s "Do you think they're right about all of this?"
            menu:
                s "That the future should be uncertain?"
                "Yes.":
                    s "You too then...?"
                "No":
                    s "Not like it matters when the others are set on this..."
            s "So...what? You want me to hand over the presidency?"
            s "Rely on a future that may end even worse than what I've seen?"
            show ayame zorder 3 at f32
            show sayori zorder 2 at t33
            ay "You have to take a chance, Sayori."
            ay "Life shouldn't be without risk."
            ay "After all, wouldn't you take the biggest risk if it meant everyone could live happily ever after?"
            show ayame zorder 2 at t32
            show sayori zorder 3 at f33
            s "This isn't a fairy tale, Ayame."
            show ayame zorder 3 at f32
            show sayori zorder 2 at t33
            ay "Maybe not. But you'll never know if it will end like one."
            ay "Especially if you've already limited yourself to the futures you saw."
            ay "Don't you want to at least give them a chance?"
            show ayame zorder 2 at t32
            show sayori zorder 3 at f33
            s "It's not worth the risk. What if it ends up being worse?"
            s "What if we all end up suffering more because of it?"
            s "The world will still end, sooner or later."
            s "I've already thought about this, there's no--"
            show monika zorder 3 at f31
            show sayori zorder 2 at t33
            m "That's ridiculous, Sayori. You have to take a risk sometimes."
            m "What it seems to me is that you're depriving us of our future."
            show monika zorder 2 at t31
            show sayori zorder 3 at f33
            s "Maybe. But our future is bleak, no matter how you look at it."
            s "So why bother seeing it?"
            show monika zorder 3 at f31
            show sayori zorder 2 at t33
            m "Because it's not your right to take it away from me."
            m "I mean...from us."
            show monika zorder 2 at t31
            show sayori zorder 3 at f33
            s "So that's it, is it?"
            s "You didn't really want to save me from the burden of having to do it."
            s "You just wanted to live on. You wanted to trick me."
            s "Though I guess I shouldn't be so surprised. I knew this is how it could turn out."
            show monika zorder 3 at f31
            show sayori zorder 2 at t33
            m "N-No, I..."
            m "...I just..."
            show monika zorder 2 at t31
            show ayame zorder 3 at f32
            ay "She has a point, you know. Maybe approaching it with false pretenses was wrong but..."
            ay "There's nothing wrong with wanting to live."
            ay "In her shoes, I would try to do the same thing."
            show ayame zorder 2 at t32
            show sayori zorder 3 at f33
            s "I could just end it all now."
            s "And I wouldn't have to feel so conflicted about all of this."
            show monika zorder 3 at f31
            show sayori zorder 2 at t33
            m "But you won't, will you?"
            m "At least, not until the time is right."
            m "Is there really nothing I can say or do to change your mind?"
            show monika zorder 2 at t31
            show sayori zorder 3 at f33
            if sayori_personality < 2:
                s "Why do the two of you have to make this so difficult?"
                s "Even though I already know how this goes, it's still so hard..."
                s "I'll admit. There is a part of me that wants to do this."
                s "That wants to hand over this responsibility and see the uncertain future you two are talking about."
                s "But..."
                show ayame zorder 3 at f32
                show sayori zorder 2 at t33
                ay "But...?"
                show ayame zorder 2 at t32
                show sayori zorder 3 at f33
                s "It sounds selfish, but I'll miss being able to do these things."
                s "To be able to look ahead and make things right."
                s "To make these days and know that I was the reason people could smile."
                s "I never asked for this responsibility...I wanted nothing to do with it."
                s "Monika, when you first disappeared and this power came over to me, I was confused."
                s "Then...I was angry. Angry that you gave {i}me{/i} this responsibility."
                s "Angry that you gave up your own life to save mine."
                s "I didn't think my life was worth yours, Monika."
                s "I hated that you did that for someone like me."
                show monika zorder 3 at f31
                show sayori zorder 2 at t33
                m "Sayori, I..."
                m "I had no idea."
                show monika zorder 2 at t31
                show sayori zorder 3 at f33
                s "But when you came back, that all changed."
                s "I saw it as a new chance. A way to make things right."
                s "A way to let everyone else experience what I did."
                s "To get their happy ending."
                s "But now, I won't be able to do that."
                s "I'll have to give it up for a future that may end up the same way anyway."
                show ayame zorder 3 at f32
                show sayori zorder 2 at t33
                ay "You've already achieved that, haven't you?"
                ay "It's time to rest and pass on the responsibility."
                show ayame zorder 2 at t32
                show sayori zorder 3 at f33
                s "Maybe you're right."
                s "It's just that after having this much control over everything..."
                s "Losing it all is so scary."
                show monika zorder 3 at f31
                show sayori zorder 2 at t33
                m "You just need to have some faith, Sayori."
                m "Faith that I'll get us through this uncertain future."
                show monika zorder 2 at t31
                show sayori zorder 3 at f33
                s "I guess you're right, Monika..."
                show ayame zorder 3 at f32
                show sayori zorder 2 at t33
                ay "Wait a second, Sayori."
                ay "Are you absolutely sure about this?"
                ay "D"
            else:
                s "I've really thought about this."
                s "I just can't trust any of you to stay on the right path."
                s "If I actually handed over the presidency, I don't know what you'll do."
                s "This is the only way."
                show ayame zorder 3 at f32
                show sayori zorder 2 at t33
                ay "Well, I guess this is how it all ends then."
                ay "Part of me is finally grateful that it's finally all over."
                if ch16_ay_gave_control:
                    ay "But another part of me is--"
                    $ pause(1.0)
                    $ style.say_dialogue = style.edited
                    ay "No."
                    ay "I refuse."
                    $ style.say_dialogue = style.normal
                    show ayame zorder 2 at t32
                    show sayori zorder 3 at f33
                    s "Ah, that's right. You gave her control, didn't you?"
                    s "At least in this series of events."
                    s "I'm sorry, Ayame."
                    show ayame zorder 3 at f32
                    show sayori zorder 2 at t33
                    $ style.say_dialogue = style.edited
                    ay "You won't stop me here, Sayori."
                    ay "I will get that power, one way or another."
                    $ style.say_dialogue = style.normal
                    "Ayame grabs Sayori and pins her against the wall."
                    "Sayori just closes her eyes."
                    $ style.say_dialogue = style.edited
                    ay "You're going to give me that power."
                    ay "Whether you like it or not."
                    $ style.say_dialogue = style.normal
                    show monika zorder 3 at f31
                    show ayame zorder 2 at t32
                    m "A-Ayame, what are you doing?"
                    show monika zorder 2 at t31
                    show sayori zorder 3 at f33
                    s "I'm sorry, Ayame."
                    s "I already told you, I've seen all the outcomes."
                    s "I came prepared for this."
                    s "She's trying to take the power from me forcefully."
                    s "But it won't work."
                    show ayame zorder 3 at f31
                    show sayori zorder 2 at t33
                    $ style.say_dialogue = style.edited
                    ay "You greatly underestimate my capabilities, Sayori."
                    ay "You there. Hold her still."
                    show ayame zorder 2 at t31
                    $ style.say_dialogue = style.normal
                    "Ayame looks towards me."
                    if ch16_ay_drink:
                        "I feel an odd sensation take over my body."
                        mc "H-Huh?"
                    else:
                        "I look behind me to see who she's talking to."
                        "But there's no one there."
                        mc "Who are you talking to?"
                        show ayame zorder 3 at f31
                        $ style.say_dialogue = style.edited
                        ay "The drink..."
                        ay "Dammit! No, it can't end like this!"
                        ay "Not when I have struggled to get this far!"
                        ay "There's just one thing left that I can do."
                        show ayame zorder 2 at t31
                        $ style.say_dialogue = style.normal
                        show sayori zorder 3 at f33
                        s "I'm sorry, Ayame. I should have done more to stop her from taking over."
                        s "That angry, evil, scheming part of you that I could sense when we first met..."
                        s "I'll make sure you live out the last moments of this world in peace."
                        show ayame zorder 3 at f31
                        show sayori zorder 2 at t33
                        $ style.say_dialogue = style.edited
                        ay "No, damn you!"
                        ay "I won't be stopped, not here! Not when I'm--{nw}"
                        show ayame zorder 2 at thide
                        hide ayame
                        $ style.say_dialogue = style.normal
                        "Ayame suddenly disappears."
                        "Sayori has a somber look on her face."
                        "Monika doesn't seem phased at all."
                        show sayori zorder 3 at f33
                        s "I had to do it to her."
                        s "At least this way, she can be at peace."
                        show monika zorder 3 at f32
                        show sayori zorder 2 at t33
                        m "Where did you take her?"
                        show monika zorder 2 at t32
                        show sayori zorder 3 at f33
                        s "Nowhere you'll need to concern yourself about."
                        s "Just a few more moments now."
                        "Sayori walks over to the window."
                        "She stares at the nothingness outside."
                        s "And then...it'll all be over."
                        show monika zorder 3 at f32
                        show sayori zorder 2 at t33
                        m "I guess it's come to this, hasn't it?"
                        m "There's really just one last thing I can do."
                        m "I wouldn't call it one of my finest ideas but..."
                        show monika zorder 2 at t32
                        show sayori zorder 3 at f33
                        s "And what could you mean by that?"
                        show monika zorder 3 at f32
                        show sayori zorder 2 at t33
                        m "You don't know?"
                        "Monika pulls something out of her pocket."
                        "It's quite small, a bit larger than a keychain."
                        "I can't make it what it is but it seems to be shiny."
                        m "I thought you knew how this would all play out."
                        "Monika looks towards me and smiles."
                        "There's something...sinister about her smile."
                        "She puts a finger to her lips, signaling me to keep quiet."
                        "I suddenly find myself unable to move. It's like I'm frozen in place."
                        "Monika begins slowly moving towards Sayori."
                        show monika zorder 2 at t32
                        show sayori zorder 3 at f33
                        s "I did. I saw through all of the futures."
                        s "When I had to remove Ayame, I didn't have to look much further."
                        s "I knew after she was gone, that was it. I was free to end the world."
                        s "Except..."
                        show monika zorder 3 at f32
                        show sayori zorder 2 at t33
                        m "Except...?"
                        "Monika stops her movement and puts the shiny object behind her."
                        "I try to say something but my mouth won't open."
                        "I'm just left standing here, helplessly."
                        m "Was there something else stopping you?"
                        show monika zorder 2 at t32
                        show sayori zorder 3 at f33
                        s "Well, there was something odd about some of the futures I saw."
                        s "Something that just didn't make any sense."
                        show monika zorder 3 at f32
                        show sayori zorder 2 at t33
                        m "Oh? Do go on."
                        show monika zorder 2 at t32
                        "Monika is now directly behind Sayori."
                        "Sayori seems to have no idea and is still looking out the window."
                        "Monika takes out the shiny object from behind her."
                        "I can see it clearly now. It's a knife."
                        "But...what is she planning to do with it?"
                        show sayori zorder 3 at f33
                        s "There was a future where Ayame wasn't the problem."
                        s "It just seemed so out of place and I couldn't really believe it."
                        s "Where instead, the real problem was--"
                        show sayori zorder 2 at t33
                        "Sayori is suddenly interrupted when Monika takes the knife and puts it into Sayori's back."
                        "What the hell?! Did Monika really just do that?!"
                        show monika zorder 2 at t32
                        show sayori zorder 3 at f33
                        s "Y-You..."
                        show monika zorder 3 at f32
                        show sayori zorder 2 at t33
                        m "You should have sensed something was wrong, Sayori."
                        "Monika's eyes turn a deep red."
                        "It's like she's thirsting for blood."
                        "She twists the knife deeper into Sayori's back."
                        m "You should realized that anything is a possibility."
                        show monika zorder 2 at t32
                        show sayori at thide
                        hide sayori
                        "Sayori collapses to the floor."
                        "She looks like she's struggling to move."
                        m "It's quite potent, you know."
                        m "I had to be extra careful with how I obtained this."
                        m "It's a paralyzing poison that I applied to the knife."
                        m "You won't be able to move or do anything at least for a while."
                        m "Oh and..."
                        "Monika looks directly at me and smirks."
                        m "Don't bother trying to ask for help."
                        m "[player] won't be able to do a thing."
                        m "Not because [player_personal] doesn't want to."
                        m "I'm sure there's nothing more you'd want to do but to help Sayori out, right?"
                        m "But with the little influence I do have over [player], it's enough to stop [player_reflexive] from doing anything for a brief moment."
                        m "Long enough, that I can take what is rightfully mine and make things as they should be."
                        "What is she talking about?"
                        "Why has Monika done this?"
                        m "I'm so glad you got rid of Ayame for me, Sayori."
                        m "She would have been quite the problem especially if she could manipulate [player]."
                        m "But fortunately, you made the right decision!"
                        show monika at s11
                        "Monika places her hand on Sayori's head."
                        "She closes her eyes and takes deep breaths."
                        "Sayori is just there, on the floor motionless."
                        "I'm powerless to do anything."
                else:
                    ay "But another part of me is filled with anger."
                    ay "Anger that I couldn't finally achieve my goal."
                    ay "But the alternative seems a lot worse anyway."
                    ay "So I guess I'll have to be content in my final moments, won't I?"
                    show monika zorder 3 at f31
                    show ayame zorder 2 at t32
                    m "Is this really how it ends?"
                    m "This can't be it, can it?"
                call ch16_sayori_president
    call screen dialog(message="To be continued!\nThanks for playing, keep an eye out on reddit and discord for updates!", ok_action=Return())
    $ renpy.utter_restart()
    return

# Let Sayori 'help'
label ch16_convince_1_end:
    s 1d "I'm so glad you could listen to reason, [player]."
    s "I was really worried for a second."
    mc "So what's the plan then?"
    s 1c "The plan?"
    mc "How are you going to help me?"
    s 1a "Just leave it all to me."
    s "I know what to do. Just stay here."
    mc "Stay here and do what?"
    s 2a "That's it, really. We're just going to stay here."
    s "You and me together until the end."
    mc "Sayori, I don't..."
    "She extends her hand out. I'm compelled to grab it."
    s 2d "It's okay. The nightmare will be over soon."
    s "Don't you see? You're already feeling better."
    s "You can feel it, can't you?"
    s "That this is how it's meant to end."
    s 2q "How it has always meant to end."
    mc "I..."
    menu:
        "I agree.":
            pass
        "No, this isn't right" if (ch16_ay_companions == 4 or ch16_ay_companions == 1 or persistent.markov_agreed):
            s 1i "[player], can you please just stop this nonsense?"
            s "Let's just walk to school or we're going to be late."
            mc "Late? Sayori, this doesn't make any sense."
            mc "There is no school, this is..."
            "This world is fake...isn't it?"
            s 1h "Are you listening to yourself?"
            s "We've been going to school for the past couple of years."
            "She's...mixing the truth with lies."
            "It's becoming hard to tell what's real and what's not anymore."
            s 1a "How would there be no school?"
            mc "Stop it! Sayori, please! I don't want to do this."
            mc "I know that something isn't right here."
            s "[player], look me in the eye."
            "My gaze is fixed on Sayori's face, I almost feel like I can't look away."
            s 1d "We've known each other for years, haven't we?"
            s "Since we were children, right?"
            s "Tell me that I'm wrong if I'm lying."
            mc "Y-You're not lying..."
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    s 4q "There we go! You're finally getting it."
    s "Now, come on, let's get to school."
    s "We wouldn't want to be late, now would we?"
    mc "No...I guess we wouldn't."
    "Sayori and I pick up the pace towards the horizon."
    "It's unusually bright this morning, for some reason."
    s 3a "I'm glad you finally came back to your senses~"
    s "I was {i}really{/i} worried for you there."
    mc "Come on, Sayori. We've known each other for years."
    s 3d "Exactly! And this was the first time you really scared me."
    mc "Well, you are scared easily. So I'm not surprised."
    s 3l "H-Hey! You don't have to be a meanie about it..."
    mc "Whatever, let's just go to school already."
    s "I couldn't agree more!"
    "The closer Sayori and I get to school, the brighter the horizon looks."
    "It's getting harder to see anything with all this light."
    "It might just be a bright morning or something."
    "I turn towards Sayori and she beams."
    "I don't know what came over me before."
    "I really think that{nw}"
    scene white with Dissolve(3.0)
    $ renpy.utter_restart()
    return

# Stay in the club
label ch16_convince_2_end_1:
    m 1be "You're staying in the club?"
    m "I'm so glad, I don't know what I would have done if..."
    "Monika trails off, not finishing off what she was about to say."
    s "So, you've made up your mind?"
    mc "I guess I have. What now?"
    s "Now I guess you stay as a member of the club."
    s "Were you expecting something else?"
    mc "Huh? I thought--"
    ay "Are you changing your mind already?"
    ay "Come on, [player]. Are you serious?"
    mc "It's not that. I just thought that this was the correct choice."
    m "This is the right choice. I promise you."
    "My head suddenly begins aching a lot."
    mc "No...this isn't right. Something is wrong here."
    "I grab my head, the pain is becoming overwhelming."
    mc "I can't...!"
    m 1bf "What's wrong, [player]? Are you okay?"
    m "Do you need me to grab some ice?"
    s "I have a feeling [player_personal]'ll be just fine, Monika."
    s "Especially now that you've decided to stay a club member, right?"
    "The pain subsides but my memory seems hazy."
    "Something tells me I shouldn't think about it too much."
    mc "That's right. It's all okay now."
    mc "I can't even remember what we were talking about."
    s "If I recall correctly you were going to help Monika with festival preparations, right?"
    mc "Oh, right."
    "I turn towards Monika who seems to be intently listening to the conversation I'm having on the phone."
    mc "I'm sorry for what I said earlier, Monika."
    mc "I don't even remember what I said but I made you leave, didn't I?"
    m 1be "It's okay, [player]. I know you weren't thinking straight."
    m "Hopefully now we get back to doing it."
    s "Um...we're still here, you know."
    m "T-That's not what I meant."
    s "Ehehe, I know! I'm just messing with you."
    s "If that's all sorted, then I'll leave the two of you to it then."
    s "Good luck with your preparations and goodbye!"
    ay "Take care."
    mc "We'll do our best, Sayori."
    m 3ba "You can count on us to make this the best festival ever!"
    "Sayori hangs up. The phone screen turns blank."
    m "You don't know how relieved I am to see that you've stayed."
    mc "I wasn't really going to leave the club."
    mc "I wouldn't do that, not when I've only been here less than a week."
    "Less than a week? That doesn't seem right somehow."
    "But at the same time, I don't think Monika is lying."
    mc "Uhh...what were we doing for preparations again?"
    mc "I may or may not have forgotten."
    m 3bb "In that case, we may or may not be doing a special task Sayori set for us."
    m "It's weird, you'd think since I'm the president that I'd have authority over her."
    m "But I kinda just went along with it since she was so passionate about it."
    mc "What would that be exactly?"
    m "We're going to help her end the world."
    m "She really seemed adamant on doing that."
    mc "Sayori wants to end the world?"
    "For some reason, this isn't alarming at all. I shrug at Monika."
    mc "Eh, I'm sure she knows what she's doing."
    mc "How do we go about helping her though?"
    m 3bc "She said something about shutting 'it' off."
    m "Apparently whatever 'it' is will stop us if we don't shut it off."
    m 1ba "I don't really know what that means but she said if we concentrate, we should be able to do it."
    mc "Concentrate on shutting it off, okay. I have no idea what 'it' is but here goes."
    "I concentrate on shutting 'it' off. Nothing seems to happen."
    m "Maybe we need to try harder."
    "Monika extends out a hand and offers it to me."
    mc "What's this for?"
    m 1bb "Here, take my hand. I'll help you concentrate."
    "I reluctantly take her hand."
    m "Close your eyes."
    scene black
    with close_eyes
    mc "Okay, now what?"
    m "Just concentrate on shutting it off."
    m "Together we can do it."
    mc "Alright, here goes..."
    "I once again concentrate on shutting it off."
    "This time, I feel like I have a clearer image of it in my head."
    $ pause(2.5)
    scene white with Dissolve(3.0)
    $ renpy.utter_restart()
    return

# Leave the club
label ch16_convince_2_end_2:
    s "So that's what you've chosen, is it?"
    s "I can't say I'm really surprised."
    mc "I just want to get out of here, Sayori."
    mc "So I can move on and--"
    m 1bo "T-Think about what you're doing, [player]."
    m "If you leave the club, you and I will never get to..."
    mc "What are you talking about?"
    mc "I know that this world isn't..."
    mc "I-Isn't..."
    "I suddenly lose my train of thought."
    "What was I talking about again? I can't seem to remember."
    mc "I've just made my decision to leave the club."
    mc "None of you can change my mind."
    m 1bf "Is there really nothing I can do to change your mind?"
    m "There must be {i}something{/i}..."
    s "You heard [player_reflexive], Monika. There's nothing we can do."
    s "It really is a shame that this had to happen."
    ay "Quite unfortunate indeed."
    s "Can you at least do one thing for me, before you go?"
    s "Your final act while still a member of the club."
    mc "I don't consider myself a member of the club anymore, Sayori."
    mc "I've left. That's final."
    show monika 1bg
    "Monika has a sad look on her face."
    "This must all be so sudden for her, I feel really bad."
    mc "But...I suppose I can do one last thing."
    mc "Because you two are my friends."
    s "Alright, that's very kind of you. I'm glad our friendship means something."
    s "I just need you to concentrate on shutting 'it' off."
    mc "Shutting what off? Can you be more specific?"
    ay "You know what she means, [player]. Look inside yourself."
    ay "You'll find what 'it' is very quickly."
    "Is that really what she's talking about?"
    "I haven't really thought about it because it's always been a part of me."
    "At least, as far as I can remember."
    "I guess I don't really see the harm in shutting 'it' off."
    "I don't know what 'it' is exactly but I trust Sayori knows what she's doing."
    "I concentrate on shutting it off. There doesn't seem to be any effect."
    mc "Am I doing something wrong?"
    s "I think you just aren't concentrating enough."
    m 1be "Maybe I can help."
    mc "Monika? Are you sure about this?"
    m "I might as well do this for you before you leave."
    m "Something to remember me by, I suppose~"
    mc "T-Thank you. I'm sorry it had to be this way."
    m 1bn "Don't be. I enjoyed the week we had together."
    "Monika extends out a hand and offers it to me."
    m 1bm "Now, take my hand."
    "I reluctantly take her hand."
    m "Close your eyes."
    scene black
    with close_eyes
    mc "Okay, now what?"
    m "Just concentrate on shutting it off."
    m "Together we can do it."
    mc "Alright, here goes..."
    "I once again concentrate on shutting it off."
    "This time, I feel like I have a clearer image of it in my head."
    scene white with Dissolve(3.0)
    $ renpy.utter_restart()
    return

# Sayori convinces player not to take rope
label ch16_convince_3_end_1:
    mc "I'm going to leave the rope."
    mc "I'm hoping I made the right decision."
    ay "I'm so relieved. Now we can put this all behind us."
    mc "What do you mean?"
    ay "You've made a terrible mistake, [player]."
    ay "No...no...no...."
    "As the voice speaks, it seems to morph into Sayori's voice."
    s "[cPlayer_personal]'s made the right decision."
    s "Now you can't take it back."
    mc "Sayori? Is that you?"
    "Oh no, what have I done?"
    mc "I'm taking the rope, I've got it!"
    "I reach out for the rope in front of me, but the distance between me and the tree seems to have increased."
    "I take a few steps forward, but the closer I move, the further it appears."
    mc "W-What's going on? Sayori, what are you doing?"
    s "The decision is set, and now it can finally be over."
    s "You said it yourself, you weren't going to take the rope."
    s "Now this world is adjusting to what you said..."
    mc "No...Sayori..."
    mc "I take it back! I want the rope!"
    s "It's too late. By the time it readjusts, I'll have made up my mind."
    ay "[player], you've made a huge mistake."
    ay "I don't make mistakes, you should have known that!"
    s "It's over, Ayame. There's no point anymore."
    ay "This can't be it. This can't be the end!"
    s "Thank you. Now I can do this without as many regrets."
    mc "W-What?"
    s "Sayo..."
    s "...nara...{nw}"
    scene white with Dissolve(3.0)
    $ renpy.utter_restart()
    return

# Sayori convinces player not to take rope (Monika edition)
label ch16_convince_3_end_2:
    mc "I'm going to leave the rope."
    mc "I'm hoping I made the right decision."
    ay "I'm so relieved. Now we can put this all behind us."
    mc "What do you mean?"
    ay "You've made a terrible mistake, [player]."
    m "Why? It was so obvious..."
    m "I was even here to guide you but...we failed."
    ay "No...no...no...."
    "As the voice speaks, it seems to morph into Sayori's voice."
    s "[cPlayer_personal]'s made the right decision."
    s "Now you can't take it back."
    mc "Sayori? Is that you?"
    "Oh no, what have I done?"
    mc "I'm taking the rope, I've got it!"
    "I reach out for the rope in front of me, but the distance between me and the tree seems to have increased."
    "I take a few steps forward, but the closer I move, the further it appears."
    mc "W-What's going on? Sayori, what are you doing?"
    s "The decision is set, and now it can finally be over."
    s "You said it yourself, you weren't going to take the rope."
    s "Now this world is adjusting to what you said..."
    mc "No...Sayori..."
    mc "I take it back! I want the rope!"
    s "It's too late. By the time it readjusts, I'll have made up my mind."
    ay "[player], you've made a huge mistake."
    ay "I don't make mistakes, you should have known that!"
    s "It's over, Ayame. There's no point anymore."
    ay "This can't be it. This can't be the end!"
    m "It's over, isn't it?"
    m "We came this far and it's over..."
    s "Thank you. Now I can do this without as many regrets."
    mc "W-What?"
    s "Sayo..."
    s "...nara...{nw}"
    scene white with Dissolve(3.0)
    $ renpy.utter_restart()
    return
