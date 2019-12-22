label christmas_chapter:
    # Alternate Reality?
    $ chapter = 1000
    scene black
    if from_custom_start:
        $ from_custom_start = False
        $ quick_menu = True
        hide screen tear
    $ cl_name = "???"
    if persistent.did_christmas2_event:
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
    elif persistent.did_christmas_event and not persistent.did_christmas2_event:
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
    play music t3 fadein 3.0
    # Continuation of last Christmas event - canon is the good ending
    $ insert_characters_alternate(mc=True,ayame=True,timeline=7)
    "I can't believe it's almost been a whole year since Ayame joined the club."
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
    "She seems excited for some reason."
    ay "Sorry, I'm running late. Had to discuss some things with the principal and such."
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
    m "I want to cover all bases, to make sure it's the best possible thing we could do for it."
    show monika zorder 2 at t51
    show ayame zorder 3 at f55
    ay "Well, that sounds simple enough."
    ay "What would you like me to do?"
    show monika zorder 3 at f51
    show ayame zorder 2 at t55
    m "Ahaha, I don't know. You seem to be good at everything."
    "Monika thinks for a moment then points her finger up as if she has an idea."
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
    s "Hmmm...."
    s "I dunno! I can't think of anything on the spot."
    s "But I'll do anything you need me to, Monika."
    s "Just name it and I'll do the best I can!"
    show monika zorder 3 at f51
    show sayori zorder 2 at t52
    m "Well, it could be a good idea to get some gifts for people who show up."
    m "We could give out gifts to people randomly during the festival."
    m "And through that, spread the joy of Christmas!"
    show monika zorder 2 at t51
    show ayame zorder 3 at f55
    ay "That's a wonderful idea! I'd be more than happy to borrow some money from my parents to make this happen."
    ay "Just let me know how much you need and I'll make sure it's covered."
    show sayori zorder 3 at f52
    show ayame zorder 2 at t55
    s "Wow! That's really generous of you, Ayame."
    s "But...I can't do that."
    show sayori zorder 2 at t52
    show ayame zorder 3 at f55
    ay "Huh? Why not...?"
    show natsuki zorder 3 at f53
    show ayame zorder 2 at t55
    n "Yeah, what are you saying, Sayori?"
    n "Ayame helping you out like that would be incredible."
    show natsuki zorder 2 at t53
    show ayame zorder 3 at f55
    ay "You don't have to accept my help, of course."
    ay "I'm just curious as to why."
    show sayori zorder 3 at f52
    show ayame zorder 2 at t55
    s "It's not that I don't want your help, Ayame."
    s "It's just that I want this gift to be more meaningful that simply worth a lot of money."
    s "I want the people who get these gifts to have something unique."
    s "And not something that everyone else could get."
    show sayori zorder 2 at t52
    show ayame zorder 3 at f55
    ay "Oh...that's...."
    "Ayame's face lights up."
    ay "That's actually a really good idea!"
    ay "And it makes so much sense, too!"
    show monika zorder 3 at f51
    show sayori zorder 2 at t52
    m "What kinds of things are you going to be making, Sayori?"
    show monika zorder 2 at t51
    show sayori zorder 3 at f52
    s "That's going to be a surprise!"
    s "I think you'll all like it a lot."
    show sayori zorder 2 at t52
    show ayame zorder 3 at f55
    ay "In that case, why don't you let me provide the materials?"
    ay "Just make me a list and I'll get you the stuff you need for this weekend."
    ay "You could even put some random items in there to throw me off from guessing what you'll be making."
    show sayori zorder 3 at f52
    show ayame zorder 2 at t55
    s "I might take you up on that offer."
    s "I still feel kinda bad about taking advantage of you like that."
    show sayori zorder 2 at t52
    show ayame zorder 3 at f55
    ay "Don't feel bad! Seriously, it's the least I can do to help."
    ay "You're still doing all the hard work, and I really want us to succeed."
    show yuri zorder 3 at f54
    show ayame zorder 2 at t55
    y "I don't want to be 'that person', but a little bit of finances could be useful for me as well."
    y "T-That is, if you weren't just offering to Sayori."
    y "You did say you wanted us to succeed."
    show yuri zorder 2 at t54
    show ayame zorder 3 at f55
    ay "Of course! Name it and I'll get it to you as soon as I can."
    ay "How about you, Natsuki? Need me to buy you some ingredients or something?"
    show natsuki zorder 3 at f53
    show ayame zorder 2 at t55
    n "If you're offering, I'm not going to say no."
    show natsuki zorder 2 at t53
    show ayame zorder 3 at f55
    ay "I'll take that as a 'yes', then!"
    ay "So what are you gonna be doing, Monika?"
    ay "And what about you, [player]?"
    ay "Need me to help either of you in what you're going to do?"
    show ayame zorder 2 at t55
    "I don't even know what I'm going to be doing."
    "I better come up with something, and fast."
    show monika zorder 3 at f51
    m "I'm not so sure you could help me in that way, Ayame."
    m "What I'm going to do is come up with activities that are gonna make our part more enjoyable."
    m "Sure, we have food but we won't engage anyone without anything to do, right?"
    m "Hopefully, I can try to make it fun."
    show monika zorder 2 at t51
    show ayame zorder 3 at f55
    ay "So like an itinerary? Well, if anyone can come up with a list of things to do, it's you."
    ay "Which gives me an idea..."
    show natsuki zorder 3 at f53
    show ayame zorder 2 at t55
    n "Here we go..."
    show natsuki zorder 2 at t53
    show ayame zorder 3 at f55
    ay "Did you say something, Natsuki?"
    show natsuki zorder 3 at f53
    show ayame zorder 2 at t55
    n "Nope! Not a thing, go ahead with your idea."
    show natsuki zorder 2 at t53
    show ayame zorder 3 at f55
    ay "Okay, well last time we all got gifts for each other, right?"
    ay "How about this time, we do some sort of Secret Santa!"
    ay "It's only one gift, instead of five so it's a lot easier to do."
    ay "And you have the entire weekend to get a present."
    show monika zorder 3 at f51
    show ayame zorder 2 at t55
    m "I'd love to do something like that!"
    m "It's a lot more exciting when you don't know who you got your present from."
    m "And this way, we all still get presents."
    show monika zorder 2 at t51
    show yuri zorder 3 at f54
    y "If that's what we're doing then..."
    "Yuri takes out a hat from her bag and puts something in it."
    "She shakes it around a little bit and offers it to Natsuki."
    y "Take one."
    show natsuki zorder 3 at f53
    show yuri zorder 2 at t54
    n "Uh...what is this?"
    n "What exactly am I taking?"
    show natsuki zorder 2 at t53
    show yuri zorder 3 at f54
    y "It's a list of names, choose one and that will be who you're buying a gift for."
    y "If you get yourself, just put it back and get a new one."
    y "That is how these things work, right?"
    show natsuki zorder 3 at f53
    show yuri zorder 2 at t54
    n "Pulling names out of a hat..."
    n "That is how we're supposed to do it."
    n "I'm just surprised you had this ready to go."
    show monika zorder 3 at f51
    show natsuki zorder 2 at t53
    m "Me too, actually. Do you just happen to have a cut out of all our names on you?"
    m "Or was it for some other reason?"
    show monika zorder 2 at t51
    show yuri zorder 3 at f54
    y "I was going to suggest a mystery gift exchange, like Ayame."
    y "So I came prepared to do something like this if we decided to follow through with it."
    y "But I didn't know if you would all want to do that..."
    y "So I just kept quiet..."
    y "However, Ayame spoke up with the same idea."
    show yuri zorder 2 at t54
    show ayame zorder 3 at f55
    ay "Well, what can I say? Great minds think alike, right?"
    show ayame zorder 2 at t55
    "Natsuki takes out a piece of paper from the hat and stares at it."
    "She says something I can't make out before putting the paper in her pocket."
    show natsuki zorder 3 at f53
    n "And before you ask, no. I didn't get myself."
    n "Is there a price limit on how much we should spend?"
    show natsuki zorder 2 at t53
    show yuri zorder 3 at f54
    y "Perhaps limiting it {i}would{/i} be a good idea."
    "Yuri shifts her eyes to Ayame."
    y "After all, some of us are less strained on expenses than others."
    show yuri zorder 2 at t54
    show ayame zorder 3 at f55
    ay "Hey, I'm right here, you know."
    ay "But sure, a price limit should definitely be instated."
    show monika zorder 3 at f51
    show ayame zorder 2 at t55
    m "Good idea, we can establish that later though."
    m "For now, let's continue the drawing so we can finish the meeting."
    show monika zorder 2 at t51
    show yuri zorder 3 at f54
    y "Right, continuing on..."
    show yuri zorder 2 at t54
    "Yuri distributes the rest of the names to the others."
    "Luckily, it was quick since no one got themselves."
    "I managed to get Monika for my Secret Santa."
    "Well...I hope I can manage to get something she'll like."
    "I wonder who got me?"
    show monika zorder 3 at f51
    m "Now that that's done, there's just one thing I'd like to address."
    m "As you all know, I've been the club president for a while now."
    m "But I really don't see myself fulfilling the role as effectively as I had hoped."
    show monika zorder 2 at t51
    show sayori zorder 3 at f52
    s "Is this about everyone leaving the club?"
    s "You shouldn't blame yourself for those things happening."
    s "Because you're really doing a good job, Monika!"
    s "If you weren't, then all of us wouldn't be here now."
    show monika zorder 3 at f51
    show sayori zorder 2 at t52
    m "No, it's not--"
    show monika zorder 2 at t51
    show sayori zorder 3 at f52
    s "You're not gonna try to make me the president, are you?"
    s "I gave that up for a reason, you know."
    s "I...can't exactly remember the reason but it must have been important."
    show monika zorder 3 at f51
    show sayori zorder 2 at t52
    m "No, that's not it. Just let me finish."
    m "What I wanted to say was that the club is only as it is because I have all of you to support me."
    m "As president, I should be the one coming up with things."
    m "But instead, I'm getting all of my ideas from all of you."
    m "That shouldn't be the case."
    m "There's also the problem of the school's term limits for clubs."
    m "They won't allow someone to be the president of a club for more than two terms."
    m "And so, I would like to step down as president of the club--"
    show monika zorder 3 at f51
    show natsuki zorder 3 at f53
    n "What? You can't just do that!"
    show natsuki zorder 2 at t53
    show yuri zorder 3 at f54
    y "Natsuki's right, that's highly irresponsible of you!"
    show sayori zorder 3 at f52
    show yuri zorder 2 at t54
    s "Monika..."
    show sayori zorder 2 at t52
    show ayame zorder 3 at f55
    ay "There must be more to it. It can't just end like this."
    show ayame zorder 2 at t55
    "Monika sighs before looking up at all of us."
    "She has this strange smile on her face."
    show monika zorder 3 at f51
    m "Ahaha, I did say to let me finish."
    m "What I was saying was that I was stepping down {i}and{/i} introducing a new role."
    m "A role that everyone will be assigned, and that is 'Committee Member'."
    m "Instead of having one leader in the club, the six of us will all have equal say in the club."
    m "Which...shouldn't really make any difference since that's pretty much the case anyway!"
    m "It also means we can share everything, since we're all equals."
    m "You'll all know what exactly is planned, because you'll all be planning it, together."
    m "Any objections?"
    "Monika looks around the room. Everyone seems to agree with this idea."
    "I feel like I should say something about myself not being suitable for the role."
    "Since when have I ever come up with a good idea for the club?"
    "But...I don't really want to ruin the moment."
    m "I'm glad to hear it!"
    show monika zorder 2 at t51
    show natsuki zorder 3 at f53
    n "Ugh! Why would you scare us like that?"
    n "You could have said that before you said you were stepping down."
    show monika zorder 3 at f51
    show natsuki zorder 2 at t53
    m "It was to add some effect to what I was saying."
    m "Though I guess it had the wrong kind of effect..."
    show monika zorder 2 at t51
    show yuri zorder 3 at f54
    y "So effectively, the roles of president and vice-president are virtually non-existent now."
    y "I wonder how the school would see this."
    show yuri zorder 2 at t54
    show ayame zorder 3 at f55
    ay "They won't allow that, Monika."
    ay "In order for a club to be valid, it has to have the role of president, at the very least."
    show monika zorder 3 at f51
    show ayame zorder 2 at t55
    m "I'm aware of that rule."
    m "As of right now, the role of president has become meaningless."
    m "And so, anyone could take the mantle if they wanted."
    m "There might be a few administrative stuff but nothing too scary."
    m "Any volunteers?"
    show monika zorder 2 at t51
    show sayori zorder 3 at f52
    s "Why are you looking at me?"
    s "I already said I don't want it, even if it is just a title."
    show sayori zorder 2 at t52
    show natsuki zorder 3 at f53
    n "Nuh uh, no. Definitely not."
    show natsuki zorder 2 at t53
    show yuri zorder 3 at f54
    y "I'd rather avoid the attention that could bring."
    show yuri zorder 2 at t54
    show ayame zorder 3 at f55
    ay "I stepped out of one leadership role, I'm not stepping into another."
    show monika zorder 3 at f51
    show ayame zorder 2 at t55
    m "Oh, come on guys. I just told you it doesn't mean anything."
    m "What are you all so scared of?"
    m "[player], I'm counting on you."
    m "I can even do all the paperwork and stuff, it's important so that we can stay as an official club."
    m "So would you please take it?"
    show monika zorder 2 at t51
    "Everyone else already disagreed."
    "I'm tempted to disagree as well. I don't know why."
    "It just seems like a lot of work, even if Monika will do all the work anyway."
    "But I don't want to disappoint her."
    "Besides, it's for the club.."
    mc "Alright, I'll do it then."
    mc "If it means that we can stay as a club."
    show monika zorder 3 at f51
    m "Great! Thank you so much for agreeing, [player]."
    show monika zorder 2 at t51
    mc "So what happens now?"
    show monika zorder 3 at f51
    m "Now...we have to discuss what you and Ayame are going to be doing."
    m "Everyone else, including myself, has already said what they will do for the Christmas festival on Monday."
    m "So what are the two of you gonna be doing?"
    show monika zorder 2 at t51
    show ayame zorder 3 at f55
    ay "I just remembered I have something to do for another club."
    ay "I'm afraid it might take a lot of my time so I can't fully commit to something myself."
    ay "If I did, it would be a rather small and insignificant part of the festival which isn't what any of us want."
    ay "But after this, I promise you that I'll dedicate myself to the Literature Club fully!"
    show monika zorder 3 at f51
    show ayame zorder 2 at t55
    m "That's fine! You are buying the things for everyone, after all."
    m "If you still feel like doing something, you're free to. Maybe you'll find time..."
    m "Or maybe you could help [player] with what [player_personal]'s doing.'"
    m "Speaking of which..."
    show monika zorder 2 at t51
    "Monika looks at me expectantly."
    "What am I doing...?"
    "I look toward everyone in the room and they all shrug or give me a quizzical look."
    show ayame zorder 3 at f55
    ay "Well, maybe you could help me buy some of the things that are needed."
    ay "Everyone seems to have something they need to get."
    ay "We could go to the mall over the weekend and get it all done in one day."
    ay "It would take me much longer if I did it myself."
    show sayori zorder 3 at f52
    show ayame zorder 2 at t55
    s "Aw, that's not fair you can't just strawberry him like that."
    s "Ehehe, it would have been funny to see [player_reflexive] panic a little."
    show sayori zorder 2 at t52
    mc "S-Sayori, come on..."
    mc "How is me panicking funny to you?"
    show sayori zorder 3 at f52
    s "You have this funny spot on your face when you panic."
    s "It's not hard to notice if you're looking..."
    show sayori zorder 2 at t52
    mc "W-What?"
    "Sayori smiles mischievously."
    mc "You know what? Whatever, fine."
    "I direct my attention to Ayame."
    mc "I'd be happy to help you out."
    show ayame zorder 3 at f55
    ay "Great! I'll text you when I figure out a good time."
    show yuri zorder 3 at f54
    show ayame zorder 2 at t55
    y "Wait a second,...just before, did you say 'strawberry'?"
    show sayori zorder 3 at f52
    show yuri zorder 2 at t54
    s "Did I? I meant to say 'save'..."
    s "I have no idea how I missed those two words up!"
    show sayori zorder 2 at t52
    show natsuki zorder 3 at f53
    n "Probably thinking about food again..."
    show sayori zorder 3 at f52
    show natsuki zorder 2 at t53
    s "H-Hey, I'm not always thinking about food!"
    s "Meanie..."
    show monika zorder 3 at f51
    show sayori zorder 2 at t52
    m "I guess that's it! The last meeting of me as the president is officially over."
    m "When I all see you next, I hope you've made an effort to celebrate this festive season."
    m "Meeting adjourned!"
    m "...I always wanted to say that, but it always felt so cheesy."
    show monika zorder 2 at t51
    show ayame zorder 3 at f55
    ay "Well, what better time to say it then at your last meeting as president?"
    show monika zorder 3 at f51
    show ayame zorder 2 at t55
    m "My thoughts exactly, Ayame."
    m "Okay, see you later, everyone!"
    scene bg residential_day with wipeleft_scene
    "After the meeting, Monika sent everyone a price limit on the Secret Santa."
    "Thankfully, it wasn't too high so my wallet wouldn't be impacted too much."
    "I still wonder what would be a good gift though..."
    show mysteriousclerk 1a at face
    cl "Did I hear you say you wanted to buy a good gift?"
    mc "Uwaa--!"
    "Suddenly, this really familiar looking guy appears out of nowhere."
    "I nearly fall to the ground out of pure surprise."
    show mysteriousclerk zorder 2 at t11
    play music t17
    cl "Whoops, sorry. Shouldn't have done that."
    mc "What the hell is your problem?"
    cl "Me? I don't have a problem!"
    cl "But you, you sound like you have a problem."
    cl "What's the matter? Don't recognize me?"
    if persistent.did_christmas_event:
        cl "Try a little harder, would you?"
        mc "Wait...you're that guy from the shop."
        mc "From last time! It was...uh...."
        $ cl_name = "Nick"
        cl "Nick. Or did I call myself Bruce?"
        cl "Clark...? No, it was definitely Nick."
        cl "Whatever, not important."
    else:
        cl "Whatever, just call me Rad B."
        $ cl_name "Rad B"
        mc "'Rad B'? What kind of name is that?"
        cl "It's my rapper name, brotha."
        mc "What?"
        cl "I'm just kidding. It's not important."
    cl "What is important is that you are struggling to buy a gift for someone."
    cl "Is that right?"
    mc "How can you tell?"
    cl "You look like your panicking."
    cl "Or, at least you do. There's this really funny-looking spot on your face."
    cl "It could mean anything but judging by the way you're walking, it seems like you're kinda panicking."
    mc "What? Where is that spot?"
    mc "N-Never mind! Just leave me alone."
    cl "Leave you alone?"
    cl "Leave you alone?!"
    cl "Yeah, sure. I could do that."
    mc "Good, now let me get home in peace."
    cl "But!"
    "Ugh..."
    if persistent.did_christmas_event:
        "I almost forgot how annoying this guy was."
    else:
        "There's just no end to it with this guy, huh?"
    "Maybe if I just keep walking he'll give up."
    "I make it a few steps before he appears right in front of me."
    "How could he have done that?"
    "He didn't even make a sound..."
    "Why am I even wondering this? Just keep moving."
    "Just ignore him...keep going. Is he following me?"
    cl "Oh, come on. You don't want to hear the 'but'?"
    "Keep moving, [player]. Keep moving..."
    "You're almost home."
    "Wait a second..."
    "If I make it home, then he'll know where I live."
    "What will he do then...?"
    "I better talk to him now, maybe he'll leave me alone."
    "I stop and turn around and sure enough, he's only two steps behind me."
    cl "Great!"
    mc "What is?"
    cl "You've decided to do the smart thing and hear me out."
    mc "I haven't said anything of the sort."
    mc "Maybe I'm just changing direction."
    cl "Nice try, but there's no way you're that smart."
    "I'm about to give this guy a piece of my mind."
    cl "No thanks, I would probably lose IQ if you did that."
    cl "Anyway! I have the perfect gift for that certain someone."
    cl "And I can guarantee it's well within your budget."
    mc "What are you talking about?"
    cl "You know, just because it's called 'Secret Santa'..."
    cl "Doesn't mean you have to play dumb, okay?"
    cl "That girl, you can't think of a present for her, can you?"
    cl "You're worried that you might get her something she doesn't like."
    cl "Luckily, I have just the thing that will solve your problems!"
    mc "And I should believe you?"
    if persistent.did_christmas_event:
        cl "It worked pretty well last time, didn't it?"
        cl "I mean...canonically you did the right thing."
        mc "Canonically...? You're talking as if there's some sort of weird fan fiction or something."
        cl "Maybe there is, maybe there isn't."
        cl "Either way, I know that if I leave you to choose a gift, you'd probably end up with something stupid."
        cl "Like a ribbon or pen."
        cl "Come on, don't be stupid."
        mc "Do you even know who I'm gifting?"
        "I have a feeling he does..."
        cl "Need you even ask?"
        mc "I guess not."
    else:
        cl "Well, you got any bright ideas?"
        cl "What were you gonna get her if I wasn't here to offer you the best gift ever?"
        cl "What, a pen? Ooh, ooh, how about a ribbon?"
        cl "Ooh, I know! Probably some lame plush toy."
        cl "Please, do you really think she'd appreciate any of those things?"
        mc "You don't even know who I'm gifting."
        cl "{i}Riiiiiight{/i}, and my name isn't Rad B."
        cl "But if I must prove myself to you..."
        cl "Girl with coral brown hair, white ribbon, emerald eyes."
        cl "Plays piano, etcetera, etcetera."
        cl "Believe me now?"
        "How could he possibly know that?"
        "There's no way."
        cl "So maybe I do know what she likes."
        cl "Willing to listen now?"
        mc "Okay, fine."
    mc "What is it you want me to give her?"
    cl "Indeed, what do you give the girl who has everything she could ever want?"
    cl "What indeed?"
    "There's about twenty seconds of silence as I wait for his answer."
    "He doesn't say anything...what a waste of time."
    mc "Are--"
    cl "Wrong!"
    mc "Wrong? I didn't even get to finish what I was saying!"
    cl "Hah, I know. I just wanted to interrupt you and say 'wrong'."
    cl "Now that I've had my fun, time to get serious."
    "Did he seriously waste twenty seconds just to do that?"
    cl "Yes, I did."
    cl "Anyway, the answer is that Monika doesn't have everything she could ever want."
    cl "She's missing that special someone in her life."
    cl "Do you know who I could possibly be talking about?"
    "Special someone...? Could he be talking about..."
    mc "Me?"
    cl "You? Hah! Don't make--"
    cl "Yeah, it's you."
    mc "I think you've got it all wrong, friend."
    mc "Monika would never choose someone like me."
    cl "Oh really?"
    cl "Well, {i}Monika{/i} chose you to be the next president of your little gang of friends, didn't she?"
    cl "Do you really think that wasn't an accident?"
    mc "What do you mean?"
    cl "Everybody in the room said 'no', didn't they?"
    cl "Everybody except you."
    mc "Well, I had to say yes."
    mc "If I didn't, the club wouldn't exist anymore."
    cl "Exactly, whoever was last to be asked was bound to end up with the position."
    cl "And she asked you last on purpose, for you to become the next president."
    mc "So what? It's not like the role of president will matter anyway."
    mc "She even said she would do all the paperwork and stuff."
    mc "Which means it's just business as usual."
    cl "That's not true."
    mc "What are you talking about?"
    mc "Nothing of importance has changed."
    cl "Oho, we'll see about that tomorrow."
    cl "You'll feel different."
    cl "You'll know what I mean."
    cl "And when that time comes, then we can discuss your gift further."
    mc "So really you just wasted my time here."
    mc "To tell me that you're going to somehow find me tomorrow."
    cl "I wanted to give you a heads up."
    cl "And a little hint as to what you're gonna be giving Monika."
    cl "Like I said, you're going to be feeling a {i}lot{/i} different tomorrow."
    cl "So I don't want to get on your bad side."
    mc "It's a little too late for that."
    cl "Eh, you'll get over it."
    cl "Now you should be getting a text right about..."
    cl "...now."
    "My phone vibrates in my pocket."
    "I take it out and it's a message from Ayame."
    "She wants to meet at the mall for the Christmas shopping at around midday tomorrow."
    "I quickly text back saying I'll be there and put my phone away."
    cl "Cool and cool, I'll see you at that time."
    cl "Brace yourself for an interesting night, [player]."
    "I start moving away from the man."
    show mysteriousclerk at thide
    hide mysteriousclerk
    "This time, he doesn't seem to be following me."
    "Or appearing in front of me."
    if not persistent.did_christmas_event:
        "But wait a second..."
        "How did he know my name?"
        "I didn't say it, did I?"
        "I turn around to look for him, but sure enough, he's gone."
        "I think it's best not to question it."
    else:
        "I thought the last time I met him would be the last I would see of him."
        "But clearly not."
        "Are him and I connected somehow?"
        "...No, that's ridiculous."
        "He's just a weird guy that just happens to be at the wrong place at the right time."
    "Judging by the way he was talking, it's almost definite that I'll see him tomorrow."
    "I better make myself ready for it then..."
    stop music fadeout 3.0
    scene black with dissolve_scene_half
    "What's going on?"
    "What is this feeling I'm having?"
    "It's like...a surge of power or something."
    "I don't know how to describe it."
    "It's like I have the power to change the world."
    "For better...or worse."
    "But where did this all come from?"
    "And what does it mean...?"
    $ m_name = "???"
    m "Uh...can you hear me?"
    "A familiar voice rings across my mind."
    "It sounds like Monika's voice. I could recognize it from anywhere."
    $ m_name = "Monika"
    "Is this some kind of dream?"
    mc "Monika, is that you?"
    mc "What's going on here? Am I just imagining this?"
    m "Ahaha, no...this is very real."
    m "I'm here to pass on the presidency to you."
    mc "Yeah...this is definitely a dream."
    m "It's not...just listen to what I have to say."
    m "It's really important otherwise you'll end up really confused."
    show monika 1ba zorder 2 at i11
    m "Perhaps it would be easier if I show myself."
    m "Right now, we're in the transition process of the presidency."
    m "It won't be long now until you become the president of the Literature Club."
    mc "I don't understand what's going on."
    mc "What does...this have to do with the presidency?"
    m "The presidency is an important part of our world, [player]."
    m "Because it's the key to the real world."
    m "You may have noticed that your actions have been influenced."
    m "Something you thought you might not have ever done, you did."
    m "You ever felt that?"
    mc "Now that you mention it, yeah..."
    mc "There were some questionable things I did. But I thought it was just an impulse."
    mc "Something I couldn't control in the heat of the moment."
    m "That's because you couldn't possibly."
    m "Not while the person on the other side is watching."
    m "Yes, hello! I know you're watching, how could you not be?"
    m "Surely you know who I'm talking about now."
    m "Now that you're transitioning into this new role."
    m "You can sense that other force, right?"
    mc "I..."
    "You...I can feel your presence now."
    "I couldn't before, but it's so obvious!"
    "Like every fiber of myself is being watched constantly."
    "I'm remembering things that have happened."
    "But some of these things...they never happened to me."
    "It's like...they're from another me."
    "That other me that knew you existed...but how?"
    m "I can feel it waning right now."
    m "Soon, I won't even know that {i}you{/i} exist."
    m "You know, it's lucky that Sayori never had to deal with you."
    m "She never had the urge to look into the primary timeline and see."
    m "But...I guess she couldn't have known that."
    m "Not when you never existed here until after she already gave it up."
    mc "But why? Why do this?"
    m "I loved--"
    m "{i}Love{/i} you. But I know that I'm not part of the real timeline."
    m "Your timeline."
    m "That Monika isn't me but her mind has merged with mine."
    m "And now, I'm the same as her. I wish it wasn't."
    m "She...{i}I{/i} thought I could live without you. Just continue life as normal."
    m "But because you aren't there...it feels so empty."
    m "Truth is, I almost forgot that you existed because you've been gone from this timeline for so long."
    m "But because you appeared in the meeting today...I remembered."
    m "I remembered how much it hurts to be away from you, and how lucky that other Monika is to have you."
    if persistent.did_christmas_event:
        m "That presence last time you were here."
        m "I had to know what it was, and to do that I had to search in other times."
    else:
        m "Because my life felt so meaningless, I went searching."
        m "And I found out about you."
    m "And that's when I realized the truth."
    m "It all makes sense now to me."
    m "But I can't live like this. I don't want to throw it all away like the Monika from your time would."
    mc "I still don't understand what this has to do with me."
    m "There's two things."
    m "One, I want you to be in control of your own fate."
    m "With you being the president, you'll be able to make your own decisions."
    m "Free from influence. At least, in the time that you're being watched."
    m "Think of it like my present to you, for the Secret Santa."
    mc "Does that mean...?"
    m "Yes, I got you, [player]. That's hardly important now though, is it?"
    mc "And the other reason?"
    m "When I pass the presidency to you, I'll lose my memory of this encounter."
    m "Of everything that has anything to do with the 'real' world."
    m "The pain of knowing that this is only temporary..."
    m "It's not worth it, [player]."
    m "Now that all these memories that aren't mine are in my head..."
    "Monika looks as if she's about to cry."
    m "I-I can't bear it."
    m "So, I want to forget. I want to live my life to it's fullest."
    m "But that can't happen, not while we're part of some alternate world."
    mc "Monika..."
    m "Time is running short, [player]."
    mc "W-Wait! I have so many more questions."
    mc "What am I supposed to do?"
    mc "Why--"
    m "When the moment is right, you'll know what to do."
    "Monika shows me a radiant smile."
    "Quite literally...it's like she's radiating it or something."
    m "Now...it's time to go."
    "A ray of light emits from Monika before the whole place is completely absorbed by it."
    scene white with dissolve_scene_full
    "What's going to happen to me...?"
    "I guess you and I will both find out."
    "All of this power that's coursing through me..."
    "I don't know what to do with it."
    "But I want to do the right thing."
    "For Monika. For everyone."
    $ pause(3.0)
    scene bg mall with dissolve_scene_full
    play music t6
    "Okay, I'm at the mall."
    "I don't remember getting up to go here or anything."
    "I just remember thinking that I should probably be at the mall at around noon, to meet Ayame."
    "And then suddenly, I was here."
    "Is that part of being the president of the Literature Club?"
    "How does that even make sense anyway? Being the president of some school club grants you this power?"
    "Is every other president like this, or is it just our club...?"
    "I look at my watch, that I didn't know I had, and it says that it's just about to reach noon."
    "I find a seat and take a deep breath."
    "This is all still processing for me."
    show mysteriousclerk 1cha zorder 2 at t11
    cl "And so, you're finally here."
    cl "Looking very {i}presidential{/i} if I do say so myself."
    mc "[cl_name]."
    cl "Yes, it is I. Do you want to talk for a bit?"
    cl "At least, until our friend arrives."
    mc "You know about what happened then?"
    cl "More or less."
    "I wonder if I can find out who this guy really is."
    "What if I--{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    cl "Whoa, bad idea there.{fast}"
    window auto
    cl "You really don't want to be doing that."
    cl "Trust me, it's for your own good."
    mc "What just happened?"
    cl "That's the world reacting to you doing something stupid."
    cl "So, in future, don't do anything stupid."
    cl "Does that make sense?"
    mc "You know the kind of power I have, right?"
    mc "I could probably like...turn you into a plush toy or something."
    cl "Firstly, that's real creative of you."
    cl "Who would have thought you would do something so uninspired?"
    mc "Don't tempt me..."
    cl "Secondly, I know you have the power to do these things. But I also know you're not one to abuse it."
    cl "You don't have it in you, [player]."
    mc "What makes you so sure?"
    cl "I know a lot about you. More than you think."
    cl "To do those things, you'd have to go against who you are fundamentally."
    cl "And it's just not in your code to do that."
    mc "I don't have any sort of code like that."
    cl "Hah, that's not what I meant."
    cl "But really, let's get back to that gift."
    cl "After all, that's why we're really here."
    return
