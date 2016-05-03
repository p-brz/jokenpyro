from model import *

import Pyro4

class UnfairPlayException(Exception):
    pass

class Player(object):
    winnerName = {
        1: "você",
        2 : "mim"
    }
    winmessages = {
        -2 : "Ihh... essa foi moleza",
        -1 : "Lamento, mas não foi dessa vez.",
        1 : "Parabéns, você venceu o jogo. \n... mas talvez não tenha tanta sorte na próxima.",
        2 : "Ok, eu admito. Você é bom.",
    }

    match_results = ['Empate!', 'Você ganhou. Dessa vez...', 'Eu venci! Muahaha!']

    def __init__(self):
        self.jokenpo = Pyro4.Proxy("PYRONAME:example.JokenpoServer")
        self.sessid = None
        self.countRound = 0

    def play(self):
        self.countRound = 0
        self.sessid = self.jokenpo.start()

        try:
            self.game_loop()
        except KeyboardInterrupt:
            print()
            print("Fuja enquanto pode!")
        except UnfairPlayException:
            print()
            print("Assim não dá! Você não sabe brincar!")

    def game_loop(self):
        while True:
            self.do_match()

            if self.game_state.has_winner():
                self.print_winner()
                return


    def do_match(self):
        self.countRound += 1
        print("=========================== Round %d ==========================="
                % self.countRound)
        print()

        playerChoice = self.receive_player_choice()

        result = self.jokenpo.play(self.sessid, playerChoice)
        self.game_state = result.state

        self.print_match_result(result)

    def receive_player_choice(self):
        playerChoice = None

        for i in range(4):
            options = ['Pedra', 'Papel', 'Tesoura']

            playerChoice = input("Você escolhe: 1 - Pedra, 2 - Papel ou 3 - Tesoura?\n").strip()

            try:
                if int(playerChoice) in (1, 2, 3):
                    playerChoice = options[int(playerChoice) - 1]
            except ValueError:
                pass


            if playerChoice not in options:
                print("Ei! Assim não vale! Escolha direito!")
                print()
            else:
                return playerChoice


        raise UnfairPlayException()

    def print_match_result(self, result):
        print("Jo.. ken.. pô!")
        print()
        print(result.player_choice(), " vs ", result.server_choice())

        print(self.match_results[result.winner])
        print()

    def print_winner(self):
        winner = self.game_state.get_winner()
        other = 1
        if winner == 1:
            other = 2

        winnerPts = self.game_state.pts[winner]
        looserPts = self.game_state.pts[other]

        # print("winner: ", winner, " looser: ", other, " pts: ", game_state.pts)

        print()
        print(winnerPts, " a ", looserPts, " para ", self.winnerName[winner], ".")

        diff = self.game_state.player_pts() - self.game_state.server_pts()
        print(self.winmessages[diff])

def main():
    Pyro4.config.SERIALIZER = 'pickle'
    
    player = Player()
    player.play()

if __name__ == '__main__':
    main()
