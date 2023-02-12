label ch16_ayame_president:
    $ get_achievement("*Welcome To The Book Club!*")
    # Unlock Ayame bonus day
    $ persistent.old_ayame_bonus = True
    return

label ch16_old_ayame_president:
    $ get_achievement("*The Plan Revealed*")
    return

label ch16_monika_president:
    $ get_achievement("*Once Again*")
    # Unlock True Monika bonus day
    $ persistent.true_monika_bonus = True
    return

label ch16_markov_president:

    if monika_type == 1 and ch12_markov_agree:
        # Unlock evil Monika loving player bonus day
        $ persistent.love_markov_bonus = True
    else:

    $ get_achievement("*At Long Last*")
    return

label ch16_true_sayori_president:
    s "I only wanted what was best for all of us."
    s "That's why I wanted to help them."
    s "Why I wanted to solve their problems for them..."
    s "But that's wrong, isn't it?"
    s "I should've given them a small nudge."
    s "Just to help them, one step at a time."
    s "Instead, I shoved them right into the deep end."
    s "And I could see I was wrong."
    s "And I thought that was because given enough time, this world can only bring pain."
    s "They might've been happpy then but it's only a matter of time before they get hurt again."
    s "But these feelings you've given me have changed my mind."
    $ get_achievement("*Unlimited Strawberries*")
    # Unlock True Sayori bonus day
    $ persistent.true_sayori_bonus = True
    return

label ch16_sayori_president:
    s "This is my decision."
    s "I feel like, for once, I can make this with a clear head."
    s "No one to tell me what's right and wrong."
    s "Just my own judgement."
    mc "Is this really the right thing to do, Sayori?"
    s "It has to be like this, [player]."
    s "This power is just too powerful."
    s "I wanted to help my friends..."
    s "I wanted to solve their problems."
    s "And I did, didn't I?"
    s "Yuri isn't cutting herself anymore and Natsuki..."
    if ch12_outcome == 3:
        s "Well, she's got her family back, doesn't she?"
    elif ch12_outcome == 2:
        s "Well, she's got her mom back, doesn't she?"
    elif ch12_outcome == 1:
        s "Well, her dad isn't such a bad person now, isn't he?"
    else:
        s "Well...she's working things out without her dad."
    s "Is that a good thing?"
    s "Those things won't be bothering them anymore."
    s "Basically, I cured them, right?"
    mc "I...guess so?"
    s "And now it's time to make sure it stays that way."
    s "I don't want them to have new issues to go through."
    s "They don't deserve to be sad anymore."
    s "With this power, I can make that happen."
    mc "Can't you keep helping them?"
    mc "If that power is as strong as you say it is, then you could keep helping them."
    mc "And the world doesn't have to end."
    s "But at what cost, [player]?"
    s "I don't know how long I'm going to keep being myself the longer I'm president."
    s "I mean...look at me. I've already done things I shouldn't have."
    s "Things that just aren't me, [player]."
    s "What kind of person would I become in another week?"
    s "I've only been president for a short while, and I've already changed who I was."
    s "Is it because I used this power too much?"
    s "Maybe Monika was right."
    s "Maybe it should have been more natural."
    s "Trying to make things end up perfect was just impossible."
    s "You were always that factor that could just make things turn out the wrong way."
    s "But still...I had to try."
    s "And the more I did, the more it would hurt."
    s "I just thought that..."
    "Sayori's eyes begin to tear up."
    s "I didn't want them to be sad."
    s "I wanted to make them happy sooner."
    mc "Sayori...you had good intentions."
    mc "It's just..."
    s "It wasn't just that."
    s "There was a faint feeling I had."
    s "Like I could sense the whole world around me."
    s "It was easy to ignore first, I didn't think about it."s
    s "But as the days went by, it would become stronger."
    s "It was like I could feel Yuri, Natsuki and...even Monika's feelings."
    s "I wasn't sure about it at first."
    s "But when we helped Yuri, part of it went away."
    s "It's like the sky cleared up a little bit."
    s "Some rainclouds went away but most of them were still there."
    s "And the ones that stayed only grew stronger."
    s "It just felt like I needed to get rid of them."
    s "When we helped Natsuki, it made those rainclouds go away too."
    s "And for a few moments, it felt like things were finally perfect."
    s "But it didn't last long..."
    s "The rain came back and it was even worse."
    s "What felt what was just a little rain before, now felt like a storm."
    s "It was like these feelings were kept inside for a long time and were all coming out at once."
    mc "New feelings after Natsuki?"
    mc "Wouldn't all the rainclouds have gone away?"
    mc "Whose feeling are you talking about?"
    mc "Was it Monika's?"
    if monika_type == 0 and not persistent.markov_agreed:
        s "No, it wasn't Monika."
        s "Ever since I became the president, it felt like her problems just went away."
        s "Maybe that was your doing."
        s "And I'm glad that you two could solve her problems."
        s "Who I'm talking about is Ayame."
    else:
        s "It wasn't just Monika anymore."
        s "At least, I don't think so."
        s "There was some rainclouds from her."
        s "But it's like she was hiding them from me somehow."
        s "Or like the storm was coming later..."
        s "But I'm talking about Ayame."
    s "Her feelings felt like a whole storm of emotions."
    mc "Ayame? But you said you only felt Yuri, Natsuki and Monika's feelings."
    s "That's what I thought at first."
    s "I didn't even know it was her until I had already made my mind up about what to do.."
    s "She had her own problems, and they seemed more complicated than anyone elses."
    s "And I knew nothing about her. She's from a different kind of place from the rest of us."
    s "Amd even with my power, how long would it take to help her?"
    s "Would I still be me by the time it's all over?"
    s "I needed these feelings to go away."
    s "Even now, with her gone, it's still pouring hard."
    s "It's like they're a part who I am now."
    s "I have to solve her problems for the rainclouds to fully go away."
    s "Or...I could just end things here."
    mc "So you had some other reason to want the world to end?"
    s "I admit, it's a seflish reason."
    s "But honestly...it's part of why I want to end this world now."
    s "And why I won't change my mind."
    s "Things right now aren't perfect."
    s "But I don't know if I can deal with it for much longer."
    s "I don't know if I want to deal with it."
    s "Ha...listen to me."
    s "I would have done anything to make Ayame's problems go away at the beginning of this."
    s "It's best that this world...that this {i}game{/i} ends, [player]."
    s "For your sakes..."
    "Sayori stares into the void."
    "She has a really tired look on her face."
    "As if she could collapse at any moment,"
    s "...and my own."


    s "I'm sorry."
    s "This is for the good of all, [player]."
    $ get_achievement("*For The Good Of All*")
    return

label ch16_mc_president:
    show monika zorder 2 at t31
    show sayori zorder 3 at f33
    s "[player]...are you sure about this?"
    s "This isn't a choice you should make lightly."
    s "Once you have this power...your whole world will change."
    s "The way you think, the way you feel, the way you see us."
    s "It's all going to be different."
    s "Do you really want that?"
    show ayame zorder 3 at f32
    show sayori zorder 2 at t33
    ay "That was the choice that was made, wasn't it?"
    ay "There's no turning back."
    show monika zorder 3 at f31
    show ayame zorder 2 at t32
    m "It sure beats ending this world."
    m "Though whether the new world that [player] will come up with is any better than our current one..."
    m "Well, that's yet to be seen. But at least we'll have a world to live in."
    show monika zorder 2 at t31
    show sayori zorder 3 at f33
    s "[player], I don't know what you have in store for us."
    s "I think you really do want to help us."
    s "But that's not the reason I'm scared to give you this power."
    s "I just don't want you to feel the way we did."
    s "The way...{i}I{/i} do..."
    show sayori zorder 2 at t33
    "I can feel a strange sensation take over my body."
    "It's like nothing I've ever felt. Like something clicked in my head and changed the way I think."
    "Is this what they've been dealing with?"
    "I feel like I have the power to change the world, and in a way, I guess I do."
    "But at the same time..."
    "I can feel a range of emotions rush through me."
    "Are these the feelings of the previous presidents?"
    "There's sorrow...anger...despair...loneliness..."
    "This must have been what they went through and what they felt."
    "And now I understand them."
    $ get_achievement("*It's Up To Me*")
    # Unlock MC bonus day
    $ persistent.mc_bonus = True
    return