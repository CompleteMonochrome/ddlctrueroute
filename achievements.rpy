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
        background "#333333cc"
        xalign .98
        yalign .02
        xysize (450, 100)

        #

        hbox:
            vbox:
                spacing 10
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
    def get_achievement(ach_id, trans=achievement_transform):
        ach = persistent.achievements_dict[ach_id]
        # achievement.grant(ach_id)
        if not ach["achieved"]:
            ach["achieved"] = True
            renpy.show_screen(_screen_name='scr_achievement_get', title=ach['title'],
                            a_text=ach['text'], icon=ach['icon'], trans=trans)

    def update_achievement(ach_id, to_add=1, trans=achievement_transform):
        persistent.achievements_dict[ach_id]["cur_prog"] += to_add
        ach = persistent.achievements_dict[ach_id]

        # achievement.progress(ach_id, to_add)
        if ach['cur_prog'] > ach['max_prog']:
            persistent.achievements_dict[ach_id]["cur_prog"] = ach['max_prog']
            ach = persistent.achievements_dict[ach_id]

        renpy.show_screen(_screen_name='scr_achievement_update', title=ach['title'], a_text=ach['text'],
                          icon=ach['icon'], cur_prog=ach['cur_prog'], max_prog=ach['max_prog'], trans=trans)





    # Define your achievements here
    if not persistent.achievements_dict:
        persistent.achievements_dict = {"*Custom Start*": {"type": 0,
                                                            "title": "Custom Start",
                                                            "text": "Use Custom Start for the first time.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*True Route*": {"type": 0,
                                                            "title": "True Route",
                                                            "text": "Enter the beginning of the mod.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*Book of Despair*": {"type": 0,
                                                            "title": "Book of Despair",
                                                            "text": "Finish Yuri's arc.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*A Second Chance*": {"type": 0,
                                                            "title": "A Second Chance",
                                                            "text": "Finish Natsuki's arc.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*Inauguration Day*": {"type": 0,
                                                            "title": "Inauguration Day",
                                                            "text": "Finish Sayori's arc.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*A Whole New World*": {"type": 0,
                                                            "title": "A Whole New World",
                                                            "text": "Finish Monika's arc.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*What Will It Take?*": {"type": 0,
                                                            "title": "What Will It Take?",
                                                            "text": "Finish the Special Day event.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*It's Christmas!*": {"type": 0,
                                                            "title": "It's Christmas!",
                                                            "text": "Finish the Christmas event.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*The Bashful Lady*": {"type": 0,
                                                            "title": "The Bashful Lady",
                                                            "text": "Go on a date with Yuri.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*Sweet, Sweet Love*": {"type": 0,
                                                            "title": "Sweet, Sweet Love",
                                                            "text": "Go on a date with Natsuki.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*Childhood Sweetheart*": {"type": 0,
                                                            "title": "Childhood Sweetheart",
                                                            "text": "Go on a date with Sayori.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*Monika's Reality*": {"type": 0,
                                                            "title": "Monika's Reality",
                                                            "text": "Go on a date with Monika.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*Who's Natsuki?*": {"type": 0,
                                                            "title": "Who's Natsuki?",
                                                            "text": "Delete Yasuhiro when you first meet him.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*Past Life*": {"type": 0,
                                                            "title": "Past Life",
                                                            "text": "Delete Ayame when you first meet her.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*Father's Redemption*": {"type": 0,
                                                            "title": "Father's Redemption",
                                                            "text": "Make Yasuhiro regret his past actions.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*A Mother's Love*": {"type": 0,
                                                            "title": "A Mother's Love",
                                                            "text": "Reunite Natsuki with her mother.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*Together Once More*": {"type": 0,
                                                            "title": "Together Once More",
                                                            "text": "Bring Natsuki's whole family back together.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*Strawberries*": {"type": 0,
                                                            "title": "Strawberries",
                                                            "text": "Use strawberries to do the impossible.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*The Truth*": {"type": 0,
                                                            "title": "The Truth",
                                                            "text": "Learn the truth about the world.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*True Sayori*": {"type": 0,
                                                            "title": "True Sayori",
                                                            "text": "Convince Sayori to bring you along.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*True Monika*": {"type": 0,
                                                            "title": "True Monika",
                                                            "text": "Help Monika stay true to herself.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*True Monika, Again*": {"type": 0,
                                                            "title": "True Monika, Again",
                                                            "text": "Continue to help Monika be herself.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*Let Your Hair Down*": {"type": 0,
                                                            "title": "Let Your Hair Down",
                                                            "text": "Make Monika wear her hair down.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*Just Do It.*": {"type": 0,
                                                            "title": "Just Do It.",
                                                            "text": "Be forced to select an option.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                        "*Fastest Man Alive*": {"type": 0,
                                                            "title": "Fastest Man Alive",
                                                            "text": "Choose an option that disappears quickly.",
                                                            "icon": "mod_assets/gui/achievements/ach1.png",
                                                            "achieved": False
                                                            },
                                    # "*achievent_name*": {"type": 1, # Progress achievent
                                    #                      "title": "",
                                    #                      "text": "",
                                    #                      "icon": "images/icons/ach.png",
                                    #                      "cur_prog": , # current progress
                                    #                      "max_prog": # maximal progress
                                    #                      }
                                    }


        # for i, a in persistent.achievements_dict.items():
        #     if a['type'] == 0:
        #         achievement.register(i, steam=a['title'])
        #     if a['type'] == 1:
        #         achievement.register(i, steam=a['title'], stat_max=a['max_prog'])
