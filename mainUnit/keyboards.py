from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from local.lang import Texts

class TordKeyboard:
    def __init__(self, loc_file: Texts):
        self.loc_file = loc_file

        self.to_menu_cb = CallbackData('name', 'action')
        self.to_menu_kb = InlineKeyboardMarkup(row_width=1,
                                               inline_keyboard=[
                                                   [
                                                       InlineKeyboardButton(
                                                           text=f"""🔙 {self.loc_file.keyboards["menu"]} 🔙""",
                                                           callback_data=self.to_menu_cb.new(action='main menu')
                                                       )
                                                   ]
                                               ])

        self.cb_td = CallbackData('name', 'action')
        self.keyboard_td = InlineKeyboardMarkup(row_width=2,
                                                inline_keyboard=[
                                                    [
                                                        InlineKeyboardButton(text=f"""❔ {self.loc_file.keyboards["truth"]}""",
                                                                             callback_data=self.cb_td.new(
                                                                                 action='truth')),
                                                        InlineKeyboardButton(text=f"""🤸 {self.loc_file.keyboards["dare"]}""",
                                                                             callback_data=self.cb_td.new(
                                                                                 action='dare'))
                                                    ],
                                                    [
                                                        InlineKeyboardButton(text=f"""🔚 {self.loc_file.keyboards["end"]}""",
                                                                             callback_data=self.cb_td.new(
                                                                                 action='end'))
                                                    ]
                                                ])

        self.cb_all_level = CallbackData('name', 'action')

        # self.mark1 = ""
        # self.mark2 = ""
        # self.mark3 = ""
        # self.mark4 = ""
        # self.mark5 = ""
        self.mark1, self.mark2, self.mark3, self.mark4, self.mark5 = "", "", "", "", ""
        # self.lifestyle_level = False
        # self.absurd_level = False
        # self.relations_level = False
        # self.personal_level = False
        # self.adult_level = False

        self.keyboard_level_all = InlineKeyboardMarkup(row_width=2,
                                                       inline_keyboard=[
                                                           [
                                                               InlineKeyboardButton(f'{self.loc_file.keyboards["about life"]} {self.mark1}',
                                                                                    callback_data=self.cb_all_level.new(
                                                                                        action='lifestyle'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   f'{self.loc_file.keyboards["absurd"]} {self.mark2}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='absurd')),
                                                               InlineKeyboardButton(
                                                                   f'{self.loc_file.keyboards["company"]} {self.mark3}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='company'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   f'{self.loc_file.keyboards["relations"]} {self.mark4}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='relations')),
                                                               InlineKeyboardButton(
                                                                   f'{self.loc_file.keyboards["awkward"]} {self.mark5}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='awkward'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   text=f""">>> {self.loc_file.keyboards["choice is made"]} <<<""",
                                                                   callback_data=self.cb_all_level.new(action='ready')
                                                               )
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   text=f"""🔙 {self.loc_file.keyboards["menu"]} 🔙""",
                                                                   callback_data=self.cb_all_level.new(action='main menu')
                                                               )
                                                           ]
                                                       ]
                                                       )

        self.cb_players = CallbackData('name', 'action')

        self.keyboard_players = InlineKeyboardMarkup(row_width=2,
                                                     inline_keyboard=[
                                                         [
                                                             InlineKeyboardButton(text=f"""👍 {self.loc_file.keyboards["right"]}""",
                                                                                  callback_data=self.cb_players.new(
                                                                                      action='yes')),
                                                             InlineKeyboardButton(text=f"""✏️ {self.loc_file.keyboards["need edit"]}""",
                                                                                  callback_data=self.cb_players.new(
                                                                                      action='no')),
                                                         ],
                                                         [
                                                             InlineKeyboardButton(
                                                                 text=f"""🔙 {self.loc_file.keyboards["menu"]} 🔙""",
                                                                 callback_data=self.cb_all_level.new(action='main menu')
                                                             )
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
                                                          InlineKeyboardButton(self.loc_file.keyboards["free mode"],
                                                                               callback_data=self.cb_mode.new(
                                                                                   action='free'
                                                                               )),

                                                      ],
                                                      [
                                                          InlineKeyboardButton(self.loc_file.keyboards["alternate mode"],
                                                                               callback_data=self.cb_mode.new(
                                                                                   action='step'
                                                                               ))
                                                      ]
                                                  ])

        self.cb_completed = CallbackData('name', 'action')
        self.keyboard_completed = InlineKeyboardMarkup(row_width=2,
                                                       inline_keyboard=[
                                                           [
                                                               InlineKeyboardButton(text=f"""✔️ {self.loc_file.keyboards["done"]}""",
                                                                                    callback_data=self.cb_completed.new(
                                                                                        action='completed'
                                                                                    )),

                                                           ],
                                                           [
                                                               InlineKeyboardButton(text=f"""❌ {self.loc_file.keyboards["not done"]}""",
                                                                                    callback_data=self.cb_completed.new(
                                                                                        action='failed'
                                                                                    ))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(text=f"""🔚 {self.loc_file.keyboards["end the game"]}""",
                                                                                    callback_data=self.cb_completed.new(
                                                                                        action='over'
                                                                                    ))
                                                           ]
                                                       ])
        self.cb_completed_f = CallbackData('name', 'action')

        self.keyboard_completed_f = InlineKeyboardMarkup(row_width=2,
                                                         inline_keyboard=[
                                                             [
                                                                 InlineKeyboardButton(text=f"""✔️ {self.loc_file.keyboards["done"]}""",
                                                                                      callback_data=self.cb_completed.new(
                                                                                          action='completed_f'
                                                                                      )),

                                                             ],
                                                             [
                                                                 InlineKeyboardButton(text=f"""❌ {self.loc_file.keyboards["not done"]}""",
                                                                                      callback_data=self.cb_completed.new(
                                                                                          action='failed_f'
                                                                                      ))
                                                             ]
                                                         ])
    def __str__(self):
        return f"""Tord Kb object. Sample: {self.loc_file.keyboards["dare"]}"""

    def reset(self):
        self.mark1 = ""
        self.mark2 = ""
        self.mark3 = ""
        self.mark4 = ""
        self.mark5 = ""
        # self.lifestyle_level = False
        # self.absurd_level = False
        # self.relations_level = False
        # self.personal_level = False
        # self.adult_level = False

    def update_keyboard(self, row: int, index: int, old_keyboard: InlineKeyboardMarkup, game_obj):
        object_text = old_keyboard.values.get("inline_keyboard")[row][index]['text']
        print(old_keyboard.values.get("inline_keyboard"))
        if "+" in str(object_text):
            if row == 0:
                self.mark1 = ""
                game_obj.lifestyle_level = False
                print(f"index: {row}; mark: {self.mark1}; {game_obj.lifestyle_level}")
                # self.lifestyle_level = False
            elif row == 1:
                if index == 0:
                    self.mark2 = ""
                    game_obj.absurd_level = False
                    # self.absurd_level = False
                    print(f"index: {row}; mark: {self.mark2}; {game_obj.absurd_level}")
                elif index == 1:
                    self.mark3 = ""
                    game_obj.company_level = False
                    # self.relations_level = False
                    print(f"index: {row}; mark: {self.mark3}; {game_obj.company_level}")
            elif row == 2:
                if index == 0:
                    self.mark4 = ""
                    game_obj.company_level = False
                    # self.personal_level = False
                    print(f"index: {row}; mark: {self.mark4}; {game_obj.company_level}")
                elif index == 1:
                    self.mark5 = ""
                    game_obj.awkward_level = False
                    # self.adult_level = False
                    print(f"index: {row}; mark: {self.mark5}; {game_obj.awkward_level}")


        elif "+" not in str(object_text):
            if row == 0:
                self.mark1 = " +"
                game_obj.lifestyle_level = True
                print(f"index: {row}; mark: {self.mark1}; {game_obj.lifestyle_level}")
                # self.lifestyle_level = False
            elif row == 1:
                if index == 0:
                    self.mark2 = " +"
                    game_obj.absurd_level = True
                    # self.absurd_level = False
                    print(f"index: {row}; mark: {self.mark2}; {game_obj.absurd_level}")
                elif index == 1:
                    self.mark3 = " +"
                    game_obj.company_level = True
                    # self.relations_level = False
                    print(f"index: {row}; mark: {self.mark3}; {game_obj.company_level}")
            elif row == 2:
                if index == 0:
                    self.mark4 = " +"
                    game_obj.company_level = True
                    # self.personal_level = False
                    print(f"index: {row}; mark: {self.mark4}; {game_obj.company_level}")
                elif index == 1:
                    self.mark5 = " +"
                    game_obj.awkward_level = True
                    # self.adult_level = False
                    print(f"index: {row}; mark: {self.mark5}; {game_obj.awkward_level}")

        updated_keyboard = InlineKeyboardMarkup(row_width=2,
                                                       inline_keyboard=[
                                                           [
                                                               InlineKeyboardButton(f'{self.loc_file.keyboards["about life"]} {self.mark1}',
                                                                                    callback_data=self.cb_all_level.new(
                                                                                        action='lifestyle'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   f'{self.loc_file.keyboards["absurd"]} {self.mark2}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='absurd')),
                                                               InlineKeyboardButton(
                                                                   f'{self.loc_file.keyboards["company"]} {self.mark3}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='company'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   f'{self.loc_file.keyboards["relations"]} {self.mark4}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='relations')),
                                                               InlineKeyboardButton(
                                                                   f'{self.loc_file.keyboards["awkward"]} {self.mark5}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='awkward'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   text=f""">>> {self.loc_file.keyboards["choice is made"]} <<<""",
                                                                   callback_data=self.cb_all_level.new(action='ready')
                                                               )
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   text=f"""🔙 {self.loc_file.keyboards["menu"]} 🔙""",
                                                                   callback_data=self.cb_all_level.new(action='main menu')
                                                               )
                                                           ]
                                                       ]
                                                       )
        return updated_keyboard

    # def update_keyboard_mode(self, index: int, old_keyboard: InlineKeyboardMarkup):
    #     object_text = old_keyboard.values.get("inline_keyboard")[index][0]['text']
    #     if "+" in str(object_text):
    #         if index == 0:
    #             self.mode_mark1 = ''
    #             self.free_mode = False
    #         elif index == 1:
    #             self.mode_mark2 = ''
    #             self.step_mode = False
    #     elif "+" not in str(object_text):
    #         if index == 0:
    #             self.mode_mark1 = ' +'
    #             self.free_mode = True
    #         elif index == 1:
    #             self.mode_mark2 = ' +'
    #             self.step_mode = True
    #     updated_keyboard_mode = InlineKeyboardMarkup(row_width=2,
    #                                                  inline_keyboard=[
    #                                                      [
    #                                                          InlineKeyboardButton(f'{self.loc_file.keyboards["free mode"]} {self.mode_mark1}',
    #                                                                               callback_data=self.cb_mode.new(
    #                                                                                   action='free'
    #                                                                               )),
    #
    #                                                      ],
    #                                                      [
    #                                                          InlineKeyboardButton(f'{self.loc_file.keyboards["alternate mode"]} {self.mode_mark2}',
    #                                                                               callback_data=self.cb_mode.new(
    #                                                                                   action='step'
    #                                                                               ))
    #                                                      ]
    #                                                  ])
    #     return updated_keyboard_mode
class NieKeyboard:
    def __init__(self, loc_file: Texts):
        self.loc_file = loc_file
        self.cb_nie = CallbackData('name', 'action')
        self.keyboard_nie = InlineKeyboardMarkup(row_width=2,
                                                 inline_keyboard=[
                                                     [
                                                         InlineKeyboardButton(text=f"""❔ {self.loc_file.keyboards["truth"]}""",
                                                                              callback_data=self.cb_nie.new(
                                                                                  action='truth_nie')),
                                                         InlineKeyboardButton(text=f"""🤸 {self.loc_file.keyboards["dare"]}""",
                                                                              callback_data=self.cb_nie.new(
                                                                                  action='dare_nie'))
                                                     ],
                                                     [
                                                         InlineKeyboardButton(text=f"""💡 {self.loc_file.keyboards["never i ever"]}""",
                                                                              callback_data=self.cb_nie.new(
                                                                                  action='next_nie'))
                                                     ],
                                                     [
                                                         InlineKeyboardButton(text=f"""🔚 {self.loc_file.keyboards["end the game"]}""",
                                                                              callback_data=self.cb_nie.new(
                                                                                  action='end_nie'))
                                                     ]
                                                 ])
        self.cb_all_level = CallbackData('name', 'action')

        # self.mark1 = ""
        # self.mark2 = ""
        # self.mark3 = ""
        # self.mark4 = ""
        # self.mark5 = ""
        self.mark1, self.mark2, self.mark3, self.mark4, self.mark5 = "", "", "", "", ""
        # self.lifestyle_level = False
        # self.absurd_level = False
        # self.relations_level = False
        # self.personal_level = False
        # self.adult_level = False

        self.keyboard_level_all = InlineKeyboardMarkup(row_width=2,
                                                       inline_keyboard=[
                                                           [
                                                               InlineKeyboardButton(f'{self.loc_file.keyboards["about life"]} {self.mark1}',
                                                                                    callback_data=self.cb_all_level.new(
                                                                                        action='lifestyle'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   f'{self.loc_file.keyboards["absurd"]} {self.mark2}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='absurd')),
                                                               InlineKeyboardButton(
                                                                   f'{self.loc_file.keyboards["company"]} {self.mark3}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='company'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   f'{self.loc_file.keyboards["relations"]} {self.mark4}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='relations')),
                                                               InlineKeyboardButton(
                                                                   f'{self.loc_file.keyboards["awkward"]} {self.mark5}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='awkward'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   text=f""">>> {self.loc_file.keyboards["choice is made"]} <<<""",
                                                                   callback_data=self.cb_all_level.new(action='ready')
                                                               )
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   text=f"""🔙 {self.loc_file.keyboards["menu"]} 🔙""",
                                                                   callback_data=self.cb_all_level.new(action='main menu')
                                                               )
                                                           ]
                                                       ]
                                                       )
        self.cb_completed = CallbackData('name', 'action')
        self.keyboard_completed = InlineKeyboardMarkup(row_width=2,
                                                       inline_keyboard=[
                                                           [
                                                               InlineKeyboardButton(text=f"""✔️ {self.loc_file.keyboards["done"]}""",
                                                                                    callback_data=self.cb_completed.new(
                                                                                        action='completed'
                                                                                    )),

                                                           ],
                                                           [
                                                               InlineKeyboardButton(text=f"""❌ {self.loc_file.keyboards["not done"]}""",
                                                                                    callback_data=self.cb_completed.new(
                                                                                        action='failed'
                                                                                    ))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(text=f"""🔚 {self.loc_file.keyboards["end the game"]}""",
                                                                                    callback_data=self.cb_completed.new(
                                                                                        action='over'
                                                                                    ))
                                                           ]
                                                       ])
        self.cb_completed_f = CallbackData('name', 'action')

        self.keyboard_completed_f = InlineKeyboardMarkup(row_width=2,
                                                         inline_keyboard=[
                                                             [
                                                                 InlineKeyboardButton(text=f"""✔️ {self.loc_file.keyboards["done"]}""",
                                                                                      callback_data=self.cb_completed_f.new(
                                                                                          action='completed_f'
                                                                                      )),

                                                             ],
                                                             [
                                                                 InlineKeyboardButton(text=f"""❌ {self.loc_file.keyboards["not done"]}""",
                                                                                      callback_data=self.cb_completed_f.new(
                                                                                          action='failed_f'
                                                                                      ))
                                                             ]
                                                         ])

    def __str__(self):
        return f"""Nie Kb object. Sample: {self.loc_file.keyboards["dare"]}"""


    def reset(self):
        self.mark1 = ""
        self.mark2 = ""
        self.mark3 = ""
        self.mark4 = ""
        self.mark5 = ""
        # self.lifestyle_level = False
        # self.absurd_level = False
        # self.relations_level = False
        # self.personal_level = False
        # self.adult_level = False

    def update_keyboard(self, row: int, index: int, old_keyboard: InlineKeyboardMarkup, game_obj):
        object_text = old_keyboard.values.get("inline_keyboard")[row][index]['text']
        print(old_keyboard.values.get("inline_keyboard"))
        if "+" in str(object_text):
            if row == 0:
                self.mark1 = ""
                game_obj.lifestyle_level = False
                print(f"index: {row}; mark: {self.mark1}; {game_obj.lifestyle_level}")
                # self.lifestyle_level = False
            elif row == 1:
                if index == 0:
                    self.mark2 = ""
                    game_obj.absurd_level = False
                    # self.absurd_level = False
                    print(f"index: {row}; mark: {self.mark2}; {game_obj.absurd_level}")
                elif index == 1:
                    self.mark3 = ""
                    game_obj.company_level = False
                    # self.relations_level = False
                    print(f"index: {row}; mark: {self.mark3}; {game_obj.company_level}")
            elif row == 2:
                if index == 0:
                    self.mark4 = ""
                    game_obj.company_level = False
                    # self.personal_level = False
                    print(f"index: {row}; mark: {self.mark4}; {game_obj.company_level}")
                elif index == 1:
                    self.mark5 = ""
                    game_obj.awkward_level = False
                    # self.adult_level = False
                    print(f"index: {row}; mark: {self.mark5}; {game_obj.awkward_level}")


        elif "+" not in str(object_text):
            if row == 0:
                self.mark1 = " +"
                game_obj.lifestyle_level = True
                print(f"index: {row}; mark: {self.mark1}; {game_obj.lifestyle_level}")
                # self.lifestyle_level = False
            elif row == 1:
                if index == 0:
                    self.mark2 = " +"
                    game_obj.absurd_level = True
                    # self.absurd_level = False
                    print(f"index: {row}; mark: {self.mark2}; {game_obj.absurd_level}")
                elif index == 1:
                    self.mark3 = " +"
                    game_obj.company_level = True
                    # self.relations_level = False
                    print(f"index: {row}; mark: {self.mark3}; {game_obj.company_level}")
            elif row == 2:
                if index == 0:
                    self.mark4 = " +"
                    game_obj.company_level = True
                    # self.personal_level = False
                    print(f"index: {row}; mark: {self.mark4}; {game_obj.company_level}")
                elif index == 1:
                    self.mark5 = " +"
                    game_obj.awkward_level = True
                    # self.adult_level = False
                    print(f"index: {row}; mark: {self.mark5}; {game_obj.awkward_level}")

        updated_keyboard = InlineKeyboardMarkup(row_width=2,
                                                inline_keyboard=[
                                                    [
                                                        InlineKeyboardButton(
                                                            f'{self.loc_file.keyboards["about life"]} {self.mark1}',
                                                            callback_data=self.cb_all_level.new(
                                                                action='lifestyle'))
                                                    ],
                                                    [
                                                        InlineKeyboardButton(
                                                            f'{self.loc_file.keyboards["absurd"]} {self.mark2}',
                                                            callback_data=self.cb_all_level.new(
                                                                action='absurd')),
                                                        InlineKeyboardButton(
                                                            f'{self.loc_file.keyboards["company"]} {self.mark3}',
                                                            callback_data=self.cb_all_level.new(
                                                                action='company'))
                                                    ],
                                                    [
                                                        InlineKeyboardButton(
                                                            f'{self.loc_file.keyboards["relations"]} {self.mark4}',
                                                            callback_data=self.cb_all_level.new(
                                                                action='relations')),
                                                        InlineKeyboardButton(
                                                            f'{self.loc_file.keyboards["awkward"]} {self.mark5}',
                                                            callback_data=self.cb_all_level.new(
                                                                action='awkward'))
                                                    ],
                                                    [
                                                        InlineKeyboardButton(
                                                            text=f""">>> {self.loc_file.keyboards["choice is made"]} <<<""",
                                                            callback_data=self.cb_all_level.new(action='ready')
                                                        )
                                                    ],
                                                    [
                                                        InlineKeyboardButton(
                                                            text=f"""🔙 {self.loc_file.keyboards["menu"]} 🔙""",
                                                            callback_data=self.cb_all_level.new(action='main menu')
                                                        )
                                                    ]
                                                ]
                                                )
        return updated_keyboard

class ThreeOfFiveKeyboard:
    def __init__(self, loc_file: Texts):
        self.loc_file = loc_file
        # self.cb35 = CallbackData('name', 'action')
        # self.kb35 = InlineKeyboardMarkup(row_width=2,
        #                                  inline_keyboard=[
        #                                      [
        #                                          InlineKeyboardButton(self.loc_file.keyboards["chapter truth"],
        #                                                               callback_data=self.cb35.new(action="Truth"))
        #                                      ],
        #                                      [
        #                                          InlineKeyboardButton(self.loc_file.keyboards["chapter dare"],
        #                                                               callback_data=self.cb35.new(action="Dare"))
        #                                      ],
        #                                      [
        #                                          InlineKeyboardButton(self.loc_file.keyboards["chapter nie"],
        #                                                               callback_data=self.cb35.new(action="Never"))
        #                                      ],
        #                                      [
        #                                          InlineKeyboardButton(self.loc_file.keyboards["endgame new game"],
        #                                                               callback_data=self.cb35.new(action="End"))
        #                                      ]
        #                                  ])

        self.cb35b = CallbackData('name', 'action')
        self.kb35b = InlineKeyboardMarkup(row_width=2,
                                          inline_keyboard=[
                                              [
                                                  InlineKeyboardButton("⬅️",
                                                                       callback_data=self.cb35b.new(action="main menu")),

                                                  InlineKeyboardButton(text=f"""🤸 {self.loc_file.keyboards["begin"]}""",
                                                                       callback_data=self.cb35b.new(action="begin"))
                                              ]
                                          ])

        self.cb35n = CallbackData('name', 'action')
        self.kb35n = InlineKeyboardMarkup(row_width=2,
                                         inline_keyboard=[
                                             [
                                                 InlineKeyboardButton("⬅️",
                                                                      callback_data=self.cb35n.new(action="previous")),
                                                 InlineKeyboardButton("➡️",
                                                                          callback_data=self.cb35n.new(action="next"))
                                             ],
                                             [
                                                 InlineKeyboardButton(text=f"""🔚 {self.loc_file.keyboards["end the game"]}""",
                                                                      callback_data=self.cb35n.new(action="end"))
                                             ]
                                         ]

        )

    def __str__(self):
        return f"""35 Kb object. Sample: {self.loc_file.keyboards["dare"]}"""
class ThemesKeyboard:
    def __init__(self, loc_file: Texts):
        self.loc_file = loc_file

        self.cb_themes = CallbackData('name', 'action')
        self.kb_themes = InlineKeyboardMarkup(row_width=2,
                                              inline_keyboard=[
                                                  [
                                                      InlineKeyboardButton(self.loc_file.themes["school name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="school")),
                                                      InlineKeyboardButton(self.loc_file.themes["work name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="work")),

                                                  ],
                                                  [
                                                      InlineKeyboardButton(self.loc_file.themes["travel name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="travel")),

                                                      InlineKeyboardButton(self.loc_file.themes["worldview name"],
                                                                           callback_data=self.cb_themes.new(
                                                                                action="worldview"))
                                                  ],

                                                  [

                                                      InlineKeyboardButton(self.loc_file.themes["social media name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="social media")),
                                                      InlineKeyboardButton(self.loc_file.themes["art name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="art"))
                                                  ],
                                                  [
                                                      InlineKeyboardButton(self.loc_file.themes["relations name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="relations")),
                                                      InlineKeyboardButton(self.loc_file.themes["memes name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="memes"))
                                                  ],
                                                  [
                                                      InlineKeyboardButton(self.loc_file.themes["religion name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="religion")),
                                                      InlineKeyboardButton(self.loc_file.themes["memories name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="memories"))
                                                  ],
                                                  [
                                                      InlineKeyboardButton(self.loc_file.themes["if name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="if")),
                                                      InlineKeyboardButton(self.loc_file.themes["videogames name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="videogames"))
                                                  ],
                                                  [
                                                      InlineKeyboardButton(self.loc_file.themes["education name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="education")),
                                                      InlineKeyboardButton(self.loc_file.themes["fashion name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="fashion")),
                                                  ],
                                                  [
                                                      InlineKeyboardButton(self.loc_file.themes["hard choice name"],
                                                                           callback_data=self.cb_themes.new(
                                                                               action="hard choice"))
                                                  ],
                                                  [
                                                      InlineKeyboardButton(text=f"""🔙 {self.loc_file.keyboards["menu"]} 🔙""",
                                                                           callback_data=self.cb_themes.new(
                                                                               action="main menu"))
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
                                                           InlineKeyboardButton(text=f"""🔚 {self.loc_file.keyboards["end the game"]}""",
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
                                                              InlineKeyboardButton("⬅️",
                                                                                   callback_data=self.cb_themes_confirm.new(
                                                                                       action='menu'
                                                                                   )),
                                                              InlineKeyboardButton(text=f"""🤸 {self.loc_file.keyboards["begin"]}""",
                                                                                   callback_data=self.cb_themes_confirm.new(
                                                                                       action='begin'
                                                                                   ))

                                                          ]
                                                      ]
                                                      )

    def __str__(self):
        return f"""Themes Kb object. Sample: {self.loc_file.keyboards["dare"]}"""

# class OtherKBs:
#     def __init__(self, loc_file: Texts):
#         self.loc_file = loc_file
#
#         self.main_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#
#     def set_up_main_menu_kb(self):
#


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