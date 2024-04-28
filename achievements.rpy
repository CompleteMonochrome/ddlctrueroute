# Taken from https://github.com/OlegWock/Roselia-achievements, modified for use with True Route

transform achievement_transform:
    on show:
        alpha 0
        linear 1.0 alpha 1.0
        3.0
        alpha 1.0
        linear 1.0 alpha 0
    on hide:
        linear 3.0 alpha 0


screen scr_achievement_get(title, a_text, icon, trans=achievement_transform):
    layer "achievements"
    timer 5 action Hide("scr_achievement_get")
    window:
        at trans
        background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
        xalign .98
        yalign .02
        xysize (450, 100)
        hbox:
            vbox:
                spacing 10
                xpos 4
                ypos 2
                image icon
            vbox:
                xoffset 10
                xsize 330
                text title:
                    size 28
                    id title
                text a_text:
                    size 22
                    id a_text

screen scr_achievement_update(title, a_text, icon, cur_prog, max_prog, trans=achievement_transform):
    layer "achievements"
    timer 5 action Hide("scr_achievement_update")
    window:
        at trans
        background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
        xalign .98
        yalign .02
        xysize (450, 100)

        #

        hbox:
            vbox:
                spacing 10
                xpos 4
                ypos 2
                image icon
                text "{0}/{1}".format(cur_prog, max_prog):
                    xcenter 0.5
                    ycenter 0.2
            vbox:
                xoffset 10
                xsize 330
                text title:
                    size 28
                    id title
                text a_text:
                    size 22
                    id a_text






init python:
    import collections
    def get_achievement(ach_id, trans=achievement_transform):
        ach = persistent.achievements_dict[ach_id]
        # achievement.grant(ach_id)
        if not ach["achieved"]:
            ach["achieved"] = True
            renpy.play("mod_assets/sfx/achievementsound.ogg",channel="sound")
            renpy.show_screen(_screen_name='scr_achievement_get', title=ach['title'],
                            a_text=ach['text'], icon=ach['icon'], trans=trans)

    def update_achievement(ach_id, to_add=1, trans=achievement_transform):
        persistent.achievements_dict[ach_id]["cur_prog"] += to_add
        ach = persistent.achievements_dict[ach_id]

        # achievement.progress(ach_id, to_add)
        if ach['cur_prog'] > ach['max_prog'] and not ach["achieved"]:
            ach["achieved"] = True
            persistent.achievements_dict[ach_id]["cur_prog"] = ach['max_prog']
            ach = persistent.achievements_dict[ach_id]
            renpy.play("mod_assets/sfx/achievementsound.ogg",channel="sound")
            renpy.show_screen(_screen_name='scr_achievement_update', title=ach['title'], a_text=ach['text'],
                              icon=ach['icon'], cur_prog=ach['cur_prog'], max_prog=ach['max_prog'], trans=trans)





    # Define your achievements here
    if not persistent.achievements_dict:
        persistent.achievements_dict = collections.OrderedDict()
        persistent.achievements_dict["*True Route*"] = {"type": 0,
                            "title": "True Route",
                            "text": "Enter the beginning of the mod.",
                            "icon": "mod_assets/gui/achievements/achmod.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*Custom Start*"] = {"type": 0,
                            "title": "Custom Start",
                            "text": "Use Custom Start to decide your new fate.",
                            "icon": "mod_assets/gui/achievements/achcustomstart.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*Book of Despair*"] = {"type": 0,
                            "title": "Book of Despair",
                            "text": "Finish Yuri's arc.",
                            "icon": "mod_assets/gui/achievements/achyuri.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*A Second Chance*"] = {"type": 0,
                            "title": "A Second Chance",
                            "text": "Finish Natsuki's arc.",
                            "icon": "mod_assets/gui/achievements/achnatsuki.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*Inauguration Day*"] = {"type": 0,
                            "title": "Inauguration Day",
                            "text": "Finish Sayori's arc.",
                            "icon": "mod_assets/gui/achievements/achsayori.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*A Whole New World*"] = {"type": 0,
                            "title": "A Whole New World",
                            "text": "Finish Monika's arc.",
                            "icon": "mod_assets/gui/achievements/achmonika.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*What Will It Take?*"] = {"type": 0,
                            "title": "What Will It Take?",
                            "text": "Finish the Special Day event.",
                            "icon": "mod_assets/gui/achievements/achspecialday.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*It's Christmas!*"] = {"type": 0,
                            "title": "It's Christmas!",
                            "text": "Finish the Christmas event.",
                            "icon": "mod_assets/gui/achievements/achchristmas.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*Christmas Miracle*"] = {"type": 0,
                            "title": "Christmas Miracle",
                            "text": "Finish the 2019 Christmas event.",
                            "icon": "mod_assets/gui/achievements/achchristmas2.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*Valentine Revelation*"] = {"type": 0,
                            "title": "Valentine Revelation",
                            "text": "Finish the Valentine's Day event.",
                            "icon": "mod_assets/gui/achievements/achvalentines.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*The Bashful Lady*"] = {"type": 0,
                            "title": "The Bashful Lady",
                            "text": "Go on a date with Yuri.",
                            "icon": "mod_assets/gui/achievements/achbashfullady.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*Sweet, Sweet Love*"] = {"type": 0,
                            "title": "Sweet, Sweet Love",
                            "text": "Go on a date with Natsuki.",
                            "icon": "mod_assets/gui/achievements/achsweetlove.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*Childhood Sweetheart*"] = {"type": 0,
                            "title": "Childhood Sweetheart",
                            "text": "Go on a date with Sayori.",
                            "icon": "mod_assets/gui/achievements/achchildhoodsweetheart.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*Monika's Reality*"] = {"type": 0,
                            "title": "Monika's Reality",
                            "text": "Go on a date with Monika.",
                            "icon": "mod_assets/gui/achievements/achmonikasreality.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*Timeless Classic*"] = {"type": 0,
                            "title": "Timeless Classic",
                            "text": "Go on a \"date\" with Ayame.",
                            "icon": "mod_assets/gui/achievements/achtimelessclassic.png",
                            "achieved": False,
                            "hidden": True
                            }
        persistent.achievements_dict["*Okay, Everyone!*"] = {"type": 0,
                            "title": "Okay, Everyone!",
                            "text": "Go on a date with everyone.",
                            "icon": "mod_assets/gui/achievements/achokayeveryone.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*Genocide*"] = {"type": 0,
                            "title": "Genocide",
                            "text": "Have Yuri kill everyone in the club.",
                            "icon": "mod_assets/gui/achievements/achgenocide.png",
                            "achieved": False,
                            "hidden": True
                            }
        persistent.achievements_dict["*Who's Natsuki?*"] = {"type": 0,
                            "title": "Who's Natsuki?",
                            "text": "Delete Yasuhiro when you first meet him.",
                            "icon": "mod_assets/gui/achievements/achwhosnatsuki.png",
                            "achieved": False,
                            "hidden": True
                            }
        persistent.achievements_dict["*An Important Character*"] = {"type": 0,
                            "title": "An Important Character",
                            "text": "Delete Ayame when you first meet her.",
                            "icon": "mod_assets/gui/achievements/achpastlife.png",
                            "achieved": False,
                            "hidden": True
                            }
        persistent.achievements_dict["*When Will It End?!*"] = {"type": 0,
                            "title": "When Will It End?!",
                            "text": "Get through the play by telling Yuri to kill you.",
                            "icon": "mod_assets/gui/achievements/achwhenwillitend.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*Detective*"] = {"type": 0,
                            "title": "Detective",
                            "text": "Explore all the rooms in Natsuki's house.",
                            "icon": "mod_assets/gui/achievements/achdetective.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*More Than Just Friends*"] = {"type": 0,
                            "title": "More Than Just Friends",
                            "text": "Make Sayori recall a previous life through poetry.",
                            "icon": "mod_assets/gui/achievements/achmorethanfriends.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*Easy Modo?!*"] = {"type": 0,
                            "title": "Easy Modo?!",
                            "text": "Accept Monika's help during Natsuki's play.",
                            "icon": "mod_assets/gui/achievements/acheasymodo.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*Back From The Dead*"] = {"type": 0,
                            "title": "Back From The Dead",
                            "text": "Create Haruki.chr during Natsuki's play.",
                            "icon": "mod_assets/gui/achievements/achbackfromdead.png",
                            "achieved": False,
                            "hidden": True
                            }
        persistent.achievements_dict["*A Father's Redemption*"] = {"type": 0,
                            "title": "A Father's Redemption",
                            "text": "Make Yasuhiro regret his past actions.",
                            "icon": "mod_assets/gui/achievements/achfathersredemption.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*A Mother's Love*"] = {"type": 0,
                            "title": "A Mother's Love",
                            "text": "Reunite Natsuki with her mother.",
                                "icon": "mod_assets/gui/achievements/achmotherslove.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*Together Once More*"] = {"type": 0,
                            "title": "Together Once More",
                            "text": "Bring Natsuki's whole family back together.",
                            "icon": "mod_assets/gui/achievements/achtogetheroncemore.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*The Truth*"] = {"type": 0,
                            "title": "The Truth",
                            "text": "Learn the truth about the world.",
                            "icon": "mod_assets/gui/achievements/achthetruth.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*True Sayori*"] = {"type": 0,
                            "title": "True Sayori",
                            "text": "Convince Sayori to bring you along.",
                            "icon": "mod_assets/gui/achievements/achtruesayori.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*True Monika*"] = {"type": 0,
                            "title": "True Monika",
                            "text": "Help Monika stay true to herself.",
                            "icon": "mod_assets/gui/achievements/achtruemonika.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*True Monika, Again*"] = {"type": 0,
                            "title": "True Monika, Again",
                            "text": "Continue to help Monika be herself.",
                            "icon": "mod_assets/gui/achievements/achtruemonikaagain.png",
                            "achieved": False,
                            "hidden": True
                            }
        persistent.achievements_dict["*Let Your Hair Down*"] = {"type": 0,
                            "title": "Let Your Hair Down",
                            "text": "Make Monika wear her hair down.",
                            "icon": "mod_assets/gui/achievements/achdownmonika.png",
                            "achieved": False,
                            "hidden": True
                            }
        persistent.achievements_dict["*Loneliness Is Bliss*"] = {"type": 0,
                            "title": "Loneliness Is Bliss",
                            "text": "Make it to Inauguration Day alone.",
                            "icon": "mod_assets/gui/achievements/achblank.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*Blossoming Friendship*"] = {"type": 0,
                            "title": "Blossoming Friendship",
                            "text": "Make Yuri and Natsuki befriend each other.",
                            "icon": "mod_assets/gui/achievements/achtruefriends.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*The Die Is Cast*"] = {"type": 0,
                            "title": "The Die Is Cast",
                            "text": "Cast the die.",
                            "icon": "mod_assets/gui/achievements/achevilmonika.png",
                            "achieved": False,
                            "hidden": True
                            }
        persistent.achievements_dict["*Strawberries*"] = {"type": 0,
                            "title": "Strawberries",
                            "text": "Use strawberries to do the impossible.",
                            "icon": "mod_assets/gui/achievements/achstrawberries.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*Just Do It*"] = {"type": 0,
                            "title": "Just Do It",
                            "text": "Be forced to select an option.",
                            "icon": "mod_assets/gui/achievements/achdoit.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*Illusion of Choice*"] = {"type": 0,
                            "title": "Illusion of Choice",
                            "text": "Try an option that leads to the same result.",
                            "icon": "mod_assets/gui/achievements/achillusion.png",
                            "achieved": False,
                            "hidden": True
                            }
        persistent.achievements_dict["*Fastest Man Alive*"] = {"type": 0,
                            "title": "Fastest Man Alive",
                            "text": "Make a choice that quickly disappears.",
                            "icon": "mod_assets/gui/achievements/achfastestman.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*Sadist*"] = {"type": 0,
                            "title": "Sadist",
                            "text": "Continue to do the wrong thing after a rewind.",
                            "icon": "mod_assets/gui/achievements/achsadist.png",
                            "achieved": False,
                            "hidden": True
                            }
        persistent.achievements_dict["*Playboy*"] = {"type": 0,
                            "title": "Playboy",
                            "text": "Write for each girl at least once without going on a date.",
                            "icon": "mod_assets/gui/achievements/achplayboy.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*Another Perspective*"] = {"type": 0,
                            "title": "Another Perspective",
                            "text": "Unlock another perspective on Inauguration Day.",
                            "icon": "mod_assets/gui/achievements/achnewperspective.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*Can You Hear Me?*"] = {"type": 0,
                            "title": "Can You Hear Me?",
                            "text": "Listen to all 3 pieces Monika composed.",
                            "icon": "mod_assets/gui/achievements/achcanyouhearme.png",
                            "achieved": False,
                            "hidden": True
                            }
        persistent.achievements_dict["*Good Guy Clerk*"] = {"type": 0,
                            "title": "Good Guy Clerk",
                            "text": "Encounter the Mysterious Clerk.",
                            "icon": "mod_assets/gui/achievements/achgoodguyclerk.png",
                            "achieved": False,
                            "hidden": True
                            }
        persistent.achievements_dict["*Who Are You?*"] = {"type": 0,
                            "title": "Who Are You?",
                            "text": "Enter a poem game with completely new people.",
                            "icon": "mod_assets/gui/achievements/achwhoareyou.png",
                            "achieved": False,
                            "hidden": True
                            }
        persistent.achievements_dict["*Dark Side*"] = {"type": 0,
                            "title": "Dark Side",
                            "text": "Have evil Monika fall in love with you.",
                            "icon": "mod_assets/gui/achievements/achdarkside.png",
                            "achieved": False,
                            "hidden": True
                            }
        persistent.achievements_dict["*Is This The Right Mod?*"] = {"type": 0,
                            "title": "Is This The Right Mod?",
                            "text": "Play Monika After Story.",
                            "icon": "mod_assets/gui/achievements/achmas.png",
                            "achieved": False,
                            "hidden": True
                            }
        persistent.achievements_dict["*Naomik*"] = {"type": 0,
                            "title": "Naomik",
                            "text": "Save 'Naomik'.",
                            "icon": "mod_assets/gui/achievements/achnao.png",
                            "achieved": False,
                            "hidden": True
                            }
                                    # "*achievent_name*": {"type": 1, # Progress achievent
                                    #                      "title": "",
                                    #                      "text": "",
                                    #                      "icon": "images/icons/ach.png",
                                    #                      "cur_prog": , # current progress
                                    #                      "max_prog": # maximal progress
                                    #                      }
        
    # 0.9.8 update achievements
    if "*Valentine Revelation*" not in persistent.achievements_dict:
        persistent.achievements_dict["*Valentine Revelation*"] = {"type": 0,
                        "title": "Valentine Revelation",
                        "text": "Finish the Valentine's Day event.",
                        "icon": "mod_assets/gui/achievements/achvalentines.png",
                        "achieved": False,
                        "hidden": False
                        }
        persistent.achievements_dict["*Naomik*"] = {"type": 0,
                        "title": "Naomik",
                        "text": "Save 'Naomik'.",
                        "icon": "mod_assets/gui/achievements/achnao.png",
                        "achieved": False,
                        "hidden": True
                        }
        persistent.achievements_dict["*Once Again*"] = {"type": 0,
                        "title": "Once Again",
                        "text": "Finish True Route with True Monika as the president.",
                        "icon": "mod_assets/gui/achievements/achtmpres.png",
                        "achieved": False,
                        "hidden": True
                        }
        persistent.achievements_dict["*At Long Last*"] = {"type": 0,
                        "title": "At Long Last",
                        "text": "Finish True Route with Evil Monika as the president.",
                        "icon": "mod_assets/gui/achievements/achempres.png",
                        "achieved": False,
                        "hidden": True
                        }
        persistent.achievements_dict["*Unlimited Strawberries*"] = {"type": 0,
                        "title": "Unlimited Strawberries",
                        "text": "Finish True Route with True Sayori as the president.",
                        "icon": "mod_assets/gui/achievements/achtspres.png",
                        "achieved": False,
                        "hidden": True
                        }
        persistent.achievements_dict["*For The Good Of All*"] = {"type": 0,
                        "title": "For The Good Of All",
                        "text": "Finish True Route with Sayori as the president.",
                        "icon": "mod_assets/gui/achievements/achspres.png",
                        "achieved": False,
                        "hidden": True
                        }
        persistent.achievements_dict["*The Plan Revealed*"] = {"type": 0,
                        "title": "The Plan Revealed",
                        "text": "Finish True Route with True Ayame as the president.",
                        "icon": "mod_assets/gui/achievements/achtaypres.png",
                        "achieved": False,
                        "hidden": True
                        }
        persistent.achievements_dict["*Welcome To The Book Club!*"] = {"type": 0,
                        "title": "Welcome To The Book Club!",
                        "text": "Finish True Route with Ayame as the president.",
                        "icon": "mod_assets/gui/achievements/achaypres.png",
                        "achieved": False,
                        "hidden": True
                        }
        persistent.achievements_dict["*It's Up To Me*"] = {"type": 0,
                        "title": "It's Up To Me",
                        "text": "Finish True Route with the player as the president.",
                        "icon": "mod_assets/gui/achievements/achmcpres.png",
                        "achieved": False,
                        "hidden": True
                        }
        persistent.achievements_dict["*Final Route*"] = {"type": 0,
                        "title": "Final Route",
                        "text": "Complete the Final Route.",
                        "icon": "mod_assets/gui/achievements/achfinalroute.png",
                        "achieved": False,
                        "hidden": True
                        }
    
    # 0.9.8 Bugfix
    if "*A Long Time Coming" not in persistent.achievements_dict:
        persistent.achievements_dict["*A Long Time Coming*"] = {"type": 0,
                            "title": "A Long Time Coming",
                            "text": "Finish True Route.",
                            "icon": "mod_assets/gui/achievements/achtr.png",
                            "achieved": False,
                            "hidden": False
                            }
        persistent.achievements_dict["*Once Again*"] = {"type": 0,
                            "title": "Once Again",
                            "text": "Finish True Route with True Monika as the president.",
                            "icon": "mod_assets/gui/achievements/achtmpres.png",
                            "achieved": False,
                            "hidden": True
                            }
        persistent.achievements_dict["*At Long Last*"] = {"type": 0,
                            "title": "At Long Last",
                            "text": "Finish True Route with Evil Monika as the president.",
                            "icon": "mod_assets/gui/achievements/achempres.png",
                            "achieved": False,
                            "hidden": True
                            }
        persistent.achievements_dict["*Unlimited Strawberries*"] = {"type": 0,
                            "title": "Unlimited Strawberries",
                            "text": "Finish True Route with True Sayori as the president.",
                            "icon": "mod_assets/gui/achievements/achtspres.png",
                            "achieved": False,
                            "hidden": True
                            }
        persistent.achievements_dict["*For The Good Of All*"] = {"type": 0,
                            "title": "For The Good Of All",
                            "text": "Finish True Route with Sayori as the president.",
                            "icon": "mod_assets/gui/achievements/achspres.png",
                            "achieved": False,
                            "hidden": True
                            }
        persistent.achievements_dict["*The Plan Revealed*"] = {"type": 0,
                            "title": "The Plan Revealed",
                            "text": "Finish True Route with True Ayame as the president.",
                            "icon": "mod_assets/gui/achievements/achtaypres.png",
                            "achieved": False,
                            "hidden": True
                            }
        persistent.achievements_dict["*Welcome To The Book Club!*"] = {"type": 0,
                            "title": "Welcome To The Book Club!",
                            "text": "Finish True Route with Ayame as the president.",
                            "icon": "mod_assets/gui/achievements/achaypres.png",
                            "achieved": False,
                            "hidden": True
                            }
        persistent.achievements_dict["*It's Up To Me*"] = {"type": 0,
                            "title": "It's Up To Me",
                            "text": "Finish True Route with the player as the president.",
                            "icon": "mod_assets/gui/achievements/achmcpres.png",
                            "achieved": False,
                            "hidden": True
                            }
        persistent.achievements_dict["*Final Route*"] = {"type": 0,
                            "title": "Final Route",
                            "text": "Complete the Final Route.",
                            "icon": "mod_assets/gui/achievements/achfinalroute.png",
                            "achieved": False,
                            "hidden": True
                            }

    # 0.9.9 update achievements
                            


        # for i, a in persistent.achievements_dict.items():
        #     if a['type'] == 0:
        #         achievement.register(i, steam=a['title'])
        #     if a['type'] == 1:
        #         achievement.register(i, steam=a['title'], stat_max=a['max_prog'])
