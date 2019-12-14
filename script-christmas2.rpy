label christmas_chapter:
    # Alternate Reality?
    $ chapter = 1000
    scene black
    if from_custom_start:
        $ from_custom_start = False
        $ quick_menu = True
        hide screen tear
    $ cl_name = "???"
    if presistent.did_christmas2_event:
        cl "Ho, ho, oh, it's you again."
        cl "Why are you even here?"
        cl "Are you expecting something new to happen?"
        cl "Because I can guarantee you, nothing new is gonna happen."
        cl "Buuut whatever. I'll just pretend this conversation never happened."
        cl "Just to make it easier for myself."
        cl "You understand right?"
        cl "Now...where was I."
        cl "Oh, yeah. Today is a day to have fun, yada, yada."
        cl "Enjoy it and so on and so forth."
    elif persistent.did_christmas_event and not presistent.did_christmas2_event:
        cl "Ho, ho, ho! Good to see you."
        cl "Back again, are you?"
        cl "I don't know what you think you're gonna get out of this."
        cl "But since it's something special, probably something good."
        cl "Or...at least not inherently bad."
        cl "I wonder what you'll do."
        cl "Not like you'll have much choice anyway!"
        cl "But seriously. Don't mess this up."
        cl "It's just a day to have fun."
        cl "A day to relax."
        cl "A day where everyone will get exactly what they want."
        cl "So enjoy it."
        cl "Okay?"
        cl "Well, I mean it's not like I can force you to enjoy it."
        cl "I'm just suggesting--"
        cl "Alrighty, I'll shut up now."
    else:
        cl "Ho, ho, ho! It's Christmas!"
        cl "Or at least, in our time it's Christmas."
        cl "Do you know what that means?"
        menu:
            "No.":
                pass
        cl "Of course you don't!"
        cl "I mean, how could you, right?"
        cl "It's not like you've done this before."
        cl "Have you...? Well, if you did then good for you!"
        cl "You're going to waste your time...again."
        cl "If not, then I only have a couple of things to say to you."
        cl "This isn't something you can mess up."
        cl "Even if you tried really, really hard."
        cl "It's just a day to have fun."
        cl "A day to relax."
        cl "A day where everyone will get exactly what they want."
        cl "So enjoy it."
        cl "Okay?"
        cl "Well, I mean it's not like I can force you to enjoy it."
        cl "I'm just suggesting--"
        cl "Alrighty, I'll shut up now."
    scene bg club_day with Dissolve(1.5)
    play music t2 fadein 3.0
    # Continuation of last Christmas event - canon is the good ending
    $ insert_characters_alternate(mc=True,ayame=True,timeline=7)
    if persistent.did_christmas_event:
        $ cl_name = "Nick"
    "I can't believe its almost been a whole year since Ayame joined the club."
    "So much has happened since then."
    "Members have joined the club."
    "Members have left the club."
    "It's been a wild rollercoaster of emotions over the last year."
    "The club got really popular after our play last year but since then it's only been downhill."
    "We've been slowly losing members ever since then for one reason or another."
    "In fact, someone left just last week."
    "It wasn't because of any hard feelings, I think he just couldn't handle it."
    "But despite all of that, we're all still here."
    "The six of us have kept the Literature Club alive through thick and thin."
    "It feels like only yesterday that I was out at the mall buying presents for everyone."
    "But so much time has passed since then."
    show sayori 1a zorder 2 at t11
    s "Daydreaming again, [player]?"
    mc "What do you mean {i}again{/i}?"
    s "You've been doing that a lot lately, you know."
    s "Are you okay?"
    mc "I'm fine. Don't worry about me."
    s "Ehehe, that's my line~"
    show monika 1a zorder 3 at f31
    m "What's going on here?"
    m "We've got a meeting to get on with and not much time to do it in."
    m "So it would certainly help if the two of you weren't just standing around."
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s "We were just talking, that's all."
    s "Besides, [player] is the one you should be blaming."
    s "[cPlayer_personal] was daydreaming and I was trying to snap [player_reflexive] out of it."
    show sayori zorder 2 at t32
    mc "I wasn't daydreaming."
    mc "I was just...reflecting on things."
    show sayori zorder 3 at f32
    s "What's the difference?"
    show monika zorder 3 at f31
    show sayori zorder 2 at t32
    m "Well, whatever it is...can it wait?"
    m "The others are waiting for the two of you."
    show monika zorder 2 at t31
    mc "Right, sorry. We're coming."
    "We walk over to the others, where they are sitting around a crudely table formed by several desks."
    "This was Sayori's idea, back when we had more members."
    "Ever since then, we just haven't changed back."
    "I take a seat around the table and Sayori takes the spot next to me."
    show monika zorder 3 at f31
    m "Now that we're all here..."
    m "Well, most of us anyway...she'll be here shortly."
    m "It's time to discuss what exactly we're gonna be doing for the Christmas festival on Monday."
    show monika zorder 2 at t31
    show natsuki zorder 3 at f33
    n "You know, it might have been a good idea to do this earlier this week."
    n "Instead of, you know, the Friday before the event."
    show monika zorder 3 at f31
    show natsuki zorder 2 at t33
    m "You have a good point, Natsuki."
    m "But you know we can't discuss things like this without everyone present."
    m "And since a certain someone is busy most days..."
    show monika zorder 2 at t41
    show sayori zorder 2 at t42
    show natsuki zorder 2 at t43
    show yuri zorder 3 at f44
    y "This feels all too familiar."
    y "I feel as if we've been in a similar situation before."
    y "Getting ready to prepare for something, with little time to actually do it."
    show monika zorder 3 at f41
    show yuri zorder 2 at t44
    m "W-Well, you know how it is."
    m "People like us, we work best under pressure!"
    "Monika gives an unconvincing smile."
    "I guess she's still beat up about losing that member last week."
    "He just wasn't used to the way Monika ran things in the club."
    "She expects us to get things done, and fast."
    "It's a miracle he managed to stay as long as he did."
    "Though as I look around the room, I can't help but feel there was probably an ulterior reason to him staying."
    m "Let's just do our best. Okay, everyone?"
    show monika zorder 2 at t41
    show natsuki zorder 3 at f43
    n "You don't need to tell us that."
    show sayori zorder 3 at f42
    show natsuki zorder 2 at t43
    s "Whatever you say, Monika!"
    show sayori zorder 2 at t42
    show yuri zorder 3 at f44
    y "I doubt anyone would do otherwise."
    show yuri zorder 2 at t44
    "Everyone turns towards me in anticipation."
    "Are they expecting an answer from me?"
    "It's silent for a few moments before Natsuki decides to speak up."
    show natsuki zorder 3 at f43
    n "Well? Come on, [player]. Say something!"
    show natsuki zorder 2 at t43
    mc "W-What? I didn't know I was supposed to say anything."
    mc "Unless you wanted me to say 'I'll do my best' or something."
    mc "But I mean, you guys already said you would so I feel like I didn't need to."
    show sayori zorder 3 at f42
    s "Oh come on, just say something."
    show sayori zorder 2 at t42
    mc "What? Fine."
    mc "Uh...I'll try my best...!"
    show monika zorder 2 at t51
    show sayori zorder 2 at t52
    show natsuki zorder 2 at t53
    show yuri zorder 2 at t54
    show ayame 1a zorder 3 at f55
    ay "Wow, that was the least convincing thing I've ever heard you say."
    "Ayame walks in the room and takes the other seat next to me."
    "She sees excited for some reason."
    ay "Sorry, I'm running late. Had to discuss somethings with the principal and such."
    show monika zorder 3 at f51
    show ayame zorder 2 at t55
    m "About the funding being given to clubs and events?"
    show monika zorder 2 at t51
    show ayame zorder 3 at f55
    ay "Aha, something like that."
    ay "I definitely do not miss doing these sort of things."
    ay "'School leader' was a title I'm more than willing to give up."
    show sayori zorder 3 at f52
    show ayame zorder 2 at t55
    s "Well, it would have been nice to say we had a school leader in our club!"
    show monika zorder 3 at f51
    show sayori zorder 2 at t52
    m "I think that novelty wore off sometime after the first exodus of members we had, Sayori."
    m "Besides, I don't think Ayame appreciates being used as a form of leverage like that."
    show monika zorder 2 at t51
    show ayame zorder 3 at f55
    ay "I know Sayori doesn't mean it, so it's fine."
    ay "I really shouldn't have made so many commitments to other clubs."
    ay "It keeps clashing with the things I want to be doing."
    ay "And that's being with you guys."
    show yuri zorder 3 at f54
    show ayame zorder 2 at t55
    y "When you're as popular as you are, it's no wonder."
    y "What matters is that you're here now."
    show yuri zorder 2 at t54
    show ayame zorder 3 at f55
    ay "Anyway, enough about me. The six of us are here now."
    ay "I heard you were talking about the Christmas festival."
    show monika zorder 3 at f51
    show ayame zorder 2 at t55
    m "Exactly, we were about to start assigning tasks."
    m "I want to cover all bases, to make sure its the best possible thing we could do for it."
    show monika zorder 2 at t51
    show ayame zorder 3 at f55
    ay "Well, that sounds simple enough."
    ay "What would you like me to do?"
    show monika zorder 3 at f51
    show ayame zorder 2 at t55
    m "Ahaha, I don't know. You seem to be good at everything."
    "Monika thinks for a moment then she points her finger up as if she has an idea."
    m "How about this..."
    m "We'll let the others decide first and you can do what hasn't been taken already."
    show monika zorder 2 at t51
    "The Literature Club sure has participated in lots of events."
    "Ever since Ayame joined, we've had a much easier time organizing things."
    "She seems to be able to do anything and everything."
    "We put her on food duty once and she brought back some delicious pies."
    "We made her responsible for the atmosphere and we got a lot of attention for that festival."
    "It seems like she's capable of everything."
    "The same can't be said for everyone else..."
    "When I was put in charge of food, the interest in it was high."
    "But no one actually ate anything."
    "Granted, it was glowing green but it was thematic to that festival."
    "And when Sayori got assigned the role for atmosphere, she forgot to bring her banner in for the day."
    "Let's just say, those times may have been the cause of losing some of our members."
    show ayame zorder 3 at f55
    ay "That's a great idea. What's everyone going to be doing then?"
    ay "I can help or do whatever you all need me to do."
    show yuri zorder 3 at f54
    show ayame zorder 2 at t55
    y "I think it would be best if we all did what we are best at."
    y "In which case, I would prefer to work on creating a festive atmosphere for the day."
    show monika zorder 3 at f51
    show yuri zorder 2 at t54
    m "Sounds good! I know you'll create a fantastic atmosphere, Yuri."
    m "I can't wait to see it."
    show monika zorder 2 at t51
    show natsuki zorder 3 at f53
    n "In that case, I'll bring some desserts for the day."
    n "I could also try bringing in some sushi or something..."
    n "I promise I've improved since last time!"
    show monika zorder 3 at f51
    show natsuki zorder 2 at t53
    m "P-Perhaps it's better if you stick to what you know you're good at, Natsuki."
    m "I mean it's good that you're expanding the list of things you can make..."
    m "But sushi isn't exactly very Christmassy, is it?"
    m "There's only so much you can do with sushi that you could do with cupcakes and such."
    show monika zorder 2 at t51
    show natsuki zorder 3 at f53
    n "I guess you have a point..."
    show natsuki zorder 2 at t53
    "I know Monika is just trying to save us all."
    "Last time that Natsuki brought sushi in, Sayori ate some..."
    "...and threw up on my shirt."
    "Let's just say that wasn't exactly the best day we've had as the Literature Club."
    "Though I'm sure Natsuki's sushi isn't as deadly as it is now."
    "But as president, Monika probably wants to play it safe."
    show monika zorder 3 at f51
    m "Great, so that's the snacks and atmosphere taken care of!"
    m "What about you, Sayori? And you, [player]?"
    m "Any ideas as to what you would like to do?"
    show monika zorder 2 at t51
    show sayori zorder 3 at f52
    return
