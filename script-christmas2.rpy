label christmas2_chapter:
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
    y "Wait a second...just before, did you say 'strawberry'?"
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
    cl "You look like you're panicking."
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
    play music m1
    "What's going on?"
    "What is this feeling I'm having?"
    "It's like...a surge of power or something."
    "I don't know how to describe it."
    show bg glitch:
        yoffset 480 ytile 2
        linear 0.25 yoffset 0
        repeat
    "It's like I have the power to change the world."
    "For better...or worse."
    "But where did this all come from?"
    "And what does it mean...?"
    scene black
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
    show bg glitch:
        yoffset 480 ytile 2
        linear 0.25 yoffset 0
        repeat
    m "It's not...just listen to what I have to say."
    m "It's really important otherwise you'll end up really confused."
    m "Perhaps it would be easier if I show myself.{nw}"
    $ _history_list.pop()
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    scene black
    show monika 1ba zorder 2 at i11
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    m "Perhaps it would be easier if I show myself.{fast}"
    window auto
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
    if persistent.did_christmas_event:
        mc "Like during Christmas last year...it was..."
        mc "It was like I couldn't make my own decisions."
    else:
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
    m "And now, I'm the same as her. I wish that wasn't the case."
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
    m "So, I want to forget. I want to live my life to its fullest."
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
    scene bg mall_interior with dissolve_scene_full
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
    "He's right though. I would never do such a thing."
    "I don't know if I'll ever become corrupt and abuse my power."
    "But the person standing in front of him right now..."
    "That person would never do such a thing."
    cl "But really, let's get back to that gift."
    cl "After all, that's why we're really here."
    mc "That gift you said I should give her."
    mc "You were implying me, weren't you?"
    cl "I was. But not in the way you would imagine."
    cl "As I, and now you, know she loved that person outside of our world."
    cl "The one that's probably watching the two of us have this conversation right now."
    cl "Probably through some fancy monitor or screen or something."
    cl "Hello! I see you. Not really."
    cl "You can pretty much ignore it, just let them watch the events unfold."
    cl "After all, you're the master of your own fate now."
    cl "Anyway, back to Monika."
    cl "The point is, she didn't know that. That is...until last Christmas when she finally learned of their existence."
    cl "Because of their interaction with this world."
    cl "Because of their interaction through you."
    mc "So the reason Monika is acting this way is because of this person...?"
    cl "Kind of. I wouldn't blame them. In fact, I'd say they actually saved Monika."
    cl "Because she wouldn't have been able to comprehend that feeling of emptiness."
    cl "So the gift you should give her...is peace of mind."
    mc "Peace of mind?"
    cl "Assure her that everything is going to be okay."
    cl "That you've both accepted your new positions in this world."
    cl "And that you'll do the right thing."
    cl "You could give her something materialistic, of course."
    cl "But just telling her that you'll do the right thing, even if she doesn't know what it means..."
    cl "It will be the best Christmas present she could ask for."
    mc "You're sure about this?"
    cl "I'm [cl_name], but I am feeling absolutely positive."
    cl "Without a doubt."
    mc "Okay...then I'll tell her. Something tells me you know what you're talking about."
    cl "Good instinct. And with that, I'll take my leave."
    mc "What, that's it?"
    cl "What else do you want me to say?"
    cl "Congratulations on your new position?"
    cl "Don't destroy the world?"
    cl "You don't need me to tell you that."
    cl "And...right on queue."
    show ayame 1ba zorder 3 at f33
    ay "[player]? And whos this?"
    "Ayame approaches me carrying some shopping bags."
    "She sees me look at them and laughs."
    ay "Oh, don't worry about these. These are for something else."
    ay "Our real shopping has yet to begin."
    "Ayame looks at [cl_name] and seems deep in thought."
    "It's like she knows him somehow."
    ay "Do I...know you?"
    show mysteriousclerk zorder 3 at f32
    show ayame zorder 2 at t33
    cl "Me? I don't believe we've had the pleasure of meeting."
    cl "But sadly, we'll have to get better acquainted at some other time."
    cl "As I am afraid I have run my course."
    cl "Fare the well, maiden."
    show mysteriousclerk at thide
    hide mysteriousclerk
    "[cl_name] quickly leaves the scene."
    "What was with the way he was talking?"
    show ayame zorder 2 at t11
    ay "He seems like a gentleman."
    mc "Really?"
    ay "Did you not hear the way he talked?"
    ay "All formal and such."
    ay "It's kind of attractive, actually."
    mc "He looks like he's at least ten years older than you."
    ay "Oh, I know! I'm just saying..."
    ay "A-Anyway, let's forget I said anything."
    mc "Did you know him?"
    ay "He seems familiar, but I can't say for sure."
    ay "What I can say for sure..."
    "Ayame takes something out of her pocket and hands it to me."
    "It's a piece of paper with lots of different items written on it."
    "The font size is kinda small, and it fills almost the entire page."
    ay "Is that this is half the list of things that everyone wanted."
    mc "This is...a lot of stuff."
    mc "Are you sure this is half of it and not {i}all{/i} of it?"
    ay "Do you not trust me?"
    mc "I do, it's just..."
    "Sigh, I'm gonna be here for a while, aren't I?"
    "At least I can buy that materialistic thing [cl_name] was talking about."
    "What could I get her?"
    "There's a lot of things she could want."
    "But what would she really want?"
    "[cl_name] said it himself. She's the girl who has everything she could want."
    "Maybe I need to be more creative."
    ay "Earth to [player], come in, [player]."
    mc "Huh? What?"
    ay "I don't know, you zoned out there or something."
    ay "Are you okay?"
    mc "Yeah, just fine. We should get going if we want to get this done."
    ay "True enough. I got some people to separate the list by stores."
    ay "So each section shows which items you get from there."
    mc "You had someone do that for you?"
    ay "Just some extra expanses, don't worry yourself."
    ay "It's also separated by which side of the mall the shops are in."
    ay "So I have the west side..."
    mc "And I have the east side."
    ay "Call or text me when you've finished."
    ay "I might have some 'personal' shopping to do."
    mc "Will do."
    show ayame at thide
    hide ayame
    "Since Ayame was already carrying some bags, it kinda makes me think that I'm doing more work than her."
    "Though knowing her, she's probably got some servant or something to take those bags from her."
    "Which means she probably has one to do her shopping too."
    "I can't complain. I couldn't come up with anything to do."
    mc "Let's see, the first item on the list is..."
    mc "Scented candles, lavender."
    "Must be something Yuri wanted."
    mc "I wonder if I could just..."
    "Out of thin air, a candle appears on my hands."
    "Still in the packaging, too."
    "While this is cool and all, I probably shouldn't do it again unless I have to."
    "Because there's two things that could be happening."
    "One, it's being taken from some place and placed on my hand."
    "Or two, it's being created out of seemingly nothing and I will crash the economy."
    "Either way, I don't want to cause any trouble, so I'll do the rest of my shopping manually."
    scene bg mall with wipeleft_scene
    "After what was apparently a long time, I'm finally outside with all of the stuff from that list."
    "I told Ayame and she replied she wouldn't be long."
    "Enjoying the show?"
    "I know I can't stop you from watching."
    "Well...not without hindering my self."
    "I figure there's no harm in letting you see what's going on."
    "After all, it is Christmas. It's the season of giving."
    "And so, I'm giving you this opportunity."
    "Giving you the chance to see the world as it should have been."
    "Without your interference."
    show ayame 1ba zorder 2 at t11
    ay "I'm all set, [player]."
    "Ayame comes out of the mall, but with no bags."
    ay "Sorry, it took a bit longer than expected."
    ay "My parents insisted that the servants take all the shopping home."
    mc "But you got everything?"
    ay "Everything...and more."
    ay "By that, I mean I got the gift I was buying for my secret Santa."
    "That's right! The secret Santa. I almost forgot about it."
    "I didn't get to buy Monika anything because I was so preoccupied."
    "Maybe I can just get something similar to what Ayame got."
    mc "I take it you're not going to tell me what you bought."
    ay "Doing that would ruin the surprise."
    mc "What now then? Are we going to deliver the materials to everyone?"
    ay "That won't be necessary. I've got it covered."
    ay "You just do whatever you need to do to make your transition to president smooth."
    ay "Meanwhile, {i}I{/i} have to do a couple of things for the other clubs."
    mc "You did get your task done, so I'd say you have the time."
    ay "We got our task done. It was a joint effort."
    "The sound of a violin emanates from Ayame's pocket."
    "She takes out her phone and answers it."
    "After a few minutes of back and forth, she puts it away and shrugs."
    ay "Well, that's me. I hope you have a ride home."
    mc "I have a way."
    ay "Great! Then I'll see you on Monday."
    ay "Take care, {i}president{/i}."
    show ayame at thide
    hide ayame
    "A fancy looking car arrives and Ayame jumps inside."
    "She gives me one final wave of goodbye before it drives off into the distance."
    "I should probably get home, and fast.{nw}"
    $ _history_list.pop()
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    scene bg bedroom
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    "I should probably get home, and fast.{fast}"
    window auto
    "And just like that, I'm there."
    "That's definitely a useful trick."
    "You could really mess people with that."
    "Like if you were talking to them and then they walk away..."
    "You could appear right in front of--"
    "Wait a second."
    "That man. That can't be right."
    "Does he have the power I have as well?"
    "Has he known this whole time?"
    "Is that how he can do all those weird things?"
    "Whatever the case, it's not important."
    "I can sense that he doesn't have bad intentions."
    "Clearly, he's doing his own thing in this world."
    "From what I can tell, he seems to be helping it."
    "Helping it in his own weird way."
    "He's probably went through his own struggle to get to how he is now."
    "Maybe...I'll end up like that someday."
    "Speaking of a struggle, I still don't know what to get Monika."
    "I want to make it something special."
    "Something truly unique."
    cl "I already told you."
    show mysteriousclerk 1cha zorder 2 at t11
    cl "She won't care what you get her."
    "[cl_name] bursts open the door to my bedroom."
    "I'd say I'm surprised but I'm more shocked at how he seems to appear at all the right moments."
    cl "Anything, [player]. Come up with anything."
    cl "Visualize it in your mind, and make it reality."
    cl "It doesn't have to be anything incredible."
    cl "She'll be happy, as long as it's from you."
    "I peer back into my past. And the past from another world."
    "The gift for the girl who has everything."
    "And then, it hit me. Literally. [cl_name] pat me on the shoulder and smiled."
    "I know I said I wouldn't just make things appear out of nowhere, but this is important."
    cl "Perfect. Now, this is probably the second to last time you'll see me."
    mc "Second to last?"
    cl "Soon, it won't be necessary."
    cl "But who cares about that? Go wrap your gift."
    cl "Enjoy your weekend. You got bigger things to worry about than some old man."
    cl "Take care..."
    show mysteriousclerk at thide
    hide mysteriousclerk
    "He steps out the bedroom and nods his head."
    "As soon as he disappears from sight, I can tell he's nowhere near."
    "He probably did the same thing I did."
    "Which makes me even more curious as to who he really is."
    "I guess that as long as he doesn't want me to know, I'll never figure it out."
    "But he's right. Christmas is coming and I have to be ready for it."
    scene black with dissolve_scene_full
    stop music fadeout 3.0
    scene bg residential_day with dissolve_scene_full
    play music t2
    "It's the day of the Christmas festival."
    "I made sure to contact everyone to see if their preparations were going okay."
    "I just felt like I had that responsibility as the president now."
    "I know Monika said I didn't have to do these kind of things, but I can't help it."
    $ s_name = "???"
    s "Heeeeeeeyyy!!"
    "I'd recognize that voice anywhere. Sayori must have decided to catch up to me today."
    "I turn around and notice she has two large bags with her. Those must be the gifts she made for today."
    "She puts the bags down and starts waving her arms around like she's oblivious to all the attention she might bring herself."
    "Luckily for her, there doesn't seem to be many people walking to school today."
    $ s_name = "Sayori"
    show sayori 4p zorder 2 at t11
    s "Haaahhh...haaahhh..."
    mc "I would have thought you'd be late today."
    mc "You've been getting into that habit again lately."
    s "N-Not today! This time, I caught you."
    "Sayori struggles to catch her breath."
    mc "Need a hand? You look like you're struggling."
    "I point to one of the bags she's carrying."
    s "I thought you'd never ask!"
    "Sayori offers me one of the bags."
    s "I'm only struggling because these things are so heavy."
    mc "Yeah, right."
    "I take the bag from her hand and surprisingly it is pretty heavy."
    "I'm surprised she managed to carry one, let alone two of these."
    "I peer inside and see a few wrapped gifts."
    mc "What the hell did you pack in here? Rocks?"
    s "Rocks? No, where would I even find that many rocks?"
    s "But if I did put rocks in there, it would be coal."
    s "Besides, why does it matter to you?"
    s "It's not like you're getting any of them anyway."
    mc "I guess not...it's just, a little heavy is all."
    mc "Don't worry, I'll manage."
    s "I'm sure you will! If I can do it, then you can as well."
    s "You know, I've always wanted to experience the snow."
    mc "Huh?"
    s "It doesn't really snow around here."
    s "Any you see all those films and shows that show a snowy Christmas."
    s "It would be kinda nice to have that, don't you think?"
    s "Buuut, I guess with where we live, that's not really possible."
    s "Ehehe, sorry...I guess I'm just fantasizing about things that can never happen."
    mc "Snow..."
    "Sayori wants to see the snow."
    s "That's right. I'm talking about the snow."
    hide bg residential_day
    show bg residential_transition_snow zorder 0
    s "Is there a..."
    "A drop of snow suddenly falls on Sayori's face."
    s "What the...?"
    "Snow suddenly comes slowly falling from the sky."
    "How did that happen?"
    "Did I do this?"
    s "[player], it's snowing!"
    mc "You're a master of observation, Sayori."
    s "How did this happen?"
    s "It's like some sort of Christmas miracle!"
    mc "Maybe someone out there is looking out for us."
    s "Well, tell that someone that they're the best person ever!"
    s "I can't believe it!"
    "Seeing Sayori so happy like this...it warms my heart."
    "Small things like this, maybe this is how I can bring good to the world."
    s "This is going to be the best Christmas ever, [player]."
    s "It's going to be twice as fun as last year! Merry, Merry Christmas!"
    mc "Double the 'Merrys', huh? Merry Christmas, Sayori."
    "Sayori beams."
    s "Now come on! Let's hurry to the school."
    s "I can't wait to see everyone's reaction!"
    "Sayori starts running ahead at full speed."
    "While I'm struggling to keep up with her enthusiasm."
    scene bg club_day with wipeleft_scene
    "After an otherwise average day of school, I arrive at the club. Everyone else is already here."
    "Yuri is putting up decorations but with how the room is already, I'm surprised she's not done."
    "There's Christmas decorations everywhere and a huge banner saying 'Merry Christmas' on the wall."
    "She really did an incredible job with the atmosphere."
    "There's also this divine smell coming from the closet."
    "I can only guess that must be Natsuki's baking."
    "Everything seems to be going according to plan."
    "Natsuki and Sayori are helping Yuri put the decorations up."
    "While Monika and Ayame are talking amongst themselves until they notice me."
    show ayame 1a zorder 2 at t21
    ay "Look who decided to show up!"
    ay "We were just talking about you."
    mc "Oh? What about exactly?"
    show ayame zorder 2 at t21
    ay "About how Monika gave you your gift early."
    ay "I wonder what's going on there, eh?"
    show monika 1a zorder 3 at f22
    m "T-There's nothing going on, Ayame!"
    m "I just felt like I needed to get it to [player_reflexive] as soon as possible."
    m "But...I don't even remember what I got [player_reflexive]."
    m "I just know that it happened."
    m "But I want to know...did you end up liking it, [player]?"
    show monika zorder 2 at t22
    mc "I did. It was a very thoughtful gift, Monika. Thank you."
    mc "You don't have to worry about it."
    show monika zorder 3 at f22
    m "That's a relief. I'm glad you liked the gift then."
    m "I wonder who got me...and what they got me."
    m "I guess I'll find out later today, huh?"
    m "We were meant to have a set time for the exchange but I guess because of me it's kinda ruined."
    show ayame zorder 3 at f21
    show monika zorder 2 at t22
    ay "Everyone understood, Monika. Besides, I doubt they could be angry at you for being in the spirit of Christmas."
    ay "But let's finish up here and help with the setting up."
    ay "We have quite a long day ahead of us."
    show ayame zorder 2 at t21
    show monika zorder 3 at f22
    m "True enough. What do you say, president [player]?"
    m "Shall we get to work?"
    show monika zorder 2 at t22
    mc "Let's do this."
    scene bg club_day with wipeleft
    "After putting up all of the decorations, the students arrived soon after."
    "I saw some familiar faces. People that were a part of the club before."
    "There weren't any bad blood or anything, it was just a lot of small talk."
    "I understood their reasons for leaving, now more than ever."
    "There's just so many things with the club that are incompatible with their personalities."
    "It made sense that they would leave before they started to resent us."
    show yuri 1a zorder 2 at t11
    y "Everything appears to be running smoothly."
    y "I'm so glad it turned out this way."
    mc "Yeah...I couldn't have asked for a better Christmas festival."
    mc "Thank you for creating this wonderful environment, Yuri."
    y "I-It's nothing."
    mc "No, really. You did an awesome job. Don't discredit yourself."
    mc "You even came prepared with that drawing names out of a hat thing."
    mc "Even if you didn't say it out loud, you had the idea in mind."
    mc "You deserve recognition for it."
    y "I appreciate you saying that, [player]."
    y "It's just a bad habit I need to get rid of."
    y "I put a lot of effort into the things I do."
    y "I suppose I just need to stop being so humble..."
    mc "Being humble isn't bad, but when you do something like this..."
    mc "You should feel proud of yourself."
    mc "Proud of all you've accomplished."
    y "Thank you. I'll take those words to heart."
    mc "I hope you do."
    "Yuri looks outside at the snow still slowly falling down."
    y "I never would have expected it to snow here."
    y "Let alone on a day like this."
    y "There truly are some extraordinary things in this world."
    y "Things that are better left unexplained, am I correct?"
    mc "Trying to explain it would ruin the magic."
    y "Precisely."
    "Yuri smiles bashfully."
    y "One last thing, [player]...Merry Christmas."
    show yuri at d11
    "Yuri approaches me and gives me a hug."
    "I happily return it and smile for her."
    mc "Merry Christmas, Yuri."
    y "N-Now, I think I left something over there."
    y "Y-Yeah, I'll go get that."
    mc "Do what you need to do."
    show yuri at thide
    hide yuri
    "Yuri walks over to one of the Christmas decorations and begins fiddling with it."
    "It's clear that she still has feelings for me."
    "And still gets really embarrassed when I give her compliments but I know she's improving."
    show natsuki a zorder 2 at t11
    n "What was that about?"
    "Natsuki points to where Yuri is."
    mc "Oh, nothing. She's just 'getting something'."
    mc "Did you need to speak to me about something, Natsuki?"
    n "Well...no. Not particularly."
    n "But I did want to greet you."
    mc "Greet me?"
    n "Greet you for Christmas, you idiot."
    n "So, you know...I hope you have a Merry Christmas and stuff."
    n "Just don't expect this to happen too often."
    mc "Are you okay, Natsuki? Did something hit you on the head or something?"
    n "No, but something is about to hit you in a second."
    mc "I-I'm only kidding. Thank you, Natsuki."
    mc "I hope you have a Merry Christmas with your parents too."
    n "I never thought I'd get to spend Christmas as a whole family again."
    n "I thought it would be a one time thing and that there would be more conflict."
    n "Somehow, the three of us managed to stick together."
    n "But then again, strange things happen all the time."
    n "Like right now with the snow..."
    mc "What do you think of it?"
    n "I know it should be impossible."
    n "It doesn't make any sense."
    n "But I don't care. Maybe it's a sign."
    "Natsuki looks over at the desserts she's prepared."
    "It looks like they're running low."
    n "I have to put more on the table."
    mc "Go ahead."
    show natsuki at thide
    hide natsuki
    "Natsuki goes to the closet for a minute and returns with a new tray full of cupcakes."
    "She also made some gingerbread men which tasted incredible."
    "I never knew she could make those, maybe she's had it under her sleeve for a while."
    "If so, today was the perfect occasion to bring them out for sure."
    "They were a huge success with all the students."
    "Some of the teachers even came in and complimented Natsuki's baking too."
    "Monika begins addressing the crowd of people again."
    "We had to move all the desks to the edge of the room to make space."
    "I don't think any of us were expecting this many people to go to our event."
    "Sayori even ran out of gifts just a couple of minutes ago."
    "Where did this surge of popularity come from anyway?"
    "We weren't this popular since Ayame joined..."
    "I find her in the room, talking to the presidents from one of the other clubs."
    "I don't know which one exactly but I do know it was a pretty big one."
    "He notices me and nods to Ayame before leaving the two of us."
    show ayame 1a zorder 2 at t11
    ay "[player], can I help you?"
    mc "Did you have something to do with this?"
    ay "I don't know what you could possibly be talking about."
    mc "About all these people here."
    mc "I don't think me and the others expected such a crowd."
    ay "Oh, that! Well, I might have called in a few favors."
    ay "Helping out the other clubs does come with some benefits, you know."
    mc "Really, you did that?"
    ay "Is...is that a problem?"
    mc "No, in fact it's the opposite."
    mc "Look at everyone! They're so happy."
    mc "They have all these people here with them enjoying our event."
    mc "It's like all their hard work and preparation paid off."
    ay "That was the intention I was going for."
    ay "I'm glad it didn't backfire or anything."
    mc "You sure are full of surprises, aren't you?"
    ay "I try to be. Just like today seems to be."
    ay "I mean...snow? Seriously?"
    ay "That's something I never would thought I'd see here."
    ay "I've been overseas and seen it, but to be home and witness it for myself..."
    ay "Let's just say it seems nothing short of a miracle."
    mc "It does seem something like that, doesn't it?"
    ay "Merry Christmas, to you and the Literature Club."
    mc "Merry Christmas, Ayame."
    ay "Now that that's done, I better go talk to the other presidents here."
    ay "I'll see you later, maybe."
    mc "Maybe."
    show ayame at thide
    hide ayame
    "We still have a long day ahead of us."
    "How long is this event meant to last for anyway?"
    "I guess I better participate too."
    "The teachers don't know that the president role is meaningless, so as the new president I should probably greet them."
    scene bg corridor
    with wipeleft_scene
    "People actually stayed up until the very end of the event."
    "Which meant that we had to pack up and didn't have time for the gift exchange."
    "Sayori figured that the best time to do it was now, before Christmas was over."
    "It turns out that everyone managed to get the same person who was gifting them."
    "Yuri got Natsuki, and Sayori got Ayame."
    "Which means Natsuki got Yuri, and Ayame got Sayori."
    "I guess that makes this whole process a lot easier."
    "Now, to give my gift to Monika."
    show monika 1a zorder 2 at t11
    m "Ah, [player]. I should have known you would have gotten me."
    m "Why would fate have it any other way?"
    mc "Fate can be kind."
    m "Fate can also be incredibly cruel."
    m "But today fate seems to be in our favor."
    m "Snow, a huge turnout and more importantly, time with each other."
    m "Who could ask for a better day?"
    mc "I couldn't have said it better myself."
    m "Just one thing left now, isn't there?"
    mc "Right..."
    "I search my bag for the gift that I created for Monika."
    "I wrapped it in a small box and attached a card to it."
    "She takes the card and begins reading it."
    m "Let's see here...'Everything will be okay. There's nothing for you to worry about anymore.''"
    m "'Happy holidays and best wishes, from [player].'"
    m "I..."
    "Tears begin to well up in Monika's eyes."
    m "I don't know why but I'm so happy to hear those words."
    m "It doesn't even make any sense. There's just no context."
    m "But somehow, those words just touch me deeply."
    m "Thank you."
    mc "Well, you haven't even opened the present yet."
    mc "I spent some time thinking about what you would want."
    m "Oh? Did you now?"
    "Monika begins unwrapping the present I made for her."
    "Slowly, the expression on her face changes to one of pure joy."
    m "H-How did you get this?"
    mc "Let's just say that fate had been kind over the weekend, and leave it at that."
    "She takes the little miniature I made of her and hugs it."
    m "It's so adorable. It's like a tiny version of me."
    m "I love it. Thank you so much."
    mc "There was two ways I thought that would go."
    mc "You would either love it or be really creeped out by it."
    mc "I'm so glad it wasn't the creeped out option."
    m "Don't worry, this is amazing. I'll cherish this gift forever."
    m "To be honest, anything from you would have done fine."
    m "I know you aren't exactly the richest person around."
    m "It must have cost you a fortune to get this custom-made."
    mc "I wouldn't think about it too much."
    m "Then I won't. Merry Christmas, [player]!"
    "Monika wraps her arms around me in a warm embrace."
    mc "Merry Christmas, Monika."
    show mysteriousclerk zorder 3 at f33
    cl "And so, this is how our story ends."
    "[cl_name] places an arm on my shoulder and stares out the window."
    cl "What a neat little story."
    show monika zorder 3 at f32
    show mysteriousclerk zorder 2 at t33
    m "What? Who are you?"
    "Monika releases her embrace and stares in bewilderment at [cl_name]."
    m "If you're here for the event, you're a bit late..."
    show monika zorder 2 at t32
    show mysteriousclerk zorder 3 at f33
    cl "But nothing can last forever, can it?"
    cl "Just like how this can't last forever."
    cl "Perhaps it's time to return to your own time."
    cl "And to stop dallying in this world that doesn't need you."
    show monika zorder 3 at f32
    show mysteriousclerk zorder 2 at t33
    m "[player], do you know who this is?"
    show monika zorder 2 at t32
    mc "Even if I did, I can't stop him."
    mc "Because he's right."
    "This is as far as you need to see."
    "This world doesn't need you anymore."
    "And I think we're better off without you."
    "But still, I hope you at least enjoyed this little event we did."
    "But my fate is my own now, and I intend to keep it that way."
    show mysteriousclerk zorder 3 at f33
    cl "And so it is with deep regret that I must transition us to black."
    cl "And end this fairy tale that will never come to pass."
    cl "That never should have come to pass."
    cl "Perhaps, with the right choices you can still achieve this path."
    cl "If you stick to the side of righteousness."
    cl "Stray away from the darkness and trust your friends."
    cl "Then maybe...your timeline can still be saved."
    cl "Farewell!"
    play sound "sfx/closet-open.ogg"
    scene black
    n "Hey, who turned out the lights?"
    y "Did the power go out?"
    s "What's going on?"
    ay "Does anyone have their phone on them?"
    cl "Goodnight."
    $ persistent.did_christmas2_event = True
    $ christmas2_chapter = False
    $ get_achievement("*Christmas Miracle*")
    $ pause(1.0)
    $ style.say_window = style.window
    $ quick_menu = True
    $ renpy.utter_restart()
    return
