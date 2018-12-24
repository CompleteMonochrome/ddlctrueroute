label christmas_chapter:
    $ monika_type = 1
    $ ch12_markov_agree = True
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
    s "Do events like this even exist in our world?"
    s "I'm not really sure myself."
    s "I've lived enough years to know whether it should or shouldn't exist."
    s "At least, to me I have."
    s "To you, I could just be completely new."
    s "But from my memories, I can't really give an answer."
    s "Ours is based off of yours but..."
    s "I shouldn't complain."
    s "This is good for us."
    s "It's nice to have a little rest, I guess."
    s "This is Christmas Eve..."
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
    s "{cps=5}I really hope you know what you're doing...{/cps}{nw}"
    stop music fadeout 1.5
    scene bg mall_day with Dissolve(1.5)
    play music t5christmas fadein 3.0
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
    "I know what Sayori would want out of a Christmas present."
    "What did I get her last year?"
    "Maybe I can use that as some sort of base."
    "..."
    "I have no idea what I got her last year."
    "In fact, did I even get her anything?"
    "We've been so out of touch since our childhood until recently."
    "And it's all because of the Literature Club."
    "But that still leaves me clueless as to what to get her."
    "When we were younger, anything would make her happy."
    "I could have gotten her some chocolate and she would scream like it was the best thing ever."
    "Could I still do something like that?"
    "Or would that look like me just being cheap?"
    show mysteriousclerk 1cha zorder 2 at t11
    cl "Hey there, little man."
    cl "Watch where you're going."
    "A strange looking man appears in front of me."
    "He seems to be stocking the shelves with...something."
    "It looks like some kind of plant...?"
    "Which is odd because the rest of the store is filled with books and electronics."
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
    cl "The executive officer of this humble abode."
    cl "The master of this venerable estate."
    cl "The--"
    mc "Alright, I get it."
    "Did I even say that out loud?"
    "If not, why the hell did this guy just introduce himself like that all of a sudden?"
    cl "Like I said, you pick up a few tricks."
    mc "..."
    cl "Anyway, what can I do for you?"
    cl "Want some help getting some gifts?"
    mc "What? No."
    mc "Especially not from--"
    cl "Call me Nick."
    $ cl_name = "Nick"
    mc "Right...Well, I was just about to leave, {i}Nick{/i}."
    mc "So, if you don't mind."
    "I try to make my way past him but he blocks my way."
    cl "Ho, ho, ho little man."
    cl "Are you sure you wanna do that?"
    cl "I know exactly the sort of thing those girls would like."
    cl "Well, it's more of a fifty-fifty."
    cl "But it's better than getting them nothing, am I right?"
    mc "Look, I'm not sure how exactly you knew this much already."
    mc "But I really doubt you know enough about those girls to know what gift to get them."
    cl "Is that a test?"
    cl "Good sir, are you challenging my knowledge?"
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
    "But then how would she have known I'd end up here."
    cl "Just hear me out, okay?"
    cl "You can make the decision in the end."
    mc "Fine."
    cl "Splendid!"
    cl "Right this way."
    "The man takes me to a section of the store."
    "There's all sorts of fluffy animals here."
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
            $ christmas_gifts[0] = 0
        "Management book.":
            $ christmas_gifts[0] = 1
    $ persistent.did_christmas_event = True
    $ special_chapter = False
    $ pause(1.0)
    $ style.say_window = style.window
    $ renpy.utter_restart()
    return