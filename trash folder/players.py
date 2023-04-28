class Players:
    def __init__(self):
        self.players_list = []

        self.current_player_number = 0
        self.score = {}
        self.result = []

        self.truth_max = 0
        self.truth_min = 100
        self.dare_max = 0
        self.dare_min = 100

        self.truth_winner = ""
        self.truth_antiwinner = ""
        self.dare_winner = ""
        self.dare_antiwinner = ""

        self.players_number = 0

        self.truth_circle = True

    def list_of_players_names(self, data: str):
        """
        The function returns a list of names from a raw string where names are separated with commas.

        :param data: str.
        :return: names_list.
        """
        raw_names_list = data.split(sep=",")
        names_list = []
        for raw_name in raw_names_list:
            name = (raw_name.replace(" ", ""))
            if name.islower():
                name.capitalize()
            else:
                pass
            names_list.append(name)
        return names_list

    def add_player(self, players: list):
        """
        The function adds players' names to the list variable 'self.players_list'.
        """
        for player in players:
            self.players_list.append(player)
            self.score[player] = {'t+': 0,
                                  't-': 0,
                                  'd+': 0,
                                  'd-': 0,
                                  'p': 0}

    def players_number(self, players_list: list):
        """
        The function updates variable 'self.players_number' with an int that is equal to
        number of players in the players list.
        """
        self.players_number = len(players_list)

    def next_player_number(self):
        """
        The function updates the variable 'self.current_player_number' increasing it by 1.
        """
        self.current_player_number += 1
        if self.current_player_number == len(self.players_list):
            self.current_player_number = 0

    def circle_changer(self):
        if self.current_player_number == 0:
            if self.truth_circle == True:
                self.truth_circle = False
            elif self.truth_circle == False:
                self.truth_circle = True

    def fail_check(self, name):
        object_ = self.score[name]['p']
        if 0 <= object_ < 5:
            pass
        elif object_ % 5 == 0:
            return True
        else:
            return False

    def print_statistics(self):
        """
        The function returns 4 variables with statistics of the current game.

        :return: self.truth_winner, self.truth_antiwinner, self.dare_winner, self.dare_antiwinner
        """

        def get_percents_truth(truth_yes: int, truth_no: int):
            truth_yes_part_ = truth_yes / (float(truth_yes + truth_no) / 100)
            truth_no_part_ = truth_no / (float(truth_yes + truth_no) / 100)
            return truth_yes_part_, truth_no_part_

        def get_percents_dare(dare_yes: int, dare_no: int):
            dare_yes_part_ = dare_yes / (float(dare_yes + dare_no) / 100)
            dare_no_part_ = dare_no / (float(dare_yes + dare_no) / 100)
            return dare_yes_part_, dare_no_part_

        for player in self.score:
            typ, tnp = get_percents_truth(player["t+"], player["t-"])
            dyp, dnp = get_percents_dare(player["d+"], player["d-"])
            self.result.append([player, [typ, tnp], [dyp, dnp]])

        for index in range(0, len(self.result)):
            if self.result[index][1][0] > self.truth_max:
                self.truth_winner = self.result[index][0]
                self.truth_max = self.result[index][1][0]
            else:
                pass
            if self.result[index][1][1] < self.truth_min:
                self.truth_antiwinner = self.result[index][1][0]
                self.truth_min = self.result[index][1][0]
            else:
                pass
            if self.result[index][2][0] > self.dare_max:
                self.dare_winner = self.result[index][0]
                self.dare_max = self.result[index][1][0]
            else:
                pass
            if self.result[index][2][1] < self.dare_min:
                self.dare_antiwinner = self.result[index][1][0]
                self.dare_min = self.result[index][1][0]
            else:
                pass

        return self.truth_winner, self.truth_antiwinner, self.dare_winner, self.dare_antiwinner