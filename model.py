
class PlayerState(object):
    def __init__(self):
        self.matches = 0
        self.pts = {
            1 : 0,
            2 : 0
        }

    def player_pts(self):
        return self.pts[1]
    def server_pts(self):
        return self.pts[2]

    def addResult(self, winnerIdx):
        if winnerIdx != 0:
            self.pts[winnerIdx] += 1

    def has_winner(self):
        return self.get_winner() is not None

    def get_winner(self):
        for player, pts in self.pts.items():
            if pts >= 2:
                return player

        return None

class MatchResult(object):
    def __init__(self, winner, state, choices):
        self.winner = winner
        self.state = state
        self.choices = choices

    def is_draw(self):
        return self.winner == 0

    def is_winner(self, playerNum):
        return self.winner == playerNum

    def player_choice(self):
        return self.choices.get(1, None)

    def server_choice(self):
        return self.choices.get(2, None)
