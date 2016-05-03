import random

class JokenpoManager(object):
    PEDRA = 'Pedra'
    PAPEL = 'Papel'
    TESOURA = 'Tesoura'

    choices = [PEDRA, PAPEL, TESOURA]

    wins = {
        PEDRA   : TESOURA,
        PAPEL   : PEDRA,
        TESOURA : PAPEL
    }

    def choiceJokenpo(self):
        return random.choice(self.choices)

    def compare(self, firstChoice, secondChoice):
        if self.wins.get(firstChoice) == secondChoice:
            #first wins
            return 1
        elif self.wins.get(secondChoice) == firstChoice:
            #second wins
            return 2
        else:
            #empate
            return 0
