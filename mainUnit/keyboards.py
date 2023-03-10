from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class Keyboards:

    def __init__(self):
        self.cb_nie = CallbackData('name', 'action')
        self.keyboard_nie = InlineKeyboardMarkup(row_width=2,
                                                 inline_keyboard=[
                                                     [
                                                         InlineKeyboardButton('Правда',
                                                                              callback_data=self.cb_nie.new(
                                                                                  action='truth_nie')),
                                                         InlineKeyboardButton('Действие',
                                                                              callback_data=self.cb_nie.new(
                                                                                  action='dare_nie'))
                                                     ],
                                                     [
                                                         InlineKeyboardButton('Я никогда не ...',
                                                                              callback_data=self.cb_nie.new(
                                                                                  action='next_nie'))
                                                     ],
                                                     [
                                                         InlineKeyboardButton('Завершить',
                                                                              callback_data=self.cb_nie.new(
                                                                                  action='end_nie'))
                                                     ]
                                                 ])

        self.cb_td = CallbackData('name', 'action')
        self.keyboard_td = InlineKeyboardMarkup(row_width=2,
                                                inline_keyboard=[
                                                    [
                                                        InlineKeyboardButton('Правда',
                                                                             callback_data=self.cb_td.new(
                                                                                 action='truth')),
                                                        InlineKeyboardButton('Действие',
                                                                             callback_data=self.cb_td.new(
                                                                                 action='dare'))
                                                    ],
                                                    [
                                                        InlineKeyboardButton('Завершить',
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
                                                               InlineKeyboardButton(f'О жизни {self.mark1}',
                                                                                    callback_data=self.cb_all_level.new(
                                                                                        action='lifestyle'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   f'Абсурд {self.mark2}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='absurd'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   f'Компания {self.mark3}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='relations'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   f'Узнать получше {self.mark4}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='personal'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   f'451℉ {self.mark5}',
                                                                   callback_data=self.cb_all_level.new(
                                                                       action='adult'))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(
                                                                   'В ы б о р   с д е л а н',
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
                                                             InlineKeyboardButton('Да, всё верно.',
                                                                                  callback_data=self.cb_players.new(
                                                                                      action='yes')),
                                                             InlineKeyboardButton('Нет, хочу исправить.',
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
                                                          InlineKeyboardButton('Свободный',
                                                                               callback_data=self.cb_mode.new(
                                                                                   action='free'
                                                                               )),

                                                      ],
                                                      [
                                                          InlineKeyboardButton('Поочередный',
                                                                               callback_data=self.cb_mode.new(
                                                                                   action='step'
                                                                               ))
                                                      ]
                                                  ])

        self.cb_completed = CallbackData('name', 'action')
        self.keyboard_completed = InlineKeyboardMarkup(row_width=2,
                                                       inline_keyboard=[
                                                           [
                                                               InlineKeyboardButton('Выполнено',
                                                                                    callback_data=self.cb_completed.new(
                                                                                        action='completed'
                                                                                    )),

                                                           ],
                                                           [
                                                               InlineKeyboardButton('Не выполнено',
                                                                                    callback_data=self.cb_completed.new(
                                                                                        action='failed'
                                                                                    ))
                                                           ],
                                                           [
                                                               InlineKeyboardButton(' О к о н ч и т ь  и г р у',
                                                                                    callback_data=self.cb_completed.new(
                                                                                        action='over'
                                                                                    ))
                                                           ]
                                                       ])

        self.cb_completed_f = CallbackData('name', 'action')

        self.keyboard_completed_f = InlineKeyboardMarkup(row_width=2,
                                                         inline_keyboard=[
                                                             [
                                                                 InlineKeyboardButton('Выполнено',
                                                                                      callback_data=self.cb_completed.new(
                                                                                          action='completed_f'
                                                                                      )),

                                                             ],
                                                             [
                                                                 InlineKeyboardButton('Не выполнено',
                                                                                      callback_data=self.cb_completed.new(
                                                                                          action='failed_f'
                                                                                      ))
                                                             ]
                                                         ])

        self.cb35 = CallbackData('name', 'action')
        self.kb35 = InlineKeyboardMarkup(row_width=2,
                                         inline_keyboard=[
                                             [
                                                 InlineKeyboardButton(f'Раздел "Правда"', callback_data=self.cb35.new(action="Truth"))
                                             ],
                                             [
                                                 InlineKeyboardButton(f'Раздел "Действие"',
                                                                      callback_data=self.cb35.new(action="Dare"))
                                             ],
                                             [
                                                 InlineKeyboardButton(f'Раздел "Я никогда не..."',
                                                                      callback_data=self.cb35.new(action="Never"))
                                             ],
                                             [
                                                 InlineKeyboardButton(f'Закончить/Новая игра',
                                                                      callback_data=self.cb35.new(action="End"))
                                             ]
                                         ])

        self.cb35b = CallbackData('name', 'action')
        self.kb35b = InlineKeyboardMarkup(row_width=2,
                                         inline_keyboard=[
                                             [
                                                 InlineKeyboardButton('Начать',
                                                                      callback_data=self.cb35.new(action="Begin"))
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
                                                        InlineKeyboardButton(f'О жизни {self.mark1}',
                                                                             callback_data=self.cb_all_level.new(
                                                                                 action='lifestyle'))
                                                    ],
                                                    [
                                                        InlineKeyboardButton(
                                                            f'Абсурдные {self.mark2}',
                                                            callback_data=self.cb_all_level.new(
                                                                action='absurd'))
                                                    ],
                                                    [
                                                        InlineKeyboardButton(
                                                            f'Для компании {self.mark3}',
                                                            callback_data=self.cb_all_level.new(
                                                                action='relations'))
                                                    ],
                                                    [
                                                        InlineKeyboardButton(
                                                            f'Отношения {self.mark4}',
                                                            callback_data=self.cb_all_level.new(
                                                                action='personal'))
                                                    ],
                                                    [
                                                        InlineKeyboardButton(
                                                            f'Неловкие {self.mark5}',
                                                            callback_data=self.cb_all_level.new(
                                                                action='adult'))
                                                    ],
                                                    [
                                                        InlineKeyboardButton(
                                                            'В ы б о р   с д е л а н',
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
                                                             InlineKeyboardButton(f'Свободный {self.mode_mark1}',
                                                                                  callback_data=self.cb_mode.new(
                                                                                      action='free'
                                                                                  )),

                                                         ],
                                                         [
                                                             InlineKeyboardButton(f'Поочередный {self.mode_mark2}',
                                                                                  callback_data=self.cb_mode.new(
                                                                                      action='step'
                                                                                  ))
                                                         ]
                                                     ])
        return updated_keyboard_mode




