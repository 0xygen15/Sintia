from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from local.lang import Texts

# texts = Texts.keyboards
# texts_themes = Texts.themes
class TordKeyboard:
    def __init__(self):
        self.cb_td = CallbackData('name', 'action')
        self.keyboard_td = InlineKeyboardMarkup(row_width=2,
                                                inline_keyboard=[
                                                    [
                                                        InlineKeyboardButton(Texts.keyboards["truth"],
                                                                             callback_data=self.cb_td.new(
                                                                                 action='truth')),
                                                        InlineKeyboardButton(Texts.keyboards["dare"],
                                                                             callback_data=self.cb_td.new(
                                                                                 action='dare'))
                                                    ],
                                                    [
                                                        InlineKeyboardButton(Texts.keyboards["end"],
                                                                             callback_data=self.cb_td.new(
                                                                                 action='end'))
                                                    ]
                                                ])

        self.cb_all_level = CallbackData('name', 'action')

        self.mark1 = ""
        self.mark2 = ""
        self.mark3 = ""
        self.mark4 = ""
        self.mark5 = ""
        self.lifestyle_level = False
        self.absurd_level = False
        self.relations_level = False
        self.personal_level = False
        self.adult_level = False

        self.keyboard_level_all = InlineKeyboardMarkup(row_width=1,
                                                       inline_keyboard=[
                                                           [
                                                               InlineKeyboardButton(f'{Texts.keyboards["about life"]} {self.mark1}',
                                                                                    callback_data=self.cb_all_level.new(
                                                                                        action='lifestyle'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   f'{Texts.keyboards["absurd"]} {self.mark2}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='absurd'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   f'{Texts.keyboards["company"]} {self.mark3}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='company'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   f'{Texts.keyboards["relations"]} {self.mark4}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='relations'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   f'{Texts.keyboards["awkward"]} {self.mark5}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='awkward'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   Texts.keyboards["choice is made"],
                                                                   callback_data=self.cb_all_level.new(action=
                                                                                                       'ready')
                                                               )
                                                           ]
                                                       ]
                                                       )

        self.cb_players = CallbackData('name', 'action')

        self.keyboard_players = InlineKeyboardMarkup(row_width=2,
                                                     inline_keyboard=[
                                                         [
                                                             InlineKeyboardButton(Texts.keyboards["right"],
                                                                                  callback_data=self.cb_players.new(
                                                                                      action='yes')),
                                                             InlineKeyboardButton(Texts.keyboards["need edit"],
                                                                                  callback_data=self.cb_players.new(
                                                                                      action='no')),
                                                         ]
                                                     ]
                                                     )
        self.cb_mode = CallbackData('name', 'action')
        self.free_mode = False
        self.step_mode = False
        self.mode_mark1 = ''
        self.mode_mark2 = ''
        self.keyboard_mode = InlineKeyboardMarkup(row_width=2,
                                                  inline_keyboard=[
                                                      [
                                                          InlineKeyboardButton(Texts.keyboards["free mode"],
                                                                               callback_data=self.cb_mode.new(
                                                                                   action='free'
                                                                               )),

                                                      ],
                                                      [
                                                          InlineKeyboardButton(Texts.keyboards["alternate mode"],
                                                                               callback_data=self.cb_mode.new(
                                                                                   action='step'
                                                                               ))
                                                      ]
                                                  ])

        self.cb_completed = CallbackData('name', 'action')
        self.keyboard_completed = InlineKeyboardMarkup(row_width=2,
                                                       inline_keyboard=[
                                                           [
                                                               InlineKeyboardButton(Texts.keyboards["done"],
                                                                                    callback_data=self.cb_completed.new(
                                                                                        action='completed'
                                                                                    )),

                                                           ],
                                                           [
                                                               InlineKeyboardButton(Texts.keyboards["not done"],
                                                                                    callback_data=self.cb_completed.new(
                                                                                        action='failed'
                                                                                    ))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(Texts.keyboards["end the game"],
                                                                                    callback_data=self.cb_completed.new(
                                                                                        action='over'
                                                                                    ))
                                                           ]
                                                       ])
        self.cb_completed_f = CallbackData('name', 'action')

        self.keyboard_completed_f = InlineKeyboardMarkup(row_width=2,
                                                         inline_keyboard=[
                                                             [
                                                                 InlineKeyboardButton(Texts.keyboards["done"],
                                                                                      callback_data=self.cb_completed.new(
                                                                                          action='completed_f'
                                                                                      )),

                                                             ],
                                                             [
                                                                 InlineKeyboardButton(Texts.keyboards["not done"],
                                                                                      callback_data=self.cb_completed.new(
                                                                                          action='failed_f'
                                                                                      ))
                                                             ]
                                                         ])


    def update_keyboard(self, index: int, old_keyboard: InlineKeyboardMarkup):
        object_text = old_keyboard.values.get("inline_keyboard")[index][0]['text']

        if "+" in str(object_text):
            if index == 0:
                self.mark1 = ""
                self.lifestyle_level = False
            elif index == 1:
                self.mark2 = ""
                self.absurd_level = False
            elif index == 2:
                self.mark3 = ""
                self.relations_level = False
            elif index == 3:
                self.mark4 = ""
                self.personal_level = False
            elif index == 4:
                self.mark5 = ""
                self.adult_level = False

        elif "+" not in str(object_text):
            if index == 0:
                self.mark1 = " +"
                self.lifestyle_level = True
            elif index == 1:
                self.mark2 = " +"
                self.absurd_level = True
            elif index == 2:
                self.mark3 = " +"
                self.relations_level = True
            elif index == 3:
                self.mark4 = " +"
                self.personal_level = True
            elif index == 4:
                self.mark5 = " +"
                self.adult_level = True

        updated_keyboard = InlineKeyboardMarkup(row_width=1,
                                                inline_keyboard=[
                                                    [
                                                        InlineKeyboardButton(f'{Texts.keyboards["about life"]} {self.mark1}',
                                                                             callback_data=self.cb_all_level.new(
                                                                                 action='lifestyle'))
                                                    ],
                                                    [
                                                        InlineKeyboardButton(
                                                            f'{Texts.keyboards["absurd"]} {self.mark2}',
                                                            callback_data=self.cb_all_level.new(
                                                                action='absurd'))
                                                    ],
                                                    [
                                                        InlineKeyboardButton(
                                                            f'{Texts.keyboards["company"]} {self.mark3}',
                                                            callback_data=self.cb_all_level.new(
                                                                action='company'))
                                                    ],
                                                    [
                                                        InlineKeyboardButton(
                                                            f'{Texts.keyboards["relations"]} {self.mark4}',
                                                            callback_data=self.cb_all_level.new(
                                                                action='relations'))
                                                    ],
                                                    [
                                                        InlineKeyboardButton(
                                                            f'{Texts.keyboards["awkward"]} {self.mark5}',
                                                            callback_data=self.cb_all_level.new(
                                                                action='awkward'))
                                                    ],
                                                    [
                                                        InlineKeyboardButton(
                                                            Texts.keyboards["choice is made"],
                                                            callback_data=self.cb_all_level.new(action=
                                                                                                'ready')
                                                        )
                                                    ]

                                                ]
                                                )
        return updated_keyboard

    def update_keyboard_mode(self, index: int, old_keyboard: InlineKeyboardMarkup):
        object_text = old_keyboard.values.get("inline_keyboard")[index][0]['text']
        if "+" in str(object_text):
            if index == 0:
                self.mode_mark1 = ''
                self.free_mode = False
            elif index == 1:
                self.mode_mark2 = ''
                self.step_mode = False
        elif "+" not in str(object_text):
            if index == 0:
                self.mode_mark1 = ' +'
                self.free_mode = True
            elif index == 1:
                self.mode_mark2 = ' +'
                self.step_mode = True
        updated_keyboard_mode = InlineKeyboardMarkup(row_width=2,
                                                     inline_keyboard=[
                                                         [
                                                             InlineKeyboardButton(f'{Texts.keyboards["free mode"]} {self.mode_mark1}',
                                                                                  callback_data=self.cb_mode.new(
                                                                                      action='free'
                                                                                  )),

                                                         ],
                                                         [
                                                             InlineKeyboardButton(f'{Texts.keyboards["alternate mode"]} {self.mode_mark2}',
                                                                                  callback_data=self.cb_mode.new(
                                                                                      action='step'
                                                                                  ))
                                                         ]
                                                     ])
        return updated_keyboard_mode
class NieKeyboard:
    def __init__(self):
        self.cb_nie = CallbackData('name', 'action')
        self.keyboard_nie = InlineKeyboardMarkup(row_width=2,
                                                 inline_keyboard=[
                                                     [
                                                         InlineKeyboardButton(Texts.keyboards["truth"],
                                                                              callback_data=self.cb_nie.new(
                                                                                  action='truth_nie')),
                                                         InlineKeyboardButton(Texts.keyboards["dare"],
                                                                              callback_data=self.cb_nie.new(
                                                                                  action='dare_nie'))
                                                     ],
                                                     [
                                                         InlineKeyboardButton(Texts.keyboards["never i ever"],
                                                                              callback_data=self.cb_nie.new(
                                                                                  action='next_nie'))
                                                     ],
                                                     [
                                                         InlineKeyboardButton(Texts.keyboards["end the game"],
                                                                              callback_data=self.cb_nie.new(
                                                                                  action='end_nie'))
                                                     ]
                                                 ])
        self.cb_all_level = CallbackData('name', 'action')

        self.mark1 = ""
        self.mark2 = ""
        self.mark3 = ""
        self.mark4 = ""
        self.mark5 = ""
        self.lifestyle_level = False
        self.absurd_level = False
        self.relations_level = False
        self.personal_level = False
        self.adult_level = False

        self.keyboard_level_all = InlineKeyboardMarkup(row_width=1,
                                                       inline_keyboard=[
                                                           [
                                                               InlineKeyboardButton(f'{Texts.keyboards["about life"]} {self.mark1}',
                                                                                    callback_data=self.cb_all_level.new(
                                                                                        action='lifestyle'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   f'{Texts.keyboards["absurd"]} {self.mark2}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='absurd'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   f'{Texts.keyboards["company"]} {self.mark3}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='company'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   f'{Texts.keyboards["relations"]} {self.mark4}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='relations'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   f'{Texts.keyboards["awkward"]} {self.mark5}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='awkward'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   Texts.keyboards["choice is made"],
                                                                   callback_data=self.cb_all_level.new(action=
                                                                                                       'ready')
                                                               )
                                                           ]
                                                       ]
                                                       )
        self.cb_completed = CallbackData('name', 'action')
        self.keyboard_completed = InlineKeyboardMarkup(row_width=2,
                                                       inline_keyboard=[
                                                           [
                                                               InlineKeyboardButton(Texts.keyboards["done"],
                                                                                    callback_data=self.cb_completed.new(
                                                                                        action='completed'
                                                                                    )),

                                                           ],
                                                           [
                                                               InlineKeyboardButton(Texts.keyboards["not done"],
                                                                                    callback_data=self.cb_completed.new(
                                                                                        action='failed'
                                                                                    ))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(Texts.keyboards["end the game"],
                                                                                    callback_data=self.cb_completed.new(
                                                                                        action='over'
                                                                                    ))
                                                           ]
                                                       ])
        self.cb_completed_f = CallbackData('name', 'action')

        self.keyboard_completed_f = InlineKeyboardMarkup(row_width=2,
                                                         inline_keyboard=[
                                                             [
                                                                 InlineKeyboardButton(Texts.keyboards["done"],
                                                                                      callback_data=self.cb_completed_f.new(
                                                                                          action='completed_f'
                                                                                      )),

                                                             ],
                                                             [
                                                                 InlineKeyboardButton(Texts.keyboards["not done"],
                                                                                      callback_data=self.cb_completed_f.new(
                                                                                          action='failed_f'
                                                                                      ))
                                                             ]
                                                         ])


    def update_keyboard(self, index: int, old_keyboard: InlineKeyboardMarkup):
        object_text = old_keyboard.values.get("inline_keyboard")[index][0]['text']

        if "+" in str(object_text):
            if index == 0:
                self.mark1 = ""
                self.lifestyle_level = False
            elif index == 1:
                self.mark2 = ""
                self.absurd_level = False
            elif index == 2:
                self.mark3 = ""
                self.relations_level = False
            elif index == 3:
                self.mark4 = ""
                self.personal_level = False
            elif index == 4:
                self.mark5 = ""
                self.adult_level = False

        elif "+" not in str(object_text):
            if index == 0:
                self.mark1 = " +"
                self.lifestyle_level = True
            elif index == 1:
                self.mark2 = " +"
                self.absurd_level = True
            elif index == 2:
                self.mark3 = " +"
                self.relations_level = True
            elif index == 3:
                self.mark4 = " +"
                self.personal_level = True
            elif index == 4:
                self.mark5 = " +"
                self.adult_level = True

        updated_keyboard = InlineKeyboardMarkup(row_width=1,
                                                inline_keyboard=[
                                                           [
                                                               InlineKeyboardButton(f'{Texts.keyboards["about life"]} {self.mark1}',
                                                                                    callback_data=self.cb_all_level.new(
                                                                                        action='lifestyle'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   f'{Texts.keyboards["absurd"]} {self.mark2}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='absurd'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   f'{Texts.keyboards["company"]} {self.mark3}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='company'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   f'{Texts.keyboards["relations"]} {self.mark4}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='relations'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   f'{Texts.keyboards["awkward"]} {self.mark5}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='awkward'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   Texts.keyboards["choice is made"],
                                                                   callback_data=self.cb_all_level.new(action=
                                                                                                       'ready')
                                                               )
                                                           ]
                                                       ]
                                                )
        return updated_keyboard

class ThreeOfFiveKeyboard:
    def __init__(self):
        self.cb35 = CallbackData('name', 'action')
        self.kb35 = InlineKeyboardMarkup(row_width=2,
                                         inline_keyboard=[
                                             [
                                                 InlineKeyboardButton(Texts.keyboards["chapter truth"],
                                                                      callback_data=self.cb35.new(action="Truth"))
                                             ],
                                             [
                                                 InlineKeyboardButton(Texts.keyboards["chapter dare"],
                                                                      callback_data=self.cb35.new(action="Dare"))
                                             ],
                                             [
                                                 InlineKeyboardButton(Texts.keyboards["chapter nie"],
                                                                      callback_data=self.cb35.new(action="Never"))
                                             ],
                                             [
                                                 InlineKeyboardButton(Texts.keyboards["endgame new game"],
                                                                      callback_data=self.cb35.new(action="End"))
                                             ]
                                         ])

        self.cb35b = CallbackData('name', 'action')
        self.kb35b = InlineKeyboardMarkup(row_width=2,
                                          inline_keyboard=[
                                              [
                                                  InlineKeyboardButton(Texts.keyboards["begin"],
                                                                       callback_data=self.cb35.new(action="Begin"))
                                              ]
                                          ])
class ThemesKeyboard:
    def __init__(self):
        # self.cb_completed = CallbackData('name', 'action')
        # self.keyboard_completed = InlineKeyboardMarkup(row_width=2,
        #                                                inline_keyboard=[
        #                                                    [
        #                                                        InlineKeyboardButton('Выполнено',
        #                                                                             callback_data=self.cb_completed.new(
        #                                                                                 action='completed'
        #                                                                             )),
        #
        #                                                    ],
        #                                                    [
        #                                                        InlineKeyboardButton('Не выполнено',
        #                                                                             callback_data=self.cb_completed.new(
        #                                                                                 action='failed'
        #                                                                             ))
        #                                                    ],
        #                                                    [
        #                                                        InlineKeyboardButton(' О к о н ч и т ь  и г р у',
        #                                                                             callback_data=self.cb_completed.new(
        #                                                                                 action='over'
        #                                                                             ))
        #                                                    ]
        #                                                ])
        self.cb_themes = CallbackData('name', 'action')
        self.kb_themes = InlineKeyboardMarkup(row_width=3,
                                              inline_keyboard=[
                                                  [
                                                      InlineKeyboardButton(Texts.themes["school name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="school")),
                                                      InlineKeyboardButton(Texts.themes["work name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="work")),
                                                      InlineKeyboardButton(Texts.themes["travel name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="travel"))
                                                  ],
                                                  [
                                                      InlineKeyboardButton(Texts.themes["worldview name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="worldview")),
                                                      InlineKeyboardButton(Texts.themes["social media name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="social media")),
                                                      InlineKeyboardButton(Texts.themes["art name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="art"))
                                                  ],
                                                  [
                                                      InlineKeyboardButton(Texts.themes["relations name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="relations")),
                                                      InlineKeyboardButton(Texts.themes["memes name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="memes")),
                                                      InlineKeyboardButton(Texts.themes["religion name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="religion"))

                                                  ],
                                                  [
                                                      InlineKeyboardButton(Texts.themes["memories name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="memories")),
                                                      InlineKeyboardButton(Texts.themes["if name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="if")),
                                                      InlineKeyboardButton(Texts.themes["videogames name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="videogames"))
                                                  ],
                                                  [
                                                      InlineKeyboardButton(Texts.themes["education name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="education")),
                                                      InlineKeyboardButton(Texts.themes["fashion name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="fashion")),
                                                      InlineKeyboardButton(Texts.themes["hard choice name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="hard choice"))
                                                  ]
                                              ])

        self.cb_themes_game = CallbackData('name', 'action')
        self.kb_themes_game = InlineKeyboardMarkup(row_width=2,
                                                   inline_keyboard=[
                                                       [
                                                           InlineKeyboardButton('⬅️',
                                                                                callback_data=self.cb_themes_game.new(
                                                                                    action='previous'
                                                                                )),
                                                           InlineKeyboardButton('➡️',
                                                                                callback_data=self.cb_themes_game.new(
                                                                                    action='next'
                                                                                ))

                                                       ],
                                                       [
                                                           InlineKeyboardButton(Texts.keyboards["end the game"],
                                                                                callback_data=self.cb_themes_game.new(
                                                                                    action='end'
                                                                                ))
                                                       ]
                                                   ]
                                                   )
        self.cb_themes_confirm = CallbackData('name', 'action')
        self.kb_themes_confirm = InlineKeyboardMarkup(row_width=2,
                                                      inline_keyboard=[
                                                          [
                                                              InlineKeyboardButton(Texts.keyboards["menu"],
                                                                                   callback_data=self.cb_themes_confirm.new(
                                                                                       action='menu'
                                                                                   )),
                                                              InlineKeyboardButton(Texts.keyboards["begin"],
                                                                                   callback_data=self.cb_themes_confirm.new(
                                                                                       action='begin'
                                                                                   ))

                                                          ]
                                                      ]
                                                      )

class ConfigKeyboard:
    cb_lang = CallbackData('name', 'action')
    kb_lang = InlineKeyboardMarkup(row_width=3,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton("English", callback_data=cb_lang.new(action="en")),
                                           InlineKeyboardButton("Deutsch", callback_data=cb_lang.new(action="de")),
                                           InlineKeyboardButton("Espana", callback_data=cb_lang.new(action="es")),
                                       ],
                                       [
                                           InlineKeyboardButton("Русский", callback_data=cb_lang.new(action="ru")),
                                           InlineKeyboardButton("Српски", callback_data=cb_lang.new(action="sr")),
                                           InlineKeyboardButton("Українська", callback_data=cb_lang.new(action="uk")),
                                       ],
                                       [
                                           InlineKeyboardButton("France", callback_data=cb_lang.new(action="fr"))
                                       ]
                                   ])