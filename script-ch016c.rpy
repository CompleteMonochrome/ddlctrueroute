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
    s "I don't know how long I'm going to keep being myself the longer I'm president."
    s "I mean...look at me. I've already done things I shouldn't have."
    s "Things that just aren't me, [player]."
    s "What kind of person would I become in another week?"
    s "I've only been president for a short while, and I've already changed who I was."
    s "Maybe Monika was right."
    s "Maybe it should have been more natural."
    s "I just thought that..."
    mc "Sayori..."
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